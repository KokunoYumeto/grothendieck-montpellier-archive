#!/usr/bin/env python3
"""Exact distance layers and moment bounds for Harper's initial segments.

This computes only the finite arithmetic in the cited isoperimetric theorem;
it is not a proof of Harper's theorem.  No numerical optimizer is used.
"""
import json
import sys
from collections import Counter, deque
from fractions import Fraction
from pathlib import Path


def pair(value):
    return [value.numerator, value.denominator]


def calculate(D, width, terms):
    d = D-1
    size = 1 << d
    count = (size+terms-1)//terms
    # On a fixed weight level, tuple order is precisely
    # A < B iff min(A symmetric_difference B) belongs to A.
    ordered = sorted(range(size), key=lambda s: (
        s.bit_count(), tuple(i for i in range(d) if (s >> i) & 1)))
    initial = ordered[:count]
    distance = [d+1]*size
    queue = deque(initial)
    for vertex in initial:
        distance[vertex] = 0
    while queue:
        vertex = queue.popleft()
        for coordinate in range(d):
            neighbour = vertex ^ (1 << coordinate)
            if distance[neighbour] > distance[vertex]+1:
                distance[neighbour] = distance[vertex]+1
                queue.append(neighbour)
    histogram = Counter(distance)
    layers = [histogram[i] for i in range(max(distance)+1)]
    assert sum(layers) == size and layers[0] == count
    threshold = width*D-1
    integer_lower = sum(number*max(0, threshold-2*width*radius)**2
                        for radius, number in enumerate(layers))
    lower = Fraction(integer_lower, size)
    # Width six and three summands: log_2(3)>19/12.
    assert width == 6 and terms == 3
    upper = Fraction(2809*D*D, 144)
    return dict(dimension=D, cube_dimension=d, cube_size=size,
                high_set_size=count, initial_segment=initial,
                distance_layers=layers,
                cumulative_neighbourhoods=[sum(layers[:i+1])
                                           for i in range(len(layers))],
                rank_threshold=threshold, integer_second_moment=integer_lower,
                lower_second_moment=pair(lower), strict_upper_moment=pair(upper),
                exact_margin=pair(lower-upper), excludes=lower >= upper)


def main():
    config = json.loads(Path(sys.argv[1]).read_text())
    result = dict(config=config,
                  theorem='Harper initial simplicial segment, closed r-neighbourhood',
                  rows=[calculate(D, config['width'], config['terms'])
                        for D in config['dimensions']])
    path = Path(sys.argv[2])
    temp = path.with_suffix('.json.tmp')
    temp.write_text(json.dumps(result, separators=(',', ':')))
    temp.replace(path)
    for row in result['rows']:
        print(json.dumps({key:row[key] for key in (
            'dimension','high_set_size','distance_layers',
            'lower_second_moment','exact_margin','excludes')}))


if __name__ == '__main__':
    main()
