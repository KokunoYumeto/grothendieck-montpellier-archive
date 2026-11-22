#!/usr/bin/env python3
"""Exact polynomial identities for the standard ramified A2 MF lattice.

This certificate verifies identities, not exact-category additivity or the
ideal exact sequences, which are proved in the accompanying TeX source.
Formal differentiation is performed over QQ[p,x,z] before any specialization.
"""

from __future__ import annotations

import hashlib
import json
import time
from pathlib import Path

import sympy as sp


def main() -> None:
    start = time.perf_counter()
    p, x, z, alpha = sp.symbols("p x z alpha")
    eye2, eye4 = sp.eye(2), sp.eye(4)
    zero2 = sp.zeros(2)
    phi = sp.Matrix([[-x, -p**2], [p, z]])
    psi = sp.Matrix([[z, p**2], [-p, -x]])
    sigma = sp.diag(1, 1, -1, -1)
    D = zero2.row_join(phi).col_join(psi.row_join(zero2))
    Dprime = D.diff(p)
    g = p**3 - x*z
    T = sigma + D
    h = alpha*Dprime
    F = sigma - h
    checks = []

    def check(name: str, residual: sp.MatrixBase) -> None:
        entries = [sp.cancel(a) for a in residual]
        assert all(a == 0 for a in entries), (name, residual)
        checks.append({"identity": name, "entries": len(entries), "passed": True})

    check("phi psi = g I", phi*psi - g*eye2)
    check("psi phi = g I", psi*phi - g*eye2)
    check("D squared = g I", D*D - g*eye4)
    check("sigma D + D sigma = 0", sigma*D + D*sigma)
    check("T squared = (1+g) I", T*T - (1+g)*eye4)
    check("(T-I)(T+I) = g I", (T-eye4)*(T+eye4)-g*eye4)
    check("(T+I)(T-I) = g I", (T+eye4)*(T-eye4)-g*eye4)
    check("D Dprime + Dprime D = 3 p squared I", D*Dprime + Dprime*D-3*p**2*eye4)
    check("Dprime squared = 2 p I", Dprime*Dprime-2*p*eye4)
    check("sigma h + h sigma = 0", sigma*h+h*sigma)
    check("T F + F T = (2-3 alpha p squared) I", T*F+F*T-(2-3*alpha*p**2)*eye4)
    check("F squared = (1+2 p alpha squared) I", F*F-(1+2*p*alpha**2)*eye4)
    F_integral = F.subs(alpha, 2/(3*p**2))
    check("F anticommuter over QQ[p,x,z,p inverse]", T*F_integral+F_integral*T)
    check("F square after alpha substitution", F_integral*F_integral-(1+8/(9*p**3))*eye4)

    # Congruence calculations modulo g use a Groebner remainder over QQ.
    ideal = sp.groebner([g], x, z, p, order="lex", domain=sp.QQ)

    def mod_g(mat: sp.MatrixBase) -> sp.Matrix:
        return mat.applyfunc(lambda a: ideal.reduce(sp.expand(a))[1])

    P = eye4+D*sigma/2
    Pinv = eye4-D*sigma/2
    check("P Pinv = I modulo g", mod_g(P*Pinv-eye4))
    check("Pinv P = I modulo g", mod_g(Pinv*P-eye4))
    check("P sigma Pinv = T modulo g", mod_g(P*sigma*Pinv-T))
    check("row(p,x) phi = (0,-g)", sp.Matrix([[p,x]])*phi-sp.Matrix([[0,-g]]))
    check("row(x,p squared) psi = (-g,0)", sp.Matrix([[x,p**2]])*psi-sp.Matrix([[-g,0]]))

    # Both lifted kernel formulas used to identify the MF cokernels as ideals.
    c, d = sp.symbols("c d")
    check("first syzygy lift", phi*sp.Matrix([d,-c])-sp.Matrix([-x*d+p**2*c,p*d-z*c]))
    check("second syzygy lift", psi*sp.Matrix([-c,-d])-sp.Matrix([-z*c-p**2*d,p*c+x*d]))

    # Specialize 2=v p^e only after proving the polynomial identities.
    # These reductions are finite examples of the uniform proof, not its scope.
    v = sp.symbols("v")
    specialized = []
    for e in range(2,9):
        coefficient = sp.cancel(2-3*(v*p**(e-2)/3)*p**2)
        remainder = sp.rem(coefficient, v*p**e-2, p)
        assert remainder == 0
        specialized.append({"e":e,"alpha":"v*p**(e-2)/3","anticommutator_coefficient_remainder":str(remainder)})

    root = Path(__file__).resolve().parents[1]
    source = root/"notes"/"C_MF_Swan_transfer_proposed.tex"
    result = {
        "status":"PASS",
        "scope":"Exact symbolic identities only; exactness and Grothendieck-group relations are proved in the cited source.",
        "symbolic_ring":"QQ[p,x,z,alpha]; integer identities computed before ramified specialization",
        "identity_count":len(checks),
        "scalar_entry_count":sum(row["entries"] for row in checks),
        "identities":checks,
        "illustrative_ramification_specializations":specialized,
        "source":"notes/C_MF_Swan_transfer_proposed.tex",
        "source_sha256":hashlib.sha256(source.read_bytes()).hexdigest(),
        "runtime_seconds":time.perf_counter()-start,
    }
    output = root/"logs"/"C_finish_MF_Swan_cancellation.json"
    output.write_text(json.dumps(result,indent=2)+"\n")
    print(json.dumps(result,indent=2))


if __name__ == "__main__":
    main()
