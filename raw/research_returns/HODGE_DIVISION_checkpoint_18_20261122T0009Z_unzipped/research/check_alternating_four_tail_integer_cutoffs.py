"""Exact numerical supplement to the derived HD-ALT-10 corollary."""
from pathlib import Path
from datetime import datetime,timezone
from fractions import Fraction as F
import hashlib,json,time
import sympy as s
R=Path(__file__).resolve().parent
start=time.perf_counter();stamp=datetime.now(timezone.utc).isoformat()
n,m,x=s.symbols('n m x')
poly=5*n*(n-3)*(4*m*(n-5)-(n-1)*(n-2))-6*m*(n-1)*(n-2)
endpoint=poly.subs(m,(n+3)/4)
assert s.expand(endpoint-(s.Rational(7,2)*n**3-100*n*n+s.Rational(531,2)*n-9))==0
shift=s.expand(endpoint.subs(n,x+36))
assert shift==s.Rational(7,2)*x**3+278*x*x+s.Rational(13347,2)*x+43245
assert all(c>0 for c in s.Poly(shift,x).all_coeffs())
assert s.expand((4*m*(n-5)-(n-1)*(n-2)).subs(n,4*m-2))==-12
a=n*(n-1)*(n-2)*(n-7)/24
assert s.factor(a-n*(n-3)/2)==n*(n+1)*(n*n-11*n+22)/24
assert 3*35**2>5*27**2 and 3*19**2<5*15**2
fields=[('i',2),('-2',4),('-7',6),('-11',10),('-19',18),('-43',42),('-67',66),('-163',162)]
rows=[];count=0
for field,h in fields:
    M=5*h;cut=20*h-2
    for N in range(36,cut):
        assert F(4*(N-5),(N-1)*(N-2))-F(1,M)>F(6,5*N*(N-3))
        count+=1
    N=cut;degree=N*(N-1)*(N-2)*(N-7)//24
    assert degree>=N*(N-3)//2
    assert F(4*(N-5),(N-1)*(N-2))<F(1,M)
    assert 3*N*N<5*(N-8)**2
    rows.append({'quadratic_radicand':field,'h':h,'necessary_n':cut,'endpoint_degree':degree})
proof=R/'alternating_four_tail_integer_cutoffs_section.tex'
result={'status':'PASS','started_utc':stamp,'elapsed_seconds':time.perf_counter()-start,
        'finite_excluded_endpoints':count,'rows':rows,
        'proof_sha256':hashlib.sha256(proof.read_bytes()).hexdigest(),
        'checker_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
        'scope':'Exact polynomial identities and finite necessary-inequality checks; no source existence, no independent movement.'}
(R/'alternating_four_tail_integer_cutoffs_checked.json').write_text(json.dumps(result,indent=2)+'\n')
print(json.dumps(result,indent=2))
