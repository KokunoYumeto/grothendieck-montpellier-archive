"""Record review05 once, from the live register and immutable review04."""
from pathlib import Path
from datetime import datetime, timezone
import csv
import json
import re
import shutil

root = Path(__file__).resolve().parents[1]
now = datetime.now(timezone.utc)
assert now >= datetime(2026, 11, 21, 22, 31, tzinfo=timezone.utc)
stamp = now.isoformat()
with (root / "QUESTIONS.tsv").open(newline="") as f:
    rows = list(csv.DictReader(f, delimiter="\t"))
with (root / "evidence/review_04_questions.tsv").open(newline="") as f:
    old = {r["id"]: r for r in csv.DictReader(f, delimiter="\t")}
current = {r["id"]: r for r in rows}
gate = "Q-MA-LA-GENERALS"
assert "open" in old[gate]["state"]
assert "proved" in current[gate]["state"].lower()
assert "MA-GA-001" in str(current[gate])
assert not (root / "evidence/review_05_questions.tsv").exists()
shutil.copyfile(root / "QUESTIONS.tsv", root / "evidence/review_05_questions.tsv")

changes = []
for row in rows:
    prior = old.get(row["id"], {})
    for field in ["state", "finding_ids", "current_gate", "next_step"]:
        if prior.get(field, "") != row[field]:
            changes.append({"id": row["id"], "field": field,
                            "previous": prior.get(field, ""), "current": row[field]})
with (root / "evidence/review_05_changes.tsv").open("w", newline="") as f:
    wr = csv.DictWriter(f, fieldnames=["id", "field", "previous", "current"],
                        delimiter="\t", lineterminator="\n")
    wr.writeheader()
    wr.writerows(changes)

extra = {"Q-MA-SOURCE-BRIDGE", "Q-MA-LA-GLOBAL", "MA-Q1-RF002", "MA-Q2",
         "MA-Q1-HM001", "MA-Q1-HM002", "MA-Q3c", "MA-Q1-PR009", "MA-Q1-PR010",
         "MA-Q-MEY-narrow", "MA-Q1-PR007", "MA-Q1-PR003", "Q-MA-LD-FINITE",
         "MA-Q2-FQ006B", "MA-Q2-FQ-primes", "Q-MA-CAUSAL-001"}
qualified = [r for r in rows if r["id"] in extra or re.search(
    r"open|unproved|unresolved|conditional|partially|not established|gate|regime|unmodified|equivalent|antecedent",
    r["state"], re.I)]
reviews = json.loads((root / "evidence/movement_reviews.json").read_text())
assert len(reviews) == 4
reviews.append({
    "number": 5, "timestamp_utc": stamp, "movement": True,
    "consecutive_stalled_reviews": 0, "question_rows": len(rows),
    "open_or_qualified_rows_reviewed": len(qualified),
    "changed_or_new_rows_since_previous_review": len({r["id"] for r in changes}),
    "movement_witness": gate,
    "next_review_utc": "2026-11-21T23:31:00+00:00",
    "decision": "Continue. The previously open general-field annular-rate and nuclear-lift question is proved by MA-GA-001 on its original inherited LF source and physical norm cutoffs. No arithmetic gate reduction is claimed."
})
(root / "evidence/movement_reviews.json").write_text(json.dumps(reviews, indent=2) + "\n")

body = f"""\n\n## Timed movement review05 — {stamp}

Decision: **continue**. Genuine movement: **yes**. Consecutive reviews without movement: **0**. Next movement review: **2026-11-21 23:31 UTC /2026-11-22 00:31 Berlin**. Next scheduled checkpoint: **2026-11-21 23:01 UTC /2026-11-22 00:01 Berlin**. The complete {len(rows)}-row immutable snapshot is evidence/review_05_questions.tsv; every state/finding/gate/next-step change from review04 is in evidence/review_05_changes.tsv. A register change is not automatically mathematical movement.

### The sole movement witness counted

At review04, **Q-MA-LA-GENERALS** explicitly left general class groups, positive unit rank and arbitrary archimedean signatures open. MA-GA-001 now proves the annular rates and actual nuclear lift for every fixed number field, structural S and fixed smooth unitary compact character, on the coordinate-flat additive subspace with its inherited strict LF topology. The source has a continuous section and exactly the closed S-unit relation kernel. A single nuclear series returns the actual finite-cutoff operator to a fixed original stage; the same physical norm cutoffs have the stated XY and epsilonY rates. Author and both independent complete written-proof readings have passed. The final coordinate-change paragraph was separately read and retains the physical cutoffs with the explicit character twist. This decides the pre-existing row at its actual source scope. No equality with a separately interpreted printed projective tensor completion is asserted.

The ideal-trace evaluations and full-matrix refinements MO014–026 are not counted as closure of a formerly open primary row: the review04 trace-scope audit found that the relevant ideal endomorphism rows were already proved. The new exterior/boundary necessity results and every-width RH equivalences do not shrink FT002. GA002's newly documented scalar-estimate counterexamples, source reading, editorial reconciliation and packaging are likewise not additional movement witnesses. Any module still awaiting its complete reading remains outside checked paper integration.

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

1. **Masullo/Q and Dirichlet:** actual all-weight, full-test finite Gram transport, slow-band asymptotic, boundary-jet accounting and source-profile comparison are proved. The corrected full identity retains exactly FT002's upper-deficiency condition; all widths mean own-sector RH. The stipulated theorem A supplies rational/Dirichlet zero location explicitly. Original rate-independent and specified raw-domain routes remain refuted. The polar completion permits the full prime-bearing matrix under its explicit half-plane premise; polar source preservation fails. General-field local annular transport is now closed by GA001, while literal original finite-projection factorizations remain a separate identification problem.
2. **Non-induced imaginary-quadratic character:** the actual full-test trace formula, ideal-domain endomorphism and evaluated nuclear local-source return are proved at their stated regimes. The full common matrix is conditional on the dual half-plane premise; strict exterior zeros obstruct it on actual source inputs. The every-width operator condition is another equivalent own-character RH criterion. Neither that equivalence nor the local trace evaluation supplies arithmetic deficiency vanishing. Generic arbitrary-smooth and fixed-width boundary/no-margin sufficiency remain at their explicitly recorded scopes.
3. **Unregularized returns:** PR006–011 still require full local primary retention and polynomial growth of canonical whole-quotient block inclusion costs. Adaptive regularized returns are complete; they do not prove these arithmetic estimates. TN001–002 remains an equivalent ambient S1 exhaustion criterion, not a smaller gate.
4. **S5:** beta=b+n is proved under R_B. Without it, the strongest comparison gate remains exclusion of the shared real zero in RB008's discriminant-aware interval, with normal-closure multiplicity at least9k. RB009, RB010 and the inspected analytic converse/nonregular Galois routes yield no new exclusion and no positive-excess field.
5. **PF26:** the invoked algebraic proof audit, exact own analytic premise, complete bad-prime reduction and explicit single Kummer-Hecke residual list remain complete at their stated outside-input scope. The separate companion analytic proof is not claimed freshly audited.
6. **Input classification and frameworks:** all563 supplied finding rows remain classified with secondary premises. Missing original CX proof sources remain an explicit provenance limit. Nuclear source/quotient pairings retain the cote1 scans079–080 and111–112 interpretation; no faithful full-jet positivity or new motivic purity is inferred.

No final package is triggered. Continue primarily on the remaining actual original projection/domain identifications, arbitrary-smooth estimates and arithmetic deficiency/cost gates. A new theorem is movement only if it decides a question already open at this review or strictly reduces one of these gates.
"""
with (root / "LEDGER.md").open("a") as f:
    f.write(body)

p = root / "README.md"
s = p.read_text()
start = s.rfind("Work remains active.")
assert start >= 0
s = s[:start] + "Work remains active. The fifth timed review records closure of the pre-existing general-field annular-rate and nuclear-lift question, with zero stalled reviews. The next checkpoint is23:01UTC on21November /00:01Berlin on22November; the next movement review is23:31UTC on21November /00:31Berlin on22November. Every included new proof has actual complete-reading records; source-statement inspection is distinguished from a complete primary-proof audit. Prior checkpoints remain immutable.\n"
p.write_text(s)
print(json.dumps({"review": 5, "timestamp": stamp, "question_rows": len(rows),
                  "qualified": len(qualified), "movement": True,
                  "witness": gate, "stalled_reviews": 0}))
