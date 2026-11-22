#!/usr/bin/env python3
"""Independent stdlib full orbit-cover and direct-Koszul permanent gate.

Input contains only candidate orbit representatives and orbit sizes.
For each row this checker constructs all 1152 symmetry images, verifies
minimality and the asserted size, and recomputes a modular Koszul minor
rank.  Distinct canonical representatives have disjoint orbits; equality
of the sum of orbit sizes with C(36,10) proves complete coverage.
An OPEN output is a genuine unresolved case, never a rank upper bound.
"""
import argparse
from collections import Counter
from itertools import permutations
from math import comb
from multiprocessing import Pool
from pathlib import Path
import json
import time

from br_linear import PAIRS, RECTS
from check_koszul import koszul

TABLES = None
PRIME = 1000003


def make_tables():
    positions = {rectangle: i for i, rectangle in enumerate(RECTS)}
    actions = []
    for rows in permutations(range(4)):
        for columns in permutations(range(4)):
            for transpose in (False, True):
                action = []
                for I, J in RECTS:
                    r = tuple(sorted(rows[i] for i in I))
                    c = tuple(sorted(columns[j] for j in J))
                    action.append(1 << positions[(c, r) if transpose else (r, c)])
                actions.append(tuple(action))
    assert len(set(actions)) == 1152
    tables = []
    for action in actions:
        chunks = []
        for offset in range(0, 36, 6):
            values = [0] * 64
            for mask in range(1, 64):
                bit = mask & -mask
                values[mask] = values[mask ^ bit] | action[offset + bit.bit_length() - 1]
            chunks.append(values)
        tables.append(chunks)
    return tables


def worker(record):
    mask, stated_size = record
    assert mask.bit_count() == 10 and mask < 1 << 36
    r0, r1, r2, r3, r4, r5 = [(mask >> (6 * i)) & 63 for i in range(6)]
    orbit = {t[0][r0] | t[1][r1] | t[2][r2] | t[3][r3] | t[4][r4] | t[5][r5]
             for t in TABLES}
    assert len(orbit) == stated_size and min(orbit) == mask
    subset = [i for i in range(36) if mask >> i & 1]
    tests = []
    for along, degree in [('A', 1), ('A', 2), ('A', 3), ('A', 4),
                          ('B', 2), ('B', 3), ('B', 4)]:
        rank, blocks, cost = koszul(subset, 1, along, degree, PRIME)
        test = {'factor': along, 'p': degree, 'rank': rank, 'cost': cost}
        tests.append(test)
        if rank > 17 * cost:
            return {'mask': mask, 'orbit_size': stated_size, 'status': 'EXCLUDED',
                    'witness': test}
    return {'mask': mask, 'subset': subset, 'orbit_size': stated_size,
            'status': 'OPEN', 'tests': tests}


def main():
    global TABLES
    parser = argparse.ArgumentParser()
    parser.add_argument('--workers', type=int, default=6)
    parser.add_argument('--limit', type=int)
    args = parser.parse_args()
    assert all(PRIME % p for p in range(2, int(PRIME**0.5) + 1))
    records = [tuple(map(int, line.split())) for line in
               Path('certificates/per10_orbits.tsv').read_text().splitlines()[1:]]
    assert len({mask for mask, size in records}) == len(records)
    assert records == sorted(records)
    assert sum(size for mask, size in records) == comb(36, 10)
    whole_count = len(records)
    if args.limit:
        records = records[:args.limit]
    TABLES = make_tables()
    start = time.time()
    counts, witness_counts = Counter(), Counter()
    remaining, checked, covered = [], 0, 0
    destination = Path('certificates/per10_global_gate.json')
    trace = Path('certificates/per10_global_gate_trace.jsonl')
    with trace.open('w') as output, Pool(args.workers) as pool:
        for result in pool.imap(worker, records, chunksize=24):
            output.write(json.dumps(result, separators=(',', ':')) + '\n')
            checked += 1
            covered += result['orbit_size']
            counts[result['status']] += 1
            if result['status'] == 'OPEN':
                remaining.append(result)
            else:
                witness = result['witness']
                witness_counts[witness['factor'] + str(witness['p'])] += 1
            if checked % 1000 == 0 or checked == len(records):
                output.flush()
                final = checked == whole_count
                out = {'scope': 'Global permanent coordinate ten-plane gate; characteristic zero',
                       'status': 'COMPLETE' if final else 'PARTIAL',
                       'representatives': whole_count, 'checked': checked,
                       'covered_subsets': covered, 'required_subsets': comb(36, 10),
                       'counts': dict(counts), 'witness_counts': dict(witness_counts),
                       'prime': PRIME, 'remaining': remaining,
                       'seconds': time.time() - start}
                temporary = destination.with_suffix('.json.tmp')
                temporary.write_text(json.dumps(out, indent=2) + '\n')
                temporary.replace(destination)
                print(json.dumps({key: value for key, value in out.items() if key != 'remaining'}),
                      flush=True)


if __name__ == '__main__':
    main()
