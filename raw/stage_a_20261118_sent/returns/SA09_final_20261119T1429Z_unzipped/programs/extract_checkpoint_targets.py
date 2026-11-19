#!/usr/bin/env python3
"""Read only named textual project endpoints from a retrieved nested archive.

No restoration instruction or program inside the external checkpoint is run.
"""
import hashlib,json,tarfile,zipfile
from pathlib import Path
base=Path('/workspace/scratch/81b6665e34a6')
archive=base/'project_sources/LM4_SUCCESSOR_checkpoint_40.zip'
out=base/'project_sources/LM4_SUCCESSOR_checkpoint_40_selected'
targets={'sections/b_remaining.tex'}
found=[]; first=[]
with zipfile.ZipFile(archive) as z:
 for name in ['LM4_SUCCESSOR/historical_data.tar','LM4_SUCCESSOR/historical_documents.tar']:
  with z.open(name) as stream, tarfile.open(fileobj=stream,mode='r|') as tar:
   for entry in tar:
    n=entry.name.removeprefix('./').removeprefix('LM4_SUCCESSOR/')
    if len(first)<10:first.append(entry.name)
    if n in targets and entry.isfile():
     data=tar.extractfile(entry).read()
     dest=out/n;dest.parent.mkdir(parents=True,exist_ok=True);dest.write_bytes(data)
     found.append({'path':n,'tar':name,'member':entry.name,'bytes':len(data),'sha256':hashlib.sha256(data).hexdigest()})
     targets.remove(n)
    if not targets:break
  if not targets:break
print(json.dumps({'archive':str(archive),'extracted':found,'missing':sorted(targets),'sample_members':first},indent=2))
if targets:raise SystemExit(1)
