# Tensor-norm subtask: checked mathematical notes

Run: `GCT_GINEQ/tensor_norms`. Agent: `/root/tensor_norms`.
Model: GPT-6 Astra Pro (inherited). Effort: not exposed by the runtime.
Started 2026-11-20T23:00Z (2026-11-21T00:00+01:00 Europe/Berlin).

These are results derived or checked in this run; no claim of bibliographic
novelty is made. The parent owns final statement identifiers and deliverables.

## Conventions

The field is `F = R` or `C`, and all factor spaces have their standard
Euclidean/Hermitian structures. Write `F(T)=||T||_2` for the Hilbert tensor
norm, `sigma(T)` for the injective/spectral norm, and `pi(T)` for the
projective/nuclear norm. Tensor rank means ordinary CP rank unless otherwise
specified. Complex border rank is Zariski border rank; over `R`, the proofs
below apply to Euclidean border rank. Support-based bounds also apply to the
complex border rank of real tensors even when their real norm is used,
because the support dimensions are the same over both fields.

Duality gives `F(T)^2 <= pi(T) sigma(T)`. Consequently the three homogeneous
ratios

`a(T)=F(T)^2/sigma(T)^2`, `b(T)=pi(T)^2/F(T)^2`,
`c(T)=pi(T)/sigma(T)` satisfy `a <= c <= b` for nonzero `T`.

Exact source: Friedland--Lim, *Nuclear Norm of Higher-Order Tensors*,
arXiv:1410.6072v3, §2, equations (5)--(8) and the displayed duality argument
immediately following (8), pp. 3--4. The attachment is the same version.

## N-01. Intrinsic-support norm inequalities

**Statement.** Let `d>=2`, let `T` be nonzero, and let `q_i` be its mode-i
flattening rank. Put `Q=min_j prod_{i!=j} q_i`. Then

`pi(T) <= sqrt(Q) F(T)` and `sigma(T) >= F(T)/sqrt(Q)`.

In particular, each of `a,b,c` is at most `Q`. If border rank is `r`, then

`r >= ceil((pi(T)/F(T))^(2/(d-1)))`,

and the weaker lower bounds with `a^(1/(d-1))` or `c^(1/(d-1))` are also
valid. Every one of these bounds is at most `max_i q_i`, the ordinary
mode-flattening bound.

**Proof.** For each `i`, the image of the mode-i flattening gives a minimal
support subspace `E_i` of dimension `q_i`, and `T` lies in
`E_1 tensor ... tensor E_d`. One elementary verification is to project to
the orthogonal complement of each image: all contractions in the remaining
factors vanish, so each such projection annihilates `T`; the mutually
commuting projections to the `E_i` therefore fix `T`. Orthogonal projection
onto each `E_i` is contractive, so computing either tensor norm in these
subspaces gives its value in the original spaces.

Fix `j` and orthonormal bases in all `E_i` with `i!=j`. Expand

`T = sum_alpha e_{alpha_1} tensor ... tensor v_alpha tensor ... tensor e_{alpha_d}`,

where `v_alpha in E_j` and there are `P_j=prod_{i!=j}q_i` indices. This is
a decomposition into pure tensors, so

`pi(T) <= sum_alpha ||v_alpha|| <= sqrt(P_j) (sum_alpha ||v_alpha||^2)^(1/2)
         = sqrt(P_j) F(T)`.

For every nonzero `v_alpha`, evaluation at the corresponding basis vectors
and `v_alpha/||v_alpha||` proves `sigma(T)>=||v_alpha||`. Hence
`F(T)^2=sum_alpha||v_alpha||^2 <= P_j sigma(T)^2`. Minimize `P_j` over `j`.
The three ratio inequalities follow, including `c<=Q` by multiplying the
two inequalities. Each mode flattening has rank at most CP rank, and its
`(r+1)`-minors vanish on every rank-at-most-r tensor, hence on its Zariski
closure (or Euclidean closure over `R`). Thus `q_i<=r` and `Q<=r^(d-1)`.
Finally `Q<= (max_i q_i)^(d-1)`. Taking roots and ceilings cannot exceed
the integer `max_i q_i`. This proves every assertion. QED.

**Scope.** This is a barrier for this specified support-norm conversion,
not a theorem excluding every conceivable norm-assisted rank method.

## N-02. Matrix multiplication: exact norms and no constant repair

Let `M_n=sum_{i,j,k=1}^n E_ij tensor E_jk tensor E_ki`.
The exact values are

`F(M_n)^2=n^3`, `sigma(M_n)=1`, `pi(M_n)=n^3`.

These are known: Derksen, arXiv:1308.3860v2, Corollary 1.10 (rectangular
version `pi(M_pqr)=pqr`, `sigma(M_pqr)=1`), with the coordinate convention
in §1.5, equation (4). The real-field specialization follows from the
same proof: the coordinate decomposition gives the real upper bound and
`|tr(XYZ)|<=||X||_F||Y||_F||Z||_F` gives the real and complex spectral upper
bound; a compatible triple of matrix units attains it. The dual witness
`M_n` then proves the matching nuclear lower bound. This short comment
records why the complex source gives the real form as well.

**Statement.** No finite constant `C` can make any one of

`a(T)<=C rank(T)`, `b(T)<=C rank(T)`, `c(T)<=C rank(T)`

valid even just for all square matrix multiplication tensors. Nor can
`rank` be replaced by border rank. In particular, inserting any fixed
power of a fixed Grothendieck constant cannot repair these inequalities.

**Proof.** Strassen's seven-term decomposition, reproduced exactly in
Derksen §1.5 equation (5), is defined over `R`, so
`rank_F(M_2)<=7` for either field. Factorwise tensoring of decompositions
proves `rank(S boxtimes T)<=rank(S)rank(T)`. Under the identification
`E_ij tensor E_ab -> E_(i,a),(j,b)` in each of the three factors,
`M_n boxtimes M_m=M_nm`. Consequently `rank_F(M_(2^k))<=7^k`.
For these tensors each of `a,b,c` equals `(2^k)^3=8^k`. If any proposed
inequality held with constant `C`, it would give `8^k<=C 7^k`, which is
false for `k` sufficiently large. Since border rank is at most rank,
the border-rank versions fail too. No norm multiplicativity assertion
for arbitrary tensor products is used. QED.

**Lower-bound comparison.** N-01 gives only `ceil(n^(3/2))` for `M_n`.
Every mode flattening has `n^2` singular values equal to `sqrt(n)`, so
its matrix norm ratios all give `n^2`. This exceeds the full-tensor
support-norm bound for `n>=2` (allowing equality only after very small
rounding coincidences; at n=2, ceil(2sqrt(2))=3<4).

## N-03. A border-rank-two counterexample and an explicit rank-two example

Let `W=e_1 tensor e_1 tensor e_2 + e_1 tensor e_2 tensor e_1
       +e_2 tensor e_1 tensor e_1` in `(F^2)^(tensor 3)`.

**Statement.** `rank_F(W)=3`, `border_rank_F(W)=2`. The norm values are

`F(W)^2=3`, `sigma_R(W)=sigma_C(W)=2/sqrt(3)`,
`pi_R(W)=3`, `pi_C(W)=3sqrt(3)/2`.

The exact norm values are the rescaling of Friedland--Lim Lemma 6.2,
equations (34)--(37). Thus over `C` all three ratios `a,b,c` are `9/4>2`;
over `R` they are respectively `9/4`, `3`, and `3sqrt(3)/2`, again all
greater than border rank.

**Proof of the rank assertions.** The displayed three-term expression
gives rank at most 3. First-mode slices span the pencil

`[[y,x],[x,0]]`, whose determinant is `-x^2`.

Only the line `x=0` in this two-dimensional pencil consists of matrices
of rank at most one. If the tensor had rank two, the first-mode flattening
rank two would force its two first factors to be independent, and the
slice space would be spanned by two independent rank-one matrices. That
is impossible. Thus rank is 3. On the other hand,

`T_t=((e_1+t e_2)^(tensor 3)-e_1^(tensor 3))/t -> W`

as nonzero real `t` tends to zero. The tensors `T_t` have rank at most
two. Their first-mode flattenings have rank two, since the two vectors
`e_1+t e_2,e_1` and their corresponding squares are independent, so they
have rank exactly two. The flattening of `W` has rank two too. Hence
border rank of `W` is exactly two, for either field and also for real
Euclidean border rank. QED.

**Explicit exact refutation of ordinary-rank versions.** Take `t=1/100`.
Then `rank_F(T_t)=2` and

`F(T_t)^2=3+3t^2+t^4 >=3`,
`F(T_t-W)=sqrt(3t^2+t^4)<=2t=1/50`.

The spectral triangle inequality and `2/sqrt(3)<6/5` give

`sigma_F(T_t)<6/5+1/50=61/50`.

Therefore

`a(T_t)>3/(61/50)^2=7500/3721>2`.

Since `a<=c<=b`, all three ordinary-rank comparisons with constant 1
fail for this explicit rational tensor, over both fields. QED.

## N-04. What bounded summands actually certify

**Statement.** Let `B>0`. If `T=sum_{j=1}^r A_j` with every `A_j` pure and
`||A_j||_2<=B`, then `r>=pi(T)/B`. More generally a dual witness `Z`
with a positive certified upper bound `sigma(Z)<=U` yields
`r>=|<Z,T>|/(UB)`. These are valid certificates for the stated bounded
summand model. They do not certify unrestricted rank or border rank.

For fixed finite-dimensional factor spaces, fixed `r` and finite `B`,
the set of all such sums is compact. In particular, a limit of rank-r
decompositions with uniformly bounded pure terms has ordinary rank at
most r. Every rank-two decomposition along any sequence `T_t -> W`
as in N-03 must have unbounded largest summand norm.

**Proof.** Each pure tensor has `pi(A_j)=||A_j||_2`, so
`pi(T)<=sum_j pi(A_j)<=rB`; duality gives
`|<Z,T>|<=sigma(Z)pi(T)<=UrB`.
The set of pure tensors of Hilbert norm at most `B` is compact: it is
the continuous image of `[0,B]` times the product of unit spheres
(with a complex phase placed in one sphere when necessary). Taking an
r-fold product and then the continuous sum map preserves compactness.
If largest summand norms in rank-two decompositions of some sequence
`T_t -> W` were bounded, a convergent subsequence of their two terms
would exhibit `W` as a sum of two pure tensors. This contradicts N-03.
QED.

**Additional elementary observation.** The convex hull of the entire
rank-one cone is the whole tensor space, because every tensor is a
finite sum of pure tensors and the same sum is a convex combination
after multiplying each term by the number of summands. Thus nuclear
norm balls relax *normalized* atoms, not the unrestricted rank-one cone.

## N-05. Corrected flattening comparisons and two source defects

**Checked source defects, not merely stylistic objections.** In the supplied
Friedland--Lim v3 source (and PDF), Lemma 9.2 equation (57) displays

`sigma(A) = max |<A,x tensor M>|/(||x|| ||M||_sigma)`.

As written this is false. For `A=e tensor I_m`, the left side is 1,
whereas taking `x=e`, `M=I_m` gives value `m` on the right. The denominator
must use the matrix nuclear norm. The equation immediately before (60)
also asserts `||M||_* <= sqrt(rank M) ||M||_sigma`, false for `M=I_m`,
`m>1`. The final Theorem 9.4 has the standard, correct inequalities and
should be used only with a corrected proof rather than these displays.

**Correct forms.** For a 3-tensor with mode ranks `(q_1,q_2,q_3)`, write
`A_(1)` for the first flattening and `s=min(q_2,q_3)`. Then

`||A_(1)||_* <= pi(A) <= sqrt(s) ||A_(1)||_*`,
`sigma(A) <= ||A_(1)||_op <= sqrt(s) sigma(A)`.

**Proof.** First restrict all factors to their minimal Hilbert supports.
Every pure tensor becomes a rank-one matrix under flattening, with the
same Hilbert product norm. This gives the first nuclear lower bound;
the spectral upper bound follows because the flattened spectral
optimization permits arbitrary unit vectors in the last two factors,
including decomposable ones. In a matrix singular value decomposition
`A_(1)=sum_l s_l x_l tensor V_l`, each `V_l` has Hilbert norm one and is
a matrix supported in dimensions `(q_2,q_3)`, so its matrix nuclear norm
is at most `sqrt(s)`. Decomposing each `V_l` into its matrix SVD gives
`pi(A)<=sqrt(s)sum_l s_l`.
For the other spectral inequality, take arbitrary unit `x` and a unit
Hilbert matrix `V` in the last two factors. Matrix nuclear/operator
duality gives
`|<A,x tensor V>| <= sigma(A) ||V||_* <= sqrt(s) sigma(A)`.
Indeed the contraction `A(x)` is a matrix with operator norm at most
`sigma(A)`. Maximize over `x,V`. QED.

These proofs avoid the invalid claim that a maximizing matrix can be
replaced by its top singular term while preserving its pairing.

## N-06. Parent results independently checked

The parent supplied symmetric polynomial tensors `S_det,S_per` in
`Sym^n(F^(n x n))`, defined by their polynomial and with coefficient
`+/-1/n!` on the `(n!)^2` valid ordered lists of n distinct matrix units.

### N-06a. Catalecticant singular spectrum

For a `k | (n-k)` flattening, the nonzero blocks are indexed by row and
column subsets `(I,J)` of cardinality k. Each block has `(k!)^2` rows
and `((n-k)!)^2` columns. For the permanent every entry is `1/n!`.
For the determinant the sign factors into the sign of the partial
matching on `I -> J`, that on the complement, and a fixed row/column
shuffle sign depending only on `(I,J)`. Consequently every block has
rank one and singular value

`sqrt((k!)^2 ((n-k)!)^2)/n! = 1/binom(n,k)`.

There are `binom(n,k)^2` blocks. Their squared singular values sum to
1, agreeing with `F(S_det)^2=F(S_per)^2=1`. The matrix norm rank
certificates give both ordinary and symmetric border rank at least
`binom(n,k)^2`.

### N-06b. Full tensor nuclear norms via finite sign averages

For the determinant put
`X_(sigma,epsilon)=sum_i epsilon_i E_(i,sigma(i))/sqrt(n)` and
`w_(sigma,epsilon)=sgn(sigma)prod_i epsilon_i`, averaging uniformly over
`sigma in S_n` and `epsilon in {+/-1}^n`. In each coefficient of
`E[w X^(tensor n)]`, the sign average vanishes unless each row appears
an odd number of times. Since total degree is n, each row appears once;
the permutation support then also forces each column to appear once.
There is one compatible permutation, giving coefficient
`sgn(sigma) n^(-n/2)/n!`. Therefore the average equals
`n^(-n/2) S_det`. Every `X` has Hilbert norm one, so
`pi(S_det)<=n^(n/2)`.

For the permanent put `X_(epsilon,delta)=(epsilon_i delta_j)_(ij)/n`
and `w=prod_i epsilon_i prod_j delta_j`. Averaging independently over
all row and column signs forces all row and column occupancies odd,
hence exactly one each. The surviving coefficient is `n^(-n)`, so
the average equals `(n!/n^n) S_per`. All `X` again have Hilbert norm
one, giving `pi(S_per)<=n^n/n!`.

Banach's symmetric spectral norm theorem (Friedland--Lim §5 equation
(23)), the determinant singular-value inequality, and the CLL permanent
inequality imply respectively `sigma(S_det)=n^(-n/2)` and
`sigma(S_per)=n!/n^n`. Equality is attained at `I/sqrt(n)` and `J/n`.
Since both Hilbert norms are one, duality proves that both nuclear
upper bounds are equalities. The proof works over both fields.

**Independent check outcome.** Every coefficient, sign constraint,
normalization, block count, and real/complex use was independently
rederived, and the full proof was read. No gap was found. Parent
statement IDs should replace the temporary N-06 labels in final events.

## N-07. Constant-factor failure also for determinant/permanent targets

This extension may be used if desired; N-02 already suffices to refute a
universal repair of the three matrix-style norm/rank comparisons.

### Row tensors

For the row determinant `D_n=sum_sigma sgn(sigma)e_sigma(1) tensor ...`
the exact norms give `a=b=c=n!`. Derksen §8, p.23 (the final displayed
inequality immediately before Remark 8.1) proves
`rank(D_n)<=(5/6)^floor(n/3)n!` over R and C (the displayed 5-term
formula for `D_3` and repeated Laplace expansion have rational
coefficients). Thus the ratio of any of a,b,c to rank is at least
`(6/5)^floor(n/3)`, unbounded.

For the row permanent `P_n`, Derksen Theorem 1.14, §5 proof, and
§1.7 equation (8) give `a=b=c=n^n/n!` and
`rank(P_n)<=2^(n-1)`. Put `A_n=n^n/(2^(n-1)n!)`. For `n>=2`,

`A_(n+1)/A_n=(1+1/n)^n/2
 >= (1+1+(n-1)/(2n))/2 >=9/8`.

The middle bound keeps the first three terms of the binomial expansion.
Therefore `A_n` tends to infinity, giving the same conclusion.

### Symmetric polynomial tensors

In N-06b, replacing all `epsilon_i` by `-epsilon_i` leaves the weighted
tensor summand unchanged, since both weight and n-th power acquire
the factor `(-1)^n`. Thus the determinant sign average has at most
`n! 2^(n-1)` distinct weighted pure powers. The permanent average has
the same independent redundancy for all row signs and all column
signs, leaving at most `2^(2n-2)=4^(n-1)` terms. Hence even their real
Waring ranks satisfy

`rank_sym(S_det)<=n!2^(n-1)`,
`rank_sym(S_per)<=4^(n-1)`.

Their three full-tensor norm ratios are respectively `n^n` and
`(n^n/n!)^2`. Dividing these by the preceding upper bounds gives
`A_n` and `A_n^2`, which diverge by the elementary recurrence above.
This disproves a fixed-constant comparison with Waring rank, hence
also with CP rank or either corresponding border rank, for both
polynomial families. No assertion that CP rank equals Waring rank is
needed. QED.

## Bibliographic locators checked

1. Friedland--Lim, arXiv:1410.6072v3, §2 equations (5)--(8), p.4 duality;
   §5 equation (23) (Banach); Theorem 5.1, Corollary 5.2 and Corollary 5.3
   (symmetric nuclear decomposition); Lemma 6.2 equations (34)--(37)
   (W state); Lemma 9.2 equation (57), equation before (60), and Theorem
   9.4 (the source defects and correct final comparison).
   URL: https://arxiv.org/pdf/1410.6072
2. Harm Derksen, arXiv:1308.3860v2, §1.5 equations (4),(5), Corollary
   1.10; §1.7 equation (8), Theorems 1.14 and 1.15; §5 proofs;
   §8 pp.22--23 and final displayed bound before Remark 8.1.
   URL: https://arxiv.org/pdf/1308.3860
3. Carlen--Lieb--Loss, arXiv:math/0508096v1, Theorem 1.1 equation (1.1),
   p.1, sharp permanent inequality (complex inputs).
   URL: https://arxiv.org/pdf/math/0508096
4. Landsberg--Michalek, arXiv:1608.07486v1, Theorem 1.1, p.1, gives
   `border_rank(M_n)>=2n^2-ceil(log_2 n)-1` using border substitution
   and Koszul flattenings. URL: https://arxiv.org/pdf/1608.07486
   This historical comparison is checked, but no claim it is a current
   optimal bound is made here.

## Check events (draft records for parent integration)

All timestamps below are UTC; Europe/Berlin date is the following day.
No Lean/formal verification was performed. No unexposed effort setting
has been invented.

| ID | Timestamp | Who | Actual type | Outcome |
|---|---|---|---|---|
| N-01 | 2026-11-20T23:06Z | GPT-6 Astra Pro; effort not exposed; GCT_GINEQ/tensor_norms | targeted proof check | Full proof reread; projection, orthonormal expansion, border minors and dominance checks pass. |
| N-02 | 2026-11-20T23:06Z | same | targeted proof check | Full amplification proof reread; uses actual M_nm identification, not an unjustified norm multiplicativity rule. Pass. |
| N-03 | 2026-11-20T23:06Z | same | targeted proof check | Full pencil rank proof, degeneration, and exact t=1/100 inequalities reread and checked. Pass. |
| N-04 | 2026-11-20T23:06Z | same | targeted proof check | Full duality and compactness proof reread; unrestricted-rank limitation follows precisely. Pass. |
| N-05-invalid-57 | 2026-11-20T23:06Z | same | refuted, refined statement N-05 | Counterexample e tensor I_m checked against actual supplied and web PDF formula. |
| N-05-invalid-matrix-bound | 2026-11-20T23:06Z | same | refuted, refined statement N-05 | Identity matrix refutes stated sigma denominator; corrected Hilbert denominator used. |
| N-05 | 2026-11-20T23:06Z | same | targeted proof check | Complete corrected proof reread. Pass. |
| N-06a | 2026-11-20T23:06Z | same | independent re-proof | Parent catalecticant block formula independently rederived, including determinant signs. Pass. |
| N-06b | 2026-11-20T23:06Z | same | independent re-proof | Parent sign twirls independently expanded coefficientwise, field and normalization checked. Pass. |
| N-07 | 2026-11-20T23:06Z | same | targeted proof check | Full constant-repair failure extension reread, term-count redundancies and recurrence checked. Pass. |
| B-FL-W | 2026-11-20T23:06Z | same | used and rechecked in this run | Lemma 6.2 source and exact rescaling checked; real/complex nuclear distinction preserved. |
| B-Derksen-M | 2026-11-20T23:06Z | same | used and rechecked in this run | Corollary 1.10 read; short real specialization and norm witness checked. |
| B-Strassen-7 | 2026-11-20T23:06Z | same | used and rechecked in this run | Derksen §1.5 equation (5) located and read; an exact coefficient expansion check is recorded separately if executed. |
| B-Derksen-row | 2026-11-20T23:06Z | same | used and rechecked in this run | Theorems 1.14,1.15, eq(8) and §8 displayed bound read; scalar ratios recalculated. |
| B-CLL | 2026-11-20T23:06Z | same | carried as background without fault found | Theorem 1.1 statement and field hypotheses read; long literature proof not reproved. |
| B-LM-2016 | 2026-11-20T23:06Z | same | carried as background without fault found | Theorem 1.1 read, exact ceiling verified; no reproof. |
| B-Strassen-7 | 2026-11-20T23:06:43Z | same | computation or formal certificate | `check_tensor_decompositions.py` expanded the 7 displayed terms over exact rational coefficients; exactly the 8 coefficients of M_2 remain. Pass. This is computation, not theorem-prover formalization. |
| B-Derksen-D3 | 2026-11-20T23:06:43Z | same | computation or formal certificate | Same script expanded the 5 displayed terms of D_3 over exact rational coefficients; exactly the 6 signed permutation coefficients remain. Pass. |
| N-03-rational-margin | 2026-11-20T23:06:43Z | same | computation or formal certificate | Exact Fraction arithmetic gives `7500/3721 - 2 = 58/3721 > 0`. Pass. |

### Source-locator correction/check, 2026-11-20T23:24Z

The five-term `D_3` formula and the final `(5/6)^floor(n/3)n!` rank bound in Derksen arXiv:1308.3860v2 are **unnumbered** displays. The precise locator is **Section 8, p.23 (PDF zero-based page 22), the five-term display and the final display immediately preceding Remark 8.1**. Any earlier informal reference to these as equations (12)--(13) is withdrawn. The present notes already used the correct unnumbered locator; the computation script's source comment has now been made equally explicit. Both displays were reread in the primary PDF and visually inspected on the actual page. No mathematical statement or exact computation changes.

| ID | Timestamp | Who | Actual type | Outcome |
|---|---|---|---|---|
| B-Derksen-D3-locator | 2026-11-20T23:24Z | GPT-6 Astra Pro; effort not exposed; GCT_GINEQ/tensor_norms | used and rechecked in this run | PASS, locator clarified: §8, p.23, unnumbered five-term display and final display before Remark 8.1; inspected actual PDF page. |

