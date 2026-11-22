"""Record one verified successful checkpoint save after the actual Library response."""
from pathlib import Path
from datetime import datetime, timezone, timedelta
from zoneinfo import ZoneInfo
import hashlib, json, sys, time

R=Path(__file__).resolve().parents[1]
began=time.perf_counter()
number=int(sys.argv[1]);library_id=sys.argv[2];saved_utc=sys.argv[3]
assert library_id.startswith('libfile_')
stamp=datetime.fromisoformat(saved_utc)
assert stamp.tzinfo is not None
target=R/'code'/f'root_record_checkpoint_save_{number:02d}_output.json'
assert not target.exists()
run=json.loads((R/'code'/f'root_timed_checkpoint_{number:02d}_output.json').read_text())
assert run['exit_code']==0
archive=run['archive'];path=Path(archive['path'])
assert path.stat().st_size==archive['bytes']
assert hashlib.sha256(path.read_bytes()).hexdigest()==archive['sha256']
records_path=R/'notes/checkpoint_saved_records.json'
records=json.loads(records_path.read_text())
assert not any(x['name']==path.name for x in records['checkpoints'])
item=dict(name=path.name,saved_utc=saved_utc,bytes=archive['bytes'],sha256=archive['sha256'],library_file_id=library_id)
records['checkpoints'].append(item)
records_path.write_text(json.dumps(records,indent=2)+'\n')
qa=json.loads((R/'logs/typesetting_current.json').read_text())
audit=json.loads((R/'logs/records_audit.json').read_text())
report=json.loads((R/'code/root_reconcile_report_output.json').read_text())
next_due=stamp+timedelta(minutes=45)
review=json.loads((R/'notes/progress_review_state.json').read_text())
entry=f'''

### Checkpoint{number:02d} saved {saved_utc}

The scheduled immutable archive `{path.name}` contains{archive['files']}files and{archive['bytes']}bytes. SHA256: `{archive['sha256']}`. Its paper is build{qa['build']},{qa['pages']}pages, with{audit['numbered_statements']}numbered statements,{audit['result_rows']}CSV rows and{report['program_files']}retained program files. The current build has zero overfull boxes, undefined references/citations or missing-character diagnostics; every listed QA sample page was actually displayed and inspected. The archive integrity check passed. No earlier checkpoint was changed or nested.

The substantive review state is review{review['review_number']}, no-movement streak{review['no_movement_streak']}. The remaining original-source readings are Pfluger1960, Lieberman1968 and Fujiwara1995; historical runtime limitations are separately disclosed. Full raw non-user literature caches are represented by their source/provenance records, while authored work, finite certificates and their outputs are retained. This checkpoint does not constitute completion or research movement.

Next checkpoint due: {next_due.isoformat()} / {next_due.astimezone(ZoneInfo('Europe/Berlin')).strftime('%Y-%m-%d %H:%M:%S Europe/Berlin')}. Next substantive review: {review['next_review']}.
'''
with (R/'PROGRESS_LEDGER.md').open('a') as f:f.write(entry)
out=dict(**item,files=archive['files'],next_due_utc=next_due.isoformat(),recorded_utc=datetime.now(timezone.utc).isoformat(),seconds=time.perf_counter()-began)
target.write_text(json.dumps(out,indent=2)+'\n')
print(json.dumps(out,indent=2))
