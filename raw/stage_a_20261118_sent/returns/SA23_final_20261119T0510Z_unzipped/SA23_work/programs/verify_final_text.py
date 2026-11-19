#!/usr/bin/env python3
"""Save the already performed final text/identifier check, without judging content."""
import datetime,json,re
from pathlib import Path
W=Path(__file__).resolve().parents[1]
rows=[]
for name in ['SA23_dossier.md','SA23_directions.md','SA23_editorial_directions.md']:
 s=(W/name).read_text()
 old=sorted(set(re.findall(r'\bMP-SA23-[a-z_]+-\d+',s)))
 markers=re.findall(r'.{0,70}(?:TODO|not yet searched|final completeness audit has not yet run|current working assembly|provisional deliverable).{0,70}',s,re.I)
 rows.append(dict(file=name,words=len(s.split()),unresolved_owner_problem_ids=old,unfinished_delivery_markers=markers))
report=dict(utc=datetime.datetime.now(datetime.timezone.utc).isoformat(),scope='Final rendered Markdown text and identifier check; not a mathematical completeness inference.',files=rows,passed=all(not x['unresolved_owner_problem_ids'] and not x['unfinished_delivery_markers']for x in rows))
(W/'outputs/final_text_validation.json').write_text(json.dumps(report,ensure_ascii=False,indent=2)+'\n')
print(json.dumps(report,ensure_ascii=False))
assert report['passed']
