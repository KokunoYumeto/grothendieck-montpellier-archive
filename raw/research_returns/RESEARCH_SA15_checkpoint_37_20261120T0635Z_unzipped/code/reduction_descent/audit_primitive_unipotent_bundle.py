"""Author-output-preserving independent run and retained audit record."""
from pathlib import Path
from datetime import datetime, timezone
import hashlib
import json
import subprocess
import sys

own = Path(__file__).resolve().parents[1]
author = own.parent / "obstructions_crystals"
source = author / "post_CP26_unipotent_bundle_candidate.tex"
program = author / "code/primitive_unipotent_transition_checks.initial.py"
author_output = author / "code/primitive_unipotent_transition_checks.output.json"
sha = lambda p: hashlib.sha256(p.read_bytes()).hexdigest()
before = sha(author_output)
copied = own / "code/independent_primitive_unipotent_transition.py"
assert not copied.exists()
copied.write_bytes(program.read_bytes())
result = subprocess.run([sys.executable, str(copied)], capture_output=True, text=True)
(own / "outputs/independent_primitive_unipotent_transition.stdout.txt").write_text(result.stdout)
(own / "outputs/independent_primitive_unipotent_transition.stderr.txt").write_text(result.stderr)
assert result.returncode == 0, result.stderr
check = json.loads(copied.with_suffix(".output.json").read_text())
assert check["status"] == "PASS" and len(check["identities"]) == 17
assert sha(author_output) == before
now = datetime.now(timezone.utc).isoformat()
record = {
    "status": "FULL_PROOF_SOURCE_CODE_PASS",
    "actual_utc": now,
    "candidate": str(source),
    "candidate_sha256": sha(source),
    "labels": ["lem:DE-A3-primitive-unipotent-candidate", "rem:DE-A3-primitive-unipotent-scope-candidate"],
    "proof_scope": [
        "Entire candidate independently read and rederived, including relative complementary Frobenius types, actual global O/O filtration and transition cocycle.",
        "Norm transition, gamma=(nu^c)^*kappa^(2), dual etale kernel and H1 isomorphism, differential of polarization and actual local-index split/nonsplit distinction checked.",
        "Entire prior integral local-polarization-block proof and positive-index bundle dependency reread.",
        "No restricted cup nonvanishing, generic rank conclusion or global Frobenius-class assertion inferred from the finite checker."
    ],
    "primary_source_read": {
        "source": str(author / "sources/edixhoven_geer_moonen_AV.txt"),
        "locator": "Theorem7.5 and Proposition7.6, both full proofs, printedp100",
        "method": "Retained original full text read; no fresh web retrieval or page-image inspection claimed."
    },
    "program_source_sha256": sha(program),
    "copied_program": str(copied),
    "independent_output": str(copied.with_suffix(".output.json")),
    "independent_runtime_seconds": check["elapsed_seconds"],
    "identities": check["identities"],
    "author_output_sha256_before": before,
    "author_output_sha256_after": sha(author_output),
    "author_output_preserved": True,
    "cosmetic_correction": "Literal comma exponents repaired by author before final audit; exact prior candidate retained by author."
}
dest = own / "outputs/independent_primitive_unipotent_bundle_audit.json"
dest.write_text(json.dumps(record, indent=2) + "\n")
with (own / "CHECK_EVENTS.tsv").open("a") as stream:
    for label in record["labels"]:
        stream.write("\t".join([now, label, "INDEPENDENT_FULL_PASS", "Typed unipotent-bundle O/O extension and actual local-index split criterion; no cup nonvanishing inferred.", str(dest.relative_to(own)), "Full proof and primary AV7.5/7.6 proofs read; entire17-identity code independently rerun with author output preserved"]) + "\n")
print(json.dumps({"status": record["status"], "actual_utc": now, "candidate_sha256": record["candidate_sha256"], "elapsed_seconds": check["elapsed_seconds"], "audit": str(dest)}))
