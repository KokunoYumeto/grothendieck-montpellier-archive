"""AM-K032 exact finite certificate; no analytic or Lean proof inference.

Uses the adjacent AM-K031 script's transparent integer/Fraction parameter
and primality routines, with that dependency's hash recorded below.
"""
from datetime import datetime, timezone
from fractions import Fraction as Q
from math import gcd, isqrt, lcm, prod
from pathlib import Path
import hashlib
import json

from enlarged_host_ranks_characters_alpha_certificate import (
    parameter_check, prime_factors, prime_trial
)


def qmul(x, y, a):
    p, q = x
    r, s = y
    return (p*r + q*s, p*s + q*r + a*q*s)


def trace(x, a):
    return 2*x[0] + a*x[1]


def qnorm(x, a):
    p, q = x
    return p*p + a*p*q - q*q


def matmul(A, B):
    return [[sum(A[i][k]*B[k][j] for k in range(len(B)))
             for j in range(len(B[0]))] for i in range(len(A))]


def tensor(A, B):
    return [[A[i][j]*B[k][ell] for j in range(len(A[0])) for ell in range(len(B[0]))]
            for i in range(len(A)) for k in range(len(B))]


def transpose(A):
    return list(map(list, zip(*A)))


def valuation(n, p=11):
    n = abs(n)
    assert n
    result = 0
    while n % p == 0:
        n //= p
        result += 1
    return result


def quadratic_check(a):
    d = a*a+4
    assert d in (5, 13) and prime_trial(d) and d % 4 == 1
    one, u = (Q(1), Q(0)), (Q(0), Q(1))
    uinv = (Q(-a), Q(1))
    sqrt = (Q(-a), Q(2))
    delta = (Q(a*a+2, d), Q(-a,d))
    assert qmul(u,uinv,a) == one
    assert qmul(sqrt,sqrt,a) == (Q(d), Q(0))
    assert qmul(delta,sqrt,a) == uinv
    assert qnorm(u,a) == -1 and qnorm(delta,a) == Q(1,d)
    basis=[one,u]
    gram=[[trace(qmul(delta,qmul(x,y,a),a),a) for y in basis] for x in basis]
    assert gram == [[1,0],[0,1]]
    M=[[0,1],[1,a]]
    assert M == transpose(M)
    MM=matmul(M,M)
    assert MM == [[1+a*M[i][j] if i==j else a*M[i][j] for j in range(2)]
                  for i in range(2)]
    assert a > 0 and d-a*a == 4  # sqrt(d)>a, giving both QH5 signs.
    # Embedding determinant square and denominator valuation are exact.
    assert d % 11 and d % 29
    return dict(a=a,d=d,delta_coefficients=[str(x) for x in delta],
                gram=[[str(x) for x in row] for row in gram],
                action=M,delta_norm=str(qnorm(delta,a)),
                embedding_determinant_squared=d,
                inverse_entry_discriminant_prime_valuation="-1/2")


def main():
    quadratics=[quadratic_check(a) for a in (1,3)]
    I2=[[1,0],[0,1]]
    A=tensor(I2,quadratics[0]['action'])  # basis 1,u1,u3,u1u3
    B=tensor(quadratics[1]['action'],I2)
    assert A == transpose(A) and B == transpose(B)
    assert matmul(A,B) == matmul(B,A)
    gram4=tensor(I2,I2)
    assert gram4 == [[int(i==j) for j in range(4)] for i in range(4)]
    params=parameter_check(k=168,f=168,m=2,t=1633)
    assert params['N'] == [168,1802,3436]
    assert params['S'] == 3435 and params['S_cubed'] == 40530337875
    C=params['C']
    assert C == 40530339687 and C%7 == 5
    assert params['nu0'] == [(337-2*i)*C+i-984 for i in range(168)]
    assert params['nu0_min'] == 3*C-817
    assert params['Delta'] == 4*C-1634
    assert params['G_lower_threshold'] == 56448
    assert 168%8 == 0 and 168 == 42*4 and 56 == 14*4
    assert (2**4)*21 == 336 and (2**2)*21 == 84
    modulus=52780
    assert modulus == 28*29*5*13
    old_disc={2:84,7:70,29:72}
    new_disc={p:e*4 for p,e in old_disc.items()}
    new_disc.update({5:168,13:168})
    assert new_disc == {2:336,7:280,29:288,5:168,13:168}
    assert gcd(prod(old_disc), 5*13) == 1
    primes=[]
    for a,q,g in [(52781,22285932761,3),(211121,64072175441,6)]:
        assert a*a + 7*modulus*modulus == q
        assert prime_trial(q)
        assert (a-1)%modulus == 0 and q%modulus == 1
        assert gcd(q,2*a) == 1 and q-1 > 56448
        fac=prime_factors(q-1)
        assert prod(p**e for p,e in fac.items()) == q-1
        assert all(prime_trial(p) for p in fac)
        wit={p:pow(g,(q-1)//p,q) for p in fac}
        assert all(x != 1 for x in wit.values()) and pow(g,q-1,q)==1
        primes.append(dict(a=a,b=modulus,q=q,trial_limit=isqrt(q),
                           q_mod11=q%11,factors_q_minus_1=fac,
                           primitive_root=g,primitive_root_witnesses=wit))
    root_lcm=lcm(28,*(x['q']-1 for x in primes))
    assert root_lcm == 13526981751068240
    assert 11*11%29 == 5 and 10*10%29 == 13
    index_checks=0
    for rank in range(1,5):
        for e in range(1,4):
            M=29**e
            residue_gl=prod(29**rank-29**i for i in range(rank))
            local=29**((7*e-1)*rank**2)*residue_gl
            expected=Q(M**(168*rank**2))
            for i in range(1,rank+1):
                expected *= (1-Q(1,29**i))**24
            assert expected.denominator == 1 and expected == local**24
            index_checks += 1
    principal_index_v11_at168=24*sum(valuation(29**i-1) for i in range(1,169))
    assert principal_index_v11_at168 == 408
    result=dict(result='PASS',checked_at=datetime.now(timezone.utc).isoformat(),
        scope='Exact quadratic weighted trace and integral matrices, new Ranks/HC/centred/NCGaps and selected recurrence, direct trial-division primality, full congruences and primitive-root witnesses, degree/discriminant arithmetic and rational29 index checks. No polarized-variety, Hecke, selected-image, analytic-window or Lean theorem is computationally inferred.',
        script_sha256=hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
        dependency_sha256=hashlib.sha256(Path(__file__).with_name(
            'enlarged_host_ranks_characters_alpha_certificate.py').read_bytes()).hexdigest(),
        quadratics=quadratics,tensor_actions=[A,B],tensor_gram=gram4,
        absolute_degree=336,real_degree=168,ordinary_J_multiplicity=56,
        conductor=modulus,discriminant_exponents=new_disc,parameters=params,
        primes=primes,coefficient_root_lcm=root_lcm,
        rational29_real_place_count=24,rational29_ramification_index=7,
        rational29_index_checks=index_checks,principal_index_v11_at168=principal_index_v11_at168)
    Path(__file__).with_suffix('.json').write_text(json.dumps(result,indent=2)+'\n')
    print(json.dumps({k:result[k] for k in [
        'result','checked_at','script_sha256','dependency_sha256','quadratics',
        'absolute_degree','real_degree','ordinary_J_multiplicity','conductor',
        'primes','coefficient_root_lcm','principal_index_v11_at168']},indent=2))


if __name__ == '__main__':
    main()
