"""Schema, evidence and coverage audit; not a mathematical truth classifier."""
import json,csv,re,collections,hashlib
from pathlib import Path
D=Path(__file__).resolve().parent;root=D.parents[2]
errors=[]
def check(test,msg):
 if not test:errors.append(msg)
def j(name):return json.loads((D/name).read_text())
C=j('claims.json');I=j('items.json');P=j('problems.json');R=j('reference_details.json');A=j('directions.json')
ED=j('editorial_tasks.json');EA=j('editorial_directions.json');edids={e['id'] for e in ED}
ids={c['id'] for c in C};items={i['id'] for i in I};problems={p['id'] for p in P}
check(len(C)==85 and len(ids)==85,'claim cardinality/uniqueness')
check(len(I)==20 and len(items)==20,'item cardinality/uniqueness')
check(len(P)==14 and len(problems)==14,'problem cardinality/uniqueness after approved origin audit')
check(len(ED)==15 and len(edids)==15,'editorial task cardinality/uniqueness')
for c in C:
 for k in ['id','items','cote','scans','lines','his_statement','statement','status_on_pages','status_category','computation','class','fate','fate_date','present_status','refs','confidence']:
  check(k in c,c['id']+' missing '+k)
 check(c['class'] in 'ABCDEF' and len(c['class'])==1,c['id']+' invalid class')
 check(bool(c['refs']) and all(k in R for k in c['refs']),c['id']+' invalid references')
 check(all(i in items for i in c['items']),c['id']+' invalid item')
 check(not re.search(r'PENDING|mapping in progress|under targeted investigation',c['fate']+' '+c['present_status'],re.I),c['id']+' unfinished fate')
for p in P+ED:
 check(bool(p.get('occurrences')),p['id']+' no occurrences')
 check(bool(p.get('state_of_art')) and 'mapping in progress' not in p['state_of_art'],p['id']+' unfinished state')
 check(all(k in R for k in p['refs']),p['id']+' invalid reference')
for p in P:check(bool(p.get('source_cue')) and p.get('count_as_authorial_mathematical_problem'),p['id']+' lacks authorial problem cue')
for e in ED:
 check(bool(e.get('original_id'))!=bool(e.get('source_problem_id')),e['id']+' needs exactly one redirect/split origin')
 check(e.get('original_id') not in problems,e['id']+' whole redirect still in MP register')
 check(not e.get('source_problem_id') or e['source_problem_id'] in problems,e['id']+' split source missing')
for d in A+EA:
 check(all(k in ids for k in d['claims']),d['id']+' invalid claims')
 check(all(k in items for k in d['items']),d['id']+' invalid items')
 check(all(k in problems for k in d['problems']),d['id']+' invalid problems')
 check(all(k in edids for k in d['editorial_tasks']),d['id']+' invalid editorial tasks')
 check(bool(d['problems']) if d in A else not d['problems'],d['id']+' wrong Stage6/editorial partition')
 check(bool(d['first_step']) and bool(d['known']) and bool(d['residual']),d['id']+' missing task detail')
entries=list(csv.reader((D/'entries.tsv').open(),delimiter='\t'))
check(entries==[['entry_id','item_id','verdict','reason']],'successor Stage1 file must have exact header and zero rows')
check(all(not x['sources'] for x in I),'successor item falsely claims indexed-note sources')
log=[json.loads(x) for x in (D/'search_log.jsonl').read_text().splitlines()]
searched={x['claim'] for x in log if x.get('type')=='exact hypothesis match after search'}
check(searched==ids,'not every claim has searched fate audit')
events=list(csv.DictReader((D/'check_events.tsv').open(),delimiter='\t'))
event_ids={e['statement_id'] for e in events}
check(ids|items|set(R)<=event_ids,'missing claim/item/reference check event')
comp=j('computation_output.json')
labels={x['name'] for x in comp}
for c in C:
 check(set(c['computation']['certificate_search_labels'])<=labels,c['id']+' bad certificate reference')
sources={'HC1-01':261,'K1-01':758,'K1-02':545,'K1-03':494,'K1-04':541,'K1-05':643,'K1-06':662,'K1-07':437,'K21-01':505,'K21-02':301}
reads=[json.loads(x) for x in (D/'read_logs/reads.jsonl').read_text().splitlines()]
coverage=[]
for name,n in sources.items():
 path='sources/texts/codex/'+name+'_transcription.tex';covered=set()
 for r in reads:
  if r['path']==path:covered.update(range(r['first_line'],r['last_line']+1))
 check(set(range(1,n+1))<=covered,name+' unlogged source range')
 actual=(root/path).read_bytes()
 check(len(actual.decode().splitlines())==n,name+' source line count changed')
 coverage.append(dict(source=path,lines=n,sha256=hashlib.sha256(actual).hexdigest(),logged_full_range=True))
for name in ['section.md','proof_notes.md','coverage.md','directions.md','links.tsv','references.bib','other_project_links.tsv','REBUILD.md','status_categories.json']:
 check((D/name).exists(),name+' absent')
for key in R:check('@misc{'+key+',' in (D/'references.bib').read_text(),key+' missing bib')
check((D/'references.bib').read_text().count('note = {verified}')==len(R),'bibliography verification markers')
out=dict(errors=errors,items=len(I),indexed_entries=0,claims=len(C),problems=len(P),readings=len(list(csv.DictReader((D/'readings.tsv').open(),delimiter='\t'))),links=len(list(csv.DictReader((D/'links.tsv').open(),delimiter='\t'))),references=len(R),check_events=len(events),search_records=len(log),finite_certificates_or_illustrations=len(comp),directions=len(A),class_counts=dict(collections.Counter(c['class'] for c in C)),status_counts=dict(collections.Counter(c['status_category'] for c in C)),source_lines=sum(sources.values()),source_coverage=coverage)
out.update(editorial_tasks=len(ED),editorial_directions=len(EA))
(D/'validation.json').write_text(json.dumps(out,ensure_ascii=False,indent=2)+'\n')
print(json.dumps(out,ensure_ascii=False,indent=2))
raise SystemExit(bool(errors))
