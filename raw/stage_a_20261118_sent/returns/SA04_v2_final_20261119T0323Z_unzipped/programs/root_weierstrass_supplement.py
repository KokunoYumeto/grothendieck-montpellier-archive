"""Exact checks of the normalized and small-characteristic formulas in Deligne's supplied formulaire."""
from pathlib import Path
import sympy as S,json,datetime
a1,a2,a3,a4,a6,u,r,s,t=S.symbols('a1 a2 a3 a4 a6 u r s t')
def invariants(v):
    A,B,C,D,E=v
    b2=A*A+4*B;b4=A*C+2*D;b6=C*C+4*E;b8=A*A*E+4*B*E-A*C*D+B*C*C-D*D
    return b2*b2-24*b4,-b2**3+36*b2*b4-216*b6,-b2*b2*b8-8*b4**3-27*b6*b6+9*b2*b4*b6
c4,c6,de=invariants([0,a2,0,a4,a6]);gb=S.groebner([a2*a4-9*a6],a2,a4,a6)
exprs={'3.3_c6':c6+64*(a2**3-27*a6),'3.3_Delta':de-64*(-a2**3*a6-a4**3+54*a6**2),'3.4_a2':4*a2*c4+c6,'3.4_a4':a4*c4*c4+36*de,'3.4_a6':a6*c4**3-c6*de}
out={'normalized_identities':{k:str(gb.reduce(S.expand(v))[1]) for k,v in exprs.items()}}
assert set(out['normalized_identities'].values())=={'0'}
ap=[(a1+2*s)/u,(a2-s*a1+3*r-s*s)/u**2,(a3+r*a1+2*t)/u**3,(a4-s*a3+2*a2*r-(t+r*s)*a1+3*r*r-2*s*t)/u**4,(a6+r*a4+r*r*a2+r**3-t*a3-t*t-r*t*a1)/u**6]
ordinary=[S.factor(x.subs({a1:1,a3:0,a4:0,r:0,t:0,u:1+2*s},simultaneous=True)) for x in ap]
expected=[1,(a2-s-s*s)/(1+2*s)**2,0,0,a6/(1+2*s)**6]
assert all(S.cancel(x-y)==0 for x,y in zip(ordinary,expected))
out['ordinary_char2_normalization']=[str(x) for x in ordinary]
def zero_mod(expr,p):
    n=S.together(expr).as_numer_denom()[0]
    return S.Poly(n,*sorted(n.free_symbols,key=str),modulus=p).is_zero if n.free_symbols else int(n)%p==0
sub3={a1:0,a2:0,a3:0,s:0,t:0}
exp3=[0,0,0,a4/u**4,(a6+r*a4+r**3)/u**6]
assert all(zero_mod(x.subs(sub3,simultaneous=True)-y,3) for x,y in zip(ap,exp3))
sub2={a1:0,a2:0,r:s*s}
exp2=[0,0,a3/u**3,(a4+s*a3+s**4)/u**4,(a6+s*s*a4+t*a3+s**6+t*t)/u**6]
assert all(zero_mod(x.subs(sub2,simultaneous=True)-y,2) for x,y in zip(ap,exp2))
out['small_characteristic_changes']={'p3':'all five coefficients verified','p2':'all five coefficients verified'}
parameter=S.symbols('z')
families={2:[parameter,0,1,0,0],3:[0,parameter,0,-1,0]}
out['wild_j_special_fibres']={}
for p,coefs in families.items():
    c,d,dis=invariants(coefs)
    c=S.Poly(c,parameter,modulus=p).as_expr();dis=S.Poly(dis,parameter,modulus=p).as_expr()
    num=S.Poly(c**3,parameter,modulus=p).as_expr()
    order=min(k[0] for k,v in S.Poly(num,parameter,modulus=p).terms())
    assert dis.subs(parameter,0)!=0 and order==({2:12,3:6}[p])
    out['wild_j_special_fibres'][str(p)]={'coefficients':[str(x) for x in coefs],'c4':str(c),'Delta':str(dis),'j':str(num/dis),'order_at_z0':order,'scope':'special-fibre local model; mixed-characteristic quotient assertion is separate'}
out['ordinary_modular_invariants']={}
for p,coefs,expected in [(2,[a1,a2,a3,a4,a6],(a1**4,a1**6)),(3,[a1,a2,a3,a4,a6],((a1*a1+a2)**2,-(a1*a1+a2)**3))]:
    c,d,di=invariants(coefs);assert zero_mod(c-expected[0],p) and zero_mod(d-expected[1],p)
    out['ordinary_modular_invariants'][str(p)]='c4,c6 congruences verified; ring generation is not inferred from congruences'
root=Path(__file__).resolve().parents[1];p=root/'outputs/root_weierstrass_supplement.json'
p.write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out,indent=2))
with (root/'progress.log').open('a') as f:f.write(datetime.datetime.now(datetime.timezone.utc).isoformat()+'\troot_weierstrass_supplement.py\tall assertions passed\n')
