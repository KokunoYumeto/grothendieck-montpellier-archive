"""Independent exact algebra supplement to the whole-reviewed OL01--03 proof."""
from pathlib import Path
from datetime import datetime, timezone
from fractions import Fraction as F
import hashlib, json, time
import sympy as s

R=Path(__file__).resolve().parents[1]
t=time.perf_counter()
d,m,x=s.symbols('d m x', real=True)
J=10**30; M=2*10**29
assert F(1,10**29)*M==2
assert (1-F(1,4))/4==F(3,16)
assert F(6)/(12*F(3,16)-2)==24
# k<=d/6+2/3 proves the level exponent uniformly for d>=50.
assert s.expand(d-2*(d/6+s.Rational(2,3))-2-s.Rational(3,5)*d-(d-50)/15)==0
E=lambda y:y*y/8-y/4-2
assert s.expand(E(d)-(d*d/s.Integer(8)-d/s.Integer(4)-2))==0
assert s.expand(E(2*J+x)-M*(2*J+x)-(s.Rational(J*J,10)-s.Rational(J,2)-2+(s.Rational(3*J,10)-s.Rational(1,4))*x+x*x/8))==0
assert F(J*J,10)-F(J,2)-2>0 and F(3*J,10)-F(1,4)>0
# Compare each invoked spin/SO exponent to the common E(d).
assert s.expand(m*(m-1)/2-2-E(2*m))==0
assert s.expand(m*(m+1)/2-2-E(2*m+1))==m/2+s.Rational(1,8)
assert s.expand((m*m/2-1)-E(2*m+1))==s.Rational(9,8)
proof=R/'agents/imprimitive/orthogonal_levels/orthogonal_level_section.tex'
out={'date_utc':datetime.now(timezone.utc).isoformat(),'status':'PASS',
 'proof_sha256':hashlib.sha256(proof.read_bytes()).hexdigest(),
 'scope':'independent universal rational identities only; no group enumeration and no author program imported',
 'sigma_M':2,'support':'3/16','degree_ceiling':24,'J':str(J),'M':str(M),'natural_dimension_cutoff':str(2*J),
 'elapsed_seconds':time.perf_counter()-t}
(R/'research/root_orthogonal_level_checked.json').write_text(json.dumps(out,indent=2)+'\n')
print(json.dumps(out,indent=2))
