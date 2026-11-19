"""Exact finite trace and joint-order certificate for B-RD32."""
from pathlib import Path
from time import perf_counter
import itertools, json, math
import sympy as S

start = perf_counter()
z=S.symbols('z')
def cyc(f): return S.rem(S.Poly(f,z),S.Poly(z**4+1,z)).as_expr()
traces=[]
for a in range(8):
    norm=cyc(z**(4*a))
    trace=cyc(z**a+z**(3*a))
    if norm==1:
        assert trace in (2,-2,0)
        order=8//math.gcd(8,a)
        assert trace=={1:2,2:-2,4:0}[order]
    else:
        assert norm==-1 and 8//math.gcd(8,a)==8
        assert cyc(trace**2)==-2
    traces.append({'a':a,'norm':str(norm),'trace':str(trace)})

# Each norm-one image is represented by (wild order, tame order).
types=[(1,1),(1,2),(1,4),(3,1),(3,2),(3,4)]
joint=[]
remaining81=[]
remaining27=[]
for a,b in itertools.combinations_with_replacement(types,2):
    p1,t1=a; p2,t2=b
    wilds=(1,) if p1==p2==1 else ((3,9) if p1==p2==3 else (3,))
    for wild in wilds:
        m=wild*math.lcm(t1,t2)
        assert m in (1,2,3,4,6,9,12,18,36)
        row={'individual_orders':sorted([p1*t1,p2*t2]),
             'tame_orders':[t1,t2],'joint_order':m}
        joint.append(row)
        if t1!=t2 and m>9: remaining27.append(row)
        if t1!=t2 and m>27:
            assert m==36 and wild==9
            assert row['individual_orders'] in ([3,12],[6,12])
            remaining81.append(row)
assert {tuple(r['individual_orders']) for r in remaining81}=={(3,12),(6,12)}
assert all(2*r['joint_order']<=2*3**4 for r in joint)
assert 16<=2*3**2
result={'status':'PASS','cyclotomic_traces':traces,
        'joint_order_cases':len(joint),'remaining27_numerical_cases':remaining27,
        'remaining81_numerical_cases':remaining81,
        'elapsed_seconds':perf_counter()-start}
print(json.dumps(result,indent=2))
Path(__file__).with_suffix('.output.json').write_text(json.dumps(result,indent=2)+'\n')
