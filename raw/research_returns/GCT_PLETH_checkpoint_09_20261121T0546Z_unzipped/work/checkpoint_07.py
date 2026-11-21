from pathlib import Path
import sys,csv,json,hashlib
from datetime import datetime,timezone
from zoneinfo import ZoneInfo
sys.path.insert(0,'work')
import build_package
now=datetime.now(timezone.utc)
assert now>=datetime(2026,11,21,4,16,8,tzinfo=timezone.utc),now
assert not Path('GCT_PLETH_checkpoint_07.zip').exists()
stamp=now.astimezone(ZoneInfo('Europe/Berlin')).isoformat()
p=Path('deliverables/LEDGER.md')
with p.open('a') as f:
 f.write(f'\n\n## Checkpoint07 — {stamp}\n\nThis checkpoint contains completed full central equal-row and adjacent-gap-one coefficient formulas G033/G034 with T054–T056; all ideal orders through three G032; the corrected generic-singleton statement T057; explicit even-tail preimages R037; and the actual higher-row canonical families R039–R041. All stated mathematical checks are recorded by their actual scope. Review03 recorded genuine main-gate movement and a zero no-movement streak; review04 is due05:01:08UTC. The generic four-parameter upper-cone certificate and the degree-three continuation of R041 remain active work until their full proofs and checks are completed and recorded.\n\nCurrent open rows at checkpoint:\n\n| Question | State | Current exact gate |\n|---|---|---|\n')
 for r in csv.DictReader(Path('deliverables/QUESTIONS.tsv').open(),delimiter='\t'):
  if not(r['state'].startswith('proved') or r['state'].startswith('specified assertion refuted') or r['state'].startswith('refuted')):
   f.write('| '+' | '.join(r[k].replace('|',' / ').replace('\n',' ') for k in ('id','state','finding_ids_or_current_gate'))+' |\n')
build_package.merge_events();build_package.manifest()
out=build_package.package('GCT_PLETH_checkpoint_07.zip')
record={'local_path':str(out),'created_at':stamp,'bytes':out.stat().st_size,'sha256':hashlib.sha256(out.read_bytes()).hexdigest()}
Path('work/checkpoint_07_local.json').write_text(json.dumps(record,indent=2)+'\n')
print(json.dumps(record))
