from pathlib import Path
from datetime import datetime,timezone
import json
own=Path(__file__).resolve().parents[1]
path=own/'outputs/independent_common_Cartier_incidence_audit.json'
prior=own/'notes/common_incidence_audit.before_dependency_tail_completion.json'
assert not prior.exists();prior.write_bytes(path.read_bytes())
record=json.loads(path.read_text())
now=datetime.now(timezone.utc).isoformat()
record['initial_record_utc']=record['actual_utc']
record['actual_utc']=now
record['dependency_read_completion_note']='The final tail of the reused degree-one proposition (Oda simplicity and actual relative determinant) was reopened and read after the first audit JSON was written. This final timestamp, rather than the initial record timestamp, is the complete dependency-read audit time. No mathematical defect or code rerun occurred.'
path.write_text(json.dumps(record,indent=2)+'\n')
with (own/'CHECK_EVENTS.tsv').open('a') as f:
 for label in record['labels']:
  f.write('\t'.join((now,label,'FULL_AUDIT_FINAL_DEPENDENCY_READ','Final reused degree-one proof tail now read; complete independent PASS. Initial record retained and its timing explicitly corrected.','outputs/independent_common_Cartier_incidence_audit.json','No mathematical change; no computation'))+'\n')
print(json.dumps({'status':record['status'],'complete_audit_utc':now},indent=2))
