# A-081. Whole-proof audit of the complete outer-five formula G036

**Status: PASS.** I read the entire saved `work/root/complete_outer_five_report.md`, CF.1–CF.10 and all six sections, and every line of `work/root/outer_five_positive.py`. The actual representation transports, exhaustive route, zero conventions and fixed positive-description and evaluation bounds all pass.

This audit uses the already completed independent checks of G021, G033/G034, G035 and T058/T059. In particular A079 and A080 establish both remaining normalized regions by complete independent phase reconstruction and whole-proof review. No new coefficient sampling is needed to prove this final routing step.

## 1. Original module and zero cases

The exact tensor-word, Cauchy and Young maps identify the requested coefficient with the multiplicity of $[\mu]$ in
$(S_\lambda\mathbb Q^5)_{(n,n,n,n,n)}$.
The actual permutation-matrix action is retained. The outer Schur projector is a rational idempotent on the tensor power; the component therefore occurs only among shapes produced by five successive horizontal strips. Such a strip cannot add two new first-column boxes, proving the asserted length-greater-than-five zero.

At $n=0$, the balanced space is the trivial line, which gives multiplicity one for $(5)$ and zero for the other labels. The implementation sends this input to the order-zero bulk formula and uses the same convention. It validates nonnegative decreasing integer rows, divisibility of the size by five and the outer partition.

## 2. Stable multiplication

For raw order $k=\lambda_2-n\le0$, the exact stable-chart map is multiplication by $u^{-k}$, where $u$ is the product of the five first-column coordinates. Its row weight is $(1^5)$, its right weight is $(5,0,0,0,0)$, and its permutation action is invariant. The proved normal-order extension of the inverse division map gives an actual module isomorphism.

The resulting partition has degree $5\lambda_2$ and first gap
$3\lambda_2-\lambda_3-\lambda_4-\lambda_5\ge0$.
Thus the stable removal remains inside partitions, has order zero and introduces no sign. The code computes precisely this nonnegative stable power.

## 3. Complement, determinant sign and the normalized inequalities

The perfect exterior-column pairings and rational Young projections give
$B_{\lambda^c,H-n}\simeq B_{\lambda,n}^*\otimes\operatorname{sgn}^H$,
where $H=\lambda_1$ and
$\lambda^c=(H-\lambda_5,\ldots,H-\lambda_1)$.
An invariant positive rational Gram form and its inverse identify the dual with the original rational finite-group module. The row/column Young comparison identifies sign tensoring with transposition of the Specht label. Hence the program's transposition precisely when $H$ is odd is the required transport.

For the physical parameters in CF.4, direct substitution gives

$$
x^c=2b+x+3c-5k,\qquad b^c=c,\qquad c^c=b,\qquad
k^c_{\rm raw}=b+c-k,\qquad d^c=0.
$$

The code complements exactly for $k>0$ and $b+c-k<k$.
Without complement this decision gives $b+c\ge2k$.
With complement and positive new order, the old strict inequality gives
$b+c>2(b+c-k)$.
With nonpositive new order, the stable map gives order zero.
The final first gap is nonnegative because both operations preserve the actual partition; at negative complementary raw order the explicit gap is

$$
x-5(k-b-c)=(2b+x+3c-5k)+3b+2c\ge0.
$$

Only one complement and one stable removal are performed. There is no iterative reduction argument or unstated termination requirement.

I independently reconstructed eight algebraic identities in this dictionary, including both degree equalities, all four complement parameters and both stable endpoint gaps. They pass exactly in symbolic rational arithmetic. The executed receipt is `OUTER_FIVE_NORMALIZATION_SYMBOLIC_RECEIPT.json`.

## 4. Exhaustive positive providers

After the exact maps, the parameters satisfy
$k\ge0$, $b+c\ge2k$, $2b+x+3c\ge5k$.
The three decisions are disjoint and exhaustive:

| Range | Provider | Maximum tags | Maximum integer variables |
|---|---|---:|---:|
| $c\ge2k$ | G021 with twist parameter $c-2k$ | 122 | 11 |
| $k\le c<2k$ | T059 | 151 | 11 |
| $c<k$ | G035 | 152 | 11 |

The first includes every order-zero case. The second has the exact nonnegative inverse
$(x,b-2k+c,2k-c-1,c-k)$.
The third is exactly A079's independently checked fourteen-branch domain. Thus every original coefficient is covered by a previously proved positive formula.

The selector and increasing-subset maps in each provider give literal bijections with the displayed bounded-polytope points. The finite outer tag separates the selected summands. Each fixed constant is an integer. Positive-order nonnegativity follows from the checked domination polynomials; zero-order nonnegativity follows from the actual finite representation whose trace was evaluated. This does not require a large residue-cube computation.

## 5. Description size and bit complexity

The number of affine substitutions and decisions is fixed. The original partition has at most five retained rows, each at most $5n$. Complement height and complementary degree are at most $5n$; stable removal only decreases the first row and inner degree. All physical parameters and provider coordinates are fixed affine expressions in these bounded quantities.

All residue moduli, phase polynomials, Newton downsets and class tables are fixed data. Every fixed difference constant is evaluated at a bounded residue plus a bounded multiple of 60. No summation length in this operation depends on the original inner degree. Each selected Newton term uses binomial coefficients of bounded order, with total order at most six. Their arguments have $O(\log(n+2))$ bits, and each can be computed by a fixed product and exact division.

There are at most 152 terms. Each polytope has at most eleven integer variables, fixed coefficient matrices, and bounds with polynomial binary description length. The coefficient calculation consequently uses a fixed number of operations on polynomial-bit-length integers. The theorem's fixed-outer-degree bounds follow. The separate varying-outer-degree efficiency gate is not asserted to have been solved.

## 6. Code and audit scope

The public router implements the exact complement test, determinant transpose, stable power and physical dictionary just checked. Its shape assertion is CF.5, and its two normalized inequalities are CF.9. Its bulk, high and below calls use the correct argument ordering. The physical entry point first builds the original partition and then uses the same complete route. Overlength inputs return zero and an empty polytope union.

The parent routing receipt records 1,708 coefficient comparisons at 244 original partitions, all sixteen concrete provider branches and 112 provider exports. I read that receipt but did not rerun its coefficient sampling. The underlying independent whole-proof, phase, support and evaluator checks are the separately logged archive events; the new computation here is the eight-identity symbolic dictionary check.

The scheme, Schur-operation and associated-sheaf discussion retains the integral objects and explicit rational generic-fiber projectors with their denominators. The comparison uses the already checked EGA/SGA locators and the same actual tensor, normal, Young, exterior and lattice-point maps throughout. No additional assertion about unspecified residue-characteristic multiplicities enters this theorem.
