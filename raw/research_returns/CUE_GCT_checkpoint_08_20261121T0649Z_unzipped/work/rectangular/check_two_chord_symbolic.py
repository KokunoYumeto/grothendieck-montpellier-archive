"""Symbolic checks on the cofactor identity used in the all-n R-15 proof.

The general proof is algebraic in findings.tex; these finite checks guard
indices and the scalar/sign normalization, rather than proving all n.
"""
from itertools import permutations
from pathlib import Path
import json
import sympy as sp

x, y, z, w, epsilon = sp.symbols('x y z w epsilon')


def permanent(matrix):
    total = 0
    for sigma in permutations(range(len(matrix))):
        factors = [matrix[i][j] for i,j in enumerate(sigma)]
        if all(factor != 0 for factor in factors):
            total += sp.prod(factors)
    return sp.expand(total)


results = []
for n in range(4,8):
    ell = [x-(i+1)*y for i in range(n)]
    v = [z-(i+1)**2*w for i in range(n)]
    matrix = [[sp.S.Zero for _ in range(n)] for _ in range(n)]
    for i in range(n):
        matrix[i][i] = ell[i]
        matrix[i][(i+1)%n] = v[i]
    p = epsilon*ell[0]
    q = epsilon*v[2]
    matrix[0][2] = p
    matrix[1][0] = q
    cofactors = []
    for j in range(3):
        small = [[matrix[i][h] for h in range(n) if h != j]
                 for i in range(n) if i != 2]
        cofactors.append(permanent(small))
    rest = sp.prod(ell[3:])
    formulas = [(v[0]*v[1]+p*ell[1])*rest,
                (ell[0]*v[1]+p*q)*rest,
                (ell[0]*ell[1]+v[0]*q)*rest]
    assert all(sp.expand(actual-expected) == 0
               for actual, expected in zip(cofactors,formulas))
    T = ell[0]*v[0]*v[2]*rest
    identity = ell[0]*cofactors[0]-v[0]*cofactors[1]-p*cofactors[2]
    assert sp.expand(identity+2*epsilon**2*T) == 0
    assert sp.cancel(T/sp.prod(ell)-v[0]*v[2]/(ell[1]*ell[2])) == 0
    for alpha, _ in sp.Poly(T,x,y,z,w).terms():
        assert alpha[0]+alpha[1] == n-2
        assert alpha[2]+alpha[3] == 2
    results.append({'n': n, 'three_cofactor_formulas': True,
                    'negative_two_epsilon_squared_identity': True,
                    'rational_residue_support_two_and_three': True,
                    'bidegree_n_minus_two_two': True})
path = Path(__file__).with_name('two_chord_symbolic_results.json')
path.write_text(json.dumps(results,indent=2)+'\n')
print(json.dumps({'cases':len(results),'all_checks_passed':True,'output':str(path)}))
