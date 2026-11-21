# DP53: prime redistribution for the actual cyclotomic Jacobian preserves the leading bare-jet budget

Date: **2026-11-21 UTC**. Author: `/root/formal_bound`, **GPT-6 Astra Pro**; runtime reasoning effort **not exposed**. The parent reserved DP53. This memo proves the full residue-class spectrum, its prime-sum consequence, and an integer periodic-floor comparison for arbitrary derivative orders fixed across the prime sum. All rates are for **bare integral invariant derivatives**, not normalized theta kernels or selected theta determinants.

## 1. Precise results

Let `J=Jac(y²=x⁷−1)` with the good integral model of DP22, and let

\[
E=\mathbf Q(\zeta_7),\qquad
\Phi=\{1,2,3\},\qquad \Psi=\{1,2,4\}
\subset(\mathbf Z/7)^\times.
\tag{PR1}
\]

The first is the actual covariant Jacobian CM type; the second is the type induced from `Q(√−7)` used for the comparison. Only odd primes `p≠7` occur below. Put

\[
c_2(p)=\frac{p}{p^2-1},\qquad
c_3(p)=\frac1{p-1}-\frac1{p^3-1},
\qquad D(p)=(p-1)(p^3+1).
\tag{PR2}
\]

The three **sharp bare directional slopes** of the actual Jacobian, labelled by the global differential characters `i=1,2,3`, are:

| `p mod 7` | `c_1^Φ(p)` | `c_2^Φ(p)` | `c_3^Φ(p)` | Total `B_Φ(p)` |
|---|---:|---:|---:|---:|
| 1 | 0 | 0 | 0 | 0 |
| 2 | `p/(p³−1)` | `p²/(p³−1)` | `c_3(p)` | `2c_3(p)` |
| 4 | `p²/(p³−1)` | `p/(p³−1)` | `c_3(p)` | `2c_3(p)` |
| 3 | `p/D(p)` | `p³/D(p)` | `p²/D(p)` | `T(p)` |
| 5 | `p³/D(p)` | `p/D(p)` | `p²/D(p)` | `T(p)` |
| 6 | `c_2(p)` | `c_2(p)` | `c_2(p)` | `3c_2(p)` |

Here

\[
T(p)=\frac{p(p^2+p+1)}{(p-1)(p^3+1)}.
\tag{PR3}
\]

The superscripts on the directional column labels avoid confusion with the height-indexed functions in (PR2); every actual direction has the uniform formula (PR6) below. For the induced type `Ψ`, every selected direction has slope

\[
c^{\Psi}(p)=
\begin{cases}
0,&p\equiv1,2,4\pmod7,\\
c_2(p),&p\equiv3,5,6\pmod7.
\end{cases}
\tag{PR4}
\]

Fix arbitrary nonnegative integers `n_1,n_2,n_3`, **constant across the primes being summed**, and put `N=n_1+n_2+n_3`. Then, uniformly in these orders and the prime cutoff `X≥2`,

\[
\sum_{\substack{p\le X\\p\ne2,7}}\log p\,
\sum_{i=1}^3n_i c_i^\Phi(p)
=\frac N2\log X+O(N),
\]

\[
\sum_{\substack{p\le X\\p\ne2,7}}\log p\,
\sum_{i=1}^3n_i c^{\Psi}(p)
=\frac N2\log X+O(N).
\tag{PR5}
\]

Their difference is therefore `O(N)`. The implied constants are independent of the `n_i` and `X`; the good model and modulus seven are fixed. In particular equal orders `n_i=n` give the same leading coefficient `(3/2)n log X` for both types. The same `O(N)` comparison holds for the **integer periodic-floor lower certificates** from DP43, as proved in §5. These statements do not bound the actual selected theta gain from above.

## 2. Actual integral CM directions at every residue class

The two-chart good model, its genus-three Jacobian abelian scheme, and its integral cyclotomic action are the checked geometric inputs of DP22. Its relative differential basis is

`ω_i=x^(i−1)dx/y`, `i=1,2,3`.

These differentials are defined over `Z[1/14]`. On every good fibre they form a basis of the three-dimensional differential space, so they form a primitive integral relative basis. Their dual basis of the Lie lattice, and hence the normalized invariant directions `D_i`, is defined over the same base. This supplies global labels independent of the prime; no prime-dependent change of direction is being made.

The covariant automorphism `a[P−∞]=[(ζ_7 x(P),y(P))−∞]` has cotangent and tangent characters `i=1,2,3`. The ordinary transpose of the scalar eigenvalue retains that eigenvalue. After the unramified extension containing `ζ_7`, each integral character eigenspace is a rank-one direct summand, because seven is a unit and the seventh roots have distinct residues. The Teichmüller tangent generator from the local display and the generator dual to `ω_i` therefore differ by an integral unit. Directional valuations and sharp slopes are unchanged by this comparison.

At a good prime, write `f=ord_7(p)`. The integral cyclotomic order splits into the Frobenius orbits under multiplication by `p` on `(Z/7)^×`. The standard CM height/type theorem gives height `f` for an orbit and dimension equal to its number of members of `Φ`: Tate, local CM formula (10*) and Theorem 3 in §5, printed pp.106–108, at the exact source already checked for DP22. This is a cited known CM theorem, not a new classification claim.

For an orbit containing a selected embedding, its factor is connected. Indeed it has a unital action of the unramified field of degree `f` up to isogeny. A nonzero étale quotient would have rational Tate dimension a positive multiple of `f`, hence full height `f`; the factor would then be étale of dimension zero, contradicting the positive selected count. If the count is strictly between zero and `f`, the same argument applies to its dual. Integral idempotents and the connected-formal equivalence identify these with actual formal direct factors of the completed Jacobian, not merely isogeny factors.

For every partially selected orbit, the argument of DP45 and DP49 now constructs the actual integral unit-arrow display. Over the `p`-nilpotent quotients of the unramified base, Zink's display has rank `f`. The cyclotomic Witt idempotents split it into free eigenspaces; semilinear Frobenius cyclically permutes them and its linearization is invertible after inverting `p`, so their ranks are all one. The exact Hodge quotient forces `Q_i=I P_i` on the selected characters and `Q_i=P_i` on the others. The normal-decomposition map is a monomial invertible matrix, so all its arrows are units. Compatible generators lift through the Witt reductions and give the integral model over the unramified base. These are exactly DP40's hypotheses.

The only selected full orbits for the actual type `Φ` occur when `p≡1`, and then `f=1`. They are one-dimensional height-one formal groups. Their sharp slope is zero. A short distribution check makes the exactness explicit. Kill the logarithm terms of degrees 2 through `p−1` by an integral strict coordinate. If `b_p` is its degree-`p` logarithm coefficient, height one gives `p b_p` a unit: the degree-`p` coefficient of `[p]` is `(p−p^p)b_p`. The integral translation operator at degree `p` gives

`D^p/p!+b_p D` integral.

Thus modulo `p`, `D^p` is a unit multiple of `D`. Iterating gives a unit value on a normalized coordinate at every order `p^r`. All derivatives were already integral, so the sharp slope is exactly zero. This uses the already established distribution identity, not a rational-slope surrogate.

The induced comparison type `Ψ` is constant on the Frobenius orbits when `p∈{1,2,4}` and alternating when `p∈{3,5,6}`. Its former formal factors are ordinary of multiplicative type and have zero bare slope. Equivalently, after a faithfully unramified strictly Henselian extension their étale Cartier duals become constant and the formal factors become formal multiplicative groups; the restricted operation is invertible and the CM eigendirections have unit `p^f`-power, giving zero sharp slopes. Its alternating factors have selected gaps two, so DP40 gives `c_2(p)` in every selected direction. This proves (PR4) for the integral induced-type model. No assertion that the actual type `Φ` changes into `Ψ` is made.

## 3. Direction formulas and the full residue table

Let `a=p mod 7` and let `i∈Φ`. DP40/DP43 give

\[
\boxed{
c_i^\Phi(p)=\sum_{r\ge1}
\mathbf1_{a^r i\notin\Phi}\,p^{-r}
=\frac{\sum_{r=1}^{f}
\mathbf1_{a^r i\notin\Phi}\,p^{f-r}}{p^f-1}.}
\tag{PR6}
\]

For a constant selected orbit this is zero, consistent with the ordinary case. For every partially selected orbit these are the sharp slopes in the actual primitive integral eigenbasis, including the exact `p^(fm)` witness sequence of DP40.

For `a=2`, the two cycles are `(1,2,4)` and `(3,6,5)`; for `a=4` they are their inverses. Substituting the three labels into (PR6) gives the two rows displayed above. For `a=3`, the order `(1,3,2,6,4,5)` has three consecutive selected positions; for `a=5`, use `(2,3,1,5,4,6)`. DP45's ordered triple is `(p,p²,p³)/D(p)`, which in the fixed global label order gives respectively `(p,p³,p²)/D(p)` and `(p³,p,p²)/D(p)`. For `a=6`, the three two-cycles are `(1,6),(2,5),(3,4)`, with one selected member each. The class `a=1` is ordinary. This proves every entry of the table, including its label consistency.

As a useful exact algebraic check, evaluate the six residue formulas at a common variable `p>1`. Their formal averages satisfy

\[
\frac{4c_3(p)+2T(p)+3c_2(p)}6
-\frac{9c_2(p)}6
=\boxed{\frac{4p^2(p^2+1)}{3(p^6-1)}}.
\tag{PR7}
\]

Indeed, over denominator `p^6−1`, the numerators of `c_3,T,c_2` are respectively

`p(p+1)(p³+1)`, `p(p²+p+1)²`, `p(p⁴+p²+1)`.

The numerator of `4c_3+2T−6c_2` is `8p²(p²+1)`, proving (PR7). This is a formal common-variable identity. It does not identify the sign of the actual weighted prime-sum constant; the residue-class prime distributions still matter.

## 4. The unconditional prime-sum comparison with arbitrary fixed orders

Put

\[
\alpha_i(a)=\mathbf1_{a i\notin\Phi},\qquad
\alpha^{\Psi}(a)=\mathbf1_{a\in\{3,5,6\}}.
\tag{PR8}
\]

Formula (PR6) gives the uniform error bound

\[
0\le c_i^\Phi(p)-\frac{\alpha_i(a)}p
\le\sum_{r\ge2}p^{-r}=\frac1{p(p-1)}.
\tag{PR9}
\]

The same bound applies to the induced type. For each fixed `i∈Φ`, multiplication by `i` permutes the six nonzero residues. Exactly three send it into `Φ^c`. Therefore

\[
\sum_{a=1}^{6}\alpha_i(a)=3,
\qquad \sum_{a=1}^{6}\alpha^{\Psi}(a)=3.
\tag{PR10}
\]

Use the established unconditional fixed-modulus estimate

\[
\sum_{\substack{p\le X\\p\equiv a\ (7)}}\frac{\log p}{p}
=\frac16\log X+O(1)
\qquad(a=1,\ldots,6).
\tag{PR11}
\]

An exact direct primary-author reference is Zeév Rudnick, *Primes in Arithmetic Progressions: Fixed Modulus*, May 26, 2015, §2, p.2, equation (1), on the author's official site:

`https://www.math.tau.ac.il/~rudnick/courses/sieves2015/fixed%20progressions.pdf`.

The paragraph immediately preceding (1) states the quantitative fixed-modulus prime number theorem with exponential-square-root-log error; no RH hypothesis is present. The exact page was independently read in this run by the archive agent, and this agent retrieved and read the official PDF text. The known prime number theorem is cited, not reproved here. The stronger constant-plus-`o(1)` version, if wanted, is justified by partial summation in `prime_sums_mod7_primary_source.md`; only (PR11) is needed below.

The error series from (PR9), weighted by `log p`, converges absolutely, by comparison with `Σ_(m≥2)log m/m²`. Equations (PR10)–(PR11) consequently give

\[
\sum_{\substack{p\le X\\p\ne2,7}}
c_i^\Phi(p)\log p=\frac12\log X+O(1),
\qquad
\sum_{\substack{p\le X\\p\ne2,7}}
c^{\Psi}(p)\log p=\frac12\log X+O(1).
\tag{PR12}
\]

Deleting the finitely many bad primes changes only the bounded term. There are three fixed labels, so the bounds can be made uniform in `i` and in all `X≥2`. Multiplying (PR12) by arbitrary `n_i≥0` and adding proves (PR5), with an error bounded by a constant times `N`. The orders can vary with an outer parameter; they only have to be held fixed as the prime in that sum varies.

For equal orders, the actual first-coefficient totals in classes `1,2,3,4,5,6` are

`(0,2,1,2,1,3)`,

whereas the old induced totals are

`(0,0,3,0,3,3)`.

Both have sum nine. Their difference `(0,2,−2,2,−2,0)` explains why an absolute same-prime estimate is insufficient, while the actual prime redistribution still changes only the bounded term of the coefficient sum.

## 5. The same comparison for the integer periodic-floor certificates

For `i∈Φ`, define the exact DP43 lower certificate

\[
E_{i,p}^{\Phi}(n)
=\sum_{r\ge1}\mathbf1_{a^r i\notin\Phi}
\left\lfloor\frac n{p^r}\right\rfloor.
\tag{PR13}
\]

This is finite. It is zero on a selected ordinary orbit. For the induced type define `E_p^Ψ(n)` by its analogous periodic membership pattern; it is zero in split classes and `Σ_(r odd) floor(n/p^r)` in inert classes. These are coefficientwise lower bounds in the integral distribution lattice, not asserted exact values at every order.

Then, uniformly in `X≥2` and arbitrary nonnegative `n_i`,

\[
\boxed{
\left|
\sum_{\substack{p\le X\\p\ne2,7}}\log p
\sum_{i=1}^{3}
\bigl(E_{i,p}^{\Phi}(n_i)-E_p^{\Psi}(n_i)\bigr)
\right|=O(N).}
\tag{PR14}
\]

To prove this, fix one `i` and write `n=n_i`. If `n≤1`, every floor is zero. Otherwise put `Y=min(X,n)` and `δ_i(a)=α_i(a)−α^Ψ(a)`. The first-power contribution is

\[
\begin{split}
\sum_{\substack{p\le Y\\p\ne2,7}}
\delta_i(a)\left\lfloor\frac np\right\rfloor\log p
={}&n\sum_{\substack{p\le Y\\p\ne2,7}}
\delta_i(a)\frac{\log p}{p}
+O\!\left(\sum_{p\le Y}\log p\right).
\end{split}
\tag{PR15}
\]

The first sum is bounded because `Σ_a δ_i(a)=0` and (PR11) applies. The last sum is `O(Y)=O(n)` by the same fixed-modulus prime number theorem, summed over its six classes, with the finitely many omitted primes restored. Thus (PR15) is `O(n)`.

For the higher powers, the absolute difference of the two membership indicators is at most one, so their entire contribution is at most

\[
n\sum_p\log p\sum_{r\ge2}p^{-r}
=n\sum_p\frac{\log p}{p(p-1)}=O(n).
\tag{PR16}
\]

The constant is independent of the cutoff. Summing over `i` proves (PR14). Thus the conclusion survives integer rounding and the whole periodic pattern; it is not only a comparison of leading real slopes.

## 6. General combinatorial reason and the exact arithmetic boundary

Let a finite group `Γ` act transitively on a set `Ω` of size `2g`, and let `A⊂Ω` have size `g`. For `σ∈Γ` set

\[
\alpha_A(\sigma)=\#\{i\in A:\sigma i\notin A\}.
\]

For fixed `i∈A`, each target in `Ω` has equally many preimages under the map `σ↦σi`. Exactly half the targets lie outside `A`. Consequently

\[
\boxed{\frac1{|\Gamma|}\sum_{\sigma\in\Gamma}
\alpha_A(\sigma)=\frac g2.}
\tag{PR17}
\]

More generally, fixed nonnegative weights `n_i` give average `(Σ_i n_i)/2`. The corresponding periodic directional expression

`Σ_(r≥1) 1_(σ^r i∉A) p^(−r)`

has first term `1_(σi∉A)/p` and a tail bounded by `1/[p(p−1)]`. This is the elementary structural reason for the calculation above.

The arithmetic application must still specify the Frobenius distribution. In the present abelian cyclotomic case, Frobenius is the actual residue element `a mod 7`, and (PR11) supplies precisely the required uniform distribution. For a general nonabelian Galois embedding action, `α_A` need not be a conjugacy-class function. Choosing a prime in a reflex or other base field can also change the sampling. Thus (PR17) is not asserted to be, by itself, a general prime-average theorem for every CM variety over every base field.

## 7. Consequence and remaining scope

This closes a concrete alternative to a same-prime comparison: the actual Jacobian type does move bare derivative divisibility into residue classes where the old induced type has none, but for arbitrary orders attached to its fixed global rational directions, the full prime-summed linear budget and the natural integer lower-certificate budget change by only `O(N)`. Their leading logarithmic coefficient is unchanged.

The result does not identify these bare derivatives with normalized theta-selected values. In particular it does not reverse the source's one-way `LinkG` lower certificate into an upper bound on actual gain, assert that selected orders may be freely permuted at each prime, or dismiss a finite `O(N)` improvement in a finite inequality. Genuine prime-dependent direction choices, special sections, selected harmonic row degrees, the new endpoint period, and all normalization/cost terms remain separate data. The arbitrary fixed `n_i` version already avoids assuming equal derivative orders merely for convenience.

Actual full saved-text readings and independent challenges of the proof and exact source locators are recorded separately with their hashes and observed times. No numerical experiment, Lean execution, machine formalization, or audit of the accepted global premise is claimed.
