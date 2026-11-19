#!/usr/bin/env python3
"""Read exact source ranges and retain tool-visible output as an audit record.

This utility performs no interpretation or verdict assignment.
"""
import argparse, datetime, pathlib, hashlib
p=argparse.ArgumentParser()
p.add_argument('source')
p.add_argument('start',type=int)
p.add_argument('end',type=int)
p.add_argument('--label',default='root')
a=p.parse_args()
root=pathlib.Path(__file__).resolve().parents[1]
source=pathlib.Path(a.source)
if not source.is_absolute(): source=root.parent/'source'/source
lines=source.read_text().splitlines()
end=min(a.end,len(lines))
content='\n'.join(f'{i}: {lines[i-1]}' for i in range(a.start,end+1))+'\n'
head=f'SOURCE {source.name}; physical lines {a.start}–{end}; sha256 {hashlib.sha256(source.read_bytes()).hexdigest()}\n'
output=head+content
out=root/'outputs'/'source_reads';out.mkdir(parents=True,exist_ok=True)
dest=out/f'{a.label}_{source.stem}_{a.start:04d}-{end:04d}.txt'
dest.write_text(output)
with (root/'read_log.tsv').open('a') as f:
 f.write(f'{datetime.datetime.now(datetime.timezone.utc).isoformat()}\t{a.label}\t{source}\t{a.start}\t{end}\t{dest.relative_to(root)}\n')
print(output,end='')
