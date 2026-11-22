"""Exact symbolic/endpoint certificate for HD-ALT-06, not a group scan."""
from pathlib import Path
from fractions import Fraction as F
import hashlib,json,time
import sympy as s
start=time.perf_counter()
n,k,x=s.symbols('n k x')
T=n*(n-1)/2-k*(n-k+1)
m=n-k
S0=m*(m-1)*(2*m-1)/6
N=T*T+n*(n-1)-3*S0
V=4*N/(n*(n-1)*(n-2)*(n-3))
assert s.expand(s.diff(N,k)-(-2*T*(n+1-2*k)+3*m*m-3*m+s.Rational(1,2)))==0
assert s.expand(T-n*(n-2*k-1)/2-k*(k-1))==0
c=s.Rational(13,100); A=1-2*c+2*c*c
dstar=(1-A*A)/4
assert A==s.Rational(3869,5000)
assert dstar==s.Rational(10030839,100000000)>s.Rational(1,10)
u=k*(n-1-k)/((n-1)*(n-2))
assert s.factor((u.subs(k,c*n)-c*(1-c))-13*(161*n-174)/(10000*(n-1)*(n-2)))==0
poly=1906518*n*n-6812633*n+4129618
assert s.factor(A*A-V.subs(k,c*n)-13*poly/(25000000*(n-1)*(n-2)*(n-3)))==0
assert s.expand(poly.subs(n,x+15))==1906518*x*x+50382907*x+330906673
assert c*(1-c)==s.Rational(1131,10000)>dstar
assert 6/(10*dstar-1)==s.Rational(60000000,30839)<2000
assert s.Rational(2*30**3,27)==2000
# The derivative majorant is strictly negative for every n>=15.
assert all(a>0 for a in s.Poly(s.expand(((n*n*(n-14)/4-s.Rational(1,2))).subs(n,x+15)),x).all_coeffs())
expected=[F(4001,32760),F(1091,7280),F(341,2380),F(1679,12240),
 F(2039,15504),F(2447,19380),F(1453,11970),F(3419,29260),
 F(3989,35420),F(1875,14168),F(19483,151800),F(573,4600),
 F(2831,23400),F(28891,245700),F(10865,95004)]
rows=[]
for nn,want in zip(range(15,30),expected):
 kk=(13*nn+99)//100
 tt=F(nn*(nn-1),2)-kk*(nn-kk+1)
 ss=F((nn-kk)*(nn-kk-1)*(2*(nn-kk)-1),6)
 vv=4*(tt*tt+nn*(nn-1)-3*ss)/F(nn*(nn-1)*(nn-2)*(nn-3))
 dd=min(F(1,4),F(kk*(nn-1-kk),(nn-1)*(nn-2)),(1-vv)/4)
 assert dd==want and dd>F(1,9)
 rows.append({'n':nn,'k0':kk,'delta':str(dd)})
assert 6/(10*F(1,9)-1)==54<90
assert 15*(15-3)//2==90 and 14*13//2==91
assert F(19)>F(6*22,7) and F(19)<=F(87*22,100)
p=Path(__file__).resolve().parent/'ordinary_alternating_87_section.tex'
text=p.read_text()
assert text.count(r'\[')==text.count(r'\]')
assert not any(ord(c)<32 and c not in '\n\r\t' for c in text)
out={'status':'PASS','scope':'universal symbolic identities and all15 exact endpoint fractions; no character-table enumeration',
 'proof_sha256':hashlib.sha256(p.read_bytes()).hexdigest(),'endpoint_rows':rows,
 'uniform_delta':str(dstar),'large_n_degree_ceiling':'60000000/30839',
 'small_n_degree_ceiling':54,'strict_witness':[19,3],'seconds':time.perf_counter()-start}
p.with_name('alternating_87_checked.json').write_text(json.dumps(out,indent=2)+'\n')
print(json.dumps(out,indent=2))
