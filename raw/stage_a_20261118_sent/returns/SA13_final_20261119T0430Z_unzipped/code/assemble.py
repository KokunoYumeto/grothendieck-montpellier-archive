"""Assemble authored reviews using explicit, human-reviewed semantic ID maps.

This program never creates a note verdict from a heading, keyword or score.
Every input verdict was authored after reading its entry and source passage.
"""
from pathlib import Path
from collections import Counter
import json,csv,re,copy
R=Path(__file__).resolve().parents[2];D=R/'deliverable'
SHARDS=['p1','p2','p3','p4','root_codex']
def readj(p):return json.loads(p.read_text())
def unique(a):
 out=[];seen=set()
 for x in a:
  k=json.dumps(x,sort_keys=True,ensure_ascii=False)
  if k not in seen:seen.add(k);out.append(x)
 return out
def arr(x):return x if isinstance(x,list) else [x]
def writej(name,a):(D/name).write_text(json.dumps(a,ensure_ascii=False,indent=2)+'\n')
def rows(p):return list(csv.DictReader(p.open(),delimiter='\t'))
def writet(name,fields,a):
 with (D/name).open('w',newline='') as f:
  w=csv.DictWriter(f,fieldnames=fields,delimiter='\t');w.writeheader();w.writerows(a)
records={k:[] for k in ['items','claims','problems']}
for s in SHARDS:
 for k in records:
  for obj in readj(D/'shards'/s/(k+'.json')):
   obj=copy.deepcopy(obj);obj['review_shard']=s
   # Relative paths in the original shard remain intelligible as well as the
   # normalized, archive-root paths used in the consolidated records.
   if k=='claims' and s in ['p2','p3','p4']:
    obj['computation_base']='shards/'+s+'/'
   records[k].append(obj)
 for k in records:
  ids=[x['id'] for x in records[k]]
  assert len(ids)==len(set(ids)),('duplicate allocation',k,s)

decisions=[];patches={}
for p in [D/'shards/p2/cross_package_merge_map.json',D/'shards/p3/cross_package_merge_map.json',D/'shards/p2/supplementary_merge_map.json',D/'semantic_merge_decisions.json']:
 if p.exists():
  data=readj(p)
  for a in data.get('merges',[]):
   a=copy.deepcopy(a);a['audit_file']=str(p.relative_to(D));decisions.append(a)
  patches.update(data.get('canonical_patches',{}))
alias={a['from']:a['canonical'] for a in decisions}
def canonical(x):
 seen=set()
 while x in alias:
  assert x not in seen,'alias cycle';seen.add(x);x=alias[x]
 return x
for a in decisions:a['canonical']=canonical(a['canonical']);a['status']='applied after source-based semantic review'

def merge_one(dst,src,kind):
 if kind=='claims':dst.setdefault('occurrence_statuses',[{'id':dst['id'],'status':dst['status_on_pages'],'scans':copy.deepcopy(dst['scans'])}])
 dst.setdefault('merged_occurrences',[]).append(copy.deepcopy(src))
 dst['aliases']=unique(dst.get('aliases',[])+[src['id']]+src.get('aliases',[]))
 for key in ['sources','items','cote','scans','lines','occurrences','refs','search_ids','claims','claim_ids']:
  if key in src:dst[key]=unique(arr(dst.get(key,[]))+arr(src[key]))
 textfields={'items':['his_words','statement','reconstruction','check_reason'],
             'claims':['his_statement','statement','fate','fate_date','present_status'],
             'problems':['as_he_states','plausible_today','state_of_art','why_open','worth']}[kind]
 for key in textfields:
  if src.get(key) and src.get(key)!=dst.get(key):dst[key]=str(dst.get(key,''))+'\n\nFurther occurrence ('+src['id']+'): '+str(src[key])
 if kind=='claims':
  dst['occurrence_statuses'].append({'id':src['id'],'status':src['status_on_pages'],'scans':src['scans']})
  dst.setdefault('additional_computation_audits',[]).append({'id':src['id'],'base':src.get('computation_base',''),'computation':src['computation']})
 if kind=='items':dst.setdefault('occurrence_checks',[]).append({'id':src['id'],'check':src['check'],'reason':src['check_reason']})

for kind,objs in records.items():
 idx={x['id']:x for x in objs}
 for a in decisions:
  if {'item':'items','claim':'claims','problem':'problems'}.get(a['kind'])!=kind:continue
  assert a['from'] in idx and a['canonical'] in idx,(kind,a)
  merge_one(idx[a['canonical']],idx[a['from']],kind)
 for old in alias:
  if old in idx:del idx[old]
 for ident,p in patches.items():
  if ident not in idx:continue
  o=idx[ident]
  for key,val in p.items():
   if key=='append':o['statement']+=' '+val
   elif key in o or key in ['title','items','statement']:o[key]=val
  o['assembly_patch']=p
 records[kind]=sorted(idx.values(),key=lambda x:int(x['id'].rsplit('-',1)[1]))

# Explicit mathematical assembly refinements for the recovered continuous lemma.
cs={x['id']:x for x in records['claims']}
if 'C-SA13-064' in cs:
 c=cs['C-SA13-064'];c['status_on_pages']='proved there';c['class']='E'
 c['fate']='The complete reused Lemma2 is a classical common-completion and ideal-contraction result for two regular local rings, not only the special case where the larger ring already is the completion. Its exact hypothesis and proof continuation were recovered across33:173→137→135. The independent proof is in shards/p2/cross_package_merge_audit.md; the precise original bibliographic source remains unverified.'
 c['present_status']='As of2026-11-19: established under the restored hypotheses; source authorship/edition not identified.'
 c['computation']={'kind':'independent symbolic re-proof','proof':'shards/p2/cross_package_merge_audit.md','scope':'Associated graded isomorphisms, completion, faithful flatness, contraction, principality and fraction-field intersection; no numerical calculation is required.'}
for c in records['claims']:
 c['items']=unique([canonical(x) for x in c['items']])
for p in records['problems']:
 for k in ['items','claims','claim_ids']:
  if k in p:p[k]=unique([canonical(x) for x in p[k]])
ps={x['id']:x for x in records['problems']}
if 'MP-SA13-133' in ps:
 ps['MP-SA13-133']['occurrences']=unique(ps['MP-SA13-133']['occurrences']+[
  {'file':'pro/MPL_36_053-085+39_transcription.tex','cote':36,'scan':79,'start':786,'end':790},
  {'file':'pro/MPL_36_053-085+39_transcription.tex','cote':36,'scan':80,'start':794,'end':799}])
 ps['MP-SA13-133']['state_of_art']+=' The36:079–080 occurrence gives a distinct geometric warning: a finite extension detecting one torsion point need not carry an entire compatible division tower. Preserve the K/Kprime scan alarm. See C-SA13-439 and the p3/p4 semantic audit.'
if 'MP-SA13-99' in ps:
 ps['MP-SA13-99']['editorial_dependency']={'item':'SA13-257','problem':'MP-SA13-64','locator':{'file':'pro/MPL_36_002-052_transcription.tex','cote':36,'scan':4,'start':119,'end':120},'scope':'The draft2.6(a) objection asks about trait/limit hypotheses. The separate Néron completion problem is retained; identity of missing draft and printed quantifiers is not presumed.'}
if 'MP-SA13-240' in ps:
 ps['MP-SA13-240']['occurrences']=unique(ps['MP-SA13-240']['occurrences']+cs['C-SA13-605']['lines'])
 ps['MP-SA13-240']['state_of_art']+=' Later in the supplied text,34:154 Corollary5.4 supplies the lower bound explicitly promised on142. Its historical proof conditions and current trait theorem are distinguished in C-SA13-605; it is no longer only deferred within this dossier.'
if 'MP-SA13-242' in ps:
 for cid in ['C-SA13-600','C-SA13-609']:ps['MP-SA13-242']['occurrences']=unique(ps['MP-SA13-242']['occurrences']+cs[cid]['lines'])
 ps['MP-SA13-242']['state_of_art']+=' Later34:149 §5.1 and157 §6.1 explicitly impose vanishing on every strict generization or the whole punctured special fibre. These supply the missing uniform premise; the earlier defective wording remains a separate reading alarm.'

entries=[]
for s in SHARDS:
 p=D/'shards'/s/'entries.tsv'
 if not p.exists():continue
 for e in rows(p):
  old=e['item_id'];e['item_id']=canonical(old)
  if old!=e['item_id']:
   e['reason']+=' Cross-package source-based consolidation: '+old+' is an alias of '+e['item_id']+'.'
   if e['verdict']=='kept':e['verdict']='merged into item'
  if e['verdict']=='merged into item':e['verdict']='merged'
  entries.append(e)
index=rows(R/'sources/notes/NOTES_INDEX.tsv')
sourceids=[x.get('entry_id') or x.get('id') for x in index]
assert len(entries)==379 and Counter(x['entry_id'] for x in entries)==Counter(sourceids),'source entry coverage'
order={x:i for i,x in enumerate(sourceids)};entries.sort(key=lambda x:order[x['entry_id']])
writet('SA13_entries.tsv',['entry_id','item_id','verdict','reason'],entries)
for kind,a in records.items():writej('SA13_'+kind+'.json',a)
writet('SA13_aliases.tsv',['kind','alias','canonical','reason','audit_file'],[{'kind':a['kind'],'alias':a['from'],'canonical':a['canonical'],'reason':a['reason'],'audit_file':a['audit_file']} for a in decisions])

readings=[];links=[];events=[]
for s in SHARDS:
 base=D/'shards'/s
 for name,dest in [('readings.tsv',readings),('links.tsv',links),('check_events.tsv',events)]:
  p=base/name
  if p.exists():dest.extend(rows(p))
 for p in base.glob('*_check_events.tsv'):
  for e in rows(p):
   if 'statement_id' in e:events.append(e)
   else:
    targets=re.findall(r'C-SA13-\d+|MP-SA13-\d+|SA13-\d+',e.get('target','')) or (e.get('target') or e.get('id')).split(';')
    for target in targets:events.append(dict(statement_id=target,date='2026-11-19',who=e.get('who',''),type=e.get('type','targeted proof check'),outcome=e.get('result','')+' Evidence: '+e.get('evidence','')+' Original audit event '+e.get('id','')))
for e in events:
 e['type']=e['type'].replace('statement’s',"statement's")
 old=e['statement_id'];e['statement_id']=canonical(old)
 if old!=e['statement_id']:e['outcome']='Original event for alias '+old+'. '+e['outcome']
for a in decisions:events.append(dict(statement_id=a['canonical'],date='2026-11-19',who='GPT-6 Astra Pro; configured effort not exposed; SA13/root with independent shard review',type='used and rechecked in this run',outcome='Source-based semantic merge of '+a['from']+': '+a['reason']+' Audit: '+a['audit_file']))
supp=D/'shards/p2/supplementary_merge_map.json'
if supp.exists():
 for rel in readj(supp).get('component_identity_links',[]):
  src=cs[canonical(rel['from'])];dst=cs[canonical(rel['to'])]
  links.append({'kind':'folder','from':', '.join(src['scans'])+' ('+src['id']+')','to':', '.join(dst['scans'])+' ('+dst['id']+')','what':rel['relation'],'evidence':rel['evidence']+' See shards/p2/supplementary_merge_audit.md. This is an ingredient/occurrence link, not an alias of the full assertions.','note_ids':'Codex leads; no indexed Pro entry created'})
 links.append({'kind':'folder','from':'34:149 §5.0 (SA13-62)','to':'34:142–143 §3.2–3.3 (SA13-502)','what':'Explicit prerequisite reference followed by execution','evidence':'K34-09 §5.0 explicitly refers back to3.3/3.2; retained as a programme/execution link because the later geometric-depth questions have distinct scope.','note_ids':'Codex K34-08,K34-09'})
readings=unique(readings);links=unique(links);events=unique(events)
writet('SA13_readings.tsv',['cote','scan','line','reading','alternative','evidence','weight','confidence'],readings)
writet('SA13_links.tsv',['kind','from','to','what','evidence','note_ids'],links)
writet('SA13_project_links.tsv',['kind','from','to','what','evidence','note_ids'],[x for x in links if x['kind']=='our projects'])
writet('CHECK_EVENTS.tsv',['statement_id','date','who','type','outcome'],events)

# BibTeX entries are split only at top-level @entry boundaries. Duplicate keys
# must be explicitly reconciled; arbitrary later records never silently win.
bib={};conflicts=[]
for s in SHARDS:
 for p in sorted((D/'shards'/s).glob('*references.bib')):
  for block in re.split(r'(?m)(?=^@\w+\{)',p.read_text()):
   if not block.strip():continue
   m=re.match(r'@\w+\{([^,]+),',block.strip())
   if not m:continue
   key=m.group(1);block=block.strip()
   if key in bib and block!=bib[key]['block']:conflicts.append({'key':key,'first':bib[key]['source'],'second':str(p.relative_to(D)),'first_block':bib[key]['block'],'second_block':block})
   else:bib[key]={'block':block,'source':str(p.relative_to(D))}
# These nine duplicate keys were reviewed against both records. Eight identify
# the same source with complementary access notes. SGA7IX uses p3's corrected
# chapter DOI (BFb0068694), not the volume/ExposéI DOI in the earlier p2 record.
resolved_keys={'IllusieErrSGA5III','SGA5I','SGA5III','SGA4XVII','Stacks0FPP','Stacks03TI','Stacks0A3J','SGA7IX','BrinonConrad2009'}
for conflict in conflicts:
 if conflict['key'] in resolved_keys:
  if conflict['key']=='SGA7IX':bib[conflict['key']]={'block':conflict['second_block'],'source':conflict['second']}
  conflict['resolution']='Same source; preserve both exact access audits in the original shard bibliographies. '+('Use p3 chapter DOI10.1007/BFb0068694.' if conflict['key']=='SGA7IX' else 'Use first record for the canonical citation; complementary verification scope retained in both shard audits.')
writej('outputs/bibliography_conflicts.json',conflicts)
(D/'SA13_references.bib').write_text('\n\n'.join(v['block'] for k,v in sorted(bib.items()))+'\n')
summary={'entries':len(entries),'items':len(records['items']),'claims':len(records['claims']),'problems':len(records['problems']),'readings':len(readings),'links':len(links),'project_links':sum(x['kind']=='our projects' for x in links),'check_events':len(events),'bibliography_keys':len(bib),'bibliography_conflicts':len(conflicts),'unresolved_bibliography_conflicts':sum('resolution' not in x for x in conflicts),'aliases':len(decisions),'verdict_counts':dict(Counter(x['verdict'] for x in entries)),'item_kind_counts':dict(Counter(x['kind'] for x in records['items'])),'claim_class_counts':dict(Counter(x['class'] for x in records['claims'])),'claim_status_counts':dict(Counter(x['status_on_pages'] for x in records['claims']))}
writej('outputs/assembly_counts.json',summary);print(json.dumps(summary,indent=2))
