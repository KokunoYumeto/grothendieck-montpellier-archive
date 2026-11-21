from pathlib import Path
from datetime import datetime,timezone
from zoneinfo import ZoneInfo
import argparse,hashlib,json,shutil,zipfile

base=Path(__file__).resolve().parent.parent
parser=argparse.ArgumentParser();parser.add_argument('index',type=int);args=parser.parse_args()
start=datetime(2026,11,21,0,15,36,tzinfo=timezone.utc)
due=start.timestamp()+45*60*args.index
now=datetime.now(timezone.utc)
if now.timestamp()<due: raise SystemExit('Checkpoint is not due; refusing early save')
dest=base/f'K17_checkpoint_{args.index:02d}.zip'
if dest.exists(): raise SystemExit('Refusing to overwrite an earlier checkpoint')
pkg=base/'K17_package'
ev=pkg/'evidence'/'work';ev.mkdir(parents=True,exist_ok=True)
suffixes={'.md','.tsv','.tex','.py','.json','.txt','.lean','.sh','.png','.gap','.csv','.sage','.gp','.jsonl','.cpp','.h','.log'}
excluded={'texcache','library_helpers_current'}
# Keep source hashes and exact citations rather than redistributing complete
# downloaded publications through their extracted text. Earlier ZIPs are immutable.
source_texts={p.with_suffix('.txt') for p in (base/'work').rglob('*.pdf')
              if p.with_suffix('.txt').is_file()}
for p in source_texts:
    staged=ev/p.relative_to(base/'work')
    if staged.is_file(): staged.unlink()
copied=0
for p in (base/'work').rglob('*'):
    rel=p.relative_to(base/'work')
    if not p.is_file() or p in source_texts or p.suffix not in suffixes or any(x in excluded for x in rel.parts): continue
    q=ev/rel;q.parent.mkdir(parents=True,exist_ok=True);shutil.copy2(p,q);copied+=1

pdfmanifest=[]
for p in (base/'work').rglob('*.pdf'):
    row={'path':str(p.relative_to(base)),'bytes':p.stat().st_size,'sha256':hashlib.sha256(p.read_bytes()).hexdigest(),'retrieval':'Primary URL and exact locator in research notes or bibliography; not redistributed wholesale'}
    extracted=p.with_suffix('.txt')
    if extracted.is_file():
        row['extracted_text']={'path':str(extracted.relative_to(base)),'bytes':extracted.stat().st_size,'sha256':hashlib.sha256(extracted.read_bytes()).hexdigest()}
    pdfmanifest.append(row)
(pkg/'evidence'/'PRIMARY_PDF_MANIFEST.json').write_text(json.dumps(pdfmanifest,indent=2))
with (pkg/'LEDGER.md').open('a') as f:
    f.write(f'\n## Timed checkpoint {args.index:02d} — {now.isoformat()}\n\nScheduled interval reached. Creating {dest.name} with all current deliverables, authored research notes, exact computation, proof audits and pinned Lean source evidence. No prior checkpoint is included. This is not a final answer or a scheduled three-hour progress review.\n')
with zipfile.ZipFile(dest,'x',compression=zipfile.ZIP_DEFLATED,compresslevel=6) as z:
    for p in sorted(pkg.rglob('*')):
        if p.is_file() and p.suffix not in {'.aux','.out','.toc'} and (p.suffix!='.log' or 'evidence' in p.relative_to(pkg).parts):
            z.write(p,p.relative_to(pkg))
with zipfile.ZipFile(dest) as z:
    bad=z.testzip()
    if bad: raise SystemExit('Corrupt member '+bad)
    assert all(not n.lower().endswith('.zip') for n in z.namelist())
    assert all(n in z.namelist() for n in ['K17.tex','QUESTIONS.tsv','LEDGER.md','CHECK_EVENTS.tsv','IMPLICATIONS.md','TRANSCRIPTION_NOTES.tsv'])
print(json.dumps({'path':str(dest),'bytes':dest.stat().st_size,'sha256':hashlib.sha256(dest.read_bytes()).hexdigest(),'evidence_files':copied}))
