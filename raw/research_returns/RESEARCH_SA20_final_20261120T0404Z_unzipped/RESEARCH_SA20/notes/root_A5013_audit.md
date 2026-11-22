# Independent root audit of A5.013

19 November 2026, 15:50 UTC. AI-produced by GPT-6 Astra (OpenAI, ChatGPT Pro mode).

We independently read the full pending proof in
`agents/lie_theory/notes_A5_surface_pending.tex`, reread the barycentric
homogeneity argument of A5.008, and opened both original inputs:

- Masahiro Shiota, *PL and differential topology in o-minimal structure*,
  arXiv:1002.1508v3, printed pp.33–34, unnumbered two-coordinate statement
  and its proof. <https://arxiv.org/pdf/1002.1508>.
- David Marker, *Model Theory for Algebra and Algebraic Geometry*, Orsay,
  spring 2010, Theorem 2.4, printed p.17.
  <https://homepages.math.uic.edu/~marker/orsay/orsay1.pdf>.

Root source references: `turn418625417view0`, `turn418625417view1`,
`turn772396760view0`. The local Shiota text was also read at
`source_external/shiota_1002.1508.txt`, pages33–34.

## First-order uniformity

The compactness argument has a legitimate domain at both applications.
First, Shiota supplies left and right deleted-interval certificates at *every*
point of each fixed edge, in every elementary extension. A certificate is a
fixed formula format with finitely many geometric parameters; all its
homeomorphism, continuity, diagram, and containment assertions are first-order.
Failure of any finite subcollection of formats to cover the edge would produce
an elementary extension with a point admitting none, contrary to Shiota.

The union of all intervals certified by the resulting finite list of formats
is therefore definable. Its complement has no interval and is finite by
o-minimality. This is stronger than just having arbitrary intervals near every
point in a non-Archimedean order: the finite-format step is essential.

Only after this definable domain has been obtained is compactness applied
again, now to local finite simplicial-map models at all its points. It is not
applied to the unknown good locus. Any finite simplicial map can be put in a
fixed rational realization; its combinatorial type belongs to the format.
The good simplices for each resulting model are chosen in the original
structure, using A5.008. No transfer of an unspecified infinite disjunction
expressing goodness is needed.

## Whole-fibre PL models

If a continuous map agrees with a finite piecewise affine map on an open
inverse image, a fibre there is a definable clopen subset of a semilinear
fibre of the latter map. Finite semilinear path components make it
semilinear; closedness makes it a compact polyhedron. A PL function vanishing
exactly on that fibre gives a compact polyhedral neighbourhood contained in
the agreement region. The closed image of the complement of its interior
excludes stray preimages after shrinking the target. Thus the resulting model
contains the *whole* nearby inverse image. This does not assume that the
piecewise affine extension is continuous elsewhere.

For the planar chart, the target finite complex may contain both the image of
the selected source polyhedron and a small compact box around the target
point. The simplicial model need not be surjective onto that target complex.
This makes the domain and target of the model explicit, including empty fibres.

## Signed edge and noncompact reduction

We checked that applying Shiota to `(s−a,abs(t))` is compatible with both closed
side subcomplexes because its isotopy preserves every simplex. Restoring the
sign yields the required piecewise affine agreement on an *open* two-sided
neighbourhood of the deleted edge interval. Agreement at the centre `a` is
not asserted or used.

The noncompact reduction uses a bounded graph closure. Over the original
manifold target, properness and a compact neighbourhood prevent added graph
points. Thus the compactified map has exactly the original whole fibres
there. A Hardt-compatible finite triangulation supplies the open triangles;
each interior edge of the two-manifold has exactly two incident triangles;
the argument above handles its locus, and only finitely many vertices remain.

Outcome: PASS under the stated hypotheses, over every real closed field and
every o-minimal expansion. The maximal manifold-and-local-triviality locus of
every continuous definably proper map to a target of dimension at most two
is definable. The separate recursive partition assertion remains refuted.
For the unresolved maximal-locus assertion, the first possible remaining
target dimension is three, with positive-dimensional fibres. This result
does not itself settle the A.1 higher concordance comparison.
