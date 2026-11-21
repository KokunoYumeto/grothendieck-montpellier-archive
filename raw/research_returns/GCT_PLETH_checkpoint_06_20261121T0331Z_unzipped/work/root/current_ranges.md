# Current map ranges and the exact remaining transfer

## M-001. Canonical maps, coefficient inequalities, and the checked parameter ranges

Use the actual normalized grid morphism
\[
h_{b,a}:\operatorname{Sym}^{b}(\operatorname{Sym}^{a}V)
 \longrightarrow\operatorname{Sym}^{a}(\operatorname{Sym}^{b}V),
\qquad
h_{b,a}(v_1^a\cdots v_b^a)=(v_1\cdots v_b)^a,
\quad b\ge a.
\]
Its adjoint, for the invariant tensor inner products, is the transposed-grid map \(h_{a,b}\). This follows by taking the adjoint of the orthogonal row and column averaging projectors: \((P_KP_H)^*=P_HP_K\). Thus surjectivity of the displayed map and injectivity of its adjoint are equivalent by finite-dimensional linear algebra. The dimensions of the source and target multiplicity spaces are the two plethysm coefficients, while their common matrix rank is G-002/G-011. These are the exact maps connecting the several assertions used below.

The strongest uniform bound located and checked in this run is Suvrit Sra, *The q-Foulkes problem III: On Foulkes' conjecture with a graded inner factor*, v1, 29 October 2026, Theorem 1.3 and its proof in Section 2.2: the displayed map is surjective for
\[
b\ge(a-1)^2.
\tag{M1.1}
\]
The proof, including Lemma 2.1 and the common-polarization induction, was read in full. Its statement is used as a cited result. The September 2026 bound \(b\ge a(a-1)\) in OpenAI's *Quadratic stabilization for Foulkes' conjecture*, Theorem 1, is contained in (M1.1). The endpoint observation T-015 is retained as work history and makes no improvement to (M1.1).

The canonical binary map is an isomorphism on every output with at most two rows, for every \(a,b\), in all ambient dimensions: this is G-006, carrying Landsberg's Theorem 7.21 through the natural Schur-functor multiplicity spaces. The actual morphism, and its rank on every such block, are specified there.

Cheung--Ikenmeyer--Mkrtchyan, *Symmetrizing tableaux and the 5th case of the Foulkes conjecture*, arXiv:1509.03944v1, Theorem 6(a), proves injectivity of \(h_{5,6}\); Theorem 6(b) records the kernel at \((5,5)\). Theorem 6(c) supplies the exact component
\[
\lambda=(20,7,6,1,1,1)
\]
with multiplicity one in each \(\operatorname{Sym}^6\operatorname{Sym}^6 V\), on which \(h_{6,6}\) is zero. This is a concrete test of the rank step: both multiplicities equal one while the prescribed map has rank zero.

The coefficient inequality for outer degree six is supplied by OpenAI, *Foulkes' conjecture for sixth powers*, 25 September 2026, Theorem 1.1. Its exact assertion is existence of an equivariant injection for all inner degrees at least six. The current run read its statement, reduction, and computation descriptions; it did not execute its full certificates and does not label the source formally verified. The specified zero component at \((6,6)\) remains a property of the prescribed canonical map. The two assertions are related by the common multiplicity spaces and the explicit zero matrix on that component.

Evseev--Paget--Wildon, *Character deflations and a generalization of the Murnaghan--Nakayama rule*, Corollary 5.2, supplies the coefficient inequality for \(a\le b\) and \(a+b\le19\). Sra III, Theorem 1.4, supplies the stated graded inequalities in depths at most six for \(b\ge a\ge4\), and the further depth-seven, eight, and ten ranges in that theorem. Those finite graded certificates were inspected as source evidence and were not replayed in this run. No canonical-map rank is inferred from these dimension inequalities.

The actual rank findings of this run include the prime-width and product families R-008–R-009, the all-even-rank determinant boundary preimages R-021, the recursive whole-isotypic ranges R-024, and the explicit cofactor families R-025–R-026. Each proof specifies an actual preimage or excludes the displayed irreducible line from the exact transpose annihilator. For R-024, a≥6 and b≥binom(a,2)−4 give surjectivity on every target isotypic component with λ2≤b−binom(a,2)+10; the additional endpoint and triangular profiles are proved there.

For R-026, put r=a−1≥3 and b=r²−k, 2≤k≤r−1. When r is even, the image label is ((r²)^r,r²−k(r+1)). When r is odd, it is (r²,(r²−1)^(r−2),r²−3,r²−(k−1)(r+1)). The target multiplicity and actual image multiplicity are both one. R-025 supplies the adjacent degree b=r²−1 with its displayed parity-dependent labels. The full varying canonical-map surjectivity problem below the square bound remains an exact annihilator gate, narrowed by R-019–R-024 and these explicitly excluded components.

## M-002. The orbit, theta, and purity transfer gates

The compact dual pair and its vacuum twist in T-001 identify the polynomial oscillator module with the Cauchy decomposition. Balanced weight extraction gives \((S_\lambda\mathbb C^m)_{(n^m)}\), and the specified symmetric-group Reynolds idempotent gives its invariant part. The ordinary Gelfand--Tsetlin polytope counts the whole weight space. Its transfer to plethysm is exactly the finite projector, evaluated by G-009 and, explicitly for \(m=3\), G-012. T-005's determinant sign and G-001's nonmonomial example identify failures of the particular unprojected count and permutation-basis construction, with their exact morphisms.

The attached Alpöge note is cited as instructed. Its steps 7 and 8, page 4, discuss interlacing period multiplicities and iterated theta lifts. The cited declarations `ALPOGE_Main.lean`, `ALPOGE_Statements.lean`, and `ALPOGE_LEAN_SCAN.tsv` are absent from the supplied ZIP; no declaration in them was inspected in this run. The transfer needed for the present question is an explicit equivariant map from the groups and representations of those steps to the balanced-weight representation together with its normalizer idempotent, or to the two grid idempotents defining \(h_{b,a}\). The four-page note supplies no such object or map. The exact compact theta realization in T-001--T-002 and the invariant presentations in G-009--G-011 establish the formulas directly without such an identification. No claim about the cited RH and GRH theorems is needed for these proofs.

For the suggested purity route, G-004 constructs the two exact Artin projectors on \(\operatorname{Spec}\mathbb F_{q^2}\). Both images have weight zero, while their invariant dimensions are one and zero. It computes the missing datum explicitly: the projector rank. This calculation leaves available geometric constructions that include the projector, such as the finite quotient and coherent-module constructions proved here.

For width seven, T-016--T-020 identifies the open orbit with stabilizer \(G_2\times\mu_3\), and the extension map is the inclusion of polynomial functions into their discriminant localization. The end-node sector has the exact valuation and positive formula of T-018. The remaining valuation filtration for other highest weights is an explicit smaller orbit calculation. G-009--G-010 already give terminating positive counts for those coefficients; the unresolved question there is a small direct orbit formula replacing the general elimination construction.

The requested Masullo locator is an input gate: no Masullo work, statement, or identifier occurs in the supplied file inventory. A theorem or a map from such a work is not introduced by inference.

## Source URLs

* Sra III: <https://suvrit.github.io/papers/qfoulkes3/qfoulkes3-v1.pdf>; supplement: <https://suvrit.github.io/papers/qfoulkes3/qfoulkes3-v1-supplement.pdf>.
* Cheung--Ikenmeyer--Mkrtchyan: <https://arxiv.org/abs/1509.03944>.
* Landsberg's supplied survey, Theorem 7.21: <https://arxiv.org/abs/1305.7387>.
* Alpöge: <https://alpo.ge/remark.pdf>, attached four-page file, steps 7--8 on page 4.

This register is a current-source audit dated 21 November 2026, Europe/Berlin. Its labels identify the audit and explicit morphisms; the attributed literature theorems remain cited results.
