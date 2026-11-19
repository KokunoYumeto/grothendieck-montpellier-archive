#!/usr/bin/env python3
"""Read numbered source passages; this tool never assigns research verdicts."""
from pathlib import Path
import argparse, re, datetime, json

ROOT=Path(__file__).resolve().parents[2]
WORK=ROOT/'SA06_work'
p=argparse.ArgumentParser()
p.add_argument('path')
p.add_argument('--start',type=int,default=1)
p.add_argument('--end',type=int,default=10**9)
p.add_argument('--entries',action='store_true')
p.add_argument('--scans')
p.add_argument('--headings',action='store_true')
a=p.parse_args()
path=ROOT/a.path
lines=path.read_text().splitlines()
out=[]
if a.entries or a.headings:
    starts=[i for i,s in enumerate(lines) if s.startswith('### ')]
    for j,i in enumerate(starts):
        n=j+1
        if a.start<=n<=a.end:
            stop=starts[j+1] if j+1<len(starts) else len(lines)
            out.append(f'ENTRY {path.stem.replace("_notes","")}#{n}, note lines {i+1}-{stop}')
            out.extend(f'{k+1}: {lines[k]}' for k in range(i,min(i+1,stop) if a.headings else stop))
else:
    scan='preface'
    wanted=set(a.scans.split(',')) if a.scans else None
    for i,line in enumerate(lines,1):
        m=re.search(r'\\scanpage\{([^}]+)\}',line)
        if m:scan=m.group(1)
        if a.start<=i<=a.end and (wanted is None or scan in wanted):out.append(f'{i} [scan {scan}]: {line}')
text='\n'.join(out)
print(text)
stamp=datetime.datetime.now(datetime.timezone.utc).strftime('%Y%m%dT%H%M%S%f')
log=WORK/'audit'/f'read_{stamp}.txt'
log.write_text(json.dumps(vars(a),ensure_ascii=False)+'\n'+text+'\n')
