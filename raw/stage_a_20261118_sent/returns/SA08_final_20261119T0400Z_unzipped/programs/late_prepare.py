"""Create structural indexes only; all adjudications are separately authored."""
from pathlib import Path
import csv,json,re,datetime
ROOT=Path(__file__).resolve().parents[1]
OUT=ROOT/'work/late'
OUT.mkdir(parents=True,exist_ok=True)
rows=list(csv.DictReader((ROOT/'sources/notes/NOTES_INDEX.tsv').open(),delimiter='\t'))
for pkg in ['MPL_136_235-281','MPL_136_282-327']:
    note=(ROOT/f'sources/notes/pro/{pkg}_notes.md').read_text()
    heads=list(re.finditer(r'^### (.*)$',note,re.M))
    entries=[]
    for n,m in enumerate(heads,1):
        end=heads[n].start() if n<len(heads) else len(note)
        entries.append({'entry_id':f'{pkg}#{n}','heading':m[1],'note_line_start':note[:m.start()].count('\n')+1,'text':note[m.start():end]})
    expected=[x for x in rows if x['package']==pkg]
    assert {x['entry_id'] for x in expected}=={x['entry_id'] for x in entries}
    (OUT/f'{pkg}_entries_source.json').write_text(json.dumps(entries,ensure_ascii=False,indent=2))
    print(pkg,len(entries))
    for e in entries: print(e['entry_id'],e['heading'])
    tex=(ROOT/f'sources/texts/pro/{pkg}_transcription.tex').read_text().splitlines()
    scans=[]
    for i,line in enumerate(tex,1):
        m=re.search(r'\\scanpage\{(\d+)\}',line)
        if m: scans.append({'scan':int(m[1]),'line_start':i})
    for i,s in enumerate(scans):s['line_end']=scans[i+1]['line_start']-1 if i+1<len(scans) else len(tex)
    (OUT/f'{pkg}_scan_index.json').write_text(json.dumps(scans,indent=2))
    print('SCAN INDEX',json.dumps(scans))
print('Prepared at',datetime.datetime.now(datetime.timezone.utc).isoformat())
