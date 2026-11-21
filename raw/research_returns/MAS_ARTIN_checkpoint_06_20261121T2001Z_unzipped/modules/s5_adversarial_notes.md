# Adversarial review of the complete S5 Fourier argument

**Date:** 2026-11-21. **Reviewer:** GPT-6 Astra Pro, /root/s5_audit; effort inherited and not externally exposed. **Conclusion:** the complete implication MA-S5-001/004 → MA-LD-001 → MA-FQ-001–004 passes this independent adversarial review under the exact stated hypothesis \(\mathcal R_B\). No counterexample satisfying all the combined premises was found. The checks below identify the precise failures of several genuine or natural candidate examples, rather than treating failure to find a counterexample as a proof. The proof is the chain of complete arguments in the cited modules.

The review reread all four FQ proofs together, the complete written LD-001 proof, the original S5 notation and comparison argument, and the complete written S5-004 Tauberian argument. It challenged the interfaces against the primary Calegari and Booker definitions and against explicit nonperiodic crystalline examples. The original independent proof reviews and this adversarial review are distinct recorded events.

## 1. The same actual meromorphic quotient is used throughout

The order definitions are

\[
\beta=\operatorname{ord}_{1/2}B,\qquad
b=\operatorname{ord}_{1/2}C,\qquad
n=\operatorname{ord}_{1/2}A,\qquad k=\beta-b-n.
\]

The all-prime identity \(B=C L_W\), including the ramified factors, gives

\[
\operatorname{ord}_{1/2}L_W=\beta-b,\qquad
\operatorname{ord}_{1/2}(A/L_W)=n-(\beta-b)=-k.
\]

Thus the height-coordinate divisor of the actual difference datum has \(m_R(0)=-k\). There is no change from the quotient to its inverse when the central order is computed; the later minus sign is the deliberate choice \(a=-m_R\), required by the negative prime sum in Booker's explicit formula.

The archimedean calculation uses more than equality of degrees. Complex conjugation is a double transposition, so \(E=L^{A_5}\) is real. At its two real places the finite-image odd parameter is \(1\oplus\operatorname{sgn}\). The actual symmetric-fourth-power descent has parameter \(1^{\oplus3}\oplus\operatorname{sgn}^{\oplus2}\); its determinant twist is trivial there. Base change from a split real place is the identity on this parameter. The rank-five Artin representation has the same multiplicities because its trace at complex conjugation is one. Consequently the gamma factors, and hence Booker's kernels, cancel exactly. The conductor ratio is a nonvanishing exponential and changes no divisor order.

The finite factor at an exceptional prime is checked in the reciprocal-polynomial convention:

\[
\frac{L_p(\varpi,s)}{L_p(W,s)}
=\frac{P_{W,p}(p^{-s})}{P_{\varpi,p}(p^{-s})}
=\left(\frac{1+p^{-s}}{1-p^{-s}}\right)^2.
\]

Its logarithm is \(4\sum_{j\ {\rm odd}}p^{-js}/j\). In Booker's normalization this gives exactly \(f_R(p^j)=4(\log p)p^{-j/2}\) for odd \(j\), and zero for even \(j\). This verifies both the sign and the factor four used in the prime atoms.

## 2. Critical-line support is established before ordinary Fourier transformation

The hypothesis \(\mathcal R_B\) says that the entire quadratic Hecke function \(B\) has no real zero in \((0,1)\setminus\{1/2\}\). The positive Euler product and the audited Landau argument place the possible real pole of the comparison quotient at \(1/2\), giving \(k\ge0\) and the convergence half-plane \(\operatorname{Re}s>1/2\). The S5-004 Tauberian step is not a zero-location assumption: it uses the actual pole order and a positive measure to obtain the exceptional-prime size bound.

LD-001 then proves that the actual Euler logarithm is locally absolutely convergent in that open half-plane. Exponentiation is holomorphic and nonvanishing there. The canonical completed factor is nonvanishing there as well; in the present equal-kernel case it is just the conductor exponential, up to normalization. The completed functional equation gives the same assertion on the opposite open half-plane. The full signed divisor is consequently on the critical line. No equality of individual zero orders on that line is inferred.

This order of deductions matters. Applying an ordinary real Fourier transform to a divisor at nonreal height coordinates would be invalid. Here the support has already been proved real. Booker's polynomial total-variation bound and integrality then give a locally finite tempered signed real measure. In particular, no off-line pole, endpoint term or gamma zero has been silently removed.

## 3. A4, its test class, and the continuous correction

Booker's A4 has a minus sign before a sum starting at \(n=1\). In the present convention \(\widehat g(t)=\int e^{ixt}g(x)\,dx\), the exact identity is

\[
\widehat{-\mu}=M_\Omega+B_0,\qquad
B_0=2f_R(1)\delta_0+
\sum_{p\ {\rm bad},\,j\ge1}
\left(f_R(p^j)\delta_{j\log p}
+\overline{f_R(p^j)}\delta_{-j\log p}\right).
\]

The conductor contributes only the displayed atom at zero. There is no residual archimedean continuous density because \(K_R=0\), not merely \(d_R=0\).

The extension from Hermitian compact tests to arbitrary complex compact tests is legitimate: every \(g\) is \(g_1+ig_2\) with both \(g_i(-x)=\overline{g_i(x)}\), and both sides of the asserted distribution identity are complex linear. The subsequent extension to Schwartz tests uses temperedness of all three terms. The good positive measure has polynomial growth by S5-004, while A1 with logarithmic exponent two makes the finitely many bad-prime tails absolutely summable.

Taking

\[
q(t)=-\frac1{2\pi}\int e^{-itx}\,dB_0(x)
\]

therefore gives a bounded continuous function and
\(\widehat{-\mu+q\,dt}=M_\Omega\ge0\). The positive-type calculation retains the reflection and normalization:

\[
\langle-\mu+q\,dt,\psi*\widetilde\psi\rangle
=\frac1{2\pi}\int|\widehat\psi(-x)|^2\,dM_\Omega(x).
\]

No sign condition is imposed on the bad coefficients. Finite total variation is the property that permits their removal by a continuous density.

## 4. The two group topologies do different jobs

The shrinking bump calculation has fixed autocorrelation height at an atom: for \(\phi_\epsilon(t)=\epsilon^{-1/2}\phi(t/\epsilon)\), it is \(\Psi(t/\epsilon)\), not an approximate delta of height \(\epsilon^{-1}\). For any fixed finite set of pair differences, local finiteness isolates the relevant atoms simultaneously. The density \(q\,dt\) contributes \(O(\epsilon)\). The resulting finite quadratic forms prove that the function \(a(t)=-m_R(t)\) is positive definite on the abstract additive real group, equivalently on \(\mathbb R_d\).

This is not an assertion that \(a\) is continuous for the usual real topology. Bochner's representing measure is on the compact character group of \(\mathbb R_d\), and it is not the ordinary Fourier transform of the atomic measure. The GNS proof supplied in FQ-001 verifies this distinction even for the nonmetrizable compact dual.

The bound \(|a(t)|\le a(0)=k\) and integrality give finite range. Cohen's theorem is applied to this discrete locally compact group. Its finite cosets can be dense in the ordinary topology, which is why FQ-002 is necessary. I checked its dense-atom argument explicitly: an inclusion-minimal dense intersection subgroup either avoids an excluded coset completely, or meets it in a coset with nowhere-dense closure. A surviving dense atom cannot lie in a locally finite set. Thus the ordinary lattice-comb conclusion does not assume uniform separation.

Only after that finite-comb representation has been obtained does FQ-003 take the ordinary distributional Fourier transform. A physical translation modulates a reciprocal comb:

\[
\widehat{\sum_{n\in\mathbb Z}\delta_{\alpha n+\beta}}
=\frac{2\pi}{\alpha}
\sum_{m\in\mathbb Z}e^{2\pi i m\beta/\alpha}
\delta_{2\pi m/\alpha}.
\]

It does not translate the reciprocal lattice. Finite singleton terms give a continuous trigonometric-polynomial density, which vanishes because the actual Fourier transform is purely atomic. Each remaining unshifted lattice contains \(\log p\) for at most one rational prime. Bad-prime powers cannot cancel a good-prime atom, by unique factorization. The resulting finiteness of \(\Omega\) contradicts \(k>0\) through the already audited S5 equivalence.

## 5. Candidate counterexamples and their exact failures

### A genuine positive-Euler degree-zero datum

The actual datum for \(\zeta(s)/L(s,\chi_5)\), with the even quadratic character modulo five, has equal gamma kernels and nonnegative logarithmic coefficients. It is the genuine example in LD-003. However its completed quotient has poles at both \(s=0\) and \(s=1\). The denominator is nonzero at these completed endpoints by its functional equation and the usual nonvanishing at one. Thus its height divisor includes nonreal points \(z=\pm i/2\), independently of any conjecture about nontrivial zeros.

Even if both nontrivial divisors were on the critical line, deleting these two poles would change A4 by
\[
h(i/2)+h(-i/2)=\int 2\cosh(x/2)g(x)\,dx.
\]
The Fourier formula for the remaining real divisor would therefore acquire a continuous \(-2\cosh(x/2)\) density. Its positive prime measure is not tempered. Indeed, polynomial mass growth would make every positive Laplace transform converge, so the Euler logarithm would converge locally throughout \(\operatorname{Re}s>1/2\), contradicting the actual pole at one. This is not the tempered positive-prime-plus-finite-measure identity in FQ-001. A hypothesis about the nontrivial zeros cannot remove the completed endpoint poles.

### Ratios of two nontrivial even Dirichlet functions

For \(L(s,\chi_5)/L(s,\chi_{13})\), both individual completions are entire and the kernels again agree. Its coefficient at a prime is
\[
(\chi_5(p)-\chi_{13}(p))\frac{\log p}{\sqrt p}.
\]
For primes \(p\equiv3\pmod{65}\) it is negative, while for \(p\equiv11\pmod{65}\) it is positive. Both progressions contain infinitely many primes by the classical theorem on primes in arithmetic progressions. Therefore the nonnegative-good-prime premise fails outside every finite bad-prime set. Even granting GRH for these functions would not fix this sign failure. The elementary character values were checked directly; the classical nonvanishing and prime-progression theorems are background inputs, not newly reproved here.

### A nonperiodic positive Fourier quasicrystal

Kurasov–Sarnak (2020), equations (39), (41), (43) and Theorem 1, supply
\[
P=1-z_1/3+z_2^2/3-z_1z_2^2.
\]
Choose \(\xi_1=\log2,\xi_2=\log3\), \(A=\xi_1/2+\xi_2\), \(D=\xi_1/2-\xi_2\). Its unit-mass zero set satisfies \(S(t)=3\sin(At)+\sin(Dt)=0\).

Here is a direct matrix test. A nonzero root \(\lambda\) exists between \(\pi/(2A)\) and \(3\pi/(2A)\). Roots are simple since \(|3A\cos(A\lambda)|\ge\sqrt8 A>|D|\). If \(2\lambda\) were also a root, then
\[
0=6\sin(A\lambda)\{\cos(A\lambda)-\cos(D\lambda)\},
\]
which together with \(S(\lambda)=0\) forces \(A/D\in\mathbb Q\), impossible. Hence its mass function has \(a(0)=a(\lambda)=1\), \(a(2\lambda)=0\). The matrix on \(0,\lambda,2\lambda\) gives
\[
(1,-1,1)
\begin{pmatrix}1&1&0\\1&1&1\\0&1&1\end{pmatrix}
(1,-1,1)^T=-1.
\]
It is not positive definite. The bump argument therefore rules out any bounded continuous correction making this measure positive type. Its logarithmic coefficient at \(z_1z_2^4\) is \(8/27\), also giving a nonzero mixed frequency \(\log162\), which is not a prime power.

### A one-prime lattice with central zeros

The tempting normalized Euler function \(F(s)=(1-p^{1/2-s})^{-1}\) has a central vertical pole lattice and only one prime progression. But its logarithm corresponds to \(f(p^j)=\log p\) for all \(j\). This violates Booker's A1, which requires \(f(p^j)(j\log p)^N=O_N(1)\) for every \(N\). Its reciprocal-frequency comb has constant masses and infinite total variation. It cannot be treated as one of the allowed finite-total-variation bad-prime corrections.

These tests give neither a genuine counterexample to FQ-003 nor an arithmetic counterexample to FQ-004.

## 6. A source-level hypothesis check

Calegari's §3 opening contains the sentence that both three and five split in \(E\), although Theorem 1.1 imposes only the condition at five. This additional assertion about three is absent from the theorem's hypotheses. To check whether it hid an assumption, I inspected Sasaki's published Theorem 1, *Documenta Mathematica* 18 (2013), pp.998–999: it requires that five split completely, the representation be totally odd and icosahedral, and each projective decomposition image above five have order two. It has no condition at three. The stipulated Frobenius double transposition supplies exactly those requirements. Thus the stray assertion does not enlarge the family hypotheses used in the construction.

This was a check of the precise statement and its specialization, not a fresh audit of Sasaki's full modularity-lifting proof. Calegari's automorphic construction and its classical functorial inputs remain the explicitly carried published inputs.

## Scope retained

The central equality is closed under \(\mathcal R_B\). This audit supplies no proof of \(\mathcal R_B\) for every extension in the stipulated family, and it supplies no unconditional all-factor GRH. The input \(M\) is sufficient for \(\mathcal R_B\) and supplies the additional Hecke zero-location premises for the latter conclusion. The formal integer-order witnesses from earlier modules remain legitimate witnesses to the insufficiency of those finite constraints alone; the global explicit-formula argument excludes their arithmetic realization in the positive-excess branch under \(\mathcal R_B\).

## Exact primary locators

Booker, A. R. (2015). *L-functions as distributions*. Mathematische Annalen, 363, 423–454. https://doi.org/10.1007/s00208-015-1178-z. Author version arXiv:1308.3067v2: Definition 1.3(A1)–(A4), p.3; Examples 1.4(2)–(3), p.4; Proposition 2.1, p.9, and its proof. The complete invoked source proofs were already independently read in this run; A1/A3/A4 were freshly checked for this interface review.

Calegari, F. (2013). *The Artin conjecture for some S5-extensions*. Mathematische Annalen, 356, 191–207. https://doi.org/10.1007/s00208-012-0839-4. Author-hosted publisher PDF: Theorem 1.1, p.2; character table, p.4; §3 opening, p.7; Lemma 3.2 and §4 opening, pp.8–9; comparison/Landau lemmas, pp.12–15.

Kurasov, P., & Sarnak, P. (2020). *Stable polynomials and crystalline measures*. Journal of Mathematical Physics, 61, 083501. https://arxiv.org/abs/2004.05678. Author version: §2, the summation-formula derivation and Theorem 1 proof, pp.3–8; §3, equations (41)–(43), pp.8–10. The exact example and matrix obstruction above were checked independently; the paper's deeper additive-structure classification is not used.

Sanders, T. (2020). *Bounds in Cohen's idempotent theorem*. Journal of Fourier Analysis and Applications, 26, Article 25. https://doi.org/10.1007/s00041-020-09732-y. §12, Fourier–Stieltjes and coset-ring definitions, Theorems 12.1 and 12.3. The finite qualitative conclusion applies to \(\mathbb R_d\).

Sasaki, S. (2013). *On Artin representations and nearly ordinary Hecke algebras over totally real fields*. Documenta Mathematica, 18, 997–1038. https://doi.org/10.4171/DM/419. Theorem 1, pp.998–999; statement and exact local specialization checked here.
