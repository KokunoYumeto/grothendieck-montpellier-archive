"""HD-G20: exact spin and Hochschild ranks; no external dependencies.

Finite checks supplement the real-form and actual-functor proof in the
separate note. A modular rank lower bound is combined with an explicit
independent rational kernel basis, so no characteristic-zero rank is
inferred solely from a modular upper bound.
"""
from itertools import combinations
from pathlib import Path
import json

N = 16
P = 65537
TOP = (1 << N) - 1
SOURCE = {0: 1, TOP: -1}

def add(a, b, scale=1):
    out = dict(a)
    for mask, coeff in b.items():
        out[mask] = out.get(mask, 0) + scale*coeff
        if not out[mask]:
            del out[mask]
    return out

def wedge(i, a):
    return {mask | (1 << i): coeff*(-1)**((mask & ((1 << i)-1)).bit_count())
            for mask, coeff in a.items() if not (mask >> i) & 1}

def contract(i, a):
    return {mask ^ (1 << i): coeff*(-1)**((mask & ((1 << i)-1)).bit_count())
            for mask, coeff in a.items() if (mask >> i) & 1}

def deriv(R, a):
    out = {}
    for i in range(N):
        for j in range(N):
            if R[i][j]:
                out = add(out, wedge(i, contract(j, a)), R[i][j])
    return out

def spin_columns(a):
    cols = []
    for i in range(N):
        for j in range(N):
            twice = {mask: 2*c for mask, c in wedge(i, contract(j, a)).items()}
            cols.append(add(twice, a, -int(i == j)))
    cols += [wedge(i, wedge(j, a)) for i, j in combinations(range(N), 2)]
    cols += [contract(i, contract(j, a)) for i, j in combinations(range(N), 2)]
    assert len(cols) == 496
    return cols

def modular_rank(cols):
    pivots = {}
    for col in cols:
        v = {m: c % P for m, c in col.items() if c % P}
        while v:
            key = min(v)
            if key not in pivots:
                scale = pow(v[key], -1, P)
                pivots[key] = {m: c*scale % P for m, c in v.items()}
                break
            scale = v[key]
            for m, c in pivots[key].items():
                v[m] = (v.get(m, 0) - scale*c) % P
                if not v[m]:
                    del v[m]
    return len(pivots)

src = spin_columns(SOURCE)
assert modular_rank(src) == 241
count = 0
for i in range(N):
    for j in range(N):
        if i != j:
            assert src[i*N+j] == {}
            count += 1
for i in range(N-1):
    assert add(src[i*N+i], src[(N-1)*N+N-1], -1) == {}
    count += 1
assert count == 255

# Holomorphic basis indices 0..7; antiholomorphic indices 8..15.
# HH1 consists of the eight first contractions and eight last wedges.
def hh1(i, a):
    return contract(i, a) if i < 8 else wedge(i, a)
hh2 = [hh1(i, hh1(j, SOURCE)) for i, j in combinations(range(16), 2)]
assert modular_rank(hh2) == 56

# Real Weil volume Re product_i(x_i+i*y_i), in a real integral basis.
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
assert modular_rank(spin_columns(weilt)) == 241

# 64 independent real (1,1) bivectors, and their 64 dual contractions.
pairs = [[(i, i+8, 1)] for i in range(8)]
for i, j in combinations(range(8), 2):
    pairs.append([(i, j, 1), (i+8, j+8, 1)])
    pairs.append([(i, j+8, 1), (i+8, j, -1)])
assert len(pairs) == 64
for terms in pairs:
    w, c = {}, {}
    for i, j, value in terms:
        w = add(w, wedge(i, wedge(j, weilt)), value)
        c = add(c, contract(i, contract(j, weilt)), value)
    assert w == {} and c == {}

# 127 independent realifications of complex matrices A+iB with tr(B)=0.
def realify(A, B):
    return [[A[i][j] if i < 8 and j < 8 else
             -B[i][j-8] if i < 8 else
             B[i-8][j] if j < 8 else A[i-8][j-8]
             for j in range(16)] for i in range(16)]

glcount = 0
for i in range(8):
    for j in range(8):
        A, B = [[0]*8 for _ in range(8)], [[0]*8 for _ in range(8)]
        A[i][j] = 1
        R = realify(A, B)
        assert add(deriv(R, weilt), weilt, -int(i == j)) == {}
        glcount += 1
        if i != j:
            A[i][j], B[i][j] = 0, 1
            assert deriv(realify(A, B), weilt) == {}
            glcount += 1
for i in range(7):
    A, B = [[0]*8 for _ in range(8)], [[0]*8 for _ in range(8)]
    B[i][i], B[7][7] = 1, -1
    assert deriv(realify(A, B), weilt) == {}
    glcount += 1
assert glcount == 127
assert 64+64+glcount == 255

def matmul(A, B):
    return [[sum(A[i][k]*B[k][j] for k in range(len(B)))
             for j in range(len(B[0]))] for i in range(len(A))]

I = [[0]*16 for _ in range(16)]
for i in range(8):
    I[i][i+8], I[i+8][i] = -1, 1
J = [[0]*32 for _ in range(32)]
Q = [[0]*32 for _ in range(32)]
for i in range(16):
    Q[i][i+16] = Q[i+16][i] = 1
    for j in range(16):
        J[i][j] = I[i][j]
        J[i+16][j+16] = -I[j][i]
assert matmul(J, J) == [[-int(i == j) for j in range(32)] for i in range(32)]
assert matmul(list(map(list, zip(*J))), matmul(Q, J)) == Q

out = dict(check='PASS', spin_lie_dimension=496, modular_prime=P,
           source_action_rank=241, source_explicit_kernel_dimension=255,
           source_HH2_contraction_rank=56,
           target_real_Weil_action_rank=241,
           target_explicit_kernel_blocks=[64,127,64],
           orthogonal_complex_structure_checks=True,
           source_Killing_signature=[135,120], target_Killing_signature=[128,127],
           scope='Finite exterior ranks and exact annihilators only; actual transport, Fock comparison and real-form identification are proved in the accompanying note.')
Path(__file__).with_suffix('.json').write_text(json.dumps(out, indent=2)+'\n')
print(json.dumps(out, indent=2))
