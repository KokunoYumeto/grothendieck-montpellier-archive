"""Exact algebraic supplement to the integral consequence HD-ALT09."""
from pathlib import Path
from datetime import datetime,timezone
from fractions import Fraction as Q
import hashlib,json,time
import sympy as s
start=time.perf_counter();R=Path(__file__).resolve().parent
n,m,x=s.symbols('n m x')
F=5*n*(n-3)*(3*m*(n-4)-(n-1)*(n-2))-6*m*(n-1)*(n-2)
poly=s.expand(F.subs(m,(n+2)/3))
assert poly==3*n**3-63*n**2+158*n-8
assert s.expand(poly.subs(n,x+27))==3*x**3+180*x**2+3317*x+17380
assert 3*169>5*100
assert s.cancel((3*(n-4)/((n-1)*(n-2))-1/m).subs(n,3*m-1)+6/(m*(3*m-2)*(3*m-3)))==0
rows=[];checks=0
for h in (2,4,6,10,18,42,66,162):
 mm=5*h;endpoint=15*h-1
 for nn in range(27,endpoint):
  beta=Q(3*(nn-4),(nn-1)*(nn-2))
  assert beta-Q(1,mm)>Q(6,5*nn*(nn-3))
  checks+=1
 nn=endpoint;degree=nn*(nn-1)*(nn-5)//6
 assert degree>=nn*(nn-3)//2 and 12<nn
 beta=Q(3*(nn-4),(nn-1)*(nn-2));assert beta<Q(1,mm)
 rows.append({'h':h,'minimum_allowed_n':nn,'two_row_degree':degree,'beta':str(beta),'strict_endpoint_difference':str(beta-Q(1,mm))})
proof=R/'alternating_remaining_integer_cutoffs_section.tex'
out={'status':'PASS','completed_utc':datetime.now(timezone.utc).isoformat(),'runtime_seconds':time.perf_counter()-start,
 'proof_sha256':hashlib.sha256(proof.read_bytes()).hexdigest(),'script_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
 'exact_rejected_integer_cases':checks,'field_rows':rows,'universal_shifted_polynomial':str(s.expand(poly.subs(n,x+27))),
 'scope':'Universal polynomial identities and exact field-table consequences of an already reduced gate; not additional standalone movement or a source-existence certificate.'}
(R/'alternating_integer_cutoffs_checked.json').write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out,indent=2))
