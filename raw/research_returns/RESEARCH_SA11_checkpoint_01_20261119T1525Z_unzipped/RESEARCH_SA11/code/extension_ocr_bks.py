from pathlib import Path
import subprocess,time,json,concurrent.futures
root=Path('/workspace/scratch/eccd14a17414/RESEARCH_SA11_work'); out=root/'audit/extension_BKS_render';out.mkdir(exist_ok=True)
start=time.monotonic();subprocess.run(['pdftoppm','-r','160','-png',str(root/'sources/extension_BKS1994.pdf'),str(out/'page')],check=True,capture_output=True)
def ocr(p):
 subprocess.run(['tesseract',str(p),str(p.with_suffix('')),'--psm','3'],check=True,capture_output=True)
 return p.with_suffix('.txt').read_text()
paths=sorted(out.glob('page-*.png'))
with concurrent.futures.ThreadPoolExecutor(max_workers=4) as e: texts=list(e.map(ocr,paths))
(root/'sources/extension_BKS1994_ocr.txt').write_text('\n\n'.join('PDF PAGE '+str(i+1)+'\n'+t for i,t in enumerate(texts)))
print(json.dumps({'pages':len(paths),'runtime_s':time.monotonic()-start,'ocr':'tesseract psm3 160dpi'}))
