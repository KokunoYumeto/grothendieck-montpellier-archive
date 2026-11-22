"""Persist actual root audit events before the generated register is rebuilt."""
from pathlib import Path
import csv,datetime,json,shutil
w=Path(__file__).resolve().parents[1]
out=w/'outputs/CP31_root_audit_event_persistence.json'
assert not out.exists()
generated=list(csv.DictReader((w/'CHECK_EVENTS.tsv').open(),delimiter='\t'))
path=w/'notes/root_check_events.tsv'
root=list(csv.DictReader(path.open(),delimiter='\t'))
known={(r['statement_id'],r['date'],r['who']) for r in root}
audits=[json.loads((w/f'outputs/{n}').read_text()) for n in
 ['root_Moore_classification_audit.json','root_twisted_Cartier_Moore_audit.json']]
expected={(label,audit['actual_utc']) for audit in audits for label in audit['labels']}
selected=[r for r in generated if (r['statement_id'],r['date']) in expected]
assert len(selected)==len(expected)==11
new=[r for r in selected if (r['statement_id'],r['date'],r['who']) not in known]
snapshot=w/'notes/CP31_root_events_before_persistence.tsv';assert not snapshot.exists()
shutil.copy2(path,snapshot)
with path.open('a',newline='') as f:
 writer=csv.DictWriter(f,fieldnames=['statement_id','date','who','type','outcome'],delimiter='\t')
 writer.writerows(new)
record={'status':'PASS','actual_utc':datetime.datetime.now(datetime.timezone.utc).isoformat(),
 'persisted_actual_events':len(new),'total_matched_actual_events':len(selected),
 'scope':'The two already executed audit recorders appended to the generated CHECK_EVENTS register. These same events are now copied unchanged to the durable root input before any merge, preventing loss. No audit is rerun, redated or invented.',
 'events':selected}
out.write_text(json.dumps(record,indent=2)+'\n')
print(json.dumps({k:v for k,v in record.items() if k!='events'},indent=2))
