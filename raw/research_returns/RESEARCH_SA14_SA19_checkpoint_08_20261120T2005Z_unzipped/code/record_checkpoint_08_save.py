"""Record checkpoint08 only after its persistent save is observed successful."""
from pathlib import Path
import datetime,json,sys,zipfile
root=Path(__file__).resolve().parents[1]
library_id=sys.argv[1]
assert library_id.startswith('libfile_')
with zipfile.ZipFile(root/'RESEARCH_SA14_SA19_checkpoint_08.zip') as archive:
    meta=json.loads(archive.read('CHECKPOINT_STATUS.json'))
review=json.loads((root/'code/formal_review_04.json').read_text())
p=root/'code/checkpoint_state.json'
old=json.loads(p.read_text())
if old['checkpoint']<8:
    history=old.pop('history',[])
    history.append(old)
    state=dict(checkpoint=8,created_utc=meta['created_utc'],
        save_seen_succeeded_utc=datetime.datetime.now(datetime.timezone.utc).isoformat(),
        library_file_id=library_id,filename='RESEARCH_SA14_SA19_checkpoint_08.zip',
        next_target_utc='2026-11-20T20:47:47+00:00',
        next_formal_review_target_utc=review['next_review_target_utc'],
        consecutive_reviews_without_movement=review['consecutive_reviews_without_movement'],
        history=history)
    p.write_text(json.dumps(state,indent=2)+'\n')
else:
    state=old
print(json.dumps(state,indent=2))
