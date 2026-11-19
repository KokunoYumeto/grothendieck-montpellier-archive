#!/usr/bin/env python3
"""Read exact line/entry ranges; logging aids auditing, never assigns verdicts."""
import argparse, csv, datetime, hashlib, json, re
from pathlib import Path

BASE = Path(__file__).resolve().parents[2]
OUT = BASE / 'SA23_work'
p = argparse.ArgumentParser()
p.add_argument('path')
p.add_argument('--start', type=int, default=1)
p.add_argument('--end', type=int)
p.add_argument('--entries', help='Inclusive note-entry interval, e.g. 1:12')
p.add_argument('--owner', default='root')
a = p.parse_args()
path = BASE / a.path
lines = path.read_text().splitlines()
start,end = a.start, a.end or len(lines)
if a.entries:
    lo,hi = map(int,a.entries.split(':'))
    heads = [i+1 for i,x in enumerate(lines) if x.startswith('### ')]
    start = heads[lo-1]
    end = heads[hi]-1 if hi < len(heads) else len(lines)
body='\n'.join(f'{i}: {lines[i-1]}' for i in range(start,min(end,len(lines))+1))
logdir=OUT/'parts'/a.owner/'read_logs'
logdir.mkdir(parents=True,exist_ok=True)
name=f'{path.stem}_L{start}-{end}.txt'
(logdir/name).write_text(body+'\n')
event={'utc':datetime.datetime.now(datetime.timezone.utc).isoformat(),'path':str(path.relative_to(BASE)), 'first_line':start,'last_line':end,'sha256':hashlib.sha256(path.read_bytes()).hexdigest(),'output':str((logdir/name).relative_to(OUT)),'purpose':'source reading, not automatically a mathematical check'}
with (logdir/'reads.jsonl').open('a') as f:f.write(json.dumps(event)+'\n')
print(body)
