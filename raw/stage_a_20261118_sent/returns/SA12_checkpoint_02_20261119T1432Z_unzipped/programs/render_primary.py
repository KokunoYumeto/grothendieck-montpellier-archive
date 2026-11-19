#!/usr/bin/env python3
"""Render selected primary-source PDF pages for formula inspection; zero-based indices."""
import sys,pathlib,json,fitz,datetime
source=pathlib.Path(sys.argv[1]);out=pathlib.Path(sys.argv[2]);out.mkdir(parents=True,exist_ok=True)
doc=fitz.open(source)
records=[]
for n in map(int,sys.argv[3:]):
    target=out/f'{source.stem}_p{n:04}.png'
    doc[n].get_pixmap(matrix=fitz.Matrix(1.3,1.3)).save(str(target))
    records.append({'pdf':str(source),'page_zero_based':n,'image':str(target)})
print(json.dumps(records,indent=2))
log=pathlib.Path(__file__).resolve().parents[1]/'outputs'/'render_primary.jsonl'
with log.open('a') as f:
    f.write(json.dumps({'utc':datetime.datetime.now(datetime.timezone.utc).isoformat(),'records':records})+'\n')
