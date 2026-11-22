"""Produce the immutable final ZIP only after the user's stopping rule is met."""
from datetime import datetime, timezone
from pathlib import Path
import json
import subprocess
import sys
import time

ROOT = Path(__file__).resolve().parents[1]
review = json.loads((ROOT / "notes/progress_review_state.json").read_text())
assert review["no_movement_streak"] >= 2
assert "final disposition" in (ROOT / "RESEARCH_SA22_report.md").read_text().lower()
output = ROOT / "code/root_timed_final_archive_output.json"
assert not output.exists()
started = time.perf_counter()
started_utc = datetime.now(timezone.utc).isoformat()
process = subprocess.run([sys.executable, str(ROOT / "code/make_checkpoint.py"), "final"],
                         text=True, capture_output=True, cwd=ROOT)
record = dict(started_utc=started_utc, seconds=time.perf_counter() - started,
              exit_code=process.returncode, stdout=process.stdout, stderr=process.stderr,
              review_number=review["review_number"], no_movement_streak=review["no_movement_streak"])
if process.returncode == 0:
    record["archive"] = json.loads(process.stdout)
output.write_text(json.dumps(record, indent=2) + "\n")
print(json.dumps(record, indent=2))
sys.exit(process.returncode)
