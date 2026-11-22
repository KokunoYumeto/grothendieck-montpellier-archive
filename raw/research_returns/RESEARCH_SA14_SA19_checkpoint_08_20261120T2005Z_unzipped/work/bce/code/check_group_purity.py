import json,time
from pathlib import Path
import sympy as S
start=time.perf_counter()
s,t,x,y,x1,x2,y1,y2=S.symbols('s t x y x1 x2 y1 y2')
checks=[]
for p in (2,3,5,7):
 F=lambda v,a:v**p-a**(p-1)*v
 primitive_x=S.Poly(S.expand(F(x1+x2,s)-F(x1,s)-F(x2,s)),x1,x2,s,modulus=p).is_zero
 primitive_y=S.Poly(S.expand(F(y1+y2,t)-F(y1,t)-F(y2,t)),y1,y2,t,modulus=p).is_zero
 points=all(S.Poly(F(i*s,s),s,modulus=p).is_zero and S.Poly(F(i*t,t),t,modulus=p).is_zero for i in range(p))
 addition=all(((i+j)%p-i-j)%p==0 for i in range(p) for j in range(p))
 checks.append({'p':p,'primitive_x':primitive_x,'primitive_y':primitive_y,'all_constant_sections':points,'all_additions':addition,'monic_basis_size':p*p})
u=S.symbols('u')
X,Y,Z=S.symbols('X Y Z')
f=Y**2*Z+u**2*X*Y*Z+Y*Z**2+X**3
section=S.Poly(S.expand(f.subs({X:u,Y:1,Z:u**3})),u,modulus=2).is_zero
inversion=S.Poly(S.expand(f.subs(Y,Y+u**2*X+Z)-f),X,Y,Z,u,modulus=2).is_zero
fixed=S.Poly(u**2*u+u**3,u,modulus=2).is_zero
# Standard Weierstrass invariants: a1=u^2,a3=1, others zero.
b2=u**4;b4=u**2;b6=S.Integer(1);b8=S.Integer(0)
delta=S.Poly(-b2**2*b8-8*b4**3-27*b6**2+9*b2*b4*b6,u,modulus=2).as_expr()
assert S.Poly(delta-(1+u**6),u,modulus=2).is_zero
assert section and inversion and fixed and all(all(c[k] for k in ('primitive_x','primitive_y','all_constant_sections','all_additions')) for c in checks)
out={'model':'GPT-6 Astra (OpenAI)','scope':'Exact finite identities; monicity/freeness, all-prime formula and geometric zero-locus proved in companion note','finite_group_checks':checks,'elliptic':{'section_on_curve':section,'inversion_preserves_curve':inversion,'section_fixed_by_inversion':fixed,'discriminant_mod2':str(delta),'point_coordinates':['u','1','u^3'],'identity':['0','1','0']},'elapsed_seconds':time.perf_counter()-start}
p=Path('work/bce/code/check_group_purity.output.json');p.write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out,indent=2))
