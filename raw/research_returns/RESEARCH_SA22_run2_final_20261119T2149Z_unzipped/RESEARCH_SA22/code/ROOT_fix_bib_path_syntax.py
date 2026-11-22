#!/usr/bin/env python3
"""Escape the observed raw path underscores in bibliography note fields."""
from pathlib import Path
from datetime import datetime, timezone
import json,re
root=Path(__file__).resolve().parents[1]
p=root/'A567_references.bib';lines=p.read_text().splitlines(keepends=True)
changed=[]
for i,line in enumerate(lines):
 if re.search(r'^\s*note\s*=',line) and re.search(r'(?<!\\)_',line):
  assert '\\url{' not in line and '\\path{' not in line
  lines[i]=re.sub(r'(?<!\\)_',r'\\_',line)
  changed.append(i+1)
p.write_text(''.join(lines))
out={'updated_utc':datetime.now(timezone.utc).isoformat(),'file':p.name,'changed_lines':changed,'scope':'Typesetting only: escape literal filename underscores in the observed note field. No historical or mathematical content changed.'}
(root/'logs/ROOT_fix_bib_path_syntax.json').write_text(json.dumps(out,indent=2)+'\n')
print(json.dumps(out,indent=2))
