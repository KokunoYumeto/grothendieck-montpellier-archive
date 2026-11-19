"""Print and retain the exact source chunks displayed for human/model review."""
import argparse,json
from pathlib import Path
from datetime import datetime,timezone
p=argparse.ArgumentParser()
p.add_argument('mode',choices=['entries','lines'])
p.add_argument('source');p.add_argument('start',type=int);p.add_argument('end',type=int)
a=p.parse_args()
root=Path(__file__).resolve().parents[2]
if a.mode=='entries':
    es=json.loads((root/'work'/a.source/'entries.json').read_text())
    text='\n\n'.join(f"ENTRY {e['id']} (notes source line {e['source_start']})\n{e['text']}" for e in es[a.start-1:a.end])
else:
    src=root/a.source
    text='\n'.join(f'{n}: {v}' for n,v in enumerate(src.read_text().splitlines(),1) if a.start<=n<=a.end)
stamp=datetime.now(timezone.utc).strftime('%Y%m%dT%H%M%S%fZ')
out=root/'deliverable/outputs/source_reads';out.mkdir(parents=True,exist_ok=True)
(out/f'{stamp}.txt').write_text(f'{a.mode} {a.source} {a.start} {a.end}\n\n'+text+'\n')
print(text)
