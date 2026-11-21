# A higher-height scalar kernel: a failed intermediate estimate and two valid replacements

Date: 2026-11-21 (UTC). Author/checking agent: `/root/formal_bound`, inherited GPT-6 Astra Pro; reasoning-effort setting is not exposed. This is mathematical source reading and a written proof, not Lean compilation or a machine-checked formalization. It does not edit `DP_MULT.tex`.

## Decision

The scalar logarithm and its inverse do generalize from $p^2$ to $q=p^h$. The first specific obstruction in the recovered proof of `LemmaS` is its **weight quantization** step, not the existence or the coefficient estimate of the inverse logarithm. The direct higher-height version of `LemmaS` is false, even when all of the natural generalized scalar `BHyp` conditions actually hold. Statement HK2 below is the proposed **DP28**.

That failure does **not** refute a final estimate for factorial-weighted kernel coefficients. A direct argument proves the original one-letter residual coefficient $1/(p^2-1)$ at every $h\ge2$, under the generalized hypotheses. In addition, an explicit nonzero correction kernel realizes the larger formal-group derivative slope $c_h=1/(p-1)-1/(p^h-1)$, with exact nonvanishing coefficients. These are HK3 and HK4, reserved as **DP29**. The subsequent memo higher_height_kernel_classification.md proves the stronger universal scalar statement **HK5 / DP31** over $W(k)$ when $h>2$: the correction is an integral-unit gauge and the full slope $c_h$ holds. None of these results is an automorphic theta-lift construction or the full Cartier determinant/nonvanishing package.

The notation matters:

| Quantity | Meaning | Effect of increasing $h$ |
|---|---|---|
| $\rho_h=1/(p^h-1)$ | Radius weight controlling the inverse formal logarithm | Decreases |
| $c_h=1/(p-1)-\rho_h$ | Factorial-weighted derivative slope of an integral function on the height-$h$ group | Increases |
| $r_0=p/(p^2-1)$ | A sufficient weight for the general corrected scalar kernel proved in HK3 | Kept fixed |
| $1/(p-1)-r_0=\rho_2$ | Final residual slope in HK3 | Kept fixed |

Thus a smaller $\rho_h$ is an improvement for the intermediate inverse-logarithm radius, but it would be a weaker lower bound if simply substituted as the final positive residual coefficient. HK2 addresses the intermediate `LemmaS` estimate precisely.

## 1. The generalized scalar interface

Fix an odd prime $p$, an integer $h\ge2$, and put $q=p^h$. Define

\[
 L_h(T)=\sum_{e\ge0}\frac{T^{q^e}}{p^e},\qquad E_h=L_h^{-1}.
\]

Let $K\supset\mathbf Q_p$ be a valued extension containing a primitive $(q-1)$-st root of unity $\zeta$, with valuation $v(p)=1$, and let $R$ be its valuation ring. The natural scalar higher-height version used here has two variables $X,Y$, with torus action

\[
 (X,Y)\longmapsto(\zeta X,\zeta^{-p}Y).
\tag{H0}
\]

This keeps the two original characters $1,-p$, replaces the original root order $p^2-1$ by $q-1$, and replaces both scalar logarithms by $L_h$. This is an explicit proposed analytic interface. It is not asserted to be the same as an $h$-letter CM orbit or the original alternating geometric host.

For $\beta\in K[[X,Y]]$, impose:

1. Its coefficients lie in an unramified subfield $K_0\subset K$, meaning $v(K_0^\times)\subset\mathbf Z$.
2. $\beta(\zeta X,\zeta^{-p}Y)=\beta(X,Y)$.
3. All its nonzero monomials $X^aY^b$ have $a,b>0$, and the coefficient of $XY$ is zero.
4. With
   \[
   \delta_X\beta=\beta(X+X',Y)-\beta(X,Y)-\beta(X',Y),
   \]
   and the analogous $\delta_Y$, the series
   \[
   H_X=\exp\bigl(\delta_X\beta(L_h(S),L_h(S'),L_h(T))\bigr),
   \quad
   H_Y=\exp\bigl(\delta_Y\beta(L_h(S),L_h(T),L_h(T'))\bigr)
   \tag{H1}
   \]
   belong to the respective integral power-series rings and have constant coefficient $1$.

These are exactly the five scalar ingredients of the source `BHyp`, with the declared modifications. For $h=2$, there are two letters, and its shift by $-2e$ on `ZMod 2` is the identity, so (H1) agrees with the original scalar specialization. The additional unused primed variable in the source's four-variable presentation changes no condition.

## 2. HK1: the Honda logarithm, inverse radius, and exact coefficients

**Statement.** The formal group

\[
 F_h(S,T)=E_h(L_h(S)+L_h(T))
\]

belongs to $\mathbf Z_p[[S,T]]$, and its special fibre has height $h$. If $\pi^{q-1}=p$, then

\[
 E_{h,\pi}(Z)=\pi^{-1}E_h(\pi Z)
\]

is integral. Its reduction is

\[
 \overline E_{h,\pi}(Z)=\sum_{r\ge0}(-1)^r Z^{q^r}.
\tag{1}
\]

Consequently

\[
 v([T^n]E_h)\ge-\frac{n-1}{q-1},
\qquad
 v([T^{q^r}]E_h)=-\frac{q^r-1}{q-1}.
\tag{2}
\]

**Integral formal-group proof.** We first establish a congruence. If $A,B\in (Z_1,\ldots,Z_m)\mathbf Z_p[[Z_1,\ldots,Z_m]]$ and $A\equiv B\pmod p$, then

\[
 A^{p^r}-B^{p^r}\in p^{r+1}\mathbf Z_p[[Z_1,\ldots,Z_m]].
\]

Indeed, write $A=B+pC$. In the binomial expansion, the term indexed by $1\le i\le p^r$ has valuation at least $r-v_p(i)+i\ge r+1$, using

\[
 \binom{p^r}{i}=\frac{p^r}{i}\binom{p^r-1}{i-1}.
\]

Therefore $L_h(A)-L_h(B)\in p\mathbf Z_p[[\mathbf Z]]$: its $e$-th summand is divisible by $p^{he+1-e}$, and only finitely many summands contribute to any fixed total degree.

Construct $F_h$ degree by degree. Suppose its truncation (G) below degree $N\ge2$ is integral. Put

\[
 H=L_h(G)-L_h(S)-L_h(T).
\]

It has order at least $N$, because (G) agrees with the characteristic-zero formal group through lower degrees. The identity $L_h(U)=U+p^{-1}L_h(U^q)$ gives

\[
 H=G-S-T+\frac{L_h(G^q)-L_h(G(S^q,T^q))}{p}
       +\frac{H(S^q,T^q)}p.
\]

Here $G^q\equiv G(S^q,T^q)\pmod p$, since coefficients in $\mathbf Z_p/p$ are fixed by $q$-th power. The first fraction is integral by the preceding congruence. The last term has order at least $qN>N$. Thus the degree-$N$ homogeneous part of $H$ is integral. Since the logarithm has linear coefficient $1$, the required degree-$N$ correction to (G) is exactly the negative of that homogeneous part. This completes the induction. Associativity and commutativity hold over $\mathbf Q_p$ by construction and therefore hold integrally.

The first nonlinear term of multiplication by $p$ is

\[
 [p]_{F_h}(T)=pT+(1-p^{q-1})T^q+O(T^{q+1});
\]

there are no terms of degrees $2,\ldots,q-1$. Its reduction has initial degree $q=p^h$, proving the height assertion.

**Inverse-radius proof.** The scaled logarithm is

\[
 \pi^{-1}L_h(\pi Z)
 =\sum_{e\ge0}p^{(q^e-1)/(q-1)-e}Z^{q^e}.
\]

All exponents of $p$ are nonnegative. For $e=0,1$ they are zero, and for $e\ge2$ they are positive. This is an integral series with linear coefficient $1$, so its formal inverse $E_{h,\pi}$ is integral. Modulo the maximal ideal, the logarithm is $Z+Z^q$. Its inverse is $1$, since the $q$-th power is Frobenius in the residue field and the successive terms cancel. In particular all its $q^r$-coefficients are nonzero. Rescaling gives $2$.

Also, if $\eta^{q-1}=1$, then $L_h(\eta T)=\eta L_h(T)$, hence $E_h(\eta T)=\eta E_h(T)$. This will verify the torus action below.

## 3. HK2 / proposed DP28: generalized `LemmaS` is false

**Statement.** For every odd $p$ and $h\ge3$, there is a series satisfying every condition in §1 for which

\[
 v(\beta_{a,b})+\rho_h(a+b)\ge\frac1{p-1}-1
\tag{3}
\]

fails. This is the first conclusion of the direct $q$-logarithm version of source `LemmaS`.

**Construction and verification of every axiom.** Take $K_0=\mathbf Q_p$, take $K$ to contain the unramified degree-$h$ extension and its Teichmüller roots, and define

\[
 I(S,T)=1+S^pT,
 \qquad
 \beta(X,Y)=\log I(E_h(X),E_h(Y)).
\tag{4}
\]

The series has coefficients in $\mathbf Q_p$, giving the unramified coefficient condition. Every monomial has positive $X$- and $Y$-degrees and its order is at least (p+1), so the axis and $XY$ exclusions hold. By the equivariance in HK1,

\[
 I(E_h(\zeta X),E_h(\zeta^{-p}Y))
 =1+\zeta^p E_h(X)^p\zeta^{-p}E_h(Y)
 =I(E_h(X),E_h(Y)),
\]

which proves exact torus invariance.

For the first coboundary, formal exponential and logarithm identities give

\[
 H_X(S,S',T)=
 \frac{I(F_h(S,S'),T)}{I(S,T)I(S',T)}.
\tag{5}
\]

The numerator is integral by HK1. Each denominator has constant coefficient $1$ and is invertible in the integral power-series ring. Thus $H_X$ is integral with constant coefficient $1$. Similarly

\[
 H_Y(S,T,T')=
 \frac{I(S,F_h(T,T'))}{I(S,T)I(S,T')}
\tag{6}
\]

is an integral unit with constant coefficient $1$. These verify both coboundary hypotheses without invoking a hypothetical theta realization.

Set $k=p^{h-1}<q$. Expanding $4$,

\[
 \beta=\sum_{m\ge1}\frac{(-1)^{m-1}}m E_h(X)^{pm}E_h(Y)^m.
\]

Because $E_h(Y)=Y+O(Y^q)$, a coefficient of $Y^k$, with $k<q$, can occur only for $m=k$, and then its coefficient is $1$. The leading term of $E_h(X)^{pk}=E_h(X)^q$ is $X^q$. Hence the exact witness is

\[
 \boxed{\ \beta_{q,p^{h-1}}
     =\frac{(-1)^{p^{h-1}-1}}{p^{h-1}}\ },
\qquad v(\beta_{q,p^{h-1}})=-(h-1).
\tag{7}
\]

For odd $p$ the displayed sign is positive; the analogous coefficient is negative at $p=2$. The valuation calculation is independent of that sign.

The left side of $3$ at $7$ is

\[
 -(h-1)+\frac{p^h+p^{h-1}}{p^h-1}
 =2-h+\frac{p^{h-1}+1}{p^h-1}.
\]

For $h>2$,

\[
 \frac{p^{h-1}+1}{p^h-1}<\frac1{p-1},
\]

because multiplying by the positive denominators reduces this to $p<p^{h-1}$. Since $2-h\le-1$, $3$ is strictly violated. This completes the counterexample.

### Where the source proof first requires height two

`GenLogInverse` and `generalized_log_weight` require only a logarithm tangent to the identity and the inequality

\[
 \frac{q^e-1}{q-1}\ge e;
\]

they admit the same degree-induction proof for $q=p^h$. Integral substitution and factorial estimates also persist.

The recovered `lemmaS_of` calls `asmS_diff`, which first bounds $\exp(\delta\beta)-1$ with weight $\rho_2$, then calls `weightQuantization` to raise its positive weight to $s=1/(p-1)$. Its proof uses torus invariance to get total degree divisible by (p+1), integral coefficient valuations, and the exact identity

\[
 (p+1)\rho_2=s.
\tag{8}
\]

That is the first genuinely height-two numerical upgrade in this dependency path. A direct counterexample to the generalized quantization implication alone is coefficient $1$ at the invariant monomial $X^pY$. Its weight ((p+1)/(q-1)) is at least $\rho_h$, but is strictly less than $s$ for $h>2$. HK2 proves that the subsequent failure is realized by a full generalized kernel, not merely an isolated weight vector.

For completeness, the scalar quantization that actually follows from the same data is only

\[
 w\ge\rho_h>0\quad\Longrightarrow\quad
 w\ge\frac{\gcd(p+1,q-1)}{q-1}.
\tag{9}
\]

Indeed $w=k+(a+b)/(q-1)$ with $k\in\mathbf Z$, and invariance says $a-pb\equiv0\pmod{q-1}$. Thus ((q-1)w) is an integer multiple of $\gcd(p+1,q-1)$, and positivity proves $9$. For odd $p$, this gcd is (p+1) when $h$ is even and $2$ when $h$ is odd. At $h=2$ the result is exactly $8$; in higher height it no longer reaches the exponential threshold $s$.

## 4. HK3: a valid higher-height one-letter estimate

**Statement.** Assume the scalar conditions in §1, with any $h\ge2$. In fact the unramified-coefficient condition is not needed for this statement. Let (J) be any finite index set, let $U\in R[[S_j:j\in J]]$, let $\ell_j(\mathbf t)$ be integral linear forms in $N$ variables, let $\epsilon\in R^\times$, and let $\sigma\in\{1,-1\}$. Define

\[
 \Theta(\mathbf t)
 =U\bigl(E_h(\ell_j(\mathbf t)):j\in J\bigr)
   \exp\left(\frac\sigma2\sum_{j\in J}
     \beta(\ell_j(\mathbf t),\epsilon\ell_j(\mathbf t))\right).
\tag{10}
\]

For every multiindex $\kappa$, with $n=|\kappa|$,

\[
 \boxed{\quad
 v\bigl(\kappa!\,[\mathbf t^\kappa]\Theta\bigr)
 \ge \rho_2 n-\frac1{p-1}\sum_{i=1}^N s_p(\kappa_i).
 \quad}
\tag{11}
\]

For $n\ge1$, the right side is at least

\[
 \rho_2 n-N(\log_p n+1),
\tag{12}
\]

the final shape of the original `OneLetterR`. The estimate is valid for the modified height-$h$ scalar logarithm, rather than obtained by keeping the original $p^2$-logarithm.

**Proof.** For a series (A), write $w_r(A)=\inf_\nu(v(A_\nu)+r|\nu|)$. All arguments below can equally be read coefficient by coefficient; no analytic convergence assertion is used. Multiplication adds lower weight bounds, and substitution of series of weight at least $r$ for variables preserves them. HK1 implies $w_r(E_h)\ge r$ for every $r\ge\rho_h$, because $E_h$ has zero constant coefficient.

Torus invariance and the positive bidegrees force $\operatorname{ord}\beta\ge p+1$. In fact, for $a,b\ge1$ and $a+b\le p$, the integer (a-pb) is nonzero and has absolute value strictly less than $p^2-1\le q-1$. It cannot be a multiple of (q-1).

Put

\[
 s=\frac1{p-1},\qquad r_0=\frac p{p^2-1}.
\]

Then $r_0\ge\rho_h$ and $(p+1)r_0=s+1$. Both integral units $H_X,H_Y$ of (H1) satisfy $\operatorname{ord}(H-1)\ge p+1$. After substituting $E_h$ in each variable, their differences from $1$ have weight at least (s+1). For such a series $Z$,

\[
 w_{r_0}(Z^m/m)\ge m(s+1)-v_p(m)\ge s+1
\]

for $m\ge1$; for instance $v_p(m)\le m-1$ proves the last inequality. Formal logarithms therefore show

\[
 w_{r_0}(\delta_X\beta)\ge s+1,
 \qquad w_{r_0}(\delta_Y\beta)\ge s+1.
\tag{13}
\]

Take a nonzero coefficient $\beta_{a,b}$. At least one of (a,b) is at least $2$. For every integer $a\ge2$ there is $0<i<a$ with $v_p\binom ai\le1$. To see this, if $a$ is not a power of $p$, its base-$p$ expansion provides an interior index $i=p^r$ whose binomial coefficient is nonzero modulo $p$. This follows directly by expanding $(1+T)^a=\prod_r(1+T^{p^r})^{a_r}$ modulo $p$. If $a=p^r$, choose $i=p^{r-1}$; then

\[
 \binom{p^r}{p^{r-1}}
 =p\binom{p^r-1}{p^{r-1}-1}
\]

has valuation exactly $1$, since the second binomial coefficient is a unit modulo $p$.

The coefficient of $X^i(X')^{a-i}Y^b$ in $\delta_X\beta$ is exactly $\binom ai\beta_{a,b}$. If instead $b\ge2$, use $\delta_Y\beta$. Equation $13$ therefore gives

\[
 w_{r_0}(\beta)\ge s.
\tag{14}
\]

Integral linear substitutions, multiplication by $\epsilon$, the finite sum, and multiplication by $\sigma/2$ preserve this lower bound; here $p$ is odd. Hence the exponent in $10$ has weight at least $s$. Its exponential has weight at least $0$, since $v_p(m!)\le ms$. The factor (U$E_h(\ell_j)$) also has weight at least $0$. Thus

\[
 v([\mathbf t^\kappa]\Theta)\ge-r_0n.
\]

Legendre's identity gives

\[
 v_p(\kappa!)=\sum_i\frac{\kappa_i-s_p(\kappa_i)}{p-1}.
\]

Since $s-r_0=1/(p^2-1)=\rho_2$, this proves $11$. The ordinary digit bound $s_p(m)\le(p-1)(\log_p n+1)$ for $1\le m\le n$ proves $12$; zero coordinates contribute zero. At $\kappa=0$, $11$ just says (U(0)) is integral, already assumed.

This is a sufficient estimate. No optimality of $\rho_2$ for the entire generalized class is asserted.

## 5. HK4: a nonzero correction kernel with exact larger-slope nonvanishing

Use the actual $\beta$ of HK2 and choose $\epsilon\in R^\times$. With $U(S)=S$, one variable, and positive sign, $10$ becomes

\[
 \Theta_h(t)=E_h(t)
     \left(1+E_h(t)^p E_h(\epsilon t)\right)^{1/2}.
\tag{15}
\]

This has a nonzero correction exponent $\frac12\beta(t,\epsilon t)$. For odd $p$, all binomial coefficients $\binom{1/2}{m}$ belong to $\mathbf Z_p$: one may approximate $1/2\in\mathbf Z_p$ by ordinary nonnegative integers and use continuity of each binomial polynomial. Therefore $15$ is an integral function of the two formal-group coordinates $E_h(t),E_h(\epsilon t)$.

For $n=q^r$, it satisfies the exact equality

\[
 \boxed{\quad
 v\bigl(n!\,[t^n]\Theta_h\bigr)
 =v_p(n!)-\frac{n-1}{q-1}
 =c_h(n-1).
 \quad}
\tag{16}
\]

Indeed, scale by $\pi^{q-1}=p$. Then

\[
 \pi^{-1}\Theta_h(\pi z)
 =E_{h,\pi}(z)
   \left(1+\pi^{p+1}E_{h,\pi}(z)^p
                    E_{h,\pi}(\epsilon z)\right)^{1/2}
 \equiv E_{h,\pi}(z)\pmod\pi.
\]

By $1$, its coefficient at $z^{q^r}$ is a unit. Rescaling gives the first equality in $16$. The second follows from $s_p(q^r)=1$.

This is a constructive scalar nonvanishing result, in addition to the universal lower estimate. It explicitly shows that the failure of the intermediate `LemmaS` estimate is compatible with the full height-$h$ derivative slope. The correction here is an **integral-unit gauge** after logarithmic substitution: $\exp\beta(L_h(S),L_h(T))=I(S,T)$. It does not establish the prescribed Cartier minors, polarizations, CM signatures, trace/nonvanishing conditions, or a theta-lift comparison in the global construction.

## 6. Precise recovered-source locations

All paths below are relative to `research/external_lean/`. The public pinned mirror prefix is

`https://raw.githubusercontent.com/CocoSgt/riemann-hypothesis-lean/7cbf7a0c32fca1badf05931879a37c3f8a2b03b4/src/`.

The parent has independently matched earlier targeted modules byte for byte against the author's 14-part archive. The additional modules for this memo were fetched on 2026-11-21 and recorded in `external_lean/higher_kernel_metadata_1.json` and `_2.json`; their separate author-archive verification should be read from the parent's latest manifest, not assumed merely from the pinned mirror.

| File and declaration | Locator | Role |
|---|---|---|
| `Formalism/GaussJetBounds/Statement.lean`, `lw`, `torus`, `NoLowBidegree`, `letterLog`, `BHyp` | lines 39–94 | Original torus characters, exclusions, logarithm, and coboundary conditions |
| same, `LemmaS` | lines 98–105 | The intermediate conclusion refuted by HK2 after the declared changes |
| same, `oneLog`, `OneLetterR` | lines 175–197 | Exact scalar $p^2$-logarithm and final one-letter coefficient functional |
| `Formalism/GaussJetBounds/GenLogInverse.lean`, `GenLogWeight`, `GenLogInverse`, `Quant`, `BinomExtract` | lines 24–44 and 104–125 | Separates inverse calculus, quantization, and binomial extraction |
| `Formalism/GaussJetBounds/GaussJetProofs/LogarithmWeightComparison.lean`, `generalized_log_inverse` | line 227 onward | Inverse existence from tangent identity; the power $p^2$ is replaceable here |
| same, `generalized_log_weight` | line 252 onward | Coefficient induction with the geometric-series radius inequality |
| `Formalism/GaussJetBounds/GaussJetProofs/OneLetterRadiusIdentity.lean`, `weightQuantization` | lines 48–99; identity at lines 73–76 | First specific height-two numerical upgrade; uses $(p+1)\rho_2=s$ |
| `Formalism/GaussJetBounds/GaussJetProofs/ConstantCoeffEvenDerivativeEqZero.lean`, `asmS_diff`, `lemmaS_of` | lines 98–163 and 165–180 | Calls quantization before the logarithm step, then binomial extraction |
| `Formalism/GaussJetBounds/GaussJetProofs/LogStep.lean`, `logarithm_weight_induction` | line 36 onward | Exponential-to-log estimate at threshold $s$ |
| `Formalism/GaussJetBounds/GaussJetProofs/SwappedParitySeriesBinomialForm.lean`, `bnx_choose_nonpow`, `bnx_choose_pow` | lines 445–483 | Source version of the elementary binomial extraction |
| `Formalism/GaussJetBounds/OneLetterRadius.lean`, `lemmaS`, `oneLetterR` | lines 17–25 | Actual assembly of the recovered theorems, not merely definitions |
| `Formalism/GaussJetBounds/GaussJetProofs/AsmOne.lean`, `oneLetterR_of` | line 86 onward | Scalar assembly; uses $s-\mathrm{gam}(p)=\rho_2$ at lines 115–118 |

## 7. Check record and limitations

- **HK-C1, 2026-11-21 00:47:23 UTC observed clock.** Read the complete source definitions of `BHyp`, `LemmaS`, and `OneLetterR`; read the logarithm induction and the relevant source dependency declarations. Checked that the counterexample changes the root order and both scalar logarithms explicitly, and does not claim the original theorem is false.
- **HK-C2, 2026-11-21 00:50:09 UTC observed clock.** Read `weightQuantization`, `asmS_diff`, `lemmaS_of`, the scalar assembly, and the inverse-logarithm construction. Identified the actual identity $8$ and the coefficient-level failure of its higher-height version.
- The elementary proofs above were developed and checked by the same agent. Independent parent review is requested for HK2–HK4; it should not be counted as completed until the parent actually records it.
- No Lean files were changed, compiled, or executed. No finite coefficient calculation was represented as a proof. The displayed exact coefficients follow from formal degree arguments and reduction modulo $\pi$.
- **HK-C3, 2026-11-21 01:02:29 UTC observed clock.** Challenged the complete HK1–HK4 arguments: checked the congruence behind Honda integrality, the exact witness and its sign, the invariant minimum degree, both binomial cases, substitution and exponential thresholds, and the scaled nonvanishing coefficient. No mathematical defect found. This was a self-review by the same inherited GPT-6 Astra Pro agent, not an independent model or formal check.
- The classification route has now been completed separately in higher_height_kernel_classification.md. It supplies the integral trivializations and torus normalization; it does not infer them from slope vanishing alone. The present elementary proofs HK1–HK4 do not depend on that result.
- A complete hash table for the nine source files cited above is saved in higher_height_kernel_sources.tsv.

