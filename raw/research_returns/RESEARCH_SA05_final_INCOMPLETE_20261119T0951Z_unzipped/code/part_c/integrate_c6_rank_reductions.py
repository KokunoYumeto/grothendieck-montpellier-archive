"""Integrate the independently audited C6 rank reductions and their records."""
from pathlib import Path
import csv
import io
import json
import re
from datetime import datetime, timezone

ROOT = Path(__file__).resolve().parents[2]
C = ROOT / "part_c"
D = ROOT / "part_d"
now = datetime.now(timezone.utc).strftime("%Y-%m-%d %H:%M UTC")

old = (D / "c6_rank_conjecture_reduction.tex").read_text()
new = (D / "c6_motivated_rank_reduction.tex").read_text()
assert "cohomological action must be idempotent" in old
assert "we use that definition over $K$" in new
main_path = ROOT / "sections/part_c.tex"
main = main_path.read_text()
marker = r"\begin{remark}[The remaining general-motive claim]"
assert main.count(marker) == 1
if r"\label{c:chow-unramified-rank-reduction}" not in main:
    main = main.replace(marker, old + "\n\n" + new + "\n\n" + marker)
gate_start = (
    "For general motives, the precise named sufficient conjecture is Fontaine's "
    "motivic Weil--Deligne compatibility conjecture:"
)
gate_new = (
    r"For Andr\'e motivated motives, Theorem~\ref{c:motivated-unramified-rank-reduction} "
    "supplies a second named sufficient hypothesis: independence of homological "
    "equivalence for rational cycles on all smooth projective varieties over "
    r"$\overline{\F}_p$. It controls the monodromy ranks and the finite inertia "
    "action, but remains conditional on that finite-field conjecture. "
    r"Corollary~\ref{c:motivated-abelian-strata-unramified} "
    "gives the stated unconditional geometric case only when all auxiliary "
    "strata have the required algebraic abelian-type presentations. Neither "
    "result proves a converse to the finite-field conjecture.\n\n"
    "For general motives, another precise named sufficient conjecture is "
    "Fontaine's motivic Weil--Deligne compatibility conjecture:"
)
if gate_start in main:
    main = main.replace(gate_start, gate_new, 1)
main_path.write_text(main)

bib_path = C / "references.bib"
bib = bib_path.read_text()
if "@article{c_vandobben2020," not in bib:
    bib += r"""

@article{c_vandobben2020,
 author={van Dobben de Bruyn, Remy},
 title={The equivalence of several conjectures on independence of $\ell$},
 journal={\'Epijournal de G\'eom\'etrie Alg\'ebrique},
 volume={4}, number={16}, pages={1--27}, year={2020},
 doi={10.46298/epiga.2020.volume4.5570},
 url={https://epiga.episciences.org/6931/pdf},
 note={Opened: published PDF and arXiv v3. Theorem 1, p.~3; Definition 4.1, Remarks 4.2--4.4 and Theorem 4.6, pp.~15--17; complete proof of Theorem 5.1 and Corollary 5.2, pp.~17--18, independently read by C and root. The finite-field rank and homological-equivalence formulations are a sufficient conjectural hypothesis, not a proved general theorem or a converse local unramifiedness statement.}
}
"""
if "@article{c_wanzhang2026betti," not in bib:
    bib += r"""

@article{c_wanzhang2026betti,
 author={Wan, Daqing and Zhang, Dingxin},
 title={Betti number bounds for varieties and exponential sums},
 journal={Advances in Mathematics},
 volume={490}, pages={110852}, year={2026},
 doi={10.1016/j.aim.2026.110852},
 url={https://zhangdingxin.gitlab.io/math/pdf/betti.pdf},
 note={Opened: author PDF, section 1.1, p.~2, including the explicit current statement that independence of total compactly supported Betti numbers remains open in general for singular or nonproper varieties. Used only as a bounded current source-status check, not as a proof of a new independence theorem. Publisher metadata retrieved; publisher full text not obtained.}
}
"""
andre_old = "Sections 8--9 also inspected."
andre_new = (
    "Sections 8--9 also inspected. For the motivated rank reduction, the "
    "definitions and complete supplied proofs in Sections 1.1--1.3, printed "
    "pp.~10--13, and the setup and Definition 1 in Section 2.1, pp.~13--14, "
    "were independently reread. The factor formula is Lemma 1.3.2. The "
    "normalized lowering identity is proved directly from p.~10 definitions, "
    "rather than using the discrepant p.~11 equality of two normalizations."
)
if andre_old in bib and "For the motivated rank reduction" not in bib:
    bib = bib.replace(andre_old, andre_new, 1)
saito_old = "the hyperplane retraction is supplied explicitly in our surface/low-degree argument."
saito_new = (
    saito_old + " For the rank reductions, complete Corollary 1.2.6 and its "
    "base-change input, p.~16; Section 2.4, Lemmas 2.4.1--2.4.2, Corollary "
    "2.4.3 and Proposition 2.4.4, pp.~33--36; and complete Lemmas 3.2--3.3 "
    "with the conjugate-alteration setup, pp.~36--39, were reread. "
    "These are targeted full-proof checks, not a claim to have rechecked "
    "the entire paper."
)
if saito_old in bib and "For the rank reductions, complete" not in bib:
    bib = bib.replace(saito_old, saito_new, 1)
bib_path.write_text(bib)

def read_table(path, delimiter):
    with path.open(newline="") as f:
        reader = csv.DictReader(f, delimiter=delimiter)
        return reader.fieldnames, list(reader)

def save_table(path, fieldnames, rows, delimiter):
    stream = io.StringIO(newline="")
    writer = csv.DictWriter(stream, fieldnames=fieldnames, delimiter=delimiter)
    writer.writeheader()
    writer.writerows(rows)
    path.write_text(stream.getvalue())

result_path = C / "results.csv"
fields, rows = read_table(result_path, ",")
records = [
    ("c:chow-unramified-rank-reduction",
     "The finite-field correspondence-rank conjecture implies monodromy-rank and unramifiedness independence for homogeneous algebraic homological projectors",
     "Proved conditional implication; no converse asserted",
     "van Dobben de Bruyn2020 Theorems4.6/5.1; Saito2003 section2.4; block rank formula",
     "Only cohomological idempotence is needed; no Chow-idempotent lift is assumed. Original-base finite inertia is retained."),
    ("c:chow-rank-reduction-scope",
     "Exact categorical and conditional scope of the algebraic rank implication",
     "Proved scope clarification; universal equivalence unresolved",
     "c:chow-unramified-rank-reduction",
     "Saito alone supplies algebraic E1 maps; the subsequent motivated theorem uses additional inverse-expression graphs. No converse geometric realization is supplied."),
    ("c:motivated-unramified-rank-reduction",
     "The same finite-field rank conjecture controls all Andre motivated motives at the original finite place",
     "Proved conditional implication; general C6 proof and named-conjecture equivalence remain unresolved",
     "Andre1996 sections1.1-1.3/Definition1; Saito2003 Cor1.2.6/section2.4/Lemmas3.2-3.3; graph rank formula",
     "Whole-product Lefschetz inverse diagrams remove algebraicity of the generic projector; simultaneous conjugate semistable models retain finite inertia. No weight-monodromy hypothesis."),
    ("c:motivated-abelian-strata-unramified",
     "Actual abelian Chow-motive presentations for every auxiliary semistable stratum suffice unconditionally",
     "Proved special geometric case using the current abelian Tate theorem",
     "c:motivated-unramified-rank-reduction; CM Hodge/abelian Tate; homological equals numerical; semisimplicity",
     "The condition applies to all auxiliary varieties in the motivated expression, not only the original ambient variety. No geometric positivity is transferred."),
    ("c:motivated-rank-reduction-scope",
     "The motivated reduction does not identify every absolute-Hodge projector or prove a converse rank conjecture",
     "Proved scope clarification; universal C6 gate retained",
     "c:motivated-unramified-rank-reduction; exact definition of motivated cycles over K",
     "No numerical-to-realization lift or universal degeneration realization is asserted."),
]
ids = {r["id"] for r in rows}
for ident, statement, status, depends, notes in records:
    if ident not in ids:
        rows.append(dict(zip(fields, [
            ident, statement, status, "sections/part_c.tex, label " + ident,
            depends, "12:140; C.6", notes
        ])))
save_table(result_path, fields, rows, ",")

event_path = C / "CHECK_EVENTS.tsv"
fields, events = read_table(event_path, "\t")
new_events = []
for ident, *_ in records:
    new_events.append([
        ident, "2026-11-19 07:48 UTC", "GPT-6 Astra (OpenAI), /root/part_c",
        "targeted proof check",
        "Read the complete written algebraic and motivated fragments; block padding, normalized rows, graph constraints, semilinear conjugate models and finite-order unipotent descent pass. Details in c6_rank_chain_audit.md and c6_motivated_operator_independent_audit.md."
    ])
    new_events.append([
        ident, "2026-11-19 07:48 UTC", "GPT-6 Astra (OpenAI), /root",
        "independent re-proof",
        "Root read the complete written motivated fragment and confirmed the proof, including the definition over K, after the earlier complete algebraic rank audit. Explicitly did not count this sufficient conditional theorem as movement on the unconditional general gate."
    ])
new_events += [
    ["c:motivated-unramified-rank-reduction", "2026-11-19 07:48 UTC",
     "GPT-6 Astra (OpenAI), /root/part_c", "used and rechecked in this run",
     "Independently reread Andre section2.1 setup/Definition1; Saito Proposition2.4.4 with arbitrary dimensions and complete Lemmas3.2-3.3 transport/conjugate proofs. No full-paper audit claimed."],
    ["c:motivated-unramified-rank-reduction", now,
     "GPT-6 Astra (OpenAI), /root/part_c", "computation or formal certificate",
     "Inspected the retained scope of root code/check_lefschetz_factor_operators.py (21 strings and100 tensor pairs) and code/check_rank_diagrams.py (48 chain maps and48 inverse graphs). These finite checks corroborate the direct operator/rank proofs; they do not test the finite-field conjecture or semistable geometry."],
    ["c:ell-independence-gate", now,
     "GPT-6 Astra (OpenAI), /root/part_c", "used and rechecked in this run",
     "Opened Wan-Zhang2026 author PDF section1.1 p2, which still identifies general singular/nonproper compact-Betti independence as unresolved. This is a bounded current-status check, not proof of absence of every possible newer result."]
]
for values in new_events:
    event = dict(zip(fields, values))
    if event not in events:
        events.append(event)
save_table(event_path, fields, events, "\t")

source_path = C / "sources.tsv"
fields, sources = read_table(source_path, "\t")
source_entries = [
    ["c_vandobben2020", "opened complete relevant published and arXiv proofs",
     "https://epiga.episciences.org/6931/pdf",
     "Theorem1 p3; Definition4.1 and Theorem4.6 pp15-17; complete Theorem5.1 proof and Corollary5.2 pp17-18. C and root independently checked exact all-correspondence rank equivalence; no conjecture closure asserted."],
    ["c_wanzhang2026betti", "opened author PDF; publisher metadata retrieved, publisher full text not obtained",
     "https://zhangdingxin.gitlab.io/math/pdf/betti.pdf",
     "Section1.1 p2; current scope statement only. C reopened primary author PDF at integration, ref turn163734451view0; D independently read same passage."],
]
for values in source_entries:
    entry = dict(zip(fields, values))
    sources = [r for r in sources if r["key"] != entry["key"]]
    sources.append(entry)
for source in sources:
    if source["key"] == "andre1996" and "normalized lowering" not in source["locators"]:
        source["locators"] += "; complete relevant definitions and supplied proofs sections1.1-1.3 pp10-13; Definition1 and K-scheme setup section2.1 pp13-14; normalized lowering independently derived, printed p11 discrepancy not used"
    if source["key"] == "saito2003weights" and "Cor1.2.6" not in source["locators"]:
        source["locators"] += "; full Cor1.2.6 p16 and base-change input; complete section2.4 pp33-36; complete Lemmas3.2-3.3 with conjugate setup pp36-39; arbitrary dimensions in Prop2.4.4; targeted checks only"
save_table(source_path, fields, sources, "\t")

labels = re.findall(r"\\label\{([^}]+)\}", main)
assert len(labels) == len(set(labels)), "Duplicate Part C labels"
for ident, *_ in records:
    assert labels.count(ident) == 1
assert r"\label{eq:c-induced-cohomology-rank}" in main
report = {
    "time": now,
    "new_statement_ids": [r[0] for r in records],
    "part_c_label_count": len(labels),
    "rank_equation_defined": True,
    "root_and_c_full_written_audits_passed": True,
    "unconditional_general_gate_remains_open": True
}
out = ROOT / "code/part_c/integrate_c6_rank_reductions_output.json"
out.write_text(json.dumps(report, indent=2) + "\n")
print(json.dumps(report, indent=2))
