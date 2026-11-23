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

**Earlier IDs:** SA20 A.101–A.112, A.147–A.160. **Proof:** Paper 2; the
marked fragmentation gate is recorded separately.

Strictly rigidified collar choices are contractible, whereas derived choices
of tubular or conical data can detect the concordance space of a boundary.
The six-dimensional torus supplies the nontrivial concordance information in
the Additif counterexamples. In the language of moduli problems, forgetting
rigidification changes the homotopy fibre; an ordinary uniqueness statement
does not establish contractibility of that fibre. This observation concerns
topological and PL moduli, not an algebraic stack over Spec Z.

The proposed all-real-closed-field PL/definable comparison has been reduced
to relative marked fragmentation and compatible parameter prisms, after
variation-clock and Lipschitz regularization arguments. Those analytic
reductions are not themselves a proof of the remaining fragmentation gate.

## 3. Polynomial rings and the tensor criterion

**Earlier IDs:** SA20 B.054, B.064, B.082. **Proof:** Paper 2, algebraic
part and its explicit dependency discussion.

For integer-valued polynomial rings, the multiplication map from a tensor
product to the ring in two variables has both a kernel obstruction and an
image obstruction. The mapping-cone and Tor formulation separates them.
This is directly about rings and affine schemes: a proposed biring or
composition structure requires the relevant polynomial operations to land
in the appropriate tensor product. Weak polynomial compositeness is a
different assertion from a tensor isomorphism. The Noetherian classification
still has specified structural dependencies to audit; finite computations
do not settle that classification.

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
