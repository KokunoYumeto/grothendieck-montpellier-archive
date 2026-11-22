"""Retain the successful fifth-checkpoint save without rewriting the archive."""
from pathlib import Path
import datetime,json,time
root=Path(__file__).resolve().parents[1]
started=time.perf_counter()
target=root/'logs/root_checkpoint05_receipt.json'
if target.exists():
    raise SystemExit('Receipt already recorded.')
receipt={'local_path':'/workspace/scratch/a7ef7e55112c/RESEARCH_SA23_checkpoint_05.zip',
 'purpose':'create_library_file','status':'succeeded',
 'file_id':'file_0000000013d482109736b1a7664ab9a9',
 'library_file_id':'libfile_d7fa01245bf08191bc2bba043755eb63',
 'file_name':'RESEARCH_SA23_checkpoint_05.zip','local_metadata_applied':True,
 'path':'/RESEARCH_SA23_checkpoint_05.zip','current_version_number':0}
history_path=root/'checkpoint_history.json'
history=json.loads(history_path.read_text())
entry=next(item for item in history if item['checkpoint']==5)
assert entry['bytes']==279693853
assert entry['sha256']=='da1db29ec461b54ae7d0538c50f435d4385e9abe11e57394518aa95b6ebb137e'
assert Path(receipt['local_path']).stat().st_size==entry['bytes']
entry.update({key:receipt[key] for key in ['file_id','library_file_id','current_version_number','local_metadata_applied']})
history_path.write_text(json.dumps(history,indent=2)+'\n')
record={'recorded_utc':datetime.datetime.now(datetime.timezone.utc).isoformat(),
        'ordered_results':[receipt],'archive_unchanged':True,
        'elapsed_seconds':time.perf_counter()-started}
target.write_text(json.dumps(record,indent=2)+'\n')
print(json.dumps(record,indent=2))
