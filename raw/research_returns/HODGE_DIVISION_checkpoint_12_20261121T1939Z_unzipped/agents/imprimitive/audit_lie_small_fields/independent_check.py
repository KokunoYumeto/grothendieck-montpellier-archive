#!/usr/bin/env python3
"""Independent exact arithmetic for peer review of D-BI-20.

No author code is imported.  The published degree formulae are inputs;
this verifies their stated specializations and the ceiling comparisons.
"""
from fractions import Fraction
from pathlib import Path
from math import gcd
import hashlib
import json

def prime_power(n):
    p = next((d for d in range(2, n + 1) if n % d == 0), None)
    while n % p == 0:
        n //= p
    return n == 1

def allowed(q):
    # ceil(e(q-9)/(4q)), written using integer quotient and remainder.
    bound = 6*q // (q-27)
    result = []
    for e in range(3, bound+1):
        quotient, remainder = divmod(e*(q-9), 4*q)
        if 12*(quotient + bool(remainder)) <= 2*e+6:
            result.append(e)
    return result

def classical(q):
    return {
        "linear_rank3": q*q+q-1,
        "symplectic_rank2": Fraction(q*q-1, 2) if q % 2 else
            Fraction((q*q-1)*(q*q-q), 2*(q+1)),
        "odd_orthogonal_rank3": q**4+q*q-1,
        "plus_orthogonal_rank4": (q*q+1)*(q**3+q)-2,
        "minus_orthogonal_rank4": q*(q**4+1)-1,
        "unitary_even_rank4": (q-1)*(q*q+1),
        "unitary_odd_rank3": q*(q-1),
    }

def exceptional(q):
    # Closed forms for Phi_j(q), independent of the author's recursion.
    phi1, phi2 = q-1, q+1
    phi3, phi4, phi6 = q*q+q+1, q*q+1, q*q-q+1
    phi7, phi8 = sum(q**i for i in range(7)), q**4+1
    phi9, phi12 = q**6+q**3+1, q**4-q*q+1
    phi14, phi18 = sum((-q)**i for i in range(7)), q**6-q**3+1
    phi20, phi24 = q**8-q**6+q**4-q*q+1, q**8-q**4+1
    values = {
        "G2": q**3 + (1 if q % 3 == 1 else -1),
        "3D4": q*phi12,
        "F4": phi3*phi6*phi12 if q % 2 else
            Fraction(q*phi1**2*phi3**2*phi8, 2),
        "2E6": q*phi8*phi18,
        "E6": q*phi8*phi9,
        "E7": q*phi7*phi12*phi14,
        "E8": q*phi4**2*phi8*phi12*phi20*phi24,
    }
    if q == 32:
        values.update({"Suzuki": 124,
                       "large_Ree": 124*(q+1)**2*(q*q-q+1)})
    return values

qs = [n for n in range(28,47) if prime_power(n)]
assert qs == [29,31,32,37,41,43]
rows = []
for q in qs:
    assert (q+9)**2 <= 81*q  # c(q)=9/q exactly.
    degrees = allowed(q)
    upper = max(degrees)
    lower = Fraction(q*q-1,2)
    c, ex = classical(q), exceptional(q)
    assert all(v >= lower > upper for v in c.values())
    assert all(v > upper for v in ex.values())
    assert all(v >= q*(q-1) for k,v in ex.items() if k != "Suzuki")
    a = (q-1)//gcd(2,q-1)
    assert a*a > upper
    rows.append({"q":q,"allowed_degrees":degrees,"maximum":upper,
                 "classical_minimum_rank_values":{k:str(v) for k,v in c.items()},
                 "exceptional_minimum_values":{k:str(v) for k,v in ex.items()},
                 "PSL2_projective_lower":a,"tensor_square_lower":a*a})
assert [r["maximum"] for r in rows] == [87,45,33,21,15,15]
assert not set(allowed(37)).intersection({1,18,19,36,37,38})
assert all((q-1)//2 > max(allowed(q)) for q in [41,43])
assert [x for x in range(29) if (x*x+1) % 29 == 0] == [12,17]
assert not [x for x in range(31) if (x*x+1) % 31 == 0]

proof = Path(__file__).parents[2] / "g34_eightfolds/bireflection/lie_small_fields_section.tex"
result = {"status":"PASS","scope":"independent exact arithmetic, not a reconstruction of published classification tables",
          "author_code_imported":False,
          "proof_sha256":hashlib.sha256(proof.read_bytes()).hexdigest(),
          "fields":rows,"degree37_intersection":[],
          "minus_one_roots_mod29":[12,17],"minus_one_roots_mod31":[]}
target = Path(__file__).with_suffix(".json")
target.write_text(json.dumps(result,indent=2)+"\n")
print(json.dumps({"status":"PASS","fields":qs,"upper_bounds":[r["maximum"] for r in rows],"proof_sha256":result["proof_sha256"]}))
