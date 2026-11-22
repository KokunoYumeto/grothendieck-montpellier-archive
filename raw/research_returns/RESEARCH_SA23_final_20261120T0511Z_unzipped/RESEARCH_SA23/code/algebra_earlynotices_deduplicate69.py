from pathlib import Path
from datetime import datetime, timezone
import json
root=Path(__file__).resolve().parents[1]
events=root/'notes/algebra_history_CHECK_EVENTS.tsv'
lines=events.read_text().splitlines()
match=[s for s in lines if 'geometry_analysis' in s and 'Geometry independently individually viewed all3 original AG5' in s]
geo=(root/'notes/geometry_CHECK_EVENTS.tsv').read_text().splitlines()
canonical=[s for s in geo if s.startswith('geo-H-history\t') and 'Visually read all three original AG5 pages' in s]
if len(match)!=1 or len(canonical)!=1:raise SystemExit('Expected unique duplicate and canonical event; no edit made')
events.write_text('\n'.join(s for s in lines if s not in match)+'\n')
note=root/'notes/algebra_earlynotices_source_audit.md'
with note.open('a') as f:f.write('\nDocumentary event deduplication: geometry had already recorded its independent AG5 reading in `notes/geometry_CHECK_EVENTS.tsv`. The duplicate report-only row in the algebra event fragment was removed; its visual check remains documented in this audit and in geometry\'s canonical event. See `code/algebra_earlynotices_deduplicate69.py` and `logs/algebra_earlynotices_deduplicate69.json`. This does not remove or repeat an actual source check.\n')
out={'utc_recorded':datetime.now(timezone.utc).isoformat(),'removed_duplicate_events':1,'canonical_event_file':'notes/geometry_CHECK_EVENTS.tsv','paper_or_bib_changed':False}
(root/'logs/algebra_earlynotices_deduplicate69.json').write_text(json.dumps(out,indent=2)+'\n')
print(json.dumps(out,indent=2))
