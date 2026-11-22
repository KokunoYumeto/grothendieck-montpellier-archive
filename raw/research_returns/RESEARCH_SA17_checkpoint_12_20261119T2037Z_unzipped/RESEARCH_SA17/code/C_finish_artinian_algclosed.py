#!/usr/bin/env python3
"""Bounded certificate for R=F_p[a,b]/(a,b)^2, p=3,5,7,11.

Checks the faithful regular encoding, centralizer and entry recovery for
free ranks 1,2,3, the R-dual versus the nonfree k-dual, and recovery of a
rank-two O_1 coaction and its R-valued invariant form from a scrambled
k-basis. This is not an implementation of the full canonical-template
algorithm and does not certify arbitrary ranks or coefficient degrees.
"""
from pathlib import Path
from datetime import datetime, timezone
from time import perf_counter
import json
import random
import numpy as np

start = perf_counter()


def rref(matrix, p):
    A = np.array(matrix, dtype=np.int64).copy() % p
    row = 0
    pivots = []
    for col in range(A.shape[1]):
        candidates = np.flatnonzero(A[row:, col])
        if not len(candidates):
            continue
        pivot = row + int(candidates[0])
        A[[row, pivot]] = A[[pivot, row]]
        A[row] = A[row] * pow(int(A[row, col]), -1, p) % p
        for other in range(A.shape[0]):
            if other != row and A[other, col]:
                A[other] = (A[other] - int(A[other, col])*A[row]) % p
        pivots.append(col)
        row += 1
        if row == A.shape[0]:
            break
    return A, pivots


def kernel(matrix, p):
    A, pivots = rref(matrix, p)
    free = [j for j in range(A.shape[1]) if j not in pivots]
    result = []
    for j in free:
        v = np.zeros(A.shape[1], dtype=np.int64)
        v[j] = 1
        for i, pivot in enumerate(pivots):
            v[pivot] = -A[i, j] % p
        result.append(v)
    return result


def inverse(A, p):
    n = A.shape[0]
    reduced, pivots = rref(np.concatenate((A, np.eye(n, dtype=np.int64)), axis=1), p)
    if pivots[:n] != list(range(n)):
        raise ValueError('singular matrix')
    return reduced[:, n:] % p


def is_invertible(A, p):
    return len(rref(A, p)[1]) == A.shape[0]


def eq(A, B, p):
    return np.array_equal(np.array(A) % p, np.array(B) % p)


Qa = np.array([[0, 0, 0], [1, 0, 0], [0, 0, 0]], dtype=np.int64)
Qb = np.array([[0, 0, 0], [0, 0, 0], [1, 0, 0]], dtype=np.int64)
Q = [np.eye(3, dtype=np.int64), Qa, Qb]


def reg(x, p):
    return sum((int(x[i])*Q[i] for i in range(3)), np.zeros((3, 3), dtype=np.int64)) % p


def reg_matrix(M, p):
    return np.block([[reg(M[i, j], p) for j in range(M.shape[1])]
                     for i in range(M.shape[0])]) % p


def recover_matrix(A, p):
    assert A.shape[0] % 3 == A.shape[1] % 3 == 0
    M = np.zeros((A.shape[0]//3, A.shape[1]//3, 3), dtype=np.int64)
    for i in range(M.shape[0]):
        for j in range(M.shape[1]):
            block = A[3*i:3*i+3, 3*j:3*j+3] % p
            M[i, j] = block[:, 0]
            assert eq(block, reg(M[i, j], p), p)
    return M


def rmatmul(A, B, p):
    C = np.zeros((A.shape[0], B.shape[1], 3), dtype=np.int64)
    C[:, :, 0] = A[:, :, 0] @ B[:, :, 0] % p
    for i in (1, 2):
        C[:, :, i] = (A[:, :, 0] @ B[:, :, i] + A[:, :, i] @ B[:, :, 0]) % p
    return C


def rtranspose(A):
    return np.transpose(A, (1, 0, 2)).copy()


def ridentity(n):
    A = np.zeros((n, n, 3), dtype=np.int64)
    A[:, :, 0] = np.eye(n, dtype=np.int64)
    return A


def intertwiner_space(left, right, p):
    n = left[0].shape[0]
    I = np.eye(n, dtype=np.int64)
    equations = np.concatenate([np.kron(A, I)-np.kron(I, B.T)
                                for A, B in zip(left, right)], axis=0) % p
    return [v.reshape(n, n) for v in kernel(equations, p)]


records = []
recovered_centralizer_basis_elements = 0
ring_basis_products = 0
for p in (3, 5, 7, 11):
    rng = random.Random(17000+p)
    # Basis multiplication, including all four radical products.
    for i in range(3):
        for j in range(3):
            expected = Q[j] if i == 0 else Q[i] if j == 0 else np.zeros((3, 3), dtype=np.int64)
            assert eq(Q[i] @ Q[j], expected, p)
            ring_basis_products += 1
    centralizer_dimensions = {}
    socles = {}
    for n in (1, 2, 3):
        N = 3*n
        regular = [np.kron(np.eye(n, dtype=np.int64), X) for X in (Qa, Qb)]
        centralizer = intertwiner_space(regular, regular, p)
        assert len(centralizer) == 3*n*n
        centralizer_dimensions[str(n)] = len(centralizer)
        for X in centralizer:
            recovered = recover_matrix(X, p)
            assert eq(reg_matrix(recovered, p), X, p)
            recovered_centralizer_basis_elements += 1
        regular_socle = len(kernel(np.concatenate(regular, axis=0), p))
        kdual_socle = len(kernel(np.concatenate([X.T for X in regular], axis=0), p))
        assert regular_socle == 2*n
        assert kdual_socle == n
        socles[str(n)] = {'R_free': regular_socle, 'ordinary_k_dual': kdual_socle}
    # Hom_R(R,R) consists exactly of multiplication matrices. Its R-action
    # by multiplication on the target has the original regular matrices.
    for action in (Qa, Qb):
        coordinates = np.column_stack([(action @ X % p)[:, 0] for X in Q])
        assert eq(coordinates, action, p)

    one = np.array([1, 0, 0], dtype=np.int64)
    a = np.array([0, 1, 0], dtype=np.int64)
    b = np.array([0, 0, 1], dtype=np.int64)
    I2 = ridentity(2)
    P = I2.copy()
    P[0, 1], P[1, 0] = a, b
    Pinv = I2.copy()
    Pinv[0, 1], Pinv[1, 0] = -a % p, -b % p
    assert eq(rmatmul(P, Pinv, p), I2, p)
    D = I2.copy()
    D[1, 1] = -one % p
    T = rmatmul(rmatmul(P, D, p), Pinv, p)
    B = rmatmul(rtranspose(Pinv), Pinv, p)
    assert eq(rmatmul(T, T, p), I2, p)
    assert eq(rmatmul(rmatmul(rtranspose(T), B, p), T, p), B, p)
    assert is_invertible(B[:, :, 0], p)

    # Scramble every k-coordinate, then recover an R-basis using only the
    # linear intertwiner equations, not the saved scrambling matrix.
    N = 6
    S0 = np.eye(N, dtype=np.int64)
    for _ in range(24):
        i, j = rng.sample(range(N), 2)
        S0[i] = (S0[i] + rng.randrange(1, p)*S0[j]) % p
    S0inv = inverse(S0, p)
    standard = [np.kron(np.eye(2, dtype=np.int64), X) for X in (Qa, Qb)]
    scrambled = [S0 @ X @ S0inv % p for X in standard]
    scrambled_T = S0 @ reg_matrix(T, p) @ S0inv % p
    solutions = intertwiner_space(scrambled, standard, p)
    assert len(solutions) == 12
    recovered_basis = None
    for attempt in range(1, 501):
        candidate = sum((rng.randrange(p)*X for X in solutions),
                        np.zeros((N, N), dtype=np.int64)) % p
        if is_invertible(candidate, p):
            recovered_basis = candidate
            break
    assert recovered_basis is not None
    for X, Y in zip(scrambled, standard):
        assert eq(X @ recovered_basis, recovered_basis @ Y, p)
    found_T = recover_matrix(inverse(recovered_basis, p) @ scrambled_T @ recovered_basis % p, p)
    C = recover_matrix(S0inv @ recovered_basis % p, p)
    Cinv = recover_matrix(inverse(reg_matrix(C, p), p), p)
    assert eq(found_T, rmatmul(rmatmul(Cinv, T, p), C, p), p)
    found_B = rmatmul(rmatmul(rtranspose(C), B, p), C, p)
    assert is_invertible(found_B[:, :, 0], p)
    assert eq(rmatmul(found_B, found_T, p),
              rmatmul(rtranspose(found_T), found_B, p), p)
    h0 = (I2+found_T)*pow(2, -1, p) % p
    h1 = (I2-found_T)*pow(2, -1, p) % p
    assert eq(rmatmul(h0, h0, p), h0, p)
    assert eq(rmatmul(h1, h1, p), h1, p)
    assert not np.any(rmatmul(h0, h1, p))
    assert np.any(h1)
    for h in (h0, h1):
        assert eq(rmatmul(found_B, h, p), rmatmul(rtranspose(h), found_B, p), p)
    # Exterior-square determinant of this O_1 involution is the sign line.
    determinant_T = (rmatmul(found_T[0:1, 0:1], found_T[1:2, 1:2], p)
                     - rmatmul(found_T[0:1, 1:2], found_T[1:2, 0:1], p)) % p
    assert eq(determinant_T[0, 0], -one, p)
    records.append({'p': p, 'centralizer_dimensions': centralizer_dimensions,
                    'socle_dimensions': socles, 'linear_basis_recovery_trials': attempt,
                    'recovered_R_rank': 2, 'coefficient_degree': 1,
                    'R_dual_and_form_invariance': 'PASS', 'exterior_square_sign': 'PASS'})

result = {
    'utc': datetime.now(timezone.utc).isoformat(timespec='seconds'),
    'model': 'GPT-6 Astra (OpenAI, ChatGPT Pro mode)',
    'agent': 'descent_groups', 'run': 'RESEARCH_SA17_FINISH-20261119',
    'scope': __doc__, 'ring_basis_products': ring_basis_products,
    'centralizer_cases': 12,
    'centralizer_basis_elements_recovered': recovered_centralizer_basis_elements,
    'free_basis_recovery_cases': 4,
    'records': records, 'result': 'PASS', 'seconds': perf_counter()-start
}
target = Path(__file__).resolve().parents[1]/'logs/C_finish_artinian_algclosed.json'
target.write_text(json.dumps(result, indent=2)+'\n')
print(json.dumps({k:v for k,v in result.items() if k not in ('scope','records')}, indent=2))
