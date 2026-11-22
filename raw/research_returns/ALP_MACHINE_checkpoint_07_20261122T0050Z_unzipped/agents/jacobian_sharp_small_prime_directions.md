# AM-K020 — two sharp pure directions of the actual trace-one theta section

Author: /root/kummer_extension, GPT-6 Astra Pro, ALP_MACHINE, 21 November 2026 UTC. The full actual source gauge was identified in AM-K018. The supplied DP41 bounded-multiplier lemma and DP45/53 bare cyclic-display bounds are used as accepted theorems. The new result concerns the single fixed actual section, not an arbitrary integral test function.

## 1. Statement

Let $J=\operatorname{Jac}(y^2=x^7-1)$, and use the global invariant differential basis $\omega_i=x^{i-1}dx/y$ and its logarithmic coordinates $u_i$. Let $\sigma_q$ be the actual reduced theta germ of the trace-one principal line $L_{2\infty}$, normalized by
\[
\sigma_q(u)=u_1u_3-u_2^2+\text{higher terms}.
\]
Its complete algebraic normalization, actual Chern/source gauge, and integral content are AM-K014, AM-K018, and ALP-LIFT-08. Write $v_p(p)=1$, with $v_p(0)=+\infty$.

The following are exact sharp directional statements:
\[
\boxed{\begin{aligned}
v_3\!\left(\partial_1^n\sigma_q(0)\right)
 &\ge \max\left\{0,\frac n{56}-\frac{s_3(n)}2\right\},
&
\liminf_{n\to\infty}
\frac{v_3(\partial_1^n\sigma_q(0))}{n}
 &=\frac1{56},\\[2mm]
v_5\!\left(\partial_2^n\sigma_q(0)\right)
 &\ge \max\left\{0,\frac n{504}-\frac{s_5(n)}4\right\},
&
\liminf_{n\to\infty}
\frac{v_5(\partial_2^n\sigma_q(0))}{n}
 &=\frac1{504}.
\end{aligned}}
\tag{K21.1}
\]
Here $s_p(n)$ is the base-$p$ digit sum. These are derivatives along two precisely specified global CM eigenlines, on $J$ itself. They require no conjugated factor and no comparison of mixed-action product gauges.

There are also explicit sharp witness sequences, not just a nonconstructive liminf. Put
\[
n_3(r)=28\cdot3^r+18,\qquad n_5(r)=126\cdot5^r+30.
\]
Then
\[
\boxed{\begin{aligned}
v_3(\partial_1^{n_3(r)}\sigma_q(0))
 &=\frac{3^r+3-s_3(n_3(r))}{2}\quad(r\ge0),\\
v_5(\partial_2^{n_5(r)}\sigma_q(0))
 &=\frac{5^r-1}{4}\quad(r\ge0).
\end{aligned}}
\tag{K21.1a}
\]
For $r\ge3$, the first expression is $(3^r-1)/2$. Its values for $r=0,1,2$ are $0,1,5$; the last has one extra unit of valuation from a base-three carry. Every derivative in (K21.1a) is nonzero.

The same sharp slopes hold for the translated, value-one theta $F$ in those directions. For $\sigma_q$ they persist under every permitted pullback with the source normalization $M^{-n}$, since its reduced pullback is $\sigma_q(Mu)$ and the two factors cancel exactly. In particular the previously used odd levels $M=29^e$ are prime to both 3 and 5.

The accepted DP45/53 bare integral-function slopes in these directions are respectively $3/56$ and $5/504$. Thus these actual normalized theta derivatives have slope equal to $1/p$ times that bare slope at these two primes. This comparison is an actual matching lower/asymptotic upper result for one fixed section; it is not a conclusion about the total cost of a later automorphic row.

## 2. An exact weighted-initial-form lemma

Let $p$ be odd, $q=p^h$, $s=1/(p-1)$, and
\[
H(t)=\sum_{n\ge2}\ell_n\frac{t^n}{n!}.
\]
Assume
\[
\ell_n=0\ (n\text{ odd}),\qquad
v(\ell_n)\ge \max\{0,\lfloor(n-2)/q\rfloor\},\qquad
v(\ell_{q+1})=0.
\tag{K21.2}
\]
Put
\[
c=\frac{s}{q+1},\qquad w_*=s-c,\qquad
I=[s-2c,s-c].
\tag{K21.3}
\]
For a rational $w\in I$, choose a finite ramified coefficient extension and $\gamma$ with $v(\gamma)=w$. Write $\delta=w_*-w\in[0,c]$ and
\[
\tau=s-(q+1)\delta\in[0,s].
\tag{K21.4}
\]
Then $H(\gamma T)$ has coefficient infimum exactly $\tau$, and its entire initial form, after division by an element of valuation $\tau$, is a nonzero scalar times $T^{q+1}$. In particular that initial form has nonzero formal derivative in characteristic $p$.

**Proof.** For even $n$, Legendre's formula gives
\[
v\!\left(\frac{\ell_n\gamma^n}{n!}\right)
=v(\ell_n)+s\,s_p(n)-(c+\delta)n.
\tag{K21.5}
\]
An even positive integer has $s_p(n)\ge2$. At $n=q+1$, the digit sum is exactly two, and the unit assumption makes (K21.5) equal
$2s-(c+\delta)(q+1)=\tau$.

If $2\le n<q+1$, the same expression is at least
$2s-(c+\delta)n$, exceeding $\tau$ by at least
$(c+\delta)(q+1-n)>0$.

If $n>q+1$ is even, put $k=\lfloor(n-2)/q\rfloor\ge1$. Then
$n\le(k+1)q+1$, so (K21.5) minus $\tau$ is at least
\[
k-(c+\delta)(n-q-1)
\ge k\{1-q(c+\delta)\}
\ge k\left(1-\frac{2qs}{q+1}\right)>0.
\tag{K21.6}
\]
The last inequality holds because $p\ge3$ implies $2s\le1$. These estimates also bound all coefficients below and show that the higher-degree excess grows at least linearly in $k$. Odd coefficients are zero. There is therefore one and only one initial monomial. Its degree is $q+1\equiv1\pmod p$, proving the derivative assertion. ∎

Let $\nu_w(G)=\inf_n(v([t^n]G)+wn)$. Suppose $V(t)\ne0$ is any formal series for which $V(\gamma T)$ is bounded for every rational $w\in I$, and integral for $w=w_*$. The accepted DP41 bounded-multiplier lemma applies to the full initial form just proved, not merely to the existence of a first pole. It gives
\[
\nu_w(Ve^H)=-\infty\quad(w<w_*),
\qquad
0\le\nu_w(Ve^H)<\infty\quad(w\ge w_*).
\tag{K21.7}
\]
For the first assertion take $w\in I$, $w<w_*$, so $0\le\tau<s$, and use the nonzero-derivative initial form. The multiplier is only required to be nonzero and bounded; a zero at the origin is allowed. Monotonicity of $\nu_w$ extends unboundedness to every smaller nonnegative weight. At $w=w_*$, all coefficients of $H(\gamma T)$ have valuation at least $s$, so its exponential and its inverse are integral, with constant term one. This gives the asserted boundedness and finite infimum; larger weights follow by monotonicity.

If $Ve^H=\sum a_nt^n$, (K21.7) implies
\[
v(a_n)\ge-w_*n,\qquad
\liminf_{n\to\infty}\frac{v(a_n)}n=-w_*.
\tag{K21.8}
\]
Indeed, a strictly larger liminf would make the coefficient infimum finite at some rational weight below $w_*$, a contradiction. Multiplication by $n!$ and $s_p(n)/n\to0$ give
\[
v(n!a_n)\ge cn-s\,s_p(n),\qquad
\liminf_{n\to\infty}\frac{v(n!a_n)}n=c.
\tag{K21.9}
\]
All assertions also hold with $H(2t)$ in place of $H(t)$, since $p$ is odd and multiplication of its $n$-th logarithmic derivative by $2^n$ changes no valuation or initial-form nonvanishing.

## 3. Apply the lemma to the actual translated theta

For the actual value-one $F$, AM-K012 proves
\[
\partial_i^2\log F=-W_{ii}(a+u)
\]
in the explicit integral, invariant-derivation-stable Abel-coordinate ring. AM-K013 proves the all-order operator bound
$D_i^mR\subset p^{\lfloor m/q\rfloor}R$ at the indicated nilpotence exponent, and hence exactly the logarithmic bounds (K21.2), except for its final unit condition. This is an iterated assertion on a stable integral ring, not an iteration of one coefficient congruence.

The exceptional constants were computed exactly in the primary algebraic theta recurrence of AM-K017:
\[
\begin{array}{c|c|c|c}
p&i&q&\ell_{q+1}\bmod p\\ \hline
3&1&27&2\\
5&2&125&1.
\end{array}
\tag{K21.10}
\]
The computations are in $\mathbb F_p[Z]/\Phi_7(Z)$, which is a field in both cases because $p$ has order six modulo seven. The residues shown are nonzero scalars, so the logarithmic derivatives are units. The actual trace-one section is not being substituted for $F$ in the definition of these logarithmic derivatives: $F(0)=1$, whereas $\sigma_q(0)=0$.

These exact values and their full algebraic ODE inputs are saved in:

    work/agents/jacobian_hessian_pcurvature_certificate.py
    work/agents/jacobian_hessian_pcurvature_certificate.json
    work/agents/jacobian_theta_direction_jets.py

The certificate regenerates the values using the branch divisor $(\zeta,\zeta^3,\zeta^5)$, the exact Kleinian Hessian, and division-free Hurwitz recurrences. Its recorded PASS is a finite arithmetic check. The all-order deduction here uses (K21.2) and the complete initial-form lemma above.

With $V=1$, (K21.9) proves the sharp slopes $1/56$ and $1/504$ for the two indicated restrictions of $F$.

## 4. Transfer to the actual vanishing source section

AM-K015 proved an equality of actual reduced germs
\[
\sigma_q(2u)=r(u)F(2u),
\tag{K21.11}
\]
where $r$ is a rational function on $J$ regular and integral on a formal neighborhood of zero at every odd prime other than 7. This comes from the canonical rigidified $[2]$-identification of the two theta lines and their actual integral sections; it is not an arbitrary integral formal prefactor. The equality is in the Chern gauge, so no additional quadratic exponential occurs. The value-one normalization of $F$ is a unit at 3 and 5 by ALP-LIFT-07, and the $q$-normalized source section is primitive there by ALP-LIFT-08.

Write $V_i(t)=r(te_i)$. Its restriction is nonzero in the two cases:
\[
\sigma_q(t,0,0)=\frac{t^4}{12}+O(t^{18}),\qquad
\sigma_q(0,t,0)=-t^2+O(t^{16}).
\tag{K21.12}
\]
These initial terms are exact coefficients of the actual section in AM-K014. Since $F(2te_i)$ is a formal unit, (K21.11) implies $V_i\ne0$. In fact $V_i(0)=0$ in both cases. No unit quotient is assumed.

The remaining hypothesis of (K21.7) is boundedness of this actual restricted prefactor. The accepted DP45/53 theorem gives, in these globally labelled integral eigendirections,
\[
c_i^{\mathrm{bare}}(p)=\frac{p}{(p-1)(p^3+1)}=pc,
\qquad q=p^3.
\tag{K21.13}
\]
For every integral formal germ $r$, its invariant Taylor coefficients therefore satisfy
\[
v([t^n]r(te_i))\ge-(s-pc)n.
\tag{K21.14}
\]
This is the accepted mixed bound with only direction $i$ retained, followed by the exact factorial formula; any zero coefficients only improve it. The global invariant basis differs from DP45's primitive display basis by diagonal units, as explicitly checked in DP53.

Every $w\in I$ satisfies
\[
w\ge s-2c>s-pc,
\tag{K21.15}
\]
because $p\ge3$. Thus $V_i(\gamma T)$ is integral and bounded throughout the whole initial-form interval. Its zero at the origin is harmless for DP41's nonzero bounded-multiplier lemma. Apply (K21.9) to
$V_i(t)\exp(H_i(2t))=\sigma_q(2te_i)$.
Finally $2^n$ is a unit, so its derivatives have exactly the same valuations as those of $\sigma_q(te_i)$. This proves the matching liminf and the displayed digit-loss lower bound in (K21.1). The extra lower bound zero follows from the actual odd-prime Hurwitz integrality of $\sigma_q$ in AM-K014.

## 5. Explicit sharp subsequences of the fixed source section

### 5.1. Exact finite Sato determinant, without partition enumeration

Two additional finite residues are
\[
\partial_1^{18}\sigma_q(0)\equiv1\pmod3,\qquad
\partial_2^{30}\sigma_q(0)\equiv4\pmod5.
\tag{K21.17}
\]
Here is a direct finite certificate and its truncation justification.
Use AM-K014's actual Sato frame
\[
v_j(t)=t^{\,2-n_j}A(t^{14})^{-\lfloor n_j/2\rfloor},
\quad A=1-TA^7,\quad(n_j)=(0,2,4,6,7,8,\ldots).
\]
Write $a_{m,j}=[t^m]v_j$. For a single KP time $t_d=v$, put
$h_{dn}=v^n/n!$ and $h_m=0$ when $m<0$ or $d\nmid m$. Then
\[
\tau(v)=
\det\left(\sum_m a_{m,j}h_{m+i}(v)\right)_{1\le i,j\le L}
\pmod{v^{N+1}}
\qquad(L\ge\max\{3,dN\}).
\tag{K21.18}
\]
To prove this, apply Cauchy–Binet, ordering the selected exponents
$m_1>\cdots>m_L\ge-L$. Set $\lambda_i=m_i+i$. These form a partition,
and the two determinants in each summand are respectively its stable
Plücker coefficient and
$\det(h_{\lambda_j-j+i})=s_\lambda$, by Jacobi–Trudi. Every term of
ordinary $v$-degree at most $N$ has $|\lambda|\le dN$, hence length at
most $L$. All its Plücker coefficients already stabilize at this $L$:
the added rows and columns have upper triangular identity tail, since
$v_j$ has leading exponent $-j$ for $j\ge4$ and only higher corrections.
Thus no omitted partition can contribute. The sum over $m$ is finite
at each truncation, which also justifies Cauchy–Binet formally.

The exact integer coefficients needed for the matrix are
\[
[T^k]A^{-m}
=\frac m k(-1)^{k-1}\binom{7k-m-1}{k-1}\quad(k\ge1),
\qquad [T^0]A^{-m}=1.
\tag{K21.19}
\]
The generalized integer binomial is used if the upper entry is negative.
Its displayed numerator is divisible by $k$, as also follows from the
integral implicit recursion for $A$.

The script

    work/agents/jacobian_sigma_hurwitz_determinant.py

evaluates (K21.18) in the truncated Hurwitz ring. Its multiplication is
$(ab)_n=\sum_{k=0}^n\binom nk a_kb_{n-k}$; it never inverts $n!$
modulo $p$. Complete unit pivoting leaves the actual two-dimensional
constant-rank defect and an exact $2\times2$ residual determinant.
Finally the factor $4\cdot2^{-n}$ converts the $n$-th derivative of
$\tau(v)=\sigma(v)$ into that of $\sigma_q(u)=4\sigma(u/2)$.

For the two computations, $(d,N)=(5,18)$ and $(3,30)$, so $L=90$
is sufficient. Each was executed again with $L=104$; the complete
retained derivative vectors agreed. The outputs are

    work/agents/jacobian_sigma_hurwitz_p3_order18.json
    work/agents/jacobian_sigma_hurwitz_p3_order18_tail14.json
    work/agents/jacobian_sigma_hurwitz_p5_order30.json
    work/agents/jacobian_sigma_hurwitz_p5_order30_tail14.json

The nonzero residues through those cutoffs are respectively
$S_4=2,S_{18}=1$ modulo 3, and
$S_2=3,S_{16}=4,S_{30}=4$ modulo 5. Separate low-order executions
reproduce $S_4=2$, $S_2=-2$, and $S_6=1$ in their corresponding
directions. These are exact finite computations, distinct from the
all-order argument that follows. The one-command replay is

    python work/agents/jacobian_sigma_sharp_certificate.py

It regenerates both matrix sizes, verifies the entire retained vectors,
and writes jacobian_sigma_sharp_certificate.json with script hashes,
exact critical weights, finite possible initial degrees, and witness
digit sums. Its recorded status is PASS.

### 5.2. The critical exponential coefficients

At $w=w_*$, the scaled logarithm $H(2\gamma T)$ has exactly one
coefficient of valuation $s$, in degree $n_0=q+1$; every other
coefficient has valuation strictly above $s$. Write
$E(T)=\exp(H(2\gamma T))$. Its constant term is one, and
\[
v([T^n]E)\ge s\quad(n>0),\qquad
v([T^n]E)=s
\ \Longleftrightarrow\ n=n_0p^r\ (r\ge0).
\tag{K21.20}
\]
For the equivalence, factor the exponential formally into the
exponentials of its separate logarithmic monomials. A nonzero
coefficient from a logarithmic coefficient of valuation $s+\epsilon$
has valuation at least $s\,s_p(m)+m\epsilon>s$. The unique critical
monomial contributes in degree $mn_0$ with valuation
$ms-v(m!)=s\,s_p(m)$, which equals $s$ exactly when $m=p^r$.
All other contributions at such a degree have larger valuation, so
there is no cancellation. Each coefficient involves only finitely
many factors, making this a formal argument rather than an analytic
product assertion.

### 5.3. The actual algebraic prefactor has a unique critical monomial

Set $\widetilde V(T)=r(\gamma T e_i)$ and
$G(T)=\sigma_q(2\gamma T e_i)=\widetilde V(T)E(T)$.
By (K21.14),
\[
v([T^j]\widetilde V)\ge\delta_0j,\qquad
\delta_0=(p-1)c>0.
\tag{K21.21}
\]
Thus its coefficient infimum $\nu$ is attained in finitely many
degrees. Since $E(0)=1$ and every positive coefficient of $E$ has
valuation at least $s>0$, Gauss multiplicativity and reduction show
that $G$ and $\widetilde V$ have the same infimum and the same entire
initial form. In particular their initial degrees must satisfy the
actual CM selection rule of $\sigma_q$.

For $p=3$, the exact unit $S_{18}$ gives
\[
\nu\le -v_3(18!)+18w_*=-8+\frac{27\cdot18}{56}
=\frac{19}{28}.
\]
Any initial degree of $\widetilde V$ is at most
$(19/28)/\delta_0=19$. The source CM rule leaves only degrees 4 and 18.
The value at 4 is $-1+4w_*=13/14>19/28$, so
\[
\nu=\frac{19}{28},\qquad
\operatorname{in}(\widetilde V)=aT^{18}\quad(a\ne0).
\tag{K21.22}
\]

For $p=5$, the exact unit $S_{30}$ gives
\[
\nu\le -v_5(30!)+30w_*=-7+\frac{125\cdot30}{504}
=\frac{37}{84}.
\]
Initial degrees are at most $(37/84)/\delta_0=111/2$, hence the
selection rule leaves only 2, 16, 30, and 44. The value at degree 2
is $2w_*=125/252>37/84$. Hurwitz integrality alone bounds the values
at 16 and 44 below by respectively
$s\,s_5(16)-16c=1-16/504$ and
$s\,s_5(44)-44c=2-44/504$, both larger than $37/84$. Therefore
\[
\nu=\frac{37}{84},\qquad
\operatorname{in}(\widetilde V)=aT^{30}\quad(a\ne0).
\tag{K21.23}
\]

### 5.4. Unique coefficient contributions give exact valuations

In either case put $m=18$ or 30, respectively, and
$n=n_0p^r+m$. The contribution
$[T^m]\widetilde V\,[T^{n_0p^r}]E$ has valuation exactly $\nu+s$.
Every other contribution with a positive $E$-degree has larger
valuation, by the uniqueness in (K21.22)–(K21.23) and (K21.20).
The sole constant-$E$ contribution is $[T^n]\widetilde V$; it also
has larger valuation because
\[
\delta_0(n_0+m)>\nu+s:
\qquad \frac{46}{28}>\frac{33}{28},\quad
\frac{156}{126}>\frac{29}{42}.
\tag{K21.24}
\]
Thus for every $r\ge0$,
\[
v([T^{n_0p^r+m}]G)=\nu+s.
\tag{K21.25}
\]
Undo the weight and the unit rescaling by 2, and multiply by $n!$.
Since $v(S_m)=0$ and $s_p(m)=2$ in both cases, the result is
\[
v(S_n)=cn+\nu+s-s\,s_p(n)
=\frac{p^r+3-s_p(n)}{p-1}.
\tag{K21.26}
\]
For $p=5$, adding $30=5+25$ to $126\cdot5^r$ causes no base-five
carry, so $s_5(n)=4$ for every $r\ge0$. For $p=3$, adding
$18=2\cdot3^2$ causes precisely one carry when $r=2$ and none for
$r=0,1$ or $r\ge3$. This proves every assertion of (K21.1a),
including the small-order exception. It also independently yields
the two liminf upper bounds in (K21.1).

## 6. Source scope, exact comparison, and the remaining general-prime condition

The resulting exact comparison is

| Prime and fixed global direction | Actual bare DP45/53 slope | Actual $\sigma_q$ sharp slope | Difference |
|---|---:|---:|---:|
| $p=3$, $\partial_1$ | $3/56$ | $1/56$ | $1/28$ |
| $p=5$, $\partial_2$ | $5/504$ | $1/504$ | $1/126$ |

The operators are already specified global CM directions; no prime-dependent relabelling occurs in either statement. Each pure monomial is killed by conjugate-pair contractions whenever it is placed alone in a positive CM-labelled polynomial block. That elementary harmonic observation does not assert membership in an unspecified full row with its other degree, invariance, and HC conditions. Nor does the construction identify these particular pure derivative sequences with a required later theta-lift image.

The same proof gives a precise generalization criterion. For $p\equiv3\pmod7$, take $i=1$; for $p\equiv5\pmod7$, take $i=2$. In either case $q=p^3$, the all-order logarithmic bound and the bare bound (K21.13) already hold for the actual Jacobian. If the single actual constant
\[
\partial_i^{p^3+1}\log F(0)
\tag{K21.16}
\]
is a $p$-adic unit, then the actual fixed source germ has the exact sharp slope
$1/((p-1)(p^3+1))$ in that direction. AM-K017 makes this a global Hessian restricted-power constant; it is independent of the chosen nonzero local theta frame. Its unit status for every prime in these two residue classes is not proved here. A unit claim cannot be inferred solely from the existence of a rank-one cyclic display without identifying the relevant universal-extension or primitive-kernel pairing.

Thus the new result is unconditional for the two explicitly certified primes 3 and 5, and gives a single checkable unit condition at every other prime in the two classes. It supplies actual directional upper sharpness without a conjugated-product gauge gap. It does not settle the full prime budget or the later selected-row cost.

## 7. Exact accepted-result locators and verification boundary

The accepted source archive is RETURN_DP_MULT_checkpoint_06_20261121T0420Z. The used statements are:

- research/DP41_integrated_fragment.tex, proof paragraph “Exponential obstruction, including arbitrary nonzero bounded multipliers,” lines 131–147. Its lemma allows a complete ramified coefficient DVR, a logarithm with coefficient infimum in $[0,1/(p-1))$, a nonzero-derivative entire initial form, and any nonzero bounded multiplier. Its proof and hypotheses were read to verify applicability; the accepted lemma is not rederived here.
- research/DP45_integrated_fragment.tex, the actual integral cyclic-display theorem and its primitive directions; research/DP53_integrated_fragment.tex, the full globally labelled spectrum and the diagonal-unit comparison of the fixed differential basis.
- AM-K012–015, the actual Hessian, stable integral ring, [2]-ratio, and source sigma normalization; AM-K017, the complete finite certificate for (K21.10); AM-K018, the exact full-$\mathcal O_E$ Chern/source gauge.

The new weighted inequalities (K21.5)–(K21.6), the multiplier verification (K21.11)–(K21.15), the exact finite determinant specialization and residues (K21.17)–(K21.19), and the actual explicit witness sequences (K21.20)–(K21.26) are the proof contributions of this note. The underlying genus-three theta identities are cited and source-audited in AM-K012–014; this note does not introduce a new analytic theta identity.
