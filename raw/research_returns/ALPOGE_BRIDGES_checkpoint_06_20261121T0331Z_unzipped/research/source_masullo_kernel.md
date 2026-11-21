# Actual-kernel investigation: Masullo §12.3

Run: /root/source_and_masullo, within ALPOGE_BRIDGES. Model: GPT-6 Astra Pro. Effort: not exposed. Investigation began 2026-11-21 00:04:02 UTC. The complete statements and proofs are in **source_masullo_kernel.tex**, Findings F-SM-18–22.

## What is now proved

The investigation found a specific defect in the proposed orbital indentation and obtained two concrete repairs. It also proves that, once a valid indentation and the actual spectral trace-class input are supplied, the diagonal shell sum has a direct \(L^1\) domination argument. The remaining difficulty is the identification of the resulting global pieces with the manuscript's separately constructed local operators.

The operators considered are exactly

\[
S_\phi=A(\phi)P_a^{\mathrm{spec}},\qquad
T_{\rho,\phi}=M_\rho A(\phi)P_a^{\mathrm{geom}}
\]

on \(H=W_I^s(C_F)=L^2(C_F,w_{I,s}d\mu)\). Their source locators are Definition 10.4.1.1, p. 456; Theorem 10.4.2.8, pp. 463–464; and equations (10.4.3.48)–(10.4.3.50), pp. 473–474. The bound in F-SM-18 is conditional on this actual \(S_\phi\) being trace class and on the stated kernel identification. The full earlier nuclearity argument was not independently rebuilt in this investigation.

## 1. The missing convergence can be sharply separated from kernel identification

For any trace-class \(S\), the canonical trace density is the unique \(d_S\in L^1\) characterized by

\[
\operatorname{Tr}(M_fS)=\int f\,d_S,\qquad \|d_S\|_1\leq\|S\|_1.
\]

F-SM-18 proves this directly by a singular-value expansion and proves trace-norm-to-\(L^1\) contractivity. Since the actual geometric kernel is the convolution kernel minus the spectral kernel, its trace-density diagonal for \(\phi(1)=0\) is \(-d_{S_\phi}\). This gives a single integrable majorant for every bounded norm cutoff. Agreement with the manuscript's pointwise averaged diagonal still requires its stated trace-diagonal regularity; that requirement is not concealed.

For a genuine normalized indentation \(b\), the two-variable lifting weights satisfy

\[
\omega_b(x,h)=\sum_r b(r^{-1}x)b(r^{-1}h^{-1}x)\geq0,
\qquad \sum_h\omega_b(x,h)=1.
\]

An increasing shell exhaustion therefore gives a tail probability \(\beta_N(x)\in[0,1]\) tending to zero. The exact remaining absolute diagonal mass is bounded by

\[
\int_D |d_{S_\phi}(\pi x)|\,\beta_N(x)\,d\mu_D(x)\longrightarrow0.
\]

The bound is uniform over all cutoffs of absolute value at most one. In fact the \(L^1\) norms of the shell densities sum to exactly the norm of the full density. Thus Fubini and shell summation follow without a new Hilbert–Schmidt estimate for every piece.

For a proposed operator realization on a common Hilbert space, the corresponding stronger target is

\[
\|E_N\|_1
=\inf_{E_N=U_NV_N}\|U_N\|_2\|V_N\|_2\longrightarrow0.
\]

F-SM-18 proves the factorization identity using polar decomposition. It is equivalent to trace-norm convergence, not necessary for a scalar trace identity alone. It also gives the complete counterexample showing why Hilbert–Schmidt convergence alone is insufficient: \(N^{-1}\) times a rank-\(N\) projection has Hilbert–Schmidt norm tending to zero while its trace remains one.

Theorem 11.1.2.1, pp. 480–483, describes the intersection of closed carving subspaces and special theta-function limits. It does not state the required common-space local-operator realization or a trace-norm remainder estimate. The precise unproved step is therefore smaller than an unspecified convergence concern: the correctly lifted diagonal pieces must be shown to be the diagonal densities of the advertised \(S\)-local and orbital operators, with the correct transports and cutoff limits.

## 2. The printed orbital indentation is identically zero

Equation (11.3.2.2), p. 495, proposes the scalar-valued function

\[
U(x,y)=\sum_{\xi\in F^\times}\int_{E_F^1}
1_{\tau(\mathbb R_{>0})}(\xi gx)
1_{\tau(\mathbb R_{>0})}(\xi gy)\,d\mu_1(g).
\]

The differential is implicit in that displayed definition; its immediately adjacent orbital trace formulas explicitly use the ordinary Haar measure \(d\mu_1\). The source calls this a piecewise-constant function. Its introductory discussion, pp. 21–22, allows ordinary indicators of fundamental domains; it does not introduce Dirac distributions in this formula.

The source itself fixes the relevant space and measure. Definition A.2.3.6, p. 549, equation (A.2.3.14), makes \(E_F^1\) a subset of the norm-one ideles. For \(\mathbb Q\),

\[
E_{\mathbb Q}^1=\{1\}_\infty\times\widehat{\mathbb Z}^{\,\times}.
\]

Definitions A.3.2.1–2, pp. 559–560, give its ordinary probability Haar measure; counting measure is assigned to \(\mathbb Q^\times\). The compact unit group is infinite and its Haar measure has no atoms.

For fixed \(x,\xi\), the condition \(\xi gx=\tau(t)\) forces \(t=|x|\), and thus fixes at most one \(g\). Every integral in the formula is zero. F-SM-19 proves that the proposed function is identically zero, so it cannot satisfy the source's normalization for an indentation.

The contradiction with the stated orbital formula is explicit. Take \(F=\mathbb Q\), the trivial character, \(S=\{\infty\}\), \(a=1/2\), \(s=4\), and any positive strip half-width. Let \(h\in C_c^\infty((3/2,5/2))\) satisfy \(h(2)=1\), and let \(\phi(u,t)=h(t)\). All the theorem's class-number, ramification, finite-unit invariance and support assumptions hold. Only \(\pi_2^{-1}\) contributes to the right-hand prime-power sum, so that side is

\[
\frac{\log2}{\mu_2(\mathbb Z_2^\times)}=\log2>0.
\]

The literal indented left side is zero. This disproves the formula with its stated ordinary-function interpretation. It does not disprove a future distributional or disintegrated replacement, and it makes no adverse claim about the adopted Alpöge theorem.

## 3. Two actual repairs

F-SM-20 constructs the valid indentation

\[
Z=\mathbb R_{>0}\times\widehat{\mathbb Z}^{\,\times}
\subset\mathbb A_{\mathbb Q}^\times,\qquad b=1_Z.
\]

The set is an open and closed fundamental domain for \(\mathbb Q^\times\), and its quotient map is a homeomorphism. Every idele has a unique rational multiple in \(Z\), proving the required normalization. Its two-variable lift satisfies \(b^\Delta(x,qx)=1_{q=1}\) for \(x\in Z\). Therefore the outside-shell diagonal tails vanish, but the part labelled \(S\) still contains the entire original global spectral diagonal. A valid indentation alone does not turn that kernel into the independently defined \(S\)-local Paley–Wiener kernel.

The second repair is a genuine compact averaging, rather than averaging an indicator of a null section. For \(K=\widehat{\mathbb Z}^{\,\times}\), let \(Jf(u,t)=f(t)\) and \(J^*F(t)=\int_KF(u,t)\,du\). Then \(E=JJ^*\) is an orthogonal projection. For the stated compact-invariant test functions and norm cutoffs, the actual projections commute with \(E\), and

\[
T_{\rho,\phi}=ET_{\rho,\phi}E,\qquad S_\phi=ES_\phi E.
\]

This uses the actual closed invariant geometric subspace in Definition 10.4.1.1 and Lemma 10.4.1.2, p. 456. A trace-class operator of this form has exactly the same trace and trace norm as \(J^*TJ\). Its compressed kernel is obtained by integrating its genuine Hilbert–Schmidt kernel over \(K\times K\), with the stated norm contraction. F-SM-20 gives the complete proof.

The remaining task is an intertwining and kernel-identification theorem relating this compressed global operator to the \(S\)-local operator in Theorem 12.4.1.1, pp. 514–519. The identities just proved do not supply that theorem.

## Sources and checks

Masullo, A. (2026). *The music of the primes* [supplied manuscript]. https://math216.wordpress.com/wp-content/uploads/2026/11/the-music-of-the-primes.pdf . Primary retrieval refs from the earlier source verification: turn575499152view2 and turn466669506search3.

Exact pages inspected in this investigation: pp. 21–22, 456, 463–464, 473–474, 480–483, 491–496, 498–514, 519–520, 549, and 559–560. The p. 495 indentation was additionally read from a rendered image, saved as **source_review_images/masullo_orbital_495.png**. Context renders are **masullo_indent_context_504.png**, **masullo_indent_context_549.png**, and **masullo_indent_context_560.png** in the same directory.

F-SM-18–22 were each read in their entirety after drafting. These are complete drafter proof checks, conditional where explicitly stated. Parent independently read all five proofs F-SM-18–22 in full and reported PASS, with separate check events. The source checks included the original p. 495 formula, p. 549/559–560 definitions, p. 514–515 and 519–520 operator formulas, and the F-SM-13 explicit-formula normalization. No formal kernel certification or reconstruction of the full 940-page manuscript is claimed.

## 4. Two specific repairs are now excluded quantitatively

F-SM-21 constructs a real test h supported in (1.5,2.5) with h(2)=1 and both the archimedean functional A0(h) and the combined pole moment P(h) equal to zero. The two constraints are solved by adding two bumps supported away from2; the coefficient matrix is invertible because the ratio of the two integral densities is strictly decreasing. The fully proved numerical explicit formula then gives the global zero trace exactly log(2)/sqrt(2), while the unchanged S={infinity} local Paley–Wiener trace limit is zero under its stated source formula. Therefore, conditional on the manuscript's global and local operator trace identifications, no trace-preserving transport can make the naive remaining-kernel difference tend to zero in trace norm: its liminf is at least log(2)/sqrt(2). This refutes that unchanged-kernel replacement, not an assembly retaining the required prime contribution.

F-SM-22 treats the proposed multiplicative Dirac interpretation exactly. For the actual compact-invariant cutoff operator, F-SM-20 gives T=E_K tensor B, with E_K the rank-one constant projection. Multiplying its radial kernel by the compact diagonal Dirac kernel changes the operator to identity tensor B. Whenever B is nonzero this is not compact, as an infinite orthonormal sequence of compact characters gives orthogonal images of fixed positive norm. In the conditional operator setting of F-SM-21 the positive trace limit ensures B is nonzero for sufficiently advanced cutoffs. Restoring a compact-isotypic projection restores the original global operator; it does not identify it with the local PW kernel.
