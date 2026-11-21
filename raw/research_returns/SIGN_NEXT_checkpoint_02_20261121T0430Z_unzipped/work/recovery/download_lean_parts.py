from pathlib import Path
import subprocess
from concurrent.futures import ThreadPoolExecutor, as_completed
import shutil, time
r=Path(__file__).resolve().parents[3]/'lean_parts'
r.mkdir(exist_ok=True)
old=Path(__file__).resolve().parents[3]/'lean_part01'
if old.exists(): old.rename(r/'part01')
def f(i):
 p=r/f'part{i:02d}'
 if p.exists(): return i,p.stat().st_size
 for attempt in range(3):
  try:
   subprocess.run(['curl','--fail','--silent','--show-error','--max-time','90',f'https://alpo.ge/lean.tar.gz.part{i:02d}','-o',str(p)],check=True)
   return i,p.stat().st_size
  except Exception:
   if attempt==2: raise
with ThreadPoolExecutor(max_workers=4) as pool:
 for future in as_completed([pool.submit(f,i) for i in range(1,15)]):
  print(future.result(),flush=True)
