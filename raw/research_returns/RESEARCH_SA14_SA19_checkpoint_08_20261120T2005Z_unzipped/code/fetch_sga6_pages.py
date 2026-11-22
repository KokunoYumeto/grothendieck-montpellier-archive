"""Download the exact original page scans used to check the SGA6 citation."""
from pathlib import Path
import urllib.request, json, hashlib, time
root=Path(__file__).resolve().parents[1]
out=[]
for number in (639,640):
    url=f'https://wstein.org/sga/sga/6/6t_{number}.jpeg'
    target=root/'sources'/f'SGA6_{number}.jpeg'
    start=time.monotonic()
    try:
        with urllib.request.urlopen(url,timeout=40) as stream:
            data=stream.read()
        target.write_bytes(data)
        out.append(dict(page=number,url=url,seconds=round(time.monotonic()-start,3),bytes=len(data),sha256=hashlib.sha256(data).hexdigest(),status='downloaded'))
    except Exception as error:
        out.append(dict(page=number,url=url,seconds=round(time.monotonic()-start,3),status='failed',error=str(error)))
result=json.dumps(out,indent=2)
(root/'code'/'fetch_sga6_pages_output.json').write_text(result+'\n')
print(result)
