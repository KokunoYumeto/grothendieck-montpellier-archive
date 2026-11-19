#!/usr/bin/env python3
"""Reproducible source inventory; does not generate research judgements."""
from pathlib import Path
import csv,collections,re,json,hashlib
root=Path(__file__).resolve().parents[1]
src=root.parent/'source'
with (src/'SA12_notes/NOTES_INDEX.tsv').open() as f:
 rows=list(csv.DictReader(f,delimiter='\t'))
data={'entries':len(rows),'packages':dict(collections.Counter(r['package'] for r in rows)),'files':[]}
for p in sorted(src.rglob('*')):
 if not p.is_file(): continue
 s=p.read_text()
 data['files'].append({'path':str(p.relative_to(src)),'bytes':p.stat().st_size,'lines':len(s.splitlines()),'sha256':hashlib.sha256(p.read_bytes()).hexdigest(),'scan_markers':re.findall(r'\\scanpage\{([^}]+)\}',s)})
output=json.dumps(data,ensure_ascii=False,indent=2)+'\n'
(root/'outputs/inventory.json').write_text(output)
print(output)
