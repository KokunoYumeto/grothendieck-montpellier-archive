# A-073. Independent audit of the remaining upper strip T-056

**Status: PASS.** Reviewer: GPT-6 Astra Pro; effort not exposed; run
/root/archive_audit. The complete OS.1–OS.6 proof, all four sections,
the substitution constructor/evaluator and the residue checker were
read. A-072 records the underlying rank-three pair-map audit.

## Exact extension to the strip

Here $b=3k-4$, $k\ge5$, $a=b+x$, $x\ge0$. The actual partition
has first gap $k-5+x\ge0$, and the normal degree is
$N=2b+x+3\ge5k$. Terms with at least four selected directions
vanish by the same exact quotient-degree bound as T055.

For a three-point term, the remaining standard module is a line.
The skew factor for outer $(a+1,b+1,1)$ requires both
$\rho_1\ge b+1$ and $\rho_2\ge1$. Consequently

$$
|\rho|\ge b+2=3k-2>3(k-1),
$$

which exceeds the selected normal polynomial's degree. This is the
correct endpoint argument: the inequality on $\rho_1$ alone would
give equality with the available bound.

The singleton interlacing and exact involution require $b\ge k-1$,
which holds. The pair comparison requires
$p\le2(k-1)<b+1=3k-3$, which also holds throughout the range.
Its contraction sequence, the $p=q$ and $p=0$ endpoints, and the
interchanged-pair trace remain the actual maps reviewed in A-072.
The determinant line remains $\operatorname{sgn}^{d+b+x+1}$.
Thus the exact restriction trace extends to this strip before the
polynomial substitution is made.

## Substitution, differences and support

With $X=x$ and $K=k-5$, the substitution is precisely

$$
(X_{\mathrm{old}},B_{\mathrm{old}},K_{\mathrm{old}})
=(X,-1,K+2).
$$

The physical residues are those of
$a=3K+11+X$, $b=3K+11$, $k=K+5$, exactly as the evaluator
uses. The triangles have orders $k$ and $k-1\ge4$, so the initial
phase identities hold. The substitution therefore gives the actual
characters on the complete nonnegative orthant.

The identity polynomial OS.4 agrees with the reconstructed data,
including every coefficient. Its 17-element order downset is OS.5.
All 16 nonzero differences have coefficientwise nonnegative
character-triangle margins and strictly positive constants. The five
printed nontrivial comparisons are correct; the minimum constant
over all orders is **6,450,290**. The remaining orders use only
the positive identity polynomial. All omitted orders vanish.

The exact Newton identity and the two increasing-subset chains give
the positive count. Deleting the redundant $q_B=0$ coordinate and
its equality is a specified bijection to the eight-variable version.
With that coordinate retained, the implemented matrices have at most
nine variables. The selector has exactly the difference constant
many choices.

All **25,200** order-zero base coefficients are positive. Their origin
vector is $(1,2,3,2,3,2,1)$. The positive first differences prove
positivity throughout the strip. The low-order routing statement
also checks: $3k-4\le2k+1$ for $k\le5$, so those possible strip
endpoints are already covered by the stated complementary branch.

## Independent executed checks

The T055 polynomials were independently reconstructed from the
unexpanded rank-three normal traces as detailed in A-072. All
**449** exact strip phases obtained by the displayed substitution
agree with the saved data. Repeated literal step-60 translations
recover all **16** complete margin polynomials.

The full **25,200**-entry base box was recomputed with Python
unbounded integers. All seven minima, maxima, origin values and
empty zero sets agree, and the original combined representation-based
SHA-256 digest is reproduced. In addition, **140** literal rank-three
normal traces on twenty strip points independently agree with the
substituted phases, separately checking actual values on the strip.

The evaluator audit checks all five printed margin rows, **98**
coefficients with both determinant parities at seven parameter pairs,
**1,666** literal matrix systems, and **1,396** witnesses. All pass.
The shared receipts are ONE_TWIST_INDEPENDENT_RECEIPT.json and
ONE_TWIST_EVALUATOR_RECEIPT.json; their executable reconstructions
are check_one_twist_independent.py and check_one_twist_evaluator.py.
