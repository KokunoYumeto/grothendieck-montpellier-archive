from pathlib import Path
import sys,datetime
base=Path('/workspace/scratch/c38eb4e8f07f')
path=base/sys.argv[1]
lo=int(sys.argv[2]) if len(sys.argv)>2 else 1
hi=int(sys.argv[3]) if len(sys.argv)>3 else 1000000
out='\n'.join(f'{i}: {s}' for i,s in enumerate(path.read_text().splitlines(),1) if lo<=i<=hi)
stamp=datetime.datetime.now(datetime.timezone.utc).strftime('%Y%m%dT%H%M%S%f')
log=base/'SA18_work/parts/agent45/outputs'/f'read_{stamp}_{path.name}_{lo}-{hi}.txt'
log.write_text(out+'\n')
print(out)
