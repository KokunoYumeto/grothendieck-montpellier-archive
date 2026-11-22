"""Record a manually assessed unchanged hourly review, never before its due time.

The fixed assertions deliberately reject this recorder if a source gate or the
mathematical-scope registry changes. Such a change requires a fresh substantive
assessment instead of silently counting another no-movement review.
"""
from datetime import datetime, timedelta, timezone
from pathlib import Path
from zoneinfo import ZoneInfo
import json
import sys
import time

ROOT = Path(__file__).resolve().parents[1]
number = int(sys.argv[1])
assert number in (5, 6)
began = time.perf_counter()
now = datetime.now(timezone.utc)
due = datetime(2026, 11, 19, 11, 4, tzinfo=timezone.utc) + timedelta(hours=number + 2)
assert now >= due, "Do not record an hourly review before its scheduled time."
output = ROOT / "code" / f"root_record_no_movement_review_{number:02d}_output.json"
snapshot = ROOT / "notes" / f"progress_review_{number:02d}_snapshot.json"
assert not output.exists() and not snapshot.exists()
previous = json.loads((ROOT / "notes/progress_review_state.json").read_text())
assert previous["review_number"] == number - 1
live_path = ROOT / "notes/live_source_requirements.json"
live = json.loads(live_path.read_text())
assert live["remaining"] == ["Pfluger1960", "Lieberman1968", "Fujiwara1995"]
gaps = json.loads((ROOT / "notes/live_mathematical_scope_gaps.json").read_text())
assert all(x["status"].startswith("closed:") for x in gaps)
assert all(x.get("closed_utc", "") < "2026-11-19T17:04:00" for x in gaps)
streak = previous["no_movement_streak"] + 1
stopped = streak >= 2
next_due = due + timedelta(hours=1)
next_text = ("None: two consecutive scheduled hourly reviews without movement require stopping."
             if stopped else next_due.strftime("%Y-%m-%d %H:%M UTC") + " (" +
             next_due.astimezone(ZoneInfo("Europe/Berlin")).strftime("%H:%M Europe/Berlin") + ")")
summary = ("No open requirement changed status and no main question reduced to a strictly smaller gate. "
           "Pfluger1960, Lieberman1968 and Fujiwara1995 remain unread in the prescribed original mathematical passages. "
           "The retained mathematical conclusions and their explicit limits are unchanged. "
           "Negative source searches, repeated proof checks, source-cache normalization, typesetting and packaging are not counted as movement.")
state = dict(review_number=number, review_time=now.strftime("%Y-%m-%d %H:%M:%S UTC"),
             review_time_client=now.astimezone(ZoneInfo("Europe/Berlin")).strftime("%Y-%m-%d %H:%M:%S Europe/Berlin"),
             scheduled_time=due.strftime("%Y-%m-%d %H:%M UTC"), movement=False,
             no_movement_streak=streak, summary=summary, next_review=next_text,
             open_requirements=previous["open_requirements"],
             documentation_limitation=previous["documentation_limitation"],
             counted_existing_row_changes=[], stopping_rule_met=stopped)
for path in [ROOT / "notes/progress_review_state.json", snapshot]:
    path.write_text(json.dumps(state, indent=2) + "\n")
live.update(updated_utc=now.isoformat(), next_review_utc=None if stopped else next_due.isoformat())
live_path.write_text(json.dumps(live, indent=2) + "\n")
gates = [
 ("A.1 / L2", "Unrestricted global isomorphisms and raw toric cut-isotopy descent are refuted. The geodesic convention has the exact support image and invertible tangent map; actual unequal toric seams have that image and signed-edge real-E-dimensional fibres. Full external cap shapes retain their matching condition; orbifold fundamental groups and low-complexity cases are treated."),
 ("A.2 / L3 / L4", "Fixed pointed compactification: radius injectivity, full support image, relative-growth Strebel limits, cusp norms and decorations, and the exact collar equation with a fully specified sign-changing counterexample. The moving-seam regularity audit found no new defect and changes no status."),
 ("A.3 / L5", "Corrected welding existence and removable-seam uniqueness, vertex compatibility, Jordan-arc cutting and both073 readings are proved in the stated scopes. The separate Pfluger original reading remains outstanding."),
 ("A.4", "The literal orange model is refuted. Its precise asymptotic replacement and the mixed cusp/boundary Teichmuller space with intrinsic length action are proved."),
 ("A.5 / L7", "The characteristic-not2 theorem, corrected proposition, characteristic5 counterexample, characteristic3 inertia and stack/coarse distinction are supplied."),
 ("A.6 / L6", "Framed reconstruction, model systems, existing-model tame specialization, intrinsic all-DVR tame category and corrected presentations are supplied. Wild-cover, nonsplit-node, chosen-fibre and strict-reconstruction-preservation overstatements have explicit counterexamples. General mixed-characteristic regular-model existence is not asserted."),
 ("A.7 / L9", "The real classification, corrected integral gluing/count, topology and H1 are proved and compared with the opened Alling-Greenleaf original passages."),
 ("B.1 / L1", "Characteristic-zero equality, the all-ell abelian-fourfold deduction with its explicit opened2026-preprint input, the precise domain and geometric members of the positivity argument, and the first-question quintic counterexample are supplied. Lieberman's original remains unread."),
 ("B.2", "The generic algebraically trivial divisor with nontorsion square and the exact Albanese-kernel replacement are proved through opened Mumford/Bloch inputs and the complete parameter-space argument."),
 ("B.3", "All28 subjects and9 Pour memoire headings retain individually scoped strongest proved formulations. Gabber's original main theorem was directly checked; Fujiwara's prescribed original remains unread. No blanket solution of motives or arbitrary positive-characteristic resolution is asserted."),
 ("C.1", "Filtered exp/log, the exact differential-automorphism criterion, locally nilpotent intertwining and arbitrary module-functor image/fibre tests are proved, including the stated non-Noetherian and non-finite-type cases."),
 ("C.2 / L8", "The literal017 group-system classification, finite ConditionK counterexample and exact replacement, non-forced extension and symmetry characterization are proved. Stronger021/022 assumptions are kept separate.")
]
entry = "\n\n## Substantive progress review" + str(number) + " — " + state["review_time"] + " / " + state["review_time_client"] + "\n\n"
entry += "**Movement: no. Consecutive reviews without movement:" + str(streak) + ".** " + summary + "\n\n"
entry += "### Every main-question gate at this review\n\n| Item | Strongest retained proved formulation / boundary |\n|---|---|\n"
entry += "\n".join("| " + item + " | " + gate + " |" for item, gate in gates) + "\n\n"
entry += "### Every remaining substantive open row\n\n| Requirement | Exact remaining gate | Status |\n|---|---|---|\n"
entry += "| Pfluger1960 | Original relevant mathematical passage in JIMS24(1960), pp401–412, with its hypotheses. | Unread; no new original text obtained. |\n"
entry += "| Lieberman1968 | Original relevant theorem and hypotheses in AJM90(1968), pp366–374. | Unread; later sources remain distinguished from the original. |\n"
entry += "| Fujiwara1995 | Original Cor6.6.4 or an equally explicit original comparison in Duke80(1995), pp15–57. | Unread; modern proofs and later author exposition do not close this requirement. |\n\n"
entry += "The access histories record each actually attempted route and its limit. A failed service or unread catalogue is not treated as a zero-result inventory, and an indexed absence is not an exhaustive absence claim. The smallest next substantive step for each row is an actual publicly available or otherwise authorized original passage, followed by a hypothesis-by-hypothesis comparison with the written result.\n\n"
entry += "The historical documentation limitation also remains: some early failed or administrative executions have no recorded duration. Their actual outputs and known/unknown timing scope are preserved; later runtimes are never substituted for an unmeasured earlier run. This limitation is not hidden by the three-source count.\n\n"
entry += ("**Stopping decision:** the user's two-consecutive-no-movement rule is now met. Stop substantive research and prepare the final package, retaining INCOMPLETE on the report's first line and every unmet requirement. No remaining row is relabelled as completed.\n" if stopped else "The stopping rule is not yet met. Continue within the existing authorization; the next scheduled review is " + next_text + ".\n")
with (ROOT / "PROGRESS_LEDGER.md").open("a") as handle:
    handle.write(entry)
record = dict(**state, seconds=time.perf_counter() - began)
output.write_text(json.dumps(record, indent=2) + "\n")
print(json.dumps(record, indent=2))
