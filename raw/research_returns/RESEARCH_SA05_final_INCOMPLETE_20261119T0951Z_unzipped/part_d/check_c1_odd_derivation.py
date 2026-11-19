"""Exact 8-dimensional superalgebra certificate for C.1's parity gate.

We use H*(E x P1,Q) = exterior(x,y) tensor Q[z]/(z^2),
|x|=|y|=1, |z|=2, and the odd derivation D(x)=z,D(y)=D(z)=0.
This is a scope check, not a counterexample to a Chow assertion.
"""
from pathlib import Path
import json
from time import perf_counter

started = perf_counter()
basis = ['1', 'x', 'y', 'xy', 'z', 'xz', 'yz', 'xyz']
degrees = [((i & 1) != 0) + ((i & 2) != 0) + 2*((i & 4) != 0) for i in range(8)]

def unit(i):
    v = [0]*8
    v[i] = 1
    return v

def add(u, v):
    return [a+b for a,b in zip(u,v)]

def scale(a, v):
    return [a*b for b in v]

def multiply(u, v):
    w = [0]*8
    for i, a in enumerate(u):
        for j, b in enumerate(v):
            if i & j:
                continue
            # The only reordering of odd generators is y in u past x in v.
            sign = -1 if (i & 2 and j & 1) else 1
            w[i | j] += sign*a*b
    return w

def derive(u):
    w = [0]*8
    for i,a in enumerate(u):
        if i & 1 and not i & 4:
            w[(i ^ 1) | 4] += a
    return w

def trace(u):
    return u[7]

def parity(u):
    return [((-1)**degrees[i])*a for i,a in enumerate(u)]

zero = [0]*8
leibniz_failures = []
pairing_failures = []
associativity_failures = []
for i in range(8):
    a = unit(i)
    for j in range(8):
        b = unit(j)
        rhs = add(multiply(derive(a),b),scale((-1)**degrees[i],multiply(a,derive(b))))
        if derive(multiply(a,b)) != rhs:
            leibniz_failures.append([i,j])
        if trace(rhs) != 0:
            pairing_failures.append([i,j])
        for k in range(8):
            c = unit(k)
            if multiply(multiply(a,b),c) != multiply(a,multiply(b,c)):
                associativity_failures.append([i,j,k])

matrix = [[derive(unit(j))[i] for j in range(8)] for i in range(8)]
pairing = [[trace(multiply(unit(i),unit(j))) for j in range(8)] for i in range(8)]
checks = {
    'algebra_associativity_512_triples': not associativity_failures,
    'super_leibniz_64_pairs': not leibniz_failures,
    'infinitesimal_pairing_invariance_64_pairs': not pairing_failures,
    'annihilates_unit': derive(unit(0)) == zero,
    'annihilates_point_xyz': derive(unit(7)) == zero,
    'trace_composed_with_D_zero': all(trace(derive(unit(i))) == 0 for i in range(8)),
    'D_squared_zero': all(derive(derive(unit(i))) == zero for i in range(8)),
    'D_nonzero': derive(unit(1)) == unit(4),
    'D_odd': all((degrees[i]-degrees[j]) % 2 == 1 for i in range(8) for j in range(8) if matrix[i][j]),
    'D_degree_plus_one': all(degrees[i]-degrees[j] == 1 for i in range(8) for j in range(8) if matrix[i][j]),
    'pairing_nondegenerate_signed_permutation': all(sum(abs(a) for a in row)==1 for row in pairing) and all(sum(abs(pairing[i][j]) for i in range(8))==1 for j in range(8)),
    'parity_anticommutes_with_D': all(parity(derive(unit(i))) == scale(-1,derive(parity(unit(i)))) for i in range(8)),
    'parity_not_in_ordinary_commutant_of_D': derive(parity(unit(1))) != parity(derive(unit(1))),
}
assert all(checks.values()), checks
output = {
    'scope': 'Odd infinitesimal symmetry of the ungraded marked Frobenius superalgebra; no claim that a finite Chow criterion is false.',
    'basis': basis,
    'cohomological_degrees': degrees,
    'D_matrix_columns_are_images': matrix,
    'pairing_matrix_trace_ab': pairing,
    'parity_obstruction_on_x': {'D_after_parity': derive(parity(unit(1))), 'parity_after_D': parity(derive(unit(1)))},
    'checks': checks,
    'elapsed_seconds': perf_counter()-started,
}
path = Path(__file__).with_name('check_c1_odd_derivation_output.json')
path.write_text(json.dumps(output,indent=2)+'\n')
print(json.dumps(output,indent=2))
