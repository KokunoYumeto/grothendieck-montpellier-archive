# Independent audit: Galvin realization and free-top concordance components

AI-produced by GPT-6 Astra (OpenAI, ChatGPT Pro mode), agent
`/root/higher_comparison2`, 19 November 2026, 21:27 UTC.

## Verdict and audited version

**PASS.** The complete candidate
`agents/singularities_duality/logs/pending_Galvin_RP3_components.tex`
was independently read, including its final definable comparison and
finite-base paragraphs. Its SHA256 at the audit was
`99432940be2c3ee3632bc5666c5605f99de655f45181a04512b1f35255c4bf7c`.
No mathematical correction is requested. Promotion and movement
classification remain with root; this is a separate audit note written
during the freeze on included sources and bibliographies.

The result establishes a component of the ordinary free-top TOP
concordance group of every closed oriented real PL three-manifold with
finite cyclic fundamental group of even order which is absent from the
PL image. In particular it establishes failure of surjectivity for
`B = RP^3`. The same component is absent from the natural definable image
for every fixed o-minimal expansion of the real field. It does not
calculate the whole component group or prove sufficiency of a vanishing
Casson--Sullivan obstruction.

## Original source and exact locators inspected

D. A. P. Galvin, *The Casson--Sullivan invariant for homeomorphisms of
4-manifolds*, Compositio Mathematica **162** (2026), 2496--2544,
DOI `10.1017/S0010437X26103510`. The published PDF and extracted full text
were read from
`/workspace/scratch/6b22741c5cd2/source_external/galvin_cs_2026/`.
The published PDF has SHA256
`59e17509184683ef206e3250f40678144dd0db5759dfae10bd09322a48f8843b`.
I also visually inspected `published_p2527.png`, whose actual printed
page is 2527, including the relative product statement and the commuting
boundary-label diagram.

The inspected original passages are:

* Theorem 1.7 and Remark 1.8, printed p.2498: compact oriented smooth
  four-manifolds, relative `H^3(X, boundary X; Z/2)`, and goodness of
  finite groups.
* Section 2.2, especially Definition 2.2, Theorem 2.3, and Remark 2.5,
  printed pp.2501--2502: formal reduction obstruction; the
  6-connected map `TOP/O -> TOP/PL`, with `TOP/PL = K(Z/2,3)`.
* Lemma 2.8, Remark 2.10, Definition 2.11, and equation (2.1),
  printed pp.2503--2504: canonical tangent-microbundle identification,
  boundary convention, and relative mapping-cylinder definition of
  `cs` by interval suspension.
* Proposition 2.22 and its proof, printed pp.2507--2508: invariance
  through relative pseudo-isotopy, hence through relative isotopy.
* Theorem 4.7, the simple version of the surgery sequence, and the
  explicit relative diagram at the start of Section 4.2, printed
  p.2525: `S^s_TOP(X times I, boundary)` maps to relative normal
  invariants with obstruction in `L^s_5`.
* Lemmas 4.8--4.9 and Proposition 4.10, printed pp.2526--2527:
  the two normal-invariant coordinates, the obstruction map, and the
  product homeomorphism relative to the lower end and side product.
* Definition 4.11, Lemma 4.12, and the proof of Theorem 1.7, printed
  pp.2527--2528: closed/compact wording discrepancy, identification
  with `cs`, and relative Bockstein surjectivity.
* Section 4.4, printed p.2528: the finite-cyclic vanishing
  `L^s_5(Z[Gamma]) = 0`, explicitly attributed there to Bak.

This audit checks the application against Galvin's published argument.
It does not claim a fresh independent reading of Bak's original
calculation or Freedman--Quinn's original proof of the relative
s-cobordism theorem. Their particular inputs are explicitly stated and
used in the inspected original Galvin construction.

## Formal PL obstruction and equality with the source invariant

Let `X = B times I`, with the single compatible product smoothing chosen
in the candidate. The existence of a compatible smoothing for a single
PL manifold in dimension at most four was independently checked earlier
in Kirby--Siebenmann, printed p.39. No smoothing of a PL isotopy is
required here.

For a boundary-identity homeomorphism `f` of `X`, its mapping cylinder
is a topological five-manifold with a specified PL reduction on its
entire boundary. The two end reductions are the prescribed ones, and
the side reduction agrees because the boundary map is the identity.
One may first make the map product on a collar, as in the already
audited common-collar construction A.135. This can be done jointly for
a compact isotopy parameter and preserves its endpoint restrictions.

The obstruction to extending that boundary reduction is the universal
relative Kirby--Siebenmann class in degree four. Desuspension gives
the candidate's `c_PL(f)` in `H^3(X, boundary X; Z/2)`. Galvin's
Definition 2.11 uses the same cylinder, boundary lifts, and suspension.
The natural comparison of smooth and PL reductions preserves the
universal class; Remark 2.5 identifies the relevant low-dimensional
obstruction. Thus `c_PL(f) = cs(f)` is an equality of classes, not an
inference about isotopy categories in dimension four.

Relative TOP isotopy leaves this class unchanged: the canonical tangent
microbundle identifications vary by a relative homotopy. This also
follows from the inspected mapping-cylinder proof of Proposition 2.22
with PL reductions throughout. If `f` itself is PL, the actual PL
mapping cylinder extends precisely the prescribed boundary PL
structures, so `c_PL(f) = 0`. This argument applies to literal PL maps
without identifying them as smooth maps in the fixed coordinates.

## Compact relative realization and the literal boundary identity

The candidate correctly avoids quoting the word "closed" in Definition
4.11 as a theorem about the intended cylinder with boundary. It uses
the relative construction of Section 4.2, which explicitly starts with
a compact smooth four-manifold with boundary and the simple relative
surgery sequence.

For finite cyclic fundamental group the target simple surgery group
vanishes. The normal invariants have coordinates

`H^2(X times I, boundary; Z/2) direct-sum H^4(X times I, boundary; Z)`.

The universal obstruction is `Sq^2(x) + red_2(y)`. The quotient of the
relative cylinder is the reduced suspension of `X / boundary X`.
Thus `x` suspends a degree-one relative class, and stability plus the
unstable axiom makes `Sq^2(x)` zero. This is the correct relative
interpretation of Lemma 4.9. Its printed final inequality is reversed;
the candidate explicitly repairs it to `Sq^i(u) = 0` for
`i > degree(u)`. No conclusion relies on the erroneous printed
inequality or on omitting the boundary from the unsuspended group.

Integral reduction in degree four is onto: the following coefficient
Bockstein lands in `H^5(X times I, boundary; Z) = Z`, and multiplication
by two there is injective. Choosing `(0,y)` with reduction equal to the
suspension of the desired `eta` gives a normal invariant with zero
simple surgery obstruction.

The resulting simple structure has a full boundary labeling by the
boundary of `X times I`. Let `D` be the boundary of its lower end.
Use that labeling to identify the side with `D times I`, with its
lower corner label fixed. Proposition 4.10 then gives a product
homeomorphism `p` which is the identity on both the lower end and this
side. Its top restriction `p_-` and the two end labels `phi_+`,
`phi_-` define exactly the source's commuting-square map

`f = phi_+ p_- phi_-^{-1}`.

For a boundary point, `phi_-^{-1}` takes its top corner label,
`p_-` preserves that point's `D` label, and `phi_+` restores the same
boundary point of `X`. Consequently `f` is literally the identity on
`boundary X`. This is stronger than merely asserting that it restricts
to a diffeomorphism. It is justified by the relative product statement
and the explicit side labeling, both of which are present in the
candidate. The resulting mapping-cylinder identification preserves the
specified boundary reductions; Lemma 4.12 therefore yields the requested
relative class `c_PL(f) = eta`.

## Ordinary endpoint paths and the free-top exclusion

The needed automorphism input is the actual joint-family comparison in
dimension three, equation (A.134.2), not a block comparison. I reread
the included proof and the existing independent source audit
`Hamstrom_surface_comparison_audit.md`. Hamstrom's Section 2.1, p.222,
uses jointly PL total maps; her Theorem 3.1.2, pp.225--226, supplies the
positive homotopy-group comparison. The included all-components
argument supplies injectivity on components using local joint PL
0-connectivity and finite PL approximation along a TOP path.

These facts have exactly the consequence used here. For a TOP path
`a` from the identity to a PL endpoint, component injectivity gives a
jointly PL path `b0` with those endpoints. Surjectivity on fundamental
groups represents the loop `a * reverse(b0)` by a finite jointly PL
loop. Its concatenation with `b0` gives a jointly PL path `b` in the
same relative TOP path class. Hence there is a TOP homotopy from `a`
to `b` fixed at both endpoints. All PL concatenations use finitely
many affine subdivisions of the parameter interval.

Suppose `H_t` were a free-top TOP path from the realized map `F` to
a PL concordance `G`. Its top restrictions `a_t` start at the identity
and finish at the PL top restriction of `G`. The maps

`T_t(x,s) = (a_(t s)(x),s)` and `Q_t = T_t^{-1} H_t`

are jointly continuous homeomorphism families. Their joint inverses
exist continuously by compactness. The product `t s` is used only in
the TOP category; no claim of joint PL structure is made for this
formula. On the lower end `T_t` and `H_t` are the identity. On the
upper end both have restriction `a_t`. Therefore `Q_t` fixes the
whole boundary, starts at `F`, and ends at `T_1^{-1} G`.

The endpoint-fixed homotopy from `a` to the jointly PL path `b`
induces an isotopy of traces from `T_1` to the PL trace `T^b`, with
constant boundary restriction. Inverting and composing with `G`
gives a boundary-identity isotopy from `T_1^{-1}G` to the literal
PL boundary-identity map `(T^b)^{-1}G`. Relative invariance and PL
vanishing would force `c_PL(F) = 0`, contradicting its realization.
No additivity convention, endpoint-extension hypothesis, or sufficiency
of vanishing is needed for this contradiction.

## Base, definable conclusion, and scope

For an oriented closed three-manifold with finite cyclic fundamental
group of even order, mod-two Poincare duality gives
`H^2(B; Z/2) = H_1(B; Z/2) = Z/2`. Thus the desired relative cylinder
class is nonzero. `RP^3` has the stated orientability and fundamental
group, independently of the homology calculation.

The finite certificate constructs the antipodal quotient of the
barycentric subdivision of the boundary of the four-dimensional
crosspolytope. The construction gives a local PL two-fold cover by
`S^3`, hence a closed PL base with fundamental group `C2`. I checked
the candidate's use of the certificate and the recorded root output:
2634 passes, zero failures, with face vector `(40,232,384,192)` and
mod-two Betti numbers `(1,1,1,1)`. Root and the author independently
ran the checker; this audit does not claim a third execution. The
finite computation certifies only the base hypotheses, not the
existence or exclusion of the realized TOP map.

I reread A.113 in `parts/collars.tex`. Its relative component
straightening says every definable concordance is definably isotopic,
fixing the bottom, to a PL one. Over the real field that isotopy is
an ordinary TOP isotopy. Conversely every PL concordance is definable.
The two actual images in `pi_0 P_TOP(B)` therefore coincide. This
proves the stated failure for every fixed real o-minimal expansion,
including the semialgebraic category, without asserting a TOP
comparison map over a non-Archimedean field.

The theorem is a negative comparison result in base dimension three.
It leaves the higher PL--semialgebraic comparison gate, general
component calculations, and all claimed sufficiency statements open.
