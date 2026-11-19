"""Selected original published pages, rendered and OCRed solely for source verification.
Raw images/text stay in work, not in the final deliverable. English OCR is a search
aid only; equations and qualifications are checked against the page image.
"""
from pathlib import Path
import subprocess,os,concurrent.futures,json
ROOT=Path(__file__).resolve().parents[4]
WORK=ROOT/'work/p4_primary'
OUT=Path(__file__).resolve().parents[1]/'outputs'
ENV=dict(os.environ,OMP_THREAD_LIMIT='1',OMP_NUM_THREADS='1')
JOBS=[('sga4h_original',p) for p in (239,245,246,247,248,249,250)]+[('sga7ii_original',p) for p in (87,88,93,101,103,106,107,108,109,110,111,112,113,114,115,116,117,118,119,120,121)]+[('sga7i_original',p) for p in (160,170,177,178,179,180,181,190,200,208,209,210,211,219,273,274,275,276,277,278,279,280,281,282,283,293,305)]
def work(pair):
 name,p=pair
 pdf=WORK/(name+'.pdf') if name!='sga7i_original' else ROOT/'work/p2_primary/sga7_original.pdf'
 prefix=WORK/f'{name}_physical_{p}'
 if not prefix.with_suffix('.png').exists():subprocess.run(['pdftoppm','-f',str(p),'-singlefile','-scale-to','1800','-png',str(pdf),str(prefix)],check=True,env=ENV,stdout=subprocess.DEVNULL,stderr=subprocess.DEVNULL)
 if not prefix.with_suffix('.txt').exists():subprocess.run(['tesseract',str(prefix.with_suffix('.png')),str(prefix),'-l','eng','--psm','3'],check=True,env=ENV,stdout=subprocess.DEVNULL,stderr=subprocess.DEVNULL)
 return dict(source=name,physical_page=p,png=str(prefix.with_suffix('.png').relative_to(ROOT)),text=str(prefix.with_suffix('.txt').relative_to(ROOT)))
if __name__=='__main__':
 with concurrent.futures.ThreadPoolExecutor(max_workers=3) as pool:
  rows=list(pool.map(work,JOBS))
 (OUT/'original_page_inspection_manifest.json').write_text(json.dumps(rows,indent=2)+'\n')
 for r in rows:print(r['source'],r['physical_page'])
