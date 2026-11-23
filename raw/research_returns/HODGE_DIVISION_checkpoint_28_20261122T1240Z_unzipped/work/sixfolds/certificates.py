#!/usr/bin/env python3
"""Exact arithmetic checks for HODGE_DIVISION sixfold findings.
Does not claim a formal proof or geometric smoothness at a specialization.
"""
from itertools import product
from math import factorial
import json
from pathlib import Path
import sympy as S

out = {}
# Schoen 1998, section 13: character labels of the maximal exponent-3 cover.
branch=[(1,0,0),(0,1,0),(0,0,1),(2,2,2)]
characters={1:[],2:[]}
for k in product(range(3),repeat=3):
    residues=[sum(x*y for x,y in zip(k,b))%3 for b in branch]
    assert sum(residues)%3==0
    multiplicity=-1+sum(residues)//3
    chi=(k[0]+k[1])%3
    if chi and multiplicity:
        characters[chi].append({'character':k,'multiplicity':multiplicity,'residues':residues})
assert [sum(v['multiplicity'] for v in characters[j]) for j in [1,2]]==[3,3]
sums=[tuple((x+y)%3 for x,y in zip(a['character'],b['character']))
      for a in characters[1] for b in characters[2]]
assert len(sums)==len(set(sums))==9
out['schoen_1998_rank9']={'character_lists':characters,'nine_distinct_products':sums}

# Koike 2004 pp.568,571: directly expand all displayed quadratic identities.
s,t,x,y=S.symbols('s t x y'); I=S.I
a=[s+t+x+y,s*t+t*x+x*y+y*s,t*x*y+s*x*y+s*t*y+s*t*x,s*x+t*y,s*t*x*y,S.Integer(1)]
b=[s-t+x-y,s*t-t*x+x*y-y*s,t*x*y-s*x*y+s*t*y-s*t*x,s*x-t*y]
c=[s-I*t-x+I*y,s*t-I*t*x-x*y+I*y*s,t*x*y-I*s*x*y-s*t*y+I*s*t*x]
d=[s+I*t-x-I*y,s*t+I*t*x-x*y-I*y*s,t*x*y+I*s*x*y-s*t*y-I*s*t*x]
a1,a2,a3,a4,a5,a6=a
lhs6=[b[0]**2,b[1]**2,b[2]**2,b[0]*b[2],b[0]*b[3],b[2]*b[3],b[3]**2]
rhs6=[a1*a1-4*a2*a6,a2*a2-4*(a1*a3-a2*a4)+16*a5*a6,a3*a3-4*a2*a5,
      a1*a3-2*a2*a4,a1*a4-2*a3*a6,-a3*a4+2*a1*a5,a4*a4-4*a5*a6]
lhs7=[c[0]*d[0],c[2]*d[2],c[1]*d[1],(c[0]*d[2]+c[2]*d[0])/2,
      I*(c[0]*d[2]-c[2]*d[0])/2,(c[0]*d[1]-I*c[1]*d[0])/(1-I),
      (c[0]*d[1]+I*c[1]*d[0])/(1+I),(c[1]*d[2]+I*c[2]*d[1])/(1+I),
      -I*(c[1]*d[2]-I*c[2]*d[1])/(1+I)]
rhs7=[a1*a1-2*a2*a6-4*a4*a6,a3*a3-2*a2*a5-4*a4*a5,a2*a2-2*a1*a3+2*a2*a4,
      -a1*a3+a2*a4+8*a5*a6,b[1]*b[3],a1*a2-4*a3*a6,b[0]*b[1],
      -a2*a3+4*a1*a5,b[1]*b[2]]
assert all(S.expand(z-w)==0 for z,w in zip(lhs6+lhs7,rhs6+rhs7))
# Matrix M over the 9-parameter Grassmannian chart of invariant 3-planes.
u,v,w=S.symbols('u v w')
A=S.symbols('A1:4'); B=S.symbols('B1:4'); C=S.symbols('C1:4')
p4=sum(z*q for z,q in zip(A,[u,v,w]));p5=sum(z*q for z,q in zip(B,[u,v,w]));p6=sum(z*q for z,q in zip(C,[u,v,w]))
alpha=[u*u,v*v,w*w,u*v,u*w,v*w]
gamma=[u*u-2*v*p6-4*p4*p6,v*v-2*u*w+2*v*p4,w*w-2*v*p5-4*p4*p5,
       u*v-4*w*p6,-u*w+v*p4+8*p5*p6,-v*w+4*u*p5]
M=S.Matrix([[S.Poly(S.expand(f),u,v,w).coeff_monomial(a) for a in alpha] for f in gamma])
zero={p:0 for p in A+B+C}
M0=M.subs(zero)
assert M0.det()==1 and M0.rank()==6
# Quadratic b-products span the six alpha monomials on a nonempty open.
qb=[u*u-4*v*p6,v*v-4*(u*w-v*p4)+16*p5*p6,w*w-4*v*p5,
    u*w-2*v*p4,u*p4-2*w*p6,-w*p4+2*u*p5,p4*p4-4*p5*p6]
N=S.Matrix([[S.Poly(S.expand(f),u,v,w).coeff_monomial(a) for a in alpha] for f in qb])
# A single rational coefficient tuple witnesses both open rank conditions.
chosen=dict(zip(A+B+C,[1,0,1,0,1,1,1,1,0]))
assert N.subs(chosen).rank()==6
assert M.subs(chosen).det()!=0
out['koike_2004']={'sixteen_polynomial_identities':True,
                   'M_at_zero':str(M0),'det_M_at_zero':int(M0.det()),
                   'rank_M_at_zero':M0.rank(),
                   'chosen_coefficients':{str(k):v for k,v in chosen.items()},
                   'det_M_at_chosen':int(M.subs(chosen).det()),
                   'rank_quadratic_basis_at_chosen':N.subs(chosen).rank(),
                   'geometric_conclusion':'generic period differential rank 9, using Koike Proposition 3.1 for the nonempty smooth etale open; no smoothness assertion for these particular coefficient tuples'}

# Integral anti-invariant homology block for a cyclic quartic etale cover.
T=S.Matrix([[0,0,0,1],[1,0,0,0],[0,1,0,0],[0,0,1,0]])
E=S.Matrix([[1,0],[0,1],[-1,0],[0,-1]])
assert E.T*E==2*S.eye(2)
assert T*E==E*S.Matrix([[0,-1],[1,0]])
H=S.Matrix([[0,I],[-I,0]])
P=S.diag(1,I)
assert S.conjugate(P.T)*H*P==S.Matrix([[0,-1],[-1,0]]) # convention: linear in second slot
# Under the paper's first-slot convention use P^t H conjugate(P).
assert P.T*H*S.conjugate(P)==S.Matrix([[0,1],[1,0]])
out['quartic_integral_lattice']={'anti_invariant_pairing':str(E.T*E),'Hermitian_block':str(H),'first_slot_basis_change':str(P),'result':'U'}

A4=3**6*factorial(13)//factorial(7); T4=3**9*factorial(9)*4**3
A3=3**6*factorial(10)//factorial(4); T3=3**6*factorial(6)*3**3
out['detector_constants']={'Q_i':{'W6_degree':A4,'full_norm_Prym_dimension':9,'full_Prym_degree':T4,'D6':A4*T4*8//27},
                           'Q_omega':{'W6_degree':A3,'full_norm_Prym_dimension':6,'full_Prym_degree':T3,'D6':A3*T3//27}}
Path(__file__).with_name('certificates.json').write_text(json.dumps(out,indent=2)+'\n')
print(json.dumps(out,indent=2))
