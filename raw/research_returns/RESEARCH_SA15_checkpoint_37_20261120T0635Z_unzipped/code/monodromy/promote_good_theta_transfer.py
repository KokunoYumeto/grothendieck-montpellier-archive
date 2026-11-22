from pathlib import Path
import datetime
import hashlib
import json

root = Path(__file__).resolve().parent.parent
candidate = root / "nonordinary_good_theta_norm_transfer_candidate.tex"
source = candidate.read_text()
assert hashlib.sha256(candidate.read_bytes()).hexdigest() == "cc6cac954b0326be99593ad298e3d943361e8a5e70cc7a570eeb9592f7b57e46"
source = source.replace(
    "% Post-CP24 research candidate. No assertion here is promoted until full audit.",
    "% Post-CP24 theorem; exact pre-promotion candidate is retained separately.",
).replace(
    "\\status{Candidate; full proof submitted for independent audit.}",
    "\\status{Proved and independently checked.}",
).replace(
    "\\textup{[Candidate.]}",
    "\\textup{[Proved; independent audits passed.]}",
)
source = source.replace(
    "symbolic norm-step assembly.\n\\end{remark}",
    "symbolic norm-step assembly. The parent completed a full independent "
    "proof audit at 20:52:36 UTC. The obstruction/crystal reviewer completed "
    "a full independent proof and dependency audit at 20:47:34 UTC, with "
    "the final typography and exact-source hash checked at 20:52:17 UTC. "
    "Both audits reread the complete graph, gluing and finite-Lang "
    "dependencies; neither claims a new numerical experiment for this "
    "symbolic extension.\n\\end{remark}",
)
canonical = root / "nonordinary_good_theta_norm_transfer.tex"
assert not canonical.exists()
canonical.write_text(source)
now = datetime.datetime.now(datetime.timezone.utc).isoformat()
labels = [
    "lem:good-theta-uniform-node-product-candidate",
    "prop:good-theta-uniform-gluing-candidate",
    "thm:good-theta-odd-norm-step-candidate",
    "cor:f0-three-five-degree-groups-candidate",
    "rem:good-theta-norm-transfer-scope-candidate",
]
record = {
    "status": "PROMOTED",
    "actual_timestamp_utc": now,
    "candidate": candidate.name,
    "candidate_sha256": hashlib.sha256(candidate.read_bytes()).hexdigest(),
    "canonical": canonical.name,
    "canonical_sha256": hashlib.sha256(canonical.read_bytes()).hexdigest(),
    "labels": labels,
    "root_audit": "../../outputs/root_good_theta_transfer_audit.json",
    "companion_audit": "../obstructions_crystals/good_theta_norm_transfer_independent_audit.json",
    "scope": "Conditional good-nodal-theta norm transfer for arbitrary odd kernels; unconditional fixed f0 degrees 3^i 5^j and sums of two such degrees. No all-odd/all-even or fixed-f1 degree-five assertion.",
    "preservation": "Exact final candidate and the earlier literal-typo draft/diff remain retained; only statuses, initial comment and completed-audit paragraph changed on promotion.",
}
(root / "outputs/good_theta_transfer_promotion.json").write_text(json.dumps(record, indent=2) + "\n")
with (root / "post_CP16_notes.md").open("a") as handle:
    handle.write(
        "\n## " + now + " — Good-theta norm transfer promoted\n\n"
        "Promoted nonordinary_good_theta_norm_transfer.tex after the full "
        "root and obstruction/crystal proof audits. Exact candidate retained; "
        "the literal plus-sign typo draft and exact correction diff are in history/. "
        "The promoted proof includes the node product, all type hearts, actual "
        "source block, and clopen rank-drop comparison for an arbitrary good "
        "odd theta kernel. Combined with the proved uniform five-self-isogeny, "
        "it proves every fixed two-rank-zero degree 3^i5^j and sums of two "
        "such degrees. Fixed two-rank-one degree five remains a separate gate. "
        "No new finite experiment is used. Stable labels were preserved.\n"
    )
with (root / "CHECK_EVENTS_post_CP16.tsv").open("a") as handle:
    for label in labels:
        handle.write("\t".join([
            now, label, "promotion_after_full_root_OC_proof_audits", "PASS",
            "Arbitrary good odd theta kernel; fixed f0 degree semigroup and even sums; no new numerical inference",
            canonical.name,
        ]) + "\n")
print(json.dumps(record, indent=2))
