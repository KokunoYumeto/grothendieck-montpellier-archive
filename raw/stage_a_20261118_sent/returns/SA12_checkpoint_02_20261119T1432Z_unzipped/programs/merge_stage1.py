#!/usr/bin/env python3
"""Assemble independently read judgments and verify the index bijection."""
from pathlib import Path
import csv,json,collections,datetime
root=Path(__file__).resolve().parents[1]
entries=[];items=[]
for folder in ('29a','29b','31','33'):
    d=root/'reviews'/folder
    entries+=list(csv.DictReader((d/'entries.tsv').open(),delimiter='\t'))
    items+=json.loads((d/'items.json').read_text())
index=list(csv.DictReader((root.parent/'source/SA12_notes/NOTES_INDEX.tsv').open(),delimiter='\t'))
expected={r['entry_id'] for r in index}
actual=[r['entry_id'] for r in entries]
assert len(actual)==342 and len(set(actual))==342 and set(actual)==expected
assert len({i['id'] for i in items})==len(items)
assert all(r['item_id'] in {i['id'] for i in items} for r in entries)
with (root/'SA12_entries.tsv').open('w') as f:
    w=csv.DictWriter(f,fieldnames=['entry_id','item_id','verdict','reason'],delimiter='\t');w.writeheader();w.writerows(entries)
(root/'SA12_items.json').write_text(json.dumps(items,ensure_ascii=False,indent=2)+'\n')
result={'entries':len(entries),'items':len(items),'entry_verdicts':dict(collections.Counter(r['verdict'] for r in entries)),'index_bijection':True,'utc':datetime.datetime.now(datetime.timezone.utc).isoformat()}
(root/'outputs/stage1_merge.json').write_text(json.dumps(result,indent=2)+'\n');print(json.dumps(result,indent=2))
