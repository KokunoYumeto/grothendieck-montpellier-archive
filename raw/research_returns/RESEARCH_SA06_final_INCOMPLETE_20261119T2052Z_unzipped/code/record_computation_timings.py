"""Supply missing wall-clock timings for the existing exact certificates.

This single rerun fills the requested reproducibility metadata.  It does not
broaden the mathematical test ranges.  Each program's own proof-scope warning
and full stdout are retained, together with interpreter and exit status.
"""
from concurrent.futures import ThreadPoolExecutor
from pathlib import Path
import json
import subprocess
import sys
import time

ROOT = Path(__file__).resolve().parents[1]
DEST = ROOT / "code" / "timing_runs"
DEST.mkdir(exist_ok=True)
PROGRAMS = [
    "code/check_local_cone.py",
    "agents/cycles/code/check_nori_counterexamples.py",
    "agents/frobenius/code/verify_c4_exterior.py",
    "agents/frobenius/code/verify_c4_prym_arithmetic.py",
    "agents/frobenius/code/orlov_surface_parity.py",
    "agents/real_weil/code/verify_local_picard.py",
]

def run(relative):
    path = ROOT / relative
    started = time.perf_counter()
    process = subprocess.run([sys.executable, str(path)], cwd=ROOT,
                             text=True, capture_output=True, timeout=90)
    elapsed = time.perf_counter() - started
    output = DEST / (relative.replace("/", "__") + ".txt")
    output.write_text(process.stdout + "\nSTDERR:\n" + process.stderr)
    return {"program": relative, "interpreter": sys.executable,
            "arguments": [], "working_directory": str(ROOT),
            "runtime_seconds": elapsed, "exit_code": process.returncode,
            "full_output": str(output.relative_to(ROOT))}

with ThreadPoolExecutor(max_workers=3) as pool:
    results = list(pool.map(run, PROGRAMS))
(ROOT / "code" / "computation_timing_output.json").write_text(json.dumps(results, indent=2))
print(json.dumps(results, indent=2))
if any(item["exit_code"] for item in results):
    raise SystemExit("A recorded certificate failed; inspect the retained output")
