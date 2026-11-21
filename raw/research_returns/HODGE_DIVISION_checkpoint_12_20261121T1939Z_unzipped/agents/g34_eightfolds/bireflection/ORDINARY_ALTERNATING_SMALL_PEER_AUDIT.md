# Whole-proof audit: HD-ALT-02a/b

**Result: PASS on the corrected final statement.** Reviewer
`/root/g34_eightfolds`, GPT-6 Astra Pro, effort inherited/unexposed,
HODGE_DIVISION, 2026-11-21, approximately17:13–17:16 UTC.

The entire file `research/ordinary_alternating_small_obstruction.tex`
was read. Final reviewed SHA-256:
`07b0d67eef62e9ee959b4c0440afe9efc147e954fe60e9b031b2efde1ba25938`.

The first reading found a literal scope defect in the opening lemma:
it called every irreducible representation other than the standard one
nonstandard, although its degree assertion necessarily excludes the
trivial representation. This was reported immediately. The author
inserted **nontrivial** into that opening sentence; the proof and all
computations had already selected only nonlinear rows. The corrected
sentence was reread and its final hash frozen above. No mathematical
or computational conclusion was weakened.

## Complete independent finite reconstruction

The input is the complete fourteen generic GAP tables for A_n and S_n,
8≤n≤14, with SHA-256
`f406cf1ad89801369196f36422c4dc2608e5cf96c763e5fab53b8a2ecfa1939c`.

I wrote and ran `audit_ordinary_alternating_small.py`. It imports only
my own previously reviewed integer-polynomial and Ramanujan arithmetic,
not the author's or sibling's Fourier routines, selected rows or
spectra. It checks all fourteen identifiers and source strings, group
orders, character degrees and table dimensions, and every one of the
seven core fusions: identity kernel, element-order preservation, full
normal class-size unions and compatibility with every retained prime
power map.

Symmetric rows are selected afresh by the rational normalized trace of
their exact restriction norm, with a further pointwise check against
the complete alternating rows. This gives exactly682 selected rows.
Every one of49,650 nonscalar spectra is independently reconstructed
using the cyclic Fourier formula followed by normalized rational field
trace, expressed as Ramanujan sums. Every multiplicity is nonnegative
integral and sums to its degree. Only after completing that calculation
does the program compare against the retained GAP scan: every row
minimum, every minimizing class and its entire spectrum agree.

The independent run passed in2.687 seconds. It verifies all the fifth,
seventh and quarter bounds asserted in the lemma, all nonreal and
small-degree assertions, the unique extra degree14 parameter, and the
standard tensor contradictions14<49,24<64,54<81. Its full output is
retained as `audit_ordinary_alternating_small.json`.

## Published-data and source scope

The generic character-table routines are explicit mathematical inputs.
They are not described as ATLAS tables. I freshly opened the official
CTblLib documentation at
<https://www.math.rwth-aachen.de/~Thomas.Breuer/ctbllib/doc/chap4.html>,
§4.2 and §4.2-1: it defines parameterized generic character tables and
identifies the alternating and symmetric calls and their partition
parameters. The ordinary alternating/symmetric representation theory
and Aut(A_n)=S_n for n≥8 are the same published inputs independently
checked in HD-ALT-01. This audit does not claim to rederive the complete
generic character-table algorithm or the classification of automorphisms
from these finite consistency checks.

## Full mathematical proof

The passage from symmetric extensions to all outer linear normalizers
is valid. After adjusting an odd normalizer by an inner element, its
projective action is a transposition. Its square centralizes the
irreducible core, so scalar rescaling makes an actual involution and
constructs the required S_n representation. Every original odd element
is then scalar times an element in that represented extension. Because
all symmetric characters in this complete finite range are real, a
nonreal alternating character cannot have such a normalizer; it has
only inner projective action.

D-BI-19 gives transitive permutation of the simple factors. Their
characters are related by automorphisms, so their degrees, standard
status and self-duality status agree. The fifth bound handles every
nonreal factor, including factor permutations, and contradicts the
actual sixfold branch budget since its factor degree exceeds15.

If the factor characters are real, each is self-dual. The tensor core
has a unique invariant nondegenerate bilinear form, regardless of its
symmetric or alternating type, and its full normalizer is essentially
self-dual. The original imaginary quadratic field remains contained
in the possibly larger inducing field. Thus the two nontrivial
similitude inertias required by D-BI-09 are available; no equality of
the two fields is assumed.

For nonstandard factors, the two half-moving inertias and the remaining
ten seventh-moving inertias give e≤14. The table forces the single
degree14 A_8 case, whose full quarter bound contradicts the exact
integer branch sum. For standard factors, the single-factor case is
removed by the already reviewed scalar deleted-standard theorem.
When there are at least two factors, the half-moving argument and
the lower bound1/(n−1) give exactly the three stated contradictions
for n=8,9,10. The weighted tensor-cycle quarter bound is stronger
throughout this range and correctly covers all permutations.

The surviving necessary condition is n∈{11,12,13,14}, at least two
factors, every factor standard. The theorem asserts no construction or
dominance for these survivors, and does not extrapolate the finite
calculation to n≥15. Its nonsplit and primitive factorwise
tensor-indecomposable hypotheses are retained. No TeX compilation was
performed.
