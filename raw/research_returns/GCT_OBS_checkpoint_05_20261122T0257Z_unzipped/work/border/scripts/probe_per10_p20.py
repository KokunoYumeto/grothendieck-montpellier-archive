#!/usr/bin/env python3
"""A genuine-solvable-symmetry flag probe for the permanent P20 ten-plane.

Besides common changes of row leaves1,2 and column leaves2,3, the two-edge
row-star tensor has opposite translations on B and C: b_i -> b_i+s b_0,
c_i -> c_i-s c_0.  They preserve the row-star tensor exactly.  These give
two extra positive root operators on A tensor B, with trivial A action.
The four roots together form a connected solvable symmetry subgroup.
The inherited full determinant Borel is NOT asserted to preserve per.

This probes one permanent ten-plane only.  OPEN is not an upper bound.
"""
from collections import defaultdict
from pathlib import Path
import json
from br_linear import tensor, add, RECTS
from borel_quiver import module
import check_det10_gate as gate

S = [0, 1, 2, 3, 4, 6, 7, 8, 9, 10]


def per_p20_module(subset):
    assert list(subset) == S
    support, U, aw, bw, unused_blocks = tensor(S, 1)
    positions = {value: i for i, value in enumerate(support)}
    slice_positions = {value: i for i, value in enumerate(S)}
    rectangles = {value: i for i, value in enumerate(RECTS)}
    actions = []
    for leaf in (1, 2):
        def translation(coordinate, leaf=leaf):
            a, b = coordinate
            row, column = divmod(support[b], 4)
            return {(a, positions[column]): 1} if row == leaf else {}
        actions.append(translation)
    for axis, lower in ((0, 1), (1, 2)):
        dual = defaultdict(dict)
        for h, code in enumerate(S):
            pair = RECTS[code][axis]
            if lower + 1 not in pair:
                continue
            assert lower not in pair
            replacement = tuple(lower if value == lower + 1 else value for value in pair)
            rectangle = list(RECTS[code])
            rectangle[axis] = tuple(sorted(replacement))
            target = slice_positions[rectangles[tuple(rectangle)]]
            dual[target][h] = -1

        def common_root(coordinate, axis=axis, lower=lower, dual=dual):
            a, b = coordinate
            output = {(new_a, b): value for new_a, value in dual[a].items()}
            entry = list(divmod(support[b], 4))
            if entry[axis] == lower + 1:
                entry[axis] = lower
                new_b = positions[4 * entry[0] + entry[1]]
                output[a, new_b] = output.get((a, new_b), 0) + 1
            return {key: value for key, value in output.items() if value}
        actions.append(common_root)
    weight = lambda coordinate: add(aw[coordinate[0]], bw[coordinate[1]])
    ambient = [{(a, b): 1} for a in range(len(S)) for b in range(len(support))]
    result = module(U, ambient, weight, actions)
    result.update({'subset': S, 'support': support, 'aw': aw, 'bw': bw,
                   'actions': actions, 'kind': 'permanent'})
    return result


if __name__ == '__main__':
    gate.ab_module = per_p20_module
    result = gate.run(S, r=17)
    result['claim_scope'] = 'Only the permanent P20 coordinate ten-plane'
    result['solvable_root_count'] = 4
    destination = Path('certificates/per10_p20_gate.json')
    temporary = destination.with_suffix('.json.tmp')
    temporary.write_text(json.dumps(result, indent=2) + '\n')
    temporary.replace(destination)
