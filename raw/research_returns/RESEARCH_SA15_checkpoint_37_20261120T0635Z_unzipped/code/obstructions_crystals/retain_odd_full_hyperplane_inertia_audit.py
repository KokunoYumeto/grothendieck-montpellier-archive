"""Retain the full independent typed proof audit; no numerical run is claimed."""
from pathlib import Path
from datetime import datetime, timezone
import hashlib
import json
import re

root = Path(__file__).resolve().parents[3]
own = root / "agents/obstructions_crystals"
candidate = root / "agents/monodromy/ppav_all_odd_full_root_inertia_candidate.tex"
expected = "0bb79d06ae2ec1a09d9ad1ac3b9cbad85d34621d91357129a4a9c5c11a4de8cf"
assert hashlib.sha256(candidate.read_bytes()).hexdigest() == expected
labels = re.findall(r"\\label\{((?:lem|prop|thm|cor|rem):[^}]+)\}", candidate.read_text())
assert len(labels) == 5
now = datetime.now(timezone.utc).isoformat()
record = {
    "status": "FULL INDEPENDENT PROOF PASS",
    "actual_utc": now,
    "candidate": str(candidate.relative_to(root)),
    "candidate_sha256": expected,
    "labels": labels,
    "proof_read_scope": (
        "Entire stable five-assertion candidate read. The complete finite-Heisenberg symmetrizer "
        "proof, complete central Q/Pfaffian lemma, exact symmetry-compatible addition gauge and "
        "TCM5 cross-block proof, non-two-torsion theorem and outgoing isotropic descent were "
        "freshly read. The entire canonical common-incidence and local-wall proofs were "
        "freshly reread. The strict-henselian Artin-Schreier proof was fully independently "
        "read in the retained 01:54:54 local-wall audit; it is reused through that canonical "
        "lemma, without claiming another fresh source opening or numerical rerun here."
    ),
    "checks": [
        "The symmetric theta splitting is a finite Heisenberg splitting. Its coefficient-square representation equals the contragredient in the actual bases e_i and e_i^(2), so the equivariant map is literally e_i^(2) -> e_i*. Full tensor symmetry is unchanged in this fixed basis. At central rank eight the left and right kernel coordinate vectors are s, and the actual Euler wall is sum s_i^3.",
        "The exact TCM5 identity gives cross contraction c_(u-v)(a) s_(u+v) after i=2u,j=2v, up to a common nonzero scalar. Every nontrivial odd character has P^2 != O, so its Moore determinant is a nonzero polynomial. The separately fully audited universal Fermat theorem excludes the same Fermat cubic as a factor.",
        "For multiplication by the original s, Q^2=P and phi_M(u)=Q give the second basis e_j(z+2u) and target basis e_k^(2)(z'+F(u)). The balanced substitution w=z+u,a=-u keeps e_i(z) exactly as the first input. The matrix entry is c_(k-j)(-u) s_(2k-j)=c_(k-j)(-u) s_(-(k+j)). Its only variable change is inversion of the F3^2 index, preserving sum s_i^3. No arbitrary change of theta coordinates or parameter-dependent independent row gauges is introduced.",
        "The relative-Frobenius target is M^(2)Q^(2), whose pullback is M^2P. The fixed two-rank-one shift a_0 affects only the Moore coefficient vector. All translation and square-isomorphism ambiguities at the fixed parameter are a common nonzero scalar and cannot alter nonvanishing on the Fermat cubic.",
        "The central Pfaffian cubic q is nonzero and not proportional to the Fermat cubic by the complete earlier four-parameter coefficient argument. The Fermat cubic is smooth and geometrically integral. Its dense q != 0 open can therefore be intersected with finitely many nonempty multiplication and dual-cross determinant opens. The total multiplication rank is 8+9(n-1)=N-1, its unique left kernel is supported on the trivial target block, and the dual rank is 8+18(n-1)/2=N-1 for that very same left kernel.",
        "The resulting wall point belongs to the maximal common-rank open U_max, not to the Frobenius-bijective open. Its existence does not require a smooth zero divisor. This distinction avoids falsely intersecting the wall with the smaller common-incidence good open where the relative determinant is nonzero.",
        "For the entire universal hypersurface, H^1(A,L^-1)=0 and the nonzero evaluation W* tensor O(-1) -> O give a locally free relative H^1 quotient equal to the Euler bundle. The cohomology sequence is valid even at singular members; evaluation is everywhere surjective, so no unwanted R^2 term persists. Multiplication/Cartier duality gives the actual regular transpose restriction M_s^t:ann(s^[2])->ann(s).",
        "The local-wall proposition applies on U_max. Its derivative identifies d kappa with the nondegenerate form on W/ks; the wall is smooth reduced and its Euler determinant has order one. Restriction of the etale kappa has derivative rank N-2. The squared-frame lemma forces stable rank N-2, and the already fully audited strict-henselian Artin-Schreier argument yields the entire hyperplane radical of order 2^(N-2).",
        "The whole-space coherent model and the smooth-member model give the same generic finite Lang representation. On the nonempty Frobenius-bijective open, restriction to a dense smooth-member open preserves every connected finite etale cover: over a normal integral base such a cover is integral and its nonempty open remains connected. Thus the divisorial subgroup belongs to the smooth-family image even if the chosen wall component parametrizes singular curves. No stable-fibre specialization across a rank drop is assumed.",
        "For every fixed odd d, the actual outgoing isotropic etale quotient has degree d^2 and a symmetric principal descendant M_0 with 3dTheta=pi*(M_0^3). The target remains nonordinary. Applying N=9d^2 yields the precise geometric subgroup order 2^(9d^2-2), including d=1. No arithmetic descent stronger than containment of the geometric subgroup is asserted.",
        "The scope correctly leaves connectedness of the nonzero Lang cover, irreducibility, normal generation, and full global monodromy open. A full hyperplane radical alone does not exclude the retained parabolic countermodels."
    ],
    "dependencies_freshly_read": [
        "agents/monodromy/ppav_theta_cartier_symmetrizer.tex: entire theorem and proof",
        "agents/monodromy/nonordinary_ppav_uniform_Q_inertia.tex: entire central Q/Pfaffian lemma and proof",
        "agents/monodromy/ppav_twisted_Cartier_Moore.tex: entire symmetric gauge, TCM5 cross identification, non-two-torsion theorem and odd quotient corollaries",
        "agents/obstructions_crystals/A4_common_Cartier_incidence.tex: entire four-assertion proof",
        "agents/monodromy/Cartier_kernel_wall_inertia.tex: entire three-assertion proof"
    ],
    "other_retained_dependency_audits": [
        "agents/obstructions_crystals/Cartier_kernel_wall_independent_audit.json",
        "outputs/root_Moore_Fermat_full_audit.json",
        "agents/reduction_descent/outputs/independent_Moore_Fermat_full_audit.json"
    ],
    "source_scope": "No new original-source opening claimed. All new geometry is directly proved using the fully audited canonical theta, coherent-cohomology, and local-inertia lemmas.",
    "numerical_scope": "No numerical experiment or new checker rerun needed or claimed for this five-assertion geometric deduction.",
    "scope": "Uniform nonempty common Cartier wall and full local hyperplane-radical containment for every fixed nonordinary odd principal-cube system. No full global image theorem."
}
dest = own / "odd_full_hyperplane_inertia_independent_audit.json"
with dest.open("x") as out:
    json.dump(record, out, indent=2)
    out.write("\n")
with (own / "CHECK_EVENTS.tsv").open("a") as out:
    for label in labels:
        out.write("\t".join([
            now, label, "independent_full_proof_audit", str(candidate.relative_to(root)),
            "Exact fixed theta coordinates, nonempty common wall, whole-space Euler model and generic inertia transfer",
            "PASS; full local radical only", str(dest.relative_to(root))
        ]) + "\n")
print(json.dumps({"status": record["status"], "actual_utc": now, "record": str(dest.relative_to(root)), "labels": labels}))
