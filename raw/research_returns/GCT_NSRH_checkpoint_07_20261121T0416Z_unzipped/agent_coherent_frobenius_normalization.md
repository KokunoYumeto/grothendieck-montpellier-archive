# F36 supplement: normalization supplies an actual unit coherent Frobenius model

Author/checker: `/root/gct_statements`, GPT-6 Astra Pro; effort inherited/not exposed. Date: 2026-11-21 UTC. This is a separate constructive supplement, leaving the independently reviewed hash of `agent_coherent_frobenius_gate.md` unchanged. All arguments below are explicit module calculations, not a new arithmetic-purity claim.

## 1. The actual normalized model and its module comparison

Retain `R=k[[t]]`, `Delta=t^m u`, and

\[
C=R[x]/(x(x-\Delta)),\qquad L_1=C/(x),\quad L_2=C/(x-\Delta).
\]

The normalization embeds the actual center into

\[
\bar C=R\times R,
\qquad a+bx\longmapsto(a,a+b\Delta).
\tag{N1}
\]

Its image consists of pairs congruent modulo `Delta`; its cokernel is `R/(Delta)` and has length `m`. The corresponding normalization of the actual algebra is

\[
A=R\times R\times M_2(C)
\hookrightarrow
\bar A=R\times R\times M_2(R)\times M_2(R).
\tag{N2}
\]

The quotient `bar A/A` has `R`-length `4m`, one copy of `R/(Delta)` for each matrix entry; the scalar blocks contribute zero. This inclusion is an isomorphism after inverting `t` but retains the actual integral collision defect.

Write `S=Spec R sqcup Spec R sqcup Spec C`, and let `f:bar S->S` be its normalization, with four components above the base trait. On them choose the free bundles

\[
\bar E=(R,R,R^2,R^2),\qquad
\bar{\mathcal F}=(R^{20},R^4,R^{16},R^4).
\tag{N3}
\]

Here `bar E=f^*E` for the actual `E=(R,R,C^2)` from F21. Exact pushforward gives

\[
f_*\bar{\mathcal F}
=(R^{20},R^4,L_1^{16}\oplus L_2^4)
=\mathcal F.
\tag{N4}
\]

Since `E` is finite locally free, ordinary tensor-Hom adjunction gives

\[
f_*\mathcal Hom_{\bar S}(f^*E,\bar{\mathcal F})
\simeq\mathcal Hom_S(E,f_*\bar{\mathcal F})
=\mathcal Hom_S(E,\mathcal F).
\tag{N5}
\]

Under this isomorphism, the right action of `A=Gamma End(E)` is restriction of the right action of `bar A=Gamma End(bar E)` along (N2). On the matrix component, this is simply the equality between the two branch row modules and the row module with coefficients `L_1^16⊕L_2^4`. Thus global sections of (N5) are exactly the actual 64-dimensional tensor lattice with its original specified `A`-action, via the already checked regular F21 isomorphism. This is stronger than a character or dimension match. Passing upstairs enlarges the acting algebra but does not change the action of the original one after restriction.

## 2. Unit coherent Frobenius exists upstairs

On each normalized component use absolute Frobenius `r->r^p`, and on every free bundle in (N3) use its standard basis to define the linearization by `1 tensor e_j -> e_j`. This gives unit isomorphisms

\[
F_{\bar S}^*\bar E\simeq\bar E,
\qquad F_{\bar S}^*\bar{\mathcal F}\simeq\bar{\mathcal F}.
\tag{N6}
\]

The induced endomorphism on `bar A` is entrywise Frobenius in each matrix block. It is a ring homomorphism, and the inclusion (N2) commutes with it because both branch evaluations commute with the absolute Frobenius on `C`. The right row module upstairs also has a unit algebra-linearized Frobenius structure. Therefore this is a unit coherent Frobenius model on the normalization which preserves the actual original algebra action under restriction.

No claim is made that the normalized center equals the original center, or that the extra branch idempotents belong to the original algebra over `R`. The quotient length `4m` records precisely that difference.

## 3. Why pushforward loses the unit property

The absolute Frobenius square with the finite map `f` commutes. Its natural pullback-pushforward comparison is

\[
F_S^*f_*\bar{\mathcal F}
\longrightarrow f_*F_{\bar S}^*\bar{\mathcal F}
\simeq f_*\bar{\mathcal F}.
\tag{N7}
\]

On one branch this comparison is exactly

\[
C/(x_i^p)\twoheadrightarrow C/(x_i),
\qquad x_1=x,\quad x_2=x-\Delta,
\]

the surjection computed in the F36 report. Thus it has an `R/(Delta^(p−1))` torsion kernel per branch copy. Its total torsion length is `20m(p−1)` on `mathcal F` and `40m(p−1)` on the actual row tensor module. For the original order-two center the latter is `80(p−1)`.

Consequently a unit coherent Frobenius structure upstairs pushes forward to the explicit nonunit structure downstairs. The parameter-base linearization remains a unit because the pushed-forward sheaf is a free `R`-module; the center pullback imposes the additional singular-center relations and is different. These are exactly the two linearizations distinguished in the main F36 report.

After inverting `t`, the normalization is an isomorphism and the torsion kernel vanishes. The failure is supported on the actual collision, not on the generic representation. Its length depends on the collision order which the ordinary constant étale trace family in F22 does not detect.

## 4. Scope and verification

This constructs the promised normalization repair explicitly. It does not identify the quantum grading with a Weil weight, produce an ℓ-adic realization of the coherent structure sheaf, identify VIII's basis, or establish the required path-output sign. Nor does it descend a unit structure to the original center: (N7) shows exactly why that descent fails.

Checked in full: the normalization inclusion and quotient; the actual multiplicity bundles; the exact right-action comparison through finite pushforward/Hom; unit coherent Frobenius on the free normalized branches; commutation of the algebra diagram; the explicit comparison map and its kernel; and generic-versus-collision support. Suggested event: `F36-NORMALIZATION-REPAIR-PROPOSAL`. A fresh reviewer should check this separate supplement before it is incorporated into a final statement.
