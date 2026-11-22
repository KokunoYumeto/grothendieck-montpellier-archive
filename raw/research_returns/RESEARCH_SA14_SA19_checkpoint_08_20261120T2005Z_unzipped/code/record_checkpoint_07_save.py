"""Record immutable checkpoint07 only after its persistent save succeeded."""
from pathlib import Path
import datetime,json
root=Path(__file__).resolve().parents[1]
p=root/'code/checkpoint_state.json';old=json.loads(p.read_text())
if old['checkpoint']<7:
 history=old.pop('history',[]);history.append(old)
 state=dict(checkpoint=7,created_utc='2026-11-20T19:18:12.819918+00:00',
  save_seen_succeeded_utc=datetime.datetime.now(datetime.timezone.utc).isoformat(),
  library_file_id='libfile_4c5e4f2d22688191aebf1be4673b1cc4',
  filename='RESEARCH_SA14_SA19_checkpoint_07.zip',
  next_target_utc='2026-11-20T20:02:47+00:00',
  next_formal_review_target_utc='2026-11-20T20:02:47+00:00',
  consecutive_reviews_without_movement=0,history=history)
 p.write_text(json.dumps(state,indent=2)+'\n')
else:state=old
print(json.dumps(state,indent=2))
