#!/usr/bin/env python3
"""Record one due mathematical review, rejecting early or duplicate records."""
from pathlib import Path
from datetime import datetime, timezone
import argparse, contextlib, io, json, runpy

R=Path(__file__).resolve().parents[1]
p=argparse.ArgumentParser()
p.add_argument('number',type=int)
p.add_argument('target_utc')
p.add_argument('assessment')
p.add_argument('--movement',choices=['YES','NO'],required=True)
p.add_argument('--dry-streak',type=int,required=True)
a=p.parse_args()
now=datetime.now(timezone.utc)
target=datetime.fromisoformat(a.target_utc)
if now<target: raise SystemExit('Refusing an early scheduled review')
receipt=R/'logs'/f'scheduled_review_{a.number:02d}.json'
if receipt.exists(): raise SystemExit('Refusing to overwrite a completed review')
assessment=R/a.assessment
if not assessment.is_file(): raise SystemExit('Missing review assessment')
if (a.movement=='YES' and a.dry_streak!=0) or (a.movement=='NO' and a.dry_streak<1):
    raise SystemExit('Inconsistent movement and streak')
with contextlib.redirect_stdout(io.StringIO()):
    data=runpy.run_path(str(R/'code/build_registers.py'))
tasks=data['TASKS']
if len(tasks)!=41: raise SystemExit('Expected all41 main and Lead rows')
table=['| Item | State | Statements | Current gate or scope |','|---|---|---|---|']
table += ['| '+' | '.join(str(y).replace('|','\\|') for y in x)+' |' for x in tasks]
assert len(table)==43
body=(f'\n## Scheduled mathematical review {a.number} — {now.isoformat()}\n\n'
      f'Target {target.isoformat()}. Qualifying movement: **{a.movement}**. '
      f'Consecutive dry reviews: **{a.dry_streak}**.\n\n'
      +assessment.read_text()+'\n\n'+'\n'.join(table)+'\n')
with (R/'PROGRESS_LEDGER.md').open('a') as f:f.write(body)
result={'review':a.number,'target_utc':target.isoformat(),'actual_utc':now.isoformat(),
        'movement':a.movement,'dry_streak':a.dry_streak,'task_and_lead_rows':41,
        'assessment':a.assessment,'stop_rule_reached':a.dry_streak>=2}
receipt.write_text(json.dumps(result,indent=2)+'\n')
print(json.dumps(result,indent=2))
