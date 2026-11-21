"""Same exact model, with modular screening of identifying evaluation points.

A full-rank evaluation matrix modulo 1000003 is automatically full rank
over Q. Every selected matrix, determinant, and full Hecke calculation
is then exact and subject to the independent characteristic-zero replay.
This avoids repeated symbolic rank simplification on large integers.
"""
from pathlib import Path
import argparse
import importlib.util
import json
import random
import time

HERE = Path(__file__).resolve().parent
SOURCE = HERE.parent / 'compute_harmonic_hecke.py'
spec = importlib.util.spec_from_file_location('u3_frozen_discovery', SOURCE)
model = importlib.util.module_from_spec(spec)
spec.loader.exec_module(model)
model.BASE = HERE / 'fast'
model.BASE.mkdir(exist_ok=True)
model.NEIGHBORS = HERE.parent.parent / 'hecke_level_one/u3_weight5_exact_exploration.json'


def rank_mod(rows, p=1000003):
    a = [[int(x) % p for x in row] for row in rows]
    r = 0
    for j in range(len(a[0])):
        pivot = next((i for i in range(r, len(a)) if a[i][j]), None)
        if pivot is None:
            continue
        a[r], a[pivot] = a[pivot], a[r]
        v = pow(a[r][j], -1, p)
        a[r] = [v * x % p for x in a[r]]
        for i in range(r + 1, len(a)):
            v = a[i][j]
            if v:
                a[i] = [(x - v*y) % p for x, y in zip(a[i], a[r])]
        r += 1
        if r == len(a):
            break
    return r


def choose_points(k, expanded, H):
    rng = random.Random(20261121+k)
    points, rows = [], []
    columns = list(zip(*[[int(x) for x in row] for row in H.tolist()]))
    for attempt in range(1000):
        z = tuple(rng.randrange(-2, 4) for _ in range(3))
        w = tuple(rng.randrange(-2, 4) for _ in range(3))
        values = model.eval_orbits_integer(expanded, k, z, w)
        row = [sum(x*y for x, y in zip(values, column)) for column in columns]
        if rank_mod(rows + [row]) > len(rows):
            rows.append(row)
            points.append((z, w))
        if len(points) == H.cols:
            matrix = model.sp.Matrix(rows)
            assert matrix.det(method='domain-ge')
            return points, matrix
    raise RuntimeError('No full evaluation matrix found modulo screening prime')


model.choose_points = choose_points
parser = argparse.ArgumentParser()
parser.add_argument('k', type=int)
args = parser.parse_args()
neighbors = json.loads(model.NEIGHBORS.read_text())
start = time.monotonic()
data = model.calculate(args.k, [r for r in neighbors['results'] if r['p'] in (7, 13)])
print('FULL_TIMING', args.k, time.monotonic() - start, flush=True)
