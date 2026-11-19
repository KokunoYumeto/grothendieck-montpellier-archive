from pathlib import Path
import sys, datetime

path=Path(sys.argv[1]); start=int(sys.argv[2]); stop=int(sys.argv[3])
lines=path.read_text().splitlines()
text='\n'.join(f'{i+1:04d} {lines[i]}' for i in range(start-1,min(stop,len(lines))))+'\n'
out=Path(__file__).parent/'evidence'/f'{path.name}.{start}-{stop}.txt'
out.parent.mkdir(parents=True,exist_ok=True); out.write_text(text)
with (Path(__file__).parent/'commands.log').open('a') as f:
 f.write(datetime.datetime.now(datetime.timezone.utc).isoformat()+' python3 agents/p18/read_source.py '+str(path)+' '+str(start)+' '+str(stop)+' -> '+str(out)+'\n')
print(text)
