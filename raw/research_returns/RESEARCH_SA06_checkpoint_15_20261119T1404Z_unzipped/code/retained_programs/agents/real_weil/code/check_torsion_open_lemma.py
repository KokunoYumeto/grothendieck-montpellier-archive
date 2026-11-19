#!/usr/bin/env python3
"""Exact algebra/source check for the rejected open-complement lemma.

This checks the finite polynomial data, not a numerical approximation to
singular cohomology. The cohomological calculation is proved in the note.
"""
from concurrent.futures import ThreadPoolExecutor
from datetime import datetime, timezone
from pathlib import Path
from time import perf_counter
from urllib.request import Request, urlopen
import hashlib
import json
import sympy as sp

started = datetime.now(timezone.utc).isoformat()
t0 = perf_counter()
base = Path(__file__).resolve().parents[1]
src = base / "sources"
out = base / "output"
src.mkdir(exist_ok=True)
out.mkdir(exist_ok=True)

urls = [
    ("patel_ravindra_torsion_author.pdf", "https://www.math.purdue.edu/~patel471/torsionWL.pdf"),
    ("patel_ravindra_torsion_published.pdf", "https://www.math.umsl.edu/~girivaru/torsion.pdf"),
    ("patel_ravindra_torsion_erratum.pdf", "https://www.math.purdue.edu/~patel471/torsion_erratum.pdf"),
]

def retrieve(item):
    name, url = item
    tick = perf_counter()
    result = {"name": name, "url": url}
    try:
        data = urlopen(Request(url, headers={"User-Agent": "Mozilla/5.0"}), timeout=20).read()
        if not data.startswith(b"%PDF"):
            raise ValueError("response was not a PDF")
        (src / name).write_bytes(data)
        result.update(status="downloaded", bytes=len(data), sha256=hashlib.sha256(data).hexdigest())
    except Exception as exc:
        result.update(status="not downloaded", error=f"{type(exc).__name__}: {exc}")
    result["runtime_seconds"] = perf_counter() - tick
    return result

with ThreadPoolExecutor(max_workers=3) as pool:
    downloads = list(pool.map(retrieve, urls))

check_t0 = perf_counter()
x = sp.symbols("x0:5")
q = x[0]*x[1] - x[2]*x[3]
grad = [sp.diff(q, z) for z in x]
hess = sp.hessian(q, x)
restricted = sp.expand(q.subs(x[0], 0))
coeff = sp.symbols("a0:9")
mons = [x[0]**2, x[0]*x[1], x[0]*x[2], x[0]*x[3], x[0]*x[4],
        x[2]**2, x[1]*x[2], x[2]*x[3], x[2]*x[4]]
generic = sum(a*m for a, m in zip(coeff, mons))
generic_hess = sp.hessian(generic, x)
checks = [
    {"name": "equation vanishes on the base plane", "pass": q.subs({x[0]:0, x[2]:0}) == 0},
    {"name": "gradient ideal is the four nonvertex coordinates", "pass": set(sp.groebner(grad, *x).polys[i].as_expr() for i in range(4)) == set(x[:4])},
    {"name": "quadratic rank is four over Q", "pass": hess.rank() == 4, "rank": hess.rank()},
    {"name": "unique projective singular point is the stated vertex", "pass": hess.nullspace() == [sp.Matrix([0,0,0,0,1])]},
    {"name": "quadric irreducible over Q; rank proof gives geometric irreducibility", "pass": len(sp.factor_list(q)[1]) == 1 and sp.factor_list(q)[1][0][1] == 1},
    {"name": "restriction is two distinct plane factors", "pass": restricted == -x[2]*x[3]},
    {"name": "target chart x2=1 leaves precisely x3 invertible", "pass": restricted.subs(x[2], 1) == -x[3]},
    {"name": "base smooth quadric in P3 has no projective critical point", "pass": set(grad[:4]) == {x[1],x[0],-x[3],-x[2]}},
    {"name": "all quadrics containing this plane have rank at most four", "pass": sp.expand(generic_hess.det()) == 0},
    {"name": "rank-four locus in that linear system is nonempty", "pass": hess.extract(range(4), range(4)).det() != 0},
    {"name": "degree-two Gysin matrix has zero kernel over Q", "pass": len(sp.Matrix([[2]]).nullspace()) == 0},
]
record = {
    "started_utc": started,
    "scope": "Exact polynomial geometry and one-dimensional rational Gysin matrix for the P4 counterexample; no computation of arbitrary topology or of any Chow torsion theorem.",
    "downloads": downloads,
    "equation": str(q),
    "gradient": [str(v) for v in grad],
    "checks": checks,
    "passed": sum(c["pass"] for c in checks),
    "total": len(checks),
    "algebra_runtime_seconds": perf_counter() - check_t0,
    "runtime_seconds": perf_counter() - t0,
}
(out / "torsion_open_lemma_check.json").write_text(json.dumps(record, indent=2) + "\n")
print(json.dumps(record, indent=2))
assert all(c["pass"] for c in checks)
