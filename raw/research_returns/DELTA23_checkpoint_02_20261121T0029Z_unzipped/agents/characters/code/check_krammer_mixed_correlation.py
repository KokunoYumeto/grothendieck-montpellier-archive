#!/usr/bin/env python3
"""Literal six-dimensional mixed-pair correlation and direct-sum certificate."""
import json
from pathlib import Path
import numpy as np
from sympy.combinatorics import PermutationGroup
import krammer_mixed_structure as k


def blockdiag(a,b):
    out=np.zeros((len(a)+len(b),len(a)+len(b)),dtype=np.int64)
    out[:len(a),:len(a)]=a;out[len(a):,len(a):]=b
    return out


def det3(a):
    result=0
    for i,j,l,s in [(0,1,2,1),(1,2,0,1),(2,0,1,1),(0,2,1,2),(2,1,0,2),(1,0,2,2)]:
        result=k.A[result,k.M[s,k.M[a[0,i],k.M[a[1,j],a[2,l]]]]]
    return int(result)


def comm(a,b):return k.mm(k.mm(k.mm(a,b),k.inverse(a)),k.inverse(b))


root=Path(__file__).resolve().parents[1]
data=json.loads((root/"records"/"krammer_mixed_structure.json").read_text())
raw=k.kp.matrices(4,3,6);a,b,c=raw
xs=[k.mp(a,2),k.mp(b,2),k.mp(c,2),k.mp(k.mm(k.mm(a,b),a),2),k.mp(k.mm(k.mm(c,b),c),2)]
splits=[];blocks=[];rows=[]
for row in data["pairs"]:
    bs=[np.array(row["proper_cyclic_submodules"][j]["basis"],dtype=np.int64) for j in [2,3]]
    full=np.concatenate(bs,axis=1);assert k.rank(full)==6
    ii=k.inverse(full);gens=[xs[j-1] for j in row["label"]]
    mats=[k.mm(k.mm(ii,g),full) for g in gens]
    assert all(np.count_nonzero(g[:3,3:])==np.count_nonzero(g[3:,:3])==0 for g in mats)
    hs=[g[:3,:3] for g in mats];us=[g[3:,3:] for g in mats]
    ps,degree=k.kp.orbit_perm(list(map(k.kp.to3,hs)),np.eye(6,dtype=np.int64),limit=1000)
    hg=PermutationGroup(ps);horders=[int(g.order()) for g in hg.derived_series()]
    assert horders==[108,27,3,1]
    assert all(g.order() in [1,3] for g in hg.derived_subgroup().generate_schreier_sims())
    dets=[[det3(h),det3(u)] for h,u in zip(hs,us)]
    dimage={(1,1)};pending=[(1,1)]
    while pending:
        v=pending.pop()
        for d in dets:
            w=(int(k.M[v[0],d[0]]),int(k.M[v[1],d[1]]))
            if w not in dimage:dimage.add(w);pending.append(w)
    expected=8 if row["label"]==[3,4] else 4
    assert len(dimage)==expected
    order=27*6048*len(dimage)
    rows.append({"pair":row["label"],"splitting_basis":full.tolist(),
                 "solvable_generators":[g.tolist() for g in hs],
                 "unitary_generators":[g.tolist() for g in us],
                 "solvable_derived_orders":horders,"solvable_derived_exponent":3,
                 "determinant_pairs":dets,"determinant_joint_image":[list(v) for v in sorted(dimage)],
                 "full_order_by_Goursat":order,
                 "full_derived_orders_by_Goursat":[order,27*6048,3*6048,6048]})
    splits.append(full);blocks.append((hs,us))

ch=np.array([[4,1,0],[3,0,0],[0,0,1]],dtype=np.int64)
cu=np.array([[1,3,2],[3,5,0],[0,1,0]],dtype=np.int64)
qh=np.array([[4,0,6],[2,1,0],[1,0,0]],dtype=np.int64)
qu=np.array([[2,0,2],[2,5,0],[6,2,1]],dtype=np.int64)
assert all(k.rank(p)==3 for p in [ch,cu,qh,qu])
xh,yh=blocks[0][0];xu,yu=blocks[0][1]
uh,vh=blocks[1][0];uu,vu=blocks[1][1]
zh=k.inverse(k.mm(uh,vh));zu=k.inverse(k.mm(uu,vu))
assert np.array_equal(k.mm(xh,ch),k.mm(ch,k.mp(zh,3)))
assert np.array_equal(k.mm(yh,ch),k.mm(ch,uh))
assert np.array_equal(k.mm(xu,cu),k.mm(cu,k.M[2,zu]))
assert np.array_equal(k.mm(yu,cu),k.mm(cu,uu))
assert all(np.array_equal(k.mm(k.mp(zh,2),g),k.mm(g,k.mp(zh,2))) for g in [uh,vh])
for z,u,v,q in [(zh,uh,vh,qh),(zu,uu,vu,qu)]:
    assert np.array_equal(k.mm(z,q),k.mm(q,z))
    assert np.array_equal(k.mm(u,q),k.mm(q,v))

cfull=k.mm(k.mm(splits[0],blockdiag(ch,cu)),k.inverse(splits[1]))
qfull=k.mm(k.mm(splits[1],blockdiag(qh,qu)),k.inverse(splits[1]))
dfull=k.mm(k.mm(splits[1],blockdiag(k.mp(zh,2),2*np.eye(3,dtype=np.int64))),k.inverse(splits[1]))
x,u,v=xs[2:];z=k.inverse(k.mm(u,v))
assert np.array_equal(k.mm(x,cfull),k.mm(cfull,k.mm(dfull,z)))
assert np.array_equal(k.mm(u,cfull),k.mm(cfull,u))
assert all(np.array_equal(k.mm(dfull,g),k.mm(g,dfull)) for g in [u,v])
assert np.array_equal(k.mm(z,qfull),k.mm(qfull,z))
assert np.array_equal(k.mm(u,qfull),k.mm(qfull,v))
# A word in F' ignores a central multiplier on either input.  Independently
# test representative commutators and their conjugates to audit direction.
for aa,bb in [(1,1),(2,1),(1,3)]:
    source=comm(k.mp(x,aa),k.mp(u,bb))
    target=comm(k.mp(z,aa),k.mp(u,bb))
    assert np.array_equal(k.mm(k.mm(k.inverse(cfull),source),cfull),target)

out={"statement":"D23.C9", "field":"F3[i], i²=-1; encoding a+3b",
     "X_matrices":[g.tolist() for g in xs],"pairs":rows,
     "C_solvable":ch.tolist(),"C_unitary":cu.tolist(),
     "Q_solvable":qh.tolist(),"Q_unitary":qu.tolist(),
     "C_full":cfull.tolist(),"Q_full":qfull.tolist(),"D_central_full":dfull.tolist(),
     "z_full":z.tolist(),
     "identities":["X3 C=C D z", "X4 C=C X4", "[D,X4]=[D,X5]=1", "z Q=Q z", "X4 Q=Q X5"],
     "gentle_correlation":"For R=f(X3,X4), r=C^{-1} R C: f(X4,X5)=Q^{-1} r Q r^{-1}",
     "result":"PASS"}
path=root/"records"/"krammer_mixed_correlation.json"
path.write_text(json.dumps(out,indent=2)+"\n")
print(json.dumps({"result":"PASS","full_pair_orders":[r["full_order_by_Goursat"] for r in rows],
                  "certificate":str(path)}))
