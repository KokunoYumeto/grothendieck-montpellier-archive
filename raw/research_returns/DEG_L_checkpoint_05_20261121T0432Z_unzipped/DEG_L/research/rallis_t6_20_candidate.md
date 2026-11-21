# Candidate T6.20: exact Chow cancellation and simultaneous input/output transport

Status: author, root and bounds whole-proof reviews passed; promoted as DEG-L.T6.20. This file retains the candidate history. Date: 2026-11-21. Actor: GPT-6 Astra Pro; effort not exposed; /root/rallis_t6. This addresses intrinsic Chow normalization, which must be distinguished from T6.19's denominator of a presentation in unscaled outputs.

## Proposed theorem T6.20

Work over the complex numbers and fix the Galois CM coefficient field \(E\). All eigenvectors below are \(E\)-coefficient Betti vectors, not polarization-unit vectors obtained by arbitrary complex rescaling. For four factors let
\[
 h_i:A_{i,0}\longrightarrow A_i,\qquad
 g_i:B_{i,0}\longrightarrow B_i
\]
be actual \(E\)-linear isogenies between fixed-type CM abelian varieties. Write \(h=\prod_i h_i\), \(g=\prod_i g_i\), and let \(z_0=f_{0*}[Y]\) for fixed actual maps from a smooth projective surface to \(A_0=\prod_iA_{i,0}\). Choose nonzero eigenvectors with
\[
 h_i^*\alpha_i=\lambda_i\alpha_{i,0},\qquad
 g_i^*\beta_i=\mu_i\beta_{i,0},\qquad
 \lambda_i,\mu_i\in E^\times.
 \tag{T20.1}
\]
Assume every scalar conjugate of each \(\alpha_i\otimes\beta_i\) has Hodge type \((1,1)\), and similarly for the reference vectors. Choose the uniquely determined birigidified divisor-correspondence classes
\[
 D_i\in\operatorname{CH}^1(A_i\times B_i)\otimes E,
 \qquad
 D_{i,0}\in\operatorname{CH}^1(A_{i,0}\times B_{i,0})\otimes E
\]
with these pure mixed Betti classes. Let \(K=\prod_iD_i\), \(K_0=\prod_iD_{i,0}\), with the usual pullbacks to the full products. Assume
\[
 k_0=\int_Y f_{1,0}^*\alpha_{1,0}\wedge\cdots\wedge
                         f_{4,0}^*\alpha_{4,0}\ne0,
 \qquad C_0=K_{0*}z_0/k_0.
\]
Set
\[
 \Lambda=\prod_i\lambda_i,\qquad M=\prod_i\mu_i,
 \qquad k_h=\Lambda k_0,\qquad
 C_{A,B}=K_*h_*z_0/k_h.
\]
All surface pushforwards retain their actual multiplicities.

### A. Exact cancellation and simultaneous transport

There are identities in Chow groups with \(E\) coefficients
\[
 (h_i\times g_i)^*D_i=\lambda_i\mu_iD_{i,0},
 \tag{T20.2}
\]
\[
 g^*C_{A,B}=M C_0,
 \qquad
 C_{A,B}=\frac{M}{\deg g}\,g_*C_0.
 \tag{T20.3}
\]
Every input factor \(\lambda_i\) cancels. In particular, at fixed output \(B=B_0\), with fixed output eigenvectors and \(g=1\),
\[
 C_{A,B_0}=C_0.
 \tag{T20.4}
\]
This extends T6.5 from clearing integers to arbitrary actual \(E\)-linear input isogenies, provided that the source surface maps and output are fixed and the kernels are the pure birigidified classes stated here. Coefficientwise traces of the normalized cycle are then fixed rational Chow classes and have fixed intrinsic rational denominators. A growing index of the unscaled outputs, as in T6.19, does not contradict (T20.4).

### B. Genuine dual outputs and the direction of the dual isogeny

Suppose \(B_i=A_i^\vee\), \(B_{i,0}=A_{i,0}^\vee\), and \(D_i\), \(D_{i,0}\) are the selected \(E\)-eigencomponents of the normalized Poincare bundles. Normalize \(\beta_i\), \(\beta_{i,0}\) by these Poincare components, so their pure classes are exactly \(\alpha_i\otimes\beta_i\) and \(\alpha_{i,0}\otimes\beta_{i,0}\). Then the actual dual isogeny points in the reverse direction:
\[
 q=\prod_i h_i^\vee:B=\prod_iA_i^\vee
                      \longrightarrow B_0=\prod_iA_{i,0}^\vee.
\]
The exact formulas are
\[
 (h_i^\vee)^*\beta_{i,0}=\lambda_i\beta_i,
 \qquad
 K_*h_*z_0=q^*(K_{0*}z_0),
 \tag{T20.5}
\]
\[
 C_{A,B}=\Lambda^{-1}q^*C_0,
 \qquad
 q_*C_{A,B}=\frac{\deg q}{\Lambda}\,C_0.
 \tag{T20.6}
\]
Thus the moving-output problem is an actual isogeny pullback followed by a specified coefficient division. It is not a residual input-period ambiguity.

### C. Uniform denominator for factorwise integral output tensors

There is a useful construction that does not require varying the input factors at all. Fix integral \(\mathcal O_E\)-coefficient input eigenvectors \(\alpha_{i,0}\), fixed actual \(f_{i,0}\), and their nonzero period \(k_0\in\mathcal O_E\). Let the output CM factors \(B_i\) vary arbitrarily within the required fixed CM types. For every choice of integral \(\mathcal O_E\)-coefficient output eigenvectors \(\beta_i\) of the opposite types, there exist integral \(\mathcal O_E\)-coefficient birigidified divisor kernels on \(A_{i,0}\times B_i\) with class \(\alpha_{i,0}\otimes\beta_i\).

Put
\[
 Z_B=K_{B*}z_0\in\operatorname{CH}^2(B)\otimes\mathcal O_E,
 \qquad C_B=Z_B/k_0.
\]
For every fixed \(a\in\mathcal O_E\), the rational Chow class
\[
 \Gamma_B(a)=\operatorname{Tr}_{E/\mathbf Q}(a C_B)
\]
has an integral multiple with the same denominator for all output lattices:
\[
 N_0\Gamma_B(a)\in\operatorname{im}
 \bigl(\operatorname{CH}^2(B)\longrightarrow
                 \operatorname{CH}^2(B)\otimes\mathbf Q\bigr),
 \qquad
 N_0=|N_{E/\mathbf Q}(k_0)|.
 \tag{T20.7}
\]
A fixed finite set of fractional coefficient weights only adds one fixed clearing integer. This proves a genuine uniform Chow denominator for these **factorwise integral eigenvector tensors**. It does not by itself make their rational Galois-orbit lattice saturated in integral cohomology or give a degree bound for the signed cycles.

### D. Exact denominator of the displayed dual-pullback representative

Choose a finite representative
\[
 C_0=\sum_{\ell=1}^u c_\ell[Z_\ell],\qquad c_\ell\in E,
 \tag{T20.8}
\]
with distinct integral subvarieties \(Z_\ell\subset B_0\). In the dual situation (B), a representative of \(\Gamma_B(a)\) has coefficient
\[
 \operatorname{Tr}_{E/\mathbf Q}(a c_\ell/\Lambda)
 \tag{T20.9}
\]
on every irreducible component of \(q^{-1}(Z_\ell)\). Therefore the exact common denominator of this displayed rational cycle is the least common multiple of the denominators of (T20.9).

Let \(\mathfrak C=\sum_\ell\mathcal O_Ec_\ell\) and let \(\mathfrak D\) be the different of \(E/\mathbf Q\). The least positive integer clearing this representative simultaneously for every \(a\in\mathcal O_E\) is the positive generator of
\[
 (\Lambda\mathfrak D^{-1}\mathfrak C^{-1})\cap\mathbf Z.
 \tag{T20.10}
\]
Its exponent at a rational prime \(p\) is
\[
 \max\left(0,\max_{\mathfrak p\mid p}
 \left\lceil\frac{v_{\mathfrak p}(\Lambda)
                      -v_{\mathfrak p}(\mathfrak D)
                      -v_{\mathfrak p}(\mathfrak C)}{e_{\mathfrak p}}\right\rceil\right).
 \tag{T20.11}
\]
These are exact representative denominators and hence upper bounds for the intrinsic Chow denominator. Rational equivalence or divisibility in the Chow group may reduce the latter; no converse lower bound is asserted.

## Proof

### Birigidification makes the entire divisor class faithful

For complex abelian varieties \(U,V\), write \(\operatorname{Pic}^{\mathrm b}(U\times V)\) for divisor-correspondence classes trivialized along the two zero axes. Its first Chern class is injective. Indeed, a class in its kernel lies in \(\operatorname{Pic}^0(U\times V)\), and
\[
 \operatorname{Pic}^0(U\times V)
 =\operatorname{pr}_U^*\operatorname{Pic}^0(U)
  \oplus\operatorname{pr}_V^*\operatorname{Pic}^0(V).
\]
Restriction to the two axes recovers these two summands, so birigidification makes both trivial. Equivalently, the divisor-correspondence group is \(\operatorname{Hom}(U,V^\vee)\), and the induced map on first cohomology detects a homomorphism. This is the correspondence/biextension identification of SGA7 I, Expose VII, Examples 2.9.5--2.9.6. Tensoring the injective first Chern class map with the characteristic-zero field \(E\) preserves injectivity.

Pullback by a homomorphism in either argument preserves birigidification. The first Chern class of the left side of (T20.2) is, in the full \(E\)-coefficient Betti space,
\[
 h_i^*\alpha_i\otimes g_i^*\beta_i
   =\lambda_i\mu_i(\alpha_{i,0}\otimes\beta_{i,0}).
\]
This is not merely an equality after evaluating one complex embedding. Applying the just-proved injectivity gives (T20.2) in the entire birigidified Picard group with \(E\) coefficients, and hence in \(\operatorname{CH}^1\otimes E\).

### Projection and flat base change

Let \(p_A,p_B\) denote the two projections from \(A\times B\). By definition,
\[
 K_*h_*z_0=(p_B)_*\bigl(p_A^*h_*z_0\cdot K\bigr).
\]
Flat base change along \(g\) and then along the product square for \(h\), followed by the projection formula, gives
\[
 \begin{aligned}
 g^*(K_*h_*z_0)
 &= (K|_{A\times B_0})_*h_*z_0\\
 &= ((h\times g)^*K)_*z_0\\
 &=\Lambda M\,K_{0*}z_0.
 \end{aligned}
 \tag{T20.12}
\]
Here the first kernel is the pullback by \(1\times g\), not a literal restriction to a subvariety. All isogenies in characteristic zero are finite etale, hence flat, so these are ordinary Chow pullbacks and proper pushforwards. The product of the four identities (T20.2) proves the last equality. The period scales by \(\Lambda\), proving the first equation of (T20.3). Applying \(g_*\) and using \(g_*g^*=(\deg g)\operatorname{id}\) proves the second. This also proves (T20.4).

The fixed rational Chow denominator in (T20.4) is concrete. Choose a finite cycle representative of \(\operatorname{Tr}(a C_0)\) and clear its finitely many rational coefficients once. The same representative on the same output works for every input isogeny. This is stronger than a bound on the selected period and is not contradicted by the nonsaturation of an unscaled subgroup of Chow classes.

### Duality and the reversed map

For a homomorphism \(h_i:A_{i,0}\to A_i\), the normalized Poincare bundles satisfy
\[
 (h_i\times1)^*\mathcal P_{A_i}
   \simeq (1\times h_i^\vee)^*\mathcal P_{A_{i,0}}.
 \tag{T20.13}
\]
This is the defining universal property of the dual homomorphism. The selected \(E\)-eigencomponents agree because \(h_i\) is \(E\)-linear. In Betti cohomology, the selected equality reads
\[
 \lambda_i\alpha_{i,0}\otimes\beta_i
   =\alpha_{i,0}\otimes(h_i^\vee)^*\beta_{i,0},
\]
so it gives the first identity of (T20.5). Birigidified Chern-class injectivity also gives (T20.13) for the selected divisor components themselves. These components are legitimate \(E\)-coefficient divisor classes even when their projection from the integral Poincare class has denominators. This part does not assert their integrality.

Taking the fourfold product of (T20.13), pulling it against \(z_0\), and applying flat base change on the output gives the second identity of (T20.5). Divide by \(k_h=\Lambda k_0\) to obtain the first identity of (T20.6). Its pushforward follows from \(q_*q^*=(\deg q)\operatorname{id}\). In particular the scalar in (T20.6) is \(\Lambda\), not an assumed field norm or an arbitrarily chosen complex metric period.

### Integral factorwise tensors require only one fixed period denominator

For part (C), each pure mixed class \(\alpha_{i,0}\otimes\beta_i\) belongs to integral cohomology tensored with \(\mathcal O_E\), and all its scalar conjugates are of type \((1,1)\). The integral descent argument of T6.7 and T6.18 puts it in the saturated mixed Neron--Severi lattice tensored with \(\mathcal O_E\). Passing to the birigidified representative removes axis restrictions and introduces no coefficient denominator. Products and proper pushforward preserve integral \(\mathcal O_E\)-coefficient cycles, proving that \(Z_B\) has the stated coefficients.

For a nonzero algebraic integer \(k_0\), the element \(N_0/k_0\) is an algebraic integer: up to the sign of its rational norm it is the product of the other scalar conjugates. Consequently
\[
 N_0\Gamma_B(a)
   =\operatorname{Tr}_{E/\mathbf Q}
       \bigl(a(N_0/k_0)Z_B\bigr)
\]
is an integral cycle class, proving (T20.7). This argument is uniform over the target lattices and does not use a bound for an isogeny degree. It proves uniform division for the explicitly stated factorwise integral tensors; primitivity in a larger rational orbit lattice is a separate question.

### The explicit representative and the trace dual

A finite etale pullback of an integral subvariety is generically reduced; each irreducible component has multiplicity one in the flat pullback cycle. Every component maps onto the original subvariety. Thus the inverse images of distinct \(Z_\ell\) have no common irreducible components. Apply (T20.6) to the representative (T20.8) and then trace the coefficients. This gives exactly (T20.9), with no cancellation among supports of different \(Z_\ell\).

An integer \(D>0\) clears these coefficients for all \(a\in\mathcal O_E\) if and only if
\[
 D c_\ell/\Lambda\in\mathfrak D^{-1}
 \quad\hbox{for every }\ell.
\]
Equivalently, \(D\mathfrak C\subseteq\Lambda\mathfrak D^{-1}\). Since \(\mathfrak C\) is an invertible fractional maximal-order ideal, this is precisely \(D\in\Lambda\mathfrak D^{-1}\mathfrak C^{-1}\). Taking its intersection with the integers proves (T20.10); comparing valuations gives (T20.11). The denominator of a particular representative always clears its Chow class. The proof supplies no reason that a rationally equivalent representative cannot have a smaller denominator. This completes the proof. QED.

## Comparison with the fixed-K Weil determinant plane

In B23 the coefficient space is a rank-one module over an imaginary quadratic field \(K\), hence a two-dimensional rational Weil plane. For an \(E\)-linear isogeny with scalar \(\alpha\), the pullback scalar on that determinant line is
\[
 s=N_{E/K}(\alpha).
\]
If \(\nu\) is the homology covolume ratio, its degree is \(\delta=\nu^{-1}s\bar s\). A normalization compatible with the chosen target determinant generator therefore has the same general form
\[
 C_A=\frac{s}{\delta}\,h_*C_0
     =\frac{\nu}{\bar s}\,h_*C_0.
 \tag{T20.14}
\]
This is the formal comparison of scalar conventions; it does not identify B23's determinant plane with the four-factor switch orbit. B23's common integral pushforward content \(\bar{\mathfrak j}\) records the image before saturation. Multiplication by \(s/\delta\) can leave that integral image, and a claim that the result is integral in Chow would require an additional divisibility argument. Conversely, the image index alone does not prove that the normalized class has an unbounded intrinsic denominator.

For the four separate CM factors, the scalar \(M\) in (T20.3) is a product of four selected embedding eigenvalues; it is generally not \(N_{E/K}(\alpha)\). Its full rational Galois orbit has dimension \([E:\mathbf Q]\), rather than two. Any comparison with a generic \(K\)-Weil target must retain the actual correspondence and its integral lattice map.

The positive conclusion is precise: all varying input isogenies and their period normalization cancel in Chow, and direct kernels with fixed integral input vectors give a uniform denominator for every factorwise integral output tensor. The unresolved moving-output primitive question is whether the integral orbit classes needed for the intended Weil target can be represented by these tensors with uniformly controlled saturation, or whether their normalized isogeny pullbacks have additional Chow divisibility. Neither a metric Rallis norm nor scalar trace contraction settles that question.

## Primary sources and exact locators

- Grothendieck, SGA7 I, Expose VII, Example 2.9.5, printed p.175 (PDF p.180; VII43), and Remark 2.9.6, printed p.176 (PDF p.181; VII44), identify birigidified line bundles, biextensions and divisor correspondences \(\operatorname{Hom}(U,V^\vee)\). Original scan: <https://library.slmath.org/nonmsri/sga/sga/pdf/sga7-1.pdf>. This agent independently read both original page images in this phase.
- Milne, *Abelian Varieties*, v2.00, Chapter I, Poincare universal property and Remark 8.7, printed p.37, and the opening paragraph of Section 9, printed p.41. The latter explicitly states (T20.13) and defines the dual homomorphism. <https://www.jmilne.org/math/CourseNotes/AV.pdf>.
- Stacks Project, Lemma 42.15.1 (tag 02RG) and Lemma 42.15.2 (tag 02RH), in Section 42.15 (tag 02RF), state flat base change and finite locally free push-pull. <https://stacks.math.columbia.edu/tag/02RF>. Exact statements and complete short proofs read.
- Stacks Project, Lemma 43.22.1 (tag 0B10), supplies the flat proper projection formula. <https://stacks.math.columbia.edu/tag/0B10>. Statement and full displayed proof read; on Chow groups the usual moving/intersection formalism gives the formula used above.
- Conrad, *The Different Ideal*, Definition 3.2 p.4, Theorems 3.9--3.10 p.8 and Definition 4.1 p.9, supplies the trace-dual convention in (T20.10). <https://kconrad.math.uconn.edu/blurbs/gradnumthy/different.pdf>. The denominator calculation itself is proved here.

## Check status

The entire saved proof was read by the author, root and bounds; all reviews passed before promotion. Source checks are recorded separately. No local compilation is claimed.
