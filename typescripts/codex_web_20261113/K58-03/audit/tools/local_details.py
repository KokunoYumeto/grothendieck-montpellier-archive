import csv,json,sys,subprocess
from pathlib import Path
sys.path.insert(0,"out")
from tex_elements import arguments,page_path
n=int(sys.argv[1]); marks=list(arguments(page_path(n,'out/pages').read_text(),{'unsure','illegible'}))
rows=json.load(sys.stdin)
assert len(rows)==len(marks),(len(rows),len(marks))
coords={r[1].split('_',1)[1][:-4]:list(map(int,r[2:7])) for r in list(csv.reader(open('out/crop_coordinates.tsv'),delimiter='\t'))[1:] if int(r[0])==n}
items=[]; details=[]
for j,(row,mark) in enumerate(zip(rows,marks),1):
 spec,location,stroke,confidence,context=row
 if '@' in spec:
  base,portion=spec.split('@');x,y,r,b,angle=coords[base];assert not angle
  x1,y1,x2,y2=map(float,portion.split(','))
  box=[max(0,round(x+(r-x)*x1)),max(0,round(y+(b-y)*y1)),round(x+(r-x)*x2),round(y+(b-y)*y2)]
  spec=f'place{j:02}'; items.append([spec,box])
 details.append([location,spec,stroke,{'l':'low','m':'medium','h':'high'}[confidence],context])
if items:
 subprocess.run([sys.executable,'work/crop.py',str(n)],input=json.dumps(items),text=True,check=True)
subprocess.run([sys.executable,'work/doubt_details.py',str(n)],input=json.dumps(details),text=True,check=True)
print(n, len(rows), 'local entries;', len(items),'additional tight crops')
