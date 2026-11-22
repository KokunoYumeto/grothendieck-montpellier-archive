from pathlib import Path
from datetime import datetime,timezone
import hashlib,json,re,difflib
own=Path(__file__).resolve().parents[1]
p=own/'B_first_wild_cyclotomic_different_candidate.tex'
old=p.read_text()
before='A separate exact program will check the symbolic different and\nconductor identities without replacing any field-theoretic step.\n'
after=r'''The standalone exact supplement
\path{code/reduction_descent/verify_first_wild_cyclotomic_different.py}
passed at 05:33:21.626818 UTC on 20 November 2026 in
1.8577888349973364 seconds. It checks nine symbolic identities,
3,482 derivative monomials and 346 distinct-residue profiles,
and all 3,336 nonidentity cyclotomic exponents at the nine primes
from five through31. It retains rational upper breaks, checking
82,106 pairs and 164,212 terminal conductor comparisons. At
$p=5,7,11$ it checks all 17,667 terminal matrices and their
determinants, and both complete column-dual ranks for all 15,696
ordered bases. These symbolic and finite checks supplement the
complete actual-field proof; they infer no formal-group realization
and make no finite-residue or integer-upper-break assumption.
The executed code, complete output and stdout are retained.
No checker failure occurred.
'''
assert old.count(before)==1
new=old.replace(before,after)
hist=own/'notes/B98_certificate_finalization';hist.mkdir(exist_ok=False)
(hist/'candidate.before.tex').write_text(old)
(hist/'candidate.diff').write_text(''.join(difflib.unified_diff(old.splitlines(True),new.splitlines(True),fromfile='candidate.before.tex',tofile=p.name)))
p.write_text(new)
sha=lambda x:hashlib.sha256(x.read_bytes()).hexdigest()
code=own/'code/verify_first_wild_cyclotomic_different.py';out=code.with_suffix('.output.json')
data=json.loads(out.read_text());assert data['status']=='PASS'
src=own/'sources/colmez_corps_locaux.txt'
r={'status':'CANDIDATE','actual_utc':datetime.now(timezone.utc).isoformat(),
 'candidate':str(p),'candidate_sha256':sha(p),'labels':re.findall(r'\\label\{([^}]+)\}',new),
 'program':str(code),'program_sha256':sha(code),'output':str(out),'output_sha256':sha(out),
 'author_actual_utc':data['actual_utc'],'author_runtime_seconds':data['runtime_seconds'],'counts':data['counts'],
 'source_read':{'path':str(src),'sha256':sha(src),'scope':'Fresh retained original Colmez Proposition3.17, Proposition3.18 including continuation, Corollary3.19, complete proofs printed17–18. Complete B86 Cohen-field and B97 actual-field proofs read. No new web opening or image inspection.'},
 'retention':'Exact pre-field-wording and pre-certificate sources/diffs, executed standalone code, full output and stdout retained. No executed failure; no canonical or shared edit.',
 'claim_scope':'All-prime irreducible residual recovery at first wild absolute index. Full least-index equality only (p,e,h)=(5,20,2), conditional on complete independent audits before promotion.'}
(own/'outputs/B98_candidate_record.json').write_text(json.dumps(r,indent=2)+'\n')
print(json.dumps(r,indent=2))
