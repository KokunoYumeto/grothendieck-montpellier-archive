"""Create one immutable research checkpoint. Invoke only at the scheduled interval."""
from pathlib import Path
import hashlib,json,sys,zipfile
ROOT=Path(__file__).resolve().parents[1]
number=int(sys.argv[1])
target=ROOT.parent/f'RESEARCH_SA22_checkpoint_{number:02d}.zip'
if target.exists():raise RuntimeError('Never overwrite a checkpoint')
manifest=[]
for p in sorted((ROOT/'sources').rglob('*')):
    if p.is_file():
        manifest.append(dict(path=str(p.relative_to(ROOT)),bytes=p.stat().st_size,
                       sha256=hashlib.sha256(p.read_bytes()).hexdigest()))
(ROOT/'notes'/'public_source_cache_manifest.json').write_text(json.dumps(manifest,indent=2)+'\n')
included=[]
for p in sorted(ROOT.rglob('*')):
    if not p.is_file():continue
    rel=p.relative_to(ROOT)
    if rel.as_posix()=='CHECKPOINT_CONTENTS.txt':continue
    if '__pycache__' in rel.parts or 'tex-runtime' in rel.parts:continue
    if rel.parts[0]=='sources' and p.suffix!='.bib':continue
    if rel.parts[0]=='qa' and not p.name.startswith('paper'):continue
    if p.suffix in {'.zip','.fmt'}:continue
    included.append(p)
(ROOT/'CHECKPOINT_CONTENTS.txt').write_text(
    '\n'.join(str(p.relative_to(ROOT)) for p in included)+'\nCHECKPOINT_CONTENTS.txt\n')
included.append(ROOT/'CHECKPOINT_CONTENTS.txt')
with zipfile.ZipFile(target,'x',compression=zipfile.ZIP_DEFLATED,compresslevel=6) as z:
    for p in included:z.write(p,'RESEARCH_SA22/'+str(p.relative_to(ROOT)))
if target.stat().st_size>=500_000_000:raise RuntimeError('Archive exceeds user limit')
print(json.dumps(dict(path=str(target),files=len(included),bytes=target.stat().st_size,
                     sha256=hashlib.sha256(target.read_bytes()).hexdigest())))
