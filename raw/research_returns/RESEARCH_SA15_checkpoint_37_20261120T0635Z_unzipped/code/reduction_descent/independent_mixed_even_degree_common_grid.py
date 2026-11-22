"""Exact common-grid certificate for the proposed all-even mixed-product argument.

Only F2 graph quotients, projection witnesses, and rank arithmetic are checked.
No geometric monodromy, gluing, or specialization statement follows from a run.
The uniform graph proof is in notes/mixed_even_common_grid_candidate.tex.
"""
from pathlib import Path
import datetime,json,time
started=time.perf_counter()
def rank(vectors):
    pivots={}
    for v in vectors:
        while v:
            p=v.bit_length()-1
            if p in pivots:v^=pivots[p]
            else:pivots[p]=v;break
    return len(pivots)
def grid_cuts(n):
    return [sum(1<<(n*i+j) for j in range(n)) for i in range(n)]+[sum(1<<(n*i+j) for i in range(n)) for j in range(n)]
cases=[]
for d in range(2,21,2):
    n=3*d;q=n-3;N=18*(d-1)
    edge=lambda i,j:1<<(n*i+j)
    cuts=grid_cuts(n);cutrank=rank(cuts)
    assert cutrank==2*n-1
    small={0,1,2};large=set(range(n))-small
    alt={0,1,3};partitions=[]
    for I,J in [(small,small),(alt,alt)]:
        crosses=[edge(i,j) for i in range(n) for j in range(n) if (i in I)!=(j in J)]
        assert len(crosses)==N
        heart=[crosses[0]^v for v in crosses[1:]]
        assert rank(heart)==N-1
        assert rank(cuts+heart)-cutrank==N-2
        assert rank(cuts+[sum(crosses)])==cutrank
        partitions.append({'selected_rows':sorted(I),'selected_columns':sorted(J),'cross_edges':N,'heart_rank_in_graph':N-2})
    v_small=edge(0,2)^edge(1,2);v_large=edge(3,4)^edge(3,5)
    alt_edges={(i,j) for i in range(n) for j in range(n) if (i in alt)!=(j in alt)}
    assert {(0,2),(1,2),(3,4),(3,5)}<=alt_edges
    cyc_small=edge(0,1)^edge(0,2)^edge(2,1)^edge(2,2)
    cyc_large=edge(3,3)^edge(3,4)^edge(4,3)^edge(4,4)
    assert (v_small&cyc_small).bit_count()%2==1
    assert (v_large&cyc_large).bit_count()%2==1
    def project(v,selected):
        indices=sorted(selected);m=len(indices)
        return sum(((v>>(n*i+j))&1)<<(m*a+b) for a,i in enumerate(indices) for b,j in enumerate(indices))
    for v,selected in [(v_small,small),(v_large,large)]:
        internal=grid_cuts(len(selected));assert rank(internal+[project(v,selected)])==rank(internal)+1
        assert project(v,set(range(n))-selected)==0
    r_large=9*(d-1)**2-1;relative=9*d*d-2;K=relative-2
    graph=(n-1)**2;grid_relative=graph+n-1
    assert grid_relative==9*d*d-3*d
    assert r_large+8+(N-2)==K
    cases.append({'d':d,'grid_side':n,'global_graph_rank':graph,'grid_relative_rank':grid_relative,
                  'generic_relative_rank':relative,'common_covector_kernel_rank':K,
                  'large_odd_block_rank':r_large,'small_block_rank':8,
                  'partitions':partitions,'internal_projection_witnesses':[True,True]})
record={'status':'PASS','actual_utc':datetime.datetime.now(datetime.timezone.utc).isoformat(),
        'scope':'Exact finite graph arithmetic and rank identities only; all-even geometric proof remains separate.',
        'tested_even_degrees':[r['d'] for r in cases],'cases':cases,
        'runtime_seconds':time.perf_counter()-started}
w=Path(__file__).resolve().parents[1];dest=w/'outputs/mixed_even_degree_common_grid.json'
# Independent audit: original author destination is never written.
print(json.dumps(record,indent=2))
