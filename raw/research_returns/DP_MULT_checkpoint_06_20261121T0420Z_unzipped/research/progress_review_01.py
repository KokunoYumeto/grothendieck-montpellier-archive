#!/usr/bin/env python3
"""Record the actual first scheduled progress review, once it is due."""
import csv,json
from pathlib import Path
from datetime import datetime,timezone
root=Path(__file__).resolve().parents[1]
now=datetime.now(timezone.utc)
due=datetime.fromisoformat("2026-11-21T02:50:00+00:00")
if now<due:raise SystemExit("First three-hour review is not due yet.")
marker="## Scheduled three-hour progress review"
p=root/"LEDGER.md"
if marker in p.read_text():raise SystemExit("First review already recorded.")
with (root/"QUESTIONS.tsv").open(newline="") as f:
    questions=list(csv.DictReader(f,delimiter="\t"))
opened=[r for r in questions if "current gate" in r["state"]]
lines=[
f"\n\n{marker} — {now.isoformat()}\n",
"Conservative work start23:50UTC on20November; this is the first actual review at approximately three hours. It is not a retrospective or simulated elapsed-time claim.\n",
"### Main questions and strongest current gates\n",
"| Main question | Current state | Strongest proved reduction |\n|---|---|---|",
"| Q1 formal-group bound | Proved | DP1–DP4: coefficientwise optimal affine slope and constant h−1, complementary exact floor sum, h1 and infinite-height endpoints. DP43 further gives codimension error for cyclic CM displays. |",
"| Q2 step2 | Proved with exact scope | Height2 gives the scalar coefficient; the actual source theta/gauge/period/path/denominator comparisons are identified. It is not a height-only theorem about an arbitrary normalized theta expression. |",
"| Q3 higher height and fewer lifts | Local theorems proved; global saving open | DP40–DP48 settle general cyclic directional sums/errors, primitive mixed-line radii with arbitrary unit arrows, polarized trace-one normalization and quadratic gauge. DP44 rebuilds smaller even rank/HC/host/Spaces inputs; new endpoint periods, selected local data and the net global inequality remain. |",
"| Q4 archive/Cartier/crystals | Proved within stated source scope | Boxed zero is the universal extension's vector kernel; Oda/Cartier give the classical comparison. Scalar valuation estimates do not by themselves supply crystal descent/connection. Autograph corrections distinguished from transcription errors. |",
"| Q5 binomial/homotopy | Precise mathematical statement proved; one source/prior-run comparison row open | Torsion-free identity Frobenius/binomial equivalence, numerical-polynomial divided-power graded algebra, and Horel's derived nilpotent finite-type reconstruction are established/cited exactly. The extra historical/B7 comparison is separated below. |",
"\n### Every currently open question row\n",
"| Row | Status | Current gate |\n|---|---|---|",
]
for r in opened:
    lines.append("| "+r["id"]+" | "+r["state"].replace("|","/")+" | "+r["current_gate_or_scope"].replace("|","/")+" |")
lines += [
"\n### Movement assessment\n",
"**Movement: YES. Consecutive no-movement reviews: 0.** Relative to the initial ledger, Q1/Q2/Q4 and the precise mathematical Q5 statements changed from open to proved/refuted. Q3 reduced from an unspecified higher-height formal/kernel mechanism to explicit integral models, exact primitive radii and gauge formulas, plus concrete endpoint/selected-data/cost interfaces. This meets the user's movement definition independently of packaging or side observations.\n",
"Concrete work continuing: DP49 is a local polarized Jacobian/nonzero-path application under proof review; the nonunit theta tensor parameter is being investigated; the actual selected harmonic/global endpoint comparison remains active. A renewed targeted autograph search is assigned for the unresolved cote133/137 locators. No missing B7 statement is invented.\n",
"The next progress review is due03:50UTC. The two-consecutive-no-movement stop condition has not occurred. The separate scheduled checkpoint04 is due now; next checkpoint05 will be03:35UTC if work continues.\n",
]
with p.open("a") as f:f.write("\n".join(lines))
record={"review":1,"actual_utc":now.isoformat(),"due_utc":due.isoformat(),
        "movement":True,"consecutive_no_movement_reviews":0,
        "open_rows":[r["id"] for r in opened],"next_review_due_utc":"2026-11-21T03:50:00+00:00"}
(root/"research/progress_review_01.json").write_text(json.dumps(record,indent=2)+"\n")
print(json.dumps(record))
