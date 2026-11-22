# Complete root review of K-032

Date: 22 November 2026 UTC. Reviewer: `/root`; model: GPT-6 Astra Pro; effort setting: not exposed; run: GCT_POS.

**PASS within the stated family and coefficient scope.** The complete normalization proof, graded-piece formula, and leading-coefficient argument in `branches/kronecker/AMPLIFIED_COMPONENT_NORMALIZATION.tex` were read. The complete K-020, K-021 and K-029 proofs were reread to verify the spectral-collapse, mass-denominator and component-image dependencies. The entire independent finite verifier was read and replayed successfully.

The centralizer is the product of block general-linear groups with the full-factor determinant constraints, hence connected reductive. A centralizer-minimal vector fixed by the unitary element has its full moment map in the centralizer Lie algebra. Its centralizer moment map vanishes, so the full one vanishes. The equality of nullcones then makes the image algebra's positive ideal primary to the homogeneous maximal ideal of the centralizer invariant algebra. The homogeneous induction yields a finite module. This is a proof of the precise restriction form required here; the general finite-restriction theorem is credited to the literature.

On the effectively free closed-orbit open set, any other orbit in the same quotient fibre would have to have dimension greater than the effective group, so the whole fibre is one closed orbit. Equality of the two full-stabilizer elements with the same faithful determinant character holds modulo the scalar kernel. The unique repeated eigenvalue in each factor excludes every nontrivial scalar spectral shift. Thus the conjugating element centralizes the actual h, proving one generic centralizer orbit and birationality in characteristic zero. Normality of the invariant algebra gives the claimed normalization.

The prefix incidence columns are independent. Replacing the selected edge degree by s(r−1+rho), keeping every other degree sp_e, is therefore the unique solution of the full determinant-character margin equations. The reduced denominator of rho is exactly M, so M divides s whenever a graded piece is nonzero. The Schur–Weyl, Pieri, and rectangle-complement steps give exactly the double sum, with ordered partitions and integral limits. The convention in degree zero is consistent.

The normalization cokernel has dimension at most d−1, so it leaves the top Hilbert density unchanged. The moving class's generic rank gives the top component term. Its nontrivial two-power eigenvalue factors are units at primes over three. None of this computes the density, its three-adic valuation, the conductor terms, or the simple Laurent coefficient. This identifies one actual collision family, not all remaining collision components.

The replay `verify_component_normalization_formula.py` compares independent symmetric-group character sums with direct monomial-weight/Weyl extraction for test rank2 at s=4,8,12. It also checks the actual n58 prefix denominator, all selected/outside margins, incidence multiplicities, and complete fixed dimension. Those rank2 tests are explicitly not amplified components. No huge rank8 Kronecker value or density was numerically evaluated.

## Literature scope

Bate, M., Geranios, H., & Martin, B. (2019). Orbit closures and invariants. *Mathematische Zeitschrift, 293*(3–4),1121–1159. https://doi.org/10.1007/s00209-019-02228-6. Root read Theorem1.1 and its characteristic-zero attribution on p.1 of arXiv:1604.00924v2, dated5December2018, and the convention allowing disconnected reductive groups in §2.1. Publisher metadata confirms the final citation. No complete reading of the general positive-characteristic proof is claimed.

The attribution to Luna (1975), *Adhérences d'orbite et invariants*, *Inventiones Mathematicae,29*,231–238, is through that primary modern source. Root has not obtained and read Luna's original 1975 proof. K-032 supplies its own complete specialized finite-module proof, so that access limitation is not an unproved dependency.
