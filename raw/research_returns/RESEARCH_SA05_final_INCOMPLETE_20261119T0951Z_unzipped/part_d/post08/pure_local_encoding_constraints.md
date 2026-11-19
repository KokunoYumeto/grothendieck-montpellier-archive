# Two constraints on an attempted pure local encoding

19 November 2026. These are formal diagnostics of particular constructions. Neither is an impossibility theorem for every geometric encoding, and neither proves a converse to C6.

## 1. A hyperbolic pairing does not by itself supply weight purity

Let A and B be finite-dimensional Frobenius modules of weight zero, and let a:A→B commute with Frobenius. Write their dimensions as s,t and the rank of a as r. Consider the doubled upper and lower spaces

\[
U=A\oplus B^\vee,\qquad
L=(B\oplus A^\vee)(1).
\]

Their Frobenius weights are respectively zero and minus two, and both dimensions equal s+t. Put N equal to zero on L and, as a map U→L(-1), set

\[
N=\begin{pmatrix}a&0\\0&-a^\vee\end{pmatrix}.
\]

Take the symmetric hyperbolic pairing that pairs A with A^vee(1) and B^vee with B(1). The indicated minus sign gives its infinitesimal skew-adjointness condition, after the canonical twists. For an alternating hyperbolic pairing, replace the second block by +a^vee; the same skew-adjointness condition then holds. In particular adding the dual map can repair either elementary pairing condition. Neither choice changes the rank calculation

\[
\operatorname{rank}N=2r.
\]

If this two-weight module is to be pure of generic weight minus one in the weight–monodromy sense, its only required nontrivial monodromy isomorphism is

\[
N:\operatorname{Gr}^{W}_{0}\xrightarrow{\sim}
\operatorname{Gr}^{W}_{-2}(-1).
\]

It would therefore require 2r=s+t. Since r≤min(s,t), this equality is equivalent to s=t=r: a must already be an isomorphism. When s+t>0, the zero map or a rank-deficient map does not become a single pure monodromy string merely by this doubling. The zero object is the harmless vacuous case.

This conclusion is a direct linear-algebra consequence of the stated weight–monodromy purity requirement. It is not an unconditional claim that all pure local motives satisfy the still-conjectural weight–monodromy theorem. Nor does it exclude a direct sum of different generic weights. Separating an arbitrary map into strings and residual weight-zero or weight-minus-two pieces, however, needs its actual kernels, images and cokernels. A numerical projector need not realize those cohomological pieces without additional hypotheses. The BGV stable-category equivalence supplies the square-zero object, but does not supply this pure decomposition.

## 2. A scalar detector cannot remain a smooth lisse family at its zero parameter

Fix one coefficient prime l≠p, a finite extension K/Qp, and a lisse Q_l local system V on an open neighborhood S of zero in the parameter line A1_K. Suppose V comes from a finite relative algebraic or motivated presentation as in the established local/global approximation proposition. A stable integral lattice and Kisin's local constancy theorem give a K-adic neighborhood U of 0 on which the G_K-modules V_x are all isomorphic. In particular, unramifiedness is constant on U.

Consequently one cannot realize, in such a family containing 0, the proposed rule

\[
V_x\text{ is unramified}\quad\Longleftrightarrow\quad x\,a_l=0
\]

for a fixed nonzero Q_l-linear map a_l and every rational parameter x∈Q∩U. Multiplication is here defined by the canonical inclusion Q→Q_l; no inclusion K→Q_l is assumed. The nonzero rational parameters x=p^n approach zero in K, so the right side changes between zero and arbitrarily nearby permitted parameters, whereas the left side is locally constant. Any such scalar construction must leave this smooth lisse setting at its zero parameter, change its coefficient presentation, or use a different detector. This does not exclude a discrete construction for each input cycle.

The only external input in the second observation is the already independently checked Kisin Theorem 5.1 and Proposition 5.2, author pp.16–18: https://people.math.harvard.edu/~kisin/dvifiles/locconstpap.dvi. The first observation is proved by the displayed rank inequality. The underlying analytic encoding and its exact pure-category limitation are documented in `part_d/post06/bgv_converse_scope_audit.md`; the established number-field approximation is in `part_d/c6_global_local_reduction.tex`.

Part C independently read the complete note and checked the hyperbolic signs, twists and rank inequality. Its initial check caught an undefined multiplication by an arbitrary K-scalar in the second observation. The corrected actual text restricts to rational parameters and was reread and passed. The zero-object qualification was also made explicit. These are written mathematical checks; no new primary-source proof audit is asserted here.

Root independently read the complete corrected note at the measured time 08:42:15 UTC and passed both pairing signs, the rank criterion, its explicit weight–monodromy conditionality, and the rational-parameter Kisin argument. The check is recorded here during the checkpoint metadata freeze; no frozen ledger has been changed.
