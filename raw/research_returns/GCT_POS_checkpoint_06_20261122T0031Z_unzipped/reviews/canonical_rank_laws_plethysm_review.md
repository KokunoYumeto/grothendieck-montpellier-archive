# Independent whole-proof review of R-NEW-002

Reviewer: `/root/plethysm_proof`, GPT-6 Astra Pro, effort not exposed. Date: 21 November 2026 UTC.

**Outcome: PASS.** I read the complete `branches/root/canonical_rank_laws.tex` and the entire inherited R-031 report `outer_five_canonical_rank_law.md`. I also read the annihilator definition (K.2) and the displayed critical injection (K.28) in `canonical_boundary_ranges.md`. The actual requested annihilators are the kernels of the reverse grid maps; no calculation of the larger common-polarization module is required once those kernels are zero.

## Map identification and rank laws

The nested averaged tensor inclusions and quotient maps are adjoint for the stated evaluation pairings. The grid permutation transposes to its inverse, so the dual map is precisely the reverse grid map, with no missing scalar. The conversion from a multilinear-weight map to all Schur multiplicity maps is valid by Schur–Weyl duality: every Schur functor of degree N has a nonzero multilinear weight in dimension N, and the same multiplicity matrix occurs in every dimension.

The fourth-degree law uses invertibility at (4,4), McKay propagation in the correct direction, and transpose duality. The low cases n=2,3 satisfy Sra's bound with outer parameter a=n and b=4. The fifth-degree law uses the injective (5,6) base, the eight multiplicity-one defects at (5,5), fourth-degree injectivity at (4,5), and the two low cases from b=5. All parameter inequalities and all eight partitions agree with the cited sources. Shapes exceeding the vector-space dimension are correctly omitted. The zero and identity cases are treated consistently.

## Primary input checks and exact replay

Opened and read Cheung, Ikenmeyer, and Mkrtchyan, *Symmetrizing tableaux and the 5th case of the Foulkes conjecture*, arXiv:1509.03944, map definition on p.2 and Theorem6(a),(b) on p.3. Their injective (5,6) map and exact (5,5) kernel are the canonical tensor-grid map used here. Their original large matrices remain cited published computations; I did not repeat them.

Opened Ikenmeyer, *On McKay's propagation theorem for the Foulkes conjecture*, arXiv:1509.04957, map definition and Theorem1.3, p.2. The propagation direction matches both applications. This review checked the primary theorem statement; it does not claim an additional independent rereading of that paper's entire proof.

Opened Jacob's 2004 dissertation at its primary RWTH URL. Checked Definition4.1.1, p.92, the collapsed-matrix convention in Definition1.1.11, p.9, and the identification and determinant of B42, p.99. The averaged multilinear map is 24^−3 times the transverse zero-one matrix. Invertibility of right multiplication by that element gives its inverse in the unital adjacency algebra, hence invertibility in its faithful matrix representation. Reran the supplied 43×43 table with exact Bareiss elimination and separate modular Gaussian eliminations: determinant 2^223·3^67; residues82,15,6627 modulo101,1009,10007. Receipt: `jacob_plethysm_replay.json`. Original orbital enumeration and table extraction were not repeated. Müller–Neunhöffer's §4 final paragraph explicitly attributes the fourth-square calculation to Jacob.

Independently read all of Sra's Lemma2.1 and Theorem1.3 proof, §§2.1–2.2, pp.3–5, in the primary preprint retrieved from https://hexagonmath.org/pdf/2610.00724v1. The sl₂-string norm bound is correct. The first derivative sequence has positive degree excess through its final step; the induction uses b−r≥(r−1)²; and each whole polarization block has degree excess at least r when b≥r². All spectator variables are retained and every claimed operator coefficient is nonzero. This verifies the limited surjectivity input used here independently of a statement-level inherited claim.

## Critical submodules and scope

Injectivity of h_{4,8} and h_{5,15} follows directly from the established bases and propagation. Therefore their kernels are exactly zero, and so are their images in the two displayed common-polarization tensor modules. By transposition this gives full target rank for h_{8,4} and h_{15,5}, including every previously isolated critical-band component. I requested that those two forward maps be named explicitly after the boxed kernel formula, solely to remove a possible orientation ambiguity in the wording.

The conclusions do not imply N₃=0 or N₄=0 and do not claim novelty for the underlying rank laws. Inside Sra's quadratic windows the maps are surjective, so there is no deficient target component. The square (5,5) defects lie outside those windows and concern the specified canonical map, while the equal-parameter Foulkes multiplicity inequality is tautological equality.
