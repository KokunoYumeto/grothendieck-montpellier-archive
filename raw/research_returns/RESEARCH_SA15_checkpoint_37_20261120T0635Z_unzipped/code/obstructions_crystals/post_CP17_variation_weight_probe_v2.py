#!/usr/bin/env python3
"""Finite probe of the weight restrictions of the trace-direction quadratic.
This is one coefficient point, not a uniform geometric assertion.
"""
from pathlib import Path
from time import perf_counter
import ast,json
start=perf_counter()
source=Path(__file__).with_name('post_CP16_variation_trace_projection_probe.py')
nodes=[]
for node in ast.parse(source.read_text()).body:
    if isinstance(node,ast.Assign) and any(isinstance(t,ast.Name) and t.id=='out' for t in node.targets):
        break
    nodes.append(node)
env={'__file__':str(source.resolve())}
exec(compile(ast.Module(body=nodes,type_ignores=[]),str(source),'exec'),env)
rank,apply,nullspace=(env[x] for x in ('rank','apply','nullspace'))
trace=env['trace'];pairs=env['smallpairs'];idx=env['smallidx'];n=len(pairs)
Dtarget=env['ns']['variation']
piv={}
for j,v in enumerate(trace):
    lift=1<<j
    while v:
        k=v.bit_length()-1
        if k in piv:v^=piv[k][0];lift^=piv[k][1]
        else:piv[k]=(v,lift);break
def lift(v):
    out=0
    while v:
        k=v.bit_length()-1
        v^=piv[k][0];out^=piv[k][1]
    return out
def variation(v):
    z=lift(v);d=[0,0]
    for j,m in enumerate(Dtarget):
        if z>>j&1:d=[a^b for a,b in zip(d,m)]
    return d
def flat(m):return m[0]|(m[1]<<2)
def toral(v):
    ans=0
    for j,((i,h),z) in enumerate(pairs):
        if not v>>j&1:continue
        if (i+h)%2:ans^=1<<j
        if h:ans^=1<<idx[((i+2,0),z)]
    return ans
e=[toral(1<<j) for j in range(n)]
assert all(apply(e,apply(e,1<<j))==apply(e,1<<j) for j in range(n))
rows=env['transpose'](e,n)
w0=nullspace(rows,n);w1=nullspace([r^(1<<j) for j,r in enumerate(rows)],n)
assert len(w0)==len(w1)==9
spaces=[]
for w in (w0,w1):
    mats=[variation(v) for v in w]
    entries=[flat(v) for v in mats]
    spaces.append({'basis_vectors':w,'matrices':mats,'rank':rank(entries),
                   'distinct_matrices':sorted(set(entries))})
source_vector=env['source_section']
source_weight_one=toral(source_vector)
assert variation(source_vector)==[0,0]
assert variation(source_weight_one)==[0,0]
result={'source_variation':variation(source_vector),'toral_source_variation':variation(source_weight_one),'status':'COMPLETED_FINITE_PROBE','scope':'One sharp F2 source, toral weight restriction of descended variation only',
        'source_section':env['source_section'],'weight_spaces':spaces,
        'all_trace_direction_matrices':[variation(1<<j) for j in range(n)],
        'elapsed_seconds':perf_counter()-start}
Path(__file__).with_suffix('.output.json').write_text(json.dumps(result,indent=2)+'\n')
print(json.dumps(result,indent=2))
