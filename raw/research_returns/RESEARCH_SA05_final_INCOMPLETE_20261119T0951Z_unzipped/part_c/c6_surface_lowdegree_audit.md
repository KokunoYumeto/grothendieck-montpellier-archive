# Surface and low-degree C.6 scope audit

Created during CP04 main-file freeze, 19 November2026, 05:40 UTC.
The proposed TeX is `c6_surface_lowdegree_insert.tex`; it was integrated into the main section and ledgers after CP04 save.

The parent proposed the extension. We independently reopened Saito's
primary author PDF and read all of Lemma3.9, author p42, including the
alteration and hyperplane reduction. Exact opened references:
turn695349448view0, turn158392876view0, turn670068456view0.
URL: https://www.ms.u-tokyo.ac.jp/~t-saito/pp/wmr2r.pdf

The surface input is Rapoport–Zink Satz2.13, already fully opened in
our C.4 proof audit. It is not necessary to invoke any 2026 theorem
for this case. No new bibliography key is required.

## Proof issues checked

1. A Galois-stable subrepresentation of a pure Weil–Deligne
representation need not be pure: the bottom of a nontrivial monodromy
string is a counterexample. Thus an unsplit weak-Lefschetz injection
would be insufficient. Here the split is explicit. If dim(X)=d and a
smooth complete intersection Y has dimension r, then

    i_* i^* = L^(d-r)
    H^r(X) -> H^(2d-r)(X)(d-r).

The inverse hard-Lefschetz map is Galois-equivariant. Composing it with
i_* gives a retraction of i^*. The required splitting is therefore
available on each realization even when algebraicity of that inverse
is not known.

2. The realization splitting is used only for the local purity claim.
The final motive is cut out by the algebraic projector stipulated in
the statement, so Saito's common-trace theorem is applicable. We do
not turn the realization retraction into an unproved Chow projector.

3. Semistable alteration has a proper generically finite trace:
f_* f^* is multiplication by the degree, invertible in Q_l.
After passing to a finite field extension, the original realization
is a direct summand of one admitting the semistable model. The
surface weight–monodromy theorem applies there. Purity descends to
the original field because monodromy scales by a nonzero scalar and
a suitable Frobenius power has the normalized expected weights.
This is not descent of unramifiedness.

4. For a surface, degrees0,1,2 are covered directly and degrees3,4 by
Poincare duality. Products then have pure Weil–Deligne representations
in every degree by Kunneth and tensor stability. A homogeneous
algebraic Chow projector gives a direct summand. Duals and Tate twists
preserve this statement; finite sums are grouped by their common
motivic weight.

5. For arbitrary-dimensional varieties, only supplied homogeneous
low-degree Chow projectors are included. We have not asserted that
all Kunneth or inverse-Lefschetz projectors are algebraic. The high
cohomological degrees follow from duality on realizations and can
likewise be used when their algebraic projectors are supplied.

6. With one unramified realization, the pure local summand has one
Frobenius weight. The already audited Saito proposition forces N=0
for every prime-to-p realization, and then its finite-inertia traces
force actual trivial inertia over the original field. All projectors
remain algebraic throughout this application.

The full written insert was checked against these points. The new
special case is unconditional in its stated Chow-projector scope.
The general C.6 question and the C.4 threefold H3 gate remain open.

Root independently reopened and read Saito Lemma3.9 and checked the full written insert; the audit passed before integration.
