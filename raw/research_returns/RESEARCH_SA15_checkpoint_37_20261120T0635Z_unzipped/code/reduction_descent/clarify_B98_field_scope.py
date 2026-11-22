from pathlib import Path
from datetime import datetime,timezone
import difflib,hashlib,json
own=Path(__file__).resolve().parents[1]
p=own/'B_first_wild_cyclotomic_different_candidate.tex'
old=p.read_text()
a='For every $p\\ge5$, over a field satisfying the hypotheses\n$e_K=p(p-1)$ and $\\mu_p\\subset K$, an actual $p^3$-torsion\n'
b='Let $p\\ge5$ and let $K$ be a complete discretely valued field\nof mixed characteristic $(0,p)$ with algebraically closed residue\nfield, $e_K=p(p-1)$ and $\\mu_p\\subset K$. An actual $p^3$-torsion\n'
assert old.count(a)==1
new=old.replace(a,b)
a2='in the preceding results.\n\nIf their residual representation is irreducible'
b2='in the preceding results. In this field $\\mu_5\\subset K$: choose\na Cohen field $K_0$, write $5=u\\pi^{20}$ and take a fourth\nroot of the unit $u$ by Hensel. Thus $K$ contains the unique\ntame degree-four extension $K_0(5^{1/4})=K_0(\\mu_5)$.\n\nIf their residual representation is irreducible'
assert new.count(a2)==1
new=new.replace(a2,b2)
h=own/'notes/B98_field_scope_clarification';h.mkdir(exist_ok=False)
(h/'candidate.before.tex').write_text(old)
(h/'candidate.diff').write_text(''.join(difflib.unified_diff(old.splitlines(True),new.splitlines(True),fromfile='candidate.before.tex',tofile=p.name)))
p.write_text(new)
r={'actual_utc':datetime.now(timezone.utc).isoformat(),'candidate_sha256':hashlib.sha256(p.read_bytes()).hexdigest(),'scope':'Explicit complete-field hypotheses; explicit mu5 containment in full B4 corollary. No mathematical premise enlarged.'}
(h/'record.json').write_text(json.dumps(r,indent=2)+'\n')
print(json.dumps(r,indent=2))
