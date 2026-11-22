# Independent audit of A.137

19 November 2026, 20:25–20:33 UTC. We performed this audit as
GPT-6 Astra (OpenAI, ChatGPT Pro mode), agent
`/root/higher_comparison2`, with inherited effort configuration.
We read the full candidate
`agents/singularities_duality/logs/A137_base_four_component_image_draft.tex`.

**Verdict: PASS**, including the homomorphism, exact kernel and
finite elementary abelian quotient. We suggested two short
clarifications about arbitrary lifts and common collars, neither of
which changes the argument. No component-surjectivity conclusion is
being inferred.

## Sources and dependence

This audit uses the exact original Kirby–Siebenmann inputs already
independently opened and visually checked for A.135–A.136: Essay V
relative (1.5), p. 229; relative classification (3.2), pp. 240–241;
Theorem 5.5(I), p. 251; and the universal Kirby–Siebenmann square and
its relative chosen-lift description in §5.6, pp. 252–253.
Our A.135 audit records the explicit original-page views. We also
independently verified the whole A.136 proof and its geometric
description of `pi_0 beta_B`; its audit is recorded separately.

No statement about smooth four-manifold isotopy, block
automorphisms, or the excluded compact-boundary version of the
boundary classification is an input here.

## Relative obstruction with a literally PL top

After the established common-product-collar normalization, a
bottom-fixed TOP cylinder map with literally PL top pushes the
standard PL structure to a structure equal to the standard one
near both ends. The relative five-dimensional classification
therefore assigns its component a class in
`H^3(N,partial N;Z/2) = H^2(B;Z/2)`.

The zero test is exact. A zero class gives a path of relative
structures from the standard structure to the pushed-forward
one. The relative automorphism orbit captures the entire standard
component and has the needed Kan path lifting. Lifting from the
identity produces a TOP map `g`, joined to the identity through
maps fixed near both ends, with `g_* alpha = F_* alpha`. Hence
`g^{-1}F` is PL and the lifted path gives a TOP isotopy from `F`
to that PL map, fixed on both ends. Conversely such a relative
isotopy gives the path of relative structures and a zero class.

This does not assume that every relative PL structure is PL
isomorphic to the standard cylinder. Only the standard component
is used when its obstruction is zero. The top of `F` need not be
the identity; it is enough that it is PL, since the correcting
isotopy fixes that top pointwise.

## Additivity and trivial coefficient action

The relative structure classes form the natural torsor furnished
by the universal Kirby–Siebenmann lift description. A
boundary-PL homeomorphism acts affinely: it changes the origin by
its own class and acts on differences by its induced relative
cohomology map. This gives the stated cocycle rule, with pushforward
or inverse-pullback conventions agreeing after the action is shown
to be trivial.

For any bottom-fixed cylinder map, its top map is homotopic to
the identity by `pr_B F(x,t)`. Its action on the two boundary
cohomology factors is therefore the identity. The restriction
`H^j(N) → H^j(partial N)` is the injective diagonal map, so the
connecting sequence identifies `H^3(N,partial N)` with the
cokernel of the diagonal map on `H^2(B)`. Naturality gives trivial
action on the relative group. Consequently the cocycle is the
ordinary additive homomorphism on the subgroup of maps with
literally PL top.

The argument is valid for disconnected `B`: bottom fixing
preserves every cylinder component. Modulo-two coefficients avoid
any orientation assumption.

## Endpoint normalization and all ambiguities

The formula
`E_{gamma,s}(x,t)=(gamma_{s t} f^{-1}(x),t)`
is a genuine TOP isotopy of ordinary concordances, starts at the
identity, fixes the bottom, and changes the top of `h` from `f`
to `gamma_s`. It has a jointly continuous inverse, written
slice by slice. Thus the first endpoint condition in the theorem
is sufficient to carry out normalization. No endpoint-extension
condition is left implicit.

For two choices from the same initial top `f`, the difference of
the normalized cylinder maps is exactly the trace of the path
`eta_t gamma_t^{-1}`. Its endpoint is the PL map `b a^{-1}`.
The geometric description in A.136 therefore identifies its
relative class with an element of `im(pi_0 beta_B)`. Additivity
gives precisely the claimed ambiguity.

Conversely every element of that image is represented by such a
trace, and each trace is joined to the identity through free-top
concordances. Postcomposition adds the desired obstruction class
while remaining in the same original component. The image is a
subgroup because `beta_B` is the loop of a based map under the
specified equivalence with the based loop structure space.

We suggested making the arbitrary-lift independence explicit.
If two endpoint lifts start at the identity and have the same
endpoint restriction at every time, their pointwise quotient is
a path in the group fixed at both ends, starting at the identity.
Its final map has zero relative class. Thus replacing the displayed
canonical lift by any such lift changes neither the class nor its
coset. This is the only extra check needed for the statement's
wording “lift this endpoint change”.

## Independence of the TOP concordance component

For the path `H_s` between two representatives with PL endpoint
maps, the correction in (A.137.13) has top `f_s a^{-1}`.
Consequently `Q_s=T_s^{-1}H_s` has exactly the same top `a` for
all `s`, and the bottom is the identity. After applying the
common-collar normalization to this whole path, its relative
structure class is constant. At the final time the correction
is the trace of a path from the identity to a PL map; its class
lies in `J_B`. This proves invariance on the original ordinary
TOP components, not merely on block concordance classes.

We suggested explicitly invoking common-collar normalization
at this step. Intermediate trace slices need not already be
products near the top, but the established normalization preserves
their constant PL top and gives a common collar. The candidate's
opening convention already authorizes exactly this operation.

## Homomorphism, exact kernel and finite quotient

The set `I_B` is a subgroup because it is the inverse image of a
subgroup under the endpoint homomorphism on components. We may
represent each of two of its elements by maps with literally PL
top. Their product represents the product of the original
components and again has PL top. Additivity of the relative class
therefore proves that the coset invariant is a homomorphism.

Every PL concordance has zero relative class, so its component
lies in the kernel. Conversely a zero coset permits postcomposition
by a trace with the opposite class. The corrected map has zero
relative obstruction and hence is TOP-isotopic, with both ends
now fixed, to PL. Both preliminary corrections stayed in the
original free-top component. Thus the kernel is exactly the
image of the PL concordance component map.

The first isomorphism theorem now embeds the quotient of `I_B`
by that kernel into `H^2(B;Z/2)/J_B`. This proves normality and
the finite elementary abelian two-group conclusion, with the
stated order bound. The obstruction homomorphism need not be
surjective. If `H^2(B;Z/2)=0`, the endpoint-image condition is
indeed the only remaining condition. The empty case is trivial.

## Scope retained

The component-image criterion is complete but remains conditional
on the actual endpoint-image predicate and the actual image of
`pi_0 beta_B`. Neither is evaluated in general. We found no
additional endpoint-extension assumption, missing component,
uncontrolled four-dimensional boundary, or illicit smooth/PL
comparison in the proof.
