"""Mark the manuscript as a final incomplete record after a verified stop review.

This performs administrative status edits only. It refuses to act before the
dated two-negative-review stopping receipt exists.
"""
from pathlib import Path
from datetime import datetime, timezone
import hashlib
import json

root = Path(__file__).resolve().parents[1]
receipt_path = root / "logs/scheduled_review_16.json"
receipt = json.loads(receipt_path.read_text())
assert receipt["stop_rule_reached"] is True
assert receipt["movement"] == "NO" and receipt["dry_streak"] == 2
assert datetime.now(timezone.utc) >= datetime.fromisoformat(receipt["actual_utc"])
manifest_path = root / "logs/final_status_edits.json"
if manifest_path.exists():
    raise SystemExit("Refusing to repeat the final-status edits")

records = []
def change(relative, old, new):
    path = root / relative
    data = path.read_bytes()
    text = data.decode()
    assert text.count(old) == 1, (relative, old)
    revised = text.replace(old, new).encode()
    path.write_bytes(revised)
    records.append({"file": relative,
                    "before_sha256": hashlib.sha256(data).hexdigest(),
                    "after_sha256": hashlib.sha256(revised).hexdigest(),
                    "old": old, "new": new})

change("RESEARCH_SA06_paper.tex",
       r"\textbf{INCOMPLETE --- work in progress}",
       r"\textbf{INCOMPLETE --- final record; stopped at review 16}")
change("RESEARCH_SA06_paper.tex",
       "Research manuscript: incomplete",
       "Final research record: incomplete")
anchor = "\\paragraph{F.2a (Proved correction): two normalizations in the supplied Tate survey.}"
notice = r"""\paragraph{Final stopping decision.}
We stopped mathematical research at the scheduled 20:50 UTC review on
19 November 2026, after two consecutive reviews without a change in an
open main-row status or a proved reduction to a strictly smaller main gate.
The mathematical programme remains \textbf{INCOMPLETE}.
The final report and dated ledger retain all 41 Part and Lead rows,
including every unresolved gate. Subsequent compilation, visual inspection
and archiving implement delivery and do not constitute mathematical movement.
Dated intermediate notes are retained with their original scope and are
superseded only where a later certified statement explicitly says so.

"""
change("sections/F_state.tex", anchor, notice + anchor)
record = {"utc": datetime.now(timezone.utc).isoformat(),
          "stop_receipt": str(receipt_path.relative_to(root)),
          "mathematical_changes": False,
          "edits": records}
manifest_path.write_text(json.dumps(record, indent=2) + "\n")
print(json.dumps(record, indent=2))
