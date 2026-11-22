# C.3bj: independent full proof and source audit

**Verdict: PASS for the complete six-step mathematical argument.** The statement is restricted to codimension two, every characteristic p>0 and every local dimension N≥5; it constructs an actual ordinary algebraically trivial restriction-kernel class of exact order p. It asserts no nonzero rational class and no all-codimension theorem.

- File read in full: `research/agents/real_weil/C3_uniform_higher_integral_kernel_draft.tex`.
- Read-version SHA256: `78dd637bbd0ee2318c301a63265d3ffdb4377de55dab5bfb771cf765bab19735`.
- Reviewer: GPT-6 Astra (OpenAI), ChatGPT Pro mode; run RESEARCH_SA06 /root/frobenius; inherited effort setting not separately exposed.
- Complete mathematical read and new Stacks checks finished at the tool clock 14:49:25 UTC on 19 November 2026. Fresh Braunling product-source check finished by 14:49:53 UTC. Fresh Kerz definition and exact theorem-scope reread followed after checkpoint16 thaw, at approximately 14:55 UTC.
- The review was communicated during the read-only checkpoint freeze and saved after thaw. The theorem was expressly excluded from checkpoint16 and review10 movement.
- Disclosure: this reviewer supplied the independently audited relative Milnor quotient and contributed the earlier characteristic-five cubic incidence geometry. The six-step synthesis, all-p/all-N incidence argument, actual-family lifting and complete boundary argument were independently rederived here. This is not a claim of an entirely uninformed review.

## 1. Smooth projective choices and the cubic divisor cup

The ordinary-quartic and nondegenerate deformation-form input is exactly the previously certified C.3bg result. Its symmetric bilinear form interpretation uses the dual of Sym² H⁰(K_C), without dividing by two. Thus the characteristic-two use is legitimate.

For p≠3 the Fermat cubic is smooth, and the stated line lies on it. For p=3 the four derivatives of u s²+v t²+u²t+v²s are s²−ut, t²−vs, −us+v², −vt+u². If any coordinate vanishes, their common vanishing forces all four coordinates to vanish. Otherwise normalize u=1: the gradient equations give s=v², t=v⁻¹ and v⁵=1, while the defining polynomial equals v⁴≠0. Hence there is no projective singular point.

The twisted conormal/Euler computation identifies the divisor cup with the binary quadratic quotient by Q₀|D and Q₁|D. These quadratics have no common zero. The resulting bilinear form on H⁰(O_D(1)) is nondegenerate: a nonzero degenerate symmetric two-by-two matrix over an algebraically closed field has rank one and is an evaluation form, which would force a common zero. In the given models the matrix is the off-diagonal identity matrix. It is nonsingular in characteristic two as well. The line-bundle obstruction is the embedded-line obstruction followed by the divisor boundary, whose isomorphism was explicitly checked from H¹ and H² of O_W(D−A). No characteristic-dependent coefficient is lost.

For B=A⊠K_C on the threefold W×C, B is very ample. Successive Bertini cuts give a smooth codimension-two base curve. The rank conditions on the three z-coefficients are nonempty open conditions; the witness x₀s,x₀t,x₁s verifies both independence and nonzero divisor cup. Their intersection with the Bertini open is nonempty because the parameter space is irreducible. For m=2 a further transverse section has a reduced finite zero locus; for m≥3 one additional section avoids that finite set. Extra coefficients may then be zero. The incidence divisor is smooth at base points by linear independence of the section differentials, and away from the base by a nonzero projective-direction derivative. This covers every m≥1, including arbitrary large m.

All choices lie in nonempty opens defined over finite fields. A search over finite extensions and coefficient tuples therefore terminates. This is an exact specification, with no unproved uniform runtime bound.

## 2. The actual contraction

The equation F+τℓH is primitive linear in the line-bundle coordinate and integral because F is prime and does not divide ℓH. Along the zero section its differential contains the nonzero differential of the smooth quartic. The Segre contraction is projective, is an isomorphism off the zero section and retains the W-projection. Connectedness of V gives one point over the vertex after normalization. Removing the proper image of any remaining singular locus away from V preserves a regular projective source after localization.

The Segre generators generate the fibre ideal on every chart. Consequently the pulled-back maximal ideal equals I_V, and I_V/I_V²=L. The strict transform of f=τℓ=0 is exactly the split line bundle over the smooth incidence divisor T. Thus both punctures are regular. The dimensional count is dim(V)=m+3 and dim(R)=m+4=N.

The normalization source must be understood on the regular neighborhood just described, rather than incorrectly calling the initially defined global hypersurface everywhere regular. This is the prose precision already requested by the parent; it does not change the argument.

## 3. Actual ordinary Picard endpoint

All displayed cohomological vanishings follow from the cubic hypersurface sequence, nonnegative projective-space cohomology and the curve identities H¹(K_C)=k, H¹(K_Cⁿ)=0 for n≥2. In particular H³(V,Lⁿ)=0 for n≥0, as needed for the target divisor calculation.

The extension-class image is the three-dimensional coefficient space U. Its rank is preserved by the nondegenerate quartic deformation form. Multiplication by ℓ on H¹(O_V) has the same image because Serre duality identifies the coordinate multiplications with the canonical basis pairings. The selected cubic cup is nonzero on U.

Ordinary Verschiebung kills coherent H¹ and has kernel (Z/p)³. The Hom–Ext exact sequence identifies its restriction to this finite kernel with the extension class. Since the latter has rank three, the finite subgroup spans U and embeds; therefore at least one finite-kernel point has nonzero divisor cup. This does not infer nonvanishing merely from the size of the finite group.

On the target, the exact divisor sequence gives H¹(T,L_T)=U₀/U and kills all higher H¹ and H² of L_Tⁿ for n≥2. Its split first neighborhood gives a product Picard extension. The vector coordinate of a morphism from J^(p) is constant and hence zero after normalization, while the reduced coordinate factors through Verschiebung. Thus the selected endpoint has zero first jet on the target. No identification of the full Pic⁰(T) is required.

The actual family is constructed on a smooth proper curve in J^(p) through the two endpoints. The mixed lifting obstruction is killed by Verschiebung pullback; a lift to E×P differs from the specified classifying map by a constant vector, removed by its zero fibre. Higher obstructions vanish by the coherent calculations on V×P. Formal GAGA, finite-data Popescu descent and a henselian lift preserving the first jet then give a bundle on the fixed actual product Z×P. The inverse and first-jet identification are included among finite data. Uniqueness of higher endpoint lifts and the established punctured Picard comparison prove actual source p-torsion and target triviality. This is not a replacement of ordinary algebraic equivalence by a formal-family relation.

## 4. Divisibility and the canonical detector

The separate complete audit `K2_cohomology_divisibility_independent_REVIEW.md` proves the exact H¹(V,K₂^M) divisibility used here. Its eight copies of k* are correct for m≥1. The proof uses the localization generation sequence and an open-restriction calculation for blow-ups, not an unsupported inference from global K₁.

The relative Milnor kernel is generated by symbols having one principal unit because each reduced Steinberg relation lifts via u and 1−u. It is killed by p. The rank-one conormal sequence is locally split by smoothness of V, so restricting dlog defines a canonical quotient to L⊗Ω¹_V in every characteristic. In characteristic two symbols with two infinitesimal entries are sent to zero, without being declared zero in the Milnor kernel.

The connecting homomorphism from divisible H¹(V,K₂^M) to the exponent-p H²(J) is zero. Thus the relative class of the actual line-product injects into absolute H²(E,K₂^M). Its canonical differential image is precisely the nonzero coherent cup selected in Step 3. The cocycle maps naturally from Čech to sheaf cohomology; no acyclicity assumption for the relative sheaf is necessary.

## 5. The entire exceptional image

If β vanished on the puncture, localization would express it as i_*γ for γ∈Pic(V). Self-intersection forces Lγ=0. For m≥2 the h² coefficient gives b=0 and the h coefficient then gives γ₀=0. For m=1 the coefficient recursion gives γ₀=−bc and bc²=0. Multiplication by c and integer degree gives 36b=0 in Z, so b=0 even in characteristics two and three. This controls arbitrary Pic(C)-torsion as well, because the recursion forces the whole γ₀ to equal the stated integer multiple of c.

Hence β would already be zero on Z. The integral Milnor–Bloch product identification then makes its restriction to H²(E,K₂^M) zero, contradicting the preceding detector. This concludes exact order p and actual ordinary algebraic triviality. The source is regular; the proof never invokes a Milnor–Quillen comparison on E.

For the limit presentation, the precise phrase should be a finite pointed étale stage over the original local model, followed by a suitable regular finite-type neighborhood over the perfect coefficient field. Any proposed finite rational-equivalence witness and both line bundles descend to such a stage. The parent has requested this wording refinement; the finite-data argument is valid with that interpretation.

## 6. Newly opened exact primary inputs

1. Rost, M. (1996). *Chow groups with coefficients*. Documenta Mathematica, 1, 319–393. https://www.math.uni-bielefeld.de/~rost/data/10000028002.pdf. Freshly read Proposition 4.1(3), p.351; Section 5 localization and grading, p.356; Remark 5.4, p.357; Corollary 6.5, p.360; Proposition 8.6 with proof, p.370; Section 12 pullback and open-restriction formula, pp.382–383. The author's corrections at https://www.math.uni-bielefeld.de/~rost/chowcoeff.html were also read.
2. Braunling, O. (2013). *Bad intersections and constructive aspects of the Bloch–Quillen formula*. New York Journal of Mathematics, 19, 545–564. https://nyjm.albany.edu/j/2013/19-28p.pdf. Freshly opened the full published PDF and read Section 1, especially Remark 1, pp.548–549; Section 3, equations (21) and (22), pp.557–558; and the dlog construction, p.559. Equation (22) is the full integral ring-product comparison, not merely a numerical top-degree formula. The smooth infinite-field hypotheses fit the finite models; no comparison is imported for the singular thickening.
3. Kerz, M. (2009). *The Gersten conjecture for Milnor K-theory*. Inventiones Mathematicae, 175(1), 1–33. https://kerz.app.uni-regensburg.de/articles/milnork_inventiones.pdf. Freshly opened the 29-page author version dated 29 April 2008 and read Definition 2.1, author p.3, Theorem 7.1, p.21, and Theorem 7.5, p.22, with adjoining proof/scope discussion. The regular source contains an infinite field, so the residue-cardinality hypothesis is satisfied.
4. The Stacks Project, Lemma 33.47.3 in Tag 0FD4: https://stacks.math.columbia.edu/tag/0FD4. Full statement and proof freshly read. A very ample system and all its successive restrictions give the required smooth cuts in arbitrary characteristic.
5. The Stacks Project, Lemma 10.131.9, Tag 00RU: https://stacks.math.columbia.edu/tag/00RU. Full statement and proof freshly read. This supplies the conormal sequence; left injectivity in the square-zero case is independently proved from local smooth splittings, not asserted by the general lemma.

Previously certified exact Picard, formal existence, approximation, Elkik, cubic-surface and Illusie inputs are reused with their earlier records. No new rereading of every underlying proof or new program/build run is claimed here. The owner and parent retain responsibility for final prose corrections, finite certificate, standalone/master build and registration.
# Final promoted version check

At 15:12:40 UTC on 19 November 2026, we read the promoted `C3_uniform_higher_integral_kernel.tex`, SHA256 `94fd7b808253738a98b5954ff6a9d5860a5758f0469f5c813a316bbe7fdf11ee`. Both requested source-model precisions are present: the regular neighbourhood is obtained by removing the proper image of the nonregular locus, and finite descent uses a pointed etale neighbourhood of the algebraic vertex, followed by a smooth finite-type model over the perfect coefficient field. The final six-step proof and its scoped codimension-two corollary pass. No fresh program rerun is claimed by this receipt.

