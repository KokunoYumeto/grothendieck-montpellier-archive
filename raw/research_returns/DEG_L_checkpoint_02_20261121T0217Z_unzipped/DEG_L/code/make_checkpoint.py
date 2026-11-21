"""Create one named checkpoint at an externally verified scheduled time.

This script does not schedule itself and never uploads or overwrites a ZIP.
"""
from pathlib import Path
import sys, zipfile, hashlib, json

root=Path(__file__).resolve().parents[1]
number=int(sys.argv[1])
stamp=sys.argv[2]
dest=root.parent/f'DEG_L_checkpoint_{number:02d}.zip'
if dest.exists():
    raise SystemExit(f'Refusing to overwrite {dest}')
manifest=[]
for p in sorted(root.rglob('*')):
    if p.is_file() and p.suffix.lower()!='.zip' and '__pycache__' not in p.parts:
        manifest.append((p,p.relative_to(root.parent)))
with zipfile.ZipFile(dest,'x',compression=zipfile.ZIP_DEFLATED,compresslevel=9) as z:
    for p,arc in manifest:
        z.write(p,arc)
    z.writestr('CHECKPOINT_INFO.txt',f'DEG_L checkpoint {number:02d}\nScheduled creation UTC: {stamp}\nResearch is ongoing. This is not a final or complete proof of the open Weil-family question.\nAll current deliverables and research/check documentation are included. Original uploaded inputs remain the companion attachments. No previous checkpoint is included.\n')
with zipfile.ZipFile(dest) as z:
    bad=z.testzip()
    if bad:
        raise SystemExit(f'Corrupt member: {bad}')
print(json.dumps({'path':str(dest),'bytes':dest.stat().st_size,'sha256':hashlib.sha256(dest.read_bytes()).hexdigest(),'members':len(manifest)+1}))
