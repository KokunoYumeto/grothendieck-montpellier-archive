"""Literal coupled BC module for an already unique invariant AB extension.

This module alone makes no exclusion.  The intersection G=E_BC intersect R
must be permitted to have every dimension from dim T(A*) through17.
"""
from collections import defaultdict
from fractions import Fraction

from br_linear import Space, add, rank
from borel_quiver import module, extension_vectors, linear_apply
from permanent_solvable import per_module
from probe_coupled_borel import intersection, bc_support


def decode_flag(data, M):
    F = [() for _ in M['blocks']]
    for row in data:
        F[row['weight_block']] = tuple(tuple((i, Fraction(x)) for i, x in v)
                                      for v in row['rows'])
    return tuple(F)


def unique_module(record):
    assert record['search_complete'] and not record['open_families']
    assert not record.get('unhandled_error')
    assert len(record['surviving_flags']) == 1
    M = per_module(record['subset'])
    a, b = len(M['subset']), len(M['support'])
    E = M['U']+extension_vectors(M, decode_flag(record['surviving_flags'][0], M))
    assert rank(E) == 17
    invariant = Space()
    for vector in E:
        invariant.append(vector)
    for vector in E:
        for action in M['actions']:
            assert not invariant.reduce(linear_apply(vector, action))
    positions = {v: i for i, v in enumerate(M['support'])}
    actions = []
    for number, root in enumerate(M['roots']):
        variable = {}
        for i, v in enumerate(M['support']):
            rc = list(divmod(v, 4))
            if rc[root['axis']] != root['upper']:
                continue
            rc[root['axis']] = root['lower']
            variable[i] = positions[4*rc[0]+rc[1]]
        if root['C_sign'] == -1:
            # Every slice is symmetric, so an opposite BC action that
            # preserves their symmetric span must vanish on that span.
            # Verify explicitly that its induced A action is zero.
            for h in range(a):
                for i in range(b):
                    expected = {(h, variable[i]): 1} if i in variable else {}
                    assert M['actions'][number]((h, i)) == expected
        # Common roots act identically in AB and AC.  An opposite root
        # has zero A action and acts with opposite scalar in AC; hence
        # both quotient modules have exactly the same invariant spaces.
        def action(coordinate, variable=variable, sign=root['C_sign']):
            i, j = coordinate
            result = {}
            if i in variable:
                result[variable[i], j] = 1
            if j in variable:
                key = (i, variable[j])
                result[key] = result.get(key, 0)+sign
            return {key: value for key, value in result.items() if value}
        actions.append(action)
    V = intersection(E, E, a, b)
    R = bc_support(V, a)
    U = [dict() for _ in range(a)]
    for c, vector in enumerate(M['U']):
        for (h, z), value in vector.items():
            U[h][z, c] = value
    weight = lambda bc: add(M['bw'][bc[0]], M['bw'][bc[1]])
    B = module(U, R, weight, actions)
    B.update({'subset': list(range(b)), 'support': list(range(b)),
              'aw': M['bw'], 'bw': M['bw'], 'actions': actions,
              'roots': M['roots'], 'V': V, 'original': M,
              'original_subset': record['subset'], 'AB_extension': E})
    assert rank(U) == a
    assert rank(R) == a+sum(len(basis) for w, basis in B['blocks'])
    return B


def weight_dimension_constraints(B):
    """Upper bounds on the coupled kernel for any torus-fixed G.

    For each triple weight, projection to one BC quotient weight involves
    a unique A coordinate because the original A weights are distinct.
    Its allowed preimage has dimension at most dim(V_w)-rank+d_j.
    Taking the minimum of these upper bounds is conservative.
    """
    M = B['original']
    uspaces = defaultdict(Space)
    for vector in B['U']:
        i, j = next(iter(vector))
        uspaces[add(M['bw'][i], M['bw'][j])].append(vector)
    block_index = {w: i for i, (w, basis) in enumerate(B['blocks'])}
    groups = defaultdict(list)
    for vector in B['V']:
        h, i, j = next(iter(vector))
        w = add(add(M['aw'][h], M['bw'][i]), M['bw'][j])
        assert all(add(add(M['aw'][a], M['bw'][b]), M['bw'][c]) == w
                   for a, b, c in vector)
        groups[w].append(vector)
    assert len(set(M['aw'])) == len(M['aw'])
    constraints = []
    for weight, vectors in sorted(groups.items()):
        maps = {}
        for h, aw in enumerate(M['aw']):
            bc_weight = tuple(x-y for x, y in zip(weight, aw))
            if bc_weight not in block_index:
                continue
            index = block_index[bc_weight]
            columns = []
            for vector in vectors:
                contraction = {(i, j): value for (a, i, j), value in vector.items() if a == h}
                columns.append(uspaces[bc_weight].reduce(contraction))
            r = rank(columns)
            if r:
                assert index not in maps
                maps[index] = r
        constraints.append({'weight': weight, 'dimension': len(vectors),
                            'projection_ranks': maps})
    return constraints
