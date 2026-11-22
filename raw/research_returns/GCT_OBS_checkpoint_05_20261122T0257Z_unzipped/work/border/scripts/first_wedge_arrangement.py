"""Exact linear-arrangement cover for one torus-weight extension family.

Each new first-Koszul column has a distinct output weight.  Its rank
increment is therefore the number of nonzero quotient column maps.
Enumerating intersections of their kernels covers all possible zero
patterns over the infinite characteristic-zero field, in any dimension.
"""
from collections import defaultdict
from br_linear import Space, add, wedge, rowspace, nullspace
from borel_quiver import extension_vectors, linear_combination
from check_higher_prolongation import arrangements


def allowed_subspaces(M, F, block, K, target_rank=17):
    E0 = M['U'] + extension_vectors(M, F)
    X = [linear_combination(M['blocks'][block][1], vector) for vector in K]
    weights = [M['aw'], M['bw']]
    conditions, base_ranks = [], []
    for orientation, fw in zip(('A', 'B'), weights):
        assert len(set(fw)) == len(fw)
        spaces = defaultdict(Space)
        for vector in E0:
            a, b = next(iter(vector))
            w = add(M['aw'][a], M['bw'][b])
            assert all(add(M['aw'][i], M['bw'][j]) == w for i, j in vector)
            for index, weight in enumerate(fw):
                spaces[add(w, weight)].append(wedge(vector, orientation, index))
        base_ranks.append(sum(space.rank() for space in spaces.values()))
        for index, weight in enumerate(fw):
            rows = defaultdict(dict)
            space = spaces[add(M['blocks'][block][0], weight)]
            for column, vector in enumerate(X):
                for key, value in space.reduce(wedge(vector, orientation, index)).items():
                    rows[key][column] = value
            conditions.append(rowspace([tuple(row.items()) for row in rows.values()]))
    a, b = len(M['aw']), len(M['bw'])
    good = []
    all_states = arrangements(conditions, len(K), 0)
    for equations, zeros in all_states:
        if base_ranks[0] + a - len(zeros & set(range(a))) > target_rank * (a - 1):
            continue
        if base_ranks[1] + b - len(zeros & set(range(a, a+b))) > target_rank * (b - 1):
            continue
        good.append(equations)
    # Keep only maximal allowed parameter subspaces (minimal equation spaces).
    maximal = [equations for equations in good
               if not any(other != equations and rowspace(equations + other) == equations
                          for other in good)]
    result = []
    for equations in maximal:
        parameter_basis = nullspace(equations, len(K))
        basis = []
        for parameter in parameter_basis:
            vector = defaultdict(int)
            for i, value in parameter.items():
                for j, coefficient in K[i].items():
                    vector[j] += value * coefficient
            basis.append({j: value for j, value in vector.items() if value})
        result.append(basis)
    return result, {'arrangement_states': len(all_states),
                    'base_ranks': base_ranks,
                    'allowed_dimensions': [len(basis) for basis in result]}
