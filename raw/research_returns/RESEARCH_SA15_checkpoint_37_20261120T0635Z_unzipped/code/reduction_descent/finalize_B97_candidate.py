from pathlib import Path
from datetime import datetime,timezone
import hashlib,json,re,difflib
own=Path(__file__).resolve().parents[1]
p=own/'B_irreducible_point_field_layers_candidate.tex';old=p.read_text()
before='is claimed. A separate exact supplement will check the finite\nmatrix and arithmetic statements without replacing these proofs.\n'
after=r'''is claimed. The separate standalone exact supplement
\path{code/reduction_descent/verify_irreducible_point_field_layers.py}
passed at 05:24:04.441182 UTC on 20 November 2026 in
1.2538034710014472 seconds. At $p=5,7,11$ it enumerates all
19,882 matrix planes, identifies 7,132 planes with every nonzero
evaluation surjective, and checks 934,848 corresponding nonzero
evaluations and 88,335 literal matrix powers. It checks 14,109
permitted first-break rows, 1,584 impermissible first degrees, all
nine displayed boundary comparisons and 164,874 uniform point
conductor rows. It enumerates 2,020 matrix hyperplanes and their
29 Lie subalgebras, verifying the common invariant line in every
nontraceless case. The quadratic-field checks use all 3,345
elements at nine stated primes, alongside the exact cyclotomic
inequalities. These finite checks supplement the complete all-prime
proof and infer no field or formal-group realization. The exact
executed source, complete output and stdout are retained; no
executed checker failure occurred.
'''
assert old.count(before)==1;new=old.replace(before,after)
hist=own/'notes/B97_certificate_finalization';hist.mkdir(exist_ok=False)
(hist/'candidate.before.tex').write_text(old)
(hist/'candidate.diff').write_text(''.join(difflib.unified_diff(old.splitlines(True),new.splitlines(True),fromfile='candidate.before.tex',tofile=p.name)))
p.write_text(new)
sha=lambda x:hashlib.sha256(x.read_bytes()).hexdigest()
code=own/'code/verify_irreducible_point_field_layers.py';out=code.with_suffix('.output.json')
data=json.loads(out.read_text());assert data['status']=='PASS'
r={'status':'CANDIDATE','actual_utc':datetime.now(timezone.utc).isoformat(),'candidate':str(p),'candidate_sha256':sha(p),'labels':re.findall(r'\\label\{([^}]+)\}',new),'program':str(code),'program_sha256':sha(code),'output':str(out),'output_sha256':sha(out),'author_actual_utc':data['actual_utc'],'author_runtime_seconds':data['runtime_seconds'],'counts':data['counts'],'retention':'Exact pre-certificate source/diff, executed standalone code, full output and stdout retained. No failure; no shared or canonical edit.'}
(own/'outputs/B97_candidate_record.json').write_text(json.dumps(r,indent=2)+'\n')
print(json.dumps(r,indent=2))
