# Certified order-seven twists of the cubic Artin function at 1

## Result and scope

Let \(F=\mathbf Q(\sqrt[3]{269})\), let \(\rho\) be the standard two-dimensional representation of its \(S_3\) splitting group, and write
\[
L_0(s)=L(s,\rho)=\frac{\zeta_F(s)}{\zeta(s)}.
\]
Let \(\psi\) be the primitive order-seven Dirichlet character modulo 49 with
\(\psi(3)=\exp(2\pi i/7)\), extended by zero on multiples of 7. Then the independent interval computation in **certify.py** proves
\[
\boxed{
\prod_{j=0}^{6}L(1,\rho\otimes\psi^j)
\in
[\,0.649404996624796245942874132454723367397362332028805348924404
\ \pm 5.49\cdot10^{-61}\,].
}
\tag{1}
\]
The displayed interval includes decimal-output rounding. The underlying Arb ball has radius less than \(7.319\cdot10^{-62}\).

This assignment is a targeted analytic computation, not a statement-blind reconstruction. The existing exact coefficient routine in **workbench/programs/cubic_theta_certificate.py** was read with the parent's permission. The local coefficient formulas, conductor, twist root numbers, summation identity, and error bounds are derived below. The new certificate reads no previous coefficients, class numbers, regulators, or numerical L-values.

No GRH assumption enters. Equation (1) supplies a residue ratio for the separate first-layer class-number argument; it does not by itself certify a unit index or class number.

## 1. Exact arithmetic and gamma data

The only ramified rational primes in \(F\) are 3 and 269. At 269 the cubic polynomial is Eisenstein and the extension is tame, so the discriminant exponent is 2. At 3,
\[
v_3((-1)^3-269)=3>2v_3(3(-1)^2)=2.
\]
Hensel's criterion gives a cube root in \(\mathbf Q_3\). Thus the local cubic algebra is
\(\mathbf Q_3\times\mathbf Q_3(\omega)\), with discriminant exponent 1. Consequently
\[
D_F=-3\cdot269^2=-217083,\qquad N:=217083.
\]
The signature of \(F\) is \((1,1)\). Dividing the completed Dedekind zeta function of \(F\) by the completed Riemann zeta function gives
\[
\Lambda_0(s)=N^{s/2}\Gamma_{\mathbf C}(s)L_0(s),\qquad
\Gamma_{\mathbf C}(s)=2(2\pi)^{-s}\Gamma(s),
\]
and
\[
\Lambda_0(s)=\Lambda_0(1-s).
\tag{2}
\]
The harmless constant 2 in the definition of \(\Gamma_{\mathbf C}\) does not affect the equation. The Dedekind functional equation in precisely this form, up to that constant convention, is recorded in Sutherland (2015, Remark 18.14). The quotient is an entire nontrivial cubic Hecke function over \(K=\mathbf Q(\omega)\).

The associated cubic Hecke character \(\chi\) has conductor \((269)\) over \(K\). It is locally trivial at 3, tamely ramified with conductor exponent 1 at 269, and unramified elsewhere. Its conjugate is \(\chi^{-1}\ne\chi\). Its weight-one theta form
\[
f(z)=\sum_{n\ge1}a_n e^{2\pi i n z}
\]
has level \(N\) and nebentypus \(\eta=\left(\frac{-3}{\,\cdot\,}\right)\). Here the rational-ideal restriction of \(\chi\) is trivial, so no additional factor occurs in the nebentypus. The precise Hecke theta modularity statement is Simard (2015, Theorem 5, §3.4); the weight-one conductor and irreducibility/cuspidality description is also stated in Darmon, Lauder, and Rotger (2015, §3).

The integer 3 has order 42 modulo 49. Since
\[
-1\equiv3^{21}\pmod{49},
\]
the character \(\psi\) is even. Every nontrivial \(\psi^j\), \(1\le j\le6\), has exact conductor 49: an order-seven character cannot factor through
\((\mathbf Z/7\mathbf Z)^\times\), whose order is 6.

At 7 the original representation is unramified. A scalar twist by a character of conductor exponent 2 has exponent 4 on a two-dimensional unramified representation. At every other finite prime the twisting character is unramified and leaves the conductor exponent unchanged. The even twist leaves the two archimedean signs unchanged. Thus for \(j\ne0\)
\[
N_j=N\cdot49^2=521216283,\qquad
\Gamma_j(s)=\Gamma_{\mathbf C}(s).
\tag{3}
\]
Equivalently, 7 splits in \(K\); the Hecke twist has conductor exponent 2 at each of its two primes, giving the same norm factor \(7^4=49^2\).

## 2. Root number: a finite Fourier derivation

Set \(M=49\), and for a primitive character \(\xi\bmod M\) use
\[
\tau(\xi)=\sum_{u\bmod M}\xi(u)e^{2\pi i u/M}.
\]
The required formula, with its orientation fixed, is
\[
\boxed{\varepsilon_j=\psi^j(N)\frac{\tau(\psi^j)^2}{49}}.
\tag{4}
\]

Here is a direct derivation rather than an appeal to a convention-dependent twist formula. Use the normalized weight-one slash operator and write
\[
W_Q=\begin{pmatrix}0&-1\\Q&0\end{pmatrix},\qquad
A_u=\begin{pmatrix}1&u/M\\0&1\end{pmatrix}.
\]
Finite Fourier inversion gives
\[
f_\xi=\sum_{n\ge1}a_n\xi(n)e^{2\pi i nz}
=\frac1{\tau(\bar\xi)}
\sum_{u\bmod M}\bar\xi(u)\,f|A_u.
\tag{5}
\]
This uses
\(\sum_u\bar\xi(u)e^{2\pi inu/M}=\xi(n)\tau(\bar\xi)\), including zero for nonunits \(n\).

For each unit \(u\bmod M\), choose \(v\bmod M\) satisfying
\(Nuv\equiv-1\pmod M\). The exact matrix identity is
\[
A_uW_{NM^2}
=
\begin{pmatrix}
(1+Nuv)/M&u\\ Nv&M
\end{pmatrix}
\cdot M W_NA_v.
\tag{6}
\]
The first matrix belongs to \(\Gamma_0(N)\), has determinant 1, and has lower-right entry \(M\). A positive scalar matrix acts trivially under the normalized slash operation. Therefore
\[
f|A_uW_{NM^2}=\eta(M)(f|W_N)|A_v.
\]
Because \(\xi\) is even and \(u\equiv-(Nv)^{-1}\),
\[
\bar\xi(u)=\xi(N)\xi(v).
\]
Substituting in (5), and using (5) again for \(\bar\xi\), yields
\[
f_\xi|W_{NM^2}
=\eta(M)\xi(N)\frac{\tau(\xi)}{\tau(\bar\xi)}
(f|W_N)_{\bar\xi}.
\tag{7}
\]
The base equation (2), or Mellin inversion of it on the positive imaginary axis, gives
\(f|W_N=-if\). Also \(\eta(49)=1\), and even primitivity gives
\[
\tau(\xi)\tau(\bar\xi)=M.
\]
Thus (7) becomes
\[
f_\xi|W_{NM^2}=-i\,\xi(N)\frac{\tau(\xi)^2}{M}\,f_{\bar\xi}.
\]
The weight-one Mellin factor contributes \(i\), proving (4), and
\[
\Lambda_j(s)=\varepsilon_j\Lambda_{7-j}(1-s).
\tag{8}
\]

There is a useful exact check in this specific modulus. Since
\[
3^6\equiv1-7\pmod{49},\qquad
\psi(1+7b)=\zeta_7^b,
\]
grouping the Gauss sum into \(a+7t\) with \(1\le a\le6\) gives
\[
\sum_{t=0}^{6}\psi^j(a+7t)\zeta_{49}^{a+7t}
=
\psi^j(a)\zeta_{49}^a
\sum_{t=0}^{6}\zeta_7^{(1+j/a)t}.
\]
Only \(a\equiv-j\pmod7\) survives. Also
\(N\equiv13\equiv3^{33}\pmod{49}\), so \(\psi(N)=\zeta_7^5\).
The exact exponents are:

| \(j\) | \(\tau(\psi^j)/7\) | \(\varepsilon_j\) |
|---:|---:|---:|
| 1 | \(\zeta_{49}^{48}\) | \(\zeta_{49}^{33}\) |
| 2 | \(\zeta_{49}^{19}\) | \(\zeta_{49}^{10}\) |
| 3 | \(\zeta_{49}^{18}\) | \(\zeta_{49}^{43}\) |
| 4 | \(\zeta_{49}^{31}\) | \(\zeta_{49}^{6}\) |
| 5 | \(\zeta_{49}^{30}\) | \(\zeta_{49}^{39}\) |
| 6 | \(\zeta_{49}^{1}\) | \(\zeta_{49}^{16}\) |

In particular, \(|\varepsilon_j|=1\) and
\(\varepsilon_{7-j}=\overline{\varepsilon_j}\). The certificate computes the original finite Gauss sums directly with Acb; the table is an independent exact simplification of those sums.

## 3. The exact summation formula at 1

For \(j\ne0\), put
\[
c=\frac{2\pi}{49\sqrt N},\qquad
\Theta_j(t)=\sum_{n\ge1}a_n\psi^j(n)e^{-cnt}.
\]
The Fricke identity just proved is equivalent to
\[
\Theta_j(t)=\frac{\varepsilon_j}{t}\Theta_{7-j}(1/t).
\tag{9}
\]
For \(\operatorname{Re}s>1\), termwise Mellin integration gives
\[
\int_0^\infty\Theta_j(t)t^{s-1}\,dt
=c^{-s}\Gamma(s)L(s,\rho\otimes\psi^j).
\]
Split at 1 and use (9) in the first integral. The exponential decay at infinity then gives the entire continuation in the form
\[
c^{-s}\Gamma(s)L_j(s)
=
\int_1^\infty\Theta_j(t)t^{s-1}\,dt
+\varepsilon_j\int_1^\infty\Theta_{7-j}(t)t^{-s}\,dt.
\]
At \(s=1\), using
\(E_1(x)=\int_x^\infty e^{-u}\,du/u\), this is exactly
\[
\boxed{
L_j(1)
=
\sum_{n\ge1}\frac{a_n\psi^j(n)e^{-cn}}n
+
\varepsilon_j c
\sum_{n\ge1}a_n\overline{\psi^j(n)}E_1(cn).
}
\tag{10}
\]
There is no missing factor 2 or incomplete-gamma normalization. The factor 2 in
\(\Gamma_{\mathbf C}\) cancels on the two sides before (10).

For \(j=0\), the same formula holds with \(\varepsilon_0=1\), no deletion of multiples of 7, and
\[
c_0=\frac{2\pi}{\sqrt N}.
\]

## 4. Exact coefficients and unconditional tails

The integers \(a_n\) are multiplicative. For a prime power \(p^k\):

- \(p=269\): \(a_{p^k}=0\) for \(k\ge1\).
- \(p=3\): \(a_{p^k}=1\).
- \(p\equiv2\pmod3\), \(p\ne269\): \(a_{p^k}=1\) for even \(k\), and 0 for odd \(k\).
- \(p\equiv1\pmod3\) and \(269^{(p-1)/3}\equiv1\pmod p\): \(a_{p^k}=k+1\).
- Otherwise \(p\equiv1\pmod3\): \(a_{p^k}\) is the repeating sequence \(1,-1,0\) for \(k\equiv0,1,2\pmod3\).

These are respectively the inverse Euler polynomials
\[
1,\quad 1-T,\quad 1-T^2,\quad (1-T)^2,\quad 1+T+T^2.
\]
At primes \(p\equiv1\pmod3\), the stated modular exponent test is exactly the criterion for complete splitting of \(X^3-269\). At \(p\equiv2\pmod3\), the cube map on the residue field is bijective, giving transposition type. The ramified factors follow from the inertia invariants described in §1.

It follows prime by prime, and hence multiplicatively, that
\[
|a_n|\le d(n)\le n.
\tag{11}
\]
For \(x>0\),
\[
0<E_1(x)\le e^{-x}/x.
\]
Therefore truncating both sums in (10) after \(X\) produces a joint complex error of modulus at most
\[
\boxed{
T(c,X)=\frac{2e^{-c(X+1)}}{1-e^{-c}}.
}
\tag{12}
\]
Indeed each of the two tails is bounded by \(\sum_{n>X}e^{-cn}\).
The script adds (12) to both real and imaginary component radii, which is conservative for a modulus bound.

For the theta consistency checks, the exact geometric tail is
\[
\sum_{n>X}n e^{-ctn}
=e^{-ct(X+1)}
\left(\frac{X+1}{1-e^{-ct}}+
\frac{e^{-ct}}{(1-e^{-ct})^2}\right).
\tag{13}
\]
It encloses the complete theta remainder by (11). The certificate checks (9) at \(t=1\) and \(t=2\), independently of the exponential-integral evaluations. These checks confirm the implemented root-number convention; they do not replace the proof in §2.

## 5. Rigorous computation

The successful run used Python 3.12.14, python-flint 0.9.0, and 300-bit Arb/Acb precision. It generated every \(a_n\) through \(550000\) by an exact smallest-prime-factor sieve. The nontrivial twists required \(84778\) nonzero terms after removing multiples of 7.

All six twists are computed in one pass. For \(r=0,\ldots,6\), the script collects the real sums corresponding to \(\psi(n)=\zeta_7^r\):
\[
A_r=\sum_{\substack{n\le X\\\psi(n)=\zeta_7^r}}
a_n e^{-cn}/n,\qquad
B_r=\sum_{\substack{n\le X\\\psi(n)=\zeta_7^r}}
a_n cE_1(cn).
\]
Then
\[
L_j(1)=\sum_r A_r\zeta_7^{jr}
+\varepsilon_j\sum_r B_r\zeta_7^{-jr}
+\text{bounded remainder}.
\]
Every exponential and \(E_1\) value is evaluated directly with Arb. No interpolated values, floating-point E1 approximation, or unproved asymptotic expansion enters.

The cutoffs and rigorous tails are:

| Component | Cutoff | Joint absolute tail |
|---|---:|---:|
| \(L_0(1)\) | \(14000\) | \(<1.496\cdot10^{-80}\) |
| Each \(L_j(1)\), \(1\le j\le6\) | \(550000\) | \(<1.328\cdot10^{-62}\) |

The certified values, shown here to 45 decimal places for readability, are
\[
\begin{aligned}
L_0(1)&=1.697675723262554305985176685976171181067447196\ldots,\\
L_1(1)&=0.840861044178358639478921659729123775821123260\ldots\\
&\qquad{}+0.420151846287963799408564565659256852021543146\ldots i,\\
L_2(1)&=1.049194685135451841688990490550383258379748078\ldots\\
&\qquad{}-0.012970836498624184319071095004253008709981378\ldots i,\\
L_3(1)&=0.617143770120603573858404539556778997195861764\ldots\\
&\qquad{}+0.111160445335631907511303553479537594335971757\ldots i.
\end{aligned}
\]
The remaining values are their conjugates:
\(L_{7-j}(1)=\overline{L_j(1)}\). Full outward-rounded balls for all values are in **certificate.json**.

The product is evaluated as the positive real expression
\[
L_0(1)\prod_{j=1}^{3}
\bigl((\operatorname{Re}L_j(1))^2+(\operatorname{Im}L_j(1))^2\bigr),
\]
yielding (1). The certificate explicitly asserts a product radius below
\(10^{-55}\), so its precision claim is checked numerically as an interval width rather than inferred from a displayed digit count.

The exact coefficient list, serialized as comma-separated integers from \(a_1\) through \(a_{550000}\) followed by a newline, has SHA-256
**732db9ff4bb5760ae965350f79634cd9a4b9dacc314130ed207563fd966bfed4**.

## 6. Identification with the degree-21 residue ratio

Let \(Q_1\) be the degree-seven field cut out by \(\psi\), and let \(F_1=FQ_1\).
The splitting closure has group \(S_3\times C_7\): the two Galois extensions have coprime degrees 6 and 7. The permutation representation for \(F_1\) is
\[
(\mathbf1\oplus\rho)\otimes\mathbf C[C_7].
\]
Subtracting the permutation representation of \(Q_1\) gives
\(\rho\otimes\mathbf C[C_7]\). Artin formalism, including ramified Euler factors, proves
\[
\frac{\zeta_{F_1}(s)}{\zeta_{Q_1}(s)}
=\prod_{j=0}^{6}L(s,\rho\otimes\psi^j).
\tag{14}
\]
Taking the ratio of the simple residues at 1 proves that (1) is exactly
\[
\frac{\operatorname{Res}_{s=1}\zeta_{F_1}(s)}
{\operatorname{Res}_{s=1}\zeta_{Q_1}(s)}.
\]

There is a useful independent conductor-and-gamma check on (14).
The six nontrivial characters of \(Q_1\) all have conductor 49, so
\(D_{Q_1}=49^6\). The two fields have coprime discriminants, giving
\[
|D_{F_1}|=N^7D_{Q_1}^3=N^7\,49^{18}.
\]
Dividing by \(D_{Q_1}\) gives \(N^7\,49^{12}\), exactly
\(N\cdot(N49^2)^6\), the product of the seven conductors in (2)–(3).
The signatures are \((7,7)\) for \(F_1\) and \((7,0)\) for \(Q_1\); their quotient gamma factor is \(\Gamma_{\mathbf C}(s)^7\), again as required.

## 7. Reproduction and records

From this directory, with Python 3 available:

    python3 -m venv .venv
    .venv/bin/python -m pip install -r requirements.txt
    .venv/bin/python certify.py > run.txt

If python-flint 0.9.0 is already installed, use **python3 certify.py**.
The script resolves **certificate.json** relative to its own location, so it may also be invoked from another working directory. It reads no input-data file.

The files are:

- **certify.py**: exact coefficient generation and complete ball-arithmetic certificate;
- **certificate.json**: all results, tails, root numbers, grouped sums, and consistency checks;
- **run.txt**: the successful run, including progress and the JSON report;
- **requirements.txt**: the pinned python-flint dependency;
- **proof.md**: this analytic derivation;
- **SHA256SUMS**: integrity hashes for the distributed files.

Run **sha256sum -c SHA256SUMS** from this directory to check the saved files before regenerating them. Runtime metadata and printed rounding may differ under another software version. The interval assertions are checked anew on each run.

## References

Darmon, H., Lauder, A., & Rotger, V. (2015). Stark points and p-adic iterated integrals attached to modular forms of weight one. *Forum of Mathematics, Pi, 3*, e8. https://doi.org/10.1017/fmp.2015.7. Author's version, §3, p. 24: https://web.mat.upc.edu/victor.rotger/docs/DLR1.pdf

Johansson, F. (2017). Arb: Efficient arbitrary-precision midpoint-radius interval arithmetic. *IEEE Transactions on Computers, 66*(8), 1281–1292. https://doi.org/10.1109/TC.2017.2690633

Simard, N. (2015, November 2). *Notes on theta series*. Theorem 5, §3.4, p. 11. https://www.math.mcgill.ca/goren/GS/Thetas.pdf

Sutherland, A. V. (2015, November 12). *The analytic class number formula*. MIT 18.785 Number Theory I, Lecture 18. Theorem 18.13 and Remark 18.14, p. 11. https://math.mit.edu/classes/18.785/2015fa/LectureNotes18.pdf

