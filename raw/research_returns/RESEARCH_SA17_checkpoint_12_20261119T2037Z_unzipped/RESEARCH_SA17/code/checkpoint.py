"""Create one immutable full checkpoint at the requested 45-minute boundary.

This script does not upload. It refuses to overwrite any earlier checkpoint.
Original inputs and downloaded sources are outside the selected directory.
"""
from pathlib import Path
import argparse, hashlib, json, zipfile
from datetime import datetime, timezone

parser=argparse.ArgumentParser()
parser.add_argument('number',type=int)
args=parser.parse_args()
root=Path(__file__).resolve().parents[1]
name=f'RESEARCH_SA17_checkpoint_{args.number:02d}.zip'
target=root.parent/name
assert not target.exists(), 'Checkpoint names are immutable'
created=datetime.now(timezone.utc).isoformat()
paths=[]
for path in sorted(root.rglob('*')):
    if not path.is_file() or '__pycache__' in path.parts or path.suffix in {'.pyc','.zip'}:
        continue
    if path.suffix in {'.aux','.toc','.out','.bbl','.blg'}:
        continue
    if path.suffix=='.pdf':
        flag=root/'logs/pdf_qa_passed.json'
        if not flag.exists() or json.loads(flag.read_text()).get('pdf_sha256') != hashlib.sha256(path.read_bytes()).hexdigest():
            continue
    paths.append(path)
manifest={'created_utc':created,'checkpoint':name,'members':[]}
payloads=[]
for path in paths:
    data=path.read_bytes()
    payloads.append((path,data))
    manifest['members'].append({'path':str(path.relative_to(root)),
        'bytes':len(data),'sha256':hashlib.sha256(data).hexdigest()})
manifest_path=root/'logs'/f'checkpoint_{args.number:02d}_manifest.json'
manifest_path.write_text(json.dumps(manifest,indent=2)+'\n')
paths.append(manifest_path)
payloads.append((manifest_path,manifest_path.read_bytes()))
with zipfile.ZipFile(target,'x',compression=zipfile.ZIP_DEFLATED,compresslevel=9) as z:
    # Archive the same bytes that were hashed, even if research notes are
    # extended while compression runs. Prior checkpoints remain immutable.
    for path,data in payloads:
        z.writestr(str(Path(root.name)/path.relative_to(root)),data)
assert target.stat().st_size<500*1024*1024
print(json.dumps({'path':str(target),'bytes':target.stat().st_size,
                  'members':len(paths),'created_utc':created}))
