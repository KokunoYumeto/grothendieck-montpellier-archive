# C.3aw: positive-characteristic low ordinary-restriction kernels

Status: finalized after full independent root and cycles proof/source audits.
Root certified11:25:10UTC; cycles certified11:25:12.660118UTC in its
C3aw_positive_characteristic_low_injectivity_independent_REVIEW.md and
canonical events. The final file is C3_positive_characteristic_low_injectivity.tex;
the former draft is a comment-only supersession pointer.

## Exact mathematical scope

For every prime p, r>=2 and r+1<=N<=2r-1, this specifies an excellent
normal strictly henselian N-dimensional coefficient-field ring, with both
punctures regular, whose ordinary closed restriction has a non-torsion
kernel. The exhibited class is the principal Gysin image of an actual
ordinary family on the divisor, so open restriction also kills it.
The field is explicitly the algebraic closure of Fpbar(T), with T from
C.3at. No rational ordinary nonvanishing over Fpbar is asserted. This
statement alone leaves N>=2r open.

The new steps are a smooth connected positive-dimensional complete
intersection through both fixed points; an exact finite-constant
coefficient enumeration over the same function field; the smooth
incidence divisor; the actual ordinary Gysin family; and the exact
projective-bundle quotient. The generic-point non-torsion is the proved
slope-zero theorem C.3at, not a differential or finite-point inference.

## Fresh primary-source checks

- Stacks Lemma33.47.1 and Lemma33.47.3 with proof, Tag0FD4:
  https://stacks.math.columbia.edu/tag/0FD4 . The system vanishing at
  the two points is immersive off them for large degree. General
  members are smooth there. The prescribed first jets handle both
  base points. These are the precise hypotheses used.
- Stacks Lemma30.17.1, Tag0B5U:
  https://stacks.math.columbia.edu/tag/0B5U . Serre vanishing applied
  to the square of the two-point ideal gives the simultaneous
  first-jet surjection. This newly opened source is registered in
  C3aw_references.bib.
- Stacks Lemma31.15.2, Tag0B3P:
  https://stacks.math.columbia.edu/tag/0B3P . The Cartier normal
  line is the restriction of O(Y), which is trivial for the principal
  divisor used here.
- Stacks Definition42.29.1, Tag02T8, and Remark42.29.6, Tag0B6Z:
  https://stacks.math.columbia.edu/tag/02T8 and
  https://stacks.math.columbia.edu/tag/0B6Z . The integral Gysin
  formula on a contained cycle is the first Chern class of that
  restricted normal line; hence the self-intersection is zero.
  The pre-existing bibliography key cyStacksPrincipalGysin is reused.

C.3e is used in its previously proved all-characteristic integral
strict-cone scope. The full normal section ring is generated in degree
one: hypersurface Veronese and Segre multiplication supply generation,
and the divisorial valuation intersection supplies normality. No
normality or full-section-ring statement about the divisor's vertex
is assumed. Every operation on ordinary classes is performed on an
actual product with the same smooth proper parameter curve.

## Computation and layout records

code/check_positive_characteristic_low_injectivity.py retains seven
exact smooth coordinate-base examples from the C.3at hypersurfaces,
66dimension/codimension cases and198polynomial-quotient cases. All
pass, runtime0.6138760150024609seconds. The seven geometric examples
are illustrative constant-point geometry only; they are not the
transcendental generic-point witness and are not used to infer
non-torsion. The universal argument is separately proved.

The revised complete draft compiled in four stages with no undefined
citations or overfull boxes, runtime2.5362750189997314seconds. Source,
stdout, JSON and timestamped logs are retained. The final renamed
wrapper is recorded in its own event after completion.

Final renamed proof had a0.10272pt heading overflow. Shortening only the heading removed it; the four-pass rerun passed at 2026-11-19T11:31:46.698918+00:00, runtime2.667724256000seconds, zero diagnostics. Final event retained separately.
