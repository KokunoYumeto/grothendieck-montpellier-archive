#!/usr/bin/env python3
"""Exact replay for the formal-character countermodel PNEW-014.

The all-n claims are proved in trace_index_obstruction.tex. This verifier
checks the construction in n=10,12,14, complete periodic wave blocks, the
positive-mask tail inequalities, and representative exact ambient bounds.
No invariant algebra is constructed or claimed.
"""
from __future__ import annotations

import json
from math import comb, isqrt
from pathlib import Path


def parameters(n: int) -> dict[str, int]:
    assert n >= 10 and n % 2 == 0
    A = n * n
    D = n**3 - 3 * n * n + 3
    E = 2 * comb(n, 3) + 1
    S = isqrt(n)
    S += S * S != n
    L = 1 << (n - 2)
    r = (L - A - 2) // 2
    return dict(n=n, A=A, D=D, E=E, S=S, L=L, M=2*L,
                r=r, a=r//2, dE=E+1-A, dD=D+1-A,
                K=D-A-2*S)


def polynomial_q(s: int, E: int, dE: int) -> int:
    """Coefficient of (1-t^dE)/(1-t)^(E+1), for s>=0."""
    return comb(s+E, E) - (comb(s-dE+E, E) if s >= dE else 0)


def q0_coefficients(end: int, D: int, K: int, S: int) -> list[int]:
    """Exact O(end) recurrence for t^S(1+t)^K/(1-t)^D.

    If U=(1+t)^K/(1-t)^D, then
    (1-t^2) U' = ((D+K)+(D-K)t) U.
    """
    u = [1]
    if end >= 1:
        u.append(D+K)
    for j in range(1, max(1, end-S)):
        numerator = (D+K)*u[j] + (D-K+j-1)*u[j-1]
        assert numerator % (j+1) == 0
        u.append(numerator//(j+1))
    return [0 if s < S else u[s-S] for s in range(end+1)]


def wave(s: int, r: int, L: int, which: str) -> int:
    if s < r:
        return 0
    j, rem = divmod(s-r, L)
    if rem not in (0, 2):
        return 0
    seq = (1, -1) if which == 'G' else (1, 2, 1, -1, -2, -1)
    return (1 if rem == 0 else -1) * seq[j % len(seq)]


def verify(n: int) -> dict:
    p = parameters(n)
    A, D, E, S = (p[k] for k in ('A', 'D', 'E', 'S'))
    L, M, r, a = (p[k] for k in ('L', 'M', 'r', 'a'))
    dE, dD, K = (p[k] for k in ('dE', 'dD', 'K'))
    assert E >= 3 and E+1 <= D and S < dE and 0 < K < D
    assert A+2*(S-1) < L and r >= 2*S and a >= 1 << (n-5)
    assert r-S >= a and D-1 >= E and dD > S+K
    assert D+1 < n**3
    assert E % 2 == D % 2 == 1 and A % 2 == 0
    assert E+1-dE == D-2*S-K == L-2-2*r == A
    q = lambda s: polynomial_q(s, E, dE)
    N = q(a)
    C = N + ((1-N) % 3)
    h = (C-1)//3
    B = sum(q(j) for j in range(1, S))
    assert C % 3 == 1 and N <= C <= N+2
    assert B == comb(E+S, E+1)-1
    assert (B+1)*(E+1) == S*q(S)
    assert q(S)-B-2 > 0
    assert q(r) >= 2*N

    end = 3*M+r+2
    q0 = q0_coefficients(end, D, K, S)
    # Independent literal binomial expansion at representative degrees.
    q0_samples = sorted({0, S-1, S, S+1, a, r, dD, end})
    for s in q0_samples:
        direct = sum(comb(K, j)*comb(s-S-j+D-1, D-1)
                     for j in range(min(K, s-S)+1)) if s >= S else 0
        assert q0[s] == direct
    assert q0[r] >= comb(r-S+D-1, D-1) >= comb(a+E, E) >= N >= h+1
    assert all(q0[s+1] >= q0[s] for s in range(end))

    negative_constituent_residue = r+2
    jconst = -sum(q(j) for j in range(1, S)
                  if (negative_constituent_residue-j) % (A+2*j) == 0)
    assert wave(negative_constituent_residue, r, L, 'G') == -1
    off_residue_value = N + jconst - C
    assert off_residue_value <= 0

    # q(X+dD) has positive nonconstant coefficients by product dominance;
    # these are its smallest product constants and remaining constant margin.
    assert dD-dE+1 > 0 and dD-S-K+1 > 0
    assert q(dD)-B-2 > 0

    ambient_points = {0, 1, S-1, S, S+1, a, r, r+2,
                      r+L, r+L+2, dD, end}
    minimum_c = None
    ambient_checks = []
    Bseq = [1]
    for s in range(1, end+1):
        numerator = Bseq[-1]*(s+E)
        assert numerator % s == 0
        Bseq.append(numerator//s)
    for s in range(end+1):
        qs = Bseq[s] - (Bseq[s-dE] if s >= dE else 0)
        js = -sum(q(j) for j in range(1, S)
                  if s >= j and (s-j) % (A+2*j) == 0)
        tg, tf = (wave(s, r, L, w) for w in ('G', 'F'))
        assert abs(tg) <= 1 and abs(tf) <= 2
        assert (tf-tg) % 3 == 0
        t0 = (tf-tg)//3
        assert abs(t0) <= 1
        cs = q0[s]+t0-h*tg
        gs = qs+js+C*tg
        fs = qs+js+3*q0[s]+tf
        assert cs >= 0 and fs == gs+3*cs and gs >= 0
        if 1 <= s < S:
            assert fs == gs == cs == 0
        elif s == 0:
            assert fs == gs == 1 and cs == 0
        else:
            assert fs > 0 and gs > 0
        minimum_c = cs if minimum_c is None else min(minimum_c, cs)
        if s in ambient_points:
            ambient = comb(n*s+n**3-1, n**3-1)
            assert fs <= ambient
            ambient_checks.append(dict(s=s, F_bits=fs.bit_length(),
                                       ambient_bits=ambient.bit_length()))

    # Explicit padding budget for the all-degree injection.
    assert 2*S+4 <= n*S and 6 <= n*S
    return dict(status='PASS', parameters=p,
                C_decimal=str(C), C_bits=C.bit_length(), C_mod_3=C % 3,
                checked_actual_degrees=[0, end],
                checked_degrees_count=end+1,
                auxiliary_strict_index_lower_bound=a,
                tensor_model_saturation_index=S-1,
                tensor_model_positivity_upper_bound=dD,
                negative_constituent_residue=negative_constituent_residue,
                negative_constituent_value_at_a=str(off_residue_value),
                minimum_c_in_checked_range=minimum_c,
                q0_independent_binomial_checks=q0_samples,
                ambient_checks=ambient_checks,
                tail_positivity_inequalities_verified=True,
                functional_equation_exponents_verified=True,
                scope='Formal rational characters, not invariant algebras.')


def main() -> None:
    cases = [verify(n) for n in (10, 12, 14)]
    result = dict(status='PASS', finding='PNEW-014', cases=cases,
                  total_checked_degrees=sum(c['checked_degrees_count'] for c in cases),
                  proof='trace_index_obstruction.tex',
                  scope='Does not identify G with the actual auxiliary B_n.')
    output = Path(__file__).resolve().parents[1] / 'certificates' / 'trace_index_obstruction.json'
    output.write_text(json.dumps(result, indent=2)+'\n')
    print(json.dumps(dict(status='PASS', cases=len(cases),
                          checked_degrees=result['total_checked_degrees'],
                          certificate=str(output)), indent=2))


if __name__ == '__main__':
    main()
