#!/usr/bin/env python3
"""Bounded D4 three-term exploration with the exact geometric moment row.

The old branch driver is reused without alteration.  Every propagation
operation below is an integer implication.  A partial tree, solver status,
or surviving box is not a mathematical exclusion.
"""
import importlib.util
import json
import math
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
spec = importlib.util.spec_from_file_location(
    'sh_old_three_term_tree', HERE / 'sh_three_term_dimension_four_tree.py')
old = importlib.util.module_from_spec(spec)
spec.loader.exec_module(old)


def propagate(lower, upper):
    trace = []

    def update(kind, a, s, value, reason):
        table = lower if kind == 'lower' else upper
        if (kind == 'lower' and value <= table[a][s]) or (
                kind == 'upper' and value >= table[a][s]):
            return False
        table[a][s] = value
        trace.append([kind, a, s, value] + reason)
        if lower[a][s] > upper[a][s]:
            raise old.Contradiction(['bounds', a, s])
        return True

    try:
        for a in range(3):
            for s in range(8):
                if lower[a][s] > upper[a][s]:
                    raise old.Contradiction(['bounds', a, s])
        while True:
            changed = False
            for a in range(3):
                total = sum(lower[a])
                square = sum(x*x for x in lower[a])
                if total > 141:
                    raise old.Contradiction(['budget', a])
                if square > 2496:
                    raise old.Contradiction(['quadratic_budget', a])
                for s in range(8):
                    changed |= update('upper', a, s,
                                      141-total+lower[a][s], ['budget'])
                    changed |= update('upper', a, s,
                                      math.isqrt(2496-square+lower[a][s]**2),
                                      ['quadratic_budget'])
                for s in range(8):
                    for u in range(8):
                        raw = (s ^ u).bit_count()
                        h = min(raw, 4-raw)
                        if h:
                            changed |= update('lower', a, s,
                                              lower[a][u]-12*h,
                                              ['lipschitz', u, h])
                            changed |= update('upper', a, s,
                                              upper[a][u]+12*h,
                                              ['lipschitz', u, h])
            for s in range(8):
                caps = [2**upper[a][s] for a in range(3)]
                if sum(caps) < 2**24:
                    raise old.Contradiction(['single_cut', s])
                for a in range(3):
                    residual = 2**24-sum(caps[b] for b in range(3) if b != a)
                    changed |= update('lower', a, s, old.clog(residual),
                                      ['single_cut'])
            for s in range(8):
                for u in range(8):
                    raw = (s ^ u).bit_count()
                    h = min(raw, 4-raw)
                    if not h:
                        continue
                    p = 2**(6*(4-h))
                    specs = [(1, (67*p+48)//49), (3, 2*p)]
                    specs += [(z*z, z*p) for z in
                              (2**e for e in range(1, 6*h+1))]
                    for weight, target in specs:
                        caps = [min(2**upper[a][s],
                                    weight*2**upper[a][u]) for a in range(3)]
                        if sum(caps) < target:
                            raise old.Contradiction(
                                ['weighted', s, u, weight, target])
                        for a in range(3):
                            residual = target-sum(caps[b] for b in range(3)
                                                  if b != a)
                            if residual > 0:
                                changed |= update('lower', a, s,
                                                  old.clog(residual),
                                                  ['weighted', s, u, weight,
                                                   target, 0])
                                changed |= update('lower', a, u,
                                                  old.clog((residual+weight-1)
                                                           //weight),
                                                  ['weighted', s, u, weight,
                                                   target, 1])
            if not changed:
                return trace, None
    except old.Contradiction as error:
        return trace, error.reason


if __name__ == '__main__':
    old.propagate = propagate
    old.main()
    path = Path(sys.argv[2])
    data = json.loads(path.read_text())
    data['model'] = dict(name='SH55 three-term geometric moment', dimension=4,
                         width=6, terms=3, linear_budget=141,
                         quadratic_budget=2496,
                         quadratic_derivation='144 sum kappa^2 < 2809*4^2*8')
    tmp = path.with_suffix('.json.tmp')
    tmp.write_text(json.dumps(data, separators=(',', ':')))
    tmp.replace(path)
