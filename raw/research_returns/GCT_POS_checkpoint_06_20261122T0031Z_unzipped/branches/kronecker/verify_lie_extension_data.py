"""Finite bookkeeping certificates for the all-dimensional K-015 proof.

The induction itself is proved in LIE_EXTENSION.tex. This checks its base,
the canonical n=5 type, and the first three spectral-indexing cases.
"""
from itertools import product
from fractions import Fraction as F
from pathlib import Path
import json

root=Path(__file__).resolve().parent
support=[(0,0,0),(0,3,1),(1,1,3),(1,2,1),(2,0,3),(2,1,2),(2,3,0),(3,1,1),(3,2,3),(3,3,2)]
masses=list(map(F,['3/4','1/4','3/8','5/8','1/4','1/2','1/4','1/8','3/8','1/2']))
base_weights=[[-1,8,-7,-4],[-1,8,-4,5],[2,-4,-1,8]]
receipts=[]
for n in range(4,8):
    if n>=5:
        weights=[factor+[8*(-2)**(r-4) for r in range(5,n+1)] for factor in base_weights]
        modulus=2**(n-1)
        fixed=[e for e in product(range(n),repeat=3) if sum(weights[a][e[a]] for a in range(3))%modulus==0]
        assert set(fixed)==set(support)
        assert all(len(set(v%modulus for v in factor))==n for factor in weights)
        pairs=[]
        for factor in weights:
            pairs_here=[(i,j) for i in range(n) for j in range(i+1,n) if (factor[i]-factor[j])%modulus==modulus//2]
            assert len(pairs_here)==1;pairs.append(set(pairs_here[0]))
        one_pair_edges=[e for e in support if sum(e[a] in pairs[a] for a in range(3))==1]
        assert one_pair_edges
        for a in range(3):
            others=[b for b in range(3) if b!=a]
            for coordinate in range(n):
                assert any(e[a]==coordinate and all(e[b]!=n-1 for b in others) for e in support)
        assert all(sum(x for e,x in zip(support,masses) if e[a]==i)==1 for a in range(3) for i in range(n))
        receipt={'n':n,'M':modulus,'support_size':len(support),'paired_indices':[sorted(x) for x in pairs],'one_pair_edges':one_pair_edges,'pair_deletion_coverage':True}
        if n==5:
            inverse=pow(sum(map(sum,weights))%16,-1,16)
            normalized=[[v*inverse%16 for v in factor] for factor in weights]
            canonical=min(tuple(sorted(tuple(sorted((v-edge[a])%16 for v in factor)) for a,factor in enumerate(normalized))) for edge in product(*normalized) if sum(edge)%16==0)
            types=json.loads((root/'recursive_n5_m16_result.json').read_text())['feasible']
            assert tuple(map(tuple,types[62]['W']))==canonical
            receipt['canonical_type']=63
            receipt['canonical_spectra']=canonical
            # Independent integer row reduction over F_10007 for the actual
            # unpermuted coefficient-one seed, not a transported matrix.
            columns=[];support_set=set(support)
            matrix=[]
            for e in product(range(5),repeat=3):
                row=[]
                for a in range(3):
                    for i in range(5):
                        for j in range(5):
                            source=list(e);source[a]=j
                            row.append(int(e[a]==i and tuple(source) in support_set))
                matrix.append(row)
            prime=10007;rank=0;pivots=[];row_ids=list(range(125))
            for col in range(75):
                pivot=next((i for i in range(rank,125) if matrix[i][col]%prime),None)
                if pivot is None:continue
                matrix[rank],matrix[pivot]=matrix[pivot],matrix[rank]
                row_ids[rank],row_ids[pivot]=row_ids[pivot],row_ids[rank]
                pivots.append([row_ids[rank],col])
                scale=pow(matrix[rank][col]%prime,-1,prime)
                matrix[rank]=[(v*scale)%prime for v in matrix[rank]]
                for i in range(rank+1,125):
                    scale=matrix[i][col]%prime
                    if scale:matrix[i]=[(x-scale*y)%prime for x,y in zip(matrix[i],matrix[rank])]
                rank+=1
            assert rank==73
            receipt['seed_lie_rank_mod_10007']=rank
            receipt['rank_minor_pivots']=pivots
        receipts.append(receipt)
    if n==7:break
    selected=(1,1,3) if n==4 else (n-1,n-1,n-1)
    index=support.index(selected);mass=masses[index]
    support.pop(index);masses.pop(index)
    i,j,k=selected
    support.extend([(i,j,n),(i,n,k),(n,j,k),(n,n,n)])
    masses.extend([mass/2,mass/2,mass/2,1-mass/2])
(root/'lie_extension_checks.json').write_text(json.dumps(receipts,indent=2))
print('PASS K015: n5 seed rank73, type63, and exact n5/n6/n7 indexing and coverage')
