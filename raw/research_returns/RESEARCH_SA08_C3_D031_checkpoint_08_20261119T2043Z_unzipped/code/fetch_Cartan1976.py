#!/usr/bin/env python3
"""Reproduce the primary Cartan PDF fetch and optional page-image OCR."""
from pathlib import Path
import argparse, concurrent.futures, hashlib, json, subprocess, time, urllib.request
p=argparse.ArgumentParser();p.add_argument('destination');p.add_argument('--ocr',action='store_true');a=p.parse_args()
out=Path(a.destination).resolve();out.mkdir(parents=True,exist_ok=True)
url='https://gdz.sub.uni-goettingen.de/download/pdf/PPN356556735_0035/LOG_0030.pdf'
pdf=out/'Cartan_Theories_cohomologiques.pdf';start=time.monotonic();cached=pdf.exists()
if not cached:
 with urllib.request.urlopen(url,timeout=60) as r:pdf.write_bytes(r.read())
data={'url':url,'bytes':pdf.stat().st_size,'sha256':hashlib.sha256(pdf.read_bytes()).hexdigest(),
      'cache_used':cached,'fetch_or_cache_seconds':time.monotonic()-start}
if a.ocr:
 t=time.monotonic()
 subprocess.run(['pdftoppm','-png','-scale-to','1600',str(pdf),str(out/'page')],check=True)
 pages=sorted(out.glob('page-*.png'))
 def read_page(path):
  target=path.with_suffix('')
  subprocess.run(['tesseract',str(path),str(target)],check=True,capture_output=True)
  return f'\n--- PDF PAGE {path.stem} ---\n'+target.with_suffix('.txt').read_text()
 with concurrent.futures.ThreadPoolExecutor(max_workers=4) as pool:texts=list(pool.map(read_page,pages))
 (out/'ocr_all.txt').write_text(''.join(texts))
 data.update(ocr_pages=len(pages),ocr_seconds=time.monotonic()-t)
(out/'reproduction_log.json').write_text(json.dumps(data,indent=2)+'\n')
print(json.dumps(data))
