#!/usr/bin/env python3
"""Exact small solvable quotient of the new degree72 Hurwitz mixed pair."""
from pathlib import Path
import json,numpy as np
from sympy.combinatorics import Permutation,PermutationGroup
HERE=Path(__file__).resolve().parents[1];PENT=HERE.parent/'pentagon'
raw=np.load(PENT/'hurwitz_cubic216_four_13_pair34_component9.npz')['generators']
H=PermutationGroup([Permutation(g.tolist())for g in raw]);series=H.derived_series()
assert [int(g.order())for g in series]==[995328,82944,27648,1728,64,1]
blocks=H.minimal_blocks();block=next(v for v in blocks if len(set(v))==18)
labs=sorted(set(block));ix={v:i for i,v in enumerate(labs)};reps=[block.index(v)for v in labs]
gs=np.array([[ix[block[int(g[t])]]for t in reps]for g in raw])
G=PermutationGroup([Permutation(g.tolist())for g in gs]);Z=G.center();A=G.derived_subgroup()
assert [int(g.order())for g in G.derived_series()]==[144,12,4,1]
assert Z.order()==6 and Z.abelian_invariants()==[2,3]
comp=PermutationGroup(A.generators+[Permutation(gs[1].tolist())])
assert comp.order()==24
assert comp.subgroup_search(lambda q:Z.contains(q)).order()==1
# The four order-three subgroups of A4 give its faithful S4 conjugation action.
arrs=[tuple(g.array_form)for g in A.generate_schreier_sims()]
def mul(g,h):return tuple(g[h[i]]for i in range(len(g)))
def inv(g):return tuple(g.index(i)for i in range(len(g)))
def power(g,n):
    out=tuple(range(len(g)))
    for _ in range(n):out=mul(out,g)
    return out
subs=sorted({tuple(sorted((g,power(g,2))))for g in arrs
             if g!=tuple(range(18)) and power(g,3)==tuple(range(18))})
assert len(subs)==4
perm4=[]
for gg in gs:
    g=tuple(int(v)for v in gg);ig=inv(g)
    perm4.append(tuple(subs.index(tuple(sorted(mul(mul(g,h),ig)for h in sub)))for sub in subs))
# Mark the second S4 by p=(123), v=(14).  This is a (3,2,4) pair.
p=(1,2,0,3);v=(3,1,2,0);t=(1,2,3,0)
import itertools
mark=next(k for k in itertools.permutations(range(4))
          if mul(mul(k,perm4[0]),inv(k))==p and mul(mul(k,perm4[1]),inv(k))==v)
assert Permutation(p).order()==3 and Permutation(v).order()==2
assert Permutation(mul(p,v)).order()==4
joint=PermutationGroup([Permutation(g.tolist()+[18+j for j in h])for g,h in zip(gs,[p,t])])
assert joint.order()==576
assert [int(g.order())for g in joint.derived_series()]==[576,48,16,1]
twoS4=PermutationGroup([Permutation(list(g)+[4+j for j in h])for g,h in [(p,p),(t,v)]])
assert [int(g.order())for g in twoS4.derived_series()]==[96,48,16,1]
# The kernel is H''' by containment and the exact index.
fulljoin=PermutationGroup([Permutation(g.tolist()+[72+j for j in h])for g,h in zip(raw,[p,t])])
assert fulljoin.order()==H.order()
assert H.order()//joint.order()==series[3].order()
# Verify independence from the retained first degree36 pair.
d=np.load(PENT/'hurwitz_cubic216_four_13.npz');a,b=d['detector_generators'];first=[a[a],b[b]]
F=PermutationGroup([Permutation(g.tolist())for g in first])
J=PermutationGroup([Permutation(g.tolist()+[36+j for j in h])for g,h in zip(first,raw)])
assert F.order()==1944 and J.order()==F.order()*H.order()
# The small order24 pair45 pieces have the same exact marked kernel as q3(F).
U=np.array([[1,1],[0,1]],dtype=int);L=np.array([[1,0],[2,1]],dtype=int)
vectors=[(a,b)for a in range(3)for b in range(3)if a or b];vi={v:i for i,v in enumerate(vectors)}
def mp(M):return [vi[tuple(M@np.array(v)%3)]for v in vectors]
pure=[mp(U@U%3),mp(L@L%3)]
pieces=[]
for no in [9,11,13,15]:
    pair=np.load(PENT/f'hurwitz_cubic216_four_13_pair45_component{no}.npz')['generators']
    B=PermutationGroup([Permutation(g.tolist())for g in pair])
    BJ=PermutationGroup([Permutation(g.tolist()+[24+j for j in h])for g,h in zip(pair,pure)])
    assert B.order()==BJ.order()==24
    pieces.append({'component':no,'degree':24,'order':24,'same_marked_q3_kernel':True})
out={'statement':'D23.C21','mixed_degree':72,'mixed_derived_orders':[int(g.order())for g in series],
     'mixed_abelian_invariants':H.abelian_invariants(),'block_labels18':block,
     'block_generators18':gs.tolist(),'block_image_order':144,'block_center_order':6,
     'block_center_invariants':[2,3],'complement_order':24,'second_S4_raw_generators':perm4,
     'second_S4_conjugator':mark,'second_S4_marking':[p,v],
     'second_S4_peripheral_orders':[3,2,4],'harmonic_S4_marking':[p,t],
     'compact_joint_order':576,'compact_joint_derived_orders':[576,48,16,1],
     'two_S4_joint_derived_orders':[96,48,16,1],
     'compact_kernel_equals_mixed_third_derived':True,
     'first_pair_derived_orders':[int(g.order())for g in F.derived_series()],
     'first_mixed_joint_order':int(J.order()),'first_mixed_full_direct_product':True,
     'pair45_q3_pieces':pieces,'result':'PASS',
     'scope':'Exact group and marked-quotient facts. The second S4 phase is not identified with Psi3/2 or with an actual gentle lift.'}
(HERE/'records/hurwitz_mixed72_structure.json').write_text(json.dumps(out,indent=2)+'\n')
print(json.dumps({k:v for k,v in out.items()if k not in ['block_labels18','block_generators18']},indent=2))
