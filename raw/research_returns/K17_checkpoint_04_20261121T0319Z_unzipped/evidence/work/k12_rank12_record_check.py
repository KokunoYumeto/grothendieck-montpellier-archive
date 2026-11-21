"""Exact rank check on the first published n8/rnk12 GAP record.

Input is the archived prefix of the official repository file. No GAP
code is executed: the first matrix is parsed as a Python literal.
This checks the recorded vectors and their quadratic rank; it does not
rerun the source's complete minimum-vector enumeration.
"""
from ast import literal_eval
from fractions import Fraction
from pathlib import Path
import hashlib
import json


def rational_rank(rows):
    a = [[Fraction(x) for x in row] for row in rows]
    if not a:
        return 0
    rank = 0
    for col in range(len(a[0])):
        pivot = next((i for i in range(rank, len(a)) if a[i][col]), None)
        if pivot is None:
            continue
        a[rank], a[pivot] = a[pivot], a[rank]
        scale = a[rank][col]
        a[rank] = [x / scale for x in a[rank]]
        for i in range(rank + 1, len(a)):
            scale = a[i][col]
            if scale:
                a[i] = [x - scale * y for x, y in zip(a[i], a[rank])]
        rank += 1
        if rank == len(a):
            break
    return rank


path = Path(__file__).parent / 'k12_source_data/first_n8_rnk12_prefix.gap'
source = path.read_text()
outer = source.index('[')
start = source.index('[', outer + 1)
depth = 0
end = None
for i in range(start, len(source)):
    if source[i] == '[':
        depth += 1
    elif source[i] == ']':
        depth -= 1
        if depth == 0:
            end = i + 1
            break
assert end is not None
vectors = literal_eval(source[start:end])
assert all(len(v) == 8 and all(isinstance(x, int) for x in v) for v in vectors)
signed = {tuple(v) for v in vectors} | {tuple(-x for x in v) for v in vectors}
quadratics = [[v[i] * v[j] for i in range(8) for j in range(i, 8)] for v in vectors]
result = {
    'date': '2026-11-21',
    'source_url': 'https://raw.githubusercontent.com/elbazvip/Voronoi-complexes-database/master/DATA_gap/ListSHV_n8_rnk12',
    'repository_blob_sha': '12d9599d545c2f057f780ea96a7ed5a3369a8f1b',
    'prefix_sha256': hashlib.sha256(path.read_bytes()).hexdigest(),
    'record_index_one_based': 1,
    'listed_pair_representatives': len(vectors),
    'listed_signed_vectors': len(signed),
    'vector_span_rank_over_Q': rational_rank(vectors),
    'quadratic_span_rank_over_Q': rational_rank(quadratics),
    'projective_cone_dimension': rational_rank(quadratics) - 1,
    'vectors': vectors,
    'scope': 'Exact checks of the first stored vector record; no independent source minimum-set completeness or full file enumeration check.'
}
out = Path(__file__).with_suffix('.json')
out.write_text(json.dumps(result, indent=2) + '\n')
print(json.dumps({k: v for k, v in result.items() if k != 'vectors'}, indent=2))
