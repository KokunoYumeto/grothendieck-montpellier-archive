from pathlib import Path
import sys,csv,json,hashlib
from datetime import datetime,timezone
from zoneinfo import ZoneInfo
sys.path.insert(0,'work');import build_package
now=datetime.now(timezone.utc)
assert now>=datetime(2026,11,21,5,46,8,tzinfo=timezone.utc),now
assert Path('work/REVIEW_04.json').exists()
assert not Path('GCT_PLETH_checkpoint_09.zip').exists()
stamp=now.astimezone(ZoneInfo('Europe/Berlin')).isoformat()
with Path('deliverables/LEDGER.md').open('a') as f:
 f.write('\n\n## Checkpoint09 — '+stamp+'\n\nThis checkpoint contains all prior deliverables plus the completed stable two-row formulas G038/G039 and every fixed-second-part construction G040; actual higher hook jet splittings and positive formulas T062–T066 through the full a≥2k−1 range; finite repeated-four mixed profiles R047; refined odd-part canonical threshold R048/R049; and the complete actual canonical isomorphism on every hook tail R050. Later completed reports present at this snapshot retain their own question rows and accurately scoped events. Active whole-proof audits and mathematical drafts are preserved with their status. Review04 has movement YES and no-movement streak0. Review05 is due06:01:08UTC. Checkpoint10 is due06:31:08UTC.\n\nCurrent open rows at checkpoint:\n\n| Question | State | Current exact gate |\n|---|---|---|\n')
 for r in csv.DictReader(Path('deliverables/QUESTIONS.tsv').open(),delimiter='\t'):
  if not(r['state'].startswith('proved') or 'refuted' in r['state']):
   f.write('| '+' | '.join(r[k].replace('|',' / ').replace('\n',' ') for k in ('id','state','finding_ids_or_current_gate'))+' |\n')
build_package.merge_events();build_package.manifest()
out=build_package.package('GCT_PLETH_checkpoint_09.zip')
record={'local_path':str(out),'created_at':stamp,'bytes':out.stat().st_size,'sha256':hashlib.sha256(out.read_bytes()).hexdigest()}
Path('work/checkpoint_09_local.json').write_text(json.dumps(record,indent=2)+'\n')
print(json.dumps(record))
