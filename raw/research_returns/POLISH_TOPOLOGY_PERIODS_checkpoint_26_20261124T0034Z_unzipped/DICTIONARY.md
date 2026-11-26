# Mathematical dictionary and limits of the translations

This record connects the selected findings to algebraic geometry and to the
manuscript questions. It does not assert an algebro-geometric analogue merely
because a topological statement resembles descent. Earlier statement IDs are
kept here and in CROSSWALK.tsv, outside the papers. The entries below concern
current draft findings; the full inherited register has not been certified.

## 1. Tubes, overlaps, and descent

**Earlier IDs:** SA10 A1.1–A1.5, A2.1–A2.2. **Proof:** Paper 1, open-cover,
membership-category, and base-change arguments.

The closed strata determine open neighborhoods only after a simultaneous
choice of neighborhoods and deletion of the order-forbidden closed pieces.
Their genuine pair and triple intersections give ordinary sheaf descent.
The algebraic-geometric language is a covering presentation of a topos with
descent data and cocycle equations. The proof uses actual open immersions,
so it does not by itself prove an analogous assertion for formal completions,
henselizations, or étale neighborhoods of schemes. The manuscript connection
is explicit in cotes 150–151; the order-defined deleted set matters.

For an arbitrary open diagram, the fundamental groupoid of the objects
containing a point measures the ambiguity of gluing a stalk. This is the
ordinary-topos part of descent. Higher sheaves require higher coherences,
which the groupoid criterion does not supply. Pro-neighborhoods retain
information lost by an ordinary inverse limit; their base change is a
cofinality assertion, not an automatic formal property of inverse images.

## 2. Collars, concordance, and the Additif

**Earlier IDs:** SA20 A.101–A.112, A.147–A.160. **Proof:** Paper 2; the complete relative fragmentation and finite-parameter assembly proofs are recorded in notes/paper02_root_chain_audit.md and its separate reconstruction records.

Strictly rigidified collar choices are contractible, whereas derived choices
of tubular or conical data can detect the concordance space of a boundary.
The six-dimensional torus supplies the nontrivial concordance information in
the Additif counterexamples. In the language of moduli problems, forgetting
rigidification changes the homotopy fibre; an ordinary uniqueness statement
does not establish contractibility of that fibre. This observation concerns
topological and PL moduli, not an algebraic stack over Spec Z.

The all-real-closed-field PL/definable comparison is proved for the specified finite jointly definable and jointly PL concordance models. Relative marked fragmentation, compatible parameter prisms, compact resolutions and finite-join assembly complete the argument. Separate statement-only reconstructions and full proof comparisons are recorded for the main assembly steps. This concerns definable homotopy types over ordered fields; it does not identify arbitrary Hausdorff families or supply a comparison with ordinary TOP concordance spaces in every low dimension.

## 3. Polynomial rings and the tensor criterion

**Earlier IDs:** SA20 B.054, B.064, B.082. **Proof:** Paper 2, algebraic
part and its explicit dependency discussion.

For integer-valued polynomial rings, the multiplication map from a tensor
product to the ring in two variables has both a kernel obstruction and an
image obstruction. The mapping-cone and Tor formulation separates them.
This is directly about rings and affine schemes: a proposed biring or
composition structure requires the relevant polynomial operations to land
in the appropriate tensor product. Weak polynomial compositeness is a
different assertion from a tensor isomorphism. The arbitrary-Noetherian coefficient classification is proved and checked at the stated scopes, including all original Part B rows. Its proof uses local algebra, completion and explicit tensor detectors; finite computations serve only as examples. The separately identified finite-residue, non-Noetherian ambient conductor extension remains open.

## 4. Joint periods and conjugation

**Earlier IDs:** SA07 A.2.2–A.2.6, A.3.3. **Proof:** Paper 3, the joint
comparison-torsor orbit calculation and the separate dimension memo.

Use the motive N=M direct-sum c* M. Its joint motivic group J is a subgroup
of the product of the individual groups, not an assumed independent product.
The kernel N2 of the first projection has a flag orbit of dimension
v=dim N2−dim(N2 intersect B-minus). The dimension table follows by computing
the stabilizers of the relevant comparison and flag data. Normality makes
the orbit dimension uniform. The actual period point therefore satisfies
unconditional upper bounds; equality requires period genericity for N.

This is an assertion about motives, tensor correspondences, Hodge flags and
period torsors. A motivated isomorphism M≅c*M forces v=0, but an arbitrary
isomorphism between realization vector spaces does not. Cote 18's strong
transcendence prediction fails for the real non-CM elliptic example because
the predicted independence is already contradicted by these unconditional
algebraic relations. No ordinary period conjecture is proved here.

## 5. Integral and p-adic realizations

**Earlier IDs:** SA07 A.4.21, A.4.31, C.1.5, D.5.2, E.1.2–E.2.1.
**Proof:** Paper 3, ordinary splitting, restricted Lie, computability,
Betti-place and ideal-class arguments.

Ordinary p-divisible groups can acquire endomorphisms after compatible
base extension that do not come from the elliptic curve. Integral
comparison also retains ideal-class and inverse-limit obstructions that
disappear rationally. The Q(sqrt(-5)) example distinguishes a nonprincipal
invertible ideal from a free rank-one module; local and rational comparisons
therefore cannot be silently promoted to one global integral comparison.
The restricted p-power formula is an exact characteristic-p Lie calculation,
with finite certificates at 5, 7 and 11 and a separate general proof.

The non-computable Hodge example is deliberately non-geometric. Its
computability obstruction uses countable algebraic descriptions and
computable period integrals; it is not a classification of all Hodge
structures arising from motives.

## 6. Conformal caps, tensor data, and plumbing

**Earlier IDs:** SA22/SA22_run2 single-cap, plumbing, toric and cusp claims.
**Proof:** Paper 4, projective developing maps and local series.

A pointed embedded cap determines the projective local coordinate but
initially leaves a length scalar. Comparing logarithmic derivatives on the
universal cover and taking a holonomy translate that has a simple zero or
pole forces the scalar ratio to be ±1. This proves length reconstruction
under the stated negative-Euler-characteristic and positive-cap hypotheses,
including other cusp ends. A tangent tensor at a node remembers only the
first-order plumbing datum. Its equality does not identify the entire cap
germ. The toric example exploits exactly that distinction.

The algebro-geometric counterpart used here is the tensor product of the two
tangent lines at a node, the first-order smoothing parameter. The proof
does not identify every analytic welding with an algebraic family over an
arbitrary base, and higher cap jets are additional analytic data. Cotes
66–68 supply the particular surgery and forgetting questions.

## 7. Involutions and integral eigenspaces

**Earlier IDs:** integral involution example from cote 67/091.
**Proof:** Paper 4, matrix factorization and the characteristic-two fibre.

For R=Z[x,y,z]/(x²+yz−1), the matrix with rows (x,y),(z,−x) is an
involution. Its eigenmodule has generic rank one but a two-dimensional
fibre at (2,x−1,y,z), so it is not an invertible module. Over Spec Z the
prime 2 is a structural obstruction: the projectors (1±sigma)/2 are not
available. Dedekind hypotheses or invertibility of 2 with connected base
restore the appropriate line-module statement, with the scalar-involution
case separated. This is a vector-bundle and lattice-gluing issue, not a
failure of the generic eigenspace calculation.

## 8. Relative positions and the genus formula

**Earlier IDs:** SA11 E2, E3, T1–T3, C.04–C.05. **Proof:** Paper 5; its
independent-counting memo records the remaining local independent check.

The extension poset supplies two Euler-count identities. The separately
constructed reflection-gluing surface has Euler characteristic
1−n−4 sum(k c_(2k+1)), hence the stated nonorientable genus. The two
six-line arrangements give distinct values. This is oriented-matroid and
surface topology, not a claim that the corresponding surface is an
algebraic moduli space. No schemes-over-Z, weights or lambda-ring
interpretation is inferred from the attached sources. The connection to
Grothendieck is the explicit relative-position construction of cote 154.

## 9. Divided powers, laws, and mixed coherence

**Earlier IDs:** SA09 A1.5–A1.8. **Proof:** Paper 6, finite coherence and
the three explicit counterexamples.

Homogeneous substitution in a tensor category does not force its mixed
degree or constant terms to compose correctly. The repair uses finite
truncated divided-power sums, a compatible coproduct, counits, and
coassociativity, together with the exact mixed-component normalization.
Over finite fields a scalar-degree condition is weaker than a polynomial
law natural under every base change: entrywise cubing over F2 gives an
explicit obstruction.

The algebro-geometric language is representability of polynomial laws by
divided powers, with base change included in the functor of points. It
must be distinguished from the fixed-degree divided-power category used
for strict polynomial functors. Neither construction by itself supplies
a lambda-ring or K-theory operation; those require their own identities.

## 10. Exactness and cochain reconstruction

**Earlier IDs:** SA09 A2.1–A2.5, A3.1–A3.2. **Proof:** Paper 6, disk
copresentations, pullback induction and evaluation objects.

The walking disks encode a complex. Its extension to all finite-free
bounded tests exists precisely when the specified matrix kernels exist.
For exact targets, the resolution condition must use a Quillen exact
structure, including pullbacks of admissible epimorphisms. The finite
abelian-group example proves that weaker closure axioms do not suffice.

The full natural divided-power action recovers cross terms and the unit,
then the entire cosimplicial ring of integral functions on simplices.
Horel's binomial-ring homotopy model explains the relation to derived
integral homotopy types. Binomial rings are special torsion-free lambda
rings; this is a precise connection to lambda language, not an assertion
that a cohomology ring alone retains the same information. Cote 137
sheet 38 is the manuscript source of the extra-structure question.

## 11. Cellwise holomorphic groups

**Earlier ID:** SA09 B3.1. **Proof:** Paper 6, dart propagation and analytic
rigidity.

Suppressing the white vertices of a clean dessin changes the cellwise
automorphism problem. The graph-theoretic kernel has at most one
nonidentity element, and positive genus makes the dart-fixing holomorphic
kernel trivial. The sphere permits the affine and dilation families.
These are groups of a compact complex curve with specified ordinary
cells; they are not all automorphisms of its Belyi morphism. The Belyi
examples provide the algebraic curves, while the larger sphere groups
depend on forgetting the marked white points.

## 12. Interval supports, events, and oriented maquettes

**Earlier IDs:** SA21 A.3–A.4, interval transfer, B.3–B.4, C.1–C.2.
**Proof:** Paper 7, split posets, polar cuts, event reconstruction and
the regular-cell realization theorem.

For finite posets, adjoining point intervals through a split-poset
construction transports the orthomodularity question to conditional
lattices. For arbitrary posets, the Boolean classification is governed
by the chain of nonisolated points. The general neighborhood criterion
is credited to Jenča's 2026 theorem. Contrées satisfying the specified
finite compatibility axioms reconstruct a precise binary event class;
an arbitrary event structure cannot be substituted. The o-minimal
atelier uses finite definable cell decompositions and common refinements.

An oriented regular-cell poset needs spherical lower intervals. Signed
diamond relations and connectedness alone permit a torus boundary and
therefore fail. These are incidence and support constructions; the
attached sources do not establish an equivalence with schemes,
correspondences or weight filtrations. Their role in the programme is
to identify exactly which combinatorial conditions support a geometric
realization.

## Explicit real compactification of straight positions

Paper5, Proposition8.7, constructs the real blowup of the dual projective plane at six old-line points and an explicit229-face dual cellulation. Algebraic-geometrically the six exceptional real projective lines are Möbius cores; topologically cubical corner subdivision and band replacement give(234,468,229) cells and Euler characteristic−5. This realizes the numerical source C.06 claim under a precise defined compactification, without an unproved identification with its unspecified gluing. The complete proof is in the paper and its scope in notes/paper05_scope_reconciliation_review.md.

## Integer-valued polynomial freeness on one-dimensional local schemes

For a one-dimensional analytically irreducible Noetherian local domain D, the quasi-coherent module associated to Int(D) on Spec(D) is a direct sum of countably many copies of the structure sheaf. This is a module statement; it does not assert that Int(D) is a polynomial D-algebra. The module-to-sheaf correspondence carries the proved free decomposition to that direct sum.

The normalization Spec(V) has one closed point, V is a finite DVR normalization, and the conductor gives the fiber-product ring D=V×_{V/J}(D/J). The proof glues the free polynomial-value module over V to the free locally constant residue-function module over D/J. Milnor patching gives a projective D-module and Kaplansky gives a free one. The exact normalization hypotheses and their equivalence with domain completion are proved in Paper 2, prop:analytic-one-branch.

The isomorphisms Int(D)^{⊗n}≅Int(D^n) give a unique compatible biring and plethory, hence ring operations and composition on the represented functor. Their proof is the finite dual-basis argument in result-25. This answers the polynomial-operation formulation in cote153, sheet4, where the actual archival connection is recorded; it is not attributed to the collar questions of cote119.

The cusp’s leading-coefficient ideal in degree two is the nonprincipal D-module V. Thus an arbitrary free basis need not be compatible with degree, and a regular polynomial basis is not asserted. The rank is infinite, so this argument alone supplies no class of a finite vector bundle in K_0(D). It also supplies no canonical λ-structure, motivic realization, correspondence or weight filtration. Those require additional structures and theorems. The new supplemental statement IDs and precise source-row relationships are in CONTINUATION_REGISTER.tsv and CONTINUATION_PAPER2_CROSSWALK.tsv.


## Continuation: arbitrary-base binary injectivity and nonflat polynomial laws

The binary tensor criterion for any Noetherian inclusion R⊂S is local at finite-residue closed points. Its effective coefficient algebra is the saturation C_m=∪_j(R_m:_(S_m)m^j). The complete classification says that binary injectivity holds precisely when each such C_m is R_m or the canonical fraction field of a one-dimensional analytically irreducible local domain. In scheme language the nontrivial allowed coefficient map is the canonical generic-point inclusion of a single completed branch. Ferrand's complete-local epimorphism theorem separates the closed fibre; completion, faithful flat descent and explicit orthogonal or nilpotent tensor detectors exclude all other local possibilities. No reduction or torsion-free assumption on R or S is used. The nilpotent detector has arbitrarily high parameter-torsion order, so bounded torsion is not an unstated substitute for this obstruction. Proof: Paper2 Section19; three independently frozen reconstruction stages and full comparison are recorded in notes/continuation_arbitrary_base_root_final_audit.md.

The non-Noetherian forest example has all arity maps Ω(R,S)^{⊗n}→Ω_n(R,S) invertible while Ω(R,S) is not R-flat. Thus exact reconstruction of these polynomial laws alone does not imply module flatness. Its proper injective ring epimorphism is a scheme monomorphism without the flatness property; the explicit balancing and fresh-branch coefficient functionals prove the distinction. Source construction and independent existential reconstruction use different proper subrings, a distinction kept in the audit. This supplies no automatic λ-ring or K-theory identification; such an identification would require additional structure and proof.

The Hausdorff hairpin example separates convergence of closed cone images and outer faces from the existence of a continuous family of face parametrizations. For descent of geometric gluing data, the total-space family condition is real input: converging underlying closed sets do not provide it. The proof is an explicit polygonal example and the two complementary boundary arcs. It does not decide the stronger torus filling question for Hausdorff-only families. Proof: Paper2 Example2.3.


## Countable concordance presentations and algebraic K-theory

**Earlier IDs:** SA20 A.119–A.120. **Proof:** Paper 2, component_presentations.tex, with exact classical inputs in the references. Stable PL concordance components, and unstable smooth or smoothable PL components in dimensions at least nine, are presented by a countable cycle quotient E(K). The quotient retains the full composition group and incorporates the monomial-unit image in algebraic K-theory. Acyclic group completion and the stable parametrized h-cobordism theorem carry this comparison; the independent reconstruction uses plus constructions, abelian-cover homology and a smooth thickening.

For the Grothendieck programme this supplies an explicit obstruction group for moduli of collar choices, rather than uniqueness of unparameterized underlying objects. The relevant K-theory is the K-theory of the specified spherical loop-ring model. It is not automatically algebraic K-theory of a scheme over Z, and no lambda-ring, motivic correspondence or weight filtration follows without an additional comparison theorem. The connection to the Additif is through the concordance-space obstruction already established in Paper 2, not a new archival quotation.

## Nilpotent conductors and the arithmetic of residue fields

**Earlier row:** SA20 B.059. **Refined IDs:** P02-B059-REGULAR-CONDUCTOR and P02-B059-NOETHERIAN-FINITE-RESIDUE. **New examples:** CONT20261123::P02-CONDUCTOR-INFINITE-RESIDUE and CONT20261123::P02-CONDUCTOR-NONNOETHERIAN-DETECTOR. **Proof:** Paper 2, conductor_scope.tex and the preceding regular-conductor and finite-residue corollaries.

A conductor supported only on a square-zero thickening need not contain any regular function cutting out a closed fibre. The complete local example over an infinite field has such a nonzero conductor but only ordinary polynomial functions: invertible Vandermonde matrices recover all coefficients. Thus the tensor algebra of polynomial operations is unaffected in that example despite the nilpotent thickening. This identifies the finite-residue hypothesis in the proved Noetherian obstruction as genuine.

Over F_q[[t]], the positive square-zero family has a different outcome. A residue-linear functional detects the nonzero tensor H tensor H, while the corresponding product polynomial vanishes. Taking an infinite product module gives a complete non-Noetherian ambient ring and preserves that detector. These are precise affine-ring and tensor-module assertions. They neither establish flatness of the coefficient algebra nor construct a lambda-operation, motivic realization or weight decomposition. The general finite-residue ambient extension is posed exactly in the last section of Paper 2; loss of a regular conductor and failure of tensor injectivity under arbitrary base extension are the remaining obstructions.
# Continuation: concordance components, 23 November 2026

The translations in this section concern the choice spaces in the
Additif of cote119, archive sheets147–149, at the manuscript scope
quoted in Paper2. They do not assign these results to a different
cote or identify a concordance invariant with a motivic invariant.

## A.123 and the closed-surface consequence

The group of PL automorphisms of a cylinder fixing its bottom and
side boundary, with the upper boundary free, has one isotopy
component for PL balls in every dimension, compact manifolds of
dimensions zero and one, all closed PL surfaces, and compact
orientable surfaces with boundary. The original A.123 surface
clauses exclude the sphere and projective plane; the full
closed-surface conclusion also uses the separately checked
A.125/A.127/A.128 cases. Finite disjoint unions give products because
the fixed bottom forbids permutations of components.

In the language of moduli, this computes the set of connected
components of the specified automorphism object, with its group
law. It eliminates this particular component obstruction to
connectedness of collar-choice spaces for those bases. It does
not supply a contraction of the derived choice space: positive
homotopy groups encode additional families. This distinction is
the same distinction between an isomorphism of connected-component
sets and an equivalence of moduli objects.

The proof is explicit: conical PL Alexander isotopies handle balls;
the free upper face removes annular winding; Waldhausen straightens
orientable surface products; Laudenbach's properly-homotopic-implies-
isotopic theorem and the ordinary category comparisons handle the
closed nonorientable products. The inverse of the moving bottom
restriction corrects an ordinary isotopy to one fixing the bottom.
The already checked relative PL/definable comparison then transports
the result to the chosen finite models over arbitrary real closed
fields. This transport concerns definable families, not ordinary
connectedness in a non-Archimedean topology.

## A.125–A.129: standard spheres and recognized manifolds

Standard PL spheres of every dimension at least two have trivial
bottom-fixed, top-free concordance component group. The separate
closed simply connected three- and five-dimensional consequences
retain their exact classical recognition and pseudoisotopy inputs;
the five-dimensional assertion has no additional π₂=0 hypothesis.
These are statements about automorphism components of finite
geometric models. They must not be replaced by assertions about
all homotopy groups, all exotic PL structures, or an arbitrary
simply connected four-manifold.

The connection with Grothendieck's programme is the same precise
concordance obstruction underlying the Additif comparison. No
statement about schemes over ℤ, weights, or a motive of the
manifold follows from this component calculation alone.

## A.130: an infinite-rank three-dimensional obstruction

For every closed connected orientable PL three-manifold with
infinite fundamental group, the concordance component group
contains a subgroup isomorphic to ⊕ₙ≥₁ℤ. Over ℝ this subgroup is
still detected when every boundary condition is forgotten in
the homeomorphism group of the cylinder. The result follows from
Lin–Xie–Zhang's2026v1 detection theorems and the relative PL–PD
triangulation comparison; the manuscript proves the composition
law and the transfer to stipulated definable models in full.

Thus the automorphism object contains infinitely many independent
component obstructions already in base dimension three. The
subgroup is an abstract free abelian subgroup, not a recursive
list of geometric generators or a classification of the whole
group. The calculation is unstable. An identification of these
particular elements with classes in stable A-theory, algebraic
K-theory of an ordinary group ring, or a category of motives has
not been derived. The countable cycle presentation below has its
own dimension and stabilization hypotheses.

## A.121–A.122: the full PL cycle presentation from dimension six

For every compact PL manifold M of dimension at least six,
with finite simplicial homotopy model K, the entire concordance
component group is E(K), where E(K) is the finite-support
two-cycle quotient of the abelian-cover monomial-to-derived-matrix
map defined in Paper2. Its group law is composition. Positive
smooth suspension is an isomorphism on components. A general PL
manifold need not be smoothable. A smoothable three-handle core maps
three-connectedly to M and extension by identity is surjective on
concordance components. Its natural stable comparison is an
isomorphism, forcing both the extension and stabilization to be
isomorphisms. The original component-reduction statement and the
precise surjectivity range are separately sourced; the full original
higher-connectivity proof is not claimed to have been inspected.

This is an A-theory presentation over the spherical group ring
Σ∞₊G(K). The matrix objects are derived automorphisms of finite
free modules over that ring spectrum; replacing them by discrete
matrices over ℤ[π₁K] loses the higher homotopy information. The
group-completion and abelian-cover calculation identifies
E(K) with π₂Whᴰⁱᶠᶠ(K). The corrected geometric exact sequence
first identifies this stable group with the unstable group for
the smoothable core. Both the Postnikov and framing terms
of the second obstruction are required. This is why a naive
direct sum of lower Whitehead groups is not the presentation.

The three-skeleton inclusion induces E(K³)≅E(K). Its loop map is
two-connected; the bars of the derived matrix and monomial objects,
their telescopes, and the specified abelian covers consequently give
isomorphisms on both second homology groups in the presentation. This
argument verifies the actual induced map and does not claim that
abstract π₁ and π₂ alone classify the result. In algebraic-geometric language the
construction illustrates a derived K-theoretic obstruction
object; it establishes no new λ-ring structure, motivic
correspondence, or weight filtration. Its mathematically proved
connection to the programme is the concordance component group
of the Additif's geometric choice space.

## A.132: a higher discrepancy invisible to components

For the standard three-sphere, the jointly PL concordance object has
vanishing homotopy groups in degrees zero, one and two. The actual
compact-open TOP concordance object has zero groups in degrees zero
and one but has second homotopy group ℤ/2. Its full based weak type
is the loop space of hofib(BO(4)→BTOP(4)), with TOP(4) the global
origin-fixing homeomorphism group of ℝ⁴. A parameterized germ model
is introduced only after an exact relative lifting argument relates
it to those global maps.

This distinguishes agreement of geometric components from agreement
of the whole derived automorphism object. The nonzero degree-two
class is a higher family obstruction. It is a topological smoothing
calculation using the stable ℤ/2 class, not a period, a motivic
cohomology class, or an arithmetic realization theorem. In particular,
the all-field PL/definable comparison cannot by itself imply an
unrestricted real PL/TOP comparison.

## A.131: effective presentations of the full family object

An ordered finite simplicial model of a closed PL manifold determines
countable simplicial PL and semialgebraic concordance groups over the
real algebraic field. Each has finite codes, decidable validity and
equality, and computable group and simplicial operations. Each
separately models its geometric group over every real closed field.
The general construction enumerates complete presentations of the
homotopy groups; in positive degrees these can be written as countable
integer relation matrices. This is a statement of effective
presentation, with no terminating word problem or manifold-recognition
algorithm asserted.

The relevant object is the whole simplicial family of automorphisms,
with the bottom fixed and top free. A Moore cycle is a family trivial
on every attaching face; a Moore boundary is a higher family witnessing
its triviality. The presentation takes every cycle as a generator,
includes the complete multiplication table, and imposes every boundary
relation. In language familiar from derived moduli, the procedure
presents all homotopy groups of the automorphism object, rather than
only classifying its isolated geometric points. This is an analogy
of constructions, not an assertion that this concordance object is
an algebraic stack or a motivic realization.

The coefficient comparison preserves the full parameter projection.
Its PL proof relocates finite labelled triangulations and uses a
cellwise coning isotopy preserving those labels and time. Its
semialgebraic proof combines graph triviality with a closed-bounded
fibre argument for joint evaluation. The field-extension statement
does not identify the computable PL-to-SA map as a new weak
equivalence by itself. The real TOP interpretation in component
dimensions at least five uses the separately credited classical
comparison. The definable interpretation asserted here is degree
zero. Other higher comparisons have their own proofs and gates.

Classical inputs are Basu–Pollack–Roy's effective real algebraic
geometry and May's Moore description; the precise source editions
and locators are in the manuscript and A131 source receipts. No
arithmetic operation in these graph codes is an operation on
Grothendieck motives, and no new weight, lambda, or correspondence
structure is claimed.



## Elementary extensions and marked automorphism families (A.133)

For any elementary extension of o-minimal real closed structures, the joint definable automorphism simplicial group of a closed bounded definable set, with finitely many setwise or pointwise marks, has unchanged weak homotopy type. Marks need not be closed. The proof uses a finite coefficient-cell partition on which evaluation and inverse evaluation are jointly continuous, then a cell path for surjectivity and an existential Moore witness for injectivity. This is invariance under extension of a real closed structure; it is not an algebro-geometric descent assertion for schemes or a motivic comparison theorem. It supplies a precise parameter-invariance statement for the concordance spaces used in the Additif analysis. The countable-language consequence gives cardinality, not computability. Full proof: papers/02_additif/elementary_extensions.tex; exact checked scope and dependency chain: notes/continuation_root_A133_acceptance.md.


## Real low-dimensional PL and TOP concordance models (A.134)

For closed real PL bases in component dimensions at most two, the ordinary bottom-fixed/top-free PL concordance group has the weak homotopy type of the actual compact-open TOP group. In dimensions zero and one this type is weakly contractible. Full surface automorphism groups, including all nonorientable and disconnected components, agree as well. The theorem gives a precise low-dimensional topological interpretation of the concordance objects in the Additif analysis; it does not assert a higher-dimensional smoothing or motivic comparison. The already effective PL codes consequently compute countable weak TOP models and enumerate complete homotopy-group presentations at this scope. Proof: papers/02_additif/low_dim_comparison.tex; full independent/target provenance: notes/continuation_root_A134_acceptance.md.


## Four-dimensional concordance comparison and its component obstruction (A.135–A.137)

For a closed compact real PL four-manifold B, the relative PL-to-TOP comparison with both ends fixed is the unbased mapping space Map(B,K(Z/2,1)). The free-top comparison fibre is controlled by the specified product-with-a-line stabilization map beta_B into Map(B,K(Z/2,2)). On components, topological concordances first must have a top map ordinarily TOP-isotopic to a PL map. Within that subgroup I_B, the obstruction is a well-defined homomorphism to H2(B;Z/2)/im(pi0 beta_B), with kernel exactly the PL image. The resulting quotient injects into that finite mod-two group. This is the precise relative-structure obstruction for the concordance objects used in the Additif programme, without a motivic or algebraic-geometric interpretation being asserted. The analogy with lifting and descent refers only to these defined homotopy pullbacks. Proof: papers/02_additif/four_dimensional_comparison.tex; exact independent and source scopes: notes/continuation_root_A135_A137_acceptance.md.


## Stable quotients in dimension five

The complete stable concordance group E(K) is a quotient of the five-dimensional component group, for smooth, PL and stipulated definable models. This is a group-level realization theorem, not a computation of its kernel. It applies to the concordance choice objects in the Additif programme; no additional motivic or algebraic-geometric identification is asserted. The original A124 question with pi2=0 now reduces to injectivity. Complete proof: papers/02_additif/five_stable_surjectivity.tex; independent and targeted records: notes/continuation_root_five_surjectivity_acceptance.md.


## Ordinary sphere concordances and unstable smoothing (A.139)

For every standard real sphere S^n, n≥2, the ordinary bottom-fixed and top-free TOP concordance space is the homotopy fibre of product with a line on the finite-rank smoothing spaces Y_n→Y_(n+1). Thus the concordance object appearing in the Additif programme measures this specific failure of stabilization. On the standard four-sphere the first four homotopy invariants, degrees0–3, vanish in both TOP and joint-PL categories. No degree4 assertion, general four-manifold classification, or additional connection with schemes, motives, or weights is claimed. Proof: papers/02_additif/topological_sphere_stabilization.tex. Complete separate reconstruction and comparison: notes/continuation_root_A139_acceptance.md.


## Finite definable homeomorphism formats and infinitesimal approximation (A.138)

For a closed bounded definable set over an arbitrary o-minimal real closed field, every finite formula family of marked homeomorphisms is definably affine in the uniform map-and-inverse metric and has arbitrarily small strong definable contraction neighborhoods. This describes finite parameter charts used by the concordance programme; it does not assert a uniform contraction over all formulas. The exact quadratic bound1/(8m²) shows why ordinary finite PL approximation cannot meet an infinitesimal tolerance, while a semialgebraic isotopy still exists. This is an application of Walsberg and definable triangulation, with the distinct mathematical notions separated. No additional arithmetic or motivic identification is asserted. Full proof: papers/02_additif/finite_format_metric.tex; complete checking: notes/continuation_root_A138_acceptance.md.


## Realized four-dimensional concordance obstructions (A.140)

The component obstruction of the Additif comparison has a precisely stated realization range controlled by the quadratic surgery assembly summand and the localized coefficient Bockstein. Under the two stated hypotheses, the quotient of endpoint-admissible TOP components by the PL image is H²(B;F₂)/J_B. For simply connected closed real PL four-manifolds the ordinary TOP concordance space is connected, but ordinary automorphism loops realize every degree-two mod-two class, and jointly PL loops realize zero. The finite S²×S² model gives two independent obstruction coordinates. This describes a topological comparison obstruction; no additional motivic or arithmetic interpretation is asserted. Full proof: papers/02_additif/four_dimensional_realization.tex.


## Increasing clocks and based sphere parameters (A.150, A.152)

A scalar parameter can be changed by an increasing definable Lipschitz homeomorphism fixing any prescribed finite collection of times over every o-minimal real closed field. The uniform spatial Lipschitz coefficient is unchanged. For a real based sphere, a based parameter map homotopic to identity makes a bounded compact-set family Hausdorff-Lipschitz. Relative cube maps fix the entire boundary and give graph-regularization homotopies of homeomorphism families preserving all spatial conditions. These are parameter-control results for the concordance comparison, not arithmetic or motivic assertions. Full proof: papers/02_additif/scalar_sphere_regularization.tex. The optional all-field sphere strengthening is separately held at its new clean gate.


## Local support for four-dimensional trace obstructions (A.141)

A simply connected codimension-zero part of a real PL four-manifold produces ordinary automorphism loops with prescribed local support. Their relative PL difference classes map to the ambient group by extension by zero, equivalently by inclusion on dual H2. If that inclusion is onto, the trace subgroup is all H² and the image of the PL concordance component map is exactly the separately defined endpoint subgroup I_B. This includes C#D with C simply connected and H2(D;F2)=0. The statement refines the topological comparison in the Additif programme; no extra scheme-theoretic, K-theoretic or motivic identification is implied. Complete proof: papers/02_additif/supported_four_dimensional_traces.tex.


## Based parameters and effective concordance models over real closed fields (A.152, A.161)

Finite cellwise reparameterization regularizes a bounded definable compact-set family on a based cubical sphere over every real closed field, preserving the basepoint. For homeomorphism cubes the full maps and inverses remain continuous and common spatial markings persist. Separately, the effective real-algebraic PL model, followed by full-family comparison and triangulation conjugation, gives complete recursively enumerable presentations of definable concordance homotopy groups from the finite complex. These are parameter and computability statements within the Additif comparison programme. No algebraic-geometric representability, motivic realization, finite presentation, or decision algorithm for the presented groups follows. Full proofs: scalar_sphere_regularization.tex and effective_definable_models.tex in Paper2.


## A three-dimensional base obstructing ordinary concordance comparison (A.142)

For a closed oriented PL three-manifold with finite even cyclic fundamental group, including RP3, the PL and real-definable concordance components fail to cover the ordinary TOP components. A nonzero relative Casson–Sullivan class gives a homeomorphism fixing both ends which has no PL or definable representative even in its absolute isotopy component. This is a precise topological limitation in the Additif comparison programme; it asserts no additional scheme-theoretic or motivic correspondence. Complete proof and classical credit: papers/02_additif/cyclic_three_obstruction.tex.


## A natural three-dimensional concordance obstruction (A.143)

The relative PL tangent difference descends to a natural additive invariant c_B of ordinary concordance components for every real PL three-manifold. Its target is H²(B;F2); both PL and definable images lie in its kernel. The finite even-cyclic case gives a nonzero quotient, while the full kernel and comparison images remain distinct questions. This refines the topological obstruction in the Additif programme without asserting a new algebraic-geometric realization. Proof: papers/02_additif/natural_three_obstruction.tex.


## Finite-group three-manifold realization and projective germs (A.144, A.162)

The natural relative PL obstruction on ordinary concordance components is onto for every oriented finite-fundamental-group three-manifold. Periodicity of the universal-cover chain complex supplies the Sylow arithmetic needed for simple surgery; a fully marked relative product realizes the exact cohomology class. This strengthens the local automorphism obstruction relevant to the Additif programme without asserting an algebraic-geometric realization. Proof: papers/02_additif/finite_three_realization.tex.

For real projective three-space, the full ordinary concordance component group is an abelian kernel of forgetting antipodal symmetry on joint local-homeomorphism germs. Exact finite-parameter extension, rather than a pointwise germ construction, yields the comparison. Its PL subgroup and remaining quotient are not computed. This is a concrete local-versus-global automorphism comparison; no unproved translation to schemes, motives, weights or lambda-rings is claimed. Proof: papers/02_additif/projective_joint_germs.tex.


## Weak filtrations require additional compatibility (A.204; P02-WEAK-FILTRATION-R3)

Regular equidimensional layers alone do not ensure a least or even a common regular coarsening. The explicit surface-and-arc example in three-space and the pure two-sheet example in four-space force the whole nonmanifold to be one block. The distinction matters when transporting Grothendieck's partition programme: frontier and closed-union saturation are mathematical hypotheses, not consequences of smooth strata. No unproved assertion about scheme-theoretic or motivic strata is inferred. Proof: papers/02_additif/weak_filtration_counterexamples.tex.


## Locally supported three-manifold concordance obstructions (A.145)

Finite-fundamental-group punctured summands of any closed real PL three-manifold contribute the duals of their included first-homology classes to the ordinary concordance obstruction. Compact relative realization and explicit support compression identify the value with extension by zero. For a connected sum, this gives a surjection onto the sum of the finite-group pieces first homology, with PL and real definable images in its kernel. This local-to-global obstruction is relevant to the Additif automorphism comparison; no realization by schemes, motives, weights or lambda-rings is asserted. Full proof: papers/02_additif/supported_three_realization.tex.


## Aspherical four-manifold relative comparison (A.163)

Quadratic surgery assembly in degrees6–8 controls the discrepancy between jointly PL and ordinary TOP automorphisms of a fully boundary-fixed four-manifold cylinder. The kernel and fundamental-group extension are cohomology in degrees1and0; realizing central group elements by PL loops supplies the missing component surjectivity. The precise finite-dimensional CAT(0) and hyperbolic examples follow from assembly, while the ordinary-loop contribution vanishes under its stated central condition. This identifies a relative automorphism obstruction in the Additif programme; it does not compute the free-top fibre or assert a motivic, weight, scheme or lambda-ring realization. Full proof: papers/02_additif/aspherical_relative_comparison.tex.


## The vanishing obstruction on the three-torus (A.146)

The natural relative PL obstruction on ordinary concordances of the standard three-torus vanishes. Relative quadratic assembly and, independently, large odd covers with local deformation prove this. The conclusion computes one obstruction group homomorphism in the Additif programme; it does not identify the complete concordance component group or its PL image. The covering argument records all endpoint markings before applying formal obstruction pullback. No scheme, motive, weight or lambda-ring realization is asserted. Full proof: papers/02_additif/torus_three_obstruction.tex.


## Mapping cylinders around a closed core (A.201)

Small scalar sublevels over any fixed o-minimal real closed field are mapping cylinders with specified outer faces. The whole core, exterior collar and quotient cone are controlled, and attaching maps for a fixed tube have one homotopy class. This is a compact definable form of the classical semialgebraic neighbourhood construction, explaining the admissible descriptions at cote119/151. It does not assert contractibility of their choice space or an algebraic/motivic reconstruction. Full proof: papers/02_additif/mapping_cylinder_neighborhoods.tex.


## Embedded smooth partition and its naturality (A.303, A.304, A.206)

Real semialgebraic marked spaces admit a canonical coarsest cellular partition whose every closed saturated union has saturated embedded nonsmooth locus. Connected and pure local-dimensional variants are proved separately. Unlike intrinsic PL regularity, this construction records the ambient smooth embedding; the compact cusp and interval are homeomorphic but have different finite singular strata. In the programme of stratified spaces this identifies exactly which geometric data survive a morphism. It asserts no scheme-theoretic regularity, motivic invariant or K-theoretic comparison. Full proofs: papers/02_additif/embedded_smooth_partitions.tex and embedded_smooth_naturality.tex.


## Boundary bundles and collapse (A.203)

Collapsing a boundary bundle can forget limiting boundary directions and concordance components. For specified compact strict mapping-cylinder presentations with locally trivial boundary bundles, cutting the open inner tube and extending maps in fixed product coordinates are inverse functors, also on all jointly definable simplicial mapping spaces. This explains the category correction accompanying the Additif boundary-bundle proposal, without asserting an equivalence for unrestricted homeomorphisms or an algebraic/motivic reconstruction. Full proof: papers/02_additif/boundary_bundle_categories.tex.


## Attachment fibres and the limits of numerical recognition (A.202, A.207–A.209)

In stratified geometry, the difference between ambient and stratum dimensions does not determine the topology or dimension of a tubular attachment fibre: the disk with a transverse segment forces a positive-dimensional fibre where that difference predicts zero. Boundary cores impose a stronger condition: their definable attachment fibres contract internally. Singleton fibres recover the concordance group, while allowing arbitrary fibres still preserves its ordinary component group for the six-torus cylinder. These statements explain the exact role of transverse topology and automorphisms in the Additif and strict-cone programme. The derived cone choice space, the numerical fixed-tube group and the unrestricted fixed-tube monoid are distinct objects. The full proofs are in papers/02_additif/tubular_attachment_fibres.tex. No assertion about Chow groups, motivic weights, lambda-operations or schemes over Z follows merely from these topological component statements.
