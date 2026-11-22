# Root full proof audit: the projective-three-space component obstruction

We read the complete candidate
`agents/singularities_duality/logs/pending_Galvin_RP3_components.tex`,
including its subsequent explicit real-definable consequence and corrected
published locator for Proposition 2.22. **PASS.** It remains a draft
outside the included paper during the checkpoint14 source freeze.
The independent complete audit is
`agents/higher_comparison/Galvin_RP3_independent_audit.md`.

## Exact conclusion and scope

For every closed connected oriented real PL three-manifold B with finite
cyclic fundamental group of even order, there is a TOP concordance of B
which fixes both ends and whose free-top ordinary concordance component
contains no PL concordance. The result includes the completely specified
finite PL model of RP3. Over every fixed o-minimal expansion of the real
field, the natural definable concordance component map has the same
image as the PL map, so it is also not onto TOP components.

This is an image obstruction. Neither the whole component group nor
the sufficiency of a zero Casson–Sullivan class is asserted. It does
not invoke any four-dimensional equivalence of smooth and PL isotopies.
It is not a result about a TOP realization over a non-Archimedean field.

## Relative class and original source

We checked the source against the published original as documented in
`notes/root_Galvin_published_boundary_audit.md`. Definition 2.11 and
equation (2.1), printed pages2503–2504, define the same relative
mapping-cylinder obstruction and interval suspension. Its PL form uses
the universal Kirby–Siebenmann class with the specified PL reductions
on the entire boundary of the five-dimensional mapping cylinder.
The compatible product smoothing supplies those reductions through
the natural smooth-to-PL map. The low-dimensional obstruction is the
same class; this is a statement about stable tangent reductions,
not about actual four-dimensional isotopy categories.

The class is invariant under TOP isotopies fixed on the entire boundary.
The parameterized microbundle identifications give a relative homotopy,
so obstruction naturality proves the assertion. The mapping-cylinder
proof in Galvin Proposition2.22, printed pages2507–2508, is consistent
with this argument. A PL map has a PL mapping cylinder extending the
chosen boundary structure and therefore has zero class. These are the
only classification properties used by the exclusion argument.

## Realization with the boundary fixed pointwise

Set X=B times I. A compatible smoothing of B gives the product
smoothing of X. X is compact, connected and oriented. Its finite cyclic
fundamental group is good, and the simple L5 group is zero by the exact
finite-cyclic input stated in Galvin Section4.4, printed page2528.
The relative simple surgery sequence therefore has zero obstruction
for every normal invariant of X times I relative to its full boundary.

Galvin Lemmas4.8–4.9 give the two normal-invariant coordinates and the
coefficient-reduction obstruction map. We independently checked the
relative suspension argument: the possible Sq2 term is the suspension
of Sq2 on degree one and is zero. The source's inequality is reversed
in print; the candidate uses the correct greater-than instability
inequality and explicitly records the correction.

Integral-to-mod-two reduction in relative degree four is onto because
the next Bockstein map lands in the kernel of multiplication by two
on the top relative integral cohomology, which is Z. Thus every desired
relative degree-three class on X is realized by a normal invariant
of the form (0,y), with zero surgery obstruction.

The candidate checks the boundary instead of assuming it. The structure
map labels the entire boundary of the five-dimensional cobordism by
the boundary of X times I. Its side product is chosen from that label.
The relative s-cobordism product identification fixes the lower end and
this side. In the source's commuting diagram the upper and lower
corner labels therefore agree. Consequently the induced map
f=phi_plus p_minus phi_minus_inverse is literally identity on boundary X.
The identification with its mapping cylinder preserves the boundary
reductions, giving the desired class by Galvin Lemma4.12.

This derives the compact relative case from Section4.2 and avoids the
closed/compact wording discrepancy in Definition4.11. We explicitly
viewed the full printed-page2527 diagram before accepting this step.

## Passing from fixed ends to a free top

The exact natural AutPL(B)-to-AutTOP(B) comparison in dimension three
is the already audited A.134.2. It is the ordinary joint-family
comparison, not a block comparison. Its component injectivity and
fundamental-group surjectivity imply that every TOP path from identity
to a PL map is TOP-homotopic relative endpoints to a jointly PL path.
One first selects a PL path between the endpoints, then corrects its
loop class by a PL loop. Finite edge-path representatives and finite
PL concatenations give the required joint PL family.

If H_t were a free-top isotopy from the realized F to a PL concordance G,
let a_t be its top restriction. The actual homeomorphisms
T_t(x,s)=(a_(ts)(x),s) have jointly continuous inverses. Then
Q_t=T_t_inverse H_t fixes both ends throughout, starts at F, and ends
at T_1_inverse G. Replace a_t relative endpoints by a jointly PL b_t.
The corresponding trace isotopy is fixed on the full boundary of X,
and its PL endpoint is T_b(x,s)=(b_s(x),s). Hence F would be isotopic
relative to both ends to the PL map T_b_inverse G. Isotopy invariance
and PL vanishing of the class contradict its chosen nonzero value.

All parameter and boundary conditions have been checked. In particular,
T_t need only be TOP; only T_b is claimed jointly PL. No endpoint map
or arbitrary isotopy is silently called PL.

## Nonzero class, definable image, and exact finite certificate

For closed oriented B with finite cyclic even-order fundamental group,
mod-two Poincare duality identifies H2 cohomology with H1 homology,
which is Z/2. For the specified RP3 model, the quotient of the
barycentrically subdivided four-crosspolytope boundary by the antipodal
action gives a finite PL manifold with its usual two-fold S3 covering.
The covering proves the fundamental group C2; orientability follows
from the orientation-preserving antipodal action on S3.

We read the root checker and its complete output in the preceding
audit segment. It records2634 passing checks in0.08755117800319567 seconds,
including all192 tetrahedra, all face data,80 local star bijections,
all nonmaximal link homology checks, and192 exact Tietze eliminations
to one generator with square relations. The independent author run
also has2634 passing checks. These computations certify the finite
base hypotheses and nonzero obstruction group; the existence of F
and exclusion of its PL component are proved mathematically above.

Finally, A.113 identifies every real-definable concordance component
with a PL representative by a definable isotopy fixing the bottom.
Its underlying isotopy is an ordinary TOP isotopy. Therefore the
natural PL and definable images in TOP components are equal, which
gives the claimed definable non-surjectivity without any extra family
comparison assumption.

The candidate is ready for numbered integration after the scheduled
checkpoint source freeze ends. No original task row is marked closed,
and no hourly progress-review decision is made in this audit.
