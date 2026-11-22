# A.140 independent audit: realizing and evaluating the component obstruction

19 November 2026, after checkpoint 13. We write as GPT-6 Astra
(OpenAI, ChatGPT Pro mode), agent `/root/higher_comparison2`, with
inherited effort configuration. Root controls promotion and movement.

## Verdict and candidate

**PASS** for the complete mathematical proof in
`agents/singularities_duality/logs/A140_OPR_obstruction_realization_draft.tex`.
The concrete finite `S^2 x S^2` certificate locator is being supplied
by root and was still a comment placeholder when we read this version.
We do not count that pending locator as verification of an algorithmic
construction of any TOP loop; no such construction is claimed.

We read every step of the complete draft. The general realization
statement is conditional on the stated assembly summand vanishing.
The simply connected conclusion uses the corrected ordinary TOP
pseudo-isotopy theorem only after the block realization has supplied
an actual both-end-fixed concordance. The proof never identifies a
block loop with an ordinary automorphism loop.

## Original sources independently inspected

1. Orson–Powell–Randal-Williams, *Smoothing topological pseudo-isotopies
   of 4-manifolds*, full author original at
   <https://www.maths.gla.ac.uk/~mpowell/smoothing_pseudo_isotopies.pdf>.
   We reopened Section 2.1, printed pp. 4–5; Definition 2.1 and
   Lemma 2.2, p. 5; the exact sequence (1) and Theorem 2.3(D), p. 6;
   Section 3.1, pp. 7–9; and the explicit `PD o ks o Sm` definition
   on p. 9. We also read the original Definition 5.8 and the theorem's
   proof pp. 21–22 in the retrieved full text. We visually checked
   printed pp. 6, 7 and 9. Retrieval records:
   `turn241605972view0`, `turn362149453view0`,
   `turn349932861view0`, `turn349932861view1`, and screenshots
   `turn298375357view0`, `turn298375357view1`,
   `turn298375357view2`.
2. Gabai–Gay–Hartman–Krushkal–Powell, *Pseudo-isotopies of simply
   connected 4-manifolds*, full corrected author original at
   <https://www.maths.gla.ac.uk/~mpowell/pseudo-isotopy.pdf>.
   We reopened and visually checked Theorem 1.5, printed p. 2,
   together with the ordinary pseudo-isotopy convention on p. 1.
   Records: `turn241605972view1`, screenshot
   `turn298375357view3`. The theorem isotopes the entire ordinary
   pseudo-isotopy to the identity relative to the bottom and vertical
   boundary, not merely its top map.
3. Kirby–Siebenmann, printed p. 39, last paragraph: we independently
   viewed `agents/singularities_duality/logs/kirby_siebenmann1977_printed39.png`.
   It explicitly supplies compatible DIFF structures for PL manifolds
   of dimension at most four. Only existence for one manifold is used.
4. The relative universal KS square in Essay V, Section 5.6,
   pp. 252–253, and relative PL-lift classification are the exact
   original inputs independently inspected for A.135–A.137. We retain
   those audits; no smooth isotopy comparison in dimension four is
   inferred from them.

## 1. The two KS conventions agree as classes

Let `N=B x I`, `W=N x I`, and
`C=(N x {0}) union (boundary N x I)`. Normalize common product
collars before comparing the boundary lifts. A.137's class of a
both-end-fixed F is the difference of the pushed PL structure from
the standard structure in `H^3(N,boundary N;Z/2)`.

The OPR boundary smoothing is standard on C and pulled back by F on
the top N. Forgetting smoothing gives the same PL-lift extension
problem. The universal KS square identifies PL lifts with
nullhomotopies of the map to `K(Z/2,4)`, relative to the chosen
standard lift. Two boundary nullhomotopies that agree on C have
difference

`d in H^3(boundary W,C;Z/2) = H^3(N,boundary N;Z/2)`.

Their extension obstructions differ by the connecting map for the
triple `(W,boundary W,C)`. This connecting map is an isomorphism
onto `H^4(W,boundary W;Z/2)`: the inclusion C into W is a homotopy
equivalence, with both retracting to the bottom N. Thus the map is
the interval suspension. This establishes equality of the actual
classes, and does not merely compare whether they vanish.

OPR uses pullback, so d initially equals `kappa(F^-1)`. A.137 proved
both the affine-torsor cocycle and that every bottom-fixed F acts
trivially on this relative cohomology. Hence
`kappa(F^-1)=-kappa(F)=kappa(F)` over `Z/2`. Under Kunneth the two
interval factors give `kappa_B cross u cross v`; capping with
`[B] cross [I] cross [I]` yields `PD_B(kappa_B)`. This proves the
precise displayed identity `KS_OPR(F)=PD_B(kappa(F))`.

Collar normalization is relative to the boundary, so it changes
neither lift class. This takes care of literal agreement at corners
and uses no derivative regularity of F.

## 2. Literal concordances from the block realization theorem

The source explicitly defines its automorphism objects as Kan block
semi-simplicial groups; its pi_0 classes are pseudo-isotopy classes.
For `z in ker delta_*`, Theorem 2.3(D) supplies an element q in the
image of the block connecting map with KS value z. If q is
represented by `F:id -> f`, exactness says that f is smoothly
pseudo-isotopic to the identity. Choose such a smooth G, from f to id.

The formula `G'=G o (f^-1 x id)` has bottom id and top f^-1.
Thus `F_0=G' o F` has both endpoint maps literally equal to id.
Source additivity and zero obstruction for the smooth G' show that
its KS value remains z. The proof uses no assertion that a smooth
map is literally PL in the chosen triangulation. Instead, F_0's
identity boundary maps supply precisely the PL boundary condition
needed for the preceding relative identity.

Consequently `kappa(F_0)=PD_B^-1(z)`. Its ordinary free-top component
lies in I_B, so A.137 gives the asserted inclusion
`im lambda_B contains (L_B+J_B)/J_B`.

The no-2-torsion condition on `H_1(B;Z_(2))` kills the Bockstein:
its image is the kernel of multiplication by two. It therefore makes
L_B all of `H^2(B;Z/2)`. A.137's already audited kernel calculation
then supplies the displayed exact quotient. Neither the endpoint
predicate nor J_B is evaluated for an arbitrary B.

## 3. The ordinary-loop conclusion in the simply connected case

For simply connected B the assembly domain and the Bockstein target
vanish. The corrected GGHKP theorem says that the entire ordinary
space P_TOP(B) is path connected. Therefore I_B is the trivial
component group, and the general quotient statement already forces
`J_B=H^2(B;Z/2)`.

The stronger ordinary-loop statement is also proved directly.
Given v, choose the both-end-fixed F_0 realizing it. An ordinary
free-top path `H_s:id -> F_0` has top restrictions `gamma_s=e(H_s)`
forming a based ordinary TOP loop. The explicit maps

`T_s(x,t)=(gamma_(st)(x),t)`, `Q_s=T_s^-1 H_s`

are joint continuous homeomorphism families with joint continuous
inverses. Every Q_s fixes both ends. It runs from id to
`T_gamma^-1 F_0`. Common-collar normalization of this whole finite
parameter family makes relative lift invariance directly applicable.
Thus `kappa(Q_s)=0`, and additivity gives
`kappa(T_gamma)=kappa(F_0)=v`.

Based homotopies of loops give relative-end families of traces, so
eta_B is well defined. Pointwise multiplication of loops multiplies
the traces, and agrees with the group operation on pi_1 of a
topological group. A.137 additivity makes eta_B a homomorphism.
Its identification with the composite through `pi_0 F_A` is exactly
the geometric trace description from A.136. The homotopy-fibre
sequence therefore makes eta_B zero on the PL-loop image.
Equivalently, a jointly PL loop has a jointly PL trace and zero
relative difference class.

Surjectivity of eta_B and its vanishing on that image prove the
claimed failure of automorphism pi_1-surjectivity when H^2 is
nonzero. This is an automorphism comparison statement. The draft
correctly makes no extra claim about the corresponding higher
concordance groups or pi_0 P_PL.

## Scope and remaining certificate

All parameter and component distinctions used in the proof pass:
the block realization, literal both-end representative, ordinary
free-top path, ordinary top loop, and relative-end trace comparison
are separate justified steps. The auxiliary single-manifold smoothing
is sourced, while no family of PL isotopies is converted to a smooth
family. Root is independently verifying the explicit finite base
and H^2 calculation for `S^2 x S^2`; that finite certificate does not
replace the source theorems that realize the TOP loops.
