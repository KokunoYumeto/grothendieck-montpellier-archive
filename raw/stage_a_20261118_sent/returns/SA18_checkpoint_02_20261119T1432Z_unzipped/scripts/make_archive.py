"""Create immutable complete work snapshots or the final deliverable archive."""
from pathlib import Path
from datetime import datetime, timezone, timedelta
import argparse, json, zipfile, hashlib

ROOT = Path(__file__).resolve().parents[1]
START = datetime.fromisoformat('2026-11-19T13:02:45.988797+00:00')
p = argparse.ArgumentParser()
p.add_argument('--checkpoint', type=int)
p.add_argument('--final', action='store_true')
a = p.parse_args()
assert bool(a.checkpoint) != a.final
now = datetime.now(timezone.utc)
name = 'SA18.zip' if a.final else f'SA18_checkpoint_{a.checkpoint:02d}.zip'
out = ROOT.parent / name
assert not out.exists(), f'Refusing to replace {out}'
due = None if a.final else START + timedelta(minutes=45*a.checkpoint)
if due and now < due:
    raise SystemExit(f'Checkpoint not due until {due.isoformat()}')
with (ROOT/'progress.log').open('a') as f:
    f.write(f'{now.isoformat()}\t'+('FINAL ARCHIVE' if a.final else f'CHECKPOINT {a.checkpoint:02d}; scheduled {due.isoformat()}')+'\n')
paths = sorted(x for x in ROOT.rglob('*') if x.is_file() and '__pycache__' not in x.parts and x.suffix not in {'.zip','.pyc'})
manifest = {'created_utc':now.isoformat(),'name':name,'scheduled_utc':due.isoformat() if due else None,
            'earlier_checkpoints_required':[], 'restore':'Unzip this complete snapshot and the original user attachment; source inputs and public-source PDFs are deliberately not duplicated.',
            'files':[{'path':str(x.relative_to(ROOT)),'bytes':x.stat().st_size,'sha256':hashlib.sha256(x.read_bytes()).hexdigest()} for x in paths]}
with zipfile.ZipFile(out,'x',zipfile.ZIP_DEFLATED,compresslevel=6) as z:
    for x in paths: z.write(x,str(x.relative_to(ROOT)))
    z.writestr('ARCHIVE_MANIFEST.json',json.dumps(manifest,indent=2))
print(json.dumps({'path':str(out),'bytes':out.stat().st_size,'files':len(paths),'created_utc':now.isoformat(),'scheduled_utc':manifest['scheduled_utc']}))
