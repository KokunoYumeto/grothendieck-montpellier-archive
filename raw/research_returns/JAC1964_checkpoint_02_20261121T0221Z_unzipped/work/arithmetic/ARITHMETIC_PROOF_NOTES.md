# Arithmetic sibling of cote 44: corrected theorem and remaining gate

Run: `JAC1964-20261121`. Author/checker: `/root/arithmetic_sign`, GPT-6 Astra Pro; effort setting not exposed. Date: 2026-11-21 UTC. These are working proof sections for incorporation into the parent manuscript. They are not an independent review of the parent manuscript. No Lean build was attempted here. Accepted attached results are used at their stated scope.

## A. Conventions and exact background

Let \(K\) be a number field, \(A/K\) an abelian variety of dimension \(g\), and \(\ell=c_1(L)\) for a symmetric ample line bundle. All Chow groups and Chow motives have rational coefficients. Write \(L\) also for multiplication by \(\ell\). The raw Beilinson--Bloch pairing, normalized by \([K:\mathbf Q]\), is denoted \(h_K\). Thus \(h_K\) is invariant under finite extension of the field of definition. This normalization is distinct from the choice whether the bilinear Néron--Tate form is the polarization of \(\widehat h\) with or without a factor two; below the Néron--Tate convention is Künnemann's.

**Background AR-B1 (existence and functoriality).** Künnemann, *Height pairings for algebraic cycles on abelian varieties*, Ann. Sci. ENS 34 (2001), Theorem 1.6 and Corollary 1.7, give the pairing on every abelian variety over a number field. Section 1.3 records compatibility with correspondences; §1.4, equation (7), gives the extension-of-field scaling before normalization. The pairing uses extensions perpendicular to vertical cycles; an arbitrary closure on a model is insufficient. The correspondence projection formula is also Künnemann 1996, §5, equation (18), from Lemma 4.1.

**Background AR-B2 (Picard comparison and sign).** Künnemann, *Higher Picard varieties and the height pairing*, Amer. J. Math. 118 (1996), Theorem 8.2, equation (23), identifies the height of algebraically trivial cycles with the Néron--Tate biextension pairing on higher Picard varieties, with the positive comparison integer \(k_X^p\). His Theorem 6.1 calibrates the raw curve height as **minus** the positive Jacobian pairing. Let \(B^p(A_K)\) be algebraically trivial cycles modulo geometric incidence equivalence. Theorem 12.1(ii) gives

\[
 x\ne0,\quad L^{g+2-2p}x=0
 \quad\Longrightarrow\quad
 (-1)^p h_K(x,L^{g+1-2p}x)>0.
\]

The old regular-model hypothesis in the 1996 statement can be met after finite extension using AR-B1; the positive base-change factor does not affect the conclusion. This is a known theorem, not a new consequence of GRH or of the attached CM Hodge theorem. For \(g=2m-1,p=m\), the positive candidate is

\[
q_A(x,y)=(-1)^m h_K(x,y),\qquad Lx=Ly=0.
\tag{AR.1}
\]

Consequently “the BB height equals a positive Néron--Tate height” requires a specified signed duality. With the parent's convention \(\phi_L(a)=t_a^*L\otimes L^{-1}\), the signed incidence is \((-1)^m D\). Its Hodge cup-product counterpart carries \((-1)^{m-1}\); the incidence dictionary supplies the extra minus. The \(m=1\) Faltings--Hriljac case is an indispensable check.

**Background AR-B3 (motivic Lefschetz).** Künnemann, *A Lefschetz decomposition for Chow motives of abelian schemes*, Invent. Math. 113 (1993), Theorem 5.1, Theorem 5.2, and Corollary 5.3, all on printed p.96, supply actual Chow projectors, motivic hard Lefschetz, and transposition compatibility. For \(g=2m-1\), the primitive projector \(\pi_P\) on \(h^g(A)\) satisfies \({}^t\pi_P=\pi_P\); the primitive motive \(P\) has its perfect middle Poincaré pairing. These three statements were checked directly in the rendered source page, not inferred from a cohomological decomposition.

**Background AR-B4 (degree one is faithful).** The functor from abelian varieties up to isogeny to degree-one Chow motives is fully faithful (contravariantly). In particular,

\[
\operatorname{End}_{\mathrm{Chow}}(h^1B)=\operatorname{End}(B)_{\mathbf Q}^{\mathrm{op}},
\]

and the Betti realization of this endomorphism algebra is faithful. A directly inspected modern statement is Laga--Shnidman, *Ceresa cycles of bielliptic Picard curves*, arXiv:2312.12965, Proposition 4.5, citing Kings, *Higher regulators, Hilbert modular surfaces, and special values of L-functions*, Duke Math. J. 92 (1998), Proposition 2.2.1. The contravariant/opposite convention changes no invertibility assertion below.

## B. Exact removal of the irrelevant Beauville grades

For \([n]^*x=n^{2p-s}x\), say \(x\) has Beauville grade \(s\). The well-known height selection rule is

\[
h_K(\operatorname{CH}^p_{(s)},\operatorname{CH}^{g+1-p}_{(t)})=0
\quad\text{unless}\quad s+t=2.
\tag{AR.2}
\]

An explicit literature locator is Zhang, *Gross--Schoen cycles and dualising sheaves*, Invent. Math. 179 (2010), §5.3, printed p.68. For completeness its proof is one line: the projection formula gives

\[
h_K([n]^*x,[n]^*y)=n^{2g}h_K(x,y),
\]

whereas the eigenvalue computation gives \(n^{2(g+1)-s-t}\) times the original pairing. Take \(n>1\).

**Proposition AR-1 (primitive grade reduction).** Put

\[
V^p=\ker\bigl(L^{g+2-2p}:\operatorname{CH}^p(A)_{\mathrm{hom}}
\longrightarrow\operatorname{CH}^{g+2-p}(A)\bigr),\qquad 2p\le g+1.
\]

Then \(V^p_{(s)}=0\) for \(s\ge2\). Every \(V^p_{(s)}\) with \(s\le0\) belongs to the radical of the signed height on \(V^p\). Thus semipositivity on the full primitive group is equivalent to semipositivity on grade one. Strict positivity on the full group is equivalent to strict positivity on grade one together with the vanishing of the primitive grades \(s\le0\).

*Proof.* A grade-\(s\) class of codimension \(p\) is a Chow class of \(h^i(A)\) with \(i=2p-s\). For \(s\ge2\), put \(e=g+2-2p\). Then \(i\le g\) and \(e\le g-i\). Motivic hard Lefschetz makes \(L^{g-i}\) an isomorphism. If \(L^e x=0\), multiply by \(L^{g-i-e}=L^{s-2}\) to obtain \(L^{g-i}x=0\), hence \(x=0\). Consequently every surviving primitive grade is at most one. Multiplication by a symmetric \(\ell\) has grade zero. Equation (AR.2) therefore pairs a primitive grade \(s\le0\) only with grade \(2-s\ge2\), which has just been proved zero. This proves the radical assertion and both equivalences. No assertion that all negative Beauville grades vanish was used. \(\square\)

For \(g=2m-1,p=m\), the grade-one component of \(V^m\) is exactly

\[
V^m_{(1)}=\operatorname{CH}^m(P).
\tag{AR.3}
\]

Indeed the motivic Lefschetz decomposition of \(h^g(A)\) is a direct sum of the primitive middle summand and longer Lefschetz strings. On the middle-degree term of each longer string, \(L\) has a left inverse; on \(P\), it is zero. This checks that (AR.3) is a Chow-level assertion, rather than merely a statement about realization.

**Corollary AR-1a (the threefold has no additional lower-grade gate).** If \(g=3,p=2\), then \(\operatorname{CH}^2_{(s)}(A)=0\) for every \(s<0\), and \(\operatorname{CH}^2_{(0)}(A)_{\mathrm{hom}}=0\). Consequently the full primitive homologically trivial group equals \(\operatorname{CH}^2(P)\), and strict positivity has no separate lower-grade vanishing condition.

*Proof.* Fourier gives
\[
\mathcal F:\operatorname{CH}^2_{(s)}(A)
 \simeq\operatorname{CH}^{1+s}_{(s)}(\widehat A).
\]
For \(s<-1\) the target has negative codimension. For \(s=-1\) it is \(\operatorname{CH}^0_{(-1)}=0\). For \(s=0\), a homologically trivial class maps to a homologically trivial divisor of grade zero. Such a divisor lies in \(\operatorname{Pic}^0\), which has grade one, so it is zero. Fourier is invertible and preserves homological triviality. AR-1 removes all primitive grades at least two; only grade one remains. \(\square\)

## C. A CM Chow summand with a strictly positive height

Assume the attached 032 Theorem 1.1, i.e. the rational Hodge conjecture for products of CM abelian varieties. Its Lemma 8.1 supplies effective CM realizations; in weight one it is the usual realization by a CM abelian variety. The statement below uses those accepted inputs, classical motivic Lefschetz, and the established Picard height theorem. It does not use GRH.

**Theorem AR-2 (orthogonal Picard summand and exact remaining arithmetic gate).** Let \(A/K\) be CM, \(\dim A=2m-1\), with symmetric ample \(L\). After a finite number-field extension \(K'/K\), there are a CM abelian variety \(B/K'\), an actual self-transpose Chow idempotent \(e\) of the primitive middle motive \(P\), and an orthogonal decomposition

\[
P=M\oplus N,\qquad M\simeq h^1(B)(1-m),
\tag{AR.4}
\]

with the following properties.

1. \(H(M)\) is the maximal rational sub-Hodge structure of \(H(P)\) having only types \((m,m-1)\) and \((m-1,m)\). Thus \(H(N)\) has no nonzero such sub-Hodge structure.
2. \(\operatorname{CH}^m(M)\simeq\operatorname{Pic}^0(B)(K')_{\mathbf Q}\). The restriction of \(q_A=(-1)^m h_{K'}\) to this full Chow summand is a Néron--Tate form for a rational polarization, with the positive comparison normalization of AR-B2. It is strictly positive on every nonzero class.
3. The two Chow summands are height orthogonal. Therefore the semipositivity problem on the full primitive homologically trivial Chow group over \(K'\) reduces **exactly** to

\[
(-1)^m h_{K'}(z,z)\ge0
\qquad(z\in\operatorname{CH}^m(N)).
\tag{AR-GATE}
\]

For strict positivity one must additionally prove the vanishing of the primitive grades \(s\le0\) and strict positivity on the nonzero classes of \(\operatorname{CH}^m(N)\).

*Proof.* Let \(W\subset H(P)\) be the sum of all rational sub-Hodge structures of the indicated types. Polarizable Hodge structures are semisimple; this sum is a sub-Hodge structure and has an orthogonal complement. Because \(A\) is CM, so is \(W\). Its twist \(W(m-1)\) is effective of weight one. The degree-one case of 032 Lemma 8.1, followed by Poincaré complete reducibility, gives a CM \(B\) and an isomorphism

\[
H^1(B)(1-m)\simeq W.
\]

A complex CM abelian variety admits a number-field model (Milne, Abelian Varieties, version 1.10, Proposition 16.10, printed p.65). After enlarging \(K\), both \(B\) and chosen polarizations are defined over the same number field. Write \(b=\dim B\). The inclusion of this weight-one twist into \(H^g(A)\) is a Hodge class of codimension \(b+m-1\) on \(B\times A\). Theorem 1.1 applied to \(B\times A\) makes it an algebraic correspondence. This is exactly the codimension bookkeeping in the proof of 032 Corollary 8.2: \(n=1,r_0=m-1\).

The correspondence can be chosen over \(\overline{\mathbf Q}\). Indeed spread each of its finitely many cycle components over a finitely generated extension of \(\overline{\mathbf Q}\), or equivalently represent it by a complex point of the Hilbert scheme of the fixed variety \(B\times A\). Take the connected component of that finite-type Hilbert scheme containing this point. Because the scheme is defined over the algebraically closed field \(\overline{\mathbf Q}\), that component contains a \(\overline{\mathbf Q}\)-point. The universal family is flat, and its Betti cycle class on the fixed complex variety is locally constant on the analytification; connectedness therefore preserves the class. Specializing each component in this way preserves the original rational Hodge correspondence. Finitely many algebraic coefficients and cycle equations require only one finite extension \(K'\). Sandwich the resulting correspondence between the actual degree-one and primitive Chow projectors. We obtain a Chow morphism

\[
u:M_0=h^1(B)(1-m)\longrightarrow P
\]

whose realization is the chosen injection onto \(W\).

There is an algebraic, perfect alternating form on \(M_0\) given by a polarization of \(B\) and motivic hard Lefschetz. On \(P\), use \((-1)^{m-1}\) times the middle Poincaré form. Its restriction to the types occurring in \(W\) is a Hodge polarization. Both forms are perfect at the Chow-motive level: for \(B\) this is motivic hard Lefschetz; for \(P\) it is AR-B3. They define a Chow adjoint \(u^\dagger\). The realization of

\[
a=u^\dagger u\in\operatorname{End}_{\mathrm{Chow}}(M_0)
\]

is positive and invertible: for the positive Hodge Hermitian forms, \((av,v)=(uv,uv)>0\) for nonzero \(v\). By AR-B4 this is an actual rational isogeny endomorphism of \(B\), so \(a^{-1}\) exists in the Chow endomorphism algebra. This step does **not** infer Chow invertibility from a general cohomological isomorphism; it uses full faithfulness specifically in degree one.

Set

\[
v=a^{-1}u^\dagger,\qquad e=uv=u a^{-1}u^\dagger.
\]

Then \(vu=1\), \(e^2=e\), and \(e^\dagger=e\), by direct composition. Since the form on \(P\) is a scalar multiple of its Poincaré pairing, \(e^\dagger=e\) says precisely \({}^t e=e\) within \(P\). Its realization is the orthogonal projector onto \(W\). The complementary motive \(N=(P,1-e)\) therefore has the stated realization. No assertion that a realization-zero complementary motive is zero is made; such a conclusion would need a separate nilpotence theorem. This avoids a hidden lift from homological to Chow motives.

The retraction identifies \(\operatorname{CH}^m(M)\) with \(\operatorname{CH}^1(h^1B)=\operatorname{Pic}^0(B)(K')_{\mathbf Q}\). Such classes are algebraically trivial. This identification is also injective modulo incidence equivalence: if \(u_*x\) is incidence equivalent to zero, apply the correspondence \(v\); then \(x\) is incidence equivalent to zero as a divisor on \(B\), hence \(x=0\) in \(\operatorname{Pic}^0(B)_{\mathbf Q}\). The latter assertion follows either from the identity correspondence in the definition of incidence equivalence, or from the ordinary Picard universal property. Thus AR-B2's primitive strict positivity applies to every nonzero class of this Chow summand, not only to an unspecified quotient. Its Theorem 8.2 identifies the form with the pullback of the signed primitive Picard polarization, giving the stated Néron--Tate description.

For \(x=e_*x\) and \(y=(1-e)_*y\), the height projection formula gives

\[
h_{K'}(x,y)=h_{K'}(x,{}^t e(1-e)_*y)=0.
\]

Combining this with AR-1 and (AR.3) proves the exact gate and the strict-positivity assertion. Finite base change is harmless for classes descending to \(K\): normalized heights are unchanged, and pullback on rational Chow groups is injective since pushforward composed with pullback multiplies by \([K':K]\). \(\square\)

**Scope caution.** The decomposition is asserted over \(K'\). For a fixed initial \(K\), positivity on all of \(N(K')\) is a sufficient condition for positivity on descended classes, not a claim of logical equivalence with positivity over \(K\) alone. The exact equivalence in the theorem concerns the group over \(K'\). The theorem is a derived consequence of stated inputs; no claim of literature novelty is made.

## D. A small explicit complement which the reduction does not erase

Let \(E/K\) have an automorphism \(\rho\) of order six acting on \(H^{1,0}(E)\) by a primitive sixth root \(\zeta\), and assume this automorphism is defined over \(K\). For example take a \(j=0\) elliptic curve after extending its number field. On \(A=E^3\), use the product polarization and let \(\rho_\Delta=(\rho,\rho,\rho)\). Let \(\Pi=\pi_1\otimes\pi_1\otimes\pi_1\) be the degree-one tensor Chow projector. Put

\[
e_3=\Pi\,\frac16\sum_{r=0}^5(-1)^r\rho_\Delta^{*r}.
\tag{AR.5}
\]

**Proposition AR-3.** Equation (AR.5) is an actual rational Chow idempotent, self-transpose on the middle motive, and its motive \(T\) is primitive. Its Hodge realization has dimension two and types \((3,0),(0,3)\). Its entire \(\operatorname{CH}^2(T)\) lies in Beauville grade one and is homologically trivial. Consequently its height is a concrete surviving case of (AR-GATE), with positive-sign candidate \(h_K(z,z)\).

*Proof.* The cyclic group character projector is idempotent because the coefficient character \(r\mapsto(-1)^r\) is a rational character of the order-six group. It commutes with \(\Pi\). Transposition replaces group elements by their inverses and fixes the character projector; \(\pi_1\) of an elliptic curve is self-transpose. In the tensor \(H^1(E)^{\otimes3}\), the eigenvalues are \(\zeta^3=-1\), \(\zeta\), \(\zeta^{-1}\), and \(\zeta^{-3}=-1\), according to the number of holomorphic factors. The two all-holomorphic/all-antiholomorphic tensors are exactly the \(-1\)-eigenspace. Multiplication by each factor's divisor class kills the factor \(h^1(E)\), since it would land in \(h^3(E)=0\); this is exact in the Chow-motive grading. Hence \(L\Pi=0\), so \(T\) is primitive. Finally \(T\subset h^3(A)\), and \(\operatorname{CH}^2(h^3(A))=\operatorname{CH}^2_{(1)}(A)\). It has zero ordinary degree-four cycle realization. \(\square\)

This is a specified motive and a specified height problem. It is not an assertion that \(\operatorname{CH}^2(T)\) is known to contain a nonzero class, nor an assertion that all its heights have been determined. No general height-to-\(L'\) identity for this group follows from the supplied papers.

### D.2 The complementary gate contains a nonzero Fermat-quartic cycle

**Theorem AR-7 (a nonzero CM complementary class).** Let \(C:x^4+y^4=z^4\), let \(J=\operatorname{Jac}(C)\), and choose a degree-one base class after a finite number-field extension. Write
\[
\kappa=[C]-[-1]_*[C]\in\operatorname{CH}^2(J)_{\rm hom,\mathbf Q}.
\]
Let \(\pi_P\) be the primitive middle Chow projector for a symmetric theta divisor, and let \(e\) be the Picard-summand projector of AR-2. Then
\[
z_N=(\pi_P-e)_*\kappa\in\operatorname{CH}^2(N)
\tag{AR.9}
\]
is nonzero modulo algebraic equivalence, even over \(\overline{\mathbf Q}\). In particular (AR-GATE) is a genuine remaining sign problem on a group containing a specified nonzero class. In this example \(H(N)\) has precisely types \((3,0),(0,3)\), each of dimension one.

*Proof.* Bloch, *Algebraic cycles and values of L-functions*, J. reine angew. Math. 350 (1984), Lemma (3.1), p.99, gives an isogeny \(J\to E^2\times E'\), of degree a power of two, where \(E:y^2=x^3-x\) and \(E':y^2=x^3+x\). Thus \(J\) is CM; over \(\overline{\mathbf Q}\) it is isogenous to the cube of a \(j=1728\) elliptic curve. Bloch's Theorem (4.1), p.104, says that this Ceresa cycle has infinite order modulo algebraic equivalence. Its class modulo algebraic equivalence is independent of the chosen embedding (Theorem (3.4) and following text, p.102).

We first check that \(\kappa\) has grade one, so the Chow projector \(\pi_3\) does not discard its nonzero Griffiths class. It is odd under \([-1]^*\), hence only odd Beauville grades can occur. The Fourier isomorphism
\[
\mathcal F:\operatorname{CH}^2_{(s)}(J)
 \simeq\operatorname{CH}^{1+s}_{(s)}(\widehat J)
\]
kills every odd \(s\ge3\), by dimension, and every odd \(s\le-3\), by negative codimension. For \(s=-1\) the target is \(\operatorname{CH}^0_{(-1)}(\widehat J)=0\), since \(\operatorname{CH}^0\) is spanned by the fundamental class and has grade zero. Therefore \(\kappa\in\operatorname{CH}^2_{(1)}(J)=\operatorname{CH}^2(h^3J)\).

Motivic Lefschetz gives \(h^3(J)=P\oplus Lh^1(J)\). The codimension-two Chow group of the second summand is an image under \(L\) of \(\operatorname{Pic}^0(J)_{\mathbf Q}\); all these classes are algebraically trivial. The same is true of \(\operatorname{CH}^2(M)\), by AR-2. Consequently
\[
\kappa-z_N=(1-\pi_P)_*\kappa+e_*\kappa
\]
is algebraically trivial. Bloch's theorem now forces \(z_N\) to be nonzero modulo algebraic equivalence. This argument is unchanged after finite extension.

For the final Hodge-type assertion, the rational CM decomposition of \(H^3(E^3)\) splits off its two extreme types \((3,0),(0,3)\). One can see rationality explicitly by applying the scalar CM endomorphism \(1+i\): its eigenvalues on the extreme types satisfy \(T^2+4T+8\), while those on \((2,1),(1,2)\) satisfy \(T^2-4T+8\). These coprime rational polynomials give the two rational Hodge substructures. The full level-one part has dimension \(18\). The Lefschetz summand \(LH^1(J)\) is six-dimensional and lies entirely in that part. The extreme two-dimensional substructure is already primitive, by Hodge type. Thus the primitive middle piece has a twelve-dimensional maximal level-one part and the indicated two-dimensional complement. \(\square\)

This proof refutes a CM-wide assertion that homological triviality is algebraic triviality up to torsion: the rational Griffiths quotient is nonzero already for this CM Jacobian. It does not refute the arithmetic Hodge-index sign conjecture. The new statement here is the precise placement of the known nonzero cycle in the orthogonal complementary Chow summand, using AR-2; Bloch's nonvanishing theorem is an accepted established input.

The Beauville Fourier grading used above is the standard Fourier decomposition (Beauville, *Sur l'anneau de Chow d'une variété abélienne*, Math. Ann. 273 (1986), 647--651). An explicitly read statement with the grading convention is Shen--Vial, *The Fourier transform for certain hyperkähler fourfolds*, Introduction A, p.2, displayed (1) and property (a). Its Fourier inversion is also recalled in Künnemann 1993, §2, printed p.88.

### D.3 A canonical nonzero complementary cycle with an exact local height formula

**Theorem AR-8 (Fermat symmetry and Gross--Schoen reduction).** For the Fermat quartic choose the hyperflex \(P_0=(1:0:1)\) and its Abel embedding \(f(x)=[x-P_0]\). Let \(X_1\) be the grade-one part of \(f_*[C]\), and set
\[
\eta=\mathcal F(X_1)\in\operatorname{CH}^2(J).
\]
One can choose the splitting in AR-2 so that \(\eta\in\operatorname{CH}^2(N)\). This class is nonzero modulo algebraic equivalence. Let \(K'\) contain the relevant definitions and admit a semistable model of \(C\), and put
\[
\Omega_{K'}=\frac{\omega_a^2}{[K':\mathbf Q]},
\qquad
\Phi_{K'}=\frac{1}{[K':\mathbf Q]}
 \sum_v\varphi(C_v)\deg(v).
\]
Then the raw normalized middle height has the exact value
\[
h_{K'}(\eta,\eta)
 =\frac16 h_{K'}(\Delta_{P_0},\Delta_{P_0})
 =\frac7{24}\Omega_{K'}-\frac16\Phi_{K'}.
\tag{AR.10}
\]
Thus this specified nonzero complementary class has nonnegative height exactly when \(7\Omega_{K'}\ge4\Phi_{K'}\), and strictly positive height exactly when the inequality is strict. There is no positive Picard contribution to subtract for this choice of splitting.

*Proof.* The tangent \(x=z\) meets \(C\) at \(P_0\) with multiplicity four, so \(K_C\sim4P_0\). Let \(G=\mu_4^2\) act by the two coordinate scalings on the affine equation \(x^4+y^4=1\). Each \(\gamma P_0\) satisfies \(4\gamma P_0\sim K_C\), so \(\gamma P_0-P_0\) is four-torsion in \(J\). Translation by a torsion point acts identically on rational Chow groups: if \(na=0\), then \([n]\circ t_a=[n]\); since \([n]_*\) is invertible on rational Chow groups by the Chow--Künneth eigenvalue decomposition, \([n]_*t_{a*}=[n]_*\) implies \(t_{a*}=1\). Therefore the class \(f_*[C]\), its grade-one part, and its Fourier transform \(\eta\) are \(G\)-invariant. The last assertion uses the \(G\)-invariance of the symmetric principal theta class; the Fourier kernel is consequently \(G\)-equivariant.

The holomorphic differentials have \(G\)-characters
\[
(1,1),\quad(1,2),\quad(2,1)\qquad\text{in }(\mathbf Z/4)^2.
\]
Their exterior triple has trivial character. In a mixed exterior triple of type \((2,1)\), canceling a holomorphic and antiholomorphic character leaves one of the three nonzero characters above; using three distinct indices gives \((0,2),(2,0),(2,2)\), again nonzero. Conjugation handles type \((1,2)\). Hence \(H^3(J)^G\) consists exactly of the two extreme Hodge types. In particular it has no overlap with \(W=H(M)\).

Let \(p_G=|G|^{-1}\sum_{\gamma\in G}\gamma_*\). This is an exact self-transpose Chow idempotent. It commutes with the primitive projector because \(G\) preserves theta. In AR-2 replace the constructed inclusion by
\[
u'=(1-p_G)u.
\]
Its realization is unchanged on \(W\); therefore the same adjoint argument gives a split inclusion and a self-transpose projector \(e'\). Now \(p_Gu'=0\) holds exactly, and transposition gives \((u')^\dagger p_G=0\), hence \(e'p_G=0\). Since \(p_G\eta=\eta\), we get \(e'\eta=0\). Zhang's Theorem 1.5.6 says \(\eta\) is primitive; therefore \(\eta\in\operatorname{CH}^2(N)\) for this splitting.

By AR-7, the Ceresa class is \(2X_1\) and is nonzero modulo algebraic equivalence. Fourier is an invertible algebraic correspondence and preserves algebraic equivalence, so \(\eta\) is likewise nonzero. Zhang, *Gross--Schoen cycles and dualising sheaves* (2010), Theorem 1.5.6, printed p.14, gives the first equality in (AR.10) in genus three. His Theorem 1.3.1, printed p.5, gives the second because \(P_0-K_C/4=0\) in the rational Picard group. Dividing every global intersection by \([K':\mathbf Q]\) gives the displayed normalization. \(\square\)

The theorem makes the remaining calculation concrete; it does not establish the inequality in (AR.10). Good finite places contribute zero to \(\Phi_{K'}\). For the displayed integral plane quartic, every odd prime is a smooth-reduction prime by the partial derivatives. Thus only places over \(2\) and the archimedean places can contribute to \(\Phi_{K'}\). The admissible self-intersection \(\Omega_{K'}\) also includes arithmetic metric and model information. A computation of these terms, including the semistable reduction at \(2\), would settle the height of this cycle. Positivity of this one nonzero class would still not establish positivity of the whole group \(\operatorname{CH}^2(N)\).

### D.4 The finite local term is strictly positive; the archimedean gate is explicit

**Proposition AR-9 (local arithmetic progress for the Fermat cycle).** Work over a number field \(K'\) on which \(C\) is semistable. For each finite place set
\[
b_v=\frac1{18}\operatorname{ord}_v(\chi'_{18})-\lambda(\Gamma_v),
\]
and put
\[
D_2=\frac1{[K':\mathbf Q]}\sum_{v\mid2}\delta(\Gamma_v)\log N(v),\qquad
A_\infty=\frac1{[K':\mathbf Q]}\sum_{v\mid\infty}
\left(-\frac1{18}\log\|\chi'_{18}\|_{\mathrm{Hdg},v}-\lambda(C_v)\right),
\]
using de Jong's archimedean multiplicity convention. Then
\[
h_{K'}(\eta,\eta)
 =\frac72\left(
  \frac1{[K':\mathbf Q]}\sum_{v\mid2}b_v\log N(v)+A_\infty
 \right)
 \ge\frac{D_2}{6}+\frac72 A_\infty,\qquad D_2>0.
\tag{AR.12}
\]
In particular \(A_\infty>-D_2/21\) is a sufficient condition for strict positivity of this specified nonzero complementary class. Moreover the graph contribution in (AR.10) is explicitly
\[
\varphi(\Gamma_v)=\frac43\,\delta(\Gamma_v)\qquad(v\mid2).
\tag{AR.13}
\]

*Proof.* Van Bommel--Docking--Dokchitser--Lercier--Lorenzo García, *Reduction of Plane Quartics and Cayley Octads*, Table 7.1 in the read preprint (published version Table 9), identifies the Fermat curve's stable reduction at \(2\) as type \((0eee)\): one genus-zero central component with three elliptic tails. The source cites Liu, *Algebraic Geometry and Arithmetic Curves*, Example 10.4.39, for this characteristic-two calculation. We use the stated stable type; Liu's example itself has not yet been directly read. The dual graph is a tree, all three edges separate genus one from genus two, and all have strictly positive thickness. The curve has smooth nonhyperelliptic reduction at every odd prime, so \(b_v=0\) there.

De Jong, *On the height of Gross--Schoen cycles in genus three* (2018), Theorem 8.2, expresses the canonical Gross--Schoen height as \(21\) times the sum of these finite and archimedean terms. Divide by \([K':\mathbf Q]\) and by \(6\), using AR-8, to obtain the equality in (AR.12). De Jong's Lemma 11.2 applies to every genus-three metrized tree and proves \(b_v\ge\delta(\Gamma_v)/21\). This proves the inequality and \(D_2>0\).

For (AR.13), Zhang 2010, Proposition 4.4.1, printed pp.58--59, gives the separating-edge contribution \(2i(g-i)\ell_e/g\). Here \(g=3,i=1\) for all edges, and there is no cyclic contribution, so summing gives \(4\delta(\Gamma_v)/3\). One may also check the accompanying invariant from de Jong, Example 5.4: \(\lambda(\Gamma_v)=2\delta(\Gamma_v)/7\). The inequality \(b_v\ge\delta_v/21\) is then \(\operatorname{ord}_v(\chi'_{18})\ge6\delta_v\), exactly the tree bound used in his proof. \(\square\)

This is a genuine determination of the sign of the finite local contribution in the \(\chi'_{18}\)-formula. It is not a determination of the global sign: the remaining archimedean term must be evaluated or bounded. Neither (AR.12) nor (AR.13) identifies the bad-prime logarithmic coefficient of the different automorphic comparison (AR.11); those two local decompositions must not be conflated.

**Subsequent resolution for this class, AR-12 and AR-13.** The companion FERMAT_THETA_GATE.md reduces the archimedean term to an explicit logarithmic theta integral at the exact Fermat period matrix. FERMAT_THETA_CERTIFICATE.md combines a new finite Hodge-lattice estimate JAC-P10 with a deterministic, enclosed theta computation to prove \(h_K(\eta,\eta)>1/100\). The computation uses a torsion-grid lower bound for the Frobenius-theta mean and a cell-Jensen upper bound for the ordinary-theta mean; it does not use an \(L'\)-height comparison. The final certificate and its independent-review status are in fermat_theta_certify.py/.json and CHECK_EVENTS.tsv. This settles the sign on \(\mathbf Q\eta\), while positivity on the full complementary Chow group remains open.

**Corollary AR-14 (a positive arithmetic space containing a Griffiths class).** For the Fermat threefold and the splitting chosen in AR-8, the height is strictly positive on
\[
\operatorname{CH}^2(M)(K')_{\mathbf Q}\oplus\mathbf Q\eta.
\]
Indeed AR-2 gives strict positivity on the first summand and orthogonality to \(\eta\in\operatorname{CH}^2(N)\); AR-13 gives positivity on the second. Thus \(h(x+a\eta,x+a\eta)=h(x,x)+a^2h(\eta,\eta)\), which is positive unless both terms vanish. No assertion that \(\eta\) spans \(\operatorname{CH}^2(N)\) is needed or made.

## E. Mixed-characteristic and constant-family checks

The correct arithmetic analogue of an intersection formula has the form

\[
h_K(z,z')=\frac1{[K:\mathbf Q]}\widehat{\deg}
 \bigl(\widehat z^{\mathrm{adm}}\cdot\widehat z'^{\mathrm{adm}}\bigr),
\tag{AR.6}
\]

with vertical-orthogonal extensions and the compatible Green-current data. Künnemann 2001, §1.2--1.4, is the exact construction used here. Thus a raw closure intersection does not become a height merely by inserting \((-1)^m\). The parent's quadric counterexample to the uncorrected pencil formula is consistent with this distinction: integral fibers do not remove all higher-codimension local correction terms.

**Constant-family check.** For the constant family \(B\times C\to C\) over a field \(k\), and a constant section \(s_P\) with \(P\in B(k)\), the geometric canonical height over \(k(C)\) is zero. Indeed the pullback of a line bundle from \(B\) along the constant map is a constant one-dimensional vector space tensored with \(\mathcal O_C\), hence has degree zero; the same holds after every multiplication by \(n\). If \(k=K\) is a number field and \(P\) is nontorsion, its arithmetic Néron--Tate height on \(B/K\) is strictly positive for an ample polarization. Therefore the arithmetic value cannot be recovered from that geometric degree alone. The missing term is genuine arithmetic metric/finite-place information. This is a counterexample to any claimed direct replacement of a geometric height by the number-field height with all these terms omitted, not a counterexample to a correctly normalized biextension formula.

For ordinary divisors, Faltings--Hriljac gives \(h_K(D,D)<0\) when the Jacobian class of \(D\) is nontorsion. For a primitive codimension-two class on a threefold the proposed positive sign is \(+h_K\). These two low-dimensional checks prevent an unsigned “BB is NT-positive” statement.

## F. What GRH actually gives

**Lemma AR-4 (central sign).** Let \(F\) be holomorphic in a neighborhood of the real interval \([c,\infty)\), real on that interval, positive for sufficiently large real arguments, and nonzero for every real \(s>c\). If \(F\) vanishes to order \(r\ge1\) at \(c\), then \(F^{(r)}(c)>0\). In particular \(F'(c)\ge0\), with strict inequality exactly when \(r=1\).

*Proof.* Continuity and the absence of a real zero on \((c,\infty)\) give \(F(s)>0\) there. In the expansion \(F(c+t)=a_rt^r+O(t^{r+1})\), \(a_r\) is real and nonzero. Positivity for small \(t>0\) forces \(a_r>0\), and \(F^{(r)}(c)=r!a_r\). \(\square\)

If \(F=G L\), with \(G(c)>0\) real and \(L(c)=0\), then \(F'(c)=G(c)L'(c)\). Thus GRH supplies the lemma's zero-free interval for an appropriately normalized real self-dual completed \(L\)-function, provided poles and the positivity normalization have also been handled. A complex non-self-dual Hecke \(L\)-function has no ordered derivative sign until an appropriate real combination has been specified.

**Corollary AR-5 (conditional height sign).** If a proven formula gives \(q_A(z,z)=C L'(c)\), \(C>0\), with the hypotheses of AR-4, then \(q_A(z,z)\ge0\). It is strictly positive if the central zero is simple. If the central zero has higher order, the formula gives zero; it does not prove \(z=0\). To deduce positivity for an entire cycle space one needs a spanning family and control of cross terms, or a formula for every vector in that space. A regulator determinant alone is insufficient: the real symmetric matrix \(\operatorname{diag}(-1,-1,1,\ldots,1)\) has positive determinant and is not positive definite.

The attached Alpöge `Statements.lean` quantifies over Dirichlet characters \(\chi:\operatorname{DirichletCharacter}(\mathbf C,N)\). Its `Main.lean` proves exactly those advertised Dirichlet statements from imported results; it contains no theorem for arbitrary number-field Hecke characters. We accept the cited theorem; this is a scope check, not a re-verification of its proof. The Masullo index labels 14.1.2.1 (printed p.529) a **Conjecture**, and 14.1.2.3 (p.531) a proposition conditional on that conjecture and 14.1.2.2. The row on p.522 whose opening reads "13.3.1.2 (Divisor of L(s, chi))" includes unfinished statement text (the index parses its number as 13.3.1). Accordingly any use of broad Hecke GRH is explicitly **conditional (Hecke-GRH/Masullo)**. No such input supplies the height identity in AR-5.

### F.2 The concrete CM derivative and the newer triple-product comparison

Bloch 1984, Proposition (5.2), printed p.107, proves that the Hecke \(L\)-function of the Fermat-quartic rank-two motive of types \((3,0),(0,3)\) has a simple zero at \(s=2\). This is a theorem about order of vanishing. The proposition does not state an arithmetic height identity or an ordered sign for the derivative. The introduction, printed p.95, explicitly presents the height formula as a possible further assertion. Thus the supplied Dirichlet-GRH theorem, Bloch's nonvanishing, and (AR.10) are three distinct inputs.

**New analytic deduction AR-11.** The companion proof FERMAT_LDERIVATIVE_SIGN.md proves unconditionally
\[
L'(M,2)>\frac7{20}>0
\]
for this particular Fermat rank-two motive, using the known character \(\psi^3\mu\), its conductor \(64\), its root number \(-1\), and an elementary Mellin-transform tail estimate. A supplementary certified interval is \(1.5071685<L'(M,2)<1.5071697\). Thus the analytic sign is no longer a gate for this example. The geometric height identity or local-height inequality remains a separate requirement.

A stronger next comparison is available in Yuan--Zhang--Zhang, *Triple product L-series and Gross--Kudla--Schoen cycles*, manuscript dated 14 November 2023, with appendix by Yifeng Liu. Proposition 1.3.2, printed p.7, expresses the trilinear cycle height as a coefficient \(\mathcal L(\pi)\) times a product of local invariant pairings. Theorem 1.3.3, printed p.8, states
\[
\mathcal L(\pi)=
\frac{16\zeta_F(2)^2}{L(1,\pi_L,\mathrm{ad})}
 L'(1/2,\pi_L)+\sum_{p\in S}c_p\log p,
\qquad c_p\in\overline{\mathbf Q},
\tag{AR.11}
\]
where \(S\) consists of rational primes below ramification places of \(\pi\). The exact generalized Gross--Kudla formula holds in their everywhere-unramified case. This is stronger than the older September 2012 manuscript, Theorem 1.2.4, whose hypotheses included at least two finite nonsplit quaternion places.

The Fermat quartic is \(X_0(64)\); for example the explicit modular-form embedding and the relation \(x^4+y^4=z^4\) are given in Fang-Ting Tu, *Arithmetic of Quaternion Orders and Its Applications* (Waseda dissertation, February 2012), §5.3.2, p.59. Hence the relevant modular elliptic constituents are unramified away from \(2\). If one carries out the precise trilinear-cycle identification and the local test-vector normalizations for this example, the possible correction in (AR.11) is supported at \(2\). Its shape is \(c_2\log2\); its vanishing or sign is not supplied by an \(L\)-function zero-free theorem. The whole identification is retained as a task, rather than treating a general modular parametrization as an automatic equality with \(\eta\).

The newer Gao--Zhang manuscript, *Heights of Ceresa and Gross--Schoen cycles*, Theorems 1.1 and 1.4, constructs canonical adelic height objects and proves a lower bound on a suitable Zariski-open part of moduli. This offers genuine geometry for the Bost route below. A bound with an additive constant on an unspecified open subset does not determine the sign at this fixed Fermat point. The specific formula (AR.10), or a completed comparison including the term in (AR.11), remains the concrete height gate.

AR-13 subsequently proves the required local-height inequality for the specified Fermat class directly. The full complementary-group inequality and the automorphic cycle/test-vector comparison, including \(c_2\), remain distinct unresolved tasks.

## G. Testing the two suggested Alpöge mechanisms

### G.1 Sign-only Weil/explicit-formula route

The note's footnote 3, printed p.3, explains the sign in the finite-field trace calculation using concentration in middle cohomology and the opposing zero-mode parity, with a bound from repeated Parseval. Step 5 (pp.3--4) changes to a von Mangoldt/Guinand--Weil variance setup. Neither statement identifies the cycle intersection or arithmetic height form with the analytic form.

A minimal algebra check isolates the missing information. Let \(F=pI\) on \(\mathbf Q^2\), \(p>0\). Both \(b_+=I\) and \(b_\pm=\operatorname{diag}(1,-1)\) satisfy \(F^tbF=p^2b\); they have the same Frobenius eigenvalues and traces and different signatures. Thus eigenvalue purity and trace parity do not determine a compatible form's signature. This is an information-loss test, not a proposed geometric counterexample. A valid geometric transfer still needs an identification of the form and its polarization.

### G.2 Bost slope route

Bost, *Algebraic leaves of algebraic foliations over number fields*, Publ. Math. IHES 93 (2001), §4.1.4, Proposition 4.5, equation (4.11), gives for an injective \(K\)-linear map between hermitian bundles

\[
\widehat{\deg}_{n}(E)
\le\operatorname{rk}(E)\bigl(\widehat\mu_{\max}(F)+h(\varphi)\bigr).
\tag{AR.7}
\]

Proposition 4.6, equation (4.14), is its filtered version. The note's step 13, p.4, names this inequality. The attached Lean map points to `Formalism/LatticeSlopes/LatticeSlopesProofs/SlopeInequality.lean` and `Formalism/LatticeSlopes/Statement.lean`; these implementation files were **not attached or read**, and no claim is made to have run them.

**Proposition AR-6 (precise slope gate).** Suppose that a geometric construction associates to a cycle \(z\) a hermitian line \(\overline{\mathcal B}_z\) with \(\widehat{\deg}_n\overline{\mathcal B}_z=q_A(z,z)\), and an injective map \(\varphi:\mathcal B_z^\vee\to F_z\) satisfying

\[
\widehat\mu_{\max}(F_z)+h(\varphi)\le0.
\tag{AR.8}
\]

Then \(q_A(z,z)\ge0\); a strict upper bound in (AR.8) gives strict positivity.

*Proof.* Apply (AR.7) to the rank-one source \(\overline{\mathcal B}_z^\vee\), whose normalized degree is \(-q_A(z,z)\). \(\square\)

The hypotheses in AR-6 are substantive: the line must be the cycle's canonical arithmetic biextension/height object, and the map and norm bounds must be proved. Merely declaring a trivial line to have metric \(e^{-q_A(z,z)}\) is circular. To see why the inequality by itself yields no sign, let \(E_a=(\mathcal O_K,\|1\|_\sigma=e^{-a})\). Then \(\widehat{\deg}_n(E_a)=\widehat\mu_{\max}(E_a)=a\), and the identity map has height zero. Equation (AR.7) becomes \(a\le a\) for every positive or negative real \(a\).

This explicitly tests the next tool: a Bost proof of (AR-GATE) would require (AR.8) for the height line of every class in the complementary motive \(N\), including local and archimedean terms. Neither the four-page note nor the supplied Lean map provides this bridge. On the Picard summand the Poincaré biextension already gives the canonical object and the result is known independently.

**Construction supplied by AR-10.** Root's work/root/AR10_adelic.tex, independently whole-read here, specializes Gu 2026, Theorem 1.3 and Proposition 5.3, to the exact middle signed height and constructs \(\overline{\mathcal B}_z\) as a metrized Deligne pairing. This resolves the construction of the height line for a chosen rational representative, with representative-independent arithmetic degree. The resulting line is integrable adelic. One applies the adelic rank-one slope inequality, or a justified model passage to Bost's hermitian version; clearing rational tensor powers by itself is not that passage. The injection and its norm/slope bound remain open.

## H. Sources and reading record

- Attached 032: Theorem 1.1; Lemma 8.1; Corollary 8.2 and its proof. Accepted inputs; targeted statement/codimension reading.
- Attached cote 44 scan004: Theorem 5 and its margin. It assumes algebraically trivial generic restrictions; its printed intersection formula is handled separately by the parent's H9 counterexample and correction.
- Künnemann 1993: https://gdz.sub.uni-goettingen.de/download/pdf/PPN356556735_0113/LOG_0011.pdf . Direct PDF downloaded, rendered printed pp.96--98; Theorems 5.1,5.2, Corollary 5.3 directly read.
- Künnemann 1996: DOI https://doi.org/10.1353/ajm.1996.0033 . Primary paper's indexed PDF at https://citeseerx.ist.psu.edu/document?doi=24752c170be79846ab861e9c80a8977cac60035f&repid=rep1&type=pdf . Web retrieval exposed full extracted text after direct-download failures. Lemma 4.1, equation (18), Theorems 6.1,8.2,9.1,12.1, and Remark 12.2 were targeted-read; not a full proof audit.
- Künnemann 2001: https://www.numdam.org/item/10.1016/s0012-9593(01)01068-0.pdf . §1.2--1.4, Theorem 1.6, Corollary 1.7 directly read via extracted primary PDF.
- Milne, Abelian Varieties v1.10: https://www.jmilne.org/math/CourseNotes/AV110.pdf . Proposition 16.10, printed p.65, model over a number field; statement read, proof omitted in this source.
- Zhang 2010: https://web.math.princeton.edu/~shouwu/publications/gross-schoen.pdf . §5.3, p.68, height selection; directly read.
- Laga--Shnidman: https://arxiv.org/pdf/2312.12965 . Proposition 4.5, Proposition 5.9 and Proposition 5.10 directly read; Kings Prop.2.2.1 is cited through this source, not directly read.
- Bost 2001: https://www.numdam.org/item/PMIHES_2001__93__161_0.pdf . §4.1.4, Propositions 4.5--4.6, equations (4.11),(4.14), directly read.
- Gu 2026: https://arxiv.org/abs/2609.33223 . Local primary v2 read at work/references/Gu2026.pdf/.txt: Theorem 1.3, Proposition 5.3, §2.2 and Corollary 1.6; root's complete AR-10 proof independently checked against these statements.
- Additional Fermat derivative sources, calculation and application-scope checks: see FERMAT_LDERIVATIVE_SIGN.md and KNOWN_STATEMENT_COMPARISONS.md.
- Attached Alpöge note: pp.3--4, footnote3, steps5 and13; attached Main/Statements; Lean-map §4 and §5. No formal build and no claim to inspect omitted implementation files.
- Attached Masullo index: rows 13.3.1.2,14.1.2.1,14.1.2.3. The full paper is not attached; broad Hecke GRH is retained as an explicit hypothesis.

## I. Self-check summary

AR-1: exponent \(g-i-e=s-2\) checked; grade zero of symmetric \(\ell\) checked; no unproved Beauville vanishing inserted. AR-2: codimension \(b+m-1\), twist \(1-m\), Chow degree \(m+(1-m)=1\), exact inverse specifically in \(h^1\), self-transpose projector, incidence injection, field extension scope, and height orthogonality each checked. AR-3: idempotent group algebra character, transpose/inverse, eigenvalue multiplicities \(1,3,3,1\), primitive tensor action, and grade \(2p-i=1\) checked. AR-4: poles, real-valuedness, positivity normalization, order of zero, and derivative/leading-coefficient distinction checked. AR-6: dual-source sign and rank-one rescaling test checked. AR-7: Fourier odd-grade elimination, primitive versus Lefschetz summand, algebraic triviality of the discarded terms, and the two CM characteristic polynomials checked; root independently confirmed this argument. AR-1a: all negative grades and the homologically trivial grade-zero divisor image checked. AR-8: hyperflex canonical class, torsion translation using invertible multiplication, all twenty exterior character triples, exact averaged-projector annihilation, and the constants 7/24 and 1/6 checked. The character enumeration independently returned only the all-holomorphic and all-antiholomorphic triples as invariant.

Remaining parent-facing review request: independently check AR-2's motivic-adjoint sign and field-descent argument before promoting it in the final paper. It is a complete written argument from stated background, not a formal certificate and not a claimed solution of (AR-GATE).
