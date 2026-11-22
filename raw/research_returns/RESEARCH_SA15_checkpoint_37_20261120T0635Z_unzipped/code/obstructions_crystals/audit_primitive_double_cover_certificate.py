"""Read-completed exact certificate audit with an unchanged isolated rerun."""
from pathlib import Path
from datetime import datetime, timezone
import hashlib
import json
import shutil
import subprocess
import sys
import time

root = Path(__file__).resolve().parents[3]
own = root / "agents/obstructions_crystals"
program = root / "code/verify_primitive_double_cover_counterexamples.py"
output = program.with_suffix(".output.json")
run = own / "outputs/primitive_double_cover_certificate_independent_run"
rp = own / "primitive_double_cover_certificate_independent_audit.json"
assert not run.exists() and not rp.exists()
sha = lambda p: hashlib.sha256(p.read_bytes()).hexdigest()
before = {str(p.relative_to(root)): sha(p) for p in (program, output)}
assert before[str(program.relative_to(root))] == "d525e0eb86fa0de2161e36fd5e02adebd8f80823b6b08fb14d4cc5a8f0400e20"
assert before[str(output.relative_to(root))] == "d86d00ad4ba932776e73ec38deba09f25507c83382195b4be89275531e423005"
run.mkdir(parents=True)
copy = run / program.name
shutil.copyfile(program, copy)
assert sha(copy) == sha(program)
start = time.perf_counter()
proc = subprocess.run([sys.executable, str(copy)], cwd=run, capture_output=True, text=True)
elapsed = time.perf_counter() - start
(run / "stdout.txt").write_text(proc.stdout)
(run / "stderr.txt").write_text(proc.stderr)
assert proc.returncode == 0, proc.stderr
author = json.loads(output.read_text())
actual = json.loads(copy.with_suffix(".output.json").read_text())
assert author["status"] == actual["status"] == "PASS"
omit = {"actual_utc", "runtime_seconds"}
assert {k:v for k,v in author.items() if k not in omit} == {k:v for k,v in actual.items() if k not in omit}
after = {str(p.relative_to(root)): sha(p) for p in (program, output)}
assert before == after
now = datetime.now(timezone.utc).isoformat()
checks = [
    "The exact GF(2) homogeneous cubic and its three partials are reconstructed. Their common affine-cone zero is only the origin, proving the explicit projective smoothness uniformly, not by sampled points.",
    "The universal intersection matrix verifies L_m^2, fibre degree and the destabilizing effective divisor square. Explicit unimodular left/right integer matrices reconstruct the full Smith form diag(1,-2m-1). These identities hold symbolically for all m.",
    "Every nonzero vector of F2^n modulo the all-one line is represented exactly once by a vector with last coordinate zero. The subset/complement weight is checked for every representative and every adjacent transposition at the six certified n. Counts and binomial subcover sizes are exact; the n=3 row is explicitly not a proper-image counterexample.",
    "All 120 S5 permutation matrices on the actual four-dimensional quotient are separately constructed, checked invertible and distinct. All 14400 multiplication pairs agree with permutation composition; the explicit quotient orientation and last-basis-vector all-one relation are correct.",
    "All GL orders use the exact product formula and all strict comparisons are made as integers. The reported generic ranks are explicitly inputs from the proved geometric theorem, not conclusions of a finite test. Ampleness, stability, global generation, sheaf exactness and Galois identification remain the separately audited full written proofs.",
]
record = {
    "status": "FULL CODE AND UNCHANGED ISOLATED RERUN PASS",
    "actual_utc": now,
    "reviewer": "/root/obstructions_crystals",
    "complete_program_and_full_author_output_actually_read": True,
    "written_proof_audit": "agents/obstructions_crystals/primitive_elliptic_double_cover_independent_audit.json",
    "written_proof_sha256": "43b704d52a72fe1c4b7174746dfe34be30dd5f83dea521466e472d81b2829e17",
    "author_hashes_before": before,
    "author_hashes_after": after,
    "checks": checks,
    "counts": actual["counts"],
    "run": {
        "exact_copy": str(copy.relative_to(root)),
        "exact_copy_sha256": sha(copy),
        "output": str(copy.with_suffix(".output.json").relative_to(root)),
        "internal_runtime_seconds": actual["runtime_seconds"],
        "wall_runtime_seconds": elapsed,
        "exit_code": proc.returncode,
        "all_mathematical_output_identical": True,
        "excluded_metadata_fields": sorted(omit),
    },
    "source_scope": "No additional external source opening needed for this finite/algebraic supplement. The complete primary-source proof audit is linked separately.",
    "scope": "Exact computable identities and finite permutation-module certificate only; no geometric theorem is inferred from finite enumeration.",
}
with rp.open("x") as f:
    json.dump(record, f, indent=2)
    f.write("\n")
with (own / "CHECK_EVENTS.tsv").open("a") as f:
    for label in ["lem:root-elliptic-double-cover-lines", "thm:root-primitive-prime-permutation-counterexamples", "cor:root-primitive-permutation-Lang-components"]:
        f.write("\t".join([now, label, "exact-certificate-independent-rerun",
                            str(program.relative_to(root)),
                            "Entire unchanged standalone code/output read and isolated rerun",
                            "PASS; all mathematical output identical; geometric proof retained separately",
                            str(rp.relative_to(root))]) + "\n")
print(json.dumps({"status": record["status"], "actual_utc": now,
                  "runtime_seconds": actual["runtime_seconds"],
                  "record": str(rp.relative_to(root)), "counts": actual["counts"]}))
