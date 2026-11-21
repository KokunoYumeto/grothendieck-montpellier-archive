# Complete audits of G-020 and G-021

Reviewer: GPT-6 Astra Pro, run /root/archive_audit; reasoning setting not exposed.
All statements below concern the actual maps and formulas in the saved reports.
The executed receipts distinguish independent reconstructions from readings of
the authors' proofs.

## A-037. G-020 and its standalone evaluator

**Status: complete proof review PASS.** Read the whole report
work/root/five_point_three_parameter_report.md, TP.1–TP.14, including the
115 exceptional parameter triples, parity rule and endpoint conventions.

The tautological quotient sequence is locally split before tensoring with the
point ideal. Its symmetric-power sequence therefore remains exact after that
tensor product. The scalar cohomology bounds of A-029, together with the
degree-zero and first-power calculations, give the asserted higher-cohomology
vanishing. The exceptional source group at \(k=1,t=0\) is retained in the
Euler class. In particular the resulting trace is the actual trace
\[
h_a h_{2k+t}-h_{a-1}h_{2k+t-1}
-m_1h_{k-1}(h_a-h_{a-1}),
\]
with every \(h_j\) evaluated on the same permutation. The jet factor follows
from the explicit point chart and quotient-bundle trivialization in A-033.

The complementary-column pairing and determinant calculation give the outer
label twist \(\operatorname{sgn}^{d+a}\). The relevant residue polynomials
have degree at most three in \(a\), total degree at most three in \((k,t)\),
and total degree at most five. Thus the 36 stated Newton orders include
every term. The inequalities defining each polytope count exactly one
constant-sized tag and three increasing subsets. The stated support follows
from its complete initial cube and its strictly positive first differences.

### Independent fixed-data reconstruction

The script work/archive/check_three_parameter_analytic.py reconstructs all
96,768,000 fixed coefficients from the seven elementary residue polynomials
for \(h_N(E)\). It applies universal finite-difference matrices to polynomial
coefficients. It does not call the root's cycle recurrence. All seven complete
coefficient-stream hashes, all extrema, all 28 vanishing orders, all 115
zero triples and every remaining positive-order sign agree.

Its seven generating-function checks and fourteen shifted denominator checks
also verify the initial-range polynomial identities. The largest proved
bound for an intermediate signed 64-bit calculation is
22,422,562,560,000. The complete receipt is
work/archive/THREE_PARAMETER_ANALYTIC_RECEIPT.json.

The delegated standard-library evaluator is
work/root/five_point_three_parameter_positive.py. Its validation script is
work/archive/check_three_parameter_evaluator.py. The saved receipt records:

- 245 actual symmetric-group plethysm calculations by Murnaghan–Nakayama;
- 280 specializations to the independently checked G-019 and T-042 tables;
- 460 zero and first-direction checks;
- seven comparisons at parameters with up to 120 decimal digits;
- 63 polytope count cases, 1,053 literal boundary points and 3,651 distinct
  lazy witnesses;
- fourteen witnesses with enormous quotient coordinates, five invalid-input
  cases, and a complete CLI JSON check.

Every check passed. These are executable calculations, with no claim of
proof-assistant formalization.

## A-038. The exact two-row Schur complex

**Status: independent construction and complete proof saved.**
The report work/archive/GENERAL_TWO_ROW_SCHUR_COMPLEX.md specifies the
signed tensor differential, primitive Young idempotent, rational Specht
intertwiners, Frobenius-reciprocity sum and evaluation map that identify its
three terms. It includes every invalid-partition boundary.

The actual local contraction onto the quotient tensor power, averaged over
the symmetric group and restricted to the idempotent, proves locally split
exactness. Tensoring that contraction with the ideal preserves the
homotopy identity. The cohomology spectral sequence has no positive total
degree in the region \(c\ge2k\), including \(k=1,c=2\). This proves the
Euler representation used in G-021. Root and theta separately read this
complete proof and reported their checks; those reports remain their own
events.

## A-039. G-021, all sections including the two outside regions

**Status: complete proof review PASS after the recorded index correction.**
Read all of work/root/five_point_two_row_report.md, TR.1–TR.19,
including every exceptional tuple in §7 and both maps of §8.

### Representation, cohomology and fixed polynomials

For \(a=b+x\) and \(c=2k+t\), the relative-flag complementary pairing is
\[
S_{(a,x)}Q^*
\simeq(\det Q^*)^a\otimes S_{(a,b)}Q.
\]
The equality \(\det Q^*=\det E^*\otimes\mathcal O(-1)\) gives the
twist \(c\) and sign \(\operatorname{sgn}^{d+a}\). The point order is
exactly \(\lambda_2-n=k\). These are the same ordinary ideal powers
proved by the normal-coordinate pullback in G-015.

The exact complex of A-038 and its cohomology proof establish TR.8.
The two negative scalar indices that occur at the boundaries are \(-1,-2\);
each elementary residue polynomial gives zero at both indices. Thus the
residue-polynomial calculation starts at the initial cube without an
eventual-range assumption.

I independently reconstructed every phase polynomial from the different
ambient-section/jet formula
\[
\operatorname{sgn}(g)^a
 s_{(a+c,a,x,0)}(E)(g)
-m_1(g)h_{k-1}(E)(g)\,
 s_{(a,b)}(E-\mathbf1)(g).
\tag{AR.1}
\]
The first term is the actual complementary-column Borel–Weil module.
The second is the actual point-jet quotient from A-033. Its Schur character
uses \(h_j(E-\mathbf1)=h_j(E)-h_{j-1}(E)\). A three-by-three
Jacobi–Trudi determinant computes the first term. Therefore this
reconstruction does not reuse the two-row Euler expansion being tested.

The script work/archive/check_two_row_domination_independent.py verifies
the identity's 122 positive monomials and exact downset; all sixteen
transposition, sixteen double-transposition and eighty-one three-cycle
phase polynomials; and every coefficientwise domination margin for the
34 positive orders of total degree at most three. Its finite-difference
operator is the direct Stirling-number expansion. The minimum constant
margin is 29,260. For the remaining 87 active positive orders, every
nonidentity phase polynomial is killed and the identity has a positive
constant. The complete margin polynomials are retained in
work/archive/TWO_ROW_DOMINATION_INDEPENDENT_RECEIPT.json.

This proves the strict signs of all positive-order constants. The zeroth
constants are actual representation multiplicities. The finite Newton
identity and the four increasing-subset bijections give precisely TR.15
and TR.16, including the eleven-variable bound.

### Exact maps for §8

Under \(\lambda_2+\lambda_3\le2n\), the integers of TR.18 are
nonnegative. For \(\lambda_2>n\),
\[
t=2n-\lambda_2-\lambda_3\ge0;
\]
for \(\lambda_2\le n\), \(k=0\) and \(t=\lambda_2-\lambda_3\).
The reconstructed base inner degree is
\[
d+b+x+k+t=\lambda_2-k=\min(\lambda_2,n)=n-e.
\]
Its last four parts agree with the original partition, and its first
part is \(\lambda_1-5e\). That first part remains at least the
second part by the displayed nonnegative parametrization.

When \(e>0\), the two spaces use the same flag weight \(\tau\), and
both point orders are zero. Their actual inverse-chart maps are
\[
F\longmapsto F(v(X)),\qquad
F\longmapsto u^eF(v(X)).
\]
Here \(u=\prod_iX_{i1}\), exactly as in GF.6 and GF.9. It is fixed
by slot permutations. Multiplication gives an injective polynomial map;
division by \(u^e\) on its image and the same section \(F\) give the
inverse. The G-015 extension criterion proves that both expressions are
polynomial. The audit found the transposed indices \(X_{1i}\) in the
original §8 sentence; root corrected them to \(X_{i1}\), and the
saved statement now uses the actual invariant column product.

For the opposite region, exterior-column multiplication gives the perfect
pairing to \(\det^H\). Its restrictions pair the two indicated balanced
weights. On permutation matrices the target action is
\(\operatorname{sgn}^H\); rational Specht modules are self-dual.
Thus the stated transpose of the outer label is exactly the duality
map's sign, and the transformed inequality is the first region.

### Evaluator verification

The delegated single-file standard-library evaluator is
work/root/five_point_two_row_positive.py. It computes only the active
122 constants from trace indices between \(-2\) and 539, exports the
literal equality and inequality matrices, and enumerates tagged points
lazily. No large table is needed at runtime.

The independently executed script work/archive/check_two_row_evaluator.py
checks:

- the complete 122-element downset;
- 392 genuine Murnaghan–Nakayama plethysm cases;
- 126 G-020 specializations and 140 T-043 hook specializations;
- all 155 listed zeros and all 620 first-direction shifts by sixty;
- seven enormous-parameter comparisons using (AR.1), without residue
  interpolation;
- 63 literal matrix count cases, 3,591 boundary points and 4,264 distinct
  lazy witnesses;
- fourteen huge-quotient witnesses, five invalid-input cases and CLI JSON.

All passed; the receipt is work/archive/TWO_ROW_EVALUATOR_RECEIPT.json.
The root's entire 90,720,000-entry zeroth support stream was not independently
rerun in this event. The proof review checked its role, and the evaluator
check verified every listed exceptional tuple and its propagation.
