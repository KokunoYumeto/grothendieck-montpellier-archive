"""Reconstruct long original records in a separate disposable working folder.

Run from any directory:
  python3 WORKBENCH/tools/reassemble_records.py /tmp/fermat-record-replay
  cd /tmp/fermat-record-replay
  gp -q records/septic56_replay_principal.gp

The destination must not already exist. No file in the workbench is changed.
Every chunk and reconstructed record is checked by SHA-256. This restores
large mathematical witness records; it does not fetch any external source.
"""
from pathlib import Path
import hashlib
import json
import shutil
import sys

root=Path(__file__).resolve().parent.parent
destination=Path(sys.argv[1]).resolve()
if destination.exists():raise SystemExit('Destination already exists; choose a new empty path.')
if root in destination.parents:raise SystemExit('Choose a destination outside the workbench.')
destination.mkdir(parents=True)
shutil.copytree(root/'records',destination/'records')
restored=[]
for manifest in sorted((root/'records').rglob('*.parts.json')):
    data=json.loads(manifest.read_text());chunks=[]
    for part in data['parts']:
        chunk=(root/part['path']).read_bytes()
        assert len(chunk)==part['bytes']
        assert hashlib.sha256(chunk).hexdigest()==part['sha256']
        chunks.append(chunk)
    assembled=b''.join(chunks)
    assert len(assembled)==data['bytes']
    assert hashlib.sha256(assembled).hexdigest()==data['sha256']
    target=destination/data['reconstructed_path']
    if target.exists():raise RuntimeError('Unexpected pre-existing reconstruction target')
    target.parent.mkdir(parents=True,exist_ok=True);target.write_bytes(assembled)
    restored.append(data['reconstructed_path'])
print(json.dumps({'destination':str(destination),'reconstructed':restored,
                  'all_hashes_verified':True},indent=2))
