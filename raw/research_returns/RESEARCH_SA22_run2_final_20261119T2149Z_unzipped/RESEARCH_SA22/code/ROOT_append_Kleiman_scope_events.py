#!/usr/bin/env python3
"""Append the completed narrow Kleiman source checks; run no mathematics."""
from pathlib import Path
from datetime import datetime, timezone
import csv
import hashlib
import json
import time

root=Path(__file__).resolve().parents[1]
started=datetime.now(timezone.utc)
timer=time.perf_counter()
source=root/'notes/C_Kleiman1994_CHECK_EVENTS_proposal.tsv'
target=root/'C_CHECK_EVENTS.tsv'
sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest()
assert sha(source)=='2457fd3d19ded85507bc6a5d7b9fb7a22baa8d14099f3627e724f91945cccea4'
rows=list(csv.DictReader(source.open(),delimiter='\t'))
existing=list(csv.DictReader(target.open(),delimiter='\t'))
assert len(rows)==3
assert {r['statement_id'] for r in rows}=={'B:abelian','B:ancona-scope','B:criterion'}
assert all(r['type']=='targeted proof check' for r in rows)
assert all(r not in existing for r in rows)
before=sha(target)
assert target.read_bytes().endswith(b'\n')
with target.open('a',newline='') as stream:
    csv.DictWriter(stream,fieldnames=list(rows[0]),delimiter='\t').writerows(rows)
record={
 'started_utc':started.isoformat(),'finished_utc':datetime.now(timezone.utc).isoformat(),
 'elapsed_seconds':time.perf_counter()-timer,'added_events':3,
 'source':str(source.relative_to(root)),'source_sha256':sha(source),
 'target':str(target.relative_to(root)),'target_sha256_before':before,
 'target_sha256_after':sha(target),'mathematical_programs_run':0,
 'scope':'Record already completed selected-page source checks; no status or task-gate change.'
}
(root/'logs/ROOT_Kleiman_scope_event_append.json').write_text(json.dumps(record,indent=2)+'\n')
print(json.dumps(record,indent=2))
