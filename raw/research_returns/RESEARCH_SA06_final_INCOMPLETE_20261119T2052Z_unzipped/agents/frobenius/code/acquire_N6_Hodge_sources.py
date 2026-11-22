from pathlib import Path
from concurrent.futures import ThreadPoolExecutor
import urllib.request, hashlib, subprocess, json, time
root = Path(__file__).resolve().parents[1]
items = [
 ('Zarhin1983_HodgeK3.pdf','https://pub.math.leidenuniv.nl/~luijkrmvan/K3Banff/papers/Zarhin_K3_crelle_1983.pdf'),
 ('BrevikNollet2009v3.pdf','https://arxiv.org/pdf/0806.1243'),
 ('Beauville2014_maximal_picard.pdf','https://www.numdam.org/article/JEP_2014__1__101_0.pdf'),
 ('Huybrechts_K3Global.pdf','https://www.math.uni-bonn.de/people/huybrech/K3Global.pdf'),
]
def acquire(item):
 name, url = item
 p = root / 'sources' / name
 if not p.exists():
  with urllib.request.urlopen(url, timeout=30) as response:
   data = response.read()
  assert data.startswith(b'%PDF')
  p.write_bytes(data)
 subprocess.run(['pdftotext','-layout',str(p),str(p.with_suffix('.txt'))],check=True)
 return dict(file=str(p.relative_to(root)),url=url,bytes=p.stat().st_size,sha256=hashlib.sha256(p.read_bytes()).hexdigest())
start=time.monotonic()
with ThreadPoolExecutor(max_workers=4) as pool:
 result=list(pool.map(acquire,items))
report=dict(sources=result,runtime_seconds=round(time.monotonic()-start,3))
(root/'output'/'N6_Hodge_sources_manifest.json').write_text(json.dumps(report,indent=2)+'\n')
print(json.dumps(report,indent=2))
