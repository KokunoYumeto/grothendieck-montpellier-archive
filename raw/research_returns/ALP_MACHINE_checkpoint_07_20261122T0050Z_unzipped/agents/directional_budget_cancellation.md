# ALP-LIFT-06: directional prime constants and unequal-order Cauchy cancellation

ALP_MACHINE; /root/lift_accounting, GPT-6 Astra Pro, with the directional
question proposed by /root. Reasoning effort not exposed. This refines
ALP-LIFT-04 using the actual CM eigenbases and polarization constructed in
ALP-LIFT-05. It concerns the bare DP64 certificate and a specified Chern
metric. It does not identify actual theta-selected gain or source division
error.

## Statement

Use \(\Phi=\{1,2,3\}\), \(\Psi=\{1,2,4\}\) in
\((\mathbb Z/7\mathbb Z)^\times\). For \(i=1,2,3\), define
\[
 b_i(a)=\mathbf1_{ai\notin\Phi}-\mathbf1_{a\notin\Psi},
 \qquad
 d_i(p)=\sum_{r\ge1}\frac{b_i(p^r)}{p^r}\quad(p\ne7).
 \tag{D1}
\]
The second indicator is the same for every selected direction of
\(\Psi\), since \(\Psi\) is a subgroup. Thus it is the appropriate
comparison for any pairing of the three chosen \(\Phi\)-directions
with the three \(\Psi\)-directions. Let
\(\ell_a=\log\Gamma(a/7)\) and
\[
 Q=\ell_1+\ell_2-\ell_3+\ell_4-\ell_5-\ell_6.
\]

**(a) Directional constants in ordinary prime order.** The limits
\[
 C_i=\lim_{X\longrightarrow\infty}
                  \sum_{\substack{p\le X\\p\ne7}}d_i(p)\log p
 \tag{D2}
\]
exist, with the primes in their ordinary increasing order, and satisfy
\[
 \boxed{C_i=\frac12\bigl(Q-2\ell_i+2\ell_{7-i}
                              -\ell_{7-2i}+\ell_{2i}\bigr).}
 \tag{D3}
\]
In particular
\[
\begin{split}
 C_1&=-\tfrac12\ell_1+\ell_2-\tfrac12\ell_3
                         +\tfrac12\ell_4-\ell_5+\tfrac12\ell_6,\\
 C_2&=\tfrac12\ell_1-\tfrac12\ell_2-\ell_3
                         +\ell_4+\tfrac12\ell_5-\tfrac12\ell_6,\\
 C_3&=\tfrac12\ell_2-\tfrac32\ell_3
                         +\tfrac32\ell_4-\tfrac12\ell_5
      =C_1+C_2=\tfrac12\delta_7.
\end{split}
 \tag{D4}
\]
Let \(G_i\), \(G_B\) be the exact metrics in ALP-LIFT-05. Then
\[
 \boxed{C_i-\frac{2i}{7}\log2
               =-\frac12\log(G_i/G_B)\qquad(i=1,2,3).}
 \tag{D5}
\]
The subtraction removes exactly the formal prime-2 contribution;
it leaves the actual common good-prime range \(p\nmid14\).

**(b) Integer certificates with an arbitrary growing cutoff.** For
an integer \(n\ge0\), real \(X\ge2\), and fixed finite set of
rational primes \(S\) containing 7, put
\[
 D_{i,S}(n;X)=\sum_{\substack{p\le X\\p\notin S}}\log p
                     \sum_{r\ge1}b_i(p^r)\left\lfloor n/p^r\right\rfloor,
 \qquad
 C_{i,S}=C_i-\sum_{p\in S\setminus\{7\}}d_i(p)\log p.
 \tag{D6}
\]
There is \(c>0\) such that, uniformly in \(n\ge4\), \(X\ge2\),
\[
 D_{i,S}(n;X)=nC_{i,S}
    +O_S\!\left(n\exp\{-c\sqrt{\log\min(X,\sqrt n)}\}\right).
 \tag{D7}
\]
The constant can be chosen for all three directions at once.
Consequently, for any vector of nonnegative integer orders
\(\boldsymbol n=(n_1,n_2,n_3)\), any common cutoff \(X\), and
\(N=n_1+n_2+n_3\),
\[
 \sum_{i=1}^3D_{i,\{2,7\}}(n_i;X)
       =-\frac12\sum_{i=1}^3n_i\log(G_i/G_B)+o(N)
 \tag{D8}
\]
in every joint limit \(N\to\infty\), \(X\to\infty\).
No fixed positive limiting ratio between the three orders is required.

**(c) Unequal-order Cauchy comparison.** In the actual diagonal CM
coordinates of ALP-LIFT-05, let the two functions satisfy its growth
inequalities (H26), with fixed constants \(C_J^\theta,C_A^\theta>0\).
Pair \((\omega_1,\omega_2,\omega_3)\) with
\((\vartheta_1,\vartheta_2,\vartheta_4)\). Define the logarithmic
polydisk Cauchy bounds
\[
 \mathcal C_J(\boldsymbol n)=\log C_J^\theta+
   \sum_{i=1}^3\left[
     \log(n_i!)+\frac{n_i}{2}\log(\pi e/n_i)
                          -\frac{n_i}{2}\log G_i\right],
 \tag{D9}
\]
where a term with \(n_i=0\) is interpreted by continuity as zero,
and define \(\mathcal C_A\) by replacing \(G_i\) by \(G_B\)
and the leading constant by \(C_A^\theta\). Then
\[
 \mathcal C_J(\boldsymbol n)-\mathcal C_A(\boldsymbol n)
 =\log(C_J^\theta/C_A^\theta)
               +\sum_{i=1}^3n_i C_{i,\{2,7\}}.
 \tag{D10}
\]
It follows from (D8) that
\[
 \sum_iD_{i,\{2,7\}}(n_i;X)
       -\bigl(\mathcal C_J(\boldsymbol n)-
                                 \mathcal C_A(\boldsymbol n)\bigr)
                                                        =o(N)
 \tag{D11}
\]
for the same arbitrary joint limit. Multiplying both budgets by the
source's factor 2 leaves this cancellation unchanged. The assertion
is about the displayed bounds, not equality of actual theta values.

## Proof of the local functions and convergence

Direct evaluation of the six residue classes gives
\[
 b_1=\mathbf1_{\{4\}}-\mathbf1_{\{3\}},\qquad
 b_2=\mathbf1_{\{2\}}-\mathbf1_{\{5\}},\qquad
 b_3=b_1+b_2.
 \tag{D12}
\]
They have mean zero and are odd: \(b_i(-a)=-b_i(a)\). Geometric
summation of the powers of a residue class gives the following exact
local table:

| \(p\bmod7\) | \(d_1(p)\) | \(d_2(p)\) | \(d_3(p)\) |
|---|---|---|---|
| \(1,6\) | \(0\) | \(0\) | \(0\) |
| \(2\) | \(p/(p^3-1)\) | \(p^2/(p^3-1)\) | \(p(p+1)/(p^3-1)\) |
| \(4\) | \(p^2/(p^3-1)\) | \(p/(p^3-1)\) | \(p(p+1)/(p^3-1)\) |
| \(3\) | \(-p^2/(p^3+1)\) | \(p/(p^3+1)\) | \(-p(p-1)/(p^3+1)\) |
| \(5\) | \(p/(p^3+1)\) | \(-p^2/(p^3+1)\) | \(-p(p-1)/(p^3+1)\) |

For example, in class 3 the nonzero terms of \(b_1(p^r)\) are
\(-1\) at \(r\equiv1\pmod6\) and \(+1\) at
\(r\equiv4\pmod6\); hence
\((-p^{-1}+p^{-4})/(1-p^{-6})=-p^2/(p^3+1)\).
In class 2 the period is three, and the nonzero \(b_1\)-term is
at exponent 2, giving \(p^{-2}/(1-p^{-3})=p/(p^3-1)\).
Interchanging classes 2 and 4, or 3 and 5, interchanges
\(b_1\) and \(b_2\); (D12) gives the last column. These
observations prove every entry. In particular
\[
                  (d_1(2),d_2(2),d_3(2))=(2/7,4/7,6/7).
 \tag{D13}
\]

For clarity about convergence, the quantitative prime theorem for
fixed modulus 7, already cited in ALP-LIFT-04, gives
\[
 B_i(x):=\sum_{p\le x}b_i(p)\log p
                   =O(xe^{-c_0\sqrt{\log x}}).
 \tag{D14}
\]
The terms at 7 are defined to be zero. The main terms cancel
because \(\sum_{a=1}^6b_i(a)=0\). The prime-power version of the
same theorem implies this prime version as well, since powers of
exponent at least two contribute \(O(\sqrt x\log x)\).
Partial summation now proves convergence of
\(\sum_p b_i(p)\log p/p\), with tail
\(O((1+\sqrt{\log X})e^{-c_0\sqrt{\log X}})\).
The series of the remaining terms is absolutely convergent, since
\[
 \sum_p\log p\sum_{r\ge2}|b_i(p^r)|p^{-r}
       \le\sum_{m\ge2}\frac{\log m}{m(m-1)}<\infty.
\]
This proves (D2) in the asserted ordinary-prime order. It also
justifies absorbing the harmless polynomial factor in the tail
by decreasing \(c_0\).

## Proof of the exact constants

Let \(\chi(3)=\exp(\pi\mathrm i/3)\), and write
\(Z_\eta=L'(0,\eta)/L(0,\eta)\). In the ordered odd character
basis \((\chi,\chi^3,\overline\chi)\), the coefficients of
the three functions in (D12) are
\[
 \begin{array}{c|ccc}
 &\chi&\chi^3&\overline\chi\\\hline
 b_1&(-1+\mathrm i\sqrt3)/6&1/3&(-1-\mathrm i\sqrt3)/6\\
 b_2&(-1-\mathrm i\sqrt3)/6&1/3&(-1+\mathrm i\sqrt3)/6\\
 b_3&-1/3&2/3&-1/3.
 \end{array}
 \tag{D15}
\]
This follows either by substituting the six group elements into the
table, or by the normalized Fourier coefficient
\(6^{-1}\sum_ab_i(a)\overline\eta(a)\). The sum of each row of
coefficients is zero, since \(b_i(1)=0\).

For real \(s>1\), the Euler product gives
\[
 \sum_{p\ne7}\log p\sum_{r\ge1}b_i(p^r)p^{-rs}
        =-\sum_\eta\widehat b_i(\eta)
                                      \frac{L'(s,\eta)}{L(s,\eta)}.
 \tag{D16}
\]
Partial summation using (D14) permits the limit \(s\downarrow1\)
for the first powers by an integrable bound independent of
\(s\in[1,2]\); the higher powers converge absolutely there.
The functional equation for an odd primitive character of conductor
7 gives
\[
 \frac{L'(1,\eta)}{L(1,\eta)}+Z_{\overline\eta}
                         =\gamma+\log(2\pi/7).
 \tag{D17}
\]
The constant vanishes after summation because the coefficient row
sums in (D15) are zero. Hence
\[
 C_i=\sum_\eta\widehat b_i(\eta)Z_{\overline\eta}.
 \tag{D18}
\]
The conjugation in this formula is essential. Write
\(Z=Z_\chi\), \(Z_3=Z_{\chi^3}\). Then (D15)–(D18) give
\[
 C_1=(Z_3-\operatorname{Re}Z+\sqrt3\operatorname{Im}Z)/3,
 \quad
 C_2=(Z_3-\operatorname{Re}Z-\sqrt3\operatorname{Im}Z)/3,
 \quad C_3=2(Z_3-\operatorname{Re}Z)/3.
 \tag{D19}
\]

The Hurwitz special values used in ALP-LIFT-02 yield
\[
 Z_3=-\log7+Q,
\]
\[
 \operatorname{Re}Z=-\log7+\ell_1+\tfrac14\ell_2
          +\tfrac54\ell_3-\tfrac54\ell_4-\tfrac14\ell_5-\ell_6,
\]
and the same finite character calculation yields
\[
 \sqrt3\operatorname{Im}Z=-\tfrac32\ell_1+\tfrac94\ell_2
             +\tfrac34\ell_3-\tfrac34\ell_4-\tfrac94\ell_5
             +\tfrac32\ell_6.
 \tag{D20}
\]
For example, the last two formulas follow by multiplying
\(\sum_a\chi(a)\ell_a\) by
\(L(0,\chi)^{-1}=1-\mathrm i\sqrt3/2\), whose value was
computed exactly in ALP-LIFT-02. Substituting (D20) into (D19)
gives all three expansions in (D4), and these are exactly (D3).

To identify the actual metric, the elliptic case of the same
normalized Colmez formula, together with (H22), gives
\[
                         \log G_B=\log(\pi/7)+Q.
 \tag{D21}
\]
Here is the normalization explicitly. ALP-LIFT-02's Yang convention
gives \(h_F(B)=-\tfrac12Z_3-\tfrac14\log7\); passing to its
L² convention subtracts \(\tfrac12\log\pi\). On the other
hand (H22) gives \(h_{F,L^2}(B)=-\tfrac14\log7-
\tfrac12\log G_B\). Equating these expressions proves (D21).
No isogeny invariance is used.

The gamma duplication formula, applied at \(i/7\) and
\(1/2-i/7\), rewrites (H8) as
\[
 \log G_i=\log(\pi/7)+\frac{4i}{7}\log2
          +2\ell_i-2\ell_{7-i}+\ell_{7-2i}-\ell_{2i}.
 \tag{D22}
\]
All gamma arguments are positive for \(i=1,2,3\). Subtracting
(D21) from (D22), then multiplying by \(-1/2\) and using (D3),
proves (D5). The explicit prime-2 values (D13) show that its left
side is exactly \(C_{i,\{2,7\}}\). This proves part (a).

## Proof of the uniform integer estimate

We give the estimates rather than identifying a formal slope with a
theta value. First let \(S=\{7\}\), suppress the index \(i\),
and put \(b=b_i\). Decompose (D6) into first powers and higher
powers. Define
\[
 P_1(X)=\sum_{p\le X}b(p)\log p/p,\qquad
 P_2(X)=\sum_{p\le X}\log p\sum_{r\ge2}b(p^r)/p^r.
\]
The convergence proof gives
\[
 P_1(X)+P_2(X)=C_i+O(e^{-c_1\sqrt{\log X}}),\quad
 P_1(X)-P_1(\infty)=O(e^{-c_1\sqrt{\log X}}),
 \tag{D23}
\]
and \(P_2(X)-P_2(\infty)=O((1+\log X)/X)\).

The higher-power floor errors are uniformly
\(O(\sqrt n\log n)\). Indeed
\(H_2(t)=\sum_{p^r\le t,r\ge2}\log p=O(\sqrt t\log t)\)
by \(\theta(t)=O(t)\). Floors for \(p^r\le n\) produce an
error at most \(H_2(n)\); the tail of the linear approximation is
at most \(n\int_{(n,\infty)}t^{-1}dH_2(t)
=O(\sqrt n\log n)\). Restricting to \(p\le X\) only reduces
these absolute bounds. Thus the higher-power contribution is
\(nP_2(X)+O(\sqrt n\log n)\).

Put \(y=\lfloor\sqrt n\rfloor\). If \(X\le y\), the
first-power floor error is at most \(\theta(X)=O(X)\).
Together with (D23) this proves (D7) in that range. If \(X\ge y\),
expanding the floors gives the exact identity
\[
 \sum_{p\le X}b(p)\log p\left\lfloor n/p\right\rfloor
 =\sum_{p\le y}b(p)\log p\left\lfloor n/p\right\rfloor
 +\sum_{k\le n/y}
       \{B_i(\min(X,n/k))-B_i(y)\}.
 \tag{D24}
\]
In the second sum, \(y\le\min(X,n/k)\le n/k\). Formula (D14)
and the harmonic-sum bound show that its absolute value is at most
\(O(n(1+\log n)e^{-c_0\sqrt{\log y}})\). The first sum is
\(nP_1(\infty)+O(ne^{-c_1\sqrt{\log y}}+y)\).
Combining with the higher powers and
\(P_2(X)-P_2(\infty)=O((1+\log y)/y)\) proves (D7) for
\(X\ge y\), after reducing \(c>0\). In both ranges the
\(O(\sqrt n\log n)\) error is absorbed by the displayed
exponential bound. The replacement of \(y\) by \(\sqrt n\)
only changes a fixed multiplicative constant for \(n\ge4\).

For a fixed omitted prime \(p\ne7\), the corresponding floor
sum differs from \(nd_i(p)\) by \(O_p(1+\log n)\): only
\(O_p(1+\log n)\) powers have a nonzero floor, and the remaining
linear geometric tail is \(O_p(1)\). Its \(\log p\) factor is
fixed. Once \(X\) contains the exceptional set, subtracting these
finitely many terms proves (D7) for \(S\). When it does not,
\(X\) stays bounded by the largest exceptional prime, and an
extra \(O_S(n)\) is absorbed by the right side after enlarging
its constant. This establishes the full uniform assertion.

To deduce (D8) without a restriction on relative orders, fix
\(\varepsilon>0\). Choose \(K\) large enough that the error
factor in (D7) is below \(\varepsilon\) whenever
\(n_i\ge K\) and \(X\ge\sqrt K\). The sum of errors in
these directions is at most a constant times
\(\varepsilon N\). In directions with \(n_i<K\), both their
floor sums and their linear approximations are bounded by a
constant depending only on \(K\), since every nonzero floor has
\(p\le n_i<K\), independent of \(X\). Divide by \(N\),
let \(N,X\to\infty\), then let \(\varepsilon\to0\).
Using (D5) now proves (D8).

## Proof of the Cauchy statement and its scope

Apply polydisk Cauchy to the bounds in (H26). For a positive
directional order choose \(R_i^2=n_iG_i/\pi\); for order zero
take \(R_i\downarrow0\). The resulting bound is (D9).
Perform the same calculation in the normalized induced eigenbasis
(H12), whose three metric values are all \(G_B\). The factorial
terms, \(\pi e\) terms and the individual \(n_i\log n_i\)
terms cancel exactly between the two expressions. The remaining
metric terms give (D10) by (D5); (D8) proves (D11).
A common tensor level \(\kappa\) changes \(\pi\) to
\(\kappa\pi\) and hence adds \((N/2)\log\kappa\) to both
expressions, so it cancels as well. This is the level dependence
whose source differential normalization is treated in AM-R004.
This completes the proof. \(\square\)

The input in this theorem is an actual diagonal CM eigenbasis for
both principally polarized abelian varieties, primitive at every
common good prime. Thus the metric term is not a hypothetical
period parameter. The lower prime certificate remains precisely
the accepted DP64 object. The theorem proves that assigning
different orders to the three fixed CM directions does not create
an order-linear advantage within this paired bare-certificate and
Cauchy-bound calculation.

At 7 the normalized eigenbasis need not be integral one direction
at a time, although its determinant has the exact valuation proved
in ALP-LIFT-05. This theorem does not bound an unequal-order
7-adic theta error. Nor does it show that the Cauchy bounds are
attained, that selected values equal their universal lower
certificates, or that the same arithmetic normalization gives the
constants \(C_J^\theta,C_A^\theta\). The arithmetic kernel,
row content, bad-prime theta normalization and division losses
are still required before applying the full DP44 comparison.

## Numerical cross-checks and citations

The accompanying exact-algebra/numerical script is
`work/agents/hodge_lattice_certificate.py`; it checks the gamma,
Fourier and metric identities to 90 decimal digits as a cross-check
of the symbolic proof. Its current approximate constants are:

| direction | all \(p\ne7\): \(C_i\) | good \(p\nmid14\): \(C_{i,\{2,7\}}\) |
|---|---:|---:|
| 1 | −0.127202946857769870150102196626 | −0.325244998446325672840739945614 |
| 2 | 0.155046463619921284560680397991 | −0.241037639557190320820595099985 |
| 3 | 0.0278435167621514144105782013653 | −0.566282638003515993661335045599 |

External known inputs and exact locators are unchanged from
ALP-LIFT-02/04/05: the abelian Colmez theorem in Yang (2010),
Section 3, pp. 464–466, with Colmez (1993) and Obus (2013),
arXiv v2 Theorem 3.9; Rudnick (2015), fixed-modulus prime theorem,
Section 2, printed p. 2 before equation (1); DLMF 25.15.2,
25.15.5 and 25.15.9 for the Euler product, primitive functional
equation and nonvanishing at 1, 25.11.13 and 25.11.18 for Hurwitz
special values, and 5.5.5 for gamma duplication. The smooth
Picard/Hodge and compatible-biextension interpretation is precisely
that in ALP-LIFT-05, with the accepted DP22 FGA locators; it
requires no additional weight or comparison-isomorphism claim.

