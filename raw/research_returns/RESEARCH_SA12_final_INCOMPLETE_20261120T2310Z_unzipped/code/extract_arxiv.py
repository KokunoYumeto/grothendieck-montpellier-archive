"""Extract an arXiv source: tar archive or a single gzip-compressed TeX file."""
from pathlib import Path
import gzip, tarfile, argparse, json, time
p=argparse.ArgumentParser()
p.add_argument('source');p.add_argument('destination')
a=p.parse_args(); started=time.perf_counter()
source=Path(a.source); dest=Path(a.destination);dest.mkdir(parents=True,exist_ok=True)
if tarfile.is_tarfile(source):
    with tarfile.open(source) as t:
        t.extractall(dest,filter='data')
    kind='tar'
else:
    data=source.read_bytes()
    if data[:2]==b'\x1f\x8b':
        data=gzip.decompress(data)
    (dest/'source.tex').write_bytes(data)
    kind='single source'
files=sorted(str(f.relative_to(dest)) for f in dest.rglob('*') if f.is_file())
print(json.dumps({'source':str(source),'destination':str(dest),'kind':kind,
                  'files':files,'seconds':time.perf_counter()-started},indent=2))
