"""Create one checkpoint at its scheduled time, or the final requested ZIP.

Inputs, third-party full texts, bytecode and earlier archives are excluded.
The output manifest is written before zipping, so the archive documents itself.
"""
from pathlib import Path
import datetime,json,sys,zipfile,hashlib
root=Path(__file__).resolve().parents[2]
data=root/'deliverable'
name=sys.argv[1]
assert name=='SA03.zip' or (name.startswith('SA03_checkpoint_') and name.endswith('.zip'))
dest=root/name
assert not dest.exists(),f'Never overwrite an archive: {dest}'
files=sorted(p for p in data.rglob('*') if p.is_file() and '__pycache__' not in p.parts and p.suffix not in {'.pyc','.zip'})
manifest=[]
payloads={}
for p in files:
    if p.name=='PACKAGE_MANIFEST.json':continue
    raw=p.read_bytes()
    payloads[p.relative_to(data).as_posix()]=raw
    manifest.append(dict(path=p.relative_to(data).as_posix(),bytes=len(raw),sha256=hashlib.sha256(raw).hexdigest()))
(data/'PACKAGE_MANIFEST.json').write_text(json.dumps(dict(archive=name,date=datetime.datetime.now(datetime.timezone.utc).isoformat(),files=manifest),indent=2)+'\n')
with zipfile.ZipFile(dest,'x',compression=zipfile.ZIP_DEFLATED,compresslevel=9) as z:
    for relative,raw in payloads.items():
        z.writestr(relative,raw)
    z.write(data/'PACKAGE_MANIFEST.json','PACKAGE_MANIFEST.json')
print(json.dumps(dict(archive=str(dest),files=len(manifest)+1,bytes=dest.stat().st_size)))
