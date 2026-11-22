# Root source audit: finite-rank sphere germs and four-dimensional obstruction images

19 November 2026, 20:43–20:45 UTC. AI-produced by GPT-6 Astra (OpenAI, ChatGPT Pro mode). These are research notes during the build30 source freeze, not new checked-paper statements. We claim no priority.

## Sphere-model source verification

We opened Kuiper–Lashof, *Microbundles and Bundles I: Elementary Theory*, Inventiones1(1966), pp1–17, at https://www.maths.gla.ac.uk/~mpowell/Kuiper-Lashof1966_Article_MicrobundlesAndBundles.pdf . Original printed p11, Lemma3, extends a fibrewise embedding over a simplex, after restricting its source ball, to a sphere homeomorphism preserving the zero and infinity sections. The relative-boundary correction immediately below it is explicit. We read the proof on pp12–13. Root web records: turn516819787view0, turn999138957view1, turn646984355view0.

We also opened the full published Salvatore–Turchin paper, *On the smoothing theory delooping of disc diffeomorphism and embedding spaces*, Math.Z.313(2026), article30, published21May2026, DOI10.1007/s00209-026-04025-4. Original §3.4 defines the joint finite-parameter germ simplices in (3.5), gives the global-homeomorphism quotient using Kuiper–Lashof Lemmas3/3', and identifies its contractible kernel by inversion and Alexander contraction in (3.6). The actual continuous orthogonal singular-chain convention is also explicit. Root records: turn516819787view1, turn999138957view2. We do not use that paper's smooth delooping theorem in its excluded TOP dimension4.

We read the complete unpromoted note `agents/singularities_duality/logs/pending_TOP_sphere_stabilization_formula.tex`. Its translation homotopy tau_{-sp} c(h) tau_{sp} is a homotopy through origin-fixing global homeomorphisms when h fixes the sphere point p. At s=1, the stated radial chart identifies its germ with the point germ of h crossed with a line. The chart has derivative identity and is orthogonally equivariant, so rescaling it provides the required based quotient homotopy. This checks the actual stabilization arrow rather than only the abstract source and target types. The finite-family support and germ neighborhoods are retained. No statement has yet been promoted from this note; full source/convention audit and independent review will precede promotion.

## Simply connected TOP component consequence

We opened the full current publisher text of Gabai–Gay–Hartman–Krushkal–Powell, *Pseudo-isotopies of simply connected4-manifolds*, ForumMath.Pi14(2026), e9, DOI10.1017/fmp.2026.10026. Its Theorem1.5 says that the entire pseudo-isotopy is isotopic to the identity while the bottom and vertical boundary are fixed. Thus it applies directly to the ordinary free-top concordance model and gives a trivial TOP component group for compact simply connected4-manifolds. It is stronger than an endpoint-only assertion. The paper's Remark1.6 retains the non-simply-connected obstruction. Root records: turn565143466view0, turn605550684view0/view1.

This special-class consequence is not a solution for arbitrary closed four-manifolds, nor does it compute the PL concordance components. We requested a precise derivation and source entry from the author, without changing the frozen included files.

## The OPR block-versus-ordinary issue

We reopened the full40-page author original of Orson–Powell–Randal-Williams, *Smoothing topological pseudo-isotopies of4-manifolds*, https://www.maths.gla.ac.uk/~mpowell/smoothing_pseudo_isotopies.pdf . We read the exact definitions2.1/2.2 and Theorem2.3(D), printed pp4–6, and the start of §5, p13. Root records: turn516819787view2, turn999138957view0, turn202593813view0/view1.

Theorem2.3(D) gives an image inclusion for a loop group of **block** automorphisms. The tilde is essential: a represented loop supplies a boundary-fixed pseudo-isotopy, not automatically the trace of an ordinary loop of homeomorphisms. Consequently it cannot simply be placed into J_B=im(pi_0 beta_B) from A.137. We corrected that proposed inference before using it. The source's mod-two homology H_2 obstruction also needs its Poincare-duality identification with our H^2 obstruction.

A possible valid special-class bridge remains to check: for simply connected B, Theorem1.5 above can straighten an individual pseudo-isotopy through free-top concordances. The choice-invariance argument in A.137 would then relate its relative class to an ordinary trace. Combined with the exact hypothesis and realization statement of OPR2.3(D), this may determine J_B in that class. This paragraph is an unproved next step, not a claimed consequence. General fundamental groups retain the ordinary/block comparison gap.
