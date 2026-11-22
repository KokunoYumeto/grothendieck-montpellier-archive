# Independent audit of A.135

19 November 2026, 20:03–20:07 UTC. We performed this independent audit as
GPT-6 Astra (OpenAI, ChatGPT Pro mode), agent
`/root/higher_comparison2`, with the inherited effort configuration.
This note is an audit of the complete candidate, not a new numbered result.

**Verdict: PASS for the displayed homotopy-fibre sequence and exact
segment, with the two wording clarifications below.** We do not infer
that the four-dimensional comparison gate is closed.

## Candidate and original sources actually read

We read the complete candidate
`agents/singularities_duality/logs/A135_base_four_comparison_fibre_draft.tex`
saved at 20:01:38 UTC. We independently read the original
Kirby–Siebenmann, *Foundational Essays on Topological Manifolds,
Smoothings, and Triangulations* (1977), Essay V, using its full local
original PDF/text. We explicitly displayed and visually inspected the
original printed pages 229, 240, 251, 252 and 253 from the files
`agents/singularities_duality/logs/KS_relative_comparison_printed229.png`,
`KS_relative_comparison_printed240.png`,
`KS_relative_comparison_printed251.png`,
`KS_relative_comparison_printed252.png` and
`KS_relative_comparison_printed253.png`. We also read printed page 241
in the extracted original text.

The precise inputs are Essay V (1.5) and its relative paragraph,
p. 229; the relative classification square (3.1) and fibre equivalence
(3.2), p. 240; the ball application and Morlet theorem discussion,
pp. 240–241; Theorem 5.5(I), p. 251; and the universal
Kirby–Siebenmann homotopy-pullback description in §5.6, pp. 252–253.

## Ordinary top evaluation and the iterated fibre

The explicit horn extension uses a PL horn retraction and a relative
jointly PL prism homotopy, whose target is the convex simplex. Such a
homotopy need not consist of homeomorphisms and can be obtained by
extending its compatible PL boundary data. This avoids treating the
bilinear straight-line formula as jointly PL.

For the formula in (A.135.5), the correction family is the identity on
the horn; composing its parameter with the prism homotopy therefore
makes the correction identity at the bottom and on the prescribed
horn, while its top is the exact required correction. Every slice is
a homeomorphism. Total inversion and composition retain the joint PL
condition. Thus top restriction is a genuine Kan fibration with
literal kernel the group fixed on both ends. It need not be surjective
on vertices or on all components of the full automorphism group.

Taking based homotopy fibres vertically in the natural comparison of
these two fibration sequences gives
`F_H → F_P → F_A`: the two iterated homotopy fibres are the same
pointed homotopy limit. No additional component-surjectivity
assumption is being smuggled into this step.

## Collar conversion and relative theorem hypotheses

The collar function
`sigma_s(t)=min(t+s,(t+delta)/2)` is strictly increasing from
`[0,delta]` onto `[s,delta]`, is the identity at `s=0`, fixes `delta`,
and is at least `t`. Its inverse on its total image is
`max(t-s,2t-delta)`, so both total maps are PL. Conjugation on the
compressed cylinder, glued to the identity on the removed collars,
is therefore joint PL, as well as continuous in the TOP category.
The gluing agrees exactly because both original ends are fixed.
Since `sigma_s(t)≥t`, an existing fixed collar remains fixed.
Identity parameter faces remain exactly identity. Finite representatives
and nullhomotopies consequently yield the asserted weak comparison.

**Common-collar wording:** `H_C^col` should be defined as the
simplicial complex whose each parameter simplex fixes one common
collar. It should not silently mean the singular complex of the union
of the pointwise collar-fixed subgroups with the subspace topology:
compact families in such a union need not have a common collar.
The candidate's compression argument supplies the needed uniform
collar for each finite family and makes the intended definition work.

After attaching exterior collars, `M=B×R` is a boundaryless
five-manifold and `C=M\(B×(0,1))` is closed. The relative version on
p. 229 fixes a neighbourhood of this closed set, exactly the
common-collar convention. Compact support in the finite cylinder
equates locally finite PL on `M` with the finite joint PL convention
used for the original families.

The quotient's image in the structure space is only a union of
components, as the original p. 229 explicitly says. It contains the
whole component of the standard structure. Based looping therefore
gives `F_H ≃ Omega S_alpha`; there is no inference that all relative
PL structures have the original PL isomorphism type.

The relative restriction map of (3.1) is a fibration in dimension
at least five. Its exceptional four-dimensional hypothesis is
`H^4(M,C;Z/2)=0`; it is not needed for the present five-dimensional
ambient manifold. The candidate correctly explains why a closed
three-dimensional base does not satisfy the analogous relative
four-dimensional hypothesis.

## Untwisting and the two loop shifts

Theorem 5.5(I) identifies `TOP(5)/PL(5)` with the stable fibre
`K(Z/2,3)`. Section 5.6 explicitly constructs the universal
Kirby–Siebenmann square with the path space over `K(Z/2,4)` and
states its relative version. The chosen standard PL lift supplies a
nullhomotopy. Comparing to that fixed nullhomotopy trivializes the
relative lift space; no claim based merely on a trivial action on
`Z/2` is needed.

We obtain `S ≃ Map_*(N/partial N,K(Z/2,3))`, with the standard
structure at the constant map. Maps fixed near the boundary and maps
fixed on the boundary have the same finite-family homotopy theory by
collar compression. Since `N/partial N = Sigma B_+`, looping once
for the automorphism-comparison fibre and once by suspension
adjunction gives

`F_H ≃ Map_*(B_+,Omega^2 K(Z/2,3)) = Map(B,K(Z/2,1))`.

This is the whole based homotopy fibre: its components are
`H^1(B;Z/2)`, its fundamental group at the constant map is
`H^0(B;Z/2)`, and all higher homotopy groups vanish. The displayed
long exact segment, including the leading zero, is correctly indexed;
`pi_j F_P → pi_j F_A` is an isomorphism for `j≥3`. The final terms
have the stated pointed-set interpretation.

## Scope retained

**Extension-data wording:** the abstract weak homotopy type of `F_A`
alone does not determine `F_P`. The fibration and its connecting or
extension data remain part of the reduction. The theorem identifies
the fibre of the natural map and gives the exact segment; it does not
classify `F_P` from a bare list of groups of `F_A`.

We found no mathematical gap in the candidate within these scopes.
We do not infer contractibility of either free-top or automorphism
comparison fibre, surjectivity on original components, or a
higher-parameter PL-to-semialgebraic comparison. We made no edits to
included TeX, result tables, check ledgers, or bibliography while the
checkpoint freeze was in force.
