# Whole-proof audit: SF-E819 and E819R

**Mathematical result: PASS.** Reviewer `/root/g34_eightfolds`,
GPT-6 Astra Pro, effort inherited/unexposed, HODGE_DIVISION,
2026-11-21, approximately17:22–17:34 UTC.

I read the entire frozen Markdown proof, including the separately
labelled reduced equal-length corollary, the actual rank36 example,
and all scope limitations. The final frozen version has SHA-256
`10d171d811e27e5eeae0381b00d137b2439fa90c6bfde38046e6cf94baaf2baf`.
I reread the final direct published-source substitution in the introduction
and section4, the formal-logarithm coordinates, and the closing scope
qualification. The mathematical text already reviewed is unchanged.
No unrefereed032 theorem is accepted through an indirect citation.

## 1. First-order local algebra and the hull map

The biderivation product is associative modulo epsilon squared. In
formal logarithm coordinates the invariant bivectors have constant
coefficients, and the resulting power-series multiplication and all
matrix operations are continuous. Only first-order quantization is
used.

For a finite-length module over the four-variable regular local ring,
the displayed Koszul/filtration argument gives Ext^j(-,R)=0 for j<4.
The two exact sequences then give Ext^1(M,R^r)=0: Ext^1(K,R^r) is
Ext^2(Q,R^r), and the terms from T vanish. This calculation remains
valid when M has actual point torsion; no torsion-free assumption was
inserted.

A flat module over the dual numbers has the required successive flat
syzygies. Lifting the chosen finite resolution generator by generator
and using the nilpotent Nakayama argument at its last step gives a
finite free resolution over the deformed algebra. Reduction of the
Hom complex is termwise surjective, with kernel the original Hom
complex multiplied by epsilon. Therefore the only obstruction to
lifting the given hull morphism is precisely Ext^1(M,R^r), which is
zero. The proof lifts the specified map, not merely an unrelated map
to a free module.

## 2. The finite perfect cone and supertrace

The cone has two flat dual-number terms. Its reduction has finite-length
cohomology T and Q. The short exact sequence with its epsilon multiple
therefore proves bounded finite-dimensional cohomology for the cone
itself, although its two original terms are infinite-dimensional over C.
Over the Noetherian Artinian dual-number ring this is pseudo-coherent;
the two flat terms supply finite Tor amplitude.

I freshly read the complete Stacks Project Lemma15.76.2, tag0658, and
its proof at <https://stacks.math.columbia.edu/tag/0658>. It gives exactly
the finite perfect replacement used here. Finite projectives over this
local ring are free. Since derived reduction equals the displayed
ordinary reduction, the alternating finite free rank is length(Q)−length(T).

Left multiplication by the coordinates is a chain action on this cone
because the lifted hull map is linear over the deformed algebra. These
are dual-number-linear endomorphisms, which is all that the trace
argument requires. On a bounded projective replacement, the derived
commutator equality is represented up to chain homotopy. Ordinary
matrix trace is cyclic over the commutative dual-number ring, and the
graded cancellation makes null-homotopic degree-zero maps have zero
supertrace. Thus the displayed epsilon times the signed-length equality
is valid. Some bivector coefficient is nonzero, so characteristic zero
forces that signed length to vanish. No infinite-dimensional trace
has been taken.

## 3. Characteristic obstruction and continuity

The bar equation is the first-order module associativity equation with
the stated sign convention. A vanishing Ext² class gives the necessary
correction. The finite free resolution formulation avoids any need to
choose a discontinuous bar cochain on formal power series: the lifted
differential has square epsilon times a degree-two cocycle, and a
null-homotopy of that cocycle corrects its square to zero.

The resulting finite free deformed complex reduces to a resolution
with cohomology only in degree zero. Its square-zero exact sequence
gives no other cohomology and a degree-zero module N fitting into
0→M→N→M→0, with multiplication by epsilon identified with the indicated
composite. Hence ker(epsilon)=im(epsilon), the flatness criterion over
the dual numbers. Its finite presentation and continuity follow from
the finite free construction. This correctly distinguishes a flat
module deformation from a merely arbitrary derived lift.

Restriction to an affine open and formal completion eliminates the
H¹(T) and H²(O) components; the constant bivector component remains
the first-order multiplication class. The nonzero HKR normalization
cannot affect vanishing or the trace contradiction.

## 4. Global cap kernel and source status

The two independent bivectors supported on the two RM planes produce
the two displayed cap-kernel classes. Contraction of the degree-four
term in one plane is cancelled by wedge with the corresponding H²(O)
class, whose further wedge on that same plane vanishes. A divisor
shear preserves the leading holomorphic bivector component. This
calculation is over C and does not require the individual RM eigenplane
classes to be rational.

I reread supplied DEG_L S-20, the opening proof of(S20.1), and the
entire relevant S-21 argument around(S21.5)–(S21.8). Evaluation is
invariant because translations and degree-zero tensor operations act
trivially on HH and evaluation is natural. The specified coherent
action and the identity-sector/forgetting argument retain exactly
their supplied, previously reviewed status. The proof here needs
injective trace on invariant Ext; it does not need CY4 surjectivity of
evaluation or a dimension equality.

The S-20 text cites032 for the composition identity. I flagged that
source-status issue rather than treating the indirect citation as a
new refereed premise. A direct published replacement is available:

R.-O. Buchweitz and H. Flenner, *The global decomposition theorem for
Hochschild (co-)homology of singular spaces via the Atiyah–Chern
character*, Advances in Mathematics, DOI10.1016/j.aim.2007.06.013.
The primary author version actually opened is
<https://arxiv.org/pdf/math/0606730>, displaying v1,28 June2006.

I freshly read Proposition6.2.1 and proof (numbered pp29–30),
Proposition6.3.1 and its complete proof (p30), Corollary6.3.2 (p31),
Theorem6.4.2 and its source-precision remark (p31), and the complete
Proposition6.4.4 proof (pp32–33). These give respectively the
identification with the usual semiregularity map, HH-linearity,
evaluation-followed-by-trace as cap with the Hochschild Chern character,
and the exact compatibility with contraction against the ordinary
Chern character. The theorem expressly supplies this last diagram
without assuming multiplicativity of the HKR map. Thus it is the
precise published premise needed for E819, and no general formality
or full HKR-ring theorem needs to be imported.

## 5. Reduced defects: E819R

For reduced Q and T, the residue quotient can be put in standard form,
and the free summand of its kernel splits from the extension. The
Koszul presentation gives exactly the six matrices B_ij. Relations
among these relations are respected because the maximal ideal kills T.

The equation C B_ij=pi_ij I follows from the lifted hull map, including
all its correction terms. Terms containing a coordinate vanish at the
origin. The epsilon correction to the original module relation maps
into K and therefore vanishes in the prescribed residue quotient.
Consequently this equation has no omitted error term.

The local trace lemma first gives equal reduced lengths. A nonzero
bivector coefficient then makes the square matrix C invertible and
forces all six B_ij to be one fixed invertible matrix times the
coefficients of that bivector. Applying the same reasoning separately
to the second independent RM bivector contradicts those fixed matrices.
The two deformations need not coexist over a two-parameter base.
The argument correctly leaves equal-length nonreduced defects open.

## 6. Actual example and independent certificate

I checked the actual finite étale isogeny and the integral half-divisor
pullback, the finite étale GRR computation, the rank36 direct sum, and
the global extension-space calculation. Since the hull is locally
free and the quotient is a skyscraper sheaf, its positive Ext groups
into that quotient vanish. The stated global Ext¹ identification with
the point Koszul Ext² is therefore exact. Every nonzero class defines
an actual coherent sheaf. Its maximal torsion, double dual and
canonical hull-map defect are exactly the specified point modules;
there is no virtual-sheaf substitution.

I independently wrote and ran `audit_local_quantization.py`. It imports
no author code and expands the characters in the entire256-coordinate
exterior algebra on eight generators, rather than the author's
two-variable quotient. It verifies both RM-plane square identities,
both independent cap kernels, the integral isogeny pullback, and the
entire balanced character. Results: rank36, isogeny degree4, point
lengths34 and36, extension-space dimension7344, top Chern-character
integral16, and self-Euler2304. The full output is retained.

This computation verifies the explicit example and cap calculations;
the universal deformation and categorical arguments are checked by
the whole-proof reading above. No finite action, simplicity or
semiregular object is asserted to have been constructed.

## 7. Limits retained

The nontrivial-modification qualification is necessary and now
explicit: locally free E itself has zero defect and is not excluded
by this theorem. Singular reflexive hulls, positive-dimensional defects,
equal-length nonreduced local modules, and unrelated derived or twisted
objects remain outside the conclusion. No TeX compilation was performed.
