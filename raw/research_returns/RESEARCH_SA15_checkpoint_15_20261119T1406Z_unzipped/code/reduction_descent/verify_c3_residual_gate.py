#!/usr/bin/env python3
"""Exact polynomial and valuation enumeration for B39, no local-pair search."""
from pathlib import Path
import itertools,json,math,time
import sympy as s
started=time.perf_counter()
t,D,w,pi=s.symbols('t D w pi')
a1,a3=3*t,t**3-D
b2,b4,b6=a1*a1,a1*a3,a3*a3
c4=s.expand(b2*b2-24*b4)
disc=s.expand(-8*b4**3-27*b6**2+9*b2*b4*b6)
assert s.expand(c4-9*t*(t**3+8*D))==0
assert s.expand(disc-27*D*(t**3-D)**3)==0
assert s.rem(s.Poly((1+pi*w)**3-1-pi**3*(w**3+w+pi*w*w),pi),s.Poly(pi*pi-3,pi))==0
cube_vals=[]
for r in range(1,1001):
    terms=[6+r,6+2*r,3*r]
    if min(terms)<9:
        assert terms.count(min(terms))==1 and min(terms) in [3,6]
    cube_vals.append({'root_deviation':r,'term_valuations':terms})

def tame(delta):return 4//math.gcd(4,delta)
tables=[];direct=[];reverse=[]
for d in [1,2]:
    source=[];target=[]
    for r in [-1,0,1]:
        S=min(3*r,d);delta=6+d+3*S
        assert 6+3*r-d>0
        source.append({'r':r,'S':S,'delta':delta,'tame':tame(delta)})
    for r in [-2,-1,0]:
        S=min(3*r,-d);delta=6-d+3*S
        assert 6+3*r+d>0
        target.append({'r':r,'S':S,'delta':delta,'tame':tame(delta)})
    tables.append({'d':d,'source':source,'reverse_target':target})
    pairs=[]
    for A,B in itertools.product(source,repeat=2):
        if A['tame']!=B['tame'] and (A['S']-B['S'])%3==0:
            assert {A['S'],B['S']}=={-3,0}
            pairs.append([A['S'],B['S']])
    deviation=3+d
    assert deviation in [4,5] and deviation%3 and deviation<9
    direct.append({'d':d,'opposite_pairs':pairs,'forbidden_deviation':deviation})
    for A,B in itertools.product(source,target):
        if A['tame']!=B['tame'] and (A['S']+B['S'])%3==0:
            x,y=3-d-B['S'],3+d-A['S']
            assert x!=y and min(x,y) in [4,5,7]
            assert min(x,y)<9 and min(x,y)%3
            reverse.append({'d':d,'S_E':A['S'],'S_target':B['S'],
                            'deviation_terms':[x,y,x+y],
                            'forbidden_deviation':min(x,y)})
assert len(reverse)==6
unit=[]
for depth in [1,2]:
    rows=[{'S':S,'delta':6+3*S,'tame':tame(6+3*S)} for S in [-3,0,depth]]
    dp=[];rp=[]
    for A,B in itertools.product(rows,repeat=2):
        if A['tame']==B['tame']:continue
        if (A['S']-B['S'])%3==0:dp.append([A['S'],B['S']])
        if (A['S']+B['S'])%3==0:rp.append([A['S'],B['S']])
    assert dp==[[-3,0],[0,-3]] and rp==dp
    unit.append({'depth':depth,'rows':rows,'direct_opposite_pairs':dp,'reverse_opposite_pairs':rp})
out={'status':'PASS','polynomial_identities':['c4','Delta','Hensel(1+pi*w)^3'],
     'cube_deviation_cases':len(cube_vals),'tables':tables,
     'direct_nonunit_cases':direct,'reverse_nonunit_cases':reverse,'unit_depth_cases':unit,
     'remaining_rows':[{'residual':'C4','individual':[3,6],'joint':18,'j':[6,6]},
                       {'residual':'C3','individual':[12,6],'joint':36,'j':[3,'>=6']}],
     'scope':'Necessary restrictions only; neither final level27 row evaluated for existence',
     'elapsed_seconds':time.perf_counter()-started}
Path(__file__).with_suffix('.output.json').write_text(json.dumps(out,indent=2)+'\n')
print(json.dumps(out,indent=2))
