#!/usr/bin/env python3
"""Create a complete, immutable scheduled checkpoint or the final ZIP.

Run assemble.py first. A checkpoint cannot be created before its 45-minute
deadline. This script never copies an earlier ZIP or externally fetched full
literature. User-supplied source extracts and all original working records are
preserved. Attachments are identified by INPUTS.tsv and remain the source base.
"""
from pathlib import Path
from datetime import datetime, timezone, timedelta
import argparse, csv, hashlib, json, zipfile

p=argparse.ArgumentParser()
g=p.add_mutually_exclusive_group(required=True)
g.add_argument('--checkpoint',type=int)
g.add_argument('--final',action='store_true')
p.add_argument('--include-verified-pdf',action='store_true')
a=p.parse_args()
ROOT=Path(__file__).resolve().parents[2]
meta=json.loads((ROOT/'work/RUN_METADATA.json').read_text())
now=datetime.now(timezone.utc)
start=datetime.fromisoformat(meta['started_utc'].replace('Z','+00:00'))
if a.checkpoint is not None:
    if a.checkpoint<1: raise SystemExit('Checkpoint number must be positive.')
    due=start+timedelta(minutes=45*a.checkpoint)
    if now<due: raise SystemExit(f'Checkpoint not due until {due.isoformat()}')
    name=f'GRH_NIGHT_checkpoint_{a.checkpoint:02d}.zip'
else:
    name='GRH_NIGHT_final.zip'
dest=ROOT/name
if dest.exists(): raise SystemExit(f'Will not overwrite {dest}')

entries={}
extensions={'.tex','.tsv','.md','.json','.py','.txt'}
for path in (ROOT/'deliverable').iterdir():
    if path.is_file() and path.suffix in {'.tex','.tsv','.md','.json'}:
        entries[path.name]=path
pdf=ROOT/'deliverable/GRH_NIGHT.pdf'
if a.include_verified_pdf and pdf.exists(): entries[pdf.name]=pdf
for path in (ROOT/'work').rglob('*'):
    if not path.is_file(): continue
    rel=path.relative_to(ROOT)
    if any(part in {'sources','literature','__pycache__'} for part in rel.parts): continue
    if 'evidence' in rel.parts:
        # Only user-provided input extracts/images, never downloaded literature.
        if not (path.name.startswith('masullo') and path.suffix in {'.png','.txt'}) and path.name not in {'ALPOGE_remark.txt','MASULLO_the-music-of-the-primes.txt',
                             'masullo_trace_selected.txt','masullo_p425.png',
                             'masullo_p426.png','masullo_p804.png',
                             'masullo_range-484.png','masullo_range-485.png',
                             'masullo-cutoff-428.png','masullo-cutoff-480.png',
                             'masullo-cutoff-482.png','masullo-indentation-495.png'}: continue
    elif path.suffix not in extensions: continue
    entries[str(rel)]=path
for path in (ROOT/'work/checks').iterdir():
    if path.is_file() and path.suffix in extensions:
        entries['checks/'+path.name]=path
prompt=ROOT/'upload/PROMPT(20261121-010237).md'
if prompt.exists(): entries['ORIGINAL_PROMPT.md']=prompt

record={'created_utc':now.isoformat(),'checkpoint':a.checkpoint,
        'filename':name,'file_count_without_manifest':len(entries),
        'excluded':'Earlier ZIPs, TeX runtime/cache, and externally fetched full literature; source URLs/locators retained.',
        'continuation':'Use this archive with original attached source ZIP. Working source drafts and scripts are included.'}
manifest=[]
with zipfile.ZipFile(dest,'x',compression=zipfile.ZIP_DEFLATED,compresslevel=9) as z:
    for rel,path in sorted(entries.items()):
        data=path.read_bytes(); z.writestr(rel,data)
        manifest.append(f'{hashlib.sha256(data).hexdigest()}  {rel}')
    z.writestr('SNAPSHOT.json',json.dumps(record,ensure_ascii=False,indent=2)+'\n')
    z.writestr('SHA256SUMS.txt','\n'.join(manifest)+'\n')
with zipfile.ZipFile(dest) as z:
    bad=z.testzip()
    if bad: raise SystemExit(f'ZIP CRC error: {bad}')
    nested=[n for n in z.namelist() if n.lower().endswith('.zip')]
    if nested: raise SystemExit(f'Unexpected nested ZIPs: {nested}')
print(json.dumps(dict(record,path=str(dest),bytes=dest.stat().st_size,
                     sha256=hashlib.sha256(dest.read_bytes()).hexdigest()),indent=2))
