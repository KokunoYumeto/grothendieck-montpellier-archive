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

## 14. Exact translations to modern single-valued periods and mock modular forms

**ELL-11 (proved translation).** In the notation of Alfes–Griffin–Ono–Rolen, *Weierstrass mock modular forms and elliptic curves*, Research in Number Theory 1, article24 (2015), equations (1.5)–(1.6), printed preprint p.3, the regularized lattice sum S(Λ) is exactly our h, with the short-Weierstrass differential ω=dz and ξ=℘(z)dz. This is an equality, not just equality up to an algebraic factor. Their equation (2.2), p.9, says that

\[
\zeta_\Lambda(z)-S(\Lambda)z-\frac{\pi}{A}\overline z
\]

is Λ-periodic. Taking its increment at ω_i gives η_i−S(Λ)ω_i−(π/A)barω_i=0. The linear system for h in §3 is η_i−hω_i−(π/A)barω_i=0, so subtraction, with ω_i≠0, proves S(Λ)=h. Their Remark6, p.5, explicitly treats non-CM S(Λ) as expected transcendental. This is additional primary status evidence as of2015, not a proof of a present-day impossibility theorem.

For an optimal modular elliptic curve over Q in their period normalization, put

\[
F_E(q)=\sum_{n\ge1}a_nq^n,\quad a_1=1,\qquad
\mathcal E_E(q)=\sum_{n\ge1}(a_n/n)q^n,
\quad
\widehat{\mathfrak Z}_E^+(q)
=\zeta_\Lambda(\mathcal E_E(q))-h\mathcal E_E(q).
\]

All Laurent coefficients of ζΛ at0 are rational polynomials in g2,g3, apart from its initial term1/z, and the chosen algebraic differential gives g2,g3∈Q. Thus every coefficient of ζΛ(\mathcal E_E(q)) is rational. Since the ζ expansion has no linear term in z,

\[
[q]\widehat{\mathfrak Z}_E^+
=\frac{a_2^2}{4}-\frac{a_3}{3}-h.
\tag{14.1}
\]

Consequently algebraicity of h is equivalent to algebraicity of this one coefficient and to algebraicity of all coefficients of this weight-zero mock modular form. This gives a precise application target for coefficient theorems; it does not establish the non-CM converse. For the 37a1 model y²+y=x³−x, the substitution Y=2y+1 gives Y²=4x³−4x+1 and (a2,a3)=(-2,-3), so (14.1) is2−h. The algebraic isomorphism overQ(i) with the model of §9 changes h to−h, explaining the independently computed positive coefficient2.113219… in their example, printed p.29.

**ELL-12 (proved comparison with Fonseca2020).** Suppose the elliptic curve and an adapted de Rham basis (ω,ξ) are defined over a real algebraic field. Write the integration matrix with cycles as rows,

\[
P_c=\begin{pmatrix}\omega_1&-\eta_1\\\omega_2&-\eta_2\end{pmatrix},\qquad
S=P_c^{-1}\overline{P_c}=(s_{ij}).
\]

The first column represents the Betti-conjugate holomorphic class: its period vector is (barω1,barω2), so the proof of §3 gives s21=−A/π≠0 and h=s11/s21. This is also the single-valued involution of Fonseca, *On coefficients of Poincaré series and single-valued periods of modular forms*, Research in the Mathematical Sciences7, article33 (2020), equation(0.4) and Example0.1 p.4. His Theorem0.4 p.6, proved as Proposition8.1 pp.28–29, gives, for a symplectic rational basis ([f],[g]) in the case dimS_{k+2}(Γ0(N))=1,

\[
a_n(P_{-m,k+2,N})
=\frac{k!}{m^{k+1}}a_m(f)a_n(f)\frac{s_{11}}{s_{21}}+r_{m,n},
\qquad r_{m,n}\in\mathbf Q.
\tag{14.2}
\]

For k=0 and f normalized, m=n=1, this is an exact one-coefficient formulation of the algebraicity of the Hodge splitting in that basis. In the X0(11) example, Fonseca uses ξ_gen=xω=(℘+1/3)dz, so the basis-change formula gives h_short=h_gen+1/3; Example0.3 pp.5–6 has a1(P_{−1,2,11})=h_gen−1. This checks both sign and translation against (14.1).

**ELL-13 (failed theorem application resolved by a primary corrigendum).** The original 2008 version of Bruinier–Ono–Rhoades, *Differential operators for harmonic weak Maass forms and the vanishing of Hecke eigenvalues*, Theorem1.4, printed journal p.677, is unsafe to use as printed. The authors' one-page corrigendum (Math.Ann.345(2009),31), opened in full at https://uva.theopenscholar.com/files/ken-ono/files/124.pdf, replaces it: if p∤N and a_p(g)=0, a good harmonic Maass preimage has algebraic holomorphic coefficients at n with ord_p(n) odd. The corrected arXiv0802.0963v3 (26Jan2009), printed p.4, contains this replacement. The unrestricted claim about all coefficients must not be used.

The corrected statement supplies no contradiction to h algebraicity or transcendence in (14.2). In weight2 the Hecke recurrence

\[
a_{p^r}=a_p a_{p^{r-1}}-p\,a_{p^{r-2}}
\]

and a_p=0 give a_{p^{2r+1}}=0 by induction; multiplicativity then gives a_n=0 whenever ord_p(n) is odd. At every such n, the coefficient of h in (14.2) vanishes. The test n=1, which actually detects h, has ord_p(1)=0 and is not covered by the corrected theorem. This is an exact failure of this proposed specialization, not a blanket claim that harmonic Maass methods can never settle the question.

**ELL-14 (2025 source normalization checked).** Brown–Fonseca, arXiv2508.04844v2 (18Aug2025), Lemma6.3, equations(6.8)–(6.9), printed p.34, use S=barP_c^{-1}P_c and ρ=S11/S21. The matrix is the inverse of the convention in the preceding paragraph. Their displayed Betti-conjugate class is ξ+barρ ω, so our scalar is h=barρ. The bar was checked in the original rendered page. Lemma6.4, p.35, proves algebraicity in the CM case. Proposition7.3, p.38, expresses the meromorphic modular forms Ψ^{m,n} in powers of ρ plus a cusp-form term; Proposition7.5, p.39, specializes at a CM point. These exact formulas do not prove the converse required in ELL-GATE-01. The later Gross–Zagier extension in Theorem8.14, p.47, explicitly takes both marked points CM; substituting a non-CM point does not meet that hypothesis. No unproved general motivic assertion from their §9 is used here.

All four primary documents have been retained under `work/sources_elliptic/`; the 2008 PDF and 2009 corrected version have distinct filenames so that the obsolete statement cannot silently enter the proof chain.

## 15. The exact tensor and the exact generated-torsor test

**ELL-15 (proved projector comparison).** Let e be the projector onto H01 along H10. In the adapted de Rham basis of §2 its matrix is

\[
e_{\mathrm{dR}}=\begin{pmatrix}0&h\\0&1\end{pmatrix}.
\]

In Betti coordinates with H10=C(1,τ) and H01=C(1,barτ), its matrix is

\[
e_B=\frac1{\overline\tau-\tau}
\begin{pmatrix}-\tau&1\\-\tau\overline\tau&\overline\tau\end{pmatrix}.
\tag{15.1}
\]

Indeed, conjugate diag(0,1) by the matrix whose columns are (1,τ) and (1,barτ). Conversely, τ=−(e_B)11/(e_B)12 and barτ=(e_B)22/(e_B)12. Thus

\[
\overline{\mathbf Q}(\text{entries of }e_B)
=\overline{\mathbf Q}(\tau,\overline\tau).
\tag{15.2}
\]

Schneider's theorem consequently proves that e_B has algebraic entries exactly in the CM case. Algebraicity of h makes e_dR algebraic; it does not verify the second coefficient-field requirement in the definition of a Qbar-de Rham–Betti tensor. This calculation identifies exactly what would have to be proved to use the Hodge projector as such a tensor. No assertion that no other tensor construction could work is made.

There is another precise tensor formulation. For a real model choose cycles for which complex conjugation on Betti cohomology is F=diag(1,−1). Write P_c=[[x,p],[y,q]], with columns the periods of ω and ξ, and put D=det(P_c). Then

\[
S=P_c^{-1}FP_c
=D^{-1}\begin{pmatrix}xq+yp&2pq\\-2xy&-xq-yp\end{pmatrix}.
\]

The rational Betti vector F belongs to End(H_B), and S is its inverse comparison image in End(H_dR). Since traceF=0, this tensor lies in End⁰(H)≅Sym²(H)(1), a rank-three weight-zero tensor construction. For the algebraic functional ℓ_a(T)=T11−aT21 one has

\[
\ell_a(S)=\frac{xq+yp+2axy}{D},\qquad
h=a\ \Longleftrightarrow\ \ell_a(S)=0.
\tag{15.3}
\]

The vanishing of this one coordinate is the exact period relation. It says that the inverse comparison image of the rational vector F lies in the algebraic de Rham plane kerℓ_a. To be a de Rham–Betti class the full vector S, and not just this one coordinate, would have to have algebraic coordinates. Formula (15.3) does not verify that requirement. The equality End⁰(H)≅Sym²(H)(1) follows from H∨≅H(1) supplied by the polarization and the decomposition H⊗H=Sym²H⊕∧²H, with ∧²H(1)=Q(0).

**ELL-16 (proved, exact compatibility with generated torsor).** For a∈Qbar set

\[
V_a=\left\{\begin{pmatrix}x&p\\y&q\end{pmatrix}\in\mathrm{GL}_2:
xq+yp+2axy=0\right\}.
\]

This is a three-dimensional irreducible algebraic variety, and the smallest algebraic subtorsor of GL2 containing V_a is all of GL2. Here is a complete group-generation proof. The algebraic change of de Rham basis B_a=[[1,a],[0,1]] gives V_a B_a=V_0. Let

\[
H=\begin{pmatrix}1&1\\1&-1\end{pmatrix},\qquad
T=\{\operatorname{diag}(r,s):rs\ne0\}.
\]

Every point of V0 has x,y,p≠0, q=−yp/x, and therefore the unique three-parameter representation

\[
\begin{pmatrix}x&p\\y&-yp/x\end{pmatrix}
=\operatorname{diag}(x,y)H\operatorname{diag}(1,p/x).
\tag{15.4}
\]

Its determinant is−2yp, so V0 is isomorphic to(G_m)³. After choosing the algebraic basepoint H, the set H^{-1}V0 contains both T and H^{-1}TH: take x=y for the former, and p=x for the latter. The Lie algebra of the generated closed subgroup consequently contains I, Z=diag(1,−1),

\[
X=H^{-1}ZH=\begin{pmatrix}0&1\\1&0\end{pmatrix},
\qquad[Z,X]=\begin{pmatrix}0&2\\-2&0\end{pmatrix}.
\]

These four matrices form a basis of gl2. The generated closed subgroup has dimension4, and a closed dimension4 subgroup of the connected dimension4 group GL2 is GL2. Right translation by B_a and the corresponding conjugation after changing basepoint prove the same assertion for Va.

Kreutz–Shen–Vial, arXiv2206.08618v3 (21Jan2026), Proposition3.1 p.8 and Theorem5.13(ii) pp.20–22, have now been opened directly. For one non-CM elliptic curve and Betti coefficient field L=Qbar, they imply that the period point generates the full GL2 comparison torsor, as translated in the generation agent's GEN-1. Equations (15.3)–(15.4) prove that the actual proposed algebraic-h equation defines a proper three-dimensional locus which nevertheless generates that full torsor. Thus inclusion of the period locus in Va does not contradict the cited generated-torsor conclusion. This is a test of the exact equation in the problem; Va is not asserted to be the period locus of an actual elliptic curve.

The identities, the Lie-algebra rank, the projector, and the fixed-determinant parametrization were checked symbolically in `work/code_elliptic/check_torsor_gate.py`; all exact assertions passed. This is an algebraic verification and supplies no transcendence conclusion by itself.

## 16. The Bakker–Tsimerman family specialization, with dimensions checked

The full 2025 primary article has been opened both in publisher HTML and as the publisher PDF: *Functional Transcendence of Periods and the Geometric André–Grothendieck Period Conjecture*, Forum of Mathematics, Sigma13,e97, DOI10.1017/fms.2025.10036. Theorem1.3 is on p.5; Corollary2.9 on p.8; Theorem4.25 on p.18. The following computes their hypotheses in a family containing every real three-root elliptic model after an algebraic scaling and root translation.

Use the Legendre family

\[
E_t:Y^2=4X(X-1)(X-t),\quad
t\in S=\mathbf A^1\setminus\{0,1\},\qquad
x=X-(1+t)/3.
\]

In short-Weierstrass form it has

\[
g_2(t)=\frac43(t^2-t+1),\qquad
g_3(t)=\frac4{27}(2-3t-3t^2+2t^3).
\]

Take ω=dx/Y and ξ=x dx/Y. For t in(0,1), all three roots are real. Choose the period cycles continuously on a complex neighborhood of a real t0 so that on the real interval the first row of P(t) is real and the second is purely imaginary; hence F=diag(1,−1) and the same polynomial R_a=xq+yp+2axy in matrix coordinates detects h(t)=a.

The Legendre monodromy contains nontrivial upper and lower unipotents with off-diagonal entries±2. For completeness, the periods can be written in terms of K(t) and iK(1−t). The logarithmic term of K(1−t) at0 is −K(t)log(t)/π, as follows from its Picard–Fuchs equation and K(1−t)~(1/2)log(16/t); a loop around0 adds twice the first period to the second. The analogous calculation at1 gives the other unipotent. Their Zariski closures contain the two one-parameter unipotent subgroups, whose Lie algebras and bracket span sl2. The algebraic monodromy is therefore SL2 and has dimension3.

In the algebraic de Rham frame (ω,ξ), the full period torsor Ω has dimension1+3=4; its fibers are detP=D=2πi. These are complex algebraic varieties, so the nonzero constant D is an allowed coefficient. The hypersurface W_a in Ω defined by R_a=0 has dimension3. In fact, its fiber has the explicit two-parameter description

\[
P=\begin{pmatrix}
x&-D/(2y)-ax\\
y&D/(2x)-ay
\end{pmatrix},\qquad x,y\ne0.
\tag{16.1}
\]

Let Σ be the one-dimensional horizontal period leaf. The holomorphic function R_a(P(t)) cannot vanish identically on any open disc: continuation around loops would put the full monodromy orbit of P(t0) in the proper hypersurface R_a=0, and Zariski density would then put its entire three-dimensional determinant fiber in the two-dimensional fiber (16.1), a contradiction. Thus any given solution at t0 is an isolated intersection component U of W_a∩Σ. Its codimension is

\[
\operatorname{codim}_{W_a}U=3=\dim\mathrm{SL}_2.
\]

Theorem1.3 requires the strict inequality codim_W U<dimG, so this isolated solution does not meet its hypothesis. If instead one adds the equation t=t0 to W_a, the resulting variety has dimension2, and the strict inequality holds. The conclusion then places {t0} in a proper weak Mumford–Tate subvariety. By Corollary2.9 this conclusion holds for every point of this family, since restriction to a point has trivial monodromy, strictly smaller than SL2. It gives no CM conclusion for t0.

For Theorem4.25, a constant elliptic curve spread over C(t) has trivial relative monodromy and hence trivial relative motivic group; all its period functions are constants already in C. Its asserted lower bound is0 in that specialization. A nonconstant family has the monodromy just computed, but the single equality h(t0)=a does not become an identity of meromorphic functions. These computations specify what the family theorem actually proves in this attempted application. They make no claim that no additional arithmetic argument could be combined with it.

## 17. The canonical unitary lift and its exact arithmetic hypothesis

**ELL-17 (proved, with a primary arithmetic theorem).** Write c=π/A. The universal vector extension has the analytic uniformization

\[
E^\dagger(\mathbf C)=\mathbf C^2/\Lambda^\dagger,
\qquad\Lambda^\dagger=\mathbf Z(\omega_1,\eta_1)+\mathbf Z(\omega_2,\eta_2).
\tag{17.1}
\]

On the algebraic chart above E minus the origin, use coordinates (x,y,t). The uniformization and algebraic invariant differentials are

\[
(u,s)\longmapsto(\wp(u),\wp'(u),\zeta(u)-s),
\quad du=dx/y,\quad ds=-dt-x\,dx/y.
\tag{17.2}
\]

These exact signs are in Fonseca–Matthes2020, §4.1–4.2, equation(4.1) and Proposition4.2, pp.7–8. Their symbol η(λ) is the integral of xdx/y, hence the negative of our quasiperiod; the lattice in (17.1) consequently has the displayed positive quasiperiods.

The maximal compact subgroup is the real span of Λ† modulo Λ†. By η_i=hω_i+c barω_i, this real plane is exactly

\[
W=\{(u,hu+c\overline u):u\in\mathbf C\}.
\]

Indeed, the right-hand formula is real-linear and sends the real basis ω1,ω2 to the two lattice generators. The quotient W/Λ† is compact. The quotient C²/W is a real vector group, so every compact subgroup of C²/Λ† maps trivially to it and is contained in W/Λ†. This proves maximality directly. Projection to E(C) restricts to an isomorphism of real Lie groups, with canonical section κ. Its coordinate above a nonzero point P=(℘(u),℘′(u)) is

\[
t(\kappa(P))=\zeta(u)-hu-c\overline u.
\tag{17.3}
\]

The expression is independent of the chosen logarithm u, because its increment under ω_i is η_i−hω_i−c barω_i=0.

Bost–Künnemann, *Astérisque*327(2009), Theorem3.1.2, printed p.386, proves that an algebraic point in a universal vector extension whose image at **one** complex embedding is in its maximal compact subgroup is torsion. The equivalent unitary-connection statement is Theorem3.1.1 on the same page; the analytic identification of the compact section with the unitary connection is AppendixB.7, equations(B.17)–(B.20), pp.421–422. Therefore, for every nonzero P∈E(Qbar),

\[
\zeta(u)-hu-c\overline u\in\overline{\mathbf Q}
\quad\Longleftrightarrow\quad P\text{ is torsion}.
\tag{17.4}
\]

For the reverse implication, the map E†[n]→E[n] is an isomorphism: multiplication by n is invertible on the additive kernel, so each n-torsion point has one n-torsion lift. This lift is algebraic and lies in W/Λ†, hence is κ(P). For the forward implication, (17.2) makes κ(P) algebraic, so the cited theorem makes it torsion and its projection P torsion.

The exact infinitesimal datum measured by h is also now explicit. The complex-linear part of dκ at the origin has image

\[
L_h=\{(u,s):s=hu\}\subset\operatorname{Lie}E^\dagger.
\tag{17.5}
\]

Since du and ds are algebraic invariant differentials, L_h is defined over Qbar exactly when h is algebraic. It annihilates ds−hdu, whose de Rham class is −(ξ+hω), so this is the exact Lie-algebra realization of the Hodge-splitting line. Its exponential intersects the maximal compact subgroup only at the identity: if (u,hu) belongs to W, then c bar u=0, hence u=0; adding a lattice vector does not change membership in W. Algebraicity of h is thus an infinitesimal condition in (17.5), while the hypothesis of the arithmetic theorem at an algebraic point P is exactly algebraicity of the full quantity (17.3). No implication from the former to the latter has been proved here.

A potentially misleading search lead has also been checked. Künnemann's 2003 Barcelona seminar abstract says that nontriviality of the arithmetic Hodge extension over Qbar is discussed. Bost–Künnemann's January2007 PartI preprint, §0.2 pp.5–6, constructs the Hodge extension and calls nonvanishing an issue related to deep transcendence problems; it gives no converse resolving (ELL-GATE-01). Künnemann's Oberwolfach Report1/2005 contribution, p.56, gives a Faltings-height bound involving the size of the Hodge extension, with no such converse. These documents were opened rather than treating the seminar abstract as a theorem.

## 18. Exact p-th-power test on the same algebraic line

**ELL-18 (proved).** For every elliptic curve E/Qbar and every a∈Qbar, the nonvertical line L_a={s=au} in Lie(E†) is not the Lie algebra of an algebraic subgroup. Consequently its reductions fail to be closed under p-th powers at infinitely many good primes of any number field of definition.

For the first assertion, a connected one-dimensional algebraic subgroup with nonzero projection to E would map surjectively to E and have finite kernel in Ga. In characteristic zero that kernel is trivial. It would therefore split E†→E. Such a splitting is impossible even analytically: its lift to universal covers would be u↦(u,bu), and it would require bω_i=η_i for both i, contrary to η1ω2−η2ω1=2πi. The other possibility is the vertical additive subgroup, whose Lie algebra is not L_a. This proves the assertion without a classification theorem about CM.

Bost, *Publications mathématiques de l'IHÉS*93(2001), Theorem2.3, printed p.172, proves that a Lie subalgebra of an algebraic group over a number field is the Lie algebra of an algebraic subgroup if and only if its reductions are closed under p-th powers at all but finitely many primes. Applying its contrapositive to L_a gives the infinite-prime assertion. This is a proved statement about every algebraic complement line, including the lines in the explicit CM examples; it is not a claim that all p-adic approaches to the splitting question fail.

There is a direct, checkable reduction calculation. In the algebraic chart (17.2), let

\[
D_a=y\partial_x+(6x^2-g_2/2)\partial_y-(x+a)\partial_t,
\qquad V=-\partial_t.
\tag{18.1}
\]

Then du(D_a)=1 and ds(D_a)=a, so D_a generates L_a. In characteristic5, repeated differentiation in the coordinate ring y²=4x³−g2x−g3 gives

\[
D_a^5=2g_2D_a+(3g_3-2g_2a)V.
\tag{18.2}
\]

It suffices to check x,y,t, since both sides are derivations. Their values on x are 2g2y; on y they are 2g2x²+4g2²; on t they are 3g2x+2g3. Thus the line is p-closed at this prime precisely when 3g3−2g2a=0.

For the actual CM curve y²=4x³−30x−28, with h=1/2 and discriminant5832, reduction at5 is good. Formula(18.2) gives

\[
D_h^5=4V\ne0,
\]

which is not in the line generated by D_h because du(D_h)=1 and du(V)=0. Hence even CM algebraicity of h does not imply p-integrability of this particular line at every good prime. The infinite-prime failure for this same line follows from the preceding theorem.

The exact identities were verified in `work/code_elliptic/check_p_curvature.py`, with output retained. An independent finite-field computation for p=5,7,11,13,17,19,23,29,31,41 also computes D_E^(p−1)x=H_p x+C_p and checks H_p against the Hasse coefficient of x^(p−1) in (4x³−g2x−g3)^((p−1)/2). For the CM model the defect C_p−H_p/2 vanishes at the tested split primes11,17,19,41 and is nonzero at the tested inert primes. Those finite tests are not used to prove a general density statement.

The recent primary preprint F. Bianchini, *On the Ramanujan Vector Field modulo p*, arXiv2602.20109v1(23Feb2026), was also opened. Its Theorem1, pp.2–3, computes the p-th power of the Ramanujan vector field on the three-dimensional moduli of de Rham bases; Theorem2 describes its supersingular locus. The computation (18.1) is on the fixed universal vector extension and is derived directly here, without identifying those two vector fields. A possible further application would require an explicit morphism between these spaces and its effect on the relevant foliations.

## 19. Torsion evaluations and the attempted algebraic compact point

**ELL-19 (proved exact addition and multiplication identities).** Put Z(P)=ζ(u)−hu−c bar u for P=[u]≠O. For points with distinct x-coordinates and P+Q≠O, the zeta addition formula gives

\[
Z(P+Q)=Z(P)+Z(Q)+\frac{y(P)-y(Q)}{2(x(P)-x(Q))}.
\tag{19.1}
\]

The h and c terms cancel because they are real-linear in the elliptic logarithm. Duplication gives

\[
Z(2P)=2Z(P)+\frac{12x(P)^2-g_2}{4y(P)}.
\tag{19.2}
\]

Both equations are identities on the open chart and extend wherever their meromorphic sides are defined. More generally, R_m(P)=ζ(mu)−mζ(u) is an elliptic function with rational expression over Q(g2,g3), obtained recursively from (19.1) and duplication. It satisfies

\[
Z(mP)=m Z(P)+R_m(P).
\tag{19.3}
\]

For P of exact order n≥2, (n−1)P=−P and Z is odd, so

\[
Z(P)=-\frac1nR_{n-1}(P).
\tag{19.4}
\]

In particular Z(P)=0 for nonzero two-torsion, and

\[
Z(P)=-\frac{12x(P)^2-g_2}{12y(P)}
\]

for nonzero three-torsion. These algebraic torsion values and their recurrences do not require algebraicity of h. Algebraic group addition, inverse, multiplication, and taking division points, starting from torsion points, produce only torsion points: every finite sum has a common annihilating integer, and nQ=P with mP=0 gives mnQ=0. Thus this specified set of torsion operations supplies no non-torsion point at which to apply (17.4). This is an exact closure argument, not an assertion about every possible use of torsion values.

There is a fully algebraic non-CM example. On E*:y²=4x³−4x−1, let r be the unique real root in (1,2) of

\[
3r^4-6r^2-3r-1=0,
\]

and let s=√(4r³−4r−1)>0. Then P=(r,s) has exact order three. Indeed, with m=(3r²−1)/s, the displayed polynomial gives m²=3r, and duplication gives x(2P)=m²−2r=r and y(2P)=−s. Its canonical compact lift has the algebraic coordinates

\[
\kappa(P)=\left(r,s,-\frac{3r^2-1}{3s}\right).
\tag{19.5}
\]

The last coordinate t satisfies x=3t² and

\[
243t^8-54t^4-9t^2-1=0.
\]

The resultant of 4x³−4x−1 and 3x⁴−6x²−3x−1 is−1369, so y≠0 at every point used. Numerically (r,s,t)≈(1.651571265505797,3.227010548681081,−0.7419728803457704). The curve is non-CM because its j=110592/37 is not an algebraic integer. This provides a nontrivial algebraic point in the maximal compact subgroup without any CM conclusion; the point is torsion, exactly as the arithmetic theorem requires.

**ELL-20 (proved exact test of the horizontal lift).** For every a∈Qbar,

\[
\exp(L_a)\cap E^\dagger(\overline{\mathbf Q})=\{O\}.
\tag{19.6}
\]

To prove this, use the original German primary preprint of Wüstholz, MPIM84-7, Hauptsatz and Bemerkung2, printed p.3 (PDFp.4), now opened, OCR-read, and visually checked. Its analytic subgroup theorem says that a Qbar-defined analytic homomorphism with a nonidentity algebraic point in its image contains a positive-dimensional algebraic subgroup in that image. Apply it to the analytic homomorphism Ga(C)→E†(C), u↦exp(u,au). Its differential is defined over Qbar by (17.2). A positive-dimensional algebraic subgroup in this one-dimensional image would have Lie algebra L_a, excluded by ELL-18. This proves (19.6).

For a nonzero algebraic point P=[u], the horizontal lift has coordinates (x(P),y(P),ζ(u)−au), hence

\[
\zeta(u)-au\notin\overline{\mathbf Q}
\quad(a\in\overline{\mathbf Q}).
\tag{19.7}
\]

This explicitly checks the alternative construction from the algebraic tangent line. For a CM example with a=h, the algebraic torsion lift (19.4) and the horizontal lift differ by the additive fiber coordinate c bar u; the latter is transcendental by (19.7). The exact correction needed to reach the compact section has therefore not become algebraic merely because its holomorphic tangent coefficient is algebraic. No conclusion about a non-CM value of h is inferred from this calculation.

The exact three-torsion example is checked in `work/code_elliptic/check_torsion_lifts.py`, whose output is retained and copied into the deliverable code directory. The original primary Wüstholz scan is retained separately from the modern English translation, so the theorem does not depend on that translation.

## 20. De Rham-only Hodge endomorphisms and the exact arithmetic hypotheses

**ELL-21 / A.4.18 (proved).** Let D_E be the Qbar-algebra of Qbar-linear de Rham endomorphisms preserving both Hodge lines at the specified complex embedding. In the basis (ω,ξ), preservation of Cω gives T=[[a,b],[0,d]], with a,b,d algebraic. Preservation of C(hω+ξ) gives ah+b=dh. Hence

\[
 D_E=\{aI+(d-a)e_h:a,d\in\overline{\mathbf Q},\ (d-a)h\in\overline{\mathbf Q}\},
 \qquad e_h=\begin{pmatrix}0&h\\0&1\end{pmatrix}.
\]

This algebra is Qbar×Qbar when h is algebraic and Qbar I otherwise. The pullback injection End(E)⊗Z Qbar→D_E has exactly the image of those T whose Betti matrices have algebraic entries. The forward inclusion follows because an actual endomorphism has integral Betti action. For the reverse inclusion, a nonscalar T has T_B=aI+(d−a)e_B, with a,d algebraic and d−a≠0. Thus T_B algebraic implies e_B algebraic. A.4.11 recovers τ and conjugateτ from e_B, and Schneider gives CM. In CM, End(E)⊗Qbar has dimension two and acts diagonally with distinct eigencharacters on the two Hodge lines, hence fills D_E. A scalar T is always in the image. For non-CM E the image is Qbar I; the cokernel is one-dimensional exactly when h is algebraic. This computes precisely the surjectivity assertion that would settle the remaining gate, without asserting that surjectivity is known.

Moreover e_B is never rational over Q: its (1,2) entry is i/(2 Imτ), nonzero and purely imaginary. This includes CM. Bost–Charles, complete primary preprint arXiv1307.1045v2, Theorem3.8(1), equation(3.11), p17, establishes full faithfulness with an integral Betti lattice. Deligne's MainTheorem2.11 in the opened revised author edition of the 1982 article, p19, assumes a rational Betti Hodge class; the general tensor definition on pp15–16 explicitly retains this rationality. The computed nonreal entry proves that the single projector fails this hypothesis. In CM it is an algebraic-coefficient combination of actual endomorphisms, which is different from a rational-coefficient endomorphism by the displayed matrix, not merely terminology.

**ELL-22 / A.4.19 (proved).** For an elliptic curve and a rank-one de Rham projector e over a number field L, its crystalline-Frobenius fixity lower weighted density, using Tang's Definition2.3.1 p7,

\[
 \underline\delta(e)=\liminf_{X\to\infty}
 \frac{\sum_{v:p_v\le X,\ \varphi_v(e)=e}[L_v:\mathbf Q_{p_v}]\log p_v/(p_v-1)}
 {[L:\mathbf Q]\sum_{p\le X}\log p/(p-1)},
\]

is at most3/4. Tang arXiv1510.01357v3, Theorem2.3.3 p7, identifies 1-absolute-Tate endomorphisms with the image of End_L(E)⊗Q; Corollary5.2.3 p23 gives algebraicity with rational coefficients already at density greater than3/4 for geometrically simple A. An elliptic curve is geometrically simple, and its rational endomorphism algebra has no nontrivial idempotent: every nonzero endomorphism is an isogeny, so becomes invertible after tensoring with Q. A rank-one projector is a nontrivial idempotent, proving the assertion. The coefficient algebra here is End(E)⊗Q, explicitly not End(E)⊗Qbar. The latter does have idempotents in CM.

At an unramified good place write crystalline Frobenius as F_v σ_v with F_v=[[A,B],[C,D]] and σ_v acting on the coefficients. Direct multiplication gives

\[
 F_v\sigma_v(e_h)-e_hF_v
 =\begin{pmatrix}-hC&A\sigma_v(h)+B-hD\\-C&C\sigma_v(h)\end{pmatrix}.
\]

Thus fixity is exactly C=0 and Aσ_v(h)+B=hD. In particular it includes preservation of the Hodge line itself, a requirement not supplied by the coefficient h.

For the actual Q-defined CM curve y²=4x³−30x−28, h=1/2, the good reduction at5 has equation y²=4x³+2. The numbers of y-solutions at x=0,1,2,3,4 are0,2,2,1,0, giving six points including O. The crystalline Frobenius over Q5 has trace0, determinant5 and polynomial T²+5. It is irreducible over Q5 because v5(−5)=1, so no Q5-line is invariant. The Q-defined rank-one projector e_(1/2) therefore fails Frobenius fixity. This argument uses the base field Q and linear Frobenius over Q5. It does not replace semilinear Frobenius after passage to a CM field by a linear map.

For u²=−2 the actual endomorphism matrix is α_dR=u[[1,−1],[0,−1]], and e_(1/2)=(α_dR−uI)/(−2u). These coefficients exhibit explicitly how the algebraic-coefficient projector arises from a rational endomorphism algebra after scalar extension. The exact checks are in `work/code_elliptic/check_endomorphism_projector.py`; source and output were copied to the deliverable code directory. None of these results proves the non-CM converse for h.

### Primary-source and search record for this continuation

- Bost–Charles: https://arxiv.org/pdf/1307.1045 opened complete, downloaded and text-extracted. Theorem3.8(1) p17 and Definition5.1 p25 read. Publisher metadata at DOI10.1515/crelle-2014-0025 independently opened: J.reineangew.Math.714(2016)175–208.
- Deligne: https://www.jmilne.org/math/Documents/Deligne82.pdf opened through web retrieval, including definitions pp15–16 and MainTheorem2.11 p19; the cover states that this is Milne's revised author TeX version, dated1October2018, of the1982 article. Direct local download returned406, so no local copy is claimed. Definition2.1 is not an appropriate locator: the displayed2.1 is an example; the cited definitions occur immediately before it and in the general tensor paragraph p16.
- Tang: https://arxiv.org/pdf/1510.01357 opened complete, downloaded and text-extracted; version3,5October2017. Definition2.1.1 p4, Definition2.3.1/Theorem2.3.3 p7, Corollary5.2.3 p23 read. Publisher record https://www.cambridge.org/core/journals/compositio-mathematica/article/abs/cycles-in-the-de-rham-cohomology-of-abelian-varieties-over-number-fields/EBE4850629696746B61FCF8FC3D97E96 independently opened; final publication CompositioMath.154(2018),850–882, DOI10.1112/S0010437X17007679. Page locators here refer to the opened preprint.
- Wüstholz final1989 original: publisher https://annals.math.princeton.edu/1989/129-3/p03 opened, confirming AnnMath129(1989)501–517, DOI10.2307/1971515. The direct JSTOR PDF URL https://www.jstor.org/stable/pdf/1971515.pdf returned HTTP200 challenge HTML (3038bytes), not a PDF. The attempted publisher URL https://annals.math.princeton.edu/wp-content/uploads/annals-v129-n3-p03.pdf returned404. Repeated exact-title/DOI searches returned the publisher and JSTOR metadata, MPIM1984 preprint, and a modern translation; the final German published scan remains unobtained. https://wglobke.github.io/publications/Wuestholz1989.pdf is an18-page English translation of the1989 text by WolfgangGlobke,6June2016; its MainTheorem p2 and remarks2–3 pp2–3 were opened and are labeled as translation. The theorem application in A.4.16 uses the independently opened original German MPIM84-7 preprint, not an assertion that the final original scan was read.

## 21. The exact Frobenius-lifting criterion at one place

**ELL-23 / A.4.20 (proved).** For a non-CM elliptic curve E/L and every unramified good place v above p>2, absolute crystalline Frobenius does not preserve Fil¹ H¹_dR(E/L_v). In particular no Frobenius-fixed projector with that kernel exists at such a place.

Here is the exact proof. Put k_v=F_q, q=p^f, W=W(k_v)=O_Lv and M=H¹_dR(𝓔/W)=H¹_cris(E_k/W). The Hodge line is a saturated rank-one direct summand. Stability over L_v gives integral stability because F(M)⊂M. In a basis starting with a generator of Fil¹, F has semilinear matrix [[a,b],[0,d]] with a,b,d∈W. Its reduction kills invariant differentials, so a∈pW. Cup product makes wedge²F equal pσ, hence v_p(ad)=1 and therefore v_p(a)=1,v_p(d)=0. The linear iterate F^f has diagonal entries the σ-norms of a,d, of valuations f and0, so is nonscalar. It is the crystalline action of the algebraic q-Frobenius π_q on the special fiber. The Serre–Tate–Grothendieck–Messing criterion now lifts π_q to an actual endomorphism of 𝓔/W, because it preserves the integral Hodge filtration. The lift is nonscalar since its crystalline action is. This local endomorphism descends to Qbar: its finite kernel is a subgroup of algebraic torsion of E, the quotient is defined over Qbar, and an isomorphism of the quotient with E descends to Qbar because equal j gives such an isomorphism over an algebraically closed field and all automorphisms of E are algebraic. Thus E has CM, contradicting the assumption. A Frobenius-fixed projector would preserve its kernel, proving the final assertion.

The exact morphism-lifting statement was opened in the primary author preprint by Lorenz Panny, Damien Robert and Alessandro Sferlazza, *Hensel-lifting black-box algorithms and fast trace computation for elliptic-curve endomorphisms*, dated28September2026, https://www.math.u-bordeaux.fr/~damienrobert/pro/publications/articles/lifting_traces.pdf. Theorem3.4, pp12–13, gives the full equivalence between abelian schemes over Z_q (p>2) and their special fibers equipped with a lift of the Hodge filtration; morphisms must preserve that filtration. Remark3.5 p13 gives the exact image of the reduction homomorphism on Hom. AppendixB supplies the Grothendieck–Messing details. The original Katz1981 scan https://web.math.princeton.edu/~nmk/old/serretatelocmod.pdf was also opened, downloaded and read: Theorem1.2.1 pp143–145 is the Serre–Tate equivalence and full-faithfulness proof; Theorem2.1(4), p149, gives the ordinary homomorphism-lifting equation q(A;x,f^ty)=q(B;fx,y). No equivalence of different deformation conditions is left implicit.

This is a proved local consequence with a concrete lifted endomorphism, not a solution of H1. A.4.19 already computes that the needed crystalline stability can fail on an actual CM curve with algebraic h. A deduction of stability at a suitable place from the single complex algebraicity statement remains unestablished.

## 22. Exact ordinary base change in the Hodge–Tate criterion

**ELL-24 / A.4.21 (proved).** For the explicit non-CM curve E*:y²=4x³−4x−1, its p-divisible group after base change to O_C5 has CM and its Hodge–Tate period field is Q5. The base-changed elliptic curve still has no CM.

The discriminant37 is a unit at5. Direct enumeration gives the numbers of y-solutions0≤x<5 as2,2,0,1,2, so #E*(F5)=8 and a5=−2. Thus its good reduction is ordinary. Its ordinary p-divisible group over O_C5 is an extension

\[
 0\longrightarrow\mu_{5^\infty}\longrightarrow G
 \longrightarrow\mathbf Q_5/\mathbf Z_5\longrightarrow0.
\]

After trivializing the height-one factors, the extension is described by a Serre–Tate parameter q_ST∈1+m_C5. Choose compatible roots q_n∈O_C5 with q_n^(5^n)=q_ST and q_(n+1)^5=q_n. These exist because C5 is algebraically closed. The Kummer description of level5^n has components indexed by a mod5^n with x^(5^n)=q_ST^a; the points (q_n^a,a) define compatible sections of its étale quotient. Explicitly, addition uses the carry correction x*y/q_ST^floor((a+b)/5^n), and q_n^(5^n)=q_ST makes these points compatible with that law. The transition to level5^(n+1) sends (x,a) to(x,5a), which is compatible because q_(n+1)^5=q_n. Thus

\[
 G\simeq\mu_{5^\infty}\oplus\mathbf Q_5/\mathbf Z_5
 \quad\hbox{over }\mathcal O_{\mathbf C_5}.
\]

The two projections give Q5×Q5 inside End(G)⊗Q5, of rank2 equal to htG; this is precisely CM in Howe's definition. In the induced Tate-module basis, the Hodge–Tate line is the multiplicative summand, so has coordinate[1:0] and fieldQ5. The elliptic curve itself has j=110592/37, which is not an algebraic integer, hence is non-CM. Its endomorphism algebra does not change under algebraically closed extension by the finite-kernel/quotient descent argument in A.4.20.

Primary source: Sean Howe, *Transcendence of the Hodge–Tate filtration*, JTNB30(2018),671–680, DOI10.5802/jtnb.1044, complete final PDF https://www.numdam.org/item/10.5802/jtnb.1044.pdf opened/downloaded. The exact Hodge–Tate sequence is(1.1), p672; Theorem1.2 and Remark1.3 p673. Remark1.3 explicitly states that ordinary extensions become split over O_C, whereas a model over the integers of a finite p-adic extension has CM only for torsion Serre–Tate coordinate. Our explicit E* realizes the first phenomenon. Thus applying Howe's equivalence to this actual G reaches its true conclusion while providing no CM endomorphism of E*. This is an explicit map and example, not a general assertion that Hodge–Tate theory cannot relate to the original complex question.

## 23. The exact adelic denominator condition

**ELL-25 / A.4.22 (proved).** Let f(q)=Σb(n)q^n be a normalized rational weight-two newform, ε=Σb(n)q^n/n, and Λ_f its elliptic period lattice. For every good ordinary prime outside Guerzhoy's finite exceptional set there is λ_p∈Z_p with

\[
 \zeta(\Lambda_f,\varepsilon)-\lambda_p\varepsilon\in\mathbf Z_p((q)).
\]

For every a∈C_p, the series Z_a=ζ(Λ_f,ε)−aε has coefficients with bounded p-adic denominators if and only if a=λ_p. The proof is exact: b(p^r)=b(p)b(p^(r−1))−p b(p^(r−2)), so b(p^r) is a p-adic unit at an ordinary prime. Thus the q^(p^r) coefficient of ε has valuation−r. In Z_a=Z_λ+(λ−a)ε, the first term is integral; if a≠λ, the second term has valuation v_p(λ−a)−r, eventually negative and strictly smaller than the first. No cancellation can keep these valuations bounded.

There is an explicit actual CM example showing why coefficient algebraicity alone supplies no universal denominator bound. On E0:y²=4x³−4x, h=0. Put t=−2x/y, R=√(1+4t⁴). Then

\[
 x=(1+R)/(2t^2),\qquad du=dt/R,\qquad
 d\zeta=-\frac{1+R^{-1}}{2t^2}dt.
\]

Integrating the binomial expansion gives

\[
 \zeta(u(t))=t^{-1}-\frac12\sum_{n\ge1}
 \frac{(-1)^n\binom{2n}{n}}{4n-1}t^{4n-1}\in\mathbf Q((t)).
\]

For n_r=(3^(2r+1)+1)/4=1+2Σ_(j=0)^(r−1)3^(2j+1), adding n_r+n_r in base3 creates exactly r carries. Therefore v3 binom(2n_r,n_r)=r, while v3(4n_r−1)=2r+1. The coefficient of t^(3^(2r+1)) has valuation−r−1. This is a proof of unbounded denominators on a CM curve with algebraic splitting. Integral invertible formal coordinate changes preserve boundedness by substitution in both directions. The symbolic identities and first five exact valuations were checked in `work/code_elliptic/check_denominators.py`; source/output copied into the deliverable. The new actual E* point count for A.4.21 was added to `check_endomorphism_projector.py`, rerun and copied.

For a putative algebraic h, an embedding of its coefficient field into C_p makes the ordinary criterion applicable. The additional equality required is ι_p(h)=λ_p, or exactly the boundedness of this particular embedded series. It has not been proved. Guerzhoy's adele construction records a complex component and finite components; being an element of the adele ring does not identify those components with a diagonal algebraic number.

Primary: Guerzhoy2014, *On Zagier's adele*, Research in the Mathematical Sciences1,7, DOI10.1186/2197-9847-1-7, https://link.springer.com/content/pdf/10.1186/2197-9847-1-7.pdf. Complete PDF opened/downloaded. Equation2, Proposition2 and equation3 p4; Theorem2 pp4–5, equation4 p5; formal-group proof pp5–7. The PDF p5 was rendered and visually checked: μ_p=0 when b(p) is NOT congruent to0 modp; OCR loses this negation. Our proof uses only uniqueness of the single correction at ordinary primes, proved above, and does not rely on any unqualified uniqueness of a pair of corrections.

## 24. Exact geometric transfer to harmonic Maass coefficients

**ELL-26 / A.4.23 (proved).** For a modular parametrization π:X0(N)→E/Q of degree d, write π*ω=mω_f, m∈Q×, ω_f=f(q)dq/q. Choose the class η_f^alg=(m/d)π*ξ. The pair (ω_f,η_f^alg) has cup-product1, because our Legendre determinant2πi gives <ω,ξ>=1 and pullback multiplies the pairing by d. The pullback image is the two-dimensional f-component; its injectivity follows from the nonzero pairing. The decomposition ξ=−hω−c barω gives exactly

\[
 \eta_f^{\mathrm{alg}}=a\omega_f+b\overline{\omega_f},
 \qquad a=-m^2h/d,\quad b=-m^2c/d.
\]

Candelori's constructed harmonic Maass form F solves dF=aω_f+b barω_f−φ, with φ an algebraic second-kind representative of η_f^alg. Write φ=Σd(n)q^n dq/q, d(n)∈Q. His equation6.6 at weight2 is

\[
 [q^n]F^+=(a b(n)-d(n))/n\quad(n\ne0).
\]

Since b(1)=1, a=[q]F^++d(1). Thus all nonconstant coefficients are in Q(a), and they generate Q(a)=Q(h). With rational constant term this is exactly the whole coefficient field; an algebraic constant term preserves the algebraicity equivalence. This proves the exact morphism and scalar normalization between the geometric construction and H1.

Primary Candelori2014: *Harmonic weak Maass forms of integral weight: a geometric approach*, MathAnn360(2014)489–517, DOI10.1007/s00208-014-1043-5. Complete author-hosted32-page manuscript https://bpb-us-e1.wpmucdn.com/s.wayne.edu/dist/4/26/files/2018/09/HWMF-Final-1izyvzl.pdf opened/downloaded. Cup product5.1p20; equation6.5/Proposition6.2pp27–29; equation6.6and final paragraphp30. The final paragraph explicitly identifies the weight2 converse with Katz1976Question4.0.8 and describes it as open there.

Modern primary status check: Ehlen–Li–Schwagenscheidt, *Harmonic Maass forms associated with CM newforms*, J.reineangew.Math.813(2024)133–158, DOI10.1515/crelle-2024-0036. Complete https://arxiv.org/pdf/2210.07341 downloaded/opened; version2 submitted11February2025, manuscript date12February2025. Corollary1.2p3 proves CM coefficients lie in the newform field. Remark1.3p3 explicitly cites Candelori's geometric proof. Conjecture1.5pp3–4 states the converse classification of algebraic-coefficient shadows; it is labeled conjectural, not invoked as a theorem. Section2.2andProposition2.6p12 give the Hecke-character/binary-theta construction for the CM direction. In weight0 the algebraicity hypothesis is exactly the condition computed above. This is contemporary primary evidence of the unresolved related converse, not a proof that no later theorem could settle any special case.

Further opened primary route: Candelori–Castella2017, *A geometric perspective on p-adic properties of mock modular forms*, ResearchMathSci4,5, DOI10.1186/s40687-017-0095-z, complete final15-page PDF https://link.springer.com/content/pdf/10.1186/s40687-017-0095-z.pdf opened/downloaded. Proposition3.4andRemark3.5p7 retain a nonvanishing condition [f_beta']≠0 in overconvergent cohomology; the latter remark labels the general converse by the p-adic variational Hodge conjecture. Theorem4.1p7, Theorem5.3p11 and Theorem5.5pp11–12 give exact correction formulas under their hypotheses. Weight2 relation to A.4.20 is being checked; no application is yet claimed.

## 25. The weight-two companion-form hypothesis is proved, and the actual correction map

**ELL-27 / A.4.24 (proved).** Let f be the rational weight-two newform of E/Q and let p≥5 be good ordinary. Write roots of T²−b(p)T+p as β(unit) and β′(valuation1), and V(f)(q)=f(q^p). In the f-component of H¹_dR,

\[
 U=\mathrm{Ver},\qquad \Phi\mathrm{Ver}=p,\qquad V=U^{-1}=\Phi/p.
\]

The first two identities are Coleman's Theorems5.1and5.4; the third also follows from pullback of f(q)dq/q under the canonical-subgroup Frobenius lift q↦q^p, with its differential factor p. Restriction of proper parabolic cohomology to the wide-open ordinary locus is injective. Thus

\[
 [f-\beta Vf]=0 \iff \Phi[f]=\beta'[f].
\]

The class[f] spans the elliptic Hodge line. Stability of that line forces its eigenvalue to have valuation1, because integral Frobenius kills invariant differentials modulo p and has determinant p. Hence the displayed condition is exactly crystalline stability of Fil¹. A.4.20 proves that it forces CM. ColemanProposition7.1 constructs an overconvergent primitive of f−βVf in the CM case. Therefore CM, theta-exactness of the critical stabilization, and Frobenius-stability of Fil¹ are equivalent in this rational weight-two situation.

This is independently already proved in the original primary Emerton manuscript, *A p-adic variational Hodge conjecture and modular forms with complex multiplication*, Theorem(1.3), pp3–4: all places of the newform coefficient field above p are required, and when the coefficient field is Q there is exactly one. Proposition(1.2)p3 passes from companion forms to an inertia-split Tate module; Serre–Tate/Tate then lift Frobenius from the special fiber. Thus Candelori–Castella's general-weight remark must not be misread as an unresolved hypothesis for this rational elliptic case.

For any weakly holomorphic weight-two r with zero residues, class δ in this rank-two component, and formal primitive θB=r, put ε=Σb(n)q^n/n. Direct differentiation gives

\[
 \theta\big((B-\alpha\varepsilon)|(1-\beta'V/p)\big)
 =(1-\beta'V)(r-\alpha f),
\]

whose class is (1−Φ/β)(δ−α[f]). The primitive is overconvergent exactly when this class vanishes; the quotient theorem supplies a primitive, and the two differ only by a constant. The operator1−Φ/β has one-dimensional image, kernel the unit-root line, and nonzero value on[f] because the Hodge line cannot be the unit-root line. Thus there is exactly one α, and α=0 exactly when δ is on the unit-root line. Applied to δ=[θF+] of A.4.23, transported by an embedding of its coefficient field when h is algebraic, the remaining assertion is precisely equality of the transported complex antiholomorphic line with the unit-root line. No such equality is inferred from algebraicity. The main H1 is unchanged.

Primary sources opened in full for this check:

- Candelori–Castella2017 final PDF, Theorem3.3pp5–6, injection6p6, Prop3.4/Remark3.5p7, Theorems5.3/5.5pp11–12. The hypothesis in Remark3.5 is now verified in the rational weight-two non-CM case, through the exact map above.
- Coleman1996 *Classical and overconvergent modular forms*, InventMath124,215–241, DOI10.1007/s002220050051, https://www.wstein.org/people/coleman/papers/classical_and_overconvergent_forms.pdf, web-opened complete; same file downloaded from host without www after direct www download returned403. Theorem5.1p223, Theorem5.4p225, Proposition7.1p231, remarkp232 read. The source uses weight k+2; our weight2 is its k=0.
- Emerton original author-hosted manuscript https://www.math.uchicago.edu/~emerton/pdffiles/cm.pdf opened/downloaded complete10pages. Author's current https://www.math.uchicago.edu/~emerton/preprints.html lists it among work not intended for publication. No date appears on the PDF; p2 says the underlying observation was made in1997. We therefore label the source an undated unpublished primary manuscript, rather than assigning an unsupported publication date. Prop1.2/Thm1.3pp3–4, Remark2.3(b)p5 read. Only its proved weight2 result is used.


## 26. Corrected Mori operators and the exact theta morphism

**A.4.25 (proved).** In an algebraic symplectic frame with ∇ω=ωA+ξB and KS(ω²)=B, projection along ξ+aω gives D_a(fω^k)=(df/B+k(A/B−a)f)ω^(k+2). Therefore D_a−D_b=k(b−a) on every nonzero weight section. At an ordinary algebraic point, the equality between the complex Hodge operator transported through a specified p-adic embedding and the unit-root operator is exactly ι_p(h)=u_p. Proof is the displayed Leibniz/projection calculation in the TeX result. Mori1994 final primary PDF https://www.numdam.org/item/ASNSP_1994_4_21_1_45_0.pdf opened/downloaded complete. Theorem1 pp45–46, Theorem10p54, Sections3.3–3.5 pp56–57 retain CM and ordinary hypotheses. Section0.4p47 explicitly corrects a constant in the 1990/1991 announcements; the older numerical expressions are not used. The original 1990 download timed out/returned503 and is not claimed as fully read.

**A.4.26 (proved).** The exact normalized theta function is θ_h(u)=exp(−hu²/2)σ(u), with σ′(0)=1. The sigma coefficients lie in k=Q(g2,g3), and [u³]θ_h=−h/2; thus its coefficient field is k(h). The Kronecker theta function Θ_h=e^(−huv)σ(u+v)/(σ(u)σ(v)) begins 1/u+1/v−h(u+v)+terms of degree≥3, hence has the same exact coefficient field. Its actual line bundle is m*O([0])⊗p1*O([0])^-1⊗p2*O([0])^-1 on E×E, under the principal polarization. The sigma quasiperiod law and ηλ=hλ+c barλ prove reduced automorphy, including the area normalization c=π/area.

For every nonzero torsion class u0, define T_u0(u)=exp[−c bar(u0)(u+u0/2)]θ_h(u+u0). Direct multiplication gives T_u0=exp(−hu²/2)S_u0, with S_u0=exp[−η(u0)(u+u0/2)]σ(u+u0). Bannai–Kobayashi Theorem2.12 applies with or without CM and gives algebraic coefficients s_j of S_u0. Since s0≠0, t2=s2−hs0/2 recovers h, so Qbar(coefficients T_u0)=Qbar(h). Thus the exact torsion translation transfers the same coefficient-field condition, without introducing a new independent algebraicity input.

Primary source: https://arxiv.org/pdf/math/0610163, complete55-page version4 dated11December2007, opened/downloaded/text read. Examples1.9–1.10pp10–12; Proposition2.1/Corollary2.2pp20–21; Theorem2.12pp26–27; Proposition2.14pp28–29. Final DukeMathJ153(2010)229–295 metadata separately retrieved. The area variable in this source equals area/π. Proposition2.14's ordinary integrality proof chooses a CM multiplication whose two eigenvalues have different p-adic valuations; the proof was read and that hypothesis is retained. No ordinary integrality conclusion from coefficient algebraicity alone has been established. These are exact map/source checks; the H1 gate is unchanged.

Reproducibility: `work/code_elliptic/check_theta_operators.py` and its `.out` exactly verify the operator defect, Gaussian translation exponent identity, coefficient recovery, and theta/Kronecker initial coefficients. Source and output copied to the deliverable code directory.

## 27. Arithmetic holonomy: the exact elliptic primitive input

**A.4.27 (proved, currently a work-note result pending integration after checkpoint03).** Fix an elliptic curve y²=P(x)=4x³−g2 x−g3 over a number field K, an algebraic finite point Q=(x0,y0) with y0≠0, and an arbitrary a∈K. Enlarge K to contain Q. The germ

\[
 F_a(t)=-\int_0^t\frac{x_0+s+a}{\sqrt{P(x_0+s)}}\,ds,
 \qquad \sqrt{P(x_0)}=y_0,
\]

is a G-function over K for every such a. More explicitly it satisfies the second-order equation

\[
 2P(x)(x+a) F_a''(x)
 +\bigl(P'(x)(x+a)-2P(x)\bigr)F_a'(x)=0,
\]

with x=x0+t, and its first n Taylor coefficients admit a common denominator at most exponential in n. This includes every algebraic correction parameter; it does not single out the actual Hodge parameter.

Proof. Write P(x0+t)=y0²(1+b1t+b2t²+b3t³). The binomial identity

\[
 (1+z)^{-1/2}=\sum_{m\ge0}(-1)^m\binom{2m}{m}z^m/4^m
\]

gives an explicit algebraic derivative. Choose an integer C≥1 clearing the denominators of b1,b2,b3, (x0+a)/y0, and 1/y0 in O_K. If e_n=[t^n]F_a'(t), then (4C)^(n+1)e_n∈O_K, because every summand uses at most n of the bi and one further cleared factor. Thus (4C)^(n+1)lcm(1,…,n) clears the first n primitive coefficients. The elementary exponential bound for lcm(1,…,n) gives the required denominator bound. Each complex conjugate of the algebraic derivative is analytic on some nonzero disc around0, so Cauchy's estimate bounds all conjugates of the coefficients exponentially. Finally the logarithmic derivative of F_a′ is 1/(x+a)−P′/(2P); clearing denominators gives the displayed linear equation. This verifies each G-function condition directly.

If x=wp(u), x0=wp(u0), the exact analytic map is

\[
 F_a(x-x_0)=\zeta(u)-au-\bigl(\zeta(u_0)-au_0\bigr).
\]

At the actual Hodge value, its additive monodromy along a closed elliptic loop of period λ is η_λ−hλ=c barλ. This is nonzero for every nonzero λ. Thus this particular holomorphic primitive does not cancel any nonzero elliptic homology period. This is a computed monodromy statement, not a claim that arithmetic holonomy could never be applied through another construction.

Primary route opened: Calegari–Dimitrov–Tang, *The linear independence of 1, zeta(2), and L(2,chi_-3)*, current author-hosted218-page manuscript https://math.berkeley.edu/~ytang/L2chi.pdf, downloaded/text extracted. Theorem2.5.1 pp16–17 gives an explicit bound with a denominator template and the Bost–Charles double integral, under a strict inequality comparing conformal radius with the denominator exponent. Section2.6pp17–18 states its G-function implications. The current20-page author-hosted *Arithmetic holonomy bounds and effective Diophantine approximation*, https://math.uchicago.edu/~fcale/papers/ICM.pdf, also opened/downloaded; its cover has2026SIAM copyright and its primary publication metadata identifies ICM2026Vol3pp356–376, DOI10.1137/25M1806776. No theorem in these consulted statements identifies mere G-function algebraicity with ordinary bounded denominators. An application here still needs a concrete quantitative improvement to the displayed denominator/radius input, or a separately proved product-formula relation. Neither has been established. The actual CM unbounded-denominator example A.4.22 remains a counterexample to an unrestricted boundedness inference.

Further active primary routes: Herblot, *Algebraic points on meromorphic curves*, author PDF dated18April2012, https://webusers.imj-prg.fr/~mathilde.herblot/publi/SL.pdf, opened complete51pages; Proposition3.6 relates p-curvature density to arithmetic type, and Theorem6.1 uses arithmetic type, residue degree, and growth order. Its exact field/degree hypotheses are being checked before any application. New primary preprint Katagiri–Kobayashi arXiv2609.07024 (7September2026), *p-adic properties of division polynomials and algebraic sigma functions*, found through primary arXiv metadata; the web PDF returned DisabledError, local download status checked separately. No theorem from that preprint is yet used.


## 28. Lam–Litt and the actual CM horizontal continuation

**A.4.28 (proved).** For Legendre y²=4x(x−1)(x−t), basis ω=dx/y, η=xω, the Gauss–Manin matrix is C=[[A,A],[B,−A]], A=1/(2(1−t)), B=−1/(2t(1−t)). The reduction identity is d(x(x−1)/y)=((x−t)/2−t(t−1)/(2(x−t)))ω. At t0=1/2 the translation x=X+1/2 gives g2=1,g3=0,h=0; thus η−ω/2 is the actual anti-Hodge vector. Its horizontal extension V=(F,G), in s=t−1/2, has G=sum_m(prod_(j<m)(4j+1))²/(2m)! s^(2m), F=(1/2−2s²)G′−(1/2+s)G. Eliminating F gives (1−4s²)G″−8sG′−G=0 and proves the formula. For every prime p≡3mod4, coefficient degreep+1 has valuation−1: numerator factors lie below2p and exclude the only possible multiplep, denominator(p+1)! has valuation1. This proves infinitely many denominator primes and failure of omega(p)-integrality for an actual CM splitting with h=0.

Lam–Litt arXiv2501.13175v1, submitted22January2025, manuscript24January2025, complete93-page PDF opened/downloaded; primary abstract page confirms onlyv1 currently listed. Theorem4.1.1p21 and proofp24 read. It applies to every nonzero algebraic initial vector in positive Sym^n H1 of the nonisotrivial Legendre family, after choosing R=O_K[1/N] containing all data and makingt0,1−t0 units. The exact relation to h is horizontal continuation of ξ+hω in the Betti trivialization, obtained by freezing the antiholomorphic coordinate in the real-analytic Hodge vector. Algebraic initial data do not imply integral jets; the explicit CM example proves this directly. The adjacent Proposition4.0.1 omits a nonzero initial-value hypothesis (zero gives a trivial exception); we use the properly stated Theorem4.1.1 instead. No general conjecture from the source is used.

## 29. The Gaussian-invariant division-polynomial map

**A.4.29 (proved).** For every complex a and θ_a=e^(−au²/2)σ, the normalized division polynomial is F_n(P(u))=σ(nu)/σ(u)^(n²)=θ_a(nu)/θ_a(u)^(n²). The quotient is elliptic by sigma automorphy, has divisor[n]*O−n²O and leadingn u^(1−n²), uniquely fixing the stated rational normalization. The Gaussian cancellation is a formal characteristic-zero identity, hence also valid p-adically. Likewise η^(a)(u0)=η(u0)−a u0 gives exp(−η^(a)(u0)u0/2)θ_a(u0)=exp(−η(u0)u0/2)σ(u0). Thus the map a↦all division-polynomial quotients and normalized torsion constants is constant, an actual noninjective map. This says exactly what those data retain; it is not a categorical claim excluding any application through a different construction with additional data.

Primary Katagiri–Kobayashi arXiv2609.07024v1,7September2026, complete17-page primary PDF downloaded successfully despite web retrieval DisabledError. Text read at normalizationp2; Theorem1.3/Cor1.4pp3–4; Definition2.3,Prop2.5,Thm2.7pp6–7; proofp8. Its ordinary/supersingular p-power subsequential limits are expressed in the algebraic sigma constant appearing above, so these inspected limits preserve the Gaussian ambiguity. The exact complex reduced parameter a=h is not recovered by this map. H1 remains unchanged.

A.4.27–29 were integrated into the paper after checkpoint03. Their exact symbolic checks and eight CM prime-valuation samples are in `check_arithmetic_continuation.py` and `.out`, copied into the deliverable code directory. The infinite proofs are supplied independently of the finite samples. The CDT2024 primary arXiv metadata was opened and confirms version2,16September2024; the consulted author-hosted218-page manuscript has the same length.


## 30. The actual Hodge parameter is the unique minimal-growth correction

**A.4.30 (proved).** For theta_a(u)=exp(−a u²/2)sigma(u), c=pi/area(Lambda),

\[
 \log\max_{|u|\le r}|\theta_a(u)|
 =\tfrac12(c+|h-a|)r^2+O(r).
\]

The actual h is the unique minimizer of quadratic type; every a still has order2. Full proof: B(u)=|theta_h(u)|exp(−c|u|²/2) is continuous Lambda-periodic by reduced automorphy, hence bounded above and positive at one chosen u0 outsideLambda. The growth is B(u) times exp((c|u|²+Re((h−a)u²))/2). The real quadratic form has eigenvalues c±|h−a|. For a maximizing direction phi, choose u_r in u0+Lambda within a fixed covering radius R of (r−2R)exp(i phi). Then |u_r|≤r, B(u_r)=B(u0)>0 and u_r=r exp(i phi)+O(1), giving the lower bound. This is actual extra archimedean information; no arithmetic consequence forcing CM is established.

Exact source checks: Herblot2012 Theorem6.1pp31–32 contains order, arithmeticity, residue degrees, and a connected uniformizing curve; its inequality has no quadratic-type parameter. We do not omit those hypotheses or assert an unverified application. Fonseca2019 final original52-page journal PDF was opened and downloaded from MaxPlanck: https://pure.mpg.de/rest/items/item_3155674_6/component/file_3402781/content (web-open successful at the repository's full filename URL, content endpoint local download successful). Theorem1.2p648 requires a formal morphism over O_K[[q]], analytic continuations at every embedding with product of radii1, moderate growth, ZL-density, and concludes only at q≠0. The actual horizontal germ A4.28 places its chosen algebraic Hodge value at the excluded center0; its CM example also has infinitely many denominator primes in the displayed algebraic frame. No map meeting all these conditions and yielding the desired h consequence has been constructed. This is an exact applicability check, not a claim excluding other maps or other theorems. H1 unchanged.

Reproducibility: check_growth_type.py/.out verifies the norm automorphy cancellation and the exact quadratic-form eigenvalue polynomial; the infinite lattice-covering argument is proved separately in the result. Copied to the deliverable code directory.

Further primary searches opened since checkpoint03:

1. Masser1977, original Compositio35(3)239–258, https://www.numdam.org/article/CM_1977__35_3_239_0.pdf. Original theorem p241 and algebraically defined quasi-periodic-function hypotheses pp239–240 read. Its input is a linear quasiperiod of an algebraically defined function. For the actual Hodge relation eta−h omega=c baromega, the coefficient c=pi/area is still not proved algebraic; it is not silently inserted into that theorem.
2. Sebbar arXiv2610.30025v1, Zeros of E2, quasi-periods, and Schwarz maps,35pages, direct primary PDF downloaded successfully after web DisabledError. Section14 Prop14.1pp33–34 constructs its stated map for algebraic tau and algebraic quasi-period ratio; rank2, closure dimension2 and p(H)=2 give the failed numerical requirement4≥12. Its conjectural implications are not invoked. The ordinary E2-zero hypotheses differ from actual h by the explicitly retained E2* correction, already computed in A4.1.
3. Bertrand1978, original11-page exposition plusarchivecover, https://numdam.org/item/SDPP_1977-1978__19_2_A10_0.pdf. Section6 printed36-10 directly relates Conjecture3 to KatzQuestion4.0.8. This is historical source evidence only. The later2001 chapter was located at DOI10.1007/3-540-44550-1_1; publisher full-PDF URL redirects to subscription preview, so its Conjecture4.3 is still not claimed as read.
4. Grinspan2002, Measures of simultaneous approximation for quasi-periods of abelian varieties, JNT94(1)136–176 DOI10.1006/jnth.2001.2733: publisher metadata/abstract opened, full publisherPDF unavailable403; CiteSeer copy also403. No detailed theorem from the unopened full text is used.
5. Wuestholz1989 original German final still unobtained. Latest author-publication-list, Annals metadata, and JSTOR attempts did not yield an original scan. The separately read1984German primary preprint and2016English translation retain their exact labels.

### Source-status update at 06:39 UTC: Grinspan primary manuscript obtained

The primary 38-page author manuscript of Grinspan, *Measures of simultaneous approximation for quasi-periods of abelian varieties*, has now been opened in full through the indexed CiteSeer mirror, despite the earlier direct-download403. URL: https://citeseerx.ist.psu.edu/document?doi=cfd5bb150869cb66ffd696c5945d086f0e060ca9&repid=rep1&type=pdf . This supersedes only the earlier assertion that no detailed theorem from the manuscript was available; the final41-page journal article remains separately unobtained. Read Theorem1.2/Corollary1.1pp2–3, Proposition6.1pp22–23, and Section7pp35–36, including Proposition7.1 and the exact zero-period hypothesis. That proposition applies to a second-kind differential with a nonzero homology class on which its period vanishes. For the actual corrected differential dζ−h du, its period on λ is c barλ, which is nonzero for every λ≠0 by A.4.27. Thus this direct substitution does not meet that proposition's hypothesis. Theorem1.2 treats the full period/quasiperiod tuple; its qualitative corollary is transcendence degree at least2, with no extraction of the quadratic expression h. The source's stated higher-dimensional refinements and its own conjectural discussion are not promoted to a solution of H1. Exact potential improvement to the simultaneous approximation input remains unestablished.

Additional primary applicability work, not a theorem claim: Movasati's current author book *Leaf schemes and Hodge loci*, dated10August2026, https://w3.impa.br/~hossein/myarticles/LeafScheme.pdf , complete138-page PDF downloaded. Chapter4pp69–72, Theorems4.1–4.4, gives the enhanced elliptic moduli, its Ramanujan field, characteristic-p Cartier conditions, and special-cusp integrality. These hypotheses have not been verified for horizontal continuation from an arbitrary algebraic actual-Hodge initial point. Lam–Litt arXiv2601.07933v1, *The non-abelian p-curvature conjecture for the isomonodromy foliation*, complete45-page primary PDF downloaded and TheoremsA/Bpp2–3 read: the global foliation p-curvature hypothesis is retained; it has not been deduced from algebraicity of a single actual Hodge parameter. No H1 movement is inferred from either consultation.

### Primary 2026 p-adic source audit at 06:42 UTC

Howe–Klevdal, *Admissible pairs and p-adic Hodge structures, I: Transcendence of the de Rham lattice*, Algebra and Number Theory20(5)(2026),971–1028, DOI10.2140/ant.2026.20.971, full final primary PDF opened: https://msp.org/ant/2026/20-5/ant-v20-n5-p03-p.pdf . Remark1.1.4p976 states that the Hodge–Tate filtration of an ordinary elliptic curve is algebraic, whereas its canonical Hodge–Tate grading is algebraic precisely when its Serre–Tate coordinate is a root of unity. Section6.3p1026 explains that Howe2018 omitted the rigidification and that over O_C the étale part of a p-divisible group can always be split off from its connected part. These statements are consistent with the exact base changes retained in A.4.21. Theorem6.1.1p1023 states the Cohen–Shiga–Wolfart CM criterion with algebraicity on the Betti Hodge filtration, explicitly defined via H1(A(C),Q) and its complexification. The map from the algebraic de Rham h to that Betti filtration remains the actual comparison matrix of A.4.11/A.4.18; no algebraicity of its entries is inserted. The source's conditional TheoremA is not used. Its final version was received25January2024, revised28February2025, accepted2May2025. This source audit changes no H1 status.

## 31. General Cartier coefficient formula (work-note proof; pending paper integration)

Let k be a perfect field of characteristic p>3, let E:y²=P(x)=4x³−g2x−g3 be smooth, and retain omega=dx/y, xi=x dx/y. Define

    H_p = [x^(p−1)] P(x)^((p−1)/2),
    K_p = [x^(p−2)] P(x)^((p−1)/2).

On the universal-extension chart with coordinate t, put

    D_a = y∂x + (6x²−g2/2)∂y − (x+a)∂t,
    V = −∂t,   a∈k.

Then, as derivations of k(E)(t),

    D_a^p = H_p D_a − (K_p+a H_p)V.                 (31.1)

This is a formula for the p-th iterate, hence for the restricted Lie operation. It retains the exact algebraic coordinate t=ζ(u)−s from A.4.14.

Proof of the Cartier coefficients. Since y^(p−1)=P^((p−1)/2), write omega=P^((p−1)/2)dx/y^p and xi=xP^((p−1)/2)dx/y^p. The rule C(f^p x^m dx)=0 unless m≡p−1 modp, with C(f^p x^(p−1)dx)=f dx, extracts exactly the indicated coefficients: both numerator degrees are less than2p−1. Thus C(omega)=H_p^(1/p)omega and C(xi)=K_p^(1/p)omega. Roots are unambiguous because k is perfect. These equations also specify the Frobenius-semilinearity convention.

The invariant forms omega and beta=−dt−xi are dual to the invariant vector fields D_0,V in the sense omega(D_a)=1, beta(D_a)=a, omega(V)=0, beta(V)=1. Cartier kills dt, so C(beta)=−K_p^(1/p)omega. For a closed form alpha and a derivation D, the Cartier contraction identity reads

    alpha(D^p) − D^(p−1)(alpha(D)) = (C(alpha)(D))^p.

Applying it to omega,beta and D_a, whose displayed contractions are constants, gives omega(D_a^p)=H_p and beta(D_a^p)=−K_p. Since D_a^p is invariant and omega,beta are an invariant coframe, these two equalities give (31.1). Equivalently it may be checked on x,y,t; the polynomial identity underlying its t component is delta^(p−1)x=H_p x−K_p for delta=y∂x+(6x²−g2/2)∂y.

It follows that the line kD_a is stable under restricted p-th power precisely when K_p+aH_p=0. At an ordinary prime H_p≠0, this singles out a=−K_p/H_p. At a supersingular prime H_p=0, one has K_p≠0, hence none of these horizontal lines is p-closed. For the nonvanishing assertion, use the conjugate-filtration exact sequence for a smooth proper curve, obtained from the Cartier isomorphism:

    0 -> H1(E^(p),O) -> H1_dR(E/k) -> H0(E^(p),Omega1) -> 0.

Its last map is Cartier on meromorphic de Rham representatives. The classes omega,xi form a basis, as their cup pairing is1. The target has dimension1 and the map is surjective; therefore H_p,K_p cannot both vanish. This proves the assertion without a density hypothesis.

Primary identity opened: Ogus, *F-crystals, Griffiths transversality, and the Hodge decomposition*, Astérisque221(1994), https://www.numdam.org/item/AST_1994__221__1_0.pdf , Proposition1.2.4 and equation(1.2.4.5), printedp24, with the inverse Cartier discussionpp24–25. In its Frobenius-twisted notation, the contraction identity is precisely the displayed formula after identifying the twist using the perfect base field. The proof above calculates every coefficient, not just the existence of a Cartier map. Katz, *Equidistribution questions for universal extensions*, https://web.math.princeton.edu/~nmk/univextn44.pdf , Section9pp11–13, was also opened: its explicit coefficient-extraction computation uses the same Cartier rule. Its equidistribution Conjecture6.1 and conditional Lemma7.1 are not used.

At p=5, H_5=2g2 and K_5=2g3, so (31.1) is exactly D_a^5=2g2D_a+(3g3−2g2a)V, recovering A.4.14. The all-prime proof makes the ordinary finite-place equation explicit, but no deduction of these congruences from algebraicity of the actual complex h has been obtained. In particular the CM supersingular example remains an explicit failure of unrestricted p-closure. H1 is unchanged.

Exact finite certificate: `work/code_elliptic/check_cartier_all_primes.py` checks delta^(p−1)x=H_p x−K_p for generic g2,g3 at p=5,7,11,13,17,19, independently of the Cartier proof.

Integration update after checkpoint04: §31 is now A.4.31 in the paper. Generation and root independently passed its algebra/sign and primary Ogus source audit. The integrated proof uses the rational coframe directly, without requiring a separate invariance argument. It also constructs the xi de Rham class explicitly in the parameter z=-2x/y: xi=(z^(-2)+O(z^2))dz, remove d(-1/z), use overlap 1/z, and compute cup residue1. This makes the Cartier projection and nonvanishing argument precise. The exact script and output have been copied to the deliverable code directory. No H1 status change.

## 32. Herblot density application, with an explicit projective uniformization

**A.4.32, proved and independently audited by root and generation.** Let K be a number field containing g2,g3,a, with smooth E:y²=4x³−g2x−g3 and a algebraic. Write d=[K:Q]. Outside a finite set of primes of K, reduce the coefficients H_p,K_p of A.4.31 and a. If v lies over the rational prime p, put w_v=[K_v:Q_p]log(p)/(p−1), and define

\[
 \beta_K(a)=\liminf_{X\to\infty}
 \frac{\sum_{v\mid p,\ p\le X,\ K_p+aH_p=0} w_v}
      {\sum_{v\mid p,\ p\le X}w_v}.
\]

The proposed conclusion, proved by the construction below, is

\[
 \beta_K(a)\le 1-\frac1{4d}.
\]

For K=Q the bound is3/4. This is a bound on the specified weighted LOWER density of p-closed reductions. Equivalently, the complementary weighted UPPER density is at least1/(4d). A lower-density assertion about the complement is not made.

### 32.1 Actual compactification and growth section

Let G=E†. Its additive torsor over E determines an algebraic rank-two vector bundle V fitting into 0→O_E→V→O_E→0: a torsor cocycle b_ij is sent to the transition matrix [[1,b_ij],[0,1]]. In the projective bundle X=P_E(V) of lines, the complement of the line subbundle P_E(O_E) is exactly G, by the affine fiber coordinate s=v0/v1 on v1≠0. This constructs the compactification over K and preserves the identity point.

At a fixed embedding K→C, the period uniformization of A.4.14 gives the analytic presentation

\[
 V^{an}=(\mathbb C\times\mathbb C^2)/
 \bigl((u,v_0,v_1)\sim(u+\lambda,v_0+\eta_\lambda v_1,v_1)\bigr).
\]

Thus the holomorphic group curve is the exact map

\[
 \Theta_a:\mathbb C\longrightarrow G(\mathbb C)\subset X(\mathbb C),
 \qquad u\longmapsto [u;(au,1)].
\]

It uniformizes the smooth formal leaf of the invariant line L_a at the identity. Let B=O_E([O]) and choose N sufficiently large that

\[
 \mathcal L=O_{P(V)}(1)\otimes\pi^*B^{\otimes N}
\]

is ample. Give V a smooth Hermitian metric. Its induced metric on the tautological O_P(V)(−1) makes the vector v_a(u)=(au,1) a nowhere-zero holomorphic section of Θ_a*O(−1).

Choose a compact fundamental parallelogram, write u=w+λ with w in it, and use the preceding cocycle to identify this vector with (au−η_λ,1) over w. Since λ↦η_λ is real-linear on the period lattice, |η_λ|≤C|λ|. Uniform boundedness above and below of the Hermitian matrix on the compact parallelogram yields

\[
 C_1\le\|v_a(u)\|\le C_a(1+|u|).
\]

The positive lower bound also follows directly from the fixed quotient V→O_E, because v_a maps to1 and the quotient-map norm is bounded on the compact base.

The reduced theta multiplier is

\[
 \theta_h(u+\lambda)
 =\epsilon_\lambda
   \exp(c\bar\lambda(u+\lambda/2))\theta_h(u),
 \qquad c=\pi/\operatorname{area}(\Lambda).
\]

It presents the same line bundle B: θ_h has precisely the simple divisor Λ. In the corresponding holomorphic frame e_h of its pullback to C, the metric

\[
 \|e_h(u)\|=\exp(-c|u|^2/2)
\]

descends, because its ratio under u↦u+λ is the inverse modulus of the multiplier. It is a smooth positive metric on B. Consequently

\[
 s_a(u)=v_a(u)\otimes e_h(u)^{-N}
\]

is a nowhere-zero holomorphic section of Θ_a*\mathcal L^{-1}, and

\[
 C_1e^{Nc|u|^2/2}
 \le\|s_a(u)\|
 \le C_a(1+|u|)e^{Nc|u|^2/2}.                 \tag{32.1}
\]

This verifies Herblot Definition5.1 exactly on M=P¹, T={∞}, and ρ=2; Definitions5.4–5.5 give a connected order-two uniformization of the one formal branch at u=0.

The order cannot be reduced by choosing another nonzero holomorphic section for this ample bundle. Every such section is f(u)s_a(u) with a nonzero entire f. If f has a zero of order m at0, Jensen's formula applied to f(u)/u^m gives mean(log|f(re^{iθ})|)≥m log r+C for large r. The lower bound in(32.1) therefore forces

\[
 \log\max_{|u|=r}\|f(u)s_a(u)\|
 \ge Nc\,r^2/2+m\log r+C.
\]

Thus the minimal possible quadratic type of these growth sections is Nc/2, attained by s_a, for EVERY a. This is an exact calculation on the projective uniformization: the scalar-theta type from A.4.30 does not produce a smaller order or a smaller leading growth constant for this particular application.

### 32.2 Closure, finite-place input, and the number-field factor

The Zariski closure of Θ_a(C) in G is a connected algebraic subgroup. Indeed, the analytic image is a connected subgroup; inversion and multiplication preserve its closure, using that the product of two Zariski-dense subsets is dense in the product. Its projection to E is nonconstant and therefore surjective. If the closure had dimension1, it would be the forbidden subgroup with Lie algebra L_a of A.4.15. Hence its dimension is2. Vanishing of a rational function on the formal leaf gives vanishing on the analytic curve by the identity theorem, so the formal leaf has the same closure.

After excluding finitely many primes, the invariant line is a nonsingular algebraic foliation on the open G of the smooth projective K-surface X. By A.4.31 its p-curvature vanishes exactly when K_p+aH_p=0. Herblot Definition3.5, p20, is the displayed weighted lower density; Proposition3.6, pp20–21, makes the formal leaf (1−β_K(a))-arithmetic. Its proof also gives every slightly larger arithmeticity parameter, so the case β=1 can be handled by a positive parameter tending to0.

Regard the integral projective K-surface X as an integral projective Q-variety by composition with SpecK→SpecQ. This finite base map preserves dimension and projectivity, and the Q-variety is smooth because K/Q is etale. The identity is a closed point with residue field K and degree d; its formal branch is the same K-formal curve. Herblot Lemma2.6 preserves arithmeticity upon passing from K to a finite Galois closure. Definition4.6 and its Remark/Lemma4.5, p28, then transfer it to every residue-field embedding, giving precisely the required arithmeticity of the closed-point formal branch. Definition5.4 requires only one geometric point above each closed point, so the selected complex embedding suffices for the analytic uniformization. Theorem6.1 imposes no geometric-connectedness hypothesis on X. The Q-Zariski closure has dimension2: a Q-closed subset containing the dense chosen complex component contains all its Galois conjugates, hence every component after extending scalars.

Apply Herblot Theorem6.1, pp31–32, with one closed point, d1=d, r=2, ρ=2, and α1=1−β (or a slightly larger positive parameter). Its inequality becomes

\[
 \frac1{(1-\beta)d}\le \frac2{2-1}\,2=4.
\]

Taking the limit from positive arithmeticity parameters proves the claimed bound. The degree factor d is retained; replacing the K-variety by a Q-rational single point without constructing the corresponding restriction-of-scalars foliation would not justify deleting it.

### 32.3 Exact consequence for the main gate

This bounds the weighted density of the explicit congruences for every algebraic a, including every proved CM value h. It strengthens the infinite-prime failure of A.4.15 to a quantitative upper-density statement about the failures. No result here makes a putative algebraic actual Hodge coefficient satisfy these congruences with any positive density, and no contradictory density is inferred. H1 remains unchanged.

Source audit: primary author PDF https://webusers.imj-prg.fr/~mathilde.herblot/publi/SL.pdf , dated18April2012, complete51pages, reopened in full. Relevant exact locators: Definition3.5 and Proposition3.6, printedp20/proofp21; Definition4.6p28; Definition5.1p29; Definitions5.4–5.5p31; Theorem6.1pp31–32. Web fullref turn994742515view0; exact densityref turn994742515view2. The introductory sentence in Section3.1 interchanges the endpoint descriptions0 and1; the actual Definition3.5 and Proposition3.6/proof are used, with liminf and weights explicitly retained.

## 33. The actual antiholomorphic quotient and its exact differential scalar

**Proved, independently audited by root and generation, and integrated as A.4.33.** Retain E/Qbar, its chosen algebraic differential, h, and c=pi/area(Lambda)>0. Let conjugateE be the algebraic elliptic curve obtained by conjugating g2,g3. Its differential-normalized lattice is barLambda. There is a surjective analytic group homomorphism

\[
 \Phi_h:E^\dagger(\mathbb C)\longrightarrow\overline E(\mathbb C),
 \qquad [(u,s)]\longmapsto[(s-hu)/c]\pmod{\bar\Lambda}.
\]

Its kernel is precisely exp(L_h), and exp:C→exp(L_h), u↦[(u,hu)], is injective. The homomorphism Φ_h is never algebraic over C. Its differential in the algebraic coLie coordinates is

\[
 \Phi_h^*(d\bar u)=c^{-1}(ds-h\,du),
 \quad\text{or as a tangent row}\quad (-h/c,\,1/c).
\]

The pair (h,c) cannot belong to Qbar². In particular, algebraicity of h entails transcendence of c. The actual CM curve(g2,g3,h)=(30,28,1/2) supplies an explicit nonalgebraic analytic homomorphism between algebraic groups whose differential has algebraic projective class[-1/2:1].

### 33.1 Descent, kernel, and nonalgebraicity

The period identity eta_lambda−h lambda=c barlambda shows that changing(u,s) by(lambda,eta_lambda) changes(s−hu)/c by barlambda. This proves descent. Takingu=0 ands=cz proves surjectivity.

IfΦ_h([(u,s)])=0, choose lambda∈Lambda with(s−hu)/c=barlambda. Subtract(lambda,eta_lambda). The remaining representative satisfies

\[
 s-\eta_\lambda-h(u-\lambda)
 =(s-hu)-(\eta_\lambda-h\lambda)=0.
\]

It lies in L_h, proving the claimed kernel equality. Conversely every vector of L_h maps to0. If(u,hu) itself is a period(lambda,eta_lambda), thenu=lambda andeta_lambda−h lambda=c barlambda=0. Sincec>0, lambda=0. This also proves injectivity of its complex one-parameter uniformization.

The restriction ofΦ_h to the algebraic vertical subgroup Ga is

\[
 s\longmapsto[s/c]\in\mathbb C/\bar\Lambda,
\]

whose derivative is1/c≠0. Any algebraic map A¹_C→an elliptic curve extends at infinity to P¹_C by properness. A nonconstant map P¹→an elliptic curve is impossible by Riemann–Hurwitz: the equality−2=degree·0+ramification would have a nonnegative right-hand side. Thus this restriction, and henceΦ_h, cannot be algebraic. This conclusion holds for everyE, regardless of CM.

### 33.2 Exact use of the analytic-homomorphism theorem

The torsion points of E† are Zariski dense. Indeed,E†[n]→E[n] is an isomorphism because multiplication byn is invertible onGa. Their algebraic closureH is a subgroup whose projection contains every torsion point ofE, hence is allE. Its identity component also projects ontoE, since otherwise finitely many components would project to finitely many points. IfdimH=1, this gives the forbidden one-dimensional algebraic subgroup of A.4.15. ThereforedimH=2 andH=E†.

Huber–Wüstholz, arXiv1805.10104v8(21April2022), Theorem6.3pp44–45 and Lemma6.5pp45–46, apply to connected commutative algebraic groups overQbar. Lemma6.5 says that an analytic homomorphism with algebraic differential is algebraic when source torsion is Zariski dense. Every hypothesis has now been supplied except algebraicity of the displayed row. If h,c were both algebraic, that row would be algebraic and the lemma would makeΦ_h algebraic, contradicting§33.1. Therefore(h,c)∉Qbar².

This uses the corrected statement. Remark6.4p45 explicitly says that an earlier version omitted a vector-group factor, and gives the exponential map as a counterexample. The present application uses the dense-torsion Lemma6.5 directly, so it neither drops a vector factor nor assumes a nonexistent algebraic differential. The complete original arXiv primary manuscript has237pages; the theorem locators here are its printed pages, not the different final-book pagination. The page with the correction and Lemma6.5 was visually inspected.

### 33.3 The exact normalization map

One can instead use the analytic target

\[
 E_c^{an}=\mathbb C/(c\bar\Lambda),\qquad
 \widetilde\Phi_h([(u,s)])=[s-hu].
\]

Here the differential is(-h,1). The target's differential-normalized short Weierstrass coefficients are

\[
 g_2(E_c)=c^{-4}\bar g_2,\qquad
 g_3(E_c)=c^{-6}\bar g_3.
\]

The actual isomorphism

\[
 \mu_c:E_c^{an}\longrightarrow\bar E^{an},\qquad
 [z]\longmapsto[z/c]
\]

satisfies Φ_h=mu_c∘tildeΦ_h and mu_c*(dbar u)=dz/c. In Weierstrass coordinates it is(X,Y)↦(c²X,c³Y), as follows from wp_{c barLambda}(z)=c^-2 wp_{barLambda}(z/c). Thus the scalar has merely moved between the differential and the chosen algebraic model.

If h is algebraic, c is transcendental by§33.2. Each nonzero coefficient amongc^-4bar g2,c^-6bar g3 is then transcendental: otherwise a positive integral power ofc would be algebraic, makingc algebraic. At least one coefficient is nonzero becauseE is smooth. Althoughj(E_c)=barj(E) is algebraic andE_c is abstractly isomorphic overC to an algebraic curve, the explicit differential-preserving short equation has these coefficients. The mapmu_c computes the transition to the algebraic model and restores the factor1/c. This proves exactly why that change of coordinates does not verify the differential hypothesis of Huber–Wüstholz.

No CM converse follows: the nonzero CM valueh=1/2 already exhibits the same transcendentalc. The main H1 gate remains unchanged.

Primary source URL https://arxiv.org/pdf/1805.10104 , coverv8dated21April2022; local files work/sources_elliptic/huber_wustholz2022.pdf/.txt,1760465bytes. Web fullref turn254797657view0; exact theorem/correctionref turn610075046view0; primary screenshot of printedp45 turn610075046view1. Final book metadata separately opened: Cambridge Tracts in Mathematics227(2022), DOI10.1017/9781009019729. Source used is the explicitly identified full author manuscript.

Integration update: root independently checked §33 and exact Huber-Wustholz source, then authorized A.4.33 integration. It is now in A_elliptic.tex, with target uniformizing coordinate v (so its holomorphic differential is unambiguous) and the additional direct identity Phi_h(kappa([u]))=[bar u]. Canonical own event rows and bibliography are ready. No H1 change.

## 34. Quotient-period continuation: exact shape and new source checks

**Research continuation, 19 November 2026, 07:37 UTC; no H1 change.** The following direct calculations have been independently audited by root and integrated as A.4.34 after CP05.

Put μ_i(a)=η_i−aω_i and Λ_a=Zμ_1(a)+Zμ_2(a). The exact real-linear map carrying Λ to Λ_a is

\[
 T_a(z)=(h-a)z+c\bar z.
\]

Its real determinant is |h−a|²−c². Consequently Λ_a is a full lattice precisely when |h−a|≠c. Indeed, off this circle T_a is a real-linear isomorphism, while on the circle its image is contained in a real line and cannot be a full lattice. This assertion concerns full two-dimensional lattices; it does not assert that the rank-one-line image on the circle is always discrete. Off the circle μ_1≠0 and

\[
 r_a=\frac{\eta_2-a\omega_2}{\eta_1-a\omega_1},\qquad
 \operatorname{Im}r_a=
 \frac{A\bigl(|h-a|^2-c^2\bigr)}{|\eta_1-a\omega_1|^2}.
\]

Thus the interior disk maps to the lower half-plane, and the actual value a=h gives r_h=barτ, Λ_h=c barΛ, and j(Λ_h)=barj(E). The fractional-linear map has nonzero determinant by the Legendre relation. All the displayed statements retain the full scale c.

The second-kind primitive also gives the exact holomorphic map

\[
 F_a:E(\mathbb C)\setminus\{O\}\longrightarrow\mathbb C/\Lambda_a,
 \qquad [u]\longmapsto[\zeta(u)-au].
\]

Its descent follows from the quasi-period transformation law. Its pulled-back invariant differential is −(x+a)ω. The map has no holomorphic extension at O: an extension would pull the holomorphic invariant differential back to a holomorphic differential at O, whereas −(x+a)ω has a double pole there with nonzero leading coefficient. Hence F_a is not an algebraic map of curves. This proof is valid for every a off the degeneracy circle; it makes no inference about algebraicity of j(Λ_a).

There is a useful precise CM restriction. For E/Qbar without CM and a∈Qbar, r_a cannot be algebraic: otherwise

\[
 \eta_2-r_a\eta_1-a\omega_2+a r_a\omega_1=0
\]

would contradict the Qbar-linear independence of the four elliptic periods and quasi-periods. The latter follows directly from Huber–Wüstholz Lemma15.6, printedpp136–138, applied to the reduced saturated motive[0→E], whose endomorphism algebra is Q. Its period matrix has four entries and no toric or lattice rows, so the lemma gives precisely their independence. In particular every full quotient lattice for algebraic a has non-CM complex torus in this case. This agrees with the actual quotient barE and gives no CM converse for H1.

For CM E and a∈Qbar, the quotient torus has CM exactly when a=h. To prove the nontrivial direction, choose τ algebraic imaginary quadratic and put U=ω_1, V=c barω_1=π/(U Imτ), b=h−a∈Qbar. Then μ_1=bU+V and μ_2=bτU+barτ V. The numbers U,V are Qbar-linearly independent: any dependence gives π=αU² with algebraic α, contrary to the proved algebraic independence of U and π (Chudnovsky, original ICM1978, Corollary2p343, already opened). A CM quotient has algebraic r_a, so

\[
 b(\tau-r_a)U+(\bar\tau-r_a)V=0
\]

forces r_a=barτ and b(τ−barτ)=0, hence a=h. The converse is Λ_h=c barΛ and conjugation preserves CM. This classification only concerns CM quotient tori; algebraic j for a non-CM quotient remains the exact arithmetic problem under investigation.

### 34.1 New primary search record

1. Michel Waldschmidt, *Schanuel Property for Elliptic and Quasi-Elliptic Functions*, Hardy–Ramanujan Journal48(2025),77–101, final primary PDF https://hrj.episciences.org/15601/pdf opened in full (25pages), webref turn213721813view1. Proposition2.1p78 is an almost-all specialization theorem for algebraically independent meromorphic functions; Theorem2.2p78 gives the functional independence of elliptic/quasi-elliptic functions; Corollary2.3p79 retains the almost-all quantifier. The actual finitely prescribed periods here are not shown to lie outside its exceptional set. Reference[BeWa26]p100 is explicitly a work in progress on further conjectures. No pointwise Katz conclusion is drawn.

2. Riccardo Tosi, *On the algebraic independence of periods of abelian varieties and their exponentials*, arXiv2309.02800v1,6September2023, full17page primary PDF https://arxiv.org/pdf/2309.02800 opened as turn136119115view0. Theorem1p2 imposes trdeg_Q Q(S)=1 and 2m+n>2g before giving a lower bound on a transcendence type. In genus1, retaining both de Rham period rows gives m=2,n=0 and the stated rank inequality, but no trdeg1 hypothesis has been obtained from algebraic h. The one-row quotient-period data alone have m=1,n=0 and give equality2m+n=2g, outside the strict inequality. No contradiction follows from the directly identified data.

3. K.G. Vasil'ev, *Algebraic independence of the periods of abelian integrals*, Mat.Zametki60(1996),681–691, DOI10.4213/mzm1881. Original Russian11page primary PDF opened through MathNet fulltext link https://www.mathnet.ru/php/getFT.phtml?jrnid=mzm&option_lang=eng&paperid=1881&what=fullt as turn977129316view0. Text extraction is corrupt; screenshot requests for printedpp681–682 returned image placeholders without usable image blocks, and direct local download returned HTTP403. Therefore the exact original theorem has NOT been independently read and is NOT invoked. Tosi's primary introductionp1 explicitly describes the antecedent as independence of at least two numbers among any g+1 rows; this is recorded as Tosi's description only.

4. Ehlen–Li–Schwagenscheidt current arXiv record https://arxiv.org/abs/2210.07341 reopened as turn908614903view0: latest version remains v2,11February2025, labeled final. The author research list https://lykpi.github.io/research.html was opened as turn908614903view1 and checked for later coefficient-converse work. Queries with recent-date filters returned the already audited CM direction and half-integral-weight period literature; no proved converse was located.

5. Alfes–Bruinier–Schwagenscheidt, *Harmonic weak Maass forms and periods II*, Math.Ann.391(2025),791–817, DOI10.1007/s00208-024-02927-4, publisher full text opened as turn908614903view2. Introduction§1 explicitly uses weights3/2−k with integral k≥1. The weight0 form attached to E would require k=3/2, so this direct substitution does not meet that parameter condition. No assertion is made that other constructions from the paper cannot be relevant.

6. Huber–Wüstholz Lemma15.6/Definition15.1 reopened in full indexed primary source https://arxiv.org/pdf/1805.10104 , refs turn478243586view0/1; original local PDF and text retained. Exact application above is independent of the quotient's differential scale, because its additional CM assumption makes r_a algebraic and hence supplies an actual linear relation with algebraic coefficients.

Queries recorded: “quasi-period lattice elliptic algebraic”; “second kind period lattice elliptic transcendence”; “quasi-periods modular invariant algebraic”; “quasiperiod lattice j-invariant”; “periods of the second kind algebraic independence”; “quasiperiods lattice isogenous”; “second kind period ratios algebraic elliptic”; and recent Ehlen/Li/Schwagenscheidt coefficient-converse queries. Known Katz/Grinspan/Sebbar/HW results resurfaced and were not counted as new results. The unsupported Stanford-UQ answer resurfaced and remains rejected for its missing de Rham-to-Betti transfer.

A.4.34 integration update: full draft retained at work/A4_34_draft.tex; exact symbolic determinant, oriented-area numerator, denominator and second-kind differential/period convention checked by work/code_elliptic/check_quotient_lattice.py, with output retained and both copied into output/RESEARCH_SA07/code. Huber–Wüstholz printedp136 was rendered and visually read to verify the Qbar coefficient field; image work/sources_elliptic/hw136.png. H1 remains unchanged.

7. Jones–Schmidt, *A Manin–Mumford Theorem for the Maximal Compact Subgroup of a Universal Vectorial Extension of a Product of Elliptic Curves*, IMRN2021(21),16205–16228, DOI10.1093/imrn/rnz207. Complete accepted author manuscript,23pages including repository cover, opened at https://pure.manchester.ac.uk/ws/portalfiles/portal/125978993/Maximal_compact_subgroup_IMRN_revision_4.pdf (turn113631040view0). Theorem1.1, printedp2, requires an algebraic subvariety V with dimV≤dimA; for an elliptic curve, an algebraic curve has finite intersection with the maximal compact subgroup. Theorems1.2–1.3 are onpp3–4; the actual isogeny and conjugate period matrices are onpp6–7. The present algebraic tangent line L_a exponentiates to a Zariski-dense analytic subgroup by A.4.15/A.4.32, so this construction does not produce the required algebraic curve V. This is a check of this particular substitution, not an assertion that other uses of that theorem cannot help.

8. Senthil Kumar K, *Algebraic independence of values of Weierstrass elliptic and zeta functions*, Proc.Edinburgh Math.Soc.69(4)(2026),1239–1271, DOI10.1017/S001309152610145X, final primary full HTML reopened at https://www.cambridge.org/core/journals/proceedings-of-the-edinburgh-mathematical-society/article/algebraic-independence-of-values-of-weierstrass-elliptic-and-zeta-functions/E91A8EEEB1F63536D95D1DE7D7DD47E2 (turn746810099view0). This is the same 2026 article already audited by root, not a new theorem discovery. The rank and transcendence-degree inputs remain as previously recorded; no new H1 inference.

## 35. The second-kind rank-one connection and the exact privileged-local-system test

**Proved route calculation, retained in work only before the07:55 review; root independently checked the p-curvature formula. No H1 movement and no new paper result asserted.**

Let K be a number field containing g2,g3,a and let U=E\{O}. On its trivial line bundle consider the algebraic connection

\[
 \nabla_a=d+(x+a)\omega.
\]

For the chosen cycles, its horizontal monodromy is

\[
 \rho_a(\gamma_i)
 =\exp\!\left(-\int_{\gamma_i}(x+a)\omega\right)
 =\exp(\eta_i-a\omega_i)=e^{\mu_i(a)}.
\]

The first equality is obtained by solving dy+(x+a)ωy=0 on the universal cover, and the second uses the actual convention ∫ξ=−η. The residue at O is zero, so the boundary monodromy is1. The connection has a genuine irregular pole there: (x+a)ω has a nonzero double-pole term, whereas changing a meromorphic rank-one frame adds dlog(f), which has at most a simple pole. Thus no meromorphic frame eliminates the double pole.

### 35.1 Exact reduction at every good prime

At a good prime of characteristic p>3 where a is integral, put δ=y∂x+(6x²−g2/2)∂y, the derivation dual to ω. All formulas are now in the rational function field of the reduced elliptic curve. With H=H_p and K=K_p from A.4.31,

\[
 \delta^p=H\delta,\qquad
 \delta^{p-1}x=Hx-K.
\]

Write f=x+a. The p-curvature is, by its definition,

\[
 \psi_p(\delta)
   =(\delta+f)^p-\nabla_{\delta^p}
   =(\delta+f)^p-H(\delta+f)
   =f^p+\delta^{p-1}f-Hf
   =(x+a)^p-K-aH.                                  \tag{35.1}
\]

Here is an elementary verification of the operator identity used in the middle equality. The commutator of δ+f with multiplication by any rational function b is multiplication by δb. In characteristic p, the identity ad(T)^p=ad(T^p) shows that (δ+f)^p−δ^p commutes with every multiplication operator. It is therefore multiplication by its value at1, namely (δ+f)^p(1). Over the universal integral differential polynomial ring, that value is the complete Bell polynomial

\[
 \sum_{\sum j m_j=p}
 \frac{p!}{\prod_j m_j!\,(j!)^{m_j}}
       \prod_j(\delta^{j-1}f)^{m_j}.
\]

Modulo p, every coefficient vanishes except the partitions m1=p and mp=1: in every other partition all j and all m_j are strictly less than p, so the denominator is prime to p while the numerator is divisible by p. The two surviving terms are f^p and δ^{p-1}f. This proves the identity, hence(35.1), without importing a stronger p-curvature theorem.

The right-hand side of(35.1) is nonzero for every such prime. Its x^p coefficient is1, whereas K and aH are constants; x is transcendental over the constant residue field of the elliptic function field. Consequently this specific connection never has vanishing p-curvature at a good prime p>3. This remains true for any algebraic value a=h and also for the known algebraic CM Hodge coefficients. The statement concerns the multiplicative rank-one connection; the separate additive foliation from A.4.31 has the previously computed p-closedness condition K+aH=0.

### 35.2 Exact Betti moduli and source theorem hypotheses

The abelianization of π1(U) is Z²; its boundary loop is the commutator of the two generators. Hence its rank-one character variety with boundary monodromy1 is exactly(C*)², via the two displayed monodromy values. It is smooth of dimension2 at every point. In particular no character in this variety is the unique point with its tangent-space dimension.

When Λ_a is full, this character has infinite image. Indeed, finite image would make both e^{μ_i(a)} roots of unity, so μ_i(a)∈2πi Q. Both generators would then lie on the same real line, contradicting the full-lattice condition. Thus the determinant of this rank-one character, which is the character itself, is not torsion. At a=h the lattice is always full, so this conclusion holds without assuming algebraicity of h.

The newly consulted primary source is Esnault–Groechenig, *The Grothendieck–Katz Conjecture for Privileged Local Systems*, full14-page author PDF at https://page.mi.fu-berlin.de/esnault/preprints/helene/156_privileged.pdf (opened in full; turn219215142view0; exact theorem/proof turn599195418view0/1). Definition2.2, printedp4, calls a local system privileged when its tangent-space dimension distinguishes it from every other point of the relevant Betti moduli space; the optional fixed determinant is required to be torsion. Theorem3.1, printedp7, proves the p-curvature conjecture for such systems with quasi-unipotent boundary monodromy. Its proof, printedp11, explicitly starts with vanishing p-curvature almost everywhere.

For the concrete map a↦∇_a↦ρ_a, the preceding computations supply neither of those hypotheses: the unrestricted Betti point is not privileged; fixing a torsion determinant excludes ρ_h; and(35.1) directly proves nonvanishing p-curvature. This completely checks this substitution, without asserting any obstruction to every possible construction from that theorem. The arithmetic relation for the actual non-CM Hodge coefficient remains unresolved.

Queries checked in this continuation include “quasiperiods algebraic lattice j”, “second kind period lattice elliptic algebraic j-invariant”, “Katz Hodge splitting transcendence”, “real-normalized differentials transcendence”, and recent quasi-period algebraic-independence searches. The already audited Kumar2026 theorem and unsupported UQ answer were not counted as new movement.

## 36. Real-normalized integral-period forms: the exact genus-one map

**A proved calculation for a newly opened source route; work note only. No H1 movement.** The complete primary final chapter Grushevsky–Krichever, *Real-Normalized Differentials and the Elliptic Calogero-Moser System*, Abel Symposia10(2015),123–137, DOI10.1007/978-3-319-20337-9_6, was opened at https://www.math.columbia.edu/department/krichever/pdfs/2015-2019/2015-RNDATECMS.pdf (full15pages, turn261272730view0). Definition7p127 specifies two independent second-kind differentials with integer periods. Equations(1)–(2)p128 cancel their principal parts and integrate the resulting holomorphic differential to an elliptic curve. Theorem6p129 identifies the resulting loci with spectral curves. We compute this map in genus one.

Put D=2πi=η1ω2−η2ω1. The two differentials

\[
 \Phi_1=\frac{-\eta_2\omega-\omega_2\xi}{D},
 \qquad
 \Phi_2=\frac{\eta_1\omega+\omega_1\xi}{D}
\]

have period rows(1,0) and(0,1), respectively, by direct multiplication with the already established period matrix. They generate the entire lattice of integer-period differentials in H0(E,Ω(2O)): this space has complex dimension2, the displayed period matrix is invertible, and therefore every integral period row has the corresponding unique integral linear combination of Φ1,Φ2. In particular the construction exists for every complex elliptic curve, independently of any algebraicity of h.

Their principal parts are determined by the coefficients of ξ. Their ratio is

\[
 q=\frac{\omega_1}{-\omega_2}=-\frac1\tau\in\mathfrak H.
\]

Cancelling principal parts gives exactly

\[
 \Phi_2-q\Phi_1=\frac{\omega}{\omega_2}.
\]

Consequently the source's integrated map is

\[
 E^{an}=\mathbb C/\Lambda\longrightarrow
 \mathbb C/(\mathbb Z+q\mathbb Z),\qquad
 [u]\longmapsto[u/\omega_2].
\]

It is an isomorphism: multiplication by1/ω2 carries Λ onto
(ω1/ω2)Z+Z=Z+qZ. In particular its degree is1, proved directly by the lattice equality. Thus this specific genus-one construction returns the original elliptic curve's isomorphism class. The differential coefficients explicitly retain periods divided by2πi; the construction supplies no algebraicity assertion for those coefficients or for h.

For comparison within the same differential space, the unique real-normalized forms with principal parts du/u² and i du/u² are

\[
 \Psi=\xi+(h-c)\omega,\qquad
 \Psi'=i\bigl(\xi+(h+c)\omega\bigr).
\]

Their periods are −2c Re(ω_i) and −2c Im(ω_i), respectively, hence real. Uniqueness follows because a holomorphic differential bω with real periods has bω1,bω2 real, forcing b=0 since Imτ>0. If both these forms had algebraic coefficients in the algebraic basis(ω,ξ), then h−c and h+c would both be algebraic, hence h and c would both be algebraic, contradicting A.4.33. In particular the already proved algebraicity of a CM h does not make this pair algebraic. This is an explicit coefficient calculation, not a claim about every possible application of the source's geometric method.

Separate source status: the final publisher page of Guy Diaz's Ramanujan Journal4(2000),157–199 survey, DOI10.1023/A:1009879120323, was opened (turn190763008view0). It provides metadata, abstract and references only, explicitly subscription preview. The publisher PDF endpoint was inaccessible (turn190763008view1). Its exact theorems have not been read and are not invoked.

## 37. The theta-jet torsor and the exact Hodge jet

**New primary source, exact map verified; work note only. H1 remains unresolved.** Kenz Kallal and Akshay Venkatesh, *Algebraic theory of indefinite theta functions*, complete114-page author draft dated9October2026, was opened at https://web.math.princeton.edu/~kk2703/KV_indefinite_theta.pdf and downloaded as `work/sources_elliptic/kallal_venkatesh2026.pdf` with corresponding extracted text. Exact opened references are turn222464851view0, turn389308362view0 and turn560530293view0–3. The applicable construction assumes an abelian scheme and a symmetric rigidified nondegenerate line bundle whose polarization induces an isomorphism on Lie algebras. Over characteristic zero it identifies normalized symmetric jets modulo I^3 with Lagrangian splittings. The source's precise jet convention is I^2/I^3 and O/I^3, printedpp49–50. LemmaIIb.4, equations(IIb.5)–(IIb.6), pp50–51, gives the quadratic change formula. PropositionIIb.5, pp52–53, shows that the resulting normalized heat connection is independent of the chosen jet. TheoremIIIb.6, p79, identifies its monodromy with the finite Weil representation. We compute the actual jet in our fixed algebraic elliptic basis.

### 37.1 Explicit construction over the algebraic elliptic curve

Fix a nonzero point P of order2, put e=x(P), and choose u0 with P=[u0]. Then 2u0 belongs to Λ and e=wp(u0) is algebraic. Enlarge k to contain P. Let L=O_E(P), with its symmetric structure and rigidification at O chosen so that its canonical section s=1 has value1 there. Since P differs from O, this section is nonvanishing near O. The formal coordinate u obtained by integrating ω has algebraic coefficients and satisfies [-1]^*u=−u. Hence every normalized symmetric second jet has the unique form

\[
 s_b=(1+b u^2)s\pmod {I^3}.
\]

It is defined over k exactly when b belongs to k. In dimension one every complement of F^1 is Lagrangian.

Here is a direct computation of the source's torsor map, including its sign. Write the infinitesimal translating point as ε in the u-coordinate, with ε²=0. Its image under the polarization defined by L is

\[
 N_\epsilon=T_\epsilon^*L\otimes L^{-1}
       =\mathcal O_E([P-\epsilon]-[P]).
\]

Near P use w=u−u0. A regular nonvanishing local generator of Nε is w/(w+ε)=1−ε/w. Relative to its rational section1, write a connection as ∇(1)=εΩ. Regularity at P requires Ω to have principal part −dw/w²; regularity elsewhere and the source's normalization at O require Ω(O)=0. The unique such second-kind differential is

\[
 \Omega=-(\wp(u-u_0)-e)\,du
       =-\frac{3e^2-g_2/4}{x-e}\,\omega.             \tag{37.1}
\]

For the last equality use the Weierstrass addition formula and y(P)=0:

\[
 \wp(u-u_0)=-x-e+\frac{y^2}{4(x-e)^2}
           =e+\frac{3e^2-g_2/4}{x-e}.
\]

The numerator is nonzero since the cubic has simple roots. At P, x−e=(3e²−g2/4)w²+O(w^4), which verifies the stated principal part. At O the rational expression vanishes. The difference of any two candidates is a holomorphic differential vanishing at O, hence zero. Translation on E acts trivially on H1, so integration of the translated ξ gives the same periods as ξ; the de Rham comparison is injective and therefore

\[
 [\Omega]=-\xi+e\omega.
\]

This is the image of the tangent vector dual to ω under the jet-induced right section, with the quotient coordinate given by the polarization map [L] in the source.

Multiplying the jet by1+b u² modifies its translated ratio to first order by1+2b εu. Its differential at O is2b εdu. Thus the connection normalized to annihilate this ratio at O changes by−2b εdu. Consequently the exact right-section formula in our basis is

\[
 \phi(s_b)(\partial_u)=-\xi+(e-2b)\omega.          \tag{37.2}
\]

This proves the rank-one version of the source's quadratic-action formula directly, independently of the symbolic conventions for symmetric tensors. The map b↦the displayed vector is affine with nonzero slope and therefore identifies all normalized symmetric2-jets with all complements of F^1.

### 37.2 Matching the actual Hodge splitting

The image in(37.2) is H01=C(ξ+hω) exactly when

\[
 b_H=\frac{e+h}{2}.                              \tag{37.3}
\]

The proportionality scalar must be−1 by the ξ coefficient. Thus the exact coefficient fields satisfy k(b_H)=k(h); algebraicity of the actual Hodge jet is precisely the same arithmetic condition as algebraicity of h.

The Gaussian normalization can also be checked directly. Define

\[
 S(u)=\frac{\sigma(u+u_0)}{\sigma(u_0)}
          e^{-\zeta(u_0)u},\qquad
 R_h(u)=e^{-hu^2/2}S(u).
\]

Then S(0)=1, S'(0)=0, and(log S)''(0)=−wp(u0)=−e. All Taylor coefficients of S are algebraic: its logarithmic derivative has value0 and derivative−wp(u+u0), whose Taylor coefficients follow algebraically from the Weierstrass differential equation at the algebraic point P; integration and exponentiation preserve the algebraic coefficient field. For an order-two point, ζ(u0)=η_(2u0)/2, so this S is the normalized torsion translate already used in A.4.26. Hence

\[
 R_h(u)=1-\frac{e+h}{2}u^2+O(u^3),\qquad
 R_h(u)^{-1}=1+\frac{e+h}{2}u^2+O(u^3).
\]

The actual Hodge jet is the inverse reduced-theta jet times s, in agreement with(37.3). This inverse is important for the sign: the global algebraic section and the local normalized frame have reciprocal expressions.

### 37.3 What the finite heat monodromy does at this jet

The normalized heat operator of PropositionIIb.5 is the same for every s_b. Its defining normalization evaluates the operator at O and compares it with the connection induced by projecting Gauss–Manin along im φ(s_b). The source proves that the change−2bω in(37.2) is exactly cancelled by the second-order operator applied to the quadratic change b u²; this is equations(IIb.9)–(IIb.10), pp52–53. Therefore specializing that finite-monodromy connection at the actual jet neither singles out b_H nor imposes a further condition on b_H. The exact additional arithmetic datum in this substitution remains(37.3). No statement excluding other uses of the source is asserted.

The source also gives an explicit Jacobi-curve computation in §IIIc, pp83–86: for y²=(1−x²)(1−k²x²), identity(1,0), and P=(−1/k,0), its jet-induced complement is spanned by[dx/y]−k[x²dx/y]. Those pages and the dual-number calculation were read. The short-Weierstrass calculation above supplies the precise comparison needed here, rather than transferring that complement to H01 without checking its coefficient.

Search record: the source was found through the author's public draft link and the official5November2026 UCSD seminar page. Further queries for the literal Katz question number, algebraic Hodge splittings, second-kind period lattices, and almost-holomorphic modular transcendence returned the already checked Katz, Spence, Kumar, Fonseca and Sebbar sources, plus unrelated or unsupported secondary material. Those repeated hits were not counted as advances. A fresh Bakker–Pila–Tsimerman2026 period-map-derivative source was referred to the generation agent for independent inspection; no theorem from it is used here.

## 38. Torsion evaluation, its corrected Galois action, and the exact descent equation

**New primary-source route, with two author-issued corrections checked. Work note only; the actual nonzero algebraic-h gate is unchanged.**

The complete373-page September1999 primary manuscript of Shinichi Mochizuki, *The Hodge-Arakelov Theory of Elliptic Curves: Global Discretization of Local Hodge Theories*, was opened and downloaded. The characteristic-zero evaluation theorem is Introduction, Theorem A_simple, printedp5: for L=O_E(d[η]), with η of order not dividing d, restriction to E†[d] identifies the sections of torsorial degree less than d with the d²-dimensional torsion-value space. ChapterIII, Definition3.2pp63–64 defines the compact real section; ChapterVII, Proposition4.1p245 identifies its connection interpretation, and Theorem4.5p249 gives the orthogonal differential-operator description. ChapterIX, Theorem3.3p364 and Definition3.4p365 require the correction below.

The exact downloaded source is work/sources_elliptic/mochizuki1999_hodge_arakelov.pdf, with extracted text. Opened web references include turn559060740view0, turn723623039view0–2 and turn436481786view3–4. The torsion-evaluation theorem uses the actual compact section κ([u])=[(u,hu+c conjugate(u))] already computed in A.4.14 and A.4.33, because this section is the real span of the period lattice and contains all torsion lifts. The expression follows directly from η_λ=hλ+c conjugate(λ); it is not a new normalization.

### 38.1 Corrected integral object and corrected groupoid action

Two later primary manuscripts were opened in full. The May2000 paper *Connections and Related Integral Structures on the Universal Extension of an Elliptic Curve*, 80pages, §9pp76–79, corrects the integral object in the1999 comparison theorem. Its Theorem9.2p79 uses the pushed-out Hodge torsor associated to O_E(η), with its étale integral structure, and the torsorial-degree filtration. The characteristic-zero evaluation space above is unchanged.

The July2000 paper *The Galois-Theoretic Kodaira-Spencer Morphism of an Elliptic Curve*, 28pages, Definition1.1pp3–4 and Propositions1.2–1.3pp4–5, separates the actions on torsion points, coefficients and their diagonal combination. Corollary1.6p7 corrects the1999 ChapterIX claim: the acting object is the conjugation-twisted fundamental groupoid on the indicated étale stack, and the denominator divisor V(4) is replaced by V(d). This correction is used here.

The exact primary URLs are:

- https://www.kurims.kyoto-u.ac.jp/~motizuki/Connections%20and%20Related%20Structures%20on%20the%20Universal%20Extension%20of%20an%20Elliptic%20Curve.PDF
- https://www.kurims.kyoto-u.ac.jp/~motizuki/The%20Galois-Theoretic%20Kodaira-Spencer%20Morphism%20of%20an%20Elliptic%20Curve.pdf

Exact opened web references: turn641689295view0 and turn329932922view2 for the integral correction; turn939983527view0 for Definition1.1, Propositions1.2–1.3 and Corollary1.6. Local copies are mochizuki2000_connections.pdf and mochizuki2000_galois_kodaira_spencer.pdf in work/sources_elliptic, with extracted text.

### 38.2 The precise coefficient equation after torsion evaluation

Here is a direct linear-algebra calculation of the descent map at a number-field point. Let K contain the elliptic curve, η and every chosen algebraic coefficient. Write

\[
 V=\Gamma(E^\dagger,L)^{<d},\qquad T=E^\dagger[d],
 \qquad \Xi:V\longrightarrow \Gamma(T,L|_T).
\]

The canonical section1 of L=O_E(d[η]) is nonzero at every point of T, because η is not d-torsion. It therefore gives a K-defined trivialization of L|_T. Choose a finite Galois extension K_d/K splitting T and a K-basis v_1,...,v_{d²} of V. In the delta-function basis indexed by t∈T(K_d), the evaluation matrix is

\[
 B_{t,j}=(v_j/1)(t)\in K_d,\qquad B\in\operatorname{GL}_{d^2}(K_d).
\]

For σ∈Gal(K_d/K), define the permutation matrix P_σ by
\((P_\sigma f)(t)=f(\sigma^{-1}t)\).
Since each v_j is defined over K, evaluation satisfies

\[
 \sigma(B)=P_\sigma^{-1}B.                         \tag{38.1}
\]

Indeed, its (t,j)-entry is σ((v_j/1)(t))=(v_j/1)(σt), which is the corresponding entry of P_σ^{-1}B. Thus the diagonal semilinear action on the value space is \(f\mapsto P_\sigma\sigma(f)\), and it fixes every evaluated K-section.

For every \(A\in\operatorname{End}_K(V)\), its transported matrix \(Q=BAB^{-1}\) consequently satisfies

\[
 \sigma(Q)=P_\sigma^{-1}QP_\sigma,\qquad
 P_\sigma\sigma(Q)P_\sigma^{-1}=Q.                \tag{38.2}
\]

Equation(38.2) is the exact consequence of K-algebraicity. Commutation with the linear permutation action is the additional equality

\[
 [Q,P_\sigma]=0,
\]

which, by(38.2), is equivalent to σ(Q)=Q in these value coordinates. Thus the required replacement can be tested as an explicit matrix equality.

The replacement does not hold for arbitrary algebraic operators, as this exact finite-étale example shows. Take \(T=\operatorname{Spec}\mathbb Q(\sqrt2)\), \(V=\mathbb Q(\sqrt2)\), and A multiplication by √2. In the rational basis(1,√2), A has matrix \(\bigl(\begin{smallmatrix}0&2\\1&0\end{smallmatrix}\bigr)\). Evaluation at the two embeddings gives

\[
 B=\begin{pmatrix}1&\sqrt2\\1&-\sqrt2\end{pmatrix},
 \quad Q=\begin{pmatrix}\sqrt2&0\\0&-\sqrt2\end{pmatrix},
 \quad P=\begin{pmatrix}0&1\\1&0\end{pmatrix}.
\]

Then σ(Q)=−Q and PQP^{-1}=−Q, so the semilinear identity holds while \(PQ\ne QP\). This verifies the precise descent issue without making any claim about all possible applications of the source.

The actual h-algebraicity assumption gives the K-defined two-jet computed in§37 and the K-defined de Rham projector of A.4.11. This continuation has not constructed from them an operator on V with the additional permutation-commutation equation. Nor does the source's corrected comparison assertion identify σh with the actual Hodge coefficient at every conjugate elliptic curve. These are exact outstanding bridges in the proposed use of torsion evaluation; no exclusion of other routes is asserted.

### 38.3 Source search and scope

The correction was located after directly checking descent of the1999 claimed action, then searching the author's later papers. The official paper list links both corrected manuscripts and the2012 one-page survey comments; those comments were also opened. The original characteristic-zero comparison, the compact-section map, the finite-dimensional evaluation matrix, and the corrected semilinear equation are retained. No claim from an unrelated later theory is used. The repeated Fonseca2020 final-paper check and the two-isogeny formula h′=2h+x(P), which reduces to the existing zero-value theorem, are not counted as new results or H1 movement.

Exact finite certificate for §38.2: work/code_elliptic/check_torsion_evaluation.py, with adjacent .out and .json. All nine exact checks passed; the metadata records inputs, SymPy1.14.0, UTC start and elapsed time0.227786seconds. Production TeX and production code were not modified.


## 39. The modular-foliation test on the exact shifted Weierstrass point

**Work-only source application. H1 remains the same nonzero algebraic-h question.**

The full primary manuscript of Hossein Movasati, *On elliptic modular foliations*, arXiv0806.3926v1, 24June2008,20pages, was opened. Exact locators in this consulted version are Theorem2p3; Theorem3 and Corollary1pp13–14; Corollary2p14; Theorem4 and its proofp15. Theorem2 allows at most one algebraic point on a nonsingular leaf of the indicated Ramanujan foliation, and excludes algebraic points where the distinguished nonzero differential has a zero integral over a nonzero integral cycle. Corollary2 identifies two simple algebraic abelian varieties carrying nonzero algebraic de Rham classes with the same integral period module by an isomorphism pulling one class to the other. Web primary references: turn736115119view0/3 and turn844842651view0. The published article has a different pagination; the displayed locators are for the opened arXiv version.

### 39.1 The actual Hodge point in the source's chart

The source family is

\[
 E^t:\quad Y^2=4(X-t_1)^3-t_2(X-t_1)-t_3,
 \qquad \alpha_t=X\,dX/Y.
\]

For every scalar a, set t=(a,g2,g3) and use the exact isomorphism

\[
 f_a:E\longrightarrow E^t,\qquad (x,y)\longmapsto (x+a,y).
\]

Then f_a^*(dX/Y)=omega and f_a^*alpha_t=xi+a omega. The latter class has xi coefficient1, so it is nonzero and lies outside the holomorphic subspace. The period row is

\[
 \left(\int_{\gamma_1}f_a^*\alpha_t,
             \int_{\gamma_2}f_a^*\alpha_t\right)
 =(-\eta_1+a\omega_1,-\eta_2+a\omega_2).
\]

At the actual a=h, this equals -c(conjugate(omega1),conjugate(omega2)). For an integral cycle m gamma1+n gamma2, the value is

\[
 -c\,\overline{m\omega_1+n\omega_2},
\]

which is nonzero whenever (m,n) differs from(0,0), because the original period generators are real-linearly independent. Thus the zero-period condition in Theorem2(2) does not occur at this point. Algebraicity of h would make t algebraic; Theorem2(1) bounds the number of algebraic points on its leaf by one. This substitution supplies one candidate point, without producing a second point on the same leaf. In particular, no second point is obtained by changing to a curve with the same j-invariant unless the differential and its entire unscaled period module are checked.

### 39.2 What the raw quotient invariants would imply

There is a direct consequence for the exact period lattices from A.4.34. Fix a in Qbar and suppose Lambda_a=Z(eta1-a omega1)+Z(eta2-a omega2) is a full lattice, retaining the degeneracy-circle qualification of that result. Its raw lattice invariants cannot both belong to Qbar.

Indeed, if both invariants belonged to Qbar, the short Weierstrass curve F attached to Lambda_a would be an elliptic curve over Qbar and its holomorphic differential dz would have integral period module Lambda_a. On E, the algebraic class -xi-a omega has exactly the same period module. Corollary2 therefore gives an algebraic isomorphism b:E to F with b^*[dz]=-xi-a omega. The pullback of a regular differential under an isomorphism is regular, whereas this latter class has nonzero xi coefficient. Since (omega,xi) is a de Rham basis and F1=Qbar omega, these two conclusions contradict one another. This proves the assertion. Every curve here is simple, both classes are nonzero, and equality is of the full Z-period modules; all the hypotheses of the cited corollary are accounted for.

Consequently, whenever a rescaling z to z/d makes the quotient's short-Weierstrass invariants algebraic, the scalar d must be transcendental. An algebraic nonzero d would make the raw invariants algebraic as well, by the exact rules

\[
 g_2(d^{-1}\Lambda_a)=d^4g_2(\Lambda_a),\qquad
 g_3(d^{-1}\Lambda_a)=d^6g_3(\Lambda_a).
\]

At the actual a=h, the known rescaling is d=c, with Lambda_h=c conjugate(Lambda); it yields the algebraic conjugate model. Thus this application confirms, for every algebraic a, the scalar obstruction already explicit for actual h in A.4.33. It does not exclude the algebraicity of j(Lambda_a), which is unchanged by the rescaling. In particular it does not settle the actual non-CM algebraic-j quotient.

### 39.3 Further exact source checks retained without an arithmetic inference

The complete final18-page paper Movasati, *On elliptic modular foliations, II*, Moscow Mathematical Journal22(1)(2022),103–120, was opened at https://w3.impa.br/~hossein/myarticles/2021-EMFII.pdf. Its Theorem1p105 classifies algebraic leaves of the specified self-joined foliation by modular curves. No algebraic leaf containing the point of39.1 has been constructed in this continuation, so this classification supplies no additional H1 conclusion. Opened reference turn736115119view1.

The complete24-page primary paper Shiga–Suzuki–Wolfart, *Arithmetic properties of Schwarz maps*, Kyushu Journal of Mathematics63(2009),167–190, was opened at https://www.jstage.jst.go.jp/article/kyushujm/63/1/63_1_167/_pdf. Section1.4p171 defines the projective period value; Theorem2.1p173 applies to the explicitly stated Appell–Lauricella differentials and assumes algebraicity of that projective value. In the actual rank-two quotient considered here, the projective coordinate is (eta2-h omega2)/(eta1-h omega1)=conjugate(tau), which is transcendental for a non-CM algebraic E by the opened Schneider theorem. Algebraicity of j of this ratio is a different explicit equation; no transformation supplying the theorem's projective-algebraicity hypothesis has been obtained. This is only an applicability check of that exact statement, without a claim excluding other uses of the paper. Opened primary reference turn171922731view0, with the period theorem separately confirmed in turn294322452search4.

Search record: queries for second-kind period lattices, algebraic analytic quotients of universal extensions, algebraic intrinsic second-kind differentials, and recent harmonic-Maass algebraicity returned the above primary papers and previously retained sources. The repeated UQ/rStation/openmaths material was not used as a theorem source. The Choi–Lim Schneider–Siegel Hecke-orbit-values paper was located by metadata; its theorem has not yet been invoked.

Section39 integration update: A.4.35 appended to the production elliptic section after root proof/source audit. Six exact finite chart and scaling identities checked by work/code_elliptic/check_raw_lattice_invariants.py; adjacent .out/.json retain all inputs and timing. The arbitrary algebraic-model comparison is explicitly [z] to [z/d], with differential dz/d. Canonical proof/source/computation check rows are retained. H1 unchanged.

## 40. The level37 third-kind period route and its exact relation to h

**Work-only arithmetic route. The relevant new primary period formula is applied below through its actual differential and elliptic point. It does not change H1.**

### 40.1 Exact algebraic twist and the two coefficients

Write E_+:Y²=4u³−4u+1 and E_*:y²=4x³−4x−1. The level37 minimal model v²+v=u³−u maps to E_+ by Y=2v+1. The Q(i)-isomorphism

\[
 f:E_*\longrightarrow E_+,\qquad (x,y)\longmapsto(-x,iy)
\]

satisfies f*omega_+=i omega_* and f*xi_+=−i xi_*. Consequently

\[
 h_+=-h_*,\qquad c_+=c_*,\qquad \Lambda_+=i\Lambda_*.
\]

Here the equality of c follows from equality of the lattice areas under multiplication by i, and the equality of h follows by pulling back xi_++h_+omega_+. The Weierstrass zeta scaling gives zeta_+(iz)=−i zeta_*(z).

For the level37 normalized newform, f37=q−2q²−3q³+O(q⁴), its Eichler integral is epsilon=q−q²−q³+O(q⁴). Hence [q](zeta_+(epsilon)−h_+epsilon)=2−h_+=2+h_*. This makes the sign in the earlier level37 example explicit: the h in the level37 equation is h_+, while the actual positive h in the fixed E_* gate is h_*.

### 40.2 From a third-kind differential to a compact-section value

For a point P=[v]=(e,y_P) on a short Weierstrass curve, with P different from O and from a point of order2, put

\[
 \beta_P=\frac{y_P}{2(x-e)}\,\omega.
\]

Its residues at P and −P are 1/2 and −1/2. The zeta addition formula gives the exact identity

\[
 \beta_P=
 \tfrac12\bigl(\zeta(u-v)-\zeta(u+v)+2\zeta(v)\bigr)\,du.
                                                        \tag{40.1}
\]

One can verify this addition formula by subtracting the two standard zeta addition identities: the terms zeta(u) cancel and the remaining rational term is wp'(v)/(wp(u)−wp(v)). Equivalently both sides have the displayed residues and agree at u=0. A local primitive is

\[
 \tfrac12\log\frac{\sigma(u-v)}{\sigma(u+v)}+\zeta(v)u.
\]

The sigma quasi-period law therefore gives, for any lift of a lattice cycle avoiding the poles,

\[
 \int_{\gamma_i}\beta_P
   =\zeta(v)\omega_i-\eta_i v+\pi i n_i,
 \qquad n_i\in\mathbb Z.                              \tag{40.2}
\]

Changing the avoidance paths only changes the last term; thus the real part is unambiguous.

Now let E=E_+ and P be real. Choose a positive real lattice period omega_R. Then eta_R=(h_++c_+)omega_R. Define the lattice-invariant function

\[
 W_+(P)=\zeta_+(v)-h_+v-c_+\bar v.                    \tag{40.3}
\]

It is invariant under v to v+lambda by eta_lambda=h_+lambda+c_+bar(lambda). It is real on E_+(R): complex conjugation commutes with zeta and preserves the lattice, so W_+(bar v)=overline(W_+(v)); realness of P says bar v and v represent the same point. Consequently

\[
 \frac{\operatorname{Re}\int_{\gamma_R}\beta_P}{\omega_R}
 =\operatorname{Re}\zeta_+(v)-(h_++c_+)\operatorname{Re}v
 =W_+(P).                                             \tag{40.4}
\]

This proof includes the nonidentity real component. Its parameter may have an imaginary half-period; no assertion that v is real is used. For integration over the full real locus with the positive differential orientation, both components have the same real-period ratio. Their cycles differ, after avoiding the poles, only by homologous cycles and small residue loops; the latter contribute purely imaginary multiples of pi. Thus (40.4) also holds with numerator Re integral over E_+(R) and denominator integral of omega_+ over E_+(R).

The newly opened primary paper is Jan Hendrik Bruinier, *Harmonic Maass forms and periods*, complete22-page author manuscript dated14January2013, https://www.mathematik.tu-darmstadt.de/media/algebra/homepages/bruinier/publikationen/maassper8.pdf. Introduction p3 explicitly gives, for the specified weight1/2 harmonic Maass form of level4*37,

\[
 c^+(1)=
 \frac{\operatorname{Re}\int_{E_+(\mathbb R)}-\omega_+/(2u)}
      {\int_{E_+(\mathbb R)}\omega_+}.
\]

The general formulas are Theorem1.1p4 and Theorem1.2p5; the canonical third-kind differential theorem is Theorem2.1p6. The published article is Math.Ann.357(2013),1363–1387; all these page locators refer to the opened author manuscript. The exact substitution P=(0,−1) makes beta_P=−omega_+/(2u), and (40.4) proves

\[
 c^+(1)=W_+(0,-1)=-iW_*(0,i),                       \tag{40.5}
\]

where the last identity follows from f and zeta scaling. The consulted source's numerical value, approximately−0.28176178499, is not used in the proof.

### 40.3 Actual transcendence at this point and the unproved bridge

The point (0,−1) is nontorsion. In the minimal model it is (u,v)=(0,−1). The good reductions at2 and3 have orders5 and7, respectively: for each x mod2 both y solve y²+y=x³−x; for every x mod3 exactly two y solve it. The discriminant is37. Reduction is injective on torsion of order prime to the residue characteristic, since the kernel is a pro-p formal group. The2-primary part would inject into the order7 group at3, the3-primary part into the order5 group at2, and every other primary part into both; all are trivial. Thus E_+(Q) has no nonzero torsion, and the displayed nonidentity rational point is nontorsion.

In the algebraic universal-extension chart already constructed in A.4.14, the compact-section lift of P has fiber coordinate W_+(P). Bost–Kunnemann's proved algebraic-compact-point criterion used there therefore makes W_+(P) transcendental for this algebraic nontorsion point: if W_+(P) were algebraic, the whole compact lift would be an algebraic point, hence torsion, and so would its projection P. This recovers the known transcendence of the half-integral coefficient in (40.5) through the exact map. The value depends on zeta(v), the elliptic logarithm v and the area scalar c, not only on h; (40.3) displays each term.

The theta-lift connection was also checked in the complete final31-page Alfes–Griffin–Ono–Rolen2015 publisher PDF, https://link.springer.com/content/pdf/10.1007/s40993-015-0026-2.pdf. Definition(4.1) and Theorem4.5, finalpp21–22, express each positive-index lift coefficient as the stated weighted difference of traces of the values F(D_lambda) of the full harmonic form at CM points. The formula evaluates the full function. It is not a coefficientwise algebraic operation on its holomorphic q-series. For the Weierstrass input those full values have precisely the form zeta(epsilon(tau))−h_+epsilon(tau)−c_+conjugate(epsilon(tau)), with the specified algebraic modular correction and normalization retained. Thus to infer algebraicity of the lift coefficient from algebraicity of h one would still have to prove algebraicity of these actual value traces. Neither the coefficient identity2−h_+=2+h_* nor the trace formula proves that additional statement. No claim excluding another use of the lift is made.

### 40.4 Exact scope of the Hecke-orbit-values lead

The complete primary Choi–Lim arXiv1812.01770v1,5December2018,14pages, was opened at https://arxiv.org/pdf/1812.01770. Definition1.1p2 defines an arithmetic harmonic form using principal parts; Theorems1.2–1.5p3 concern special values on Hecke orbits. Theorem1.2 includes a regularized Petersson period in its algebraicity conclusion. Theorem1.3 additionally requires nonzero Petersson pairing (g,xi_0(F)) for every cusp Hecke eigenform g. That additional hypothesis fails for an input with a single level37 newform shadow.

Here is the precise verification. The action of PSL2(Z) on P1(F37) gives index38. The order2 generator has two fixed points, solving x²+1=0, and the order3 generator has two fixed points, solving x²+x+1=0. The parabolic generator has two cycles, of lengths1 and37. The corresponding ramification contributions for X0(37) to X(1) are18,24 and36. Riemann–Hurwitz gives2g−2=−2*38+18+24+36=2, hence g=2. The space S2 has dimension2. The commuting self-adjoint Hecke operators preserve the orthogonal complement of the chosen newform, and its one-dimensional complement contains a Hecke eigenform g orthogonal to that shadow. This proves that the displayed all-eigenform-pairing assumption is not met in the proposed substitution. This observation concerns the consulted preprint statement and our input; it makes no assertion about an unobtained final-version formulation.

Opened web references: Bruinier turn881710214view2, turn242416843view5 and turn775075917view0; AGOR final turn775075917view1 and turn508122073view0; Choi–Lim turn881710214view0 and turn242416843view2–3. The complete original2008/2009 Bruinier–Ono–Rhoades corrigendum audit remains in the earlier notes. No deleted or corrected claim is reintroduced. H1 remains unchanged.

Section40 finite certificate: work/code_elliptic/check_third_kind_route.py, .out and .json; eleven exact checks pass. The two new primary manuscripts were downloaded and extracted as work/sources_elliptic/choi_lim2018.pdf/.txt and bruinier2013_periods.pdf/.txt. The A.4.35 raw-lattice certificate was also rerun with a,g2,g3 unrestricted, including zero; only the division parameters d and lambda are assumed nonzero.

## 41. The exact row quantifier in Vasil'ev's period theorem

The earlier source-access limitation is now resolved. The original Russian11-page PDF of K.G.Vasil'ev, *On the algebraic independence of the periods of abelian integrals*, MatematicheskieZametki60(5)(1996),681–691, was downloaded from the primary MathNet archive. Its extracted web text remains garbled, but the local rendering of printedpp681–682 was visually read successfully. The local PDF is work/sources_elliptic/vasiliev1996.pdf and the two inspected images are vasiliev1996-01.png and -02.png. The English translated article was not obtained; its publisher page was opened only for metadata.

The introduction on p681 takes an algebraic curve of genusg and a nondegenerate2g-by-2g matrix Omega of periods of2g algebraically defined second-kind differentials on2g closed cycles. Its unnumbered Theorem on p682 states: any g+1 distinct rows of Omega, taken together, contain two algebraically independent numbers. The quantifier is g+1 rows; it does not say that every single differential has two algebraically independent periods. The preceding p681 explicitly recalls Chudnovsky's elliptic bound and the CM independence of omega1 and pi.

For genus1 the theorem uses both rows of the full period matrix. A change from the algebraic basis(omega,xi) to(omega,xi+a omega), for any algebraic a, is the invertible algebraic matrix [[1,0],[a,1]]. Thus it preserves the theorem's algebraic-differential and nondegeneracy hypotheses. At the actual Hodge value this would be the matrix with rows(omega1,omega2) and(−c baromega1,−c baromega2). The conclusion remains the existence of two algebraically independent entries somewhere in that two-row matrix. It does not isolate h or a single row. The already proved dimension and matrix calculation in A.4.12 gives the exact comparison locus for the putative algebraic-h relation; no stronger period relation theorem is obtained from this row-bound substitution.

Primary records: https://www.mathnet.ru/php/archive.phtml?jrnid=mzm&option_lang=eng&paperid=1881&wshow=paper, https://www.mathnet.ru/php/getFT.phtml?jrnid=mzm&option_lang=eng&paperid=1881&what=fullt. Opened references turn686641440view0, turn496628701view0. The two primary pages were read from local images after standard direct retrieval succeeded; the web screenshot response only returned placeholders and is not claimed as the visual source. English publisher metadata: https://link.springer.com/article/10.1007/BF02309165, turn686641440view1. No theorem from the unread English full text is claimed. H1 unchanged.

## 42. Normalized shifted periods and the quotient with algebraic j

### 42.1 An exact normalized-period consequence

For every elliptic curve with algebraic invariants, every nonzero lattice period w, and every algebraic a, the two numbers

\[
 X=w/\pi,\qquad Y_a=(\eta(w)-aw)/\pi
 \tag{42.1}
\]

are algebraically independent over Qbar. Here eta is the full quasi-period, with the sign convention fixed in section3.

Proof from the already opened primary Nesterenko theorem. First take w primitive and extend it to an oriented lattice basis (w,w2), with tau=w2/w in H. Put Y=eta(w)/pi. The exact normalization identities are

\[
 E_2(\tau)=3XY,\quad E_4(\tau)=\frac34g_2X^4,
 \quad E_6(\tau)=\frac{27}{8}g_3X^6.
\]

If X,Y were algebraically dependent, the field generated by these three Eisenstein values would have transcendence degree at most1. Adjoining q adds at most1, contradicting Nesterenko's lower bound3 for Q(q,E2,E4,E6). This argument also covers g2=0 or g3=0: the displayed inclusion of fields, rather than division by either invariant, is sufficient. Every nonzero period is an integer multiple of a primitive period, and eta is additive on the lattice, so multiplication of both coordinates by that nonzero integer proves the general case. Finally (X,Y) maps to (X,Y-aX) by an invertible matrix over Qbar; its inverse is (X,Z) to (X,Z+aX). This proves (42.1).

The newly opened primary Chang author manuscript, dated7May2010 and uploaded by its author6January2016, independently states the unshifted assertion as Theorem2.2.1, p5, citing Chudnovsky1976. Theorem2.1.1 pp4–5 and its proof give the period normalization used for quasimodular forms. This is the full author-uploaded text at https://www.researchgate.net/publication/228393829_Transcendence_of_special_values_of_quasi-modular_forms, not a claim to have read the final2012 publisher PDF. The original Chudnovsky1976 four-page Russian article was not obtained in this search; the proof above instead uses the already opened Nesterenko original. Publisher metadata confirms ForumMath24(2012),539–551, DOI10.1515/form.2011.072. Opened references turn113207937view0, turn718354232view1–2, turn231361543view0/2.

### 42.2 What the quotient supplies, with its scale retained

Write mu_i=eta_i-a omega_i. For a full lattice Lambda_a=Zmu_1+Zmu_2 whose j-invariant is algebraic, choose an algebraic elliptic model F and an analytic uniformization F(C)=C/Lambda_F using its algebraic invariant differential. The equality of j-invariants gives a homothety

\[
 \Lambda_a=d\Lambda_F,\qquad
 \nu_i=\mu_i/d\in\Lambda_F.
 \tag{42.2}
\]

The nu_i form a lattice basis; its orientation may be negative, which does not change the period assertion. The analytic isomorphism is [z] to [z/d], with differential dz/d. A.4.35 proves that d is transcendental whenever a is algebraic. Equation(42.1) then says exactly that omega_i/pi and d nu_i/pi are algebraically independent. It does not remove d from(42.2). At the actual Hodge value, the precise choice is F=bar E, d=c and nu_i=bar omega_i. Thus the quotient equation gives no algebraic-coefficient linear relation among holomorphic periods of E and bar E: its displayed coefficient is c. This identifies the still-required arithmetic information without asserting that another use of a period theorem is impossible.

In the real rectangular E_* case, mu_1=c omega_1 and mu_2=-c omega_2. Replacing mu_1 by c omega_1 in(42.1) leaves the independent pair omega_1/pi,c omega_1/pi. The change (X,c) to (X,cX) is birational for X nonzero, so the normalized-period result would force c and omega_1/pi to be independent at an algebraic Hodge value. This is a consequence required of such a value, not a contradiction and not a proof that the value exists. The main nonzero algebraic-h gate is unchanged.

### 42.3 The final Jacobi–Weierstrass construction retains h

The full final33-page article Alfes–Funke–Mertens–Rosu, *On Jacobi–Weierstrass mock modular forms*, AdvMath465(2025),110147, was opened at https://publications.rwth-aachen.de/record/1005979/files/1005979.pdf. Theorem1.2 p6 includes weight2; Section3.1 pp14–15 gives the completed Weierstrass input, and Theorem3.1 p15 gives its harmonic-Maass construction. The completion for Lambda_tau=Z+Ztau is

\[
 \zeta^*_{\Lambda_\tau}(z)
 =\zeta_{\Lambda_\tau}(z)-G_2^*(\tau)z
       -\frac{\pi}{\operatorname{Im}\tau}\bar z,
 \qquad G_2^*=\frac{\pi^2}{3}E_2^*.
 \tag{42.3}
\]

Our h for this lattice is G2*, and our c is pi/Imtau. For any nonzero lambda, the identities

\[
 \zeta_{\lambda\Lambda}(\lambda z)=\lambda^{-1}\zeta_\Lambda(z),
 \quad h_{\lambda\Lambda}=\lambda^{-2}h_\Lambda,
 \quad c_{\lambda\Lambda}=|\lambda|^{-2}c_\Lambda
\]

give zeta-star_(lambda Lambda)(lambda z)=lambda^{-1}zeta-star_Lambda(z) term by term. Therefore the exact weight2 specialization of the new construction is the same completed function zeta(u)-hu-c bar(u) already used in sections23 and40. Its linear coefficient still contains h. No algebraicity theorem for that coefficient is stated in the consulted construction. Opened final source references turn113207937view1 and turn718354232view3–4. The web text was read; a direct local download encountered the repository's challenge page, so a local final PDF is not claimed saved.

### 42.4 Search and access record

Primary-source searches used the exact phrases second-kind period lattice, quasi-period algebraic j-invariant, algebraic quotient lattice, and the titles of Chang2012, Masser–Wustholz1983 and Vergnaud2009. The full Masser–Wustholz1983 original was not obtained: EuDML143029 returned403, while the Springer DOI10.1007/BF01398396 PDF request redirected to the subscription article page. The author's publication list confirms metadata only. No theorem from its unread full text is used.

Vergnaud, JNT129(2009),1212–1233, DOI10.1016/j.jnt.2009.01.021, was found by title (*Mesures d'independance lineaire de carres de periodes et quasi-periodes de courbes elliptiques*), but the publisher full PDF remained inaccessible. The author publication page lists it with a DOI; no source theorem is asserted from search snippets. The final2025 Jacobi–Weierstrass article and Chang manuscript above were actually opened. The known Stanford UQ statement that algebraic de Rham splitting forces an algebraic Betti period ratio was excluded: it supplies no comparison-map proof, while (42.2) explicitly retains its missing scale. H1 remains unchanged.

## 43. The new functional period-recovery theorem and its exact local maps

### 43.1 Opened statement and coefficient field

Bakker–Pila–Tsimerman, *Periods in families and derivatives of period maps*, JIMJ25(6)(2026),3187–3206, DOI10.1017/S1474748026101972, was opened and downloaded in its complete final20-page version. Local files: work/sources_elliptic/bakker_pila_tsimerman2026.pdf/.txt. Theorem1.1, pp3189–3190, compares fields of meromorphic germs at a basepoint, generated over the rational-function field of a complex variety by period functions and by Hodge-flag coordinates and their algebraic derivatives. The equality of algebraic closures uses the stated exclusion of an infinite-monodromy unitary tensor factor. The more general definable-equivariant version is Theorem3.9 p3196; Definition3.6 p3195 defines the derivative-generated field. Section4.2 pp3202–3203 explicitly treats elliptic curves.

These fields contain C. On the subring of germs holomorphic at the basepoint, evaluation is a C-algebra homomorphism to C and hence fixes every complex constant, including all entries of a chosen constant change of flat basis. Evaluation is not defined on the full field of germs, since 1/(t-t0) has a pole. Thus a conclusion about an algebraic extension of these germ fields alone supplies no descent of a chosen constant matrix to Qbar. The next calculation exhibits that matrix and its effect, rather than making a categorical separation assertion.

### 43.2 Direct check of the published elliptic example

Put J1=j'(tau), J2=j''(tau). The source chooses the relative form theta=sqrt(J1) dz and its two periods

\[
 f_1=\sqrt{J_1},\qquad f_2=\tau\sqrt{J_1}.
\]

The ordinary chain rule d/dj=(1/J1)d/dtau gives

\[
 2\frac{df_1}{dj}=\frac{J_2}{J_1^{3/2}}=:R_1,
 \qquad
 2\frac{df_2}{dj}=\tau R_1+\frac{2}{\sqrt{J_1}}=:R_2.
 \tag{43.1}
\]

The displayed R2 in the final source p3202 has a minus sign. This was visually verified in the local rendering work/sources_elliptic/bpt2026_p3202.png. The plus in(43.1) is the derivative of the source's own f2. The discrepancy is exactly4/sqrt(J1), which is nonzero on the chosen open locus. It can also be checked by tau to -1/tau: on a consistent square-root branch, J1 transforms to tau^2 J1, J2 to tau^4 J2+2 tau^3 J1, and the pair(R1,R2) in(43.1) transforms to(R2,-R1). This is a correction of this local displayed calculation; no claim that it invalidates the main functional theorem is made.

The differential normalization also matters arithmetically. On a fixed algebraic Weierstrass model with g2 g3 nonzero and first period w, write u=wz, so its algebraic differential is du=w dz. The standard j-derivative identity and our invariant normalizations yield

\[
 j'(\tau)=-2\pi i\,j(\tau)\frac{E_6(\tau)}{E_4(\tau)},
 \qquad
 \left(\frac{\sqrt{j'(\tau)}}{w}\right)^2
 =-\frac{9i}{\pi}\,j(\tau)\frac{g_3}{g_2}.
 \tag{43.2}
\]

Thus the source's theta is an explicitly scaled version of du. At E_* the square of that scale is a nonzero algebraic multiple of1/pi, and so the scale is transcendental. This is allowed by the source's algebraic structure over C. It is not an algebraic change of our chosen Qbar de Rham basis.

### 43.3 A non-CM family with a rational normalized period germ

Consider y^2=4x(x-1)(x-t), with t avoiding0,1, and omega=dx/y. Its period f satisfies

\[
 t(1-t)f''+(1-2t)f'-\tfrac14f=0.
 \tag{43.3}
\]

This also follows directly from the Gauss–Manin matrix proved in A.4.28: differentiate the first equation and eliminate the eta period. In the algebraic basis (omega,nabla_(d/dt)omega), the period matrix P satisfies P'=A(t)P, where

\[
 A(t)=\begin{pmatrix}0&1\\
 1/(4t(1-t))&(2t-1)/(t(1-t))\end{pmatrix}.
\]

Choose any t0 in Qbar outside0,1 and let P0=P(t0) be the actual period matrix in a Betti integral basis. Its determinant is nonzero. The constant complex change of flat basis

\[
 F(t)=P(t)P_0^{-1}
 \tag{43.4}
\]

gives F'=AF and F(t0)=I. If A=sum A_n(t-t0)^n and F=sum F_n(t-t0)^n, then

\[
 F_0=I,\qquad
 (n+1)F_{n+1}=\sum_{k=0}^n A_kF_{n-k}.
 \tag{43.5}
\]

Every A_n lies in Qbar, so induction proves that every F_n does too. In particular the projective first-row coordinate phi=F12/F11 has all Taylor coefficients algebraic, phi(t0)=0 and phi'(t0)=1. This construction holds for every algebraic t0, without a CM assumption.

For a fully explicit non-CM example take t0=3. Its invariant is j=256(1-t+t^2)^3/(t^2(1-t)^2)=21952/9, a noninteger rational number, so the known integrality of CM j-invariants excludes CM. In this example all coefficients in(43.5) are rational. The finite certificate below gives the first12 Taylor coefficients of phi; the induction proves the assertion for every coefficient.

The exact relation with the original Betti period ratio is also visible. Write

\[
 P_0=\begin{pmatrix}a&b\\c&d\end{pmatrix},\qquad
 \tau(t)=\omega_2(t)/\omega_1(t).
\]

Multiplication in(43.4) gives

\[
 \phi(t)=\frac{a\tau(t)-b}{d-c\tau(t)}.
 \tag{43.6}
\]

The coefficients a,b,c,d are entries of the actual period matrix, not asserted algebraic. At t0, tau=b/a and phi=0. Formula(43.6), with its actual coefficients retained, explains how the rational Taylor germ is compatible with the transcendental non-CM Betti period ratio. The complex local system and its period map still satisfy the functional theorem after this constant change of basis: the monodromy is conjugated by P0, and the map on the flag variety is the displayed projective transformation. It is therefore not legitimate to infer Qbar-rationality in the original Betti structure just from the germ-field equality or the new algebraic Taylor coefficients.

For the actual Hodge question, algebraicity of h would give an algebraic initial de Rham vector (h,1); its horizontal continuation already has algebraic Taylor coefficients by the same recurrence. It does not furnish algebraicity of P0 or of the coefficients in(43.6). Proving the relevant arithmetic descent is still an additional obligation. This checks the proposed specialization route and leaves other possible applications of the functional theorem open. H1 remains unchanged.

### 43.4 Reproducible checks and source record

work/code_elliptic/check_period_germ_recovery.py, .out and .json contain16 passing exact checks: the two derivatives and their sign difference, the S-transformation, the projective basis map, rational companion-system coefficients through degree12, the Wronskian formula, j(3), and the form scale(43.2). The execution completed with exit0 in19.269353337 seconds; the JSON contains the actual UTC start, inputs and SymPy version. Infinite Taylor rationality is proved by(43.5), not inferred from a finite truncation.

Opened primary references: turn704256714view0; turn821549115view0/3; turn231361543view1. Final publisher URL: https://www.cambridge.org/core/services/aop-cambridge-core/content/view/0E049E0EA1AD619AB320C19B679494C2/S1474748026101972a.pdf/div-class-title-periods-in-families-and-derivatives-of-period-maps-div.pdf. Local p3202 was visually inspected. The original germ theorem is used with its complex coefficient field and exact basis maps retained; no arithmetic converse is attributed to it.


## 44. The opened Vergnaud thesis and the exact square-period specialization

The previously inaccessible 2009 journal paper now has an independently opened primary predecessor: Damien Vergnaud's complete doctoral thesis, *Approximation diophantienne et courbes elliptiques. Protocoles asymetriques d'authentification non-transferable*, defended at Caen on17November2006. The author's page https://www.di.ens.fr/~vergnaud/These.html links the original full PostScript at https://www.di.ens.fr/~vergnaud/TheseVergnaud.ps.gz. That file was downloaded, decompressed and converted locally without changing its content; retained files are work/sources_elliptic/vergnaud2006_thesis.ps.gz, .ps, .pdf and .txt. The final2009 Journal of Number Theory article remains unobtained. Author-page refs: turn560371786view0, turn717636677view1, turn293163150view0. The web parser could not decode the gzip, so the actual theorem was read from the local original, not inferred from its landing page.

Chapter2 begins on printedp37. Its Theorem2.1.14, printedp43, gives an explicit Q-linear independence measure for

\[
1,\quad (\omega(1/q)/\pi)^2,\quad
\omega(1/q)\eta(1/q)/\pi^2,\quad (\eta(1/q)/\pi)^2
\]

for integer q in (-infinity,-108606] or [112138,infinity). Theorem2.1.13 on the same page treats the three contiguous hypergeometric values at1/q under its distinct stated bounds. I visually read the page, saved as vergnaud2006_thesis_p43.png, to verify that the coefficient field in these statements is Q. The chapter uses normalized functions omega(lambda)=pi F(1/2,1/2;1;lambda) and eta(lambda)=pi F(-1/2,1/2;1;lambda), defined on p40. Its quantitative assertions are retained with their specified rational arguments.

### 44.1 Exact comparison of its eta with the short-model quasiperiod

For 0<lambda<1, take the short Weierstrass model whose roots are

\[
e_1=(2-\lambda)/3,\qquad e_2=(2\lambda-1)/3,
\qquad e_3=-(1+\lambda)/3.
\]

Its first full period is w=2K(lambda), with differential dx/y and y squared equal to4 times the cubic. Write E(u) for the Jacobi epsilon function, whose derivative is1-lambda sn(u)^2 and whose increment over2K is2E(lambda). The Jacobi differential equation gives

\[
\frac{d}{du}\frac{\operatorname{cn}(u)\operatorname{dn}(u)}{\operatorname{sn}(u)}
=-\operatorname{sn}(u)^{-2}+\lambda\operatorname{sn}(u)^2.
\]

Consequently

\[
\zeta(u)=\frac{\operatorname{cn}(u)\operatorname{dn}(u)}{\operatorname{sn}(u)}
+E(u)+\frac{\lambda-2}{3}u,
\]

because the derivatives are -wp(u), and both sides have the same odd principal part1/u at zero. The periodic first term and the epsilon increment then give the exact full quasiperiod

\[
\eta_{\rm short}(w)=2E(\lambda)-\frac{2-\lambda}{3}w.
\tag{44.1}
\]

Thus the thesis's named pair is related to our short-model pair by the invertible algebraic shear

\[
\binom{\omega}{\eta_{\rm thesis}}
=\begin{pmatrix}1&0\\ (2-\lambda)/3&1\end{pmatrix}
\binom{w}{\eta_{\rm short}}.
\tag{44.2}
\]

This identifies the normalization rather than silently replacing the second-kind differential. Qualitative algebraic independence of the normalized pair for algebraic lambda follows already from section42 and this algebraic shear. The newly opened chapter supplies quantitative information only in its stated range.

### 44.2 No rational Legendre parameter for the fixed E_star

Any Legendre parameter of the fixed curve E_star has

\[
256\frac{(1-\lambda+\lambda^2)^3}{\lambda^2(1-\lambda)^2}
=\frac{110592}{37}.
\]

Equivalently it is a zero of

\[
P(T)=37T^6-111T^5-210T^4+605T^3-210T^2-111T+37.
\tag{44.3}
\]

This polynomial is primitive. The rational-root theorem restricts any rational root to the six values plus or minus1,37,1/37. Direct exact evaluation excludes all six; for example P(1)=37 and P(-1)=-729. The remaining exact values are retained in the certificate. Hence no choice of ordered branch points for E_star gives a rational lambda. In particular the input lambda=1/q required by the opened Theorem2.1.14 is not obtained from E_star by an algebraic isomorphism.

This checks the direct numerical substitution. It does not exclude an argument using different functions, isogenies, or a further quantitative theorem. No such additional map with verified numerical hypotheses has been constructed here. The nonzero algebraic-h gate remains unchanged.

### 44.3 Reproducibility and search record

The exact certificate work/code_elliptic/check_vergnaud_specialization.py ran exit0 with12checks in0.269100313seconds. Its .json and .out preserve the input curve, polynomial, all six rational-root evaluations, Jacobi derivative identity and shear matrix. This code proves no transcendence assertion.

Fresh exact-title searches for second-kind lattices with algebraic j, quasi-period modular invariants, algebraic Hodge splittings, almost-holomorphic value transcendence, and period-square measures returned the already audited Kumar2026, Howe-Klevdal2026, Spence2018 and Bertolin-Waldschmidt2025 sources. Their reappearance is not counted as mathematical movement. The unsupported Stanford-UQ deRham-to-Betti assertion remains excluded. EuDML143029 again returned403 for Masser-Wustholz1983; no theorem from its unobtained full text is invoked. The actual new access obtained in this continuation is the Vergnaud thesis above.

## 45. The final harmonic-Maass period theorem and the actual theta-lift input

The complete final paper Claudia Alfes-Neumann, Jan Hendrik Bruinier and
Markus Schwagenscheidt, *Harmonic weak Maass forms and periods II*,
Math. Ann.391(2025),791–817, DOI10.1007/s00208-024-02927-4, was opened
and downloaded as `work/sources_elliptic/alfes_bruinier_schwagenscheidt2025.pdf`.
Theorem5.1 and equation(5.3) are on p.812; Theorem5.2 continues onto
p.813; Theorem6.1 and its three-step proof discussion are on p.814.
This is new primary access, rather than a new H1 theorem.

Theorem5.1 has as its input the prescribed harmonic Maass form f of weight
3/2−k, with principal part over the Hecke field F_G and shadow the normalized
Shimura correspondent of G of weight2k. Its equivalence compares the
coefficient c_f^+(|Delta|,rho), all square-multiple coefficients, and the
Fourier coefficients of the canonical meromorphic form eta_{k,Delta,rho}(f).
The latter coefficients must belong to **i pi^k sqrt(Delta) F_G**. The
coefficient relation is exactly equation(5.3), a sum over divisors with
the genus character, powers of n and d, and
c_f^+(|Delta|n²/d²,rho n/d). The scalar i pi^k sqrt(Delta) is retained.
Theorem5.2 subtracts the appropriate multiple of G to set the first
coefficient to zero and expresses c_f^+(|Delta|,rho) by the resulting
cycle-integral quotient. These are statements for the specified
half-integral input form and its actual theta lift.

Theorem6.1 recalls the weight1/2 case: under its newform, sign,
Shimura-correspondent and principal-part hypotheses, the indicated
coefficient is algebraic exactly when the central derivative L'(G,chi_Delta,1)
vanishes. Its proof passes through the actual canonical differential of
the third kind and the torsion of its Heegner divisor. The following
higher-weight discussion explicitly leaves the corresponding algebraicity
to cycle-vanishing step unproved. No claim from that discussion is used here.

The exact map from the weight-zero Weierstrass form in §40 is the
Alfes–Griffin–Ono–Rolen theta lift already opened there. Its coefficients
are CM traces of the **full** input values, not a coefficientwise map of
the holomorphic q-series. Those values are, up to the specified algebraic
correction,

\[
 \zeta(\varepsilon(z))-h\varepsilon(z)-c\overline{\varepsilon(z)}.
\]

The algebraicity of the q-coefficients implied by an algebraic h does not
by that formula supply algebraicity of these CM traces. In particular the
c-term and the elliptic logarithms remain in the map. Thus the exact
input needed for Theorem6.1 has not been deduced from algebraicity of h.
This is an identified coefficient-map obligation; it makes no claim that
the two weights or theories are unrelated. The main gate is unchanged.

## 46. The symmetric-square class, its stabilizer, and the conjugate extension map

### 46.1 An actual degree-two period on E_star squared

For a real short model with three real roots, use the established cycles
with w=omega1 positive real, omega2=tau w positive imaginary, and
eta1=(h+c)w, eta2=(h−c)tau w. Here h is real, c>0 and
c tau w²=pi i. The latter identity is exactly the Legendre relation.
The integration matrix, with cycles as rows and forms (omega,xi) as
columns, is

\[
 P=\begin{pmatrix}w&-(h+c)w\\ \tau w&-(h-c)\tau w\end{pmatrix},
       \qquad \det P=2c\tau w^2=2\pi i.
\tag{46.1}
\]

For an arbitrary complex a, define the actual Kunneth class on E×E

\[
 \theta_a=\operatorname{pr}_1^*\omega\wedge\operatorname{pr}_2^*\xi
          +\operatorname{pr}_1^*\xi\wedge\operatorname{pr}_2^*\omega
          +2a\operatorname{pr}_1^*\omega\wedge\operatorname{pr}_2^*\omega.
\tag{46.2}
\]

Thus theta_a is algebraic de Rham exactly when a is algebraic, since the
three symmetric Kunneth tensors displayed are independent over Qbar.
Its coefficient matrix in the two factors is
T_a=[[2a,1],[1,0]]. The product-cycle periods are the entries of P T_a P^t.
This gives, without omitting any period,

\[
 {1\over2\pi i}PT_aP^{\mathsf T}=
 \begin{pmatrix}
 (a-h-c)/(c\tau)&(a-h)/c\\
 (a-h)/c&(a-h+c)\tau/c
 \end{pmatrix}.
\tag{46.3}
\]

In particular the period over gamma1×gamma2 is
2(a−h)tau w², so it vanishes exactly at a=h. At that value,

\[
 {1\over2\pi i}PT_hP^{\mathsf T}
        =\operatorname{diag}(-\tau^{-1},\tau).
\tag{46.4}
\]

The class theta_h has type(1,1), since it is the sum of the products of
omega with xi+h omega, and the latter is the antiholomorphic class.
But (46.4) has projective coordinate ratio −tau². For the fixed non-CM
E_star, Schneider's theorem makes tau transcendental. Hence tau² is
transcendental, and **no nonzero complex scalar multiple** of this Betti
period vector has all coordinates in Qbar. Indeed algebraicity of both
nonzero coordinates of such a multiple would make their ratio algebraic.
This assertion concerns the Betti vector of theta_h, irrespective of
whether h is algebraic.

For the divisor route the actual hypothesis is therefore absent:
algebraicity of theta_h in de Rham would not make theta_h, or even its
projective Betti line, a Qbar-de Rham–Betti class. The source definition
requires the full comparison vector to be algebraic on the Betti side.
The opened author-hosted45-page version of Kreutz–Shen–Vial states this
in Definition4.5 p.13 and the introductory definition p.5; its
Theorem7.12(ii) p.27 proves algebraicity of the resulting classes on
products of elliptic curves. Equation(46.4) checks that exact hypothesis
on this proposed class. This does not exclude a different tensor
construction with different comparison coordinates.

### 46.2 The exact map to the earlier Hodge projector

There is in fact a canonical comparison-compatible isomorphism

\[
 \operatorname{Sym}^2 V\otimes(\det V)^{-1}
                       \longrightarrow\mathfrak{sl}(V).
\tag{46.5}
\]

In a basis with determinant generator, represent a symmetric tensor by
its matrix T and put J0=[[0,1],[-1,0]]. The map is T↦T J0.
Every trace-zero matrix occurs uniquely: if U has trace zero, then
−U J0 is symmetric. Thus it is an isomorphism. Under a basis comparison
P, the determinant-twisted tensor transforms to PTP^t/detP. The identity
P^t J0 P=(detP)J0 proves

\[
 (PTP^{\mathsf T}/\det P)J_0=P(TJ_0)P^{-1},
\]

which establishes comparison compatibility, including the Tate factor.
For the tensor (46.2) this map gives

\[
 T_aJ_0=\begin{pmatrix}-1&2a\\0&1\end{pmatrix};
 \qquad T_hJ_0=2e_h-I,
 \qquad e_h=\begin{pmatrix}0&h\\0&1\end{pmatrix}.
\tag{46.6}
\]

Its Betti matrix from(46.4) is

\[
       \begin{pmatrix}0&-\tau^{-1}\\-\tau&0\end{pmatrix}.
\tag{46.7}
\]

The symmetric-square proposal therefore carries exactly the same
comparison data as the earlier Hodge projector, by the explicit
isomorphism(46.5). It has not reduced H1 to a smaller gate.

The stabilizer can be computed in the same coordinates. The centralizer
of T_aJ0 in GL2(C) is exactly

\[
 C_a=\left\{\begin{pmatrix}r&a(s-r)\\0&s\end{pmatrix}:
                                  r,s\in\mathbf C^*\right\}.
\tag{46.8}
\]

To prove exhaustiveness, its two distinct eigenlines are C omega and
C(xi+a omega). A commuting matrix must preserve each and acts on them
by r and s; writing that action in the original basis gives(46.8).
Thus C_a is an algebraic two-dimensional torus for every algebraic a,
even for a chosen complement on a non-CM curve. For the actual a=h,
the Betti centralizer is its conjugate P C_h P^{-1}. The algebraic
entries of a matrix in C_h do not replace the Betti requirement: from
(46.7), a nonscalar algebraic de Rham element with algebraic Betti
entries would recover tau algebraically, as in A.4.18. This checks the
positive-dimensional-stabilizer proposal through the actual conjugation
map, rather than assuming a motivic meaning for that stabilizer.

### 46.3 The complete conjugate-period map on universal extensions

For an arbitrary algebraic short model, use the tangent coordinates
(u,s) of §17, with period vectors (omega_i,eta_i) and
eta_i=h omega_i+c bar(omega_i). The unique complex-linear map carrying
these two period vectors to their conjugates is

\[
 M=\begin{pmatrix}
 -h/c&1/c\\ c-h\overline h/c&\overline h/c
 \end{pmatrix}.
\tag{46.9}
\]

Indeed on a vector (u,hu+cv) it gives (v,bar(h)v+cu). Substitution
v=bar(omega_i) proves the claimed lattice map. The two period vectors
are a complex basis by Legendre, so this also proves uniqueness.
Consequently M descends to a holomorphic group isomorphism
(E^dagger)^an→(bar E^dagger)^an. Its determinant is−1 and bar(M)M=I.
In the shifted coordinates (u,s−hu) and (v,t−bar(h)v), its matrix is
[[0,1/c],[c,0]]. This is the exact comparison; both scales remain.

This analytic group map is not an algebraic group map over C. Any
algebraic group map E^dagger→bar E^dagger must send the vertical Ga
into the vertical Ga, since its composition Ga→bar E is constant:
the latter morphism extends across infinity to P1→bar E and must be
constant, for example by Riemann–Hurwitz. But M sends the vertical
tangent vector (0,1) to a vector with first coordinate1/c≠0.

Bost–Charles, arXiv1307.1045v2, Theorem3.1 p.13, applies to algebraic
Lie maps preserving these period lattices: the periods span the source
Lie algebra, so such a map would be algebraic. Hence the entries of M
cannot all be algebraic. In particular algebraic h and algebraic c
cannot occur together, recovering the earlier exact obstruction with
the full two-dimensional map visible. Nothing in (46.8) makes the
entry1/c in (46.9) algebraic. This route supplies no non-CM exclusion
for algebraic h alone.

### 46.4 Certificates and source locators

`work/code_elliptic/check_symmetric_hodge_tensor.py` ran with exit0 in
0.373440449seconds. Its output and JSON record the exact tensor,
determinant-twist equivariance, all four normalized product periods,
projector, stabilizer and conjugate-extension matrix identities.

The KSV author-hosted snapshot was downloaded in this continuation as
`ksv_author45_20261119.pdf/.txt`. Its45-page pagination is distinguished
from the later arXiv version already cited elsewhere in this dossier;
the locators above apply only to this opened snapshot. Bost–Charles
Theorem3.1 was reopened in the complete original author preprint.
The current searches for algebraic Hodge splittings, unitary universal
extensions, stabilizers, and second-kind period lattices returned the
already audited Bost–Kunnemann, Fonseca and KSV results. The exact maps
above were checked; no unsupported new transcendence assertion is
inferred from repeated source hits.

## 47. The exact tangent map to the ordinary etale integral structure

This continuation applies an additional theorem from the already retained
Mochizuki May2000 primary manuscript; it is not a new source discovery.
Theorem1.3, printedpp13–14, constructs the functorial, non-finite-type group
scheme E†_et over a Z-flat base, with ordinary generic fibre E†. Its
coordinate algebra has the stated factorial integral filtration. Lemma2.1,
p16, identifies the completed binomial algebra with Cont(Z_p,Z_p).
Theorem2.2, pp18–19, identifies the p-adic completion of E†_et with the
inverse Verschiebung tower described onpp16–17.

**47.1. Exact base change and tangent.** First work over the formally etale
ordinary moduli neighborhood used in §2.2 of the source. Its maps
V^n:E^{F^n}→E are finite etale of degree p^n. Pull back this whole diagram,
and the isomorphism of Theorem2.2, along an actual classifying point
Spec(R)→S for an ordinary elliptic curve with good reduction, where R
is Z_p or a finite unramified extension used to choose an etale moduli
chart or prime-to-p level structure. This use
of base change does not assert that the individual point's classifying
map is itself etale. The functoriality in Theorem1.3 and the displayed
isomorphism permit this pullback.

At the identity, a nilpotent first-order test map to E has a unique lift
to each finite etale V^n-cover after prescribing the identity lift of its
closed point. These lifts are compatible, by uniqueness, and give a
unique map to the inverse tower and its p-adic completion. Consequently

    Lie((E†_et)^completion) → Lie(E)

is an isomorphism of rank-one R-modules. Composing with the canonical
map of Theorem2.2 to (E†)^completion gives one specific integral line in
Lie(E†). The two-dimensional Lie space of the usual smooth universal
extension has many other algebraic lines projecting isomorphically to
Lie(E); the preceding map selects just one of them.

This loss of vertical tangent is also visible directly in the source's
binomial description after its indicated pro-etale trivialization. For
r≥1,

    (b d/dT) binom(T,r) evaluated at T=0
       = b (-1)^(r−1)/r.

The formula follows by differentiating the factor T in
T(T−1)...(T−r+1)/r! at zero. For any nonzero b∈Q_p, its valuation at
r=p^n is v_p(b)−n. Thus no nonzero constant vertical derivation, even
after multiplication by one fixed nonzero scalar, preserves all levels
of the integral binomial algebra. This is an explicit calculation of
the missing integral tangent map; it does not assert that an arbitrary
algebraic complement is the line furnished by Theorem2.2.

**47.2. An exact ordinary-prime test on E*.** Use the invariant vector
fields and coframe already fixed in A.4.31:

    D_a = y ∂x + (6x²−g2/2) ∂y − (x+a) ∂t,
    V = −∂t,
    D_a^p = H_p D_a − (K_p+aH_p)V.

A rank-one formal subgroup's invariant Lie line is closed under the
restricted p-th power after reduction modulo p. Therefore a normalized
D_a which actually comes from the integral tangent map in47.1 must
satisfy K_p+aH_p=0 modulo p. This is a necessary congruence; lifting that
congruence alone to the full tower is not asserted.

For E*:y²=4x³−4x−1 at p=5, put P=4x³−4x−1. Direct expansion gives

    P²=16x⁶−32x⁴−8x³+16x²+8x+1,
    H_5=[x⁴]P²=3 mod5,    K_5=[x³]P²=2 mod5.

The curve has8 points overF5, so it is ordinary (trace−2), and the
necessary tangent condition is a=1 mod5. The algebraic integral line
D_0 on this exact curve fails it. This is an example concerning an
arbitrary algebraic complement, not an identification of D_0 with the
actual complex Hodge complement. No congruence for h_infinity has been
derived merely from algebraicity of h_infinity.

**47.3. The base connection and the vertical line.** The source's
Theorem5.2, printedp41, constructs a connection on the family over the
moduli base. Its horizontal map is a splitting
sigma:T_S→T_(E†) of the differential of the projection to S, so
(d pi) sigma=id. The invariant vertical field D_a is in ker(d pi).
Hence im(sigma)∩ker(d pi)=0, by applying d pi. The displayed morphisms
prove precisely why a curvature statement for that base connection
cannot simply be substituted for the p-th-power calculation of D_a.
No impossibility statement about other uses of the source is intended.

The exact finite certificate
`work/code_elliptic/check_etale_integral_tangent.py` has inputs E*,p5 and
binomial degrees1–25. It verifies the25 derivative identities, the point
count and H,K coefficients, and D_a^5 on all three coordinate generators
modulo the curve equation. It ran with exit0 in0.512329359seconds;
`.out` and `.json` retain output, input, SHA256 and UTC start. The
all-degree derivative proof and the formal etale tangent proof above do
not rest on a finite test. H1 is unchanged.

## 48. Waldschmidt's exact period term and the Hodge quotient graph

**48.1. Primary theorem, with its actual rank.** The complete original
paper is Michel Waldschmidt, *On the transcendence methods of Gel'fond
and Schneider in several variables*, in *New advances in transcendence
theory* (Durham1986), Cambridge1988, pp375–398. The author-hosted scan was
opened and downloaded from
https://webusers.imj-prg.fr/~michel.waldschmidt/articles/pdf/Durham1986TMGSSV.pdf.
Theorem4.1 is on printedpp385–386, visually read in the retained images
`waldschmidt1988_p385_386.png` (actually the spread384–385) and
`waldschmidt1988_p386_387.png` (spread386–387). The scan's13 PDF pages
contain two printed pages apiece. Its plain pdftotext output contains no
text; no OCR-transcribed inequality was substituted for the images.

Here is the exact specialization notation needed below. For an algebraic
commutative group G=Ga^d0×Gm^d1×G2 of dimension d, a complex n-dimensional
linear subspace V of LieG, a Qbar-defined W⊂V, and a finitely generated
Y⊂V with Gamma=exp_G(Y)⊂G(Qbar), set
kappa=rank_Z(Y∩ker exp_G). The theorem supplies a proper connected
algebraic subgroup G′. Write delta=dim(G/G′), delta0 anddelta1 for the
codimensions of its projections to the displayed additive and toric
factors, delta2=delta−delta0−delta1, and

    lambda=rank_Z(Gamma/(Gamma∩G′)),
    tau=dim_C(W/(W∩LieG′)).

Its conclusions are delta>tau and

    (lambda+delta1+2delta2)(d−n)
       ≤ (delta−tau)(d1+2d2−kappa).                 (48.1)

In particular lambda is the rank AFTER exponentiation. Replacing it by
rank_Z(Y/(Y∩LieG′)) would be an incorrect theorem: periods disappear
from Gamma and are accounted for separately by kappa.

**48.2. Exact period input, without an algebraic rescaling.** Let E/Qbar
be any elliptic curve in the fixed short-Weierstrass normalization, and
use its actual numbers h,c=pi/Area with
eta_i=h omega_i+c conjugate(omega_i). The analytic homomorphism already
proved in A.4.33 is

    Phi_h:E†(C)→conjugate(E)(C),
    [(u,s)] ↦ [(s−hu)/c].

Set G=E†×conjugate(E), d=3,d0=d1=0,d2=3, and

    V_c={(u,s,v):s−hu=cv},    dim V_c=2.

Its exponential image is the graph of Phi_h. Its intersection with the
period kernel consists exactly of

    (omega,eta_omega,conjugate(omega)),   omega∈Lambda,

because a source period uniquely determines the third coordinate from
the displayed equation. It therefore has rank2. The scale c is retained
as its actual complex value throughout; it is not assumed algebraic.

When h is algebraic the line W=C(1,h,0) is defined overQbar. Taking Y to
be precisely the two period generators gives Gamma=0,kappa=2. For G′=0
we have delta3,tau1,lambda0. Inequality(48.1) becomes6≤8, and delta>tau
also holds. Thus the original theorem's conclusion is already satisfied
by the trivial subgroup on this precise period input. It supplies no
contradiction to algebraicity of h from these periods alone.

**48.3. A proved rank bound on algebraic points of the graph.** For any
E/Qbar for which its actual h is algebraic, put

    S_h = graph(Phi_h) ∩ (E†×conjugate(E))(Qbar).

Then S_h, as an abelian group, has torsion-free rank at most2. This is a
proved consequence of(48.1), not an assertion that the hypothesis is
known for non-CM E. It gives an exact necessary arithmetic consequence
of algebraicity of the actual h.

Proof. First recall the earlier analytic-subgroup argument in§19:
exp(C(1,h))∩E†(Qbar) consists only of the identity. Indeed an algebraic
nonidentity exponential in this Qbar-defined line would give, by the
analytic subgroup theorem, a positive-dimensional algebraic subgroup
with Lie algebra in that line. No such subgroup exists. The vertical
Ga has different Lie algebra; an elliptic subgroup mapping to E would
split the nonzero universal extension after an isogeny, which is
impossible because isogeny pullback is injective on H¹(O_E) in
characteristic zero. There is no torus: a map Gm→E is trivial and a map
Gm→Ga is trivial. The exact kernel of Phi_h is exp(C(1,h)), by
subtracting the unique source period corresponding to a target period.
Consequently S_h∩(E†×{0})={0}.

Let Gamma be any finitely generated subgroup of S_h, and choose
logarithms in V_c of its generators, together with the two period
generators. Their Z-span Y has kappa=2. Formula(48.1) reduces to

    lambda ≤ 2 delta−4 tau,    delta>tau.          (48.2)

We list all subgroups which its conclusion can use. A connected
one-dimensional subgroup of G is either the vertical Ga×{0} or
{0}×conjugate(E). Indeed the only one-dimensional affine possibilities
are Ga andGm, and any elliptic subgroup has zero projection to E† by
the universal-extension argument just given. Neither of these two
lines contains W. Both meet Gamma trivially: the first lies in
E†×{0}, and the second meets the graph of a function only at identity.
For such a subgroup delta2,tau1,lambda=rankGamma, so(48.2) forces
rankGamma=0.

For a connected two-dimensional G′, (48.2) requires tau0, hence
W⊂LieG′. Let q:G→E×conjugate(E) be the projection. Its vertical kernel
is Ga. If dim q(G′)=1, that elliptic image contains the tangent line
Lie(E)×0. Its map to conjugate(E) has zero differential and is trivial,
so q(G′)=E×0. Thus G′=E†×0. If dim q(G′)=2, q|G′ is an isogeny onto
E×conjugate(E). It would split the pullback of the nonzero extension
class of G by this isogeny, contrary to the same injectivity of
isogeny pullback on H¹(O). This second case is impossible. Hence the
only two-dimensional possibility has delta1,tau0, and its intersection
with Gamma is trivial, giving rankGamma≤2.

Finally G′=0 has delta3,tau1 and gives rankGamma≤2 directly. These
exhaust the proper connected subgroups of G, proving the asserted
bound for every finitely generated Gamma and therefore for S_h.

This argument supplies no third independent algebraic point of S_h.
The actual torsion points, whose graph coordinates are both algebraic,
have torsion-free rank0. Algebraicity of h by itself has not produced
any additional independent point. Thus the rank bound and the exact
period calculation do not settle H1 for E* or any other non-CM curve.
The rank calculation is recorded as work evidence, not as a smaller
resolved replacement for the nonzero algebraic-h gate.

**48.4. Search and scope.** The source was located from its author's
publication list, which gives the exact title andpp375–398. The nearby
file Durham1986PW.pdf is a different Philippon–Waldschmidt paper
(pp280–312) and was not substituted. The same author's later primary
exposition *Variations on the Six Exponentials Theorem*, Theorem5.1,
p352, was opened; it omits the W term in the displayed corollary, so
Theorem4.1 of the original was obtained for the actual computation.
Unreviewed AI summaries encountered during discovery were not used as
theorem sources. In particular the original image resolves exactly
what lambda counts. Searches for second-kind period lattices,
algebraic-j quotients, algebraic Hodge coefficients and unitary
connections otherwise returned the already retained primary sources;
no repeated hit is counted as new evidence for a converse.

## 49. Actual Galois coherence on the isogeny orbit and the exact local denominator

This section isolates arithmetic information that uses the actual Hodge
splitting, while retaining its local denominator obligation. It does
not assert that an arbitrary conjugate of an algebraic h is the Hodge
coefficient of the conjugate curve.

**49.1. An explicit differential-preserving quotient.** Let
E:y²=4x³−g2x−g3 overQbar, with omega=dx/y, xi=x omega, and let
C⊂E(Qbar) be a finite subgroup of order N. The corresponding lattice
Lambda_C contains Lambda with indexN. In the actual complex
uniformization one has

    wp_(Lambda_C)(u)
      = sum_(v in C) wp_Lambda(u+v) − S_C,
    S_C=sum_(v in C, v≠0) wp_Lambda(v).

Indeed both sides have exactly the simple list of double poles for
Lambda_C moduloLambda, with identical principal parts, and their
constant Laurent coefficients at0 are zero. Their difference is an
entire elliptic function, hence constant, and that constant is zero.
The addition formula makes the right side a rational function of x,y
and the algebraic coordinates of C. Its u-derivative supplies the y
coordinate of the quotient, and its Laurent expansion supplies
algebraic short-Weierstrass coefficients. This defines the algebraic
isogeny with f_C*omega_C=omega.

For each nonzero v put

    F_v=(y−y(v))/(2(x−x(v))).

The zeta addition formula, or direct differentiation of this rational
function, gives

    dF_v=(wp(u)−wp(u+v))du.

Consequently the actual pullback of second-kind differentials is

    f_C*xi_C=N xi−S_C omega−d(sum_(v≠0)F_v).       (49.1)

In particular it is N xi−S_C omega in algebraic de Rham cohomology.
Since the periods of xi are−eta, (49.1) gives
eta_C(omega)=N eta(omega)+S_C omega for every omega∈Lambda.
Also Area(Lambda_C)=Area(Lambda)/N. Inserting
eta=h omega+c baromega and c_C=Nc proves

    h(E_C,omega_C)=N h(E,omega)+S_C.              (49.2)

No algebraic period rescaling is assumed in this argument.

**49.2. The precise Galois statement.** Let K be a number field
containing g2,g3 and the actual number h(E,omega), when that number is
algebraic. For every sigma∈Gal(Qbar/K), the quotient construction and
its rational formulas identify (E_C)^sigma with E_(sigma C), with
identical indicated differential normalization. Formula(49.2) then
proves

    sigma(h(E_C,omega_C))
       =N h(E,omega)+S_(sigma C)
       =h(E_(sigma C),omega_(sigma C)).           (49.3)

Thus the actual splittings on this whole isogeny orbit, in the specified
frames, are compatible with this particular Galois group. The proof
uses sigma(h(E))=h(E), which follows because sigma fixes K. It makes no
claim for a sigma not fixing K, and no claim that sigma(h(E)) always
equals h(E^sigma). For a subsequent algebraic change of short frame,
the same conclusion follows by the explicitly prescribed differential
scaling in(49.4) below.

**49.3. The ordinary integral tangent is functorial for these actual
isogenies.** Use the ordinary integral line supplied by47.1, and denote
its slope in the (du,ds) coframe by u_p(E). This notation here denotes
the line defined by the inverse-Verschiebung construction itself; the
proof does not need an identification with a differently normalized
Hodge–Tate splitting. The line is integral because its projection to
Lie(E) is an isomorphism over the complete valuation ring.

For an isogeny f:E→E′ of good ordinary elliptic schemes, quotienting
both sides by their multiplicative p^m-torsion gives an actual map
f^{F^m}:E^{F^m}→(E′)^{F^m}, commuting with V^m and f. The two maps from
E^{F^m} modulo p^m to (E′)† obtained using f† and the normalized
splittings kappa[p^m] in Mochizuki§2.2 lift the same map to E′. Their
difference is a map from the proper elliptic scheme E^{F^m} to the
vector kernel. Such a map is constant, because global regular
functions on each such elliptic scheme are the base ring; it is zero
at the identity. The two maps therefore agree. Passing to the inverse
tower and then to its identity tangent proves that f† carries the
integral tangent line of E to that of E′. This proves the required
functorial map, including p-power isogenies, before using it.

Suppose now f has kernel C of order N and f*omega′=lambda omega in
short-Weierstrass frames. The differential-preserving quotient in49.1
has omega_C=omega′/lambda, x_C=lambda² x′ and xi_C=lambda xi′.
Dividing(49.1) bylambda therefore yields

    f*xi′=(N/lambda)xi−(S_C/lambda)omega.

On the universal extension the corresponding linear map is
(u,s)↦(lambda u,(N/lambda)s+(S_C/lambda)u). It follows both for the
actual Hodge line and for the functorial integral tangent line that

    lambda² h(E′)=N h(E)+S_C,
    lambda² u_p(E′)=N u_p(E)+S_C.

Subtracting gives the exact identity

    lambda²(h(E′)−u_p(E′))
         =N(h(E)−u_p(E)).                        (49.4)

When h is algebraic, fix an embedding of its number field into Cp in
this identity. The algebraicity of h(E′) then follows from the first
line; u_p is its actual p-adic value, not an assumed algebraic number.

**49.4. Connected-kernel p-power tower.** For an ordinary good E at
p>3, let C_n be its multiplicative subgroup of order p^n and let
f_n:E→E_n=E/C_n. Work over a complete finite-extension valuation ring
where the chosen algebraic frames and quotients have good reduction,
and normalize v_p(p)=1. Choose Neron differentials so
f_n*omega_n=lambda_n omega. The dual isogeny has etale kernel and
therefore unit differential multiplier mu_n. Its composite with f_n
is[p^n], giving lambda_n mu_n=p^n and v_p(lambda_n)=n. The coefficient
u_n=u_p(E_n) is integral by49.3. Formula(49.4) now gives, whenever the
difference is nonzero,

    v_p(h(E_n)−u_n)=v_p(h(E)−u_p(E))−n.           (49.5)

For all sufficiently large n the right side is negative. Since u_n is
integral, the ultrametric inequality is then an equality with the
negative term, so

    v_p(h(E_n))=v_p(h(E)−u_p(E))−n.

Thus disagreement with the integral tangent produces exactly linear
unbounded denominators in these good frames. Proving a uniform lower
bound for these valuations of the actual Hodge coefficients would
remove this disagreement, but no such lower bound has been deduced
from algebraicity or from(49.3). The global fields of the quotient
points are allowed to grow; no fixed-degree bound or integrality is
silently inserted. This is the exact remaining arithmetic map in this
attempt, and H1 is unchanged.

**49.5. Exact degree-two certificate.** If C is generated by(r,0),
where4r³−g2r−g3=0, put k=3r²−g2/4. Then

    X=x+k/(x−r),   Y=y(1−k/(x−r)²),
    g2′=60r²−4g2,  g3′=14g2r+22g3,
    f*xi′=2xi−r omega−d(y/(2(x−r))).

The self-contained symbolic program
`work/code_elliptic/check_isogeny_hodge_orbit.py` verifies the target
curve equation, the actual differential multiplier1, the exact
primitive in this formula, and the difference identity(49.4), using
independent indeterminates g2,r with g3=4r³−g2r. Its `.out` and `.json`
retain inputs, SHA256, timing and exit0 status. The arbitrary-order
proof above is by the actual elliptic-function identity and does not
rest on this finite specialization.

## 50. Ordinary cyclic isogeny branches and exact denominator averages

**50.1. Scope and actual local norm.** Continue49 with an ordinary good
elliptic curve E over a number field K, a fixed embedding K into Cp,
and p>3. In the attempted algebraic-h case enlarge K to contain the
actual complex coefficient h(E), and use this embedding for its
p-adic image. Exclude the finite set where that coefficient or the
chosen initial short model is nonintegral. The inverse-Verschiebung
slope u=u_p(E) is integral. If h=u all differences below vanish; for
the remaining case set b=v_p(h-u)>=0, with v_p(p)=1.

For each cyclic subgroup C of order p^n, take the finite flat closure
over a finite valuation extension where it and the good quotient are
defined. Choose a good short Weierstrass model of E_C=E/C, with Neron
differential omega_C, and put f_C*omega_C=lambda_C omega. Two such
short good frames differ by a unit scaling, so the negative valuation
of the resulting h_C is independent of this choice. This defines an
intrinsic local denominator norm in those Neron frames. It is not
identified with the height of a scalar obtained by unrelated global
frame choices.

**50.2. Connected depth and exact multiplier.** Over the algebraic
closure identify E[p^n] with (Z/p^n)^2, with the ordinary multiplicative
subgroup as the first axis. Put |C intersect E[p^n]_mu|=p^m. The
isogeny factors through this multiplicative intersection of degree
p^m; its dual is etale and hence has unit differential multiplier.
The first multiplier therefore has valuation m. The remaining kernel
maps isomorphically to its subgroup of the etale quotient: after
splitting the latter over a finite extension, the finite flat kernel
has rank one above each of its p^(n-m) generic points, and the same
rank on each corresponding base component, so each component is the
base itself. Thus this remaining isogeny is etale and its multiplier
is a unit. Consequently

    v_p(lambda_C)=m,
    v_p(h_C-u_p(E_C))=b+n-2m.                    (50.1)

The second equality is the actual map49.4. Since u_p(E_C) is integral,
the ultrametric inequality proves, with no cancellation exception,

    d_p(C):=max(0,-v_p(h_C))=max(0,2m-n-b).        (50.2)

When the right side is zero both summands are integral; when it is
positive the term h_C-u_p(E_C) has smaller valuation than u_p(E_C).

**50.3. Count every branch.** A cyclic subgroup of order p^n is a
primitive vector modulo multiplication by a unit. If its second
coordinate is a unit it has a unique representative(a,1), with a
arbitrary; these are the p^n subgroups with m=0. Otherwise its first
coordinate is a unit and its unique representative is(1,z), z in
pZ/p^n. For 1<=m<n, the vectors with v_p(z)=m number
(p-1)p^(n-m-1), and z=0 gives the unique depth-n branch. Thus

    N_(n,0)=p^n,
    N_(n,m)=(p-1)p^(n-m-1)  (1<=m<n),
    N_(n,n)=1,
    D_n=sum_m N_(n,m)=(p+1)p^(n-1).              (50.3)

This count is of actual cyclic subgroups, and (50.1) assigns the
corresponding valuation to each; no equidistribution assertion is
inserted.

**50.4. Exact average and actual Galois orbits.** Since b>=0, the sum
of (50.2) over all subgroups is at most

    S_n=sum_m N_(n,m)max(0,2m-n).

Direct finite-geometric summation gives

    S_(2r)=2(p^r-1)/(p-1),
    S_(2r+1)=((p+1)p^r-2)/(p-1).                 (50.4)

For completeness, writing k=n-m gives
S_n=n+(p-1)sum_(1<=k<n/2) p^(k-1)(n-2k).
Subtracting the same expression with n replaced by n-2 gives
S_n-S_(n-2)=2p^(n/2-1) for even n, and
S_n-S_(n-2)=(p+1)p^((n-3)/2) for odd n. The initial values S_1=1,
S_2=2 prove (50.4) for every n. In particular S_n/D_n tends to zero
at rate O_p(p^(-n/2)). The single fully connected branch has
contribution max(0,n-b), which is fully compatible with this average.

For non-CM E the actual image G_p of Gal(Qbar/K) has a finite index
I_p in GL2(Z_p). An opened original final-journal source giving the
stronger adelic bound is Lombardo2015, Corollary9.3, printedp2393
(also restatedp2348), with hypotheses E/K a non-CM elliptic curve over
a number field. The products theorem is not specialized to one
factor. Reduction modp^n has index at most I_p. For a transitive
finite G-set X and subgroup H of index at most I, the orbit of any
x has size |H|/|H intersect Stab_G(x)| >= |G|/(I|Stab_G(x)|)=|X|/I.
Apply this to the primitive cyclic lines. Every actual Galois orbit
O therefore has |O|>=D_n/I_p, and nonnegativity gives

    (1/|O|)sum_(C in O)d_p(C) <= I_p S_n/D_n.    (50.5)

Formula49.3 supplies the actual G_K compatibility in differential-
preserving algebraic frames. Passing to Neron frames in (50.5) uses
the indicated local norm and the unit-scaling invariance in50.1.
Thus (50.5) is a precise local contribution estimate. A global
height statement would also need a coherent metrized line and its
other places; none is silently supplied here. This calculation
establishes that this averaged denominator estimate does not
contradict the linear denominator on the connected tower. It neither
proves a global height bound nor removes the actual nonzero
algebraic-h gate.

**50.5. Primary source and finite certificate.** Opened the complete
final publisher PDF of Davide Lombardo, *Bounds for Serre's open
image theorem for elliptic curves over number fields*, Algebra &
Number Theory9(2015),2347--2395, DOI10.2140/ant.2015.9.2347,
https://msp.org/ant/2015/9-10/ant-v9-n10-p06-p.pdf . Exact inspected
locators: introduction printed2347, Corollary9.3 printed2393 and its
restatement2348; webrefs turn169172744view0, turn315315557view0.
Search record: system2 query 'Lombardo Bounds for index Galois image
elliptic curves number fields Theorem 1.1 pdf'; opened final journal
and used its numbering, rather than the earlier preprint's Theorem1.1.

`work/code_elliptic/check_isogeny_branch_denominators.py` independently
enumerates all primitive vectors and their actual cyclic subgroups
for p=3,n<=4 and p=5,7,n<=3; directly counts intersection sizes with
the first axis; verifies (50.3), (50.4), and fractional-b nonnegative
bounds. It also checks both finite sum identities for six primes and
1<=n<=100. Output, precise inputs, script SHA256 and timing are saved
in the adjacent `.out` and `.json`. The general proof is50.2--50.4.

## 51. Primary access recovered: Masser--Wustholz1983, exact direct substitution

**51.1. Access status superseding42.4 for these pages.** EuDML143029
and the Springer article remained unavailable, but the original GDZ
volume scan was obtained through the manifest advertised by
https://gdz.sub.uni-goettingen.de/id/PPN356556735_0072 . Its saved
manifest is `work/sources_elliptic/gdz_inventiones72_manifest.json`.
Article rangeLOG_0026 has canvases413--470; canvas number minus6 is
the printed page. The observed image service is
https://images.p.sub.uni-goettingen.de/iiif/image/gdz:PPN356556735_0072:00000413/full/1800,/0/default.jpg .
Only printed407--410 were downloaded and visually read, as
`work/sources_elliptic/masser_wustholz1983_gdz/p407.jpg` through
`p410.jpg`. The full58-page article is not represented as read.

**51.2. Opened source statement.** The Main Theorem, printed407--408,
uses a non-CM Weierstrass function with algebraic invariants, two
Q-linearly independent lists u_1,...,u_n and v_1,...,v_m, and explicit
lower bounds exp(-T^kappa), exp(-S^kappa) for their integer linear
forms at sufficiently large coefficient heights. Its size condition
is mn >= (2^(k+1)(k+7)+4kappa)(m+2n); the conclusion is algebraic
independence of at least k defined values wp(u_i v_j). Printed410
also records the earlier k=1 size condition mn>=m+2n without these
Diophantine estimates. This is the exact statement inspected, not an
inference from the title.

**51.3. The actual quotient-period substitution.** Set
u_i=eta_i-h omega_i=c conjugate(omega_i), i=1,2, and v_1=1/c;
use the algebraic conjugate elliptic curve's Weierstrass function.
Then u_i v_1=conjugate(omega_i), actual periods, so the corresponding
values are poles. The row list has Q-rank2, while the scalar list has
Q-rank1. Both lists satisfy the displayed lower-bound condition with
kappa=0: the period lattice is discrete with a real-linear invertible
basis, so the absolute value of a nonzero integer combination grows
at least a fixed positive multiple of its maximum coefficient; the
single scalar has the same property directly. The Main Theorem's
k=1 inequality reads2>=160 and fails; the quoted earlier condition
reads2>=5 and fails. Introducing the known algebraic torsion values
by replacing v_1 with rational multiples of1/c does not increase the
Q-rank of the scalar list, so it does not meet the hypothesis by
padding. This proves the failure of this specific direct
substitution. No statement that all other uses of this theorem fail
is asserted; the nonzero algebraic-h gate is unchanged.

## 52. Actual period-product logarithmic derivative and the G-function input

**52.1. Exact map for the fixed smallest curve.** The curve E_star
has three distinct real roots e1>e2>e3. Set delta=e1-e3>0 and
m=(e2-e3)/delta in(0,1), all algebraic. Write K=K(m), L=K(1-m),
E=E(m), J=E(1-m) for complete elliptic integrals in the parameter
convention of the retained normalization certificate. In the actual
oriented period basis,

    omega1=2K/sqrt(delta), omega2=2iL/sqrt(delta),
    eta1/omega1=delta(E/K-(2-m)/3),
    eta2/omega2=delta((1+m)/3-J/L).

These are precisely the already checked differential and period
normalizations; no second-kind class is replaced. As the first
period is real and the second purely imaginary, their two ratios
are h+c and h-c. Define the actual holomorphic function of m on a
simply connected subdomain of C minus{0,1}

    F(m)=K(m)K(1-m).

Differentiate the defining complete integrals, or integrate the
zero boundary term d(sin(theta)cos(theta)/sqrt(1-m sin²(theta))), to
obtain

    K'=(E-(1-m)K)/(2m(1-m)),
    L'=-(J-mL)/(2m(1-m)).

Their sum and difference give the exact formulas

    h=delta[m(1-m)F'/F-(2m-1)/3],
    c=delta*pi/(4F).                              (52.1)

The second identity follows equivalently from the retained Legendre
relation EK(1-m)+E(1-m)K-KK(1-m)=pi/2. When differentiating here,
delta is held fixed: this is the short-model family with roots
(2-m)delta/3, (2m-1)delta/3, -(1+m)delta/3. The chosen m gives the
original E_star exactly.

**52.2. Actual second jet and the retained scale.** Both K and L solve
Y''+pY'+qY=0, with

    p=(1-2m)/(m(1-m)), q=-1/(4m(1-m)).

Their actual Wronskian is W=K L'-K' L=-pi/(4m(1-m)). Direct
multiplication of this differential equation proves

    F'''+3pF''+(p'+4q+2p²)F'+(2q'+4pq)F=0,
    (F')²-2FF''-2pFF'-4qF²=W².                   (52.2)

For the second identity expand F'=K'L+KL' and use
F''=-pF'-2qF+2K'L'; its remaining term is exactly(KL'-K'L)².
Thus, at the actual algebraic m,

    F''/F = (r²-2pr-4q)/2
            - c²/(2delta²m²(1-m)²),
    r=F'/F=(h/delta+(2m-1)/3)/(m(1-m)).            (52.3)

In the proposed contradiction argument h is algebraic. Then r is
algebraic. The proved joint exclusion A.4.33 says that h and c
cannot both be algebraic; hence c² is transcendental in this case
(otherwise its square root c would be algebraic). The nonzero
coefficient of c² in(52.3) shows F''/F is transcendental. Consequently
there is no constant rescaling of this actual germ at m for which
all Taylor coefficients are algebraic: a nonzero algebraic constant
coefficient and algebraic second coefficient would make their ratio
F''/F algebraic. In particular the normalization F(m+z)/F(m) has
algebraic first jet but transcendental second jet in this argument.
This is an exact obstruction to the proposed ordinary G-function
input, with the nonalgebraic scale still visible.

There is an unconditional instance within the already proved CM
case: take m=1/2, where h=0. Here(52.3) is

    F''/F=2-8c²/delta²,

and A.4.33 again makes it transcendental. Thus an actual algebraic
Hodge coefficient does not supply an ordinary G-function germ of
the normalized period product, even for this explicit CM model.
The original germ at m=0 also cannot be used as an ordinary power
series: K(m) tends to pi/2 and K(1-m) is asymptotic to
-(1/2)log m, so F has a nonzero logarithmic term. The asymptotic
follows directly by comparing the endpoint portion of the second
complete integral with integral dt/sqrt(t²+m). These statements do
not rule out another value theorem or another explicitly constructed
input; none has been supplied by this calculation.

**52.3. Exact pointwise counterexample to an unrestricted G-function
specialization step.** For any positive integer M set

    G_M(z)=1+2log(1-2Mz)-log(1-3Mz).

Its Taylor coefficients for n>=1 are
(3^n-2^(n+1))M^n/n. They satisfy the G-function exponential size and
common-denominator conditions, and (1,G_M)^t solves the rational
Fuchsian system with matrix[[0,0],[R_M(z),0]], where

    R_M(z)=-4M/(1-2Mz)+3M/(1-3Mz).

This system has poles only at1/(2M),1/(3M), and a simple pole at
infinity. The function is transcendental: the residues2 and-1 of
its derivative give nonzero additive logarithmic monodromy, which
cannot occur for an algebraic function with finite branching. Thus
1,G_M are linearly independent over C(z). At the ordinary rational
point alpha=1/(4M), strictly inside its convergence disc,

    G_M(alpha)=1, G_M'(alpha)=4M.

The logarithm identity is exact on the real interval in question,
because both1-2Malpha and1-3Malpha are positive and their squares
satisfy(1-2Malpha)²=1-3Malpha. Hence an algebraic logarithmic
derivative at an ordinary algebraic point is compatible with an
actual transcendental G-function and a Fuchsian rational system.
This disproves the specific unrestricted specialization step; it
does not claim that the special elliptic product has the same
arithmetic behavior. Letting M grow also shows why shrinking an
evaluation point while changing the differential system supplies no
uniform small-point criterion.

**52.4. Exact primary-source scope.** The original G.V.Chudnovsky,
*On applications of diophantine approximations*, PNAS81(1984),
7261--7265, was accessed through PMC392122. Its PDF endpoint returned
a browser-check page, but original page images7261--7263 were
downloaded and visually read. Theorem I on printed7263 concerns
G-functions with rational coefficients in a rational differential
system and a rational evaluation point a/b, with the explicit form
of a smallness condition |b|>=c2|a|^(n(n+1)+epsilon); its conclusion
is rational linear independence. This direct rational-point
substitution does not cover m for E_star, whose absence of rational
Legendre parameters was proved in44.2. The constants' dependence
cannot be discarded through a rescaling.

Opened the full46-page Fischler--Rivoal author manuscript dated
5March2018 at
https://www.imo.universite-paris-saclay.fr/~stephane.fischler/gfndio.pdf .
Its own Theorem3 on p4 gives a growing dimension lower bound for the
specified infinite family of iterated-integral values F_n^[s](alpha).
No identification of that family with the actual period-product
second jet in(52.3) is provided by this statement. We do not infer
individual algebraic independence from that dimension bound.

Original Chudnovsky page-image provenance:
https://pmc.ncbi.nlm.nih.gov/articles/PMC392122/ , webref
turn970679339view0; observed CDN images saved in
`work/sources_elliptic/chudnovsky1984_pnas/p7261.png` through
`p7263.png`. Exact image refs turn557211950view1 and
turn872494908view0--1. The five-page full article is not claimed
read. Fischler--Rivoal fullref turn970679339view2. Search strings:
'G functions values linear independence rational points Bombieri
Chudnovsky theorem elliptic integrals' and 'algebraic independence
elliptic integrals first second kind products Legendre non CM G
functions Andre theorem'. The already retained normalized-pair and
Vergnaud estimates are not counted as new mathematical movement.

**52.5. Reproducibility.** The self-contained exact symbolic program
`work/code_elliptic/check_period_product_gfunction_route.py` ran
exit0 in0.649976871seconds. It verifies(52.1), the symmetric-square
operator and Wronskian identity, the second-jet coefficient of c²,
and the counterexample's point, derivatives, residues and first12
Taylor coefficients. Its adjacent `.json` and `.out` retain the
input, SHA256 and timing. None of these finite computations is a
transcendence proof. H1 remains unchanged.

## 53. The actual period-map two-jet: continuation of Sections43 and52

**53.1. Exact morphism to the elliptic period map.** Keep the actual
Legendre parameter and roots of Section52, with delta fixed. Put
M=m(1-m), p=(1-2m)/M, and tau=iL/K. The derivative is with respect
to the algebraic parameter m. The already proved Wronskian gives

    tau'=iW/K^2,  W=-pi/(4M),
    F=KL=tau W/tau'.

The nonvanishing of K,L,W on the chosen real interval justifies all
divisions. Differentiating the last identity, with W'/W=-p, proves

    r=F'/F=tau'/tau-tau''/tau'-p,
    c=-delta M tau'/tau,
    h=delta[M(tau'/tau-tau''/tau')+2(2m-1)/3].    (53.1)

In particular the two ratios are recovered exactly from h,c:

    tau'/tau=-c/(delta M),
    tau''/tau'=[2(2m-1)/3-(h+c)/delta]/M.         (53.2)

Thus the equation for h in the proposed algebraic-h argument is one
specific relation in the actual two-jet of tau. It does not supply
the other ratio in(53.2): that ratio includes the retained c. These
identities establish the map instead of identifying a Hodge
splitting with an algebraic period-map coordinate.

There is also an exact description of all coefficients of the
normalized actual period-product germ. At an algebraic m0 in(0,1),
write g(z)=F(m0+z)/F(m0), and let k_g be the field over Qbar generated
by all of its Taylor coefficients. The third-order equation(52.2)
is ordinary at m0, so recursive coefficient comparison gives

    k_g=Qbar(F'/F,F''/F)=Qbar(h,c^2).             (53.3)

For completeness, its leading coefficient is1 and its other
coefficients are rational functions of m with poles only at0,1.
The coefficient of g^{(n+3)}(0) is1 after differentiating n times;
all other terms use lower derivatives and algebraic values of
rational functions and their derivatives at m0. Induction therefore
places every coefficient in Qbar(r,s), where s=F''/F. Conversely r
and s/2 themselves are Taylor coefficients. Formula(52.3) and the
nonzero factors delta,M express h,c^2 in Qbar(r,s), and give the
reverse inclusion. This proves(53.3). It does not assert that h
alone is transcendental. The proved joint exclusion of h,c makes
this coefficient field nonalgebraic, including the CM examples.

**53.2. Rechecked scope of the already retained 2026 theorem.**
This source and its displayed R2 sign correction were already read in
Section43. The initial continuation message mistakenly called them a
new source discovery; that description is withdrawn. Reopened and
downloaded the complete final20-page publisher PDF of Benjamin
Bakker, Jonathan Pila and Jacob Tsimerman, *Periods in families and
derivatives of period maps*, J.Inst.Math.Jussieu25(6)(2026),
3187--3206, DOI10.1017/S1474748026101972. Theorem1.1 on
pp3189--3190 compares two subfields of the field of meromorphic
**germs** at a point of the complex base: the field generated by
period functions and the differential field generated by Hodge
filtration coordinates. Under its stated absence of an infinite
unitary tensor factor, the algebraic closures agree. Theorem3.9
p3196 gives the more general statement for a definable equivariant
map with Zariski-dense image, a finite-kernel group action and
norm-one monodromy eigenvalues at infinity. Its Definition2.1
p3191 makes the field of germs and the complex coefficient field
explicit. The final elliptic example, Sections4.2.1--4.2.5,
pp3202--3203, identifies the corresponding field up to algebraic
closure with C(tau,j,j',j'').

The actual family in(53.1) is the pullback of this elliptic family
through the algebraic Legendre j-function and the chosen algebraic
root scaling. Its Hodge filtration coordinate is tau, and the
Gauss--Manin derivatives of the actual periods are precisely the
ones used in(53.1). The theorem therefore does apply to its field
of germs. To see exactly why this application has supplied no
pointwise arithmetic conclusion, let O be the local analytic ring
at m0. Evaluation O->C has kernel the ideal of germs vanishing at
m0, including m-m0; it does not extend to a field map on the whole
meromorphic germ field, since 1/(m-m0) has a pole. Even when one
restricts an individual identity to germs holomorphic at m0, its
constants in this theorem already range over C. An equality of
these complex function fields consequently provides no bound on
the Qbar-algebraic degree of an individual evaluated ratio. Here
the evaluated data in(53.1)--(53.3) retain c^2 explicitly. No
pointwise arithmetic specialization theorem eliminating that entry
was found in the consulted statements. This is a verification of
this application, not a claim that no other use of the theorem can
address H1.

**53.3. Exact chain-rule correction in the consulted final source.**
The final publisher page3202 was also rendered and visually read,
not merely text-extracted. Section4.2.2 uses the period pair
sqrt(j'(tau)), tau sqrt(j'(tau)). If D_j=(1/j')D_tau, differentiation
gives exactly

    2D_j sqrt(j')=j''/(j')^(3/2)=R1,
    2D_j(tau sqrt(j'))=tau R1+2/sqrt(j').          (53.4)

The displayed R2 in Section4.2.3 has a minus in the final PDF. With
the periods and derivative stated immediately above it, (53.4)
proves that this sign must be plus. This is also checked directly
from the transformation law j'(gamma tau)=(c tau+d)^2j'(tau):
if R2 is the plus expression, then

    R1(gamma tau)=d R1+c R2,
    R2(gamma tau)=b R1+a R2,

for gamma=[[a,b],[c,d]], ad-bc=1 and a consistent local square-root
branch. These equalities follow by differentiating j' once more;
the second equality uses cb+1=ad. The algebraic-closure description
of the generated fields remains valid with the corrected
expression, since sqrt(j') and its inverse are already in the
field. We make no assertion that this local display invalidates
the main theorem. The Legendre proof(53.1) was derived independently
of this display.

**53.4. Source and certificate records.** Final source:
https://www.cambridge.org/core/services/aop-cambridge-core/content/view/0E049E0EA1AD619AB320C19B679494C2/S1474748026101972a.pdf/div-class-title-periods-in-families-and-derivatives-of-period-maps-div.pdf .
Opened webref turn738199086view0, exact theorem/find/open refs
turn844375289view0--3 and turn465240732view0--1. Local source
`work/sources_elliptic/bakker_pila_tsimerman2026_final.pdf/.txt`;
visual page `bakker_pila_tsimerman2026_p3202.png`. Search first
returned the title again via a query on derivatives of period maps;
the source was already retained in Section43 under the existing key
EllBakkerPilaTsimerman2026. This repeat access is not a new source or
mathematical advance. The final source, not the17-page2024 preprint,
supplies these locators. Original Bost--Charles1307.1045v2 was also reopened,
Theorem3.8(2) p17 and Corollary3.9 p18: these concern the full
de Rham--Betti comparison class. The actual class in Section46
has Betti matrix diag(-1/tau,tau), so its single zero cross-period
does not meet that full-vector hypothesis. This repeats no claim
of new movement in that earlier route.

The exact symbolic certificate
`work/code_elliptic/check_period_map_jet.py` passed11 identities,
exit0 external0.968628931seconds/internal0.286289598seconds. It
checks the actual tau/h/c derivatives, the source display's chain
rule and SL2 transformation, and recovery of the coefficient field
in(53.3). Inputs, SHA256, start and complete output are retained in
adjacent .json/.out files. H1's nonzero algebraic first-jet gate
remains unchanged.

## 54. The rational modular coordinate and invariant actual Taylor field

**54.1. A rational evaluation coordinate really exists.** The absence
of a rational Legendre parameter in Section44 does not imply that
all modular coordinates of E_star are irrational. Put

    D=1-m+m^2, M=m(1-m),
    u=1728/j=27M^2/(4D^3).

At E_star, j=110592/37 and therefore u0=37/64. The actual algebraic
base-change map has derivative

    du/dm=27M(1-2m)(2+M)/(4D^4).                (54.1)

It is nonzero at the relevant m: its only finite zeros outside
D=0 are0,1,1/2,-1,2, whose j values are either singular or1728;
E_star has neither value. Equivalently the retained exact degree-six
polynomial(44.3) is coprime to the numerator of(54.1). Thus a local
inverse m=m(u) is algebraic and has algebraic Taylor coefficients
at the rational point u0.

To identify an actual family, fix g2=4. The root difference is the
chosen positive algebraic branch delta(m), with

    delta(m)^2=3/D,
    delta'/delta=-(2m-1)/(2D).

In that family the product of its two actual holomorphic periods is
4iF(m)/delta(m), and the area on the real interval is4F(m)/delta(m).
Consequently the appropriate holomorphic product germ in the
rational coordinate is G(u)=F(m(u))/delta(m(u)), up to the indicated
constant factor. No second-kind differential has been changed in
this statement. Setting R_u=G'/G, with prime now d/du, the chain
rule and(52.1) give

    R_u=(r-delta'/delta)/(du/dm),
    h=delta{M[(du/dm)R_u+delta'/delta]-(2m-1)/3}. (54.2)

All coefficients of this affine relation at E_star are algebraic,
and its coefficient of R_u is nonzero. Thus this is an actual
rational-argument expression of the first-jet h gate; irrationality
of the Legendre parameter is not used as an obstruction here.

**54.2. Exact invariance under algebraic coordinate and gauge changes.**
Let g(z)=F(m0+z)/F(m0), and let A(w) be a formal power series over
Qbar with A(0)!=0. Let psi(w) be a formal series overQbar with
psi(0)=0 and psi'(0)!=0. Define

    g_new(w)=[A(w)/A(0)] g(psi(w)).

The field overQbar generated by its coefficients equals the field
of coefficients of g. One inclusion follows by multiplication and
composition of formal series with algebraic coefficients. For the
other, psi has a unique formal inverse with algebraic coefficients,
constructed recursively using its nonzero algebraic linear term;
A is invertible overQbar[[w]]. Composing g_new with that inverse
and multiplying by the inverse gauge recovers g. With(53.3) this
proves the exact equality

    Qbar(coefficients of g_new)=Qbar(h,c^2).     (54.3)

At the level of the first two derivatives, write
A(w)/A(0)=1+a1 w+a2 w^2/2+..., psi(w)=p1w+p2w^2/2+...,
and g(z)=1+r z+s z^2/2+.... Then

    r_new=a1+p1 r,
    s_new=a2+2a1p1 r+p2 r+p1^2 s.              (54.4)

The coefficient of s is nonzero. In the actual algebraic-h
contradiction argument r is algebraic and s is transcendental by
A.4.39; hence(54.4) keeps the first derivative algebraic and the
second transcendental after every such coordinate/gauge change.
In particular this applies to(54.2), with
A=delta(m0)/delta(m(u0+w)) and psi=m(u0+w)-m0. The actual
normalized period-product germ in the rational modular coordinate
therefore still fails the algebraic-coefficient condition for an
ordinary G-function. Unconditionally(54.3) and the proved joint
h,c exclusion show that the coefficient field is nonalgebraic.
These statements concern this explicitly transported actual
product. They do not exclude a different G-function input or a
value theorem with logarithmic solutions and its own verified
hypotheses. No first-jet transcendence has been proved.

**54.3. Finite certificate.** The exact program
work/code_elliptic/check_modular_coordinate_jet.py ran exit0,
external1.097872519seconds/internal0.277045537seconds, with9
identities: u*j=1728, derivative(54.1), exact u0=37/64 under the
Legendre polynomial, its coprimality/nonramification, physical
product h recovery, and both generic jet transformations. The
adjacent .out/.json retain all input data, SHA and actual timing.
Formal-field equality(54.3) is proved by the infinite inverse-series
argument, not inferred from this finite check. H1 remains unchanged.
