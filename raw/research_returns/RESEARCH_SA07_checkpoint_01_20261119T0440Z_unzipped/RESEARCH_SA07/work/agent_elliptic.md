# Elliptic Hodge splittings: checked formulas, CM calculations, and the exact remaining gate

Author: OpenAI GPT-6 Astra, agent `/root/elliptic_splitting`, 19 November 2026. This file records work performed in this run. It makes no priority claim. All assertions below concern a fixed embedding of algebraic numbers into C. A statement marked **unsettled here** has neither a proof nor a counterexample in this file.

## 1. What is actually written on 18:13

The transcription `MPL_15_195-228+18_002-017_18_scan013.tex` writes the Hodge splitting parameter as an element of the additive quotient C/Qbar. It asks whether that class can be represented by an algebraic number for a curve without complex multiplication. The page does not choose a unique second differential or a unique scalar representative. Consequently an explicit scalar must be accompanied by a de Rham basis. The algebraicity property is invariant under the algebraic changes of basis described below.

The hard unresolved statement is exactly Katz's Question 4.0.8, printed p.501 of *p-adic interpolation of real analytic Eisenstein series* (1976). Katz phrases it both through simultaneous algebraicity of the three lattice functions g2, g3, S and through the Hodge splitting of algebraic de Rham cohomology. His preceding Lemma 4.0.7 proves the CM direction. I opened the complete primary PDF, rather than relying on a later paraphrase.

## 2. Full-period, quasiperiod, and de Rham conventions

Let k be an algebraic subfield of C and

\[
E/k:\quad y^2=4x^3-g_2x-g_3,\qquad
g_2^3-27g_3^2\ne0.
\]

Set \(\omega=dx/y\), \(\xi=x\,dx/y\). These are an algebraic de Rham basis of \(H^1_{\rm dR}(E/k)\), with \(F^1=k\omega\). Uniformize by

\[
\mathbf C/\Lambda\longrightarrow E(\mathbf C),\quad
z\longmapsto(\wp_\Lambda(z),\wp'_\Lambda(z)),
\]

where \(\Lambda=\mathbf Z\omega_1+\mathbf Z\omega_2\) is oriented by \(\operatorname{Im}(\omega_2/\omega_1)>0\). The periods here are **full periods**. Define

\[
\tau=\omega_2/\omega_1,\qquad
\eta_i=\zeta_\Lambda(z+\omega_i)-\zeta_\Lambda(z).
\]

Since \(\zeta'=-\wp\), the periods of \(\xi\) are \(-\eta_i\). With \(\gamma_1,\gamma_2\) the corresponding oriented homology basis, integration is the C-linear map

\[
I:H^1_{\rm dR}(E/k)\otimes_k\mathbf C
\longrightarrow\operatorname{Hom}_{\mathbf Z}(H_1(E(\mathbf C),\mathbf Z),\mathbf C),
\quad v\longmapsto\left(\gamma\mapsto\int_\gamma v\right).
\]

Its matrix, with forms as rows and cycles as columns, is

\[
P=\begin{pmatrix}\omega_1&\omega_2\\-\eta_1&-\eta_2\end{pmatrix},
\quad \det P=\eta_1\omega_2-\eta_2\omega_1=2\pi i. \tag{2.1}
\]

The last identity is Legendre's relation in these conventions. Replacing full periods by half-periods without changing this identity produces a factor-of-four error.

## 3. Exact Hodge splitting formula

**Proposition ELL-01 (proved).** Write

\[
H^{0,1}=\mathbf C(\xi+h\omega).
\]

Then, with \(A=\operatorname{Im}(\overline{\omega_1}\omega_2)=|\omega_1|^2\operatorname{Im}\tau>0\),

\[
\boxed{
h=\frac{\eta_1\overline{\omega_2}-\eta_2\overline{\omega_1}}
{\omega_1\overline{\omega_2}-\omega_2\overline{\omega_1}}
=\frac{\eta_1}{\omega_1}-\frac{\pi}{\omega_1^2\operatorname{Im}\tau}
=\frac{\pi^2}{3\omega_1^2}E_2^*(\tau).} \tag{3.1}
\]

**Proof.** The complex conjugate of the holomorphic class has periods \(\overline{\omega_i}\). Write it as \(a\omega+b\xi\); then \(a\omega_i-b\eta_i=\overline{\omega_i}\). Subtracting the two equations after multiplication by \(\omega_2,\omega_1\), respectively, and using (2.1), gives \(b=-A/\pi\ne0\). Thus its line is \(\mathbf C(\xi+(a/b)\omega)\), and elementary elimination gives the first expression in (3.1). Substitute \(\omega_2=\tau\omega_1\), \(\overline{\omega_2}=\overline\tau\,\overline{\omega_1}\), and \(\eta_2=\tau\eta_1-2\pi i/\omega_1\); this gives the second expression. The Fourier identity \(\eta_1\omega_1=\pi^2E_2(\tau)/3\) gives the third. Every denominator used is nonzero. QED.

The normalizations are

\[
E_2=1-24\sum_{n\ge1}\sigma_1(n)q^n,\quad
E_4=1+240\sum_{n\ge1}\sigma_3(n)q^n,\quad
E_6=1-504\sum_{n\ge1}\sigma_5(n)q^n,
\]

\[
q=e^{2\pi i\tau},\qquad E_2^*=E_2-\frac3{\pi\operatorname{Im}\tau},
\qquad
g_2=\frac{4\pi^4}{3\omega_1^4}E_4,\quad
g_3=\frac{8\pi^6}{27\omega_1^6}E_6. \tag{3.2}
\]

Katz's function \(S(E,\omega)\) is \(-12h\) in this basis. In his Fourier convention \(\omega_1=2\pi i\), that equality gives \(S=E_2^*\). This agrees with his Lemma 1.3.6 and equation (1.3.7), printed p.467, equation (1.3.10), p.468, and with his de Rham normalization in §1.2.

For an algebraic adapted basis \(\omega'=r\omega\), \(\xi'=s\xi+t\omega\), where \(r,s\in\overline{\mathbf Q}^{\times}\), \(t\in\overline{\mathbf Q}\), the same line has parameter

\[
h'=(s h-t)/r.
\]

This explicit affine transformation proves invariance of the assertion \(h\in\overline{\mathbf Q}\). It also shows why a basis-free class should not be confused with a canonical numerical value.

## 4. CM algebraicity, with an explicit nonzero value

**Proposition ELL-02 (proved).** For an elliptic curve over Qbar with CM, \(h\in\overline{\mathbf Q}\).

**Proof.** Choose a nonreal endomorphism \(u\in\operatorname{End}(E)\subset\mathbf C\). It is defined over a finite algebraic extension of the coefficients, and pullback on algebraic de Rham cohomology is algebraic. Its action on \(H^{1,0}\) is multiplication by u and on \(H^{0,1}\) by \(\overline u\). In the chosen de Rham basis it therefore has

\[
u^*\omega=u\omega,\qquad u^*\xi=a\omega+\overline u\,\xi,
\quad a\in\overline{\mathbf Q}.
\]

The identity \(u^*(\xi+h\omega)=\overline u(\xi+h\omega)\) yields \(a+u h=\overline u h\). Hence \(h=a/(\overline u-u)\), an algebraic number. Extending the number field does not change the complex line or the property of being defined over Qbar. QED. This is the mechanism in Katz Lemma 4.0.7.

**Example ELL-03 (exactly checked).** On

\[
E:\ y^2=4x^3-30x-28
\]

one has \(j=8000\), CM by \(\mathbf Q(\sqrt{-2})\), and \(h=1/2\) in the basis \((dx/y,x\,dx/y)\).

Here is an algebraic calculation avoiding numerical recognition. Put \(X=x+2\), \(Y=y/2\); the equation becomes

\[
E_0:Y^2=X^3-6X^2+\tfrac92X.
\]

The rational formulas

\[
X'=X-6+\frac9{2X},\qquad
Y'=Y\left(1-\frac9{2X^2}\right)
\]

give a normalized degree-two isogeny \(\varphi:E_0\to E_1\), where

\[
E_1:Y'^2=X'^3+12X'^2+18X'.
\]

The equation is verified by substitution. The map extends to the smooth projective curves, carries the identity to the identity, and has degree two because \(X'\) is a degree-two rational function of X. Its differential pullback is \(\varphi^*(dX'/(2Y'))=dX/(2Y)\).

Let \(u=\sqrt{-2}\). Scaling \(s:E_0\to E_1\), \((X,Y)\mapsto(u^2X,u^3Y)\), is an isomorphism. Thus \(\alpha=s^{-1}\varphi\) is an endomorphism of degree two and \(\alpha^*\omega=u\omega\); since u is nonrational this proves CM. Moreover

\[
d(Y/X)=\left(X-\frac9{2X}\right)\omega,
\]

\[
\alpha^*\xi/u=(-X'/2-2)\omega
=(-X+1)\omega+\tfrac12d(Y/X).
\]

Since \(\xi=(X-2)\omega\), its de Rham class satisfies \(\alpha^*\xi=-u\xi-u\omega\). Proposition ELL-02 now gives \(h=(-u)/(-2u)=1/2\). The complete rational-function checks are in `work/code_elliptic/verify_cm_isogeny.py` and its saved output. The discriminant in (3.2) is 5832, giving \(1728\cdot30^3/5832=8000\).

## 5. Masser's exact CM formula and normalization caveats

Masser, *Elliptic Functions and Transcendence*, LNM 437 (1975), Appendix One, defines on p.114, equation (100),

\[
\Psi(\tau)=\frac{3E_4(\tau)}{2E_6(\tau)}E_2^*(\tau).
\]

The capital letter here prevents a collision with the manuscript's Hodge-bigrading map \(\psi\). His Theorem A1 says that at imaginary-quadratic \(\tau\) away from the orbit of i, \(\Psi(\tau)\in\mathbf Q(j(\tau))\). In the region \(j\ne0,1728\), (3.2) gives the exact equality

\[
\boxed{h=(g_3/g_2)\Psi(\tau).} \tag{5.1}
\]

In particular, for a CM model with g2,g3 in the given algebraic field k, Masser's field inclusion gives h in k itself: j is already in k. For j=0 or1728 use h=0. Thus the final descent statement is over the coefficient field, even though the eigenspace proof in §4 temporarily enlarged it to define an endomorphism.

For completeness, the quantities in his equation (106), p.119, are as follows. Choose a primitive equation \(C\tau^2+B\tau+A=0\), with \(C>0\). Use the primitive matrix

\[
\mu=\begin{cases}
\begin{pmatrix}-B&-2A\\2C&B\end{pmatrix},&B\text{ odd},\\
\begin{pmatrix}-B/2&-A\\C&B/2\end{pmatrix},&B\text{ even},
\end{cases}\qquad D=\det\mu.
\]

Write the classical modular polynomial at \(j=j(\tau)\) as

\[
\Phi_D(j+X,j+Y)=\sum_{m,n\ge0}\beta_{mn}X^mY^n.
\]

For the ordinary case, \(\beta=\beta_{10}=\beta_{01}\ne0\) and

\[
\gamma=(\beta_{20}-\beta_{11}+\beta_{02})/\beta.
\]

For Masser's exceptional case, namely B odd and \(D=3d^2\) with integer \(d>1\), his Lemma A2 gives \(\beta=\beta_{30}=\beta_{03}\ne0\), \(\beta_{21}=\beta_{12}=0\), and

\[
\gamma=(\beta_{40}-\beta_{31}+\beta_{22}-\beta_{13}+\beta_{04})/\beta.
\]

Then

\[
\Psi(\tau)=9j\gamma+\frac{3(7j-6912)}{2(j-1728)}. \tag{5.2}
\]

This application of (5.2) is restricted to \(j\ne0,1728\), because the displayed derivation divides by \(j'(\tau)\). The values at the elliptic points are handled directly: \(h=0\) there. Applying the displayed rational formula naively at j=0 produces a spurious value and must be avoided. The theorem's algebraicity assertion at j=0 is direct.

The table on Masser's p.121 has \(\Psi(i\sqrt2)=15/28\), which together with \(g_3/g_2=28/30\) verifies the exact value in ELL-03. This is a separate check of the normalization, not the proof of CM or algebraicity in the example.

## 6. A complete zero classification for the specified scalar

**Proposition ELL-04 (proved).** For an arbitrary complex elliptic curve in the short Weierstrass normalization of §2,

\[
h=0\quad\Longleftrightarrow\quad j(E)\in\{0,1728\}.
\]

The required analytic statement is that the zeros of \(E_2^*\) on the upper half-plane are exactly the modular orbits of i and \(\rho=e^{2\pi i/3}\). An opened primary source giving a full proof is Sebbar–Besrour, *Zeros of Katz's p-adic Eisenstein series E2*, arXiv:2611.14502v1, Lemma 8.1, printed pp.25–26. The following checks spell out the elementary estimates in that lemma; this use concerns its complex analytic lemma, not its p-adic open question.

Reduce by the weight-two transformation law to \(|x|\le1/2\), \(|\tau|\ge1\), with \(\tau=x+iy\). Put \(r=e^{-2\pi y}<1/200\). For \(0<x<1/2\), the bounds \(\sigma_1(n)\le n^2\) and \(|\sin(n\theta)|\le n\sin\theta\) show that the first Fourier term strictly dominates the imaginary part:

\[
\left|\sum_{n\ge2}\sigma_1(n)r^n\sin(2\pi nx)\right|
\le\sin(2\pi x)\sum_{n\ge2}n^3r^n
<r\sin(2\pi x).
\]

The last inequality follows from

\[
S_3(r)=\sum_{n\ge1}n^3r^n=\frac{r(1+4r+r^2)}{(1-r)^4},
\qquad S_3(1/200)/(1/200)<2.
\]

Thus a zero has x=0 or x=±1/2. Along x=0, \(y\ge1\), and

\[
\frac d{dy}E_2^*(iy)=48\pi\sum n\sigma_1(n)e^{-2\pi ny}+\frac3{\pi y^2}>0.
\]

Along x=1/2, \(y\ge y_0=\sqrt3/2\). Since \(y^2e^{-2\pi ny}\) decreases on that ray,

\[
y^2\frac d{dy}E_2^*(1/2+iy)
\ge\frac3\pi-36\pi S_3(e^{-\pi\sqrt3})
>\frac3\pi-\frac\pi5>0.
\]

Here \(S_3(1/200)=8160200/1568239201<1/180\), and \(\pi^2<15\). Modular stabilizers force vanishing at i and at \(\rho+1\); monotonicity gives uniqueness on each ray. Reflection and translation finish the classification. Equation (3.1) proves ELL-04. The assertion refers to the scalar in §2; the coset of §1 vanishes for every CM curve, including the nonzero scalar example of §4.

## 7. Exact translation into the modern almost-holomorphic function

Spence, *Ax–Lindemann and André–Oort for a Nonholomorphic Modular Function*, JTNB 30 (2018), 743–779, defines

\[
\chi^*=\frac{1728E_2^*E_4E_6}{E_4^3-E_6^2}.
\]

Since \(j-1728=1728E_6^2/(E_4^3-E_6^2)\), direct substitution gives

\[
\chi^*=\tfrac23(j-1728)\Psi,\qquad
\boxed{h=\frac{3g_3}{2g_2(j-1728)}\chi^*.} \tag{7.1}
\]

For algebraic \(g_2,g_3\ne0\), the factor in (7.1) is a nonzero algebraic number. Hence Katz's converse is exactly the assertion that \(j(\tau),\chi^*(\tau)\in\overline{\mathbf Q}\) forces CM, with j=0,1728 treated in §6.

Spence's Proposition 5.1, p.773, proves \(\mathbf Q(\chi^*(\tau))\subseteq\mathbf Q(j(\tau))\) **at quadratic τ**. His Theorem 5.8, p.776, gives finiteness of maximal \((j,\chi^*)\)-special subvarieties. Definition 3.6, pp.755–756, defines the constant factors of those special subvarieties by quadratic τ. Substituting an arbitrary algebraic singleton into Theorem 5.8 says that it contains finitely many special subvarieties; that conclusion holds whether the singleton is special or contains none. Thus this direct use of his theorem provides no converse. This is an exact verification of the proposed application, not a claim that his methods cannot be extended.

Normalization warning: for explicit computations use Masser's original equation (100), not the abbreviated description of his ψ in Spence. The latter suppresses the factor 3/2; the field-inclusion statements are unaffected. The exceptional-case denominator printed on Spence's p.774 is β01, whereas Masser's original denominator is β03 and β01 vanishes in that case. Both original printed pages were visually checked, so this is not an OCR substitution. Use Masser's original formula for the explicit value.

## 8. The two flag fields on 18:12–13

**Proposition ELL-05 (proved).** In the rational Betti basis dual to \(\gamma_1,\gamma_2\),

\[
F^1=\mathbf C(1,\tau),\qquad
H^{0,1}=\mathbf C(1,\overline\tau).
\]

Consequently the field of definition of the filtration point is \(\mathbf Q(\tau)\); that of the ordered Hodge-bigrading point is \(\mathbf Q(\tau,\overline\tau)\). Indeed an affine chart of \(\mathbf P^1\) has coordinate the ratio of the two homogeneous coordinates, and the ordered-pair chart has the two ratios. These equalities specify the actual field, not just its transcendence degree. They refer to Betti coordinate structures; §3 uses the algebraic de Rham coordinate structure and the comparison map I displayed in §2.

Schneider's theorem, in the original paper's §1, result IIc, printed p.5, yields

\[
\operatorname{trdeg}_{\mathbf Q}\mathbf Q(\tau)=
\begin{cases}0,&E\text{ has CM},\\1,&E\text{ has no CM},\end{cases}
\]

for \(E/\overline{\mathbf Q}\). For CM, \(\tau\) is imaginary quadratic, so the bigrading field also has transcendence degree zero. For a non-CM curve the general unconditional bounds supplied here for the bigrading field are 1 and 2.

**Proposition ELL-06 (proved).** If \(E/\overline{\mathbf Q}\) is isogenous to its complex conjugate \(\overline E\), then \(\overline\tau\in\mathbf Q(\tau)\), and in the non-CM case the bigrading field has transcendence degree one. This includes curves that have no chosen real model.

**Proof.** A holomorphic isogeny \(E(\mathbf C)\to\overline E(\mathbf C)\) is induced on universal covers by multiplication by \(\lambda\ne0\) satisfying \(\lambda\Lambda\subset\overline\Lambda\). Thus for integers a,b,c,d,

\[
\lambda\omega_1=a\overline{\omega_1}+b\overline{\omega_2},\qquad
\lambda\omega_2=c\overline{\omega_1}+d\overline{\omega_2},
\quad ad-bc\ne0.
\]

Dividing gives \(\tau=(c+d\overline\tau)/(a+b\overline\tau)\), hence

\[
\overline\tau=(c-a\tau)/(b\tau-d).
\]

The denominator cannot vanish: otherwise the first equality gives \(c-a\tau=0\) as well, contradicting the nonzero determinant. Conversely such a rational fractional-linear relation, with nonzero determinant and the required upper/lower-half-plane orientation, gives commensurable lattices after scaling and therefore an analytic isogeny. It descends to Qbar: its finite kernel consists of torsion points of the algebraic curve, the quotient by that algebraic subgroup is defined over Qbar, and the resulting elliptic curve with the target j-invariant is isomorphic to the target over the algebraically closed field Qbar. QED.

There is a useful period-field refinement. An isogeny defined over Qbar has \(f^*\overline\omega=\lambda\omega\) with \(\lambda\in\overline{\mathbf Q}^{\times}\). The displayed integral matrix is invertible over Q, so \(\overline{\omega_1},\overline{\omega_2}\) belong to \(\overline{\mathbf Q}(\omega_1,\omega_2)\). Formula (3.1) proves that h then belongs to the ordinary period field \(\overline{\mathbf Q}(\omega_1,\omega_2,\eta_1,\eta_2)\). This argument proves the transfer property, including the case of isogeny to the conjugate without an actual real model.

**Unsettled here (ELL-GATE-02).** For E and \(\overline E\) nonisogenous and non-CM, prove algebraic independence of \(\tau,\overline\tau\), or produce an algebraic relation. ELL-06 excludes rational Möbius relations in that case; it does not exclude higher-degree polynomial relations. No source opened in this work supplies the latter exclusion.

### 8.1 Two exact examples covering the conjugation edge cases

**Example ELL-07 (proved and exactly checked).** Over \(\mathbf Q(i)\), let

\[
E_7:Y^2=X^3+2X^2+(\tfrac12+i)X.
\]

For \(a=2,b=1/2+i\), the standard degree-two isogeny

\[
(X,Y)\longmapsto\left(X+a+b/X,\ Y(1-b/X^2)\right)
\]

has target \(Y'^2=X'^3-4X'^2+(2-4i)X'\). Scaling the conjugate source by \((X,Y)\mapsto(u^2X,u^3Y)\), \(u^2=-2\), gives exactly that target: \(u^2\overline a=-4\), \(u^4\overline b=2-4i\). Thus \(E_7\) is isogenous to its conjugate. Its invariant and norm are

\[
j(E_7)=(-56512+38144i)/25,\qquad
N_{\mathbf Q(i)/\mathbf Q}(j(E_7))=929714176/125.
\]

The nonintegral norm proves that j is not an algebraic integer, hence the curve is non-CM. Its nonreal j proves that its complex isomorphism class has no model over R: every real model has real j, and j is invariant under complex isomorphism. Nevertheless ELL-06 proves transcendence degree one for its bigrading field. In short-Weierstrass coordinates its invariants are \(g_2=10/3-4i\), \(g_3=-28/27+8i/3\). All equation and invariant identities are verified by `check_conjugate_examples.py`.

**Example ELL-08 (proved and exactly checked).** Put

\[
j_0=1/(2+i),\quad c=j_0/(j_0-1728),\quad
E_8:y^2=4x^3-3cx-c.
\]

Direct substitution gives \(j(E_8)=j_0\). Let v be the valuation of \(\mathbf Q(i)\) at the Gaussian prime \(2+i\). Then \(v(j_0)=-1\), while \(v(\overline{j_0})=0\): modulo that prime, i=3 in F5 and \(2-i=4\ne0\). In particular E8 is non-CM and has no real model.

It is also not isogenous to its conjugate. Indeed any isogeny between complex elliptic curves can be replaced by a cyclic isogeny between the same isomorphism classes: if its kernel has type \(\mathbf Z/m\oplus\mathbf Z/n\), \(m\mid n\), it contains E[m], so factoring the map through [m] leaves a cyclic kernel of order n/m. A cyclic N-isogeny gives

\[
\Phi_N(j_0,\overline{j_0})=0.
\]

The modular polynomial has integer coefficients and is monic in either variable; these properties are proved in the opened Milne Theorem6.1, pp.82–83. Hence j0 would be integral over the valuation ring containing \(\overline{j_0}\), contradicting \(v(j_0)=-1\). This argument also covers N=1 by equality of j-invariants. It exhibits a specific curve for which ELL-GATE-02 asks for algebraic independence of τ and its conjugate.

## 9. A concrete remaining transcendence assertion

Take

\[
E_*/\mathbf Q:\quad y^2=4x^3-4x-1.
\]

It has \(g_2^3-27g_3^2=37\) and \(j=110592/37\), a nonintegral rational number; the integrality of singular moduli therefore proves non-CM. An opened proof is Milne, *Modular Functions and Modular Forms*, Theorem12.14 and Corollaries12.15–12.16, printed pp.119–120: CM implies potential good reduction at every finite place, hence integrality of j. Choose \(\omega_1>0\) real and \(\omega_2\in i\mathbf R_{>0}\), possible because the cubic has three distinct real roots. Reality of the Weierstrass series then gives \(\eta_1\in\mathbf R\), \(\eta_2\in i\mathbf R\). Equation (3.1) becomes

\[
h_* =\frac{\eta_1\omega_2+\eta_2\omega_1}{2\omega_1\omega_2}.
\]

For each \(a\in\overline{\mathbf Q}\), the following are exactly equivalent:

\[
h_*=a,
\qquad \eta_1\omega_2+\eta_2\omega_1-2a\omega_1\omega_2=0,
\qquad (\eta_1-a\omega_1)\omega_2=\pi i. \tag{9.1}
\]

The second equivalence uses (2.1), with no missing conjugation or factor two. **Unsettled here (ELL-GATE-01):** prove that none of the equalities (9.1) holds, for every algebraic a. Section 6 settles the single value a=0, and does not settle the other values.

The numerical check gives

\[
h_*=0.113219334661746861539065791000647532558647974361219962657816837416979\ldots
\]

This is an approximation and carries no algebraicity or transcendence inference.

## 10. What the classical lower bounds actually test

Chudnovsky's ICM 1978 contribution *Algebraic Independence of Values of Exponential and Elliptic Functions*, §2A, Theorem 1, printed p.343, gives transcendence degree at least two for the four periods and quasiperiods of an elliptic curve with algebraic invariants. His Theorem 3 on the same page gives algebraic independence of \(\pi/\omega\) and \(\eta/\omega\). The complete congress volume was downloaded from the official IMU archive; the cited page and the initial convention that g2,g3 are algebraic were read. This is a primary statement by the theorem's author.

A concrete algebraic compatibility check explains the remaining issue. Put \(x=\omega_1\), \(y=\omega_2\), \(u=\eta_1-a\omega_1\), \(v=\eta_2-a\omega_2\). Equation (9.1) says \(uy+vx=0\). On the open set \(xyu\ne0\), the variety

\[
v=-uy/x
\]

has function field \(\overline{\mathbf Q}(x,y,u)\), of transcendence degree three; its four coordinate functions x,y,u,v are Qbar-linearly independent, and its determinant \(uy-vx=2uy\) is nonzero. Thus the asserted quadratic relation is algebraically compatible with a lower bound of two and with absence of algebraic linear relations. This is a compatibility witness, not a tuple of genuine elliptic periods and not a counterexample to a stronger theorem.

Nesterenko, *Modular functions and transcendence questions*, Sbornik Mathematics 187 (1996), Theorem 1, p.1320, proves that at least three of q,E2(q),E4(q),E6(q) are algebraically independent for \(0<|q|<1\). His Corollary 3, p.1321, states for algebraic g2,g3 that

\[
q,\quad \omega_1/\pi,\quad \eta_1/\pi
\]

are algebraically independent. In our conventions, writing \(t=\omega_1/\pi\), algebraicity h=a gives

\[
\eta_1/\pi=a t+\frac1{t\,\pi\operatorname{Im}\tau}.
\]

Hence

\[
\overline{\mathbf Q}(q,t,\eta_1/\pi)
=\overline{\mathbf Q}(q,t,\pi\operatorname{Im}\tau).
\]

The theorem would then prove algebraic independence of the three generators on the right; it supplies no contradiction to this displayed equality. This calculation explicitly tests the proposed specialization of Nesterenko's result.

For Wüstholz and the modern de Rham–Betti statements, the parent agent is checking the full primary formulations. A purported application must address the quadratic tensor period in (9.1), rather than inserting it into a theorem whose input is a Qbar-linear relation on H1 periods. The calculations above do not claim that no further theorem can relate those settings.

## 11. Computations, reproducibility, and numerical limits

`work/code_elliptic/elliptic_splitting.py` computes three exact-input models at 80 and 160 decimal digits: (g2,g3)=(4,0), (30,28), (4,1). It computes periods from complete elliptic integrals, \(\eta_1\) both from E2 and an independent elliptic-integral identity, and \(\eta_2\) from the complementary elliptic integral, not by imposing Legendre's relation. It compares both expressions (3.1), Legendre's relation, and the g2,g3 reconstruction in (3.2). The saved output is `elliptic_splitting.out`.

For real roots \(e_1>e_2>e_3\), it uses \(d=e_1-e_3\), \(m=(e_2-e_3)/d\) and

\[
\omega_1=2K(m)/\sqrt d,\quad\omega_2=2iK(1-m)/\sqrt d,
\]

\[
\eta_1=2\sqrt d\,\mathrm E(m)-e_1\omega_1,
\quad\eta_2=-2i\sqrt d\,\mathrm E(1-m)-e_3\omega_2.
\]

The q-series truncation estimate uses \(\sigma_s(n)\le n^{s+1}\). With N terms, r=|q|, and \(R=r((N+2)/(N+1))^{s+1}<1\), its omitted tail has bound

\[
|c|\frac{(N+1)^{s+1}r^{N+1}}{1-R}.
\]

The estimate is rigorous for exact r; the implementation evaluates r and the elliptic integrals in high-precision floating arithmetic. It is not an interval certificate for all rounding error. The independently obtained residuals are around 10^{-160} in the 160-digit runs. These checks detect convention errors; they do not prove transcendence.

## 12. Opened source record and unsuccessful routes

| Source | Status and exact locator | Use or remaining limitation |
|---|---|---|
| Katz 1976, https://web.math.princeton.edu/~nmk/old/padicinterp.pdf | Opened complete PDF; §1.2, Lemma 1.3.6 and eqs.1.3.7/1.3.10 p.467; Theorem 4.0.4 p.500; Lemma 4.0.7 and Question 4.0.8 p.501 | Exact normalization, CM direction, original converse question. |
| Masser 1975, https://link.springer.com/content/pdf/bbm:978-3-540-37410-7/1 | Opened complete appendices; Appendix One, Theorem A1 p.114, Lemmas A1/A2 pp.116–118, eqs.100/105/106 pp.114/118/119, table p.121 | Exact CM value and modular-polynomial formula. Original image pages visually checked. |
| Nesterenko 1996, https://www.mathnet.ru/php/getFT.phtml?jrnid=sm&option_lang=eng&paperid=158&what=fullteng | Opened complete English primary PDF; Theorem1 p.1320, Corollaries3–4 p.1321 | Exact lower bounds; does not produce a contradiction in §10. |
| Chudnovsky, ICM1978, https://www.mathunion.org/fileadmin/ICM/Proceedings/ICM1978.1/ICM1978.1.ocr.pdf | Downloaded full official 45MB PDF, extracted and read pp.339 and343; §2A Theorems1,3 and Corollary2 | Primary author's period lower bound. Web open rejected the large PDF; local download succeeded. |
| Schneider 1937, *Arithmetische Untersuchungen elliptischer Integrale*, https://gdz.sub.uni-goettingen.de/download/pdf/PPN235181684_0113/LOG_0004.pdf | Downloaded original article through the Göttingen IIIF manifest; §1, result IIc, printed p.5, OCR and image both read | Original algebraic-J implication, following SatzII. |
| Waldschmidt, *Open Diophantine problems*, arXiv:math/0312440 | Opened; §3.3, printed p.31 | Explicitly records Katz's converse and Bertrand's nonholomorphic analogue of Schneider as a conjectural assertion; useful status evidence for 2004, not proof of present-day unresolvedness. |
| Waldschmidt, *Transcendence of periods: the state of the art*, author PDF `SurveyTrdceEllipt2006.pdf` | Opened; Theorem20,Corollary21 p.159; Theorem29 andCorollaries31–32 p.166 | Used to find original Schneider and Chudnovsky references; original Chudnovsky now opened. |
| Nesterenko–Philippon2001, Chapter1, https://link.springer.com/chapter/10.1007/3-540-44550-1_1 | Publisher metadata opened; full chapter not obtained | Waldschmidt points to §4, Conjecture4.3, attributed to Bertrand; do not cite an unseen exact text. |
| Spence2018, https://www.numdam.org/item/10.5802/jtnb.1048.pdf | Opened complete PDF; Definition3.6 pp.755–756, Proposition5.1 p.773, Proposition5.4 p.775, Theorem5.8 p.776 | The exact application to a singleton in §7 gives only finiteness, not CM. |
| Sebbar–Besrour2026, arXiv:2611.14502v1, https://arxiv.cnoctave.top/pdf/2611.14502 | Opened actual author PDF via mirror; Lemma8.1 pp.25–26, all its estimates rechecked | Zero classification. Its remaining non-CM algebraic-j question concerns p-adic zeros and must not be cited as the complex conjecture. |
| Bertolin–Waldschmidt2025, https://hrj.episciences.org/15602/pdf | Opened; Theorem2.5 restates Schneider; general conjectures for split elliptic/quasi-elliptic functions | No proof of the Hodge-splitting converse obtained. |
| Milne, *Modular Functions and Modular Forms*, https://www.jmilne.org/math/CourseNotes/MF110.pdf | Opened author's complete notes and proofs; Theorem6.1 pp.82–83; Theorem12.14 and Corollaries12.15–12.16, pp.119–120 | Integer monic modular polynomials and integrality of CM j; used for explicit non-CM and nonisogeny examples. |
| Senthil Kumar K, *Algebraic independence of values of Weierstrass elliptic and zeta functions*, Proc.Edinburgh Math.Soc.69(2026),1239–1271, DOI10.1017/S001309152610145X | Opened full publisher HTML; Theorem1 and §1 discussion | New three-logarithm lower bound remains at least2; its hypothesis excludes taking both added logarithms in the period lattice. No solution of (9.1) follows from that substitution. |

Search families included: Katz Question4.0.8 and de Rham Hodge splitting; nonholomorphic analogue of Schneider and Bertrand; algebraic E2* values; Masser Appendix1; Spence and χ* special values; τ and conjugate τ algebraic independence; modern Wüstholz, Bost–Charles and Kreutz–Shen–Vial. A Stanford UQ AI-generated answer claims the converse by transferring an algebraic de Rham line to algebraic Betti coordinates. The transfer matrix is exactly P in §2, whose entries are periods; that claimed step is not established. It is excluded as evidence.

The current exact unresolved assertions are ELL-GATE-01 and ELL-GATE-02. The CM direction, exact normalizations, CM example, zero exclusion, isogenous-to-conjugate case, and the tested theorem specializations are proved above. No proof of the full non-CM converse is being claimed.

## 13. Additional exact consequences written into the paper

**ELL-09 / paper A.4.3 (proved from Chudnovsky).** In the CM case,

\[
L=\overline{\mathbf Q}(\omega_1,\omega_2,\eta_1,\eta_2)
=\overline{\mathbf Q}(\omega_1,\pi/\omega_1)
=\overline{\mathbf Q}(\omega_1,\pi),\qquad
\operatorname{trdeg}_{\overline{\mathbf Q}}L=2.
\]

Indeed τ and Im τ are algebraic and h is algebraic. Formula (3.1) expresses η1 as hω1+π/(ω1 Imτ), while ω2=τω1 and η2=τη1−2πi/ω1. This proves the inclusion into the displayed two-generator field; Legendre proves the reverse inclusion. Chudnovsky ICM1978 §2A Theorem1 p343 supplies the lower bound two, so it is equality. The normalized lattices of E and its conjugate span the same imaginary quadratic field, hence they are commensurable after scaling. Their analytic isogeny descends to Qbar by the algebraic torsion-kernel argument. Pullback of de Rham classes and the homology isogeny matrix then express every conjugate period and quasiperiod as a Qbar-linear combination of the original ones. Thus adjoining the conjugate period matrix leaves L unchanged. In the absolute-Hodge category generated by abelian varieties, the CM action confines the group to Res_{K/Q}G_m; the Hodge cocharacter and its Galois conjugate are its two coordinate cocharacters, so the group has dimension two.

**ELL-10 / paper A.4.7 (proved).** For an algebraic degree-n isogeny f:E→E′, write f*ω′=λω and f*ξ′=aω+bξ. Then λ,a,b are algebraic, λb=n by the cup-product pairing, and

\[
h_{E'}=\frac{n}{\lambda^2}h_E-\frac a\lambda.
\]

This follows directly from f*(ξ′+hE′ω′)=b(ξ+hEω). Hence algebraicity of the splitting is constant on an algebraic isogeny class. This formula does not allow setting the short-Weierstrass scalar to zero by an arbitrary change of basis while retaining the same short-Weierstrass equation; section 6's zero classification uses that specified basis.

The complete TeX draft is `output/RESEARCH_SA07/sections/A_elliptic.tex`; its source entries are in `work/elliptic_references.bib`. Programs and saved outputs have also been copied into `output/RESEARCH_SA07/code/`. The bibliography verifies Masser's DOI as 10.1007/BFb0069432 and records the full Sebbar–Besrour title, *Zeros of Katz's p-adic Eisenstein series E2: Hypergeometric congruences and isogenies*.
