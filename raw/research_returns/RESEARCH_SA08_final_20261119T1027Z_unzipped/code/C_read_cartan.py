from pathlib import Path
from time import perf_counter
import subprocess, concurrent.futures
start=perf_counter()
base=Path('SA08_work/logs/C_cartan_pages');base.mkdir(exist_ok=True)
subprocess.run(['pdftoppm','-f','2','-l','13','-scale-to','2000','-png','SA08_work/sources/cartan1976.pdf',str(base/'p')],check=True,stdout=subprocess.DEVNULL)
imgs=sorted(base.glob('p-*.png'))
def read(p):
 r=subprocess.run(['tesseract',str(p),'stdout','-l','eng'],text=True,capture_output=True,check=True)
 return p.name,r.stdout
with concurrent.futures.ThreadPoolExecutor(max_workers=3) as ex: vals=list(ex.map(read,imgs))
text='\n\n'.join('## PDF '+n+'\n'+t for n,t in vals)
Path('SA08_work/sources/C_cartan1976_ocr.txt').write_text(text)
log=f'{len(imgs)} pages rendered at 2000px, OCR with tesseract eng; elapsed {perf_counter()-start:.3f}s. Mathematical formulas require image checking.\n'
Path('SA08_work/logs/C_cartan_ocr_run.txt').write_text(log)
print(log)
