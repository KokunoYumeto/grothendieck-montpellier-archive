# Independent audit of the unconditional finite criterion

**Date:** 19 November 2026. **Auditor:** Part D agent. **Audited text:** the complete 308-line `part_c/c1_finite_unconditional_criterion.tex`, including labels `c:covariant-polynomial-lifting`, `c:finite-unconditional-criterion`, and `c:finite-unconditional-scope`, before main integration.

## Verdict and exact advance

The argument passes. It removes the external sign-conjecture hypothesis from the finite necessary-and-sufficient criterion for all rational point-and-diagonal relations. It does not prove that its finite list vanishes for an arbitrary variety, does not make rational equivalence decidable, and does not settle the independently isolated all-power K3 obstruction.

The earlier nonsemisimplicity objection remains correct for the full category of rational representations of GL(a|b). The new construction avoids that category: after converting diagrams to scalar forms, each lifting problem is confined to a finite covariant polynomial degree. Exactness there is a different theorem and is established by the opened primary sources below. No auxiliary projective object is canceled, and no parity correspondence on the Chow motive is used.

## 1. The augmentation and truncation are actual Chow constructions

The degree-one zero-cycle defines ε:h(X)→1 and the unit defines η:1→h(X). Their composite εη is exactly the scalar 1, so π=1−ηε is an actual Chow idempotent. Its realization removes precisely H⁰, because X is connected over an algebraically closed field. Thus V=(h(X),π) has realization H^{>0}(X), of superdimension (a−1)|b.

The identity Δ_*o=o⊠o is equivalent, after the actual diagonal evaluation/coevaluation maps, to ε being multiplicative. Therefore V is an algebra ideal, not merely a graded subspace after realization. Associativity gives

    κ_{m+1} = κ_m ∘ (μ_V ⊗ id^{⊗(m−1)}).

Consequently the single Chow equation κ_{2n+1}=0 forces every higher form to vanish. Its cohomological vanishing uses only the positive degree of every V input and the top degree 2n. No Chow–Künneth decomposition is hidden here. The case n=0 is explicitly removed and handled separately.

## 2. The polynomial semisimplicity statement has the required rational scope

I independently opened the original Brundan–Kujawa arXiv PDF and read all of §5 through Theorem 5.2, including the coefficient-basis computation and its proof. The exact locators are equation (5.2), author p. 13; Lemma 5.1 and its full proof, p. 14; Theorem 5.2 and its full proof, p. 15. The paper works over any field of characteristic other than 2. Its identification

    S(u|v,r) = End_{Q[S_r]}(V₀^{⊗r})

therefore applies directly over Q. Maschke decomposition makes the displayed ordinary endomorphism algebra semisimple. An ordinary module splitting can be made even by conjugation with intrinsic parity and averaging; the averaging preserves the intertwiner equations. This is a representation-theoretic operation on a finite-dimensional rational vector space, not an algebraic parity lift on a motive.

I also independently read Hemmer–Kujawa–Nakano, Theorem 1.3.1(a)(i), author p. 3, and the characteristic-zero proof in Theorem 4.2.6(a), p. 12. Although that paper uses an algebraically closed ground field, the preceding Brundan–Kujawa identification plus the rational Maschke proof establishes the needed rational statement without descent assumptions.

In the form-coordinate ring, each component R_{r,d} is an actual direct summand of a finite sum of V₀^{⊗r}L₀^{−d}, via signed symmetric-power averaging. A stable ideal is homogeneous because the two central scalar actions separate total V degree and form-factor degree. Thus the multiplication surjection

    (E⊗R)_{r,d} → I_{r,d}

lies in one finite semisimple polynomial category. Applying Hom from V₀^{⊗r}L₀^{−d} is exact. This is the precise Hom functor required by the proof; it is not invariants on arbitrary mixed tensors. Parity shifts pose no extra problem: E is already a submodule of the indicated tensor-generated R component, and its even splitting stays in that tensor-generated summand.

## 3. Rational orbit ideals with arbitrary Weil coefficients

The formal supervector space V₀ over Q is not asserted to be a rational cohomology model. For the cohomological form tuple t over K, the map

    R_Q → O(G_Q)⊗_Q K,    f ↦ (g ↦ f(g·t))

is a rational comodule map. Its kernel I_Q is therefore G_Q-stable. The target includes all odd directions of the supergroup, so it retains nilpotents and is not the smaller ordinary-point orbit construction.

For a rational equivariant form F, vanishing of F(t) implies vanishing of F(g·t) over every superalgebra by equivariance. Its coordinate functions therefore lie in I_Q. Conversely, membership in I_Q implies vanishing at the identity. This proves that I_Q records exactly the rational form relations needed in the application, even when K has no specified arithmetic presentation.

The supercommutative coordinate ring is noetherian because its odd part is a finite exterior extension of a polynomial ring in even coordinates. Finitely many ideal generators lie in finitely many homogeneous degrees; their comodule span is finite. This yields the required finite stable E. Each E component splits off a finite sum of the corresponding pure tensor power.

## 4. The lifted equality transports to Chow modulo one rectangle

This is the critical part of the audit. Expand every homogeneous R component using the symmetric-power averaging idempotents. The objects in a fixed (r,d) become direct summands of finite sums of the single pure tensor V₀^{⊗r}L₀^{−d}. The equivariant maps between those pure tensors are generated by permutations, and all their relations are generated by the rectangular Young symmetrizer for a−1 even and b odd dimensions, namely a rows and b+1 columns.

The lift of F through E⊗R, followed by the chosen embedding E→T, is therefore a finite combination of permutation maps into pure-tensor summands. Applying the chosen finite generators T→E→R to the first groups of inputs and the remaining universal forms to the other inputs gives F. The equality between this expression and the original F is an equality of pure-degree permutation maps after the averaging projectors. It holds in Chow as soon as the rectangular relation holds on V. No claim about an arbitrary rational-superrepresentation identity is required.

The direct-summand maps are chosen using rational representation theory. One does not first require a new Chow projector for E: the resulting maps are written as permutation expressions between finite pure tensor powers. Their representation-theoretic identities become Chow identities modulo the rectangle. The Tate line's ordinary one-dimensional symmetric identities already hold in Chow motives.

## 5. Every finite condition belongs to the requested narrow rings

After the two normalization identities, graph multiplication reduces every monomial in the specified generators to a pointed partition. Bending such a cycle gives a product of trace-of-product forms on unpointed blocks and ε on pinned inputs. Splitting each input by h(X)=1⊕V is an actual decomposition. A pinned V input kills its term; unit inputs in an unpointed block disappear; a block made entirely of units gives trace(1)=0 for n>0. The remaining blocks are κ_m, and the high-form relation discards m>2n. Hence every requested cohomological relation reduces to a finite-degree form relation detected by I_Q.

Conversely, each of the finite equations is a rational cohomological relation in a requested point-and-diagonal ring:

- The point identity and the diagonal self-intersection identity give the two normalizations; pushing the latter gives c_n(T_X)=(a−b)o.
- The high form is the small diagonal with π inserted in each input. Expanding π gives pointed partial diagonals.
- The rectangular correspondence on V^{⊗N}, viewed on X^{2N}, expands into products of pair diagonals and point projectors.
- Each finite form generator is a product of κ_m on disjoint groups of inputs, with permutations. Its bent cycle belongs to the same rings and vanishes cohomologically because its coefficients are in I_Q.

Thus both directions of the claimed equivalence use only the requested narrow relations. The proof does not accidentally assume injectivity for the entire tensor category of arbitrary algebraic correspondences.

## 6. Effectiveness and its limit

Given a rational cohomology table, the orbit map is explicit. The more general stated input—a finite presentation of the Q-subalgebra generated by the structure constants, embedded in K—also suffices. Introduce inverse variables for the two even determinants and the final torus coordinate; retain a finite exterior basis for odd variables. Kernel elimination is a noetherian module Gröbner problem over an ordinary polynomial ring with rational coefficients. Subsequent homogeneous stable spans, even splittings, and permutation expressions use finite rational linear algebra.

Without a presentation for the coefficient arithmetic, the theorem claims only finite existence. It does not claim an algorithm that decides all relations among unknown elements of an arbitrary Weil coefficient field, nor an algorithm that decides rational equivalence of the output cycles.

## Primary sources opened independently

1. Brundan, J., & Kujawa, J. *A new proof of the Mullineux conjecture*, original arXiv:math/0210108v1. §5, equation (5.2), Lemma 5.1, Theorem 5.2, author pp. 13–15. <https://arxiv.org/pdf/math/0210108>. Independent web opens: `turn687994843view0`, `turn866197446view0/1/2`. Primary PDF and text archived by Part C as `part_c/sources/brundan_kujawa2003.pdf` and `.txt`.
2. Hemmer, D. J., Kujawa, J., & Nakano, D. K. *Representation type of Schur superalgebras*, original arXiv:math/0411390v1. Theorem 1.3.1(a)(i), author p. 3; proof of Theorem 4.2.6(a), p. 12. <https://arxiv.org/pdf/math/0411390>. Independent opens: `turn687994843view1`, `turn814795529view2`. Primary PDF and text archived by Part C.
3. Lehrer–Zhang's general-linear super FFT/SFT, Theorems 2.1 and 2.3, were independently opened and audited in the earlier superprojective audit. The present use is narrower: pure tensor intertwiners and their rectangular kernel.

Only a cosmetic cross-reference correction was requested: replace the two literal asterisk references by the equation label for the finite form generators. No mathematical gap remains in the written finite-criterion argument after this audit.
