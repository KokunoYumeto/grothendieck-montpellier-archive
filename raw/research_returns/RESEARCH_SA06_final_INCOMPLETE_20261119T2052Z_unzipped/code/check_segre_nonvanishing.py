"""Finite symbolic checks for C.3s; no computed assertion of Chow non-torsion."""
from pathlib import Path
import json
import time
import sympy as sp

start = time.perf_counter()
root = Path(__file__).resolve().parents[1]
h, H = sp.symbols("h H")
cases = []
for N in range(2, 13):
    for r in range(1, N):
        m = N-1-r
        basis = sp.groebner([h+H, h**(m+1)], h, H, order="lex")
        reduced = basis.reduce(H**(m+1))[1]
        assert reduced == 0
        # Direct division by h+H gives the exact relation in the quotient.
        remainder = sp.rem(h**(m+1), h+H, h)
        assert sp.expand(remainder-(-H)**(m+1)) == 0
        d = r+2
        u = sp.symbols(f"u0:{r}")
        w, eta = sp.symbols("w eta")
        fermat = sum(x**d for x in u)+w**d+1
        witness_remainder = sp.rem(fermat, w**d+1+sum(x**d for x in u), w)
        origin_remainder = sp.rem(1+eta**d, eta**d+1, eta)
        assert witness_remainder == origin_remainder == 0
        cases.append({"N": N, "r": r, "m": m, "CY_degree": d,
                      "cone_dimension": m+r+1,
                      "quotient_denominator_exponent": m+1,
                      "denominator_source_codimension": r-m-1,
                      "elimination_remainder": str(remainder),
                      "witness_equation_error": str(witness_remainder)})
output = {"scope": "all 66 pairs with 2<=N<=12 and1<=r<N; exact symbolic polynomial arithmetic",
          "cases": cases, "pair_count": len(cases),
          "limitation": "The general projective-bundle formula, differential-form obstruction, strict-local Chow injection and non-torsion are proved in the paper.",
          "runtime_seconds": time.perf_counter()-start}
(root / "code" / "check_segre_nonvanishing_output.json").write_text(json.dumps(output, indent=2)+"\n")
print(json.dumps({k:v for k,v in output.items() if k!="cases"}, indent=2))
