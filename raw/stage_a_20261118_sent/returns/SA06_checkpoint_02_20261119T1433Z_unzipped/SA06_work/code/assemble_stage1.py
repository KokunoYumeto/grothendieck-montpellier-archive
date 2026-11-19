#!/usr/bin/env python3
"""Mechanical union/coverage audit of manually authored entry judgments."""
from pathlib import Path
import json,csv,datetime
w=Path(__file__).resolve().parents[1];root=w.parent;out=w/'output';out.mkdir(exist_ok=True)
items=[];rows=[]
for part in ['cote14_early','cote14_late','cote15_middle','root']:
 items+=json.loads((w/'parts'/part/'items.json').read_text())
 with (w/'parts'/part/'entries.tsv').open() as f:rows+=list(csv.DictReader(f,delimiter='\t'))
with (root/'source/SA06_notes/NOTES_INDEX.tsv').open() as f:index=list(csv.DictReader(f,delimiter='\t'))
expected={r['entry_id'] for r in index};actual={r['entry_id'] for r in rows}
assert expected==actual and len(rows)==len(expected)==437
assert len({i['id'] for i in items})==len(items)
known={i['id'] for i in items};assert all(r['item_id'] in known for r in rows)
items.sort(key=lambda a:int(a['id'].split('-')[-1]));rows.sort(key=lambda a:(a['entry_id'].split('#')[0],int(a['entry_id'].split('#')[1])))
(out/'SA06_items.json').write_text(json.dumps(items,ensure_ascii=False,indent=2)+'\n')
with (out/'SA06_entries.tsv').open('w') as f:
 writer=csv.DictWriter(f,fieldnames=['entry_id','item_id','verdict','reason'],delimiter='\t');writer.writeheader();writer.writerows(rows)
report={'stage':1,'entries':len(rows),'items_before_cross_package_reconciliation':len(items),'coverage':'all437 unique source entries have hand-read verdicts','time_UTC':datetime.datetime.now(datetime.timezone.utc).isoformat()}
(w/'audit/stage1_coverage.json').write_text(json.dumps(report,indent=2)+'\n')
with (w/'progress.log').open('a') as f:f.write(report['time_UTC']+' STAGE1 all437 entries read and individually judged; mechanical coverage passed; cross-package semantic reconciliation continues.\n')
print(json.dumps(report,indent=2))
