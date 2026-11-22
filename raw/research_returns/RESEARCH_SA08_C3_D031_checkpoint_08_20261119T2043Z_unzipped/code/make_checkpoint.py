#!/usr/bin/env python3
"""Immutable ZIP snapshot; run only at a scheduled checkpoint or final delivery."""
from pathlib import Path
import argparse,datetime,hashlib,json,zipfile
p=argparse.ArgumentParser();p.add_argument('destination');a=p.parse_args()
root=Path(__file__).resolve().parents[1];dest=Path(a.destination).resolve()
if dest.exists(): raise SystemExit('Refusing to overwrite existing snapshot')
files=sorted(x for x in root.rglob('*') if x.is_file() and x.suffix!='.zip')
# Hash and archive the same byte snapshot, even when another branch finishes
# a working fragment while this scheduled checkpoint is being assembled.
contents=[]
for x in files:
 for attempt in range(5):
  before=x.stat();data=x.read_bytes();after=x.stat()
  if (before.st_size,before.st_mtime_ns)==(after.st_size,after.st_mtime_ns):break
 else:raise SystemExit(f'File kept changing during snapshot: {x}')
 contents.append((str(x.relative_to(root)),data))
manifest=[{'path':name,'bytes':len(data),'sha256':hashlib.sha256(data).hexdigest()} for name,data in contents]
with zipfile.ZipFile(dest,'x',zipfile.ZIP_DEFLATED,compresslevel=6) as z:
 for name,data in contents:z.writestr(name,data)
 z.writestr('CHECKPOINT_CONTENTS.json',json.dumps({'created_utc':datetime.datetime.now(datetime.timezone.utc).isoformat(),'files':manifest},indent=2)+'\n')
assert dest.stat().st_size<500_000_000
print(json.dumps({'destination':str(dest),'files':len(files),'bytes':dest.stat().st_size,'sha256':hashlib.sha256(dest.read_bytes()).hexdigest()}))
