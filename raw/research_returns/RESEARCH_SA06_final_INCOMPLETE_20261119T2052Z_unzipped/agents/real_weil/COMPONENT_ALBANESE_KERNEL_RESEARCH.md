# Component Albanese kernels and actual perfect families

Current record: 19 November 2026, after checkpoint20. C.3br and the restricted C.3bs extension are finalized, registered and fully root/two-peer audited. No general SNC or higher-dimensional conclusion is claimed here.

## 1. Exact two-component compatibility gate

For a projective SNC surface E=S∪_C T in characteristic p, rational closed-union K-descent gives the homotopy fibre of K(S×P)⊕K(T×P)→K(C×P) for every fixed smooth proper parameter curve P. A component family must have equal actual restrictions in perfect K0(C×P). Equality of its two endpoint restrictions alone is insufficient.

For a smooth curve A⊂S meeting C transversely, and a Poincare-type line bundle M on A×P, the restriction of the associated component zero-cycle family has the concrete form

    ζ = Σ_{x∈A∩C} m_x [x] ⊠ c1(M_x) ∈ CH0(C×P)_Q.

Each M_x has degree zero on P. Thus the Albanese coordinate on C vanishes. Tensoring M by the pullback of N∈Pic0(P) leaves the endpoint line-bundle classes on A unchanged and changes ζ by [A∩C]⊠c1(N). If n=A·C>0, divisibility of Pic0(P)(k) permits a choice N^n=(⊗ M_x^{m_x})^−1, killing the P Albanese coordinate as well. The remaining obstruction is an explicit element of the Albanese kernel of C×P, represented by

    Σ m_x ([x]−[c0]) ⊠ c1(M_x).

This is only an exact residual expression. It does not assert nonvanishing, injectivity of an exterior-product map, or survival in the puncture quotient. If a component cycle is Albanese-trivial, one may arrange its parameter in a connected reduced kernel of a curve Jacobian map after a rational multiplier, but that alone does not kill this residual product class.

## 2. A complete proper-family correction in C.3br

The final C3_triple_free_component_lifting.tex proves the following stronger positive case. Suppose E has no triple points and the joint alternating restriction

    ρ: ⊕ Pic(E_i)_Q → ⊕ Pic(C_e)_Q

is onto. Move a component point difference on a smooth proper curve P in that component, transverse to all double curves and with endpoints off them. Its edge restrictions are finite sums [c]⊠[p], with every parameter point p different from the two endpoints. For each such p, use ρ to lift the finite edge Picard tuple to component divisor classes. Their exterior products with [p] correct every edge restriction simultaneously and have zero endpoint values. Actual K-descent then produces a perfect family on the fixed E×P. No family-level Picard-surjectivity theorem is required.

The same ρ hypothesis kills the point-parameter K1 edge kernel through Picard-times-units generation. Thus the full top gamma group is the direct sum of component CH0 groups, and its proper-perfect-family quotient is just the component degrees. For a negative exceptional divisor with rational double curves and no triple strata, the normal self-intersection identity supplies an explicit diagonal right inverse to ρ. The exceptional degree matrix then kills all degrees. This proves B²_Q=0 in the exact C.3bm resolved scope, without restrictions on component Albanese kernels. It does not cover general positive-genus edges or any triple strata.

## 3. Exact primary readings in this window

* Pedrini and Weibel (1994), *Divisibility in the Chow group of zero-cycles on a singular surface*, Astérisque226,371–409. Full author primary https://sites.math.rutgers.edu/~weibel/archive/papers-dir/PW-divisibility.pdf opened; Lemma5.2 and its complete proof pp395–396 freshly read. This proves reduced-curve Picard-times-units generation of SK1. Official metadata/pagination independently checked at https://www.numdam.org/item/AST_1994__226__371_0/. No proper-parameter equivalence theorem is attributed to it.
* Quillen (1973), *Higher algebraic K-theory I*. Full original scan https://www.sas.rochester.edu/mth/sites/doug-ravenel/otherpapers/Quillen-Higher-I.pdf opened; Section7 regular K=K′ context, Proposition2.10 projection formula and proof, Proposition3.2 and equation(3.3) with full localization proof, original pp124–128, freshly read. Existing key rootQuillen1973 is reused.
* Geisser–Hesselholt (2011), primary https://math.mit.edu/~larsh/papers/025/bounded.pdf, TheoremsA/C pp29–30 freshly read. Weibel, ChapterII, Proposition4.9 and Theorem4.10 with proofs pp32–33, Corollary8.8.2/Remark8.8.5p83 freshly read. Exact singular-boundary Adams naturality reuses the already audited Levine1994 p258 arbitrary-scheme iterated-fibre/delooping construction, not the regular-only statement of Lemma2.1.
* Esnault–Srinivas–Viehweg (1999), *The universal regular quotient of the Chow group of points on projective varieties*, Inventiones135,595–664, DOI10.1007/s002229900890. Full70-page primary https://userpage.fu-berlin.de/esnault/preprints/ec/inv99.pdf opened, but only the introduction and Theorems1–2 pp595–598 were read in this block. Their universal regular quotient/finite-dimensionality criterion does not identify the present proper-perfect-family relation group. No full-proof audit or numbered-theorem input is claimed.

## 4. Remaining triple-stratum question

The initially proposed extension by support avoidance alone is insufficient: rational equivalences of edge point divisors can have different evaluations at the marked triple points. Equality of K0 restrictions by itself does not specify the coherent vertex nullhomotopies in closed-union descent. The canonical totalization and those homotopies must be controlled.

The final C3_component_lifting_no_top_dual_cohomology.tex (C.3bs) supplies one precise sufficient condition: H²(Δ,Q)=0. A rational right inverse to the edge-to-vertex incidence matrix, followed by constant K_j(P) pullback, is onto in every homotopy degree for every actual fixed parameter P. Thus both π0(T_P) and π1(T_P) inject into the edge groups. With full joint rational Picard surjectivity, this proves the complete component-map isomorphism and the actual graph correction even with triples. Negative rational edges supply the Picard hypothesis by C.3bq's triple-sensitive energy identity. The result is fully root/two-peer audited and registered; nonzero H² remains outside.

For rational double curves and an arbitrary dual complex, the projective-bundle formula shows the edge-to-vertex map on K1(C_e×P)_Q has the same image as the constant coefficient map δ¹⊗K1(P)_Q: the reduced O(1) summand restricts to zero at every marked point. Therefore the possible vertex obstruction of a component tuple whose edge K0 classes cancel belongs to H²(Δ,Q)⊗K1(P)_Q. This is the exact remaining coefficient group, not a proved nonzero obstruction for a particular family. Divisor corrections with zero endpoint classes can still have nontrivial values in this group. Rationality of the edges or avoiding the vertices does not itself remove it. No surviving ordinary quotient is inferred.

### Further precise limits,18:28 work window

For a corrected graph tuple, pushforward along the proper parameter relates the degree part of its K1(P) obstruction to the gluing obstruction of the resulting tuple of component divisors. The sum of the finitely many chosen Picard lifts can be prescribed to equal the original component graph-divisor tuple by adjusting one lift in ker(ρ). This suggests a normalization of the degree-unit part, but does not dispose of the remaining Pic0(P)-times-units coefficient. No completed theorem from this observation is asserted.

A proposed companion-family construction also has an exact properness limitation. Locally a point approaching a double curve from one component can be paired with a point on the other branch to form a Cartier family. A high linear system can interpolate finitely many such local repairs. On a proper parameter, however, a nonconstant map to that linear system generally meets the hyperplanes imposing the other boundary intersections. Avoiding every additional boundary collision would force the map into an affine complement and is not automatic. The new collisions require a global compatibility argument; this does not yet extend C.3bs to nonzero H².

The next literature question is whether the proper-parameter part of the Levine–Weibel zero-cycle group on an SNC surface is controlled by its generalized Albanese affine part, in a form compatible with actual perfect K0 families. The already opened universal regular-quotient and motivic-comparison theorems do not by themselves supply that claim. No representability, finite-dimensionality or family-lift conclusion is inferred from their abstracts or introductory formulations.

### Primary-source scope extension and the new separate edge route

The ESV source read recorded in §3 was expanded at18:30:42UTC to Definition1.7/Lemma1.8 and the complete Lemma1.12 proof, printed602–605, with the intervening Lemma1.10/Corollary1.11 proofs. The generalized Picard groups used there need not be proper. Thus the source provides generation and a regular-homomorphism criterion, not the desired proper-perfect-family compactification. Exact access and the newly checked Kohrita publication metadata are recorded in `INTRINSIC_TOP_SOURCE_SCOPE.md` §6.

After checkpoint21, cycles is typing a different, explicit marked edge-family argument: a norm-one cover makes the variable unit equal to one at every point supporting every vertex-evaluation divisor. A Dennis–Stein Čech construction and functorial sheaf-K descent are intended to give actual K1 families with literally zero restrictions to all marked vertices. The complete conditional totalization implication is typed separately in `C3_unconditional_edge_totalization.tex` (UK.1–7). It does not infer zero from endpoint restrictions alone. It uses the actual marked-family equality, treats the remaining K2(k) ambiguity by the proper-symbol family, and identifies the exact residual component Albanese-kernel quotient. At the time of this note this combined C.3bt proof is under independent audit and unregistered; no result is inferred merely from this research description.
