from pathlib import Path
import csv,json,sys
sys.path.insert(0,'out')
from tex_elements import page_path,arguments,stamp
d=json.load(sys.stdin);n=d['n'];p=page_path(n,'out/pages');s=p.read_text()
for old,new in d['edits']:
 assert s.count(old)==1,(old,s.count(old))
 s=s.replace(old,new,1)
p.write_text(s)
tab=Path('out/audit/frozen_places.tsv'); rr=list(csv.DictReader(tab.open(),delimiter='\t'));fields=list(rr[0])
for key,updates in d.get('slots',{}).items():
 row=next((r for r in rr if r['id']==key),None)
 if row is None:row={'scan':str(n),'id':key,'type':'unsure'};rr.append(row)
 row.update(updates)
 assert (Path('crops')/row['crop']).exists()
rr.sort(key=lambda r:(int(r['scan']),r['id']))
with tab.open('w',newline='') as f:
 w=csv.DictWriter(f,fields,delimiter='\t');w.writeheader();w.writerows(rr)
assert [v for a,b,k,v in arguments(s,{'unsure','illegible'})]==[r['frozen reading'] for r in rr if r['scan']==str(n)]
with open('out/K58-03_audit.md','a') as f:
 print(f"\n### Scan {n}, supplementary comparison, {stamp()}\n\n"+d['note']+'\n',file=f)
 for old,new in d['edits']:print(chr(96)+old+chr(96)+' → '+chr(96)+new+chr(96)+'\n',file=f)
