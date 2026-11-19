"""Check direction numbering and register references; no ranking or scholarly decisions."""
from pathlib import Path
import re,json
base=Path('/workspace/scratch/594d1dc856a9/SA04_work')
doc=base/'final/SA04_directions.md'
s=doc.read_text()
known=set()
for part in ['a','b','c','root']:
 for name in ['items.json','claims.json','problems.json']:
  p=base/'parts'/part/name
  if p.exists():
   known.update(x['id'] for x in json.loads(p.read_text()))
for name in ['root_supplement_items.json','root_supplement_claims.json','root_supplement_problems.json']:
 known.update(x['id'] for x in json.loads((base/'parts/b'/name).read_text()))
used=set(re.findall(r'\b(?:MP-|C-)?SA04-\d+\b',s))
unknown=sorted(used-known)
heads=[int(x) for x in re.findall(r'^## (\d+)\.',s,re.M)]
assert heads==list(range(1,31)),heads
assert not unknown,unknown
for n in range(1,31):
 text=s.split(f'## {n}.',1)[1].split('\n## ',1)[0]
 assert '**Starting records:**' in text
 assert '**Provenance:**' in text
 assert '**Establish:**' in text
 assert '**Known limits:**' in text
 assert '**First step:**' in text
 assert 'feasibility' in text
 assert f'Interest {n};' in text
result={'directions':len(heads),'distinct_referenced_register_ids':len(used),'unknown_ids':unknown,'words':len(s.split()),'separate_interest_and_feasibility':True,'structure':'pass','scope':'Numbering and ID/field validation only; rankings and consolidation were reasoned manually.'}
(base/'outputs/b_directions_validation.json').write_text(json.dumps(result,indent=2)+'\n')
print(json.dumps(result,indent=2))
