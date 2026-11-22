from pathlib import Path
from datetime import datetime, timezone
import difflib
import hashlib
import json

own=Path(__file__).resolve().parents[1]
work=own.parents[1]
backup=own/'notes/CP27_before_B74_wiring'
assert not backup.exists()
backup.mkdir()
changes=[]
for rel,old,new in [
 ('code/consolidate.py',
  "                    'B_rational_high_line.tex']:",
  "                    'B_rational_high_line.tex',\n                    'B_iterated_high_quotient.tex']:"),
 ('code/prepare_checkpoint27.py',
  "          'agents/reduction_descent/B_rational_high_line.tex']",
  "          'agents/reduction_descent/B_rational_high_line.tex',\n          'agents/reduction_descent/B_iterated_high_quotient.tex']")
]:
    path=work/rel
    before=path.read_text()
    assert before.count(old)==1,(rel,old)
    (backup/path.name).write_text(before)
    after=before.replace(old,new)
    path.write_text(after)
    delta=''.join(difflib.unified_diff(before.splitlines(True),after.splitlines(True),
                                    fromfile=rel+' (before)',tofile=rel+' (after)'))
    (backup/(path.name+'.diff')).write_text(delta)
    changes.append({'path':rel,'before_sha256':hashlib.sha256(before.encode()).hexdigest(),
                    'after_sha256':hashlib.sha256(after.encode()).hexdigest()})
now=datetime.now(timezone.utc).isoformat()
record={'status':'ROOT_AUTHORIZED_WIRING_COMPLETE','actual_utc':now,
        'canonical':'agents/reduction_descent/B_iterated_high_quotient.tex',
        'prior_versions_and_diffs':str(backup),'changes':changes,
        'build_or_updater_run':False}
(own/'outputs/B74_CP27_wiring.json').write_text(json.dumps(record,indent=2)+'\n')
p=own/'outputs/B74_promotion.json'
promotion=json.loads(p.read_text())
promotion['wiring_changes']=[item['path'] for item in changes]
promotion['wiring_record']='outputs/B74_CP27_wiring.json'
promotion['checkpoint_scope']='Promoted and root-authorized CP27 wiring complete; no build, updater or bibliography mutation performed here.'
p.write_text(json.dumps(promotion,indent=2)+'\n')
print(json.dumps(record,indent=2))
