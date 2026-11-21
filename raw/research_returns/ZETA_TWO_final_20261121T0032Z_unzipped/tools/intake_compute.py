"""Exact and numerical checks for IA06--IA08; no GRH is used.

The h-minus certificate is the determinant of an explicitly supplied
integer multiplication matrix. Bareiss elimination is implemented below
using Python integers and checked against sympy.Matrix.det().
Floating-point gamma values are illustrative numerical evaluations only.
"""
from fractions import Fraction
from pathlib import Path
import math
import sympy as sp
import mpmath as mp


def bareiss(matrix):
    a = [row[:] for row in matrix]
    n = len(a)
    sign, previous = 1, 1
    for k in range(n - 1):
        if a[k][k] == 0:
            pivot = next(j for j in range(k + 1, n) if a[j][k])
            a[k], a[pivot] = a[pivot], a[k]
            sign = -sign
        p = a[k][k]
        for i in range(k + 1, n):
            for j in range(k + 1, n):
                num = a[i][j] * p - a[i][k] * a[k][j]
                assert num % previous == 0
                a[i][j] = num // previous
        for i in range(k + 1, n):
            a[i][k] = 0
        previous = p
    return sign * a[-1][-1]


p, primitive = 23, 5
residues = [pow(primitive, j, p) for j in range(p - 1)]
assert sorted(residues) == list(range(1, p))
assert pow(primitive, 11, p) == p - 1
t = [residues[j] - residues[j + 11] for j in range(11)]
matrix = [[0] * 11 for _ in range(11)]
for col in range(11):
    for exponent, coefficient in enumerate(t):
        row = exponent + col
        sign = 1
        if row >= 11:
            row -= 11
            sign = -1
        matrix[row][col] += sign * coefficient
d1 = bareiss(matrix)
d2 = int(sp.Matrix(matrix).det(method="berkowitz"))
assert d1 == d2 == -3072 * 23**10
product_l0 = Fraction(-1, 23) ** 11 * d1
hminus = Fraction(46, 2**11) * product_l0
assert hminus == 3

# Independent character-coefficient arithmetic for the cyclic quartic CM type.
a = [2, 1, 0, 1]
I = sp.I
coeffs = [sp.simplify(sum(a[j] * I ** (-k*j) for j in range(4)) / 4)
          for k in range(4)]
assert coeffs == [1, sp.Rational(1, 2), 0, sp.Rational(1, 2)]

mp.mp.dps = 80
ga = mp.loggamma(mp.mpf(1)/5) - mp.loggamma(mp.mpf(4)/5)
gb = mp.loggamma(mp.mpf(2)/5) - mp.loggamma(mp.mpf(3)/5)
h5 = mp.log(5)/2 - (3*ga + gb)/2
phi = (1+mp.sqrt(5))/2
l15 = 2*mp.log(phi)/mp.sqrt(5)

lines = [
    "IA07 exact integer certificate",
    f"primitive root modulo 23: {primitive}",
    f"residues 5^j mod 23, j=0,...,21: {residues}",
    f"T coefficients in ascending order: {t}",
    "multiplication matrix in 1,x,...,x^10 modulo x^11+1:",
    *[" ".join(map(str, row)) for row in matrix],
    f"Bareiss determinant: {d1}",
    f"Independent Berkowitz determinant: {d2}",
    f"product of odd-character L(0,chi): {product_l0}",
    f"relative class number h-minus: {hminus}",
    "Total class number also uses Miller Theorem 1.1: h-plus=1.",
    "", "IA06 exact character arithmetic and numerical gamma evaluation",
    f"coefficients of characters 1,chi,chi^2,chi^3: {coeffs}",
    f"Q(zeta5) stable Faltings height: {mp.nstr(h5, 70)}",
    "", "IA08 illustrative numerical evaluation",
    f"L(1,chi5) = 2log(phi)/sqrt5: {mp.nstr(l15, 70)}",
    f"phi^4: {mp.nstr(phi**4, 70)}",
    "Numerical gamma/logarithm digits are evaluations, not formal interval certificates.",
]
target = Path(__file__).with_name("intake_computation_results.txt")
target.write_text("\n".join(lines) + "\n")
print(target.read_text())
