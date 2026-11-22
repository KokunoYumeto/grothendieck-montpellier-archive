#!/usr/bin/env python3
"""Full written-audit record and unchanged, author-preserving B92 rerun."""
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
candidate = root / "agents/reduction_descent/B_residual_wild_crossing_candidate.tex"
program = root / "agents/reduction_descent/code/verify_residual_wild_crossing.py"
author_output = program.with_suffix(".output.json")

def digest(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()

assert digest(candidate) == "54786c9ec226ed8855471c5c4eacaa5efd2927ec3aefee76aa9762bd5c221453"
before = {str(p.relative_to(root)): digest(p) for p in (candidate, program, author_output)}
destination = owner / "outputs/independent_B92_environment"
destination.mkdir(parents=True, exist_ok=False)
for path in (candidate, program):
    shutil.copy2(path, destination / path.name)
copied = destination / program.name
start = time.perf_counter()
process = subprocess.run([sys.executable, str(copied)], cwd=destination,
                         capture_output=True, text=True)
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
labels = ["lem:B-RD92-tame25", "lem:B-RD92-parahoric",
          "lem:B-RD92-common-high", "thm:B-RD92-crossing", "rem:B-RD92-scope"]
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
        "Entire five-label candidate and entire verifier read. All twelve degree-five point-field translation cases rederived using prime normalized coordinate valuations; both column evaluations are therefore surjective without a higher torsion comparison.",
        "Full B87 shared-diagonal argument and B88 fixed-coordinate alternatives reread. Distinct tame weights force the two off-diagonal axes; a dimension-three image has the same actual diagonal quotient, with incompatible breaks72 versus24 or66. Full additive25 image and all four coordinate breaks follow.",
        "Actual quotient lattice basis(e1/5,e2), its four jointly surjective additive characters, upper-triangular first layer, fifth powers and the opposite-weight terminal-character argument give precisely the stated parahoric image of order5^8.",
        "Both parameter-index orders rechecked: (5,45) identifies original residual/diagonal characters with A12/A22; (15,95) identifies them after the basis swap with A21/A11. The two actual fields are distinct by character independence.",
        "Common-high proof rederived in full: one-break degree-five additive-polynomial obstruction, last-line exclusion by B87, both strict first-change rows, mixed strict inequality, t=r2 endpoint including its cutoff inequality, and the surviving t=r1 formula. No cancellation or absent-prime-term case omitted.",
        "Primitive25-point orbit has degree125 over L and yields an actual Galois degree25 extension over R; its high-line-killing quotient is exactly D22R/R. The same field has coordinate-forced break72 and compositum/subgroup break336 in (15,95), while the (5,45) test consistently gives24.",
    ],
    "dependencies_freshly_reread": [
        "B60 complete fixed-coefficient break lemma and Newton argument",
        "B87 complete coefficient lemma, shared actual diagonal-field proof, and first-layer exclusion",
        "B88 entire point-field and quotient upper/lower-numbering proof",
        "B91 entire promoted high-quotient comparison, crossing parameters, and scope",
    ],
    "previously_audited_dependencies_reused": [
        "B69 exact quotient-level identity, valuation formula and descent, fully reread during this turn's B91 audit",
        "B90 actual subgroup/quotient ramification conventions and earlier Colmez proof audit",
    ],
    "source_scope": "No fresh external original-source opening claimed. Entire invoked internal coefficient and field arguments were read and rederived; no Hasse-Arf shortcut used.",
    "computation_scope": observed["scope"],
    "limitation": "Only the actual crossing(15,95) is excluded. No existence or exclusion of(5,45), no change to the both-large or irreducible branches, and no unrestricted index closure.",
}
(owner / "outputs/independent_B92_residual_wild_crossing_audit.json").write_text(
    json.dumps(record, indent=2) + "\n")
with (owner / "CHECK_EVENTS_post_CP16.tsv").open("a") as stream:
    for label in labels:
        stream.write("\t".join([label, now, "/root/monodromy", record["status"],
            "Entire proof/program read; exact actual-field identification and every common-high boundary rederived; unchanged isolated rerun and author hashes preserved; no remaining-row realization inferred."]) + "\n")
print(json.dumps(record, indent=2))
