"""Retrieve GDZ image67..86 (printed59..78), OCR for reference inspection.
External full text/images remain outside SA04_work. No manuscript ink changed.
"""
from pathlib import Path
from concurrent.futures import ThreadPoolExecutor
import subprocess,urllib.request,hashlib,json
out=Path('/tmp/SA04_a_external/Groth1966');out.mkdir(parents=True,exist_ok=True)
def one(i):
    url=f'https://images.p.sub.uni-goettingen.de/iiif/image/gdz:PPN356556735_0002:{i:08d}/full/1500,/0/default.jpg'
    target=out/f'p{i-8}.jpg'
    with urllib.request.urlopen(url,timeout=55) as r:data=r.read()
    target.write_bytes(data)
    subprocess.run(['tesseract',str(target),str(target.with_suffix('')),'-l','eng'],stderr=subprocess.DEVNULL,check=True)
    return dict(printed_page=i-8,url=url,sha256=hashlib.sha256(data).hexdigest(),ocr_bytes=target.with_suffix('.txt').stat().st_size)
with ThreadPoolExecutor(max_workers=4) as executor:
    rows=list(executor.map(one,range(67,87)))
(out/'article.txt').write_text('\n'.join('\nPRINTED_PAGE '+str(r['printed_page'])+'\n'+(out/f"p{r['printed_page']}.txt").read_text() for r in rows))
print(json.dumps(rows,indent=2))
print('External text',out/'article.txt')
