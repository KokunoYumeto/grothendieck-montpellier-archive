"""Exact finite algebra in AM-K029; no character or class-number computation."""
from pathlib import Path
from datetime import datetime,timezone
from math import gcd
import hashlib,json
import sympy as sp

x=sp.symbols('x')
phi=sp.Poly(sp.cyclotomic_poly(28,x),x)
assert phi.as_expr()==x**12-x**10+x**8-x**6+x**4-x**2+1
assert phi.eval(1)==1
bar_u0=1-sp.invert(x,phi.as_expr())
assert sp.rem((1-x)-(-x)*bar_u0,phi.as_expr(),x)==0
for a in range(28):
    e=a%2
    assert (a-15*e)%2==0
    j=((a-15*e)//2)%14
    assert (2*j+15*e-a)%28==0
assert (-14*6+68)%56==40
assert 40%8==0 and (40//8)%7==5
assert {(68*a)%28 for a in range(28)}=={0,4,8,12,16,20,24}
assert all((7*68*a)%28==0 for a in range(28))
assert gcd(7,2)==1
# Only root orders2^a7^b survive the displayed rational ramification indices.
ramification={2:2,7:6,29:7}
allowed=[]
for p in list(sp.primerange(2,100)):
 for a in range(1,5):
  cyclo_index=(p-1)*p**(a-1)
  if ramification.get(p,1)%cyclo_index==0:allowed.append(p**a)
assert allowed==[2,4,7]
result=dict(result='PASS',checked_at=datetime.now(timezone.utc).isoformat(),
 scope='Exact cyclotomic polynomial/unit quotient, Hasse-coset parity, phase exponent and displayed ramification/root-order arithmetic only. The primary class-number input and character/capitulation proof are not computationally tested.',
 script_sha256=hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
 cyclotomic_polynomial=str(phi.as_expr()),norm_1_minus_zeta=1,
 phase_u0_exponent_mod7=5,ramification=ramification,
 possible_prime_power_root_orders=allowed)
Path(__file__).with_suffix('.json').write_text(json.dumps(result,indent=2)+'\n')
print(json.dumps(result,indent=2))
