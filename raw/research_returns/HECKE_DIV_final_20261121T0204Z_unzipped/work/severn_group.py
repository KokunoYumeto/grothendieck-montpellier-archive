"""Reconstruct the finite reflection group as a faithful permutation action.
The orbit starts at printed v_2, with no use of a group database or claimed order.
"""
from pathlib import Path
import json,io,contextlib
with contextlib.redirect_stdout(io.StringIO()):
    from severn_monodromy import K,roots,norms,rank,w
from sympy.combinatorics import Permutation,PermutationGroup
K.__hash__=lambda z:hash((z.a,z.b))
def act(v,n,x):
    fac=2*sum((z.conj()*y for z,y in zip(v,x)),K())/n
    return tuple(y-z*fac for z,y in zip(v,x))
orbit=[tuple(roots[1])];idx={orbit[0]:0};at=0
while at<len(orbit):
    x=orbit[at]
    for v,n in zip(roots,norms):
        y=act(v,n,x)
        if y not in idx:
            idx[y]=len(orbit);orbit.append(y)
            if len(orbit)>5000:raise RuntimeError('orbit did not close below safety threshold')
    at+=1
perms=[]
for v,n in zip(roots,norms):perms.append(Permutation([idx[act(v,n,x)] for x in orbit]))
G=PermutationGroup(perms)
order=int(G.order())
spanrank=rank([list(x) for x in orbit])
# Since the orbit spans K^6, the permutation representation is faithful.
graph=[[j for j,u in enumerate(roots) if sum((a.conj()*b for a,b in zip(v,u)),K())] for v in roots]
seen={0};todo=[0]
while todo:
    for j in graph[todo.pop()]:
        if j not in seen:seen.add(j);todo.append(j)
# A common invariant subspace and its orthogonal complement must partition the
# reflection root lines. Connected nonorthogonality and spanning rule this out.
irreducible=len(seen)==len(roots) and rank(roots)==6
units=[K(1),K(-1),w,-w,w*w,-w*w]
scalar_members=[]
for z in units:
    p=Permutation([idx[tuple(z*a for a in x)] for x in orbit])
    scalar_members.append(bool(G.contains(p)))
# By Schur, central matrices are scalars; finite scalar groups in Q(sqrt(-3))
# are subgroups of mu_6. Thus the six memberships prove centre order exactly 6.
result={'root_nonorthogonality_graph_connected':len(seen)==len(roots),'irreducible_over_C':irreducible,'all_six_scalar_units_in_group':all(scalar_members),'centre_order':6 if irreducible and all(scalar_members) else None,'orbit_size':len(orbit),'orbit_span_K_dimension':spanrank,'faithful_action':spanrank==6,'permutation_group_order':order,'claimed_order':39191040,'matches_claimed_order':order==39191040}
Path(__file__).with_suffix('.json').write_text(json.dumps(result,indent=2)+'\n')
print(json.dumps(result,indent=2))
