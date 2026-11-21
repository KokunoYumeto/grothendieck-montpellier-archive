from pathlib import Path
from datetime import datetime,timedelta,timezone
import sys,json,zipfile,hashlib,shutil
root=Path('/workspace/scratch/59e0d6e3e1d5')
package=root/'GHOSTS_package'
nn=int(sys.argv[1])
due=datetime(2026,11,21,0,50,tzinfo=timezone.utc)+timedelta(minutes=45*nn)
now=datetime.now(timezone.utc)
if now<due:raise SystemExit('Checkpoint not yet due')
if now>due+timedelta(minutes=3):raise SystemExit('Checkpoint schedule requires review: more than three minutes late')
target=root/f'GHOSTS_checkpoint_{nn:02d}.zip'
if target.exists():raise SystemExit('Refusing to overwrite an earlier checkpoint')
for p in (root/'work/agents').iterdir():
 if p.is_file() and p.suffix in {'.md','.py','.cpp','.out'}:shutil.copy2(p,package/'research'/p.name)
for p in (root/'work').glob('root_*.md'):shutil.copy2(p,package/'research'/p.name)
shutil.copy2(__file__,package/'research'/'make_checkpoint.py')
meta_path=package/'research/RUN_METADATA.json'
meta=json.loads(meta_path.read_text())
meta['last_checkpoint_utc']=now.isoformat()
meta['last_checkpoint_name']=target.name
meta['next_checkpoint_due_utc']=(due+timedelta(minutes=45)).isoformat()
meta_path.write_text(json.dumps(meta,indent=2)+'\n')
with (package/'LEDGER.md').open('a') as f:
 f.write(f'\nCheckpoint{nn:02d} captured at {now.isoformat()}. All current authored deliverables and work documentation are included; no earlier checkpoint ZIP is nested.\n')
excluded={'.aux','.log','.toc','.out','.zip'}
files=[]
for p in sorted(package.rglob('*')):
 if not p.is_file():continue
 if p.name in {'missfont.log','DELIVERABLE_MANIFEST.tsv'}:continue
 if p.suffix in excluded and not (p.parent.name=='research' and p.suffix=='.out'):continue
 if '__pycache__' in p.parts:continue
 files.append(p)
manifest=package/'DELIVERABLE_MANIFEST.tsv'
manifest.write_text('relative_path\tbytes\tsha256\n'+''.join(f'{p.relative_to(package)}\t{p.stat().st_size}\t{hashlib.sha256(p.read_bytes()).hexdigest()}\n' for p in files))
files.append(manifest)
with zipfile.ZipFile(target,'x',compression=zipfile.ZIP_DEFLATED,compresslevel=9) as z:
 for p in files:z.write(p,p.relative_to(package))
with zipfile.ZipFile(target) as z:
 if z.testzip() is not None:raise SystemExit('Archive integrity failed')
print(json.dumps({'file':str(target),'bytes':target.stat().st_size,'entries':len(files),'captured_utc':now.isoformat()}))
