from pathlib import Path
from datetime import datetime, timezone
import hashlib, json, re

base = Path(__file__).resolve().parents[1]
candidate = base / "B_middle_tame_quotient_candidate.tex"
expected = "e1b6906c0382565e8fe42e16377cfb0aaececaafda30ebe2a9c23ab2c52f32b2"
raw = candidate.read_bytes()
assert hashlib.sha256(raw).hexdigest() == expected
preserved = base / "notes/B_middle_tame_quotient.prepromotion.tex"
assert not preserved.exists()
preserved.write_bytes(raw)
text = raw.decode()
text = re.sub(r"\\status\{Candidate[^}]*\}",
              lambda m: r"\status{Proved; full independent root and companion proof, source and exact-code audits passed.}",
              text)
text = text.replace("% Separate post-CP23 candidate. No conclusion follows from finite row checks alone.",
                    "% Proved after full root and companion audits; exact candidate retained in notes/.")
text = text.replace("at 20:40:55 UTC. These checks are supplementary to the all-prime proof.",
                    "at 20:40:55 UTC. The complete independent root and companion audits "
                    "passed, with author-output-preserving reruns in "
                    "$0.8864672490017256$ and $0.7995483489939943$ seconds, "
                    "respectively. These checks are supplementary to the all-prime proof.")
canonical = base / "B_middle_tame_quotient.tex"
canonical.write_text(text)
labels = re.findall(r"\\label\{([^}]+)\}", text)
assert len(labels) == 5
assert r"\status{Candidate" not in text
stamp = datetime.now(timezone.utc).isoformat()
record = {
    "status": "PROVED",
    "promotion_utc": stamp,
    "canonical": "RESEARCH_SA15_work/agents/reduction_descent/B_middle_tame_quotient.tex",
    "audited_candidate_sha256": expected,
    "canonical_sha256": hashlib.sha256(canonical.read_bytes()).hexdigest(),
    "labels": labels,
    "root_audit": "../../outputs/root_B66_audit.json",
    "root_time": "2026-11-19T20:54:39.825891+00:00",
    "root_runtime_seconds": 0.8864672490017256,
    "companion_audit": "../obstructions_crystals/B66_independent_audit.json",
    "companion_time": "2026-11-19T20:52:17.669675+00:00",
    "companion_runtime_seconds": 0.7995483489939943,
    "author_runtime_seconds": 0.8840610159968492,
    "scope": "Exact nu_min(p,(p^2-1)/2,2)=2 for every p>=5, full B4 monodromy setting, perfect residue and mu_p. Both actual high and low stable cyclic quotients are used. B67 and the wider initial sector remain separate candidates."
}
(base / "outputs/B66_promotion.json").write_text(json.dumps(record, indent=2) + "\n")
with (base / "CHECK_EVENTS.tsv").open("a") as f:
    for label in labels:
        f.write("\t".join([stamp, label, "PROVED_FULL_AUDITS",
                           record["scope"], "B_middle_tame_quotient.tex;outputs/B66_promotion.json",
                           "Complete root and OC proof/source/code PASS; exact candidate preserved; both author-preserving runtimes retained"]) + "\n")
with (base / "STATUS_CURRENT.md").open("a") as f:
    f.write(f"\n## {stamp} — B66 promoted\n\n"
            "All five assertions in B_middle_tame_quotient.tex are proved after complete root and OC proof/source/code audits. "
            "The exact full-monodromy height-two index is nu_min(p,(p²−1)/2,2)=2 for every p>=5. "
            "The integral high/low quotient argument and common point-field comparisons are explicit; no finite prime sample proves the theorem. "
            "The wider initial tame sector and arbitrary-index irreducible lemma remain separate B67/B68 candidates. "
            "Exact audited source, all outputs and actual runtimes are preserved.\n")
print(json.dumps(record, indent=2))
