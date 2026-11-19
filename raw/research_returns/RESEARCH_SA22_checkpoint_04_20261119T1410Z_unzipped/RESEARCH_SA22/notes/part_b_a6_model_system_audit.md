# Independent audit of the A6 compactification system

Reviewer: GPT-6 Astra, `/root/part_b_cycles`, 19 November 2026.
Target: `sections/part_a6_model_system.tex`, theorem labels `A6-model-system` and `A6-model-specialization`, as read at 13:26–13:31 UTC. This is a mathematical and source-hypothesis audit, not a computational test. No numerical program was run for it.

## Outcome

No substantive mathematical error was found. Both conclusions follow in their stated scope: characteristic-zero fields for the compactification system, and actual models of one fixed generic open over the one fixed trait `Spec(k[[t]])` for specialization. The source hypotheses do not require the additional semistability or saturated log-smoothness assumptions sometimes used in related homotopy-exact-sequence results.

Two wording refinements were sent to the author rather than silently editing the owned fragment:

1. Replace “its log structure maps canonically to that of S” by “it has a canonical morphism of log schemes to S^log.” The structural morphism points to the base, whereas the induced map on log-structure sheaves has the reverse pullback variance. The existing proof already uses the correct direction.
2. Special-fibre cover categories are compared with `FEt(U)` through extension to the total model and restriction to U. To spell out the stated normalization, write `E_X = j_X^* (i_X^*)^{-1}` with its comparison isomorphism. A comparison of two special-fibre categories is then unique **up to the unique natural isomorphism that induces the fixed identity after these identifications**. Bare uniqueness without that condition would ignore possible central natural automorphisms. The draft already says “induces that identity”; this is an explicit formulation of its intended condition, not a mathematical refutation.

## Common domination over an arbitrary characteristic-zero field

- A smooth geometrically connected finite-type k-scheme is geometrically integral: after algebraic closure it is regular, its irreducible components are disjoint, and connectedness leaves one component.
- Maps of proper models agreeing on the dense U agree everywhere, since the source is reduced and the target is separated. Properness of each map follows from the closed graph and proper projection.
- For `f:X→Y`, the prescribed U inside `W=f^{-1}(U)` is a section of the separated map `W→U`, hence closed; it is also open. As W is a nonempty open in an integral scheme, this copy is all of W. Thus no boundary point is mapped into U and the divisorial log morphism is defined.
- The reduced closure of the diagonal U in `X1×_k X2` is integral and proper. Its intersection with `U×_k X2` is the graph of `U→X2`, which is closed there; therefore U is indeed an open subscheme of the closure, rather than just a dense constructible subset.
- Set Z to be the reduced complement. Every singular point lies in Z because U is smooth. Temkin Theorem1.1.11 supplies a blow-up sequence supported on `Z∪Sing`, here just Z, with regular output and strictly monomial total inverse image of Z. Hence it fixes U and gives a reduced strict-normal-crossings boundary. Finite type over k gives the noetherian quasi-excellent hypotheses. Characteristic zero makes k perfect, so regular finite type implies smooth.
- Blow-ups of this integral graph closure along the relevant nonzero ideals are integral; the construction introduces no additional component disjoint from U. Properness over k persists. Its projections are the required arrows toward both original models.

No assertion of strong factorization is needed. In particular it is unnecessary to prove that both projections themselves are composites of blow-ups along smooth centres. The optional AKMW zigzag is a separate, correctly stated observation.

## Pro-object and variance

The category points from refinements to coarser models, exactly the direction for a cofiltered inverse system. Parallel arrows are already identical. Models over a fixed model, or over any finite list of models, form an initial/cofinal subsystem in the inverse-system sense: each relevant comma category is nonempty by common domination and connected by another common domination. The displayed `lim_j colim_i Hom(X_i,Y_j)` formula therefore gives the asserted canonical pro-isomorphisms.

For an isomorphism `φ:U→V` and a target model Y of V, the same Y marked by `j_Yφ` is an object of the source category. Its identity map gives the required representative toward Y. Compatibility with transitions is immediate; uniqueness follows after a common refinement because representatives agree on dense U. Applying the same construction to `φ^{-1}` gives inverse maps. No direction is reversed in the pro-system construction.

The anabelian conclusion is conditional on the expressly stated Isom-anabelian input. It reconstructs the system of all marked models from the reconstructed interior; it does not pick one preferred compactification or assert that each boundary stratum is anabelian.

## Models over the fixed trait

Let `R=k[[t]]`, `F=R[1/t]`. The map `U→Spec R` is separated of finite type, since U is finite type over F and F is a finitely generated R-algebra. The excellence of R and regularity of U put this directly within Temkin Theorem1.1.15 with `Y0=Y=U`. Its proof §3.5.3 starts with a compactification in which U is dense. Taking the component containing U if necessary leaves a regular proper integral model with the required boundary.

Any such integral model dominates the trait. Every nonempty affine coordinate ring is torsion-free over the DVR, hence flat. In each regular local ring, t is a unit times a monomial in those boundary parameters supporting the special fibre. This defines the morphism to the divisorial log trait, with no assertion that it is saturated or log smooth.

The same graph-closure and supported-resolution argument works over R because finite-type R-schemes are noetherian and quasi-excellent and contain Q. It preserves precisely the same embedded U. Common refinements are again proper, regular, integral and flat over R. The draft does not identify unrelated k-compactifications with R-models of a generic family.

## Cover-category specialization

For the regular model and its strict-normal-crossings boundary, the associated divisorial fs log scheme is log regular. Hoshi PropositionA.10 identifies its finite Kummer-étale covers with finite étale covers of its interior that are tame at codimension-one boundary points. All those residue fields have characteristic zero, so every finite étale cover of U satisfies that condition. Hoshi Corollary3.9 then applies to the proper log-regular model over the complete local base and identifies its finite Kummer-étale covers with those of the strict closed log fibre. The special fibre itself may be nonreduced and need not be log regular; the corollary assumes log regularity of the total space.

For `f:X'→X`, pullback has direction `KEt(X)→KEt(X')`. Restricting both sides to the same U gives the identity pullback there. The vertical restriction functors are equivalences, so f* is an equivalence. Their compatible strict-special-fibre restrictions then prove the same for `f0*`. Full faithfulness gives the normalized uniqueness and cocycle condition described above.

All maps are log morphisms over the **same** divisorial trait, so the induced outer fundamental-group identifications commute with the same augmentation to `G_F`. Pulling back along the **same** framed section `σ_t:G_k→G_F` gives the corresponding identical tangential extension. Changing the frame has the previously computed Kummer effect; changing a model adds none. This is a categorical specialization theorem for actual models of one U, not a claim that unrelated special fibres have isomorphic ordinary fundamental groups.

## Original sources opened by this reviewer

- Michael Temkin, *Functorial desingularization over Q: boundaries and the embedded case*, author version arXiv0912.2570v2, 6September2016: https://math.huji.ac.il/~temkin/papers/Embedded_Desingularization.pdf. Whole34-page PDF opened; exact Theorem1.1.11 p4, Theorem1.1.15 p5 and proof §3.5.3 p24 read. Web refs `turn221186016view0`, `turn750036382view0`, `turn750036382view1`, `turn221876856view2`; p4 screenshot `turn146682575view0`.
- Yuichiro Hoshi, *The exactness of the log homotopy sequence*, RIMS1558, July2006: https://www.kurims.kyoto-u.ac.jp/preprint/file/RIMS1558.pdf. Whole67-page PDF opened; exact Corollary3.9 pp31–32 and PropositionA.10 pp57–58 read with the stated hypotheses and proof setup. Web refs `turn221186016view1`, `turn221876856view0`, `turn221876856view1`; screenshots `turn146682575view1` and `turn146682575view2`. These are preprint locators, as the bibliography correctly states; publication numbering is not silently substituted.

The parent must open these source URLs itself before citing this branch's web references in the final chat. This audit records no new result on the broader Isom-anabelian hypothesis and does not replace its separately audited sources.
