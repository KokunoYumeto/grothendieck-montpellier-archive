"""Independent exact source verifier for the reduced-associator parity space.

No search program, numerical optimizer or exploratory certificate is imported.
The parity implication is proved in g037_hasse_parity_draft.tex. This file
checks its complete finite source interface and integer row-reduction claims.
"""
from pathlib import Path
from itertools import product
from collections import defaultdict,Counter
import json
import sympy as sp

NAMES=['mu','Sigma']+[f'g{i}_{w}' for i in (1,2) for w in ('1','12','2','21')]
FREE=list(product(range(1,10),range(1,10),range(10)))
POSITION={p:i for i,p in enumerate(FREE)}

def reconstruct():
    v=sp.Symbol('v'); ni={name:i for i,name in enumerate(NAMES)}; trace={}
    for row in json.loads(Path('sources/OURS_E4_scripts/e3_constants.json').read_text()):
        key=tuple(ni[row[s]] for s in ('b','bp','bpp'))
        assert key not in trace
        polynomial=sp.Poly(sp.expand(sp.sympify(row['c'],locals={'v':v})*v**64),v)
        coefficients={}
        for (degree,),coefficient in polynomial.terms():
            assert coefficient.is_Integer and (degree-64)%2==0
            coefficients[(degree-64)//2]=int(coefficient)
        assert coefficients and all(coefficients.values())
        trace[key]=coefficients
    assert len(trace)==132
    assert sum(abs(c) for p in trace.values() for c in p.values())==4443
    for a,z in product(range(10),repeat=2):
        wanted={0:1} if a==z else {}
        assert trace.get((0,a,z),{})==trace.get((a,0,z),{})==wanted
    # Independent exact Laurent verification of the trace algebra itself.
    for a,b,c in product(range(10),repeat=3):
        difference=defaultdict(int)
        for middle,z in product(range(10),repeat=2):
            for sign,left,right in [(1,(a,b,middle),(middle,c,z)),
                                    (-1,(b,c,middle),(a,middle,z))]:
                for u,cu in trace.get(left,{}).items():
                    for w,cw in trace.get(right,{}).items():
                        difference[z,u+w]+=sign*cu*cw
        assert all(value==0 for value in difference.values()),(a,b,c)
    quotient={}; negative={}
    for position in FREE:
        coefficients=trace.get(position,{})
        # Both grading residues are zero mod2: tbar is divisible by(q+1)^2.
        assert all(sum(c for e,c in coefficients.items() if e%2==j)%2==0
                   for j in (0,1))
        if position[2]==0:assert not coefficients
        quotient[position]=sum((e*(e-1)//2)*c for e,c in coefficients.items())%2
        negative[position]=sum(-c for c in coefficients.values() if c<0)%2
    assert all(value==0 for value in negative.values())
    assert sum(quotient.values())==28
    expected={(a,b,1) for a,b in product((2,4,6,8),repeat=2)}
    expected.update((a,b,1) for a,b in [(2,5),(3,2),(4,3),(5,4),(6,9),(7,6),(8,7),(9,8)])
    expected.update([(2,4,3),(4,2,5),(6,8,7),(8,6,9)])
    assert {key for key,value in quotient.items() if value}==expected
    return trace,quotient,negative

def parity_space():
    trace,quotient,negative=reconstruct(); rows=[]
    for a,b,c,z in product(range(1,10),range(1,10),range(1,10),range(10)):
        if z==a or z==c:continue
        indices=set()
        for middle in range(1,10):
            summands=[(quotient[a,b,middle],(middle,c,z)),
                      (quotient[middle,c,z],(a,b,middle)),
                      (quotient[b,c,middle],(a,middle,z)),
                      (quotient[a,middle,z],(b,c,middle))]
            for coefficient,position in summands:
                if coefficient:
                    index=POSITION[position]
                    if index in indices:indices.remove(index)
                    else:indices.add(index)
        if indices:
            assert sum(negative[FREE[i]] for i in indices)%2==0
            rows.append({'locator':[a,b,c,z],'indices':sorted(indices)})
    for index,position in enumerate(FREE):
        if position[2]==0:rows.append({'locator':['unit',index],'indices':[index]})
    assert len(rows)==3249
    masks=[sum(1<<i for i in row['indices']) for row in rows]
    pivots={}; witnesses={}
    for row_index,mask in enumerate(masks):
        combination=1<<row_index
        while mask:
            pivot=(mask&-mask).bit_length()-1
            if pivot not in pivots:
                pivots[pivot]=mask;witnesses[pivot]=combination;break
            mask^=pivots[pivot];combination^=witnesses[pivot]
    for pivot in sorted(pivots,reverse=True):
        for earlier in sorted(pivots):
            if earlier<pivot and (pivots[earlier]>>pivot)&1:
                pivots[earlier]^=pivots[pivot];witnesses[earlier]^=witnesses[pivot]
    reduced=[]; singles=[]
    for pivot,mask in sorted(pivots.items()):
        assert (mask&-mask).bit_length()-1==pivot
        assert all(not (mask>>other)&1 for other in pivots if other!=pivot)
        sources=[i for i in range(len(rows)) if (witnesses[pivot]>>i)&1]
        replay=0
        for i in sources:replay^=masks[i]
        assert replay==mask
        indices=[i for i in range(810) if (mask>>i)&1]
        reduced.append({'pivot':pivot,'indices':indices,'source_rows':sources})
        if len(indices)==1:singles.append(pivot)
    assert len(pivots)==718 and len(singles)==421
    assert sum(FREE[i][2]==0 for i in singles)==81
    assert sum(FREE[i][2]!=0 for i in singles)==340
    # Every original row reduces to zero, establishing the full row-space rank.
    for original in masks:
        mask=original
        for pivot in sorted(pivots):
            if (mask>>pivot)&1:mask^=pivots[pivot]
        assert mask==0
    result={'source_positions':132,'trace_associativity_triples':1000,
            'free_positions':810,'common_factor':'(q+1)^2 in F2[q,q^-1]',
            'negative_part_mass_parities_all_zero':True,
            'quotient_nonzero_positions':[list(p) for p in sorted(quotient) if quotient[p]],
            'source_rows':rows,'row_count':len(rows),'rank':len(pivots),
            'kernel_dimension':810-len(pivots),
            'reduced_row_lengths':dict(sorted(Counter(len(r['indices']) for r in reduced).items())),
            'reduced_rows':reduced,'forced_even_pair_mass_indices':singles,
            'forced_even_pair_mass_count':len(singles),
            'new_nonunit_output_even_pair_mass_count':340}
    return result,set(singles)

if __name__=='__main__':
    result,_=parity_space()
    destination=Path('work/gct/unrestricted_hasse_parity_certificate.json')
    destination.write_text(json.dumps(result,indent=2)+'\n')
    print(json.dumps({key:result[key] for key in ['source_positions','trace_associativity_triples',
          'free_positions','row_count','rank','kernel_dimension','forced_even_pair_mass_count',
          'new_nonunit_output_even_pair_mass_count','reduced_row_lengths']},indent=2))
