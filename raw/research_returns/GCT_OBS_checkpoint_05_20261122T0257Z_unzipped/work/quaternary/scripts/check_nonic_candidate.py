#!/usr/bin/env python3
"""QC-005: explicit degree-6 HW polynomial nonzero on x0 times an octic.

Only the padded-side evaluation is certified. This program makes NO claim
that the polynomial vanishes on determinant pencils.
Python standard library only; no original-run checker or matrix is read.
"""
from itertools import combinations, permutations
from math import factorial
import json

PRIME = 101
# A tuple lists the four symbolic copies on which a determinant acts.
BRACKETS = [((0,1,3,5),4), ((1,2,3,5),1), ((2,3,4,5),3),
            ((0,2,3,4),1), ((0,1,2,4),4)]
DATA = [(90,69,89,83,81), (98,94,54,38,33),
        (95,46,16,17,77), (24,52,62,65,44)]


def parity(a):
    return (-1)**sum(a[i]>a[j] for i in range(len(a)) for j in range(i+1,len(a)))


def determinant(columns):
    # Direct Leibniz formula, independent of the modular eliminators.
    return sum(parity(pi)*columns[0][pi[0]]*columns[1][pi[1]]
               *columns[2][pi[2]]*columns[3][pi[3]]
               for pi in permutations(range(4))) % PRIME


def check():
    vectors, weights = [], []
    for b,a1,a2,a3,w in DATA:
        vectors.extend([(b,a1,a2,a3),(0,a1,a2,a3)])
        weights.extend([w,-w])
    # The first of each pair minus the second has a factor x0 over Z.
    assert all(vectors[2*i][1:]==vectors[2*i+1][1:] for i in range(4))
    # Every repeated pair of assigned letters forces a determinant to zero.
    assert all(any(a in inds and b in inds for inds,power in BRACKETS)
               for a,b in combinations(range(6),2))
    degrees = [sum(power for inds,power in BRACKETS if i in inds) for i in range(6)]
    assert degrees == [9,9,9,9,8,8]
    determinants = {indices:determinant([vectors[i] for i in indices])
                    for indices in combinations(range(8),4)}
    total = 0
    nonzero = 0
    for assignment in permutations(range(8),6):
        term = 1
        for inds,power in BRACKETS:
            selected = tuple(assignment[i] for i in inds)
            bracket = parity(selected)*determinants[tuple(sorted(selected))] % PRIME
            term = term*pow(bracket,power,PRIME) % PRIME
        for i in assignment:
            term = term*weights[i] % PRIME
        term = term*vectors[assignment[4]][0]*vectors[assignment[5]][0] % PRIME
        total = (total+term) % PRIME
        nonzero += bool(term)
    differential = total*pow(factorial(9),6,PRIME) % PRIME
    assert (total,differential)==(39,34),(total,differential)
    return dict(prime=PRIME,degree=6,weight=[15,13,13,13],
                normalized_value=total,integer_differential_value=differential,
                injective_assignments=20160,nonzero_terms=nonzero,
                lies_in_linear_factor_variety=True,
                determinant_vanishing='not established by this checker')


if __name__=='__main__':
    print(json.dumps(check(),indent=2))
