#!/usr/bin/env python3
"""Merge actual check events and the DP40--DP42 question reductions."""
import csv
import hashlib
import json
from datetime import datetime, timezone
from pathlib import Path

root = Path(__file__).resolve().parents[1]
now = datetime.now(timezone.utc).isoformat()
cp = root / "CHECK_EVENTS.tsv"
with cp.open(newline="") as f:
    reader = csv.DictReader(f, delimiter="\t")
    fields, rows = reader.fieldnames, list(reader)

def add(statement, who, kind, scope, outcome, evidence, when=now):
    if any(r["evidence"] == evidence for r in rows):
        return
    number = max(int(r["event_id"].split("-")[1]) for r in rows) + 1
    rows.append(dict(zip(fields, [
        f"DPC-{number:03d}", statement, "2026-11-21 UTC", when,
        who, "GPT-6 Astra Pro", "not exposed by runtime",
        "DP_MULT_20261121", kind, scope, outcome, evidence,
    ])))

with (root / "research/archive_binomial_check_events.tsv").open(newline="") as f:
    for r in csv.DictReader(f, delimiter="\t"):
        n = int(r["event_id"].removeprefix("ABA-CE"))
        if n < 35:
            continue
        kind = ("refuted, with the refined statement's id" if n == 35
                else "independent re-proof" if n == 38
                else "targeted proof check")
        add(r["statement_id"], r["checker"], kind, r["scope"],
            r["outcome"] + " LIMIT: " + r["limitations"],
            "research/archive_binomial_check_events.tsv:" + r["event_id"],
            r["utc_time"])

event_files = [
    ("theta_normalization_sign_correction_checks.json", "DP38;DP39"),
    ("dp41_step2_review_checks.json", "DP41;DP38;DP39"),
    ("dp40_cyclic_sum_checks.json", "DP40"),
    ("dp42_mixed_line_checks.json", "DP42"),
]
for name, statement in event_files:
    d = json.loads((root / "research" / name).read_text())
    for e in d["events"]:
        if not isinstance(e, dict):
            continue
        eid = e["id"]
        kind = ("used and rechecked in this run" if eid.startswith("TN-S")
                else "computation or formal certificate" if eid == "CM40-N001"
                else "targeted proof check")
        subject = ("ZINK-HEX-196-211" if eid == "TN-S006"
                   else "DP38" if eid in ("TN-P007", "SPR-P-025")
                   else "DP39" if eid in ("TN-P008", "SPR-P-026")
                   else statement)
        when = e.get("recorded_utc", e.get("observed_clock_after_completion",
                                        d.get("recorded_utc")))
        add(subject, d["agent"], kind, e["scope"],
            e.get("status", "completed") +
            "; exact version and scope are retained in the cited metadata; no Lean execution.",
            "research/" + name + ":" + eid, when)

single_files = [
    ("DP40_model_and_combinatorial_review_metadata.json", "DP40"),
    ("DP41_whole_read_metadata.json", "DP41"),
    ("DP41_multiplier_extension_review_metadata.json", "DP41"),
    ("DP42_formal_bound_review_metadata.json", "DP42"),
]
for name, statement in single_files:
    d = json.loads((root / "research" / name).read_text())
    scope = d.get("scope", d.get("checks", d.get("event", "Complete proof reading")))
    if isinstance(scope, list):
        scope = " ".join(scope)
    add(statement, d.get("agent", d.get("reviewer")),
        "targeted proof check", scope,
        d.get("status", d.get("result", "PASS")) +
        "; mathematical reading of the recorded version, not formal verification.",
        "research/" + name,
        d.get("observed_whole_read_time_utc", d.get("time_utc", d.get("recorded_utc"))))

proofs = [
    "cyclic_display_models_DP40.md", "cyclic_cm_type_sum_DP40.md",
    "primitive_exponential_radius_DP41.md", "primitive_mixed_line_radius_DP42.md",
]
hashes = {name: hashlib.sha256((root / "research" / name).read_bytes()).hexdigest()
          for name in proofs}
note = root / "research/root_DP40_DP42_reading.json"
if not note.exists():
    note.write_text(json.dumps({
        "recorded_utc": now, "actor": "/root", "model": "GPT-6 Astra Pro",
        "effort": "not exposed by runtime",
        "scope": [
            "Read the complete saved DP40 model and Fourier proofs, including arbitrary unit ghosts, completion, actual dual, contraction witness, Fourier normalization and all equality cases.",
            "Read the updated complete DP41 proof including the completion argument, exact negative-hex logarithm, all valuation inequalities, the strengthened fraction-field multiplier lemma, and coordinate transfer.",
            "Read the complete saved DP42 sections1-10, recalculating strict weight gaps, primitive-vector inverse reduction, coefficient congruence, finite norm equality, liminf and restricted-p length.",
            "These are complete research-proof readings; later LaTeX integration is separately reviewed and preserved."
        ],
        "outcome": "PASS within every stated hypothesis; no numerical or Lean verification claimed.",
        "sha256": hashes,
    }, indent=2) + "\n")
add("DP40;DP41;DP42", "/root", "targeted proof check",
    "Complete saved research-proof readings and algebraic challenges; exact scope and hashes in metadata.",
    "PASS for the cyclic-display comparison, full primitive exponential threshold, arbitrary bounded multiplier and all primitive mixed-line slopes. The global theta/cost identification is not asserted.",
    "research/root_DP40_DP42_reading.json",
    json.loads(note.read_text())["recorded_utc"])

with cp.open("w", newline="") as f:
    w = csv.DictWriter(f, fields, delimiter="\t")
    w.writeheader()
    w.writerows(rows)

qp = root / "QUESTIONS.tsv"
with qp.open(newline="") as f:
    reader = csv.DictReader(f, delimiter="\t")
    qfields, questions = reader.fieldnames, list(reader)
for r in questions:
    if r["id"] == "Q3y":
        r["current_gate_or_scope"] = (
            "Corrected Zink convention: exact coefficients -1/p and +1/p in degree p+1; "
            "unit mixed jets and denominator rate at least1/(p+1). Oddp,h>2 invariant "
            "last-axis logarithmic path has a unit (p+1)st jet for integral unit multipliers. "
            "Exact signs in historical pre-correction checks are superseded, not erased.")
    if r["id"] == "Q3e":
        r["finding_ids_or_counterexample"] = "U2; DP21;DP23;DP25-DP42"
        r["current_gate_or_scope"] = (
            "The actual dual, primitive kernel, exact full exponential threshold and every primitive mixed-line factorial slope are proved. "
            "Those lines have best slope rho2 independent of h; arbitrary nonzero integral prefactors do not improve it. "
            "General cyclic type-plus-dual equal-direction sums are maximized by alternating type. "
            "Remaining: identify or construct the prescribed mixed-type theta section, actual connection lattice/corrections, selected polynomial/minor and geometric path; prove a quantitative selected-connection estimate beyond these settled cases if needed; "
            "construct the global correspondence and prove a net integer lift saving with its full costs. "
            "No nonexistence theorem for every shorter chain is claimed.")
new = [
    ("Q3aa", "Zink normal decomposition p129,Th5 p131,Def19/(22),Prop121,Th122; DP40",
     "What are sharp slopes for a general integral cyclic CM type, and which type maximizes their equally weighted total?",
     "proved", "DP40",
     "Arbitrary-unit cyclic displays and actual complementary duals have the stated exact sharp directions. The total is at most h*c2, equality exactly for even alternating type; each type partial sum is half. Not a componentwise or global-cost bound."),
    ("Q3ab", "Primitive Poincare display formula; Zink(196),(211),(218); DP41",
     "Can the uniform weight inflation p or its primitive exponential denominator loss be improved by an integral prefactor?",
     "refuted within the stated exact family", "DP41",
     "All rational inflation factors a<p give unbounded denominators; a>=p gives integral contraction. Every nonzero integral prefactor has the same threshold, including those vanishing at the origin. This concerns the fixed invariant primitive frame and full multivariate series."),
    ("Q3ac", "DP41 full primitive formula; actual-dual restricted-p chain; DP42",
     "What is the exact factorial slope on every logarithmic mixed line with both projections primitive?",
     "proved", "DP42",
     "Oddp,h>=3,unramified lattice: slope=1/((p-1)(p^k+1)), k the dual restricted-p nilpotency length. Best slope rho2 is independent of height. Exact coefficient congruence and nonzero-prefactor robustness proved. Pure/nonprimitive projections and selected harmonic projections remain outside this theorem."),
]
ids = {r["id"] for r in questions}
for r in new:
    if r[0] not in ids:
        questions.append(dict(zip(qfields, r)))
with qp.open("w", newline="") as f:
    w = csv.DictWriter(f, qfields, delimiter="\t")
    w.writeheader()
    w.writerows(questions)

print(json.dumps({"recorded_utc": now, "events": len(rows),
                  "questions": len(questions), "last_event": rows[-1]["event_id"]}))
