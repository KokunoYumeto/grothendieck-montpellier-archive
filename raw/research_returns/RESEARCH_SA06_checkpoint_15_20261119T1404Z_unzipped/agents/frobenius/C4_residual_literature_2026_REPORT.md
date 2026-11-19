# Residual C.4 investigation: source checks and unsuccessful routes

Date: 2026-11-19. This report records further work after C.4x. It contains no new claim that Question 2 is settled for a generic endomorphism-ring-Z type-(1,2) surface or for an arbitrary supersingular threefold in characteristics 2 and 3. No new numbered theorem or completion row is created for these searches.

## 1. Precise remaining objects

The main surface test remains a complex abelian surface A with End(A)=Z and primitive Neron–Severi generator of type (1,2). The exact ordinary integral numerical Poincare-cycle criterion of C.4r remains decisive. The calculation for cycles supported in proper abelian-subvariety translates in C.4q only treats that subgroup. The non-Jacobian result C.4t for the principal polarizations of A×Ahat does not exclude signed minimal cycles or a direct summand in a larger product of Jacobians.

For supersingular threefolds, C.4u reduces the obstruction to the characteristic prime and the universal bound reduces its exponent to one: only 2 or 3 can remain in characteristics 2 or 3, respectively. C.4x disposes of real multiplication examples satisfying its full action and Lie-module hypotheses; no such action has been supplied on an arbitrary supersingular threefold.

## 2. Kahn 2026: the latest version distinguishes the required comparison explicitly

Opened the complete current HTML of Bruno Kahn, *Divided powers on abelian varieties*, arXiv:2602.11135v2, submitted 8 June 2026 (internal date 5 June). URL: https://arxiv.org/html/2602.11135v2 . The earlier author PDF https://webusers.imj-prg.fr/~bruno.kahn/preprints/div-ab01.pdf is the first version dated February 2026; it is not silently used as the current version.

Exact checks:

- Proposition 1.1 proves weak divided powers in **etale Chow groups**, away from the characteristic.
- Theorem 1.2 and Corollary 1.3 give the canonical structure and Fourier transform in the stated etale quotient, with the precise treatment of 2-torsion.
- The introduction, under “Algebraic and etale cohomology classes,” and Question 1.11 explicitly distinguish ordinary algebraic classes from etale classes. Their rational equality and the saturation of the latter do not identify the two integral lattices.
- Proposition B.6 identifies the torsion cokernel of the ordinary one-cycle class map as a quotient, with divisible kernel, of H^{g−3}(X,H^g_et(Q_l/Z_l(g−1))). Question B.7 asks for control of multiplication maps on this group. This is an obstruction formulation, not a proof of its vanishing on A×Ahat.
- Theorem 1.10 has been corrected in v2. Its relative statement is restricted to the appropriate eigenspaces for symmetric line bundles and inverts M!p, with M=min(2g,cd(S)+2). The blanket relative assertion of v1 is explicitly withdrawn by the author. We use neither the withdrawn assertion nor a relative ordinary Chow assertion.

Opened references: turn968976604view1; turn561926606view0–3. The relevant statements and surrounding text were read, not merely their abstracts. No independent verification of the whole new preprint is claimed. In particular, existence of an etale class P^3/3! on a fourfold does not finish C.4.

## 3. Hasan–Hassan–Lin–Manivel–McBeath–Moonen 2025

Opened the full published article *Integral aspects of Fourier duality for abelian varieties*, manuscripta mathematica 176, article 64 (25 August 2025), https://doi.org/10.1007/s00229-025-01662-7 .

Theorem 4.5 constructs a transform lifting (2g+d)! times the usual one. Theorem 5.5 gives the Fourier identities and Beauville decomposition after passing to Z[1/(2g+d+1)!]; the polarization-dependent sl2 statement additionally inverts the polarization degree parameter. The positive-characteristic hypotheses in Section 3.2 are retained. These results control denominators but invert the very small primes at issue here. They therefore supply no missing odd surface class or characteristic-2/3 supersingular class.

Opened references: turn537918067view2; turn598248693view2–3. This is a source-scope check, not a new obstruction theorem.

## 4. Why the literal matroidal-family theorem is not immediately applicable

Opened the latest full Engel–de Gaay Fortman–Schreieder version, https://arxiv.org/html/2507.15704v3 . The relevant hypotheses are in Definition 4.1 and Theorem 4.10; the monodromy formalism is in Section 2.5, especially Definition 2.12 and Lemma 2.13.

Their matroidal family has nonzero rank-one monodromy logarithms around the distinguished independent boundary components. For a family of abelian varieties of the form A×Ahat, a relative polarization identifies H1(A,Q) and H1(Ahat,Q) as rational local systems. Thus every monodromy logarithm on the product is a direct sum of two conjugate operators and has rank twice the rank of the operator on A. This persists under isogeny and finite base change. Consequently a nonzero rank-one logarithm cannot occur in such an isotypic family.

This elementary rank observation shows that the literal matroidal-family hypothesis cannot simply be asserted for the residual surface family. It does **not** rule out adaptations to grouped rank-two degenerations, and does **not** imply algebraicity or nonalgebraicity of the desired cycle. The very-general ppav conclusion also does not specialize in either direction to this special locus.

Opened references: turn864092994view0; turn763967464view3; turn681223935view0. The later Engel–Schreieder 2026 degree paper and the sixfold optimality paper were already checked in the C.4x report; their hypotheses do not erase this distinction.

## 5. Supersingular polarizations and the small-Mumford–Tate lifting route

Opened Oort, *Newton polygons and formal groups: Conjectures by Manin and Grothendieck*, Annals of Mathematics 152(1) (2000), 183–206, complete published PDF at https://www.sas.rochester.edu/mth/sites/doug-ravenel/otherpapers/oort.pdf . Remark 6.4, pp. 204–205, records a three-dimensional supersingular component in the moduli of dimension-three varieties with polarization degree p^6, for every prime p. The paper later writes p^3 once for that degree; we retain the initial moduli convention and do not propagate this inconsistent exponent.

The comparison source https://webspace.science.uu.nl/~oort0109/OortFinalEdited.pdf was also opened. Theorem 7.5(3), author p. 28, states dimension floor(g^2/4) for the principally polarized supersingular locus, and Remarks 7.6 and 8.6 explain failures of this behavior without principal polarizations. These sources prevent treating principal or prime-to-characteristic polarizability of arbitrary supersingular threefolds as automatic. They do not by themselves resolve the Jacobian-summand problem. The original references Katsura–Oort (1987), Remark 6.10, and Oda–Oort (1978), Corollary 3.4, were identified from Oort's bibliography but have not been marked as independently opened in this continuation.

Opened Lam–Oswal, *Lifts of supersingular abelian varieties with small Mumford–Tate groups*, complete author version arXiv:2208.07809v1, https://arxiv.org/pdf/2208.07809 . Theorem 1.2(2), p. 2, lifts supersingular threefolds over Fpbar to varieties isogenous to a product of elliptic curves. Remark 1.3 specifies Witt-vector liftings; Section 1.6, p. 3, assumes p odd throughout. Proposition 2.1 makes the filtered Dieudonne isogeny formulation explicit. Publisher metadata for the later IMRN 2024 paper was located, but the full publisher text failed to load; the theorem locators and odd-characteristic restriction here refer explicitly to the opened author version.

The lift does not produce an actual product or a retraction of prime-to-p degree. No opened primary result upgraded an arbitrary integral gluing of elliptic factors into a Jacobian-product summand. We therefore do not use the lift to remove the residual p-primary factor. The theorem does not cover p=2 in the opened version.

Opened references: turn537918067view0–1; turn598248693view0–1; turn770069476view0; turn968976604view0; turn971900698view1. Publisher full-text failure: turn971900698view0.

## 6. Odd Prym–Tyurin and secant-sheaf leads

Opened Lange–Recillas–Rojas, *A family of Prym–Tyurin varieties of exponent 3*, complete author version https://arxiv.org/pdf/math/0412103 . The actual Theorem 5.2 on author p. 13 identifies the constructed principally polarized varieties as products of two trigonal Jacobians. The introduction on p. 2 misnumbers this as Theorem 5.3; the actual Lemma 5.3 is a representation identity. We checked the theorem and its proof on pp. 13–17, as well as Corollary 6.4 on p. 20. These were used only to test applicability: this family does not assert that the residual type-(1,2) product A×Ahat is covered. An odd Prym–Tyurin realization there would be useful, but is not supplied by this source. Opened references: turn945148879view0 and turn141016688view0–1.

Reopened Markman's complete current arXiv HTML https://arxiv.org/html/2502.03415v2 and its Sections 1.2–1.3. The entry labels itself v2 while its internal date is 24 August 2026; we record that metadata rather than assigning an invented version. The Orlov exterior-product construction has already been tested by the explicit parity calculation and script in C4_Orlov_method_REVIEW.md. That calculation limits that construction only. Rational algebraicity of Weil classes and later deformation statements do not provide the missing integral coefficient automatically. Opened reference: turn433611671view0. No full independent proof audit of this preprint's deformation theorem is claimed.

## 7. Status after these checks

These are additional primary-source and method checks. They have not produced a new counterexample or an integral splitting in either main residual case. In particular, “no theorem found in these searches” is not recorded as a proof that the remaining cases are open in the literature. The strongest proved positive subfamilies, uniform numerical bounds, and exact numerical criterion remain those already stated in C.4h–x.
