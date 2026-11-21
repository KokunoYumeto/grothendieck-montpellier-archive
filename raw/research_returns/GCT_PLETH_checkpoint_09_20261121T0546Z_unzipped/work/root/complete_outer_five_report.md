# A complete fixed positive formula in outer degree five

## G-036. Every Schur plethysm coefficient with outer size five

For every \(n\ge0\), every \(\mu\vdash5\), and every partition
\(\lambda\vdash5n\), the coefficient
\[
p_{\mu,(n)}^\lambda
=[S_\lambda V:S_\mu(\operatorname{Sym}^n V)]
\tag{CF.1}
\]
has an explicit positive formula using at most152 selected bounded
rational polytopes, each with at most eleven integer variables.
All matrices, constants, residue rules and branch maps are fixed
and specified by the constructions below. Their description sizes
are polynomial in the binary input length. The coefficient itself
is evaluated by a fixed number of arithmetic operations and
binomial coefficients of order at most six, hence in polynomial
bit complexity.

The statement applies in every ambient dimension at least the
length of \(\lambda\); the usual Schur dimension zeros apply in
smaller dimensions. It includes every outer label and every
determinant parity. The full support was already determined in
G031; the present theorem gives the positive value of every
coefficient, including the previously remaining interior regions.
No general elimination, character summation of input-dependent
length, or uncomputed cohomology rank occurs in its evaluator.

## 1. The actual balanced module and the length-zero cases

The exact Cauchy and tensor-word maps of G015 identify (CF.1)
with the multiplicity of the Specht module \([\mu]\) in
\[
B_{\lambda,n}=(S_\lambda\mathbb Q^5)_{(n,n,n,n,n)},
\tag{CF.2}
\]
with its actual action by permutation matrices. The rational
Young projector specifies the outer Schur summand. These are
the same maps used in G027/T049 and every formula below.

For \(\ell(\lambda)>5\) the coefficient is zero. Indeed the
actual idempotent image \(S_\mu(\operatorname{Sym}^n V)\)
is a summand of \((\operatorname{Sym}^nV)^{\otimes5}\).
Successive one-row Pieri inclusions add five horizontal strips.
Each strip can create at most one new row: two new rows would
both add a box in their first column, contrary to horizontality.
Thus no Young component with more than five rows occurs.
Its positive formula is the empty disjoint union.

For every other partition, pad by zeros to five rows. At
\(n=0\), (CF.2) is the trivial line; its multiplicity is one
for \(\mu=(5)\) and zero for the other six labels. This also
agrees with the formulas below.

## 2. Stable first-row removal through its exact section map

Initially put \(k_{\rm raw}=\lambda_2-n\). For
\(k_{\rm raw}\le0\), let
\[
e=n-\lambda_2,\qquad n^0=n-e=\lambda_2,\qquad
\lambda^0=(\lambda_1-5e,\lambda_2,\lambda_3,\lambda_4,\lambda_5).
\tag{CF.3}
\]
The first gap is
\[
\lambda^0_1-\lambda_2
=3\lambda_2-\lambda_3-\lambda_4-\lambda_5\ge0,
\]
so \(\lambda^0\) is a valid partition of \(5n^0\).
T032's stable-chart map is multiplication by \(u^e\), where
\(u\) is the product of the five first-column coordinates.
It is invariant under \(S_5\), adds \(5e\) to the first
right weight and \(e\) to each row weight, and identifies
\(B_{\lambda^0,n^0}\) with \(B_{\lambda,n}\).
The inverse is division by \(u^e\); T032's proved balanced
normal-order statement establishes its polynomial extension.
Thus this step retains the exact module and outer label.

The resulting order is zero and G021 applies. For positive
initial order, use the following complementary-column map when
needed, then apply (CF.3) to that partition only when its raw
order is negative. This requires at most one complement and
one stable removal.

## 3. The determinant complement and the normalized order

For a five-row partition put
\[
d=\lambda_5,\quad x=\lambda_4-\lambda_5,\quad
b=\lambda_3-\lambda_4,\quad c=\lambda_2-\lambda_3,
\quad k=\lambda_2-n.
\tag{CF.4}
\]
At \(k\ge0\), the weight sum gives exactly
\[
\begin{aligned}
n&=d+b+x+c-k,\\
\lambda&=(d+3b+2x+4c-5k,d+b+x+c,d+b+x,d+x,d),\\
g:=\lambda_1-\lambda_2&=2b+x+3c-5k\ge0.
\end{aligned}
\tag{CF.5}
\]

Take \(H=\lambda_1\) and
\[
\lambda^c=(H-\lambda_5,H-\lambda_4,H-\lambda_3,
H-\lambda_2,0),\qquad n^c=H-n.
\tag{CF.6}
\]
The exterior-column perfect pairing
\(\Lambda^jE\otimes\Lambda^{5-j}E\to\det E\),
followed by the rational Young projections, gives
\[
B_{\lambda^c,n^c}
\simeq (B_{\lambda,n})^*\otimes\operatorname{sgn}^H.
\tag{CF.7}
\]
Its maps and determinant sign are those proved in G015 and
used explicitly in G033/G034. To identify a rational finite
group module with its dual, average the positive rational
tensor dot product over \(S_5\) and use its nonsingular Gram
matrix and inverse. Thus duality in (CF.7) is an actual
equivariant isomorphism. Tensoring a Specht module with sign
is the column/row Young comparison \([\mu]\otimes\operatorname{sgn}
\simeq[\mu']\). Consequently the outer label is transposed
exactly when \(H\) is odd.

Direct substitution in (CF.4) gives the complete new dictionary:
\[
x^c=g,\quad b^c=c,\quad c^c=b,\quad d^c=0,
\qquad k^c_{\rm raw}=b+c-k.
\tag{CF.8}
\]
For positive initial \(k\), take the complement exactly when
\(b+c-k<k\). Its order after the proved stable removal is
\[
k^c=\max(0,b+c-k).
\]
For a negative complementary raw order the removed stable power
is \(e=k-b-c\). The complementary first-row gap after removal
is
\[
x-5e=g+3b+2c\ge0,
\]
which explicitly checks the endpoint partition. Its outer label
is the one already specified by (CF.7), with no additional sign.

After this single decision the retained parameters always satisfy
\[
k\ge0,\qquad b+c\ge2k,
\qquad2b+x+3c\ge5k.
\tag{CF.9}
\]
Without complement, the decision inequality is exactly
\(b+c\ge2k\). With complement and positive new order,
the old strict inequality gives
\(b+c>2(b+c-k)\). At new order zero the inequality is
automatic. All maps have been specified, so (CF.9) is a
normalization of the actual multiplicity through (CF.3) and
(CF.7), including all signs and boundary cases.

## 4. Three exhaustive positive-formula providers

On the domain (CF.9), use the following disjoint decisions:

| Parameter range | Exact provider | Maximum selected polytopes | Maximum variables |
|---|---|---:|---:|
| c≥2k | G021, with delta=c−2k | 122 | 11 |
| k≤c<2k | T059, HT1–12 | 151 | 11 |
| c<k | G035, NB1–15 | 152 | 11 |

These alternatives exhaust every nonnegative \(c,k\).
The first includes \(k=0\). The second has exactly the inverse
parameters
\[
(X,B,K,U)=(x,b-2k+c,2k-c-1,c-k),
\]
all nonnegative by (CF.9) and its stated range. The third is
precisely G035's domain. G035's explicit lower-cone, strip and
small-order inverses exhaust it; its \(c=0,1\) providers are
the completed whole-wall formulas G033/G034. Thus no additional
region or limiting case is left to evaluate.

Each provider proves an exact formula
\[
\sum_{\delta\in\mathcal D}
D_{\nu,r,\delta}\prod_i\binom{q_i}{\delta_i},
\qquad D_{\nu,r,\delta}\in\mathbb Z_{\ge0},
\tag{CF.10}
\]
with its residue rules, literal integer matrices and a bijection
between each summand and its selector/increasing-subset choices.
G021 also fixes every bounded coefficient explicitly. The
positive-order constants in T059/G035 follow from their complete
rational domination certificates; their zero-order constants
are multiplicities of the actual normal module. The entire
construction therefore has proved nonnegative constants.
The largest selected tag count is152 and the largest variable
count is eleven, as in the table.

The parameter changes (CF.3)–(CF.8) and all inverse branch maps
use affine integer expressions, parity, inequalities and maximum
with zero. Each parameter is bounded by a fixed multiple of
\(n+1\). Each Newton order is at most six in total, and all
fixed evaluation arguments are bounded constants. Arithmetic
on these expressions and binomial coefficients consequently
has polynomial bit complexity in the binary input length.
Every polytope witness has at most eleven integer coordinates
and a polynomial bit length, with fixed linear constraint data.
This proves both the positive-description assertion and the
stated exact evaluation bound.

## 5. Executable realization and independent checks

`outer_five_positive.py` accepts an original partition and outer
label. Its `partition_route` records the original degree, the
complement decision and height, the stable power, the normalized
partition, all six physical arguments, and the selected provider.
For a G035 branch it also returns its exact lower-region decision.
`coefficient_partition` evaluates the positive formula, and
`partition_polytopes` exports the corresponding literal matrices.
The same module exposes a physical-parameter entry point without
requiring the caller to normalize first.

The zero-length and degree-zero conventions are explicit. The
program validates partition order and nonnegativity, divisibility
of its size by five, and the outer label. It asserts the exact
shape identity (CF.5) and both inequalities in (CF.9) after the
actual transports. The finite provider computations use the
fixed rational data; they do not call a general plethysm oracle.

The separate checker `check_outer_five_positive.py` compares the
output against the original balanced cycle/Pieri calculation at
original partition inputs. Its cases cover all three top-level
providers, every G035 boundary, both lower cones, both entire
small-twist walls, determinant shifts, complementary partitions
and first-row extensions. It also checks exported provider
bounds, all seven overlength zeros and all seven degree-zero
values. The exact counts and outcomes are saved in
`OUTER_FIVE_POSITIVE_ROUTING_RECEIPT.json`. The whole-proof
readings and independent certificate reconstructions underlying
G021, G033–G035 and T058–T059 are recorded separately.

## 6. Grothendieck dictionary and the exact remaining uniform gate

The input is the Schur-operation class of
\(S_\mu(\operatorname{Sym}^n\mathcal V)\) on a locally free
sheaf. The integral tensor and Schur constructions define its
scheme-theoretic object over \(\mathbb Z\); the multiplicity
statement is taken on the characteristic-zero generic fiber.
The rational Young and Gram projectors have their explicit
finite matrices and denominators. They spread over the
corresponding localized integral base. No assertion about
constant multiplicity across unspecified residue characteristics
is used.

The tensor-word and weight maps identify its generic-fiber
representation class with (CF.2). Stable multiplication and the
perfect exterior-column pairing are the actual arrows (CF.3)
and (CF.7). G027/T049 then gives the exact coherent section
module, its oriented quotient complex and its normal Young
extraction. T058/G035/T059 specify every singleton, pair and
triple comparison and every finite coefficient reindexing.
The selector/subset maps in (CF.10) are literal finite-set
bijections with the displayed lattice points. Thus each stage
has its exact comparison, retaining the original Schur class.

The coordinate/Proj and section maps have the EGA II2.4.1–2.4.2
and2.5.2/2.5.4 locators; the frame and comodule maps are
SGA3 I4.5/4.7.2–4.7.3; the representation-to-associated-sheaf
K0 morphism is SGA6 VI3.3. The λ and Schur operations are
SGA6 V4.2,4.4,4.8–4.9. Cote133/028 is carried by A012's
explicit tensor-word, torus-weight and Young maps. These are
the same proved dictionaries used by the component formulas,
now joined by the complete determinant/stable routing.

The remaining positive-description gate is uniformity in a
varying outer degree. G009–G011 supply the actual finite
algebra maps and terminating positive counts there; the
polynomial bounds on their Hilbert bases, Reynolds lists and
elimination remain the stated gate. The present fixed-outer
theorem closes the full outer-five coefficient row and leaves
that exact varying-degree requirement explicitly recorded.
