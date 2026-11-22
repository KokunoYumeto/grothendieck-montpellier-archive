"""Record checkpoint 06 after the persistent save reported success."""
from pathlib import Path
import datetime, json
root = Path(__file__).resolve().parents[1]
p = root / 'code/checkpoint_state.json'
old = json.loads(p.read_text())
if old['checkpoint'] < 6:
    history = old.pop('history', [])
    history.append(old)
    state = dict(checkpoint=6,
        created_utc='2026-11-20T18:36:42.739714+00:00',
        save_seen_succeeded_utc=datetime.datetime.now(datetime.timezone.utc).isoformat(),
        library_file_id='libfile_258c31539e40819183b8c5124198d5e0',
        filename='RESEARCH_SA14_SA19_checkpoint_06.zip',
        next_target_utc='2026-11-20T19:17:47+00:00',
        next_formal_review_target_utc='2026-11-20T19:02:47+00:00',
        consecutive_reviews_without_movement=0,
        history=history)
    p.write_text(json.dumps(state, indent=2) + '\n')
else:
    state = old
print(json.dumps(state, indent=2))
