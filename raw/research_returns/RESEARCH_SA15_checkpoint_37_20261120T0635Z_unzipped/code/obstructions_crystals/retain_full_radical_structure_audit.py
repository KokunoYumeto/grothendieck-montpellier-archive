"""Full independent direct proof audit, with the geometric-component scope repair."""
from pathlib import Path
from datetime import datetime, timezone
import hashlib
import json
import re

root = Path(__file__).resolve().parents[3]
own = root / "agents/obstructions_crystals"
candidate = root / "notes/A_full_radical_image_structure_candidate.tex"
expected = "9d2e7f21840ef9025ee5c9a22d2f7ef5614876ccf55866d028697f6786b1d7f3"
assert hashlib.sha256(candidate.read_bytes()).hexdigest() == expected
labels = re.findall(r"\\label\{((?:lem|prop|cor):[^}]+)\}", candidate.read_text())
assert len(labels) == 4
now = datetime.now(timezone.utc).isoformat()
record = {
    "status": "FULL INDEPENDENT PROOF PASS",
    "actual_utc": now,
    "candidate": str(candidate.relative_to(root)),
    "candidate_sha256": expected,
    "labels": labels,
    "proof_read_scope": "Entire final four-label candidate and exact geometric-component wording delta read. Every finite group step independently rederived. The current all-odd full-inertia theorem was fully independently audited immediately before this review, and the exact canonical odd-degree invariant-covector theorem and its odd-degree proof were freshly read for the application.",
    "checks": [
        "For the span W of the chosen nonzero covectors, select a basis from the chosen set. In V=K direct-sum X with its dual basis, the radicals contain every elementary shear X->K and every elementary row addition on X. These generate the complete pointwise stabilizer of K. When m=1, GL(X) is trivial and the shears alone give the whole stabilizer. When K=0, m=r>=2 and ordinary Gaussian elimination gives GL(V).",
        "The fixed space of that complete stabilizer is exactly K: for K nonzero any vector with nonzero X-coordinate is moved by a suitable shear; for K=0, GL_r(F2) fixes no nonzero vector because r>=2. The excluded r=1 case is necessary and correctly excluded in the statement.",
        "Conjugation takes U_ell to U_(ell composed with g^-1). Applying the first lemma to the entire orbit identifies its normal closure N with the full pointwise stabilizer of K=V^N. This makes K proper and G-stable, without replacing the normal closure by unrelated divisorial generators.",
        "The restriction map from the setwise stabilizer of K onto GL(K) has precisely N as kernel. A subgroup containing this entire kernel equals the full inverse image of its image H. Thus all three block entries h,A,B in FR5 vary independently, and actual block-diagonal lifts exist; no splitting obstruction or abstract-only isomorphism is being omitted. Conjugation on B is h B A^-1.",
        "The complete GL(X) action and all shears act transitively on V minus K, with exact size 2^r-2^dimK; on K the action is exactly H. Any invariant subspace containing a vector outside K contains K by shear differences and surjects to X, hence equals V. Therefore K is the unique maximal proper submodule, including K=0, where zero is the only proper submodule.",
        "For m=1 the quotient coordinate is a nonzero invariant covector. For m>=2, shear invariance forces every invariant covector to vanish on K, and the full GL(X) then kills its quotient functional. This proves the asserted converse even when K is nonzero; absence of invariant covectors alone cannot prove K=0.",
        "For K=0 the full inverse image is GL(V), which is irreducible and transitive on nonzero vectors. A nonzero proper K prevents both properties. The claimed four-way equivalence follows with no exception for r=2 or m=1.",
        "In the actual odd principal-cube system the fully audited wall theorem supplies a full radical in the geometric image, and the canonical invariant-covector theorem gives zero geometric invariant covectors. Therefore m>=2. The subspace K is intrinsic because it is the unique maximal proper G-submodule, independent of the initial radical chosen.",
        "The component-degree assertion is now explicitly made after algebraic closure and for geometric connected components, exactly matching geometric monodromy orbits. Arithmetic monodromy may merge smaller H-orbits inside K, so no unproved arithmetic component descent is claimed. The exact prior wording and correction diff were read and are preserved under notes/full_radical_scope_repair.",
        "The resulting exact parabolic form does not determine K or H and asserts no new full-image degree. In particular it does not infer connectivity from birationality of a Cartier kernel map or identify the normal closure with all geometric monodromy."
    ],
    "dependencies_read_scope": [
        "agents/monodromy/ppav_all_odd_full_root_inertia_candidate.tex: complete five-label audit retained separately at 02:42:18.498233 UTC",
        "sections/A_nonordinary_ppav_covectors.tex: exact entire-invariant-quotient theorem and its complete odd-degree argument",
        "notes/full_radical_scope_repair: exact before/after component-scope delta"
    ],
    "source_scope": "Direct finite-dimensional proof; no fresh external-source reading or external classification imported.",
    "numerical_scope": "No finite computation or numerical experiment needed or claimed.",
    "scope": "Exact group form and geometric orbit degrees once a full hyperplane radical is present. This classifies the remaining proper-image alternative but does not exclude it."
}
dest = own / "full_radical_image_structure_independent_audit.json"
with dest.open("x") as out:
    json.dump(record, out, indent=2)
    out.write("\n")
with (own / "CHECK_EVENTS.tsv").open("a") as out:
    for label in labels:
        out.write("\t".join([
            now, label, "independent_full_proof_audit", str(candidate.relative_to(root)),
            "Full pointwise stabilizer, edge cases, exact inverse image, canonical submodule and geometric orbit degrees",
            "PASS; proper-image alternative retained", str(dest.relative_to(root))
        ]) + "\n")
print(json.dumps({"status": record["status"], "actual_utc": now,
                  "record": str(dest.relative_to(root)), "candidate_sha256": expected}))
