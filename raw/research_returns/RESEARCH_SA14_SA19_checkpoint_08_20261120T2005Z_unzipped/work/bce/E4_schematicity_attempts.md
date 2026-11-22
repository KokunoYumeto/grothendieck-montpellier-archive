# Remaining full-Picard schematicity gate

Status at 2026-11-20 18:32 UTC: **UNSETTLED**. GPT-6 Astra (OpenAI),
delegated agent `/root/bce`. This file records attempted arguments and their
failure points. It is not a counterexample or a proof of the general claim.

## Exact scope

The question on 57:315 is whether the full fppf Picard functor is a scheme
for a proper flat finitely presented **scheme** X over a scheme S with
geometrically normal, or merely geometrically integral, fibres. The broader
arbitrary-base reading is retained. Its answer must not be inferred from a
counterexample whose total family is only an algebraic space or whose
special fibre is geometrically reducible.

The following cases are proved in the current paper: projective families;
normal noetherian one-dimensional bases, in particular traits; and all
smooth proper curve families over arbitrary scheme bases (E4.Curve).
Geometrically normal curve fibres are smooth, so that case is included.
The integral-fibre question still includes nonnormal curve families, as
well as higher-dimensional families. A geometric-fibrewise H¹(O)=0
assumption also makes Pic quasi-finite and separated, hence schematic.

The smooth-curve proof is an existing argument: Česnavičius gave exactly
the BLR 6.6 Theorem 2(c) plus finite quotient argument in his answer dated
28 April 2015 to Poonen's question:
https://mathoverflow.net/questions/186723/does-every-relative-curve-have-a-picard-scheme .
This provenance has been checked; the paper's technical proof uses the
independently opened primary BLR and Stacks/SGA3 statements. No novelty is
claimed.

## Source-level exclusions

1. Kleiman, *The Picard scheme*, §4.18, and BLR §8.2 discuss the standard
   nonschematic Picard example x²+y²=tz² over R[[t]]. Its geometric special
   fibre has two components. It does not answer the integral-fibre question.
2. Laurent–Schröer, *Para-abelian varieties and Albanese maps*, §2 and the
   introduction, also refer to this general failure of schematicity without
   supplying a geometrically normal/integral-family counterexample.
   Proposition 2.2 concerns the fibrewise neutral **subfunctor**, not
   schematicity of the full Picard space. The two claims are distinct.
3. Raynaud's LNM 119, X.14 is cited in the original SGA3 VI_B §9 footnote
   as a nonschematic quotient of smooth affine groups. The complete
   construction in LNM 119 has not been accessed. Even that group-space
   example alone would be insufficient: a realization as Pic of a family
   satisfying the present hypotheses is still required.
4. The nonschematic genus-one torsors discussed in Laurent–Schröer §4
   and Zomervrucht are themselves algebraic-space families. Treating such
   a torsor as X would drop the scheme hypothesis.

Primary URLs checked include:

- https://arxiv.org/pdf/math/0504020 , §4.18, pp34–36.
- https://www.math.stonybrook.edu/~kamenova/homepage_files/Bosch_Raynaud_Neron_Model_tc.pdf , §8.2 pp209–211 and §6.6 pp164–166.
- https://arxiv.org/pdf/2101.10829 , introduction and §§2,4.
- https://webusers.imj-prg.fr/~patrick.polo/SGA3/origExp6B.pdf , §9.
- https://stacks.math.columbia.edu/tag/0DMD , separatedness under geometrically integral fibres and curve smoothness.

## Attempted constructions and exact obstructions

### Smooth genus-one scheme torsors

For a smooth proper genus-one scheme C, Pic^n is C/E[n] for n nonzero.
The finite locally free kernel E[n], together with the common-affine-open
property from BLR 6.6(c), makes this quotient a scheme. This route is
**excluded by a proof**, including n divisible by the residue characteristic.

### Singular integral genus-one curves

Here the smooth locus C_sm is a torsor under the generalized Jacobian G,
and Pic^n is the pushforward torsor under [n]. This is a potentially
smaller remaining instance, not a counterexample. In an elliptic-to-cusp
degeneration, [n] on G is not finite locally free: for n invertible the
generic kernel has n² points and the additive special kernel has one.
Consequently the preceding finite-quotient proof does not carry over.
Compactified Picard components may still have a canonical theta
construction, but effective descent of their schematicity has not been
proved here. No explicit nonprojective integral scheme family with a
nonschematic Picard component has been found.

### Higher-dimensional abelian torsors

One possible realization would be a scheme torsor T under an abelian
scheme A, with a Néron–Severi class δ such that the pushforward torsor
λ_{δ,*}T under A∨ is nonschematic. Finite-isogeny quotients are excluded
by the same finite-orbit argument. Over normal bases the local
projectivity/torsion results also obstruct this construction. A remaining
candidate would require a degenerate λ with positive-dimensional kernel
over a nonnormal base. DGJ does not know a theorem or a counterexample
settling that case. A finite-normalization descent argument might exclude
it too, but its required simultaneous affine-neighbourhood step has not
been proved. A positive-dimensional proper orbit cannot be placed inside
an affine open, so the finite-orbit proof cannot simply be reused.

### Projective bundles or modifications of a nonschematic torsor

A scheme total space of a projective bundle over a nonschematic torsor
would be attractive because of the projective-bundle Picard formula.
No such example satisfying the needed relative hypotheses has been
constructed. Taking a product with projective space does not work: the
nonschematic torsor embeds as a closed section. A Chow modification can
produce a projective scheme but need not remain flat over the original
base or have geometrically integral fibres. These are essential missing
hypotheses, not technical details that can be omitted.

### Relative Chow modification and pullback on Pic

The strongest positive route currently considered is to find a projective
surjection Z→X such that Pic(Z/S) is schematic and Pic(X/S)→Pic(Z/S) is
affine. Generic relative representability provides this only after
shrinking S. General Chow modifications do not supply flatness or
cohomological flatness over the whole base. Flattening changes the base
by a proper modification, and schematicity does not automatically descend
through it. Root independently identified the same obstruction.

## Next concrete checks

The smallest still unproved integral-fibre route above is a proper flat
integral genus-one scheme family with singular fibres over a base of
dimension at least two. The normal-fibre route first survives in relative
dimension at least two over such a base. These are **instances to attack**,
not a proof that every possible counterexample has those exact dimensions
when the base is nonnormal. No general outcome is claimed.

## Further checks, 19:09 UTC

The 2026 preprint by Dhillon–Nasserden, *Finite extensions of abelian
schemes and duality for commutative group stacks*, arXiv:2609.02826v1,
was downloaded from the primary arXiv PDF. Its introduction and Section3
were read. The scheme/projectivity assertion Theorem3.2 still assumes a
normal one-dimensional base, so it does not settle the arbitrary-base
question here. Its duality statements do not remove the Picard
nonflatness or realization requirements.

A direct finite-conductor pinching route is excluded under an explicit
positive hypothesis. Suppose nu:C'->C is finite surjective, is an
isomorphism off its conductor, the conductor C_con and its inverse image
are finite over S, and C'/S is locally projective. Then C/S is locally
projective. Indeed, after working near a given point of S, an ample L'
on C' restricts trivially to the finite inverse-image conductor. This
follows by localizing S at that point: a finite algebra over a local
ring is semilocal, and every invertible module on a semilocal ring is
free. Finite presentation spreads the trivialization to a neighborhood.
Glue L' to the trivial line bundle on the conductor through that
trivialization by the conductor fibre-product square. The resulting
line bundle L on C pulls back to L', so is ample by the finite-surjective
criterion. This argument needs the given conductor square; it does not
assert that normalization commutes with arbitrary base change.

The primary source Brion, arXiv:1310.0186v2, Section2.4 Proposition2.4(i),
printedp6, supplies exactly this ampleness descent argument under its
finite-flat conductor hypotheses. We read the proof itself. The
trivialization/ampleness argument needs only finiteness of the conductor;
we do not import any claim that an arbitrary pinching is automatically
flat with integral fibres. Those properties must still be checked.
The paper's relative realization theorem1.1 begins with extensions by
vector groups and quasi-split tori of an abelian scheme, so it already
assumes a schematic group and does not realize a general nonschematic
smooth commutative group space.

Thus a rational-curve normalization P1_S with finite pinching conductor
cannot supply the desired counterexample, even if one writes a quotient
of relative unit groups. Possible remaining curve routes require failure
of such a locally projective simultaneous normalization, or a conductor
whose relative geometry does not fit this finite pinching argument.
Source opened: https://arxiv.org/pdf/1310.0186 , pp4–6 and Theorem1.1p1.
