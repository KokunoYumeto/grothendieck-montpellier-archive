#!/usr/bin/env python3
"""Create a new immutable checkpoint/final ZIP with a SHA256 file register."""
from pathlib import Path
import argparse,hashlib,zipfile,csv,io,json
R=Path(__file__).resolve().parents[1]
p=argparse.ArgumentParser();p.add_argument('name');args=p.parse_args()
out=R.parent/(args.name+'.zip')
if out.exists():raise SystemExit('Refusing to overwrite an existing archive')
excluded_suffix={'.aux','.toc','.out','.bbl','.blg','.fmt','.fls','.fdb_latexmk','.synctex.gz'}
files=[]
for f in sorted(R.rglob('*')):
    if not f.is_file():continue
    rel=f.relative_to(R)
    if any(x in rel.parts for x in ['__pycache__','rendered','build','.git']):continue
    if 'sources' in rel.parts and f.suffix not in ['.bib','.md','.tsv','.csv']:continue
    if f.suffix in excluded_suffix and not str(rel).startswith('agents/real_weil/code/'):continue
    if f.suffix in ['.png','.jpg','.jpeg','.zip']:continue
    if f.suffix=='.pdf' and f.name!='RESEARCH_SA06_paper.pdf':continue
    if f.name in ['lualatex.log','texsys.aux']:continue
    if f.name=='FILE_LIST.tsv':continue
    files.append(f)
buf=io.StringIO();w=csv.writer(buf,delimiter='\t');w.writerow(['path','bytes','sha256','stored_in'])
for f in files:
    data=f.read_bytes();w.writerow([str(f.relative_to(R)),len(data),hashlib.sha256(data).hexdigest(),out.name])
manifest=buf.getvalue();(R/'FILE_LIST.tsv').write_text(manifest)
with zipfile.ZipFile(out,'w',compression=zipfile.ZIP_DEFLATED,compresslevel=9) as z:
    for f in files:z.write(f,f.relative_to(R))
    z.writestr('FILE_LIST.tsv',manifest)
if out.stat().st_size>=500_000_000:raise SystemExit('Archive exceeds500MB threshold')
with zipfile.ZipFile(out) as z:
    bad=z.testzip()
    if bad:raise SystemExit('CRC failure: '+bad)
print(json.dumps({'path':str(out),'bytes':out.stat().st_size,'files':len(files)+1,'sha256':hashlib.sha256(out.read_bytes()).hexdigest()}))
