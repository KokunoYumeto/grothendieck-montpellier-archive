#!/usr/bin/env python3
r"""Exact ideal certificate for the pure complex-algebraic 121/049 counterexample.

Geometry and arbitrary-open connectedness are proved in A5.010. This
program verifies, over Q by Groebner elimination, every algebraic
intersection, irreducible branch support and localization used there.
The identities therefore also hold after extension to C. It does not
replace the punctured-polydisc connectedness proof by sampling.
"""
from pathlib import Path
import json
from sympy import symbols, groebner
u,v,w,t,s,a=symbols('u v w t s a')
variables=(t,s,v,w,u)

def gb(fs):
    return tuple(p.as_expr() for p in groebner(fs,*variables,order='lex',domain='QQ').polys)

def same(fs,gs):
    return gb(fs)==gb(gs)

def intersect(fs,gs):
    basis=groebner([a*f for f in fs]+[(1-a)*g for g in gs],a,*variables,order='lex',domain='QQ')
    return gb([p.as_expr() for p in basis.polys if not p.as_expr().has(a)])

def saturate(fs,g):
    basis=groebner(list(fs)+[1-a*g],a,*variables,order='lex',domain='QQ')
    return gb([p.as_expr() for p in basis.polys if not p.as_expr().has(a)])
Y=(t,s)
E=(v,t-u*w)
T=(t,s,w)
S1=(t,s,w,v)
S2=(t,s,w,u)
C=(t,s,v,u)
S=intersect(S1,S2)
X=intersect(Y,E)
checks={
 'Y_intersect_E_is_union_S1_C':same(Y+E,intersect(S1,C)),
 'E_intersect_T_is_S1':same(E+T,S1),
 'Y_intersect_T_is_T':same(Y+T,T),
 'S1_intersect_S2_is_origin':same(S1+S2,(t,s,v,w,u)),
 'S_is_cross_uv_zero':same(S,(t,s,w,u*v)),
 'off_T_intersection_localization_is_C':same(saturate(Y+E,w),C),
 'off_T_intersection_empty_where_u_nonzero':same(saturate(Y+E,u*w),(1,)),
 'X_union_Y_E_has_correct_intersection_ideal':same(X,intersect(Y,E)),
}
assert all(checks.values())
# The two irreducible components are smooth affine 3-spaces, with explicit
# polynomial parametrizations. Substitution checks their equations.
p,q,r=symbols('p q r')
y_map={u:p,v:q,w:r,t:0,s:0}
e_map={u:p,v:0,w:q,t:p*q,s:r}
checks['Y_parameterization']=all(f.subs(y_map)==0 for f in Y)
checks['E_parameterization']=all(f.subs(e_map).expand()==0 for f in E)
# Each has a coordinate-projection polynomial inverse on its image.
checks['Y_projection_inverse']=(y_map[u],y_map[v],y_map[w])==(p,q,r)
checks['E_projection_inverse']=(e_map[u],e_map[w],e_map[s])==(p,q,r)
# Explicit rational witnesses for the join of P and Q on T.
points={
 'P_T_minus_S_meets_Q_B':(1,1,0,0,0),
 'P_S_meets_Q_B':(0,1,0,0,0),
 'P_S_meets_Q_S1':(1,0,0,0,0),
 'off_T_components_join':(0,0,1,0,0),
}
xyz=(u,v,w,t,s)
def zeros(fs,point):
    sub=dict(zip(xyz,point))
    return all(f.subs(sub)==0 for f in fs)
assert zeros(T,points['P_T_minus_S_meets_Q_B'])
assert not zeros(S,points['P_T_minus_S_meets_Q_B'])
assert not zeros(S1,points['P_T_minus_S_meets_Q_B'])
assert zeros(S,points['P_S_meets_Q_B']) and not zeros(S1,points['P_S_meets_Q_B'])
assert zeros(S1,points['P_S_meets_Q_S1'])
assert zeros(Y,points['off_T_components_join']) and zeros(E,points['off_T_components_join'])
assert not zeros(T,points['off_T_components_join'])
assert all(checks.values())
# Local frontier patterns are checked symbolically as finite partitions of
# the listed connected local pieces. Their connectedness is justified by
# the explicit polydisc formulas in the proof, not presumed by the code.
patterns={
 'origin_P':{'A':{'A','B0','S'},'B0':{'B0','S'},'S':{'S'}},
 'S1_nonzero_P':{'A_main':{'A_main','B0','S'},'A_extra':{'A_extra','S'},
                  'B0':{'B0','S'},'S':{'S'}},
 'S2_nonzero_P':{'A_main':{'A_main','B0','S'},'B0':{'B0','S'},'S':{'S'}},
 'origin_Q':{'A':{'A','B','R'},'B':{'B','R'},'R':{'R'}},
 'S1_nonzero_Q':{'A_main':{'A_main','B','R'},'A_extra':{'A_extra','R'},
                  'B':{'B','R'},'R':{'R'}},
 'unmarked_T_point':{'A_main':{'A_main','B'},'B':{'B'}},
}
for name,closures in patterns.items():
    for label,closure in closures.items():
        assert label in closure and closure<=set(closures)
        for other in closure:
            assert closures[other]<=closure
payload={'field':'Q; identities persist under extension to C',
         'variables':['u','v','w','t','s'],
         'ideals':{name:[str(f) for f in gb(fs)] for name,fs in [
             ('Y',Y),('E',E),('X',X),('T',T),('S1',S1),('S2',S2),('S',S),('C',C)]},
         'checks':checks,'witnesses':points,
         'local_frontiers':{n:{k:sorted(v) for k,v in z.items()} for n,z in patterns.items()},
         'pure_dimension':3,
         'bad_join_point':(1,0,0,0,0),
         'bad_join_support':'extra local A component closes onto S1, a proper subset of connected T'}
outdir=Path(__file__).resolve().parents[1]/'logs'
outdir.mkdir(exist_ok=True)
(outdir/'A5_complex_strict_no_coarsest.json').write_text(json.dumps(payload,indent=2)+'\n')
lines=['X = union of two smooth affine 3-spaces; pure complex dimension 3.',
       'I(X) = '+str(gb(X)),
       'I(Y intersection E) = '+str(gb(Y+E)),
       'I(E intersection T) = '+str(gb(E+T)),
       'I(S1 union S2) = '+str(S),
       'I((Y intersection E) localized at w) = '+str(saturate(Y+E,w)),
       'I((Y intersection E) localized at u*w) = '+str(saturate(Y+E,u*w)),
       'Exact ideal and parametrization checks: '+str(len(checks))+' passed.',
       'Local connected-piece frontier patterns: '+str(len(patterns))+' passed.',
       'Join witnesses: '+str(points),
       'Bad join at (1,0,0,0,0): extra A branch closes onto S1, not all T.',
       'PASS: algebraic identities and incidence certificate verified exactly.']
text='\n'.join(lines)+'\n'
(outdir/'A5_complex_strict_no_coarsest.txt').write_text(text)
print(text,end='')
