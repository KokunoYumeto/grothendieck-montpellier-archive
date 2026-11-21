# A-080. Complete independent audit of T059

**Status: PASS.** I read all of `work/theta/outer5/variable_wall/generic_high_twist_report.md`, HT.1–HT.12 and all seven sections, its phase constructor and positive evaluator. The exact module calculation, endpoint identities, complete support argument and fixed positive formula pass.

## 1. Domain and actual restriction maps

The coordinates
$x=X$, $b=K+B+1$, $k=K+U+1$, $c=K+2U+1$
give exactly $k\le c<2k$, $b+c\ge2k$. Their inverse is
$(X,B,K,U)=(x,b-2k+c,2k-c-1,c-k)$.
The first partition gap is $2B+X+U$, so every nonnegative coordinate tuple is a valid input, including the origin.

The normal-substitution and balanced inverse maps of G027/T049 identify the balanced module with the normal-ideal Schur multiplicity, twisted by $\operatorname{sgn}^{d+b+x+c}$. The degree difference is $|\alpha|-5k=2B+X+U\ge0$, which removes all four- and five-selected terms. For a triple, interlacing forces $\rho_1\ge b+c$ and $\rho_2\ge c$. Hence
$|\rho|\ge b+2c>3(k-1)$, with excess $B+U+3$.
This proves the exact three-term oriented restriction complex on the whole region.

## 2. Full singleton determinant and initial values

The singleton is the full three-row determinant simplex

$$
\sum_{r_1+r_2+r_3<k}
\det[h_{\alpha_i-i+j-r_i}(V)]_{1\le i,j\le3}.
$$

It follows by applying
$h_j(V\oplus z)=\sum_{r\ge0}h_{j-r}(V)z^r$
to every determinant row and extracting normal degrees below $k$.
This is the actual one-dimensional torus branching map followed by the Young projection. It retains the full last row and so retains the terms lost by the formula refuted in A077.

The first two rows have nonnegative indices. The last-row minimum is $c-k-1=U-1\ge-1$. The phase formulas for the three-dimensional complementary standard module have the exact initial zeros $h_{-1}=h_{-2}=0$, proved by the backward recurrence of the reciprocal degree-three characteristic polynomial.

After splitting three summation variables into residues modulo $L$, the simplex bound is
$M=\lfloor(k-1-s_1-s_2-s_3)/L\rfloor\ge-3$.
The binomial identity has numerator $M+3$ and denominator index at least three. Thus $M=-1,-2,-3$ gives exactly the empty-sum value zero. These endpoints include $k=c=1$.

## 3. Pair terms and the empty endpoint

The T058 comparison applies because the largest normal part is $p\le2k-2<b+c$. Its three exterior-dual minors, rational highest-space map and normal Schur multiplicities are retained.

Put $R=2k-c=K+1$. The fixed-pair range is $c-k+1\le l\le k-1$. Writing $l=U+s$ gives
$\sum_{s=1}^{R-1}T_{R-s}(W^*)T_s(W^*)$.
For an interchange, the coefficient is zero for odd $R$ and $T_{R/2}(W^{*2})$ for even $R$. Its orientation is negative.

The rational invariant dot product gives the $S_3$ identification $W^*\simeq W$. Since $b+c=2R+B+2U$, the determinant factor is $\det(W)^B$ through the equivariant trivialization $\omega\otimes\omega\mapsto1$. These maps justify the finite-group comparison and signs.

At $R=1$, both the original and reindexed fixed-pair ranges are empty. The auxiliary substitution $k'=R-1,c'=R-2$ is used only in its proved binomial sum, whose upper bound is then $-1$. No negative symmetric-power object is introduced.

## 4. Independent phases, positivity and support

`check_generic_high_independent.py` reconstructs the phases using original literal singleton interlacing, two-slot normal Schur multiplicities and direct skew determinants. It does not import the theta constructor or simplified pair expression. The oracle is `generic_rank_three_trace_oracle.cpp`.

The safe degrees are $(6,4,4,3,0,3,0)$. For a transposition complementary singleton, the complete function is linear plus one alternating term. Its pure linear three-row determinant vanishes; one alternating rank-one row and the other two linear rows give degree at most one. Three simplex summations give degree at most four. The double-transposition case has the same bound, and periodic complementary cases give degree at most three. Ambient and pair terms obey this safe list. These bounds justify finite unisolvent reconstruction.

All 2,291 phases were reconstructed from 16,166 literal class values, agreeing coefficient by coefficient with the source. The resulting degrees are $(6,3,2,1,0,0,0)$ and the distinct-phase counts are $(1,14,10,25,3,3,3)$. The native absolute prefix bound is
$342717623936956795150042573206<2^{127}$;
reconstruction and differences use exact rational/Python integer arithmetic.

All 150 step-60 domination polynomials agree with the source; every coefficient is nonnegative and every constant positive. The minimum constant is 293640. The 151 identity monomials equal the downset in HT.9, so all omitted differences vanish. The invariant Hermitian trace bound proves positivity of every nonzero-order multiplicity difference. Zero-order values are actual multiplicities; all constants are integers.

I independently reconstructed all 1,015 multiplicities at the 64 boundary-parity points and 81 small-cube points. All 19 zero cases agree. The four squared-minor invariants, in X,B,K,U order, have Vandermonde evaluations
241920, 8400, 27840, 2480.
Their weights give actual coordinate-plus-two injections with unchanged effective outer label. Reducing a coordinate at least three to 3 or 4 of its parity and the others to 0 or 1 proves that these 145 points settle the whole support.

The complete record is `GENERIC_HIGH_INDEPENDENT_RECEIPT.json`, with separately saved query list and reconstructed phases. No $60^4$ cube was enumerated or claimed.

## 5. Positive formula and evaluator

Residues are fixed modulo 60. The downset has 151 orders and maximum total degree six. Each term is a nonnegative integer selector times four increasing-subset counts, so the inequalities have at most $5+6=11$ integer variables. Input parameters enter only the four quotient equations and bounded chain endpoints.

The evaluator applies the exact inverse parameter map and parity $d+b+x+c$, evaluates fixed bounded constants, and exports matrices and lazy witnesses. The executed checker `check_generic_high_evaluator.py` compares every row of the printed factor table against the reconstructed identity polynomial, and compares both determinant parities, small endpoints and large continuations against independent phase data. Its exact counts are in `GENERIC_HIGH_EVALUATOR_RECEIPT.json`.

The original theta and rectangular checks remain separately attributed. This audit supplies the independent whole-proof reading, full phase reconstruction, full support-point reconstruction and evaluator checks described above.
