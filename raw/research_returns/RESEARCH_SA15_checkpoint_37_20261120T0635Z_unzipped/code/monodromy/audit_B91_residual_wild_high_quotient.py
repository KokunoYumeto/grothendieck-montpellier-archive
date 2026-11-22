#!/usr/bin/env python3
"""Preserved-author, unchanged isolated rerun after full written B91 audit."""
from datetime import datetime, timezone
from pathlib import Path
import hashlib
import json
import shutil
import subprocess
import sys
import time

root = Path(__file__).resolve().parents[3]
owner = root / "agents/monodromy"
candidate = root / "agents/reduction_descent/B_residual_wild_high_quotient_candidate.tex"
program = root / "agents/reduction_descent/code/verify_residual_wild_high_quotient.py"
author_output = program.with_suffix(".output.json")

def digest(p):
    return hashlib.sha256(p.read_bytes()).hexdigest()

assert digest(candidate) == "a4cdbaf120302a26842df27c6eef3f428ff81cef454c573a314d3a476410c065"
before = {str(p.relative_to(root)): digest(p) for p in (candidate, program, author_output)}
destination = owner / "outputs/independent_B91_environment"
destination.mkdir(parents=True, exist_ok=False)
for p in (candidate, program):
    shutil.copy2(p, destination / p.name)
copied = destination / program.name
start = time.perf_counter()
process = subprocess.run(
    [sys.executable, str(copied)], cwd=destination, capture_output=True, text=True
)
elapsed = time.perf_counter() - start
(destination / "stdout.txt").write_text(process.stdout)
(destination / "stderr.txt").write_text(process.stderr)
assert process.returncode == 0, process.stderr
observed = json.loads(copied.with_suffix(".output.json").read_text())
expected = json.loads(author_output.read_text())
ignored = {"actual_utc", "runtime_seconds"}
assert {k: v for k, v in observed.items() if k not in ignored} == {
    k: v for k, v in expected.items() if k not in ignored
}
assert observed["status"] == "PASS"
after = {str(p.relative_to(root)): digest(p) for p in (candidate, program, author_output)}
assert before == after
now = datetime.now(timezone.utc).isoformat()
labels = [
    "lem:B-RD91-first-break",
    "prop:B-RD91-divisibility",
    "prop:B-RD91-parameters",
    "thm:B-RD91-large",
    "rem:B-RD91-scope",
]
record = {
    "status": "FULL-INDEPENDENT-PROOF-CODE-PASS",
    "actual_utc": now,
    "auditor": "/root/monodromy",
    "candidate_sha256": digest(candidate),
    "labels": labels,
    "author_bytes_preserved": before == after,
    "original_hashes": before,
    "copied_program_sha256": digest(copied),
    "isolated_output": str(copied.with_suffix(".output.json").relative_to(root)),
    "program_runtime_seconds": observed["runtime_seconds"],
    "wall_runtime_seconds": elapsed,
    "all_mathematical_output_identical": True,
    "proof_checks": [
        "Actual common cyclic first-point field and prime-valuation equality versus unconditional inequality.",
        "All high-quotient cases, including B=e: actual p^3 to p^2 subgroup quotient, old-image valuation, rational quotient first level, and both-large reversed inequality.",
        "Normalized finite-character enumeration, exact crossing rows (5,45)/(15,95), and nontrivial wild action of both-large quotients.",
        "Actual u and v homomorphisms, opposite tame weights, first-layer sl2 from conjugation, fifth-power inclusion and order count.",
        "Invariant determinant functional vanishes on sl2; actual cyclotomic quotient equals the original residual field and has lower break576, contradicting the coordinate bound.",
    ],
    "dependencies_freshly_reread": [
        "B60 complete fixed-coefficient break lemma and proof",
        "B69 complete actual quotient lemma and proof, including equal slope and semilinear descent",
        "B82 complete first-wild Newton lemma and proof",
        "B84 complete one-prime tame parameter proposition and proof",
        "B86 complete cyclotomic field/break lemma and relevant traceless determinant proof",
    ],
    "source_scope": "No fresh external primary-source reading claimed. Complete internal cited proofs reread and rederived.",
    "computation_scope": observed["scope"],
    "limitation": "No construction or exclusion of either surviving layer shape and no unrestricted least-index closure.",
}
(owner / "outputs/independent_B91_residual_wild_high_quotient_audit.json").write_text(
    json.dumps(record, indent=2) + "\n"
)
with (owner / "CHECK_EVENTS_post_CP16.tsv").open("a") as stream:
    for label in labels:
        stream.write("\t".join([
            label, now, "/root/monodromy", record["status"],
            "Entire proof/program read; all actual quotient and cyclotomic boundaries checked; unchanged isolated run and author hashes preserved; no larger closure inferred."
        ]) + "\n")
print(json.dumps(record, indent=2))
