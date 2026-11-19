from pathlib import Path
from urllib.request import urlopen, Request
from time import perf_counter
urls={
'C_christensen_holm_source.tar':'https://arxiv.org/src/1301.0731v2',
'C_christensen_holm.pdf':'https://larswinther.github.io/homepage/download/lazard.pdf',
}
out=Path('SA08_work/sources');out.mkdir(exist_ok=True)
logs=[]
for name,url in urls.items():
    start=perf_counter()
    try:
        with urlopen(Request(url,headers={'User-Agent':'SA08-research-source-check/1.0'}),timeout=20) as r: data=r.read()
        (out/name).write_bytes(data)
        line=f'{name}\t{url}\t{len(data)} bytes\t{perf_counter()-start:.3f} seconds\tsuccess'
    except Exception as e:
        line=f'{name}\t{url}\t{perf_counter()-start:.3f} seconds\t{type(e).__name__}: {e}'
    print(line);logs.append(line)
Path('SA08_work/logs/C_source_fetch.tsv').write_text('\n'.join(logs)+'\n')
