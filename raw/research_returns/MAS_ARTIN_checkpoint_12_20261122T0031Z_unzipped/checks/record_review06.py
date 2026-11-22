"""Record review06 once, from the live register and immutable review05."""
from pathlib import Path
from datetime import datetime, timezone
import csv
import json
import re
import shutil

root = Path(__file__).resolve().parents[1]
now = datetime.now(timezone.utc)
assert now >= datetime(2026, 11, 21, 23, 31, tzinfo=timezone.utc)
stamp = now.isoformat()
with (root / "QUESTIONS.tsv").open(newline="") as f:
    rows = list(csv.DictReader(f, delimiter="\t"))
with (root / "evidence/review_05_questions.tsv").open(newline="") as f:
    old = {r["id"]: r for r in csv.DictReader(f, delimiter="\t")}
current = {r["id"]: r for r in rows}
gate = "MA-Q1-CQ003"
assert "unproved" in old[gate]["state"]
assert "canonical" in current[gate]["state"].lower()
assert "refuted" in current[gate]["state"].lower()
assert "MA-PI-001" in str(current[gate])
assert not (root / "evidence/review_06_questions.tsv").exists()
shutil.copyfile(root / "QUESTIONS.tsv", root / "evidence/review_06_questions.tsv")

changes = []
for row in rows:
    prior = old.get(row["id"], {})
    for field in ["state", "finding_ids", "current_gate", "next_step"]:
        if prior.get(field, "") != row[field]:
            changes.append({"id": row["id"], "field": field,
                            "previous": prior.get(field, ""), "current": row[field]})
with (root / "evidence/review_06_changes.tsv").open("w", newline="") as f:
    wr = csv.DictWriter(f, fieldnames=["id", "field", "previous", "current"],
                        delimiter="\t", lineterminator="\n")
    wr.writeheader()
    wr.writerows(changes)

extra = {"MA-Q1-CQ003", "MA-Q1-RF003", "Q-MA-SOURCE-BRIDGE", "Q-MA-LA-GLOBAL", "MA-Q1-RF002", "MA-Q2",
         "MA-Q1-HM001", "MA-Q1-HM002", "MA-Q3c", "MA-Q1-PR009", "MA-Q1-PR010",
         "MA-Q-MEY-narrow", "MA-Q1-PR007", "MA-Q1-PR003", "Q-MA-LD-FINITE",
         "MA-Q2-FQ006B", "MA-Q2-FQ-primes", "Q-MA-CAUSAL-001"}
qualified = [r for r in rows if r["id"] in extra or re.search(
    r"open|unproved|unresolved|conditional|partially|not established|gate|regime|unmodified|equivalent|antecedent",
    r["state"], re.I)]
reviews = json.loads((root / "evidence/movement_reviews.json").read_text())
assert len(reviews) == 5
reviews.append({
    "number": 6, "timestamp_utc": stamp, "movement": True,
    "consecutive_stalled_reviews": 0, "question_rows": len(rows),
    "open_or_qualified_rows_reviewed": len(qualified),
    "changed_or_new_rows_since_previous_review": len({r["id"] for r in changes}),
    "movement_witness": gate,
    "next_review_utc": "2026-11-22T00:31:00+00:00",
    "decision": "Continue. PI001–003 refute the canonical theta/physical-cutoff projector candidate explicitly left undecided in the old CQ003 gate, in corrected and exact printed norms, including principal input/output polar conditions. This is one decided pre-existing map subgate, not closure of all possible factorizations and not an arithmetic gate reduction.",
    "complete_broad_factorization_rows_closed": 0,
    "decided_preexisting_map_subgates": 1
})
(root / "evidence/movement_reviews.json").write_text(json.dumps(reviews, indent=2) + "\n")

body = f"""\n\n## Timed movement review06 — {stamp}

Decision: **continue**. Genuine movement: **yes, one pre-existing canonical-map subgate decided**. Consecutive reviews without movement: **0**. Next movement review: **2026-11-22 00:31 UTC /01:31 Berlin**. Next scheduled checkpoint: **2026-11-21 23:46 UTC /2026-11-22 00:46 Berlin**. The complete {len(rows)}-row immutable snapshot is evidence/review_06_questions.tsv; every state/finding/gate/next-step change from review05 is in evidence/review_06_changes.tsv. A changed row, new theorem, equivalent criterion or extended conditional theorem is not automatically movement.

### The sole movement witness counted, and its exact limit

At review05, **MA-Q1-CQ003** explicitly left a literal original finite-cutoff projector factorization unproved. Its gate said that the established local quotient and global Gram transport did not identify a literal full-cover or same-coordinate additive projector with the global weighted projection; its next step asked for that map's own intertwining theorem. The canonical theta map and physical Fourier cutoff now have actual counterexamples. **MA-PI001** gives genuine flat chi4 source witnesses in the corrected centered norm. **MA-PI002** derives an exact unitary to the printed norm, retaining the compact Haar mass, and proves the same failure for every0<A<1, including the original A=1/2. **MA-PI003** proves the principal rational version with both polar conditions preserved for the input and the physical-cutoff output, in both metrics. Complete author and independent whole-proof readings have passed. The canonical map identity is therefore false on the actual source, without zero-location input.

This counts **one decided pre-existing canonical-map subgate**. It counts **zero complete closures of the broad existential factorization question**: other genuinely different nonlocal or Gram-corrected maps remain possible. RF003's phrase "every common-space projection" is not fully decided and is not counted a second time. No assertion says that the source printed the exact tested map equation verbatim. The source's actual definitions, norm, twist, Haar factor and PW membership have been checked by exact locator.

MO028 extends already-proved ideal-return rows; the independent source-scope audit found zero wholly open primary-row closures there. MO029 evaluates traces on a proved conditional scope; MO030 gives a further sufficient class, while the general no-control question stays open. MO031 and MO032 give exact reciprocal-growth criteria with the positive branch supplied by A, without deciding the independent arithmetic growth condition. None of these is counted as additional movement. Newly created PI/MO rows, source audits, normalization checks and packaging are not movement. PI004, if still awaiting its complete readings at the review time, is not counted.

### Every currently open or qualified route

This table includes established conditional implications and exact equivalent criteria where an arithmetic antecedent, exceptional-width estimate, distinct original-domain identification, or source provenance remains. It records states; no antecedent is silently promoted.

| Row | Current state | Exact gate or next step |
|---|---|---|
"""
for row in qualified:
    esc = lambda s: s.replace("|", "/").replace("\n", " ")
    body += "| " + esc(row["id"]) + " | " + esc(row["state"]) + " | " + esc(
        (row["current_gate"] + " " + row["next_step"]).strip()) + " |\n"
body += """
### Main-question gates

1. **Masullo/Q and Dirichlet:** actual all-weight full-test finite Gram transport, slow-band asymptotic, boundary-jet accounting and source-profile comparison remain proved. FT002 still says that equality with unchanged geometry requires exactly empty upper deficiency; every positive width means own-sector RH. A supplies the rational/Dirichlet zero location explicitly. The canonical physical-cutoff/theta projector map is now refuted in both corrected and exact printed realizations, including genuine principal polar-free input/output. Any different intertwiner requires its own actual map statement. General-field local annular transport remains closed by GA001.
2. **Non-induced imaginary-quadratic character:** the full-test corrected trace formula and the completed-ideal nuclear source return are proved. MO028 gives the latter at all narrow widths with arbitrary compact smooth data, including boundary-zero widths. The full common matrix retains its dual half-plane premise or the checked finite/bounded-cluster boundary hypotheses. Exterior and deficient-boundary zeros obstruct it. The every-width criterion remains equivalent to own-character RH; no arithmetic deficiency vanishing is proved.
3. **Unrestricted inverse and quotient returns:** MO031 and MO032 characterize universal cutoff/test scopes by polynomial reciprocal growth on a generic line. A supplies the positive rational branch; no independent arithmetic decision is made. PR006–011 still require full local primary retention and polynomial canonical whole-quotient block costs. The general full-matrix sufficiency question with uncontrolled edge clusters remains open. TN001–002 is still an equivalent ambient S1 exhaustion criterion.
4. **S5:** beta=b+n is proved under R_B. Without it the strongest gate remains exclusion of the shared real zero in RB008's discriminant-aware interval, with normal-closure multiplicity at least9k. No new exclusion, compatible odd residual representation or positive-excess field has been produced.
5. **PF26:** the invoked algebraic proof audit, exact own analytic premise, complete bad-prime reduction and explicit single Kummer-Hecke residual list remain complete at their stated outside-input scope. The separate companion analytic proof is not claimed freshly audited.
6. **Input classification and frameworks:** all563 supplied finding rows remain classified with secondary premises. Missing original CX proof sources remain an explicit provenance limit. Nuclear source/quotient pairings retain the cote1 scans079–080 and111–112 interpretation. No faithful full-jet positivity, new motivic purity, or arithmetic consequence is inferred merely from scalar trace convergence.

No final package is triggered. Continue primarily on the actual original projection/domain identifications and arithmetic deficiency/cost gates, preserving the newly refuted canonical candidate and the remaining distinct maps. A new theorem is movement only if it decides a question already open at this review or strictly reduces one of these gates.
"""
with (root / "LEDGER.md").open("a") as f:
    f.write(body)

p = root / "README.md"
s = p.read_text()
start = s.rfind("Work remains active.")
assert start >= 0
s = s[:start] + "Work remains active. The sixth timed review records one decided pre-existing canonical-map subgate, with zero stalled reviews; it does not close the broad existence of different factorizations or reduce FT002. The next checkpoint is23:46UTC on21November /00:46Berlin on22November; the next movement review is00:31UTC /01:31Berlin on22November. Every included new proof has actual complete-reading records; source-statement inspection is distinguished from a complete primary-proof audit. Prior checkpoints remain immutable.\n"
p.write_text(s)
print(json.dumps({"review": 6, "timestamp": stamp, "question_rows": len(rows),
                  "qualified": len(qualified), "movement": True,
                  "witness": gate, "stalled_reviews": 0}))
