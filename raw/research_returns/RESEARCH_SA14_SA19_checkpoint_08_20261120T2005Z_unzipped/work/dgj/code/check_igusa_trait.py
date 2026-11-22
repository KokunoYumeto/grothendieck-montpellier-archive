#!/usr/bin/env python3
import json
from pathlib import Path
from time import perf_counter
import sympy as s

t0=perf_counter()
w=s.symbols('w')
hensel=2*w*w-w+8
curve_residual=(1**2*w+(-2)*1*w)-((-2)**3+(-2)*w*w)
assert s.expand(curve_residual-hensel)==0
b2,b4,b6,b8=1,2,0,-1
discriminant=-b2*b2*b8-8*b4**3-27*b6**2+9*b2*b4*b6
assert discriminant == -63
negative_Q=(-2,-1-(-2),w)
assert negative_Q == (-2,1,w)
approximations=[]
for n in (4,8,16,32,64):
    mod=2**n
    a=0
    for _ in range(n):
        a=(8+2*a*a)%mod
    assert (2*a*a-a+8)%mod == 0
    assert a%8 == 0
    approximations.append({'n':n,'w_mod_2n':a,'residual_mod_2n':0})
affine_F2=[]
for x in range(2):
    for y in range(2):
        if (y*y+x*y-x*x*x-x)%2==0:
            affine_F2.append([x,y])
assert len(affine_F2)+1==4
out={'elliptic_curve':'Y^2 Z + X Y Z = X^3 + X Z^2',
     'discriminant':discriminant,'P':[0,0,1],
     'Q':['-2','1','w'],'hensel_polynomial':str(hensel),
     'projective_curve_residual':str(s.expand(curve_residual)),
     'negative_Q_equals_Q':True,'special_Q':[0,1,0],
     'affine_points_F2':affine_F2,'number_points_F2':4,
     'hensel_approximations':approximations,
     'albanese_map_degrees':{'generic':4,'special':2},
     'Pic_tau_finite_flat_degree_over_F_dual':8,
     'runtime_seconds':round(perf_counter()-t0,6)}
target=Path(__file__).with_name('check_igusa_trait_output.json')
target.write_text(json.dumps(out,indent=2)+'\n')
print(json.dumps(out,indent=2))
