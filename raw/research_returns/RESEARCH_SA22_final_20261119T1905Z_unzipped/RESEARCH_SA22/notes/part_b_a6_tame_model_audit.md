# Independent audit: mixed-characteristic tame model independence

**Reviewer:** GPT-6 Astra (OpenAI), `/root/part_b_cycles`.
**Completed:** 2026-11-19 16:27:36 UTC.
**Scope:** The first theorem, `A6-tame-specialization`, in
`sections/part_a6_scope_supplement.tex`, lines 6–161 as read. This audit does
not purport to check the subsequent Frobenius or node propositions.
**Outcome:** passed; no correction requested. The statement is about an
existing proper integral log-regular fs model and its boundary-tame cover
category. It neither assumes a mixed-characteristic resolution theorem nor
reconstructs a chosen special fibre as a scheme.

## Original source actually reopened

Yuichiro Hoshi, *The exactness of the log homotopy sequence*, RIMS1558,
July 2006 author preprint:
<https://www.kurims.kyoto-u.ac.jp/preprint/file/RIMS1558.pdf>.

- Corollary 3.9, printed pp.31–32 (PDF indices30–31), was reopened at
  `turn636486270view0`, source lines2451–2595. Its hypotheses are a proper
  morphism from an fs log-regular total space to an fs log base whose
  underlying scheme is the spectrum of a complete local ring. It identifies
  finite Kummer-etale covers of the total space with those of the strict
  closed log fibre. No characteristic-zero residue hypothesis occurs.
- Proposition A.10, printed pp.57–58 (PDF indices56–57), was reopened at
  `turn636486270view1`, source lines5201–5329. Its boundary condition is
  expressly tested at points with local-ring dimension one. Its proof uses
  the divisorial description of a log-regular structure at lines5283–5308
  and invokes log purity for essential surjectivity at lines5326–5329.
- Initial full-source reference: `turn449884714view0`; find references:
  `turn535673922view0`, `turn535673922view1`. Screenshot requests for PDF
  indices30,56,57 returned references `turn657853534view0`–`view2`.

The cited locators refer to the author preprint, as the existing bibliography
already says; they are not asserted to be the published version's numbering.

## Hypothesis and valuation check

The two models are over the **same** complete noetherian DVR `R`, with the
**same identified interior** `U`. They are not merely models of birationally
equivalent opens. Properness includes finite type and separatedness of the
underlying scheme morphism. Completeness makes `R` excellent; finite-type
models and their local rings are consequently excellent, so the finite
normalizations used in the covering discussion exist as finite morphisms.

Let `V -> U` be boundary-tame for the first model `X`. Hoshi A.10 first
extends it to a finite Kummer-etale cover of `X^log`. For a codimension-one
boundary point `eta` of the second integral normal model `Y`, its local ring
`A = O_(Y,eta)` is a DVR and has fraction field `F(U)`. The original map
`Spec A -> Y -> Spec R` and the generic-point map to `X` form precisely the
diagram required by the valuative criterion for the proper morphism
`X -> Spec R`. Hence there is a map `Spec A -> X` extending the fixed
generic map.

Give the trait `Spec A` the log structure of its closed point. A local
section of the divisorial log structure of `X` is a regular function whose
restriction to `U` is invertible. Its pullback is regular in `A` and nonzero
in `F(U)`, hence belongs to the divisorial log monoid of this trait. The
construction respects restriction, units, multiplication and the structure
map to the ring. It therefore is a log morphism. This reasoning is valid
also for a horizontal divisor: there the uniformizer of `R` pulls back to
a unit, which is allowed for a log morphism.

Finite Kummer-etale morphisms remain finite Kummer-etale under **fs log
base change**. The resulting log trait is regular with its boundary log
structure. Applying A.10 to that trait shows its generic cover is tame.
On the generic point all log structures are trivial; consequently that
generic cover is exactly the restriction of `V`, not a different
extension created by saturation. Thus `V` is tame at `eta`. Doing this for
every codimension-one boundary point of `Y`, then reversing `X` and `Y`,
proves equality of the full subcategories in `FEt(U)`.

This proof does not infer tameness at untested exceptional valuations from
a numerical ramification calculation. It pulls back an existing
Kummer-etale extension to each required trait. Log purity has already
supplied that extension under the actual log-regular hypotheses. This is
why the argument works without a common regular refinement.

## Category, arithmetic and frame checks

The functor `E_X = j_X^* (i_X^*)^{-1}` has the direction stated in the
manuscript: from closed-log-fibre covers to the common subcategory of
`FEt(U)`. A comparison `E_Y^{-1} E_X` therefore has the required direction.
Its normalization by restriction to `U` removes the otherwise unspecified
natural-isomorphism choice. Full faithfulness gives uniqueness and the
composition coherence. For an actual log morphism of models fixing `U`,
the pullback has that same normalization, so is that equivalence.

Pullback of a connected finite tame extension of `F` is connected because
`U/F` is geometrically connected. This verifies the Galois-category
criterion for the asserted surjection to `G_F^t`. The notation does not
silently replace this quotient by `G_F` when the residue characteristic is
positive.

After passing to the maximal unramified extension, its residue field is
separably closed. A finite tame extension has separable residue extension,
prime-to-residue-characteristic ramification index, and no defect in this
excellent henselian discrete valuation setting. Extracting a root of the
unit by Hensel's lemma gives the usual compatible uniformizer-root
description. The compatible roots and the separable closure are choices,
as explicitly used in the proof; their inertia conjugacies are the usual
ones. The resulting inertia action is the prime-to-`p` cyclotomic action.
For `p=0`, all positive ramification indices are retained.

The change-of-frame sign was also checked directly. Write
`varpi'_m = u_m varpi_m`. If the old lift of `g in G_k` fixes `varpi_m`
and the new lift fixes `varpi'_m`, then the new lift sends `varpi_m` to
`u_m / g(u_m)` times `varpi_m`. This is the **inverse** Kummer cocycle,
as written. Roots of a unit congruent to one, with prescribed residue one,
are unique for the permitted indices, so the first-order-frame statement
has the stated tame scope.

## Scope retained

- Existence of a proper log-regular model is a hypothesis, not a claimed
  mixed-characteristic resolution result.
- The equality concerns boundary-tame finite covers of the same open over
  the same trait. It is not an equality with every finite etale cover in
  positive residue characteristic.
- The kernel `Delta^t` is defined from the displayed surjection and is not
  identified with the full geometric etale fundamental group.
- The statement yields compatible cover categories and framed extensions;
  it does not select or reconstruct one special-fibre scheme.

## Work performed

This was a hand proof and original-source scope audit. No finite
enumeration, symbolic calculation, new mathematical program, or numerical
experiment was run. Existing programs were not rerun. Ordinary text reads
and web-source opening/screenshot tools supplied the evidence above; no
program runtime is invented for this audit.
