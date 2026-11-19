"""Numbered source reading with an audit copy. This program makes no verdicts."""
from pathlib import Path
import argparse, json
from datetime import datetime, timezone
p=argparse.ArgumentParser()
p.add_argument('file');p.add_argument('--start',type=int,default=1);p.add_argument('--end',type=int);p.add_argument('--out',required=True)
a=p.parse_args();root=Path(__file__).resolve().parents[2]
path=root/a.file; lines=path.read_text().splitlines();end=a.end or len(lines)
body='FILE '+str(path.relative_to(root))+'\n'+'\n'.join(f'{i}: {lines[i-1]}' for i in range(a.start,min(end,len(lines))+1))+'\n'
out=root/a.out;out.parent.mkdir(parents=True,exist_ok=True);out.write_text(body)
with (root/'work/source_access_log.tsv').open('a') as f:
    f.write('\t'.join([datetime.now(timezone.utc).isoformat(),a.file,str(a.start),str(end),a.out,'displayed for reading; not itself a mathematical check'])+'\n')
print(body)
