# AM-K034 — complete prime-to-11 torsion gauges and sharp selected auxiliary content

Author: GPT-6 Astra Pro, ALP_MACHINE /root/kummer_extension, 22 November 2026 UTC; inherited reasoning effort not separately exposed.

This finding proves the full formal-germ comparison that was deliberately absent from AM-DO-030. A prime-to-11 torsion translation has an integral horizontal difference-line frame, and this is the difference frame of the actual reduced theta translation. Consequently a fixed nonzero auxiliary finite Heisenberg operator preserves the complete selected local image ideal, up to the coefficient content of that operator. Combined with AM-K033 and simultaneous interpolation in the actual DP59 half-orbit, this transfers the sharp selected slope \(1/1220\) to the fixed finite Steinberg family of AM-DO-034. No integrality of a Chern-reduced ample-line frame, no theta-null unit, and no saturation of a later automorphic image is asserted.

## 1. The two frames and their actual connections

Let R be a complete DVR of mixed characteristic \((0,11)\), with \(v(11)=1\). The actual data below may first be defined over a number field and then completed at11. Finite coefficient extensions are allowed; no extension is claimed unramified when its extra scalar coefficients require ramification. Let \(X/R\) be an abelian scheme, \(\mathcal L\) a symmetric rigidified relatively ample line, and let its complex realization carry the translation-invariant positive Hermitian form H. In our application \(X\) is an ordinary power of J and \(\mathcal L\) is its product principal line.

Fix an integer \(\kappa\), a positive odd integer d prime to11, and a section \(t\in X[d](R)\). Denote translation by \(T_t\). The rigidified degree-zero difference line is

\[
 \mathcal Q_t=
 T_t^*(\mathcal L^\kappa)\otimes\mathcal L^{-\kappa}
       \otimes p^*(t^*\mathcal L^\kappa)^{-1},
 \qquad p:X\longrightarrow\operatorname{Spec}R.
\tag{TG1}
\]

The displayed rigidification uses the given one on \(0^*\mathcal L\). The polarization homomorphism and the rigidified theorem of the square identify \(\mathcal Q_t\) with the value at \(\kappa t\) of the Poincare family. Therefore it has a rigidification-preserving isomorphism

\[
                 \vartheta_t:\mathcal Q_t^{\otimes d}
                                     \overset{\sim}{\longrightarrow}\mathcal O_X.
\tag{TG2}
\]

This isomorphism is unique after its origin value has been fixed. Indeed two such isomorphisms differ by a global unit on the proper geometrically connected abelian scheme, hence by a unit of R, and the rigidification fixes it. We use that uniqueness, rather than an unspecified line-translation isomorphism, below.

### Lemma TG3. Integral torsion horizontal frame

There is a unique integrable connection on \(\mathcal Q_t\) for which (TG2) is horizontal. Its origin-normalized horizontal frame on the formal completion \(\widehat X_0\) is an integral frame. If q is an integral formal frame with origin value1 and

\[
                  a=\vartheta_t(q^{\otimes d})\in
                    1+\mathfrak m_0R[[z_1,\ldots,z_g]],
\tag{TG3}
\]

where \(\mathfrak m_0=(z_1,\ldots,z_g)\), then that frame is exactly

\[
                  q_{\mathrm{hor}}=a^{-1/d}q.
\tag{TG4}
\]

Here \(a^{-1/d}\) means the unique formal d-th root with constant1. It and its inverse belong to \(R[[z]]^\times\).

**Proof.** On a local integral frame q define
\[
                        \nabla q=\frac1d\,d\log(a)\,q.
\tag{TG5}
\]
This glues under a frame change \(q'=bq\), since \(a'=b^d a\). Because d is a unit and a is a local unit, this is an integral algebraic connection; it is integrable by the displayed formula. Any connection making (TG2) horizontal must have (TG5), proving uniqueness.

The recursive coefficient equation for \(b^d=a^{-1}\), \(b(0)=1\), has at each positive total degree the new coefficient multiplied by d and all other terms already determined in R. Since d is a unit, it has a unique solution in \(1+\mathfrak m_0R[[z]]\). This argument works in several variables and in ramified R. Differentiating \(b^d a=1\) gives \(\nabla(bq)=0\), proving (TG4). No division by a theta section or by one of its values occurs. ∎

### Lemma TG6. This is the connection in the actual reduced translation

Write the reduced translation of a coefficient function F as

\[
 U_t^{\kappa H}F(u)=
   \exp\!\left(-\pi\kappa H(u,t)
                 -\frac{\pi\kappa}{2}H(t,t)\right)F(u+t).
\tag{TG6}
\]

After normalizing the difference-line fibre at0, the difference frame between this reduced translated frame and the original reduced frame is exactly the horizontal frame of Lemma TG3. In particular its complete formal ratio to an integral difference-line frame is the unit in (TG4). This is equality of normalized connections and full germs.

**Proof.** Use the first-argument-linear convention for H. The original reduced coefficient multiplier is
\[
 j_\kappa(\lambda,u)=\alpha(\lambda)^\kappa
       \exp\!\left(\pi\kappa H(u,\lambda)
                      +\frac{\pi\kappa}{2}H(\lambda,\lambda)\right).
\tag{TG7}
\]
A substitution into (TG6) shows that its multiplier is
\[
 j_\kappa(\lambda,u)\,\chi_t(\lambda),\qquad
 \chi_t(\lambda)=
       \exp\!\left(\pi\kappa\{H(t,\lambda)-H(\lambda,t)\}\right).
\tag{TG8}
\]
The second factor is constant in u and has absolute value1. Since \(dt\in\Lambda\) and \(\operatorname{Im}H\) is integral on \(\Lambda\), one has \(\chi_t(\lambda)^d=1\).

The reduced frame of the ample line has squared norm \(\exp(-\pi\kappa H(u,u))\). In the translated frame specified by (TG6), its metric is the same function: the frame multiplier is
\(\exp(\pi\kappa H(u,t)+\pi\kappa H(t,t)/2)\), whose absolute square cancels the cross and constant terms in \(\exp(-\pi\kappa H(u+t,u+t))\). The quotient frame of the rigidified line (TG1) consequently has constant norm1. It is horizontal for its flat Chern connection.

Moreover its d-th tensor power is a global holomorphic nowhere-vanishing frame of \(\mathcal Q_t^d\), since \(\chi_t^d=1\). Compare it with (TG2). Their quotient is a global holomorphic unit on the compact complex torus, hence a constant; the origin rigidification makes that constant1. Thus the actual reduced quotient frame is horizontal for exactly the connection making (TG2) horizontal. By the uniqueness in Lemma TG3 it is that connection, including its normalized formal frame.

For completeness, this comparison does not require a possibly nonconvergent integral formal frame to be evaluated over the complex numbers. Compare the algebraic torsion connection and an algebraic reference local frame after complex base change. The equality just proved descends to their finite algebraic jets. Complete at11 and then change to any integral formal frame; (TG3)–(TG5) give the resulting complete formal equality. ∎

The formal root is integral in **integral algebraic parameters**. Its expression in invariant logarithmic coordinates need not have integral divided Taylor coefficients. Similarly the original ample-line reduced frame is not claimed integral. Lemma TG6 concerns only the prime-to-11 torsion difference line and does not contradict the THETA3 C11/C19 counterexamples.

### Actual fibre normalization

The origin normalization in Lemma TG6 must be compared with the one in the actual finite Heisenberg reading. AM-DO-030, section2, supplies this comparison: pull back by an integer prime to11 killing the torsion, use the relative symmetric theta-group lift of accepted DP62, and descend through the resulting formal etale isomorphism. Its finite-order scalar is an11-unit. One may use \(2d\) instead of d throughout this auxiliary comparison; both are11-units, and this also matches the \(2d\)-divisibility in the primary Mumford construction. It changes no level or source parity condition.

Thus the actual scalar is an11-unit, rather than an unrecorded nonzero scalar. The complete connection comparison in Lemma TG6 is the additional argument beyond DO030's fibre statement. There is no assumption that \(t\in K(\mathcal L^\kappa)\), and no claim that translation by t acts globally as a theta-group automorphism of \(\mathcal L^\kappa\).

The precise primary comparison is Bannai and Kobayashi (2010), author preprint arXiv:math/0610163v4, section1.3, formulas (14) and the definition of \(U^M_{v_0}\), PDF pp.14–15; Proposition2.3, PDF pp.21–22, with the abelian-scheme observation following Corollary2.4; Lemma2.7 and Proposition2.8, PDF pp.24–25. The latter identify this normalized reduced translation with Mumford's algebraic translation. No ordinary-reduction integrality theorem from that paper is used here.

## 2. Equality of the complete translated coefficient modules

Now take the actual ordinary J-product, with the full source gauge already identified in AM-K018. Write its accepted primitive logarithm as \(\beta_{\mathrm{prod}}\), and let \(U_0\) denote the integral normalized frame factor. In an actual integral formal frame, the complete reduced coefficient module of \(\mathcal L^\kappa\) at0 is

\[
 \mathscr C_\kappa=
 U_0^\kappa\exp(-\kappa\beta_{\mathrm{prod}})
                    R[[z_1,\ldots,z_g]].
\tag{TG9}
\]

All series are compared through the same invariant tangent coordinates. The coordinates z inside \(R[[z]]\) are algebraic formal parameters; the logarithmic variables used for differentiation are distinguished from them.

### Proposition TG10. Translated modules agree

For each prime-to-11 torsion point t, take every integral formal section near t, translate it to0 by the **actual** reduced operator (TG6), and include the finite Heisenberg fibre scalar fixed above. The resulting complete coefficient module is exactly \(\mathscr C_\kappa\).

**Proof.** Translation identifies the formal neighbourhood of t with \(\widehat X_0\) over R. Choose integral frames of \(\mathcal L^\kappa\) near0 and t, and a primitive integral vector in \(t^*\mathcal L^\kappa\). Their difference is an integral frame q of (TG1), up to an integral unit. By Lemma TG6 its reduced difference frame is \(a^{-1/d}q\); by the actual fibre comparison its remaining constant is an11-unit. Hence the translated reduced coefficient of an arbitrary integral local section is
\[
 c_t\,h_t(z)\,
        U_0^\kappa\exp(-\kappa\beta_{\mathrm{prod}})\,f(z),
       \qquad c_t\in R^\times,\quad h_t\in R[[z]]^\times,
       \quad f\in R[[z]].
\tag{TG11}
\]
Every f occurs. Multiplication by \(c_th_t\) is an automorphism of the complete formal function module and of every finite jet quotient. This proves equality in (TG9), not only an inclusion or equality of their leading terms. The signs of \(h_t\) depend on which integral frame is called q; either sign is an integral unit, and the normalized connection comparison has already fixed the actual reduced operator. ∎

This application uses the actual Chern/source-gauge equality of K018 on the **untranslated** ordinary product, and the explicit reduced translation (TG6) on the translated line. It does not invoke CM invariance at the translated point, which is generally false. It does not replace the integral connection in Lemma TG3 with an arbitrary holomorphic connection on a torsion line.

## 3. Exact auxiliary selected image ideal

Use the enlarged hosts of AM-K033: h=1 or4, \(f=42h\), with actual principal variety \(A=J^{14h}\). Fix a source edge a to b, the fixed residual selected partitions, the explicit polynomials \(P_r\), and degrees

\[
                  T_r=122\,11^r+D_0
\tag{TG12}
\]

from K033(CS20–24). The full numerical Hyp3 preservation, exact source-and-target Cauchy summand, and growing first-row weights remain exactly those proved there.

Fix a nonzero auxiliary finite operator supported away from11 and29, in DO030's combined form

\[
 \mathcal O=\sum_{j=1}^{s}b_j W_{y_j},\qquad
 b_j\ne0,\qquad
 \mathcal O\phi_0\ne0,
 \qquad t_j\in X[d]\ \text{distinct},
 \quad X=A^{ab}.
\tag{TG13}
\]

Here d is odd and prime to \(11\cdot29\). The distinct classes are the classes after DO030's actual lattice phases have been combined. Set

\[
 \eta=\min_j v(b_j),\qquad
                    \mathfrak b=(b_1,\ldots,b_s)\subset\operatorname{Frac}(R).
\tag{TG14}
\]

The coefficients and operator are fixed as r varies. Put \(M=29^e\), \(\kappa=M^2\), and \(\alpha=(1+2\sqrt{-7})^e\). Choose

\[
                   M\ge 3s(T_r+1)-1 .
\tag{TG15}
\]

The exact DP59 lattice is
\[
 \mathcal W_M=[\alpha]^*H^0(X,\mathcal L^M)
                 \subset H^0(X,\mathcal L^{M^2}),
\tag{TG16}
\]
with its actual permitted integral basis \(\mathcal S_\lambda\). No full level-\(M^2\) orbit is substituted for it.

Let \(\ell_r=M^{-T_r}P_r(\partial)\vert_0\). Define the finite fractional ideal
\[
                 \mathfrak J_{r,\kappa}=\ell_r(\mathscr C_\kappa)
\tag{TG17}
\]
using full integral \(T_r\)-jets. Define \(\mathfrak I^{\rm aux}_{r,M}\) to be the ideal generated by the actual allowed auxiliary tuple values
\[
 a^{\rm aux}_{r,\lambda}
 =M^{-T_r}P_r(\partial)
       \left(\sum_j b_j\varepsilon_{j,M}
                   U_{z_j}^{M^2H}F_{\mathcal S_\lambda}\right)(0),
       \qquad z_j=[M]^{-1}t_j .
\tag{TG18}
\]
The \(\varepsilon_{j,M}\) are exactly the11-unit finite reading phases of DO030(11–13). Pullback notation in (TG18) uses the section-level functions, as in DO030(13); it is not a second multiplication by M.

### Theorem TG19. Exact content multiplication

\[
 \boxed{\quad
           \mathfrak I^{\rm aux}_{r,M}
                 =\mathfrak b\,\mathfrak J_{r,\kappa},
       \qquad
           v(\mathfrak I^{\rm aux}_{r,M})
                 =\eta+v(\mathfrak J_{r,\kappa}).
       \quad}
\tag{TG19}
\]

**Proof.** By Proposition TG10 the full integral \(T_r\)-jet coefficient module at each translated point \(z_j\), read at0 with its actual reduced operator, is exactly \(\mathscr C_\kappa\). Translation keeps the invariant tangent basis; the multiplication maps and alpha are etale at11, so their maps on formal parameters are integral isomorphisms. Thus the image ideal of the j-th summand on its independent jet module is \(b_j\varepsilon_{j,M}\mathfrak J_{r,\kappa}=b_j\mathfrak J_{r,\kappa}\).

The points \(q_j=\alpha z_j=\bar\alpha^{-1}t_j\) on the base of (TG16) remain distinct modulo11. DO030's simultaneous integral jet theorem, valid on these ordinary products by DO034 and the host constructions, states that (TG15) makes the map
\[
  \mathcal W_M\longrightarrow
          \bigoplus_{j=1}^{s}
             J^{T_r}_{z_j}(\mathcal L^{M^2})
\tag{TG20}
\]
surjective. It is obtained from the actual \(H^0(\mathcal L^M)\) by alpha pullback and the explicit \(3s(T_r+1)-1\) interpolation bound. The map is over R; formal complete-local interpolation coefficients are sufficient for equality of image ideals.

On the independent direct sum, the image of the sum functional is the sum of the individual image ideals. Surjectivity therefore gives
\[
 \mathfrak I^{\rm aux}_{r,M}
       =\sum_j b_j\mathfrak J_{r,\kappa}
       =(b_1,\ldots,b_s)\mathfrak J_{r,\kappa}.
\]
This proof also shows explicitly why potential cancellation among different auxiliary terms cannot force extra content: prescribe a desired jet at one point and zero jets at all the other points. It is not an assertion that the individual global theta functions have disjoint support. Since R is a DVR, valuation of the product is the sum, proving (TG19). ∎

The finite list of basis values generates this ideal. Its minimum valuation is attained by one permitted tuple, whose actual finite vector is \(\mathcal O\phi_\lambda\). Selecting that tuple does not require charging the norm of an interpolating coefficient vector. The vector has the exact fixed norm
\[
                \|\mathcal O\phi_\lambda\|_f^2
                               =\sum_j|b_j|^2,
\tag{TG21}
\]
by DO030's disjoint-place scaled isometry.

## 4. Sharp selected bounds after the auxiliary restriction

K033's proof of the formal ideal bounds is uniform for every unit \(\kappa=M^2\), not just its originally chosen least interpolation level. Therefore (CS34) and (TG19) give

\[
 \boxed{\quad
 \eta+\frac{T_r}{1220}-\frac15-K_0
 \ \le\ v(\mathfrak I^{\rm aux}_{r,M})\
 \le\eta+\frac{T_r}{1220}
                  +c_0-\frac1{10}-\frac{D_0}{1220}.
 \quad}
\tag{TG22}
\]

Every basis value satisfies the lower bound, and a permitted nonzero basis value attains the ideal valuation and hence satisfies both bounds. In particular

\[
 \boxed{\qquad
 \lim_{r\longrightarrow\infty}
      \frac{v(a^{\rm aux}_{r,\lambda(r)})}{T_r}
              =\frac1{1220}.
 \qquad}
\tag{TG23}
\]

The bounded additive error includes \(\eta\) and the full fixed baseline constants from K033. The conclusion concerns the **same explicit selected family** \(P_r\) in the full enlarged CM basis. The auxiliary operator is fixed, actual, and nonzero. There is no enlargement of the harmonic subspace, no appeal to a unit in the ambient unselected space, and no restriction to the degree-\(T_r\) leading algebraic term.

The fixed auxiliary coefficients may be fractional; (TG22) retains their exact minimum valuation. If they are all integral and one is a unit, then \(\eta=0\). If a scalar normalization of the finite vector is imposed, its valuation is added explicitly. These statements use the Hurwitz derivative functional \(\ell_r\), rather than the divided Taylor coefficient. The factorial shifts are already those in K033.

## 5. The actual finite Steinberg family and its costs

For the h=1 host, AM-DO-034 section5 supplies the finite Steinberg operator \(\mathcal O_G\), with fixed ranks a,b and the actual stage characters of K031. Its coefficients have minimum11-valuation0. It satisfies

\[
 \begin{aligned}
 d_G&=(g_0g_1)^{21a(a-1)},\\
 \Gamma_G:=\|\mathcal O_G\phi_\lambda\|_f^2
   &=(g_0g_1)^{42(-ab+a(a+1)/2)}
         \prod_{\epsilon=0}^{1}
           \prod_{i=1}^{a}(1-g_\epsilon^{-i})^{42},\\
 s_G&\le(g_0g_1)^{42ab}.
 \end{aligned}
\tag{TG24}
\]

Thus (TG22)–(TG23) apply to this actual prescribed finite compact type, with \(\eta=0\). The first-row modifications in K033 leave the e entries, finite stage characters, ranks, G-primes, and the operator itself unchanged. This fixed-operator hypothesis is essential for the asymptotic statement.

The proof of TG19 works without change on the h=4 host. When the analogous local finite Steinberg construction is made with its actual168-place record and G-primes, its parameters are the corresponding \(f=168\) local products. This local-product substitution does not silently claim that every global first-image assertion in the h=1 DO034 file has already been reconstructed for h=4.

There is a simple completely explicit sufficient level for either local product. Put \(Q=g_0g_1\), choose the smallest positive integer L with \(Q\le29^L\), and define

\[
 e_r=Lfab+\left\lceil\log_{29}\bigl(3(T_r+1)\bigr)\right\rceil,
                         \qquad M_r=29^{e_r}.
\tag{TG25}
\]

Here the ceiling means the least integer k with \(29^k\ge3(T_r+1)\); it can be computed using integer arithmetic. Then \(M_r\ge3s_G(T_r+1)\), proving (TG15). This bound intentionally keeps the auxiliary orbit size:

| Host baseline | a | b | \(Q=g_0g_1\) | L | Fixed term \(Lfab\) in \(e_r\) |
|---|---:|---:|---:|---:|---:|
| K031, \(J^{14}\) | 42 | 1802 | \(4615409\cdot5276377\) | 10 | 31,787,280 |
| K032, \(J^{56}\), analogous local product | 168 | 1802 | \(22285932761\cdot64072175441\) | 15 | 762,894,720 |

The large fixed exponent is a sufficient interpolation cost, not an assertion that the least useful level is this large. It is \(O(1)+O(\log T_r)\) for fixed source ranks and G-primes, but it must not disappear from a concrete MainX window.

For these two exact local products the certificate gives respectively
\[
 (v_{11}I_a,\ v_{11}\Gamma_G,\ v_{11}d_G)
       =(24,336,0)\quad\hbox{and}\quad(408,21336,0).
\tag{TG25a}
\]
The second tuple uses the24 actual real-field29 places of K032, rather than replacing their residue exponent by168. These are fixed finite normalization costs; the h=4 tuple by itself is not a new global extraction theorem.

On the h=1 host, the actual class-supported first extraction of DO034(25) now has a selected tuple with (TG22), and

\[
 \Theta_{\mathcal O_G\phi_\lambda,r_{P_r}\phi_\infty}(F_r)(1)
       =\frac{C^{14ab}a^{\rm aux}_{r,\lambda}}
                    {I_a(M)\,d_{\rho,r}\,d_G},\qquad
 \|F_r\|_2^2=\frac1{I_a(M)d_{\rho,r}d_G}.
\tag{TG26}
\]

The target vector is the primitive vector of K033(CS25), with its exact hook metric (CS36); the source highest vector used in the compact matrix coefficient is the matching source factor. The Cauchy argument already puts this possibly non-highest target vector in the single selected target summand. Compact extraction does not require it to be a target-highest vector.

Here
\[
 I_a(M)=M^{42a^2}\prod_{i=1}^{a}(1-29^{-i})^6.
\tag{TG27}
\]
Its11-valuation is independent of M; \(v_{11}(d_G)=0\). The changing compact dimension \(d_{\rho,r}\) has valuation \(O(\log(T_r+1))\), by the exact fixed-rank Weyl ratios in K033(CS40). Thus, after removing the displayed fixed period and retaining the stated algebraic normalization, the actual first coefficient in (TG26) has valuation slope \(1/1220\). Unit source and finite Schwartz normalization replaces the denominator by
\(\sqrt{\Gamma_G}\sqrt{I_a(M)d_{\rho,r}d_G}\), exactly as in DO034(27); the fixed \(\Gamma_G\) and these compact corrections also preserve that slope.

This does not discard the archimedean Schwartz norm. It remains exactly K033(CS38), including \(A_r!B_r!\), the residual hook products, and the positive CM metric factors. Those real factorial costs are not \(O(\log T_r)\), and normalizing the full archimedean Schwartz vector changes the real cost in the complete gain/error accounting. The complete DP44 inequality is not inferred from the local slope.

The theorem applies to any other **specified nonzero fixed** auxiliary vector that has an actual finite Heisenberg expansion of the form (TG13). In particular it can be used with a literal raw G factor once its fixed expansion and the relevant compact extraction have been supplied. It does not identify a raw factor with the finite Steinberg projection by definition, and it does not assert that a later theta image contains this entire selected lattice.

## 6. Scope, checks, and references

The classical finite-torsion flat-frame argument in Lemmas TG3/TG6 is written in full to fix the normalized connection, the integral root, and the actual reduced multiplier. The new application is the exact complete-module comparison TG10, the actual permitted auxiliary ideal identity TG19, and its sharp selected consequence TG22 on the enlarged CM family.

Carried accepted inputs are DP47/49/51/58/59/62 at the interfaces already specified in K018, K022, and K033. Exact local/source identifications are K018(K19.2/K19.13), K033(CS9/CS12/CS19/CS25/CS28/CS34), DO030(9–20), and DO034(12–29). No Lean execution is claimed. The simultaneous jet theorem and the accepted display bounds are used, not rederived.

Primary literature: Bannai, K., & Kobayashi, S. (2010). Algebraic theta functions and the p-adic interpolation of Eisenstein–Kronecker numbers. *Duke Mathematical Journal, 153*(2), 229–295. Author preprint: [arXiv:math/0610163v4](https://arxiv.org/pdf/math/0610163), exact locators given in section1. Those primary passages concern the reduced multiplier and algebraic Mumford translation; no positive-characteristic ordinary hypothesis from later sections is imported.

The companion exact certificate checks formal torsion-root and connection signs in finite rational jets, including the excluded d=11 case, and computes the displayed sufficient level constants and the actual fixed finite11-costs. These finite calculations check the indicated identities and arithmetic only. The infinite full-germ and image-ideal assertions are the proofs above, not inferences from a finite series sample.
