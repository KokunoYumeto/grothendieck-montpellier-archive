"""Line-numbered source reader. Navigation only: makes no scholarly verdicts.
Usage: read_source.py RELATIVE_PATH START END [--entries]
All displayed output is retained in outputs/ for the research audit.
"""
from pathlib import Path
import argparse,re,datetime,hashlib
ROOT=Path(__file__).resolve().parents[2]
p=argparse.ArgumentParser();p.add_argument('path');p.add_argument('start',type=int);p.add_argument('end',type=int);p.add_argument('--entries',action='store_true');a=p.parse_args()
f=ROOT/'source'/a.path
ls=f.read_text().splitlines()
if a.entries:
    heads=[i for i,s in enumerate(ls) if re.match(r'^###\s+',s)]
    start=heads[a.start-1]+1
    end=heads[a.end] if a.end<len(heads) else len(ls)
else: start,end=a.start,min(a.end,len(ls))
out=f'SOURCE {a.path}; lines {start}-{end}; sha256 {hashlib.sha256(f.read_bytes()).hexdigest()}\n'
out+='\n'.join(f'{i+1:05d} {ls[i]}' for i in range(start-1,end))+'\n'
tag=datetime.datetime.now(datetime.timezone.utc).strftime('%Y%m%dT%H%M%S%f')
dest=ROOT/'SA04_work/outputs'/f'read_{f.stem}_{start}_{end}_{tag}.txt'
dest.write_text(out)
print(out,end='')
