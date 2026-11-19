"""Finite symbolic certificate for the explicit C.3t equations.

The mathematical proof, not this finite grid, proves non-torsion and
the all-dimension assertion.  All computations below are exact.
"""
from pathlib import Path
import json
import time
import sympy as sp

started = time.perf_counter()
checks = []
for r in range(2, 11):
    d = r + 2
    z = sp.symbols(f"z0:{r+2}")
    u = sp.symbols(f"u0:{r+1}")
    defining_power = -1 - sum(u[j]**d for j in range(r))
    F = sum(v**d for v in z)
    point_eq = sp.expand(F.subs(dict(zip(z, (*u, 1))))).subs(
        u[r]**d, defining_power)
    assert sp.expand(point_eq) == 0
    B_sub = {z[j]: u[j]*z[-1] for j in range(2, r+1)}
    B_eq = sp.expand(F.subs(B_sub)).subs(u[r]**d, defining_power)
    B_expected = z[0]**d + z[1]**d - (u[0]**d+u[1]**d)*z[-1]**d
    assert sp.expand(B_eq-B_expected) == 0
    for m in range(r-1):
        N = m+r+1
        j0 = r-m
        x = sp.symbols(f"x0:{m+1}")
        sections = [z[j]-u[j]*z[-1] for j in range(j0,r+1)]
        section_jacobian = sp.Matrix(sections).jacobian(
            [z[j] for j in range(j0,r+1)])
        assert section_jacobian == sp.eye(m+1)
        Z_eq = sp.expand(F.subs({z[j]:u[j]*z[-1]
                               for j in range(j0,r+1)})).subs(
                                   u[r]**d, defining_power)
        C = -sum(u[j]**d for j in range(j0))
        Z_expected = sum(z[j]**d for j in range(j0)) + C*z[-1]**d
        assert sp.expand(Z_eq-Z_expected) == 0
        assert C != 0 and j0 >= 2
        incidence = sum(x[k]*sections[k] for k in range(m+1))
        assert sp.expand(incidence.subs(B_sub)) == 0
        assert [sp.diff(incidence,z[j]) for j in range(j0,r+1)] == list(x)
        checks.append({"r":r,"N":N,"m":m,"j0":j0,
                       "base_dimension":j0-1,
                       "section_jacobian_determinant":1,
                       "all_exact_checks":True})

result = {"statement":"C.3t", "checked_pairs":len(checks),
          "checks":checks, "runtime_seconds":time.perf_counter()-started,
          "limits":"Finite identities only; uniform transversality and non-torsion proved in LaTeX."}
destination = Path(__file__).with_name("check_uniform_gysin_output.json")
destination.write_text(json.dumps(result,indent=2)+"\n")
print(json.dumps({key:value for key,value in result.items() if key!="checks"},indent=2))
