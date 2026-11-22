"""Refresh a noncreating package estimate including checkpoint06."""
from pathlib import Path
import subprocess
import time
import json
from datetime import datetime, timezone

root = Path(__file__).resolve().parents[1]
names = ["notes/geometry_final_package_estimate_cp06.json", "notes/geometry_final_package_plan_cp06.json", "logs/geometry_final_package_cp06_estimate_stdout.txt", "logs/geometry_final_package_cp06_estimate_stderr.txt", "logs/geometry_final_package_cp06_estimate.json"]
if any((root / n).exists() for n in names):
    raise SystemExit("Refusing to overwrite a CP06 estimate record")
argv = ["python", str(root / "code/geometry_final_package.py"), "--estimate", "--estimate-report", str(root / names[0]), "--plan-report", str(root / names[1])]
before = sorted(str(p) for p in root.parent.glob("*.zip"))
started = time.perf_counter()
result = subprocess.run(argv, capture_output=True, text=True)
elapsed = time.perf_counter() - started
after = sorted(str(p) for p in root.parent.glob("*.zip"))
(root / names[2]).write_text(result.stdout)
(root / names[3]).write_text(result.stderr)
record = {"utc": datetime.now(timezone.utc).isoformat(), "argv": argv, "exit_code": result.returncode, "elapsed_seconds": elapsed, "zip_paths_before": before, "zip_paths_after": after, "zip_path_set_unchanged": before == after, "archive_creation_mode_used": False, "mathematical_movement": False}
(root / names[4]).write_text(json.dumps(record, indent=2) + "\n")
if result.returncode == 0:
    estimate = json.loads(result.stdout)
    print(json.dumps({k: estimate[k] for k in ["checkpoint_count", "checkpoint_logical_entries", "current_logical_files", "canonical_regular_files", "estimated_total_archive_bytes", "estimated_with_reserve_bytes", "remaining_margin_bytes"] if k in estimate}, indent=2))
else:
    print(result.stdout)
    print(result.stderr)
print(json.dumps(record, indent=2))
raise SystemExit(result.returncode)
