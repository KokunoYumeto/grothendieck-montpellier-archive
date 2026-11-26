#!/usr/bin/env python3
"""Assemble canonical questions, current-paper crosswalks and filing tables.

Run after consolidate_records.py. No mathematical verdict is inferred from
a historical word such as "proved". Source status and current checks remain
separate. Printed locators below were checked against the final fresh builds.
"""
from pathlib import Path
import csv
import hashlib
import json
import re
import shutil

ROOT = Path(__file__).resolve().parents[2]
REC = ROOT / "workbench/records"


def read(path):
    with path.open(encoding="utf-8") as f:
        return list(csv.DictReader(f, delimiter="\t"))


def write(path, fields, rows):
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", encoding="utf-8", newline="") as f:
        w = csv.DictWriter(f, fieldnames=fields, delimiter="\t",
                           lineterminator="\n", extrasaction="ignore")
        w.writeheader()
        w.writerows(rows)


def statements(directory):
    found = {}
    pattern = r"\\begin\{(theorem|proposition|lemma|corollary|example|remark)\}(.*?)\\end\{\1\}"
    for p in sorted(directory.glob("*.tex")):
        text = p.read_text()
        for m in re.finditer(pattern, text, re.S):
            label = re.search(r"\\label\{([^}]+)\}", m.group(2))
            if label:
                found[label.group(1)] = {
                    "env": m.group(1).title(),
                    "exact_statement_tex": " ".join(m.group(2).split()),
                    "final_file": str(p.relative_to(ROOT)) + ":" +
                                  str(text[:m.start()].count("\n") + 1),
                }
    return found


FIELDS = ["paper", "document", "paper_statement", "tex_label", "pdf_page",
          "earlier_ids", "source_file", "final_file", "exact_statement_tex",
          "check", "check_record", "literature_status", "tag_scope"]
TAG_SCOPE = "local record locator; permanent work number and tag unallocated"

# Locators of the exact final PDFs checked in FINAL_READS.md.
P1 = [
    ("thm:arithmetic", "1.1", "1",
     "SA12:A:A2-persistent-arithmetic-counterexample;SA12:A:A2-sharp-curve-consequences",
     "parts/A/quadratic_tower_A2_post05.tex",
     "Complete fresh main-statement-only arithmetic reconstruction and full root comparison PASS; earlier construction-assisted proof separately disclosed; original 111784-assertion certificate and independent permutation computation",
     "ROOT_ARITHMETIC_FRESH_COMPARISON.md"),
    ("thm:wild", "1.2", "2", "SA12:A:wild-affine-counterexample",
     "parts/A/mixed_affine_post01.tex",
     "Complete separate statement-only reconstruction; exact Suzuki and Gabber–Orgogozo inputs; root reciprocal check",
     "paper_4/BLIND_PAPER1_WILD.md"),
    ("thm:birational", "1.3", "2", "SA12:B:L6-R1-vanishing;SA12:B.1",
     "parts/B/L6_R1_vanishing.tex;parts/B/paper_B.tex",
     "Known Ishii–Yoshida vanishing, exact primary locator; complete separate Picard deduction and reciprocal check of the known finite-torsor consequence",
     "paper_4/BLIND_PAPER1_PICARD_FULL.md"),
    ("thm:boundary", "1.4", "3", "SA12:D:boundary-neighborhood;SA12:D:finite-exceptional-wild",
     "parts/D/paper_D.tex",
     "Complete four-clause separate statement-only reconstruction and root reciprocal comparison; exact published tame inputs",
     "papers_2_3/BLIND_PAPER1_BOUNDARY.md"),
    ("lem:wreath", "2.1", "3", "SA12:A:A2-wreath-calculation",
     "parts/A/quadratic_tower_A2_post05.tex",
     "Separate complete arithmetic reconstruction; transfer checked by two computational methods",
     "paper_1/ARITHMETIC_INDEPENDENT_COMPARISON.md"),
    ("lem:step", "2.2", "4", "SA12:A:A2-quadratic-step",
     "parts/A/quadratic_tower_A2_post05.tex",
     "Separate complete arithmetic reconstruction; root adversarial comparison of inertness, transfer and genus argument",
     "paper_1/ARITHMETIC_INDEPENDENT_COMPARISON.md"),
    ("lem:detect", "3.1", "7", "SA12:B.1c", "parts/B/paper_B.tex",
     "Complete independent Picard reconstruction includes density, components and finite Frobenius kernel; root targeted check",
     "paper_4/BLIND_PAPER1_PICARD_FULL.md"),
    ("lem:projective", "4.1", "8", "SA12:D:fixed-boundary-positive",
     "parts/D/paper_D.tex",
     "Projective case only: full reconstruction used in boundary theorem, with exact tame finite-generation sources; broader source row not blanket-certified",
     "papers_2_3/BLIND_PAPER1_BOUNDARY.md"),
    ("prop:finite-wild", "4.2", "9", "SA12:D:finite-exceptional-wild",
     "parts/D/paper_D.tex",
     "Complete finite-exceptional-wild reduction in separate boundary reconstruction and root reciprocal comparison",
     "papers_2_3/BLIND_PAPER1_BOUNDARY.md"),
    ("ex:hidden-wild", "4.3", "10", "ROOT:original-boundary-strict-tame",
     "current:workbench/papers/paper_01/boundary.tex",
     "Complete worker construction and root targeted reconstruction/comparison PASS; independent homogeneous-matrix coordinate checks; all-valuation comparison read in exact primary source",
     "ROOT_BOUNDARY_EXAMPLE_CHECK.md"),
]
P4 = {
    "1.1": ("thm:proartinian", "1"),
    "1.2": ("thm:adic", "2"),
    "1.3": ("thm:triangular", "2"),
    "2.1": ("lem:compact", "3"),
    "2.2": ("lem:quotient", "4"),
    "3.1": ("lem:adiccotangent", "5"),
    "3.2": ("lem:extvanish", "5"),
    "4.1": ("lem:formalproj", "7"),
    "4.2": ("lem:strictproj", "7"),
    "5.1": ("lem:koszul", "8"),
}


def main():
    qpaths = [REC / "paper_1/QUESTIONS.tsv",
              REC / "papers_2_3/QUESTIONS.tsv",
              REC / "papers_2_3/OTHER_QUESTIONS.tsv"]
    questions = [r for p in qpaths for r in read(p)]
    ids = [r["question_id"] for r in questions]
    if len(ids) != len(set(ids)):
        raise SystemExit("Duplicate canonical question ID")
    questions.sort(key=lambda x: x["question_id"])
    write(ROOT / "QUESTIONS.tsv", list(questions[0]), questions)

    cross = []
    p1 = statements(ROOT / "workbench/papers/paper_01")
    for label, num, page, aliases, source, check, record in P1:
        s = p1[label]
        literature = ("Known theorem / known consequence: exact comparison in Paper1"
                      if label == "thm:birational"
                      else "Earlier ingredients credited; no priority claim")
        cross.append(dict(paper="01", document="workbench/papers/paper_01",
                          paper_statement=s["env"] + " " + num, tex_label=label,
                          pdf_page=page, earlier_ids=aliases,
                          source_file=(source.removeprefix("current:")
                              if source.startswith("current:") else
                              "ours/RESEARCH_SA12/" + source),
                          **{k: s[k] for k in ["final_file", "exact_statement_tex"]},
                          check=check, check_record="workbench/records/" + record,
                          literature_status=literature, tag_scope=TAG_SCOPE))
    write(REC / "paper_1/CROSSWALK.tsv", FIELDS, cross)

    for r in read(REC / "papers_2_3/CROSSWALK.tsv"):
        n = r["paper"].zfill(2)
        cross.append({**r, "document": "workbench/papers/paper_" + n,
                      "final_file": r.get("final_file", "").removeprefix("deliverable/"),
                      "tag_scope": TAG_SCOPE})

    p2 = statements(ROOT / "workbench/papers/paper_02")
    for label, aliases in [
            ("prop:tangent-ample", "SA14_SA19:A2Gs-cross"),
            ("cor:smooth-torsor", "SA14_SA19:A2Gs-cross")]:
        s = p2[label]
        cross.append(dict(paper="02", document="workbench/papers/paper_02",
            paper_statement=s["env"], tex_label=label, earlier_ids=aliases,
            source_file="ours/RESEARCH_SA14_SA19/sections/A.tex; current exact smooth-torsor exclusion",
            **{k:s[k] for k in ["final_file", "exact_statement_tex"]},
            check="Full root proof and source comparison; different symbolic intersection computation PASS; exact smoothness and ampleness scope only",
            check_record="workbench/records/ROOT_SMOOTH_TORSOR_CHECK.md;workbench/records/SMOOTH_TORSOR_COMPUTATION.json",
            literature_status="Compared with Liedtke surface classification and Fassarella--Mendson--dos Santos--Touzet foliation results; no priority claim",
            tag_scope=TAG_SCOPE))

    for label, alias in [
            ("thm:schematic-abelian-pushout", "ROOT:E4-abelian-pushout"),
            ("cor:picard-schematic-abelian-torsor", "ROOT:E4-abelian-torsor-Picard"),
            ("lem:semilocal-multisection", "ROOT:E4-semilocal-multisection")]:
        s = p2[label]
        cross.append(dict(paper="02", document="workbench/papers/paper_02",
            paper_statement=s["env"], tex_label=label, earlier_ids=alias,
            source_file="ours/RESEARCH_SA14_SA19/work/bce/E4_schematicity_attempts.md:81-93; current proof",
            **{k:s[k] for k in ["final_file", "exact_statement_tex"]},
            check="Complete isolated main-statement-only reconstruction and full root comparison PASS; reciprocal manuscript/source comparison frozen and read in full PASS; original targeted proof/source comparison PASS",
            check_record="workbench/records/ROOT_E4_TRANSFER_COMPARISON.md;workbench/records/ROOT_E4_FRESH_COMPARISON.md;workbench/records/abelian_torsor_fresh/reciprocal_comparison_v1.md",
            literature_status="Full Picard conclusion already stated by Achter--Casalaina-Martin §1.7.2 p13; arbitrary-base proof here; transfer statement not located in bounded search; classical inputs credited; no novelty claim",
            tag_scope=TAG_SCOPE))

    for label, alias in [
            ("thm:surface-torsor-modification", "ROOT:E4-surface-torsor-modification"),
            ("lem:smooth-surface-flat-perfect", "ROOT:E4-surface-flat-perfect"),
            ("lem:relative-surface-rank-one-defect", "ROOT:E4-surface-rank-one-defect"),
            ("lem:ample-pushforward-flat-basechange", "ROOT:E4-ample-pushforward-flat-basechange")]:
        s = p2[label]
        cross.append(dict(paper="02", document="workbench/papers/paper_02",
            paper_statement=s["env"], tex_label=label, earlier_ids=alias,
            source_file="ours/RESEARCH_SA14_SA19/work/bce/E4_schematicity_attempts.md:95-104; current proof",
            **{k:s[k] for k in ["final_file", "exact_statement_tex"]},
            check="Full root proof/source comparison PASS and separate exact-input audit PASS; isolated main-statement-only reconstruction frozen and complete, full root comparison PASS; full reciprocal report frozen PASS and read entirely by root",
            check_record="workbench/records/ROOT_E4_MODIFICATION_COMPARISON.md;workbench/records/ROOT_E4_MODIFICATION_FRESH_COMPARISON.md;workbench/records/ROOT_E4_MODIFICATION_RECIPROCAL_COMPARISON.md;workbench/records/abelian_torsor_fresh/m2_literature_input_audit_v1.md",
            literature_status="Rank-one determinant/ideal-of-points construction has verified precedent in Su--Wang Lemmas3.22--3.23 and Remark3.24 pp19--21; exact schematicity consequence not located in bounded search; no priority claim",
            tag_scope=TAG_SCOPE))

    label = "thm:torsor-projective-bundle"
    s = p2[label]
    cross.append(dict(paper="02", document="workbench/papers/paper_02", paper_statement=s["env"], tex_label=label, earlier_ids="ROOT:E4-all-base-projective-bundle;ROOT:E4-normal-base-projective-bundle", source_file="Current arbitrary-base projective-bundle continuation", **{k:s[k] for k in ["final_file", "exact_statement_tex"]}, check="Complete root and separate exposed arbitrary-base proof/source/manuscript audits PASS;historical57page full expert/newcomer/visual reading PASS; current PDF full readings tracked separately; second arbitrary-base statement-only reconstruction and full source completion PASS, using its own prior normal proof; two unsuccessful attempts preserved", check_record="workbench/records/ROOT_E4_NONNORMAL_COMPARISON.md;workbench/records/papers_2_3/E4_NONNORMAL_PROJECTIVE_BUNDLE_PROOF.md", literature_status="Classical Ramanujam--Samuel and projective-bundle inputs credited; compared with Zomervrucht and Brion; exact statement not located in bounded search; no priority claim", tag_scope=TAG_SCOPE))

    for label, alias in [('lem:dual-projective-finite-normal-cover', 'ROOT:E4-dual-finite-normal-projectivity'), ('lem:projective-picard-class-torsor', 'ROOT:E4-projective-picard-class-torsor'), ('prop:torsor-projective-after-normalization', 'ROOT:E4-torsor-projective-normalization')]:
        s = p2[label]
        cross.append(dict(paper="02", document="workbench/papers/paper_02", paper_statement=s["env"], tex_label=label, earlier_ids=alias, source_file="Current arbitrary-base projective-bundle proof", **{k:s[k] for k in ["final_file", "exact_statement_tex"]}, check="Complete root and separate exposed proof/source/manuscript audits PASS;historical57page full expert/newcomer/visual reading PASS; current PDF full readings tracked separately", check_record="workbench/records/ROOT_E4_NONNORMAL_COMPARISON.md", literature_status="Classical inputs credited at exact EGA/BLR/Raynaud/Picard locators; no priority claim", tag_scope=TAG_SCOPE))

    for label, alias in [("lem:normal-affine-relative-boundary", "ROOT:E4-normal-affine-boundary"), ("lem:torsor-finite-translation-kernel", "ROOT:E4-finite-translation-kernel"), ("prop:normal-local-torsor-projective-bundle", "ROOT:E4-normal-local-projective-bundle")]:
        s = p2[label]
        cross.append(dict(paper="02", document="workbench/papers/paper_02", paper_statement=s["env"], tex_label=label, earlier_ids=alias, source_file="Current normal-base projective-bundle continuation", **{k:s[k] for k in ["final_file", "exact_statement_tex"]}, check="Complete root proof/source and manuscript comparison PASS; encompassing arbitrary-base second statement-only reconstruction and full source completion PASS, with its own prior normal proof disclosed and two unsuccessful attempts preserved", check_record="workbench/records/ROOT_E4_NORMAL_BUNDLE_COMPARISON.md", literature_status="Classical inputs or their consequences, credited at exact EGA/Milne/Stacks locators; no priority claim", tag_scope=TAG_SCOPE))

    for label, aliases in [("prop:quasielliptic-multisection", "ROOT:A2-quasielliptic-radicial-exclusion"), ("prop:normalized-mup-conductor", "ROOT:A2-generic-mup-conductor;ROOT:A2-singular-conductor-adjunction")]:
        s = p2[label]
        cross.append(dict(paper="02", document="workbench/papers/paper_02", paper_statement=s["env"], tex_label=label, earlier_ids=aliases, source_file="Current scoped Picard-kernel continuation; inherited leading-form situation", **{k:s[k] for k in ["final_file", "exact_statement_tex"]}, check="Complete root proof and primary-source comparison PASS; exposed targeted normalization review; exact auxiliary scope only, no general A2 closure", check_record="workbench/records/ROOT_A2_RESIDUAL_COMPARISON.md;workbench/records/ROOT_A2_SINGULAR_ADJUNCTION_COMPARISON.md", literature_status="Known canonical/Euler and finite/Cartier duality inputs credited at exact locators; no priority claim", tag_scope=TAG_SCOPE))

    for label, alias in [
            ("cor:normalized-equality-torsor", "ROOT:A2-equality-normalization-torsor"),
            ("prop:normalized-mup-singularity-defect", "ROOT:A2-isolated-singularity-defect"),
            ("cor:normalized-mup-plurigenera", "ROOT:A2-equality-plurigenera")]:
        s = p2[label]
        cross.append(dict(paper="02", document="workbench/papers/paper_02", paper_statement=s["env"], tex_label=label, earlier_ids=alias, source_file="Current equality-case Picard-kernel continuation", **{k:s[k] for k in ["final_file", "exact_statement_tex"]}, check="Complete root targeted proof and primary-source comparison PASS; separate exposed equality-action audit frozen PASS and fully read; complete separate global-defect audit and reciprocal manuscript/MRT comparison frozen PASS and fully read by root; algebraic recomputation PASS; no general A2 closure", check_record="workbench/records/ROOT_A2_EQUALITY_SINGULARITY_COMPARISON.md;workbench/records/a3_a2_equality_audit/AUDIT.md;workbench/records/a3_a2_global_defect_audit/AUDIT.md;workbench/records/a3_a2_manuscript_comparison/COMPARISON.md;workbench/records/PICARD_CONSTRAINT_COMPUTATIONS.json", literature_status="Classical deformed-multiplicative Kummer kernels credited to Mezard--Romagny--Tossici Section2.2 p167 and Lemma6.1 p188; known Chern inputs at exact Stacks tags; no priority claim", tag_scope=TAG_SCOPE))

    label = "prop:distinguished-ruled-cover"
    s = p2[label]
    cross.append(dict(paper="02", document="workbench/papers/paper_02", paper_statement=s["env"], tex_label=label, earlier_ids="ROOT:A2-distinguished-ruled-cover", source_file="Current almost-ruled distinguished-cover continuation", **{k:s[k] for k in ["final_file", "exact_statement_tex"]}, check="Full root and separate frozen exposed proof/source/manuscript audits PASS; exact differential algebra PASS;historical57page full expert/newcomer/visual reading PASS; current PDF full readings tracked separately", check_record="workbench/records/ROOT_A2_RULED_COVER_COMPARISON.md", literature_status="Classical field differential and surface-resolution inputs credited; no priority claim", tag_scope=TAG_SCOPE))

    label = "prop:normalized-mup-ekedahl"
    s = p2[label]
    cross.append(dict(paper="02", document="workbench/papers/paper_02", paper_statement=s["env"], tex_label=label, earlier_ids="ROOT:A2-ekedahl-smallest-equality", source_file="Current application of Ekedahl I.2.4(ii)", **{k:s[k] for k in ["final_file", "exact_statement_tex"]}, check="Complete root proof and primary-source comparison PASS; separate exposed targeted audit and reciprocal manuscript comparison frozen PASS and read entirely; tensor-exponent and numerical recomputation PASS; general A2 remains open", check_record="workbench/records/ROOT_A2_EKEDAHL_COMPARISON.md;workbench/records/a3_a2_ekedahl_audit/AUDIT.md;workbench/records/a3_a2_ekedahl_reciprocal/RECIPROCAL_COMPARISON.md;workbench/records/PICARD_CONSTRAINT_COMPUTATIONS.json", literature_status="Known foliation theorem applied with all hypotheses, fixed-cover identification and numerical consequences explicit: Ekedahl I.2.4(ii), pp109–115, Lemma0.1.5 p103; no priority claim", tag_scope=TAG_SCOPE))

    for label, alias in [
            ("lem:k3-ample-curve-vanishing", "ROOT:A2-k3-ample-curve-vanishing"),
            ("prop:k3-picard-derivations", "ROOT:A2-k3-derivations"),
            ("prop:k3-picard-paracanonical", "ROOT:A2-k3-paracanonical"),
            ("prop:k3-picard-singularities", "ROOT:A2-k3-singularity-types")]:
        s = p2[label]
        cross.append(dict(paper="02", document="workbench/papers/paper_02",
            paper_statement=s["env"], tex_label=label, earlier_ids=alias,
            source_file="Current conditional K3 Picard-kernel refinement",
            **{k:s[k] for k in ["final_file", "exact_statement_tex"]},
            check="Complete root targeted proof and full primary-source comparison PASS; separate exposed targeted audit and reciprocal manuscript comparison frozen PASS and fully read; local lengths recomputed by a different method; no existence claim or general A2 closure",
            check_record="workbench/records/ROOT_A2_K3_STRUCTURE_COMPARISON.md;workbench/records/a3_a2_k3_audit/AUDIT.md;workbench/records/a3_a2_k3_reciprocal/RECIPROCAL_COMPARISON.md;workbench/records/PICARD_CONSTRAINT_COMPUTATIONS.json",
            literature_status="Known Matsumoto rational-quotient and local-classification theorems applied with exact hypotheses; Ekedahl canonical-cover theorem and duality inputs explicitly credited; full source locators in the comparison; no priority claim",
            tag_scope=TAG_SCOPE))

    for label, alias in [
            ("lem:small-degree-curve-bound", "ROOT:A2-small-degree-curve-bound"),
            ("prop:very-ample-numerical-obstruction", "ROOT:A2-very-ample-numerical-obstruction"),
            ("cor:very-ample-equality-almost-ruled", "ROOT:A2-very-ample-equality-distinguished-ruled;ROOT:A2-very-ample-equality-almost-ruled")]:
        s = p2[label]
        cross.append(dict(paper="02", document="workbench/papers/paper_02",
            paper_statement=s["env"], tex_label=label, earlier_ids=alias,
            source_file="Current very-ample equality reduction",
            **{k:s[k] for k in ["final_file", "exact_statement_tex"]},
            check="Complete root proof and full primary-source comparison PASS; different-method exact computations PASS; separate exposed targeted and reciprocal audits frozen PASS and fully read; no general A2 closure",
            check_record="workbench/records/ROOT_A2_VERY_AMPLE_COMPARISON.md;workbench/records/abelian_torsor_fresh/a2_very_ample_k3_exclusion_v1.md;workbench/records/a3_very_ample_audit/AUDIT.md;workbench/records/a3_very_ample_reciprocal/RECIPROCAL_COMPARISON.md;workbench/records/VERY_AMPLE_EXCLUSION_COMPUTATIONS.json",
            literature_status="Kadets Proposition2.8 pp4–5 and classical intersection theory applied; the corollary uses the fully checked Ekedahl reduction; no exact precedent identified in bounded search and no priority claim",
            tag_scope=TAG_SCOPE))

    for label, alias in [("prop:equality-rational-curves", "ROOT:A2-equality-rational-curves"), ("lem:very-ample-curve-genus-bound", "ROOT:A2-very-ample-curve-genus-bound"), ("prop:positive-genus-picard-fibration", "ROOT:A2-positive-genus-picard-fibration;ROOT:A2-ample-positive-genus-fibration")]:
        s = p2[label]
        cross.append(dict(paper="02", document="workbench/papers/paper_02", paper_statement=s["env"], tex_label=label, earlier_ids=alias, source_file="Current positive-genus equality continuation", **{k:s[k] for k in ["final_file", "exact_statement_tex"]}, check="Complete frozen proof and full root primary-source comparison PASS; separate exposed audit and reciprocal source receipts fully read PASS; current final PDF full readings tracked separately", check_record="workbench/records/ROOT_A2_POSITIVE_GENUS_COMPARISON.md;workbench/records/ROOT_A2_AMPLE_SCOPE_COMPARISON.md", literature_status="Classical surface/cohomology and Hilbert-function inputs credited; no priority claim; general A2 remains open", tag_scope=TAG_SCOPE))

    p4 = statements(ROOT / "workbench/papers/paper_04")
    for r in read(REC / "paper_4/CROSSWALK.tsv"):
        n = re.search(r"(\d+\.\d+)", r["paper_statement"])
        row = dict(r, paper="04", document="workbench/papers/paper_04",
                   source_file="ours/RESEARCH_SA23/RESEARCH_SA23/" + r["source_file"],
                   tag_scope=TAG_SCOPE)
        if n:
            label, page = P4[n.group(1)]
            row.update(p4[label])
            row.update(tex_label=label, pdf_page=page,
                       paper_statement=p4[label]["env"] + " " + n.group(1))
        cross.append(row)

    p5 = statements(ROOT / "workbench/papers/paper_05")
    known_dir = ROOT / "workbench/records/papers_5_6/known_gerbe_comparison"
    known = statements(known_dir)
    for r in read(REC / "papers_5_6/CROSSWALK.tsv"):
        is_p5 = r["document"].startswith("papers/paper_05")
        label = r["tex_label"]
        statement = (p5 if is_p5 else known).get(label, {})
        cross.append(dict(
            paper="05" if is_p5 else "known-comparison",
            document="workbench/" + r["document"],
            paper_statement=r["paper_statement"], tex_label=label,
            pdf_page=r["pdf_page"], earlier_ids=r["earlier_ids"],
            source_file=r["source"].removeprefix("source/"),
            final_file=statement.get("final_file", ""),
            exact_statement_tex=statement.get("exact_statement_tex",
                                               r["scope_qualification"]),
            check=r["check"] + "; " + r["scope_qualification"],
            check_record=";".join(str((REC / "papers_5_6" / part.strip()).resolve().relative_to(ROOT))
                                  for part in r["check_record"].split(";") if part.strip()),
            literature_status=r["known_status"], tag_scope=TAG_SCOPE))
    for row in cross:
        if row.get("tex_label") == "cor:very-ample-equality-almost-ruled":
            row["check"] = "Original and strengthened conclusions have full root and separate frozen targeted/reciprocal proof/source checks PASS;historical57page full expert/newcomer/visual reading PASS; current PDF full readings tracked separately"
            row["check_record"] += ";workbench/records/ROOT_A2_RULED_COVER_COMPARISON.md"

    # Refresh printed locators from a saved extraction of the latest clean
    # build, rejecting a stale PDF hash. No temporary path enters the table.
    locator_path = REC / "root_current/CURRENT_PDF_LOCATORS.tsv"
    locators = {(r["paper"], r["tex_label"]): r for r in read(locator_path)}
    for row in cross:
        paper = row["paper"]
        label = row.get("tex_label", "")
        if paper in {"01", "02", "03", "04", "05"} and label:
            directory = ROOT / "workbench/papers" / ("paper_" + paper)
            s = statements(directory)[label]
            row.update({k:s[k] for k in ["final_file", "exact_statement_tex"]})
            loc = locators.get((paper, label))
            if loc:
                if hashlib.sha256((directory / "main.pdf").read_bytes()).hexdigest() != loc["pdf_sha256"]:
                    raise SystemExit("Stale PDF locator table for paper " + paper)
                row["paper_statement"] = s["env"] + " " + loc["number"]
                row["pdf_page"] = loc["pdf_page"]
        if not row.get("check_record"):
            if paper == "02":
                record = ("ROOT_A2_PROJECTION_COMPARISON.md" if label == "lem:surface-projection-double-point"
                    else "ROOT_A2_ODD_GENUS_COMPARISON.md" if label in {"lem:positive-selfintersection-separable", "prop:positive-genus-picard-variety"}
                    else "ROOT_A2_CANONICAL_COMPARISON.md" if label in {"thm:strict-picard-char2", "prop:rational-normalization-canonical", "cor:characteristic-three-rational-residual", "rem:rational-canonical-scope"}
                    else "ROOT_A2_EULER_COMPARISON.md" if label in {"prop:deformed-torsor-degree-filtration", "cor:normalized-equality-euler", "prop:genus-zero-equality-defect"}
                    else "ROOT_A2_CHAR2_RATIONAL_COMPARISON.md" if label in {"prop:characteristic-two-rational-normalization", "rem:characteristic-two-ample-residual"}
                    else "ROOT_F8_FRESH_COMPARISON.md" if label == "thm:local-coefficients"
                    else "ROOT_A3_FRESH_COMPARISON.md" if label == "thm:surface"
                    else "ROOT_F10_F11_INDEPENDENT.md" if label in {"thm:abelian-inertia", "thm:metabelian"}
                    else "papers_2_3/F_LOCAL_GROUP_AUDIT.md" if label.startswith("lem:")
                    else "papers_2_3/PDF_REVIEW.md")
            elif paper == "03":
                record = ("ROOT_PRO7_FRESH_COMPARISON.md" if label == "thm:criterion"
                    else "ROOT_MODULARITY_BASE_CORRECTION.md" if label in {"thm:openness", "lem:generization"}
                    else "paper_4/BLIND_PAPER3_A4.md" if label == "thm:finite-descent"
                    else "ROOT_H_FIXED_BASE_FRESH_COMPARISON.md" if label == "thm:adic"
                    else "papers_2_3/L1_PRO7_INDEPENDENT_COMPARISON.md" if label in {"thm:openness", "lem:comparison", "lem:etale", "lem:uniform", "lem:generization", "lem:stratum", "lem:local-global"}
                    else "papers_2_3/PDF_REVIEW.md" if label == "prop:finite-type"
                    else "ROOT_P_RECIPROCAL_COMPARISON.md")
            elif paper == "04":
                record = "paper_4/PROOF_AUDIT.md"
            else:
                record = "PROOF_CHECK_MATRIX.tsv"
            row["check_record"] = "workbench/records/" + record
        for record in row["check_record"].split(";"):
            if record and not (ROOT / record).is_file():
                raise SystemExit("Missing check record: " + record)
        if not row.get("literature_status"):
            row["literature_status"] = "Exact primary-source comparisons and scope qualifications in LITERATURE.md; no priority claim"
        if paper == "02" and label == "thm:surface":
            row["check"] = "Complete fresh numerical-existence-statement-only reconstruction and both comparisons PASS; original and different-method certificates agree; numerical theorem unchanged in current expanded PDF; current QA in PAPER02_FINAL_READS.md"
        if paper == "03" and label == "thm:criterion":
            row["check"] = "Complete fresh main-statement-only reconstruction and full root comparison PASS; independent pro-modular assembly does not rely on ordinary-(7) openness"
        if paper == "03" and label == "thm:openness":
            row["check"] = "Fixed-base version refuted; relative replacement has two complete isolated main-statement-only reconstructions and full root comparisons PASS for all four alternatives; both reciprocal comparisons frozen and read in full PASS"
            row["check_record"] = "workbench/records/ROOT_RELATIVE_OPENNESS_SECOND_FRESH_COMPARISON.md;workbench/records/ROOT_RELATIVE_OPENNESS_FIRST_FRESH_SECOND_COMPARISON.md"
        if paper == "03" and label == "thm:adic":
            row["check"] = "Complete fresh expanded-main-statement-only reconstruction and both comparisons PASS; exact polynomial-base and completed-base claims; arbitrary fpqc and all noetherian adic topologies"
            row["check_record"] = "workbench/records/ROOT_H_FIXED_BASE_FRESH_COMPARISON.md;workbench/records/papers_2_3/H_FIXED_BASE_RECIPROCAL_COMPARISON.md"
    write(ROOT / "CROSSWALK.tsv", FIELDS, cross)

    dictionary_paths = [REC / "paper_1/DICTIONARY.md",
                        REC / "papers_2_3/DICTIONARY.md",
                        REC / "paper_4/DICTIONARY.md",
                        REC / "papers_5_6/DICTIONARY.md"]
    lead = ("# Mathematical dictionary and proof bridges\n\n"
            "These are translations of the precise proved statements, not "
            "additional claims about every part of Grothendieck's programme. "
            "Current checking scope is in CHECK_EVENTS.tsv. Source claims outside "
            "the selected papers remain distinguished from current certification.\n")
    (ROOT / "DICTIONARY.md").write_text(
        lead + "\n\n".join("\n## Record: " + str(p.relative_to(ROOT)) +
                            "\n\n" + p.read_text() for p in dictionary_paths))

    lit_paths = [REC / "ROOT_LITERATURE.md",
                 REC / "root_current/LITERATURE.md",
                 REC / "papers_2_3/LITERATURE.md",
                 REC / "papers_2_3/FRESH_P_H_DATED_LITERATURE_SEARCH.md",
                 REC / "papers_2_3/E4_LITERATURE_SEARCH.md",
                 REC / "papers_2_3/E4_RESIDUAL_LITERATURE_SEARCH.md",
                 REC / "abelian_torsor_fresh/m2_literature_input_audit_v1.md",
                 REC / "paper_4/LITERATURE.md",
                 REC / "paper_4/ARITHMETIC_LITERATURE.md",
                 REC / "paper_4/BOUNDARY_LITERATURE.md",
                 REC / "papers_5_6/LITERATURE.md"]
    (ROOT / "LITERATURE.md").write_text(
        "# Consolidated dated literature searches\n\n"
        "An early failed opening or pending gate is historical; later dated "
        "entries state whether it closed. Search failure does not prove novelty.\n\n" +
        "\n\n".join("## Record: " + str(p.relative_to(ROOT)) + "\n\n" +
                     p.read_text() for p in lit_paths))

    corr_paths = [REC / "paper_4/CORRECTIONS_FOR_AUTHORS.md",
                  REC / "papers_2_3/CORRECTIONS_FOR_AUTHORS.md",
                  REC / "igusa_corrections/FULL_CHECK.md",
                  REC / "ROOT_CORRECTIONS.md",
                  REC / "ROOT_SOURCE_CORRECTIONS_09.md",
                  REC / "ROOT_SOURCE_CORRECTIONS_10.md",
                  REC / "ROOT_SOURCE_CORRECTIONS_11.md",
                  REC / "ROOT_SOURCE_CORRECTIONS_12.md",
                  REC / "papers_5_6/CORRECTIONS_FOR_AUTHORS.md"]
    (ROOT / "CORRECTIONS_FOR_AUTHORS.md").write_text(
        "# Source corrections, known errata, and exact scope\n\n"
        "No author has been contacted. Every item distinguishes a false "
        "assertion, a proof-step objection, a citation repair, and an already "
        "published correction. This dossier is excluded from all research papers.\n\n" +
        "\n\n".join("## Record: " + str(p.relative_to(ROOT)) + "\n\n" +
                     p.read_text() for p in corr_paths))

    # Per-paper tables are ready for the owner's later permanent-tag allocation.
    events = read(ROOT / "CHECK_EVENTS.tsv")
    for n in range(1, 6):
        directory = ROOT / "workbench/papers" / f"paper_{n:02}"
        selected = [r for r in cross if r["paper"] == f"{n:02}"]
        prior_statements = read(directory / "STATEMENTS.tsv") if (directory / "STATEMENTS.tsv").exists() else []
        def statement_key(row):
            return row.get("tex_label") or ("unlabelled", row["paper_statement"], row["earlier_ids"], row.get("source_file", ""))
        prior_local_ids = {statement_key(r): r["local_statement_id"] for r in prior_statements}
        next_local_number = max([int(v.rsplit("-", 1)[1]) for v in prior_local_ids.values()] + [0]) + 1
        statement_rows = []
        aliases = set()
        for i, r in enumerate(selected, 1):
            aliases.update(x.strip() for x in r["earlier_ids"].split(";"))
            local_id = prior_local_ids.get(statement_key(r))
            if local_id is None:
                local_id = f"P{n:02}-{next_local_number:03}"
                next_local_number += 1
            statement_rows.append(dict(
                local_statement_id=local_id, permanent_tag="",
                **r))
        write(directory / "STATEMENTS.tsv",
              ["local_statement_id", "permanent_tag"] + FIELDS, statement_rows)
        def canonical_alias(value):
            return value.replace("SA14:", "SA14_SA19:").removeprefix("SA12:")
        selected_events = []
        for e in events:
            event_id = e["statement_id"]
            direct = any(a and canonical_alias(a) in canonical_alias(event_id)
                         for a in aliases)
            local = event_id.startswith(f"P{n:02}-")
            # A disclosed historical local label places this P proof under P02.
            # Its mathematical content belongs to the representability paper.
            if event_id == "P02-P-scalar":
                local = n == 3
            if direct or local:
                selected_events.append(e)
        write(directory / "CHECK_EVENTS.tsv",
              ["statement_id", "date", "who", "type", "outcome", "evidence"],
              selected_events)
        refs = []
        for tex in directory.glob("*.tex"):
            text = tex.read_text()
            for m in re.finditer(r"\\bibitem(?:\[[^\]]*\])?\{([^}]+)\}(.*?)(?=\\bibitem|\\end\{thebibliography\})",
                                 text, re.S):
                refs.append(dict(local_source_id=m.group(1),
                                 reference_tex=" ".join(m.group(2).split()),
                                 source_file=tex.name,
                                 status="citation in current paper; detailed source opening and hashes in workbench records"))
        write(directory / "SOURCES.tsv",
              ["local_source_id", "reference_tex", "source_file", "status"], refs)

    # Authoritative top-level tables are mirrored into the ready-to-add workbench.
    for name in ["REGISTER.tsv", "CHECK_EVENTS.tsv", "QUESTIONS.tsv",
                 "CROSSWALK.tsv", "DICTIONARY.md", "LITERATURE.md",
                 "CORRECTIONS_FOR_AUTHORS.md"]:
        shutil.copyfile(ROOT / name, ROOT / "workbench" / name)
    audit = {
        "canonical_questions": len(questions),
        "question_fragments": {str(p.relative_to(ROOT)): len(read(p)) for p in qpaths},
        "crosswalk_rows": len(cross),
        "numbered_research_paper_statements": sum(
            bool(re.match(r"^(Theorem|Proposition|Lemma|Corollary|Example|Remark)\s*\d", r["paper_statement"]))
            and r["paper"] != "known-comparison" for r in cross),
        "permanent_tags_allocated": False,
        "status_policy": "Historical assertions are not promoted to current verification.",
    }
    (REC / "CONSOLIDATION_QA.json").write_text(json.dumps(audit, indent=2) + "\n")
    print(json.dumps(audit, indent=2))


if __name__ == "__main__":
    main()
