# A direct positive central derivative for the Fermat-quartic motive

Run JAC1964-20261121. Author/checker: /root/arithmetic_sign, GPT-6 Astra Pro; effort setting not exposed. This is an elementary deduction from the stated known CM identification and functional equation. It proves no height identity.

## Proposition AR-11

Let \(M\) be the rank-two motive of types \((3,0),(0,3)\) in the third cohomology of the Jacobian of \(x^4+y^4=z^4\), over \(\mathbf Q\). Normalize its motivic \(L\)-function by its Euler series \(L(M,s)=\sum_{n\ge1}a_n n^{-s}\), with \(a_1=1\). Then
\[
L'(M,2)>\frac7{20}>0.
\tag{AR.14}
\]
In particular the analytic sign required in a positively normalized height formula for this particular motive is unconditional. No GRH is used.

### Known CM input and normalization

Write \(F=\mathbf Q(i)\), \(\mathfrak q=(1+i)\), and let \(\psi,\psi'\) be the algebraic Hecke characters of the elliptic curves \(E:y^2=x^3-x\) and \(E':y^2=x^3+x\). The relevant character is
\[
\chi=\psi^2\psi'=\psi^3\mu,
\]
where \(\mu\) corresponds to \(F(\sqrt2)=\mathbf Q(\zeta_8)\). Bertolini--Darmon--Prasanna, *p-adic L-functions and the coniveau filtration on Chow groups*, §5.2, pp.24--27 of the read author manuscript, gives this identification, the conductors \(\mathfrak q^3,\mathfrak q^4\) of \(\psi,\psi'\), the conductor \(\mathfrak q^2\) of \(\psi^2\), and the root-number formula. For exponent three with the twist \(\mu\), that root number is \(-1\).

Because \(\psi^2\) is trivial on \(1+\mathfrak q^2\) whereas \(\psi'\) is nontrivial on \(1+\mathfrak q^3\), the product \(\chi=\psi^2\psi'\) has conductor exactly \(\mathfrak q^4\). Its infinity type is \((3,0)\). Thus its normalized CM theta series \(f(z)=\sum a_n e^{2\pi i nz}\) is a weight-four cusp form of level \(N=|D_F|N_{F/\mathbf Q}(\mathfrak q^4)=64\), with trivial nebentypus. Its \(L\)-function is \(L(M,s)\), with center \(2\) and sign \(-1\). The standard modular description is independently recorded as LMFDB newform 64.4.a.c; the argument below does not use the database's numerical analytic rank.

For an ideal \(\mathfrak a\) prime to \(\mathfrak q\), we have \(|\chi(\mathfrak a)|=(N\mathfrak a)^{3/2}\). The number of ideals in \(\mathbf Z[i]\) of norm \(n\) is at most \(d(n)\), the divisor count. Consequently
\[
|a_n|\le d(n)n^{3/2}\le2n^2.
\tag{AR.15}
\]
The final inequality follows by pairing divisors below and above \(\sqrt n\). The conductor removes every even-norm term. There is no ideal of norm \(3\). Hence
\[
a_1=1,\qquad a_2=a_3=a_4=0.
\tag{AR.16}
\]

### Mellin calculation

Set \(a=1/8=N^{-1/2}\). The Mellin transform is
\[
I(s)=\int_0^\infty f(iy)y^{s-1}\,dy
     =(2\pi)^{-s}\Gamma(s)L(M,s).
\]
The Fricke relation, with root number \(-1\) and weight four, reads
\[
f\!\left(\frac{i}{Ny}\right)=-N^2y^4 f(iy).
\]
Substituting \(y\mapsto1/(Ny)\) in the part below \(a\) gives
\[
I(s)=\int_a^\infty f(iy)
 \left(y^{s-1}-N^{2-s}y^{3-s}\right)\,dy.
\]
At \(s=2\) the integrand vanishes. Differentiating gives
\[
I'(2)=2\int_a^\infty f(iy)y\log(8y)\,dy.
\]
Since \(L(M,2)=0\), the Mellin prefactor contributes no derivative term and \(L'(M,2)=(2\pi)^2I'(2)\).

Let \(E_1(x)=\int_x^\infty e^{-t}\,dt/t\). Integration by parts gives
\[
\int_a^\infty e^{-2\pi ny}y\log(y/a)\,dy
 =\frac{e^{-cn}+E_1(cn)}{(2\pi n)^2},
\qquad c=\frac\pi4.
\]
The coefficient bound (AR.15) gives absolute convergence on \(y\ge a\), justifying the exchange of sum and integral. Thus
\[
L'(M,2)
 =2\sum_{n\ge1}\frac{a_n}{n^2}
       \left(e^{-cn}+E_1(cn)\right).
\tag{AR.17}
\]

### Elementary lower bound

For \(x>0\),
\[
0<E_1(x)\le e^{-x}/x.
\]
Put \(q=e^{-c}\). Since \(3/4<c<1\), we have \(q<1/2\) and \(q>1/3\): indeed \(e^{3/4}>1+3/4+(3/4)^2/2>2\), while \(e<3\). The \(n=1\) term of (AR.17) is therefore greater than \(2/3\).

By (AR.15)--(AR.16), the absolute value of the sum of every remaining term is bounded by
\[
\begin{aligned}
2\sum_{n\ge5}\frac{|a_n|}{n^2}
       \left(e^{-cn}+E_1(cn)\right)
&\le4\sum_{n\ge5}q^n\left(1+\frac1{cn}\right)\\
&<4\cdot\frac{19}{15}\cdot
       \frac{(1/2)^5}{1-1/2}
 =\frac{19}{60}.
\end{aligned}
\]
It follows that \(L'(M,2)>2/3-19/60=7/20\). This proves (AR.14). \(\square\)

## Optional numerical refinement, independently checked

The accompanying script enumerates the unique primary Gaussian-integer generator of each ideal of norm at most \(20\). It obtains exactly
\[
a_1=1,\quad a_5=-22,\quad a_9=-27,\quad a_{13}=18,\quad a_{17}=-94,
\]
with all other \(a_n\), \(1\le n\le20\), zero. These coefficients also match the primary database's displayed expansion.

At precision 160 bits, python-flint/Arb evaluates the finite sum in (AR.17). The tail is bounded mathematically by
\[
4\left(1+\frac1{21c}\right)\frac{e^{-21c}}{1-e^{-c}}
 <5.357966\cdot10^{-7}.
\]
The resulting enclosing rational interval is
\[
1.5071685<L'(M,2)<1.5071697.
\tag{AR.18}
\]
The elementary proof of the sign does not depend on this computation. The script and its output are in fermat_lderi_bound.py and fermat_lderi_bound.json.

## What this resolves and what it leaves

For this one rank-two CM motive, the derivative sign is settled without the supplied Dirichlet-GRH theorem or a hypothetical broader Hecke-GRH theorem. A proven identity \(h(\eta,\eta)=C\,L'(M,2)\), with \(C>0\), would now imply strict positivity immediately. No such identity is established here. The actual known height formula remains (AR.10), with the stronger finite-local information (AR.12); an automorphic comparison must still control its ramified contribution and identify the particular Chow cycle.

The generalized-Heegner formula of Lilienfeldt--Shnidman, *Derivatives of Rankin--Selberg L-functions and heights of generalized Heegner cycles*, Theorem 1.1 (arXiv:2408.04375, read author manuscript dated 8 August 2024), does not directly supply the missing equality for the BDP Fermat construction. Its hypotheses require an even-weight form, an unramified Hecke character over an imaginary quadratic field of odd discriminant, and splitting of every level prime. The BDP construction uses the weight-three form \(\theta_{\psi^2}\), the ramified field \(\mathbf Q(i)\), and the ramified character \(\psi'\). Their §1.5 explicitly lists odd weight and relaxed ramification/Heegner conditions as further cases. This is an application-scope observation, not a denial of their proven height formula.

## Bibliographic locators and read sources

- Massimo Bertolini, Henri Darmon, Kartik Prasanna, with appendix by Brian Conrad, *p-adic L-functions and the coniveau filtration on Chow groups*, J. reine angew. Math. 731 (2017), 21--86, DOI 10.1515/crelle-2014-0150. Read author PDF: https://sites.lsa.umich.edu/kartikp/wp-content/uploads/sites/1326/2024/07/BDP5-hl.pdf ; §1 p.6, §5.2 pp.24--27, especially the local conductor discussion pp.24--25 and displayed root-number formulas p.27.
- LMFDB, newform 64.4.a.c: https://www.lmfdb.org/ModularForm/GL2/Q/holomorphic/64/4/a/c/ . CM field, conductor, weight, Fricke sign, and first coefficients directly read; the database's numerical analytic rank is not a proof input.
- David T.-B. G. Lilienfeldt and Ari Shnidman, *Derivatives of Rankin--Selberg L-functions and heights of generalized Heegner cycles*, arXiv:2408.04375; read primary PDF https://perso.pages.math.cnrs.fr/users/david.lilienfeldt/arXivGZGHC.pdf ; Theorem 1.1 p.2 and §1.5 p.5.

Self-check: conductor product on \(1+\mathfrak q^3\), weight/conductor normalization, Fricke factor \(N^2\), Mellin derivative factor \(2\), gamma cancellation at the zero, integration-by-parts kernel, coefficient growth, vanished first terms, geometric-series tail, and \(2/3-19/60=7/20\) have each been checked. This is a written proof with a supplementary arithmetic interval check, not a formal proof-assistant certificate.
