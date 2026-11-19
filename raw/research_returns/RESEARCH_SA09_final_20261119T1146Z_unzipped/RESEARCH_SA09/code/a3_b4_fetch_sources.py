"""Fetch opened primary sources; record byte counts and elapsed times."""
from pathlib import Path
from urllib.request import urlopen
from time import perf_counter
import json, tarfile
root=Path(__file__).resolve().parents[1]
sources=[
('horel','https://arxiv.org/src/2211.02349v2'),
('toen','https://arxiv.org/src/1911.05509v3'),
('mandell','https://arxiv.org/src/math/0311016'),
('ribet_html','https://projecteuclid.org/euclid.dmj/1077313720'),
('pst','https://orbilu.uni.lu/bitstream/10993/39282/1/PeruccaSgobbaTronto-Kummer-rational.pdf'),
('linking','https://friedl.app.uni-regensburg.de/papers/linking-forms-february-26-2018.pdf')]
rows=[]
for name,url in sources:
    t=perf_counter()
    try:
        with urlopen(url,timeout=30) as r: data=r.read();mime=r.headers.get('Content-Type','');final=r.url
        suffix='.pdf' if data.startswith(b'%PDF') else '.tar' if data[:2]==b'\x1f\x8b' else '.html'
        path=root/'sources'/(name+suffix);path.write_bytes(data)
        if suffix=='.tar':
            dest=root/'sources'/name;dest.mkdir(exist_ok=True)
            with tarfile.open(path) as z:z.extractall(dest,filter='data')
        rows.append(dict(name=name,url=url,final_url=final,mime=mime,bytes=len(data),seconds=perf_counter()-t,path=str(path)))
    except Exception as e:rows.append(dict(name=name,url=url,error=str(e),seconds=perf_counter()-t))
print(json.dumps(rows,indent=2))
(root/'logs/a3_b4_fetch_sources.json').write_text(json.dumps(rows,indent=2))
