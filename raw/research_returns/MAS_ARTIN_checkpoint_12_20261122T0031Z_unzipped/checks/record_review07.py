"""Record the seventh timed review once, after the actual register reading."""
from pathlib import Path
from datetime import datetime, timezone
import csv
import hashlib
import json
import re
import shutil

root = Path(__file__).resolve().parents[1]
now = datetime.now(timezone.utc)
assert now >= datetime(2026, 11, 22, 0, 31, tzinfo=timezone.utc)
stamp = now.isoformat()
question_file = root / "QUESTIONS.tsv"
preflight = json.loads((root / "evidence/review_07_preflight.json").read_text())
assert preflight["actual_root_reading_completed"] is True
assert preflight["questions_sha256"] == hashlib.sha256(question_file.read_bytes()).hexdigest()
with question_file.open(newline="") as f:
    rows = list(csv.DictReader(f, delimiter="\t"))
with (root / "evidence/review_06_questions.tsv").open(newline="") as f:
    previous = {r["id"]: r for r in csv.DictReader(f, delimiter="\t")}
current = {r["id"]: r for r in rows}
witness = "MA-RBQ-003"
assert "RB008" in str(previous[witness]) or "RB-008" in str(previous[witness])
assert "RB012" in str(current[witness]) or "RB-012" in str(current[witness])
assert "relative" in str(current[witness]).lower()
assert not (root / "evidence/review_07_questions.tsv").exists()
shutil.copyfile(question_file, root / "evidence/review_07_questions.tsv")

changes = []
for row in rows:
    old = previous.get(row["id"], {})
    for field in ["state", "finding_ids", "current_gate", "next_step"]:
        if old.get(field, "") != row[field]:
            changes.append({"id": row["id"], "field": field,
                            "previous": old.get(field, ""), "current": row[field]})
with (root / "evidence/review_07_changes.tsv").open("w", newline="") as f:
    writer = csv.DictWriter(f, fieldnames=["id", "field", "previous", "current"],
                            delimiter="\t", lineterminator="\n")
    writer.writeheader()
    writer.writerows(changes)
qualified = [current[q] for q in preflight["qualified_row_ids"]]
reviews = json.loads((root / "evidence/movement_reviews.json").read_text())
assert len(reviews) == 6
reviews.append({
    "number": 7, "timestamp_utc": stamp, "movement": True,
    "consecutive_stalled_reviews": 0, "question_rows": len(rows),
    "open_or_qualified_rows_reviewed": len(qualified),
    "changed_or_new_rows_since_previous_review": len({r["id"] for r in changes}),
    "movement_witness": witness,
    "next_review_utc": "2026-11-22T01:31:00+00:00",
    "decision": "Continue. RB012 strictly reduces the pre-existing residual S5 shared-zero interval by an entire relative-zeta envelope, retaining the actual comparison multiplicity and every local factor without A, M or R_B. The remaining shared-zero exclusion is not proved.",
    "main_gates_strictly_reduced": 1,
    "arithmetic_shared_zero_exclusions_proved": 0,
    "positive_excess_fields_constructed": 0
})
(root / "evidence/movement_reviews.json").write_text(json.dumps(reviews, indent=2) + "\n")

body = f"""\n\n## Timed movement review07 — {stamp}

Decision: **continue**. Genuine movement: **yes, one pre-existing S5 gate is strictly smaller**. Consecutive reviews without movement: **0**. Next review: **2026-11-22 01:31UTC /02:31Berlin**. Checkpoint12 is due now, **00:31UTC /01:31Berlin**; the next checkpoint is **01:16UTC /02:16Berlin**. The complete {len(rows)}-row immutable snapshot is evidence/review_07_questions.tsv. All state/finding/gate/next-step changes since review06 are recorded separately in evidence/review_07_changes.tsv. The root's actual reading and exact register hash are recorded in evidence/review_07_preflight.json.

### The sole movement witness and its limits

At review06, **MA-RBQ-003** left the comparison-failure point in the RB008 interval determined by script-J_(Delta_L,k). **MA-RB012** now proves the strictly smaller bound frak-J_(L,k) < script-J_(Delta_L,k), taking a finite envelope over the actual relative zeta functions zeta_L/zeta_(L^H). These quotients are entire by the exactly cited Aramata theorem. The completion removes the base-field pole terms and its entire completed divisor, and all ramified factors remain. The actual residual orders give multiplicity at least m_H k. For H=A5, m_H=9; subtracting the quadratic order b preserves at least9k without assuming A. The exact positive relative logarithmic derivative is strictly below the old denominator at the old attained minimizer. This proves strictness even when the new infimum is attained at sigma=1. Explicit finite Euler tails make the new upper bounds evaluable from genuine field data without zero-location input.

If the old interval is nonempty, the new interval is strictly shorter or empty. **One main gate is strictly reduced.** No theorem here proves that the new minimum is nonpositive for every field, excludes every remaining shared zero, proves R_B, or constructs a positive-excess extension. The author and two independent readers checked the complete new proof; the final written deltas were read. Aramata's original four-page proof was also read in full, with the source scope recorded. The known theorem is cited rather than reproduced in the paper.

The new boundary-source necessity and sufficiency estimates, exact analytic criteria, whole-quotient upper/lower costs, positive-product limitation and Rankin scope certificate are not separately counted as movement. Their arithmetic budgets remain unproved. A newly created question row or a further conditional case is not a movement witness.

### Every open or qualified route reviewed

The table includes established implications whose arithmetic antecedents, distinct original-map identifications or source provenance remain unresolved. Conditional conclusions are not promoted to their antecedents.

| Row | Current state | Exact gate or next step |
|---|---|---|
"""
for row in qualified:
    esc = lambda s: s.replace("|", "/").replace("\n", " ")
    body += "| " + esc(row["id"]) + " | " + esc(row["state"]) + " | " + esc(
        (row["current_gate"] + " " + row["next_step"]).strip()) + " |\n"
body += """
### Main-question gates after the review

1. **Masullo/Q and Dirichlet:** the complete actual corrected trace transport and source comparisons remain proved. FT002 still identifies unchanged geometry at every narrow width with the arithmetic deficiency condition. A supplies the rational/Dirichlet zero location explicitly. The canonical physical-cutoff/theta projector candidate is refuted in corrected and literal printed realizations, with principal polar conditions preserved. Genuinely different nonlocal or Gram-corrected maps retain their own scopes.
2. **Non-induced Hecke sector:** the actual all-width completed-ideal nuclear return is proved; the full common matrix still requires its explicit containing-strip and analytic cost conditions. Exterior and deficient-boundary zeros obstruct it. New local reciprocal and cluster estimates do not prove the arithmetic budgets or own-character RH.
3. **Original inverse and quotient costs:** the one-sided universal tests/cutoffs have exact reciprocal-growth criteria. The full-source boundary estimates retain their actual dual sectors and rational polar coordinates. PR012–013 give concrete upper potential and lower cluster estimates in the whole quotient norm, but the original all-test PR011 arithmetic cost gate remains unresolved. None of these equivalent or conditional analytic statements is counted again.
4. **S5:** beta=b+n remains proved under R_B. Without R_B, RB012 strictly shrinks the existing shared-zero interval. Actual shared-zero exclusion within that interval, a compatible odd residual realization, and a positive-excess field remain unproved. The finite-envelope comparison is independent of A and M.
5. **PF26:** the invoked proof audit, exact outside analytic premise, complete bad-prime reduction and explicit residual Kummer-Hecke list remain complete at their recorded input scope. No fresh audit of the separate companion analytic proof is asserted.
6. **Inputs and frameworks:** the563-row classification remains complete with secondary premises and provenance limits. The new analytic estimates provide actual norm information, while finite-length K0 data and the recorded cote1/SGA1/Deligne frameworks alone supply neither positivity nor arithmetic nonvanishing.

No final package is triggered. Continue toward the remaining actual arithmetic and original-map gates. Further equivalent criteria, positive products using only the same guaranteed relative multiplicities, source-scope results and packaging do not count as additional movement.
"""
with (root / "LEDGER.md").open("a") as f:
    f.write(body)
p = root / "README.md"
s = p.read_text()
replacement = "Work remains active. The seventh timed review records one strictly smaller pre-existing S5 shared-zero gate, with zero stalled reviews. RB012 does not exclude every point in the remaining interval or prove an arithmetic excess example. Checkpoint12 is scheduled for00:31UTC /01:31Berlin on22November; the next checkpoint is01:16UTC /02:16Berlin and the next review is01:31UTC /02:31Berlin. Every new proof in the compiled paper has actual complete-reading records; source-statement inspection is distinguished from a complete primary-proof audit. Prior checkpoints remain immutable."
s, count = re.subn(r"Work remains active\. The sixth timed review.*?Prior checkpoints remain immutable\.",
                   replacement, s, count=1, flags=re.S)
assert count == 1
p.write_text(s)
print(json.dumps(reviews[-1], indent=2))
