#!/usr/bin/env python3
"""Package all new work, excluding reproducible external input caches."""
from pathlib import Path
import csv,hashlib,sys,zipfile
ROOT=Path(__file__).resolve().parent
out=Path(sys.argv[1]).resolve()
if out.exists(): raise SystemExit(f'Refusing to overwrite {out}')
included=[];excluded=[]
for p in sorted(ROOT.rglob('*')):
 if not p.is_file(): continue
 rel=p.relative_to(ROOT)
 if p.suffix=='.zip' or '__pycache__' in rel.parts: continue
 reason=None
 if p.suffix=='.fmt' or p.name=='texsys.aux': reason='Reproducible TeX runtime file, not research content'
 elif 'lean_parts' in rel.parts: reason='Redundant full external Lean input cache; use supplied archive and selected-source manifests'
 elif rel.parts[0]=='source_text': reason='Extracted supplied source text; recover from original attached files'
 elif p.suffix=='.pdf' and p.name!='SIGN_NEXT.pdf': reason='Downloaded external source PDF; source URL/locator recorded in paper and work notes'
 elif p.suffix=='.txt' and (rel.parts[0]=='references' or rel.parts[0]=='work'): reason='Extracted external or supplied source text; recover from original source'
 if reason:
  excluded.append([str(rel),p.stat().st_size,hashlib.sha256(p.read_bytes()).hexdigest(),reason])
 else: included.append(p)
manifest=ROOT/'EXCLUDED_INPUTS.tsv'
with manifest.open('w',newline='') as f:
 w=csv.writer(f,delimiter='\t');w.writerow(['path','bytes','sha256','recovery']);w.writerows(excluded)
if manifest not in included: included.append(manifest)
hashfile=ROOT/'PACKAGE_CONTENTS.sha256'
included=[p for p in included if p!=hashfile]
snapshot={p:p.read_bytes() for p in included}
hashfile.write_text(''.join(f'{hashlib.sha256(snapshot[p]).hexdigest()}  {p.relative_to(ROOT)}\n' for p in sorted(included)))
included.append(hashfile)
snapshot[hashfile]=hashfile.read_bytes()
with zipfile.ZipFile(out,'w',zipfile.ZIP_DEFLATED,compresslevel=6) as z:
 for p in sorted(included):z.writestr('SIGN_NEXT/'+str(p.relative_to(ROOT)),snapshot[p])
with zipfile.ZipFile(out) as z:
 bad=z.testzip()
 if bad: raise SystemExit(f'Failed CRC {bad}')
 for line in z.read('SIGN_NEXT/PACKAGE_CONTENTS.sha256').decode().splitlines():
  expected,name=line.split('  ',1)
  if hashlib.sha256(z.read('SIGN_NEXT/'+name)).hexdigest()!=expected: raise SystemExit(f'Hash mismatch {name}')
 print(f'{out}: {len(z.namelist())} files; {out.stat().st_size} bytes; CRC verified')
