#!/usr/bin/env python3
"""Refresh the six integrated statement texts while preserving component IDs."""
from pathlib import Path
from datetime import datetime, timezone
import csv,json,re
root=Path(__file__).resolve().parents[1]
p=root/'B_results.csv';rows=list(csv.DictReader(p.open()));fields=list(rows[0])
paths=['notes/C_Greenberg_finite_uniform_fragment.tex','notes/ROOT_complete_Greenberg_points.tex','notes/C_Witt_localization_fragment.tex','notes/B_Suzuki_Greenberg_fragment.tex']
pattern=re.compile(r'\\begin\{(theorem|proposition|lemma)\}\[[^\n]*\]\\label\{([^}]+)\}(.*?)\\end\{\1\}',re.S)
updated=[]
for path in paths:
 for m in pattern.finditer((root/path).read_text()):
  label=m.group(2)
  found=[r for r in rows if r['where_proved'].endswith('label '+label)]
  assert len(found)==1,(label,len(found))
  found[0]['statement']=' '.join(m.group(3).split())
  updated.append({'id':found[0]['id'],'label':label})
with p.open('w',newline='') as f:
 w=csv.DictWriter(f,fields);w.writeheader();w.writerows(rows)
out={'updated_utc':datetime.now(timezone.utc).isoformat(),'statements':updated,'note':'Statement inventory refresh after actual typesetting fixes; no proof inferred from this program.'}
(root/'logs/ROOT_refresh_subject11_component.json').write_text(json.dumps(out,indent=2)+'\n')
print(json.dumps(out,indent=2))
