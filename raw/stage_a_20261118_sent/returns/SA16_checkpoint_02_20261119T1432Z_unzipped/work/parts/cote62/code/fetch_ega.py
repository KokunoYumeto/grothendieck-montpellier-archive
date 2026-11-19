"""Fetch the primary EGA III-2 PDF after web-reader size-limit failure."""
from pathlib import Path
import urllib.request, subprocess, hashlib, json, datetime
P=Path(__file__).resolve().parents[1]
url='https://www.numdam.org/item/PMIHES_1963__17__5_0.pdf'
cache=P.parents[2]/'external_cache/cote62'
cache.mkdir(parents=True,exist_ok=True)
target=cache/'EGAIII2.pdf'
with urllib.request.urlopen(url,timeout=40) as response:
    data=response.read()
target.write_bytes(data)
subprocess.run(['pdftotext','-layout',str(target),str(cache/'EGAIII2.txt')],check=True)
record=dict(url=url,utc=datetime.datetime.now(datetime.timezone.utc).isoformat(),bytes=len(data),sha256=hashlib.sha256(data).hexdigest(),extraction='pdftotext -layout')
(P/'outputs/fetch_ega.json').write_text(json.dumps(record,indent=2)+'\n')
print(json.dumps(record,indent=2))
