#!/usr/bin/env python3
"""Merge identical bibliography keys without inventing metadata or verification."""
from pathlib import Path
import re,json,collections
W=Path(__file__).resolve().parents[1]
def balanced(t,start):
 assert t[start]=='{';depth=0
 for i in range(start,len(t)):
  if i and t[i-1]=='\\':continue
  if t[i]=='{':depth+=1
  elif t[i]=='}':
   depth-=1
   if not depth:return t[start+1:i],i+1
 raise ValueError('Unbalanced BibTeX field')
def records(t):
 i=0
 while True:
  m=re.search(r'@(\w+)\s*\{',t[i:])
  if not m:return
  pos=i+m.start();typ=m.group(1);start=i+m.end()-1;body,end=balanced(t,start);i=end
  key,rest=body.split(',',1);fields={};j=0
  while j<len(rest):
   m2=re.match(r'\s*,?\s*([A-Za-z][A-Za-z0-9_]*)\s*=\s*',rest[j:])
   if not m2:
    assert not rest[j:].strip().strip(','),(key,rest[j:]);break
   name=m2.group(1);j+=m2.end()
   if rest[j]=='{':value,j=balanced(rest,j)
   elif rest[j]=='"':
    k=j+1
    while k<len(rest)and(rest[k]!='"'or rest[k-1]=='\\'):k+=1
    value=rest[j+1:k];j=k+1
   else:
    k=rest.find(',',j);k=len(rest)if k<0 else k;value=rest[j:k].strip();j=k
   fields[name]=value
  yield dict(key=key.strip(),type=typ,fields=fields,raw=t[pos:end])
groups=collections.defaultdict(list)
for p in sorted((W/'parts').iterdir()):
 f=p/'references.bib'
 if f.exists():
  for r in records(f.read_text()):r['owner']=p.name;groups[r['key']].append(r)
combined=[];audit=[];conflicts=[]
for key,rs in sorted(groups.items()):
 for r in rs:assert r['fields'].get('note')in ['verified','unverified'],(key,r['owner'],r['fields'].get('note'))
 # Prefer the most informative opened record, retaining every source scope below.
 r=max(rs,key=lambda x:(x['fields']['note']=='verified',len(x['fields']),len(x['fields'].get('annote',''))))
 fields=dict(r['fields'])
 if len(rs)>1:
  for field in ['doi','year','volume','pages']:
   vals={x['fields'][field]for x in rs if x['fields'].get(field)}
   if len(vals)>1:conflicts.append(dict(key=key,field=field,values=sorted(vals),selected=fields.get(field),resolution='Variants retained in per-owner records; selected metadata requires final human review.'))
  for x in rs:
   for k,v in x['fields'].items():fields.setdefault(k,v)
  fields['note']='verified'if any(x['fields']['note']=='verified'for x in rs)else'unverified'
  scopes=[]
  for x in rs:
   s=x['owner']+': '+x['fields'].get('annote','No additional scope annotation.')
   if x['fields'].get('url')!=fields.get('url'):s+=' Also opened URL: '+x['fields'].get('url','not supplied')+'.'
   scopes.append(s)
  fields['annote']='Combined verification scopes. '+' | '.join(scopes)
 combined.append('@'+r['type']+'{'+key+',\n'+',\n'.join('  '+k+' = {'+v+'}'for k,v in fields.items())+'\n}\n')
 audit.append(dict(key=key,note=fields['note'],owners=[x['owner']for x in rs],records=[dict(owner=x['owner'],type=x['type'],fields=x['fields'])for x in rs]))
(W/'SA23_references.bib').write_text('% SA23 bibliography. Verified means an indicated link/file was opened; annote states the exact scope.\n\n'+'\n'.join(combined))
(W/'outputs'/'bibliography_audit.json').write_text(json.dumps({'reference_records':len(groups),'verified':sum(x['note']=='verified'for x in audit),'unverified':sum(x['note']=='unverified'for x in audit),'same_key_merges':sum(len(v)>1 for v in groups.values()),'metadata_conflicts':conflicts,'records':audit},ensure_ascii=False,indent=2)+'\n')
print(json.dumps({'reference_records':len(groups),'same_key_merges':sum(len(v)>1 for v in groups.values()),'metadata_conflicts':conflicts},ensure_ascii=False))
