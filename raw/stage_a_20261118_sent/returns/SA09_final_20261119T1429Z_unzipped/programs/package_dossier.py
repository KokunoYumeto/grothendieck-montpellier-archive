#!/usr/bin/env python3
"""Create a complete, immutable numbered checkpoint or final SA09 deliverable.

Attached source files and previous ZIPs are not embedded. Bulky downloaded
reference PDFs and full reference text are research inputs, not deliverables;
their opened locators and relevant checked conclusions are retained separately.
"""
import argparse, hashlib, json, zipfile
from datetime import datetime, timezone
from pathlib import Path

ROOT=Path(__file__).resolve().parents[1]
p=argparse.ArgumentParser()
p.add_argument('--name',required=True)
p.add_argument('--destination',default=str(ROOT.parent))
a=p.parse_args()
dest=Path(a.destination)/a.name
if dest.exists():
 raise SystemExit('Refusing to overwrite an existing archive: '+str(dest))
files=[]
for f in sorted(ROOT.rglob('*')):
 if not f.is_file(): continue
 rel=f.relative_to(ROOT)
 if '__pycache__' in rel.parts or f.suffix.lower() in {'.zip','.pyc'}: continue
 if f.suffix.lower()=='.pdf': continue
 if f.name in {'EGAIV3.txt','Schinzel1977.txt','transcription_numbered.txt','entries_source.json'}: continue
 if f.name.startswith('Schinzel1977_page-'): continue
 files.append((f,rel))
manifest=[dict(path=str(r),bytes=f.stat().st_size,sha256=hashlib.sha256(f.read_bytes()).hexdigest()) for f,r in files]
with zipfile.ZipFile(dest,'x',zipfile.ZIP_DEFLATED,compresslevel=9) as z:
 for f,r in files: z.write(f,str(r))
 z.writestr('ARCHIVE_MANIFEST.json',json.dumps(dict(created_utc=datetime.now(timezone.utc).isoformat(),archive=a.name,files=manifest,previous_checkpoints=[x.name for x in sorted(ROOT.parent.glob('SA09_checkpoint_*.zip'))]),ensure_ascii=False,indent=2)+'\n')
with zipfile.ZipFile(dest) as z:
 bad=z.testzip()
 if bad: raise SystemExit('CRC failure: '+bad)
print(json.dumps(dict(path=str(dest),files=len(files)+1,bytes=dest.stat().st_size,sha256=hashlib.sha256(dest.read_bytes()).hexdigest()),indent=2))
