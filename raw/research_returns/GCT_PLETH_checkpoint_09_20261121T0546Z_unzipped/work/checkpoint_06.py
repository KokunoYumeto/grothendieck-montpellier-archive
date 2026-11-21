from pathlib import Path
import sys, csv, json, hashlib
from datetime import datetime, timezone
from zoneinfo import ZoneInfo
sys.path.insert(0,'work')
import build_package
now=datetime.now(timezone.utc)
assert now>=datetime(2026,11,21,3,31,8,tzinfo=timezone.utc), now
stamp=now.astimezone(ZoneInfo('Europe/Berlin')).isoformat()
qa=Path('work/PDF_QA.md')
qa.write_text(qa.read_text()+f"\n\n## Checkpoint06 compilation and visual sample — {stamp}\n\nThe current510-page PDF completed three XeLaTeX passes. Root visually inspected page244, including the complete charged-oscillator parameter dictionary, operator display and actual module comparison. The sampled equations and catalog continuation fit the margins. Large overfull displays and the long boundary table were corrected. Seven older minor overfull boxes remain, largest15.36pt; a complete visual-clearance claim is not made for this working checkpoint. Mathematical whole-proof readings are recorded separately.\n")
p=Path('deliverables/LEDGER.md')
with p.open('a') as f:
 f.write(f"\n\n## Checkpoint06 — {stamp}\n\nThe six-hour checkpoint includes G031 complete outer-five support, G030/T051 complete ideal-order-two and three-below formulas, T052/T053 exact charged oscillator and incidence/Rees comparisons, and R033–R035 actual canonical-map families. Independent whole-proof reviews through A063 are included. R036 is active research and is not a checked finding in this checkpoint. Review03 remains due04:01:08UTC; the prior review recorded genuine main-gate movement and a zero no-movement streak.\n\nCurrent open rows at checkpoint:\n\n| Question | State | Current exact gate |\n|---|---|---|\n")
 for r in csv.DictReader(Path('deliverables/QUESTIONS.tsv').open(),delimiter='\t'):
  if not (r['state'].startswith('proved') or r['state'].startswith('specified assertion refuted') or r['state'].startswith('refuted')):
   vals=[r['id'],r['state'],r['finding_ids_or_current_gate']]
   f.write('| '+' | '.join(v.replace('|','/').replace('\n',' ') for v in vals)+' |\n')
build_package.merge_events()
build_package.manifest()
out=build_package.package('GCT_PLETH_checkpoint_06.zip')
record={'local_path':str(out),'created_at':stamp,'bytes':out.stat().st_size,'sha256':hashlib.sha256(out.read_bytes()).hexdigest()}
Path('work/checkpoint_06_local.json').write_text(json.dumps(record,indent=2))
print(json.dumps(record))
