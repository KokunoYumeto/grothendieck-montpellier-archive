#!/usr/bin/env python3
"""Finite algebra checks for TG.1--TG.5; not a Chow/K-theory certificate."""
import datetime
import itertools
import json
from pathlib import Path
import time
import sympy as s

started = datetime.datetime.now(datetime.timezone.utc).isoformat()
tick = time.perf_counter()
x = s.symbols('x0:4')
G = sum(t**5 for t in x) + sum(x[i]**4*x[j] for i in range(4) for j in range(i+1,4))
Q = s.prod(x)
checks = []

def record(name, ok, **extra):
    checks.append(dict(name=name, passed=bool(ok), **extra))
    assert ok, name

for omitted in range(4):
    variables = [x[i] for i in range(4) if i != omitted]
    face = G.subs(x[omitted], 0)
    for chosen in variables:
        others = [v for v in variables if v != chosen]
        g = s.expand(face.subs(chosen, 1))
        gb = s.groebner([g] + [s.diff(g,v) for v in others], *others, modulus=5)
        record(f'char5_face_{omitted}_chart_{chosen}', list(gb) == [1], groebner=[str(v) for v in gb])

for i,j in itertools.combinations(range(4),2):
    edge = G.subs({x[k]:0 for k in range(4) if k not in (i,j)})
    g = s.Poly(edge.subs(x[j],1),x[i],modulus=5)
    gcd = s.gcd(g,g.diff())
    record(f'char5_edge_{i}_{j}', gcd.degree()==0 and g.degree()==5 and g.eval(0)!=0,
           polynomial=str(g.as_expr()), gcd=str(gcd.as_expr()))

for i in range(4):
    record(f'char5_vertex_{i}', G.subs({x[j]:int(i==j) for j in range(4)}) == 1)

for p in [2,3,7,11,13,17,19]:
    t=s.Symbol('t')
    g=s.Poly(t**5+1,t,modulus=p)
    record(f'fermat_edge_prime_{p}', s.gcd(g,g.diff()).degree()==0)

F=Q-G
euler=s.expand(sum(x[i]*s.diff(F,x[i]) for i in range(4))-(4*Q-5*G))
record('integer_Euler_identity',euler==0)
u,v,t,w,a,b=s.symbols('u v t w a b')
record('u_chart_equation',s.expand((u*v-t*w).subs({t:u*a,v:a*w},simultaneous=True))==0)
record('t_chart_equation',s.expand((u*v-t*w).subs({u:t*b,w:b*v},simultaneous=True))==0)
record('overlap_v_identity',s.simplify((a*w).subs(w,b*v).subs(b,1/a)-v)==0)
record('overlap_t_identity',s.simplify((u*a).subs(u,t*b).subs(b,1/a)-t)==0)

assigned=[0]*4
edge_assignment=[]
for i,j in itertools.combinations(range(4),2):
    assigned[i]+=5
    edge_assignment.append(dict(edge=[i,j], chosen_component=i, nodes=5))
record('ordered_assignment',assigned==[15,10,5,0], assigned=assigned, edges=edge_assignment)
record('tetrahedral_euler',4-6+4==2)

out=dict(started_utc=started, finished_utc=datetime.datetime.now(datetime.timezone.utc).isoformat(),
         runtime_seconds=time.perf_counter()-tick, check_count=len(checks), checks=checks,
         scope='Exact char5 face/edge Groebner checks, symbolic node charts/Euler identity, and finite incidence count. General-prime geometry is proved in TG, not inferred from tested primes. No K-theory or Chow conclusion.')
dest=Path(__file__).resolve().parent.parent/'output'/'tetrahedral_resolution_certificate.json'
dest.write_text(json.dumps(out,indent=2)+'\n')
print(json.dumps(out,indent=2))
