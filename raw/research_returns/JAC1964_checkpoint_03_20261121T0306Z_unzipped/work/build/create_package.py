"""Create an immutable, scheduled, complete JAC1964 ZIP.

Only the final package or the next numbered 45-minute checkpoint is allowed.
External research PDFs, source OCR, input archives, caches and previous ZIPs
are excluded. Authored proofs, audits, calculations and current outputs stay.
"""
from pathlib import Path
from datetime import datetime, timezone, timedelta
import argparse, hashlib, json, time, zipfile

ROOT=Path(__file__).resolve().parents[2]
START=datetime(2026,11,21,0,51,37,tzinfo=timezone.utc)
parser=argparse.ArgumentParser()
choice=parser.add_mutually_exclusive_group(required=True)
choice.add_argument('--checkpoint',type=int)
choice.add_argument('--final',action='store_true')
parser.add_argument('--wait',action='store_true')
args=parser.parse_args()
now=datetime.now(timezone.utc)
if args.checkpoint:
    n=args.checkpoint
    if n<1:raise SystemExit('Checkpoint number must be positive.')
    for i in range(1,n):
        if not (ROOT/f'JAC1964_checkpoint_{i:02d}.zip').exists():
            raise SystemExit(f'Missing earlier local checkpoint {i}; restore schedule state first.')
    due=START+timedelta(minutes=45*n)
    if now<due and not args.wait:raise SystemExit(f'Not due until {due.isoformat()}')
    while datetime.now(timezone.utc)<due:
        time.sleep(min(30,max(0.01,(due-datetime.now(timezone.utc)).total_seconds())))
    if datetime.now(timezone.utc)>=due+timedelta(minutes=45):
        raise SystemExit('Missed interval: do not create an extra checkpoint; inspect the ledger.')
    name=f'JAC1964_checkpoint_{n:02d}.zip'
else:
    due=None
    name='JAC1964_final.zip'
target=ROOT/name
if target.exists():raise SystemExit(f'Refusing to overwrite {target.name}')
created=datetime.now(timezone.utc)
mandatory=['JAC1964.tex','QUESTIONS.tsv','LEDGER.md','CHECK_EVENTS.tsv','IMPLICATIONS.md','TRANSCRIPTION_NOTES.tsv']
for item in mandatory:
    if not (ROOT/'deliverables'/item).is_file():raise SystemExit(f'Missing {item}')

selected={}
for p in (ROOT/'deliverables').iterdir():
    if p.suffix in {'.tex','.pdf','.tsv','.md'}:selected[p.name]=p
for p in (ROOT/'documentation').rglob('*'):
    if p.is_file() and p.suffix in {'.md','.tsv','.json','.txt'}:
        selected[p.relative_to(ROOT).as_posix()]=p
for folder in ['root','h9','arithmetic','programme','build']:
    for p in (ROOT/'work'/folder).rglob('*'):
        if not p.is_file():continue
        allowed=p.suffix in {'.md','.tex','.py','.json','.jsonl','.tsv','.sh'}
        if p.name.endswith('_output.txt'):allowed=True
        if 'visual_qa' in p.parts and p.suffix in {'.png','.txt'}:allowed=True
        if allowed:selected[p.relative_to(ROOT).as_posix()]=p
log=ROOT/'deliverables/JAC1964.compile.txt'
if log.exists():selected['documentation/latex_compile.txt']=log

def read_stable(p):
    for attempt in range(4):
        before=p.stat(); data=p.read_bytes(); after=p.stat()
        if (before.st_size,before.st_mtime_ns)==(after.st_size,after.st_mtime_ns):return data
        time.sleep(.05)
    raise RuntimeError(f'File changed during snapshot: {p}')

payload={name:read_stable(p) for name,p in sorted(selected.items())}
manifest=''.join(f'{hashlib.sha256(data).hexdigest()}  {name}\n' for name,data in payload.items())
meta={
    'run':'JAC1964-20261121','package':target.name,'created_utc':created.isoformat(),
    'scheduled_utc':due.isoformat() if due else None,'started_utc':START.isoformat(),
    'kind':'checkpoint' if args.checkpoint else 'final','checkpoint_number':args.checkpoint,
    'content_files':len(payload),'no_previous_zip_nested':True,
    'source_policy':'Authored deliverables and documentation; external full research papers and OCR omitted; exact source locators retained.',
    'next_review_utc':'2026-11-21T03:51:37+00:00',
}
with zipfile.ZipFile(target,'x',compression=zipfile.ZIP_DEFLATED,compresslevel=9) as z:
    for name,data in payload.items():z.writestr(name,data)
    z.writestr('MANIFEST.sha256',manifest)
    z.writestr('PACKAGE.json',json.dumps(meta,indent=2)+'\n')
with zipfile.ZipFile(target) as z:
    if z.testzip() is not None:raise RuntimeError('ZIP CRC check failed')
result=dict(meta,path=str(target),size_bytes=target.stat().st_size,sha256=hashlib.sha256(target.read_bytes()).hexdigest())
print(json.dumps(result,indent=2),flush=True)
