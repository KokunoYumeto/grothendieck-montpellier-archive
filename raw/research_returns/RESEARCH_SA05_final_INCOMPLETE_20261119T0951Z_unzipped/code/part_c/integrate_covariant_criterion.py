"""Idempotently integrate the independently audited C.1 scalar-form criterion."""
from pathlib import Path
import csv
import json

ROOT = Path(__file__).resolve().parents[2]
part = ROOT / "part_c"
main = ROOT / "sections" / "part_c.tex"
fragment = (part / "c1_finite_unconditional_criterion.tex").read_text()
anchor = "\\begin{theorem}[The narrow K3 ring already detects finite-dimensionality]"
text = main.read_text()
if "\\label{c:finite-unconditional-criterion}" not in text:
    assert text.count(anchor) == 1
    text = text.replace(anchor, fragment + "\n\n" + anchor)

old_scope = """field from effective construction with specified coefficient data.
These finite criteria do not decide the resulting Chow vanishings."""
new_scope = """field from effective construction with specified coefficient data.
Theorem~\\ref{c:finite-unconditional-criterion} subsequently removes
the sign hypothesis by first passing to scalar forms in the
covariant polynomial category.  These finite criteria do not
decide the resulting Chow vanishings."""
old_cancel = """We have not proved that $C^+(X)$ follows from the point-and-diagonal
relations, or removed it from the cancellation step."""
new_cancel = """We do not infer $C^+(X)$ from the point-and-diagonal relations.
Theorem~\\ref{c:finite-unconditional-criterion} below removes that
hypothesis from the finite criterion by a different scalar-form
construction, which needs no cancellation step."""
text = text.replace(old_scope, new_scope).replace(old_cancel, new_cancel)
main.write_text(text)
for name in ("c1_finite_even_criterion.tex", "c1_finite_super_criterion.tex"):
    p = part / name
    s = p.read_text().replace(old_scope, new_scope).replace(old_cancel, new_cancel)
    p.write_text(s)

bib = part / "references.bib"
addition = (part / "c1_covariant_sources.bib").read_text()
existing = bib.read_text()
keys = ("c_brundankujawa2003", "c_hemmerkujawanakano2006")
if not any("{" + key + "," in existing for key in keys):
    bib.write_text(existing.rstrip() + "\n\n" + addition)
else:
    assert all("{" + key + "," in existing for key in keys)

def append_rows(path, rows, delimiter=",", unique=None):
    with path.open(newline="") as f:
        reader = csv.DictReader(f, delimiter=delimiter)
        fields = reader.fieldnames
        current = list(reader)
    if unique:
        present = {r[unique] for r in current}
        rows = [r for r in rows if r[unique] not in present]
    else:
        present = {tuple(r.get(k, "") for k in fields) for r in current}
        rows = [r for r in rows if tuple(r.get(k, "") for k in fields) not in present]
    if rows:
        with path.open("a", newline="") as f:
            writer = csv.DictWriter(f, fieldnames=fields, delimiter=delimiter)
            writer.writerows(rows)
    return len(rows)

sources = [
    dict(key=keys[0], status="opened; complete relevant primary proofs read",
         url="https://arxiv.org/pdf/math/0210108",
         locators="Section5 equations5.1-5.2 authorpp12-13; complete Lemma5.1 proofp14; complete Theorem5.2 proofp15; rational polynomial-comodule equivalence and signed double centralizer"),
    dict(key=keys[1], status="opened; complete characteristic-zero argument read",
         url="https://arxiv.org/pdf/math/0411390",
         locators="Theorem1.3.1(a)(i) authorp3; section3.1 pp6-7; proof4.2.6(a) p12; Maschke semisimplicity of Schur superalgebra; positive-characteristic classification not used"),
]
source_count = append_rows(part / "sources.tsv", sources, "\t", "key")

def result(ident, statement, status, depends, notes):
    return dict(id=ident, statement=statement, status=status,
                where_proved="sections/part_c.tex, label " + ident,
                depends_on=depends, manuscript_pages_settled="11:51-57; C.1(a,c)",
                notes=notes)

results = [
    result("c:covariant-polynomial-lifting",
           "Exact finite-degree Hom lifting for pure covariant polynomial supertensors",
           "Proved", "Brundan-Kujawa5.1-5.2; Schur coefficient coalgebra; Maschke",
           "Only the polynomial category is semisimple; no exactness of arbitrary mixed super-invariants is assumed. All rational splittings are finite linear algebra."),
    result("c:finite-unconditional-criterion",
           "Finite necessary-and-sufficient rational Chow identities for all-power point-and-diagonal relations without a sign hypothesis",
           "Proved; finite existence unconditional and effectiveness requires the stated coefficient data",
           "c:covariant-polynomial-lifting; augmentation projector; one high modified diagonal; Lehrer-Zhang2.1/2.3; schematic super-orbit kernel",
           "Removes C+ even over an arbitrary Weil coefficient field. Actual general Chow vanishings and the demanded K3 vanishing remain unresolved."),
    result("c:finite-power-cutoff",
           "One finite power detects all rational cohomological relations on all powers",
           "Proved; effective with the stated structure-constant presentation",
           "c:finite-unconditional-criterion; degree-one point retraction",
           "B=max(2,2n+1,2a(b+1),arities of the finite form relations). Does not provide an algorithm for rational equivalence."),
    result("c:finite-unconditional-scope",
           "Exact scope of the unconditional finite criterion and remaining K3/general vanishing gate",
           "Proved scope clarification; actual classification remains unresolved",
           "c:finite-unconditional-criterion; c:k3-gate",
           "Finite existence and effective construction are distinguished from deciding the Chow identities. The zero-dimensional point is immediate."),
]
result_count = append_rows(part / "results.csv", results, unique="id")

events = []
def event(ident, who, kind, outcome):
    events.append(dict(statement_id=ident, date="2026-11-19",
                       who="GPT-6 Astra (OpenAI), " + who,
                       type=kind, outcome=outcome))
for ident in ("c:covariant-polynomial-lifting", "c:finite-unconditional-criterion"):
    event(ident, "/root/part_c", "targeted proof check",
          "2026-11-19 06:07 UTC: Read complete BK coefficient and double-centralizer proofs and HKN characteristic-zero argument; checked pure-bidegree lifting, schematic rational orbit kernel, rectangular transport, augmentation recursion and narrow-ring necessity.")
    event(ident, "/root/part_d", "independent re-proof",
          "2026-11-19 06:02 UTC: D independently opened/read BK and HKN primary proofs, then read the entire 308-line written criterion; polynomial Hom exactness, universal rectangular transport, narrow-ring necessity, arbitrary-K kernel and effectiveness passed.")
    event(ident, "/root", "independent re-proof",
          "2026-11-19 06:06 UTC: Root read all 308 lines, BK section5 equations5.1-5.8 and complete Lemma5.1/Theorem5.2 proofs, and HKN section2.1/characteristic-zero proof4.2.6(a); full mathematical audit passed.")
event("c:finite-power-cutoff", "/root/part_c", "targeted proof check",
      "2026-11-19 06:07 UTC: Checked every finite test arity and the pullback retraction by intersecting extra factors with the degree-one point then pushing forward; no normalization or sign hypothesis is required for the retraction.")
event("c:finite-unconditional-scope", "/root/part_c", "scope correction",
      "2026-11-19 06:07 UTC: Finite existence now requires no C+, including arbitrary Weil coefficients; effective coefficient data and actual Chow vanishing remain separate. K3 determinant gate retained explicitly.")
event("c:finite-criterion-scope", "/root/part_c", "scope correction",
      "2026-11-19 06:07 UTC: Earlier mixed-invariant caveat now points to the unconditional scalar-form theorem; it remains a valid diagnosis of the direct mixed invariant method.")
event("c:super-criterion-scope", "/root/part_c", "scope correction",
      "2026-11-19 06:07 UTC: The projective/parity proof is retained with its exact hypotheses, but no longer presented as the strongest finite criterion. The new pure-form proof avoids that cancellation step entirely.")
event_count = append_rows(part / "CHECK_EVENTS.tsv", events, "\t")

note = """\n\n## 2026-11-19 06:07 UTC: unconditional finite criterion

The scalar-form construction removes C+ from the finite criterion over
arbitrary algebraically closed bases and Weil coefficient fields. The
complete proof, independently audited by D and root, is integrated as
c:covariant-polynomial-lifting and c:finite-unconditional-criterion.
The explicit high modified diagonal is Gamma_(2n+1), and
c:finite-power-cutoff reduces all powers to one finite power determined
by the constructed list. Effective computation requires a presentation
of the structure-constant Q-algebra. Actual general Chow vanishings,
especially the K3 determinant, remain unresolved. The detailed method
and failed mixed-invariant routes are recorded in
c1_covariant_finite_basis_audit.md. This is a genuine reduction of the
general criterion, not merely another positive family.
"""
notes = part / "part_c_notes.md"
if "## 2026-11-19 06:07 UTC: unconditional finite criterion" not in notes.read_text():
    notes.write_text(notes.read_text().rstrip() + note)

audit = part / "c1_covariant_finite_basis_audit.md"
s = audit.read_text()
if "Root full written audit passed" not in s:
    s += "\n\nRoot full written audit passed at 06:06 UTC. Root also independently read the complete BK coefficient and double-centralizer proofs and the HKN characteristic-zero argument. The explicit Gamma_m formula and finite-power corollary were included on integration at 06:07 UTC.\n"
    audit.write_text(s)

summary = dict(main_lines=len(main.read_text().splitlines()),
               new_result_rows=result_count, new_source_rows=source_count,
               new_check_events=event_count,
               labels=[r["id"] for r in results])
out = ROOT / "code" / "part_c" / "integrate_covariant_criterion_output.json"
out.write_text(json.dumps(summary, indent=2) + "\n")
print(json.dumps(summary, indent=2))
