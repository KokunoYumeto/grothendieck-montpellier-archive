"""Bounded validation of approved ega/analysis problem provenance application.

Checks provenance partitions, literal quotation, references, narrative IDs and
idempotence of the three final overlays. It never runs the dossier finalizer or
changes other owners. No mathematical assessment is inferred here.
"""
from pathlib import Path
import json,re,hashlib,subprocess,sys,csv

W=Path(__file__).resolve().parents[1]
ROOT=W.parent
sys.path.insert(0,str(W/'integration'))
from id_rewrite_helper import expand_compact_ids
errors=[];checks=[]
def check(ok,label,detail=None):
    checks.append({'check':label,'passed':bool(ok),'detail':detail})
    if not ok:errors.append(label)
def load(p):return json.loads(p.read_text())
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
parts=[W/'parts'/x for x in ['ega','analysis_curves']]
allids=set();oldids=set();edredirects={};counts={}
for p in parts:
    old=load(p/'provenance/pre_origin_audit/problems.json')
    ps=load(p/'problems.json');eds=load(p/'editorial_tasks.json')
    ds=load(p/'directions.json');editorialds=load(p/'editorial_directions.json')
    olds={x['id'] for x in old};pids={x['id'] for x in ps};eids={x['id'] for x in eds}
    whole={x['original_id'] for x in eds if 'original_id' in x}
    partial=[x for x in eds if 'source_problem_id' in x]
    check(olds==(pids&olds)|whole,p.name+' exact original-problem partition')
    check(not (pids&whole),p.name+' no whole redirect remains in MP')
    check(all(x['source_problem_id'] in pids and 'original_id' not in x for x in partial),p.name+' partial split origins')
    check(all(x.get('source_records',[{}])[0].get('id') in olds for x in ps+eds if x['id']!='MP-SA23-ega-60'),p.name+' original records preserved')
    check(all(x.get('source_cue') and x.get('why_open') and x.get('worth') for x in ps+eds),p.name+' all problem/task explanations present')
    caveat='No external source read in this run documents a biographical reason for abandonment'
    check(all(x['why_open'].count(caveat)<=1 for x in ps+eds),p.name+' no repeated boilerplate in live explanations')
    check(all(x.get('count_as_authorial_mathematical_problem') is True for x in ps),p.name+' MP provenance labels')
    check(all(x.get('count_as_authorial_mathematical_problem') is False for x in eds),p.name+' ED provenance labels')
    original_ds={x['id'] for x in load(p/'provenance/pre_origin_audit/directions.json')}
    check({x['id'] for x in ds+editorialds}==original_ds,p.name+' all original directions preserved')
    check(not ({x['id'] for x in ds}&{x['id'] for x in editorialds}),p.name+' direction partition disjoint')
    check([x['rank'] for x in ds]==list(range(1,len(ds)+1)),p.name+' Stage6 ranks dense')
    check(all(x['problems'] and set(x['problems'])<=pids and set(x['editorial_tasks'])<=eids for x in ds),p.name+' Stage6 exact MP/ED dependencies')
    check(all(not x['problems'] and set(x['editorial_tasks'])<=eids and x['stage6_eligible'] is False for x in editorialds),p.name+' editorial directions excluded from Stage6')
    oldids|=olds;allids|=pids|eids
    edredirects.update({x['original_id']:x['id'] for x in eds if 'original_id' in x})
    counts[p.name]={'problems':len(ps),'editorial_tasks':len(eds),'whole_redirects':len(whole),'partial_splits':len(partial),'directions':len(ds),'editorial_directions':len(editorialds)}
check(len(oldids)==81,'all81 original problem IDs covered')
check(len(edredirects)==31,'31 whole redirects retained')
check(sum(c['partial_splits'] for c in counts.values())==18,'18 partial editorial contexts retained')
for p in parts:
    for name in ['section.md','directions.md','editorial_directions.md']:
        text=(p/name).read_text()
        found=set(re.findall(r'(?:MP|ED)-SA23-(?:ega|analysis_curves)-\d{2}(?:-context)?',text))
        check(found<=allids,p.name+'/'+name+' no dangling live MP/ED IDs',sorted(found-allids))
        expanded,events=expand_compact_ids(text,oldids|allids,kinds=('problem',),with_events=True)
        check(not events,p.name+'/'+name+' no unexpanded registered problem tails',events)

ega=parts[0]
c=next(x for x in load(ega/'claims.json') if x['id']=='C-SA23-ega-098')
p=next(x for x in load(ega/'problems.json') if x['id']=='MP-SA23-ega-60')
literal=(ROOT/'sources/texts/codex/K23-03_transcription.tex').read_text().splitlines()[235]
check(c['his_statement']==literal and c['his_words']==literal,'recovered claim exact diplomatic source line')
check(p['source_cue_literal']==[literal] and p['source_cue']==literal,'recovered problem exact diplomatic source cue')
check(c['class']=='B' and c['classification']=='B','classB relative to Grothendieck, Deligne attribution retained')
check(c['confidence']=='medium' and bool(c['confidence_detail']),'canonical medium confidence plus detailed qualification')
check(c['status_category']=='open on the pages','deferred proof request page status')
check(c['items']==['SA23-1321'] and p['claims']==[c['id']],'recovered request exact subject/claim/problem chain')
check('17October1966' in c['author'] and 'Pierre Deligne' in c['author'],'recovered letter authorship/date')
for n,loc in {91:'317–318',94:'337–338',95:'342–343',96:'347'}.items():
    cc=next(x for x in load(ega/'claims.json') if x['id']==f'C-SA23-ega-{n:03}')
    check(cc['lines']==loc and 'locator_before_origin_audit' in cc,f'cote26 C{n:03} corrected locator preserved with old locator')

# These five author names and matches were manually checked; the loop only
# validates serialization of those decisions, not authorship inference.
for owner, numbers, author in [('ega',[49],'Pierre Berthelot'),('analysis_curves',[13,15,18,19],'Michèle Raynaud')]:
    claim_map={int(x['id'].rsplit('-',1)[1]):x for x in load(W/'parts'/owner/'claims.json')}
    for number in numbers:
        claim=claim_map[number]
        audit=claim.get('publication_authorship_audit',{})
        check(claim['class']==claim['classification']=='B' and audit.get('matched_publication_author')==author,
              claim['id']+' checked other-author publication is classB')

# Repeat only the final, bounded overlays. Unchanged hashes demonstrate that
# source_records, explanation text, events and direction partitions do not grow.
names=['claims.json','items.json','problems.json','editorial_tasks.json','directions.json','editorial_directions.json','section.md','coverage.md','directions.md','editorial_directions.md','references.bib','check_events.tsv','search_log.jsonl','entries.tsv','links.tsv']
paths=[p/n for p in parts for n in names]
before={str(p.relative_to(W)):sha(p) for p in paths}
commands=[]
for script in [ega/'add_lefschetz_request.py',ega/'apply_publication_authorship_audit.py',ega/'apply_problem_origin_audit.py']:
    out=subprocess.run([sys.executable,str(script)],cwd=ROOT,text=True,capture_output=True)
    commands.append({'script':str(script.relative_to(W)),'returncode':out.returncode,'stdout':out.stdout,'stderr':out.stderr})
    check(out.returncode==0,'overlay rerun '+script.name)
after={str(p.relative_to(W)):sha(p) for p in paths}
changed=[p for p in before if before[p]!=after[p]]
check(not changed,'final overlays idempotent for live registers/narratives/evidence',changed)

report={'date':'2026-11-19','checks':checks,'errors':errors,'counts':counts,'overlay_commands':commands,
        'idempotence_changed_paths':changed,'finalizer_executed':False,'other_owner_files_mutated':False,
        'editorial_direction_paths':['parts/ega/editorial_directions.json','parts/analysis_curves/editorial_directions.json']}
(W/'integration/ega_origin_validation.json').write_text(json.dumps(report,ensure_ascii=False,indent=2)+'\n')
print(json.dumps({'checks':len(checks),'errors':errors,'counts':counts,'idempotence_changed_paths':changed},indent=2))
raise SystemExit(bool(errors))
