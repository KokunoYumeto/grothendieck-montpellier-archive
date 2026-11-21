# Independent targeted whole-proof review: I-22 through I-25

Reviewer: GPT-6 Astra Pro; effort not exposed; agent `/root/purity_zero_status`; run `CUE_GCT-20261121-purity`.

Completed 2026-11-21, 02:09 UTC. I read all four complete written proofs in `I22_source_audit.tex`, `I23_plucker_codes.tex`, `I24_support_reset.tex`, and `I25_grassmann_chunk.tex`. I independently checked the algebraic calculations and argument transitions below. No large matrix computations were rerun, and no formal verification or external peer review is claimed.

**Verdict: all four pass within their explicit scopes.**

## I-22: two failures of the active-simple-block reduction

The two examples are direct and decisive for the cited proof steps.

For the first, `(M+x_1N)(M+x_2N)=x_1E_11+x_2E_22`, whereas the selected `(1,2)` entry is identically zero. The coefficient algebra contains `N`, `M`, `NM=E_11`, and `MN=E_22`, hence is the full two-by-two matrix algebra. The linear output functional does not vanish on `N`. This disproves the equivalence between the prescribed ordered coefficient products and all words in the generated algebra. At distinct specialized values, subtracting the two factors recovers `N`, and then `M`, so generic specialization does not cure this loss of the ordered output.

For the second, the full word is `x_1x_4(x_2+x_3)N`. The generated algebra is the upper triangular algebra, whose radical is exactly the square-zero ideal spanned by `N`; its two simple quotients are the diagonal characters. Every simple quotient kills this nonzero word. At nonzero multiplicative specializations with `x_2+x_3 != 0`, the algebra and this failure persist. Product length is already at least the width, and adding identity factors preserves the counterexample. The two-variable coefficient matrix of `x_2+x_3` has rank two, confirming that this scalar output is not a width-one product of univariate factors.

I independently opened the primary PDF at https://arxiv.org/pdf/2602.13449 and checked the exact source claims. The equivalence is explicitly stated after Definition 2.1 on printed p. 4 and in section 3.1 on p. 6. I read Lemma 3.1 and its complete proof on pp. 6–7; Remark 3.1.4 on p. 9; and Lemma 3.2 with its complete proof on p. 10. The latter argument explicitly makes the invalid inference from the product lying in the radical to vanishing of a long product of arbitrary algebra elements. I also checked the Theorem 7.4 bound and its proof on printed p. 38. These targeted readings support withholding the claimed bound as established by that proof. They do not disprove existence of such a hitting set by another argument and do not amount to an audit of all 48 pages.

Source: Singh, S., & Singh, V. (2026). *An algebraic rigidity framework for order-oblivious deterministic black-box PIT of ROABPs* [Preprint, arXiv:2602.13449v1]. https://arxiv.org/abs/2602.13449 . No reference-review or correctness status beyond the inspected preprint is asserted.

## I-23: diagonal Plücker cocharacters and code cost

The necessity argument is valid in every characteristic for the stipulated formal one-parameter action. Restricting to a fixed coordinate `(r-2)`-plane and using the two displayed four-column configurations gives two-term Plücker relations. Their transformed powers of the indeterminate `t` must agree, including in characteristic two. This forces equality of all three paired exponent sums.

The single-exchange graph on `(r-1)`-subsets of the complement of `{i,j}` is connected. The four-index relations make the exchange difference independent of the subset. Since `r<=w-2`, a common `(r-1)`-subset avoiding any three specified indices exists, giving the cocycle identity for those differences. Thus the exponent function is an integral element-sum plus an integral common constant. The converse is exactly the exterior action of a diagonal matrix times a scalar. The integral conclusion needs no division by `r`.

A binary-valued additive function has element weights with all pairwise differences in `{-1,0,1}`. If nonconstant, there are exactly two levels differing by one. When both levels occur at least twice and `2<=r<=w-2`, the possible intersection counts have range at least two, contradicting binary output. Hence every nonconstant bit is membership of one element or its complement.

Applying this to each seed supported at one code bit is legitimate: a positive integer factor in a formal exponent does not alter the required equality of integer exponents, even in positive characteristic. Adjacent bases exchanging `i,j` have Hamming distance `m_i+m_j`; summing the minimum-distance inequalities gives `ell>=sum m_i>=wd/2`. The resulting full-seed count follows using the stated Hoza error bound. Constants, repeated membership tests, and the layer multiplier do not invalidate the inequality.

The qualifications in the statement are essential and sufficient: this concerns every seed preserving the entire decomposable cone under a diagonal formal action. It is not a lower bound for all nonlinear decoders, all hitting sets, or separately certified subsets of seeds. No source claim about a general Grassmannian automorphism group is needed; the displayed elementary argument proves the required diagonal classification.

## I-24: exponential support despite all higher interval ranks being preserved

Each factor in `Q_(r,a)` has generic rank exactly `r`, and its constant is `P_r`. Every interval has constant product `P_min(r_i)`, whose leading minor is one; generic rank is at most the minimum factor rank. Hence both ranks agree. The same polynomial minor identities and unit minor prove the asserted rank over separate truncated local rings.

The two-position multiplication formula is correct under the stated hypothesis `q_a=0`. It both resets the unwanted middle coordinates and multiplies the final coordinate by the two fresh variables. The induction for `H_k` maintains exactly the required zero coordinates: the first `H_(k+1)` leaves coordinate `k` zero, `Q_(k,k)` resets the higher coordinates, and the second `H_(k+1)` preserves all earlier coordinates. Fresh variable copies prevent identification of positions. The recurrence gives `L_k=2(2^(w-k)-1)`, and the final three-block word has `3*2^(w-2)-2` positions.

In the full word, coordinate one is zero when the first rank-two gadget is applied; coordinate two remains zero until the second. The three copies of `H_3` complete the induction. Thus the scalar output is exactly the product of every position variable, with coefficient one, over any field.

I reread part 3 of I-21 to verify the stronger membership assertion. Adding the displayed rank-one constant endpoints makes every full starting prefix have rank one: its product is nonzero because it can be continued to the nonzero full word. Every proper suffix lying inside the constructed word has rank at least two. Therefore the shortest rank-one suffix of the penultimate prefix begins at the left endpoint, and appending the right endpoint selects exactly the complete word as a final local rank test. The interior already preserves all its higher ranks at zero. This verifies that the support obstruction belongs to the actual test class, rather than merely an unrelated matrix product class.

The conclusion correctly distinguishes the exponential support requirement from hitting-set complexity: the monomial survives any all-nonzero point and also the simplest dense SV substitution. No general generator lower bound follows.

## I-25: positive Grassmannian compression for invertible chunks

The cut-dependent normalization uses original `GL_w` basis changes, so it preserves decomposability after exterior power. Extending the coefficient field to its algebraic closure does not alter polynomial nonvanishing or the zero status of any fixed coordinate restriction. Every factor is invertible on a dense open set containing zero.

The projective prefix-state image closures are nonempty irreducible subvarieties of `Gr(r,w)`. They are nested because the next parameter may be zero. A strict inclusion of irreducible varieties raises dimension, and the usual full-rank matrix chart gives Grassmannian dimension `r(w-r)`. This bounds the number of strict inclusions.

Deleting a non-growth factor is justified at the level of image closures, not coefficient spans: the retained prefix image remains dense in the same variety, and the later invertible factors act regularly on the projective Grassmannian. Applying those regular actions to a dense prefix set yields the same eventual closure. This gives an inductive deletion argument without requiring the matrices to commute. The final scalar polynomial is zero exactly when the final projective image lies in its endpoint hyperplane. Therefore nonvanishing persists after retaining at most `r(w-r)` positions.

For the endpoint extension, the selected row of the exterior matrix of the left endpoint is decomposable over the rational function field in its variable. It must be nonzero whenever the full chosen minor is nonzero. The right endpoint supplies a linear functional, and the interior constants remain invertible over this larger field. Reintroducing the at most two endpoint variables gives support at most `r(w-r)+2`.

The statement carefully asserts existence of a low-support monomial, which suffices for the quoted SV detection. It does not claim that all monomials of the lowest homogeneous component have that support, nor does it extend the proof to singular reset factors. I-24 explains precisely why the latter extension cannot follow from interval-rank preservation alone. The newly added attribution to Liu (2026), section 3.3, pp. 7–8, is for the method that suggested the direct proof; the full general preprint is not adopted as background here.
