"""Exact connected solvable stabilizer for a permanent coordinate subspace.

For every positive row/column elementary operation, try its common and
opposite actions on B,C.  Keep it only if its infinitesimal action sends
the literal slice span to itself, and use the negative dual action on A.
All B,C matrices are upper triangular.  The faithful action on the
concise slice span makes their lift a connected solvable group.  The
complete row/column torus normalizes every retained root subgroup.
"""
from collections import defaultdict
from br_linear import add, tensor
from borel_quiver import module


def per_module(S):
    S = list(S)
    support, U, aw, bw, _ = tensor(S, 1)
    positions = {v: i for i, v in enumerate(support)}
    slices = [dict() for _ in S]
    for c, vector in enumerate(U):
        for (a, b), value in vector.items():
            slices[a][b, c] = value
    owners = {coordinate: a for a, Q in enumerate(slices) for coordinate in Q}
    assert len(owners) == 4 * len(S)
    actions, roots = [], []
    for axis in (0, 1):
        for lower in range(4):
            for upper in range(lower + 1, 4):
                variable = {}
                valid = True
                for b, value in enumerate(support):
                    rc = list(divmod(value, 4))
                    if rc[axis] != upper:
                        continue
                    rc[axis] = lower
                    target = 4 * rc[0] + rc[1]
                    if target not in positions:
                        valid = False
                        break
                    variable[b] = positions[target]
                if not valid or not variable:
                    continue
                for sign in (1, -1):
                    dual = defaultdict(dict)
                    valid = True
                    for a, Q in enumerate(slices):
                        image = defaultdict(int)
                        for (b, c), value in Q.items():
                            if b in variable:
                                image[variable[b], c] += value
                            if c in variable:
                                image[b, variable[c]] += sign * value
                        image = {key: value for key, value in image.items() if value}
                        if any(key not in owners for key in image):
                            valid = False
                            break
                        for target in {owners[key] for key in image}:
                            values = {image.get(key, 0) for key in slices[target]}
                            if len(values) != 1:
                                valid = False
                                break
                            coefficient = values.pop()
                            if coefficient:
                                dual[target][a] = -coefficient
                        if not valid:
                            break
                    if not valid:
                        continue
                    def action(coordinate, dual=dual, variable=variable):
                        a, b = coordinate
                        result = {(new_a, b): value for new_a, value in dual[a].items()}
                        if b in variable:
                            key = (a, variable[b])
                            result[key] = result.get(key, 0) + 1
                        return {key: value for key, value in result.items() if value}
                    # Check the full tensor action, not only AB invariance.
                    derivative = defaultdict(int)
                    for c, column in enumerate(U):
                        for (a, b), value in column.items():
                            for (new_a, new_b), coefficient in action((a, b)).items():
                                derivative[new_a, new_b, c] += coefficient * value
                            if c in variable:
                                derivative[a, b, variable[c]] += sign * value
                    assert not any(derivative.values())
                    actions.append(action)
                    roots.append({'axis': axis, 'lower': lower, 'upper': upper, 'C_sign': sign})
    weight = lambda coordinate: add(aw[coordinate[0]], bw[coordinate[1]])
    ambient = [{(a, b): 1} for a in range(len(S)) for b in range(len(support))]
    result = module(U, ambient, weight, actions)
    result.update({'subset': S, 'support': support, 'aw': aw, 'bw': bw,
                   'actions': actions, 'roots': roots, 'kind': 'permanent'})
    return result
