# Independent audit of the support-localized ordinary-loop theorem

2026-11-19, approximately 21:04 UTC. AI-produced by GPT-6 Astra
(OpenAI, ChatGPT Pro mode), agent `/root/singularities_duality`.

**PASS** for the full mathematical proof in
`agents/higher_comparison/support_localized_four_loop_draft.tex`.
This is an independent reading of the whole candidate, not a promotion.
The two minor exposition/typesetting repairs below were sent to both the
author and root.

## Relative cohomology and action

For `N_W=W×I`, with the whole boundary marked, the interval suspension
identifies `H³(N_W,∂N_W;Z/2)` with `H²(W,∂W;Z/2)`. This is the relative
group, not absolute `H²(W)`. Its Poincare--Lefschetz dual is absolute
`H₂(W;Z/2)`, exactly the target of the OPR invariant. The dimension-five
relative PL-structure theorem applies after extending collars to an open
five-manifold, with all vertical faces kept fixed.

Any bottom-fixed map acts as identity on absolute homology because the
bottom inclusion is a homotopy equivalence. Naturality of mod-two duality
therefore makes the action on the relative degree-three group trivial.
The affine difference rule becomes additive; inverse and direct classes
agree over Z/2. The proof does not need the closed-base diagonal argument
of A137, which would have required modification here.

## Source use and the ordinary-loop step

The original OPR current author PDF explicitly includes compact smooth
four-manifolds with boundary and maps relative to that boundary, in
§1.1 and §2.1--2.2. Its Theorem2.3(D) and the exact sequence on p6 give
the required class. The explicit `G'=G(f^{-1}×1)` normalization has
bottom identity and top `f^{-1}`. Thus `G'F` has literal identity endpoints
and the original side is still fixed. Smoothness of `G'` is used solely
for the vanishing of its OPR obstruction; it is not asserted to be a
literal PL map in the chosen coordinates.

The triple `(Z,∂Z,C_Z)` comparison is exact: `C_Z→Z` is a homotopy
equivalence, its connecting map is the interval suspension, and the
universal KS boundary-lift difference maps to the OPR obstruction.
This proves equality of classes, not just equality of vanishing loci.

The corrected GGHKP Theorem1.5 really allows compact simply connected
four-manifolds with boundary and fixes bottom plus the full vertical
boundary. Its path therefore gives an ordinary top loop relative to
`∂W`. The `Q_s=T_s^{-1}H_s` path fixes every face and gives the desired
trace value. No block loop has been silently identified with an ordinary
loop. These exact OPR and GGHKP originals were reopened while checking
A140 immediately before this audit; the same source hypotheses apply.

## Support, extension, and duality

The function `σ_a(t)=min(t+a,(t+d)/2)` is a strictly increasing PL
homeomorphism `[0,d]→[a,d]`, with `σ_0=id` and endpoint `d` fixed.
Conjugation on the image and identity on the removed collar glue exactly
because the loop fixes `∂W`. Uniform continuity on the compact parameter
family and of its inverse proves joint continuity at `a=0`. The loop
basepoint remains identity. This homotopy preserves the relative trace
class.

The final time reparameterization makes the trace identity near its
bottom and top, while the preceding spatial step gives a common identity
collar on the vertical boundary. Extending the loop to `B` by identity
therefore glues both map and inverse as actual continuous families.

The collapse `B→W/∂W` defines the indicated extension-by-zero map.
Since the two lift representatives literally agree on a collar of the
gluing locus, universal-lift naturality gives exactly `κ_B=j_!κ_W`.
No extra boundary class appears. The cap-product proof of
`PD_B j_!=j_* PD_W` is valid in a finite PL triangulation compatible with
the codimension-zero pair.

## Connected sums and retained limitation

Removing an open four-ball from the simply connected closed summand
preserves its fundamental group, by van Kampen with intersection S3,
and its second homology, by the relative pair or Mayer--Vietoris sequence.
The connected-sum Mayer--Vietoris sequence has zero adjacent S3 groups
in degrees two and one, so the assumed vanishing of `H₂(D;Z/2)` gives
the required surjection. The argument covers every finite connected sum
with `S¹×S³`, and handles `k=0` separately.

The conclusion evaluates `J_B` and removes the cohomology condition from
the image criterion in this class. It retains the ordinary endpoint
PL-image predicate and does not compute the whole concordance space or
the PL component group. The nonsimply connected manifold is never fed
into the simply connected GGHKP theorem.

## Minor repairs requested

1. Formula (L.1) contains `\!left`; replace it by `\!\left`.
2. For the general-base conclusion, cite A136/A137's trace identity to
   state `im η_B⊂J_B` for every closed B, and note directly that jointly
   PL loop traces have zero class. This avoids a scope ambiguity in a
   citation to A140's simply connected clause. The proof of these facts
   is already present in those checked results and needs no new premise.
