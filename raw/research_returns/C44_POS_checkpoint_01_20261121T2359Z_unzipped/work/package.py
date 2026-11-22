from pathlib import Path
import datetime
import hashlib
import json
import sys
import zipfile

root=Path(__file__).resolve().parents[1]
mode=sys.argv[1] if len(sys.argv)>1 else 'status'
start=datetime.datetime.fromisoformat((root/'work/started_at.txt').read_text().strip())
now=datetime.datetime.now(datetime.timezone.utc)
elapsed=(now-start).total_seconds()
prior=sorted(root.glob('C44_POS_checkpoint_*.zip'))
number=len(prior)+1
due=start+datetime.timedelta(minutes=45*number)
if mode=='status':
    print(json.dumps({'elapsed_minutes':elapsed/60,'next_number':number,'next_due_utc':due.isoformat(),'due':now>=due}))
    raise SystemExit(0)
if mode=='checkpoint':
    if now<due:
        raise SystemExit('Checkpoint not yet due; no ZIP created.')
    name=f'C44_POS_checkpoint_{number:02}.zip'
elif mode=='final':
    name='C44_POS_final.zip'
else:
    raise SystemExit('Mode must be status, checkpoint, or final.')
dest=root/name
if dest.exists():
    raise SystemExit('Refusing to overwrite an existing package.')
stamp=now.astimezone(datetime.timezone(datetime.timedelta(hours=1))).isoformat()
if mode=='checkpoint':
    with (root/'deliverables/LEDGER.md').open('a') as f:
        f.write(f'\n## Checkpoint {number:02}\n\nCreated {name} at {stamp}, after {elapsed/60:.2f} minutes of elapsed work. Scheduled due time: {due.isoformat()} UTC. The ZIP contains current deliverables and work documentation, and no previous ZIP. Durable-save outcome is recorded in the next ledger update. This is not a scheduled gate review.\n')
files=[]
for p in sorted((root/'deliverables').rglob('*')):
    if p.is_file(): files.append((p,p.relative_to(root/'deliverables').as_posix()))
for p in sorted((root/'work').rglob('*')):
    if not p.is_file(): continue
    rel=p.relative_to(root)
    if any(x in rel.parts for x in ['library_helpers_current','texformat','__pycache__','private']): continue
    if p.suffix in ['.zip','.fmt','.pdf','.aux','.toc','.out']: continue
    files.append((p,rel.as_posix()))
manifest={'created_at':stamp,'mode':mode,'elapsed_minutes':elapsed/60,
          'files':[{'path':n,'bytes':p.stat().st_size,'sha256':hashlib.sha256(p.read_bytes()).hexdigest()} for p,n in files]}
with zipfile.ZipFile(dest,'x',compression=zipfile.ZIP_DEFLATED,compresslevel=9) as z:
    for p,n in files: z.write(p,n)
    z.writestr('PACKAGE_MANIFEST.json',json.dumps(manifest,indent=2)+'\n')
with zipfile.ZipFile(dest) as z:
    bad=z.testzip()
    if bad: raise RuntimeError('Archive CRC error: '+bad)
    if any(n.endswith('.zip') for n in z.namelist()): raise RuntimeError('Nested ZIP forbidden')
print(json.dumps({'path':str(dest),'bytes':dest.stat().st_size,'files':len(files)+1,'created_at':stamp,'elapsed_minutes':elapsed/60}))
