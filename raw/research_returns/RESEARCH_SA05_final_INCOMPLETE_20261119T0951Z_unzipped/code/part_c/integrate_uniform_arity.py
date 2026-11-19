"""Integrate the independently audited uniform recursive C.1 arity bound."""
from pathlib import Path
import csv
import json

ROOT = Path(__file__).resolve().parents[2]
part = ROOT / "part_c"
main = ROOT / "sections" / "part_c.tex"
fragment = (part / "c1_uniform_arity_bound.tex").read_text()
anchor = "\\begin{remark}[What the finite criterion settles]"
text = main.read_text()
if "\\label{c:uniform-arity-bound}" not in text:
    assert text.count(anchor) == 1
    text = text.replace(anchor, fragment + "\n\n" + anchor)
    main.write_text(text)

bib = part / "references.bib"
addition = (part / "c1_uniform_sources.bib").read_text()
existing = bib.read_text()
keys = ("c_dube1990", "c_maletzky2019groebner")
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
            csv.DictWriter(f, fieldnames=fields, delimiter=delimiter).writerows(rows)
    return len(rows)

sources = [
    dict(key=keys[0], status="opened relevant original pages; closed bound not used",
         url="https://cs.uwaterloo.ca/~r5olivei/courses/2025-spring-cs860/D90.pdf",
         locators="Lemma8.1 p772; Theorem8.2 and Corollary8.3 p773; no claim that the advertised formula is false and no dependence on it"),
    dict(key=keys[1], status="opened entry and section11 proof-outline discussion; not a complete formal-proof audit",
         url="https://isa-afp.org/browser_info/current/AFP/Groebner_Macaulay/outline.pdf",
         locators="Section11 printedpp55-56; entry first published2019-06-15; current PDF2026-10-26; reports corrections to Dube proof and motivates our independent bound"),
]
source_count = append_rows(part / "sources.tsv", sources, "\t", "key")

def row(ident, statement, status, depends, notes):
    return dict(id=ident, statement=statement, status=status,
                where_proved="sections/part_c.tex, label " + ident,
                depends_on=depends, manuscript_pages_settled="11:51-57; C.1(a,c)", notes=notes)

results = [
    row("c:recursive-elimination-bound", "Coefficient-independent computable Groebner elimination degree bound from a finite controlled Dickson tree",
        "Proved", "Elementary Dickson induction; finite branching; homogeneous Buchberger pair reduction; dehomogenization",
        "No disputed closed Dube formula is imported. The bound is a total recursive function with no efficiency claim."),
    row("c:uniform-arity-bound", "Uniform finite-power cut-off depending only on dimension and even/odd Betti numbers for rational cohomology tables",
        "Proved in the stated rational-table scope", "c:recursive-elimination-bound; square-zero encoding of exterior modules; c:finite-power-cutoff",
        "All super orbit equations have degree at most 2n+1 with rational coefficients. The enormous recursive bound is not evaluated and does not settle any actual K3 Chow vanishing."),
    row("c:uniform-arity-scope", "Precise coefficient input and finite-certificate scope of the uniform arity bound",
        "Proved scope clarification", "Named coordinates of every kappa_m; rational contraction by coefficient elimination",
        "For a presented coefficient algebra, all form coordinates are named generators and their variables are eliminated. Finite checks cover five small trees and one super orbit graph only."),
]
result_count = append_rows(part / "results.csv", results, unique="id")

events = []
def event(ident, who, kind, outcome):
    events.append(dict(statement_id=ident, date="2026-11-19", who="GPT-6 Astra (OpenAI), " + who,
                       type=kind, outcome=outcome))
for ident in ("c:recursive-elimination-bound", "c:uniform-arity-bound"):
    event(ident, "/root/part_c", "targeted proof check",
          "2026-11-19 06:20 UTC: Checked controlled-tree termination, accepted-leading-monomial degree growth, dehomogenization without saturation, square-zero linear-Y identification, elimination and exact variable/degree counts.")
    event(ident, "/root", "independent re-proof",
          "2026-11-19 06:18 UTC: Root read all 181 lines and finite output; full proof passed. Required all kappa-form coordinates, not only binary cup constants, to be named in the coefficient-bound variant; this clarification is included.")
    event(ident, "/root/part_d", "independent re-proof",
          "2026-11-19 06:19 UTC: D read all 181 lines and checked Dickson/Konig, homogeneous degree doubling, nonsaturated dehomogenization, Y-homogeneous encoding and elimination. Required explicit elimination of the named coefficient variables for I_Q; included.")
event("c:recursive-elimination-bound", "/root/part_c", "exact finite computation",
      "code/part_c/check_uniform_bound.py exhausts L(1,d)=d+1 for d1-4 and L(2,1)=4. JSON output records all level sizes and maximal witnesses. No actual geometric bound evaluated.")
event("c:uniform-arity-bound", "/root/part_c", "exact finite computation",
      "The same script encodes z=x,theta1=eta,theta2=x eta in an exterior module of rank8 and ordinary polynomial ring in10 variables. Groebner elimination over Q gives theta2-z theta1 and theta1 theta2; mutual ideal membership passes.")
event("c:uniform-arity-scope", "/root/part_c", "scope check",
      "Named coefficient generators include every coordinate of kappa1 through kappa2n, with the exact defining ideal; coefficient variables are eliminated. The rational-table uniform bound is not asserted for unspecified arbitrary Weil constants.")
event_count = append_rows(part / "CHECK_EVENTS.tsv", events, "\t")

notes = part / "part_c_notes.md"
heading = "## 2026-11-19 06:20 UTC: uniform recursive arity bound"
if heading not in notes.read_text():
    notes.write_text(notes.read_text().rstrip() + "\n\n" + heading + "\n\n" +
        "Integrated the root- and D-audited controlled-Dickson-tree bound and explicit square-zero super-orbit elimination. For rational cohomology tables the finite cut-off now depends only on (n,a,b). An exact presented-coefficient variant is stated separately. The proof imports no closed Dube formula, and no enormous geometric bound was numerically evaluated. Five small tree checks and one exact exterior elimination example pass in code/part_c/check_uniform_bound_output.json. The detailed source caution and proof audit are in c1_uniform_bound_audit.md. Actual K3/general Chow vanishing remains unresolved.\n")
audit = part / "c1_uniform_bound_audit.md"
if "Full independent written audits passed" not in audit.read_text():
    audit.write_text(audit.read_text().rstrip() + "\n\nFull independent written audits passed: root at approximately 06:18 UTC and D at approximately 06:19 UTC. Both coefficient-scope clarifications were incorporated before integration.\n")

summary = dict(main_lines=len(main.read_text().splitlines()), new_result_rows=result_count,
               new_source_rows=source_count, new_check_events=event_count,
               labels=[r["id"] for r in results])
out = ROOT / "code" / "part_c" / "integrate_uniform_arity_output.json"
out.write_text(json.dumps(summary, indent=2) + "\n")
print(json.dumps(summary, indent=2))
