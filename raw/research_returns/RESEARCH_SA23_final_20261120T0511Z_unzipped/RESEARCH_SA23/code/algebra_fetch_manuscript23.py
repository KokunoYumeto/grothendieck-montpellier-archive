"""Retry the original Montpellier scan with progress and durable bytes."""
from pathlib import Path
from urllib.request import urlopen
import hashlib
import time

url='https://grothendieck.umontpellier.fr/23.pdf'
root=Path(__file__).resolve().parents[1]
dest=root/'sources'/'algebra_manuscript23.pdf'
part=dest.with_suffix('.part')
start=time.perf_counter()
print('URL',url,flush=True)
try:
    with urlopen(url,timeout=40) as response,part.open('wb') as output:
        print('HTTP',response.status,'headers',dict(response.headers),flush=True)
        size=0
        while True:
            chunk=response.read(1024*1024)
            if not chunk:
                break
            output.write(chunk)
            output.flush()
            size+=len(chunk)
            print('bytes',size,'seconds',round(time.perf_counter()-start,3),flush=True)
    part.replace(dest)
    print('COMPLETE',size,'SHA256',hashlib.sha256(dest.read_bytes()).hexdigest(),flush=True)
except Exception as error:
    print('ERROR',repr(error),flush=True)
print('Elapsed seconds',time.perf_counter()-start,flush=True)
