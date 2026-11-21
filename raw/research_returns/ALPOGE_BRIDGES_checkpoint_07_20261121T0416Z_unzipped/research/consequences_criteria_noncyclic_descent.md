# An exact noncyclic rational descent monoid

**Scope and conventions.** Work in the rational numerical abelian--Artin--Tate categories \(\mathcal A_q\) already established in AQ.15 and CC-AG01. The simple-object, rank and Schur-index formulas are the inspected Milne classification used in CC-AG08--09, with its geometric-Frobenius local-invariant convention. Only the denominators of the invariants enter the indices below. The example is a complete deduction from those inputs and elementary number-field calculations; no novelty claim is made.

## CC-AG14 — Two copies and three copies descend, but one copy does not

Put

\[
 s^2=-23,\qquad K=\mathbf Q(s),\qquad
 \omega=\frac{1+s}{2},\qquad
 \eta=1+\omega=\frac{3+s}{2},
\]

\[
 \gamma=8\bar\eta=12-4s,\qquad
 \xi=[\gamma,9]\in\mathcal W_2,\qquad
 \beta=\gamma^3\in W(2^{27}).
 \tag{CC-AG.96}
\]

Let \(S_\xi\) be the geometric rational simple object of the orbit of \(\xi\), and let \(T_\beta\in\mathcal A_{2^{27}}\) be the rational simple object of the orbit of \(\beta\). Both have centre \(K\), Schur index \(3\), and rank \(6\), and \((T_\beta)_{\bar{\mathbf F}_2}\simeq S_\xi\).

For descent from the specified field \(\mathbf F_8\), both exact multiplicity monoids are

\[
 \begin{aligned}
 \{r\ge0:S_\xi^{\oplus r}
          \text{ comes from }\mathcal A_8\}
 &=\langle2,3\rangle_{\mathbf N},\\
 \{r\ge0:T_\beta^{\oplus r}
          \text{ comes from }\mathcal A_8\}
 &=\langle2,3\rangle_{\mathbf N}\\
 &=\{0\}\cup\{r\in\mathbf Z:r\ge2\}.
 \end{aligned}
 \tag{CC-AG.97}
\]

The second base extension is the finite extension \(\mathbf F_8\subset\mathbf F_{2^{27}}\) of degree \(9\).

Thus these monoids are **not cyclic**, although their group completions are \(\mathbf Z\). In particular a gcd or virtual-object criterion does not decide descent of actual objects. The stabilized exponent and geometric index are

\[
 h_\xi=9,\qquad d_\xi=3.
 \tag{CC-AG.98}
\]

The general necessary norm bound
\((h_\xi/d_\xi)/\gcd(h_\xi/d_\xi,3)=1\) is not sufficient in this example.

Here are two source simples realizing the generators. Choose \(\alpha_0^3=\gamma\), let \(\zeta_9\) be a primitive ninth root of unity, and put \(\alpha_1=\alpha_0\zeta_9\).

| Source label over \(\mathbf F_8\) | Degree of its centre over \(K\) | Source Schur index | Rank | Multiplicity after either stated base extension |
|---|---:|---:|---:|---:|
| \(\alpha_0\) | \(3\) | \(3\) | \(18\) | \(3\) |
| \(\alpha_1\) | \(6\) | \(1\) | \(12\) | \(2\) |

Their irreducible minimal polynomials over \(\mathbf Q\) are respectively

\[
 P_0(t)=t^6-24t^3+512,
 \qquad
 P_1(t)=t^{12}+24t^9+64t^6+12288t^3+262144.
 \tag{CC-AG.99}
\]

**Complete proof.**

### 1. The quadratic ideal calculation and stabilized germ

First,

\[
 \mathcal O_K=\mathbf Z[\omega],\qquad
 \omega^2-\omega+6=0,\qquad
 N_{K/\mathbf Q}(x+y\omega)=x^2+xy+6y^2.
 \tag{CC-AG.100}
\]

For completeness, if \(a+bs\), \(a,b\in\mathbf Q\), is integral, its trace and norm are integers. Thus \(2a\in\mathbf Z\), and
\((2a)^2-4N(a+bs)=-92b^2\) is integral. The denominator of \(b\) in lowest terms is at most \(2\), because its square divides \(92\). Write \(a=A/2,b=B/2\). Integrality of the norm says \(A^2+23B^2\equiv0\pmod4\), so \(A\) and \(B\) have the same parity. This is exactly an element of \(\mathbf Z[\omega]\). Conversely \(\omega\) satisfies the displayed monic polynomial, so that ring consists of algebraic integers. The norm formula follows by multiplication with the conjugate.

Modulo \(2\), this polynomial is \(t(t-1)\). Consequently

\[
 \mathfrak p=(2,\omega-1),\qquad
 \bar{\mathfrak p}=(2,\omega),\qquad
 (2)=\mathfrak p\bar{\mathfrak p},
 \qquad N\mathfrak p=N\bar{\mathfrak p}=2.
 \tag{CC-AG.101}
\]

The primes are distinct, and the two completions of \(K\) above \(2\) are \(\mathbf Q_2\). One can see the latter directly by lifting the two simple roots of \(t^2-t+6\) modulo \(2\); the simple-root lifting statement is Milne (2020), Proposition 7.31, p. 120.

Now \(N(\eta)=8\), while \(\eta\) vanishes modulo \(\mathfrak p\) and is \(1\) modulo \(\bar{\mathfrak p}\). Unique ideal factorization and the ideal norm give

\[
 (\eta)=\mathfrak p^3.
 \tag{CC-AG.102}
\]

The ideal \(\mathfrak p\) is not principal. A generator would have positive norm \(2\), but

\[
 x^2+xy+6y^2=(x+y/2)^2+\frac{23}{4}y^2=2
\]

has no integral solution: if \(y\ne0\), the second term alone exceeds \(2\); if \(y=0\), it would say \(x^2=2\). Therefore the class of \(\mathfrak p\) has order exactly \(3\). No class-number table is needed.

It follows that

\[
 (\gamma)=\mathfrak p^3\bar{\mathfrak p}^{\,6},
 \qquad \gamma\bar\gamma=512=2^9.
 \tag{CC-AG.103}
\]

Hence \(\gamma\) is an integral weight-one Weil \(2^9\)-number. The ratio \(\gamma/\bar\gamma\) has nonzero valuations at the two primes above \(2\), and is therefore not a root of unity. Since \(K\) is quadratic, no positive power of \(\gamma\) is rational: otherwise its two conjugates would have equal powers. Thus

\[
 \mathbf Q(\gamma^N)=K\qquad(N\ge1),
 \tag{CC-AG.104}
\]

so \(K\) is the stabilized germ centre. The two normalized slopes are \(1/3\) and \(2/3\). Their local degrees over \(\mathbf Q_2\) are one, and \(K\) has no real place. Milne's invariant formula therefore gives local invariants \(-1/3,-2/3\) modulo \(\mathbf Z\), with all others zero. Their least common denominator is \(3\), so \(d_\xi=3\). The same calculation applies to \(\beta=\gamma^3\) relative to \(2^{27}\), giving \(d_\beta=3\). The rank is \(3[K:\mathbf Q]=6\). Their label-to-germ orbit map is bijective, so CC-AG09 gives \((T_\beta)_{\bar{\mathbf F}_2}\simeq S_\xi\).

We also compute \(h_\xi\) directly. If \(\delta\in K\) represents \(\xi\) at exponent \(n>0\), then
\(\delta^{9N}=\gamma^{nN}\) for some \(N\ge1\). Taking normalized valuations gives

\[
 \operatorname{ord}_{\mathfrak p}(\delta)=n/3,\qquad
 \operatorname{ord}_{\bar{\mathfrak p}}(\delta)=2n/3,
 \qquad
 (\delta)=\mathfrak p^{n/3}\bar{\mathfrak p}^{\,2n/3}.
 \tag{CC-AG.105}
\]

First \(3\mid n\). Since \([\bar{\mathfrak p}]=[\mathfrak p]^{-1}\), principality of this ideal forces
\([\mathfrak p]^{-n/3}=1\), and hence \(9\mid n\). The representative \(\gamma\) at exponent \(9\) exists, proving \(h_\xi=9\).

### 2. Necessary degrees and indices for every possible geometric lift

Consider any source label \(\alpha\in W(8)\) whose germ orbit is that of \(\xi\). Conjugate it if necessary so that \([\alpha,3]=[\gamma,9]\). For some \(N\ge1\),

\[
 \alpha^{9N}=\gamma^{3N}.
 \tag{CC-AG.106}
\]

Put \(L=\mathbf Q(\alpha)\). By (CC-AG.104), the right side generates \(K\), so \(K\subset L\). Write \(c=[L:K]\).

Taking the field norm from \(L\) to \(K\) in (CC-AG.106) shows that \(N_{L/K}(\alpha)\) is a representative of \(\xi\) at exponent \(3c\). Equivalently its \(9N\)-th power equals \(\gamma^{3cN}\). By the computed exponent condition,

\[
 9\mid3c,\qquad\text{so }3\mid c.
 \tag{CC-AG.107}
\]

This norm argument does not assume that \(L/K\) is Galois.

There are no real embeddings of \(L\), since it contains the imaginary quadratic field \(K\). For each place \(z\mid2\) of \(L\), with normalized valuation and residue degree \(f_z\), the source local invariant relative to \(q=8\) is

\[
 -\frac{\operatorname{ord}_z(\alpha)}
          {\operatorname{ord}_z(8)}[L_z:\mathbf Q_2]
 =-\frac{\operatorname{ord}_z(\alpha) f_z}{3}
 \quad\bmod\mathbf Z.
 \tag{CC-AG.108}
\]

All remaining invariants vanish. Thus

\[
 d_\alpha\in\{1,3\},\qquad
 r_\alpha=\frac{c\,d_\alpha}{3},
 \tag{CC-AG.109}
\]

by the exact transition formula CC-AG09. A multiplicity-one source simple would therefore have

\[
 [L:K]=3,\qquad [L:\mathbf Q]=6,\qquad d_\alpha=1.
 \tag{CC-AG.110}
\]

Moreover (CC-AG.106) gives the root-of-unity statement itself:

\[
 \theta=\alpha^3/\gamma\in L,\qquad
 \theta^{3N}=1.
 \tag{CC-AG.111}
\]

In particular \(\theta\), not only its cube, is a root of unity.

### 3. Roots of unity in a degree-six field containing \(K\)

If \(L\) has degree \(6\) over \(\mathbf Q\) and contains \(K=\mathbf Q(\sqrt{-23})\), then

\[
 \mu(L)=\{1,-1\}.
 \tag{CC-AG.112}
\]

To prove this, let a root of unity in \(L\) have order \(n\). The cyclotomic degree formula, Milne (2020), Theorem 6.4(a), p. 99, gives \(\varphi(n)\mid6\). The complete list is

\[
 n\in\{1,2,3,4,6,7,9,14,18\}.
 \tag{CC-AG.113}
\]

Here is a finite justification of completeness. Every prime \(l\mid n\) has \(l-1\mid\varphi(n)\mid6\), so \(l\in\{2,3,7\}\). Their exponents are at most \(2,2,1\), respectively, because the factors \(l^{e-1}(l-1)\) must divide \(6\). Checking these finitely many combinations gives exactly (CC-AG.113).

Orders \(3,6,9,18\) would put \(\mathbf Q(\sqrt{-3})\) in \(L\), and order \(4\) would put \(\mathbf Q(i)\) in \(L\). Either is a quadratic field distinct from \(K\), so its compositum with \(K\) would have degree \(4\), impossible inside a field of degree \(6\).

For orders \(7,14\), \(L\) would contain \(\mathbf Q(\zeta_7)\), itself of degree \(6\), and hence equal that field. Its Galois group is cyclic of order \(6\): it injects into \((\mathbf Z/7\mathbf Z)^\times\), and the two groups have the same order. Thus it has a unique quadratic subfield. This subfield is \(\mathbf Q(\sqrt{-7})\), as may be verified without a table: put \(u=\zeta_7+\zeta_7^2+\zeta_7^4\); then \(\bar u=\zeta_7^3+\zeta_7^5+\zeta_7^6\), \(u+\bar u=-1\), and \(u^2=u+2\bar u=-u-2\). Hence \(u^2+u+2=0\), with discriminant \(-7\). This quadratic field is not \(K\), another contradiction. Only orders \(1,2\) remain, proving (CC-AG.112).

### 4. The local cube obstruction excludes multiplicity one

At either completion \(K_v=\mathbf Q_2\), (CC-AG.103) gives \(\operatorname{ord}_2(\gamma)=3\) or \(6\). Every unit of \(\mathbf Z_2\) is a cube: its cube-root equation has the simple root \(1\) modulo \(2\), so Proposition 7.31 applies. Therefore \(\gamma\) has a cube root \(b_v\in\mathbf Q_2\), with valuation \(1\) or \(2\), respectively.

Suppose a multiplicity-one lift existed. By (CC-AG.110)--(CC-AG.112), \(\alpha^3=\gamma\) or \(-\gamma\). Replacing \(\alpha\) by \(-\alpha\) in the latter case preserves its centre, valuations and index, and gives \(\alpha^3=\gamma\). Its minimal polynomial over \(K\) has degree \(3\) and is \(t^3-\gamma\). At either place \(v\mid2\), it factors as

\[
 t^3-\gamma=(t-b_v)(t^2+b_vt+b_v^2).
 \tag{CC-AG.114}
\]

In particular the centre \(L\) has a place above \(v\) of local degree one, where the valuation of \(\alpha\) is \(1\), respectively \(2\). The source invariant (CC-AG.108) is then \(-1/3\), respectively \(-2/3\), and is nonzero. Hence \(d_\alpha=3\), contradicting (CC-AG.110).

This excludes every possible simple lift of multiplicity one, including arbitrary root-of-unity twists. An actual source object is a positive sum of source simples, each contributing a positive integer to exactly one target orbit. It therefore cannot give one copy of \(S_\xi\) unless such a simple lift exists. We have proved

\[
 1\notin H_{\bar{\mathbf F}_2}(O_\xi).
 \tag{CC-AG.115}
\]

### 5. A multiplicity-three lift

Choose \(\alpha_0\) with \(\alpha_0^3=\gamma\). It is integral and all its conjugates have absolute value \(2^{3/2}\), so it is a weight-one Weil \(8\)-number. Its germ is \(\xi\). Equation (CC-AG.104) gives \(K\subset\mathbf Q(\alpha_0)\), while its defining polynomial bounds the relative degree by \(3\). The norm constraint (CC-AG.107) forces that degree to be exactly \(3\).

The local argument (CC-AG.114) gives \(d_{\alpha_0}=3\). More explicitly, after scaling by \(b_v\) its quadratic factor is \(t^2+t+1\), irreducible modulo \(2\), so the local factors have degrees \(1\) and \(2\); already the degree-one factor proves the nontrivial index. Formula (CC-AG.109) yields

\[
 r_{\alpha_0}=3\cdot3/3=3.
 \tag{CC-AG.116}
\]

Its centre degree over \(\mathbf Q\) is \(6\). Taking the norm of \(t^3-\gamma\) from \(K\) to \(\mathbf Q\), using \(\gamma+\bar\gamma=24\) and \(\gamma\bar\gamma=512\), gives \(P_0\) in (CC-AG.99). The degree just proved establishes its irreducibility.

### 6. A multiplicity-two lift

Set \(\alpha_1=\alpha_0\zeta_9\), with \(\zeta_9\) primitive. It is again an integral weight-one Weil \(8\)-number, and

\[
 \alpha_1^9=\gamma^3,\qquad
 \alpha_1^3/\gamma=\zeta_3.
 \tag{CC-AG.117}
\]

The first equation and stabilization give \(K\subset L_1=\mathbf Q(\alpha_1)\); the second puts \(\zeta_3\) in \(L_1\). Since \(K\ne\mathbf Q(\sqrt{-3})\), the relative degree \(c_1=[L_1:K]\) is even. It is divisible by \(3\) by (CC-AG.107). On the other hand, \(\alpha_1\) is a root of

\[
 Q_1(t)=t^6+\gamma t^3+\gamma^2\in K[t],
 \tag{CC-AG.118}
\]

so \(c_1\le6\). Consequently \(c_1=6\), and \(Q_1\) is its minimal polynomial over \(K\).

At each \(v\mid2\), use the cube root \(b_v\) above. Then

\[
 Q_1(b_vt)=b_v^6(t^6+t^3+1)=b_v^6\Phi_9(t).
 \tag{CC-AG.119}
\]

The reduction of \(\Phi_9(t)\) modulo \(2\) is irreducible of degree \(6\). Indeed, its roots in characteristic \(2\) have exact order \(9\): the identity
\((t^3-1)\Phi_9(t)=t^9-1\) has no repeated roots, and excludes order \(1\) or \(3\). The least positive integer \(e\) with \(9\mid2^e-1\) is \(6\), as \(2^3\equiv-1\pmod9\). Therefore every root has degree \(6\) over \(\mathbf F_2\), proving irreducibility.

A monic polynomial with irreducible reduction remains irreducible over \(\mathbf Q_2\), so (CC-AG.119) proves that \(L_1\) has a single place of local degree \(6\) over each \(v\mid2\). Its normalized slopes are still \(1/3,2/3\), because of the germ relation. The two source local invariants are therefore

\[
 -\tfrac13\cdot6=-2,\qquad
 -\tfrac23\cdot6=-4
 \quad\bmod\mathbf Z,
\]

both zero. There are no real places and all other local invariants vanish. Thus \(d_{\alpha_1}=1\), and

\[
 r_{\alpha_1}=6\cdot1/3=2.
 \tag{CC-AG.120}
\]

Taking the norm of \(Q_1(t)\) from \(K\) to \(\mathbf Q\) gives \(P_1(t)\) in (CC-AG.99). Its degree \(12=[L_1:\mathbf Q]\) proves its irreducibility. The polynomial expansion is also checked by the accompanying exact rational script; the irreducibility argument is the field-degree proof, not an unreported numerical computation.

### 7. Exact geometric and finite-target monoids

We have realized multiplicities \(2\) and \(3\), and excluded \(1\) for the geometric target. Every integer \(r\ge2\) is a nonnegative combination of \(2\) and \(3\): use only \(2\)'s for even \(r\), and \(3\) followed by \(2\)'s for odd \(r\ge3\). Direct sums give all these multiplicities. This proves the geometric equality in (CC-AG.97).

For the finite target \(T_\beta\), (CC-AG.117) and \(\alpha_0^9=\gamma^3\) show that both source simples already map to its orbit under the ninth-power map. Their source-to-target multiplicities are still \(3\) and \(2\), since the target centre and index are \(K\) and \(3\). Conversely, a finite-field multiplicity-one lift would remain one geometric copy after further base extension, contradicting (CC-AG.115). Hence the same exact monoid holds for the finite target.

There is also a direct finite-orbit verification. The polynomial whose roots are all possible finite-target source labels is

\[
 \begin{aligned}
 (t^9-\gamma^3)(t^9-\bar\gamma^3)
 &=P_0(t)P_1(t)\\
 &=t^{18}+23040t^9+134217728.
 \end{aligned}
 \tag{CC-AG.121}
\]

The two factors are the irreducible polynomials already proved above, so there are exactly two source orbits, with multiplicities \(3\) and \(2\). This proves the finite-target assertion independently of any search cutoff.

Finally, a cyclic submonoid of \(\mathbf N\) containing both \(2\) and \(3\) would have generator dividing their gcd, hence generator \(1\), and would contain \(1\). Thus the monoids in (CC-AG.97) are not cyclic. Their group completions are \(\mathbf Z\), since \(3-2=1\). This finishes the proof. \(\square\)

### Classical abelian-variety corollary, independent of the additional motivic inputs

There is a geometrically simple abelian threefold
\(A/\mathbf F_{2^9}\) with Frobenius characteristic polynomial

\[
 f_A(t)=(t^2-24t+512)^3,
 \tag{CC-AG.122}
\]

such that, for every integer \(r\ge0\),

\[
 \begin{aligned}
 A_{\bar{\mathbf F}_2}^{r}
  \text{ is isogenous to }B_{\bar{\mathbf F}_2}
  \text{ for some }B/\mathbf F_8
 &\quad\Longleftrightarrow\quad r\in\langle2,3\rangle_{\mathbf N},\\
 A_{\mathbf F_{2^{27}}}^{r}
  \text{ is }\mathbf F_{2^{27}}\text{-isogenous to }
        B_{\mathbf F_{2^{27}}}
  \text{ for some }B/\mathbf F_8
 &\quad\Longleftrightarrow\quad r\in\langle2,3\rangle_{\mathbf N}.
 \end{aligned}
 \tag{CC-AG.123}
\]

The first assertion concerns geometric isogeny descent; the second concerns isogeny descent to a specified finite target. In particular, the square and cube of \(A\) have both kinds of descent, while \(A\) has neither. The zero-dimensional case \(r=0\) means the zero abelian variety.

**Proof using only classical Honda--Tate and the explicit arithmetic above.** Tate's account of Honda--Tate, Theorem 1(i)--(ii), printed p. 96, classifies simple abelian varieties up to isogeny by integral Weil numbers, describes their endomorphism division algebras, and gives
\(2\dim B=[\mathbf Q(\pi_B):\mathbf Q]d_B\). Its Remark 2 on the same page gives the Frobenius characteristic polynomial as the \(d_B\)-th power of the minimal polynomial. Here Tate uses the endomorphism algebra of the abelian variety, whose \(p\)-invariant has the opposite sign to the motivic convention used earlier; the Schur indices, being least common denominators, are identical. No result about higher-codimension cycles on abelian varieties is needed in this corollary.

The integral Weil number \(\gamma\) therefore gives a simple threefold \(A/\mathbf F_{2^9}\), with (CC-AG.122). For every \(N\ge1\), the number \(\gamma^N\) has centre \(K\) by (CC-AG.104), and the normalized local invariants relative to \(2^{9N}\) have the same denominators as those of \(\gamma\). Its index remains \(3\). The simple abelian variety associated to \(\gamma^N\) consequently has dimension \(3\), and the same Frobenius characteristic polynomial as \(A_{\mathbf F_{2^{9N}}}\). Tate (1966), Theorem 1(c), printed p. 139, makes these varieties isogenous. Thus \(A\) stays simple over every finite extension. Any abelian subvariety over \(\bar{\mathbf F}_2\) is defined over a finite extension, since its defining equations and group maps use only finitely many algebraic coefficients. Therefore \(A\) is geometrically simple.

Let \(B_9,B_6\) be the simple abelian varieties over \(\mathbf F_8\) associated to \(\alpha_0,\alpha_1\), respectively. The subscripts indicate their dimensions. The centre degrees and indices established in Sections 5--6 give

\[
 \dim B_9=9,\qquad \dim B_6=6,\qquad
 f_{B_9}=P_0^3,\qquad f_{B_6}=P_1.
 \tag{CC-AG.124}
\]

Under extension from \(\mathbf F_8\) to \(\mathbf F_{2^{27}}\), Frobenius becomes its ninth power. Since
\(\alpha_0^9=\alpha_1^9=\beta=\gamma^3\), all the resulting eigenvalues lie in the two-element conjugacy orbit of \(\beta\). The two eigenvalues occur with the same multiplicity: they are Galois conjugate and the characteristic polynomial is rational. The dimensions therefore give characteristic polynomials
\(m_\beta(t)^9\) and \(m_\beta(t)^6\), respectively, where
\(m_\beta(t)=(t-\beta)(t-\bar\beta)\). The variety
\(A_{\mathbf F_{2^{27}}}\) has characteristic polynomial \(m_\beta(t)^3\). Applying Tate's isogeny criterion gives actual finite-field isogenies

\[
 (B_9)_{\mathbf F_{2^{27}}}
       \sim_{\mathbf F_{2^{27}}} A_{\mathbf F_{2^{27}}}^{3},
 \qquad
 (B_6)_{\mathbf F_{2^{27}}}
       \sim_{\mathbf F_{2^{27}}} A_{\mathbf F_{2^{27}}}^{2}.
 \tag{CC-AG.125}
\]

Products of these source varieties supply every \(r\ge2\) in both assertions of (CC-AG.123).

For completeness, the impossibility of a single geometric copy can also be read entirely in the classical isogeny category. If \(C/\mathbf F_8\) were geometrically isogenous to \(A\), then \(C\) would be a geometrically simple threefold, hence simple over \(\mathbf F_8\). Let \(\alpha\) be its Weil label and \(L=\mathbf Q(\alpha)\). An isogeny over the algebraic closure is defined over some finite common extension, so, after conjugating \(\alpha\), its germ is \(\xi\). Sections 2--4 then apply to its centre and classical Schur index: \(K\subset L\), \(3\mid c=[L:K]\), and \(d_\alpha\in\{1,3\}\). The classical dimension formula and \(\dim C=3\) require
\(c d_\alpha=3\), hence \(c=3,d_\alpha=1\). But the complete root-of-unity and local cube argument in Sections 3--4 forces \(d_\alpha=3\), a contradiction. This argument uses only the Honda--Tate index formula, not the numerical-motive transition theorem. It also excludes a finite-target isogeny, which would imply a geometric one. This proves (CC-AG.123). \(\square\)

### Consequence for the remaining descent criterion

CC-AG11's integral-slope cyclic formula and CC-AG13's prime-field cyclic formula retain their stated hypotheses. A universal cyclic formula for an arbitrary specified field \(\mathbf F_{p^a}\) is false, even for a weight-one orbit with imaginary quadratic stabilized centre. The positive multiplicity equations of CC-AG09 and the finite fixed-object procedure of CC-AG12 cannot in general be replaced by one divisibility condition. This is an exact obstruction, not a claim that those existing finite decision procedures fail.

## Primary references and exact locators

- Honda, T. (1968). Isogeny classes of abelian varieties over finite fields. *Journal of the Mathematical Society of Japan, 20*(1--2), 83--95. https://doi.org/10.2969/jmsj/02010083 . Exact locator: Main Theorem, p. 83. The occurrence statement and its integral Weil-number definition were previously inspected in AQ-WEIL-EXIST and CC-AG01. Primary scan: https://people.math.rochester.edu/faculty/doug/otherpapers/Honda-Ab.pdf .
- Milne, J. S. (1994). Motives over finite fields. In U. Jannsen, S. Kleiman, & J.-P. Serre (Eds.), *Motives* (Proceedings of Symposia in Pure Mathematics, Vol. 55, Part 1, pp. 401--459). American Mathematical Society. **Version used:** corrected author manuscript, November 2, 2019. https://www.jmilne.org/math/xnotes/Seattle1.pdf . Exact locators: invariant convention p. 17; Theorem 2.15(c) and Theorem 2.16, p. 18; Theorems 2.18--2.19, p. 20. These are the checked classification inputs, applied in the abelian-generated category as in CC-AG08.
- Milne, J. S. (2020, July 19). *Algebraic number theory* (Version 3.08) [Author course notes]. https://www.jmilne.org/math/CourseNotes/ANT.pdf . Exact locators: field norm, Proposition 2.19, pp. 31--32; ideal factorization, Theorem 3.20, p. 53; ideal norms, Propositions 4.1--4.2, p. 69; cyclotomic degree, Theorem 6.4(a), p. 99; simple-root lifting over a complete discrete valuation ring, Proposition 7.31 and its proof, p. 120. The class order, root-of-unity exclusion, local factors, indices and exact monoids in this example are proved explicitly above.

- Tate, J. (1966). Endomorphisms of abelian varieties over finite fields. *Inventiones Mathematicae, 2*, 134--144. https://doi.org/10.1007/BF01404549 . Exact locator: Theorem 1(c), p. 139, equivalence of isogeny and equality of Frobenius characteristic polynomials. Primary scan directly inspected: https://pazuki.perso.math.cnrs.fr/index_fichiers/Tate66.pdf .
- Tate, J. (1971). Classes d'isogénie des variétés abéliennes sur un corps fini (d'après T. Honda). In *Séminaire Bourbaki: Vol. 1968/69, exposés 347--363* (Exposé 352, pp. 95--110). Springer-Verlag. https://www.numdam.org/book-part/SB_1968-1969__11__95_0/ . Exact locator: Theorem 1(i)--(ii), p. 96, equations (1)--(2), and Remark 2 on p. 96; talk delivered November 1968, published 1971. Primary scan directly inspected: https://www.numdam.org/article/SB_1968-1969__11__95_0.pdf .
