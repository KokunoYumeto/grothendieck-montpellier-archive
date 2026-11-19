"""Reproduce the reference-page rendering used for visual theorem checks.
Public reference PDFs and images stay outside SA05; only hashes/counts enter it.
Run acquire_references.py first if reference_cache is absent.
"""
from pathlib import Path
import subprocess, hashlib, json

cache=Path('reference_cache')
jobs=[('standard_conjectures_check.pdf','standard',list(range(1,8))),
      ('wittform.pdf','witt',[2,7,8,9,11,12,13,14,15])]
log=[]
for source,prefix,pages in jobs:
 for page in pages:
  command=['pdftoppm','-f',str(page),'-l',str(page),'-scale-to','1800','-png',str(cache/source),str(cache/prefix)]
  r=subprocess.run(command,capture_output=True,text=True,check=True)
  candidates=list(cache.glob(f'{prefix}-{page}.png'))+list(cache.glob(f'{prefix}-{page:02d}.png'))
  assert len(set(candidates))==1,(source,page,candidates)
  p=candidates[0]
  log.append(dict(reference_pdf=source,pdf_page=page,image=str(p),sha256=hashlib.sha256(p.read_bytes()).hexdigest(),bytes=p.stat().st_size,command=command,stderr=r.stderr,view_note='These pages were actually viewed through the image tool during the audit. Rendering alone is not evidence of viewing.'))
Path('SA05/work/cote11b/outputs/reference_rendering.json').write_text(json.dumps(log,indent=2)+'\n')
print('Rendered',len(log),'previously viewed reference pages; image bytes are outside SA05.')
