# Positive hook plethysm at every fixed ideal order

## T-064. An explicit parameterized positive formula

Use T062's parameters
\[
m\ge4,\quad k\ge1,\quad a\ge2k+1,\quad
0\le r\le m-2,\quad t\ge0,\quad\mu\vdash m,
\]
\[
n=a+t-k,\qquad
\lambda=((m-1)a+t-mk-r,a+t,(t+1)^r,t^{m-2-r}),
\tag{FK.1}
\]
and \(\nu=\mu\) for even \(t\), \(\nu=\mu'\) for odd \(t\).
Put \(N=m-1\), \(j=k-1\), and define
\[
D_k=\sum_{p=0}^{k-1}
\left\{\begin{matrix}k-1\\p\end{matrix}\right\}
2^p(p+1)!.
\tag{FK.2}
\]
The braces are the set-partition numbers, with the empty-set
convention. Thus \(D_1=1,D_2=4,D_3=28,D_4=268\).

There is an explicit positive bounded-polytope formula for
\(p_{\mu,(n)}^\lambda\), with at most
\[
1+D_k\bigl(2(m^2+3m-4)-1\bigr)
\tag{FK.3}
\]
pieces, each in at most \(m^2+3m-4\) variables. The construction
below specifies every matrix, selected point and finite tag. Its
running time is bounded by
\[
f(k)(m+k+1)^{\,2k+O(1)}
\operatorname{poly}(\text{binary parameter lengths})
\tag{FK.4}
\]
for an explicitly computable function \(f\), obtained from the finite
loops below. Exact coefficient evaluation and nonvanishing have the
stronger bound \(f(k)\operatorname{poly}(m+\text{input bit length})\).
In particular these are polynomial bounds for every fixed ideal
order \(k\). The ordinary binary-part interpretation applies when
\(t\ge1\), since the output lists \(m\) positive parts. At \(t=0\)
the bound retains an explicit/unary outer-degree parameter.

The exact coefficient identity is
\[
p_{\mu,(n)}^\lambda
=c_{m,a,r}(\nu)-d_{m,k,r}(\nu),
\tag{FK.5}
\]
where the first term is the complete G037 stable-hook coefficient.
Sections 1–2 give a positive bounded-size branching formula for
\(d\), with \(0\le d\le D_k\). Sections 3–4 explicitly remove
exactly \(d\) points from G037's single polytope, proving (FK.3).

### 1. Actual homogenization and monomial-orbit induction

Let \(H=\Lambda^r\mathfrak h_N\). The target of T062's split jet
map is
\[
T_{m,k,r}=
\operatorname{Ind}_{S_N}^{S_m}
\left[
\left(\bigoplus_{h=0}^{j}\operatorname{Sym}^h\mathfrak h_N\right)
\otimes H
\right].
\]
The literal permutation module \(P_N=\mathbb Q^N\) decomposes as
\(\mathbb Q u\oplus\mathfrak h_N\), with
\(u=N^{-1}(1,\ldots,1)\). Multiplication by \(u^{j-h}\) gives the
actual equivariant isomorphism
\[
\bigoplus_{h=0}^{j}\operatorname{Sym}^h\mathfrak h_N
\xrightarrow{\sim}\operatorname{Sym}^{j}P_N.
\tag{FK.6}
\]
Its inverse is the homogeneous expansion with respect to this direct
sum. Thus no degree-zero or affine-coordinate character is omitted.

The monomial basis of \(\operatorname{Sym}^jP_N\) has orbits
indexed by partitions \(\rho\vdash j\) with \(p=\ell(\rho)\le N\).
For such an orbit let \(n_0=N-p\), and for each positive integer
\(h\) let \(n_h\) be the number of parts of \(\rho\) equal to \(h\).
Omit zero blocks and write \(B_\rho\) for the number of remaining
blocks. The monomial stabilizer is
\[
K_\rho=S_{n_0}\times\prod_{h\ge1}S_{n_h},
\tag{FK.7}
\]
with a zero-size factor omitted. Sending each coset to its monomial
is an actual permutation-module isomorphism. The tensor-induction
map of HJ.12 therefore gives
\[
T_{m,k,r}\simeq
\bigoplus_{\rho\vdash j,\ \ell(\rho)\le N}
\operatorname{Ind}_{K_\rho}^{S_m}
\operatorname{Res}_{K_\rho}^{S_N}H.
\tag{FK.8}
\]

For a permutation vector, subtract its mean separately on every
nonempty block. This gives the explicit rational decomposition
\[
\operatorname{Res}_{K_\rho}\mathfrak h_N
\simeq
\bigoplus_{b}\mathfrak h_{n_b}\ \oplus\ U_\rho,
\qquad
U_\rho=\{(c_b):\ \sum_b n_bc_b=0\}.
\tag{FK.9}
\]
Here \(U_\rho\) is a trivial module of dimension \(B_\rho-1\).
Taking exterior powers, and using the actual exterior-hook Young
maps already established in G037, gives a sum indexed by
\[
e+\sum_b s_b=r,\qquad
0\le e\le B_\rho-1,\qquad
0\le s_b\le n_b-1.
\tag{FK.10}
\]
The multiplicity is \(\binom{B_\rho-1}{e}\), and the block
representation is the tensor product of hooks
\([(n_b-s_b,1^{s_b})]\). Frobenius induction therefore yields
the entirely positive formula
\[
d_{m,k,r}(\nu)=
\sum_{\rho}\ 
\sum_{\text{(FK.10)}}
\binom{B_\rho-1}{e}
\left[s_\nu\right]\!
\left(
s_{(1)}\prod_b s_{(n_b-s_b,1^{s_b})}
\right).
\tag{FK.11}
\]
The factor \(s_{(1)}\) records the one coordinate fixed by
\(S_N\subset S_m\). Every product coefficient is evaluated by
successive literal Littlewood–Richardson tableaux.

This involves only small skew shapes. When \(n_0>0\), take that
block's hook first; the remaining factors have total size
\(p+1\le k\). When \(n_0=0\), one has \(m=N+1=p+1\le k\),
so the entire computation has at most \(k\) cells. Enumerate only
intermediate diagrams between the starting hook and the requested
\(\nu\), then read each skew tableau right to left, top to bottom,
checking its content, row/column inequalities and prefix lattice
inequalities. These are the exact maps and tableaux of Macdonald
I§9(9.2), p143, whose complete proof pp142–147 was read for this
construction, together with I§7(7.3). No plethysm coefficient or
representation-decomposition oracle enters (FK.11).

### 2. A correction bound independent of the outer degree

The normalized symmetrization map embeds
\(\operatorname{Sym}^jP_N\) into \(P_N^{\otimes j}\).
Tensoring with \(H\) and inducing gives an actual injection of
the target (FK.8) into the corresponding ordered-word module.
Its word orbits are indexed by equality patterns: for \(p\)
distinct coordinate values there are
\(\left\{\begin{smallmatrix}j\\p\end{smallmatrix}\right\}\)
set partitions, each with stabilizer \(S_{N-p}\) fixing the
\(p\) selected coordinates individually.

For \(N-p\ge1\), the same coordinate-mean map gives
\[
\mathfrak h_N\big|_{S_{N-p}}
\simeq\mathfrak h_{N-p}\oplus\mathbb Q^p.
\]
Its \(r\)-th exterior power is a sum of hooks with total multiplicity
at most \(2^p\). Induction to \(S_m\) adds \(p+1\) boxes. For
each starting hook and output, the branching multiplicity is the
number of standard tableaux on that skew shape, at most \((p+1)!\).
When \(N-p=0\), the restricted space has dimension
\(\binom{N-1}{r}\le2^p\); induction from the trivial group has
multiplicity at most \(m!=(p+1)!\). Summing the actual word
orbits proves
\[
0\le d_{m,k,r}(\nu)\le D_k.
\tag{FK.12}
\]
It also proves a useful support fact: every label with \(d>0\)
is obtained from a hook by adding at most \(k\) boxes, or has
total size at most \(k\). Thus each content diagonal contains
at most \(k+1\) cells.

For \(\nu=(m)\), formula (FK.9) gives a sharper fact. A positive
exterior power of a nonzero standard block has no trivial
constituent: its exact hook label is nontrivial. Hence only
\(\Lambda^rU_\rho\) contributes, and
\[
d_{m,k,r}((m))=
\sum_{\rho\vdash k-1,\ \ell(\rho)\le N}
\binom{B_\rho-1}{r}.
\tag{FK.13}
\]
In particular \(d>0\) implies \(r\le k-1\). This also handles
size-one blocks and the orbit with \(j=0\).

### 3. Specified points in the stable-hook polytope

Assume \(d=d_{m,k,r}(\nu)>0\). Choose the parity base
\[
a_0=\begin{cases}2k+1,&a\text{ odd},\\2k+2,&a\text{ even}.
\end{cases}
\]
T062's actual jet surjection at \(a_0\) proves that G037's stable
polytope has at least \(d\) lattice points.

First let \(\nu\ne(m)\). With the notation of HJ.13, its least
numerator degree is
\[
L=b(\nu)+\min_{|S|=r}\sum_{(i,j)\in S}(j-i+1)\ge r+1.
\tag{FK.14}
\]
The inequality is the exact Koszul lowest-degree argument HJ.14.
Each point at degree \(a_0+r\) therefore has total tableau/subset
excess at most \(2k+1\).

Enumerate nonnegative semistandard increments above the row-minimum
filling, of total at most \(2k+1\). Their number is bounded by
\(\binom{m+2k+1}{2k+1}\). Standardize with the proven
left-to-right equal-entry rule and deduplicate. As in T063, this
enumerates every needed standard tableau, because its minimal
semistandard filling has entry sum comajor.

For the retained cell subset, let \(w_0\) be its \(r\)-th smallest
weight. Cells of weight below \(w_0-(2k+1)\) are forced in,
and those above \(w_0+(2k+1)\) are forced out. The middle window
contains at most
\[
(4k+3)(k+1)
\tag{FK.15}
\]
cells by the diagonal bound following (FK.12). Enumerate its
subsets of the required size, discard excess beyond \(2k+1\),
and enumerate the remaining coin partitions, whose degree is
at most \(2k+1\). The empty/full subset endpoints are unique.
Choose the first \(d\) complete valid points in the prescribed
enumeration order. The actual surjection ensures termination.
Increase their weight-two coin coordinate by
\(h=(a-a_0)/2\) to obtain \(d\) distinct points at the requested
degree.

For \(\nu=(m)\), (FK.13) gives \(r\le k-1\), so the parity-base
total degree satisfies \(a_0+r\le3k+1\). Directly enumerate
partitions of that degree into coins \(2,\ldots,\min(m,a_0+r)\).
For each exponent vector \(\beta\), let \(i\) be its least
positive index and enumerate \(r\)-subsets of its other positive
indices. These are exactly G037 HK.19's integer points. Choose
the first \(d\) points.

Their degree transport is explicit even when the least index changes.
Add \(h=(a-a_0)/2\) to \(\beta_2\); when \(h>0\), set the
least-support bit to two, and leave the subset bits unchanged.
The new point satisfies every HK.19 inequality: its subset indices
were larger than the old minimum and hence are larger than two;
their positive exponents remain; the new weight-two exponent is
positive. The map is injective. Subtract the known \(h\) from
\(\beta_2\) to recover the old exponents, recover the old minimum
from those exponents, and keep the unchanged subset. At \(h=0\)
use the identity map. Thus the complete point lists and their
inverses are specified for every outer label.

### 4. Positive cells and precise complexity

Apply the unique-owner deletion procedure HJ.16 to the \(d\)
distinct points. Each step replaces one bounded cell by its
\(2N_{\mathrm{poly}}\) first-difference cells, leaving the others.
The final number is exactly
\(1+d(2N_{\mathrm{poly}}-1)\), bounded by (FK.3).
This gives a literal lattice-set bijection with the stable-hook
polytope minus \(d\) points. The dimension identity is the actual
split jet map T062 and the exact orbit decomposition (FK.8);
these maps establish the requested plethysm coefficient.

For completeness, every complexity assertion follows from the
displayed finite loops. The orbit partition and all nonzero-exponent
blocks in (FK.11) have sizes bounded by \(k\). After their exterior
legs and \(e\) are chosen, the zero-block leg is determined by
\(s_0=r-e-\sum_{b\ne0}s_b\); it is checked against its allowed
range rather than enumerated. Thus the number of exterior choices
depends only on \(k\). Every LR skew shape has
at most \(k\) cells, and its intermediate shapes are selected
from at most \(2^k\) subsets. The target coefficient therefore
takes \(f(k)\operatorname{poly}(m)\) integer operations and has
bit length at most that of \(D_k\). G037 evaluates the stable
term in polynomial bit time in \(m\) and the original degree.
This proves the coefficient/nonvanishing bound.

For the positive matrices, the semistandard increment enumeration
has the stated binomial bound, the subset window has (FK.15)'s
parameter-only size, and the coin degree is bounded by \(2k+1\)
or \(3k+1\). There are at most \(D_k\) deletions. Writing and
checking each full matrix has polynomial cost in its number of
variables and binary parameter lengths. These explicit loops
prove (FK.4), including a computable \(f\), without a hidden
input-dependent precomputation.

The executable fixed_order_hook_positive.py implements exactly these
steps: positive monomial-orbit/exterior/LR correction, bounded-excess
point selection, both degree transports, owner-cell deletion, and
G037's exact coefficient evaluator. It specializes to T061 in the
range \(a\ge3\) and to T063 for \(k=2\). T061's separate valid
\(a=2\) endpoint remains available.

## Proof and computation status

The exact source inputs are T062's checked jet splitting, G037's
checked single-polytope model and binary-degree evaluator, the
actual tensor-induction map HJ.12, and Macdonald's complete
Littlewood–Richardson proof cited above. The author has read every
section and all executable code, checking the all-zero-block case,
the restricted-exterior multiplicities, both point transports and
all complexity bounds. That reading passed. Root and archive have
independently read the complete proof and executable code; both
reviews passed. Archive's exact scope and source rereading are recorded
in `work/archive/FIXED_ORDER_HOOK_REVIEW.md` (A096).

The separate script `check_fixed_order_hook.py` compares with
original permutation-cycle symmetric powers and literal fixed-point
jet induction. For \(m=4,\ldots,9\), \(k=1,\ldots,5\),
every leg and every outer label, all 2,910 jet multiplicities and
11,640 coefficient/parity comparisons passed. The comparison side
uses no monomial-orbit, block-exterior or LR correction formula.
All 3,036 removed-point cases passed the original matrices, including
degrees \(10^{20}+1\). In 58 cases at orders three and four,
10,813 exported cells partitioned 311 original witnesses into 116
retained witnesses and precisely the prescribed points. The receipt
is `FIXED_ORDER_HOOK_RECEIPT.json`.

Rectangular's independent original plethysm computation passed 202
coefficients: order three for outer degrees four and five, first
parts seven and eight, and order four for outer degree four and
first part nine, including both determinant parities and every valid
leg and outer label. Its comparison uses literal complementary
permutation-cycle jets, not the correction labels. The receipt is
`work/rectangular/HIGHER_UNSTABLE_HOOK_MN_CHECK.tsv`.

Whole-proof reviews, source readings and executed comparisons have
separate events in the check ledger.

