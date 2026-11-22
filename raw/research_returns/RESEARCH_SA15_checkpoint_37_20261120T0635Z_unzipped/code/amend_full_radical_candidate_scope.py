"""Preserve and apply the companion's geometric-component wording clarification."""
from pathlib import Path
import datetime,difflib,hashlib,json
w=Path(__file__).resolve().parents[1]
p=w/'notes/A_full_radical_image_structure_candidate.tex'
before=p.read_text();needle='Its nonzero Lang cover has one component corresponding to'
assert before.count(needle)==1
after=before.replace(needle,'After base change to an algebraic closure, its nonzero Lang cover\nhas one geometric connected component corresponding to')
after=after.replace('the remaining components have the degrees of the nonzero','the remaining geometric connected components have the degrees of the nonzero')
after=after.replace('Connected components of a finite etale cover over\na connected normal base correspond to orbits of its','After the same geometric base change, connected components of a\nfinite etale cover over a connected normal base correspond to orbits of its')
folder=w/'notes/full_radical_scope_repair';assert not folder.exists();folder.mkdir()
(folder/'candidate.before.tex').write_text(before)
(folder/'candidate.diff').write_text(''.join(difflib.unified_diff(before.splitlines(True),after.splitlines(True),fromfile='before',tofile='after')))
p.write_text(after)
r={'status':'PASS','actual_utc':datetime.datetime.now(datetime.timezone.utc).isoformat(),
 'before_sha256':hashlib.sha256(before.encode()).hexdigest(),'after_sha256':hashlib.sha256(after.encode()).hexdigest(),
 'correction':'The image is geometric. Component assertions now explicitly follow base change to an algebraic closure; arithmetic monodromy may merge smaller geometric orbits.',
 'scope':'Wording/type clarification only; no change to the finite-group proof and no numerical run.'}
(folder/'record.json').write_text(json.dumps(r,indent=2)+'\n')
print(json.dumps(r,indent=2))
