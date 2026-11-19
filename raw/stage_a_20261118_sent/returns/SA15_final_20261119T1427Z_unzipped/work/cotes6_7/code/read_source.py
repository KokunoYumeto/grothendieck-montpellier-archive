#!/usr/bin/env python3
"""Numbered source extracts for manual review; no verdict generation."""
import argparse, datetime, pathlib, re
p=argparse.ArgumentParser();p.add_argument('kind',choices=['notes','tex','doubts']);p.add_argument('start',type=int);p.add_argument('end',type=int);a=p.parse_args()
root=pathlib.Path('/workspace/scratch/26604d0a9a98')
work=root/'work/cotes6_7'
name='MPL_6_038-067+7_001-060'
path=root/'sources'/('SA15_texts/pro' if a.kind=='tex' else 'SA15_notes/pro')/(name+('_transcription.tex' if a.kind=='tex' else f'_{a.kind}.md'))
lines=path.read_text().splitlines()
note=0;cote='';scan=''
out=[]
for n,line in enumerate(lines,1):
    if a.kind=='notes' and line.startswith('## '): note+=1
    m=re.match(r'\\cotefile\{([^}]+)\}',line)
    if m:cote=m.group(1)
    m=re.match(r'\\scanpage\{([^}]+)\}',line)
    if m:scan=m.group(1)
    if a.start<=n<=a.end:
        label=f'[{name}##{note}] ' if a.kind=='notes' else (f'[{cote}/{scan}] ' if a.kind=='tex' else '')
        out.append(f'{n}: {label}{line}')
s='\n'.join(out)+'\n'
(work/'outputs'/f'{a.kind}_{a.start}_{a.end}.txt').write_text(s)
with (work/'commands.log').open('a') as f:
    f.write(f'{datetime.datetime.now(datetime.timezone.utc).isoformat()} python code/read_source.py {a.kind} {a.start} {a.end}\n')
print(s,end='')
