"""R047: direct standard-module exterior traces and dual Jacobi--Trudi."""
from pathlib import Path
from functools import lru_cache
from itertools import permutations
from collections import Counter
from fractions import Fraction
from math import factorial
import json

HERE = Path(__file__).resolve().parent


@lru_cache(None)
def partitions(n, maximum=None):
    if n == 0:
        return ((),)
    maximum = min(n, maximum if maximum is not None else n)
    return tuple((i,)+rest for i in range(maximum,0,-1)
                 for rest in partitions(n-i,i))


def centralizer(cycle):
    return __import__("functools").reduce(
        lambda a,item: a*item[0]**item[1]*factorial(item[1]),
        Counter(cycle).items(), 1)


@lru_cache(None)
def exterior(cycle):
    # det(1+z*g_W)=prod_l(1-(-z)^l)/(1+z).
    polynomial = [1]
    for length in cycle:
        new = polynomial[:] + [0]*length
        sign = (-1)**(length+1)
        for i,value in enumerate(polynomial):
            new[i+length] += sign*value
        polynomial = new
    answer = []
    previous = 0
    for value in polynomial[:-1]:
        previous = value-previous
        answer.append(previous)
    assert polynomial[-1] == answer[-1]
    return tuple(answer)


PERMUTATIONS = tuple((p,(-1)**sum(p[i]>p[j] for i in range(4) for j in range(i+1,4)))
                     for p in permutations(range(4)))


def trace(cycle, gamma):
    values = exterior(cycle)
    answer = 0
    for p,sign in PERMUTATIONS:
        term = sign
        for i in range(4):
            degree = gamma[i]-i+p[i]
            if degree < 0 or degree >= len(values):
                term = 0
                break
            term *= values[degree]
        answer += term
    return answer


@lru_cache(None)
def invariant(s,h,j):
    gamma = (h+j+2,h+j+1,h+1,h)
    value = sum((Fraction(trace(cycle,gamma),centralizer(cycle))
                 for cycle in partitions(s)), Fraction())
    assert value.denominator == 1
    return int(value)


def main():
    cases = []
    complement_checks = 0
    trace_cases = 0
    for h in range(1,5):
        for j in range(4):
            K = 2*h+j+3
            for s in range(2,K+3):
                got = invariant(s,h,j)
                want = min(h,max(0,s-h-j-3))
                assert got == want,(s,h,j,got,want)
                cases.append({"h":h,"j":j,"rows":s,"value":got})
                trace_cases += len(partitions(s))
                if h+j+3 <= s < K:
                    q = s-h-j-3
                    tail = (4,)*h+(3,)+(2,)*j+(1,)
                    complement = tuple(4-v for v in reversed(tail+(0,)*(s-1-len(tail))))
                    complement = tuple(v for v in complement if v)
                    assert complement == (4,)*q+(3,)+(2,)*j+(1,)
                    assert invariant(s,q,j) == got
                    complement_checks += 1
            assert invariant(K,h,j) == invariant(K+1,h,j) == h
    receipt = {
        "statement":"R047 independent finite invariant profile",
        "status":"PASS",
        "method":"literal cycle exterior determinant on the standard module; four-by-four dual Jacobi-Trudi; rational class average",
        "source_imports":[],
        "coefficient_cases":len(cases),
        "cycle_trace_cases":trace_cases,
        "actual_complement_shape_checks":complement_checks,
        "scope":"finite invariant dimensions only; actual canonical rank audited through the full proof maps",
        "cases":cases
    }
    (HERE/"REPEATED_FOUR_PROFILE_INDEPENDENT_RECEIPT.json").write_text(json.dumps(receipt,indent=2)+"\n")
    print(json.dumps({k:v for k,v in receipt.items() if k!="cases"},indent=2))


if __name__ == "__main__":
    main()
