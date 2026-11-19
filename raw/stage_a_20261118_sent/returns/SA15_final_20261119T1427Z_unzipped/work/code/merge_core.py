"""Combine hand-curated registers. No mathematical verdict is assigned by this code.
Only the explicitly enumerated cross-package identities below are merged.
"""
from pathlib import Path
from copy import deepcopy
from collections import Counter
import json,csv,re
BASE=Path(__file__).resolve().parents[2]; W=BASE/'work'; D=BASE/'deliverables';D.mkdir(exist_ok=True)
def read(p):return json.loads(p.read_text())
def write(n,x):(D/n).write_text(json.dumps(x,ensure_ascii=False,indent=2)+'\n')
FILES={
 'P56':'SA15_texts/pro/MPL_5+6_001-037_transcription.tex',
 'P67':'SA15_texts/pro/MPL_6_038-067+7_001-060_transcription.tex',
 'P78':'SA15_texts/pro/MPL_7_061-072+8_001-078_transcription.tex',
 'P894':'SA15_texts/pro/MPL_8_079-081+9+4+100_transcription.tex'}
groups=[('cotes5_6','P56'),('cotes6_7','P67'),('root_review','P78'),('cotes8_9_4','P894')]
def collected(kind):
 out=[]
 for folder,pref in groups:
  files=[W/folder/(kind+'.json')] if pref!='P78' else [W/folder/(kind+'_c7.json'),W/folder/(kind+'_c8.json')]
  for f in files:
   if not f.exists():continue
   for x in read(f):
    x=deepcopy(x);x['curation_source']=str(f.relative_to(BASE));out.append(x)
 return out
def seq(x):return x if isinstance(x,list) else [] if x is None else [x]
def unique(xs):
 seen=set();out=[]
 for x in xs:
  k=json.dumps(x,sort_keys=True,ensure_ascii=False)
  if k not in seen:seen.add(k);out.append(x)
 return out
def locnorm(x):
 prefix=x['id'].split('-')[0];file=FILES[prefix]
 cotes=[str(c) for c in seq(x.get('cote'))];x['cote']=unique(cotes)
 scans=[]
 for s in seq(x.get('scans')):
  if isinstance(s,dict):scans.append(str(s['cote'])+':'+str(s['scan']).zfill(3))
  elif isinstance(s,str) and ':' in s:scans.append(s)
  elif len(cotes)==1:scans.append(cotes[0]+':'+str(s).zfill(3))
  else:scans.append(str(s))
 x['scans']=unique(scans)
 lines=x.get('lines',[])
 if isinstance(lines,dict):
  if 'file' in lines:lines=[lines['file']+':'+('–'.join(map(str,a)) if isinstance(a,list) else str(a)) for a in lines.get('ranges',[])]
  else:lines=[json.dumps(lines,ensure_ascii=False)]
 out=[]
 for line in seq(lines):
  if isinstance(line,dict):out.append(file+':'+str(line.get('transcription_file_lines',line.get('lines','')))+' (cote'+str(line.get('cote',''))+', scan'+str(line.get('scan',''))+')')
  else:out.append(str(line) if 'SA15_texts/' in str(line) else file+':'+str(line))
 x['lines']=unique(out)
 return x
rawitems=[locnorm(x) for x in collected('items')]
rawclaims=[locnorm(x) for x in collected('claims')]

# Read at both endpoints, including the full local hypotheses. Component versions
# remain embedded so one merged item never erases a changed assertion or caveat.
ITEM_MERGES=[
 ['P56-I106','P67-I077'],
 ['P67-I080','P78-I001'],
 ['P78-I060','P894-I001']]
CLAIM_MERGES=[['P78-C069','P78-C070','P894-C001']]

kind_allowed={'conjecture','unproved claim','unpursued implication','idea of the earlier run','reading question','self-flagged step','withdrawn in the same text','title, date or page count','other'}
kind_map={'construction said to work':'unproved claim','computation':'other','open on the pages':'conjecture'}
def consolidate(raw,mergegroups,typ):
 by={x['id']:x for x in raw};alias={};merged={}
 for grp in mergegroups:
  assert all(x in by for x in grp),grp
  head=grp[0];parts=[by[x] for x in grp];z=deepcopy(parts[0]);z['component_versions']=deepcopy(parts)
  for field in ['sources','cote','scans','lines','items','refs']:
   if any(field in p for p in parts):z[field]=unique([v for p in parts for v in seq(p.get(field))])
  z['consolidation_reason']={
   'P56-I106':'Same categorical ordinary infinitesimal/stratification comparison developed on several leaves. Formal-smooth positive statements and the proposed flat-lfp weakening remain separate hypothesis layers. The distinct ambient site-cohomology question P78-I010 is not merged.',
   'P67-I080':'Same completed Čech–Alexander construction, continued through the package boundary; the later compatibility/ML qualifications are retained.',
   'P78-I060':'Exact co-Lie/character derived-tensor calculation and coefficient change continued from cote8:78 to79.',
   'P78-C069':'Same co-Lie formula and derived coefficient-change calculation continued across the package boundary; the elementary associativity step remains labeled standard within component_versions.'}[head]
  for field in ['his_words','his_statement','statement','reconstruction','check_reason','status_on_pages','computation','fate','fate_date','present_status']:
   if field not in z:continue
   vals=unique([p[field] for p in parts if field in p])
   if len(vals)>1:z[field]='\n\n'.join('['+p['id']+'] '+(p[field] if isinstance(p[field],str) else json.dumps(p[field],ensure_ascii=False)) for p in parts if field in p)
  if typ=='item':z['check']='agrees' if all(p['check']=='agrees' for p in parts) else z['check']
  else:z['search_families']=unique([v for p in parts for v in seq(p.get('search_family',p.get('search_history',p.get('search_family_id'))))])
  merged[head]=z
  for old in grp:alias[old]=head
 out=[]
 for x in raw:
  if x['id'] in alias and alias[x['id']]!=x['id']:continue
  out.append(merged.get(x['id'],x))
 mapping={}
 for i,x in enumerate(out,1):
  old=x['id'];new=f'SA15-{i}' if typ=='item' else f'CL-SA15-{i:03}'
  mapping[old]=new
 for old,head in alias.items():mapping[old]=mapping[head]
 for x in out:
  old=x['id'];x['legacy_ids']=[k for k,v in mapping.items() if v==mapping[old]];x['id']=mapping[old]
  if typ=='item' and x['kind'] not in kind_allowed:x['kind_detail']=x['kind'];x['kind']=kind_map.get(x['kind'],'other')
 return out,mapping
items,imap=consolidate(rawitems,ITEM_MERGES,'item')
claims,cmap=consolidate(rawclaims,CLAIM_MERGES,'claim')
idmap={**imap,**cmap}
def remap(x):
 if isinstance(x,str):
  return re.sub(r'P(?:56|67|78|894)-[ICP]\d{3}',lambda m:idmap.get(m.group(),m.group()),x)
 if isinstance(x,list):return [remap(v) for v in x]
 if isinstance(x,dict):return {k:(v if k in ['legacy_ids','curation_source'] else remap(v)) for k,v in x.items()}
 return x
items=remap(items);claims=remap(claims)
for c in claims:c['items']=unique(c['items'])
write('SA15_items.json',items);write('SA15_claims.json',claims);write('SA15_id_map.json',idmap)
entries=[]
for f in ['entries_c7.json','entries_c8.json']:entries+=read(W/'root_review'/f)
for e in entries:e['item_id']=imap[e['item_id']];e['reason']=remap(e['reason'])
with (D/'SA15_entries.tsv').open('w') as f:
 w=csv.DictWriter(f,fieldnames=['entry_id','item_id','verdict','reason'],delimiter='\t');w.writeheader();w.writerows(entries)
supp=[];excluded=[]
for folder,_ in groups:
 p=W/folder/'supplementary_entries.tsv'
 if not p.exists():continue
 for e in csv.DictReader(p.open(),delimiter='\t'):
  if e.get('scope') and e['scope']!='in scope':excluded.append(e);continue
  e=remap(e);supp.append(e)
def tsv(name,rows,fields):
 with (D/name).open('w') as f:
  w=csv.DictWriter(f,fieldnames=fields,delimiter='\t',extrasaction='ignore');w.writeheader();w.writerows(rows)
tsv('SA15_supplementary_entries.tsv',supp,['entry_id','item_id','verdict','reason','scope','heading','note_line'])
tsv('SA15_out_of_scope_entries.tsv',excluded,['entry_id','item_id','verdict','reason','scope','heading','note_line'])
stats=dict(indexed_entries=len(entries),supplementary_in_scope_entries=len(supp),excluded_cote100_entries=len(excluded),items=len(items),raw_items=len(rawitems),claims=len(claims),raw_claims=len(rawclaims),item_kinds=dict(Counter(x['kind'] for x in items)),indexed_verdicts=dict(Counter(x['verdict'] for x in entries)),supplementary_verdicts=dict(Counter(x['verdict'] for x in supp)),claim_classes=dict(Counter(x['class'] for x in claims)))
write('SA15_core_counts.json',stats)
print(json.dumps(stats,ensure_ascii=False))
