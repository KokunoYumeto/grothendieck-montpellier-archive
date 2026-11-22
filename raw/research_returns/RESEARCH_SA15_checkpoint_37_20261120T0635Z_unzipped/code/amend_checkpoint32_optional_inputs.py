"""Recognize only fully promoted CP32 candidates as build/visual-QA inputs."""
from pathlib import Path
import ast,datetime,difflib,hashlib,json
w=Path(__file__).resolve().parents[1]
p=w/'code/prepare_checkpoint32.py';before=p.read_text()
snap=w/'notes/CP32_scope_amendment';assert not snap.exists();snap.mkdir()
(snap/'prepare_checkpoint32.before.py').write_text(before)
needle="required=['agents/reduction_descent/B_p5_cyclotomic_break_three_example.tex']\n"
assert before.count(needle)==1
optional=['agents/reduction_descent/B_p5_third_point_ramification.tex',
 'agents/obstructions_crystals/A4_Moore_Fermat_nondivisibility.tex',
 'agents/monodromy/ppav_all_odd_full_root_inertia.tex']
insert=needle+'for optional in '+repr(optional)+''':
    p=w/optional
    if p.exists() and '\\\\status{Candidate' not in p.read_text() and '\\\\textup{[Candidate' not in p.read_text():
        required.append(optional)
'''
after=before.replace(needle,insert);ast.parse(after)
p.write_text(after)
(snap/'prepare_checkpoint32.diff').write_text(''.join(difflib.unified_diff(before.splitlines(True),after.splitlines(True),fromfile='before',tofile='after')))
r={'status':'PASS','actual_utc':datetime.datetime.now(datetime.timezone.utc).isoformat(),
 'scope':'Build-input recognition only; optional canonical files must exist and have no candidate status at actual build time. No mathematical promotion, build or review occurs here.',
 'optional_canonical_inputs':optional,
 'before_sha256':hashlib.sha256(before.encode()).hexdigest(),
 'after_sha256':hashlib.sha256(after.encode()).hexdigest()}
(w/'outputs/checkpoint32_scope_amendment.json').write_text(json.dumps(r,indent=2)+'\n')
print(json.dumps(r,indent=2))
