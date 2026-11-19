# Independent audit: the exact threefold pairing gate and positivity scope

**Auditor:** Part D agent, RESEARCH_SA05. **Date:** 19 November 2026, approximately 07:00 UTC. This is an actual source/proof audit, not a proof of the remaining weight–monodromy conjecture.

## 1. The written threefold reduction

I read the complete `part_c/c4_pairing_reduction.tex`, then reread Saito's exact dimension-three statement in §2.7 and the complete standard-conjecture argument in §§4.1–4.3. The written proposition `c:threefold-pairing-kernel` and its scope remark pass this audit.

The source is Morihiko Saito, *Monodromy Filtration and Positivity*, arXiv:math/0006162, version 11, September 2003, https://arxiv.org/pdf/math/0006162. Theorem 0.2 is on author p. 2; the complete general linear-algebra argument is §§1.1–2.5, pp. 3–8; the exact dimension-three converse is §2.7, p. 9. The standard-conjecture sufficient criterion is Theorem 0.4, p. 3, with proof in §§4.1–4.3, pp. 14–16. The local source is `part_c/sources/morihiko_saito2003_positivity.txt`; canonical bibliography key `c_msaito2003positivity`.

For the directly proved kernel formula, the source and target E2 rows have the same underlying middle space U⊕Z. The source has the extra Gysin cocycle equation, whereas the target has the extra restriction boundaries. Subtracting the shared boundary (γ_B b,ρ_B b) from a representative killed by N leaves (r,0), with r in R=imρ_A. The remaining condition is γ_U r=0, since ρ_Uρ_A=0. Two such representatives are equivalent precisely modulo R∩γ_B kerρ_B. Poincaré duality identifies γ_U with the adjoint of ρ_A, so the numerator is rad(b restricted to R). The relation γ_Uγ_B=0 makes the denominator a subspace of that radical. The pairing A×C and the surface pairing U×U both take values in Q_l(-2), so the claimed twists and Galois equivariance are correct.

Saito §2.7 states the dimension-three converse, not merely a sufficient criterion. It identifies two primitive-image conditions, in H3 of the components and H2 of the double surfaces, and states that the first is automatic by passage to a general hyperplane section. The fragment therefore correctly leaves only the primitive restriction image in H2 of the double surfaces. This is a genuine refinement of the displayed obstruction, but it is not a proof of nondegeneracy.

The Q5 line span(1,i), with i²=-1, is isotropic for the rationally negative-definite form -x²-y². A scalar Frobenius preserves it and its weight. This is a correct formal counterexample to a rational-origin inference, and the fragment explicitly does not present it as a geometric counterexample.

## 2. What Saito's standard-conjecture proof actually uses

Section 4.1 separately defines B(Y), algebraicity of the Lefschetz inverse; A(Y,L), the Lefschetz isomorphism on algebraic classes; I(Y,L), positivity of primitive algebraic pairings; and D(Y), equality of numerical and homological equivalence. The proof does not replace these by an unqualified statement that the underlying motive belongs to a convenient category.

Under B(Y) and I(Y×Y,L⊗1+1⊗L), the adjoint Γ′ formed using the Lefschetz star is algebraic and satisfies Tr(Γ′Γ)>0 for a nonzero correspondence; this is formula (4.1.3), p. 15. Section 4.2 explains how D and semisimplicity supply algebraic projectors onto images, including mixed-dimensional maps after adding projective-space factors. Section 4.3 constructs a projector onto the primitive restriction or Gysin image, proves nondegeneracy first for a simple motive by the positive adjoint trace, and then decomposes orthogonally by induction.

Both ingredients matter: a rational/algebraic image projector, and positivity for the actual geometric form. Merely knowing that the image is a Q_l-subspace of the span of divisor classes supplies neither its rational origin nor positivity after extension of coefficients.

Section 2.7 explicitly notes that, even if Imρ consists of algebraic classes, one still uses D(Y^(1)), A(Y^(1),L), or the divisor Tate conjecture for the components to finish. Section 5.4's multiplicity-one argument applies to certain coefficient primes selected by a decomposition-group condition; §5.5 does not upgrade this to all primes without the further standard-conjecture input. No such upgrade is used in the present report.

## 3. The exact Milne version warning

Milne's article is:

Milne, J. S. (2002). Polarizations and Grothendieck's standard conjectures. *Annals of Mathematics, 155*(2), 599–610. https://doi.org/10.2307/3062126

There are two distinct official author PDFs and they have different numbering:

| Official version | Exact relevant locators | Scope |
|---|---|---|
| Submitted version, dated 26 March / 14 August 2001, 16 pages, https://www.jmilne.org/math/articles/2002aS.pdf | Theorem 4.6, pp. 13–14; Corollary 4.7, p. 14; **Remark 4.10 and footnote 3, p. 14** | The theorem and corollary concern abelian varieties. Remark 4.10 explicitly warns that equality of all motives with the abelian-motive category under Tate does not make the geometric Hodge standard conjecture for arbitrary varieties follow. Footnote 3 retracts the first-version assertion. |
| Shortened published-version author PDF, dated 19 September 2001, 11 pages, https://www.jmilne.org/math/articles/2002aP.pdf | **Theorem 3.3, pp. 8–9; Corollary 3.4, p. 9** | Same abelian positivity consequence. The submitted warning is not a published Remark 3.6; that number concerns a different refinement. |

I opened both official versions and read the exact theorem/proof passages and the warning. The metadata was checked against the primary Annals page. The arXiv first-version abstract's broader assertion must not be substituted for the corrected text.

The mathematical distinction is visible already in the category of rational vector spaces: the object Q² belongs to the Tate category, but the arbitrary nondegenerate form diag(1,-1) has an isotropic rational line. An object isomorphism transports a form; it does not prove that the transported form is a positive polarization. This is an elementary nonimplication certificate, not a geometric counterexample.

The October 2026 CM Hodge theorem supplies Milne's hypothesis and hence his positivity conclusion for actual abelian geometric forms. The October 2026 rationality theorem controls Hodge–Lefschetz pairings on reductions of abelian varieties. Neither source supplies the required primitive geometric positivity for an arbitrary component or intersection surface of a semistable model. Even an abstract assertion that a stratum motive is of abelian type would still require a separate identification of the geometric form with a positive polarization.

## 4. Audit of existing Parts A and B

I searched all positivity, polarization, Hodge-standard and abelian-type occurrences in `sections/part_a.tex`, `sections/part_b.tex`, and `sections/b*.tex`, then read the substantive passages.

Part A's introductory hypothesis paragraph explicitly restricts the additional Hodge-standard positivity to the abelian motives involved. The odd-line proof uses a specified alternating odd-weight polarization and also gives an independent quaternion obstruction. Remark `A:2026-abelian` extends the theorem only to full-correspondence abelian motives, and expressly retains the arbitrary-variety Tate hypothesis. No arbitrary-stratum primitive form is transported there.

Part B's `thm:B-abelian-type` transports Tate classes and Frobenius semisimplicity through actual algebraic projectors and uses Kimura nilpotence/Kahn's comparison theorem. Its `prop:B-phantom-gate` uses the abelian-type numerical category to construct a Chow phantom and does not infer a geometric positivity statement. The new `lem:B-surface-Tate-prime` uses the actual divisor intersection form and the unconditional Hodge-index theorem for surfaces, which is a valid and different input. Other polarization occurrences concern abelian duality, principal polarizations, or local arithmetic coranks. No use of the failed positivity shortcut was found.

## 5. An honest conditional special case

Saito's algebraic-image special case can be made explicit without claiming a general theorem. Suppose the entire restriction image R is contained in the divisor span on the double surfaces and the divisor Tate conjecture holds for the threefold components over all finite residue-field extensions. After one finite extension all relevant divisor classes are fixed. The invariant algebraic part of H2(1) has a nondegenerate pairing against complementary algebraic classes; Tate then removes the generalized-one Jordan ambiguity, and an equivariant map to a Frobenius-fixed divisor space comes from the rational invariant algebraic source. Thus R is the scalar extension of a rational restriction-image subspace. Its primitive part is a rational subspace of the negative-definite primitive divisor form on the double surfaces, and is nondegenerate. Saito §2.7 then proves weight–monodromy in this restricted situation.

This is the special case already identified by Saito. It does not remove the algebraicity hypothesis on R or prove universal divisor Tate, and is not counted as a new unconditional movement of the main gate.

## 6. Audit of the subsequent divisor-image splitting

At approximately 07:07 UTC I read the complete new corollary `c:threefold-divisor-split` in the same fragment. I independently read Ito's Claim 4.6 and full proof, author pp. 12–13, in `part_c/sources/ito2004_threefolds.txt`, and reread the full proof of Kahn (2023), Theorem 8, printed pp. 89–90. The written corollary passes.

Unconditionally, the rational divisor restriction image has a rational primitive subspace: the equations are the intersection degrees against the chosen ample class on each target surface. Extension of scalars preserves the kernel and image. The surface Hodge-index form on this rational subspace is negative definite, so its Gram determinant remains nonzero over Q_l. Orthogonal projection defined by the inverse Gram matrix preserves R_prim because the projected subspace lies in R_prim. This gives the displayed orthogonal splitting without identifying all algebraic vectors of R_prim with divisor preimages.

Under the universal surface divisor Tate hypothesis across all finite constant fields, Kahn's theorem gives divisor Tate for every component and intersection stratum. The ample Lefschetz form on H2 restricts nondegenerately to NS and yields a Galois-stable direct complement. NS has only q times root-of-unity eigenvalues. If its complement had such an eigenvalue, some constant-field extension would make its eigenspace invariant; Tate would place that eigenspace back in NS, a contradiction. The same argument excludes any nonzero generalized primary block, because it contains an eigenvector. No full Frobenius semisimplicity conjecture has been invoked.

Restriction preserves these disjoint spectral blocks. The target nondivisor block is orthogonal to all divisor classes and therefore primitive. The primitive part of the divisor restriction image is exactly the unconditional rational summand already split off. Consequently the remaining orthogonal space is precisely rho(T1), inside T2. The conditional spectral identification is strictly separated from the unconditional splitting in the statement and proof.
