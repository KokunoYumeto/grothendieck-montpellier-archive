# Cubic Kummer host: finite character, splitting transport, and an explicit CM tower

**Run:** ALP_MACHINE, question 3. **Author:** GPT-6 Astra Pro; inherited effort not separately exposed; child /root/kummer_extension. **Date:** 2026-11-21. **Companion:** kummer_extension.md, AM-K000–AM-K006. This addendum proves smaller arithmetic and geometric subgates. It does not assert the Kummer RH window or an instance of the archive's complete HostRaw/MainX records.

The inputs already accepted in the main contribution retain their status. In particular the conductor table AM-K003, the elliptic Hom realization AM-K004, the field-independent analytic adapter AM-K005, and CX-ALG-024 are used without reopening the stipulated Dirichlet theorem. The new field called $B_n$ below is a CM coefficient/endomorphism field; it is not the non-CM Kummer splitting field $K(p^{1/3})$.

## 1. AM-K007: an explicit finite ray-class host for every allowed cubic prime

Put $K=\mathbf Q(\zeta)$, $\zeta=\zeta_3$, $\mathcal O=\mathbf Z[\zeta]$, and $\lambda=1-\zeta$. The ring $\mathcal O$ is norm-Euclidean, has class number one, and has units $\mu_6$. We use these established elementary facts; the source is Murty and Esmonde (2005), §2.3, Exercise 2.3.2 and its solution, together with §9.1. The norm is
\[
N(a+b\zeta)=a^2-ab+b^2.
\]

### 1.1. The case $p\ne3$, necessarily $p\equiv2\pmod3$

The reduction map
\[
\mu_6\longrightarrow(\mathcal O/(3))^\times
\]
is an isomorphism. The target has order $9-3=6$. The only unit congruent to $1$ modulo $(3)=(\lambda^2)$ is $1$: the nontrivial cube roots have $\lambda$-adic difference from $1$ of valuation one, and reduction modulo $\lambda$ distinguishes the two possible signs. Thus every $a$ prime to $3$ has a unique unit $\epsilon(a)$ with $\epsilon(a)\equiv a\pmod3$. Define $a^\circ=a/\epsilon(a)$.

For the modulus $\mathfrak m=(3p)$, the ray-class exact sequence and class number one give
\[
\operatorname{Cl}_{(3p)}(K)
 \simeq
 \bigl((\mathcal O/(p))^\times\times
             (\mathcal O/(3))^\times\bigr)/\mu_6
 \simeq \mathbf F_{p^2}^{\,\times}.
\tag{H1}
\]
The last map sends the ideal class of $(a)$, with $a$ prime to $3p$, to $a^\circ\bmod p$. It is independent of the generator: if $u\in\mu_6$, then $\epsilon(ua)=u\epsilon(a)$. Every residue class can be represented using the Chinese remainder theorem. The kernel is exactly the principal ideals with a generator congruent to $1$ modulo $3p$. This proves the displayed isomorphism, including its explicit formula. The exact sequence being used is Milne (2020a), V, Theorem 1.7, pp. 150–151.

Identify the three cube roots in $\mathbf F_{p^2}$ with $\mu_3\subset\mathbf C$ by the reduction of the fixed $\zeta$. Then
\[
\eta_p((a))=
 \left((a^\circ\bmod p)^{(p^2-1)/3}\right)^{\!\uparrow}
\tag{H2}
\]
is a nontrivial order-three ray-class character. The superscript means the inverse of the chosen reduction identification, not an arbitrary numerical logarithm.

The primitive Kummer character $\chi_{p,3}$ has conductor dividing $(3p)$ by AM-K003 and has exact order three. A cyclic group has exactly two nontrivial characters of order three, which are inverses. Therefore
\[
\chi_{p,3}=\eta_p\quad\hbox{or}\quad\eta_p^{-1}
\tag{H3}
\]
as ray-class characters, with the possible inverse accounting for the chosen Artin/Frobenius convention. AM-K001 proves that the two resulting L-functions are identical. Thus (H2) identifies the desired L-function without a new cubic-reciprocity input.

This also recovers the conductor distinction. The character descends to modulus $(p)$ exactly when the order-three character of $\mathbf F_{p^2}^\times$ is trivial on the image of $\mu_6$. Its restriction to $\mu_3$ is trivial exactly when $9\mid p^2-1$, or $p\equiv8\pmod9$ under the standing congruence. The order-two unit causes no condition for an order-three character. Hence the primitive modulus is $(p)$ in that case; otherwise AM-K003 gives $(p)\lambda^2=(3p)$. The argument includes $p=2$; no injectivity of $\mu_6\to\mathbf F_{p^2}^\times$ was assumed.

Complex conjugation acts on (H1) by $z\mapsto z^p$. Since $p\equiv-1\pmod3$, it acts on $\eta_p$ by inversion, as required.

### 1.2. The wild case $p=3$

For $\mathfrak m=(9)=\lambda^4$, normalize again by the unique unit modulo $3$. This gives
\[
\operatorname{Cl}_{(9)}(K)
 \simeq (1+3\mathcal O)/(1+9\mathcal O)
 \simeq (\mathcal O/3\mathcal O,+)
 \simeq (\mathbf Z/3\mathbf Z)^2.
\tag{H4}
\]
The middle map is $1+3u\mapsto u\bmod3$; multiplication becomes addition because the cross term is divisible by $9$. It is bijective, and the unit normalization proves the first isomorphism.

Write $u=a+b\zeta$ modulo $3$. Conjugation sends $(a,b)$ to $(a-b,-b)$. A character of this additive group has the form $\zeta^{sa+tb}$. It is anti-invariant precisely when
\[
s(a-b)+t(-b)=-sa-tb\quad\text{for every }a,b,
\]
which is equivalent to $s=0$. Thus the two nontrivial anti-invariant characters are
\[
\eta_3(1+3(a+b\zeta))=\zeta^b,\qquad \eta_3^{-1}.
\tag{H5}
\]
The actual Kummer character has conductor $(9)$ and is anti-invariant, by AM-K002 and AM-K003. It must be one of these two. Again AM-K001 identifies their L-functions. This explicitly includes the wild conductor; it is not a tame specialization.

### 1.3. Character separation and the ideal-indexed Dirichlet series

Let $H=\operatorname{Cl}_{\mathfrak m}(K)$ with the modulus just used. Its regular module over $\mathbf Q(\zeta)$ has the exact projector
\[
e_{\eta}=\frac1{|H|}\sum_{h\in H}\eta(h)^{-1}[h].
\tag{H6}
\]
Translation by an ideal class $[\mathfrak a]$ acts on its image by $\eta(\mathfrak a)$. The elementary identity
\[
1+\eta(h)+\eta(h)^{-1}
   =3\,\mathbf 1_{\eta(h)=1}
\tag{H7}
\]
gives the complete finite character separation. These statements follow directly by changing the index in (H6) and summing the three roots of unity.

A smaller integral realization uses the quotient $H/\ker\eta\simeq C_3$: the rank-two augmentation representation has trace $2$ on the identity and $-1$ otherwise. Over $\mathbf Q(\zeta)$ it splits as $\eta\oplus\eta^{-1}$. The projector onto one line uses division by $3$, so an integral construction must retain that denominator; (H6) is not asserted to be an integral idempotent at primes dividing $|H|$.

For $\Re s>1$, the ray-modulus L-function is exactly
\[
L_{\mathfrak m}(s,\eta)
 =\frac16\sum_{(a,b)\in\mathbf Z^2\setminus\{(0,0)\}}
 \frac{\eta((a+b\zeta))}{(a^2-ab+b^2)^s},
\tag{H8}
\]
where the numerator is zero when $(a+b\zeta)$ is not coprime to $\mathfrak m$. Each nonzero integral ideal has precisely six generators, which proves the formula by absolute convergence. This is a concrete ideal-indexed host. It does not turn the series into a rational Dirichlet L-function.

### 1.4. The harmless extra Euler factor is harmless for the actual window

When $p\equiv8\pmod9$, the convenient modulus $(3p)$ omits the unramified Euler factor at $\lambda$ of norm $3$. Since $\lambda$ is fixed by conjugation and the character is odd-order and anti-invariant, $\chi(\lambda)=1$.

More generally, remove an unramified Euler factor of norm $q>1$ and value $u$, $|u|=1$:
\[
L_{\rm imp}(s)=(1-uq^{-s})L_{\rm prim}(s).
\]
Use the same normalized ramp as AM-K005 for each function, including its own constant $L'/L(1)$. With $J=\lfloor\log_q x\rfloor$, direct subtraction gives
\[
G_{\rm imp}(x)-G_{\rm prim}(x)
 =\log q\left(
     \sum_{k=1}^{J}u^k+
     \frac{x(u/q)^{J+1}}{1-u/q}
            \right).
\tag{H9}
\]
Indeed the removed prime powers subtract
$\log q\sum_{k\le J}u^k(x/q^k-1)$, and the change in $L'/L(1)$ adds
$x\log q\sum_{k\ge1}(u/q)^k$. Their finite sums cancel to (H9). Consequently the difference is $O(1+\log x)$ for fixed $q$.

For the present real-valued ramps, their AM-K005 windows $W(\theta,\delta)$ are equivalent for every $\theta>0$. To prove this with the actual quantifiers, start with a majorant for one ramp at exponent $\eta/2$, and add $C(1+\log x)$ to majorize the other. The added integral over $[Y,Y^{1+\delta}]$ is at most
\[
C\int_Y^\infty (1+\log x)x^{-\theta-1}\,dx
=O_\theta(Y^{-\theta}(1+\log Y)).
\]
Increase the prescribed lower threshold so that this and $Y^{\eta/2}$ are each at most $Y^\eta/2$. The same argument reverses the roles. Thus the explicit nonminimal modulus in (H1) introduces no new analytic gate.

**Closed subgate.** For all allowed cubic $p$, the finite ray-class group, the actual character up to its L-equivalent inverse, its character projector, and the ideal-indexed L-series are explicit. No Kummer extension has been inserted as a CM field.

## 2. AM-K008: the Kummer character is an admissible splitting twist

This statement works for every odd $r$, not only $3$. Put $K^+=\mathbf Q(\zeta_r+\zeta_r^{-1})$, let $c$ denote CM conjugation, and let $\chi$ be the finite-order Kummer Hecke character. AM-K002 gives $\chi^c=\chi^{-1}$.

For $a\in\mathbb A_{K^+}^{\times}$, conjugation fixes $a$, so $\chi(a)^2=1$. Its order also divides the odd number $r$, hence
\[
\chi|_{\mathbb A_{K^+}^{\times}}=1.
\tag{H10}
\]
At infinity it is trivial because a continuous finite-order character of each connected group $\mathbf C^\times$ is trivial.

Let $T=\operatorname{Res}_{K/K^+}^{1}\mathbf G_m$ and choose $j$ with $2j\equiv1\pmod r$, for example $j=(r+1)/2$. On $T(\mathbb A_{K^+})$ define
\[
\nu(z)=\chi(z)^j.
\]
It is unitary, continuous, finite-order, and trivial on $T(K^+)\subset K^\times$. Moreover
\[
\nu(x/cx)=\chi(x)^{2j}=\chi(x).
\tag{H11}
\]
For $r=3$, one can take $j=2$. For a unitary group $U(S)$ write
$\nu_S(g)=\nu(\det g)$.

### 2.1. Exact transport of the oriented Weil record

Suppose an actual oriented Weil datum over the CM extension $K/K^+$ is given, with splitting characters $\chi_S,\chi_T$ and action $\omega$. Let $a,b\in\mathbf Z$. Set
\[
\chi_S'=\chi_S\chi^a,\qquad
\chi_T'=\chi_T\chi^b,\qquad
\omega'(g,h)=\nu_S(g)^{-b}\nu_T(h)^a\,\omega(g,h).
\tag{H12}
\]
Then it satisfies the same oriented Weil-datum conditions, with the new splitting characters, on the same Heisenberg space and with the same additive character.

Here is a check of every field in the actual source record, not just an appeal to the name of the representation. In LocalNewformFunction.lean, the record IsWeilDatumO is at lines 53–75.

- **std:** the additive character is unchanged.
- **hecS, hecT, resS, resT:** products remain Hecke characters; (H10) preserves the prescribed restriction to the real subfield.
- **om_pres:** a constant scalar multiple preserves each defining quasi-periodicity, level, continuity and archimedean smoothness condition of IsThetaFunO.
- **om_heis:** the scalar commutes with every linear Heisenberg operator, leaving the same symplectic action.
- **om_aut:** on rational unitary elements the determinants lie in $T(K^+)$, where $\nu=1$.
- **om_cont:** the new scalar is continuous; it multiplies the old continuous matrix coefficient.
- **om_unit:** the scalar has absolute value one, so every displayed squared-norm integral is identical.
- **om_split:** the source splitting factor, line 51, is
  $\chi_T(x)^{-1}\chi_S(y)$. The new factor is this times
  $\chi(x)^{-b}\chi(y)^a$. For a source determinant root, $x/cx=\det g$ and $y/cy=\det h$, so (H11) makes these exactly the scalar in (H12). The same positive real constant works.

For the last check, the source's split-place definition IsDetAt, TiedWeil.lean:77, also implies the determinant-root identity. At the selected idempotent $e$ it reads $x=e\det g+(1-e)$; the supported unitary element is the identity off $e+ce$ and satisfies $c(\det g)=(\det g)^{-1}$. Multiplying in the two orthogonal idempotent components gives $x/cx=\det g$.

Multiplication by the scalar character also preserves the group-homomorphism property of $\omega$, so the ambient type of the new action is correct. This completes the transport proof.

The related actual interface TiedWeil.lean:64,83–96 defines IsDetRoot and TwRule. Its four formulas explicitly permit a splitting-character change with trivial restriction to the real base, with the sign reversed on the reversed-rank edge. TwRule requires its character to belong to the supplied family X.Chr; membership of the new character in an existing family is not deduced from that record. Formula (H12) uses the oriented convention splitFacO, and therefore keeps its signs fixed. A reversal must use the source's corresponding formula rather than silently reuse a sign.

### 2.2. Level and integral scope

The archimedean representation and archimedean norms are unchanged. At a finite place where $\chi$ is unramified, $\nu_S$ is trivial on every compact subgroup of $U(S)$: compact determinant images have zero valuation, and an unramified character is trivial on local units. At each remaining place, replacing a compact level $U_v$ by $U_v\cap\ker\nu_S$ costs group index at most $r$.

For $r=3$, only the rational places $p,3$ can contribute. Thus the product of these elementary local kernel indices is at most $9$ for $p\ne3$, and at most $3$ for $p=3$. This is solely the index needed to kill this one character on a given level. It is not the complete adelic covolume, a Hecke-orbit count, or the cost of the archive's arithmetic columns. Root-of-unity multiplication preserves an integral coefficient lattice when that lattice is a module over a ring containing those roots; projectors and saturation may introduce further denominators.

**Closed subgate.** The target character has exactly the relative restriction needed for the archive's splitting-change formulas. This is an actual transport theorem for a supplied Weil datum. It does not manufacture the required D7 datum or the global arithmetic theta comparison.

## 3. AM-K009: coherent twists telescope and identify the remaining comparison

Fix a chain of groups $G_0,\ldots,G_m$ and kernels $K_i(g_i,g_{i+1})$. State the convention explicitly:
\[
(\Theta_i f)(h)=\int_{[G_i]}K_i(g,h)f(g)\,dg,
\]
on any function space where these integrals exist. Let $\nu_i$ be the determinant character from AM-K008 and $t_i\in\mathbf Z$. Define $M_i f=\nu_i^{t_i}f$ and
\[
K_i'(g,h)=\nu_i(g)^{-t_i}\nu_{i+1}(h)^{t_{i+1}}K_i(g,h).
\]
Then
\[
\Theta_i'=M_{i+1}\Theta_iM_i^{-1},\qquad
\Theta_{m-1}'\cdots\Theta_0'
 =M_m(\Theta_{m-1}\cdots\Theta_0)M_0^{-1}.
\tag{H13}
\]
Both formulas follow by substitution and cancellation of the adjacent multiplication operators. With a convention conjugating the input function, the corresponding powers are conjugated; the same cancellation remains. Each $M_i$ is unitary on $L^2$, and therefore norms and pairings of simultaneously transported vectors are unchanged.

Consequently, coherent splitting transport alone supplies no new prime-weighted arithmetic identity. It gives isomorphic analytic operators and the transported endpoints. To obtain the new explicit-formula functional one must identify a character-dependent arithmetic column, Hecke action or endpoint that carries (H2)/(H5), and verify its integral structure and its actual cost.

This distinction can be seen in the checked source, rather than inferred from broad terminology:

| Actual source interface | What it contains | What (H12) supplies |
|---|---|---|
| LevChiEqOne.lean:23–64, TwDat and TwDat.Is | Level charts, stabilizers, arithmetic representatives, determinant roots, and the exact character relation to the common family | The permitted determinant character; it does not construct the charts or representatives |
| Same file:73–77, abelian₂ | A prescribed product of arithmetic scalar factors times jetL of the actual abelian theta section | No new equality with a prime sum follows from scalar transport |
| Same file:87–101, VacT and PinX | The moved-vacuum theta identity, its nonzero constant, fixed positive lattice pin, and the entire family of matching characters | Once supplied, the splitting factors transform by (H12); the arithmetic identity still needs proof for the new family |
| Same file:103–115, PinColT | Finite combination datum, rational datum, and a constant combining the level volume, arithmetic weights, vacuum constant and determinant-root evaluations | Individual phase factors are explicit; the full nonzero constant and covolume are not evaluated here |
| CharacterBoxes/Supply.lean:10,42 | FReq is a predicate on Scale, Frame and HostAx; GChi adds EAtH and VVle | “Generic request” is generic only within this HostAx domain, not over arbitrary CM fields |

A precise remaining task is therefore the **twisted arithmetic comparison** for the explicit ray-class character and the actual CM lattice below: construct the arithmetic section and prove that its functional is AM-K005's $G_\chi$, with all local multiplicities, conductor factors and integral denominators. That is narrower than leaving the character, finite host and local splitting laws unspecified. It still includes a substantive theorem; this report does not rename it as a proved window.

## 4. AM-K010: an explicit CM supply tower with the induced cubic type

The previous finite host is a ray-class group, whereas the geometric construction also requires a CM field, polarization and lattice. The following explicit tower supplies several precise HostDer-shaped ingredients while keeping the Kummer character in the descent of a CM abelian variety.

### 4.1. A criterion for the invariant half-different

Let $B/K$ be a finite Galois extension of a CM field $K$, with $B$ CM and conjugation $c$ restricting to conjugation of $K$. Write $\mathfrak D=\mathfrak D_{B/K}$. There exists a Gal$(B/K)$-stable integral ideal $\mathfrak b$ with
\[
\mathfrak D=\mathfrak b\,c(\mathfrak b),\qquad
\mathfrak b+c(\mathfrak b)=\mathcal O_B
\tag{H14}
\]
if and only if $B/K$ is unramified at every finite prime $\mathfrak q$ of $K$ fixed by $c$.

For necessity, let $\mathfrak q=c\mathfrak q$. The Galois group is transitive on primes above $\mathfrak q$, so stability makes the valuation of $\mathfrak b$ the same integer at all those primes. Conjugation permutes the same set, so $c(\mathfrak b)$ has the same valuation there. Coprimality forces that integer to be zero, hence $\mathfrak D$ has valuation zero at all these primes. A finite number-field extension is unramified at a prime exactly when its local different is trivial.

For sufficiency, partition the non-conjugation-fixed primes in the support of the relative discriminant into pairs $\{\mathfrak q,c\mathfrak q\}$, and choose one member of every pair. Put into $\mathfrak b$ all prime factors of $\mathfrak D$ above the chosen members, with their full different exponents. Since the extension is Galois, $\mathfrak D$ and this choice are Gal$(B/K)$-stable. Conjugation preserves the relative different and supplies precisely the complementary factors. This proves (H14). No class-number-one assumption on $B$ is required.

For $K=\mathbf Q(\zeta_3)$, both the prime over $2$ and the prime over $3$ are conjugation-fixed. Thus an induced-type invariant half-different of this form excludes relative ramification at $2$ or $3$. In particular a literal relative extension ramified at $2$, as in an added nontrivial real $2$-power cyclotomic tower, cannot have all these properties with this distinguished $K$. This is a specific obstruction to retaining the archive's $2$-adic tower, not an obstruction to all CM host fields containing $K$.

### 4.2. The explicit tower

For each $n\ge1$ set
\[
B_n=\mathbf Q(\zeta_{3\cdot7^n})
   =K(\zeta_{7^n}),\quad
d_n=6\cdot7^{n-1},\quad
a_n=7^{n-1}(6n-1).
\tag{H15}
\]
Then $[B_n:K]=d_n$, and $B_n$ is a Galois CM field of degree $2d_n$. Its Galois group over $\mathbf Q$ is
\[
(\mathbf Z/3\mathbf Z)^\times
 \times(\mathbf Z/7^n\mathbf Z)^\times.
\]
Complex conjugation is $(-1,-1)$. At $3$, inertia is contained in the first factor; at $7$, it is contained in the second; away from $3,7$ it is trivial. Conjugation is in neither of the two nontrivial inertia groups. The inertia group for $B_n/B_n^+$ is their intersection with $\{1,c\}$, and is therefore trivial at every finite prime. Hence
\[
B_n/B_n^+\ \text{is everywhere unramified at finite primes}.
\tag{H16}
\]

The prime $7$ splits in $K$:
\[
(7)=(3+\zeta)(3+\zeta^2).
\]
The two factors have norm $7$ and are distinct. Each ramifies totally in $B_n/K$, yielding primes $P_n,cP_n$ of residue degree one and ramification degree $d_n$. There is no other relative ramification.

The local ring is generated by $\zeta_{7^n}$. The derivative of
\[
\Phi_{7^n}(X)=\frac{X^{7^n}-1}{X^{7^{n-1}}-1}
\]
at this root has valuation
\[
n\,d_n-7^{n-1}=a_n,
\]
because $v_{P_n}(7)=d_n$ and
$v_{P_n}(\zeta_{7^n}^{\,7^{n-1}}-1)=7^{n-1}$. The monogenic different formula therefore gives
\[
\mathfrak D_{B_n/K}=P_n^{a_n}(cP_n)^{a_n}.
\tag{H17}
\]
Thus $\mathfrak b_n=P_n^{a_n}$ is Gal$(B_n/K)$-stable and satisfies (H14). This is a fully specified half-different, not an existence assertion for an unspecified field.

Discriminant transitivity and (H16) yield
\[
|D_{B_n}|=3^{d_n}7^{2a_n},\qquad
D_{B_n^+}=3^{d_n/2}7^{a_n},\qquad
\operatorname{rd}(B_n)=\sqrt3\,7^{\,n-1/6}.
\tag{H18}
\]
The roots of unity in $B_n$ are exactly $\mu_{6\cdot7^n}$. One elementary check is by ramification: any root order can involve only $2,3,7$; a factor $4$ would ramify at $2$, a factor $9$ would require ramification index at least $6$ at $3$ instead of $2$, and a higher $7$-power would require larger ramification index at $7$. The stated roots already lie in $B_n$.

Every one of these roots has relative norm one to $K$. Indeed
\[
N_{B_n/K}(-1)=1,\quad
N_{B_n/K}(\zeta_3)=\zeta_3^{d_n}=1,\quad
N_{B_n/K}(\zeta_{7^n})=1.
\tag{H19}
\]
The last equality is the constant term of the even-degree cyclotomic polynomial. These three roots generate the full group. This verifies the actual norm-of-roots condition, not the stronger and false assertion that $B_n$ has only $\pm1$ as roots.

The cyclotomic facts used here are Milne (2020c), Theorem 6.4, printed p. 99 (PDF p. 101), and Remark 6.6(b), printed p. 100 (PDF p. 102), together with the elementary local cyclotomic derivative computation displayed above. The prime splitting and all discriminant exponents have been shown explicitly.

### 4.3. A positive self-dual Hermitian lattice

Set
\[
L_n=\mathfrak b_n^{-1},\qquad
h_n(x,y)=\operatorname{Tr}_{B_n/K}(x\,c(y)).
\tag{H20}
\]
It is a free $\mathcal O_K$-module of rank $d_n$, because $\mathcal O_K$ is a PID. Its Hermitian dual is
\[
L_n^\#=\mathfrak D_{B_n/K}^{-1}\,(cL_n)^{-1}
       =(\mathfrak b_n c\mathfrak b_n)^{-1}c\mathfrak b_n
       =\mathfrak b_n^{-1}=L_n.
\tag{H21}
\]
The first equality follows from the definition of the inverse different as the trace-dual of $\mathcal O_{B_n}$, extended to fractional ideals; it can also be checked after localization at each prime. Thus $h_n$ is integral and unimodular on $L_n$.

Choose the CM type $\Phi_n$ consisting of the $d_n$ embeddings extending a fixed embedding $K\hookrightarrow\mathbf C$. Then
\[
h_n(x,x)=\sum_{\sigma\in\Phi_n}|\sigma(x)|^2
\]
under that embedding, so the form is positive definite. Choose an $\mathcal O_K$-basis and use the matrix convention $h_n(x,y)=\bar y^{\,t}H_nx$ for coordinate columns. Then $H_n$ is integral Hermitian and invertible over $\mathcal O_K$. Its determinant is a positive rational unit, hence $1$.

This exactly supplies the mathematical shape of HostDer.principal and HostDer.unimodular for this induced type, together with the unramified CM quotient and discriminant square. It supplies them as new mathematical objects, not as an instance of the existing parameterized HostRaw record.

### 4.4. Actual CM abelian varieties and the cubic Hom line

Use the elliptic curves from AM-K004:
\[
A_0:y^2=x^3+1,\qquad A_p:y^2=x^3+p^2.
\]
Both have $\mathcal O_K$-endomorphisms over $K$. The chosen $\mathcal O_K$-basis of $L_n$ realizes multiplication by $\mathcal O_{B_n}$ as a subring of $M_{d_n}(\mathcal O_K)$. Consequently it acts, over $K$, on the actual products
\[
\mathcal A_{0,n}=A_0^{d_n},\qquad
\mathcal A_{p,n}=A_p^{d_n}.
\]
Give each product the polarization represented relative to its product principal polarization by the same positive integral Hermitian matrix $H_n$. This is a principal polarization: positivity is the Riemann-form criterion, and unimodularity makes the polarization morphism an isomorphism. The entries are endomorphisms defined over $K$, so the morphism is defined over $K$. The adjoint of multiplication by $b\in B_n$ for $h_n$ is multiplication by $c(b)$, proving that Rosati induces CM conjugation.

For completeness, the complex construction can be written directly as
\[
\mathbf C^{\Phi_n}/\Phi_n(L_n).
\]
Choose $\xi=-1/\sqrt{-3}$ with the fixed embedding $\sqrt{-3}\mapsto i\sqrt3$, so $\operatorname{Im}\sigma(\xi)>0$ for $\sigma\in\Phi_n$. The alternating form
$\operatorname{Tr}_{B_n/\mathbf Q}(\xi x c(y))$
is integral, positive in the Riemann convention and self-dual: the inverse different of $K/\mathbf Q$ is generated by $\xi$, and (H21) handles the relative trace. This produces the same polarized isomorphism class over $\mathbf C$ as the Hermitian matrix construction, after scaling the common elliptic period. The Riemann-form and CM-pair framework is Milne (2020b), §2, Example 2.9, Example 2.11, and Proposition 3.17; Proposition 3.12 describes the induced CM isogeny type.

The coordinatewise isomorphism
\[
g_p^{d_n}:\mathcal A_{p,n}\longrightarrow\mathcal A_{0,n}
\]
over $K(p^{1/3})$ is $\mathcal O_{B_n}$-linear because the scalar elliptic twist commutes with every matrix over $\mathcal O_K$. It respects the displayed polarizations for the same reason. Its descent cocycle is the scalar $\chi_{p,3}$ in $\mathcal O_K^\times\subset\mathcal O_{B_n}^\times$.

On any one-dimensional $B_n$-eigensummand of $H^1$ extending the chosen $\zeta$-eigensummand over $K$, the ratio of the two Galois characters is therefore exactly $\chi_{p,3}$, by the AM-K004 intertwining computation. Thus the explicit rank-one Artin Hom line survives in a principally polarized CM model with the lattice (H20). The splitting field is used only to trivialize the descent cocycle; it is not asserted to be a CM field.

The stable Faltings heights of the underlying products are
\[
h_{\rm Fal}(\mathcal A_{0,n})=d_n h_{\rm Fal}(A_0),\qquad
h_{\rm Fal}(\mathcal A_{p,n})=d_n h_{\rm Fal}(A_0).
\tag{H22}
\]
This uses additivity for products and the geometric isomorphism of $A_p$ and $A_0$. It is independent of the chosen principal polarization. It is not an evaluated theta-lift cost: derivatives, indices, normalized kernel constants and saturation still have to be computed. In particular, on the $d_n$-dimensional $\zeta$-eigenspace the determinant twist is $\chi_{p,3}^{d_n}=1$ because $3\mid d_n$, while each chosen $B_n$-eigensummand still has nontrivial character; a determinant or height alone does not recover that summand.

### 4.5. Precisely which source requirements have and have not been supplied

| Source requirement | Supplied here | Remaining difference |
|---|---|---|
| ConjEMemHostFIff.lean:89,95, CM field and CM type | $B_n$ and the type induced from $K$ | The original record has its own Frame and distinguished quadratic-field parameters |
| Same file:135, finite unramified CM quotient | (H16) | Proven for the new tower, not transported through HostRaw |
| Same file:156, invariant coprime half-different | (H17), $\mathfrak b_n=P_n^{a_n}$ | Its tower prime is $7$; retaining ramification at inert $2$ violates §4.1 |
| Same file:159, unimodular trace lattice | (H20)–(H21) | Actual later arithmetic columns still need matching to this lattice |
| Same file:163, discriminant square | (H18) | The full source root-discriminant inequalities depend on its different parameters |
| Same file:170, norm of every root of unity is one | (H19) | Its separate stronger MuPM predicate fails here; no use of that predicate may be carried silently |
| Main CM abelian variety and cubic eigensummand | Actual $\mathcal A_{0,n},\mathcal A_{p,n}$ with principal polarizations and the Hom line | No full MainX chain, terminal vector or normalized period has been constructed |
| ExistsPageN.lean:19,39 and Supply.lean:42 | No literal instance claimed | The original cyclotomic subgroup, $2$-adic PageN scale, character-specific EAtH and cohomology supply require a $7$-adic/relative replacement |

The phrase “generic CM theory” therefore conceals two separate issues: several geometric objects now exist explicitly, but the original rational congruence/tower supply and its arithmetic prime functional are not consequences of that existence.

## 5. AM-K011: the actual generic field record and its finite-place boundary

The source contains a geometric field interface weaker than HostRaw. It can be supplied completely at the level of mathematical data. This closes a named source input; the source's arithmetic character family still needs a separate extension.

### 5.1. A degree-divisibility adjustment using a second split prime

Set
\[
B_n^*=\mathbf Q(\zeta_{3\cdot7^n\cdot13}),\qquad
F_n^*=(B_n^*)^+,\qquad
f_n=[B_n^*:K]=72\cdot7^{n-1}.
\tag{H23}
\]
The extra prime $13$ splits in $K$, since
$(13)=(4+\zeta)(4+\zeta^2)$. Cyclotomic disjointness gives the displayed degree, so $8\mid f_n$. The CM quotient $B_n^*/F_n^*$ is unramified at all finite primes: inertia at $3$, $7$ or $13$ is confined to that factor of the cyclotomic Galois group, whereas conjugation is $-1$ in all three factors. Thus it lies in none of the inertia groups.

Relative ramification over $K$ is confined to the two split rational primes $7,13$. The half-different criterion in AM-K010 applies. More explicitly, choose the primes $(3+\zeta)$ and $(4+\zeta)$ of $K$, and put
\[
\mathfrak b_n^*
  =\prod_{P\mid(3+\zeta)}P^{a_n}
     \prod_{Q\mid(4+\zeta)}Q^{11}.
\tag{H24}
\]
Adjoining the other prime-power roots is unramified locally, so the different exponent at $7$ remains $a_n$ and that at $13$ is the tame exponent $12-1=11$. This proves
$\mathfrak D_{B_n^*/K}=\mathfrak b_n^*c(\mathfrak b_n^*)$ with coprime, Gal$(B_n^*/K)$-stable halves. Its inverse is therefore again a free positive unimodular Hermitian $\mathcal O_K$-lattice, now of rank $f_n$. All the principally polarized product and Artin Hom constructions of §4.4 apply with this lattice.

The roots of unity are $\mu_{6\cdot7^n\cdot13}$. Their relative norms are one: the norm of $\zeta_3$ is one because $3\mid f_n$; the norms of primitive $7^n$-th and $13$-th roots are powers of the constant terms of their even-degree cyclotomic polynomials; and $f_n$ is even. Coprime-conductor discriminant multiplication gives
\[
|D_{B_n^*}|=3^{12d_n}7^{24a_n}13^{22d_n},
\qquad
\operatorname{rd}(B_n^*)=\sqrt3\,7^{\,n-1/6}13^{11/12}.
\tag{H25}
\]
Thus satisfying the degree condition does not require introducing relative ramification at inert $2$.

### 5.2. Every field of AbelianUnramifiedExtensionConditions

The exact file is Formalism/LocalToGlobal/Columns/AbelianHostFieldConditions.lean. Its Fields structure is at lines 19–42, Fields.Ok at lines 81–108, and AbelianUnramifiedExtensionConditions at lines 110–120. To avoid its letter K being confused with the fixed quadratic field, denote its coefficient field by $C$.

Choose the source fields
\[
X.F=F_n^*,\qquad X.E=B_n^*,\qquad C=X.K=B_n^*,
\]
with their natural embeddings and conjugations. Take
$X.\mathrm{Tau}=\operatorname{Gal}(B_n^*/K)$, and let its embeddings be the corresponding automorphisms of $B_n^*$. Then every Fields.Ok condition holds:

- **realF, rankE, star_F, conjE, cplxE:** these are the CM-field identities for $B_n^*/F_n^*$.
- **emb_star:** the cyclotomic automorphisms commute with conjugation.
- **card_Tau:** the cardinal is $f_n=[F_n^*:\mathbf Q]$.
- **emb_inj:** distinct automorphisms are distinct embeddings.
- **emb_ne:** an embedding fixing $K$ cannot equal a conjugated one, whose restriction to $K$ is nontrivial.
- **emb_all:** every embedding $B_n^*\to B_n^*$ is a Galois automorphism. Its restriction to $K$ is either identity or conjugation, so it lies in the chosen set or its conjugate.
- **cplxK, normalK, conjK:** the coefficient field $C=B_n^*$ is a normal CM field, with its displayed complex embedding and conjugation.
- **quad:** the source's Kq consists of elements whose images under all chosen embeddings agree. Since the identity embedding occurs, this is the fixed field of Gal$(B_n^*/K)$, hence precisely $K$ and of rational degree two.

The remaining AbelianUnramifiedExtensionConditions fields are **eight_dvd**, proved by (H23); **galE** and **abelE**, from cyclotomy; and **unram**, proved above. For the last field, the source ideal inequality is the ramification-index-one condition, exactly the finite unramified CM quotient already checked.

This constructs all mathematical data and proofs for that named record. It is not a Lean term or a build certificate. A larger normal cyclotomic coefficient field $C\supset B_n^*$ may be used when finite character values require it: all embeddings of the normal field $B_n^*$ still have their images in $B_n^*$, so the same verification applies.

### 5.3. Why the target is still outside the particular tame split-prime family

In the same file, IsMu0 at lines 314–320 requires a character to be unramified away from the two auxiliary rational primes $g_i$, and tame everywhere. The preceding Primes.Ok record requires all the selected primes over $g_i$ to have absolute norm $g_i$ (lines 216–218), and QDat.Ok requires its primes to have prime absolute norm (line 347). These are substantive degree-one restrictions.

For $p\ne3$ under the present hypothesis, $p\equiv2\pmod3$ is inert in $K$. Therefore every prime $P$ over $p$ in every number field containing $K$ has
\[
f(P/p)\ge2,\qquad NP=p^{f(P/p)},
\]
so no such prime has prime absolute norm. AM-K003 says that $\chi_{p,3}$ ramifies at the prime $(p)$ of $K$. The extension $B_n^*/K$ is unramified at $p$, because $p$ is neither $7$ nor $13$. The pulled-back character on $B_n^*$ remains ramified: an unramified local extension leaves the inertia subgroup unchanged. Hence it cannot be placed solely in the displayed degree-one support.

At the prime above $3$, the cases with conductor $\lambda^2$ or $\lambda^4$ are wild. Indeed tame inertia at residue characteristic $3$ has no nontrivial quotient of order three, whereas these order-three characters are ramified. In (H23) the relative extension is unramified at $3$, so the same obstruction persists after pullback. Thus all cases except $p\equiv8\pmod9$ require a wild local character as well. In the exceptional congruence case the prime over $3$ is unramified, but the inert-$p$ degree restriction remains.

Consequently the general splitting transport AM-K008 is valid, while inserting its character into these particular IsMu0/QDat families is not automatic. A relative arithmetic adapter must allow the actual degree-two prime over $p$, the wild conductor at $3$ when present, and the resulting norm and lattice factors. This statement concerns these named families; it does not assert that no other source construction can represent the character.

**Closed source input and surviving gate.** The geometric field predicate AbelianUnramifiedExtensionConditions has an explicit supply with $8\mid f$. The remaining work is the target's arithmetic character/column construction and its scale-uniform cost, with these precise nonsplit and wild local conditions retained.

## 6. Resulting reduced programme

For the cubic question, four concrete parts are now closed:

1. the target character and all its finite conductor cases have a complete ray-class model;
2. the character is an allowed finite-order unitary splitting change, with exact source signs;
3. an explicit growing CM tower has an invariant coprime half-different, a positive unimodular trace lattice, the required norm-of-roots property, and a variant satisfying every mathematical field in AbelianUnramifiedExtensionConditions;
4. actual principally polarized products of the cubic CM elliptic twists carry the selected Artin Hom line.

The remaining construction must place those objects in a relative arithmetic family, prove the exact equality between its arithmetic functional and AM-K005's normalized ideal-prime ramp, and compute its lift/period/lattice costs at all scales. The source's $2$-adic supply cannot simply be relabelled as the $7$-adic tower, and its displayed tame degree-one character family must be extended at the actual nonsplit and wild places. A successful estimate must give the window for every $\theta>1/2$; all the identities here are compatible with the present gate Q3-KUMMER-WINDOW remaining open.

## References and source provenance

- Alpöge, L. (2026). *Remark* and the stipulated Lean archive. https://alpo.ge/remark.pdf. Source files actually read: Formalism/LocalToGlobal/BesselHermitianTheta/TiedWeil.lean; Formalism/LocalToGlobal/IndefiniteReal/LocalNewformFunction.lean; Formalism/LocalToGlobal/Columns/AbelianHostFieldConditions.lean; Development/AbelianVarietyTheory/Definitions/LatticeFrames/LevChiEqOne.lean; Formalism/SharpRestriction/RamificationFrobenius/TotientGaloisClasses/ConjEMemHostFIff.lean; its InertiaGaloisSymmetry/OfRawToHostRaw.lean; Development/AutomorphicArithmetic/CharacterBoxes/Supply.lean and ExistsPageN.lean.
- Milne, J. S. (2020a). *Class field theory* (v4.03). V, Theorem 1.7, pp. 150–151. https://www.jmilne.org/math/CourseNotes/CFT.pdf.
- Milne, J. S. (2020b). *Complex multiplication* (v0.10). §2, Examples 2.9 and 2.11; Propositions 3.12 and 3.17; Proposition 6.1. https://www.jmilne.org/math/CourseNotes/CM.pdf.
- Milne, J. S. (2020c). *Algebraic number theory* (v3.08). §6, Theorem 6.4, printed p. 99 (PDF p. 101); Remark 6.6(b)–(c), printed pp. 100–101 (PDF pp. 102–103). https://www.jmilne.org/math/CourseNotes/ANT.pdf.
- Murty, M. R., & Esmonde, J. (2005). *Problems in algebraic number theory* (2nd ed.). Springer. §2.3, Exercise 2.3.2 and solution; §9.1. Author-hosted copy: https://www.math.toronto.edu/~ila/2005_Book_ProblemsInAlgebraicNumberTheor.pdf.
- Companion contribution: AM-K001–AM-K005 in kummer_extension.md. The earlier conductor, functional-equation, elliptic twist and analytic adapter proofs are incorporated by reference and not rederived here.

The archive was read from the shared pinned-source recovery, with its provenance files maintained by the parent, and from the child manifest for the earlier character files. No Lean compilation or newly formalized theorem is claimed by this addendum.

