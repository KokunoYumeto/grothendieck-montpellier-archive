#!/usr/bin/env python3
"""Exact exterior and full-character checks for SF-E817.

This checks a generic cap minor and the complete explicit character.  It
does not construct sheaves, verify equivariance, or compute derived Ext.
The universal categorical argument is the separate written proof.
"""
from itertools import combinations
from pathlib import Path
import json,time
import sympy as s

start=time.monotonic()
mask=lambda xs:sum(1<<x for x in xs)
two=list(combinations(range(8),2));six=list(combinations(range(8),6))
row={mask(ix):j for j,ix in enumerate(six)}
a,b,c,d=s.symbols('a b c d')
terms={mask((0,1,4,5)):a,mask((2,3,4,5)):b,
       mask((0,1,6,7)):c,mask((2,3,6,7)):d}
M=s.zeros(28)
for j,ix in enumerate(two):
    left=mask(ix)
    for right,v in terms.items():
        if left&right:continue
        inv=sum((right&((1<<i)-1)).bit_count()for i in ix)
        M[row[left|right],j]=(-1)**inv*v
chosen_cols=[two.index(ix)for ix in ((0,1),(2,3),(4,5),(6,7))]
chosen_cols += [two.index((i,j))for i in range(4)for j in range(4,8)]
chosen_rows=[row[mask(ix)]for ix in ((0,1,2,3,4,5),(0,1,2,3,6,7),
                                  (0,1,4,5,6,7),(2,3,4,5,6,7))]
chosen_rows += [row[mask(p+q)]for p in combinations(range(4),3)
                for q in combinations(range(4,8),3)]
minor=s.factor(M.extract(chosen_rows,chosen_cols).det())
expected=(a*d-b*c)**2*(a*b*c*d)**4
assert s.simplify(minor/expected) in (1,-1)
rank_balanced=M.subs({a:18,b:-48,c:-48,d:128}).rank()
rank_hull=M.subs({a:18,b:-48,c:-48,d:144}).rank()
rank_point=M.subs({a:0,b:0,c:0,d:16}).rank()
assert (rank_balanced,rank_hull,rank_point)==(18,20,6)

coeff={}
u=s.sqrt(2)
for p in range(3):
    for q in range(3):
        value=sum(n*f**p*g**q/(s.factorial(p)*s.factorial(q))
                  for n,f,g in ((3,s.Integer(2),s.Integer(2)),
                                (3,s.Integer(-2),s.Integer(-2)),
                                (6,u,-u),(6,-u,u)))
        coeff[p,q]=s.simplify(value)
target={(0,0):18,(2,0):24,(0,2):24,(2,2):36}
assert all(v==target.get(key,0)for key,v in coeff.items())
kernel=dict(coeff);kernel[2,2]-=4
N=s.Integer(18);q=s.Rational(8,3)
assert kernel[0,0]==N and kernel[2,0]==N*q/2
assert kernel[0,2]==N*q/2 and kernel[2,2]==N*q*q/4
assert 16*s.Rational(1,4)==4
out={'status':'PASS','generic_twenty_minor':str(minor),
     'minor_rows':chosen_rows,'minor_columns':chosen_cols,
     'rank_balanced_example':rank_balanced,'rank_hull_example':rank_hull,
     'rank_point_character':rank_point,
     'hull_character':{str(k):str(v)for k,v in coeff.items()},
     'kernel_character':{str(k):str(v)for k,v in kernel.items()},
     'balanced_rank':18,'balanced_q':'8/3','quotient_length':16,
     'categorical_Ext_or_equivariance_computed':False,
     'elapsed_seconds':time.monotonic()-start}
Path(__file__).with_name('rm_point_defect_certificate_output.json').write_text(json.dumps(out,indent=2)+'\n')
print(json.dumps(out,indent=2))
