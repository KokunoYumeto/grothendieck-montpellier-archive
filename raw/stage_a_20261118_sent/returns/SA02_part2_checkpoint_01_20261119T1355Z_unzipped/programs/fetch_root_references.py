"""Fetch opened primary PDFs for local inspection; retain metadata, not redistributable copies."""
import concurrent.futures, datetime, hashlib, json, subprocess, urllib.request
from pathlib import Path
work=Path(__file__).resolve().parents[1]
cache=work.parent/'reference_cache'; cache.mkdir(exist_ok=True)
refs=[('BichselKnus1994','https://people.math.ethz.ch/~knus/papers/bk.pdf'),
      ('SGA4XVIII','https://publications.ias.edu/sites/default/files/Number4.pdf'),
      ('EGAIV4','https://www.numdam.org/article/PMIHES_1967__32__5_0.pdf')]
def fetch(spec):
 key,url=spec
 row={'key':key,'url':url,'time':datetime.datetime.now(datetime.timezone.utc).isoformat()}
 try:
  data=urllib.request.urlopen(url,timeout=40).read()
  path=cache/(key+'.pdf');path.write_bytes(data)
  subprocess.run(['pdftotext','-layout',str(path),str(path.with_suffix('.txt'))],check=True,capture_output=True)
  row.update(status='success',bytes=len(data),sha256=hashlib.sha256(data).hexdigest(),local_path=str(path))
 except Exception as exc:row.update(status='failed',error=repr(exc))
 return row
with concurrent.futures.ThreadPoolExecutor(max_workers=3) as pool:
 rows=list(pool.map(fetch,refs))
(work/'outputs/root_reference_fetch.json').write_text(json.dumps(rows,indent=2)+'\n')
for row in rows:print(json.dumps(row))
