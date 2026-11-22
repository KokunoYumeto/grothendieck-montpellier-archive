#!/usr/bin/env python3
"""Finite symbolic checks for B.2i; the proof of nonfilteredness is in the paper."""
import json
from pathlib import Path
import time
import sympy as sp

started=time.perf_counter()
a,b,x,y,z,w,t,u,v,s=sp.symbols('a b x y z w t u v s')
records=[]
for p in (2,3,5):
    f=x**p-a
    g=y**p-b
    graph=w*g-z*f
    assertions={
        'birational_inverse':sp.cancel((z*f/g)*g/f-z)==0,
        'graph_vanishes_on_map':sp.cancel(graph.subs(w,z*f/g))==0,
        'invertible_chart_relation':sp.expand(graph.subs(z,t*w)-w*(g-t*f))==0,
        'derivative_t':sp.Poly(sp.diff(g-t*f,t)+f,x,y,t,a,b,modulus=p).is_zero,
        'derivative_x_zero_mod_p':sp.Poly(sp.diff(g-t*f,x),x,y,t,a,b,modulus=p).is_zero,
        'derivative_y_zero_mod_p':sp.Poly(sp.diff(g-t*f,y),x,y,t,a,b,modulus=p).is_zero,
        'normalization_substitution':sp.expand((v**p-t*u**p).subs({v:u*s,t:s**p}))==0,
        'singular_relation_has_no_linear_term':all(sum(m[:2])>=2 for m,c in sp.Poly(v**p-t*u**p,u,v,t,modulus=p).terms()),
    }
    assert all(assertions.values()),(p,assertions)
    records.append({'prime':p,'assertions':assertions,'assertion_count':len(assertions)})
out={'statement':'B.2i','scope':'Symbolic identities for three primes; regularity and nonfilteredness require the written proof.','runs':records,'total_assertions':sum(r['assertion_count'] for r in records),'all_passed':True,'sympy_version':sp.__version__,'elapsed_seconds':time.perf_counter()-started}
dest=Path(__file__).resolve().parent/'output'/'imperfect_graph_certificate_B.json'
dest.write_text(json.dumps(out,indent=2)+'\n')
print(json.dumps(out,indent=2))
