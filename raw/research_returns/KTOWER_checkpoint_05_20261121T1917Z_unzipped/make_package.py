"""Write one immutable checkpoint/final ZIP; excludes earlier ZIPs and rebuildable caches."""
from pathlib import Path
from datetime import datetime,timezone
import argparse,hashlib,json,zipfile
B=Path(__file__).resolve().parent
p=argparse.ArgumentParser();p.add_argument('output');p.add_argument('--not-before');a=p.parse_args()
now=datetime.now(timezone.utc)
if a.not_before:
 target=datetime.fromisoformat(a.not_before.replace('Z','+00:00'))
 assert now>=target,('Prescribed checkpoint interval has not elapsed',now.isoformat(),target.isoformat())
out=Path(a.output).resolve();assert not out.exists(),'Never overwrite a previous package'
manifest=[]
# Newly retrieved complete publications stay in the research workspace; the package
# includes their locators, hashes, and mathematical audits rather than republications.
def omit(p):
 rel=p.relative_to(B)
 if '__pycache__' in rel.parts or p.suffix in {'.zip','.pyc','.fmt','.aux','.toc','.out','.xdv'}:return True
 if p.name in {'KTOWER.log','pdflatex.log','missfont.log'}:return True
 if p.suffix in {'.pdf','.txt','.png','.jpg','.jpeg'} and any(s in rel.parts for s in ['literature','framework_sources','primary']):return True
 if p.name=='KTOWER.pdf' and (p.stat().st_size<1000 or p.stat().st_mtime<(B/'KTOWER.tex').stat().st_mtime):return True
 return False
with zipfile.ZipFile(out,'x',compression=zipfile.ZIP_DEFLATED,compresslevel=6) as z:
 for path in sorted(B.rglob('*')):
  if not path.is_file() or omit(path):continue
  data=path.read_bytes();rel=path.relative_to(B).as_posix()
  z.writestr('KTOWER/'+rel,data)
  manifest.append({'path':rel,'bytes':len(data),'sha256':hashlib.sha256(data).hexdigest()})
 z.writestr('KTOWER/PACKAGE_MANIFEST.json',json.dumps({'created_utc':now.isoformat(),'files':manifest,'earlier_zip_files_included':False},indent=2)+'\n')
print(json.dumps({'path':str(out),'created_utc':now.isoformat(),'files':len(manifest),'bytes':out.stat().st_size,'sha256':hashlib.sha256(out.read_bytes()).hexdigest()}))
