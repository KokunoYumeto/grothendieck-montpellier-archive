import json,csv,sys
from pathlib import Path
sys.path.insert(0,'out')
from tex_elements import arguments,page_path,blocks
n=int(sys.argv[1]);raw=page_path(n,'out/pages').read_text()
data=json.load(sys.stdin)
marks=list(arguments(raw,{'unsure','illegible'}))
if len(marks)!=len(data):raise ValueError(f'{n}: {len(marks)} marks, {len(data)} descriptions')
path=Path('out/audit/frozen_places.tsv');init=not path.exists()
bs=blocks(raw)
with path.open('a',newline='') as f:
 w=csv.writer(f,delimiter='\t')
 if init:w.writerow(['scan','id','place','type','frozen reading','crop','stroke','confidence','context'])
 for j,((a,b,typ,val),row) in enumerate(zip(marks,data),1):
  label,crop,stroke,conf,context=row
  p=Path('crops')/f'{n:03}_{crop}.png'
  if not p.is_file():raise ValueError(str(p))
  w.writerow([n,f'{n}.{j:02}',label,typ,val,p.name,stroke,conf,context])
