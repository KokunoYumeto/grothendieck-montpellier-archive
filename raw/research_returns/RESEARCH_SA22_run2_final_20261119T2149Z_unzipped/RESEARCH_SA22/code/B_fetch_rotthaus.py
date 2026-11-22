#!/usr/bin/env python3
"""Fetch the twelve public GDZ canvases for Rotthaus (1990), not the full volume."""
from pathlib import Path
from urllib.request import urlopen
from concurrent.futures import ThreadPoolExecutor
import json, subprocess, time, hashlib
root=Path(__file__).resolve().parents[1]
manifest=json.loads((root/'literature/B_Rotthaus_1990_manifest.json').read_text())
cs=manifest['sequences'][0]['canvases'][460:472]
out=root/'literature/B_Rotthaus_1990_pages';out.mkdir(exist_ok=True)
start=time.perf_counter()
def fetch(c):
 label=c['label'];url=c['images'][0]['resource']['@id']+'/full/1800,/0/default.jpg'
 data=urlopen(url,timeout=50).read();path=out/(label+'.jpg');path.write_bytes(data)
 subprocess.run(['tesseract',str(path),str(out/label),'--psm','3'],capture_output=True,check=True)
 return {'printed_page':label,'url':url,'bytes':len(data),'sha256':hashlib.sha256(data).hexdigest()}
with ThreadPoolExecutor(max_workers=4) as ex:rows=list(ex.map(fetch,cs))
(root/'literature/B_Rotthaus_1990.txt').write_text('\n\n'.join('PRINTED PAGE '+c['label']+'\n'+(out/(c['label']+'.txt')).read_text() for c in cs))
try:
 from PIL import Image
 ims=[Image.open(out/(c['label']+'.jpg')).convert('RGB') for c in cs]
 ims[0].save(root/'literature/B_Rotthaus_1990.pdf',save_all=True,append_images=ims[1:],resolution=180)
except ImportError:
 pass
(root/'logs/B_Rotthaus_fetch_receipt.json').write_text(json.dumps({'scope':'printed pages455–466, all12pages of original paper','canvases':rows,'seconds':time.perf_counter()-start},indent=2))
print('Fetched and OCRed',len(rows),'original pages in',round(time.perf_counter()-start,2),'s')
