from pathlib import Path
from datetime import datetime, timezone
import hashlib, json, re

base = Path(__file__).resolve().parents[1]
candidate = base / "B_tame_irreducible_arbitrary_index_candidate.tex"
expected = "c4e6e1526fda7b26e930ba647855c6fa67758efd39817df991f9a66371ff9cfe"
raw = candidate.read_bytes()
assert hashlib.sha256(raw).hexdigest() == expected
preserved = base / "notes/B_tame_irreducible_arbitrary_index.prepromotion.tex"
assert not preserved.exists()
preserved.write_bytes(raw)
text = raw.decode()
text = re.sub(r"\\status\{Candidate[^}]*\}",
              lambda m: r"\status{Proved; full independent root and companion proof, original-source and exact-code audits passed.}", text)
text = text.replace("% Separate post-CP24 candidate. All statements await full independent audits.",
                    "% Proved after complete root and companion audits; exact candidate retained in notes/.")
old = "These are finite arithmetic checks of the proof, not formal-group\n+or pair constructions.".replace("\n+", "\n")
assert old in text
text = text.replace(old, "The complete independent root and companion audits passed; their\n+author-output-preserving reruns took\n+\\(2.895408538999618\\) and \\(2.5705544949887553\\) seconds,\n+respectively. These are finite arithmetic checks of the proof,\n+not formal-group or pair constructions.".replace("\n+", "\n"))
canonical = base / "B_tame_irreducible_arbitrary_index.tex"
canonical.write_text(text)
labels = re.findall(r"\\label\{([^}]+)\}", text)
assert len(labels) == 6 and r"\status{Candidate" not in text
stamp = datetime.now(timezone.utc).isoformat()
record = {
    "status": "PROVED", "promotion_utc": stamp,
    "canonical": "RESEARCH_SA15_work/agents/reduction_descent/B_tame_irreducible_arbitrary_index.tex",
    "audited_candidate_sha256": expected,
    "canonical_sha256": hashlib.sha256(canonical.read_bytes()).hexdigest(),
    "labels": labels,
    "root_audit": "../../outputs/root_B67_audit.json",
    "root_time": "2026-11-19T21:00:24.230908+00:00",
    "root_runtime_seconds": 2.895408538999618,
    "companion_audit": "../obstructions_crystals/B67_independent_audit.json",
    "companion_time": "2026-11-19T20:58:21.240887+00:00",
    "companion_final_supplement_time": "2026-11-19T21:01:36.372275+00:00",
    "companion_runtime_seconds": 2.5705544949887553,
    "author_runtime_seconds": 2.847146783999051,
    "scope": "For p>=5, mu_p and p-prime absolute ramification, actual p² torsion recovers the finite special inertia character of whole potentially supersingular height-two groups when residual inertia is irreducible over Fp. Reducible residual and p-divisible ramification remain outside this theorem."
}
(base/"outputs/B67_promotion.json").write_text(json.dumps(record,indent=2)+"\n")
with (base/"CHECK_EVENTS.tsv").open("a") as f:
    for label in labels:
        f.write("\t".join([stamp,label,"PROVED_FULL_AUDITS",record["scope"],
                           "B_tame_irreducible_arbitrary_index.tex;outputs/B67_promotion.json",
                           "Complete root and OC proof/original-source/exact-code PASS; final supplement checked; exact audited candidate and actual runtimes retained"])+"\n")
with (base/"STATUS_CURRENT.md").open("a") as f:
    f.write(f"\n## {stamp} — B67 promoted\n\n"
            "All six assertions in B_tame_irreducible_arbitrary_index.tex are proved after complete root and OC proof/source/code audits. "
            "The irreducible-residual actual p² comparison is now settled for every p>=5 and every p-prime absolute ramification with μp. "
            "All wild image sizes are handled in the same actual division field, with exact arbitrary-e break normalizations and the full additive root polynomial. "
            "Reducible residual and p-divisible ramification remain outside this theorem. Exact candidate, finite programs and all runtimes retained.\n")
print(json.dumps(record,indent=2))
