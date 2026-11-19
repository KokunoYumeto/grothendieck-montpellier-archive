#!/usr/bin/env python3
"""Finite data checks and reproducible ledger for the generic Walker example."""
import csv
from datetime import datetime, timezone
import json
from pathlib import Path
import platform
import time
import sympy as s

BASE = Path(__file__).resolve().parents[1]
start = time.perf_counter()
monomials = [(a,b,2-a-b) for a in range(3) for b in range(3-a)]
assert len(monomials) == 6
ncoeff = 2 * 3 * 2 * len(monomials)
assert ncoeff == 72
row1, row2 = (1,2,0), (1,0,2)
minor = tuple(a+b for a,b in zip(row1,row2))
assert minor == (2,2,2)
syzygies = [tuple(a+b for a,b in zip(minor,row)) for row in (row1,row2)]
assert syzygies == [(3,4,2),(3,2,4)]
h,l,t = s.symbols("h l t")
degree = s.expand((h+2*l)**3).coeff(h,1).coeff(l,2)
assert degree == 12
a2, a4 = -(1+t), t
b2, b4, b6, b8 = 4*a2, 2*a4, s.Integer(0), -a4**2
c4 = s.expand(b2**2-24*b4)
disc = s.factor(-b2**2*b8-8*b4**3-27*b6**2+9*b2*b4*b6)
assert s.expand(disc-16*t**2*(1-t)**2) == 0
j = s.factor(c4**3/disc)
assert s.cancel(j-256*(1-t+t**2)**3/(t**2*(1-t)**2)) == 0
assert s.diff(j,t) != 0
assert s.limit(t**2*j,t,0) == 256
result = {
    "purpose": "Finite defining-data verification only; Hilbert transfer and Chow nonvanishing are proved in prose",
    "utc": datetime.now(timezone.utc).isoformat(),
    "python": platform.python_version(),
    "sympy": s.__version__,
    "quadratic_monomials": monomials,
    "independent_coefficients": ncoeff,
    "minor_tridegree": minor,
    "Hilbert_Burch_syzygy_tridegrees": syzygies,
    "first_row_zero_scheme_degree": int(degree),
    "Legendre_discriminant": str(disc),
    "Legendre_c4": str(c4),
    "Legendre_j": str(j),
    "j_pole_order_at_zero": 2,
    "j_pole_leading_coefficient": 256,
    "checks_passed": True,
    "seconds": time.perf_counter()-start,
}
(BASE/"output"/"check_explicit_walker.json").write_text(json.dumps(result,indent=2)+"\n")
who = "GPT-6 Astra (OpenAI); research run RESEARCH_SA06; child cycles; no independent-model claim"
rows = [[
    "E.3r",
    "The displayed 72-parameter geometric generic Enriques pencil times an independent Legendre elliptic curve has a nonzero order2 ordinary-AJ-zero cycle detected by Walker",
    "Proved",
    "explicit_walker_counterexample.tex, paragraph E.3r",
    "OttemSuzuki2020 Lemmas2.3-2.7 and Theorem3.1 congruence(1); proper relative Hilbert schemes; integral transport; hard Lefschetz; Schoen2000Exterior Theorem0.2; Suzuki2020Remark Theorem1.1 and Proposition3.1; E.3g,j",
    "14:24-39; LeadE4",
    "Fully specified field and matrix with72 independent coefficients and independent Legendre parameter. Gamma is any representative of the least positive multiple m of the transported nonalgebraic class; m is even. No numerical gamma coefficients or numerical m claimed. Generic-cycle specialization introduces no norm or denominator; z=gamma times the displayed nonzero2-torsion divisor."
]]
with (BASE/"explicit_walker_results.csv").open("w",newline="") as f:
    w=csv.writer(f)
    w.writerow(["id","statement","status","where_proved","depends_on","manuscript_pages_settled","notes"])
    w.writerows(rows)
events = [
    ["E.3r","2026-11-19","GPT-6 Astra (OpenAI); research run RESEARCH_SA06; root independent targeted review","independent re-proof",
     "Root independently passed the complete generic construction and corrected all-embeddings argument; independently visually checked Schoen Theorem0.2 printedp177 and reopened Suzuki Theorem1.1 and Proposition3.1. No numerical minimal m or gamma coordinates claimed."],
    ["E.3r","2026-11-19","GPT-6 Astra (OpenAI); research run RESEARCH_SA06; child frobenius independent targeted review","independent re-proof",
     "Frobenius reopened Schoen Theorem0.2 primaryp177 and Suzuki Theorem1.1. Checked no exclusion of2, Hilbert properness and integral multiplicities, parity/minimal even m, gamma descent, Deligne products and Walker torsion injectivity. Passed. Suggested intrinsic mod2 etale-cycle-class comparison so the same gamma works for every complex embedding; incorporated."],
    ["E.3r","2026-11-19",who,"used and rechecked in this run",
     "Reopened OttemSuzuki2020 authorpp6-8 exact parity congruence and beta construction, plus Lemmas2.3-2.4 and2.7. Opened full Suzuki2020Remark arXivv3 Theorem1.1 p2, Proposition3.1 pp5-6; full Schoen2000Exterior primary Theorem0.2 p177 downloaded after web403."],
    ["E.3r","2026-11-19",who,"targeted proof check",
     "Verified all curve Hilbert components meeting the geometric generic fibre dominate the coefficient base and are proper over it, so integral one-cycles specialize to the bad fibre with both divisor degrees preserved. Global relative first-row divisor is Cartier on the smooth family. Parallel transport produces a parity-violating integral Hodge class."],
    ["E.3r","2026-11-19",who,"targeted proof check",
     "Hard Lefschetz and H2O=0 give finite-index algebraic H4 lattice. Minimal m is even and gamma/2 is nonzero in that lattice tensorQ/Z. Hilbert-component descent fixes gamma over k. Schoen injectivity gives nonzero2-torsion product, Deligne tensor factorization gives AJzero, and Suzuki torsion Walker injectivity gives nonzero Walker image."],
    ["E.3r","2026-11-19",who,"computation or formal certificate",
     "check_explicit_walker.py checked72 coefficient variables,6 degree2 monomials, minor/syzygy tridegrees, first-row degree12, Legendre discriminant,c4,j and its order2 pole. This does not computationally certify the Chow group or generic nonvanishing; those are proved with opened inputs."],
    ["E.3r source preservation","2026-11-19",who,"computation or formal certificate",
     "fetch_explicit_walker_sources.py downloaded Suzuki2020Remark376431bytes and Schoen2000Exterior247371bytes, withSHA256 and successful text extraction. Web direct publisher opens returned403; direct download succeeded. Two initial JavaScript template writes failed before any mutation due to TeX backticks; corrected write then succeeded."],
]
with (BASE/"explicit_walker_CHECK_EVENTS.tsv").open("w",newline="") as f:
    w=csv.writer(f,delimiter="\t")
    w.writerow(["statement_id","date","who_model_effort_run","type","outcome"])
    w.writerows(events)
print(json.dumps(result,indent=2))

