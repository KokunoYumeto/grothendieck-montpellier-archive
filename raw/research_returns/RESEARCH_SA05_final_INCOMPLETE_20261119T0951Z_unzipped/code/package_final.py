"""Package the final current deliverables only after the stopping rule is met.

The file manifest references the last successful checkpoint for unchanged
non-deliverable outputs. Earlier ZIPs and raw sources are never embedded.
"""
from pathlib import Path
from zipfile import ZipFile, ZIP_DEFLATED
from datetime import datetime, timezone
import hashlib
import json
import csv
from contextlib import ExitStack

root=Path(__file__).resolve().parents[1]
review_path=root/'progress/review_05.json'
if not review_path.exists():
    raise SystemExit('The fifth scheduled review must actually take place first.')
review=json.loads(review_path.read_text())
if review.get('consecutive_reviews_without_movement',0)<2:
    raise SystemExit('The user stopping threshold has not been reached.')
if review.get('movement'):
    raise SystemExit('A movement review cannot trigger this final package.')
prior=root.parent/'RESEARCH_SA05_checkpoint_09.zip'
if not prior.exists():
    raise SystemExit('Checkpoint09 is required for the final delta manifest.')
name='RESEARCH_SA05_final_INCOMPLETE.zip'
target=root.parent/name
if target.exists():
    raise SystemExit('Refusing to overwrite a final archive.')
with ZipFile(prior) as z:
    previous={r['path']:r for r in csv.DictReader(
        z.read('CHECKPOINT_FILE_LIST.tsv').decode().splitlines(),delimiter='\t')}
allowed={'.tex','.bib','.md','.csv','.tsv','.json','.jsonl','.py','.gp','.sh','.out','.log'}
files=[]
for f in sorted(root.rglob('*')):
    if not f.is_file():continue
    rel=f.relative_to(root)
    if any(x in rel.parts for x in ['sources','texdeps','texcache','qa','__pycache__']):continue
    if rel.parts[0]=='build':
        if f.name not in ['RESEARCH_SA05_paper.log','RESEARCH_SA05_paper.bbl','texcompat.lua'] and not f.name.startswith('build_step_'):continue
    elif f.name=='RESEARCH_SA05_paper.pdf':pass
    elif f.suffix=='.txt' and any(x in rel.parts for x in ['code','output']):pass
    elif f.suffix not in allowed:continue
    if f.name in ['CHECKPOINT_FILE_LIST.tsv','FINAL_FILE_LIST.tsv']:continue
    files.append(f)
manifest=root/'FINAL_FILE_LIST.tsv'
included=[]
with manifest.open('w',newline='') as out:
    w=csv.writer(out,delimiter='\t')
    w.writerow(['path','bytes','sha256','contained_in'])
    for f in files:
        rel=str(f.relative_to(root));data=f.read_bytes()
        digest=hashlib.sha256(data).hexdigest()
        mandatory=(f.suffix in {'.tex','.bib','.md','.csv','.tsv','.py','.gp','.sh'}
                   or f.name=='RESEARCH_SA05_paper.pdf')
        old=previous.get(rel)
        if mandatory or old is None or old['sha256']!=digest:
            included.append(f);where=name
        else:where=old['contained_in']
        w.writerow([rel,len(data),digest,where])
with ZipFile(target,'x',ZIP_DEFLATED,compresslevel=6) as z:
    for f in included+[manifest]:z.write(f,str(f.relative_to(root)))
assert target.stat().st_size<500_000_000
with ZipFile(target) as z:
    assert z.testzip() is None
    names=set(z.namelist())
    for required in ['RESEARCH_SA05_paper.tex','RESEARCH_SA05_paper.pdf',
                     'RESEARCH_SA05_results.csv','RESEARCH_SA05_references.bib',
                     'RESEARCH_SA05_report.md','CHECK_EVENTS.tsv','PROGRESS_LEDGER.md',
                     'progress/review_05.json','FINAL_FILE_LIST.tsv']:
        assert required in names,required
with ExitStack() as stack:
    archives={name:stack.enter_context(ZipFile(target))}
    with manifest.open(newline='') as f:
        final_rows=list(csv.DictReader(f,delimiter='\t'))
    for row in final_rows:
        container=row['contained_in']
        if container not in archives:
            older=root.parent/container
            assert older.is_file(),f'Missing referenced checkpoint: {container}'
            archives[container]=stack.enter_context(ZipFile(older))
        data=archives[container].read(row['path'])
        assert len(data)==int(row['bytes']),row['path']
        assert hashlib.sha256(data).hexdigest()==row['sha256'],row['path']
print(json.dumps(dict(path=str(target),bytes=target.stat().st_size,
    files=len(included)+1,unchanged_referenced=len(files)-len(included),
    all_manifest_references_verified=True,
    packaged_utc=datetime.now(timezone.utc).isoformat(),status='INCOMPLETE'),indent=2))
