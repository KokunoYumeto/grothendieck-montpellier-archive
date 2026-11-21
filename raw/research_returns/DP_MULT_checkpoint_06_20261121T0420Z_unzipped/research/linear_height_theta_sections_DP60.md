# DP60 — modulo-p interpolation and linear logarithmic section size

Date: 2026-11-21 UTC. Author: `/root/formal_bound`, GPT-6 Astra Pro; reasoning effort is not exposed. The parent reserved DP60. This memo strengthens the global-section construction of DP58 by controlling algebraic coefficients and section norms. It does not identify the resulting sections with the prescribed translated family in the source.

## 1. The statement

Let \(E=\mathbf Q(\zeta_7)\), fix a prime \(\mathfrak p\mid11\), and put

\[
A_0=\mathcal O_E[1/14],\qquad
R_0=\mathcal O_{E,\mathfrak p},\qquad
R=\widehat{R_0}=W(\mathbf F_{11^3}).
\]

Use the good Jacobian model \(J/A_0\), the integral cyclotomic action, the principal polarization and the trace-one line \(\mathcal L\) of DP49. At \(\mathfrak p\) use the actual arbitrary-unit pair and invariant product normalization of DP54. Write

\[
\Theta_s(z)=f_s(z)U(z)^\kappa B(z)^{-\kappa},
\qquad U\in1+(z)R[[z]],
\qquad B=\exp b,\qquad \beta=b\circ E_{\mathrm{fg}},
\tag{SH1}
\]

where \(E_{\mathrm{fg}}\) is the inverse formal-group logarithm. This notation distinguishes it from the number field \(E\).

Fix tensor-compatible continuous Hermitian metrics on \(\mathcal L\) at the finitely many complex embeddings of \(E\), and use their tensor powers on \(\mathcal L^{\otimes\kappa}\). Their sup norms are taken on the compact complex abelian varieties.

**DP60.** There are fixed integers \(a\ge1\), \(b_0\ge0\), and constants \(C_1,C_2,C_3\), depending only on the model, line, chosen local chart and metrics, such that the following holds. For every integer \(n\ge1\) and every integer \(\kappa\ge an+b_0\) with \(11\nmid\kappa\), there is a nonzero section

\[
s_{n,\kappa}\in H^0(J_{A_0},\mathcal L^{\otimes\kappa})
\tag{SH2}
\]

whose normalized algebraic prefactor satisfies

\[
f_{s_{n,\kappa}}U^\kappa
\equiv1\pmod{11R[[z]]+(z)^{n+1}},
\tag{SH3}
\]

and whose archimedean norms satisfy, for every embedding \(\sigma:E\hookrightarrow\mathbf C\),

\[
\boxed{
\log\max\{1,\|s_{n,\kappa}\|_{\sigma,\sup}\}
\le C_1\kappa+C_2\log(n+1)+C_3.}
\tag{SH4}
\]

The section is integral at every finite place away from 2 and 7 in this fixed model; no additional prime denominators are introduced. Its local coefficient at zero is a unit at \(\mathfrak p\).

For every explicit DP58 ordinary witness of degree at most \(n\), and for every explicit first-row two-column harmonic witness of total degree at most \(n\), this same section, or two copies of it, has exactly the pure-kernel valuation in DP58. Thus one can choose square powers

\[
\kappa=M^2=an+O(\sqrt n),\qquad 11\nmid M,
\]

and obtain both

\[
\boxed{\kappa=O(n),\qquad
\log\max\{1,\|s_{n,\kappa}\|_{\sigma,\sup}\}=O(n),}
\tag{SH5}
\]

while retaining the exact selected valuations, including the unit source factor \(M^{-m}\) at every selected derivative degree \(m\le n\). The construction is over the number field from the outset; it does not use an unquantified final approximation of an arbitrary completed global section.

An adelic version with the same \(O(\kappa+\log(n+1))\) bound follows for any fixed tensor-compatible collection of continuous sup norms which is induced by this integral model outside the finitely many places over 2 and 7; the precise conditional metric statement is in §7.

## 2. Why approximation modulo 11 already preserves the witnesses

This part works for any odd prime and actual pair in DP46; then specialize to 11. Put \(s_p^*=1/(p-1)\), written here as \(s_*\) to avoid confusing it with a section. For a primitive line of intrinsic length \(k\), put

\[
N=p^k,\qquad w=\frac{s_*N}{N+1},\qquad
c=\frac{s_*}{N+1}.
\]

At the explicit degree \(m=(N+1)p^r\), DP58 gives

\[
V_m=v_p(\text{pure ordinary value})=cm-s_*.
\tag{SH6}
\]

Suppose an integral prefactor \(W\) is congruent to one modulo \(p\) and terms of total group-coordinate degree at least \(n+1\), where \(m\le n\). Write

\[
W=1+pV+H,\qquad V\in R[[z]],\quad H\in(z)^{n+1}.
\tag{SH7}
\]

Substitution by the inverse logarithm preserves total order, so \(H\) contributes nothing to a derivative of degree \(m\). At weight \(w\), DP46 makes the substituted integral prefactor \(V\) and the unit-parameter kernel exponential integral. Therefore the degree-\(m\) ordinary derivative of the error has valuation at least

\[
1-wm+v_p(m!)=1+cm-2s_*,
\tag{SH8}
\]

because \(m\) has digit sum two. For odd \(p\), \(s_*\le1/2\), so

\[
1+cm-2s_*>cm-s_*=V_m.
\tag{SH9}
\]

The error cannot change the valuation of the nonzero pure value. This applies uniformly to every unit primitive parameter \(\lambda\), in particular \(\lambda=-\kappa\).

For the two-column family, the product of two prefactors of the form (SH7), modulo total degree \(n+1\), is

\[
(1+pV_1)(1+pV_2)
=1+p(V_1+V_2+pV_1V_2).
\tag{SH10}
\]

The expression in parentheses is integral on the product formal group. More generally the difference of products telescopes into terms containing a factor divisible by \(p\); no unit or separability assumption on the remaining error prefactor is needed.

At the first-row critical common weight \(w_*\), DP51's full-polydisc argument makes any integral function on the product formal group, after inverse-logarithm substitution and multiplication by the product unit-parameter kernel, integral after contraction. That proof applies to an arbitrary product-coordinate function: it only uses integrality of the coordinate substitutions and coefficientwise integrality of the exponential.

Now take \(a_r=p^r\), \(b_r=p^{h-1+r}\), \(m=a_r+b_r\), and \(P_{a_r,b_r}\) from DP51. For every supported four-variable differential monomial, its integral polynomial coefficient multiplied by its multi-factorial is exactly, up to sign,

\[
\binom ai\binom bi(a-i)!(b-i)!(i!)^2=a!b!.
\tag{SH11}
\]

The contracted coefficient bound therefore gives the error valuation at least

\[
1-w_*m+v_p(a_r!b_r!)
=1+c_*m-2s_*.
\tag{SH12}
\]

This is strictly greater than the exact pure value \(c_*m-s_*\) by the same inequality (SH9). This calculation retains the binomial coefficients of the differential polynomial; using only a crude digit bound for its individual monomials would lose the constant-precision conclusion.

Thus approximation **modulo \(p\)** suffices simultaneously for every explicit ordinary or first-row harmonic witness whose degree is at most the interpolated order. Higher precision depending on the degree is unnecessary for these witnesses. It is not an assertion about arbitrary differential polynomials or arbitrary nearly sharp sequences.

## 3. Fixing all algebraic generators once

Work first over \(R_0\). Apply the integral projective-coordinate construction of DP56 to choose an exponent \(a\ge1\) and sections

\[
h_0,h_1,h_2,h_3\in H^0(J_{R_0},\mathcal L^{\otimes a})
\]

such that \(h_0(e)\) is a unit, \(h_i(e)=0\) for \(i>0\), and

\[
t_i=h_i/h_0\quad(1\le i\le3)
\tag{SH13}
\]

are integral formal parameters at zero. The unit cotangent minor and formal inversion were proved in DP56. The relative ampleness needed over \(R_0\), not only its completion, follows from the same positive-polarization closed-fibre argument in DP54.

Choose an integer \(b\) such that \(\mathcal L^{\otimes m}\) is globally generated for every \(m\ge b\). For each residue class \(\ell\pmod a\), choose one integer \(b_\ell\ge b\) in that class, and one section

\[
\eta_\ell\in H^0(J_{R_0},\mathcal L^{\otimes b_\ell})
\]

whose value at zero is a unit. There are only \(a\) such sections. Put

\[
b_0=\max_\ell b_\ell.
\tag{SH14}
\]

If \(\kappa\ge an+b_0\), choose \(\ell\equiv\kappa\pmod a\) and set

\[
q=\frac{\kappa-b_\ell}{a}\ge n.
\tag{SH15}
\]

Then the fixed generator \(\eta_\ell h_0^q\) is an integral frame on the infinitesimal neighbourhood of zero. This finite residue-class choice avoids choosing unrelated auxiliary sections with potentially uncontrolled norms for each new tensor exponent.

All these finitely many generators can be taken integral over \(A_0\) after multiplying by fixed scalars outside \(\mathfrak p\). Indeed flat cohomology base change for the localization \(A_0\to R_0\), Stacks Project Lemma 30.5.2(2), identifies each relevant section space over \(R_0\) with the localization of the section module over \(A_0\). Each of our finitely many sections therefore has one denominator in \(A_0\setminus\mathfrak p\). Such a denominator can be replaced by its numerator in \(\mathcal O_E\setminus\mathfrak p\), because only powers of 14 were inverted in \(A_0\). Clear all denominators of the \(h_i\)'s by a common algebraic integer outside \(\mathfrak p\), and clear those of the finitely many \(\eta_\ell\)'s likewise.

The multipliers remain units in \(R_0\), so the vanishing conditions, the unit values and the formal coordinates are preserved. A common multiplier on all \(h_i\)'s leaves the ratios (SH13) unchanged. These generators are now fixed elements of section modules over \(A_0\). Their powers introduce divisibility at other primes if a clearing scalar vanishes there, but they introduce no new denominators. The only inverted primes are the original bad-model primes 2 and 7.

## 4. Bounded integral representatives in the number field

The reduction map \(\mathcal O_E\to R/pR\) is surjective. More generally, for every positive integer \(C\),

\[
\mathcal O_E/p^C\mathcal O_E
\longrightarrow R_0/\mathfrak p^C R_0
\cong R/p^C R
\tag{SH16}
\]

is surjective. At 11 the two distinct unramified primes satisfy \(p\mathcal O_E=\mathfrak p\overline{\mathfrak p}\). The Chinese remainder theorem makes the first map the projection from

\[
\mathcal O_E/p^C\mathcal O_E
\cong\mathcal O_E/\mathfrak p^C\times
       \mathcal O_E/\overline{\mathfrak p}^{\,C}.
\]

Localization does not change \(\mathcal O_E/\mathfrak p^C\), since every denominator outside \(\mathfrak p\) is already a unit in that quotient. Completion likewise preserves these finite quotients. This verifies the representative assertion despite both localization and completion.

Only \(C=1\) is needed here. Fix one integral representative for each element of the finite residue field. This gives a fixed finite set \(\mathcal S\subset\mathcal O_E\) and a constant \(B\ge1\) such that

\[
|\sigma(c)|\le B
\quad\text{for every }c\in\mathcal S
\text{ and every }\sigma:E\hookrightarrow\mathbf C.
\tag{SH17}
\]

One may take an explicit set in this example: the residue of \(\zeta_7\) has degree three over \(\mathbf F_{11}\), so

\[
\mathcal S=
\{c_0+c_1\zeta_7+c_2\zeta_7^2:
              0\le c_0,c_1,c_2\le10\}
\tag{SH18}
\]

maps bijectively to \(\mathbf F_{11^3}\). Each of its elements is an algebraic integer, and every complex embedding has absolute value at most 30. This uses only the already computed order of 11 modulo 7 and the fact that a root of unity has complex absolute value one. In particular the representatives do not have hidden finite-prime denominators.

## 5. The algebraic interpolant with the required residue jet

Fix \(n,\kappa\) as in the theorem, choose \(\ell,q\) by (SH15), and use an integral formal frame \(\tau\) of \(\mathcal L\) at zero. In that frame put

\[
g_\kappa(z)=\frac{\eta_\ell(z)h_0(z)^q}{\tau(z)^\kappa}
\in R[[z]]^\times.
\tag{SH19}
\]

The quotient notation denotes the coefficient of the displayed section in the tensor frame. Its integrality and unit constant follow from the integral generators and their unit values.

Express the integral unit

\[
g_\kappa^{-1}U^{-\kappa}
\]

in the integral parameters \(t_1,t_2,t_3\), and truncate it through total degree \(n\):

\[
Q^*(t)=\sum_{|\alpha|\le n}q^*_\alpha t^\alpha,
\qquad q^*_\alpha\in R.
\]

For each coefficient choose \(q_\alpha\in\mathcal S\) with
\(q_\alpha\equiv q^*_\alpha\pmod p\), and set

\[
\boxed{
s_{n,\kappa}
=\eta_\ell\sum_{|\alpha|\le n}q_\alpha
  h_0^{q-|\alpha|}h_1^{\alpha_1}
  h_2^{\alpha_2}h_3^{\alpha_3}.}
\tag{SH20}
\]

All exponents are nonnegative because \(q\ge n\). Every term has tensor exponent \(b_\ell+aq=\kappa\). The fixed generators are integral over \(A_0\), and the coefficients are algebraic integers, so (SH20) is a global section over \(A_0\).

In the formal frame, multiplying its coefficient by \(U^\kappa\) gives

\[
g_\kappa U^\kappa\sum_{|\alpha|\le n}q_\alpha t^\alpha
\equiv1\pmod{p+(t)^{n+1}}.
\]

The integral formal coordinate change identifies \((t)\) with \((z)\), proving (SH3). Its constant term is a unit modulo \(p\); hence the global section is nonzero. Section 2 now proves all the exact selected valuation claims, including the product of two copies and any finite prefix whose degrees are at most \(n\).

This constructs the section over the number field directly, from finitely many fixed global generators and representatives in a fixed finite set. No coefficient precision or final section approximation grows with \(n\).

## 6. Archimedean norm estimate

Let \(H\ge1\) dominate, at all complex embeddings, the sup norms of the finitely many fixed sections \(h_0,h_1,h_2,h_3\) and \(\eta_\ell\), using the indicated tensor-power metrics. Such an \(H\) is finite by compactness and continuity. The product in each summand of (SH20) contains \(q\) sections of exponent \(a\), counting multiplicities, and one \(\eta_\ell\). Tensor compatibility therefore bounds its norm by \(H^{q+1}\).

There are

\[
T_n=\binom{n+3}{3}
\]

monomials of total degree at most \(n\). Combining the triangle inequality, (SH17), and (SH20) gives the explicit estimate

\[
\boxed{
\|s_{n,\kappa}\|_{\sigma,\sup}
\le B\binom{n+3}{3}H^{q+1}.}
\tag{SH21}
\]

Since \(q=(\kappa-b_\ell)/a\le\kappa/a\),

\[
\log\max\{1,\|s_{n,\kappa}\|_{\sigma,\sup}\}
\le\log B+\log\binom{n+3}{3}
       +(\kappa/a+1)\log H.
\tag{SH22}
\]

This proves (SH4). With the square-power choice of DP58, \(\kappa=an+O(\sqrt n)\), it proves the linear logarithmic norm bound (SH5). Summing over the six complex embeddings, with any fixed standard normalization, gives the same order bound for the corresponding archimedean section size.

## 7. Other primes and an adelic norm formulation

The section in (SH20) is integral on \(J_{A_0}\); no denominator depending on \(n\) or \(\kappa\) has been introduced outside the original primes 2 and 7. Fixed denominator clearing in §3 cannot worsen this: it multiplied sections by algebraic integers outside \(\mathfrak p\), rather than dividing the final sections by them.

If an adelic section-size statement is desired, fix tensor-compatible norms on the line at every place, induced by this model outside the places over 2 and 7, and continuous on the proper analytifications at the remaining places. At a model place every constructed section has sup norm at most one. This follows directly from the model definition of the norm and integrality of the section; properness extends points to the valuation ring.

At each of the finitely many remaining nonarchimedean places, let \(H_v\ge1\) bound the norms of the same fixed generators. The coefficients \(q_\alpha\) are algebraic integers, so \(|q_\alpha|_v\le1\). The ultrametric triangle inequality gives

\[
\|s_{n,\kappa}\|_{v,\sup}\le H_v^{q+1}.
\tag{SH23}
\]

Together with (SH22), this proves

\[
\frac1{[E:\mathbf Q]}\sum_v [E_v:\mathbf Q_v]
  \log\max\{1,\|s_{n,\kappa}\|_{v,\sup}\}
=O(\kappa+\log(n+1)),
\tag{SH24}
\]

where the archimedean local-degree convention is interpreted in the usual way. The sum is finite because all other terms vanish. For the linear tensor levels it is \(O(n)\). This is a bound for this explicitly specified sup-size; it is not a claim that an unspecified source norm has already been identified with it.

## 8. Metric and genuine complex-frame comparisons

Any two fixed continuous positive Hermitian metrics on \(\mathcal L\) over one compact complex fibre have a ratio bounded above and below by positive constants. On \(\mathcal L^{\otimes\kappa}\), the logarithmic discrepancy is therefore at most \(C_\sigma\kappa\). Hence (SH4) and its \(O(n)\) specialization persist for any other fixed such metric, including a geometric canonical theta metric when that metric is chosen. This elementary comparison uses compactness; it does not require an equality of metrics.

For a fixed honest holomorphic frame \(e_\sigma\) on a neighbourhood of zero, restrict to a fixed relatively compact analytic chart on which the frame never vanishes. Its metric norm has a positive minimum. Therefore writing a section as \(s=f_\sigma e_\sigma^{\otimes\kappa}\) costs at most another factor \(\exp(C_\sigma\kappa)\) in the coefficient sup norm. Multiplying by a fixed holomorphic canonical-gauge factor \(\exp(\kappa h_L)\) on that same compact chart likewise costs at most \(\exp(\kappa\sup\operatorname{Re}h_L)\). Thus an actually supplied fixed analytic frame and gauge preserve an \(O(\kappa+\log n)\) logarithmic local-function bound.

This does **not** assign an archimedean norm to the \(p\)-adic display frame: its coefficients may only lie in the completion. The theorem does not identify that formal frame with a source complex gauge, nor cover a family of level-dependent norm normalizations without a separate comparison. Those are source-specific identifications. The algebraic section itself, and its norms in the fixed line metrics, are already defined over the number field and are bounded as stated.

## 9. What remains after the norm bound

For these explicit witnesses, one now has actual number-field sections, integrality at all good-model primes, linear tensor powers, and linear logarithmic sup-size, with exact normalized local valuations. The sole use of residue representatives makes the coefficient-height assertion concrete: the coefficients of (SH20) belong to the fixed finite set (SH18), while the number and degrees of its monomials are controlled.

This is an existence and upper-bound construction in the full section space. It does not prove that the section lies in the prescribed torsion-translate span, that a prescribed global differential degree sequence is the explicit ray of DP58, or that the constants in the norm bound satisfy a favorable global gain-minus-cost inequality. It supplies no lower bound on unavoidable global costs and therefore does not, by itself, prove either existence or impossibility of a shorter theta-lift chain.

The actual source-family bridge and its integral normalization remain separate from the full-section construction here.

## 10. Inputs and actual review record

The fixed geometric model and integral trace-one line are DP49; positive relative ampleness and the normalized germ are DP54. The integral projective coordinates and ample-power generation are DP56, citing Stacks Project Tags 01VT and 01Q3. Localization of global sections is Stacks Project Lemma 30.5.2(2), Tag 02KH, already directly read in this work. DP46 and DP51 supply the contracted coefficient bounds, while DP58 supplies the exact witness values and every-unit-parameter independence.

The new points proved here are constant modulo-\(p\) precision for the exact ordinary and harmonic witnesses, the fixed finite residue-class generator construction, bounded algebraic coefficient representatives, and the resulting norm estimates with explicit metric scope. Actual whole-proof reading events and exact file hashes are recorded separately. No numerical experiment, Lean execution or machine formalization is claimed.
