# A-079. Complete independent audit of G035

**Status: PASS.** I read the complete saved `work/root/normalized_below_report.md`, NB.1–NB.15 and all six sections, its constructor and its public evaluator. I independently reconstructed both four-parameter lower cones and all nine boundary pieces from the original rank-three restriction calculation. The whole proof, all reconstructed phases and margins, and the public evaluator checks pass.

This review concerns the entire normalized region
$c<k$, $b+c\ge 2k$, $2b+x+3c\ge5k$.
Its actual representation is the normal-ideal Young multiplicity in G027/T049, with the stated twist $\operatorname{sgn}^{d+b+x+c}$. The previously proved normal-substitution and balanced inverse maps are retained at every branch.

## 1. The common character and the two lower cones

Put $C=c$, $R=k-c$, $b_0=b-c$. Then $R\ge1$, $b_0\ge2R$, and $2b_0+x\ge5R$. I checked the singleton and pair formulas against the actual interlacing conditions. In particular, $b\ge k+1$ on this domain, so the two-row determinant removal used in the singleton calculation has nonnegative parts. The full three-minor pair comparison from T058 applies since the largest normal part is at most $2k-2<b+c$.

For the selected triple put $\tau=3R-3-b_0$. The exact character contribution is

$$
(-1)^{\#\operatorname{cycles}(\eta)}
\varepsilon^{x+R-1}h_\eta(C)
\{A_{\eta,\varepsilon}(\tau)
-A_{\eta,\varepsilon}(\tau-x-1)\}.
$$

I rechecked its derivation from the general triple calculation in A074: the selected normal first exponent is reversed at $3(k-1)$; interlacing gives a deficit below $k$, so the truncation can be removed for those individual coefficients; the two Weyl differences telescope exactly; and the residual last-coordinate coefficient is $h_\eta(C)$. The orientation of the selected triple and the complementary transposition sign both remain present. This evaluates the actual oriented restriction complex.

For cone A the coordinates are
$R=T+6+K$, $x=T+X$, $b_0=2T+15+3K$.
Thus $\tau=T$, $b_0-2R=K+3$, and the first partition gap is $X+K$. For cone B they are
$R=X+2S+8+K$, $x=X$, $b_0=2X+5S+20+3K$.
Here $\tau=X+S+1$, $b_0-2R=S+K+4$, and the first gap is $K$. All coordinates are nonnegative and these maps recover the physical parameters without an additional hypothesis.

The upper-cone substitutions are respectively
$(T+X,-T-1,T+K+2,C)$ and
$(X,-X-S-2,X+2S+K+4,C)$.
The actual singleton, pair and triple formulas establish the whole physical domain, including the initial summation values; formal negative substitution alone is not used to prove the extension.

The support transfer uses the invariant
$\sum_{\sigma\in S_5}(\sigma(p_{135}p_{24}))^2$ in the flag-polynomial domain. Its row degree is $(2^5)$ and its right weight is $(4,4,2)$, so multiplication sends $C$ to $C+2$ and preserves the effective outer label. Its rational Vandermonde evaluation is nonzero. The stated $C=0,1$ providers and the finite $C=2,3$ seed vectors therefore prove the asserted support for the two cones.

## 2. All nine boundary pieces

For $D=b_0-2R\in\{0,1,2\}$, the exact coordinates are

$$
C=H+2,\quad R=T+D+3,\quad
b_0=2T+3D+6,\quad x=T+3-D+Y.
$$

They give $\tau=T$ and first gap $Y$. The substitution into cone A is $(X,T,K,C)=(Y+3-D,T,D-3,H+2)$. Every negative formal $K$ here is justified by the original physical restriction calculation and its initial binomial identities.

When $R=1,2,3$ and $\tau<0$, the six remaining pieces have:

| Piece | $b_0$ | $x$ |
|---|---:|---:|
| R1a | 2 | $Y+1$ |
| R1b | $B+3$ | $X$ |
| R2a | 4 | $Y+2$ |
| R2b | $B+5$ | $X$ |
| R3a | 7 | $Y+1$ |
| R3b | $B+8$ | $X$ |

In every row $C=H+2$. The inequalities $b_0\ge2R$ and $2b_0+x\ge5R$ give exactly the displayed lower bounds. The point $R=3,b_0=6$ has $\tau=0$ and belongs to D0.

The potentially delicate residue bound is
$M=\lfloor(r-1-s-t)/L\rfloor\ge-2$ in the inner triangle. At $M=-1,-2$, the summation is empty and $\binom{M+2}{i+j+2}=0$ because its top is $1$ or $0$ and its bottom is at least $2$. The outer one-variable sum has the corresponding $M=-1$ empty endpoint. The complete-function negative indices are the exact initial zeros of the degree-three or degree-four recurrence. These checks establish the formulas at R1, R2 and R3.

## 3. Exhaustion

The route first uses the complete $c=0$ and $c=1$ walls. For $C\ge2$, set $\tau=3R-3-b_0$.

- For $\tau<0$, $R\ge4$ is exactly T058; $R=1,2,3$ is one of the six rows above.
- For $\tau\ge0$ and $x<\tau$, cone B has coordinates
  $(x,\tau-x-1,2b_0+x-5R,C)$.
- For $\tau\ge0$ and $x\ge\tau$, put $D=b_0-2R$. For $D\ge3$, cone A has coordinates $(x-\tau,\tau,D-3,C)$. For $D=0,1,2$, the strip has $(Y,T,H)=(2b_0+x-5R,\tau,C-2)$.

Substitution returns the original physical tuple. Every inverse coordinate is nonnegative by the domain inequalities and its branch test. This proves exhaustive routing by actual module formulas.

## 4. Independent reconstruction

The independent programs do not import the root or theta phase constructors. The oracle `generic_normalized_trace_oracle.cpp` evaluates the ambient three-row determinant, literal singleton interlacing, original two-slot Schur normal multiplicities and direct rank-two skew determinants. For triples it computes the original Schur coefficients and sums the interlacing region before any triple telescope.

The rational reconstruction uses the proved safe class-degree bounds $(6,4,4,3,0,3,0)$. These follow from complete-character polynomial degrees, determinant cancellations and the number of independent simplex sums, as in A078. The triple terms stay within these bounds: identity degree at most six, transposition phases at most three, double-transposition phases at most two, three-cycle phases at most one, and the remaining phases periodic. The unisolvent comparisons therefore determine whole phase polynomials.

The native oracle's absolute prefix bound is
$761594710551524286676372573206<2^{127}$;
all interpolation and finite differences use exact rational/Python integer arithmetic.

| Scope | Phases | Literal trace evaluations | Positive-order margins |
|---|---:|---:|---:|
| Lower A and B | 4,582 | 32,332 | 259 |
| All nine boundary pieces | 2,979 | 18,207 | 402 |

Every reconstructed polynomial and margin equals the saved source coefficient by coefficient. The lower minima are 131670 and 8700. In order D0,D1,D2,R1a,R1b,R2a,R2b,R3a,R3b, the boundary minima are
805020, 829590, 852540, 2362800, 3016760, 4215300, 1557680, 3371790, 3473785.
All 56 lower-cone seed multiplicities were independently recovered.

Files: `check_generic_lower_independent.py`,
`GENERIC_LOWER_INDEPENDENT_RECEIPT.json`,
`check_generic_boundaries_independent.py`,
`GENERIC_BOUNDARIES_INDEPENDENT_RECEIPT.json`, and the separately saved reconstructed phases and query lists.

## 5. Public evaluator and exact check scope

`check_normalized_below_evaluator.py` checks all fourteen provider branches at 44 physical cases, using 308 original class traces and 616 outer coefficients with both determinant parities. It also checks 308 large-coordinate continuation coefficients against the independently reconstructed polynomials, 98 provider exports, 18,816 literal matrices and 21,392 bounded witnesses. Every comparison passes; the exact counts are in `NORMALIZED_BELOW_EVALUATOR_RECEIPT.json`.

The selector/increasing-subset bijection, maximum 152 selected tags and maximum eleven integer variables were checked against the exported matrices. The zero-order constants are actual multiplicities; the positive-order constants follow from proved domination inequalities. No $60^4$ base cube was executed or claimed in this audit. The prior G033/G034/T058 proof and computation scopes remain their separately recorded events.
