#!/usr/bin/env python3
"""Create a complete immutable checkpoint at its scheduled time."""
from pathlib import Path
from datetime import datetime, timezone, timedelta
import argparse, hashlib, json, zipfile
ROOT=Path(__file__).resolve().parents[1]
p=argparse.ArgumentParser();p.add_argument('number',type=int);args=p.parse_args()
start=datetime(2026,11,21,23,14,tzinfo=timezone.utc)
due=start+timedelta(minutes=45*args.number)
now=datetime.now(timezone.utc)
if now<due: raise SystemExit('Checkpoint is not due yet: '+due.isoformat())
dest=ROOT/f'ARCH_ALG_checkpoint_{args.number:02d}.zip'
if dest.exists(): raise SystemExit('Refusing to overwrite existing checkpoint '+str(dest))
source=ROOT/'deliverable'
manifest=[]
for f in sorted(source.rglob('*')):
 if f.is_file():
  if f.suffix.lower()=='.zip': raise SystemExit('Nested ZIP forbidden: '+str(f))
  manifest.append({'path':str(f.relative_to(source)),'bytes':f.stat().st_size,'sha256':hashlib.sha256(f.read_bytes()).hexdigest()})
with zipfile.ZipFile(dest,'x',compression=zipfile.ZIP_DEFLATED,compresslevel=9) as z:
 for item in manifest:z.write(source/item['path'],item['path'])
 z.writestr('CHECKPOINT_MANIFEST.json',json.dumps({'number':args.number,'due':due.isoformat(),'created':now.isoformat(),'files':manifest},indent=2))
with zipfile.ZipFile(dest) as z:
 bad=z.testzip()
 if bad:raise SystemExit('ZIP integrity failure '+bad)
print(json.dumps({'path':str(dest),'bytes':dest.stat().st_size,'sha256':hashlib.sha256(dest.read_bytes()).hexdigest(),'members':len(manifest)+1,'created':now.isoformat()}))
