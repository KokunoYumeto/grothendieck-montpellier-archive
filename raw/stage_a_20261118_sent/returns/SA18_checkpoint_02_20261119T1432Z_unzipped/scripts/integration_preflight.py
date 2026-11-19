"""Read-only integration diagnostics, without assigning scientific verdicts."""
from pathlib import Path
from collections import Counter,defaultdict
import json,csv,re
B=Path(__file__).resolve().parents[1]
owners={'root':'','agent16':'SA18_','agent45':'','agent46':''}
out={'owners':{},'entry_duplicates':[],'bibliography_key_collisions':{},'item_id_duplicates':[],'claim_id_duplicates':[]}
entries=[];items=[];claims=[];bib=defaultdict(list)
for who,prefix in owners.items():
 p=B/'parts'/who; record={}
 for name in ['items','claims','problems']:
  q=p/(prefix+name+'.json')
  xs=json.loads(q.read_text()); record[name]=len(xs)
  if name=='items':items+=xs
  if name=='claims':claims+=xs
 q=p/(prefix+'entries.tsv'); es=list(csv.DictReader(q.open(),delimiter='\t'));entries+=es;record['entries']=len(es)
 for q in p.glob('*.bib'):
  txt=q.read_text()
  for m in re.finditer(r'@\w+\{([^,]+),',txt):bib[m.group(1)].append(str(q.relative_to(B)))
 record['present_files']=[q.name for q in p.iterdir() if q.is_file()]
 out['owners'][who]=record
for field,xs,key in [('entry_duplicates',entries,'entry_id'),('item_id_duplicates',items,'id'),('claim_id_duplicates',claims,'id')]:
 out[field]=[k for k,n in Counter(x[key] for x in xs).items() if n>1]
out['bibliography_key_collisions']={k:v for k,v in bib.items() if len(v)>1}
out['total_entries']=len(entries)
assert len(entries)==335 and not out['entry_duplicates']
original=list(csv.DictReader((B.parent/'sources/SA18_notes/NOTES_INDEX.tsv').open(),delimiter='\t'))
assert {x['entry_id'] for x in entries}=={x['entry_id'] for x in original}
out['exact_original_index_coverage']=True
assert not out['item_id_duplicates'] and not out['claim_id_duplicates']
(B/'outputs/integration_preflight.json').write_text(json.dumps(out,indent=2))
print(json.dumps({k:v for k,v in out.items() if k!='owners'},indent=2))
