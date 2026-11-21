"""Bounded exact theta[15] probe for the A13 curve over F_256.

This is one arithmetic implementation, not a formal proof assistant.
It uses the complete Riemann--Roch basis of L(17 W_infinity), not
Mumford-divisor arithmetic. All field elements use the polynomial basis
for F_2[z]/(z^8+z^4+z^3+z+1).
"""
from pathlib import Path
import hashlib
import json
import math

ROOT = Path(__file__).resolve().parent
MODULUS = 0x11B


def product(a, b):
    ans = 0
    while b:
        if b & 1:
            ans ^= a
        b >>= 1
        a <<= 1
        if a & 0x100:
            a ^= MODULUS
    return ans


MUL = [[product(a, b) for b in range(256)] for a in range(256)]


def power(a, n):
    ans = 1
    while n:
        if n & 1:
            ans = MUL[ans][a]
        a = MUL[a][a]
        n >>= 1
    return ans


INV = [0] + [power(a, 254) for a in range(1, 256)]
assert all(MUL[a][INV[a]] == 1 for a in range(1, 256))


def x_series(r, i, precision=15):
    return [
        power(r, i - j) if j <= i and math.comb(i, j) & 1 else 0
        for j in range(precision)
    ]


def convolution(a, b):
    result = [0] * len(a)
    for i, ai in enumerate(a):
        if ai:
            for j in range(len(a) - i):
                result[i + j] ^= MUL[ai][b[j]]
    return result


def curve_value(x):
    return power(x, 5) ^ power(x, 3) ^ power(x, 2) ^ x


def jets(x, y):
    h0 = MUL[x][x] ^ x
    assert h0
    f = [0] * 15
    for i in (1, 2, 3, 5):
        for j, v in enumerate(x_series(x, i)):
            f[j] ^= v
    ys = [y] + [0] * 14
    for j in range(1, 15):
        rhs = f[j] ^ ys[j - 1]
        if j >= 2:
            rhs ^= ys[j - 2]
        if j % 2 == 0:
            rhs ^= MUL[ys[j // 2]][ys[j // 2]]
        ys[j] = MUL[rhs][INV[h0]]
    # Reconstruct the implicit equation to the full claimed precision.
    residual = f[:]
    for j in range(15):
        residual[j] ^= MUL[h0][ys[j]]
        if j >= 1:
            residual[j] ^= ys[j - 1]
        if j >= 2:
            residual[j] ^= ys[j - 2]
        if j % 2 == 0:
            residual[j] ^= MUL[ys[j // 2]][ys[j // 2]]
    assert not any(residual)
    return ys


def matrix(x, y):
    ys = jets(x, y)
    columns = [x_series(x, i) for i in range(9)]
    columns += [convolution(x_series(x, i), ys) for i in range(7)]
    rows = [[columns[j][i] for j in range(16)] for i in range(15)]
    # A(0)=0 and A(1)=0, since both branch points have Y=0.
    rows += [[1] + [0] * 15, [1] * 9 + [0] * 7]
    return rows


def rank_and_minor(rows):
    a = [r[:] for r in rows]
    labels = list(range(len(a)))
    pivot_rows = []
    row = 0
    determinant = 1
    for col in range(16):
        pivot = next((j for j in range(row, len(a)) if a[j][col]), None)
        if pivot is None:
            continue
        a[row], a[pivot] = a[pivot], a[row]
        labels[row], labels[pivot] = labels[pivot], labels[row]
        pivot_rows.append(labels[row])
        value = a[row][col]
        determinant = MUL[determinant][value]
        factor = INV[value]
        a[row] = [MUL[factor][v] for v in a[row]]
        for j in range(row + 1, len(a)):
            if a[j][col]:
                factor = a[j][col]
                a[j] = [v ^ MUL[factor][w] for v, w in zip(a[j], a[row])]
        row += 1
    return row, pivot_rows, determinant


points = []
records = []
for x in range(256):
    h = MUL[x][x] ^ x
    rhs = curve_value(x)
    for y in range(256):
        if MUL[y][y] ^ MUL[h][y] == rhs:
            points.append([x, y])
            if h:
                a = matrix(x, y)
                rank, minor_rows, determinant = rank_and_minor(a)
                records.append({
                    "x": x, "y": y, "rank": rank,
                    "minor_rows": minor_rows,
                    "minor_determinant": determinant if rank == 16 else None,
                    "matrix_sha256": hashlib.sha256(bytes(sum(a, []))).hexdigest(),
                })

out = {
    "scope": "One exhaustive RR computation of nonbranch theta[15](F256) on A13",
    "field_modulus_binary": MODULUS,
    "field_all_nonzero_inverses_checked": True,
    "model": "Y^2+(X^2+X)Y=X^5+X^3+X^2+X",
    "theta_characteristic": "B=W0+W1-Winfinity",
    "RR_basis": ["X^i:0<=i<=8", "X^i*Y:0<=i<=6"],
    "conditions": "15 Taylor zeros at R, plus values zero at W0,W1",
    "rational_affine_points": points,
    "rational_projective_count": len(points) + 1,
    "nonbranch_count": len(records),
    "rank_histogram": {str(r): sum(t["rank"] == r for t in records) for r in range(17)
                       if any(t["rank"] == r for t in records)},
    "candidate_points": [[t["x"], t["y"]] for t in records if t["rank"] < 16],
    "all_records": records,
}
assert len(points) + 1 == 223
assert len(records) == 220
target = ROOT / "probe_A44_theta15.json"
target.write_text(json.dumps(out, indent=2) + "\n")
print(json.dumps({k: out[k] for k in ("rational_projective_count", "nonbranch_count",
                                    "rank_histogram", "candidate_points")}))
print("output_sha256", hashlib.sha256(target.read_bytes()).hexdigest())
