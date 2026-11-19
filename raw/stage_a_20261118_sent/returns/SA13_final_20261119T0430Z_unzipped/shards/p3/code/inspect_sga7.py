"""Render and OCR an original published SGA7 passage; OCR is navigation only.

Source PDF is shared input work/p2_primary/sga7_original.pdf. The reviewer
visually checks all mathematical hypotheses used; no claim is certified by OCR.
Generated page images remain working material, not manuscript scan evidence.
"""
from pathlib import Path
import subprocess,sys,os
ROOT=Path(__file__).resolve().parents[4]
OUT=ROOT/'work/p3_primary'
OUT.mkdir(exist_ok=True)
pages=[int(p) for p in sys.argv[1:]] or list(range(375,391))
for page in pages:
    out=OUT/f'sga7_pdf{page}'
    subprocess.run(['pdftoppm','-f',str(page),'-l',str(page),'-r','140','-png','-singlefile',str(ROOT/'work/p2_primary/sga7_original.pdf'),str(out)],check=True)
    p=subprocess.run(['tesseract',str(out)+'.png','stdout','-l','eng'],capture_output=True,text=True,check=True,env={**os.environ,'OMP_THREAD_LIMIT':'1'})
    out.with_suffix('.txt').write_text(p.stdout)
    print(f'PDF page {page}: '+p.stdout[:100].replace('\n',' '))
