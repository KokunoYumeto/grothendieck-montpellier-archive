# C.3bj: independent complete proof and source audit

**Outcome: PASS for the complete stated theorem.** We read all six steps of `../real_weil/C3_uniform_higher_integral_kernel_draft.tex` during the checkpoint16 write freeze, communicated the mathematical pass, and completed the final source/wording check at **2026-11-19 14:54:35 UTC**, after the parent released the freeze. This is an independent-agent re-proof by `/root/cycles`, GPT-6 Astra Pro, RESEARCH_SA06; it is not represented as verification by an independently chosen model.

The exact scope is: for every algebraically closed field of characteristic p>0 and every local dimension N≥5, the construction gives an actual ordinary algebraically trivial codimension-two cycle of exact order p in the kernel of restriction to a regular principal punctured divisor. The construction is available over the algebraic closure of the prime field. There is no rational nonvanishing assertion.

## 1. Projective geometry and the divisor cup

We rederived the characteristic-three cubic check. For F=u s²+v t²+u²t+v²s, its four derivative equations force all coordinates to be nonzero at a possible projective critical point. Setting u=1 gives s=v², t=v⁻¹ and v⁵=1. On this locus F=4v⁴=v⁴ in characteristic three, so no critical point lies on the cubic. For p≠3 the Fermat cubic is smooth, including in characteristic two.

For either displayed cubic and its line D, the two restricted normal quadratics are nonzero scalar multiples of s² and t². The twisted normal exact sequence has the stated degrees. We checked H⁰(O_W(D−A))=H²(O_W(D−A))=0 and χ(O_W(D−A))=0: (D−A)·A=−2 and K_W−(D−A)=−D. Thus H¹ also vanishes. The boundary is an isomorphism, and the divisor cup has the bilinear matrix with off-diagonal entries one and diagonal entries zero. It has rank two also in characteristic two. The more general basepoint-free-quadratic argument is sound and does not divide by two.

The successive incidence choices are legitimate. A⊠K_C is very ample. A general first section is smooth, a general second cuts it smoothly in codimension two, and the two stated coefficient-rank conditions are nonempty open conditions with the explicit rank witness given in the draft. Their intersection is nonempty in the irreducible coefficient space. For m=2 the third section has a reduced zero divisor on the smooth base curve; for m≥3 a fourth section avoids that finite base scheme. At a remaining base point the section differentials are independent, while away from the base the projective-variable derivative is nonzero. This proves smoothness of the incidence divisor for every m≥1, rather than only checking a finite-field point set. A closed point of each nonempty open gives a finite extension of the finite coefficient field. The enumeration is therefore a terminating specification; it is not assigned an uncomputed runtime or uniform bound.

## 2. The actual local resolution

The equation F+τℓH is globally a section of the indicated pullback of O(4). The polynomial is linear in the line coordinate, and F has no common factor with ℓH. The graph contraction by the complete Segre generators is proper. Near the connected exceptional V the equation is regular because dF is nonzero on C. The proper image of the complementary singular locus avoids the vertex, so the localization removes it. Consequently the resulting projective resolution **itself is regular**, which is the condition later needed for the Chow/Milnor comparison; it is not merely its exceptional divisor that is regular. Normalization and strict henselization preserve the stated single exceptional fibre and the isomorphism off it.

On every coordinate chart the Segre generators generate the line-coordinate ideal. Hence m_R O_Z=I_V and the first ideal quotient is exactly L. The projection to W supplies the actual fixed line bundle O_W(D). Setting f=τℓ gives the split line bundle on the smooth incidence divisor T, so the target puncture is regular. These are the same finite-data graph operations already audited in bf/bg, now with the smooth factor W retained.

## 3. Actual ordinary Picard families and their endpoint

We checked every cohomological vanishing in (C.3bj.9) using the cubic hypersurface sequence, positive projective-space cohomology and the curve Künneth formula. In particular H²(V,O_V)=H³(V,Lⁿ)=0 for n≥0, and H¹(V,Lⁿ)=H²(V,Lⁿ)=0 for n≥2. The first Picard extension is therefore by H¹(V,L), and its extension-class map has rank three because Q_H is nonsingular and the three coefficient sections are independent.

The ordinary Verschiebung v:J^(p)→J is étale with kernel (Z/p)³ and kills H¹(O_J). The Hom–Ext calculation therefore gives the lift b, whose kernel-point images span the rank-three vector subspace U and are injective on that finite kernel. The divisor cup is nonzero on U. Hence a kernel point η can be selected whose image a has nonzero cup with D.

The target argument correctly avoids assuming that its entire Picard variety is J. Its split first neighbourhood has Picard functor Pic(T) times H¹(T,L_T). The vector coordinate of b is zero by properness, and the Pic(T) coordinate factors through v, so η has zero target first jet. The exact divisor sequence gives H¹(T,L_T)=H¹(V,L)/U, and all higher endpoint ambiguities vanish.

The construction of the actual family is essential and passes. A smooth proper curve P through 0 and η in J^(p) pulls the normalized Poincare bundle back to V×P. Its mixed first obstruction vanishes because v* kills the relevant H¹(O_J) factor. A lift has classifying map differing from b|_P by a constant vector map; the inverse fibre removes that constant. Higher obstructions vanish by the displayed cohomology and H²(P,O_P)=0. Proper formal existence, finite-data Popescu descent and smooth henselian lifting modulo m² give a bundle on the fixed actual product Z×P. The equality m O_Z=I_V makes that congruence the required first jet. Endpoint uniqueness through higher orders and the punctured completion comparison then prove both A^p|_X=O_X and A|_Y=O_Y. This is not a family only on a varying or merely formal product.

## 4. The divisible group is the correct sheaf cohomology group

The proof uses H¹(V,K²_M), not K₁(V). We independently proved the localization generation assertions in `k2_cohomology_divisibility_draft.tex`, including their integral grading shifts and proper/open compatibility. For a projective-space product the open affine homotopy group is lifted by projection; its remaining image comes from G⁰,¹=k*. For a blow-up the difference c−ρ*ρ_*c restricts to zero off the exceptional divisor and hence comes from its G⁰,¹. No unproved full blow-up formula is needed.

A smooth cubic surface is a six-point blow-up of P² over an algebraically closed field. After product with C and P^m this yields the quotient of H¹(C,K²_M)⊕(k*)⁸ stated in the draft. The curve group is the cokernel of the tame-symbol map to a direct sum of copies of k*. It is divisible, as are all subsequent quotients. All arguments apply in every characteristic.

## 5. The all-prime integral Milnor detector

We separately read and re-proved the full all-degree relative Milnor lemma of frobenius; see `relative_milnor_all_characteristics_independent_REVIEW.md`. Its degree-two use here is correct. Units and Steinberg relations lift across the square-zero quotient, so the relative kernel J is generated locally by symbols with an entry 1+i. The relation (1+i)^p=1 kills J integrally, including when p=2.

Local formal smoothness of V gives a splitting of the square-zero algebra locally, which proves the left injectivity in the conormal sequence. Because I is invertible, the exterior-square kernel is canonically I⊗Ω¹_V. The usual dlog of relative symbols lands in this kernel and gives the frame- and splitting-independent map τ. Both-infinitesimal symbols have zero image; the proof does not incorrectly assert that those symbols themselves vanish in characteristic two.

The connecting map H¹(V,K²_M)→H²(V,J) vanishes because the source is divisible and the target is killed by p. Therefore H²(J) injects into H²(E,K²_M). The actual line transitions define the relative cup cocycle {1+a_ij,g_jk}, whose τ image is the already proved nonzero divisor cup. Its absolute image is thus nonzero. No comparison between Milnor and Quillen K-theory on E, no rational Chern character and no Adams filtration is used.

## 6. The entire exceptional Chow image is excluded

If the actual product β vanished on X, Chow localization would give β=i_*γ for an arbitrary γ∈Pic(V). Restriction to V and self-intersection give Lγ=0. The projective-bundle coefficient argument excludes every such γ, including the torsion in Pic(C). For m≥2, the h² and h coefficients immediately give b=γ₀=0. For m=1 the equations give γ₀=−bc and bc²=0. Intersecting with c gives the integer equation 36b=0; this remains an integer equation in characteristics two and three. Thus γ=0 and β=0 on Z.

The integral Milnor Bloch formula and full Chow-product compatibility identify β with the line-bundle cup on the regular Z. Its restriction to E is the nonzero absolute class from Step 5. For the strict localization the line bundles and any supposed finite rational-equivalence witness descend to a regular finite-type étale stage, where this product identity is the usual smooth statement; passing to the filtered limit preserves it. This explicit finite-stage explanation is retained. The contradiction proves nonvanishing, and the already proved p-torsion gives exact order p.

## 7. Primary source and computational scope

Fresh reads for this combined audit: Stacks Lemma33.47.3 and its entire proof, section tag0FD4; Stacks Lemma10.131.9, tag00RU; Braunling (2013), published §3, pp557–558, including the full product diagram(22), and the beginning of §4. URLs are respectively https://stacks.math.columbia.edu/tag/0FD4 , https://stacks.math.columbia.edu/tag/00RU , and https://nyjm.albany.edu/j/2013/19-28p.pdf . The new reads confirm the precise Bertini and conormal hypotheses and the full ring-product compatibility.

The exact Rost and Kerz primary reads completed earlier in this window are retained in `K2_COHOMOLOGY_SOURCE_AUDIT.md`, with downloaded originals, manifest, and actual source-fetch runtime. Earlier bf/bg Picard lifting, Brion, Illusie, Elkik and the cubic-surface blow-up inputs were reused as audited antecedents; they are not represented as all freshly reopened in this combined check.

At this audit time we have not inspected or rerun a bj-specific finite program. The existing supporting bg/bi finite certificates retain their own scopes and original runtimes. The complete proof audit above is not replaced by a finite computation. Any later bj-specific certificate inspection should receive a separate, actual-time event.

## Dated computational addendum — 15:02:38 UTC

We subsequently read the complete owner program `../real_weil/code/check_C3bj_uniform_kernel.py` and its full 52-check JSON certificate `../real_weil/output/C3bj_uniform_kernel_certificate.json`. All finite assertions pass inspection: the explicit off-diagonal cubic cup, the three independent section/cup images, the square-zero exponent identities for eleven listed primes, and the integral exceptional coefficients. The actual author run began 14:55:35.802170 UTC and took 0.19962774000305217 seconds. We did not rerun it. Its explicit scope disclaimer is correct: it does not purport to execute every finite-field incidence enumeration or prove the geometric, cohomological or descent steps. The conormal normalization is proved in the text; the program's determinant-one check is only a finite consistency check.

