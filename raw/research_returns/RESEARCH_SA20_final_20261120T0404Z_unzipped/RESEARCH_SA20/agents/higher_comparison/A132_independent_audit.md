# Independent audit of A.132

19 November 2026, 19:29:56 UTC. AI-produced by GPT-6 Astra
(OpenAI, ChatGPT Pro mode), agent `/root/higher_comparison`.

**Verdict: PASS on the full written draft**, with its identity-component
restriction. Audited file:
`agents/singularities_duality/logs/A132_TOP_S3_counterexample_draft.tex`.
No shared paper or bibliography was edited by this audit.

The result is a counterexample to the unrestricted **real PL–TOP**
concordance comparison. It is not a counterexample to PL–SA or to
PL–definable comparison, and it does not fill their family-straightening
gate.

## 1. Original sources independently inspected

* Edwards–Kirby, *Deformations of spaces of imbeddings*, Annals93(1971),
  63–88. Full original opened at
  <https://www.maths.gla.ac.uk/~mpowell/Edwards%20Kirby.pdf>.
  Theorem5.1, printedp70, and the proof of Corollary1.2, printedp79,
  were read. The deformation is continuous in the embedding and fixes
  the inclusion. The statement has no dimension-four exclusion.
  Web references: `turn407243357view2`, `turn305896125view0`,
  `turn681130233view1`.
* Hatcher, *A proof of the Smale conjecture*, Annals117(1983),
  553–607. Original PDF at
  <https://pi.math.cornell.edu/~hatcher/Papers/SmaleConjecture.pdf>;
  the web fetch exceeded the service size limit, so the already
  downloaded original page images were directly viewed. Printedp605
  explicitly permits TOP in the natural comparison with Diff;
  printedp606 statement(16) gives the TOP(S3) version of the Smale
  equivalence. The required map is the natural orthogonal action,
  rather than an unspecified abstract equivalence of spaces.
* Freedman–Quinn, *Topology of 4-manifolds*, Th8.7A, printedp128:
  original image directly viewed, and the original PDF opened at
  <https://www.maths.ed.ac.uk/~v1ranick/papers/freedmanquinn.pdf>.
  It states that TOP(4)/DIFF(4) stabilizes by a 5-connected map.
* Gabai–Gay–Hartman–Krushkal–Powell, *Pseudo-isotopies of simply
  connected 4-manifolds*, ForumMathPi14(2026)e9,
  DOI10.1017/fmp.2026.10026. Full published original opened at
  <https://www.cambridge.org/core/services/aop-cambridge-core/content/view/76BC09B6D1CF91456A4189800D2B0494/S2050508626100262a.pdf/div-class-title-pseudo-isotopies-of-simply-connected-4-manifolds-div.pdf>.
  Section1.1, printedp2, defines TOP(4) as global origin-fixing
  homeomorphisms of R4 and TOP(4)/O(4) as the homotopy fibre of
  BO(4)→BTOP(4). The paragraph immediately after Th1.3 states the
  5-connected stabilization in exactly that convention. The corrected
  proof, rather than the unrepaired replacement criterion, is the
  current input. Web reference: `turn603138957view0`.
* Burghelea–Lashof1974II, original full text reopened at
  <https://www.academia.edu/103489177/The_homotopy_type_of_the_space_of_diffeomorphisms_II>.
  Printedp37 formula(3) is the low-degree comparison i<j;
  p38 gives the Kuiper–Lashof sphere fibration with no stability-range
  qualification; p43 equation(1) identifies the jointly PL sphere
  concordance space with hofib(X_n→X_(n+1)). Web reference:
  `turn497029282view0`. These are the actual original-paper body,
  not the host page's generated FAQ or abstract.
* Kirby–Siebenmann1977 original local text was inspected at
  AnnexC pp317–318: TOP/PL is K(Z/2,3), TOP/O has the same homotopy
  groups below degree7, and PL/O has zero homotopy groups through
  degree6. The alternative locator in the draft, EssayV Th5.5p251,
  is consistent with this independent printed locator.

## 2. Local extension and uniform parameter lifting

The E–K input is stronger than isolated isotopy extension: it supplies
one continuous local operator σ(v). Concretely, if φ(v) is the final
embedding supplied by the deformation, σ(v) is v∘φ(v)^−1 on their
common image and the identity outside. The input and final embedding
agree near ∂U, so the extension is well defined. Their images coincide:
the modification is compactly supported in the interior; equivalently
one applies invariance of domain to the extended compact modification.
Because φ(v) is the identity on C, σ(v)|C=v|C. The normalization at
the inclusion gives σ(id)=id. Its support lies in a fixed compact
subset of intD after reducing the input neighborhood. This justifies
the operator used in the draft and does not require choosing an
extension separately at each parameter.

For the horn problem, the representative f and the given horn lift
have equality on a common neighborhood after taking the minimum of
finitely many face radii. Composing with the fixed horn deformation
gives k_(t,s)=f_(d_s(t)) a_(d_0(t))^−1. Both k_(t,0)=id and
k_(t,s)=id for t on the horn are exact equalities on a common smaller
ball. Thus the relative condition is not lost during normalization.

The sequence of choices U, then C, then V is in the correct order.
Joint inverse continuity on the compact parameter space first gives
a fixed domain for every increment k_s k_s′^−1. The chosen V then
satisfies k_s(V)⊂intC simultaneously. Continuity in the compact-open
embedding space and compactness of the diagonal (t,s,s) give one time
mesh working for every t. No parameter-dependent mesh is used.

The induction b_s=σ(k_s k_sj^−1)b_sj is valid on the same V at every
stage: b_sj(x)=k_sj(x) lies in C, where σ equals the increment.
The extension fixes the origin since C contains it. On the horn all
increments are exactly the identity, hence b remains exactly the
identity. Multiplication by a_(d_0(t)) recovers the horn lift without
any change. The same finite construction, extended outside D, proves
the global germ-restriction lifting. Both restriction maps are Kan
fibrations.

## 3. Fibre and component checks

The strict disk kernel consists of families equal to the identity
on a common ball. It is the filtered union of K_ε. Restriction to
D\intD_ε gives exactly a concordance of S3 with the inner sphere
fixed and the outer sphere free. There is no additional boundary
factor and no requirement that the outer sphere be fixed pointwise.

For ε<ε0, radial conjugation from ε0 to ε stays in K_ε throughout
the homotopy. The inclusion K_ε0→K_ε is therefore homotopic to an
isomorphism. A finite representative or finite nullhomotopy in the
union uses only finitely many simplices, hence one radius. This proves
K_ε0→K is a weak equivalence in every degree, including components.

For the global kernel, h_s(x)=s^−1h(sx) contracts every finite family.
If h is the identity on D_ε, it stays the identity there for all
0<s≤1. On each compact set it becomes identically the identity for
small s, uniformly over the parameter family; the same holds for
the inverse family. This proves weak contractibility and also puts
the entire global kernel in the identity component.

A Kan fibration by itself does not show surjectivity onto all germ
components. This was flagged in the preliminary audit and correctly
resolved in the written draft: restrict to T0→G0 and lift finite
edge paths from the identity. This gives vertex coverage of G0,
and the contractible kernel proves the required based weak
equivalence. No theorem globalizing all isolated germs is being
silently used.

## 4. Compatibility of the based fibre model

Boundary restriction Homeo(D;0)→Homeo(S3) has its actual radial-coning
section and an Alexander-contractible kernel. The Alexander
contraction retains the origin and is jointly continuous, as its
displacement and inverse displacement are bounded by 2u.
Together with the natural Hatcher comparison this gives O4→A and
SO4→A+ as weak equivalences.

Every element fixing a neighborhood of the origin is orientation
preserving. Since A+ is connected, the strict fibre of A+→G0 remains
the full K. Radial extension outside the disk is a continuous group
map e:A→T; it commutes exactly with germ restriction and agrees with
the standard orthogonal action on O4. Consequently replacing G0 by
T0 and A+ by SO4 in the homotopy fibre retains the correct maps.
Negative orthogonal elements cannot lie over the identity component
of T by orientation. Thus hofib(SO4→T0)=hofib_1(O4→T), independently
of any other possible components of T. Looping the classifying-space
fibre gives the stated Ω(TOP4/O4) model.

## 5. Homotopy calculation and scope

Five-connected stabilization identifies π1,π2,π3 of TOP4/O4 with
those of TOP/O, namely 0,0,Z/2. Therefore the free-top TOP
concordance space has π0=π1=0 and π2=Z/2.

For PL the exact sequence of hofib(X3→X4) contains

    π3X4 → π2P_PL(S3) → π2X3.

Both outer terms are zero because 3<4 and 2<3 place them in
the verified low-degree stabilization range. The identical sequence
in lower degrees gives π0=π1=0. This proves the discrepancy without
using high-dimensional smooth-to-PL comparison, applying a
dimension-five theorem in dimension three, or substituting slice-wise
PL families for total-space PL families.

No mathematical gap remains in the written argument checked here.
The distinction is in π2 of actual TOP concordances. The question
whether the PL and semialgebraic concordance simplicial groups agree
is unaffected by this audit.
