"""Number and log source spans. Reading aids only; makes no verdicts."""
from pathlib import Path
from datetime import datetime, timezone
import argparse, re, json

ROOT=Path(__file__).resolve().parents[3]
WORK=Path(__file__).resolve().parents[1]
p=argparse.ArgumentParser()
p.add_argument('source')
p.add_argument('start', type=int)
p.add_argument('end', type=int)
p.add_argument('--label', default='read')
a=p.parse_args()
source=ROOT/a.source
lines=source.read_text().splitlines()
out='\n'.join(f'{i}: {lines[i-1]}' for i in range(a.start,min(a.end,len(lines))+1))+'\n'
name=f'{source.stem}_{a.start:04d}_{min(a.end,len(lines)):04d}.txt'
(WORK/'outputs'/name).write_text(out)
log=WORK/'source_read_log.tsv'
if not log.exists():
    log.write_text('date_utc\tsource\tstart_line\tend_line\treader\tnote\n')
with log.open('a') as f:
    f.write('\t'.join([datetime.now(timezone.utc).isoformat(),a.source,str(a.start),str(min(a.end,len(lines))),'GPT-6 Astra Pro / cotes8_9_4',a.label])+'\n')
print(out,end='')
