#!/usr/bin/env python3
"""Create only a scheduled 45-minute checkpoint; never overwrite an archive."""
from pathlib import Path
from datetime import datetime, timezone, timedelta
import argparse, json, zipfile, hashlib
p=argparse.ArgumentParser();p.add_argument('--now',required=True);a=p.parse_args()
now=datetime.strptime(a.now,'%Y-%m-%d %H:%M:%S UTC').replace(tzinfo=timezone.utc)
base=datetime(2026,11,19,13,1,52,tzinfo=timezone.utc)
root=Path(__file__).resolve().parents[2]; work=root/'SA14_work'
elapsed=(now-base).total_seconds(); number=int(elapsed//2700)
if number<1: raise SystemExit('No scheduled checkpoint due yet.')
dest=root/f'SA14_checkpoint_{number:02d}.zip'
if dest.exists(): raise SystemExit('Existing checkpoint is immutable: '+str(dest))
previous=sorted(x.name for x in root.glob('SA14_checkpoint_*.zip'))
manifest={'checkpoint':number,'due_utc':(base+timedelta(minutes=45*number)).strftime('%Y-%m-%d %H:%M:%S UTC'),'created_utc':a.now,'prior_checkpoints':previous,'excluded':'Original attached files, extracted source inputs, and earlier checkpoints.','files':[]}
files=[x for x in work.rglob('*') if x.is_file() and '__pycache__' not in x.parts and x.suffix!='.zip']
for path in sorted(files):
 manifest['files'].append({'path':str(path.relative_to(root)),'bytes':path.stat().st_size,'sha256':hashlib.sha256(path.read_bytes()).hexdigest()})
manifest_path=work/'research'/f'checkpoint_{number:02d}_manifest.json'
manifest_path.write_text(json.dumps(manifest,ensure_ascii=False,indent=2)+'\n')
with zipfile.ZipFile(dest,'x',compression=zipfile.ZIP_DEFLATED,compresslevel=6) as z:
 for path in sorted(files): z.write(path,path.relative_to(root))
 z.write(manifest_path,manifest_path.relative_to(root))
print(json.dumps({'path':str(dest),'files':len(files)+1,'bytes':dest.stat().st_size,'created_utc':a.now}))
