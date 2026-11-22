"""Finite matrix certificate for the unincluded all-prime flat draft."""
from pathlib import Path
from time import perf_counter
import json
import sympy as s
from sympy.matrices.normalforms import smith_normal_form

start = perf_counter()
rows = []
for p in (2, 3, 5, 7, 11):
    n = p-1
    C = s.zeros(n)
    for j in range(n-1):
        C[j+1, j] = 1
    for i in range(n):
        C[i, n-1] = -1
    assert C**p == s.eye(n)
    assert sum((C**i for i in range(p)), s.zeros(n)) == s.zeros(n)
    a, b = s.zeros(1, n), s.zeros(n, 1)
    a[0, n-1], b[0, 0] = 1, 1
    T0, U = s.zeros(p), s.zeros(p)
    T0[0, 0] = 1
    T0[1:, 1:] = C
    U[0, 1:], U[1:, 0] = a, b
    def derivative_power(r):
        return sum((T0**i * U * T0**(r-1-i) for i in range(r)), s.zeros(p))
    assert derivative_power(p) == s.zeros(p)
    N0 = sum((T0**i for i in range(p)), s.zeros(p))
    assert N0 == s.diag(p, *([0]*n))
    assert (T0-s.eye(p)).rank() == n
    S = smith_normal_form(C-s.eye(n), domain=s.ZZ)
    smith = [abs(int(S[i, i])) for i in range(n)]
    assert smith == [1]*(n-1)+[p]
    beta_norm = sum((derivative_power(j) for j in range(1, p)), s.zeros(p))
    assert int((beta_norm[0, 1:] * b)[0]) == 1
    twists = []
    for r in range(1, p):
        Tr, Ur = T0**r, derivative_power(r)
        # Differentiate sum_{j=0}^{p-1}(T^r)^j directly, not by its invariance.
        Nr = sum((sum((Tr**i * Ur * Tr**(j-1-i) for i in range(j)),
                      s.zeros(p)) for j in range(1, p)), s.zeros(p))
        assert Nr == beta_norm
        beta0 = int(sum(Ur[i, 0] for i in range(1, p))) % p
        beta1 = int((Nr[0, 1:] * b)[0]) % p
        assert beta0 == r and beta1 == 1
        twists.append({'r': r, 'beta0': beta0, 'beta1': beta1,
                       'b_squared': beta0*beta1 % p,
                       'z_minus_1_parity': int(beta0*beta1 % p == 1)})
    assert sum(x['z_minus_1_parity'] for x in twists) == 1
    rows.append({'prime': p, 'rank_Cp_witness': p,
                 'cyclotomic_difference_Smith_diagonal': smith,
                 'Tate_dimensions': [1, 1], 'normalizer_twists': twists,
                 'induced_detector': 1})

report = {'status': 'PASS',
          'scope': 'Exact integer matrices, cyclic Tate kernels/norm image, Smith invariants, all normalizer twists for p=2,3,5,7,11; this does not replace exact-sequence additivity proof.',
          'draft_ids': ['C:cyclic_linear_Bockstein',
                        'C:unramified_flat_squarezero_allprimes'],
          'witnesses': rows, 'runtime_seconds': round(perf_counter()-start, 6)}
root = Path(__file__).resolve().parents[1]
(root/'logs/C_finish_cyclic_flat_probe.json').write_text(json.dumps(report, indent=2)+'\n')
print(json.dumps(report, indent=2))
