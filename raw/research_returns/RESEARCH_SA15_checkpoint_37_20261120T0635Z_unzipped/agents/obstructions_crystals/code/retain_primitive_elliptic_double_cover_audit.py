"""Retain a completed independent written-proof and primary-source audit."""
from pathlib import Path
from datetime import datetime, timezone
import hashlib
import json
import re

root = Path(__file__).resolve().parents[3]
own = root / "agents/obstructions_crystals"
candidate = root / "notes/primitive_elliptic_double_cover_candidate.tex"
expected = "43b704d52a72fe1c4b7174746dfe34be30dd5f83dea521466e472d81b2829e17"
sha = lambda p: hashlib.sha256(p.read_bytes()).hexdigest()
assert sha(candidate) == expected
checks = {
    "lem:root-elliptic-double-cover-lines": (
        "The affine and infinite-point smoothness of y^2+y=x^3, the regular exact differential dx, "
        "Cartier zero and f(E)=f(A)=0 were independently rederived. All three elliptic divisors "
        "have square zero and pairwise intersection one. The product-positive divisor plus nef "
        "Gamma is ample. The exact integral polarization matrix has determinant 2m+1 and Smith "
        "invariants (1,2m+1); integer unimodular operations act on E^2, so this is the actual "
        "odd polarization type even for the supersingular product. Fibrewise degree two gives "
        "q_*L0 rank two, degree one and R1=0. A destabilizing line of degree at least one would "
        "give an effective divisor of square 2-4a<0. Thus V0 and its twists are stable. "
        "Serre duality applied to the negative-slope dual twist gives H1(V_m(-b))=0 for every "
        "m>=1 and b. Surjective restriction to the full degree-two fibre system proves actual "
        "global generation. No very-ampleness or numerical-only global-generation assertion is used."
    ),
    "lem:root-double-cover-branch-module": (
        "The Artin-Schreier sequence gives H1_et(E,F2)=H2_et(E,F2)=0 because F=0 on H1(O_E). "
        "A connected unramified quadratic cover would contradict the first vanishing. The unique "
        "quadratic involution defines the actual map 1+iota. Off the branch set its kernel is "
        "the diagonal F2 and its image is the sum-coordinate F2; at a branch point its stalk "
        "is one F2 with pullback an isomorphism and image zero. This proves the exact j_! "
        "sequence even in wild characteristic two. The full original finite-direct-image "
        "proof applies to every abelian etale sheaf, with no coefficient invertibility "
        "hypothesis. Leray and the two exact sequences give the natural branch-permutation "
        "quotient F2^B/F2*1. Every arrow is canonical for the actual cover, so the resulting "
        "isomorphism is geometric-generic Galois equivariant. No finite-etale reduced branch "
        "scheme over an original parameter open is assumed or needed."
    ),
    "thm:root-primitive-prime-permutation-counterexamples": (
        "The full canonical generic-rank theorem was freshly reread, including its smooth-member "
        "construction and actual Frobenius-compatible hypersurface sequence. The explicit lines "
        "satisfy every hypothesis for n=5,7,11,13,17, so the geometric generic curve has genus "
        "n+1 and p-rank n-1. Projection is a finite degree-two map of a smooth connected curve; "
        "pure inseparability is excluded either by universal-homeomorphism invariance of etale "
        "cohomology or by the degree-two Frobenius function-field argument and genus. The "
        "natural branch module has exactly n branch points. Artin-Schreier and fixed-vector "
        "exactness identify this same Galois module with the actual relative Lang module "
        "because the ambient stable part is zero. The generic Galois image equals the finite "
        "local-system image on the integral normal smooth/sharp open and persists on dense "
        "opens. The permutation representation is faithful for odd n>=3; the exact order "
        "comparison is strict starting at 120<20160 and remains so by the displayed GL ratio."
    ),
    "cor:root-primitive-permutation-Lang-components": (
        "Nonzero vectors modulo constants correspond to subset/complement pairs, with a unique "
        "representative of size 1 through (n-1)/2 since n is odd. These actual monodromy-invariant "
        "sets have the stated binomial sizes and give open-and-closed subcovers. The lower "
        "component count does not assume transitivity or exact S_n image."
    ),
    "rem:root-primitive-permutation-scope": (
        "The examples are actual ample globally generated primitive systems on a fixed "
        "supersingular product. Their elliptic-fibre degree remains two, so none is very ample. "
        "They are not powers of a fixed embedding line, do not refute the sufficiently-large "
        "hypersurface assertion and do not contradict proved principal-cube cases. No exact "
        "monodromy subgroup, actual exceptional theta ratio, common-maximal-rank wall or "
        "closure of the general A.4 gate is inferred."
    ),
}
assert re.findall(r"\\label\{([^}]+)\}", candidate.read_text()) == list(checks)
now = datetime.now(timezone.utc).isoformat()
dependency_paths = [
    "agents/monodromy/primitive_prime_generic_rank.tex",
    "agents/obstructions_crystals/A4_primitive_type_1_3_full_group.tex",
    "agents/obstructions_crystals/A4_odd_Cartier_evaluation.tex",
    "agents/monodromy/prime_Heisenberg_rank.tex",
]
record = {
    "status": "FULL INDEPENDENT PROOF AND PRIMARY-SOURCE PASS",
    "actual_utc": now,
    "reviewer": "/root/obstructions_crystals",
    "candidate": str(candidate.relative_to(root)),
    "candidate_sha256": expected,
    "entire_candidate_actually_read": True,
    "labels": {label: {"verdict": "PASS", "checked": check} for label, check in checks.items()},
    "fresh_complete_dependency_reread": "agents/monodromy/primitive_prime_generic_rank.tex",
    "previous_complete_internal_audits": [
        "agents/obstructions_crystals/primitive_prime_generic_rank_independent_audit.json",
        "agents/obstructions_crystals/prime_Heisenberg_independent_audit.json",
        "agents/obstructions_crystals/prime_Heisenberg_cocycle_delta_audit.json",
    ],
    "dependency_hashes": {p: sha(root / p) for p in dependency_paths},
    "fresh_original_source_reads": [
        {
            "source": "The Stacks Project, Section 59.55, Vanishing of finite higher direct images",
            "url": "https://stacks.math.columbia.edu/tag/03QN",
            "retrieved_ref": "turn358347391view0",
            "actually_read": "Complete Lemma 59.55.1, Proposition 59.55.2 and Lemma 59.55.3 statements and proofs, lines 19-54.",
            "checked": "Strict henselian cofinal etale neighbourhoods make sections equal the closed stalk; a finite scheme over a strict henselization splits into strictly henselian local schemes. Higher direct images vanish for every abelian etale sheaf, including F2 in characteristic two. Finite base change is also checked on the exact geometric-fibre stalk formula.",
            "scope": "No claim to have freshly opened every cross-referenced henselian algebra or general topos theorem, and no PDF-image viewing claimed.",
        },
        {
            "source": "The Stacks Project, Section 59.63, The Artin-Schreier sequence",
            "url": "https://stacks.math.columbia.edu/tag/0A3J",
            "retrieved_ref": "turn358347391view1",
            "actually_read": "The exact Artin-Schreier sequence and complete Lemmas 59.63.1-59.63.3 with proofs, lines 18-49.",
            "checked": "Etale/coherent comparison, semilinear F-minus-one surjectivity via the finite standard-smooth polynomial algebra, and invariance of fixed vectors after algebraically closed base extension. The explicit supersingular elliptic H2 vanishing only needs F-1=-1 on coherent H1.",
            "scope": "The later general top-cohomology vanishing proofs are not imported or claimed as fully read here.",
        },
    ],
    "numerical_run": None,
    "numerical_scope": "No new numerical program is needed or claimed. Matrix, intersection, dimension and group-order identities were checked directly in the proof.",
    "candidate_unchanged": sha(candidate) == expected,
    "scope": "Five complete written assertions, their actual local-system identification and exact primary-source hypotheses checked. No new general large-degree result or actual exceptional-coefficient realization claimed.",
}
path = own / "primitive_elliptic_double_cover_independent_audit.json"
with path.open("x") as f:
    json.dump(record, f, indent=2)
    f.write("\n")
with (own / "CHECK_EVENTS.tsv").open("a") as f:
    for label, check in checks.items():
        f.write("\t".join([now, label, "independent-full-proof-primary-source-audit",
                            str(candidate.relative_to(root)),
                            "Entire written proof, actual geometric dependency and full original Stacks proofs read",
                            "PASS: " + check, str(path.relative_to(root))]) + "\n")
print(json.dumps({"status": record["status"], "actual_utc": now,
                  "candidate_sha256": expected, "record": str(path.relative_to(root)),
                  "labels": len(checks), "new_numerical_run": None}))
