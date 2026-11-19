"""Structural validation only; no mathematical classifications are inferred."""
import json,csv,re
from pathlib import Path
S=Path(__file__).resolve().parents[1];ROOT=S.parents[2]
sets={n:json.loads((S/(n+'.json')).read_text()) for n in ('items','claims','problems')}
errors=[];warnings=[]
ids={k:{x['id'] for x in v} for k,v in sets.items()}
for k,v in sets.items():
 if len(ids[k])!=len(v):errors.append('duplicate IDs in '+k)
entries=list(csv.DictReader((S/'entries.tsv').open(),delimiter='\t'))
expected={f'MPL_36_002-052#{i}' for i in range(1,94)}
if {r['entry_id'] for r in entries}!=expected or len(entries)!=93:errors.append('entry coverage mismatch')
for e in entries:
 if e['item_id'] not in ids['items']:errors.append('dangling entry '+str(e))
 if e['verdict'] not in {'kept','merged','corrected','withdrawn','rests on a misreading'}:errors.append('invalid verdict')
refs=set(re.findall(r'^@\w+\{([^,]+),',(S/'references.bib').read_text(),re.M))
for kind in ('claims','problems'):
 for x in sets[kind]:
  for r in x['refs']:
   if r not in refs:errors.append(x['id']+' dangling ref '+r)
  for it in x.get('items',[]):
   if it not in ids['items']:errors.append(x['id']+' dangling item '+it)
search=list(csv.DictReader((S/'search_log.tsv').open(),delimiter='\t'));sids={r['search_id'] for r in search}
for c in sets['claims']:
 if not c['search_ids']:errors.append(c['id']+' no search mapping')
 for k in c['search_ids']:
  if k not in sids:errors.append(c['id']+' unknown search '+k)
 if c['status_on_pages'] not in {'proved there','proof sketched','stated without proof','corrected by himself later','false as stated','open on the pages'}:errors.append('bad status '+c['id'])
 if c['class'] not in 'ABCDEF':errors.append('bad class '+c['id'])
events=list(csv.DictReader((S/'check_events.tsv').open(),delimiter='\t'))
etypes={'targeted proof check','independent re-proof','computation or formal certificate','used and rechecked in this run','carried as background without fault found',"refuted, with the refined statement's id"}
for e in events:
 if e['statement_id'] not in ids['claims']|ids['items']|refs:errors.append('dangling event '+e['statement_id'])
 if e['type'] not in etypes:errors.append('bad event type '+e['type'])
if not ids['claims']|ids['items']|refs <= {e['statement_id'] for e in events}:errors.append('event coverage mismatch')
cache={}
def smap(fn):
 if fn not in cache:
  lines=(ROOT/'sources/texts'/fn).read_text().splitlines();m={};scan=None
  for i,l in enumerate(lines,1):
   p=re.search(r'\\scanpage\{(\d+)\}',l)
   if p:scan=int(p[1])
   m[i]=scan
  cache[fn]=(lines,m)
 return cache[fn]
for x in sets['items']:
 for loc in x['lines']:
  lines,m=smap(loc['file']);a,b=loc['start'],loc['end']
  if not 1<=a<=b<=len(lines):errors.append(x['id']+' invalid locus '+str(loc));continue
  scans={m[i] for i in range(a,b+1)}
  if loc['scan'] not in scans:errors.append(x['id']+' scan absent '+str(loc)+' actual='+str(scans))
  elif scans!={loc['scan']}:warnings.append(x['id']+' range crosses scan '+str(loc)+' actual='+str(scans))
readings=list(csv.DictReader((S/'readings.tsv').open(),delimiter='\t'))
for r in readings:
 fn='codex/A36-01_transcription.tex' if 10<=int(r['scan'])<=18 else 'codex/A36-02_transcription.tex' if 19<=int(r['scan'])<=27 else 'pro/MPL_36_002-052_transcription.tex'
 lines,m=smap(fn);line=int(r['line'])
 if line not in m:errors.append('reading invalid line '+str(r))
 elif m[line]!=int(r['scan']):warnings.append('reading scan mismatch '+str(r)+' actual='+str(m[line]))
for fn in ['review.md','directions.md','links.tsv','reading_log.tsv','research_evidence.md','cross_package_audit.md','cross_package_merge_map.tsv','progress.log']:
 if not (S/fn).stat().st_size:errors.append('empty '+fn)
result={'items':len(sets['items']),'entries':len(entries),'claims':len(sets['claims']),'problems':len(sets['problems']),'readings':len(readings),'references':len(refs),'search_groups':len(search),'check_events':len(events),'errors':errors,'warnings':warnings}
(S/'outputs/validation.json').write_text(json.dumps(result,ensure_ascii=False,indent=2)+'\n')
print(json.dumps(result,ensure_ascii=False,indent=2))
