"""Locate the original SGA7 I H1 theorem; OCR is a locator, image collation decides."""
from pathlib import Path
import subprocess,concurrent.futures,json
p=Path('work/p2_primary/sga7_pages');p.mkdir(exist_ok=True)
subprocess.run(['pdftoppm','-f','6','-l','30','-scale-to','1600','-png','work/p2_primary/sga7_original.pdf',str(p/'sga7')],check=True)
def one(f):
 t=f.with_suffix('')
 subprocess.run(['tesseract',str(f),str(t),'-l','eng'],stdout=subprocess.DEVNULL,stderr=subprocess.DEVNULL,check=True)
 text=t.with_suffix('.txt').read_text()
 return {'page':f.name,'has35':('3.5' in text),'excerpt':text[text.find('3.5')-100:text.find('3.5')+1300] if '3.5' in text else ''}
with concurrent.futures.ThreadPoolExecutor(max_workers=4) as ex:
 for r in ex.map(one,sorted(p.glob('*.png'))):
  if r['has35']:print(json.dumps(r,ensure_ascii=False))
