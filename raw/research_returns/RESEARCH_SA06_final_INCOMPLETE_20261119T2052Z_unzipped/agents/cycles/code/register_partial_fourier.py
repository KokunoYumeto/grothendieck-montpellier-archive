from pathlib import Path
from datetime import datetime, timezone
import csv
import json
import time

started = time.perf_counter()
base = Path(__file__).resolve().parents[1]
now = datetime.now(timezone.utc).isoformat()
fetch = json.loads((base / "output/fetch_partial_fourier_sources.json").read_text())
build = json.loads((base / "output/compile_partial_fourier.json").read_text())
certificate = json.loads((base / "output/partial_fourier_parity.json").read_text())

with (base / "partial_fourier_results.csv").open("w", newline="") as handle:
    writer = csv.writer(handle)
    writer.writerow(["id", "statement", "status", "where_proved", "depends_on",
                     "manuscript_pages_settled", "notes"])
    writer.writerow([
        "C.4ab",
        "For the stated complex type-(1,2) surface, actual Jacobian-product splitting, integral first-Kunneth-projector algebraicity, and existence of an integral correspondence with different H1/T parity are equivalent; exact partial Fourier curve coefficient computed",
        "Proved in the stated scope",
        "partial_fourier_correspondence.tex, C.4ab",
        "C4n integral bound 2; C4i/r Matsusaka normalization; integral K0 Fourier transform; primitive norm4 lattice gluing",
        "14:52-71 (criterion and method audit only)",
        "Exact reformulation, not main-gate movement. BPS residual fibre-product surface is excluded after partial FM, since t=s=-1. No universal assertion about all integral surface cycles. Explicit End_HS(T_Q)=Q assumption retained.",
    ])

events = [
    ("targeted proof check", "Verified scalar integrality, absence of Tate/transcendental cross maps, and 4|(n-s) by the primitive norm4 class in the unimodular H2 lattice."),
    ("targeted proof check", "Constructed the integral K0 class from resolutions and the relative Fourier-Mukai transform; verified c1 has no dual-polarization term and all omitted c2 bidegrees cannot affect the mixed curve map."),
    ("targeted proof check", "Computed mixed scalar 3(t^2-s)-(n-s)/2 and its parity; verified virtual c2 is an integral Chow class and the converse uses actual integral Poincare divisors. Normalization gives the exact first Kunneth projector, proving the stated scoped splitness equivalence."),
    ("targeted proof check", "Verified the BPS residual fibre-product action is trace minus diagonal, hence t=s=-1. This excludes that construction, not every full-span surface or every transformed K-class."),
    ("primary-source verification", "Freshly opened/read Mukai1981 section1 formula1.4 and Theorem2.2; Yoshioka2001 equations2.6-2.8 at printed authorp5, including page image; BPS2010 Proposition4.5 full proof and section5 equation5.1. Exact primary files/hashes retained."),
    ("primary-source scope check", "Fresh Kahn2602.11135v2 introduction through Proposition2.6 and AppendixB.6-B.7: integral projectors are in etale Chow, not ordinary Chow. No ordinary-cycle existence inferred."),
    ("independent root proof/source check received", "Full root PASS recorded 2026-11-19T12:17:14.738805UTC in notes/ROOT_C4ab_PARTIAL_FOURIER_AUDIT.md; entire proof, certificate and exact primary pages checked."),
    ("independent proof check received", "Frobenius full typed proof PASS received before registration; explicitly reused earlier normalization sources and did not freshly reopen the four source pages or rerun the certificate. His separate record controls that audit's exact scope."),
    ("independent proof/source check received", "Real_weil final full proof/source PASS received before registration; printed Yoshioka page5 correction incorporated. Separate independent review/events retained by that agent."),
    ("program execution", "Exact exterior/parity certificate PASS; 4913 parity cases, 41 graph cases; runtime_seconds=" + str(certificate["runtime_seconds"]) + ". The identities have symbolic proofs; finite tests check signs and implementation only."),
    ("program execution", "Primary-source retrieval completed " + fetch["utc"] + "; runtime_seconds=" + str(fetch["runtime_seconds"]) + "; exact bytes/SHA256 stored in output/fetch_partial_fourier_sources.json."),
    ("document validation", "Latest four-pass wrapper " + build["utc"] + "; runtime_seconds=" + str(build["runtime_seconds"]) + "; returncodes=" + str([x["returncode"] for x in build["runs"]]) + "; diagnostics=" + str(build["diagnostics"]) + "."),
    ("scope check", "The existence of a parity-mismatched algebraic correspondence remains undecided here and is equivalent to the original residual splitting assertion. No main-gate movement or priority claim."),
]
with (base / "partial_fourier_CHECK_EVENTS.tsv").open("w", newline="") as handle:
    writer = csv.writer(handle, delimiter="\t")
    writer.writerow(["statement_id", "date", "who_model_effort_run", "type", "outcome"])
    for kind, detail in events:
        writer.writerow(["C.4ab", now, "GPT-6 Astra (OpenAI); inherited reasoning effort; /root/cycles", kind, detail])

report = """# C.4ab: a partial Fourier test for the residual surface case

**Status: proved exact reformulation and method exclusion. No main-gate movement.**

Let A be a complex abelian surface with primitive type-(1,2) polarization L, NS(A)=ZL, and scalar rational Hodge endomorphisms on H1(A) and on T(A). For an integral codimension-two correspondence Z on A^2, let t, s, n be its scalar actions on H1, T, and NS. The primitive norm-four lattice gives n-s=4k. An integral relative Fourier-Mukai K-class E_Z then produces an actual integral curve c2(E_Z)P on A x Ahat, with mixed Matsusaka scalar

    m_Z = 3(t^2-s) - (n-s)/2 = 3(t^2-s)-2k.

Its parity is t-s. Such an odd scalar, together with the already proved universal scalar2, splits A off a product of Jacobians. Conversely any actual splitting gives an integral correspondence with t=1,s=0 by pulling and pushing normalized Poincare divisors on A x C. Thus this is an exact integral criterion, not an unproved promise that a new surface supplies the desired class.

The Bastianelli-Pirola-Stoppino Galois-closure surface is the residual fibre product over a rational ruled surface. The trace-minus-diagonal formula gives t=s=-1, so its partial Fourier transform is excluded. This calculation is stronger than citing only its Albanese variety: a transformed K-class is not automatically covered by the earlier divisor-pushforward method exclusion.

The criterion does not replace ordinary Chow classes by etale Chow classes. The June2026 Kahn preprint supplies etale integral projectors and explicitly separates their algebraicity in ordinary Chow from the etale statement.

## Retained artifacts

- `partial_fourier_correspondence.tex`: full proof and exact scope.
- `partial_fourier_references.bib`: three fresh primary references; existing BPS and Voisin keys reused.
- `code/check_partial_fourier_parity.py` and `output/partial_fourier_parity.json/.out`: exact rational exterior algebra and finite checks.
- `code/fetch_partial_fourier_sources.py` and its JSON/stdout: complete primary PDFs, SHA256, bytes and actual runtimes.
- `code/compile_partial_fourier.py`, wrapper PDF and logs: final typesetting checks with actual runtime.

The main type-(1,2) splitting problem remains unresolved by this criterion.
"""
(base / "partial_fourier_REPORT.md").write_text(report + "\nRegistration UTC: " + now + "\n")

source = """# C.4ab primary-source and search-scope audit

Only the specified statements/proofs were read; no full-paper independent proof claim is intended.

1. Mukai1981, full published23-page PDF, section1 formula1.4 and Theorem2.2 at printed156: integral derived Poincare functor. Exact source URL and SHA below. Browser refs turn426689033view0 and turn118378504view0.
2. Yoshioka2001, full38-page authorv2: section2.1 equations2.3,2.6-2.8, printed authorp5 (PDFindex4), including the actual page image turn118378504view3. The initial draft's p4 locator was corrected after real_weil's independent source read. Browser refs turn426689033view1 and turn556819259view0. The proof uses general Riemann-Roch in precisely its relative Fourier form; no WIT or positive-rank hypothesis is introduced.
3. Bastianelli-Pirola-Stoppino2010, full36-page authorv2: Proposition4.1 identifies the target as F3; Proposition4.5 and its complete proof give the finite degree3 morphism; section5 equation5.1 identifies the residual fibre product. Browser refs turn426689033view2 and turn118378504view2. The prior Albanese calculation alone was not used as a Fourier obstruction.
4. Kahn2026, Divided powers on abelian varieties, arxiv2602.11135v2: introduction through Proposition2.6 and AppendixB.6-B.7. Theorem1.7 and Corollary1.8 concern etale Chow projectors. Question1.11 and the ordinary comparison prevent a false integral-cycle inference. Browser refs turn324075281view0 and turn514342808view1/2. This is a source-scope observation, not an imported ordinary projector theorem.
5. Voisin2024, published PAMQ PDF: Definition1.9 and the Mumford-Tate-general discussion, printed2473, freshly read in turn118378504view1 and turn556819259view1. Its exact published numbering is retained.

## Other searches, not theorem inputs

- Bruin-Kulkarni2025, full primary On (2,2)-decomposable genus4 Jacobians, section7: square-gluing Jacobian loci are proper surfaces in the three-dimensional genus2 moduli space for the specified markings. This did not supply a generic type-(1,2) construction.
- Honigs-Graham McDonald-Peter McDonald2608.23779: primary arxiv abstract read; PDF and HTML retrievals returned DisabledError in this pass. No theorem from its inaccessible body is asserted.
- Gounelas-Huybrechts2510.20474v2: primary introduction/TheoremsA-B read. Universal Brauer-Severi varieties are classifying spaces; their universality is not the existence of a universal zero-cycle over the abelian surface.
- Voisin2025, Algebraic Geometry12(6)888-901, primary introduction and Lemma1.5 read. Representable CH0 examples have Albanese factoring through a curve; the non-universal-zero-cycle example does not provide the needed Brauer-Severi obstruction for this type-(1,2) surface.

## Actual source retrieval

"""
source += "```json\n" + json.dumps(fetch, indent=2) + "\n```\n"
(base / "partial_fourier_SOURCE_AUDIT.md").write_text(source)

path = base / "cycles.tex"
text = path.read_text()
anchor = "\\input{agents/frobenius/C4_transfer_countermodel.tex}"
line = "\\input{agents/cycles/partial_fourier_correspondence.tex}"
assert anchor in text
if line not in text:
    text = text.replace(anchor, anchor + "\n" + line)
path.write_text(text)
record = {"utc": now, "runtime_seconds": time.perf_counter() - started,
          "rows": 1, "events": len(events), "integrated": True}
(base / "output/register_partial_fourier.json").write_text(json.dumps(record, indent=2) + "\n")
print(json.dumps(record, indent=2))
