#!/usr/bin/env python3
"""Combine checked bibliography witnesses using an explicitly approved alias map."""
import json,re,csv,collections
from pathlib import Path
B=Path(__file__).resolve().parents[1]
SCOPES=['root','cote11a','cote11b','cote12c']
M=json.loads((B/'reference_aliases.json').read_text()) if (B/'reference_aliases.json').exists() else {}
if 'aliases' in M:M=M['aliases']
def canon(k):
 seen=set()
 while k in M:
  if k in seen:raise ValueError('reference alias cycle')
  seen.add(k);k=M[k]
 return k
def parsebib(text):
 records=[];pos=0
 while True:
  m=re.search(r'@(\w+)\s*\{\s*([^,]+),',text[pos:])
  if not m:break
  start=pos+m.start();i=pos+m.end();kind=m.group(1);key=m.group(2).strip();fields={}
  while True:
   while i<len(text) and (text[i].isspace() or text[i]==','):i+=1
   if i>=len(text):raise ValueError('unclosed '+key)
   if text[i]=='}':i+=1;break
   fm=re.match(r'([A-Za-z_][\w-]*)\s*=\s*',text[i:])
   if not fm:raise ValueError('field at '+text[i:i+100])
   field=fm.group(1);i+=fm.end()
   if text[i]=='{':
    i+=1;vstart=i;depth=1
    while depth:
     if i>=len(text):raise ValueError('unclosed field '+key+field)
     if text[i]=='\\':i+=2;continue
     if text[i]=='{':depth+=1
     elif text[i]=='}':depth-=1
     i+=1
    val=text[vstart:i-1]
   elif text[i]=='"':
    i+=1;vstart=i
    while text[i]!='"':i+=2 if text[i]=='\\' else 1
    val=text[vstart:i];i+=1
   else:
    vstart=i
    while i<len(text) and text[i] not in ',}':i+=1
    val=text[vstart:i].strip()
   fields[field]=val
  records.append({'key':key,'entry_type':kind,**fields});pos=i
 return records
records=[]
for sc in SCOPES:
 for x in parsebib((B/'work'/sc/'references.bib').read_text()):
  x.setdefault('year','n.d.')
  if x['key']=='Delzant1962':
   x['note']='unverified'
   x['url']=''
   x['annote']='External-link status is unverified under the requested rule. The full supplied primary offprint transcription was read; exact extent is retained below. A later opened Numdam bibliography corroborates the citation but its DOI is not Delzant’s. See work/cote11a/delzant_external_reference_audit.md.'
  x['scope']=sc;records.append(x)
groups=collections.defaultdict(list)
for r in records:groups[canon(r['key'])].append(r)
out=[];bib=[]
for key,rs in sorted(groups.items()):
 preferred=[r for r in rs if r['key']==key]
 if not preferred:raise ValueError('No canonical record '+key)
 chosen=preferred[0].copy()
 if chosen.get('note')!='verified' and any(r.get('note')=='verified' for r in rs):
  # A verified note belongs to its actually opened URL, not to an unopened original.
  chosen=next(r for r in rs if r.get('note')=='verified').copy()
 chosen['key']=key
 chosen['source_witnesses']=rs
 chosen['aliases']=sorted({r['key'] for r in rs if r['key']!=key})
 out.append(chosen)
 fields={k:v for k,v in chosen.items() if k not in ['key','entry_type','scope','source_witnesses','aliases']}
 for k in ['author','title','year','url','note']:
  if k not in fields:raise ValueError((key,'missing',k))
 if fields['note'] not in ['verified','unverified']:raise ValueError((key,fields['note']))
 fields['urldate']='2026-11-19'
 extra='Consolidated witness details and version-specific locators are in SA05_reference_ledger.json.'
 if chosen['aliases']:extra+=' Citation aliases: '+', '.join(chosen['aliases'])+'.'
 fields['annote']=(fields.get('annote','')+' '+extra).strip()
 bib.append('@'+chosen['entry_type']+'{'+key+',\n'+',\n'.join('  '+k+' = {'+str(v)+'}' for k,v in fields.items())+'\n}')
(B/'SA05_references.bib').write_text('\n\n'.join(bib)+'\n')
out_index={r['key']:r for r in out}
supplement=B/'work/cote11b/refinement_reference_checks.tsv'
if supplement.exists():
 for row in csv.DictReader(supplement.open(),delimiter='\t'):
  out_index[canon(row['reference_key'])].setdefault('additional_opened_checks',[]).append(row)
(B/'SA05_reference_ledger.json').write_text(json.dumps(out,ensure_ascii=False,indent=2)+'\n')
with (B/'SA05_reference_ledger.tsv').open('w',newline='') as f:
 w=csv.DictWriter(f,fieldnames=['key','title','year','url','note','aliases','witness_count','checked_scopes'],delimiter='\t');w.writeheader()
 for r in out:
  w.writerow({**{k:r[k] for k in ['key','title','year','url','note']},'aliases':';'.join(r['aliases']),
   'witness_count':len(r['source_witnesses']),'checked_scopes':' | '.join(x['scope']+': '+x.get('annote',x.get('checked_extent','')) for x in r['source_witnesses'])})
summary={'input_records':len(records),'canonical_records':len(out),'verified':sum(r['note']=='verified' for r in out),'unverified':sum(r['note']=='unverified' for r in out)}
(B/'programs/outputs/consolidate_references.json').write_text(json.dumps(summary,indent=2)+'\n');print(json.dumps(summary))
