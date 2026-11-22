"""Extract preferred arXiv text sources and retain an official article preview."""
from pathlib import Path
import gzip,tarfile,hashlib,json,time,urllib.request
root=Path(__file__).resolve().parents[1]
source=root/'sources';records=[]
start=time.perf_counter()
dest=source/'blickle_fink_latex';dest.mkdir(exist_ok=True)
with tarfile.open(source/'blickle_fink_2025_source') as archive:
    for member in archive.getmembers():
        if not (dest/member.name).resolve().is_relative_to(dest.resolve()):
            raise ValueError('Unsafe source archive member')
    archive.extractall(dest,filter='data')
    records.append({'operation':'extract original Blickle–Fink LaTeX','members':archive.getnames()})
path=source/'perez_2008_original.tex'
path.write_bytes(gzip.decompress((source/'perez_2008_source').read_bytes()))
records.append({'operation':'decompress original Perez LaTeX','file':str(path.relative_to(root)),
                'bytes':path.stat().st_size,'sha256':hashlib.sha256(path.read_bytes()).hexdigest()})
url='https://londmathsoc.onlinelibrary.wiley.com/cms/asset/3f1c94ab-3c1f-4c1b-b3d0-076306e031e4/plms_s3-38.2.219.fp.png'
record={'operation':'fetch official Epstein–Thurston first-page preview','url':url}
try:
    request=urllib.request.Request(url,headers={'User-Agent':'Mozilla/5.0'})
    with urllib.request.urlopen(request,timeout=25) as response:
        data=response.read();record['content_type']=response.headers.get('Content-Type')
    path=source/'epstein_thurston_1979_first_page.png';path.write_bytes(data)
    record.update(file=str(path.relative_to(root)),bytes=len(data),sha256=hashlib.sha256(data).hexdigest())
except Exception as exc: record['error']=str(exc)
records.append(record)
result={'seconds':time.perf_counter()-start,'records':records}
(root/'logs'/'root_extract_and_fetch.json').write_text(json.dumps(result,indent=2)+'\n')
print(json.dumps(result,indent=2))
