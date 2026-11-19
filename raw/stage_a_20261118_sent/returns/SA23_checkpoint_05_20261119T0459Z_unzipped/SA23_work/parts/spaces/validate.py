from pathlib import Path
import json,csv,re,collections
P=Path(__file__).parent;B=P.parents[2]
cs=json.loads((P/'claims.json').read_text());it=json.loads((P/'items.json').read_text());ps=json.loads((P/'problems.json').read_text());refs=json.loads((P/'reference_checks.json').read_text())
errors=[]
for name,rows in [('claims',cs),('items',it),('problems',ps)]:
 ids=[x['id'] for x in rows]
 if len(ids)!=len(set(ids)):errors.append(name+' duplicate IDs')
ii={x['id'] for x in it};ci={x['id'] for x in cs}
for c in cs:
 if not set(c['items'])<=ii:errors.append(c['id']+' missing item')
 if not set(c['refs'])<=set(refs):errors.append(c['id']+' missing reference')
 if not c['fate'] or not c['computation']:errors.append(c['id']+' incomplete check')
for p in ps:
 if not {x['claim'] for x in p['occurrences']}<=ci:errors.append(p['id']+' missing claim')
dirs=json.loads((P/'directions.json').read_text());pi={x['id'] for x in ps}
for c in cs:
 if not c.get('status_category') or not c.get('record_origin'):errors.append(c['id']+' missing manual status/origin')
for d in dirs:
 for key,ids in [('items',ii),('claims',ci),('problems',pi)]:
  if not d[key] or not set(d[key])<=ids:errors.append('Direction'+str(d['rank'])+' invalid '+key)
 if not all(1<=d[k]<=5 for k in ['interest','feasible_progress_in_one_run']):errors.append('Direction'+str(d['rank'])+' invalid scores')
logs=[json.loads(x) for x in (P/'search_log.jsonl').read_text().splitlines()]
searched={i for x in logs for i in x.get('claims',[])}
if ci-searched:errors.append('Claims without searched fate: '+str(ci-searched))
required=['items.json','entries.tsv','claims.json','problems.json','readings.tsv','links.tsv','references.bib','check_events.tsv','search_log.jsonl','section.md','coverage.md','directions.md','proof_checks.md','compute_checks.py','compute_checks.output.json']
for f in required:
 if not (P/f).exists():errors.append('Missing '+f)
reads=[json.loads(x) for x in (P/'read_logs/reads.jsonl').read_text().splitlines()];coverage={}
for stem in ['K161-3-01','K161-3-02','K161-3-03','K161-4-01','K161-4-02']:
 path='sources/texts/codex/'+stem+'_transcription.tex';n=len((B/path).read_text().splitlines());seen=set()
 for r in reads:
  if r['path']==path:seen.update(range(r['first_line'],min(n,r['last_line'])+1))
 coverage[stem]={'total_lines':n,'logged_lines':len(seen),'missing_lines':sorted(set(range(1,n+1))-seen)}
 if coverage[stem]['missing_lines']:errors.append(stem+' reading gaps')
# Count register rows; no automated verdicts are inferred.
counts={'items':len(it),'claims':len(cs),'problems':len(ps),'references':len(refs),'search_events':len(logs),'directions':len(dirs)}
for f in ['readings.tsv','links.tsv','entries.tsv','check_events.tsv']:counts[f]=sum(1 for _ in csv.reader((P/f).open(),delimiter='\t'))-1
result={'date':'2026-11-19','owner':'spaces','status':'PASS' if not errors else 'FAIL','errors':errors,'counts':counts,'reading_coverage':coverage,'scope':'Structural validation only. Mathematical claims are manually checked in registers/proofs and named computations.'}
import runpy
result['problem_origin_validation']=runpy.run_path(str(P.parents[1]/'integration/validate_problem_origins.py'))['validate']('spaces')
counts['editorial_tasks']=result['problem_origin_validation']['editorial_tasks']
counts['editorial_directions']=result['problem_origin_validation']['editorial_directions']
(P/'validation.json').write_text(json.dumps(result,indent=2)+'\n');print(json.dumps(result,indent=2))
if errors:raise SystemExit(1)
