"""Record exact degree identities and the C.1n proof/source audit.

This calculation checks types only.  The motive-theoretic argument is in
endpoint_image.tex; no finite enumeration is offered as its proof.
"""
from pathlib import Path
import csv
import datetime
import hashlib
import json
import time
import urllib.request

import sympy as sp

ROOT = Path(__file__).resolve().parents[1]
t0 = time.perf_counter()
d, j, r = sp.symbols("d j r", integer=True)
s = d - j
codimension = s + r
cohomological_target_degree = 2*j + 2*codimension - 2*d
assert sp.expand(codimension - (d+r-j)) == 0
assert sp.expand(cohomological_target_degree - 2*r) == 0
assert sp.expand((d+r-j) + (j-r) - d) == 0

url = "https://epub.uni-regensburg.de/26642/1/jannsen10.pdf"
pdf = ROOT / "sources/Jannsen1992.pdf"
if not pdf.exists():
    with urllib.request.urlopen(url, timeout=45) as response:
        pdf.write_bytes(response.read())
data = pdf.read_bytes()
assert data[:4] == b"%PDF"
certificate = {
    "date_utc": datetime.datetime.now(datetime.timezone.utc).isoformat(),
    "elapsed_seconds": time.perf_counter()-t0,
    "claim": "C.1n: degree identities only; proof is in endpoint_image.tex",
    "source_dimension": str(d),
    "source_cycle_codimension": str(j),
    "functional_cycle_codimension": str(s),
    "correspondence_codimension": str(codimension),
    "target_cohomology_degree": str(sp.expand(cohomological_target_degree)),
    "numerical_motive_morphism_convention":
        "Hom(h(Y)(j),h(X)(r))=CH^(dim(Y)+r-j)(Y x X)_num,Q",
    "source": {
        "url": url,
        "local_file": str(pdf),
        "bytes": len(data),
        "sha256": hashlib.sha256(data).hexdigest(),
        "opened_exact_locator": "Theorem 1, printed pp.448-449",
    },
}
(ROOT / "output/check_endpoint_image.json").write_text(
    json.dumps(certificate, indent=2)+"\n")

with (ROOT / "endpoint_results.csv").open("w", newline="") as stream:
    writer = csv.writer(stream)
    writer.writerow(["id", "statement", "status", "where_proved", "depends_on",
                     "manuscript_pages_settled", "notes"])
    writer.writerow([
        "C.1n",
        "The universal endpoint image criterion is equivalent to standard D; for a fixed target it is equivalent to D and vanishing of its Griffiths kernel, over any algebraically closed field with a fixed Weil cohomology",
        "Proved", "endpoint_image.tex, paragraph C.1n",
        "Jannsen1992 Theorem1 pp448-449; Poincare duality; endpoint numerical=algebraic with Q coefficients; C.1k",
        "14:46",
        "Exact equivalences, not proofs of D. Rational cycle coefficients, characteristic-zero Weil-cohomology coefficient field. Necessity uses an arbitrary numerically trivial source cycle as a functional. Sufficiency uses whole numerical motives and faithful graded realization under D on all products; no algebraic Kunneth projectors are assumed. Interior universal target codimensions are refuted over C by C.1k, with no positive-characteristic transfer claimed.",
    ])

events = [
    ("used and rechecked in this run",
     "Re-read the exact K14-04 manuscript14:46 source/degree-shift quantifiers and reopened Jannsen1992 Theorem1 pp448-449. The criterion allows arbitrary source varieties, source codimensions and correspondence degree shifts."),
    ("targeted proof check",
     "Checked the source-functional counterexample: a numerically zero class a in codimension s, j=d-s, Gamma=a times h^r, zero on all algebraic inputs and nonzero on H^(2j) by Poincare duality."),
    ("targeted proof check",
     "Checked sufficiency under universal D on products: faithful full graded Betti realization of numerical motives, semisimple image projector p=fg, beta=p beta, numerical preimage and endpoint numerical-to-algebraic isomorphism. This uses no algebraic Kunneth projector."),
    ("code/experiment",
     "Ran code/check_endpoint_image.py; symbolic correspondence codimension, cohomological target degree and motive-shift identities all pass. Downloaded the opened Jannsen PDF and saved its hash in output/check_endpoint_image.json. Finite computation is not asserted as a proof of standard D."),
]
with (ROOT / "endpoint_CHECK_EVENTS.tsv").open("w", newline="") as stream:
    writer = csv.writer(stream, delimiter="\t")
    writer.writerow(["statement_id", "date", "who_model_effort_run", "type", "outcome"])
    for kind, outcome in events:
        writer.writerow([
            "C.1n", "2026-11-19",
            "GPT-6 Astra (OpenAI); research run RESEARCH_SA06; child cycles; no independent-model check claimed",
            kind, outcome])
    writer.writerow([
        "C.1n", "2026-11-19",
        "GPT-6 Astra (OpenAI); research run RESEARCH_SA06; root independent targeted review",
        "targeted proof check",
        "Root independently passed the endpoint equivalence, checking the Hom convention, whole-motive realization, degree-zero restriction, semisimple image projector and target numerical=algebraic endpoint groups. Root suggested the arbitrary algebraically closed field/fixed Weil-cohomology extension, whose proof is written explicitly.",
    ])
    writer.writerow([
        "C.1n", "2026-11-19",
        "GPT-6 Astra (OpenAI); research run RESEARCH_SA06; child frobenius independent targeted review",
        "targeted proof check",
        "Frobenius independently passed the fixed-target strengthening I(X,r) iff D and G^r(X)=0: h_X^r detects D, zero correspondence detects G, and faithful whole graded realization plus numerical semisimplicity supplies a preimage. Exact source reopening is recorded separately by frobenius.",
    ])
print(json.dumps(certificate, indent=2))
