"""Extract explicitly fetched arXiv source archives into confined source folders."""
from pathlib import Path
import gzip, tarfile, sys, json, time

root=Path(__file__).resolve().parents[1]/'sources'
for name in sys.argv[1:]:
    start=time.monotonic();source=root/name;dest=root/source.stem
    dest.mkdir(exist_ok=True)
    files=[]
    if tarfile.is_tarfile(source):
        with tarfile.open(source) as archive:
            for member in archive.getmembers():
                if not member.isfile():continue
                target=(dest/member.name).resolve()
                if not target.is_relative_to(dest.resolve()):raise ValueError(member.name)
                target.parent.mkdir(parents=True,exist_ok=True)
                target.write_bytes(archive.extractfile(member).read())
                files.append(str(target.relative_to(dest)))
    else:
        data=source.read_bytes()
        if data[:2]==b'\x1f\x8b':data=gzip.decompress(data)
        (dest/'main.tex').write_bytes(data);files=['main.tex']
    print(json.dumps({'source':name,'destination':str(dest),'files':files,
        'seconds':time.monotonic()-start}),flush=True)
