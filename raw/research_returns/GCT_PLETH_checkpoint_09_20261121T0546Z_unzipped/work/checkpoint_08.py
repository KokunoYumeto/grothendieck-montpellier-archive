from pathlib import Path
import sys,csv,json,hashlib
from datetime import datetime,timezone
from zoneinfo import ZoneInfo
sys.path.insert(0,'work');import build_package
now=datetime.now(timezone.utc)
assert now>=datetime(2026,11,21,5,1,8,tzinfo=timezone.utc),now
assert Path('work/REVIEW_04.json').exists()
assert not Path('GCT_PLETH_checkpoint_08.zip').exists()
stamp=now.astimezone(ZoneInfo('Europe/Berlin')).isoformat()
with Path('deliverables/LEDGER.md').open('a') as f:
 f.write('\n\n## Checkpoint08 — '+stamp+'\n\nThis checkpoint contains the complete outer-five coefficient formula G036 with G035/T058/T059, complete support G031, and the varying-outer-degree stable-hook formula G037 with T060, including exact matrices and binary-degree evaluators. The canonical-map portion includes the complete single-four band R044 and repeated-four block R045, with all finite endpoints, and R046 full isotypic surjectivity throughout D+t≤2n+1. A088 gives the actual invariant-base hook modules. Later fully checked reports present at this snapshot are listed in QUESTIONS.tsv and have their own actual events. Review04 records genuine main-gate movement and a zero no-movement streak. Review05 is due06:01:08UTC; Checkpoint09 is due05:46:08UTC. Active approaches are retained with their precise uncompleted steps.\n\nCurrent open rows at checkpoint:\n\n| Question | State | Current exact gate |\n|---|---|---|\n')
 for r in csv.DictReader(Path('deliverables/QUESTIONS.tsv').open(),delimiter='\t'):
  if not(r['state'].startswith('proved') or 'refuted' in r['state']):
   f.write('| '+' | '.join(r[k].replace('|',' / ').replace('\n',' ') for k in ('id','state','finding_ids_or_current_gate'))+' |\n')
build_package.merge_events();build_package.manifest()
out=build_package.package('GCT_PLETH_checkpoint_08.zip')
record={'local_path':str(out),'created_at':stamp,'bytes':out.stat().st_size,'sha256':hashlib.sha256(out.read_bytes()).hexdigest()}
Path('work/checkpoint_08_local.json').write_text(json.dumps(record,indent=2)+'\n')
print(json.dumps(record))

