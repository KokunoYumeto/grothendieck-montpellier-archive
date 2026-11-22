"""Finite combinatorial certificate for the Pries--Ulmer height-six input.

This does not construct abelian-variety homomorphisms or verify descent.
All arithmetic is integral. The bound is six letters and p in {2,3}.
"""
from pathlib import Path
from datetime import datetime, timezone
from collections import Counter
from itertools import product
import json, time

root = Path(__file__).resolve().parents[3]
started = datetime.now(timezone.utc).isoformat()
tick = time.perf_counter()

def rotations(w):
    return [w[j:]+w[:j] for j in range(len(w))]

def primitive(w):
    return len(set(rotations(w))) == len(w)

words = [w for length in range(2,7)
         for letters in product('fv', repeat=length)
         for w in [''.join(letters)]
         if primitive(w) and w == min(rotations(w))]
counts = Counter(map(len, words))
assert dict(counts) == {2:1, 3:2, 4:3, 5:6, 6:9}

cases = []
def multisets(start, chosen, remaining):
    if remaining == 0:
        cases.append(chosen)
        return
    for index in range(start, len(words)):
        w = words[index]
        if len(w) <= remaining:
            multisets(index, chosen+[w], remaining-len(w))
multisets(0, [], 6)
balanced = [case for case in cases if sum(w.count('f') for w in case)==3]

prime_results=[]
for p in (2,3):
    realizations=[]
    capacities={}
    genus_total=0
    for length in range(2,7):
        d=p**length-1
        genus=(d-1)//2
        copies=6//length
        genus_total+=copies*genus
        capacities[length]={'d':d,'copies':copies,'genus_per_curve':genus}
    for w in words:
        length=len(w)
        d=p**length-1
        # Left-to-right w gives the high-to-low base-p digits.
        a=sum((p-1 if letter=='f' else 0)*p**(length-1-j)
              for j,letter in enumerate(w))
        orbit=[]
        current=a
        while current not in orbit:
            orbit.append(current)
            current=p*current%d
        actual=''.join('f' if 2*x>d else 'v' for x in orbit)
        assert 0<a<d and 2*a!=d
        assert current==a and len(orbit)==length
        assert actual==w
        assert all(2*x!=d and x!=0 for x in orbit)
        realizations.append({'word':w,'d':d,'a':a,'orbit':orbit,'actual_word':actual})
    for case in cases:
        for w, multiplicity in Counter(case).items():
            assert multiplicity <= capacities[len(w)]['copies']
    assert genus_total == {2:62,3:555}[p]
    prime_results.append({'p':p,'product_factors':capacities,
                          'product_dimension':genus_total,
                          'realizations':realizations})

result=dict(started_utc=started, finished_utc=datetime.now(timezone.utc).isoformat(),
            runtime_seconds=time.perf_counter()-tick,
            status='PASS', word_length_bound=6,
            primitive_cyclic_words_by_length=dict(counts),
            all_local_local_height6_multisets=cases,
            balanced_dimension3_multisets=balanced,
            all_multiset_count=len(cases), balanced_multiset_count=len(balanced),
            prime_results=prime_results,
            scope='Combinatorial finite-word input only; no Hom lifting or geometry certified.')
(root/'agents/real_weil/output/bt1_height6_fermat.json').write_text(json.dumps(result,indent=2)+'\n')
summary={key:result[key] for key in ['started_utc','finished_utc','runtime_seconds','status',
            'primitive_cyclic_words_by_length','all_multiset_count','balanced_multiset_count']}
summary['product_dimensions']={entry['p']:entry['product_dimension'] for entry in prime_results}
summary['scope']=result['scope']
output=json.dumps(summary,indent=2)+'\n'
(root/'agents/real_weil/output/bt1_height6_fermat.out').write_text(output)
print(output,end='')
