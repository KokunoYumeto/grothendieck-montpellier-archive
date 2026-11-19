#!/usr/bin/env python3
"""Reproduce the exact Saito/Walker-generation refinement and source-audit ledger."""
import csv
from pathlib import Path

BASE = Path(__file__).resolve().parents[1]
WHO = "GPT-6 Astra (OpenAI); research run RESEARCH_SA06; child cycles; no independent-model check claimed"
rows = [
    ["E.3o", "Integral Walker kernel equals Saito's product A*H, while N is the zero-cycle-generated relation <H*2>_0; the general family converse is exactly their equality",
     "Known", "saito_filtration.tex, paragraph E.3o",
     "Saito1992 equation(1.8.2), Lemma1.10, Theorem6.2 proof pp321-323, Corollary6.3 and Remark6.4 p325; ACMVWalker2022 Theorem2.3; E.3m-n",
     "14:24-39",
     "Exact integral consequence derived in full. The primed quotient has finite ordinary AJ kernel; divisibility identifies its kernel with Walker's. Saito's unprimed denominator is A intersect H*2, NOT <H*2>_0. No general generated-kernel equality asserted."],
    ["E.3p", "The manuscript's N is generated integrally by Albanese kernels of smooth projective surfaces",
     "Proved", "saito_filtration.tex, paragraph E.3p",
     "Bertini with finitely imposed points; integral weak Lefschetz; Albanese H1 realization; correspondence pullback-pushforward; Saito1992 Lemma7.1.1",
     "14:24-39",
     "For each zero-cycle relation on T, choose a smooth complete-intersection surface through its support. Alb(surface)->Alb(T) is an isomorphism, so the lifted relation is still Albanese zero. This restricts the auxiliary source dimension but does not prove that all A*H classes are generated this way."],
    ["E.3q", "For varieties with CH0 supported on a surface, P2 is integrally the Walker and ordinary algebraic intermediate Jacobian group",
     "Proved under stated hypotheses", "saito_filtration.tex, paragraph E.3q",
     "E.3l transposed diagonal decomposition; E.3o; Saito1992 Corollary6.3 and Remark6.4; ACMVWalker2022 Theorem2.3; integral AJ functoriality",
     "14:24-39",
     "All dimensions n>=2 in codimension2. Transposition factors through CH0 of support surfaces and Pic0 of resolved divisors. Complements the one-cycle result E.3l; does not assert all codimensions under surface support."]
]
with (BASE / "filtration_results.csv").open("w", newline="") as f:
    w = csv.writer(f)
    w.writerow(["id", "statement", "status", "where_proved", "depends_on", "manuscript_pages_settled", "notes"])
    w.writerows(rows)

events = [
    ["E.3o-p", "2026-11-19", "GPT-6 Astra (OpenAI); research run RESEARCH_SA06; root independent targeted review", "targeted proof check",
     "Root independently checked the exact integral Saito finite quotient, both divisibility arguments identifying Walker kernel=A*H, zero-cycle H*2=Albanese kernel, and prescribed-support complete intersections with integral H1 Lefschetz. Passed; no general N=A*H conclusion asserted."],
    ["E.3o-q", "2026-11-19", "GPT-6 Astra (OpenAI); research run RESEARCH_SA06; child frobenius independent targeted review", "targeted proof check",
     "Frobenius directly viewed Saito primary pages321,323,325, checked the primed quotient and finite integral kernel, the divisor/surface factorization and divisibility in E.3q, and the complete-intersection surface reduction. All passed; separate independent review and events retained in frobenius directory."],
    ["E.3o", "2026-11-19", WHO, "used and rechecked in this run",
     "Opened full primary Saito1992 PDF and independently rendered pp296,297,320,321,323,325-327. Exact equation(1.8.2) is numerator <H*l>_0 divided by its intersection with H*(l+1), not the next zero-cycle-generated relation. Checked prime-Gr definition p321 and finite kernel argument p323, Remark6.4 p325, and Lemma1.10 divisibility p297."],
    ["E.3o", "2026-11-19", WHO, "targeted proof check",
     "A*H is divisible and lies in ordinary AJ kernel, hence maps trivially to the finite Walker isogeny kernel. Walker kernel/A*H is a finite divisible group and vanishes. For zero-cycles, Saito Cor6.3 plus Remark6.4 and Roitman give H*2 CH0=Albanese kernel. This proves exactly the two stated integral identities."],
    ["E.3p", "2026-11-19", WHO, "targeted proof check",
     "Checked integral complete-intersection surface construction through finite support, smoothness via sufficiently positive one-jet separation and Bertini, integral H1 weak Lefschetz and Albanese isomorphism, and refined Gysin correspondence identity. Dimension0/1 relations have zero Albanese kernel."],
    ["E.3 Saito failed closure", "2026-11-19", WHO, "targeted proof check",
     "A preliminary team reading replaced Saito's intersection denominator by the next zero-cycle-generated relation and suggested general closure. Root and cycles flagged the contradiction with the still-distinct universal regular quotient; cycles's locally rendered original equation(1.8.2) corrected the reading before any closure theorem or main result row was integrated. Frobenius independently inspected the local crop and explicitly withdrew the inference; its separate correction review is retained."],
    ["E.3q", "2026-11-19", WHO, "targeted proof check",
     "Transposed the integral diagonal decomposition. Verified source-support factors CH2(X)->CH0(S), target-divisor support factors CH2(X)->CH1(D), exact correspondence codimensions, and functorial ordinary AJ annihilation. One integer kills the quotient kernel; divisibility makes it zero. Saito codimension2 torsion theorem makes Walker->ordinary Jacobian an isomorphism."],
    ["E.3 modern regular-quotient search", "2026-11-19", WHO, "used and rechecked in this run",
     "Opened Barbieri-Viale2001 Section1.1, Hernandez-Pelaez2025 arXiv Section4.1 and Theorem4.1.13, and Pelaez2026 Sections3.2.4-3.2.5 and Theorems4.3.1-4.3.2. Their Samuel abelian relation is the intersection of regular kernels, not the generated N. These sources do not prove N equals the Walker kernel."],
    ["E.3 filtration source preservation", "2026-11-19", WHO, "computation or formal certificate",
     "fetch_filtration_sources.py preserved four primary PDFs with SHA256, URL, UTC timestamps, and successful pdftotext records. render_saito_pages.py rendered eight exact pages. A separate curl alternate URL timed out after40seconds at2327729bytes; its partial binary and attempt metadata are retained. The main Saito download is complete2759702bytes."],
    ["Late source preservation", "2026-11-19", WHO, "computation or formal certificate",
     "fetch_late_sources.py successfully preserved Gross-Schoen1995, Schoen1993, Vial2017Abelian and ACMVFunctorial2022 with hashes and text extraction. Vial2017 was investigated for representability; no theorem from it is used to assert the missing generated-kernel equality."]
]
with (BASE / "filtration_CHECK_EVENTS.tsv").open("w", newline="") as f:
    w = csv.writer(f, delimiter="\t")
    w.writerow(["statement_id", "date", "who_model_effort_run", "type", "outcome"])
    w.writerows(events)
print(f"Wrote {len(rows)} result rows and {len(events)} check events")

