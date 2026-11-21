#!/usr/bin/env python3
"""Create a new complete checkpoint only when its actual 45-minute slot is due."""
from datetime import datetime, timezone, timedelta
from pathlib import Path
import hashlib
import json
import zipfile

base=Path(__file__).resolve().parent.parent
state=json.loads((base/'work/session.json').read_text())
started=datetime.fromisoformat(state['started_utc'])
history_path=base/'work/checkpoint_history.json'
history=json.loads(history_path.read_text()) if history_path.exists() else []
index=len(history)+1
due=started+timedelta(minutes=45*index)
now=datetime.now(timezone.utc)
if now<due:
    raise SystemExit(f'Not due: checkpoint{index:02} due {due.isoformat()}, now {now.isoformat()}')
path=base/f'CUE_GCT_checkpoint_{index:02}.zip'
if path.exists(): raise SystemExit('Refusing to overwrite an existing checkpoint')
entry={'index':index,'due_utc':due.isoformat(),'created_utc':now.isoformat(),
       'elapsed_minutes':(now-started).total_seconds()/60,'filename':path.name,'persistence':'upload pending'}
history.append(entry)
history_path.write_text(json.dumps(history,indent=2)+'\n')
with (base/'deliverables/LEDGER.md').open('a') as f:
    f.write(f'\n## Checkpoint{index:02} — {now.isoformat()}\n\n')
    f.write(f'Actual elapsed work: {entry["elapsed_minutes"]:.2f} minutes. Full current deliverables and documentation packaged; no earlier checkpoint included. Persistence result is recorded beside the checkpoint after upload.\n')
with zipfile.ZipFile(path,'x',compression=zipfile.ZIP_DEFLATED,compresslevel=6) as z:
    for dirname in ['deliverables','work','sources']:
        for p in sorted((base/dirname).rglob('*')):
            if p.is_file() and p.suffix!='.zip' and '__pycache__' not in p.parts:
                z.write(p,p.relative_to(base))
    prompt=base/'upload/PROMPT(20261121-004824).md'
    z.write(prompt,'REQUEST.md')
with zipfile.ZipFile(path) as z:
    assert z.testzip() is None
    assert not any('checkpoint_' in name and name.endswith('.zip') for name in z.namelist())
entry['sha256']=hashlib.sha256(path.read_bytes()).hexdigest()
entry['bytes']=path.stat().st_size
history_path.write_text(json.dumps(history,indent=2)+'\n')
print(json.dumps(entry))
