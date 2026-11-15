"""Create an immutable complete checkpoint, excluding input archives and old ZIPs."""
from pathlib import Path
from archive_contents import write_zip
import csv, json, hashlib, datetime
root=Path(__file__).resolve().parents[1]
dest=root.parent
existing=list(dest.glob('PS_READERS_checkpoint_*.zip'))
numbers=[int(p.stem.rsplit('_',1)[1]) for p in existing]
for statefile in [root/'records/CHECKPOINT_STATE.json',root/'records/RECOVERY_STATE.json']:
    if statefile.exists():
        state=json.loads(statefile.read_text())
        if state.get('checkpoint'):numbers.append(int(Path(state['checkpoint']).stem.rsplit('_',1)[1]))
        numbers.append(state.get('reserved_checkpoint_number',0))
history=root/'records/CHECKPOINT_HISTORY.jsonl'
if history.exists():
    for line in history.read_text().splitlines():
        item=json.loads(line);numbers.append(int(Path(item['checkpoint']).stem.rsplit('_',1)[1]))
number=max(numbers+[0])+1
name=f'PS_READERS_checkpoint_{number:02d}.zip'
pages=list((root/'checked_pages').glob('*.tex'))
gatepath=root/'records/FINAL_QA_GATE.json'
gate_complete=gatepath.exists() and json.loads(gatepath.read_text()).get('complete') is True
status={'checkpoint':name,'created_utc':datetime.datetime.now(datetime.timezone.utc).isoformat(),'checked_page_files':len(pages),'page_keys':[p.stem for p in sorted(pages)],'status':'completed edition; consult the final QA gate and per-PDF ledgers' if gate_complete else 'in progress; consult page and PDF ledgers for verified scope'}
(root/'records/CHECKPOINT_STATE.json').write_text(json.dumps(status,indent=2)+'\n')
result=write_zip(root,dest/name)
print(json.dumps({'checkpoint':name,'checked_pages':len(pages),**result}))
