from pathlib import Path
from datetime import datetime, timezone
import hashlib,json,difflib

own=Path(__file__).resolve().parents[1];work=own.parents[1]
history=own/'notes/CP29_before_B81_wiring'
assert not history.exists();history.mkdir()
edits=[
    (work/'code/consolidate.py',"'B_first_wild_fourth_layer.tex']:",
     "'B_first_wild_fourth_layer.tex',\n                    'B_first_wild_Cartan_exclusion.tex']:"),
    (work/'code/prepare_checkpoint29.py',
     "'agents/reduction_descent/B_first_wild_fourth_layer.tex',",
     "'agents/reduction_descent/B_first_wild_fourth_layer.tex',\n          'agents/reduction_descent/B_first_wild_Cartan_exclusion.tex',")]
records=[]
for path,old,new in edits:
    before=path.read_bytes();s=before.decode()
    assert 'thirteen' in s and s.count(old)==1
    after=s.replace(old,new)
    assert 'thirteen' in after
    (history/path.name).write_bytes(before)
    (history/(path.name+'.diff')).write_text(''.join(difflib.unified_diff(
        s.splitlines(True),after.splitlines(True),fromfile=path.name+'.before',tofile=path.name+'.after')))
    path.write_text(after)
    records.append({'path':str(path.relative_to(work)),
                    'before_sha256':hashlib.sha256(before).hexdigest(),
                    'after_sha256':hashlib.sha256(path.read_bytes()).hexdigest(),
                    'norm13_wiring_preserved':True})
out={'status':'WIRED_NOT_BUILT','actual_utc':datetime.now(timezone.utc).isoformat(),
     'edits':records,'prior_versions':str(history),
     'coordination':'Waited for monodromy explicit norm13 shared-file release at00:21:37; read fresh versions.',
     'root_authorized':True}
(own/'outputs/B81_CP29_wiring.json').write_text(json.dumps(out,indent=2)+'\n')
print(json.dumps(out,indent=2))
