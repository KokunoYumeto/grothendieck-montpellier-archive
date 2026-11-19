"""Fetch primary source bytes; failures are logged and do not certify an opened source."""
from pathlib import Path
from urllib.request import urlopen
import gzip, time

ROOT=Path(__file__).resolve().parents[1]/'literature_B'
ROOT.mkdir(exist_ok=True)
URLS={
 'treumann_source':'https://arxiv.org/e-print/0708.0659',
 'treumann.pdf':'https://arxiv.org/pdf/0708.0659',
 'quinn.pdf':'https://webhomes.maths.ed.ac.uk/~v1ranick/papers/quinn5.pdf',
 'HA.pdf':'https://www.math.ias.edu/~lurie/papers/HA.pdf',
}
t=time.perf_counter()
for name,url in URLS.items():
    try:
        target=ROOT/name
        if target.exists():
            print(name, 'existing', target.stat().st_size)
            continue
        data=urlopen(url,timeout=30).read()
        target.write_bytes(data)
        print(name, 'downloaded',len(data))
    except Exception as exc:
        print(name, type(exc).__name__,str(exc))
src=ROOT/'treumann_source'
if src.exists():
    (ROOT/'treumann.tex').write_bytes(gzip.decompress(src.read_bytes()))
    print('treumann.tex decompressed')
print('elapsed_seconds',round(time.perf_counter()-t,3))
