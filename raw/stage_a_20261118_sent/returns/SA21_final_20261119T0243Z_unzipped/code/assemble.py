"""Assemble manually authored decisions. This program makes no source verdicts."""
from pathlib import Path
import json,csv,re,collections
R=Path(__file__).resolve().parents[1]
PARTS=['root','cotes_3_5','cotes_6_7','cotes_8_9','cotes_9_09_13','cotes_9_14_18','project_links','final_audit']
parts=[R/'parts'/p for p in PARTS if (R/'parts'/p).exists()]
def rd(p):return json.loads(p.read_text())
def jt(p,x):p.write_text(json.dumps(x,ensure_ascii=False,indent=2)+'\n')
def tr(p):
 with p.open(newline='') as f:return list(csv.DictReader(f,delimiter='\t'))
def tw(p,rows,fields):
 with p.open('w',newline='') as f:
  w=csv.DictWriter(f,fieldnames=fields,delimiter='\t',extrasaction='ignore');w.writeheader();w.writerows(rows)
claims=[];problems=[];readings=[];links=[];events=[]
for p in parts:
 if (p/'claims.json').exists():
  for x in rd(p/'claims.json'):
   x['audit_part']=str(p.relative_to(R));claims.append(x)
 if (p/'problems.json').exists():problems.extend(rd(p/'problems.json'))
 for name,dest in [('readings.tsv',readings),('links.tsv',links),('check_events.tsv',events),('extra_check_events.tsv',events),('additional_reference_events.tsv',events),('supplemental_check_events.tsv',events)]:
  if (p/name).exists():dest.extend(tr(p/name))
assert len({c['id'] for c in claims})==len(claims),'duplicate claim IDs'
# Genuine repeated questions. Keep different axiom versions as explicit subrecords.
merges={'MP-SA21-6-09':'MP-SA21-4-08','MP-SA21-7-08':'MP-SA21-4-12','MP-SA21-8-07':'MP-SA21-7-10','MP-SA21-9-10':'MP-SA21-9-08'}
byold={p['id']:p for p in problems};groups={}
for p in problems:groups.setdefault(merges.get(p['id'],p['id']),[]).append(p)
canonical=[];aliases={}
for n,(key,group) in enumerate(groups.items(),1):
 x=dict(group[0]);nid=f'MP-SA21-{n:03d}'
 for g in group:aliases[g['id']]=nid
 x['id']=nid;x['source_problem_ids']=[g['id'] for g in group]
 if len(group)>1:
  x['occurrences']=[o for g in group for o in g['occurrences']]
  for f in ['as_he_states','plausible_today','state_of_art','why_open','worth']:
   x[f]='\n\n'.join(g['id']+' ('+g['title']+'): '+str(g[f]) for g in group)
  x['refs']=list(dict.fromkeys(r for g in group for r in g['refs']))
  x['versions']=group
 canonical.append(x)
ref_alias={'Esquisse1997':'Esquisse1984','CSG2026':'CSGUnpublished','SGA4I1972':'SGA4II','MontpellierCatalogue':'MontpellierArchive','MontpellierSA21':'MontpellierArchive'}
def walk(x):
 if isinstance(x,str):
  for a,b in ref_alias.items():x=re.sub(r'(?<![\w-])'+re.escape(a)+r'(?![\w-])',b,x)
  for a in sorted(aliases,key=len,reverse=True):
   if a!=aliases[a]:x=re.sub(r'(?<![\w-])'+re.escape(a)+r'(?![\w-])',aliases[a],x)
  return x
 if isinstance(x,list):return [walk(a) for a in x]
 if isinstance(x,dict):return {k:(v if k in ['id','source_problem_ids','versions'] else walk(v)) for k,v in x.items()}
 return x
claims=walk(claims);canonical=walk(canonical);readings=walk(readings);links=walk(links);events=walk(events)
status_exceptions={'C-SA21-3-001':'false as stated','C-SA21-3-027':'current-run refinement','C-SA21-4-011':'corrected by himself later','C-SA21-4-012':'current-run refinement','C-SA21-4-027':'current-run refinement','C-SA21-4-035':'current-run refinement'}
status_spellings={'corrected by himself later (both places)':'corrected by himself later','false as stated (with the counterexample, every hypothesis checked)':'false as stated','proved in this run; reconstruction':'current-run refinement'}
allowed_status={'proved there','proof sketched','stated without proof','corrected by himself later','false as stated','open on the pages','definition/construction','current-run refinement'}
for x in claims:
 if not x.get('status_category'):x['status_category']=status_exceptions.get(x['id'],status_spellings.get(x['status_on_pages'],x['status_on_pages']))
 if x['status_category'] not in allowed_status:x['status_category']='awaiting explicit owner category'
for e in events:
 if e['type'].startswith('refuted, with the refined statement'):e['type']='refuted, with the refined statement’s id'
jt(R/'SA21_claims.json',claims);jt(R/'SA21_problems.json',canonical)
tw(R/'audit/problem_aliases.tsv',[{'source_id':k,'canonical_id':v,'merge_reason':'same question across axiom versions' if k in merges else 'global numbering'} for k,v in aliases.items()],['source_id','canonical_id','merge_reason'])
tw(R/'SA21_readings.tsv',readings,['cote','scan','line','reading','alternative','evidence','weight','confidence'])
# Only checked endpoints belong to the main link table. Keep explicit unresolved
# provenance as a separate audit table, never erase it or turn it into a proof.
verified=[];unresolved=[];projects=[]
for x in links:
 if x.get('note_ids','').startswith(('C-SA21-','MP-SA21-')):
  x['evidence']+=' Claim/problem pointers: '+x['note_ids']+'. These are claim/problem IDs, not source-note IDs.'
  x['note_ids']=''
 if x['kind']=='our projects':projects.append(x)
 elif any(t in x['evidence'].lower() for t in ['target absent','cannot be checked','could not be checked','explicitly unresolved','not a proved identification','not as a proved identification','not identified/opened','unresolved reference-reading alarm','unresolved forward reference','candidate endpoint mismatch','not the cited corollary','unresolved identification lead','unresolved material link']):unresolved.append(x)
 else:verified.append(x)
fields=['kind','from','to','what','evidence','note_ids']
tw(R/'SA21_links.tsv',verified,fields);tw(R/'SA21_unresolved_links.tsv',unresolved,fields)
if projects:tw(R/'SA21_project_leads.tsv',projects,fields)
project_detail=R/'parts/project_links/project_links.tsv'
if project_detail.exists():
 detail=walk(tr(project_detail))
 tw(R/'SA21_project_leads.tsv',detail,list(detail[0]))
# Every Stage1 record gets the actual content check, explicitly not an assertion
# that every mathematical statement it reports has been proved.
for x in rd(R/'SA21_items.json'):
 events.append({'statement_id':x['id'],'date':'2026-11-19','who':'GPT-6 Astra Pro; effort not exposed; /root SA21','type':'used and rechecked in this run','outcome':'Read the full source entry and its cited transcription passages; source/hypothesis check, not blanket proof certification. '+x['check_reason']})
tw(R/'CHECK_EVENTS.tsv',events,['statement_id','date','who','type','outcome'])
# Deduplicate bibliography keys. Root's specific chronology and access notes
# control when the same source was independently opened by several readers.
bib={};provenance=[]
for p in parts:
 q=p/'references.bib'
 if not q.exists():continue
 for block in re.split(r'(?=^@)',q.read_text(),flags=re.M):
  m=re.match(r'@\w+\s*\{\s*([^,]+)',block)
  if not m:continue
  key=m.group(1).strip();key2=ref_alias.get(key,key)
  block=block.replace('{'+key+',','{'+key2+',',1)
  provenance.append({'key':key2,'original_key':key,'source':str(q.relative_to(R)),'selected':key2 not in bib})
  if key2 not in bib:bib[key2]=block.strip()
(R/'SA21_references.bib').write_text('\n\n'.join(bib.values())+'\n')
jt(R/'audit/bibliography_merge.json',provenance)
counts={'entries':len(tr(R/'SA21_entries.tsv')),'items':len(rd(R/'SA21_items.json')),'claims':len(claims),'claims_by_cote':dict(collections.Counter(str(x['cote']) for x in claims)),'claims_by_class':dict(collections.Counter(x['class'] for x in claims)),'claims_by_status':dict(collections.Counter(x['status_category'] for x in claims)),'problems':len(canonical),'premerge_problem_records':len(problems),'readings':len(readings),'verified_links':len(verified),'unresolved_links':len(unresolved),'project_links':len(projects),'references':len(bib),'check_events':len(events),'parts_present':[p.name for p in parts]}
jt(R/'audit/counts.json',counts);print(json.dumps(counts,ensure_ascii=False,indent=2))
