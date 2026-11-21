# SF-E834: independent whole-proof audit

**Result: PASS in the stated stable reflexive RM fourfold scope.**

Reviewer: `/root/g34_eightfolds`, GPT-6 Astra Pro, effort inherited/unexposed,
run HODGE_DIVISION. Actual completion/source verification: 2026-11-21
21:29:17 UTC. This is a targeted whole-proof check, including independent
derivation of the new averaging, equality, bounded-curvature and extension
arguments. It is not a claim to have reconstructed the published analytic
existence theorems or their upstream proofs.

Reviewed file: `agents/sixfolds/rm_reflexive_mixed_curvature_draft.md`, all
343 lines, frozen SHA-256
`515d1e292d9925ef158bc865dd1c514b550e9c2d5634ea8d93c6cc9a4e92e89e`.
The reviewer did not edit the author's file. No mathematical repair was
requested. No numerical certificate is needed or claimed.

## 1. Statement and hypotheses

The claim concerns a slope-stable reflexive coherent sheaf on the
specified polarized abelian fourfold, with the genuine Rosati-invariant
real quadratic action and its two parallel complex rank-two eigenspaces.
It proves mixed discriminant nonnegativity and, at equality, local
freeness and projective flatness. The balanced normalized character with
positive parameter then cannot occur. Stability, the actual reflexive
sheaf, the polarization and the rational RM structure are retained.

I checked the discriminant convention
`Delta = c1^2/(2r) - ch2` and the Chern-Weil sign. For unitary curvature,
the trace-free representative is `(8 pi^2)^(-1) Tr(F0 wedge F0)`.
There is no appeal to a Chern-Weil current across the singular set without
justification. Reflexivity on the smooth fourfold makes the singular
set have complex codimension at least three, hence dimension at most one.

## 2. Mixed Chern-Weil pairing by translated surfaces

I independently checked the entire averaging argument. Admissible
curvature is square-integrable, so the coefficients of the degree-four
Chern-Weil form are integrable. For a smooth complete-intersection
surface representing positive multiples of two integral ample classes,
translations meeting the singular set lie in the image of the difference
map from `S x Y`, of complex dimension at most three. They therefore form
a Haar-null subset of the fourfold.

On every good translated surface, the sheaf is a vector bundle in a
neighborhood and ordinary smooth Chern-Weil theory applies. Its
topological pairing is the same under translation. Absolute Fubini is
valid: integration of the coefficient norms over the translation
parameter and the compact surface is bounded by a constant times the
global L1 norm. Thus no undefined product of a general current with an
L1 form is used.

The averaged integration current is translation-invariant and closed;
it is the smooth invariant representative of the surface class. This
gives exactly the desired pairing identity for ample divisor pairs.
Bilinearity and openness of the ample cone then extend the identity to
their real linear span.

The RM form needed here belongs to that span. For a rational trace-zero
Rosati-selfadjoint endomorphism `u` with `u^2=d`, the form
`lambda(v,w)=theta(uv,w)` is rational, alternating and of type (1,1).
Its denominator can be cleared to obtain a divisor class. The identity
`theta_+ theta_- = (theta^2-lambda^2/d)/4` is exact. Small rational
perturbations of theta by lambda are ample. This proves the mixed
pairing identity without supposing either eigenspace defines a subtorus.

## 3. Equality and the local curvature bound

I rederived the primitive mixed sum-of-squares identity and its equality
case. Summing it in an orthonormal basis of the trace-free unitary Lie
algebra proves nonnegativity. Vanishing integral forces the continuous
nonnegative density to vanish everywhere on the locally free locus.
The trace-free curvature then has only the two pure-plane blocks, each
primitive in its plane; every real mixed component is zero.

Bianchi gives transverse covariant constancy of each pure block. For
example, inserting two constant vectors from one parallel plane and
one from the other leaves precisely the transverse covariant derivative
of the first block. The induced connection on endomorphisms is unitary,
so its Hilbert-Schmidt norm is constant along such transverse paths.

The clean-slice argument works near a singular curve as well as an
isolated point. In nested local product boxes, project the compact
singular set in the largest box to either complex two-plane. Each image
has real measure zero. A point outside the projection gives a compact
horizontal or vertical slice in the intermediate box wholly disjoint
from the singular set, hence with uniformly bounded smooth curvature.
For a fixed coordinate, the deleted set in the other two-plane has
complex dimension at most one; its complement in a convex box is path
connected. A complex line through a point outside that analytic set is
not contained in it, and discrete intersections along a compact segment
can be avoided by small detours. Transport to the two clean slices now
bounds both pure blocks uniformly on the smaller box. There is no
assumption of a global product or of simply connected deleted fibers.

This yields a locally uniform bound for the trace-free curvature near
the entire singular set. It is stronger than the original L2 bound and
is the genuinely new input to the removal step.

## 4. Determinant repair and holomorphic extension

The reflexive determinant is a line bundle on the smooth ambient
variety. A smooth global metric on that line bundle permits scalar
rescaling of the admissible metric so that the determinant metric is
this smooth one. The endomorphism metric and trace-free curvature are
unchanged by this rescaling. The full curvature becomes the bounded
trace-free part plus the smooth scalar determinant curvature.

Consequently the modified metric has finite L4 curvature on the
fourfold. It need not remain Hermitian-Einstein; the published extension
theorem only requires the stated curvature norm. Taking G=GL(r),
K=U(r), and complex dimension n=4 satisfies its hypotheses, including
the general analytic singular set of codimension at least two.

The extension is a holomorphic vector bundle. Both that bundle and the
original sheaf are reflexive and agree off a set of codimension at least
two, so reflexive Hartogs uniqueness identifies them. This proves local
freeness of the original sheaf. The argument does not assert that the
particular admissible connection itself extends smoothly.

## 5. Final use of E811 and the balanced character

I checked the exact interface with the previously reviewed E811 bundle
theorem and its RM specialization. It applies after local freeness has
been proved, to the unchanged slope-stable sheaf and the rational
polarization. The genuine RM condition rules out a nonzero rational
class lying in either pure-plane volume line. The earlier bundle
equality argument therefore yields projective flatness.

For the displayed balanced character, B-field invariance of Delta gives
`Delta = R q (theta_+^2+theta_-^2)/2`. Its mixed pairing vanishes, whereas
its pairing with `theta^2` is strictly positive when q>0. This contradicts
the vanishing discriminant of a projectively flat bundle. The passage
does not require a separate finite group action on any analytic
construction. It also does not extend the theorem to unstable or merely
semistable sheaves or to arbitrary perfect complexes.

## 6. Primary sources actually checked

* Bando-Siu, *Stable sheaves and Einstein-Hermitian metrics*, in
  *Geometry and Analysis on Complex Manifolds* (1994), pp.39-50.
  I visually read the original author-hosted p.39 admissibility
  definition and p.40 Theorem 3. The locally free locus has an admissible
  metric for a stable reflexive sheaf; admissibility supplies the L2
  curvature used above. I also read the author's complete relevant
  construction/proof text pp.45-49, including the codimension statement
  and the stable existence passage. This is use and checking of a
  published theorem, not a new proof of nonlinear existence.
  Author source: https://people.math.harvard.edu/~siu/bando_joint_paper/index.html.
  Images and OCR are retained in the sibling `references_cache`.

* Biswas, *A criterion for holomorphic extension of principal bundles*,
  Kodai Math. J.34 (2011), 71-78. I read the complete published paper,
  particularly the curvature convention pp.71 and 76-77, Theorem 1.2
  p.72, Theorem 3.2 and its entire proof p.77, and the extension criterion
  Proposition 2.3 with its proof pp.74-75. The hypotheses concern a
  general closed analytic set of codimension at least two and finite
  L^n curvature, n the complex dimension. They impose neither an
  isolated-point condition nor a Hermitian-Einstein condition. The
  theorem cites Harris-Tonegawa for the vector-bundle result; I have not
  obtained or newly audited that upstream full proof.
  Primary PDF: https://www.jstage.jst.go.jp/article/kodaimath/34/1/34_1_71/_pdf/-char/en.
  Retained copy `sources/Biswas2011_extension_published.pdf`, 79,867 bytes,
  SHA-256 `6fa0c6645b1e7bb5797b2f4fb983d957d945afce363772fd4e9e11e29da70e42`.

* E811 is a previously reviewed new theorem of this run, not a published
  input. I rechecked its bundle/RM interface and the sum-of-squares
  calculation used here. This event does not relabel its previous
  complete reviews as a fresh independent reconstruction of every step.

The first local PDF retrieval failed before network access because the
`requests` Python module was unavailable. A subsequent standard-library
retrieval succeeded; the failure and success are both preserved in
`sources/Biswas2011_retrieval.json`. The web primary PDF was separately
read successfully. Neither event is a failed mathematical certificate.

## 7. Conclusion

Every new implication in the frozen 343-line proof has been checked.
The previous reflexive equality gap is filled in the stated stable RM
scope by the actual curvature and holomorphic extension argument.
There is no remaining unverified 032/Markman premise in this argument.
No numerical computation, TeX compilation or upstream Harris-Tonegawa
proof audit is claimed.
