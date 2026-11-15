"""Incremental image-collation ledger owned by the 134-7/8 reviewer.
The same owner also reviews the allocated first60 pages of cote134-6.
Run from the parent of PS_READERS_WORK; all stored paths are ZIP-relative.
A review JSON must be supplied only after both scan halves were opened.
"""
import csv,json,re,sys
from pathlib import Path
ROOT=Path(__file__).resolve().parents[2]
INP=ROOT/'inputs'/'text'; OUT=ROOT/'PS_READERS_WORK'
FIELDS=['key','cote','site','line','transcription_reading','image_reading','arxiv_reading','decision','reason','source_id']
PAGEFIELDS=['key','both_halves_viewed','status','issues_remaining','notes']
DIFF=list(csv.DictReader((INP/'records/PS_ARXIV_DIFF.tsv').open(),delimiter='\t'))
NOTES={r['key']:r for r in csv.DictReader((INP/'transcription/ps_NOTES.tsv').open(),delimiter='\t')}
SKIP={'normalization','silent correction','handwritten note merged (unmarked in arXiv)'}

def read(key):return (INP/'transcription/ps_pages'/f'{key}.tex').read_text()
def macros(text,name):
 result=[]
 for m in re.finditer(r'\\'+name+r'\s*\{',text):
  i=m.end();begin=i;depth=1
  while i<len(text) and depth:
   if text[i]=='\\':
    i+=2;continue
   if text[i]=='{':depth+=1
   if text[i]=='}':depth-=1
   i+=1
  result.append((m.start(),text[begin:i-1],text[m.start():i]))
 return result

def packet(keys):
 for key in keys:
  text=read(key)
  print('\n==========',key,'==========\n')
  for i,line in enumerate(text.splitlines(),1):print(f'{i:3}: {line}')
  print('NOTES:',NOTES[key]['notes'])
  for i,r in enumerate(DIFF,1):
   if r['page_key']==key and r['kind'] not in SKIP:
    print(f'DIFF:{i} [{r["kind"]}] SCAN_DRAFT={r["page_reading"]!r} ARXIV={r["arxiv_text"]!r} LOC={r["note"]}')
  for name in ['unsure','illegible']:
   print(name.upper(),[(i, x[1],text.count('\n',0,x[0])+1) for i,x in enumerate(macros(text,name),1)])

def append_tsv(path,fields,rows,key):
 existing=list(csv.DictReader(path.open(),delimiter='\t')) if path.exists() else []
 existing=[r for r in existing if r.get('key')!=key]
 with path.open('w') as f:
  w=csv.DictWriter(f,fieldnames=fields,delimiter='\t');w.writeheader();w.writerows(existing+rows)

def commit(data):
 key=data['key'];assert key.startswith(('ps_134-6_','ps_134-7_','ps_134-8_'))
 assert data['both_halves_viewed'] is True
 text=read(key);new=text;parts=key.split('_');cote=parts[1];site=int(parts[2]);rows=[]
 def add(line,old,seen,arxiv,decision,reason,sid):
  rows.append(dict(zip(FIELDS,[key,cote,site,line,old,seen,arxiv,decision,reason,sid])))
 for n,e in enumerate(data.get('edits',[]),1):
  old=e['old'];replacement=e['new'];count=new.count(old)
  assert count==e.get('count',1),(key,old,count)
  line=text.count('\n',0,text.index(old))+1 if old in text else ''
  new=new.replace(old,replacement,e.get('count',1))
  add(line,old,replacement,e.get('arxiv',''),'our transcription corrected',e['reason'],e.get('source_id',f'EDIT:{key}:{n}'))
 for obs in data.get('observations',[]):
  add(obs.get('line',''),obs.get('before',''),obs.get('reading',''),obs.get('arxiv',''),obs['decision'],obs['reason'],obs['source_id'])
 for i,r in enumerate(DIFF,1):
  if r['page_key']!=key or r['kind'] in SKIP:continue
  entry=data['diff'][str(i)]
  if isinstance(entry,str):entry={'reason':entry}
  old=r['page_reading'];line=text.count('\n',0,text.index(old))+1 if old and old in text else ''
  add(line,old,entry.get('reading',old),r['arxiv_text'],entry.get('decision','the typescript reads as our transcription'),entry['reason'],f'DIFF:{i}')
 for name in ['unsure','illegible']:
  for i,(pos,inside,whole) in enumerate(macros(text,name),1):
   obs=data.get(name,{}).get(str(i),data.get(name+'_default'))
   assert obs,(key,name,i)
   if isinstance(obs,str):obs={'reason':obs}
   decision='doubt retained' if whole in new else 'our transcription corrected'
   add(text.count('\n',0,pos)+1,whole,obs.get('reading',whole),'',obs.get('decision',decision),obs['reason'],f'{name.upper()}:{key}:{i}')
 ns=[x.strip() for x in NOTES[key]['notes'].split(' | ') if not x.startswith('LONG-HANDWRITING:')]
 for i,note in enumerate(ns,1):
  reason=data.get('notes',{}).get(str(i),data.get('notes_default'))
  assert reason,(key,'note',i)
  add('',note,'See review observation','','note checked',reason,f'NOTE:{key}:{i}')
 # Replace the superseded draft-status phrase only after actual two-half review.
 old_status='not yet checked by eye.'
 new_status='reviewed against both supplied scan halves; see CHECK_DECISIONS.tsv.'
 assert new.count(old_status)==1,(key,'review header')
 new=new.replace(old_status,new_status)
 new += '\n% Visual collation: both supplied image halves inspected; see CHECK_DECISIONS_134_7_8.tsv.\n'
 add(3, old_status, new_status+' [collation-status comment appended]', '', 'metadata updated', 'The superseded draft header is updated after both scan halves were inspected; nonprinting provenance only.',f'META:{key}')
 (OUT/'checked_pages'/f'{key}.tex').write_text(new)
 append_tsv(OUT/'records/CHECK_DECISIONS_134_7_8.tsv',FIELDS,rows,key)
 issues=len(macros(new,'unsure'))+len(macros(new,'illegible'))+data.get('masked_regions',0)
 pr=dict(zip(PAGEFIELDS,[key,'yes',data.get('status','visually checked; unresolved marks retained' if issues else 'visually checked'),issues,data['summary']]))
 append_tsv(OUT/'records/PAGE_REVIEW_134_7_8.tsv',PAGEFIELDS,[pr],key)
 (OUT/'review_notes'/f'{key}.json').write_text(json.dumps(data,ensure_ascii=False,indent=2)+'\n')
 print(key, 'committed',len(rows),'decisions;',issues,'remaining marks')


def annotate_hand_tokens(data,tokens,diagram_arrows=False):
 """Apply only an explicit, image-grounded list of handwritten token forms."""
 text=read(data['key'])
 for e in data.get('edits',[]):text=text.replace(e['old'],e['new'],e.get('count',1))
 protected=[]
 for name in ['hand','inserted','margin']:
  protected.extend((p,p+len(whole)) for p,inside,whole in macros(text,name))
 # The replacement argument of an over macro is already handwritten.
 for p,inside,whole in macros(text,'over'):
  i=p+len(whole)
  while i<len(text) and text[i].isspace():i+=1
  if i<len(text) and text[i]=='{':
   start=i;depth=1;i+=1
   while i<len(text) and depth:
    if text[i]=='\\':i+=2;continue
    if text[i]=='{':depth+=1
    if text[i]=='}':depth-=1
    i+=1
   protected.append((start,i))
 spans=[]
 for token in tokens:
  for m in re.finditer(re.escape(token)+r'(?![A-Za-z])',text):
   if not any(a<=m.start()<b for a,b in protected):spans.append((m.start(),m.end(),'\\hand{'+token+'}'))
 changed=text
 for a,b,v in sorted(spans,reverse=True):changed=changed[:a]+v+changed[b:]
 if diagram_arrows:changed=changed.replace('\\arrow[','\\arrow[color=blue,')
 oldlines=text.splitlines();newlines=changed.splitlines();assert len(oldlines)==len(newlines)
 for old,new in zip(oldlines,newlines):
  if old!=new:data.setdefault('edits',[]).append({'old':old,'new':new,'reason':'The indicated symbols/arrows are visibly hand-filled on the inspected scan; mark the handwritten layer without changing glyphs or directions. Diagram arrow color records handwriting while typed nodes stay plain.'})
 return data

if __name__=='__main__':
 if sys.argv[1]=='packet':packet(sys.argv[2:])
 elif sys.argv[1]=='commit':
  d=json.load(sys.stdin)
  for x in d if isinstance(d,list) else [d]:commit(x)
