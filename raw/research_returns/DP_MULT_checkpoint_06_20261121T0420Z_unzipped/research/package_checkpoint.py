#!/usr/bin/env python3
"""Create a scheduled immutable checkpoint; never nest previous archives."""
import csv,hashlib,io,json,sys,zipfile
from datetime import datetime,timezone
from pathlib import Path
root=Path(__file__).resolve().parents[1]
number=int(sys.argv[1]); due=datetime.fromisoformat(sys.argv[2]).astimezone(timezone.utc)
now=datetime.now(timezone.utc)
if now<due:raise SystemExit('Scheduled checkpoint is not due yet.')
dest=root.parent/f'DP_MULT_checkpoint_{number:02d}.zip'
if dest.exists():raise SystemExit('Refusing to overwrite an existing checkpoint.')
allowed={'.md','.tex','.tsv','.json','.py'}
files=[p for p in root.rglob('*') if p.is_file() and p.suffix in allowed and not any(x in p.parts for x in ['__pycache__'])]
if (root/'DP_MULT.pdf').exists():files.append(root/'DP_MULT.pdf')
files=sorted(set(files),key=lambda p:p.relative_to(root).as_posix())
with (root/'LEDGER.md').open('a') as f:
 f.write(f'\n\n## Checkpoint{number:02d} packaged at {now.isoformat()}\n\nScheduled immutable full-report checkpoint. Current authored deliverables, mathematical research notes, proof snapshots, source identity/reading metadata and reproduction scripts are included. The PDF is a working build pending final layout QA. Raw recoverable third-party source PDFs, full archive parts, extracted Lean input files and build caches are not redistributed. No earlier ZIP is included. Persistent-save confirmation follows in the continuing ledger.\n')
buf=io.StringIO();writer=csv.writer(buf,delimiter='\t');writer.writerow(['path','bytes','sha256'])
payload=[]
for p in files:
 data=p.read_bytes();rel=p.relative_to(root).as_posix();payload.append((rel,data));writer.writerow([rel,len(data),hashlib.sha256(data).hexdigest()])
status=f'''# Checkpoint {number:02d}\n\nCreated {now.isoformat()}. The main mathematical and source gates are stated in LEDGER.md and QUESTIONS.tsv. This is ongoing work, not the final delivery. The PDF is a working build. All current authored deliverables and research/proof/source metadata are included; earlier checkpoint ZIPs are excluded. Recoverable external raw inputs are identified by exact URLs, archive members and hashes.\n'''
with zipfile.ZipFile(dest,'x',compression=zipfile.ZIP_DEFLATED,compresslevel=9) as z:
 for rel,data in payload:z.writestr(rel,data)
 z.writestr('PACKAGE_MANIFEST.tsv',buf.getvalue());z.writestr('PACKAGE_STATUS.md',status)
with zipfile.ZipFile(dest) as z:
 assert z.testzip() is None
 assert not any(n.endswith('.zip') for n in z.namelist())
 count=len(z.namelist())
print(json.dumps({'path':str(dest),'created_utc':now.isoformat(),'entries':count,'bytes':dest.stat().st_size,'sha256':hashlib.sha256(dest.read_bytes()).hexdigest()}))
