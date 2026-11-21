"""Write one immutable checkpoint/final ZIP; excludes earlier ZIPs and rebuildable caches."""
from pathlib import Path
from datetime import datetime,timezone
import argparse,hashlib,json,zipfile,shutil,tempfile
B=Path(__file__).resolve().parent
p=argparse.ArgumentParser();p.add_argument('output');p.add_argument('--not-before');a=p.parse_args()
now=datetime.now(timezone.utc)
if a.not_before:
 target=datetime.fromisoformat(a.not_before.replace('Z','+00:00'))
 assert now>=target,('Prescribed checkpoint interval has not elapsed',now.isoformat(),target.isoformat())
out=Path(a.output).resolve();assert not out.exists(),'Never overwrite a previous package'
manifest=[]
pdf_review_path=B/'PDF_REVIEW.json'
pdf_review=json.loads(pdf_review_path.read_text()) if pdf_review_path.exists() else {}
# Newly retrieved complete publications stay in the research workspace; the package
# includes their locators, hashes, and mathematical audits rather than republications.
def omit(p):
 rel=p.relative_to(B)
 if '__pycache__' in rel.parts or p.suffix in {'.zip','.pyc','.fmt','.aux','.toc','.out','.xdv'}:return True
 if p.name in {'KTOWER.log','pdflatex.log','missfont.log'}:return True
 if p.suffix in {'.pdf','.txt','.png','.jpg','.jpeg'} and any(s in rel.parts for s in ['literature','framework_sources','primary']):return True
 if p.name=='KTOWER.pdf' and (not pdf_review.get('complete_visual_review') or pdf_review.get('tex_sha256')!=hashlib.sha256((B/'KTOWER.tex').read_bytes()).hexdigest()):return True
 return False
# Copy the selected member bytes before the slower compression pass. Research
# may resume after the copy finishes without changing any archive member.
# The copy is made only after the explicit not-before check above, and sits
# outside B so it can never recursively enter this or a later checkpoint.
with tempfile.TemporaryDirectory(prefix='ktower_frozen_',dir=B.parent) as td:
 frozen=Path(td)
 selected=[p for p in sorted(B.rglob('*')) if p.is_file() and not omit(p)]
 for path in selected:
  target=frozen/path.relative_to(B);target.parent.mkdir(parents=True,exist_ok=True)
  shutil.copyfile(path,target)
 frozen_at=datetime.now(timezone.utc).isoformat()
 frozen_tex_sha=hashlib.sha256((frozen/'KTOWER.tex').read_bytes()).hexdigest()
 frozen_review=json.loads((frozen/'PDF_REVIEW.json').read_text()) if (frozen/'PDF_REVIEW.json').exists() else {}
 with zipfile.ZipFile(out,'x',compression=zipfile.ZIP_DEFLATED,compresslevel=9) as z:
  for path in sorted(frozen.rglob('*')):
   if not path.is_file():continue
   data=path.read_bytes();rel=path.relative_to(frozen).as_posix()
   if path.name=='KTOWER.pdf' and (not frozen_review.get('complete_visual_review') or frozen_review.get('tex_sha256')!=frozen_tex_sha or hashlib.sha256(data).hexdigest()!=frozen_review.get('pdf_sha256') or b'%%EOF' not in data[-100:]):continue
   # Standard ZIP method14 for bulky exact JSON avoids the observed512MiB
   # transfer limit while preserving every member byte. Python zipfile and
   # 7-Zip support this directly; no additional archive is nested inside.
   method=zipfile.ZIP_LZMA if path.suffix=='.json' and len(data)>=1024*1024 else zipfile.ZIP_DEFLATED
   z.writestr('KTOWER/'+rel,data,compress_type=method,compresslevel=9)
   manifest.append({'path':rel,'bytes':len(data),'sha256':hashlib.sha256(data).hexdigest(),'zip_method':method})
  z.writestr('KTOWER/PACKAGE_MANIFEST.json',json.dumps({'created_utc':now.isoformat(),'source_copy_finished_utc':frozen_at,'compression_uses_frozen_member_bytes':True,'files':manifest,'earlier_zip_files_included':False},indent=2)+'\n')
print(json.dumps({'path':str(out),'created_utc':now.isoformat(),'files':len(manifest),'bytes':out.stat().st_size,'sha256':hashlib.sha256(out.read_bytes()).hexdigest()}))
