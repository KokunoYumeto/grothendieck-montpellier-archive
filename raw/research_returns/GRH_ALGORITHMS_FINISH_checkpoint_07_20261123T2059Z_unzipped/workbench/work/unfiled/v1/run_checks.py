#!/usr/bin/env python3
"""Run the exact finite examples and compare source-bound expected outputs.

Usage: python3 run_checks.py [--record] [--include-probe]
Requires Python 3.10+ and SymPy for the r=5 check. --record is for preparing a
new, reviewed version: it replaces expected outputs. Normal verification never
changes them. Calculations execute in an isolated temporary program directory,
so generated side files do not alter the version being checked.
"""

from __future__ import annotations

import argparse
import concurrent.futures
import datetime as dt
import hashlib
import json
from pathlib import Path
import shutil
import subprocess
import sys
import tempfile


PROGRAMS = [
    "check_tang_17_3.py", "check_kummer_examples.py",
    "check_elliptic_17_3.py", "derive_cm_inputs.py", "check_cm_15_135.py",
    "verify_restricted_volcano.py", "verify_ordinary_quartic.py",
    "verify_supersingular_point.py", "check_sextic_cm_endpoint_17.py",
    "check_fixed_wild_r5.py", "verify_higher_three_power.py",
    "check_small_cofactor_cubic.py", "verify_fixed_cm_torsion.py",
]


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--record", action="store_true")
    parser.add_argument("--include-probe", action="store_true")
    parser.add_argument("--report", type=Path, default=Path("checks/latest_run.json"))
    args = parser.parse_args()
    root = Path(__file__).resolve().parent
    expected = root / "checks" / "expected"
    if args.record:
        expected.mkdir(parents=True, exist_ok=True)
    jobs = list(PROGRAMS)
    if args.include_probe:
        jobs.append("probe_cubic_routes.py")
    with tempfile.TemporaryDirectory(prefix="finite-field-checks-") as folder:
        temp = Path(folder)
        shutil.copytree(root / "programs", temp / "programs")

        def run(name: str) -> dict:
            started = dt.datetime.now(dt.timezone.utc).isoformat()
            command = [sys.executable, str(temp / "programs" / name)]
            if name == "probe_cubic_routes.py":
                command += ["--limit", "100000", "--output-prefix", "cubic_probe"]
            completed = subprocess.run(command, cwd=temp, capture_output=True,
                                       text=True, timeout=180)
            entry = {"program": name, "started_utc": started,
                     "finished_utc": dt.datetime.now(dt.timezone.utc).isoformat(),
                     "returncode": completed.returncode}
            if completed.returncode:
                entry["stderr"] = completed.stderr
                entry["passed"] = False
                return entry
            certificate = json.loads(completed.stdout)
            target = expected / (Path(name).stem + ".json")
            if args.record:
                target.write_text(json.dumps(certificate, indent=2, sort_keys=True) + "\n")
            entry["expected_matches"] = target.exists() and json.loads(target.read_text()) == certificate
            entry["program_sha256"] = certificate["program_sha256"]
            entry["scope"] = certificate["verification_type"]
            entry["statement_scope"] = certificate["statement_scope"]
            entry["passed"] = bool(entry["expected_matches"])
            for filename in ("elliptic_17_3_certificate.json", "cubic_probe.csv", "cubic_probe_summary.json"):
                side = temp / "programs" / filename
                owned = ((name == "check_elliptic_17_3.py" and filename.startswith("elliptic"))
                         or (name == "probe_cubic_routes.py" and filename.startswith("cubic")))
                if owned and side.exists():
                    entry.setdefault("side_output_sha256", {})[filename] = hashlib.sha256(side.read_bytes()).hexdigest()
                    if args.record and filename.endswith(".json"):
                        shutil.copyfile(side, expected / filename)
            return entry

        with concurrent.futures.ThreadPoolExecutor(max_workers=4) as pool:
            entries = list(pool.map(run, jobs))
    report = {"schema": "finite-example-suite/1", "mode": "record" if args.record else "verify",
              "python_version": sys.version.split()[0], "all_passed": all(x["passed"] for x in entries),
              "results": entries}
    output = args.report if args.report.is_absolute() else root / args.report
    output.parent.mkdir(parents=True, exist_ok=True)
    output.write_text(json.dumps(report, indent=2) + "\n")
    print(json.dumps({"all_passed": report["all_passed"], "checks": len(entries), "mode": report["mode"]}))
    return 0 if report["all_passed"] else 1


if __name__ == "__main__":
    raise SystemExit(main())
