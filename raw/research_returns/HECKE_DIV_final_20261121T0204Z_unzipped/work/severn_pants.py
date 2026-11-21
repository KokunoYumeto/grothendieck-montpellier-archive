"""Check that the printed boundary intervals form pants and all vertex H1_par vanish."""
from pathlib import Path
import json,io,contextlib
with contextlib.redirect_stdout(io.StringIO()):
    from severn_monodromy import K,T,intervals,eye,mul,add,scale,adj,rank,eq
nodes=[(a,b) for a,b,k in intervals]
root=(1,20)
def prod(I):
    A=eye(6)
    for i in range(I[0]-1,I[1]):A=mul(A,T[i])
    return A
def included(I,J):return J[0]<=I[0] and I[1]<=J[1]
assert all(included(I,J) or included(J,I) or I[1]<J[0] or J[1]<I[0] for I in nodes for J in nodes)
rows=[]
for node in nodes+[root]:
    proper=[I for I in nodes if I!=node and included(I,node)]
    children=[I for I in proper if not any(I!=J and included(I,J) for J in proper)]
    leaves=[(i,i) for i in range(node[0],node[1]+1) if not any(a<=i<=b for a,b in children)]
    parts=sorted(children+leaves)
    assert len(parts)==(3 if node==root else 2)
    mons=[prod(I) for I in parts]
    if node!=root:mons.append(adj(prod(node)))
    assert eq(mul(mul(mons[0],mons[1]),mons[2]),eye(6))
    diffs=[add(eye(6),scale(K(-1),g)) for g in mons]
    ranks=[rank(A) for A in diffs]
    fixed=6-rank([row for A in diffs for row in A])
    hpar=sum(ranks)-12+2*fixed
    rows.append({'node':list(node),'parts':[list(I) for I in parts],'ranks':ranks,'common_fixed_dimension':fixed,'H1_par_K_dimension':hpar})
result={'number_of_curves':len(nodes),'pairwise_disjoint_laminar':True,'number_of_pants':len(rows),'all_vertex_parabolic_H1_zero':all(r['H1_par_K_dimension']==0 for r in rows),'pants':rows}
Path(__file__).with_suffix('.json').write_text(json.dumps(result,indent=2)+'\n')
print(json.dumps(result,indent=2))
