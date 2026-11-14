"""Supply required numeric arguments to retained lacuna marks; no new readings."""
import json,sys
from pathlib import Path
sys.path.insert(0,'PS_READERS_WORK/scripts')
from review_134_3_4 import save_review,OUT
empty=r'\illegible{}';counted=r'\illegible{1}'
def repair(v):
 if isinstance(v,str):return v.replace(empty,counted)
 if isinstance(v,list):return [repair(x) for x in v]
 if isinstance(v,dict):return {k:repair(x) for k,x in v.items()}
 return v
total=0
for path in sorted((OUT/'checked_pages').glob('ps_134-[34]_*.tex')):
 s=path.read_text();n=s.count(empty)
 if not n:continue
 key=path.stem;conf=repair(json.loads((OUT/'review_notes'/f'{key}.json').read_text()))
 extras=conf.setdefault('extra_records',[])
 for i,pos in enumerate([m for m in range(len(s)) if s.startswith(empty,m)],1):
  extras.append({'source_id':f'MECH:{key}:lacuna_count:{i}','before':empty,'after':counted,
   'line':s[:pos].count('\n')+1,'decision':'mechanical macro repair',
   'reason':'The supplied source convention requires a positive count argument. A retained unreadable word or partial-word cell receives count 1; its uncertain reading is unchanged.'})
 save_review(conf);total+=n
for path in (OUT/'scripts').glob('batch_*_134_4_review.py'):
 s=path.read_text()
 if empty in s:path.write_text(s.replace(empty,counted))
print('Repaired',total,'empty count arguments.')
