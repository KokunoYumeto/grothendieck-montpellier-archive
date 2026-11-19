#!/usr/bin/env python3
"""Exact arithmetic checks for the E.4j quadratic torsor.

The infinite nonexistence of a rational square root of 2 is proved by
the valuation argument in the text, not by a finite search.
"""
from fractions import Fraction
from time import perf_counter

start = perf_counter()

def add(u, v):
    return (u[0] + v[0], u[1] + v[1])

def mul(u, v):
    return (u[0]*v[0] + 2*u[1]*v[1], u[0]*v[1] + u[1]*v[0])

one = (Fraction(1), Fraction(0))
zero = (Fraction(0), Fraction(0))
t = (Fraction(0), Fraction(1))
derivative = (Fraction(0), Fraction(2))
inverse = (Fraction(0), Fraction(1, 4))
assert mul(t, t) == (Fraction(2), Fraction(0))
assert mul(derivative, inverse) == one
assert add(t, (Fraction(0), Fraction(-1))) == zero
assert mul((Fraction(0), Fraction(-1)), (Fraction(0), Fraction(-1))) == mul(t,t)

# For a + b*T over B, CRT evaluations are a+b*t and a-b*t.
# The matrix determinant is -2*t and has the displayed inverse.
det = (Fraction(0), Fraction(-2))
det_inverse = (Fraction(0), Fraction(-1,4))
assert mul(det, det_inverse) == one
discriminant = 0**2 - 4*1*(-2)
assert discriminant == 8 and discriminant > 0
assert 2**abs(-1)-1 == 1

def v2(n):
    result = 0
    while n and n % 2 == 0:
        n //= 2
        result += 1
    return result

for s in range(11):
    assert v2(5**(2**s)-1) == s+2
for m in range(3, 15):
    modulus = 2**m
    order = 2**(m-2)
    assert pow(5, order, modulus) == 1
    assert pow(5, order//2, modulus) != 1
    assert {pow(5,j,modulus) for j in range(order)} == set(range(1,modulus,4))

print('Base R=Z[1/2]; B=R[t]/(t^2-2).')
print('Exact identity (2*t)*(t/4)=1 verified in B.')
print('CRT evaluation determinant -2*t has inverse -t/4.')
print('Involution t -> -t preserves t^2=2; it has order two.')
print('Discriminant=8 is a unit over R; positive discriminant verifies two real embeddings.')
print('Finite-field negative-twist group order at q=2,n=-1: 1 (zero group).')
print('Nonexistence of a section: 2*v_2(a)=1 has no integer solution (proved in text).')
print('Cyclotomic tower: v_2(5^(2^s)-1)=s+2 verified for s=0,...,10.')
print('For m=3,...,14, 5 has exact order 2^(m-2) modulo 2^m and generates the units congruent to 1 modulo 4.')
print(f'Elapsed seconds: {perf_counter()-start:.6f}')
