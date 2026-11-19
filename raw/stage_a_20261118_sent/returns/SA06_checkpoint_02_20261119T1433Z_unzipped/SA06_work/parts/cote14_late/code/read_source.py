from pathlib import Path
import argparse, re, datetime
root=Path('/workspace/scratch/a5176e5b5d45/source')
part=Path(__file__).resolve().parents[1]
p=argparse.ArgumentParser(); p.add_argument('path');p.add_argument('start',type=int);p.add_argument('end',type=int);p.add_argument('--entries',action='store_true');a=p.parse_args()
s=(root/a.path).read_text()
if a.entries:
    entries=re.split(r'(?m)^### ',s)[1:]
    text='\n\n'.join(f'ENTRY {i}\n### '+entries[i-1] for i in range(a.start,min(a.end,len(entries))+1))
else:
    lines=s.splitlines();text='\n'.join(f'{i}: {lines[i-1]}' for i in range(a.start,min(a.end,len(lines))+1))
out=part/'audit'/f'{Path(a.path).stem}_{"entries" if a.entries else "lines"}_{a.start}-{a.end}.txt'
out.write_text(text+'\n')
with (part/'progress.log').open('a') as f:f.write(datetime.datetime.now(datetime.timezone.utc).isoformat()+f'\tREAD\t{a.path}:{a.start}-{a.end}; entries={a.entries}\n')
print(text)
