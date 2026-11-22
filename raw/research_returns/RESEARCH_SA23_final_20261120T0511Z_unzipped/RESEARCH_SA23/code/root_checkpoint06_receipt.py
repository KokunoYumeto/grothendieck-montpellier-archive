"""Retain the successful sixth-checkpoint save without altering its ZIP."""
from pathlib import Path
import datetime, hashlib, json, time
root=Path(__file__).resolve().parents[1]
started=time.perf_counter()
target=root/'logs/root_checkpoint06_receipt.json'
if target.exists():
    raise SystemExit('Checkpoint06 receipt already recorded.')
receipt={'local_path':'/workspace/scratch/a7ef7e55112c/RESEARCH_SA23_checkpoint_06.zip',
         'purpose':'create_library_file','status':'succeeded',
         'file_id':'file_00000000df308210bf3ac19998d74803',
         'library_file_id':'libfile_ebacd78ffe708191b77c010a5b852403',
         'file_name':'RESEARCH_SA23_checkpoint_06.zip','local_metadata_applied':True,
         'path':'/RESEARCH_SA23_checkpoint_06.zip','current_version_number':0}
history_path=root/'checkpoint_history.json'
history=json.loads(history_path.read_text())
entry=next(row for row in history if row['checkpoint']==6)
archive=Path(receipt['local_path'])
assert entry['bytes']==archive.stat().st_size==284177595
assert entry['sha256']==hashlib.sha256(archive.read_bytes()).hexdigest()=='daacb316bd324b24c1cb95902ce41a6ddee10d135f35577ebec153f3e3fc05d4'
entry.update({key:receipt[key] for key in ['file_id','library_file_id','current_version_number','local_metadata_applied']})
history_path.write_text(json.dumps(history,indent=2)+'\n')
record={'recorded_utc':datetime.datetime.now(datetime.timezone.utc).isoformat(),
        'ordered_results':[receipt],'archive_unchanged':True,
        'elapsed_seconds':time.perf_counter()-started}
target.write_text(json.dumps(record,indent=2)+'\n')
print(json.dumps(record,indent=2))
