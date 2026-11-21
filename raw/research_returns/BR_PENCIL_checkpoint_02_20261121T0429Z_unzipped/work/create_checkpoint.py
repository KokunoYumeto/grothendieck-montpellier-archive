"""Create an immutable full scheduled checkpoint. Never includes earlier ZIPs."""
from pathlib import Path
import datetime,hashlib,json,time,zipfile,csv
root=Path(__file__).resolve().parent.parent
start=datetime.datetime(2026,11,21,2,59,26,tzinfo=datetime.timezone.utc)
now=datetime.datetime.now(datetime.timezone.utc)
number=int((now-start).total_seconds()//2700)
if number<1:raise SystemExit('Not yet the first45-minute checkpoint time.')
due=start+datetime.timedelta(minutes=45*number)
if (now-due).total_seconds()>120:raise SystemExit('Outside the scheduled checkpoint window; do not make an off-cadence checkpoint.')
name=f'BR_PENCIL_checkpoint_{number:02d}.zip';target=root/name
if target.exists():raise SystemExit('Immutable checkpoint already exists; refusing to overwrite.')
context=f'''# Checkpoint {number:02d}: continuing research

Created {now.isoformat()}. Checkpoints are scheduled every45minutes
from {start.isoformat()}. The next is due
{(due+datetime.timedelta(minutes=45)).isoformat()}.
The first progress review is due2026-11-21T05:59:26Z, then hourly.
Two consecutive reviews without mathematical movement stop that work.
The current review state is recorded in LEDGER.md.

{(root/'work'/'CHECKPOINT_STATUS.md').read_text()}
'''
(root/'deliverable'/'CHECKPOINT_CONTEXT.md').write_text(context)
files=[]
# Main deliverables live at the archive root; ongoing research under work/.
for p in sorted((root/'deliverable').rglob('*')):
 if p.is_file() and p.suffix not in {'.aux','.log','.out','.toc'}:
  files.append((p,str(p.relative_to(root/'deliverable'))))
for p in sorted((root/'work').rglob('*')):
 if not p.is_file():continue
 rel=p.relative_to(root)
 if 'references' in rel.parts or '__pycache__' in rel.parts:continue
 if p.suffix in {'.fmt','.aux','.log','.out','.toc','.pyc'}:continue
 if p.name=='library_helper_path.txt':continue
 files.append((p,str(rel)))
files.append((root/'upload'/'PROMPT(20261121-025850).md','intake/BR_PENCIL_PROMPT.md'))
manifest=[]
with zipfile.ZipFile(target,'x',compression=zipfile.ZIP_DEFLATED,compresslevel=6) as z:
 for path,arc in files:
  assert not arc.lower().endswith('.zip')
  for attempt in range(8):
   before=path.stat();content=path.read_bytes();after=path.stat()
   if (before.st_size,before.st_mtime_ns)==(after.st_size,after.st_mtime_ns) and len(content)==after.st_size:break
   time.sleep(.05)
  else:raise RuntimeError(f'File changed repeatedly during snapshot:{path}')
  z.writestr(arc,content)
  manifest.append({'path':arc,'bytes':len(content),'sha256':hashlib.sha256(content).hexdigest()})
 z.writestr('CHECKPOINT_MANIFEST.json',json.dumps({'checkpoint':name,'date_utc':now.isoformat(),'scheduled_due':due.isoformat(),'files':manifest},indent=2)+'\n')
with zipfile.ZipFile(target) as z:
 assert z.testzip() is None
 assert {'BR_PENCIL.tex','QUESTIONS.tsv','CHECK_EVENTS.tsv','LEDGER.md','IMPLICATIONS.md'}<=set(z.namelist())
print(json.dumps({'checkpoint':str(target),'bytes':target.stat().st_size,'files':len(manifest),'sha256':hashlib.sha256(target.read_bytes()).hexdigest(),'date_utc':now.isoformat()}))
