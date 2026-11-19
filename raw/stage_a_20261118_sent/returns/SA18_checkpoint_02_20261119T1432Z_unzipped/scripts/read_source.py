"""Print source lines or selected entries with exact stable source coordinates."""
from pathlib import Path
import argparse,json
ROOT=Path(__file__).resolve().parents[2]
p=argparse.ArgumentParser()
p.add_argument('--file');p.add_argument('--start',type=int,default=1);p.add_argument('--end',type=int)
p.add_argument('--package');p.add_argument('--entries',help='Inclusive comma-separated numbers/ranges')
p.add_argument('--cote');p.add_argument('--scan')
a=p.parse_args()
if a.entries:
    selected=set()
    for part in a.entries.split(','):
        lo,_,hi=part.partition('-');selected.update(range(int(lo),int(hi or lo)+1))
    entries=json.loads((ROOT/'SA18_work/research/parsed_entries.json').read_text())
    for e in entries:
        pkg,n=e['entry_id'].rsplit('#',1)
        if pkg==a.package and int(n) in selected:
            print('\nENTRY',e['entry_id'],'FILE',e['file'])
            for i,line in enumerate(e['text'].splitlines(),e['start_line']):print(f'{i:5}: {line}')
else:
    file=ROOT/'sources'/a.file
    lines=file.read_text().splitlines()
    if a.scan:
        pages=json.loads((ROOT/'SA18_work/research/page_index.json').read_text())
        selected=[x for x in pages if x['file']==a.file and x['scan']==a.scan and (a.cote is None or x['cote']==a.cote)]
        assert len(selected)==1,selected
        a.start=selected[0]['start_line'];a.end=selected[0]['end_line']
    print('FILE',a.file)
    for i in range(a.start-1,min(a.end or len(lines),len(lines))):print(f'{i+1:5}: {lines[i]}')
