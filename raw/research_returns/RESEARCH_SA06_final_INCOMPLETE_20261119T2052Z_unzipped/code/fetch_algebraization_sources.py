"""Retain primary sources for the completion-algebraization transfer in C.3z."""
from pathlib import Path
from concurrent.futures import ThreadPoolExecutor
import hashlib, json, time, urllib.request
import fitz

ROOT=Path(__file__).resolve().parents[1]
SOURCES=[
 ('artin1969approximation','https://www.numdam.org/item/PMIHES_1969__36__23_0.pdf','pdf'),
 ('hauser_woblistin2021','https://www.cambridge.org/core/journals/forum-of-mathematics-sigma/article/arquile-varieties-varieties-consisting-of-power-series-in-a-single-variable/E2265D5BFAFA7E846D6A3DD1711D7B36','html'),
 ('stacks07BY','https://stacks.math.columbia.edu/tag/07BY','html'),
 ('stacks07QY','https://stacks.math.columbia.edu/tag/07QY','html'),
]
def fetch(item):
    name,url,kind=item;start=time.perf_counter();record={'name':name,'url':url}
    try:
        request=urllib.request.Request(url,headers={'User-Agent':'ResearchSourceAudit/1.0'})
        with urllib.request.urlopen(request,timeout=45) as response:
            data=response.read();record['http_status']=response.status
        path=ROOT/'sources'/(name+'.'+kind);path.write_bytes(data)
        record.update(bytes=len(data),sha256=hashlib.sha256(data).hexdigest(),path=str(path))
        if kind=='pdf':
            document=fitz.open(path)
            path.with_suffix('.txt').write_text('\n\n'.join(f'PDF PAGE {i+1}\n'+p.get_text() for i,p in enumerate(document)))
            record['pdf_pages']=len(document)
    except Exception as error:record['error']=str(error)
    record['runtime_seconds']=time.perf_counter()-start
    return record
start=time.perf_counter()
with ThreadPoolExecutor(max_workers=4) as pool:records=list(pool.map(fetch,SOURCES))
output={'sources':records,'runtime_seconds':time.perf_counter()-start}
(ROOT/'code/fetch_algebraization_sources_output.json').write_text(json.dumps(output,indent=2)+'\n')
print(json.dumps(output,indent=2))
