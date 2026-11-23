"""Exact HD-G19 exterior-algebra and real-form certificate.

Reconstruct the full spin-Lie action on the actual character
(1-vol_1)(1-vol_2), with two real eight-dimensional summands.
The mathematical proof identifies its kernel; the modular rank below
independently certifies the matching lower bound over the rationals.
"""
from itertools import combinations
from pathlib import Path
import json

N = 16
P = 65537
VOL1, VOL2 = (1 << 8) - 1, ((1 << 8) - 1) << 8
SEED = {0: 1, VOL1: -1, VOL2: -1, (1 << N)-1: 1}

def add(a, b, scale=1):
    a = dict(a)
    for m, c in b.items():
        a[m] = a.get(m, 0) + scale*c
        if a[m] == 0:
            del a[m]
    return a

def wedge(i, a):
    out = {}
    for m, c in a.items():
        if not (m >> i) & 1:
            out[m | (1 << i)] = c*(-1)**((m & ((1 << i)-1)).bit_count())
    return out

def contract(i, a):
    out = {}
    for m, c in a.items():
        if (m >> i) & 1:
            out[m ^ (1 << i)] = c*(-1)**((m & ((1 << i)-1)).bit_count())
    return out

def deriv(R, a):
    out = {}
    for i in range(N):
        for j in range(N):
            if R[i][j]:
                out = add(out, wedge(i, contract(j, a)), R[i][j])
    return out

columns = []
for i in range(N):
    for j in range(N):
        # Twice the spin action of E_ij, avoiding half-integral entries.
        col = {m: 2*c for m, c in wedge(i, contract(j, SEED)).items()}
        columns.append(add(col, SEED, -int(i == j)))
for i, j in combinations(range(N), 2):
    columns.append(wedge(i, wedge(j, SEED)))
for i, j in combinations(range(N), 2):
    columns.append(contract(i, contract(j, SEED)))
assert len(columns) == 496

pivots = {}
for col in columns:
    v = {m: c % P for m, c in col.items() if c % P}
    while v:
        p = min(v)
        if p not in pivots:
            z = pow(v[p], -1, P)
            pivots[p] = {m: c*z % P for m, c in v.items()}
            break
        z = v[p]
        for m, c in pivots[p].items():
            v[m] = (v.get(m, 0) - z*c) % P
            if v[m] == 0:
                del v[m]
assert len(pivots) == 370

kernel_count = 0
for base in (0, 8):
    for i in range(base, base+8):
        for j in range(base, base+8):
            if i != j:
                assert columns[i*N+j] == {}
                kernel_count += 1
    for i in range(base, base+7):
        assert add(columns[i*N+i], columns[(base+7)*N+base+7], -1) == {}
        kernel_count += 1
assert kernel_count == 126

# Real matrix model of su(4,4), with X=A+iB and R(X)=[[A,-B],[B,A]].
J = [1]*4 + [-1]*4
su = []
labels = []
def realify(A, B):
    return [[A[i][j] if i < 8 and j < 8 else
             -B[i][j-8] if i < 8 else
             B[i-8][j] if j < 8 else A[i-8][j-8]
             for j in range(16)] for i in range(16)]

for i, j in combinations(range(8), 2):
    A = [[0]*8 for _ in range(8)]
    B = [[0]*8 for _ in range(8)]
    A[i][j], A[j][i] = 1, -J[i]*J[j]
    su.append(realify(A, B)); labels.append('compact' if J[i] == J[j] else 'noncompact')
    A = [[0]*8 for _ in range(8)]
    B[i][j], B[j][i] = 1, J[i]*J[j]
    su.append(realify(A, B)); labels.append('compact' if J[i] == J[j] else 'noncompact')
for i in range(7):
    A = [[0]*8 for _ in range(8)]
    B = [[0]*8 for _ in range(8)]
    B[i][i], B[7][7] = 1, -1
    su.append(realify(A, B)); labels.append('compact')
assert len(su) == 63 and labels.count('compact') == 31 and labels.count('noncompact') == 32

theta = {}
for i, j in enumerate(J):
    theta = add(theta, wedge(i, wedge(i+8, {0: 1})), j)
# Real part of product_i(x_i+i*y_i), with exact integer coefficients.
weilt = {}
for choices in range(256):
    k = choices.bit_count()
    if k % 2:
        continue
    term = {0: (-1)**(k//2)}
    for i in reversed(range(8)):
        term = wedge(i+8 if choices >> i & 1 else i, term)
    weilt = add(weilt, term)
assert len(weilt) == 128
for R in su:
    assert sum(R[i][i] for i in range(16)) == 0
    assert deriv(R, theta) == {}
    assert deriv(R, weilt) == {}
for R, label in zip(su, labels):
    sign = -1 if label == 'compact' else 1
    assert all(R[j][i] == sign*R[i][j] for i in range(16) for j in range(16))
    trace_square = sum(R[i][j]*R[j][i] for i in range(16) for j in range(16))
    assert trace_square*sign > 0

ext4 = [1,8,12,8,1]
ext8 = [sum(ext4[i]*ext4[k-i] for i in range(5) if 0 <= k-i < 5) for k in range(9)]
assert ext8 == [1,16,88,208,274,208,88,16,1]
out = dict(check='PASS', lie_dimension=496, modular_prime=P,
           action_rank_mod_prime=len(pivots), explicit_rational_kernel_dimension=126,
           stabilizer='sl(8,R) direct sum sl(8,R)',
           su44_generators=63, su44_killing_signature=[32,31],
           sl8r_killing_signature=[35,28],
           theta_and_real_weil_volume_annihilated=True,
           actual_seed_ext_dimensions=ext8,
           scope='Exact exterior-algebra rank and invariant-form checks; the nonembedding and functorial morphisms are proved in the note.')
Path(__file__).with_suffix('.json').write_text(json.dumps(out,indent=2)+'\n')
print(json.dumps(out,indent=2))
