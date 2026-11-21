"""Normalize actual event records, preserving original event descriptions."""
from pathlib import Path
import csv
B=Path(__file__).resolve().parent
sources=[B/'ROOT_CHECK_EVENTS.tsv',B/'evidence/lean_chain/CHECK_EVENTS.tsv',B/'evidence/unitary_audit/CHECK_EVENTS.tsv',B/'evidence/geometry_tower/CHECK_EVENTS.tsv',B/'evidence/main_gate/CHECK_EVENTS.tsv',B/'evidence/higher4/CHECK_EVENTS.tsv']
fields=['statement_id','date_utc','who','model','effort','type','outcome','evidence']
rows=[]
for p in sources:
 if not p.exists():continue
 for x in csv.DictReader(p.open(),delimiter='\t'):
  typ=x.get('type','')
  if typ in ['targeted whole-proof check','independent whole-proof check']:typ='targeted proof check'
  elif typ in ['computational replay','exact computation']:typ='computation or formal certificate'
  elif typ=='background citation':typ='carried as background without fault found'
  r={k:x.get(k,'') for k in fields}
  r['date_utc']=x.get('date_utc',x.get('date',''))
  r['who']=x.get('who','')+'; run '+x.get('run','KTOWER')
  r['type']=typ
  r['evidence']=str(p.relative_to(B))+(' ; '+x['evidence'] if x.get('evidence') else '')
  rows.append(r)
with (B/'CHECK_EVENTS.tsv').open('w',newline='') as f:
 w=csv.DictWriter(f,fieldnames=fields,delimiter='\t');w.writeheader();w.writerows(rows)
print('Merged',len(rows),'actual event records.')
