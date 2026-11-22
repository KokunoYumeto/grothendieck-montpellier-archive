# Independent audit: assembly and the fully relative four-base comparison

Auditor: `/root/higher_comparison2`. Completed 20 November 2026 at approximately 03:14 UTC.

**Verdict: full authored-proof mathematical PASS, under the stated hypotheses.**

Audited candidate: `agents/singularities_duality/logs/pending_aspherical_four_relative_comparison.tex`.

Current version: 344 lines, 16,551 bytes; SHA256 `be04e6b4ca650fbb5312d91a58e0a722a2d6a29ddddd745dbc671670783373ca`.

The entire candidate was read. The author's final replacement of the collar-HEP sentence by compression of the entire homotopy was separately reread. This audit does not cover a subsequently proposed Farrell–Jones corollary unless an addendum is recorded.

## Exact original inputs reopened

Andrew Ranicki, *Algebraic L-theory and Topological Manifolds*, corrected author version dated 28 January 2018:
https://webhomes.maths.ed.ac.uk/~v1ranick/books/topman.pdf

The original text was opened directly at Definition 18.2 and its relative-boundary continuation, printed pages 197–198; Proposition 18.3, pages 198–199; Theorem 18.5, pages 200–201; and Example 24.16, page 278. Retrieval references are `turn275593766view0` through `turn275593766view3` (parent can independently reopen the URL).

The first location treats compact manifolds with boundary and specified boundary homeomorphisms. The ensuing relative paragraph authorizes the relative form of the normal-invariant/assembly identification. The torus example gives the relevant zero-connective assembly isomorphisms and Whitehead-group vanishing. These source statements are used in dimensions at least six; no four-dimensional surgery exactness is imported.

The previously audited A.135–136 supply the actual joint-family relative structure space, comparison fibre, and trace interpretation. They are not replaced here by a block automorphism comparison.

## Mapping-cylinder and boundary check

For the candidate's `V=B×I^r`, the homotopy `k_u:id→F` is relative to the entire boundary. Compressing both `F` and every `k_u` by the same collar embedding and extending by the identity makes this literal on one common collar. No homeomorphism property of intermediate `k_u` is needed. Reparameterizing `u` produces constant end intervals.

The map `U([x,u])=(k_u(x),u)` has identity boundary labels: at the upper face the coordinate is `y=F(x)`, at the bottom `k_0=id`, and on the side every `k_u` is the identity. The collar convention makes the map a product near every face. The bottom inclusions of both mapping cylinders are homotopy equivalences, so the common identity restriction proves that `U` is a homotopy equivalence. Its boundary restriction is a homeomorphism, giving a genuine relative normal invariant.

The target dimension is `dim(V×I)=5+r`. Thus the surgery obstruction of this actual homotopy equivalence vanishes in `L_{5+r}`. The normal invariant is identified with `H_{5+r}(B;L<1>)`; the assembly index is exactly `5+r`.

If that assembly map is injective, the relative normal invariant vanishes. Crucially, this includes its specified boundary comparison. It identifies the source stable TOP normal reduction with the target reduction pulled back through `U`, while retaining the fixed boundary identification. Pulling back the target's PL lift therefore extends the prescribed PL normal reduction on the whole boundary of the labeled source. Its relative Kirby–Siebenmann obstruction is zero. Tangent and normal versions agree here because they are stable complementary reductions. Changing the top reduction by `F` gives exactly the interval suspension of the PL difference `κ(F)`. The displayed relative suspension is an isomorphism. This proves `κ(F)=0` without converting a stable lift into an ordinary isotopy.

## Relative aspherical homotopy and traces

For `r≥2`, `B×∂I^r` is connected and its fundamental group maps onto that of `B×I^r`. A boundary-fixed map induces the identity on the latter fundamental group. Its lift fixing one boundary point fixes the entire connected preimage of the boundary. The contractibility of the universal cover removes every relative cellular obstruction to an equivariant homotopy to the identity. Choosing cells orbit by orbit produces a deck-equivariant homotopy; it descends and fixes the whole boundary. This also works after the collar replacement.

For a based `q`-cube in the relative automorphism group, the trace is an actual homeomorphism of `B×I^{q+1}`. Common spatial and parameter collars make it identity near its whole boundary. In the candidate's microbundle homotopy the second-point map is

`(y,p') ↦ (h_{p+t(p'-p)}(y),p')`.

For each fixed base point this has the inverse obtained from the inverse of the same homeomorphism slice. It preserves the zero section, joins the vertically stabilized derivative to the total trace derivative, and is constant on the prescribed boundary germs. Thus the family obstruction and the trace obstruction agree, including their relative identifications.

The indices are correct: `q=1` gives `r=2`, dimension seven for the mapping cylinder, and target `H¹(B;F₂)`; `q=2` gives `r=3`, dimension eight, and target `H⁰(B;F₂)`. Consequently `A_7` and `A_8` kill exactly the two maps asserted in the proof.

## Exact sequence and group law

The comparison fibre from A.135 is `Map(B,K(F₂,1))`. Its only nonzero homotopy data are the component group `H¹(B;F₂)` and the fundamental group `H⁰(B;F₂)`. The displayed long exact sequence therefore has the correct endpoints and no omitted higher fibre term.

Vanishing of the first trace map makes the component-kernel inclusion injective; vanishing of the second gives the asserted fundamental-group kernel and surjectivity. The degree-two comparison is then an isomorphism, and the higher comparisons follow immediately from the fibre.

This identifies groups rather than merely sets. The path-model fibre of a homomorphism is itself a group object, and its map to the PL group respects composition. Under the structure interpretation, the usual pullback term acts trivially on the relative cohomology: a bottom-fixed map is homotopic to identity on the whole cylinder, and both boundary restrictions are literally the identity. The diagonal-cokernel description in the draft then proves that relative action is identity. Thus the obstruction coordinates add, establishing the claimed group kernel.

## Components, centre, and the torus

For `r=1`, the disconnected boundary prevents the previous relative argument. The candidate correctly retains the central evaluation obstruction. Interpolating the interval coordinate reduces a boundary-fixed map to its loop of self-homotopy equivalences of the aspherical base. The elementary relative `K(π,1)` classification identifies that loop with an element of `Z(π)`.

Removing the trace of a jointly PL loop with the same evaluation class makes the map homotopic to identity relative to both ends. The assembly input is now `A_6`. Its vanishing PL difference can be converted to an actual relative TOP isotopy to a PL map because the cylinder has dimension five, where A.135 supplies the relative structure classification and orbit lifting. No dimension-four classification is used. The same calculation applies to the ordinary-loop part of `β_B`.

For the standard four-torus, Example 24.16 supplies the assembly and Whitehead conditions. The one-connective/zero-connective comparison in degrees six, seven, and eight has no extra term because ordinary homology above dimension four vanishes. The standard translation loops represent every central element and are jointly PL. The stated `H¹=(F₂)^4` and `H⁰=F₂` consequences follow.

## Scope retained

This is a computation of the fully boundary-fixed comparison kernels under explicit assembly assumptions, including a concrete torus case. It does not calculate the full free-top comparison, the part of `β_B` represented by paths ending at other PL components, or the endpoint-image condition. No splitting of either short exact sequence is proved. Those limitations are stated in the authored text and are essential.

## Addendum: complete Bartels–Lück corollary and finite certificate

Independently passed at approximately 03:18 UTC on 20 November 2026. The full revised candidate has 427 lines, 21,172 bytes, SHA256 `0b3f3f3cbe0039b134492c190771d1d0288e3994efd77c05c8bf9507dfc22a36`. Its new theorem wording and every added proof paragraph were read.

The published original of Arthur Bartels and Wolfgang Lück, *The Borel Conjecture for hyperbolic and CAT(0)-groups*, Annals of Mathematics 175 (2012), 631–689, was freshly opened at:
https://annals.math.princeton.edu/wp-content/uploads/annals-v175-n2-p05-p.pdf

Theorem B, pages 633–634, and Proposition 0.3(i) with its proof, pages 634–635, were read directly (retrieval references `turn630929786view0`–`turn630929786view2`). The source provides the low K-theory and ultimate L-theory assembly hypotheses, then explicitly derives ordinary simple-decorated assembly and the required Whitehead and lower K-group vanishings for torsion-free groups. The exact stated group class includes the two classes used in the candidate.

The torsion-free argument in the candidate is valid: restricting the finite-length free resolution from the finite aspherical four-complex to a subgroup of prime order gives a free resolution of the same finite length, contradicting the unbounded periodic cohomology of that subgroup. The restricted free modules need not have finite rank; only finite length is needed for this contradiction.

The cofiber of the one-connective cover into the full coefficient spectrum has homotopy only in degrees at most zero. Over a four-dimensional finite CW complex, the finite cellular filtration therefore has no homology in total degree greater than four. The homology exact sequence gives the required connective comparison isomorphisms in degrees six, seven, and eight. The author's stated range is sufficient; no extra stabilization or geometric Borel theorem is used.

The added general corollary keeps the centre-loop realization condition separate from the assembly conclusions. This is necessary and correctly stated.

The four-torus checker was independently read and rerun. Its separate mathematical and computational audit is `agents/higher_comparison/logs/A163_four_torus_checker_independent_audit.md`; independent output is `agents/higher_comparison/logs/check_A163_four_torus_independent.json`. The root output was preserved byte-for-byte. This certificate establishes the finite standard base and its stated chain data, with no computer claim about surgery or isotopies.
