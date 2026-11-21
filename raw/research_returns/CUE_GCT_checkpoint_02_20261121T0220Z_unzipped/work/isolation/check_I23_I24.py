"""Finite exact checks for I23 and the explicit recursive I24 witness.

These checks verify small instances and displayed identities; they are
not formal certificates of the general theorems.
"""
from itertools import combinations, product
from pathlib import Path
import json
import sympy as sp

records = {}
code_checks = []
for w, r in ((4, 2), (5, 2), (5, 3)):
    bases = tuple(combinations(range(w), r))
    position = {B: i for i, B in enumerate(bases)}
    constraints = []
    for K in combinations(range(w), r-2):
        outside = [i for i in range(w) if i not in K]
        for a,b,c,d in combinations(outside, 4):
            ix = lambda i,j: position[tuple(sorted(K+(i,j)))]
            constraints.append(((ix(a,b), ix(c,d)),
                                (ix(a,c), ix(b,d)),
                                (ix(a,d), ix(b,c))))
    found = set()
    for bits in product((0, 1), repeat=len(bases)):
        if all(bits[A]+bits[B] == bits[C]+bits[D] == bits[E]+bits[F]
               for ((A,B),(C,D),(E,F)) in constraints):
            found.add(bits)
    expected = {(0,)*len(bases), (1,)*len(bases)}
    for i in range(w):
        b = tuple(int(i in B) for B in bases)
        expected.add(b)
        expected.add(tuple(1-v for v in b))
    assert found == expected
    code_checks.append({'w':w,'r':r,'bases':len(bases),
                        'all_binary_maps_checked':2**len(bases),
                        'coherent_binary_maps':len(found),
                        'expected_constants_and_literals':2*w+2})
records['I23'] = code_checks

reset_checks = []
for w in range(3, 7):
    # A layer is (projection rank, directed variable edge source,target).
    def pair(r, a):
        return [(r, w-1, a-1), (r, a-1, w-1)]
    def H(k):
        return [] if k==w else H(k+1)+pair(k,k)+H(k+1)
    layers = H(3)+pair(2,1)+H(3)+pair(2,2)+H(3)
    h = 3*2**(w-2)-2
    assert len(layers) == h
    variables = sp.symbols('y1:'+str(h+1))
    row = sp.zeros(1,w); row[0,w-1]=1
    for y,(r,a,b) in zip(variables,layers):
        A=sp.diag(*([1]*r+[0]*(w-r)))
        A[a,b] += y
        assert A.rank() == r
        row = (row*A).applyfunc(sp.expand)
    expected=sp.prod(variables)
    assert sp.expand(row[0,w-1]-expected) == 0
    # All constant interval ranks equal the minimum local rank, and
    # factor rank provides the matching generic upper bound.
    interval_count=0
    for left in range(h):
        C=sp.eye(w); minimum=w
        for r,a,b in layers[left:]:
            C=C*sp.diag(*([1]*r+[0]*(w-r)))
            minimum=min(minimum,r)
            assert C == sp.diag(*([1]*minimum+[0]*(w-minimum)))
            assert minimum >= 2
            interval_count += 1
    reset_checks.append({'w':w,'positions':h,
                         'scalar_is_product_of_all_variables':True,
                         'local_generic_ranks_verified':True,
                         'constant_intervals_verified':interval_count,
                         'generic_interval_rank_follows_from_factor_bound':True})
records['I24'] = reset_checks
records['scope'] = 'Finite exact checks; the general proofs are in the corresponding TeX files.'
out=Path(__file__).with_name('I23_I24_computation_checks.json')
out.write_text(json.dumps(records,indent=2)+'\n')
print(json.dumps(records,indent=2))
