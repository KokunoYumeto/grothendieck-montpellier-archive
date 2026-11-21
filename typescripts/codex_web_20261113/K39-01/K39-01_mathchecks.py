"""Finite coefficient checks for the examples R8, R13 and R20 in the mathematical notes.

The calculations use exact rational arithmetic and polynomials in ascending
coefficient order. They check the cited examples only.
"""
import math
from fractions import Fraction

def multiply(left, right, degree):
    result = [0] * (degree + 1)
    for i, a in enumerate(left):
        for j, b in enumerate(right):
            if i + j <= degree:
                result[i+j] += a*b
    return result

def compose_polynomials(outer, inner, degree):
    value = [0] * (degree + 1)
    for coefficient in reversed(outer):
        value = multiply(value, inner, degree)
        value[0] += coefficient
    return value

def main():
    degree = 5
    exp_minus_one = [0] + [Fraction(1, math.factorial(i)) for i in range(1, degree+1)]
    log_one_plus = [0] + [Fraction((-1)**(i+1), i) for i in range(1, degree+1)]
    assert compose_polynomials(log_one_plus, exp_minus_one, degree) == [0, 1, 0, 0, 0, 0]
    print("R8: log(1+(exp(t)-1)) = t modulo t^6.")

    root = [0, 1, -1, 2, -5]
    result = [a+b for a,b in zip(root, multiply(root, root, 4))]
    assert result == [0, 1, 0, 0, 0]
    print("R13: the displayed root satisfies Z+Z^2-t = 0 modulo t^5.")

    factor = [1, 0, 1]
    series = [0, 0, 1, 0, 1]
    assert multiply([0, 0, 1], factor, 4) == series
    assert series[2] == 1 and series[3] == 0 and series[4] == 1
    assert multiply(factor, [1, 0, -1, 0, 1, 0, -1], 6) == [1, 0, 0, 0, 0, 0, 0]
    print("R20: Z^2+Z^4 = Z^2(1+Z^2); the exhibited inverse unit is correct modulo Z^7.")

if __name__ == "__main__":
    main()

