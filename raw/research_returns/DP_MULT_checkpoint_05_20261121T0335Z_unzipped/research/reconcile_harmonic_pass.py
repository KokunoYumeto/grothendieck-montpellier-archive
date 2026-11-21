#!/usr/bin/env python3
"""Merge actual DP49--51/source readings and record the narrowed current gates.

This supersedes reconcile_geometry_pass.py for current question/gate updates.
Historical events and review conclusions are never deleted.
"""
import csv
import json
from datetime import datetime, timezone
from pathlib import Path

root = Path(__file__).resolve().parents[1]
now = datetime.now(timezone.utc).isoformat()
cp = root / "CHECK_EVENTS.tsv"
with cp.open(newline="") as f:
    reader = csv.DictReader(f, delimiter="\t")
    fields, rows = reader.fieldnames, list(reader)


def add(sid, who, kind, scope, outcome, evidence, when=now):
    if any(r["evidence"] == evidence for r in rows):
        return
    serial = max(int(r["event_id"].split("-")[1]) for r in rows) + 1
    rows.append(dict(zip(fields, [
        f"DPC-{serial:03d}", sid, "2026-11-21 UTC", when, who,
        "GPT-6 Astra Pro", "not exposed by runtime", "DP_MULT_20261121",
        kind, scope, outcome, evidence,
    ])))


with (root / "research/archive_binomial_check_events.tsv").open(newline="") as f:
    for event in csv.DictReader(f, delimiter="\t"):
        n = int(event["event_id"].removeprefix("ABA-CE"))
        if n < 54:
            continue
        kind = "used and rechecked in this run" if n in (54, 55, 61) else (
            "computation or formal certificate" if n == 60 else "targeted proof check")
        add(event["statement_id"], event["checker"], kind, event["scope"],
            event["outcome"] + " LIMIT: " + event["limitations"],
            "research/archive_binomial_check_events.tsv:" + event["event_id"],
            event["utc_time"])

metadata = [
    ("DP49", "DP49_formal_bound_review_metadata.json", "/root/formal_bound"),
    ("DP49", "DP49_root_whole_read_metadata.json", "/root"),
    ("DP49", "DP49_integrated_root_review_metadata.json", "/root"),
    ("DP50", "DP50_author_whole_review_metadata.json", "/root/formal_bound"),
    ("DP50", "DP50_integrated_author_review_metadata.json", "/root/formal_bound"),
    ("DP50", "DP50_root_whole_read_metadata.json", "/root"),
    ("DP50", "DP50_level_normalization_root_review_metadata.json", "/root"),
    ("DP50", "DP50_integrated_root_review_metadata.json", "/root"),
    ("DP51", "DP51_author_whole_review_metadata.json", "/root"),
    ("DP51", "DP51_formal_bound_review_metadata.json", "/root/formal_bound"),
    ("DP51", "DP51_integrated_root_review_metadata.json", "/root"),
    ("DP51", "DP51_universal_corollary_root_review_metadata.json", "/root"),
    ("ARCHIVE-Q5E", "archive_q5e_root_pixel_review_metadata.json", "/root"),
]
for sid, filename, default_who in metadata:
    p = root / "research" / filename
    if not p.exists():
        continue
    d = json.loads(p.read_text())
    scope = d.get("scope", d.get("checks", "Complete reading described in the evidence metadata."))
    if isinstance(scope, list):
        scope = " ".join(scope)
    when = next((d[k] for k in ["observed_completion_utc", "whole_read_completed_utc",
                                "recorded_utc", "time_utc"] if k in d), now)
    who = d.get("who", d.get("agent", d.get("reviewer", default_who)))
    outcome = d.get("outcome", d.get("result", d.get("status", "PASS")))
    kind = "used and rechecked in this run" if sid == "ARCHIVE-Q5E" else "targeted proof check"
    add(sid, who, kind, scope, outcome, "research/" + filename, when)

d = json.loads((root / "research/dp49_jacobian_theta_checks.json").read_text())
for event in d["events"]:
    if event["id"] == "JT49-I001":
        continue  # the independent checker's own metadata is already merged
    source = event["id"] == "JT49-S001"
    add("STACKS-00IP" if source else "DP49", "/root/step2_higher",
        "used and rechecked in this run" if source else "targeted proof check",
        event["scope"], event["outcome"],
        "research/dp49_jacobian_theta_checks.json:" + event["id"],
        event.get("observed_completion_utc", event.get("recorded_utc", d["recorded_utc"])))
d = json.loads((root / "research/dp49_integrated_step2_review.json").read_text())
event = d["event"]
add("DP49", "/root/step2_higher", "targeted proof check", event["type"],
    event["outcome"], "research/dp49_integrated_step2_review.json:" + event["id"],
    event["observed_completion_utc"])
add("DP47", "/root", "targeted proof check",
    "Read the added scalar-endomorphism justification after the previously recorded complete proof reading. Normalized characteristic-zero logarithms embed integral endomorphisms of the one-dimensional formal group into scalar multiplications, which commute; equality over the fraction field is equality of the integral series. Exact old/new fragment hash checked during main synchronization.",
    "PASS; one explanatory sentence, no new theorem hypothesis.",
    "research/DP47_integrated_endomorphism_delta.json:root-added-sentence-check")
add("STACKS-00IP", "/root", "used and rechecked in this run",
    "Opened the primary Stacks Project Tag00IP and read Lemma10.51.4 and its short proof. Checked the proper-ideal, Noetherian-local-ring and finite-module hypotheses used for completion injectivity.",
    "PASS exact statement/locator; known theorem used, not claimed as new.",
    "https://stacks.math.columbia.edu/tag/00IP:root-read-20261121")

with cp.open("w", newline="") as f:
    writer = csv.DictWriter(f, fields, delimiter="\t")
    writer.writeheader()
    writer.writerows(rows)

qp = root / "QUESTIONS.tsv"
with qp.open(newline="") as f:
    reader = csv.DictReader(f, delimiter="\t")
    qfields, questions = reader.fieldnames, list(reader)
for q in questions:
    if q["id"] == "Q3e":
        q["finding_ids_or_counterexample"] = "U2;DP21;DP23;DP25-DP51"
        q["current_gate_or_scope"] = (
            "Actual cyclic CM models, precise primitive radii and trace-one polarized normalization are proved; DP49 realizes them on the concrete Jacobian. DP50 settles nonunit tensors and shows the actual M^(-degree) normalization outweighs that universal ordinary-path improvement. DP51 proves the sharp universal integral-polynomial rate, already sharp on the stated two-column HaO module, with exact digit-sum error and a specified sharp degree ray. "
            "The remaining selected-data question concerns the prescribed geometric sections and row degrees, their controlled nonvanishing, and matching the actual connection/minor/path and global links. Smaller even Ranks/HC/Host/Spaces inputs exist by DP44; endpoint period ties and the net integer gain/cost comparison remain. No arbitrary shorter-chain impossibility or construction is claimed.")
    if q["id"] == "Q5e":
        q.update(question="Can the historical binomial, composition and PD-cochain homotopy passages named in suggestion9 be located precisely?",
                 state="proved source mapping",
                 finding_ids_or_counterexample="DP11-DP14 context;ABA-PUB1-PUB6",
                 current_gate_or_scope="Original pixels locate cote153 PDF3/archive2; cote136 PDF4-6/archive3-5; cote133 PDF6/archive5 and PDF27-29/archive26-28; cote137 PDF38-39/archive37-38. Cote133's lambda identities and cote137's reconstruction are explicitly questions, not proved modern theorems. Chronology is not uniformly1976. The separately unresolved, unsupplied B7 comparison is now Q5f.")

new = [
    ("Q3aj", "DP22;DP46-DP49;actual principal polarization;ZinkTh5/9;Stacks00IP",
     "Do the primitive path rates occur on an actual polarized higher-height Jacobian theta germ, with nonzero restrictions?",
     "proved", "DP49",
     "At11, Jac(y²=x⁷−1) has the actual hyperbolic unit-arrow height3 block and integral trace-one theta line. Every primitive residue class has a nonzero restricted germ; the exact product-gauge slopes are1/1220 and1/120. A previously prescribed path and selected global theta value remain separate."),
    ("Q3ak", "DP46 primitive ghost formula;IsThRule.thExpr66-70;DP50",
     "Does a p-divisible theta tensor exponent improve the primitive kernel, and does its actual level normalization preserve the improvement?",
     "proved raw improvement; refuted normalized universal improvement", "DP50",
     "Every v_p(kappa)>=1 gives exact pure-kernel slope p^j/(p^h−1), with an infinite sharp coefficient sequence and a sharp universal integral-prefactor lower bound. For kappa=M², the source M^(−degree) factor changes the slope to p^j/(p^h−1)−v_p(M)<0. No equality is asserted for every individual prefactor."),
    ("Q3al", "RowDeg21-48;IsThRule.harmA86-87;DP42;DP46;DP51",
     "What is the sharp universal asymptotic rate after the source-shaped harmonic selection?",
     "proved within the stated primitive-kernel and integral-polynomial module", "DP51",
     "The full h-variable polydisc yields c*=1/((p−1)(p^(h−1)+1)) with exact multi-factorial digit-sum loss. This is sharp on the full integral polynomial module with one column and on the stated HaO submodule with two columns. The explicit sharp family has row-degree ratio1:p^(h−1). Prescribed geometric sections, weight sequences and growing-column errors require their actual data."),
    ("Q5f", "Fable suggestion9 lines131-135;explained307-314;Q5e refinement",
     "Does the proposed prior-run B7 comparison define a homotopy-to-multiplicity bridge that can be proved or refuted?",
     "current gate: precise statement unsupplied", "U2-context;DP13-DP14",
     "The supplied sources contain no precise B7 functor, hypotheses, categories or comparison map. Historical page locators are closed in Q5e, and DP13 gives the exact modern binomial reconstruction theorem. A further comparison cannot be proved or refuted until its mathematical statement is specified; none is invented."),
]
ids = {q["id"] for q in questions}
for q in new:
    if q[0] not in ids:
        questions.append(dict(zip(qfields, q)))
with qp.open("w", newline="") as f:
    writer = csv.DictWriter(f, qfields, delimiter="\t")
    writer.writeheader()
    writer.writerows(questions)
print(json.dumps({"utc": now, "events": len(rows), "questions": len(questions)}))
