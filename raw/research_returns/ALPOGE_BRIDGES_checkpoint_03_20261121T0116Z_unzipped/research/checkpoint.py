"""Create a complete, non-overwriting timed checkpoint of original work.
Downloaded reference books/articles and original supplied attachments are caches,
available by their documented URLs and the original packet; they are not republished.
"""
from pathlib import Path
import datetime, hashlib, json, sys, zipfile
root=Path(__file__).resolve().parents[1]
start=datetime.datetime.fromisoformat((root/'research/RUN_START.txt').read_text().strip())
now=datetime.datetime.now(datetime.timezone.utc)
n=int(sys.argv[1]);elapsed=(now-start).total_seconds()
if elapsed < 2700*n:
    raise SystemExit(f'Not due: elapsed={elapsed:.1f}, due={2700*n}')
out=root.parent/f'ALPOGE_BRIDGES_checkpoint_{n:02d}.zip'
if out.exists():raise SystemExit('Refusing to overwrite checkpoint')
files=[]
for p in (root/'deliverables').iterdir():
    if p.suffix in {'.tex','.tsv','.md'}:files.append(p)
    if p.suffix=='.pdf' and (root/'research/PDF_QA_COMPLETE.txt').exists():files.append(p)
for p in (root/'research').rglob('*'):
    if not p.is_file():continue
    own_outputs={'RUN_START.txt','source_checks_computation_output.txt','aq_symbolic_checks_output.txt','CC-F03_arithmetic_check.txt','consequences_criteria_apposition_finite_checks.txt','PDF_QA_COMPLETE.txt'}
    if p.suffix in {'.md','.tex','.tsv','.py'} or p.name in own_outputs or (p.suffix=='.log' and p.parent.name=='tex_build'):
        files.append(p)
files=sorted(set(files))
manifest=[]
with zipfile.ZipFile(out,'x',zipfile.ZIP_DEFLATED,compresslevel=6) as z:
    for p in files:
        rel=p.relative_to(root).as_posix();data=p.read_bytes()
        # Five final deliverable names are at ZIP root; supporting documents retain research/.
        arc=p.name if p.parent.name=='deliverables' else rel
        z.writestr(arc,data)
        manifest.append((arc,len(data),hashlib.sha256(data).hexdigest()))
    z.writestr('CHECKPOINT_MANIFEST.tsv','path\tsize_bytes\tsha256\n'+''.join(f'{a}\t{b}\t{c}\n' for a,b,c in manifest))
    z.writestr('CHECKPOINT_STATUS.md',f'''# Checkpoint {n:02d}

Created {now.isoformat()}; elapsed work {elapsed/60:.3f} minutes.
This is an ongoing work snapshot, not the final package.
The five current deliverables and every original research module, source note,
proof/check register and reproducibility script written so far are included.
The source packet remains the attachment supplied with the task. Downloaded
third-party reference PDFs and verbatim text-extraction caches are not republished;
their locators are in the source notes and bibliography. No earlier checkpoint is included.
No successful rendered-PDF verification is claimed unless PDF_QA_COMPLETE is present.

The first movement review is due after three hours from {start.isoformat()},
then hourly; two consecutive no-movement reviews trigger the requested stop.
Checkpoint timing remains every45elapsed minutes, with new sequential names.
''')
print(json.dumps({'path':str(out),'files':len(files),'bytes':out.stat().st_size,'elapsed_seconds':elapsed}))
