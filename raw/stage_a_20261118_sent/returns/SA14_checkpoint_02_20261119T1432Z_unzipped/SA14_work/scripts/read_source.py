"""Print source ranges and record exactly what was displayed for close reading."""
from pathlib import Path
import argparse, datetime, json
p=argparse.ArgumentParser();p.add_argument('file');p.add_argument('--start',type=int,default=1);p.add_argument('--end',type=int);p.add_argument('--reader',default='root');a=p.parse_args()
root=Path(__file__).resolve().parents[2];work=root/'SA14_work';f=root/a.file
lines=f.read_text().splitlines();end=min(a.end or len(lines),len(lines))
text=f'FILE {a.file}; PHYSICAL LINES {a.start}-{end}\n'+'\n'.join(f'{n}: {lines[n-1]}' for n in range(a.start,end+1))+'\n'
dest=work/'outputs'/'reads'/a.reader;dest.mkdir(parents=True,exist_ok=True)
(dest/f'{f.stem}_{a.start}-{end}.txt').write_text(text)
with (work/'research/read_events.jsonl').open('a') as h:h.write(json.dumps({'utc':datetime.datetime.now(datetime.timezone.utc).isoformat(),'reader':a.reader,'file':a.file,'start':a.start,'end':end,'event':'displayed for manual close reading; no automatic verdict'})+'\n')
print(text)
