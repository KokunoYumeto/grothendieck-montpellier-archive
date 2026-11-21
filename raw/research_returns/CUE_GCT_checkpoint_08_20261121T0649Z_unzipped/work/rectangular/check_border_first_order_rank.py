"""Exact modular tangent-to-rank-locus test; finite evidence only."""
import json
import sys
from pathlib import Path
import numpy as np

def rref(matrix, prime):
    a = np.asarray(matrix, dtype=np.int64).copy() % prime
    nr, nc = a.shape
    pivots = []
    r = 0
    for c in range(nc):
        eligible = np.flatnonzero(a[r:, c])
        if not len(eligible):
            continue
        i = r + int(eligible[0])
        a[[r, i]] = a[[i, r]]
        a[r] = a[r] * pow(int(a[r, c]), -1, prime) % prime
        for j in range(nr):
            if j != r and a[j, c]:
                a[j] = (a[j] - a[j, c] * a[r]) % prime
        pivots.append(c)
        r += 1
        if r == nr:
            break
    return a, pivots

def kernel(matrix, prime):
    a, pivots = rref(matrix, prime)
    free = [c for c in range(a.shape[1]) if c not in pivots]
    k = np.zeros((a.shape[1], len(free)), dtype=np.int64)
    for j, c in enumerate(free):
        k[c, j] = 1
        k[pivots, j] = -a[:len(pivots), c] % prime
    assert not np.any(matrix @ k % prime)
    return k, len(pivots)

def main():
    n = int(sys.argv[1])
    directory = Path(sys.argv[2])
    stem = directory / f"border_band2_first_order_m{n}"
    data = json.loads(stem.with_suffix('.json').read_text())
    shape = (data['rows'], data['columns'])
    a = np.fromfile(str(stem)+'_0.u16', dtype='<u2').reshape(shape).astype(np.int64)
    b = np.fromfile(str(stem)+'_1.u16', dtype='<u2').reshape(shape).astype(np.int64)
    p = data['prime']
    out = {'m': n, 'prime': p}
    for label, width in [('first', 6*n+3), ('all', 8*n+3)]:
        k, rank = kernel(a[:, :width], p)
        images = b[:, :width] @ k % p
        newrank = len(rref(np.concatenate((a[:, :width], images), axis=1), p)[1])
        out[label] = {'rank_at_zero': rank, 'kernel_dimension': k.shape[1],
                      'rank_with_first_order_kernel_images': newrank,
                      'normal_gain': newrank-rank}
    path = Path(str(stem)+'_rank.json')
    path.write_text(json.dumps(out, indent=2)+'\n')
    print(json.dumps(out, indent=2))

if __name__ == '__main__':
    main()
