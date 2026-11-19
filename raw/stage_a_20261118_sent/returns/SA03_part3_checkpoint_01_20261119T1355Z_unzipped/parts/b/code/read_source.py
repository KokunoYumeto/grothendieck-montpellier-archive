"""Line-numbered source reader used for this package; never assigns verdicts."""
from pathlib import Path
import argparse, datetime

p=argparse.ArgumentParser()
p.add_argument('file')
p.add_argument('--start',type=int,default=1)
p.add_argument('--end',type=int)
p.add_argument('--record',default='deliverable/parts/b/outputs/source_reads.txt')
a=p.parse_args()
lines=Path(a.file).read_text().splitlines()
end=min(a.end or len(lines),len(lines))
text=f'FILE {a.file} LINES {a.start}-{end}\n'+ '\n'.join(f'{i+1:5d} {lines[i]}' for i in range(a.start-1,end))+'\n'
with open(a.record,'a') as out: out.write(datetime.datetime.now(datetime.timezone.utc).isoformat()+'\n'+text+'\n')
print(text)
