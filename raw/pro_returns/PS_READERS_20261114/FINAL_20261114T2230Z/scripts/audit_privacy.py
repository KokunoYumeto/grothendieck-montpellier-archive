"""Inspect deliverable text and PDF text/metadata for prohibited location/address strings."""
from pathlib import Path
import hashlib,json,re
import fitz
P=Path(__file__).resolve().parents[1]
local_roots=[str(P.parent),str(Path.home())]
email=re.compile(r'[A-Z0-9._%+-]+@[A-Z0-9.-]+\.[A-Z]{2,}',re.I)
absolute=re.compile(r'(?<![A-Za-z0-9_.])/(?:workspace|home|mnt|tmp|usr|opt)/[^\s<>\"\x27]+')
drive=re.compile(r'\b[A-Za-z]:[\\/](?:Users|Documents|Program Files)[\\/][^\s]+')
issues=[];text_files=0;pdf_files=0;pdf_pages=0
def check(s,relative,scope):
 for category,pattern in [('email',email),('absolute location',absolute),('drive location',drive)]:
  for m in pattern.finditer(s):
   issues.append({'file':relative,'scope':scope,'kind':category,'offset':m.start(),'matched_sha256':hashlib.sha256(m[0].encode()).hexdigest()})
 for value in local_roots:
  if value and value in s:issues.append({'file':relative,'scope':scope,'kind':'current runtime location','matched_sha256':hashlib.sha256(value.encode()).hexdigest()})
for path in sorted(P.rglob('*')):
 if not path.is_file() or '__pycache__' in path.parts or path.suffix=='.zip':continue
 rel=str(path.relative_to(P))
 if path.suffix.lower()=='.pdf':
  doc=fitz.open(path);pdf_files+=1;pdf_pages+=len(doc)
  check(json.dumps(doc.metadata),rel,'PDF metadata')
  for i,page in enumerate(doc,1):check(page.get_text(),rel,'PDF page '+str(i))
 else:
  try:s=path.read_text(encoding='utf-8')
  except (UnicodeDecodeError,ValueError):continue
  text_files+=1;check(s,rel,'UTF-8 content')
result={'complete':not issues,'text_files_checked':text_files,'pdf_files_checked':pdf_files,'pdf_pages_checked':pdf_pages,'issues':issues,'method':'Every UTF-8 deliverable and every PDF text page/metadata inspected; issue values are hashed so the audit itself does not reproduce prohibited strings.'}
(P/'records/PRIVACY_AUDIT.json').write_text(json.dumps(result,indent=2)+'\n')
print(json.dumps({k:v for k,v in result.items() if k!='method'}))
