"""Retain the complete three-label actual exceptional-ratio proof audit."""
from pathlib import Path
from datetime import datetime, timezone
import hashlib
import json
import re

root = Path(__file__).resolve().parents[3]
own = root / "agents/obstructions_crystals"
source = root / "agents/monodromy/post_CP36_prime5_actual_exceptional_ratio_candidate.tex"
expected = "be70fa2a6c360c7b54b5b08478f4ca6f5fadd89451dcaf1d3eb61ca4ea8bd03c"
sha = lambda p: hashlib.sha256(p.read_bytes()).hexdigest()
assert sha(source) == expected
checks = {
    "lem:prime-five-common-wall-iff-ratio": (
        "The maximal Pfaffian gcd-one theorem gives codimension at least two for the dual "
        "rank-drop base locus. Since dQ=(sigma_i^2), every repeated factor would divide "
        "all sigma_i, so Q is squarefree. For E not proportional to Q, equal nonzero "
        "degrees imply a Q-component is not contained in E=0. Its generic open also "
        "avoids the Pfaffian base. At such y, s=sigma(y) is nonzero, B_y has rank four, "
        "and the exact polynomial composition tau(s)=E(y)y makes the adjugate s*tau^t "
        "nonzero. Alternation bounds rank M_s by four, so both ranks are exactly four; "
        "the actual left kernel is ky and Q=0 is the Euler wall equation. The converse "
        "is the fully audited exact PEW identity. Scalar normalization does not change "
        "ranks, kernels or wall equations. The simultaneous Frobenius-compatible index "
        "permutation i->2i exchanges c1 and c2, so the missing c1=0 chart reduces "
        "exactly to t=0, with a nonempty wall. No arbitrary linear coordinate change "
        "or inference from generic ambient nonvanishing is used."
    ),
    "prop:prime-five-actual-exceptional-ratio": (
        "The actual product line, global generation and type are the fully audited root "
        "double-cover construction, with its canonical generic curve-rank dependency. "
        "The natural geometric-generic branch module gives this same relative Lang "
        "image inside S5 because the ambient stable part is zero. The full abstract KWI "
        "proposition and its complete moving-kernel Artin-Schreier proof were freshly "
        "reread: on a nonempty common-rank wall, derivative rank is three, the actual "
        "Euler determinant has order one and stable rank is three, and the independent "
        "strict-henselian Artin-Schreier classes give the full elementary group of "
        "order eight. The proposition is stated for an arbitrary odd-dimensional "
        "alternating tensor, and the actual whole-space Euler criterion supplies its "
        "third hypothesis here. Restriction of the regular generic Lang cover to the "
        "dense smooth/sharp open preserves its image; no full-rank special-fibre "
        "comparison or smooth curve on the wall is needed. An elementary abelian "
        "group acting faithfully on five letters embeds in the product of its regular "
        "orbit images, whose total order is at most four. This excludes (Z/2)^3 in "
        "S5 and forces exactly the exceptional coefficient condition in any stated "
        "compatible theta basis."
    ),
    "rem:prime-five-actual-exceptional-ratio-scope": (
        "The conclusion is actual Cartier realization of the empty common wall, using "
        "the explicit product and previously certified exact identities. No secant "
        "variety identification, exact S5 image, classification of all type-(1,5) "
        "systems or contradiction to sufficiently-large powers is inferred. The "
        "retained typography delta only removes the literal plus before 'must'."
    ),
}
assert re.findall(r"\\label\{([^}]+)\}", source.read_text()) == list(checks)
now = datetime.now(timezone.utc).isoformat()
dependencies = [
    "agents/monodromy/Cartier_kernel_wall_inertia.tex",
    "agents/monodromy/mixed_degree_one_uniform_full_groups.tex",
    "agents/monodromy/prime_Heisenberg_rank.tex",
    "agents/monodromy/primitive_prime_generic_rank.tex",
    "agents/monodromy/post_CP36_prime5_exceptional_wall_candidate.tex",
    "notes/primitive_elliptic_double_cover_candidate.tex",
]
record = {
    "status": "FULL INDEPENDENT PROOF PASS",
    "actual_utc": now,
    "reviewer": "/root/obstructions_crystals",
    "candidate": str(source.relative_to(root)),
    "candidate_sha256": expected,
    "entire_candidate_actually_read": True,
    "labels": {key: {"verdict": "PASS", "checked": value} for key, value in checks.items()},
    "fresh_full_dependency_reads": [
        "Complete Cartier_kernel_wall_inertia.tex, including all hypotheses of its abstract proposition.",
        "Complete lem:moving-kernel-full-root-inertia-candidate and proof in mixed_degree_one_uniform_full_groups.tex; the strict-henselian independent Artin-Schreier classes were rederived.",
        "Complete primitive_prime_generic_rank.tex and the actual root double-cover candidate during the preceding audit.",
        "Complete post_CP36_prime5_exceptional_wall_candidate.tex and its exact identities; full isolated checker audit is linked.",
    ],
    "bounded_dependency_reread": "Complete gcd-one ending of thm:prime-Heisenberg-birational-radical, following its earlier full proof/source/code audit.",
    "dependency_hashes": {p: sha(root / p) for p in dependencies},
    "linked_full_audits": [
        "agents/obstructions_crystals/prime5_exceptional_wall_independent_audit.json",
        "agents/obstructions_crystals/primitive_elliptic_double_cover_independent_audit.json",
        "agents/obstructions_crystals/primitive_double_cover_certificate_independent_audit.json",
        "agents/obstructions_crystals/prime_Heisenberg_independent_audit.json",
    ],
    "exact_typography_delta_read": "agents/monodromy/notes/prime5_actual_ratio_typography/typography.diff",
    "new_numerical_run": None,
    "new_external_source_opening": None,
    "scope": "Three complete written assertions checked. Earlier exact polynomial and permutation certificates are dependencies, not new computations; no secant or geometric classification inference.",
    "candidate_unchanged": sha(source) == expected,
}
rp = own / "prime5_actual_exceptional_ratio_independent_audit.json"
with rp.open("x") as f:
    json.dump(record, f, indent=2)
    f.write("\n")
with (own / "CHECK_EVENTS.tsv").open("a") as f:
    for label, detail in checks.items():
        f.write("\t".join([now, label, "independent-full-proof-audit",
                            str(source.relative_to(root)),
                            "Entire written consequence and actual local-inertia dependencies read",
                            "PASS: " + detail, str(rp.relative_to(root))]) + "\n")
print(json.dumps({"status": record["status"], "actual_utc": now,
                  "candidate_sha256": expected, "record": str(rp.relative_to(root)),
                  "labels": len(checks)}))
