# AM-K017 — integral logarithmic Hessians, stronger actual theta slopes, and exact mixed-jet recurrences

Author: `/root/kummer_extension`, GPT-6 Astra Pro, ALP_MACHINE, 21 November 2026 UTC. This supplements AM-K012–016 in `jacobian_reduced_theta.md`. It concerns the actual translated germ \(F\) and the actual trace-one germ \(\sigma_q\). Every reduction below is a reduction of Hurwitz derivatives, not of divided Taylor coefficients.

## 1. Statement

Retain
\[
C:y^2=x^7-1,\quad E=\mathbb Q(\zeta_7),\quad
\omega_i=x^{i-1}dx/y,\quad D_i=\partial/\partial u_i,
\quad q(u)=u_1u_3-u_2^2.
\]
Let \(W_{ij}=-\partial_i\partial_j\log\sigma_q\) be the actual algebraic Kleinian Hessian. Its explicit expressions, normalization, and integral Abel chart are AM-K012. For an odd prime \(p\ne7\), let \(q_i=p^{h_i}\) be the sufficient restricted-power nilpotence exponent in the table (K13.2).

**(a) Global constant lemma.** The rational function
\[
\overline{D_i^{q_i-1}W_{ij}}
\tag{K18.1}
\]
on the good special fibre is a constant. It is zero unless
\[
iq_i+j\equiv0\pmod7.
\tag{K18.2}
\]
In particular the pure constant vanishes whenever \(q_i\not\equiv-1\pmod7\). This proves the additional log-derivative hypothesis in (K13.7) geometrically, at all such primes. The three exact 11-adic checks in AM-K013 are consistent independent finite checks, no longer necessary premises for that vanishing.

**(b) Improved actual finite bounds.** At every prime above \(p\), for either \(F\) or \(\sigma_q\),
\[
v_p(\partial_i^n f(0))\geq
\max\{0,c_i(p)n-s_p(n)/(p-1)\},
\tag{K18.3}
\]
where the following constants are now proved:

| \(p\bmod7\) | \(c_1(p)\) | \(c_2(p)\) | \(c_3(p)\) |
|---|---|---|---|
| 2 | \(1/(2p(p-1))\) | \(1/(2(p-1))\) | \(1/(2(p-1))\) |
| 3 | \(1/((p-1)(p^3+1))\) | \(1/(2(p-1))\) | \(1/(2p(p-1))\) |
| 4 | \(1/(2(p-1))\) | \(1/(2p(p-1))\) | \(1/(2(p-1))\) |
| 5 | \(1/(2(p-1))\) | \(1/((p-1)(p^3+1))\) | \(1/(2p(p-1))\) |
| 6 | \(1/(p^2-1)\) | \(1/(p^2-1)\) | \(1/(p^2-1)\) |

For \(p\equiv1\pmod7\), this argument provides no positive constant. As before, these constants are lower bounds, not proved optimal finite slopes.

**(c) Full restricted-operator identities at 11.** In the three-variable Hurwitz algebra over \(\mathbb F_{11}[\zeta_7]\), the actual germs satisfy
\[
\boxed{
\partial_1^{11}f=4u_3f,\qquad
\partial_2^{11}f=-\partial_1f,\qquad
\partial_3^{11}f=-u_2f,
\qquad f=F\ \hbox{or}\ \sigma_q.}
\tag{K18.4}
\]
These are identities of the complete reduced Hurwitz series. In particular
\[
\partial_1^{12}\partial_3^2\sigma_q(0)\equiv8\pmod{11}.
\tag{K18.5}
\]
This actual source mixed derivative is a unit at both primes above 11. It disproves the naive additive extension of the three pure-direction constants to all mixed multiindices.

**(d) A failed next strengthening.** For \(\ell_n=\partial_i^n\log F(0)\), exact arithmetic gives
\[
v_{11}(\ell_{2q_i})=1\qquad(i=1,2,3)
\tag{K18.6}
\]
at both primes above 11. Thus an attempted improvement based on \(p^2\mid\ell_{2q_i}\) is false. The Bell-lemma equality case at that index is a real obstruction for this particular estimate, although cancellation in the full theta derivative could still give stronger bounds by a different argument.

## 2. The integral extension lemma

We first give the general local-to-global argument, including its finite-place content.

Let \(R\) be the localization of \(\mathcal O_E\) at a prime above an odd \(p\ne7\), with residue field \(k\), and let \(\mathcal J/R\) be the smooth proper abelian scheme. Completion may be taken after the argument. All rational functions and line charts can thus be taken over the number field, where the complex comparison below applies. The total space is integral and normal, and its special fibre is geometrically integral. Let \(\mathcal L\) be the primitive integral theta line of ALP-LIFT-08, and \(s_q\) its primitive section at this prime. Write \(\Theta\) for its divisor. Its restriction to the special fibre is a nonzero theta divisor; in particular \(\Theta\) has no vertical divisor component.

Take an affine open \(\mathcal U\) on which \(\mathcal L\) is trivial, and write \(f_{\mathcal U}\) for the local equation of \(s_q\). This is a regular function. At the generic point of the special fibre it is a unit, since the section does not vanish on that entire fibre. The invariant derivatives \(D_i\) preserve regular functions on \(\mathcal U\), so
\[
D_iD_j\log f_{\mathcal U}
=\frac{D_iD_jf_{\mathcal U}}{f_{\mathcal U}}
 -\frac{D_if_{\mathcal U}D_jf_{\mathcal U}}{f_{\mathcal U}^2}
\tag{K18.7}
\]
is a rational function with no vertical pole.

The algebraic \(W_{ij}\) has no vertical pole either. Its pullback to the ordered-divisor chart \(\mathcal R\) of (K12.12) is explicitly integral by (K12.8)–(K12.10). This chart maps étale to \(\mathcal J\), and its reduction has a nonempty open image in the irreducible special fibre. Thus it detects the generic vertical valuation. An étale pullback cannot turn a negative vertical valuation into a nonnegative one. This proves the assertion without any integral Chern frame.

On the characteristic-zero generic fibre, define
\[
\beta_{ij,\mathcal U}=W_{ij}+D_iD_j\log f_{\mathcal U}.
\tag{K18.8}
\]
It is regular there. To justify the cancellation explicitly, in any analytic lift of a small open set write the actual reduced sigma as
\(\sigma_q=f_{\mathcal U}g\), where \(g\) is the holomorphic, nonvanishing transition from the algebraic local frame to the reduced frame. Since \(W_{ij}=-D_iD_j\log\sigma_q\), the right side of (K18.8) is \(-D_iD_j\log g\), which is holomorphic. The right side is also rational over the generic algebraic fibre, hence has no horizontal divisor pole. Equivalently one may check each horizontal valuation after embedding into \(\mathbb C\).

By (K18.7) and the vertical integrality of \(W_{ij}\), (K18.8) has no vertical divisor pole. Every codimension-one point of the smooth total space is either horizontal or generic in the special fibre. A normal affine domain is the intersection of its height-one valuation rings. Therefore
\[
\boxed{\beta_{ij,\mathcal U}\in\Gamma(\mathcal U,\mathcal O).}
\tag{K18.9}
\]
This is an integral statement about the logarithmic **second derivative** of a local frame. It neither asserts an integral reduced frame nor asserts integral divided Taylor coefficients. In particular it is compatible with the supplied THETA3 C11 counterexample.

Now suppose \(\overline D_i^{q}=0\) on the special fibre, where \(q=p^h\). It also vanishes on its function field: the \(q\)-th iterate is a derivation, and the quotient rule extends the zero derivation from any dense affine open. Reducing (K18.8),
\[
\overline D_i^{q-1}\overline W_{ij}
=\overline D_i^{q-1}\overline\beta_{ij,\mathcal U}
 -\overline D_i^{q}
       \left(\frac{\overline D_j\overline f_{\mathcal U}}
                    {\overline f_{\mathcal U}}\right).
\tag{K18.10}
\]
The last term is zero and the first term is regular on \(\mathcal U_k\). The left side is therefore regular on every open of a cover of \(\mathcal J_k\), hence is a global regular function. Properness and geometric connectedness give
\(H^0(\mathcal J_k,\mathcal O)=k\). This proves that it is a constant.

There is a slightly more general version that will be used at 11. If
\(\overline D_i^{p}=a\overline D_k\), with \(a\in k\), then
\[
\overline D_i^{p-1}\overline W_{ij}-a\overline W_{kj}
\tag{K18.11}
\]
is a constant. Lift \(a\) to the DVR arbitrarily and apply (K18.9) to both Hessians. The logarithmic term is
\((\overline D_i^{p}-a\overline D_k)
 (\overline D_j\overline f/\overline f)=0\), proving regularity exactly as above.

## 3. CM characters and the improved slopes

The source section has CM character 4:
\[
\sigma_q(\zeta u_1,\zeta^2u_2,\zeta^3u_3)=\zeta^4\sigma_q(u).
\tag{K18.12}
\]
This was established in AM-K014, and also follows from the invariant theta line and its leading quadratic. Twice differentiating gives
\[
a^*W_{ij}=\zeta^{-i-j}W_{ij},\qquad
a^*(D_i^mW_{ij})=\zeta^{-i(m+1)-j}D_i^mW_{ij}.
\tag{K18.13}
\]
At \(m=q_i-1\), a nonzero constant could have this character only if \(iq_i+j\equiv0\pmod7\), because \(\zeta\) still has order 7 in every residue field under consideration. This proves (K18.1)–(K18.2).

For the pure Hessian, \(i\ne0\pmod7\), so the exceptional condition is exactly \(q_i\equiv-1\pmod7\). Otherwise
\[
D_i^{q_i-1}W_{ii}\in p\mathcal R.
\tag{K18.14}
\]
Together with \(D_i^{q_i}\mathcal R\subset p\mathcal R\), this even improves the logarithmic estimate to
\[
v_p(D_i^mW_{ii}|_a)\geq
\left\lfloor\frac{m+1}{q_i}\right\rfloor,
\qquad
v_p(\ell_n)\geq\left\lfloor\frac{n-1}{q_i}\right\rfloor\ (n\geq2).
\tag{K18.15}
\]
For clarity, if \(m=Aq_i+B\), \(0\leq B<q_i\), the usual operator estimate gives \(p^A\). When \(B=q_i-1\), apply \((D_i^{q_i})^A\) to (K18.14) to obtain \(p^{A+1}\). This proves the displayed shifted floor bound; it is an iterated stable-ring statement.

In particular \(p\mid\ell_{q_i+1}\), the hypothesis of the improved Bell–Legendre bound (K13.7). The nonexceptional columns in the table of §1 use
\(1/(2p^{h_i-1}(p-1))\). The exceptional columns retain the generic constant
\(1/((p-1)(p^{h_i}+1))\) of (K13.6). These are exactly the listed entries. AM-K015 transfers both bounds to \(\sigma_q\) using the actual integral \([2]\)-ratio, so the conclusion concerns the source line and respects the source's odd level.

The exceptional possibility cannot be discarded merely by symmetry. The finite certificate computes
\[
\partial_1^{28}\log F(0)\equiv2\pmod3,
\qquad
\partial_2^{126}\log F(0)\equiv1\pmod5.
\tag{K18.16}
\]
Here the respective exponents are \(q_1=3^3=27\) and \(q_2=5^3=125\), both congruent to \(-1\pmod7\). These are exact nonzero constants in their whole cyclotomic residue algebras.

## 4. Exact restricted-operator identities at 11

### The algebraic restricted powers

The CM-label argument gives \(D_1^{11}=D_3^{11}=0\) on \(\mathcal J_k\), and \(D_2^{11}\) is a scalar multiple of \(D_1\). The scalar is \(-1\): the exact integral ODE (K12.7), evaluated at the branch divisor, gives
\[
D_2^{11}y_j=-D_1y_j\quad(j=1,2,3),
\tag{K18.17}
\]
and \(D_1y_1\) is a unit in the cyclotomic residue algebra. Its coefficient vector in \(1,\zeta,\ldots,\zeta^5\) is
\((5,4,6,4,5,0)\); the certificate verifies its inverse. Since the two sides are invariant vector fields in the same one-dimensional labelled space, this one unit evaluation determines the scalar globally. Thus
\[
\boxed{D_1^{11}=0,\qquad D_2^{11}=-D_1,
\qquad D_3^{11}=0.}
\tag{K18.18}
\]

### The logarithmic constants

For \(i=1\), condition (K18.2) permits only \(j=3\); for \(i=3\), it permits only \(j=2\). The exact finite calculation, using the particularly simple functions
\(W_{13}=x_1x_2x_3/4\) and
\(W_{23}=-(x_1x_2+x_1x_3+x_2x_3)/4\), gives
\[
-D_1^{10}W_{13}=4,\qquad
-D_3^{10}W_{32}=-1\pmod{11}.
\tag{K18.19}
\]
The global constant lemma makes these values valid everywhere on the special fibre, not just at the evaluation divisor.

For the middle operator, (K18.11) shows that
\(D_2^{10}W_{2j}+W_{1j}\) is a constant. Its CM character is
\(-(22+j)\equiv-(1+j)\pmod7\), which is nonzero for every \(j\in\{1,2,3\}\). Therefore
\[
D_2^{10}W_{2j}+W_{1j}=0\pmod{11}.
\tag{K18.20}
\]

Let \(H=\log F\), whose Hurwitz coefficients are integral and whose first and all odd-total-degree derivatives at the origin vanish. Differentiating \(\partial_1^{11}H\) once in direction \(j\) gives the constants (K18.19), so in the full three-variable Hurwitz algebra
\[
\partial_1^{11}H=4u_3,\qquad
\partial_3^{11}H=-u_2.
\tag{K18.21}
\]
There is no integration ambiguity: a series killed by all three divided-power derivations is constant, and these constants at zero vanish by parity. Similarly (K18.20) and parity give
\[
\partial_2^{11}H+\partial_1H=0.
\tag{K18.22}
\]

In characteristic 11, every positive-augmentation element of the multivariate Hurwitz algebra has 11-th power zero. For a divided-power monomial with multiindex \(\alpha\ne0\), the valuation of the scalar in its 11-th power is \(\sum_j s_{11}(\alpha_j)>0\). Frobenius is additive, and each coefficient of an infinite product involves only finitely many terms, so the same assertion holds for a complete series. The Bell-polynomial identity modulo a prime is elementary here: in the polynomial \(B_p(H',\ldots,H^{(p)})\), every term except \((H')^p\) and \(H^{(p)}\) has coefficient divisible by \(p\). Indeed its coefficient has numerator \(p!\), whereas all factorials in its denominator have arguments less than \(p\). Thus
\[
\partial_i^{11}F/F=(\partial_iH)^{11}+\partial_i^{11}H
=\partial_i^{11}H.
\tag{K18.23}
\]
Equations (K18.21)–(K18.22) prove (K18.4) for \(F\).

### Transfer to the actual trace-one section

Use the integral algebraic comparison
\(\sigma_q(2u)=r(u)F(2u)\) of AM-K015. On reductions of its coefficient functions, the three operators
\(D_1^{11}\), \(D_2^{11}+D_1\), and \(D_3^{11}\) kill \(r\), by (K18.18). Each operator is a derivation modulo 11. Apply it to the product identity. The linear terms in (K18.4) scale under \(u\mapsto2u\), while \(2^{11}=2\) in characteristic 11. Dividing by the resulting unit factor and replacing \(2u\) by \(u\) proves exactly (K18.4) for \(\sigma_q\). No integral Chern frame was introduced.

The operator identities also hold for AM-R-006's actual moved source section \(\Sigma_{\rm tr}=c\sigma_q\), since \(c\) is constant; its being an 11-adic unit preserves every unit assertion below.

## 5. Mixed derivatives, finite unit families, and their scope

Write \(S_\alpha=\partial^\alpha\sigma_q(0)\), and interpret a negative index as zero. Equation (K18.4) is equivalently the all-index recurrence
\[
\begin{aligned}
S_{\alpha+11e_1}&=4\alpha_3S_{\alpha-e_3},\\
S_{\alpha+11e_2}&=-S_{\alpha+e_1},\\
S_{\alpha+11e_3}&=-\alpha_2S_{\alpha-e_2}
\end{aligned}\qquad(\bmod11).
\tag{K18.24}
\]
The first and third equalities are just the Hurwitz Leibniz rule for multiplying by a coordinate. The second is a constant-coefficient operator equality. Each replacement lowers the total derivative order, so these relations reduce every derivative modulo 11 to a finite base cube with all three indices less than 11. They do not assert that every element of that base cube is known without further calculation.

Taking \(\alpha=e_1+2e_3\), and using \(S_{e_1+e_3}=1\), proves (K18.5). The tempting additive extension of the pure lower constants would instead give
\[
v_{11}(S_{(12,0,2)})\geq
\frac{12}{20}+\frac2{20}
-\frac{s_{11}(12)+s_{11}(2)}{10}
=\frac3{10}>0,
\]
which is false. Consequently pure-direction gains cannot be assigned additively to a selected mixed harmonic row without additional analysis.

There are explicit further unit witnesses. Since \(\partial_1u_3=0\), iteration of (K18.4), as an identity of the actual formal series, gives
\[
\partial_1^{11k}\sigma_q=4^ku_3^k\sigma_q\pmod{11}.
\]
Differentiating the leading nonzero jets yields
\[
\begin{aligned}
S_{(11k+1,0,k+1)}&=4^k(k+1)! &&(0\leq k\leq9),\\
S_{(11k,2,k)}&=-2\,4^kk! &&(0\leq k\leq10),
\end{aligned}\qquad(\bmod11).
\tag{K18.25}
\]
Every displayed value is a unit. In particular
\[
S_{(100,0,10)}=8,\quad S_{(110,2,10)}=2,
\quad S_{(0,1100,10)}=8\pmod{11}.
\tag{K18.26}
\]
The last equality uses \(\partial_2^{1100}\sigma_q=\partial_1^{100}\sigma_q\), obtained by iterating the middle identity in (K18.4). These are finite unit families and exact all-index mod-11 recurrences; they supply no asymptotic valuation upper bound.

For completeness, the same formal algebra gives
\[
\partial_1^{121}\sigma_q=0,\qquad
\partial_3^{121}\sigma_q=0,\qquad
\partial_2^{1331}\sigma_q=0\pmod{11}.
\tag{K18.27}
\]
Indeed \(u_j^{11}=11!\,u_j^{[11]}=0\) in the reduced Hurwitz algebra; iterating the first or third relation eleven times proves the first two equalities, and the middle relation then proves the last. Differentiating shows vanishing for every multiindex exceeding one of these bounds in its indicated component. The stronger pure-direction cutoffs 11,121,11 from AM-K015 are also immediate by setting the other variables to zero.

Neither (K18.24) nor (K18.27) is iterated as a divisibility statement modulo powers of 11. Such an iteration would require a stable integral module and a justified operator inclusion into \(11\) times that module. No such stronger inclusion is inferred from these formal congruences.

## 6. The next proposed divisibility is false

To test whether the improved Bell constant could be increased by forcing the equality-case logarithmic derivative to acquire an additional power of 11, the exact ODE was evaluated modulo \(121\). In the coefficient basis \(1,\zeta,\ldots,\zeta^5\), it gives

| Direction | \(q_i\) | \(\ell_{2q_i}/11\pmod{11}\) |
|---|---:|---|
| 1 | 11 | \(3+3\zeta+8\zeta^3+5\zeta^4+8\zeta^5\) |
| 2 | 121 | \(3+3\zeta+8\zeta^3+5\zeta^4+8\zeta^5\) |
| 3 | 11 | \(3+3\zeta+3\zeta^2+3\zeta^3\) |

Each displayed polynomial has gcd 1 with \(\Phi_7\) over \(\mathbb F_{11}\), so it is a unit at both primes above 11. This proves (K18.6). At the Bell index \(j=2q_i\), the lower bound in (K13.7) has
\((p-1)v(\ell_j)+s_p(j)-1=10+2-1=11\), precisely the equality value \(j/(2p^{h_i-1})\). The proposed extra divisibility is therefore unavailable. This does not prove optimality of the final theta slope, because Bell terms can cancel.

## 7. Reproducibility and source scope

The exact finite certificate is `jacobian_hessian_pcurvature_certificate.py`, with complete output in `jacobian_hessian_pcurvature_certificate.json`. It checks the two constants (K18.19), the restricted scalar (K18.17), both exceptions in (K18.16), and all three failures in (K18.6). For modulus \(121\), it computes the initial cyclotomic inverses over \(\mathbb Q[Z]/\Phi_7\) and reduces them only after checking their denominator units; it does not treat \(\mathbb Z/121\mathbb Z\) as a field. It verifies the reduced inverses multiplicatively and records the underlying recurrence SHA256.

The stable integral Abel chart, actual Baker/Chern identification, and the classical Kleinian Hessian identities are fully sourced in AM-K012 and its bibliography. The actual primitive line/section and good Hodge basis are ALP-LIFT-05, ALP-LIFT-07, and ALP-LIFT-08. The normality, character, logarithmic-operator, and transfer arguments needed for the new statements are written in full here. The elementary fact that a normal noetherian domain is the intersection of its height-one valuation rings is the sole normality criterion used; no assertion of reduced-frame integrality is hidden in that step.

This closes a further actual-theta coefficient subgate and exhibits a concrete failure of a naive mixed extension. It does not identify a source-selected harmonic row, prove a matching sharp finite slope, supply the terminal every-\(\varepsilon\) window, or extend the accepted Dirichlet theorem to Kummer RH.
