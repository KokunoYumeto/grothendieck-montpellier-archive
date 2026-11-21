# Independent proof of the level-three weight-thirteen modular-form model

Finding **K17-GL2-MODEL**. Date: 2026-11-21 UTC. Checker: `/root/archive_kummer`, GPT-6 Astra Pro. **PASS for the modular-form space, basis, exact Fourier-series formulas, and recovery of its Hecke matrices from the first three coefficients.** This audit does not establish the separate automorphic transfer/coverage statement, the unitary neighbor calculation, or any K-group vanishing.

## 1. Statement

Let \(\chi=\chi_{-3}\), and put

\[
a(\tau)=\sum_{\alpha\in\mathbb Z[\zeta_3]}q^{N\alpha},\qquad
b(\tau)=\frac{\eta(3\tau)^9}{\eta(\tau)^3},\qquad
D(\tau)=\eta(\tau)^6\eta(3\tau)^6.
\]

Then

\[
S_{13}(\Gamma_0(3),\chi)
=D\,M_7(\Gamma_0(3),\chi)
=\operatorname{span}_{\mathbb C}\{Da^7,Da^4b,Dab^2\}.
\]

The three displayed forms are a basis. Their integral Fourier expansions begin respectively in degrees one, two, and three, with leading coefficient one. Consequently the coefficient map \(f\mapsto([q]f,[q^2]f,[q^3]f)\) is an isomorphism of this complex vector space with \(\mathbb C^3\), and it identifies its integral-Fourier-expansion lattice with \(\mathbb Z^3\) through an integral matrix of determinant one.

## 2. Exact primary source and scope of its use

Fabien Cléry and Gerard van der Geer, *Generating Picard modular forms by means of invariant theory*, arXiv:2110.00849v2, 28 February 2022:

<https://arxiv.org/pdf/2110.00849>.

The paragraph **“Modular forms on \(\Gamma_1(3)\)” on printed p.12**, read in full, states

\[
M(\Gamma(3))=\mathbb C[\vartheta,\psi],\qquad
\vartheta=\sum_{\alpha\in O_{\mathbb Q(\sqrt{-3})}}q^{N\alpha},
\quad \psi=\eta(3\tau)^3/\eta(\tau),
\]

with both generators of weight one, and then

\[
M(\Gamma_1(3))=\mathbb C[\vartheta,\psi^3],\qquad
M_{2k+1}(\Gamma_1(3))=M_{2k+1}(\Gamma_0(3),(\cdot/3)).
\]

Thus the present \(a,b\) are exactly \(\vartheta,\psi^3\), with no undetermined scaling; \((\cdot/3)=\chi_{-3}\). **Remark 15.2 on printed p.33**, also read in full, identifies \(\eta(\tau)^6\eta(3\tau)^6\) as a weight-six cusp form on \(\Gamma_0(3)\), and prints its initial Fourier expansion beginning \(q-6q^2+9q^3+4q^4+\cdots\).

Only these statements are used. An adjacent extracted theta/eta relation is unnecessary for the argument and was not used as an input. The local source files are `clery_vd_geer_picard.pdf` and `clery_vd_geer_picard.txt` in this directory; their title/version and the entire two cited passages were freshly read.

## 3. The division by the weight-six cusp form

The eta product \(D\) has no zero in the upper half-plane, since the Dedekind eta function has none there. Its defining product gives \(D=q+O(q^2)\), so its order at infinity is exactly one.

The usual eta transformation \(\eta(-1/\tau)=(-i\tau)^{1/2}\eta(\tau)\), with its holomorphic branch, gives

\[
D\left(-\frac1{3\tau}\right)
=(-i3\tau)^3(-i\tau)^3D(\tau)
=-27\tau^6D(\tau).
\]

For the determinant-normalized slash operator and \(W_3=\left(\begin{smallmatrix}0&-1\\3&0\end{smallmatrix}\right)\), this says \(D|_6W_3=-D\). Therefore the order of \(D\) at the other cusp, zero, is also exactly one. These are all the cusps of \(\Gamma_0(3)\). Their widths are one and three, respectively; the corresponding stabilizer translations have lower-right entry one, so the nebentypus \(\chi\) does not introduce a fractional order at either cusp.

For any \(f\in S_{13}(\Gamma_0(3),\chi)\), the quotient \(f/D\) is holomorphic in the upper half-plane and at both cusps, by the exact orders just checked. Its transformation law is weight seven with character \(\chi\). Conversely \(Dg\) is cuspidal for every \(g\in M_7(\Gamma_0(3),\chi)\). Multiplication by \(D\) is therefore a bijection from that space onto \(S_{13}(\Gamma_0(3),\chi)\).

The source's polynomial-ring description now gives the entire weight-seven space. The nonnegative solutions to \(i+3j=7\) are \((7,0),(4,1),(1,2)\), so its basis is \(a^7,a^4b,ab^2\). This proves the dimension-three assertion without an extrapolation from finitely many Fourier coefficients. As an additional elementary check, the valence bound at infinity for weight seven and index \([\mathrm{SL}_2(\mathbb Z):\Gamma_0(3)]=4\) is \(7/3\); the three proposed forms have distinct orders zero, one, and two and hence attain the possible dimension bound.

## 4. Exact Fourier series and the integral basis

The theta series satisfies

\[
a=1+6\sum_{n\ge1}\left(\sum_{d\mid n}\chi(d)\right)q^n.
\]

One direct proof uses that the Eisenstein integers are a Euclidean principal ideal domain with six units. A nonzero element of norm \(n\) generates an ideal of norm \(n\), with exactly six generators. The number of ideals of norm \(n\) is \(\sum_{d\mid n}\chi(d)\): the Euler factors at the ramified prime three, split primes, and inert primes give respectively one, \(r+1\), and the indicator that \(r\) is even for a prime power of exponent \(r\). This is precisely the series constructed in the code.

The two other defining products are

\[
b=q\prod_{n\ge1}\frac{(1-q^{3n})^9}{(1-q^n)^3},\qquad
D=q\prod_{n\ge1}(1-q^n)^6(1-q^{3n})^6.
\]

The negative-exponent binomial expansion used by the program is the exact integer expansion \((1-X)^{-r}=\sum_{k\ge0}\binom{r+k-1}{k}X^k\). Truncating each factor and multiplication modulo \(q^{56}\) therefore computes the first 56 coefficients exactly; no analytic or floating-point approximation is involved.

Since \(a=1+O(q)\) and \(b=q+O(q^2)\), the basis \(Da^7,Da^4b,Dab^2\) has successive leading terms \(q,q^2,q^3\). Its first-three-coefficient matrix is triangular with diagonal entries one. All coefficients of these three forms are integers. A form in their complex span has integral coefficients if and only if its first three coordinates yield integral basis coefficients, proving the integral-lattice statement above.

## 5. What the Hecke computation can consequently certify

The complete source of `compute_gl2_weight13.py` was read. Its theta formula, eta factors, weight assignments, and three basis monomials agree with the proof above. For a prime \(p\nmid3\), the classical normalized Hecke operator on weight thirteen and character \(\chi\) has Fourier coefficients

\[
[q^n]T_pf=[q^{pn}]f+\chi(p)p^{12}[q^{n/p}]f,
\]

where the second term is zero when \(p\nmid n\). At \(p=7,13\), the second term is zero for \(n=1,2,3\). Since those three coefficients determine the form, solving the stated three-by-three system determines the full operator exactly. The additional available coefficient comparisons in the script are checks of the same exact formula; they are not substitutes for the dimension/basis proof.

This audit covers the modular-form model and the sufficiency of the matrix-recovery method. The numerical execution, characteristic polynomials, their evaluations, their use with the separate unitary matrix, and the arithmetic normalization/coverage of those eigenvalues remain separately recorded checks. In particular no conclusion about \(K_{12}(\mathbb Z)\) follows from this audit alone.

## 6. Actual check record

Read the entire program, the complete primary paragraph on printed p.12, and all of Remark 15.2 on printed p.33. Reconstructed division at both cusps, the exact polynomial-weight count, the theta coefficient identity, eta-product truncation, integral basis, and Hecke coefficient recovery. No proof-assistant execution is claimed, and the separate Hecke script was not rerun as part of this model-only audit.
