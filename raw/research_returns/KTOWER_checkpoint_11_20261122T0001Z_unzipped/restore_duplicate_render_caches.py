"""Optionally restore byte-identical render-cache aliases from retained canonical images."""
from pathlib import Path
import hashlib
import json
import shutil

B=Path(__file__).resolve().parent
records=json.loads((B/'REBUILDABLE_DUPLICATES.json').read_text())['files']
restored=0
for record in records:
    source=B/record['canonical_path']
    target=B/record['omitted_cache_path']
    data=source.read_bytes()
    assert hashlib.sha256(data).hexdigest()==record['sha256']
    if target.exists():
        assert target.read_bytes()==data,('Refusing to replace changed file',target)
        continue
    target.parent.mkdir(parents=True,exist_ok=True)
    shutil.copyfile(source,target)
    restored+=1
print(f'Restored {restored} identical cache aliases; mathematical artifacts unchanged.')
