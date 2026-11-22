from pathlib import Path
from datetime import datetime, timezone
import hashlib, json, re

base = Path(__file__).resolve().parents[1]
candidate = base / "B_initial_tame_sector_candidate.tex"
expected = "950f85373f69014b75339d60735c757bfec1cb90576a0dd7d910d1d189709e7a"
raw = candidate.read_bytes()
assert hashlib.sha256(raw).hexdigest() == expected
audit = json.loads((base.parent/"obstructions_crystals/B68_independent_audit.json").read_text())
assert audit["candidate_sha256"] == expected
assert "PASS" in audit["status"].upper()
preserved = base / "notes/B_initial_tame_sector.prepromotion.tex"
assert not preserved.exists()
preserved.write_bytes(raw)
text = re.sub(r"\\status\{Candidate[^}]*\}",
              lambda m: r"\status{Proved; full independent root and companion proof, source and exact-code audits passed.}", raw.decode())
text = text.replace("% Separate post-CP24 candidate; depends on the fully written B67 candidate.",
                    "% Proved after complete root and companion audits; B67 is proved and exact candidates are retained.")
old = "The all-prime assertion is the preceding proof\n+and does not follow from this finite enumeration.".replace("\n+", "\n")
assert old in text
new = "The complete independent root and companion audits passed, with\n+author-output-preserving reruns in \\(1.9408804569975473\\)\n+and \\(2.1150716640113387\\) seconds, respectively.\n+The all-prime assertion is the preceding proof and does not follow\n+from this finite enumeration.".replace("\n+", "\n")
text = text.replace(old, new)
canonical = base / "B_initial_tame_sector.tex"
canonical.write_text(text)
labels = re.findall(r"\\label\{([^}]+)\}", text)
assert len(labels) == 6 and r"\status{Candidate" not in text
stamp = datetime.now(timezone.utc).isoformat()
record = {
    "status": "PROVED", "promotion_utc": stamp,
    "canonical": "RESEARCH_SA15_work/agents/reduction_descent/B_initial_tame_sector.tex",
    "audited_candidate_sha256": expected,
    "canonical_sha256": hashlib.sha256(canonical.read_bytes()).hexdigest(),
    "labels": labels,
    "root_audit": "../../outputs/root_B68_audit.json",
    "root_time": "2026-11-19T21:04:40.000334+00:00",
    "root_runtime_seconds": 1.9408804569975473,
    "companion_audit": "../obstructions_crystals/B68_independent_audit.json",
    "companion_time": audit.get("actual_utc"),
    "companion_runtime_seconds": 2.1150716640113387,
    "author_runtime_seconds": 2.3066381700045895,
    "scope": "Exact full B4 monodromy nu_min(p,t(p−1),2)=2 for every p>=5 and 2<=t<=p−1, perfect residue and mu_p, including p5/e16. No extension to p-divisible ramification or t>=p is inferred.",
    "correction_history": "Exact pre-field-typing candidate and diff retained; R-rational first-level module in the wild point field and finite special inertia spectra are explicitly typed."
}
(base/"outputs/B68_promotion.json").write_text(json.dumps(record,indent=2)+"\n")
with (base/"CHECK_EVENTS.tsv").open("a") as f:
    for label in labels:
        f.write("\t".join([stamp,label,"PROVED_FULL_AUDITS",record["scope"],
                           "B_initial_tame_sector.tex;outputs/B68_promotion.json",
                           "Complete root and OC proof/source/exact-code PASS; both precision corrections checked; exact candidate and runtime history retained"])+"\n")
with (base/"STATUS_CURRENT.md").open("a") as f:
    f.write(f"\n## {stamp} — B68 promoted: initial tame sector exact\n\n"
            "All six assertions in B_initial_tame_sector.tex are proved after complete root and OC proof/source/code audits. "
            "The exact full-monodromy height-two index is nu_min(p,t(p−1),2)=2 for every p>=5 and 2≤t≤p−1, including p5/e16. "
            "B67 supplies the arbitrary-e irreducible branch; actual high/low cyclic quotients close the reducible branch; square determinants use the actual-target Cartier bound. "
            "The next p5 indices e20 (wild absolute index) and e24 (prime-to-p boundary) remain separate. "
            "Exact candidates, field-typing corrections and all numerical outputs/runtimes are retained.\n")
print(json.dumps(record,indent=2))
