# Root audit of A5.016 — individual real-definable surface maps

We read the complete candidate and compared its numbered promoted version.
The full proof passes within its explicit scope: the finite height-leveling
lemma works over every real closed field; the cell-like surface conclusion
is for one definable map over the real numbers. No uniform family theorem
or original A.5 progress credit is inferred.

## Primary sources actually checked

Root reopened the full Rourke–Sanderson original, read Lemma 4.23 on
printed page 58, Theorem 2.25 on page 24, and the closed-surface classification
remark following Theorem 5.5 on page 63. Retrieval records are
`turn247326264view0`, `turn686040111view0`, `turn686040111view1`, and
`turn686040111view2`. The source's matched derived-subdivision argument
supports the construction; the proof below spells out the required extension
to two different nonnegative heights. The general scalar triangulation input
is the already opened Shiota Theorem 2.2(1), printed page 6.

Root explicitly viewed the original Siebenmann scan pages 271 and 272 at
`source_external/siebappr_images/p-01.png` and `p-02.png` during this audit.
Theorem A condition (a) includes dimension two, with the boundary hypothesis
vacant for closed surfaces. Its Complement supplies the continuous family
of homeomorphisms ending at the cell-like map. The next paragraph explicitly
defers continuous dependence on that map; we do not import such dependence.

## Exact finite leveling

We checked that the collar image contains a whole small sublevel band by
the positive minimum on its compact complement. A simultaneous triangulation
makes the collar simplicial and both scalar heights linear. Their zero
vertices coincide. Descending stellar subdivision of every original mixed
simplex is legitimate: earlier stars leave its proper faces intact. The
two chosen stellar points need not correspond geometrically, but the
resulting abstract complexes are identical. Every original zero-to-positive
edge is removed, and stellar subdivision creates no new edge between old
vertices. Consequently the entire low sublevel band is exactly the subcomplex
with vertex heights zero or epsilon in each triangulation. The canonical
isomorphism fixes the zero set and preserves these vertex heights, hence
preserves the prescribed scalar height everywhere. This is finite over
every real closed field and involves no limiting mesh.

## Three-dimensional link recognition

Purity follows from manifold dimension at a point in an open maximal
simplex. The local integral homology formula gives two or one incident
tetrahedra at a triangle. Edge links are connected graphs of degree two
or one, and the local homology distinguishes a circle from an interval.
Vertex links are therefore compact PL surfaces. An interior vertex link
has the homology of a sphere and is a PL sphere. A boundary vertex link
is acyclic. Its double has H2 equal to Z to the number of boundary circles
and H1 of rank one less; the closed-surface classification forces one
circle and a sphere double. The PL Schoenflies conclusion gives a disk.
This justifies the actual triangulation being a PL manifold; it does not
assert that an arbitrary TOP coordinate map is PL.

## Mapping cylinder and definable approximation

For the source family a_t ending at q, the inverses b_s=a_(1-s) inverse
are jointly continuous for s positive. The equality of their uniform
q-error with the uniform error of a_(1-s) proves continuity of the explicit
height-preserving map from G times I to the embedded mapping cylinder.
Compactness makes that continuous bijection a homeomorphism. Only the
resulting TOP three-manifold assertion is used from this classical family.

Exact scalar definable triangulation turns the cylinder height into a PL
function and both boundary levels into subcomplexes. The link argument
and the PL collar theorem then supply the finite height-preserving collar.
Division of its middle coordinate by the positive height produces the
joint definable k_s. Uniform continuity of its last coordinate gives
q k_s tending uniformly to identity. Passing to inverse maps gives the
definable continuous extension h_0=q. Components and the double-cylinder
reflection are handled explicitly.

## Finite parameter-fold certificate and limitation

We read the exact script
`agents/maximal_locus/code/check_surface_collar_parameter_fold.py`
and its JSON output. All **21 checks passed**, in the observed runtime
**0.06886558799305931 seconds**. The script verifies the three affine
pieces, the boundary matches, and three distinct preimages with their
correct branch inequalities using positive rational-function certificates.
The substitutions cover the required open parameter ranges over any real
closed field. No numerical sampling substitutes for the inequalities.

The example is positive away from its collared zero set, but arbitrarily
near the central parameter some positive levels have three preimages.
It therefore refutes unrestricted parameter-preserving leveling. It does
not refute the special family mapping-cylinder problem, whose positive
fibres already have the fixed surface type. That special condition, the
joint parameter requirement, and the arbitrary-field version remain gates.
