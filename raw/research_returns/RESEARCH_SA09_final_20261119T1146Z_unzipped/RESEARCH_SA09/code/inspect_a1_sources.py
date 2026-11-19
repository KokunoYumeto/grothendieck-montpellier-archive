"""Unpack acquired arXiv source archives safely and extract PDF text."""
from pathlib import Path
import tarfile, gzip, subprocess, json
ROOT=Path(__file__).resolve().parents[1]
records=[]
for name in ['krause_1203.0311_source','touze_2607.00631_source']:
    path=ROOT/'sources'/name
    if not path.exists(): continue
    dest=path.with_name(name+'_unpacked'); dest.mkdir(exist_ok=True)
    if tarfile.is_tarfile(path):
        with tarfile.open(path) as tf:
            for member in tf.getmembers():
                if member.islnk() or member.issym() or not (dest/member.name).resolve().is_relative_to(dest.resolve()):
                    raise ValueError(member.name)
            tf.extractall(dest)
    else:
        data=path.read_bytes()
        if data[:2]==b'\x1f\x8b': data=gzip.decompress(data)
        (dest/'source.tex').write_bytes(data)
    records.append({'source':name,'files':[str(p.relative_to(ROOT)) for p in dest.rglob('*') if p.is_file()]})
for name in ['roby1963','friedlander_suslin1997','touze_2607.00631']:
    path=ROOT/'sources'/(name+'.pdf')
    if path.exists():
        p=subprocess.run(['pdftotext','-layout',str(path),str(path.with_suffix('.txt'))],capture_output=True,text=True)
        records.append({'source':name,'text_extraction_exit':p.returncode,'stderr':p.stderr})
out=json.dumps(records,indent=2)
(ROOT/'logs'/'inspect_a1_sources.json').write_text(out)
print(out)
