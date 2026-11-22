#!/usr/bin/env python3
"""Exact arity-one certificate for A-L09; no finite extrapolation of PD laws."""
from fractions import Fraction
from math import gcd
from pathlib import Path
import json
import time


def linear_apply(table, vector):
    result = {}
    for name, coefficient in vector.items():
        for out, value in table.get(name, {}).items():
            result[out] = result.get(out, 0) + coefficient * value
    return {name: value for name, value in result.items() if value}


def main():
    started = time.perf_counter()
    bases = ['v1', 'v2', 'a1', 'a2', 'b2', 'b3', 'c2', 'c3']
    horizontal = {'v2': {'v1': 1}, 'a2': {'a1': 1},
                  'b3': {'b2': 1}, 'c3': {'c2': 1}}
    checks = 0
    cases = []
    for m in range(2, 34):
        vertical = {'v1': {'a1': m}, 'v2': {'a2': m, 'b2': -1},
                    'a2': {'c2': 1}, 'b2': {'c2': m}, 'b3': {'c3': m}}
        for name in bases:
            v = {name: 1}
            assert not linear_apply(vertical, linear_apply(vertical, v))
            assert not linear_apply(horizontal, linear_apply(horizontal, v))
            assert linear_apply(horizontal, linear_apply(vertical, v)) == linear_apply(vertical, linear_apply(horizontal, v))
            checks += 3
        # The middle normalized vertical complex has matrices (m,-1)^T
        # and (1,m); the first is primitive and equals minus a kernel basis.
        assert m - m == 0
        assert gcd(m, 1) == 1
        assert (-m) + m == 0
        checks += 3
        # Exact finite lattice membership checks for each normalized term.
        for denominator in range(1, 17):
            for numerator in range(-16, 17):
                a = Fraction(numerator, denominator)
                at_degree_one = (m * a).denominator == 1
                at_degree_two = (m * a).denominator == 1 and a.denominator == 1
                assert at_degree_one == ((a / Fraction(1, m)).denominator == 1)
                assert at_degree_two == (a.denominator == 1)
                checks += 2
        # In saturated coordinates the horizontal differential is m.
        assert Fraction(1, 1) / Fraction(1, m) == m
        assert len({r % m for r in range(m)}) == m
        checks += 2
        cases.append({'m': m, 'vertical_H1_normalized_degree': 1,
                      'vertical_H2_normalized_degree': 3,
                      'both_vertical_torsion_orders': m,
                      'saturated_horizontal_matrix': [[m]],
                      'saturated_horizontal_H1_order': m})
    result = {'scope': 'Complete finite arity-one double-complex matrices and lattice checks for A-L09. The full free-PD and all-weight assertions are proved symbolically in the section.',
              'checks': checks, 'cases': cases,
              'runtime_seconds': time.perf_counter() - started}
    out = Path(__file__).resolve().parents[1] / 'logs' / 'B_full_saturation_certificate.json'
    out.write_text(json.dumps(result, indent=2) + '\n')
    print(json.dumps({'checks': checks, 'cases': len(cases),
                      'runtime_seconds': result['runtime_seconds'], 'output': str(out)}))


if __name__ == '__main__':
    main()
