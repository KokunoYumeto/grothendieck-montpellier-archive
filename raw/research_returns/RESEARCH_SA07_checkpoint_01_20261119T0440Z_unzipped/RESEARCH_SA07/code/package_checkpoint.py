#!/usr/bin/env python3
"""Create the scheduled research checkpoint. Saving is performed separately.
No timer is inferred here: invoke only at the authorized 45-minute boundary.
"""
from pathlib import Path
import csv,hashlib,io,json,sys,zipfile
from datetime import datetime,timezone
out=Path(__file__).resolve().parent.parent
root=out.parent.parent
number=int(sys.argv[1]);name=f'RESEARCH_SA07_checkpoint_{number:02d}.zip'
archive=root/'output'/name
if archive.exists():raise SystemExit('Refusing to replace existing checkpoint')
entries={}
allowed={'.tex','.pdf','.csv','.bib','.md','.tsv','.py','.out','.txt'}
for p in out.rglob('*'):
 if p.is_file() and p.suffix in allowed and p.name not in {'FILE_MANIFEST.tsv'}:
  entries[str(p.relative_to(out))]=p
for p in (root/'work').glob('*'):
 if p.is_file() and (p.name.startswith('agent_') or p.name.endswith('_references.bib')):
  entries['work/'+p.name]=p
for folder in (root/'work').glob('code_*'):
 for p in folder.rglob('*'):
  if p.is_file() and p.suffix in allowed:entries['work/'+str(p.relative_to(root/'work'))]=p
records=[]
for arc,p in sorted(entries.items()):
 b=p.read_bytes();records.append([arc,len(b),hashlib.sha256(b).hexdigest(),'included',name])
buf=io.StringIO();w=csv.writer(buf,delimiter='\t',lineterminator='\n');w.writerow(['file','bytes','sha256','state','held_in']);w.writerows(records)
(out/'FILE_MANIFEST.tsv').write_text(buf.getvalue())
with zipfile.ZipFile(archive,'x',compression=zipfile.ZIP_DEFLATED,compresslevel=9) as z:
 for arc,p in sorted(entries.items()):z.write(p,'RESEARCH_SA07/'+arc)
 z.writestr('RESEARCH_SA07/FILE_MANIFEST.tsv',buf.getvalue())
if archive.stat().st_size>=500*1024*1024:raise SystemExit('Checkpoint exceeds 500 MiB; split before saving')
with zipfile.ZipFile(archive) as z:
 bad=z.testzip()
 if bad:raise SystemExit('ZIP CRC failure: '+bad)
print(json.dumps({'archive':str(archive),'files':len(records)+1,'bytes':archive.stat().st_size,'sha256':hashlib.sha256(archive.read_bytes()).hexdigest(),'created_utc':datetime.now(timezone.utc).isoformat()}))
