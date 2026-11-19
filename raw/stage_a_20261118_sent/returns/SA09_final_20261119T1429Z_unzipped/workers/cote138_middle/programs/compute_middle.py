#!/usr/bin/env python3
"""Exact symbolic certificates and free-word checks for cote138 scans46–89.
Finite word checks supplement the general algebraic proofs in computation_notes.md.
"""
import json
from fractions import Fraction
from math import comb,gcd
from pathlib import Path
import sympy as s
x,y,z,t,w=s.symbols('x y z t w')
out={}
A=-x*(x*x-3*y*y);B=y*(y*y-3*x*x);C=z**3
F=x*x+y*y+z*z
out['cubic']={'expanded':str(s.expand(A*A+B*B+C*C)),
 'remainder_mod_conic':str(s.rem(A*A+B*B+C*C,F,z)),
 'factor':str(s.factor(A*A+B*B+C*C)),
 'coefficient_of_x4y2':int(s.Poly(A*A+B*B+C*C,x,y,z).coeff_monomial(x**4*y**2)),
 'no_basepoint_check_z0_and_y2_minus_x2':str(s.expand(A).subs(y**2,-x**2))}
out['conic_models']={'plus_on_parameter':str(s.factor((1-t*t)**2+(2*t)**2+(1+t*t)**2)),
 'minus_on_parameter':str(s.factor((1-t*t)**2+(2*t)**2-(1+t*t)**2)),
 'degree2_split_target':str(s.expand((x*x-y*y)**2+(2*x*y)**2-(x*x+y*y)**2))}
out['odd_power']={}
for m in range(1,10):
    expr=s.Poly(s.expand((y-s.I*x)**m),x,y)
    Bm=s.expand((expr.as_expr()+s.conjugate(expr.as_expr()).subs({s.conjugate(x):x,s.conjugate(y):y}))/2)
    Am=s.expand((s.conjugate(expr.as_expr()).subs({s.conjugate(x):x,s.conjugate(y):y})-expr.as_expr())/(2*s.I))
    residual=s.factor(s.rem(s.expand(Am**2+Bm**2+z**(2*m)),F,z))
    out['odd_power'][str(m)]={'A':str(Am),'B':str(Bm),'remainder':str(residual),'descends':m%2==1}
out['dihedral']={}
for n in range(1,9):
    f=s.Rational(1,2)-(x**n+x**(-n))/4
    out['dihedral'][str(n)]={'derivative':str(s.factor(s.diff(f,x))),
      'rotation_and_inversion':str(s.factor(f-f.subs(x,1/x))),
      'degree':2*n,'ramification_sum':2*n+2*(n-1),'RH_target':4*n-2}
out['kummer_basechange']={'factor':str(s.factor(w*w-(z+1/z)*w+1)),
 'component_equations':['x^n=z','x^n=z^(-1)'],'normalizations':'Each component is P1 with coordinate x; cyclic degree n maps.'}
R=s.Rational(27,4)*t*t*(t-1)**2/(t*t-t+1)**3
out['sextic_candidate']={'R_minus_1':str(s.factor(R-1)),'derivative':str(s.factor(s.diff(R,t))),
 's3_generator_1_minus_t':str(s.factor(R-R.subs(t,1-t))),
 's3_generator_inverse_t':str(s.factor(R-R.subs(t,1/t))),
 'ramification_sum':3*(2-1)+3*(2-1)+2*(3-1)}
out['tame_spherical_signatures']={'two_branch':'(N,N), N>=2','three_branch':[],'four_or_more':'sum_i(1-1/d_i)>=r/2>=2 contradicts strict <2'}
for a in range(2,31):
 for b in range(a,31):
  for c in range(b,31):
   q=Fraction(1,a)+Fraction(1,b)+Fraction(1,c)-1
   if q>0:out['tame_spherical_signatures']['three_branch'].append({'signature':[a,b,c],'N':str(2/q)})
out['orientation_ranks']={str(g):{'rank_H1':2*g,'rank_Lambda2_dual':comb(2*g,2),'rank_T':1} for g in range(1,7)}

def red(word):
 out=[]
 for x in word:
  if out and out[-1]==-x:out.pop()
  else:out.append(x)
 return tuple(out)
def mul(*ws):return red([x for w in ws for x in w])
def inv(w):return tuple(-x for x in reversed(w))
def conj(a,b):return mul(a,b,inv(a))
def subst(word,images):return mul(*(images[x] if x>0 else inv(images[-x]) for x in word))
out['reversal']={}
for nu in range(2,10):
 ls={i:(i,) for i in range(1,nu+1)};ls[0]=inv(mul(*(ls[i] for i in range(1,nu+1))))
 q=lambda i,start:mul(*(ls[j] for j in range(start,i)))
 images={j:conj(q(nu+1-j,1),ls[nu+1-j]) if j<nu else ls[1] for j in range(1,nu+1)}
 bad={j:conj(q(nu+1-j,0),ls[nu+1-j]) if j<nu else ls[1] for j in range(1,nu+1)}
 relation=mul(ls[0],*(images[j] for j in range(1,nu+1)))
 badrelation=mul(ls[0],*(bad[j] for j in range(1,nu+1)))
 expected_bad=mul(ls[0],inv(ls[1]),inv(ls[0]),ls[1])
 square={j:subst(images[j],images) for j in images}
 expected={j:conj(inv(ls[0]),ls[j]) for j in images}
 assert not relation and badrelation==expected_bad and square==expected
 out['reversal'][str(nu)]={'lower1_relator':relation,'lower0_relator':badrelation,'lower0_matches_commutator':True,
  'square_matches_inner_lambda0_inverse':True,'square_is_identity':all(square[j]==ls[j] for j in square)}
# Three transition pairs; assign six formal symbols for p20+,p20-,p12+,p12-,p01+,p01-.
p20p,p20m,p12p,p12m,p01p,p01m=[(i,) for i in range(1,7)]
rho0=mul(inv(p01p),p01m,inv(p20m),p20p)
rho1=mul(inv(p12p),p12m,inv(p01m),p01p)
rho2=mul(inv(p20p),p20m,inv(p12m),p12p)
out['bipyramid_product']=mul(rho2,rho1,rho0)
assert not out['bipyramid_product']
# Finite version of general-category counterexample: one-object monoid {1,e},e²=e.
monoid=lambda a,b:a*b
units=[a for a in [0,1] if any(monoid(a,b)==monoid(b,a)==1 for b in [0,1])]
out['groupoid_corollary_counterexample']={'target_endomorphisms':[0,1],'unit_group':units,
 'source_endomorphisms':[1],'object_and_component_maps_bijective':True,'unit_groups_isomorphic':units==[1],'functor_full':False}
out['rank_one_inner_map']={'group':'Zhat','centre':'Zhat','image':'1','injective':False}
out['unit_vs_cyclic_action_n5']={'Galois_exponent_generator':2,'permutation_on_exponents':[0,2,4,1,3],
 'permutation_cycle_lengths':[1,4],'nonidentity_translation_cycle_lengths':[5],
 'conclusion':'Multiplication by2 cannot be a translation, nor factor as a nontrivial order4 map through C5.'}
dest=Path(__file__).resolve().parents[1]/'outputs/computations.json'
dest.write_text(json.dumps(out,ensure_ascii=False,indent=2)+'\n')
print(json.dumps(out,ensure_ascii=False,indent=2))
