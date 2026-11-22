#!/usr/bin/env python3
"""Independently verify every C2=I, nine-epsilon evaluation, using stdlib.

The coefficient archives encode signed S3 orbit sums.  This program reads
their NPY members directly and evaluates all samples in exact 32-bit lanes.
Per-profile certificates are cached by all three input hashes, so a growing
basis can be checked without repeating already certified blocks.
"""
import argparse
from collections import Counter, defaultdict
from functools import lru_cache
import hashlib
from itertools import permutations
import json
import os
from pathlib import Path
import tempfile
import time
import zipfile

from verify_centered_evaluations import PackedSamples, check_arithmetic, read_array


PERMS = list(permutations(range(3)))
SIGNS = [(-1) ** sum(p[i] > p[j] for i in range(3) for j in range(i + 1, 3))
         for p in PERMS]
VERSION = 1


def digest(data):
    return hashlib.sha256(data).hexdigest()


def atomic_json(path, data):
    path.parent.mkdir(parents=True, exist_ok=True)
    with tempfile.NamedTemporaryFile(mode='w', dir=path.parent, prefix=path.name + '.',
                                     suffix='.tmp', delete=False) as handle:
        json.dump(data, handle, indent=2)
        handle.write('\n')
        temporary = handle.name
    os.replace(temporary, path)


def matrix_snapshot(directory):
    # The producer atomically replaces each file.  Match the metadata both
    # before and after the byte read, and require its advertised length.
    for _ in range(8):
        before = (directory / 'matrix.json').read_bytes()
        raw = (directory / 'matrix.bin').read_bytes()
        after = (directory / 'matrix.json').read_bytes()
        metadata = json.loads(before)
        if before == after and len(raw) == metadata['shape'][0] * metadata['shape'][1]:
            return metadata, raw
    raise RuntimeError('Evaluation matrix is being replaced; retry after producer finishes.')


def verify_profile(profile, archive_path, packed, coordinates, expected, cache_size):
    assert len(profile) == 8 and sum(j * k for j, k in enumerate(profile, 2)) == 27
    degrees = [j for j, k in enumerate(profile[1:], 3) for _ in range(k)]
    assert sum(degrees) == 27 - 2 * profile[0] and len(degrees) <= 9
    triples = {j: [(a, b, j - a - b) for a in range(j + 1) for b in range(j - a + 1)]
               for j in range(3, 10)}
    lookup = {tuple(x): i for i, x in enumerate(coordinates)}
    maps = {j: [[lookup[(j,) + tuple(alpha[p] for p in pi)] for alpha in triples[j]]
                for pi in PERMS] for j in range(3, 10)}
    terms = defaultdict(list)
    with zipfile.ZipFile(archive_path) as archive:
        for row in range(len(expected)):
            keys = read_array(archive, 'keys' + str(row))
            coefficients = read_array(archive, 'coeff' + str(row))
            assert len(keys) == len(coefficients) and len(set(keys)) == len(keys)
            # The signed orbit is reduced before linear combination.  Each
            # lane of each term is therefore at most 100*100.
            assert 100 * 100 * len(keys) < 2 ** 32
            for key, coefficient in zip(keys, coefficients):
                if coefficient % 101:
                    terms[key].append((row, coefficient % 101))

    @lru_cache(maxsize=cache_size)
    def monomial(variables):
        if not variables:
            return packed.one
        if len(variables) == 1:
            return packed.values[variables[0]]
        return packed.multiply_coordinate(monomial(variables[:-1]), variables[-1])

    accumulators = [0] * len(expected)
    for key, uses in terms.items():
        local = (key[0].to_bytes(8, 'big') + key[1].to_bytes(8, 'big'))[:len(degrees)]
        orbit = Counter()
        for pi, sign in enumerate(SIGNS):
            variables = tuple(sorted(maps[j][pi][index] for j, index in zip(degrees, local)))
            orbit[variables] += sign
        # An odd stabilizer annihilates an orbit.  Such keys must have been
        # omitted by the coefficient builder.  Retain even stabilizer sizes.
        assert sum(abs(count) for count in orbit.values()) == 6
        positive = sum(count * monomial(variables) for variables, count in orbit.items() if count > 0)
        negative = sum(-count * monomial(variables) for variables, count in orbit.items() if count < 0)
        # Each positive/negative lane is in [0,300].  Adding 303 before
        # subtraction gives a lane in [3,603], preventing all borrows and
        # preserving the residue modulo101.  The reducer requires <101^2.
        orbit_value = packed.reduce(positive + 303 * packed.one - negative)
        for row, coefficient in uses:
            accumulators[row] += coefficient * orbit_value
    actual = [bytes(packed.unpack(value)) for value in accumulators]
    for row, (a, e) in enumerate(zip(actual, expected)):
        assert a == e, dict(profile=profile, row=row,
                           mismatches=[i for i, (x, y) in enumerate(zip(a, e)) if x != y][:8])
    return dict(profile=profile, rows=len(actual), samples=packed.samples,
                entries=len(actual) * packed.samples, orbit_monomials=len(terms),
                monomial_cache=monomial.cache_info()._asdict(),
                recomputed_block_sha256=digest(b''.join(actual)), all_checks_passed=True)


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--samples', type=Path,
                        default=Path('work/quaternary/results/orthonormal_determinant_2420.json'))
    parser.add_argument('--basis', type=Path,
                        default=Path('work/support_lmr/results/bracket_basis_c9'))
    parser.add_argument('--evaluation', type=Path,
                        default=Path('work/support_lmr/results/bracket_evaluation_c9_determinant'))
    parser.add_argument('--cache', type=Path,
                        default=Path('work/quaternary/results/c9_evaluation_verified_blocks'))
    parser.add_argument('--cache-size', type=int, default=8192)
    parser.add_argument('--limit-profiles', type=int)
    parser.add_argument('--output', type=Path, required=True)
    args = parser.parse_args()
    started = time.monotonic()
    arithmetic = check_arithmetic()
    sample_bytes = args.samples.read_bytes()
    sample_hash = digest(sample_bytes)
    samples = json.loads(sample_bytes)
    metadata, raw = matrix_snapshot(args.evaluation)
    r, c = metadata['shape']
    assert samples['prime'] == metadata['prime'] == 101
    assert c == len(samples['normalized_tensors']) and all(v < 101 for v in raw)
    lookup = {tuple(alpha): i for i, alpha in enumerate(samples['coordinates'])}
    for a in range(3):
        for b in range(3 - a):
            alpha = (a, b, 2 - a - b)
            coordinate = lookup[(2,) + alpha]
            assert all(row[coordinate] == int(2 in alpha) for row in samples['normalized_tensors'])
    packed = PackedSamples(samples['normalized_tensors'])
    offset = 0
    records = []
    for entry in metadata['profiles']:
        profile, count = entry['profile'], entry['rows']
        tag = '_'.join(map(str, profile))
        block_bytes = raw[offset * c:(offset + count) * c]
        expected = [block_bytes[i * c:(i + 1) * c] for i in range(count)]
        archive_path = args.basis / (tag + '.npz')
        fingerprints = dict(verifier_version=VERSION, sample_sha256=sample_hash,
                            archive_sha256=digest(archive_path.read_bytes()),
                            expected_block_sha256=digest(block_bytes))
        cache_path = args.cache / (tag + '.json')
        record = json.loads(cache_path.read_text()) if cache_path.exists() else None
        cached = bool(record and record.get('fingerprints') == fingerprints)
        if not cached:
            before = time.monotonic()
            record = verify_profile(profile, archive_path, packed, samples['coordinates'],
                                    expected, args.cache_size)
            record['fingerprints'] = fingerprints
            record['seconds'] = round(time.monotonic() - before, 3)
            atomic_json(cache_path, record)
        assert record['rows'] == count and record['recomputed_block_sha256'] == digest(block_bytes)
        records.append(dict(record, reused_cached_check=cached))
        offset += count
        print(json.dumps(dict(profile=profile, rows=count, cached=cached,
                              seconds=record['seconds'], verified_rows=offset)), flush=True)
        if args.limit_profiles and len(records) >= args.limit_profiles:
            break
    result = dict(prime=101, profiles=records, rows=offset, samples=c, entries=offset * c,
                  complete=offset == 2386, arithmetic_checks=arithmetic,
                  agrees_with_entire_available_matrix=offset == r,
                  matrix_sha256=digest(raw[:offset * c]),
                  sample_sha256=sample_hash, seconds=round(time.monotonic() - started, 3),
                  all_checks_passed=True)
    atomic_json(args.output, result)
    print(json.dumps({k: v for k, v in result.items() if k != 'profiles'}), flush=True)


if __name__ == '__main__':
    main()
