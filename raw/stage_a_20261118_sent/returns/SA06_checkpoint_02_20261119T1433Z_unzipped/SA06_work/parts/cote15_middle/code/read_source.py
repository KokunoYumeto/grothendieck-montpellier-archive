from pathlib import Path
import sys,re,datetime,json
ROOT=Path('/workspace/scratch/a5176e5b5d45')
PART=ROOT/'SA06_work/parts/cote15_middle'
kind,name,start,end=sys.argv[1],sys.argv[2],int(sys.argv[3]),int(sys.argv[4])
base=ROOT/'source'
if kind=='tex':
    path=next((base/'SA06_texts').glob('*/'+name+'_transcription.tex'))
elif kind in ('notes','doubts'):
    path=next((base/'SA06_notes').glob('*/'+name+'_'+kind+'.md'))
else: raise ValueError(kind)
lines=path.read_text().splitlines()
text='\n'.join(f'{i+1:04d} {s}' for i,s in enumerate(lines) if start<=i+1<=end)
out=PART/'audit'/f'{name}_{kind}_{start:04d}-{end:04d}.txt'
out.write_text(text+'\n')
with (PART/'progress.log').open('a') as f:f.write(datetime.datetime.now(datetime.timezone.utc).isoformat()+f'\tSOURCE_READ\t{path.name} lines {start}-{min(end,len(lines))}\n')
print(text)
