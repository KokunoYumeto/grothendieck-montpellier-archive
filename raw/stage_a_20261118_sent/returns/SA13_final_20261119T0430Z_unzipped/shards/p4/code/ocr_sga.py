"""Targeted OCR of the independently downloaded original SGA 7 I scan.
Argument is physical PDF page number, one-based; printed numbers checked separately.
"""
from pathlib import Path
import subprocess,sys,os
ROOT=Path(__file__).resolve().parents[4]
WORK=ROOT/'work/p4_primary';WORK.mkdir(exist_ok=True)
OUT=WORK
PDF=ROOT/'work/p2_primary/sga7_original.pdf'
ENV=dict(os.environ,OMP_THREAD_LIMIT='1',OMP_NUM_THREADS='1')
for n in map(int,sys.argv[1:]):
 stem=WORK/f'sga7_physical_{n}'
 subprocess.run(['pdftoppm','-f',str(n),'-l',str(n),'-scale-to','2000','-png','-singlefile',str(PDF),str(stem)],check=True,env=ENV)
 target=OUT/f'sga7_physical_{n}'
 subprocess.run(['tesseract',str(stem.with_suffix('.png')),str(target),'-l','eng'],check=True,env=ENV)
 print(n,target.with_suffix('.txt'))
