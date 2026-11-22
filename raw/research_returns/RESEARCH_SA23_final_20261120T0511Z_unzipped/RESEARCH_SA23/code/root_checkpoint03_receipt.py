"""Retain the verified receipt of the third scheduled checkpoint."""
from pathlib import Path
import datetime, json
root=Path(__file__).resolve().parents[1]
receipt={
 'local_path':str(root.parent/'RESEARCH_SA23_checkpoint_03.zip'),
 'purpose':'create_library_file','status':'succeeded',
 'file_id':'file_0000000020ec820abd2e973eb3f090fa',
 'library_file_id':'libfile_4e3aa19788a88191a97c589855693492',
 'file_name':'RESEARCH_SA23_checkpoint_03.zip',
 'local_metadata_applied':True,'path':'/RESEARCH_SA23_checkpoint_03.zip',
 'current_version_number':0,
 'receipt_recorded_utc':datetime.datetime.now(datetime.timezone.utc).isoformat()
}
path=root/'checkpoint_history.json'
history=json.loads(path.read_text())
record=next(r for r in history if r['checkpoint']==3)
record.update({k:receipt[k] for k in ['file_id','library_file_id','current_version_number','local_metadata_applied']})
path.write_text(json.dumps(history,indent=2)+'\n')
(root/'logs'/'root_checkpoint03_receipt.json').write_text(json.dumps(receipt,indent=2)+'\n')
print(json.dumps(receipt))
