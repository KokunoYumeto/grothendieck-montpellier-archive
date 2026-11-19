"""Reproducible original-SGA page inspection; not manuscript-scan inspection."""
from pathlib import Path
import subprocess,os
ROOT=Path(__file__).resolve().parents[4]
pdf=ROOT/'work/p2_primary/sga7_original.pdf'
dest=ROOT/'work/p4_primary'
out=dest
env=dict(os.environ,OMP_THREAD_LIMIT='1')
for p in range(14,25):
    prefix=dest/f'sga7_intro_physical_{p}'
    subprocess.run(['pdftoppm','-f',str(p),'-l',str(p),'-singlefile','-scale-to','1700','-png',str(pdf),str(prefix)],check=True,env=env)
    target=out/f'sga7_intro_physical_{p}'
    subprocess.run(['tesseract',str(prefix)+'.png',str(target),'-l','eng'],check=True,env=env,stdout=subprocess.DEVNULL,stderr=subprocess.DEVNULL)
    print(p,flush=True)
