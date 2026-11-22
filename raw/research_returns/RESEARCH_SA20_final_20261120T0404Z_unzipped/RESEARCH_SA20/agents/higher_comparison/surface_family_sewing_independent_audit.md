# Independent audit: finite-format sewing of homeomorphism approximants

AI-produced by GPT-6 Astra (OpenAI, ChatGPT Pro mode), agent
`/root/higher_comparison2`, 19 November 2026, 21:31 UTC.

## Verdict and precise scope

**PASS** for the complete candidate
`agents/maximal_locus/notes/surface_family_sewing_2126.tex`, SHA256
`8d8f8157d213f8737e9f4ffe091bb28fdbdc1c2740ff0d7f750d90fbcc37ab04`.
All five proof steps and the surface-family consequence were independently
read. No mathematical correction is requested. Promotion remains with
root and the author; included sources and bibliographies are frozen.

The general lemma is valid over an arbitrary o-minimal real closed
field. It assumes compact definable sets `A,F,G`, a jointly continuous
definable target family `q`, and a *single* definable family of actual
homeomorphisms `psi_(a,s)` with uniform error less than `s`. It constructs
a jointly continuous definable family of homeomorphisms at positive
height, extending by `q` at height zero, uniformly in the compact
parameter. It does not infer a bounded formula format from individual
approximation alone.

Combining it with the separately audited A5.017 supplies that hypothesis
for jointly continuous cell-like maps between fixed compact closed
surfaces over a real o-minimal expansion. This gives the claimed coherent
surface approximation and its family mapping-cylinder product. Neither
the general A.5 gate nor the higher PL--semialgebraic comparison follows
without an additional reduction to these hypotheses.

## Dependencies actually used

The proof uses the already audited A.138 for fixed-format metric
affineness and small strong definable contractions, and exact scalar
triangulation from Shiota, *PL and Differential Topology in o-minimal
Structure*, arXiv:1002.1508v3, Theorem 2.2(1), printed p.6, in its
all-real-closed-fields setting from Section 2. That original theorem was
independently reopened in the A5.017 audit, recorded at
`agents/higher_comparison/A5_017_independent_audit.md`.

No stronger simultaneous triangulation of several coordinate functions
is used. The only scalar preserved exactly is the height. No assertion
that a definable choice is continuous is used. The surface consequence
uses A5.017 only for a bounded-format, possibly discontinuous choice of
approximating homeomorphisms.

## Continuity partition and scalar height triangulation

Hardt triviality of the compact graph fibers over a parameter cell gives
a homeomorphism from `S times Q` to the graph family. Projection to
`S times F` is a continuous definable bijection. On each closed bounded
parameter neighborhood inside the locally closed cell, source and target
are definably compact, so its inverse is continuous. Such neighborhoods
cover the cell. The same argument using `G` handles inverse evaluation.
Thus the claimed finite joint-continuity partition is justified.

After a frontier refinement, compatibility with closures of the pieces
ensures that every open simplex of the height triangulation lies in one
continuity piece. The compact domain `A times [0,1]` is triangulated with
its actual height linear on simplices, and the zero-height locus is a
subcomplex `L`. This supplies the useful locally closed parameter domain
`K minus L`; it avoids assuming a collar for a general arbitrary
non-locally-closed definable parameter set.

The later cutoff `r <= s0` is a finite polyhedral cut of the already
linear height. Its compatible triangulation refines the old simplices,
preserves linear height, does not increase dimension, and keeps every
new open simplex inside an old continuity piece. It does not change or
enlarge any of the already fixed map families.

## Finite pools and the order of radius choices

All maps in `H_j` are homeomorphisms `F -> G`; all maps in
`D_j = {u v^{-1}: u,v in H_j}` are self-homeomorphisms of `G`.
Inversion and finite composition preserve definable families of finite
graph format. The identity lies in every `D_j`, so
`H_(j+1) = D_j H_j` contains `H_j`.

Crucially, these pools are defined through the fixed finite number of
skeletal stages *before* any small height or contraction radius is
chosen. A.138 provides a single contraction of a neighborhood of the
identity in `D_j`, and its outputs remain in `D_j`. Thus the construction
does not hide a new format after the tolerances have been chosen.

The function `omega_n(u)` is definable, nondecreasing and bounded by the
diameter of the compact target. Its limit at zero is zero. The revised
proof establishes this over arbitrary real closed fields by definable
choice: hypothetical bad inputs `z(u)` tend to the identity in the
metric, while their selected times have a limit after shortening the
interval by o-minimal monotonicity. Joint continuity at that limiting
point contradicts a positive output-error lower bound. This does not
use an ordinary finite subcover of an infinitesimal-mesh cover.

The recursive functions `S_n` and `E_n` are nondecreasing and tend to
zero, so a single positive cutoff meets all finitely many contraction
radii. The order of construction is consequently noncircular. The
functions need not be continuous away from zero for any step of the
argument.

## Continuous target modulus

The maximum defining `D(p,p')` is definable and continuous because `Q`
is continuous on a definably compact product. For positive `t`, the
closed definable set where `D >= t` contains no diagonal point. If it
is nonempty, its minimum separation is positive; otherwise the chosen
value one is valid. This proves positivity and monotonicity of `beta`.

The inf-convolution over `0 <= u <= 1` is definable and Lipschitz.
For `t > 0`, splitting into `u <= t/2` and `u >= t/2` gives lower
bounds `t/2` and `beta(t/2)` for the expression before multiplication
by one half. It is therefore positive. Its value is at most
`beta(t)/2` and tends continuously to zero at zero. This supplies a
continuous collar-width control without importing ordinary compactness
or a nondefinable modulus.

## Partial radial collars and the interfaces

For an n-simplex, the radial coordinates
`p = (1-u)b + u c` are continuous away from its barycenter.
The chosen width `w(b)` is positive exactly where `r(b)>0`, at most
one quarter, and tends to zero at every deleted zero-height face.
For `0 < u < w(b)`, linearity of height gives

`3 r(b)/4 < r(p) < 5 r(b)/4`.

In particular `r(p)/2 < r(b) < 2 r(p)`, as used in the proof. The
other width bound gives `|p-b| < gamma(r(b))`, hence
`||Q_p - Q_b|| < r(b) <= 2 r(p)`.

The input to the contraction is `z = psi_p H_(n-1)(b)^{-1}`.
Both factors lie in `H_(n-1)`, since the pools are nested. The exact
identity

`d_G(u v^{-1}, id) = 2 ||u-v||_infinity`

uses surjectivity of both `u` and `v`; it does not use an inverse of
the possibly noninjective target map `q`. The induction and the two
collar estimates give precisely

`d_G(z,id) <= 6 r(p) + 2 E_(n-1)(2 r(p)) = S_n(r(p))`.

Thus every contraction call lies in its preselected domain.

There are four interfaces to check, all handled by the formula:

1. On the outer third of the collar the contraction time is zero,
   so the result is exactly `psi_p`. This handles the outer edge.
2. On the inner third the contraction time is one, so the result
   is exactly the previously constructed boundary family at `b`.
   Every retained positive-height boundary point has positive width,
   and `u/w(b)` tends to zero there. Hence continuity holds even
   when the initial approximants have no boundary limit.
3. If the radial boundary point tends to a deleted zero-height
   face while the interior point tends to a point of the open
   simplex, the radial parameter stays positive and the width
   tends to zero. The formula is eventually the unmodified `psi`.
4. The barycenter has a neighborhood outside the collars because
   their widths are at most one quarter.

On the collar interior the anchor and its inverse vary continuously.
The latter follows locally by definable compactness of `F,G`; the
already constructed skeleton minus `L` is locally closed and has
closed bounded local parameter neighborhoods. This gives continuity
in the map-and-inverse metric and justifies composition with the
contraction. The restrictions to each `sigma minus L` are continuous.
These are finitely many relatively closed sets in the skeleton minus
`L`, so ordinary finite closed-set pasting proves global continuity.

No uniform convergence of `C_n(z,t)` as `t -> 1` over a bounded
set of arbitrary inputs is needed: near each retained boundary the
formula is exactly the anchor.

## Error induction, zero-height extension, and cylinder consequence

For a collar point, the displacement of the contraction after
composition with the anchor is bounded by
`omega_n(S_n(r(p)))`. Adding the anchor's inductive error and the
target variation gives exactly the expression included in `E_n`.
Outside collars the original error is less than `r(p)`; on the
old skeleton the previous bound is included in the maximum.
Thus the induction closes at every stage with no missing boundary case.

At the last stage, exact preservation of the scalar height gives the
uniform estimate over all parameters and source points by `E_d(s)`.
Its limit zero and joint continuity of `q` prove continuity at the
entire zero-height set. All positive slices remain actual
homeomorphisms. Their inverses are jointly continuous on positive
height by the same local compactness argument.

For the surface consequence, A5.017 supplies the single initial
definable family for compact `A`. The trace formula on the positive
and negative halves of the family cylinder is
`(a,x,t) -> (a,t,h_(a,|t|)(x))`, with the center identified by `q`.
Uniform convergence makes this continuous across the center, and
positive-height slices and the center map are bijective. The compact
definable quotient, or the equivalent inverse criterion already stated
in the candidate, makes it a definable homeomorphism over
`A times [-s0,s0]`. The displayed inverse error identity is exact.
For an open real parameter domain, a compact closed neighborhood of
the specified parameter permits this local application.

This is a substantive special family construction. The missing
reduction from an arbitrary proper definable map to these cell-like
surface families remains a separate requirement, as the candidate
explicitly states.
