"""Normalize actual event records, preserving original event descriptions."""
from pathlib import Path
import csv
B=Path(__file__).resolve().parent
sources=[B/'ROOT_CHECK_EVENTS.tsv',B/'evidence/lean_chain/CHECK_EVENTS.tsv',B/'evidence/unitary_audit/CHECK_EVENTS.tsv',B/'evidence/geometry_tower/CHECK_EVENTS.tsv',B/'evidence/main_gate/CHECK_EVENTS.tsv',B/'evidence/higher4/CHECK_EVENTS.tsv']
fields=['statement_id','date_utc','who','model','effort','type','outcome','evidence','original_type']
rows=[]
operations=[]
canonical={'targeted proof check','independent re-proof','computation or formal certificate',
           'used and rechecked in this run','carried as background without fault found'}
operational={'compute start','computation started','authorized cancellation of redundant computation',
             'bounded primary publisher/Crossref/repository retrieval','archive search'}
def category(typ):
 if typ in canonical or typ.startswith('refuted'):return typ
 if typ in operational:return None
 if any(t in typ for t in ['reported','association','promotion after']):
  return 'carried as background without fault found'
 if 'proof' in typ or typ in {'targeted whole-section check','source-located whole-theorem audit'}:
  return 'targeted proof check'
 if any(t in typ for t in ['computation','computational','replay','execution','certificate','exact controls']):
  return 'computation or formal certificate'
 if typ=='background citation':return 'carried as background without fault found'
 return 'used and rechecked in this run'
for p in sources:
 if not p.exists():continue
 for x in csv.DictReader(p.open(),delimiter='\t'):
  original=x.get('type','')
  typ=category(original)
  r={k:x.get(k,'') for k in fields}
  r['date_utc']=x.get('date_utc',x.get('date',''))
  r['who']=x.get('who','')
  if 'run ' not in r['who']:r['who']+='; run '+x.get('run','KTOWER')
  r['type']=typ or original
  r['original_type']=original
  r['evidence']=str(p.relative_to(B))+(' ; '+x['evidence'] if x.get('evidence') else '')
  (operations if typ is None else rows).append(r)
with (B/'CHECK_EVENTS.tsv').open('w',newline='') as f:
 w=csv.DictWriter(f,fieldnames=fields,delimiter='\t');w.writeheader();w.writerows(rows)
with (B/'OPERATIONS.tsv').open('w',newline='') as f:
 w=csv.DictWriter(f,fieldnames=fields,delimiter='\t');w.writeheader();w.writerows(operations)
print('Merged',len(rows),'actual check events and',len(operations),'separate operational records; original descriptions retained.')
