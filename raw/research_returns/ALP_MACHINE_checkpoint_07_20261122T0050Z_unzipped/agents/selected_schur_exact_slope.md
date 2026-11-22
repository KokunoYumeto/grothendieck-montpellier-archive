# AM-K027 — the exact 11-adic slope in an actual full-Hyp3 selected family

Author: GPT-6 Astra Pro, ALP_MACHINE `/root/kummer_extension`, 21 November 2026 UTC. Inherited reasoning effort is not separately exposed.

The accepted DP51 common-weight theorem supplies the missing lower bound for AM-K024. The full CM gauge comparison AM-K018 now makes that theorem applicable to the actual ordinary host \(A=J^2\), including every integral local section and the exact DP59 half-orbit. The resulting fixed-rank, varying-weight selected family has **exact asymptotic normalized derivative slope \(1/1220\)**. The statement remains a selected kernel/first-extraction result. It does not identify the later restricted automorphic image or resolve the literal raw-Xi matching equation.

## 1. The common-weight bound in the actual source gauge

Let R be a finite unramified complete extension of \(\mathbb Z_{11}\) containing the needed CM eigenvalues and torsion. Normalize \(v(11)=1\). Set
\[
 J=\operatorname{Jac}(y^2=x^7-1),\qquad
 L=L_{2\infty},\qquad X=J^\ell,
\]
with its product principal line \(\mathcal L\), where \(\ell\) is fixed. Use the actual Chern/source reduced gauge of AM-K018, and let \(\kappa\) be a positive integer prime to 11. A section is integral here if its algebraic coefficient in an integral formal frame of \(\mathcal L^\kappa\) is integral. No ordinary Taylor integrality of the reduced frame is assumed.

Put
\[
                   w=\frac{121}{1220},\qquad
                   c=\frac1{1220},\qquad s=\frac1{10}.
\tag{EX1}
\]

### Proposition EX2. Full actual local-module estimate

For every integral formal local section S and its actual reduced germ \(F_S\), in the primitive ordinary J logarithmic coordinates or any integral invertible linear change of them,
\[
       v([z^\alpha]F_S)+w|\alpha|\ge0.
\tag{EX2}
\]
Consequently every integral homogeneous differential polynomial
\(P=\sum_{|\alpha|=D}p_\alpha Z^\alpha\) satisfies
\[
 v\bigl(P(\partial)F_S(0)\bigr)
 \ge \frac D{1220}
       -\frac1{10}\max_{\alpha\in\operatorname{supp}P}
                                 \sum_m s_{11}(\alpha_m).
\tag{EX3}
\]
Zero values have valuation \(+\infty\). For D≥1 the weaker uniform estimate is
\[
 v\bigl(P(\partial)F_S(0)\bigr)
 \ge \frac D{1220}
          -3\ell\bigl(1+\lfloor\log_{11}D\rfloor\bigr).
\tag{EX4}
\]
The constants in (EX2)–(EX4) are independent of \(\kappa\) as long as \(11\nmid\kappa\), and apply to the allowed levels \(\kappa=M^2\), \(M=29^e\).

**Proof and exact accepted interface.** DP49 identifies each actual formal J with its polarized arbitrary-unit singleton/complement block of height three. AM-K018, (K19.2) and (K19.13), identifies the source/Chern reduced section with
\[
              F_S=f_S\,\prod_{b=1}^{\ell}U_b^\kappa B_b^{-\kappa}
\tag{EX5}
\]
in the actual integral product frame. Here \(f_S\) is an arbitrary integral formal function on the product, and the \(U_b\) are integral units. These exact identifications are carried results; in particular there is no additional rational quadratic exponential.

Use accepted DP51 §6, (HA17)–(HA21), with p=11, h=3 and primitive parameter \(-\kappa\). Its common-weight substitution makes every full primitive kernel \(B_b^{-\kappa}\) integral at weight w, and makes the inverse logarithm maps integral at that same common weight. The latter statement applies to a joint prefactor as well as a separated product of prefactors: composing the integral series \(f_S\prod_bU_b^\kappa\) with the product of those zero-constant integral inverse maps is integral. Each resulting formal coefficient uses only finitely many terms of the prefactor. Thus no separated-factor hypothesis is needed for (EX5). This gives (EX2) directly from the accepted common-weight theorem.

If \(z=Cz'\) with \(C\in\operatorname{GL}_{3\ell}(R)\), the same common scale is applied to every coordinate. Substitution by C preserves integral coefficients at that scale; its inverse gives the converse. Hence (EX2) applies to the exact \(E'=\mathbb Q(\zeta_{28})\) coordinates \(z_{i,\pm}=u_i\pm i v_i\): both this matrix and its inverse are integral at 11. It also applies after the unit diagonal comparisons with the display eigenbasis.

Finally \(\partial^\alpha F_S(0)=\alpha![z^\alpha]F_S\). The Legendre identity
\[
 v(\alpha!)=\frac{|\alpha|-\sum_ms_{11}(\alpha_m)}{10}
\]
and \(1/10-w=1/1220\) prove (EX3) by the nonarchimedean triangle inequality. Bounding each digit sum by \(10(1+\lfloor\log_{11}D\rfloor)\) proves (EX4). These factorial manipulations are the same normalization as accepted DP51; no new display theorem is asserted. ∎

AM-K023 separately proves Hurwitz integrality of this entire actual local module. Thus the left side of (EX3) is also nonnegative, and an integer ceiling may be taken over the present unramified coefficient ring. The bound is a genuine full weighted coefficient estimate. It is not obtained by iterating the mod-11 normal form or by assuming a finitely generated differential-stable lattice, which AM-K019 excludes in the relevant unrestricted setting.

## 2. A sharper row-degree error for the selected module

On the actual edge \(U(a)\longrightarrow U(b)\), the Hom variety is \(J^{2ab}\), so \(3\ell=6ab\). Let the selected row degrees be the six partitions \(\nu_\tau\), and put
\[
 D=\sum_\tau|\nu_\tau|,\qquad
 d_{11}(n)=\begin{cases}0&n=0,\\1+\lfloor\log_{11}n\rfloor&n>0.\end{cases}
\]
Every monomial in a polynomial of these row degrees satisfies
\(\sum_{j=1}^b\alpha_{\tau,i,j}=\nu_{\tau,i}\). Since every entry in that row is at most \(\nu_{\tau,i}\), (EX3) gives
\[
 \boxed{
 v\bigl(P(\partial)F_S(0)\bigr)
 \ge \frac D{1220}
                 -b\sum_{\tau,i}d_{11}(\nu_{\tau,i}).}
\tag{EX6}
\]
This holds for every integral polynomial in the specified row-weight space, in particular for the fixed source-highest part of the actual selected Cauchy summand used here. The entire abstract tensor product of the source and target Schur modules also has other source row weights; (EX6), with these same individual row degrees, is not an assertion about all those other weight vectors. It introduces no abstract Schur projector. For the primitive highest prefix-minor polynomial using only the first a columns, b in (EX6) may be replaced by a:
\[
 v\bigl(P_{\boldsymbol\nu}(\partial)F_S(0)\bigr)
 \ge \frac D{1220}
                 -a\sum_{\tau,i}d_{11}(\nu_{\tau,i}).
\tag{EX7}
\]
These are statements in the explicit polynomial coefficient lattice. Changing to a different rationally normalized Weyl lattice requires its actual scaling factor.

For every \(M\ge3D+2\), AM-K022 identifies the image ideals of the formal jet matrix and the permitted half-orbit tuple matrix. The normalizing factor \(M^{-D}\) is an 11-unit. Consequently (EX3), (EX6), and (EX7) are also bounds for their actual allowed normalized kernel coefficients. The fixed period \(C^{2ab}\) remains outside these algebraic coefficient estimates.

## 3. Exact asymptotic slope for AM-K024

Fix one edge and its fixed residual partitions \(\nu_\tau^*\), as in AM-K024. In particular a,b and
\[
 D_0=\sum_\tau|\nu_\tau^*|,\qquad
 c_0=v\left(\prod_{\tau,i}\nu_{\tau,i}^*!\right)
\]
do not vary. Let \(Q_0\) be the residual prefix-minor polynomial on columns 2,…,a+1. Define the finite constant
\[
 K_0=\frac1{10}\max_{\beta\in\operatorname{supp}Q_0}
                                     \sum_m s_{11}(\beta_m).
\tag{EX8}
\]
It can be bounded explicitly by
\(a\sum_{\tau,i}d_{11}(\nu_{\tau,i}^*)\). Set
\[
 A_r=11^r,\quad B_r=121\,11^r,\quad
 T_r=122\,11^r+D_0.
\tag{EX9}
\]
AM-K024 supplies \(h_r\in[0,A_r]\), \(k_r\in[0,B_r]\) and the primitive integral polynomial
\[
 P_r=Z_{3,+,1,1}^{h_r}Z_{3,-,1,1}^{A_r-h_r}
     Z_{2,+,1,1}^{k_r}Z_{2,-,1,1}^{B_r-k_r}Q_0.
\tag{EX10}
\]
It already lies in the **same exact source-and-target Schur summand** with the selected partitions prescribed by (SC4). It is not merely a source-highest vector awaiting an unspecified target projection.

Choose \(M_r=29^{e_r}\) least with \(M_r\ge3T_r+2\). Let \(\mathfrak I_r\) be the derivative image ideal for \(P_r\) on the integral formal \(T_r\)-jet module of \(\mathcal L^{M_r^2}\); equivalently, by AM-K022 J30, it is the ideal generated by the actual allowed half-orbit tuple values. AM-K024 proves it is nonzero and
\[
          v(\mathfrak I_r)\le \frac{11^r-1}{10}+c_0.
\tag{EX11}
\]

The four growing variables in (EX10) are disjoint from all variables of \(Q_0\). Therefore the digit term in (EX3) is exactly bounded by
\[
 \frac{s_{11}(h_r)+s_{11}(A_r-h_r)
       +s_{11}(k_r)+s_{11}(B_r-k_r)}{10}+K_0
 \le4d_{11}(T_r)+K_0.
\]
Combining this lower bound with (EX11) proves
\[
 \boxed{
 \frac{T_r}{1220}-4d_{11}(T_r)-K_0
 \ \le\ v(\mathfrak I_r)
 \ \le\ \frac{T_r}{1220}
                 +c_0-\frac1{10}-\frac{D_0}{1220}.}
\tag{EX12}
\]
The same two bounds hold for an individual allowed tuple chosen to attain the image ideal. Such a tuple exists because the half-orbit basis is finite and generates that ideal; taking its least-valued nonzero entry attains the minimum. Its finite Schwartz vector is one translate of the fixed norm-one vacuum, with no interpolation coefficient height included.

It follows in particular that
\[
 \boxed{
 \lim_{r\to\infty}\frac{v(\mathfrak I_r)}{T_r}
 =\lim_{r\to\infty}\frac{v(a_r)}{T_r}
 =\frac1{1220}.}
\tag{EX13}
\]
This is a limit for the constructed sequence, stronger than a mere liminf upper bound. For the indices r covered by (EX13), the tuple, the selected first-row increments, and the level may vary; the ranks, residual partitions, host, and common edge character remain fixed.

By AM-K024 §2 and AM-K026 §1, choose the fixed residual partitions from the explicit full-Hyp3 baseline. Every subsequent nonnegative \(u_0\) increment preserves **all** clauses of that stronger analytic Hyp3, including Centred, NCGaps and the 1801 condition. Thus (EX13) holds inside that full analytic admissibility family. It does not preserve separately fixed SizeData₂ upper windows, nor does it by itself supply the complete old D7 arithmetic host.

## 4. Exact selected-metric and first-extraction normalization

For a fixed residual partition \(\lambda\) and first-row increment h, AM-K026 proves that the target vector represented by the primitive polynomial has squared norm
\[
 \theta_\lambda(h)=\frac{h!H_\lambda}{H_{\lambda+h e_1}}
  =\prod_{s\in S_\lambda}\frac{s}{h+s},
\tag{EX14}
\]
where \(S_\lambda\subset\{1,\ldots,\lambda_1+a-1\}\) is a fixed set of \(\lambda_1\) positive integers. Let \(\Theta_r\) be the product of the four such factors for the increments in (EX10). The product formula gives both valuation bounds
\[
 -|S_\lambda|\log_{11}(h+\lambda_1+a)
 \le v(\theta_\lambda(h))
 \le\sum_{s\in S_\lambda}v(s).
\tag{EX15}
\]
Thus \(v(\Theta_r)=O(\log(T_r+1))\), with a fixed constant depending on the residual partitions. Normalizing the target vector multiplies its algebraic value by \(\Theta_r^{-1/2}\), an explicitly retained algebraic scalar. Equations (EX12)–(EX15) imply
\[
             \lim_{r\to\infty}
       \frac{v(a_r/\sqrt{\Theta_r})}{T_r}=\frac1{1220}.
\tag{EX16}
\]
There is no claim that this square-root normalization is integral.

In the concrete compact class-supported first extraction of AM-R-012, the further unit-input factor is
\(1/\sqrt{I_a(M_r)\dim\rho_r}\). For fixed a,b,
\[
 I_a(M)=M^{6a^2}\prod_{i=1}^a(1-29^{-i})^6
\]
has 11-valuation independent of the exponent e, and the dimension ratios under first-row growth are products of fixed finitely many linear factors in the growing increments. Hence \(v(\dim\rho_r)=O(\log(T_r+1))\). Retaining the common period, that specific first value has the form
\[
 C^{2ab}\,
       \frac{a_r}{\sqrt{\Theta_r I_a(M_r)\dim\rho_r}},
\tag{EX17}
\]
with the exact mass convention of AM-R-012. Its algebraic coefficient after removal of the fixed period again has slope \(1/1220\). This conclusion is about that explicitly constructed first extraction. The raw source-array matching and any later restriction to a previously produced automorphic image are separate gates, not consequences of the normalization calculation.

The full archimedean creation norm is still the exact expression in AM-K026 (HC25), or equivalently the corresponding product of new hooks after dividing by \(\Theta_r\). Its factorial growth has not been replaced by an \(O(\log T_r)\) assertion. Only the specified target comparison and fixed-rank class/dimension factors have logarithmic logarithm or valuation corrections. These are different quantities and must not be conflated in a net gain/error computation.

## 5. Stronger compulsory bounds for the concrete full-Hyp3 baseline

The bounds above also sharpen AM-K026's first-divisibility conclusion without using any iteration of a congruence. In its exact example
\[
 k=6,\quad m=2,\quad t=1795,\quad d=1796,
 \qquad Q=46\,539\,457\,175,
\]
the two edge partitions are
\[
 \nu_0=(Q^6),\qquad
 \nu_1=((3Q)^6,(2Q)^{1796})
\]
at each of the six labels. Every positive row part has 11-adic digit length 11. Applying (EX6) and (EX7), then taking integer ceilings, gives:

| Edge | Degree D | Lower bound for every integral selected polynomial in the fixed source-highest row space | Lower bound for the primitive highest prefix-minor coefficient | Adjacent-gap upper bound for that highest coefficient |
|---|---:|---:|---:|---:|
| 6 → 1802 | 1,675,420,458,300 | 1,372,581,866 | 1,373,293,082 | 167,542,045,704 |
| 1802 → 3598 | 1,008,044,642,410,500 | 825,838,183,001 | 826,051,784,873 | 100,804,464,197,676 |

The upper bounds are AM-K026's exact adjacent-gap factorial bounds, hence apply to the image ideals and to some individual permitted tuple. The lower bounds hold for every integral section in the corresponding local module and every indicated polynomial in the stated fixed row space. The middle two columns do not assert that every element of a rationally rescaled abstract selected lattice is integral in this polynomial coefficient lattice.

These intervals are genuine local coefficient bounds, but they still leave a wide range for the exact positive Smith valuation of this particular fixed baseline. The asymptotically exact conclusion (EX13) instead concerns the explicitly varied first-row family. Neither statement computes the selected class matrix restricted to a previous theta image.

## 6. Sources, new content, and check scope

The display and common-weight estimates are accepted results, not newly derived results:

- Supplied DP51, `research/harmonic_asymptotic_rate_DP51.md`, §6, (HA17)–(HA21): entire polynomial module, exact common weight and factorial digit error. The full statement and proof were read for this application.
- Supplied DP46, `research/unit_arrow_kernel_invariance_DP46.md`, §§4–6, especially (UI16)–(UI20): arbitrary unit arrows, integral inverse-map profile and invariant integral frames.
- Supplied DP59, `research/theta_translate_span_DP59.md`, §§6–8, especially the lower-bound argument in §7: actual integral half-orbit basis, formal prefactor and normalized derivative convention.
- AM-K018 (K19.2), (K19.13): exact actual source/Chern gauge on ordinary J powers; AM-K022 J30: equality of all finite determinantal ideals; AM-K024 (SC4)–(SC20): the exact selected witness, full-Hyp3 preservation and its fixed filler; AM-K026 (HC18)–(HC25): exact target norm and mass comparisons.
- AM-DO-025: actual source-and-target Cauchy labels; AM-R-011: selected metric; AM-R-012: concrete class-supported first extraction. Their source and primary bibliographic locators are retained in those reports.

The new deductions are the transfer of the accepted full common-weight estimate to every actual ordinary-product local section, its row-support version (EX6)–(EX7), the matching selected-family sandwich and limit (EX12)–(EX13), and the retained normalized limit (EX16)–(EX17). The finite arithmetic table has a separate exact certificate. No Lean build, new display proof, full source instance, positive Smith-factor computation, or later-image valuation theorem is claimed.
