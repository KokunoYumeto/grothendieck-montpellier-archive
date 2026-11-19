"""Find numbered statements without an exactly matching check-event label.

This audits indexing only. It does not infer that an unmatched proof was unread,
and it does not manufacture a proof-check event from a label correspondence.
"""
from pathlib import Path
import csv,json,time
ROOT=Path(__file__).resolve().parents[1]
start=time.monotonic()
with (ROOT/'RESEARCH_SA05_results.csv').open(newline='') as f:results=list(csv.DictReader(f))
with (ROOT/'CHECK_EVENTS.tsv').open(newline='') as f:events=list(csv.DictReader(f,delimiter='\t'))
identifiers={e['statement_id'] for e in events}
unmatched=[{'id':r['id'],'where_proved':r['where_proved']} for r in results if r['id'] not in identifiers]
result={'numbered_statements':len(results),'check_events':len(events),'unmatched_numbered_labels':unmatched,
        'scope':'Exact event-label coverage only; no mathematical verification is inferred.',
        'seconds':round(time.monotonic()-start,4)}
(ROOT/'code/audit_check_coverage_output.json').write_text(json.dumps(result,indent=2)+'\n')
print(json.dumps(result,indent=2))
