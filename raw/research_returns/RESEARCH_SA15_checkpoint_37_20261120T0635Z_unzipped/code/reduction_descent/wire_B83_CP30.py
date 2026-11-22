from pathlib import Path
from datetime import datetime,timezone
import json,hashlib,difflib
own=Path(__file__).resolve().parents[1];work=own.parents[1]
record=json.loads((own/'outputs/B83_promotion.json').read_text())
canonical=Path(record['canonical'])
assert hashlib.sha256(canonical.read_bytes()).hexdigest()==record['canonical_sha256']
history=own/'notes/CP30_before_B83_wiring';assert not history.exists();history.mkdir()
path=work/'code/consolidate.py';before=path.read_bytes();s=before.decode()
old="'B_first_wild_reducible_terminal.tex']:"
new="'B_first_wild_reducible_terminal.tex',\n                    'B_first_wild_swapped_quotients.tex']:"
assert s.count(old)==1
after=s.replace(old,new)
(history/path.name).write_bytes(before)
(history/(path.name+'.diff')).write_text(''.join(difflib.unified_diff(s.splitlines(True),after.splitlines(True),fromfile='consolidate.before',tofile='consolidate.after')))
path.write_text(after)
out={'status':'CONSOLIDATE_WIRED_NOT_BUILT','actual_utc':datetime.now(timezone.utc).isoformat(),
     'canonical':'agents/reduction_descent/B_first_wild_swapped_quotients.tex',
     'path':'code/consolidate.py','before_sha256':hashlib.sha256(before).hexdigest(),
     'after_sha256':hashlib.sha256(path.read_bytes()).hexdigest(),
     'prior_versions':str(history),'coordination':'OC released product cross-Cartier single insertion before this fresh read; no other shared edit made.',
     'prepare30':'Requirement delegated to OC/parent; workflow file not present at prior check.'}
(own/'outputs/B83_CP30_wiring.json').write_text(json.dumps(out,indent=2)+'\n')
print(json.dumps(out,indent=2))
