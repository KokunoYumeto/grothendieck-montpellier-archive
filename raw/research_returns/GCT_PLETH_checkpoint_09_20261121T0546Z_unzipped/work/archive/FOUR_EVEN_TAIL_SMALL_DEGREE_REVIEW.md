# A-082. Whole-proof review of R042

**Status: PASS.** I read the entire `work/rectangular/four_even_tail_small_inner_degrees.md`, QD.1–QD.12 and all five sections. I also reread the R041 raw-weight identities and expectation table used in its proof. The full cubic extension space, actual canonical scalars and quadratic endpoint pass.

## 1. The row-degree functional

For the three R041 polynomials $P_1,P_2,P_3$, the leading coefficient in a varying original row is a common nonzero polynomial times

$$
\beta=\left(
\frac{a-1}{a^2},
\frac{a^2-3a+m+2}{a^3},
-\frac{(m-1)(2a-m-2)}{2a^3}\right).
$$

I reconstructed these entries from the raw weighted-minor identities, before conversion back to $P_j$. A subset containing the varying row has determinant degree two. The three raw weights have leading coefficients
$(a-1)/a$,
$1-2/a+(m+1)/a^2$,
and $-m/a+m(m+1)/(2a^2)$, each times $v_1^2$.
Using $P_1=A/a$, $P_2=(B-P_1)/a$, $P_3=(C'+P_1)/a$ gives exactly the displayed vector. Subsets omitting the row cannot contribute to degree four.

The common polynomial is nonzero: take the varying direction $e_1$ and choose the other rows $0,e_2,\ldots,e_m$. One affine determinant has nonzero linear coefficient; the sum of its real squares is positive. Every relation among the actual $P_j$ therefore annihilates $\beta$, so this is a well-defined nonzero functional on their finite-row span.

Since all three generators have row degree at most four, the cubic extension space is exactly $\ker\beta$. The pointwise row-degree cancellation proves that
$Q_2=\beta_1P_2-\beta_2P_1$ and
$Q_3=\beta_1P_3-\beta_3P_1$
extend by the actual separate homogenization. The finite relations give $Q_3=-Q_2\ne0$ at $a=m+2$ and both zero at $a=m+1$; above this they are independent. Thus the stated dimension $\min(2,\max(0,a-m-1))$ follows on every valid partition.

## 2. Actual cubic maps

At $m=2$, applying those two combinations to the original independent-row expectation table gives the rows

$$
\left(-\frac{(a-3)^2}{a^3},0,-\frac{2(a-3)}{a^4}\right),
\qquad
\left(\frac{a-3}{a^3},0,\frac{(a-3)(a-2)}{a^4}\right).
$$

The middle entries vanish before a degree-three split form is specialized. Consequently an arbitrary fourth-moment extension makes no change to the evaluation. The exact three-row relations give
$Q=-P_{1;3}/216$ and $T=-P_{1;3}/54$.
Multiplying the displayed rows by $(a)_3$ yields QD.9 and QD.10 exactly. I independently reconstructed both rational scalars, including every sign and denominator.

For $a\ge4$, QD.9 is nonzero. Its target generator is the nonzero centered-simplex generator in the full one-dimensional invariant space, so the scalar reciprocal is an actual preimage. The stated transpose pairing gives rank one for the requested direction. For $m\ge3$, the threefold tensor product supplying the source has at most three rows by the three actual Pieri inclusions, whereas this partition has $m+1\ge4$ rows. The remaining image ranks are therefore zero.

## 3. Quadratic endpoint

The leading-principal-minor product
$\Delta_1^{a-m-3}\Delta_2\Delta_{m+1}$
has the asserted degree and weight. Lower-unitriangular congruence preserves these minors in the chosen coordinate convention. The dense LDL chart and its rational inverse express every highest polynomial of fixed diagonal weight as a scalar multiple of this product, proving uniqueness. The normalized polarization
$a!^{-1}[t_1\cdots t_a]F(\sum t_iv_iv_i^t)$
is the stated actual slot map. Pure squares span the symmetric matrices, so its multilinear restriction is injective.

The requested source lies in the twofold tensor product of one-row representations and therefore has at most two rows. The displayed target has $m+1\ge3$ rows. This proves its image zero and target multiplicity one, with the exact objects and maps given.

## 4. Executed scope

The joint independent script `check_mixed_width_four_symbolic.py` reconstructs the raw top-row functional, both cubic expectation rows and both scalars by exact rational arithmetic. Its receipt is `MIXED_WIDTH_FOUR_SYMBOLIC_RECEIPT.json`. It imports no source implementation. The original 56 literal pairings and 27 target/source coefficient comparisons are read and attributed to the source report; they were not rerun in this audit.
