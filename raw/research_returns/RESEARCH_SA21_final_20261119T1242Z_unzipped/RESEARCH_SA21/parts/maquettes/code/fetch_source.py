"""Download one public source using verified HTTP byte ranges."""
from concurrent.futures import ThreadPoolExecutor, as_completed
from urllib.request import Request, urlopen
from pathlib import Path
from time import perf_counter
import sys

url, destination = sys.argv[1:3]
start = perf_counter()
with urlopen(Request(url,method='HEAD'),timeout=30) as response:
    n = int(response.headers['Content-Length'])
    can_range = response.headers.get('Accept-Ranges') == 'bytes'
p = Path(destination)
p.parent.mkdir(parents=True,exist_ok=True)
partial = p.with_name(p.name + '.partial')
print(f"source={url} bytes={n} ranges={can_range}",flush=True)
if not can_range or n < 1048576:
    with urlopen(url,timeout=60) as response:
        partial.write_bytes(response.read())
else:
    size = 65536
    chunks = [(i,min(i+size,n)-1) for i in range(0,n,size)]
    def get(ab):
        a,b = ab
        with urlopen(Request(url,headers={'Range':f'bytes={a}-{b}'}),timeout=60) as response:
            data = response.read()
            if response.status != 206 or len(data) != b-a+1:
                raise ValueError((a,b,response.status,len(data)))
        return a,data
    with partial.open('wb') as out:
        out.truncate(n)
        with ThreadPoolExecutor(max_workers=4) as pool:
            for done,future in enumerate(as_completed([pool.submit(get,ab) for ab in chunks]),1):
                a,data = future.result()
                out.seek(a)
                out.write(data)
                if done % 8 == 0 or done == len(chunks):
                    print(f'chunks={done}/{len(chunks)}',flush=True)
partial.replace(p)
print(f"saved={p} runtime_seconds={perf_counter()-start:.3f}",flush=True)
