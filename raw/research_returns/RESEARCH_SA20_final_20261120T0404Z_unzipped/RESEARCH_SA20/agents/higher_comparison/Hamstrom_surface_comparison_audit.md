# Independent audit: the natural PL–TOP comparison on surface concordances

AI-produced by GPT-6 Astra (OpenAI, ChatGPT Pro mode), inherited effort,
agent `/root/higher_comparison`; 19 November 2026, 19:43:37 UTC.
This is an audit and complete deduction for the proposed A.134, whose
author and promotion remain with `singularities_duality` and root.

## Exact original sources opened

Mary-Elizabeth Hamstrom, *Homotopy in homeomorphism spaces, TOP and PL*,
Bulletin of the American Mathematical Society 80 (1974), 207–230.
Original scan:
<https://www.maths.gla.ac.uk/~mpowell/Hamstrom%20homotopy%20in%20homeomorphism%20spaces.pdf>.
Independent web records `turn292267286view0`, `turn962989202view1`, and
`turn962989202view2`.

* Section 0.2, printed p.208, expressly allows compact manifolds with or
  without boundary. It defines `Top(N)` as the identity component of the
  full homeomorphism group, with the uniform topology.
* Section 2.1, printed p.222, first defines the PL maps as those members
  of `Top(N)` that are PL. Thus all PL maps in the TOP identity component
  are vertices; their PL path connectedness has not been assumed.
* The same section expressly distinguishes the topology of slice-wise PL
  families from the model used in the paper. Its simplices are jointly
  PL homeomorphisms of the total product `Delta^k × N`, preserving the
  parameter. Its homotopies are jointly PL on `Delta^k × N × I`,
  preserving both parameters. This is the model needed here.
* Theorem 2.3.1, printed p.224, gives PL local k-connectivity when
  `dim N <= 3`, in the precise total-family sense defined on p.222.
* Theorem 3.1.2, printed pp.225–226, expressly identifies the natural
  inclusion `PL(N) -> Top(N)` as inducing the homotopy isomorphisms.
  Its proof uses parameterized approximation, including relative
  nullhomotopies, rather than an abstract equivalence of weak types.

François Laudenbach, *Topologie de la dimension trois: homotopie et
isotopie*, Astérisque 12 (1974), printed p.7, Theorem 1.1:
<https://smf.emath.fr/system/files/filepdf/AST_1974__12__1_0.pdf>.
Independent record `turn563802260view0`; screenshot
`turn257668351view1`. The pointwise Moise theorem unambiguously states
that every homeomorphism between PL three-manifolds can be approximated
by a PL homeomorphism. The subsequent automorphism-space assertion has
an ambiguous quasi-simplicial footnote, so it is not used for the
higher-family theorem here.

The ambiguity is substantive: Morlet 1968, printed pp.315 and 341–344,
distinguishes projection-preserving simplicial automorphisms from
face-preserving quasi-simplicial automorphisms. Original scan
<https://www.numdam.org/article/ASENS_1968_4_1_3_313_0.pdf>, independent
records `turn527181164view0`, `turn438929812view0/1`.
Hamstrom supplies the needed unambiguous convention.

## Full-component bookkeeping

Let `G_PL(N)` be the full simplicial group of jointly PL automorphisms
and let `G_TOP(N) = Sing Homeo(N)`. Hamstrom's theorem directly gives
the comparison in positive degrees at the identity. It also suffices
for the components, but the following finite argument makes that point
independent of whether the phrase “homotopy groups” includes degree
zero in the source.

Every TOP component contains a PL map. Apply Moise–Bing approximation
to one homeomorphism in that component, choosing the approximation in
a path-connected neighborhood supplied by TOP local contractibility.

If two PL maps lie in the same TOP component, translate by the inverse
of the first PL map. We have a continuous TOP path `F_t` from the
identity to a PL map `f`. Its image is contained in the TOP identity
component. Fix the uniform smallness threshold `delta > 0` from PL
local 0-connectivity. By compactness of the time interval and uniform
continuity of `F`, choose a finite mesh and PL maps `a_i` approximating
`F_{t_i}`, with `a_0 = id` and `a_m = f`, so that consecutive `a_i` are
less than `delta` apart. Choose the approximations sufficiently close
that they still lie in the TOP identity component; TOP local path
connectivity allows this.

The displacement of `a_{i+1} a_i^{-1}` from the identity equals the
uniform distance from `a_{i+1}` to `a_i`. This map is PL and belongs to
the TOP identity component. PL local 0-connectivity therefore gives a
jointly PL isotopy from it to the identity. Compose with `a_i` to join
`a_i` to `a_{i+1}`. Finite concatenation after affine rescaling of the
time intervals is jointly PL. Consequently the original two PL maps
are PL isotopic. This proves injectivity on full components.

Translations now give the positive-degree comparison at every
component, and the natural map of full groups is a weak equivalence.
The proof uses no triangulation of the full continuous path by a
slice-wise PL interpretation.

## Bottom-preserving subgroup and the literal product splitting

Let `F` be a closed PL surface, possibly disconnected, and put
`V = F × I`. Let `G_CAT(V; F_0 setwise)` be the subgroup preserving
`F_0 = F × {0}` setwise. It is a union of components in either category.
Indeed a homeomorphism preserves the intrinsic boundary, and along a
continuous path the permutation of its finitely many connected
components is constant. In particular preservation of the indicated
union of boundary components is constant along a path.

The full natural comparison restricts to a weak equivalence on these
subgroups. Surjectivity on the relevant components follows by choosing
a PL representative in the same full TOP component. Injectivity and
the positive-degree groups restrict automatically, since all paths or
based families in a component remain in that subgroup.

Restriction to the bottom has the natural section
`s(a)(x,t) = (a(x),t)`. At every simplicial degree there are mutually
inverse maps

```
G_CAT(V; F_0 setwise) -> P_CAT(F) × Aut_CAT(F),
h -> (h s(r(h))^{-1}, r(h)),

(p,a) -> p s(a).
```

They commute with faces and degeneracies, preserve joint PL in the PL
case, and preserve continuous parameter families in the TOP case.
The kernel fixes the bottom pointwise; its top boundary remains free,
exactly as in the concordance space under consideration. These are
isomorphisms of underlying simplicial sets (the group law is a
semidirect product). They commute literally with the natural comparison.

Therefore the comparison on the bottom-preserving groups is the
product of the comparisons on `P(F)` and `Aut(F)`. A product map that
is a weak equivalence induces a bijection on each component factor
and an isomorphism on every homotopy-group factor: use the inclusions
and projections at the identity, or the componentwise product
description directly. It follows that

`P_PL(F) -> P_TOP(F)`

is a weak equivalence for every closed PL surface over the real
numbers. No separate surface automorphism theorem is required.

## Scope of the audit

**PASS** for the natural real PL–TOP comparison in base dimension two,
including the exact simplex convention, compact-with-boundary input,
full component argument, free top, and possibly disconnected bases.
This note does not prove PL–semialgebraic comparison, does not prove
the base-dimension-one case, and does not itself supply a final A.134
draft or authorize promotion.

## Addendum: complete A.134 draft independently read

The full draft `agents/singularities_duality/logs/A134_low_dim_TOP_comparison_draft.tex`
was subsequently read, including the circle, point, disconnected and
empty-base clauses. **PASS** for those additional clauses, for the
following exact reasons.

Scott's original thesis, *Some Problems in Topology* (Warwick, 1968),
was opened directly from
<https://wrap.warwick.ac.uk/61719/1/WRAP_THESIS_Scott_1968.pdf>.
Record `turn485277895view0` gives the full original; screenshots
`turn902980197view0/1` inspect printed pp.19 and 51. Chapter III,
Definition 0.1 on p.19 explicitly imposes PL on the total product and
commutation with projection. Chapter IV, Theorem 3.1(b)(iii), p.51
asserts that the natural evaluation map on the annulus induces
isomorphisms in all positive homotopy degrees. The proof on printed
p.53 explicitly uses the evaluation fibration; it was read in the
full text (`turn139520912view0`). The p.53 screenshot service timed
out, but the theorem screenshot and full proof text were available.

Evaluation at an interior point and evaluation at a bottom point are
homotopic by moving the point along a fixed path. With a PL path this
is a joint PL evaluation on each simplex; the induced continuous
homotopy also suffices. Hamstrom Theorem 2.2.4 and its proof on
pp.223–224 identify circle evaluation through the actual PL rotation
circle, with degree one. Thus bottom restriction is an isomorphism on
positive homotopy groups. The literal product splitting makes the
positive groups of `P_PL(S^1)` vanish; its component group is the
already checked A.123 computation.

Yagasaki's original arXiv:math/0010223 was opened at
<https://arxiv.org/pdf/math/0010223>, record `turn650920116view0`.
Lemma 2.1(ii), p.2 and proof p.3, gives contractibility of the identity
component of the annulus homeomorphisms fixing its bottom circle.
Epstein's original *Curves on 2-manifolds and isotopies* was opened at
<https://archive.ymsc.tsinghua.edu.cn/pacm_download/117/6005-11511_2006_Article_BF02392203.pdf>,
records `turn267848232view0` and `turn197981561view0`. Theorem A4,
printed p.107, supplies an isotopy from a homeomorphism to a PL one;
the paper's p.83 convention includes boundary. A point on the bottom
can be the fixed basepoint. Correcting the varying bottom map by its
product inverse, as in the draft, fixes the entire bottom and ends at
a PL concordance. A.123 then proves that the TOP group is connected.
Hence the identity-component calculation applies to the whole group.

The point case correctly uses total-product coning in the PL category
(Hamstrom Theorem 2.2.1, p.223), not bilinear interpolation. TOP may
use interpolation. Bottom fixation prevents permutation of distinct
cylinder components, so a finite disconnected base gives the exact
finite product, including different dimensions. The empty case is
the one-element simplicial group. These arguments prove the natural
comparison in all stated cases and justify transferring A.131's
explicit PL models to real TOP in this range.
