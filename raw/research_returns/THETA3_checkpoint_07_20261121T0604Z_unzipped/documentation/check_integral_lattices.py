"""Finite checks of THETA3-C06 and THETA3-C07. No external dependencies.

For q an odd prime, enumerate isotropic projective lines in F_(q^2)^3
using F_(q^2)=F_q[sqrt(d)] with d a quadratic nonresidue.
This independently checks the only finite counting input in C06.
It does not certify Li--Zhang's theorem or the infinite set of q.
"""
from fractions import Fraction


def nonresidue(q):
    squares = {a*a % q for a in range(q)}
    return next(d for d in range(1, q) if d not in squares)


def count_isotropic_lines(q):
    d = nonresidue(q)
    field = [(a,b) for a in range(q) for b in range(q)]
    def norm(z):
        a,b = z
        return (a*a-d*b*b) % q
    # Every projective vector has exactly one representative in these charts.
    count = sum(1 for x in field for y in field if (1+norm(x)+norm(y)) % q == 0)
    count += sum(1 for y in field if (1+norm(y)) % q == 0)
    # The last chart is (0,0,1), whose norm is 1, so it contributes zero.
    return count


def multiply(a,b):
    c=[0]*(len(a)+len(b)-1)
    for i,x in enumerate(a):
        for j,y in enumerate(b):
            c[i+j]+=x*y
    return c


def derivative_at_one(coeffs):
    return sum(i*c for i,c in enumerate(coeffs))


def check_negative_sector(q):
    count=count_isotropic_lines(q)
    assert count == q**3+1, (q,count)
    m3=multiply(multiply([1,-1],[1,q]),[1,-q*q])
    over=[0,0,count,-count]
    total=[a+b for a,b in zip(m3,over)]
    expected=multiply([1,-1],[1,q-q*q,1])
    assert total==expected
    intersection=-derivative_at_one(total)
    assert intersection==q+2-q*q
    print(f'q={q}: isotropic lines={count}; Den coefficients={total}; Int={intersection}')


def check_positive_sector(a):
    coeffs=[0]*(2*a+2)
    for j in range(a+1):
        coeffs[2*j]+=1
        coeffs[2*j+1]-=1
    intersection=-derivative_at_one(coeffs)
    assert intersection==a+1
    print(f'a={a}: Den coefficients={coeffs}; Int={intersection}')


if __name__=='__main__':
    for q in (3,5,7,11):
        check_negative_sector(q)
    for a in range(7):
        check_positive_sector(a)
