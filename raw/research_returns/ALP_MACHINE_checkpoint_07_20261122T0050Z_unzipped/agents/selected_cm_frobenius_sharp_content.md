# AM-K033 — explicit sharp selected content in the enlarged CM eigenbasis

Author: GPT-6 Astra Pro, ALP_MACHINE /root/kummer_extension, 22 November 2026 UTC; inherited reasoning effort not separately exposed.

This finding identifies an explicit pair of CM labels on the actual \(J^{14}\) host, and on its weighted \(J^{56}\) extension, that retains the exact sharp primitive-kernel derivative. A fixed filler places this pair inside the full source-and-target selected Schur summand. The resulting image ideals in the actual permitted DP59 half-orbit have asymptotic slope \(1/1220\), with a bounded additive error before compact metric normalization.

The proof computes the full critical logarithmic form after the seven-copy eigenbasis change. It does not infer selected sharpness merely from an invertible change of the ambient tangent lattice. The accepted display and exponential theorems are used at their exact interfaces; their proofs are not rederived. The conclusion concerns the selected kernel lattice. A previously produced automorphic image or a separately imposed auxiliary finite G-vector can still impose a further restriction.

## 1. Actual hosts, coordinates, and accepted primitive input

There are two cases:

| Parameter h | Host field | Principal variety | CM type count f |
|---:|---|---|---:|
| 1 | \(K=E_0B\), \(E_0=\mathbb Q(\zeta_{28})\), \(B\subset\mathbb Q(\zeta_{29})\), \([B:\mathbb Q]=7\) | \(J^{14}\) | 42 |
| 4 | \(K^*=K(\sqrt5,\sqrt{13})\) | \(J^{56}\) | 168 |

The integral actions, principal product identifications and standard CM lattice coefficients are AM-K030 and AM-K032. Work at11 over a finite unramified complete coefficient DVR R large enough for the CM eigenvalues and torsion being used, with \(v(11)=1\). Each level can use a larger finite unramified extension; none of the bounds depends on its degree. The coefficient-field extension needed for an unrelated global etaVal is not being asserted unramified.

Use the K030 basis \(e_0,\ldots,e_6\) of \(\pi_B^{-3}\mathcal O_B\), with
\[
 e_j=\sigma^j e_0,\qquad
 \sigma=(\zeta_{29}\mapsto\zeta_{29}^{\,2})|_B,\qquad
 U_{lj}=\sigma^l(e_j),\qquad U^{\mathsf t}U=UU^{\mathsf t}=I_7.
\tag{CS1}
\]
Here indices l,j lie in \(\mathbb Z/7\mathbb Z\), and
\(\pi_l=\sigma^l(\pi_B)\). All entries of U and its inverse and all \(\pi_l^{\pm1}\) are integral at11.

Let \(\mathcal R\) be a singleton when h=1. When h=4, let \(\mathcal R\) be the four embeddings of \(\mathbb Q(\sqrt5,\sqrt{13})\); for \(\rho=(\epsilon,\epsilon')\) put
\[
 \delta_\rho=\delta_{1,\epsilon}\delta_{3,\epsilon'},
 \qquad
 u_a=\frac{a+\sqrt{a^2+4}}2,\quad
 \delta_a=\frac{u_a^{-1}}{\sqrt{a^2+4}},\quad a=1,3.
\tag{CS2}
\]
For h=1 set \(\delta_\rho=1\). Every \(\delta_\rho\) is an11-unit.

The standard CM logarithmic coordinates will be denoted
\[
            \zeta_{i,\varepsilon,l,\rho},
       \qquad i=1,2,3,\quad \varepsilon\in\{+,-\},
                \quad l\in\mathbb Z/7\mathbb Z,\quad\rho\in\mathcal R.
\tag{CS3}
\]
For h=1, they are exactly
\[
 \zeta_{i,\pm,l}=\pi_l^3\sum_{j=0}^{6}U_{lj}
                                  (u_{i,j}\pm i v_{i,j}).
\tag{CS4}
\]
For h=4, apply in addition the two embedding matrices
\[
 V_a=\begin{pmatrix}1&u_{a,+}\\1&u_{a,-}\end{pmatrix},
 \qquad
 V_a^{\mathsf t}\operatorname{diag}(\delta_{a,+},\delta_{a,-})V_a=I_2,
\tag{CS5}
\]
on the four ordinary real tensor factors, as in K032(QH18–21). The same final \(\pi_l^3\) rescaling gives the standard lattice coordinates. All changes and their inverses are integral at11. They preserve the ordinary J label i.

For one ordinary J, the accepted DP49 decomposition and K018's actual source-gauge comparison give an integral normalized algebraic frame in which the reduced coefficient of a local section of level \(\kappa\) is
\[
                   f\,U_0^\kappa\exp(-\kappa\beta).
\tag{CS6}
\]
Here f is an arbitrary integral formal function, \(U_0\) is an integral unit, and \(\beta\) is the actual arbitrary-unit primitive logarithm. This formula is used on identical copies with the identical choice of ordinary tangent basis \(u_i\). Thus every copy has the same critical unit below. Choosing \(f=U_0^{-\kappa}\) is an actual integral formal-section choice. It does not assert that the fixed sigma section itself equals the pure kernel.

Put
\[
                  s=\frac1{10},\qquad w=\frac{121}{1220},
                         c=s-w=\frac1{1220}.
\tag{CS7}
\]
Choose a finite ramified scaling extension with \(v(\varpi)=w\), and put
\[
                      \mu=\frac{\varpi^{122}}{11^{12}},
                           \qquad v(\mu)=s.
\tag{CS8}
\]
Only this auxiliary Gauss-weight argument uses the ramified extension. The derivative values themselves remain in the original unramified coefficient ring.

### Exact accepted whole-series input

DP46(UI16–19), with h=3 and j=1, and the common-weight substitution of DP51 §6 give
\[
 \mu^{-1}\beta(\varpi u_1,\varpi u_2,\varpi u_3)
        \text{ integral},\qquad
 \overline{\mu^{-1}\beta(\varpi u_1,\varpi u_2,\varpi u_3)}
                         =\theta\,u_3u_2^{121},
                   \quad \theta\ne0.
\tag{CS9}
\]
This is the reduction of the **entire** scaled logarithm, not its first ordinary-degree term. To spell out the application: in DP46's contracted dual inverse, raising the later input \(y_2\) to the common weight w makes that input vanish in the reduction, since its profile weight is strictly smaller than w. The reduced inverse has \(Y_1=y_1\) and \(Y_2=-\bar a_1^{-1}y_1^{11}\); substitution into the complete minimum \(\bar a_2^{-1}S Y_2^{11}\) gives (CS9). The diagonal unit change from those display coordinates to the fixed ordinary CM eigenforms changes only the nonzero unit \(\theta\). Invariant integral frame changes are strictly above this critical form by DP46 §5. This is a direct use of the accepted full inverse-map and initial-form statements.

For an integral unit parameter \(\lambda\), the right side of (CS9) is multiplied by \(\bar\lambda\). In the actual tensor-level application \(\lambda=-\kappa\), where \(\kappa=M^2\), \(M=29^e\); hence it is always a unit.

## 2. Frobenius computes the new critical pairs

Bars denote residue-field reduction at11. For the unramified constants this is reduction modulo11; for the auxiliary ramified scaling extension it means reduction modulo its maximal ideal. On B, arithmetic Frobenius is the class of11 in
\((\mathbb Z/29\mathbb Z)^\times/H\), where \(H=\{1,12,17,28\}\).
One has \(11\in2^4H\) and \(121\equiv5\in2H\pmod{29}\). Therefore
\[
                   \overline{U_{lj}}^{\,121}
                            =\overline{U_{l+1,j}},\qquad
                   \bar\pi_l^{\,121}=\bar\pi_{l+1}.
\tag{CS10}
\]
This follows for the denominators29 as well because they are11-units. Equivalently, if P shifts the row l to l+1, then \(\bar U^{(121)}=P\bar U\).

On the two quadratic real fields, Frobenius squared is the identity, since their Galois groups have exponent2 and11 is unramified. Consequently
\[
                   \bar V_a^{(121)}=\bar V_a.
\tag{CS11}
\]
Also \(i^{121}=i\) modulo11.

Let \(\beta_{\rm prod}\) be the sum of the primitive logarithms on all14h ordinary J factors at one fixed matrix entry of a Hom variety. Since the principal polarization and the chosen invariant frame are products, this is the logarithm of the actual product primitive kernel in (CS6).

### Theorem CS12. Full critical form in standard CM coordinates

For every unit \(\lambda\), in the coordinates (CS3),
\[
 \boxed{\ 
 \overline{\mu^{-1}\lambda
       \beta_{\rm prod}(\varpi\boldsymbol\zeta)}
 =
 \frac{\bar\lambda\theta}{2}
 \sum_{\varepsilon,l,\rho}
       \bar\delta_\rho\,\bar\pi_{l+1}^{-6}\,
       \zeta_{3,\varepsilon,l+1,\rho}\,
                \zeta_{2,-\varepsilon,l,\rho}^{121}.\ }
\tag{CS12}
\]
The left side denotes the same actual logarithm expressed in the new coordinates before the common scaling. Every displayed coefficient is a nonzero residue. All scaled coefficients before reduction are integral.

**Proof.** Start with (CS9) on the ordinary factors and sum them. On one pair of ordinary J copies write \(w_{i,\pm}=u_i\pm i v_i\). In characteristic11, since \(121\) is a Frobenius power and fixes i,
\[
 u_3u_2^{121}+v_3v_2^{121}
  =\frac12\left(w_{3,+}w_{2,-}^{121}
                          +w_{3,-}w_{2,+}^{121}\right).
\tag{CS13}
\]
For each sign the B-coordinate change is z=Uw, with inverse \(w=U^{\mathsf t}z\). Thus the coefficient pairing between the new B labels k,l is
\[
 \sum_j\bar U_{kj}\bar U_{lj}^{121}
       =\sum_j\bar U_{kj}\bar U_{l+1,j}
       =\begin{cases}1&k=l+1,\\0&k\ne l+1.\end{cases}
\tag{CS14}
\]
This uses the actual trace orthogonality, rather than a complex-unitary approximation or a generic invertibility assertion.

In the quadratic extension, the inverse-coordinate pairing is
\[
  (\bar V_a^{-1})^{\mathsf t}
                 (\bar V_a^{-1})^{(121)}
   =\bar V_a^{-\mathsf t}\bar V_a^{-1}
   =\operatorname{diag}(\bar\delta_{a,+},\bar\delta_{a,-}),
\tag{CS15}
\]
by (CS5) and (CS11). Taking the tensor product for the two quadratics introduces exactly \(\bar\delta_\rho\) and forces the same real embedding \(\rho\) on the paired labels. For h=1 this step is absent.

Finally \(z_{i,\varepsilon,l,\rho}=\pi_l^{-3}\zeta_{i,\varepsilon,l,\rho}\). On a nonzero pair the two factors contribute
\[
              \bar\pi_{l+1}^{-3}
                        (\bar\pi_l^{-3})^{121}
                              =\bar\pi_{l+1}^{-6}.
\tag{CS16}
\]
Equations (CS13)–(CS16) prove the displayed form.

All coordinate substitutions and inverses are integral at11, and the same scale \(\varpi\) is used on every input. Substitution therefore commutes with reduction and preserves integrality of the entire scaled logarithm in (CS9). At a fixed ordinary degree there are only finitely many coefficients involved. This verifies the whole-series assertion and rules out an unexamined logarithmic term at the same critical valuation. ∎

There are fourteen nonzero pairs when h=1 and fifty-six when h=4. In particular, fix l and \(\rho\), and set
\[
                \tau_3=(3,+,l+1,\rho),\qquad
                \tau_2=(2,-,l,\rho).
\tag{CS17}
\]
On the plane where only \(X=\zeta_{\tau_3}\) and \(Y=\zeta_{\tau_2}\) are nonzero, (CS12) is exactly one nonzero monomial \(\gamma XY^{121}\). Thus the critical-exponential lemma DP58(ES6–12) applies directly to this explicit new-CM plane.

For
\[
                  A_r=11^r,\qquad B_r=121\,11^r,\qquad r\ge0,
\tag{CS18}
\]
it gives, for the actual product primitive kernel
\(F_\lambda=\exp(\lambda\beta_{\rm prod})\),
\[
 \begin{split}
 v\bigl([\zeta_{\tau_3}^{A_r}\zeta_{\tau_2}^{B_r}]F_\lambda\bigr)
                  &=-\frac{121\,11^r-1}{10},\\
 \boxed{\ 
 v\!\left(
       \partial_{\tau_3}^{A_r}\partial_{\tau_2}^{B_r}
                      F_\lambda(0)\right)
                     =\frac{11^r-1}{10}.\ }
 \end{split}
\tag{CS19}
\]
The first equality uses the full critical monomial, uniformly for every unit \(\lambda\). The second adds the two exact Legendre factorial valuations; both exponents are powers of11. Every derivative in (CS19) is nonzero.

This calculation locates the sharp primitive kernel in a particular pair of the enlarged CM eigenspaces. It does not enlarge the accepted singleton/complement display theorem to an arbitrary higher-height CM word.

## 3. An explicit actual selected Schur family

Fix an admissible source rank record and an edge with
\[
                    a=N_j,\qquad b=N_{j+1}=a+d,
                         \qquad d=t+1\ge2.
\tag{CS20}
\]
Choose fixed word-independent HC data on all f embeddings and let
\(\nu_\tau^*\) be its actual selected positive partitions of length a, as in the literal identities checked in DO025. The numerical full-Hyp3 baselines of K031 and K032 are concrete choices on the two hosts. Put
\[
 D_0=\sum_\tau|\nu_\tau^*|,\qquad
 \mathcal F_0=\prod_{\tau,i}\nu_{\tau,i}^*!,\qquad
                        c_0=v(\mathcal F_0).
\tag{CS21}
\]
Ranks, the edge, the baseline, both fields and all stage characters remain fixed as r varies.

Reserve column1 of each a-by-b creation-symbol matrix \(Z_\tau\). Define on columns2 through a+1
\[
 Q_0(Z)=\prod_\tau\prod_{q=1}^{a}
    \det Z_{\tau,[1,q],[2,q+1]}^{
                                  \nu_{\tau,q}^*-\nu_{\tau,q+1}^*},
          \qquad\nu_{\tau,a+1}^*=0.
\tag{CS22}
\]
Here \([2,q+1]\) means the consecutive q columns \(2,\ldots,q+1\). Each such column exists because b≥a+1. Set
\[
 \boxed{\ 
 P_r=Z_{\tau_3,1,1}^{A_r}
             Z_{\tau_2,1,1}^{B_r}\,Q_0(Z),\qquad
 T_r=A_r+B_r+D_0=122\,11^r+D_0.\ }
\tag{CS23}
\]
This polynomial is explicitly prescribed; no unknown distribution among the seven copies is selected.

Increase the first HC entry \(u_0\) by \(A_r\) at \(\tau_3\), by \(B_r\) at \(\tau_2\), and by zero at every other place. Make the same modifications for every word. The selected partitions on the fixed edge become exactly
\[
 \nu_{\tau_3}=\nu_{\tau_3}^*+A_r e_1,\qquad
 \nu_{\tau_2}=\nu_{\tau_2}^*+B_r e_1,\qquad
                       \nu_\tau=\nu_\tau^*\text{ otherwise}.
\tag{CS24}
\]
All e entries are unchanged. Thus the actual uniform characters supplied in K031/K032 stay the same, as do their compact G restrictions and conductors. The word row condition and the common first/last-u equations in Wts.Ok are preserved: the row data v,b,e do not change, and the first-u modification is common to every word.

Every HC inequality survives an increase of the largest u. The full numerical Hyp3 survives as well when the baseline satisfies it. The Dpar and NCGaps lists contain no u; the parity, eta and1801 clauses are unchanged. Interlacing and \(u_{\rm last}>-b_0\), together with \(e_j\ge e_0>b_0\), imply \(u_i+e_j>0\). Increasing \(u_0\) increases the absolute value in the only changing Centred inequalities. This checks all clauses, not only HC interlacing. Independently fixed upper SizeData windows are not preserved.

### Proposition CS25. Exact source-and-target summand

The polynomial \(P_r\) is primitive integral and already belongs to the exact compact Cauchy summand indexed by the partitions (CS24), with the source and target determinant twists of DO025.

**Proof.** Prefix minors are invariant under adding an earlier row to a later row. Multiplication by a first-row variable retains this invariance. The row degrees telescope to (CS24). The product of the minor diagonal monomials and the two first-column powers has coefficient one, and no other determinant choices produce the same all-diagonal filler monomial. Thus \(P_r\) is primitive in the actual polynomial coefficient lattice.

Over characteristic zero, the Cauchy decomposition at each CM place is
\[
       \operatorname{Sym}(T_\tau\otimes S_\tau^*)
          =\bigoplus_\lambda S_\lambda(T_\tau)\otimes S_\lambda(S_\tau)^*.
\tag{CS25}
\]
In the source representation of a particular summand, its maximal-unipotent invariant line has precisely the source highest weight labelled by that \(\lambda\), and no other such invariant weight. Hence the source-invariant row weight \(\nu_\tau\) of \(P_r\) selects only \(\lambda=\nu_\tau\). The target vector can be non-highest, but it lies entirely in \(S_{\nu_\tau}(T_\tau)\), rather than being a sum of different target Schur types. Tensoring over the CM places and restoring DO025's fixed determinant twists proves the claim. No rational Schur projector or unspecified lattice denominator occurs. ∎

## 4. Exact formal value and the permitted image ideal

On the Hom variety
\[
            X=(J^{14h})^{ab}=J^{14hab},
                   \qquad \mathcal L=L_{2\infty}^{\boxtimes14hab},
\tag{CS26}
\]
take the actual source/Chern reduced gauge, which is K018's full-CM gauge by K030/K032. Fix any allowed \(M=29^e\) and \(\kappa=M^2\).

At row1, column1 choose the integral formal prefactor in (CS6) that cancels the product of the normalized algebraic frame units. This produces the actual product primitive kernel with parameter \(-\kappa\). On the filler entries choose an integral algebraic monomial whose leading logarithmic term in the standard CM basis is
\[
                    \prod_{\tau,i}
                         \zeta_{\tau,i,i+1}^{\,\nu_{\tau,i}^*}.
\tag{CS27}
\]
Such an integral monomial exists because the new CM tangent basis is integral invertible at11: choose integral formal parameters with precisely those linear differentials. Its degree is D₀. On unused entries use normalized integral frame prefactors, giving reduced value1 at zero.

The first matrix entry and all filler entries are different product factors. The degree-D₀ filler derivative cannot see higher terms of its algebraic coordinates or of its reduced frame. The matching diagonal monomial has coefficient one in Q₀, and all other exponent vectors differ. Consequently its evaluation is **exactly** \(\mathcal F_0\); no factorial is inverted. Combining with (CS19) gives an actual integral formal section \(S_r\) such that
\[
 \boxed{\ 
 v\!\left(
 M^{-T_r} P_r(\partial)F_{S_r}(0)\right)
                =\frac{11^r-1}{10}+c_0.\ }
\tag{CS28}
\]
The unit \(M^{-T_r}\) is the source's normalized level reading. This is a value on an integral formal-section lattice; it is not yet a value of the fixed untranslated sigma section.

Let \(\mathfrak I_r\) be the image ideal of this normalized functional on the full integral formal \(T_r\)-jet module of \(\mathcal L^{M^2}\). Choose
\[
      M_r=29^{e_r},\qquad
      e_r=\max\{1,\lceil\log_{29}(3T_r+2)\rceil\}.
\tag{CS29}
\]
K031/K032 and the exact DP59/K022 half-orbit theorem give
\[
 \mathcal W_{M_r}=[\alpha]^*H^0(X,\mathcal L^{M_r}),
 \quad\alpha=(1+2\sqrt{-7})^{e_r},\quad
 \operatorname{rank}\mathcal W_{M_r}=M_r^{fab},
\tag{CS30}
\]
with its actual integral translated basis indexed by
\(X[\alpha^2]/X[\alpha]\), and rescaled translations \(M_rt'\in X[\alpha]\).
Its map to the integral \(T_r\)-jets is surjective. Therefore \(\mathfrak I_r\) is exactly the ideal generated by its actual allowed tuple values. From (CS28),
\[
                           v(\mathfrak I_r)
                          \le\frac{11^r-1}{10}+c_0.
\tag{CS31}
\]
This ideal is nonzero. A tuple attaining the least nonzero valuation exists because the basis is finite. It is one actual algebraic allowed tuple, although the formal interpolating coefficients may have been complete-local. Its finite Schwartz vector has norm one. The interpolation coefficient vector is not charged as an actual chosen input.

## 5. A matching lower bound with constant error

Let
\[
 K_0=\frac1{10}
       \max_{\beta\in\operatorname{supp}Q_0}
                                 \sum_m s_{11}(\beta_m).
\tag{CS32}
\]
This is a finite fixed constant, independent of r and M. One computable bound is
\[
                 K_0\le a\sum_{\tau,i}d_{11}(\nu_{\tau,i}^*),
 \qquad
 d_{11}(n)=
 \begin{cases}0&n=0,\\1+\lfloor\log_{11}n\rfloor&n>0.\end{cases}
\tag{CS33}
\]
The accepted DP51 full common-weight bound, transferred to the actual integral local module in K027(EX2–5), applies to every section here. The new standard CM change is integral invertible, so that full bound applies in these coordinates as well.

Every monomial of \(P_r\) has the two fixed growing exponents Aᵣ and Bᵣ in columns disjoint from Q₀. Both have base11 digit sum1. The factorial digit loss is therefore exactly bounded by \(1/5+K_0\), rather than by a number growing with r. Thus
\[
 \boxed{\ 
 \frac{T_r}{1220}-\frac15-K_0
 \ \le\ v(\mathfrak I_r)\
 \le\frac{T_r}{1220}
                  +c_0-\frac1{10}-\frac{D_0}{1220}.\ }
\tag{CS34}
\]
The same lower bound holds for every integral section; the individual allowed tuple attaining \(\mathfrak I_r\) satisfies both bounds. All derivative values are Hurwitz-integral by K023, so the lower bound may also be replaced by its nonnegative integer ceiling.

In particular
\[
             \boxed{\ 
             \lim_{r\to\infty}\frac{v(\mathfrak I_r)}{T_r}
              =\lim_{r\to\infty}\frac{v(a_r)}{T_r}
                                      =\frac1{1220}.\ }
\tag{CS35}
\]
More precisely, \(v(\mathfrak I_r)-T_r/1220\) stays in the fixed interval displayed in (CS34). This proves sharpness in an **explicitly prescribed** full-CM selected family on either enlarged host. It is stronger than an ambient uniform-slope obstruction, and it has no hidden CM weight projection.

For the empty filler the same argument even gives
\(v(\mathfrak I_r)=(11^r-1)/10\): the lower bound is less than this integer by only1/10. That empty-filler observation is not an assertion of the full source HC/Hyp3 conditions. The nonempty actual baseline filler is retained in (CS21)–(CS35).

For the concrete first-edge baselines already constructed in K031/K032, the constants are as follows. The last column concerns only comparison of the growing degree \(122\cdot11^r\) with D₀; it does not replace the large fixed upper error c₀.

| Actual host and fixed edge | D₀ | c₀ | Computable bound for K₀ | First r with \(122\cdot11^r\ge D_0\) |
|---|---:|---:|---:|---:|
| \(J^{14}\), 42→1802 | 3,504,831,920,337,006 | 350,483,192,023,230 | 899,640 | 13 |
| \(J^{56}\), 168→1802 | 194,467,812,219,985,248 | 19,446,781,221,824,712 | 60,484,032 | 15 |

These are exact finite sums of the actual selected baseline parts and their factorial valuations, reproduced in the certificate. Thus the bounded-error asymptotic theorem retains a potentially substantial finite baseline cost. It does not itself certify a useful fixed numerical MainX window.

## 6. Metric and first-image scope

The primitive target vector in the Cauchy summand has the exact metric correction already proved in K026:
\[
 \Theta_r=
 \frac{A_r!\,H_{\nu_{\tau_3}^*}}
               {H_{\nu_{\tau_3}^*+A_re_1}}\,
 \frac{B_r!\,H_{\nu_{\tau_2}^*}}
               {H_{\nu_{\tau_2}^*+B_re_1}}.
\tag{CS36}
\]
Here H is the hook product. Each quotient is a fixed finite product \(s/(n+s)\), so its real logarithm and its11-adic valuation have size \(O(\log(T_r+1))\), with the residual partitions fixed. Scaling the target vector to norm one multiplies the coefficient by \(\Theta_r^{-1/2}\); it is not treated as an integral unit. Hence its valuation slope is still \(1/1220\).

All real creation factors remain explicit. In standard coordinates put
\[
        h_\tau=\frac{\delta_\rho\,\pi_l^{-6}}{2G_i},
           \qquad \tau=(i,\varepsilon,l,\rho).
\tag{CS37}
\]
At the chosen complex realization these numbers are positive. The actual squared archimedean Schwartz norm of the primitive vector is
\[
 \begin{split}
 \|r_{P_r}\phi_{0,\infty}\|^2
   ={}&\det(2Y)^{-7hab}\,
          A_r!B_r!\prod_\tau H_{\nu_\tau^*}\\
      &{}\cdot(\pi h_{\tau_3})^{A_r}
                (\pi h_{\tau_2})^{B_r}
                 \prod_\tau(\pi h_\tau)^{|\nu_\tau^*|}.
 \end{split}
\tag{CS38}
\]
The two first-column powers and all filler variables are disjoint, so their Fischer norms multiply. The hook normalization is the exact parent R011/K026 normalization, and K030/K032 give the metric coefficients. This factorial archimedean cost is not an \(O(\log T_r)\) term. Dividing (CS38) by \(\Theta_r\) is an alternative target normalization of the same vector, not an additional independent loss.

For the rational29 principal class refinement, the exact index is
\[
             I_a(M)=M^{fa^2}
                         \prod_{q=1}^{a}(1-29^{-q})^{6h}.
\tag{CS39}
\]
Its11-adic valuation is independent of the exponent in M. If a class-supported extraction with the chosen finite compact type is supplied, its compact dimension factor varies by the two fixed-rank Weyl ratios
\[
 \prod_{j=2}^{a}
 \frac{A_r+\nu_{\tau_3,1}^*-\nu_{\tau_3,j}^*+j-1}
                  {\nu_{\tau_3,1}^*-\nu_{\tau_3,j}^*+j-1}
 \quad\text{and the analogous factor with }B_r,\tau_2.
\tag{CS40}
\]
These have11-valuation \(O(\log(T_r+1))\). Thus these specified metric/class corrections alone preserve the local slope. The fixed product period is \(C^{14hab}\) in the conventions of DO034, and remains separate.

There are two important restrictions on this conclusion. First, the value \(a_r\) in (CS35) comes from the unmodified allowed translated vacuum and the selected polynomial. DO034's finite Steinberg auxiliary vector, or LIFT20's literal raw G factor, defines a different functional. A separate simultaneous-germ argument is required before assigning that restricted functional the same sharp upper slope. The factorial nonvanishing theorem for an arbitrary auxiliary vector does not establish this sharper assertion. Second, the next automorphic stage acts on a previous theta image, which is a further integral sublattice. Neither (CS34) nor a nonzero theta-representation theorem determines its saturation or prevents cancellation after the class integral.

The new theorem therefore closes the enlarged-CM selected-kernel sharpness gap. It does not close the later-image arithmetic or the complete DP44 gain/error inequality. The common-type field obstruction Fields.Kq=\(\mathbb Q\) remains, including on the8-divisible host.

## 7. Exact inputs and finite certificate

- Accepted DP46, unit_arrow_kernel_invariance_DP46.md, UI16–19 and §5: full scaled inverse maps, critical logarithmic initial form, and invariant-frame comparison. Accepted DP51, harmonic_asymptotic_rate_DP51.md, §6 HA17–21: the common weight on every variable and full local-module bound. Accepted DP58, explicit_sharp_jets_linear_levels_DP58.md, ES6–12: the critical-exponential coefficient theorem. These statements were read at their full interfaces; no new display proof is claimed.
- AM-K018 K19.2/K19.13: exact source/Chern gauge on the ordinary product. K030 PH17–26 and K032 QH13–21: actual product principal lattices, full CM coordinates and integral11 comparisons. K031 HC22–26 and K032 QH33–36: the actual central alpha and permitted half-orbit.
- AM-K022 J6–16/J30: ordinary jet surjectivity and equality of the permitted image ideals. AM-K024 SC9–19: filler and exact Cauchy-label argument. AM-K026 HC18–25 and parent R011: target hook comparison and Fischer normalization. AM-K027 EX2–7: accepted common-weight transfer to arbitrary joint integral local prefactors.
- Formalism/LocalToGlobal/Columns/AbelianHostFieldConditions.lean:442–469, Wts.Ok and selected weight definitions; Columns/BaseLemmas.lean:496–552, selected recurrence; LocalRingCardinality/DataTheta.lean:529–555 and SharpRestriction/CuspSpanNormBounds/CayleySignature.lean:110–118, exact Hyp3 clauses. Paths are relative to work/research/alpoge_source. The old unmodified Fields.Kq condition is not changed.

The finite certificate selected_cm_frobenius_sharp_content_certificate.py and its JSON output verify the actual seven-copy Frobenius permutation and all49 trace-pair entries over the cyclotomic residue algebra, the plus/minus pairing, both weighted quadratic pairings, the standard-lattice unit factors, the explicit support pairs, and exact Legendre and baseline arithmetic. They do not infer an infinite coefficient theorem or a selected automorphic image from finite samples. Those assertions, where made, are proved by the cited accepted whole-series theorems and the arguments above. No Lean execution is claimed.
