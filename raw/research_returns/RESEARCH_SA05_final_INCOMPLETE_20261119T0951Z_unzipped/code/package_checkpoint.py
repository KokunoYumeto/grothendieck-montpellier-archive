"""Create an immutable research checkpoint and a hash manifest.

Raw sources, supplied files, third-party dependencies and QA renders are excluded.
Every current deliverable and all research notes/programs/output are included.
"""
from pathlib import Path
from zipfile import ZipFile, ZIP_DEFLATED
import hashlib, json, sys, csv
ROOT=Path(__file__).resolve().parents[1]
number=int(sys.argv[1])
name=f'RESEARCH_SA05_checkpoint_{number:02d}.zip'
target=ROOT.parent/name
if target.exists():
    raise SystemExit('Refusing to overwrite an existing checkpoint')
allowed={'.tex','.bib','.md','.csv','.tsv','.json','.jsonl','.py','.gp','.sh','.out','.log'}
files=[]
previous={}
if number>1:
    prior=ROOT.parent/f'RESEARCH_SA05_checkpoint_{number-1:02d}.zip'
    if not prior.exists(): raise SystemExit('Previous checkpoint is required for delta manifest')
    with ZipFile(prior) as z:
        previous={r['path']:r for r in csv.DictReader(z.read('CHECKPOINT_FILE_LIST.tsv').decode().splitlines(),delimiter='\t')}
for f in sorted(ROOT.rglob('*')):
    if not f.is_file(): continue
    rel=f.relative_to(ROOT)
    if any(x in rel.parts for x in ['sources','texdeps','texcache','qa','__pycache__']):continue
    if rel.parts[0]=='build':
        if f.name not in ['RESEARCH_SA05_paper.log','RESEARCH_SA05_paper.bbl','texcompat.lua'] and not f.name.startswith('build_step_'):continue
    elif f.name=='RESEARCH_SA05_paper.pdf':pass
    elif f.suffix=='.txt' and any(x in rel.parts for x in ['code','output']):pass
    elif f.suffix not in allowed:continue
    if f.name=='CHECKPOINT_FILE_LIST.tsv':continue
    files.append(f)
manifest=ROOT/'CHECKPOINT_FILE_LIST.tsv'
included=[]
with manifest.open('w',newline='') as out:
    w=csv.writer(out,delimiter='\t');w.writerow(['path','bytes','sha256','contained_in'])
    for f in files:
        rel=str(f.relative_to(ROOT));b=f.read_bytes();digest=hashlib.sha256(b).hexdigest()
        mandatory=(f.suffix in {'.tex','.bib','.md','.csv','.tsv','.py','.gp','.sh'} or f.name=='RESEARCH_SA05_paper.pdf')
        old=previous.get(rel)
        if mandatory or old is None or old['sha256']!=digest:
            included.append(f);where=name
        else:where=old['contained_in']
        w.writerow([rel,len(b),digest,where])
with ZipFile(target,'x',ZIP_DEFLATED,compresslevel=6) as z:
    for f in included+[manifest]:z.write(f,str(f.relative_to(ROOT)))
assert target.stat().st_size<500_000_000
with ZipFile(target) as z: assert z.testzip() is None
print(json.dumps({'path':str(target),'bytes':target.stat().st_size,'files':len(included)+1,'unchanged_referenced':len(files)-len(included)},indent=2))
