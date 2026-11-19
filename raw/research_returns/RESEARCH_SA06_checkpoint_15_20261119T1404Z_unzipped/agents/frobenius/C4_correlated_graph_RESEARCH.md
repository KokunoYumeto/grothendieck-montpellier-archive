# Correlated type-(1,2) monodromy: exact abstract obstruction and geometric gate

This is a new research note, not a restoration. The abstract all-level theorem is typed in `C4_correlated_graph_obstruction_draft.tex`. Parent assigned C.4z after the complete proof and certificate audits; registration was released after the 11:05 checkpoint was saved. **The abstract graph theorem is not an algebraicity counterexample.**

## Exact lattice and monodromy calculation

Let (D=\operatorname{diag}(1,2)). On (H_1(A)\oplus H_1(\widehat A)), with the second summand in its dual integral basis, put

\[
 E=\begin{pmatrix}0&D\\-D&0\end{pmatrix},\qquad
 \Omega=\begin{pmatrix}E&I_4\\-I_4&-2E^{-1}\end{pmatrix}.
\]

The principal polarization has determinant one. The type-(1,2) construction and positivity are those already treated in C.4t. For a symmetric (B) such that (D^{-1}B) is integral, the nilpotent monodromy on (A) sends its second two-dimensional block to its first by (D^{-1}B); on the dual it is the negative transpose. In the weight-zero ordering ((a^*_{\widehat A},b_A)), the polarized monodromy form is

\[
 Q(B)=\begin{pmatrix}2D^{-1}BD^{-1}&D^{-1}B\\BD^{-1}&B\end{pmatrix}.
\]

Take (B_1=\operatorname{diag}(1,0)), (B_2=\operatorname{diag}(0,2)), (B_3=2\mathbf1_{2\times2}). Then (Q(B_s)=L_s^tL_s), where the six rows of (L) are

\[
 (1,0,1,0),(1,0,0,0),(0,1,0,1),(0,0,0,1),
 (2,1,1,1),(0,0,1,1).
\]

The quotient map is

\[
 R=\begin{pmatrix}-1&-1&-1&0&1&0\\-1&1&0&-1&0&1\end{pmatrix}.
\]

It gives a split exact sequence (0\to\mathbb Z^4\xrightarrow L\mathbb Z^6\xrightarrow R\mathbb Z^2\to0). Every two-row block (L_s) is onto. These facts and the three monodromy formulas are checked exactly in the final certificate.

## Common orthogonal splitting gives a strict profile identity

Work over \(\Lambda=\mathbb Z_{(2)}\). In a hypothetical common orthogonal graph splitting of level (d), positivity forces a color-(s) projected coedge to have the form (L_s^t v_e), with (v_e\in\Lambda^2). The Gram identity is \(\sum_{e\in E_s}v_ev_e^t=dI_2\). If \(\beta\) is the common integral retraction, the profile map putting (v_e) in block (s) satisfies the stronger identity

\[
                  \Phi(h)=dL\beta(h)\qquad(h\in H_1(G,\Lambda)).
\]

The retraction is indispensable. Prescribing the Gram matrices for an embedding alone does not imply this identity.

## Discovery computations and the all-level repair

The necessary finite graph congruences modulo two are consistent. Modulo four, the odd-level congruences are inconsistent. A simple dual vertex function is

\[
                         f(x,y)=x-x^2+y^2-2xy\pmod4.
\]

The initial unrefined calculation weights the first flow coordinate by (f), with the corresponding quadratic Gram terms. It forces (d) even. Retaining the full level-two cycle-profile condition on \(\mathbb Z^6/(2L\mathbb Z^4+4\mathbb Z^6)\) also gives an inconsistency. The retained exploratory scripts and outputs are:

- `code/check_correlated_monodromy.py`, `output/check_correlated_monodromy.json`: exact Hermite-normal-form tests; 4 vertices/20 edges modulo two are feasible, while 16 vertices/368 edges modulo four are infeasible.
- `code/check_correlated_even_level.py`, `output/check_correlated_even_level.json`: exact two-bit row reduction for level (2\bmod4), with 256 vertices, 5888 edges and 1033 equations; infeasible. Fresh run at 10:49:49.477974 UTC, runtime 0.227541226 seconds.
- `code/derive_correlated_certificate.py`, `output/derive_correlated_certificate.json`: an independently evaluable cubic Boolean-coordinate certificate for that second system, checking all its edge types. It is retained as discovery evidence, not used in the final topological proof.

The final proof avoids testing higher levels. Axis subdivision preserves a *two-component* flux, even though it loses proportionality between the flux and the direction of an individual axis step. This is repaired by retaining a full (2\times2) profile matrix for each block. Coordinate rounding is homotopic to the identity and preserves block support. Surjectivity of (L_s) lets us isolate every matrix column in a genuine closed chain, so every block profile matrix is preserved exactly. At an internal vertex of a coarse axis subdivision, surjectivity of (L_s) forces the two-component flux to be constant. Collapsing (2^j) consecutive edges therefore divides all profile matrices by (2^j), where (j=v_2(d)).

The resulting graph has vertices \(\mathbb Z^6/(L\mathbb Z^4+4\mathbb Z^6)\simeq(\mathbb Z/4)^2\) and block profile matrices congruent to the same odd scalar (d'I_2). The function (f) works for arbitrary two-component axis flux: block one contributes the sum of all four profile entries, block two contributes zero, and block three contributes twice its entry ((2,1)). Closure gives (0=2d'\pmod4\), impossible. The typed proof gives every step, including finite integer refinement of 2-integral coefficients.

The final small certificate is `code/check_correlated_graph_identity.py`, with output `output/check_correlated_graph_identity.json`. It checks all 192 vertex/axis/basis-flux possibilities, lattice minors, the principal form determinant and all three monodromy forms. Fresh run: 11:02:35.672432 UTC; runtime: 0.012413546 seconds. The all-level descent is a proof, not an extrapolation from these finite computations.

## Opened primary source and normalization

Engel, P., de Gaay Fortman, O., & Schreieder, S. (2026). *Matroids and the integral Hodge conjecture for abelian varieties*, arXiv:2507.15704v3. The current primary HTML was opened and the exact passages read at <https://arxiv.org/html/2507.15704v3>:

- Lemma 2.13, especially item (1) and its proof: given the common strict semistable curve family and an odd minimal-class multiple (m), the natural (f^\vee) embedding restricts each graph form to **(m) times** the abelian monodromy form. The current v3 HTML includes this multiplier. Parent noticed that an older 7 August 2025 PDF omits it in the displayed statement; the versions must not be silently conflated.
- Definition 4.6, Proposition 4.5, Theorem 4.10 and Lemma 4.12: the arbitrary-level geometric construction in this source is stated for regular rank-one matroidal families and uses a strict (H)-nodal ambient extension and admissible colored resolutions.
- Lemmas 6.8--6.13 and Proposition 6.14: the coordinate rounding and homotopy mechanism. The present proof explicitly supplies the new block-matrix adaptation, rather than applying the regular-matroid theorem outside its stated scope.

Opened web records for this session include `turn490972227view0`, `turn541194960view0`, `turn531947125view0`, `turn531947125view1`, `turn810961551view1`, `turn810961551view2` and `turn410848045view0`. The existing bibliography key `cyEngelFortmanSchreieder2026` is reused. That entry records the source's conflicting version-header and manuscript dates transparently.

## Geometric transfer remains an independent gate

Lemma 2.13 itself has no rank-one hypothesis, but it presupposes a strict semistable curve family over the common polydisc and the compatible morphism to the abelian family. Theorem 4.10 does not currently supply this for the correlated rank-two cone. Repeated-color local degenerations can be nearly nodal rather than the exact (H)-nodal models in Proposition 4.5; the preservation of a common three-color graph through alteration and resolution has not been established here. The abstract result therefore does **not** yet imply that (P^2/2) is nonalgebraic, or that the type-(1,2) abelian surface is not an actual Jacobian-product summand.

Parent has read the complete abstract proof and independently checked the block rounding and the modulo-four finite differences. A second independent peer audit has been requested. Parent also read the full 192-case certificate. The source, proof and computation events are in the canonical C4_correlated_graph_CHECK_EVENTS.tsv. Main-gate movement is explicitly not claimed.
