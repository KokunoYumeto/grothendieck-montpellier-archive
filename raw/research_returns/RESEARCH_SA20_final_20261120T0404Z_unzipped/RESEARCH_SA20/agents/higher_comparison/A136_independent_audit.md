# Independent audit of A.136

19 November 2026, 20:10–20:21 UTC. We performed this audit as
GPT-6 Astra (OpenAI, ChatGPT Pro mode), agent
`/root/higher_comparison2`, with the inherited effort configuration.
We read the complete 299-line candidate
`agents/singularities_duality/logs/A136_base_four_stabilization_model_draft.tex`.

**Verdict: PASS for the full based comparison-fibre model, including
the geometric component obstruction.** We recommend the minor
zero-section wording correction recorded below. No claim about
surjectivity onto all TOP concordance components follows.

## Original-source verification

We independently read Kirby–Siebenmann (1977), Essay V, printed
pp. 217–218, 229, 240–244 and 251–253 in the original local full
PDF/text. For this audit we rendered and explicitly displayed the
original printed pages 217, 242, 243 and 244 at
`source_external/KS_printed217_A136_independent.png`,
`KS_printed242_A136_independent.png`,
`KS_printed243_A136_independent.png` and
`KS_printed244_A136_independent.png`, under the workspace parent.
In the immediately preceding A.135 audit we also explicitly displayed
the original pages 229, 240, 251, 252 and 253.

The decisive source locators are the footnote to Bundle Theorem 0.1
on p. 217; the quotient-orbit discussion and (1.5), p. 229; the
relative classification (3.1)–(3.2), p. 240; the strict collar square
(4.1), pp. 242–243; the natural stabilization diagram on p. 243;
Theorem 5.5(I), p. 251; and the universal Kirby–Siebenmann square
and its relative version in §5.6, pp. 252–253.

We checked the restriction printed below (4.4) on p. 244. The completed
boundary classification excludes four-dimensional boundary in the
present compact case. The candidate does not apply that theorem.
It uses the strict collar square while retaining the boundary
structure space, and applies classification only to the open
five-dimensional ambient manifold.

## Compact sliced structures and orbit components

A sliced PL structure on `Delta^q × B` gives a proper PL submersion.
The original p. 217 footnote explicitly supplies local bundle
triviality for proper CAT submersions and removes the compact case
from the dimensional difficulty of the noncompact bundle theorem.
The PL bundle over the simplex is trivial. If a vertex has the
standard PL isomorphism type, a choice of its identification produces
a total, parameter-preserving TOP family that carries the standard
structure to the given one.

Two such trivializations differ by an actual jointly PL automorphism
family. A prescribed horn can therefore be retained using the Kan
property of the simplicial PL automorphism group. Along any edge the
PL isomorphism type is constant. Iterating over edges shows that the
entire standard component, not just its vertices, lies in the orbit.
Other components may remain outside it.

Consequently the based homotopy fibre of `Aut_PL(B) → Aut_TOP(B)`
is the whole based loop space of the standard structure component.
Its possibly disconnected based loop space is not replaced by its
constant-loop component. This is the required full `F_A`.

## Product-collar normalization

The free-top version of collar compression is valid. On the
compressed cylinder we conjugate by `c_s`; on the removed lower
collar we use the identity; on the removed upper collar we use
`e(h) × id`. The inner upper boundary has the same map in both
formulas, so the gluing is exact. The family is joint PL in the PL
case, since the compression, its inverse on the moving image, and
the entire top restriction family are joint PL. It is jointly
continuous in TOP. At `s=0` it is the original family.

The inequality `sigma_s(t)≥t` preserves any already existing product
collars, and compression commutes with every boundary product map.
Identity parameter faces remain exact identity. Positive `s` gives
one common collar over a whole parameter simplex. This proves the
weak equivalence between the common-product-collar and ordinary
concordance complexes, including the relative nullhomotopies needed
for injectivity.

The same construction applies to a PL bundle trivialization whose
source and target carry possibly different sliced structures:
choose the compression width inside both common product collars.
The radial compression is PL for each structure, and the target and
source compressions agree as underlying radial maps. Extending by
the two actual boundary maps gives a PL isomorphism with product
collars. The lower boundary map is joint PL in the standard lower
structure; precomposition by its inverse times the identity on the
interval makes the trivialization exactly lower-relative. Any
prescribed horn then differs by a horn in the common-collar PL
concordance group and can be corrected there.

Thus the orbit quotient in (A.136.7) captures the full standard
component of the product-collar structure space. Based looping gives
the whole based `F_P`. Neither this argument nor the normalization
asserts that other relative PL structures have the standard cylinder
isomorphism type.

## The strict pullback and the dimension-five restriction

We checked the two directions of the strict pullback. A product
structure near the top of the compact cylinder extends uniquely as
that product on the whole upper exterior half-cylinder. The lower
standard structure extends uniquely to the lower exterior
half-cylinder. Conversely, equality with the prescribed product germ
near the entire closed upper half-cylinder yields a common product
collar of its finite boundary over each compact parameter simplex.
Restriction then gives exactly the original product-collar structure.

For the right vertical fibration, we first restrict structures on
`M=B×R` to `C_- union C_+`. The two closed sets have disjoint open
neighbourhoods, so their structure-germ complex is a product. Taking
the fibre over the standard lower germ yields the stated restriction
map `r`. The ambient manifold has dimension five and no boundary;
the ordinary relative restriction theorem applies. No exceptional
four-dimensional extension statement is needed. The image of `r`
may be confined to the standard target component; this is compatible
with the homotopy-fibre construction.

The lower half-cylinder inclusion is a collared homotopy equivalence,
so the relative lift space is contractible. The upper half-cylinder
retracts to `B`; its germ lift space is therefore the unbased mapping
space `Map(B,K(Z/2,3))`. The chosen standard PL lift and the original
universal Kirby–Siebenmann square provide the relative untwisting.
This applies to the rank-five tangent microbundle and leaves all
compact four-dimensional structure information in `S_B`.

Since the right map is Kan, the strict pullback is the homotopy
pullback. Contractibility of the upper-right corner identifies the
product-collar structure space with the based homotopy fibre of the
actual product-and-classification map from `S_B` to `Map(B,K3)`.

## Definition of beta and component exactness

We checked that the map `beta_B` is specified as a map of based
homotopy types: use the fixed classifying maps, standard PL lifts and
natural classification comparison choices, identify `F_A` with the
whole based loop space, and loop product with the normal line followed
by the rank-five classification. The target is
`Omega Map(B,K3) ≃ Map(B,K2)`.

Based loops preserve homotopy fibres. Applying this to the structure
pullback gives `F_P ≃ hofib_0(beta_B)` with all components of the
based comparison fibre retained. The next loop of the target is
`Map(B,K1)`, agreeing with A.135. The long exact sequence therefore
extends by `pi_0 beta_B` landing in `H^2(B;Z/2)`, and its kernel is
exactly the image of `pi_0 F_P`. The final assertions have pointed-set
exactness where stated. The abstract homotopy type of `F_A` alone is
insufficient: the actual map and its extension information remain.

## Geometric obstruction and the tangent homotopy

Let `gamma` be the indicated TOP path from the identity to a PL
automorphism `a`, reparameterized to be constant near the ends. Its
pushed-forward structures form a based loop because both endpoint
maps preserve the standard PL structure. The total cylinder map is a
homeomorphism with standard pushed-forward PL structure near both
ends. The claimed obstruction belongs to the correct relative group
`H^3(B×I,B×partial I;Z/2) = H^2(B;Z/2)`.

We checked the added microbundle homotopy directly. In pair
coordinates its base map is `(x,u) → (gamma_u(x),u)` and its second
point map is
`(y,v) → (gamma_{u+t(v-u)}(y),v)`.
After extending `gamma` constantly outside the interval, this is a
global homeomorphism in pair coordinates for each `t`. Indeed the
inverse recovers `u,v` unchanged, then recovers
`x=gamma_u^{-1}(x')` and
`y=gamma_{u+t(v-u)}^{-1}(y')`. Joint continuity follows from the joint
inverse family. It carries the diagonal to the diagonal, hence
restricts to a microbundle isomorphism germ. At `t=0` it is the
fibrewise tangent map with unchanged normal line; at `t=1` it is the
tangent map of the total cylinder homeomorphism. Near either end the
path is constant, so the homotopy is constant as a germ there. The
upper constant map is PL, which is precisely the required relative
PL compatibility.

This verifies equality of the two relative structure classes used
in the statement. The phrase “fixes the zero section” should be
replaced by “preserves the zero section over the base homeomorphism”:
the base point moves by `gamma`, so the assertion is not pointwise
fixing of the zero section. This is a wording correction, not a gap
in the construction.

## Limits of the result

We found no missing component, boundary or loop-shift hypothesis.
The result models the whole **based comparison fibre**. It does not
evaluate `beta_B` for an arbitrary compact four-manifold, compute
`F_A` in general, or establish surjectivity of the original
PL-to-TOP concordance map on components. We do not import a block
automorphism theorem, a smooth-versus-PL isotopy assertion, or the
excluded compact-boundary instance of (4.4).
