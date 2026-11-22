"""Fourth substantive hourly review; compares actual gates with review03."""
from pathlib import Path
from datetime import datetime, timezone, timedelta
import csv, json

root = Path(__file__).resolve().parents[1]
state_path = root / "RUN_STATE.json"
state = json.loads(state_path.read_text())
now = datetime.now(timezone.utc)
start = datetime.fromisoformat(state["start_utc"])
due = start + timedelta(hours=6)
if now < due:
    raise SystemExit(f"Not due until {due.isoformat()}; no review written.")
if state.get("formal_reviews_completed") != 3:
    raise SystemExit("Requires exactly completed review03; no replay.")
rows = list(csv.DictReader((root/"QUESTIONS.tsv").open(), delimiter="\t"))
byid = {r["id"]: r for r in rows}
for name, expected in {"Q2af":"proved", "Q2ag":"refuted", "Q2aj":"proved",
                       "Q2ak":"refuted", "Q2al":"refuted", "Q5m":"refuted"}.items():
    assert byid[name]["state"] == expected, (name, byid[name]["state"])
open_rows = [r for r in rows if r["state"] in ("active", "open", "unchecked")]
text = f"\n## Formal movement review04 — {now.isoformat()}\n\n"
text += f"Fourth formal review, due {due.isoformat()}, compared substantively with review03 at15:40:56 UTC.\n\n"
text += """**Movement: YES. Consecutive reviews without movement: 0.** Both continuing main gates have strictly shrunk. On Q2i, D-BI-16 reduces inducing degree6 to the explicit Gaussian scalar-G34 model and eight necessary branch profiles; D-BI-17 removes degree7. D-R5-04 excludes one actual paired scalar-G33 Nielsen component by an original-field rank3 boundary, while retaining the other-component/descent gap. D-BI-18/18a provides normal-core and self-duality character bounds; D-BI-19 proves the required irreducible quasisimple central-product core exists in every primitive factorwise tensor-indecomposable degree at least5. D-BI-20 then forces a nonalternating Lie core to have field size at most27 in degree at least10. D-SPOR-01--03 excludes every sporadic normal central-product core, with complete central-cover, outer-normalizer and tensor-permutation coverage. On Q5i, SF-E816/a/b/c excludes signed two-cohomology models without simplicity, includes ordinary-gluable overlaps and arbitrary gaps, and excludes arbitrary amplitude with globally disjoint normalized class sets. These are proper reductions from the gates at review03. The pure-character three-degree counterexample, source-reading, arithmetic infrastructure, quantitative refinements of an already excluded model, and packaging are not counted as movement.\n\n"""
if byid.get("Q2am", {}).get("state") == "refuted":
    text += "HD-SPIN-01 additionally excludes essentially self-dual spin central-product cores2.A_n with n>=8; its exceptional degree24 rows are explicitly checked to be nonreal. This is a further reduction, not an all-alternating exclusion.\n\n"
if byid.get("Q2an", {}).get("state") == "refuted":
    text += "HD-SPIN-02 further removes the ESD hypothesis and excludes every faithful double-alternating spin central-product core with n>=8, by all66 exact local spectra and a quarter moving-rank bound. Ordinary alternating and small exceptional covers remain.\n\n"
text += "### Every open row at this review\n\n| Row | State | Strongest proved reduction and remaining gate |\n|---|---|---|\n"
for row in open_rows:
    text += f"| {row['id']} | {row['state']} | {row['finding_ids_or_current_gate'].replace('|',' / ')} |\n"
text += """
### Main-question gates

- **Target1, Gaussian principal fourfolds:** complete checked numerical detector and quadratic division bounds, with actual restricted polarization and the exact published rank4 locator. No new open gate.
- **Target2, every class-number-one sixfold determinant:** every split case, every Eisenstein determinant, and Gaussian signed determinant class3 remain numerically proved, with the supplied Perry input explicitly identified where used. Other nonsplit determinant classes remain open. The finite-cover gate is now restricted by the exact low-degree exceptional profiles and by the normal-core exclusions above; a new genuine balanced-RM eightfold seed remains the alternative. No remaining local profile is asserted to give descent, dominance or a detecting cycle.
- **Target3, Eisenstein split eightfolds through G34:** complete published-input reconstruction, actual rank16, integral cycle transfer and explicit fixed-order/polarization bound. No unrefereed Severn theorem is a premise.
- **Target4, natural imprimitive sources:** exact signature criterion, all-family nondominance and sharp n5 maxima15/14 are proved. D-NR01--04 gives a terminating exact procedure per specified Nielsen component and finite tables at each fixed group degree. Only the stated explicit examples and certificates have been run; no unbounded table is claimed.
- **Target5, actual non-curve object for n3 or n4:** the n3 request remains fulfilled by an actual checked perfect complex and its numerical coherent variant. For the remaining balanced-RM n4 route, stable locally free and locally free-factor semistable models, the specified simple positive-aggregate derived models, all ordinary-gluable two-cohomology-degree primitive projectively flat models, and globally disjoint arbitrary amplitude are excluded. Overlapping primitive class sets in at least3 degrees, unstable nonprimitive factors, singular or twisted objects, and sufficiently nonsimple constructions remain open. Finite arithmetic searches with no candidate and partial construction attempts are documented without being promoted to theorems.

Every newly counted theorem has a recorded whole-proof reading. Exact finite tables and published classification statements remain cited premises, distinct from new computations. Conditional Markman/032/Severn material and the supplied Perry/DEG_L categorical inputs preserve their original status. Source-integrity checking is not TeX compilation, and no successful compilation is claimed.

Continue research on the strictly smaller nonsplit-source and balanced-RM construction gates. The next formal review is due2026-11-21T17:38:55+00:00. No stopping rule is triggered.
"""
with (root/"LEDGER.md").open("a") as f:
    f.write(text)
state.update(last_review=now.isoformat(), formal_reviews_completed=4,
             consecutive_reviews_without_movement=0,
             next_review_utc=(start+timedelta(hours=7)).isoformat())
state_path.write_text(json.dumps(state, indent=2)+"\n")
print(json.dumps({"review":4,"time_utc":now.isoformat(),"movement":True,
                  "open_rows":[r["id"] for r in open_rows]}))
