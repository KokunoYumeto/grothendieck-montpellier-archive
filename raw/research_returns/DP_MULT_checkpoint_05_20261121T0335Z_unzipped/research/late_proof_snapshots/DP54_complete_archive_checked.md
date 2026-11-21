# DP54 — global algebraic realization of finite sharp theta jets

Date: 2026-11-21 UTC. Author: `/root/formal_bound`, GPT-6 Astra Pro; reasoning effort is not exposed. This memo proves an existence statement for global sections at varying tensor powers. It gives no uniform estimate for those powers, the heights of the sections, or the costs of a theta-lift chain.

## 1. Statement and exact geometric setting

Use the actual Jacobian, good model, polarization and trace-one endomorphism of DP49:

\[
p=11,\qquad R=W(\mathbf F_{11^3}),\qquad
K=\operatorname{Frac}R,\qquad
J=\operatorname{Jac}(y^2=x^7-1),
\]

\[
w_0=-(a+a^2+a^4),\qquad
w_0+w_0^\dagger=1,\qquad
\mathcal L=(1,w_0)^*\mathcal P_\lambda.
\tag{FJ1}
\]

Here \(a\) is the integral seventh-root automorphism and \(\lambda\) is the canonical principal polarization. DP49 proves that the associated homomorphism of \(\mathcal L\) is **\(\lambda\) with its actual positive sign**. We prove below that \(\mathcal L\) is relatively ample.

Choose the invariant product canonical gauge of DP47–DP49. In an integral formal frame of \(\mathcal L\) at zero, the normalized germ of a section \(s\) of \(\mathcal L^{\otimes\kappa}\), with algebraic coefficient \(f_s\), is

\[
\Theta_s(z)=f_s(z)\,U(z)^\kappa B(z)^{-\kappa},
\qquad U\in 1+(z)R[[z]],\qquad B=\exp b.
\tag{FJ2}
\]

The coordinates \(z\) are integral coordinates on \(\widehat J=G\times G^D\). The actual primitive Poincaré splitting \(B\) is that of the arbitrary-unit display in DP46, and \(b(0)=0\). The integral unit \(U\) is the actual frame correction in DP47; no integrality of \(B\) is assumed. Write \(E\) for the inverse normalized group logarithm and \(\beta=b\circ E\).

Let \(n\ge0\). A finite jet functional means any \(K\)-linear functional on the quotient of formal series by total degree \(n+1\). This includes an invariant differential polynomial at zero, expressed as a constant-coefficient differential polynomial after composition with \(E\), and includes a restriction to a specified integral logarithmic line followed by an ordinary derivative of order at most \(n\).

**DP54(a), exact finite jets over the complete valuation ring.** For every \(n\) there is an integer \(\kappa_0(n)\) such that, for every integer \(\kappa\ge\kappa_0(n)\), there exists a global integral section

\[
s_\kappa\in H^0(J,\mathcal L^{\otimes\kappa})
\]

whose normalized logarithmic germ satisfies

\[
\Theta_{s_\kappa}(E(Z))
\equiv\exp(-\kappa\beta(Z))\pmod{(Z)^{n+1}}.
\tag{FJ3}
\]

The section is nonzero and its algebraic prefactor is a unit at zero. The same section used in any fixed finite number of formal copies has the product pure-kernel jet through total degree \(n\).

**DP54(b), square tensor powers preserving a selected valuation.** Fix finitely many finite jet functionals, on one or several copies, whose values on the product primitive kernel with exponent \(-1\) are nonzero. There is an integer \(B_0\) such that for every sufficiently large positive integer

\[
M\equiv1\pmod{11^{B_0}},\qquad \kappa=M^2,
\tag{FJ4}
\]

one can choose \(s_{M^2}\) as in (a), and every selected value has exactly the same \(11\)-adic valuation as its pure-kernel value at exponent \(-1\). A source factor \(M^{-n}\) for a homogeneous degree-\(n\) functional preserves this valuation.

**DP54(c), sharp sequences realized by algebraic sections.** Each pure-kernel sharp sequence in DP42/DP46, and the first-negative-row two-column harmonic sharp sequence of DP51 when applied to this actual arbitrary-unit pair, is realized in valuation by global sections of powers \(\mathcal L^{\otimes M_n^2}\), with \(11\nmid M_n\). The tensor power and section may depend on the selected degree. The ordinary primitive-line rates in this example are therefore \(1/1220\) and \(1/120\) along such sequences; the source-shaped first-negative-row two-column harmonic rate is \(1/1220\).

The sections may additionally be chosen over the number field \(\mathbf Q(\zeta_7)\), integral at the selected prime over 11, while preserving all the selected finite valuations. That arithmetic refinement uses approximation and is not an assertion of exact equality of the entire prescribed jet over the number field.

## 2. Why this trace-one line is relatively ample

Work first on the geometric closed fibre \(\overline J\). Let \(\mathcal T\) be an ample theta line inducing the canonical principal polarization. The calculation in DP49 gives

\[
\phi_{\mathcal L_{\overline k}}=\phi_{\mathcal T}=\lambda_{\overline k}.
\]

Consequently \(\mathcal N=\mathcal L_{\overline k}\otimes\mathcal T^{-1}\) has \(\phi_{\mathcal N}=0\), so \(\mathcal N\in\operatorname{Pic}^0(\overline J)\). The precise known facts are Milne, *Abelian Varieties*, in *Arithmetic Geometry* (1986), Proposition 9.2, pp.117–118, and the definition immediately following it on p.118. For an ample line over an algebraically closed field, Proposition 10.1, p.119, says that

\[
\phi_{\mathcal T}:\overline J(\overline k)
\longrightarrow\operatorname{Pic}^0(\overline J)
\]

is surjective. Choose \(c\) with \(\mathcal N\cong t_c^*\mathcal T\otimes\mathcal T^{-1}\). Then

\[
\mathcal L_{\overline k}\cong t_c^*\mathcal T,
\]

which is ample. Ampleness descends under an extension of the ground field by Stacks Project Lemma 35.25.6 in [Tag 02LB](https://stacks.math.columbia.edu/tag/02LB), applied to this faithfully flat base change. Thus the closed-fibre line is ample.

Stacks Project Lemma 30.21.4, Tag [0D2N](https://stacks.math.columbia.edu/tag/0D2N), then gives relative ampleness on an open neighbourhood of the closed point of \(\operatorname{Spec}R\). Every such neighbourhood is the whole spectrum, because \(R\) is local. Hence \(\mathcal L\) is relatively ample on \(J/R\), and is ample on \(J\) since the base is affine.

This reasoning uses equality with the positive principal polarization. It does not use the false implication that any line whose associated homomorphism is an isogeny must be ample.

## 3. Integral finite-jet extension

Let \(e:\operatorname{Spec}R\to J\) be the zero section and \(I\) its ideal sheaf. Put

\[
Z_n=V(I^{n+1}).
\]

Smoothness and the chosen formal parameters identify its coordinate ring with

\[
R[[z_1,z_2,z_3]]/(z_1,z_2,z_3)^{n+1}.
\tag{FJ5}
\]

In particular it is a finite free \(R\)-module. One can also see this directly from the filtration whose quotients are the symmetric powers of the free conormal module of the zero section. A formal frame restricts to a genuine frame on the finite thickening \(Z_n\): this uses only the quotient by \(I^{n+1}\), not any algebraization of an infinite formal frame.

The sheaf \(I^{n+1}\) is coherent. Serre vanishing in the precise form of Stacks Project Lemma 30.16.1(4), Tag [0B5T](https://stacks.math.columbia.edu/tag/0B5T), gives

\[
H^1(J,I^{n+1}\otimes\mathcal L^{\otimes\kappa})=0
\quad\text{for every }\kappa\ge\kappa_0(n).
\tag{FJ6}
\]

Equivalently one may use the relative version, Lemma 30.16.2, Tag [02O1](https://stacks.math.columbia.edu/tag/02O1), over this affine base. The restriction exact sequence now gives a surjection of **integral** modules

\[
H^0(J,\mathcal L^{\otimes\kappa})
\twoheadrightarrow
H^0(Z_n,\mathcal L^{\otimes\kappa}|_{Z_n}).
\tag{FJ7}
\]

Prescribe, in the restricted integral frame, the target coefficient

\[
f_{s_\kappa}\equiv U^{-\kappa}\pmod{I^{n+1}}.
\tag{FJ8}
\]

This is an integral target because \(U\) is an integral unit and \(\kappa\) is an integer. Lift it by (FJ7). Its value at zero is one, so its lift is nonzero. Multiplying by \(U^\kappa\) gives \(1+I^{n+1}\).

Substitution by \(E\) has zero constant term and identity linear term, so it preserves the ideal of terms of total degree at least \(n+1\), even though its coefficients need not be integral. Multiplication by \(\exp(-\kappa\beta)\), which has constant term one and no negative-degree terms, also preserves this ideal. These two facts prove (FJ3).

For \(r\) copies, the product of the \(r\) prefactors is \(1\) modulo total degree \(n+1\). Indeed every nonconstant error term from any one copy already has degree at least \(n+1\). Thus the same lift controls any differential functional of total degree at most \(n\) on that product. This proves DP54(a).

## 4. Dependence on the tensor exponent and the square-level choice

Fix a finite jet functional \(\ell\) of order at most \(n\) on \(r\) copies, and put

\[
F_\ell(T)=\ell\left(
\exp\left[-T\sum_{b=1}^r\beta(Z^{(b)})\right]
\right).
\tag{FJ9}
\]

This is a polynomial in \(T\) with coefficients in \(K\). To prove that assertion, set \(\gamma=\sum_b\beta(Z^{(b)})\). Since \(\gamma\) has zero constant term, \(\gamma^m\) has total degree at least \(m\); hence only \(0\le m\le n\) in

\[
\exp(-T\gamma)=\sum_{m\ge0}\frac{(-T)^m\gamma^m}{m!}
\]

can contribute. There are finitely many coefficients and therefore a finite lower bound on their valuations. This argument includes invariant derivatives after logarithmic substitution, ordinary specified-line derivatives, and the two-column harmonic differential polynomials, all interpreted as the stated finite linear functional.

Suppose \(F_\ell(1)\ne0\), and let \(m_\ell\) be the minimum of the valuations of the nonzero coefficients of \(F_\ell\). For an integer \(T\equiv1\pmod{11^B}\),

\[
v_{11}(F_\ell(T)-F_\ell(1))\ge B+m_\ell,
\tag{FJ10}
\]

because \(T^a-1\) is divisible by \(11^B\) for every positive integer \(a\). Choose \(B\) so that

\[
B+m_\ell>v_{11}(F_\ell(1)).
\tag{FJ11}
\]

The ultrametric inequality then gives

\[
v_{11}(F_\ell(T))=v_{11}(F_\ell(1)).
\tag{FJ12}
\]

For finitely many selected functionals with nonzero value at one, use the maximum of the finitely many required bounds in (FJ11). There are arbitrarily large positive integers \(M\equiv1\pmod{11^B}\). Choose any such \(M\) with \(M^2\ge\kappa_0(n)\). Then \(T=M^2\equiv1\pmod{11^B}\), so (FJ12) and the exact-jet realization in §3 prove all the simultaneous valuation assertions.

For a homogeneous degree-\(n\) differential polynomial, the source normalization \(M^{-n}\) has valuation zero because \(11\nmid M\). The exact source locator is `IsThRule.lean`, definition `thExpr`, lines 66–70: the tensor exponent is \(M^2\), and the degree normalization is \(M^{-\deg P}\). Thus the square-tensor realization is compatible with those two numerical operations. It does not by itself instantiate the source's other geometric or translated-family inputs. This proves DP54(b).

## 5. Consequences for sharp ordinary and harmonic sequences

Fix one primitive logarithmic line \((X,Y)=(ut,vt)\) on the actual pair of DP49. Take the pure kernel with exponent \(-1\). DP46 gives its exact coefficient radius and hence

\[
\liminf_{n\to\infty}
\frac{v_{11}(n![t^n]\exp[-\beta(ut,vt)])}{n}=c_k,
\tag{FJ13}
\]

where \(c_2=1/1220\) if the first dual coordinate is a unit and \(c_1=1/120\) if the first dual coordinate is divisible by 11 and the second is a unit. There are therefore degrees \(n_\nu\to\infty\) with nonzero selected value and quotient tending to the indicated finite rate. Apply DP54(b) separately to each of these finite derivatives. The resulting global sections and integers \(M_\nu\) satisfy

\[
\lim_{\nu\to\infty}\frac1{n_\nu}
v_{11}\left(
M_\nu^{-n_\nu}
\frac{d^{n_\nu}}{dt^{n_\nu}}
\Theta_{s_{M_\nu^2}}(E(ut,vt))\bigg|_{t=0}
\right)=c_k.
\tag{FJ14}
\]

For the DP51 two-column family, take the first dual row, corresponding here to \(j=1\), and use

\[
P_{a,b}=\sum_{i=0}^{\min(a,b)}(-1)^i
\binom ai\binom bi
X_1^{a-i}Y_{1,1}^{b-i}X_2^iY_{1,2}^i.
\tag{FJ15}
\]

DP51 proves the summed harmonicity and the source `HaO` row conditions, and supplies a sequence \(a_\nu+b_\nu\to\infty\) whose pure-kernel values are nonzero and have valuation divided by \(a_\nu+b_\nu\) tending to \(1/1220\). The same proof applies to the arbitrary-unit display in DP46: it uses only the same unique initial monomial with a unit coefficient, the positive gap to the other terms, and the already proved primitive-path radius, all unchanged there. Alternatively this is precisely the unit-arrow application of the DP51 statement used here.

Use two copies of the same section supplied by §3, with \(n=a_\nu+b_\nu\), and then the tensor congruence of §4. The product normalized section has the same finite \(P_{a_\nu,b_\nu}\) value in valuation as the pure exponent-\(-1\) product. This proves the harmonic assertion in DP54(c). These are global sections evaluated at the two formal identity copies. No assertion is made that these sections belong to a prescribed translated or Heisenberg family in the recovered source.

The limits (FJ14) and its harmonic counterpart concern a sequence of triples `(section, tensor power, derivative order)`. They are not the asymptotic derivative sequence of one fixed global section or one fixed tensor power.

## 6. Number-field sections with the same finite valuations

This optional strengthening removes a possible ambiguity in the word “global.” The exact-jet sections above are global on an abelian scheme over the complete DVR. Their finite selected valuations can also be realized by global algebraic sections over a number field.

Let \(E_0=\mathbf Q(\zeta_7)\), let \(\mathfrak p\mid11\) be the prime corresponding to the chosen embedding, and put \(R_0=\mathcal O_{E_0,\mathfrak p}\). Its completion is the ring \(R\) above, because the residue degree is three and 11 is unramified. The curve, its Jacobian, the polarization, \(a\), \(w_0\), and \(\mathcal L\) are defined over this ring; the good integral curve construction and the algebraic expressions in DP49 supply these data. Fix one tensor power \(\kappa=M^2\) already chosen in §4.

Set \(V_0=H^0(J_{R_0},\mathcal L^{\otimes\kappa})\). This is a finite torsion-free \(R_0\)-module, hence free. Finiteness is proper coherent cohomology; torsion-freeness follows because multiplication by 11 is injective on the invertible sheaf on the flat scheme \(J_{R_0}\), and therefore on its global sections. Flat base change, Stacks Project Lemma 30.5.2(2), Tag [02KH](https://stacks.math.columbia.edu/tag/02KH), gives

\[
V_0\otimes_{R_0}R
=H^0(J,\mathcal L^{\otimes\kappa}).
\tag{FJ16}
\]

Since \(R_0\) is dense in its completion, \(V_0\) is dense in the right-hand side in any chosen finite free basis. Every fixed finite jet evaluation is continuous on this finite-dimensional space: in a local frame it is a finite linear combination of coefficients; a finite product of section germs gives a finite polynomial expression in those coordinates. Its coefficients lie in \(K\), with a finite denominator bound. Therefore a sufficiently close section from \(V_0\) preserves each prescribed nonzero valuation, as well as the unit value of the algebraic prefactor at zero.

The approximating section is defined over \(E_0\) and is integral at \(\mathfrak p\). It need not have exactly the prescribed formal jet; equality of the finitely many selected valuations is what the argument proves. It also gives no height bound or simultaneous integrality assertion at unspecified other primes. If one clears finitely many denominators away from \(\mathfrak p\), the clearing scalar can be chosen outside \(\mathfrak p\), so it leaves these local valuations unchanged.

## 7. Precisely what is and is not resolved

The pure prefactor \(1\) examples are realized to every fixed relevant order by genuine global sections of sufficiently large powers of the actual ample trace-one theta line. The square-level and tensor-exponent conditions do not prevent this realization at the selected good prime, and the finite valuations can be realized by number-field sections.

The proof supplies neither a bound on \(\kappa_0(n)\) nor a bound on the congruence exponent in (FJ11), the heights or norms of the lifts, or the global cost of taking \(M\) large. It does not produce an integral basis of translates, instantiate a prescribed `IsVtOver`/theta-lift family, verify endpoint period assumptions, or select a new admissible shorter chain. It also does not permit one to exchange the varying-power sequence in §5 with a fixed-power asymptotic statement.

The remaining issue after this theorem is therefore quantitative and source-specific: whether a prescribed global family can provide the required jets, nonvanishing and estimates at controlled tensor/level and archimedean cost. It is no longer the bare existence of global algebraic theta sections with each individual sharp finite jet.

## 8. Primary locators and actual checks

* J. S. Milne, “Abelian Varieties,” in *Arithmetic Geometry*, Springer, 1986: Proposition 9.2, pp.117–118; definition of \(\operatorname{Pic}^0\), p.118; Proposition 10.1, p.119. Official author PDF: <https://www.jmilne.org/math/articles/1986b.pdf>. The original printed pages 117–119 were visually read in this pass. The local PDF and page images are in `research/serre_sources/`.
* Stacks Project, Lemma 30.21.4, Tag 0D2N: closed-fibre ampleness spreads to an open neighbourhood. Its hypotheses are properness over a noetherian base and an invertible sheaf.
* Stacks Project, Lemma 35.25.6, in Tag 02LB: relative ampleness of a fixed line bundle descends under an fpqc covering; this gives the ground-field descent in §2.
* Stacks Project, Lemma 30.16.1(4), Tag 0B5T, or Lemma 30.16.2, Tag 02O1: Serre vanishing in the precise proper/ample/coherent setting used in §3. The known vanishing theorem is cited, not reproved.
* Stacks Project, Lemma 30.5.2(2), Tag 02KH: flat cohomology base change, used only in §6.
* Actual geometry and formal normalization: DP49, §§1, 4–5; DP47, §§1–4; arbitrary-unit primitive kernel: DP46; selected harmonic sharp family: DP51. Source `IsThRule.lean`, `thExpr`, lines 66–70, fixes the tensor exponent and level normalization as recorded in DP50.

The proof and source-check metadata are saved separately. No Lean compilation, machine formalization, or numerical experiment is claimed.
