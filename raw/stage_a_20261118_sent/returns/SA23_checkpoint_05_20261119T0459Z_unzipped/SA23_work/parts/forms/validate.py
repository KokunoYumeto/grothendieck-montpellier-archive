#!/usr/bin/env python3
"""Structural audit. Mathematical judgments are manually recorded elsewhere."""
from pathlib import Path
import json,csv,collections,hashlib

P=Path(__file__).parent;B=P.parents[2]
def js(name):return json.loads((P/name).read_text())
def tab(name):return list(csv.DictReader((P/name).open(),delimiter='\t'))
cs=js('claims.json');its=js('items.json');ps=js('problems.json')
eds=js('editorial_tasks.json');docs=js('document_records.json')
refs=js('reference_checks.json');dirs=js('directions.json')
edirs=js('editorial_directions.json')
events=tab('check_events.tsv');logs=[json.loads(x) for x in (P/'search_log.jsonl').read_text().splitlines()]
errors=[]
def check(condition,message):
    if not condition:errors.append(message)
for name,data in [('claim',cs),('item',its),('problem',ps),('editorial task',eds),('document',docs)]:
    check(len({x['id'] for x in data})==len(data),name+' duplicate IDs')
ii={x['id'] for x in its};ci={x['id'] for x in cs};pi={x['id'] for x in ps}
ei={x['id'] for x in eds};di={x['id'] for x in docs}
check(not(ci&di),'Mathematical and document records overlap')
check(not(pi&ei),'Authorial questions and editorial tasks overlap')
allowed={'proved there','proof sketched','stated without proof','corrected by himself later',
         'false as stated','open on the pages','present-run refinement'}
for c in cs:
    check(set(c['items'])<=ii,c['id']+' missing item')
    check(set(c['refs'])<=set(refs),c['id']+' missing reference')
    check(c.get('status_category') in allowed,c['id']+' missing canonical manual status')
    check(c.get('record_origin')=='source assertion',c['id']+' unexpected origin')
    check(bool(c['fate']) and bool(c['computation']),c['id']+' missing fate/check')
for c in docs:
    check(c.get('record_type')=='document metadata',c['id']+' metadata type missing')
for p in ps+eds:
    check({x['claim'] for x in p['occurrences']}<=ci,p['id']+' missing claim')
    check(set(p['refs'])<=set(refs),p['id']+' missing reference')
    check(bool(p.get('source_cue')),p['id']+' missing source-cue/reason field')
    check(bool(p.get('worth')),p['id']+' missing individual worth judgment')
    for cue in p.get('source_cues',[]):
        lo,hi=cue['physical_lines'];ls=(B/cue['source']).read_text().splitlines()
        check(cue['verbatim']=='\n'.join(ls[lo-1:hi]),p['id']+' altered literal source cue')
for p in ps:
    check(p.get('record_type')=='authorial problem',p['id']+' not authorial')
    check(p.get('origin')=='authorial question or deferred step',p['id']+' origin mismatch')
for p in eds:
    check(p['id'].startswith('ED-SA23-forms-'),p['id']+' invalid editorial ID')
    check(p.get('original_id','').startswith('MP-SA23-forms-'),p['id']+' former ID missing')
    check(p['original_id'] not in pi,p['id']+' still present in authorial index')
for d in dirs:
    for key,valid in [('items',ii),('claims',ci),('problems',pi)]:
        check(bool(d[key]) and set(d[key])<=valid,'Direction'+str(d['rank'])+' invalid '+key)
    check(all(1<=d[k]<=5 for k in ['interest','feasible_progress_in_one_run']),
          'Direction'+str(d['rank'])+' invalid scores')
    check(all(d[k] for k in ['known','residual','first_step']),
          'Direction'+str(d['rank'])+' missing scope')
    check(set(d.get('editorial_tasks',[]))<=ei,'Direction has invalid editorial dependency')
for d in edirs:
    check(d['record_type']=='editorial follow-up outside Stage6','Invalid editorial direction type')
    for key,valid in [('items',ii),('claims',ci),('problems',pi),('editorial_tasks',ei)]:
        check(set(d[key])<=valid,d['id']+' missing '+key)
searched={c for x in logs for c in x.get('claims',[])}
check(ci<=searched,'Claims missing search/fate audit: '+str(ci-searched))
ev={x['statement_id'] for x in events}
check(ci|ii|di|set(refs)<=ev,'Missing check-event identifiers: '+str((ci|ii|di|set(refs))-ev))
check(pi|ei<=ev,'Missing problem-origin check events')
computes=js('compute_checks.output.json')
for k,v in computes.items():check(set(v['claims'])<=ci,k+' invalid computation provenance')
check(set(computes)<=ev,'Missing computation events')
check(not tab('entries.tsv'),'Unassigned indexed-entry verdicts introduced')

reads=[json.loads(x) for x in (P/'read_logs/reads.jsonl').read_text().splitlines()]
assigned=[
    'sources/texts/api/ega_v_cote24_blass_combined.tex',
    'sources/texts/api/tapis_de_quillen_162-5_combined.tex',
    'sources/texts/codex/K162-5-01_transcription.tex',
    'sources/texts/codex/K162-5-02_transcription.tex',
    'sources/notes/codex/K162-5-01_notes.md',
    'sources/notes/codex/K162-5-02_notes.md']
coverage={}
for path in assigned:
    if not (B/path).exists():
        matches=[r['path'] for r in reads if Path(r['path']).name==Path(path).name]
        if matches:path=matches[0]
    check((B/path).exists(),'Missing source '+path)
    if not (B/path).exists():continue
    raw=(B/path).read_bytes();n=len(raw.decode().splitlines());seen=set()
    digest=hashlib.sha256(raw).hexdigest()
    for r in reads:
        if r['path']==path:
            check(r['sha256']==digest,'Source changed after reading: '+path)
            seen.update(range(r['first_line'],min(n,r['last_line'])+1))
    missing=sorted(set(range(1,n+1))-seen)
    coverage[path]={'total_lines':n,'logged_lines':len(seen),'missing_lines':missing}
    check(not missing,path+' has reading gaps')

H=P.parent/'hyperplanes'
hclaims={x['id'] for x in json.loads((H/'claims.json').read_text())}
hitems={x['id'] for x in json.loads((H/'items.json').read_text())}
hprobs={x['id'] for x in json.loads((H/'problems.json').read_text())}
hed={x['id'] for x in json.loads((H/'editorial_tasks.json').read_text())}
con=js('cote24_25_concordance.json')['rows']
for r in con:
    s,t={'claim':(ci,hclaims),'item':(ii,hitems),'problem':(pi,hprobs)}[r['kind']]
    check(r['source'] in s,'Concordance missing source '+r['source'])
    check(set(r['targets'])<=t,'Concordance missing targets '+str(set(r['targets'])-t))
for r in js('cote24_25_editorial_associations.json'):
    check(r['source'] in ei|pi,'Editorial association missing source '+r['source'])
    check(set(r['targets'])<=hprobs|hed,'Editorial association missing target')
    check('no MP merge' in r['action'] or 'related target only' in r['action'],'Editorial association must not merge authorial questions')
check(len(js('problem_origin_audit.json'))==len(ps)+len(eds),'Problem provenance count mismatch')

report={'owner':'forms','date':'2026-11-19','status':'PASS' if not errors else 'FAIL',
        'errors':errors,'counts':dict(items=len(its),mathematical_claims=len(cs),
        document_records=len(docs),authorial_problems=len(ps),editorial_tasks=len(eds),
        reading_flags=len(tab('readings.tsv')),links=len(tab('links.tsv')),
        references=len(refs),directions=len(dirs),editorial_directions=len(edirs),computation_blocks=len(computes),
        check_events=len(events),search_records=len(logs),concordance_rows=len(con),
        editorial_associations=len(js('cote24_25_editorial_associations.json'))),
        'claims_by_class':dict(collections.Counter(c['class'] for c in cs)),
        'claims_by_status':dict(collections.Counter(c['status_category'] for c in cs)),
        'claims_by_origin':dict(collections.Counter(c['record_origin'] for c in cs)),
        'reading_coverage':coverage,
        'scope':'Structural and read-coverage checks only. Judgments, hypotheses, fate matches and proofs are manually recorded in the registers and proof_checks.md. Code assertions certify only their stated finite or symbolic scope.'}
(P/'validation.json').write_text(json.dumps(report,ensure_ascii=False,indent=2)+'\n')
print(json.dumps(report,ensure_ascii=False,indent=2))
if errors:raise SystemExit(1)
