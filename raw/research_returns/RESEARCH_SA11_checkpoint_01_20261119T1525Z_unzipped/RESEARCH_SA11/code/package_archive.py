#!/usr/bin/env python3
"""Immutable research archive with checksums; never nests earlier archives."""
from pathlib import Path
import hashlib, zipfile, json, sys, datetime
root=Path(__file__).resolve().parent.parent
name=sys.argv[1]
if not name.startswith('RESEARCH_SA11_') or not name.endswith('.zip'):
    raise SystemExit('Expected an explicit research archive name')
dest=root.parent/name
if dest.exists(): raise SystemExit('Refusing to overwrite an existing archive')
files=sorted(p for p in root.rglob('*') if p.is_file() and '__pycache__' not in p.parts and p.suffix!='.zip' and p.name!='ARCHIVE_MANIFEST.json')
manifest={'created_utc':datetime.datetime.now(datetime.timezone.utc).isoformat(),'archive':name,'previous_checkpoint_archives':sorted(p.name for p in root.parent.glob('RESEARCH_SA11_checkpoint_*.zip')),'files':[{'path':str(p.relative_to(root)),'bytes':p.stat().st_size,'sha256':hashlib.sha256(p.read_bytes()).hexdigest()} for p in files]}
(root/'ARCHIVE_MANIFEST.json').write_text(json.dumps(manifest,indent=2)+'\n')
files.append(root/'ARCHIVE_MANIFEST.json')
with zipfile.ZipFile(dest,'x',compression=zipfile.ZIP_DEFLATED,compresslevel=6) as z:
    for p in files:z.write(p,Path('RESEARCH_SA11')/p.relative_to(root))
with zipfile.ZipFile(dest) as z:
    assert z.testzip() is None
assert dest.stat().st_size<500_000_000
print(json.dumps({'file':str(dest),'bytes':dest.stat().st_size,'files':len(files),'sha256':hashlib.sha256(dest.read_bytes()).hexdigest()}))
