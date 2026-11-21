# F35 proposal: an actual Artin-stack realization of the F26 word-trace sequence

Author/checker: `/root/grothendieck_dictionary`, GPT-6 Astra Pro; effort not exposed. Date: 21 November 2026 UTC.

**Result:** the proposed stack realizes the complete all-extension scalar sequence. Its actual compactly supported cohomology is explicitly computable, unbounded below, and absolutely convergent for geometric-Frobenius traces. Poincaré duality exists but carries its compact spectrum to an unbounded ordinary spectrum. The construction does not supply the nonstandard algebra action, its correspondences, or its designated basis.

## 1. A finite-type stack, with exact mass

For a fixed finite field \(\mathbb F_q\), let
\[
U=\mathbb A^6\times\mathbb G_m^8,
\quad G=(\mathrm{GL}_2)^4,
\quad \mathcal Y=[U/G]=U\times(B\mathrm{GL}_2)^4,
\tag{ST1}
\]
where the action on \(U\) is trivial. Set
\[
\mathcal X=
\coprod_{a=1}^{24}\operatorname{Spec}\mathbb F_q
\ \sqcup\ \coprod_{b=1}^{16}\mathcal Y.
\tag{ST2}
\]
These are finite-type Artin stacks with affine stabilizers. The atlas \(U\to\mathcal Y\) is smooth of relative dimension 16, while \(\dim U=14\); thus \(\mathcal Y\) is smooth of dimension \(-2\). The whole \(\mathcal X\) is not equidimensional: its components have dimensions zero and minus two, and its dimension is zero.

For \(Q=q^n\), every \(\mathrm{GL}_2\)-torsor over \(\mathbb F_Q\) is trivial: it is the frame torsor of a two-dimensional vector space, and every such space has a basis. Each \(U(\mathbb F_Q)\) point therefore contributes mass \(1/|G(\mathbb F_Q)|\). Counting ordered linearly independent columns gives
\[
|\mathrm{GL}_2(\mathbb F_Q)|=(Q^2-1)(Q^2-Q)
=Q(Q-1)^2(Q+1).
\]
It follows directly that
\[
\#\mathcal Y(\mathbb F_Q)
=\frac{Q^6(Q-1)^8}{Q^4(Q-1)^8(Q+1)^4}
=\frac{Q^2}{(Q+1)^4},
\quad
\#\mathcal X(\mathbb F_Q)
=24+\frac{16Q^2}{(Q+1)^4}=h_n.
\tag{ST3}
\]
The symbol \(\#\) denotes groupoid mass, the sum of reciprocal automorphism-group orders. It is allowed to be rational. This is one fixed stack over \(\mathbb F_q\) for all \(n\), rather than a separate object chosen at each extension degree.

## 2. Primary stack formalism, with hypotheses

The exact primary source for the trace assertion is Shenghao Sun, *L-series of Artin stacks over finite fields*, **Algebra & Number Theory 6 (2012), 47--122**:

- **Theorem 1.1, p.49:** for a finite-type Artin stack over \(\mathbb F_q\), the compact-support alternating geometric-Frobenius trace converges absolutely after a fixed \(\iota:\overline{\mathbb Q}_\ell\cong\mathbb C\), and equals groupoid mass.
- **Definition 4.1, p.84, and Theorem 4.2, p.85:** the more precise convergence condition sums the absolute values of all eigenvalues to every positive real power; finite-type pushforward with compact supports preserves convergence for bounded-above, geometrically stratifiable, \(\iota\)-mixed convergent Weil complexes. The constant sheaf here is bounded, pure of weight zero, and stratifiable, so these hypotheses hold.
- **Example 7.4, p.109:** the actual nonzero groups of \(B\mathrm{GL}_2\) are
  \[
  H_c^{-8-2s}(B\mathrm{GL}_{2,\overline{\mathbb F}_q},\mathbb Q_\ell)
  \simeq\mathbb Q_\ell(s+4)^{\oplus(\lfloor s/2\rfloor+1)},\qquad s\ge0.
  \tag{ST4}
  \]
- **Theorem 4.8 and §4.8.2, pp.89--90:** the ordinary polynomial cohomology of a classifying stack, and the corresponding compact-support spectrum by duality. **Theorem 1.4, p.50**, gives weight bounds; for affine stabilizers the weights of \(H_c^i\) of a punctual weight-zero sheaf are at most \(i\).

Official PDF: <https://msp.org/ant/2012/6-1/ant-v6-n1-p03-s.pdf>. Read primary web refs: `turn788663389view0` (Example7.4), `turn788663389view1` (Definition4.1), `turn788663389view2` (4.7--4.8.2), `turn849581071view0`; local PDF/text `primary_sources/Sun_L_series_2012.*`. Published statements and their hypotheses were inspected; the full general trace-theorem proof is not claimed reproved here.

For the operations themselves, the published Laszlo--Olsson, *The six operations for sheaves on Artin stacks II: Adic coefficients*, **Publ. Math. IHÉS 107 (2008), 169--210**, was inspected at **§9.1 and Lemmas9.1.1--9.1.2, p.198** (duality and smooth pullback), and **Theorem11.0.14, p.204** (Künneth for finite-type morphisms and bounded-above constructible inputs). Its base is affine excellent finite-dimensional, with \(\ell\) invertible and finite \(\ell\)-cohomological dimension for finite-type base schemes; the finite-field base satisfies these hypotheses. Its convention is \(K\langle d\rangle=K(d)[2d]\). Official primary PDF: <https://numdam.org/item/10.1007/s10240-008-0012-5.pdf>; refs `turn239553085view0`--`turn239553085view3`, `turn494473952view0`.

## 3. Actual graded cohomology

Write
\[
\sum_{s\ge0}a_s z^s=\frac1{(1-z)^4(1-z^2)^4}.
\tag{ST5}
\]
Thus \(a_s\) counts monomials of weighted degree \(s\) in four variables of weight one and four of weight two, and is a positive integer for every \(s\ge0\). The usual classifying-stack presentation is
\[
H^*(B\mathrm{GL}_2)=\mathbb Q_\ell[c_1,c_2],
\quad \deg c_i=2i,\quad c_i\text{ spans }\mathbb Q_\ell(-i).
\]
The classes are Chern classes defined over the base field. This agrees with (ST4) and the Borel presentation in Sun4.8. Ordinary cohomology of \(\mathbb A^6\) is the unit, and that of \(\mathbb G_m^8\) is the exterior algebra on eight copies of \(\mathbb Q_\ell(-1)\) in degree one. Hence Künneth gives
\[
H^i(\mathcal Y)=
\bigoplus_{\substack{0\le b\le8,\ s\ge0\\ i=b+2s}}
\mathbb Q_\ell(-(b+s))^{\oplus\binom8b a_s}.
\tag{ST6}
\]
All cohomology is over \(\overline{\mathbb F}_q\) with the displayed arithmetic Weil structure. The direct sum in a fixed degree is finite.

For a direct compact-support derivation, \(H_c^{12}(\mathbb A^6)=\mathbb Q_\ell(-6)\), and
\[
H_c^{16-b}(\mathbb G_m^8)=
\mathbb Q_\ell(-(8-b))^{\oplus\binom8b}.
\]
Four uses of (ST4) give
\(H_c^{-32-2s}((B\mathrm{GL}_2)^4)=\mathbb Q_\ell(s+16)^{\oplus a_s}\).
The compact-support Künneth theorem therefore yields the actual decomposition
\[
H_c^j(\mathcal Y)=
\bigoplus_{\substack{0\le b\le8,\ s\ge0\\j=-4-b-2s}}
\mathbb Q_\ell(b+s+2)^{\oplus\binom8b a_s}.
\tag{ST7}
\]
This proves directly that compact cohomology is nonzero in arbitrarily negative degrees. Its summand indexed by \((b,s)\) has Frobenius eigenvalue \(q^{-(b+s+2)}\) and weight \(-2(b+s+2)=j-b\), in agreement with the affine-stabilizer weight bound. Even a fixed degree can be mixed: \(H_c^{-6}\) contains \(\mathbb Q_\ell(3)^4\) and \(\mathbb Q_\ell(4)^{28}\).

## 4. Convergence, visible cancellations, and F32

Put \(x=q^{-n}\), so \(0<x<1\). The sign of a term in (ST7) is \((-1)^j=(-1)^b\). Its Euler series is therefore
\[
\sum_j(-1)^j\operatorname{Tr}(F^n\mid H_c^j(\mathcal Y))
=x^2\frac{(1-x)^8}{(1-x)^4(1-x^2)^4}
=\frac{x^2}{(1+x)^4}.
\tag{ST8}
\]
This agrees with the direct mass calculation (ST3). The corresponding ungrouped absolute eigenvalue sum at any positive real moment \(t\) is
\[
\sum_{b,s}\binom8b a_s q^{-t(b+s+2)}
=\frac{q^{-2t}(1+q^{-t})^8}
 {(1-q^{-t})^4(1-q^{-2t})^4}
=\frac{q^{-2t}(1+q^{-t})^4}{(1-q^{-t})^8}<\infty.
\tag{ST9}
\]
Thus regrouping by eigenvalues is justified absolutely, not formally alone. At the root \(q^{-(j+2)}\) the grouped Euler multiplicity is
\[
\sum_{b=0}^{\min(8,j)}(-1)^b\binom8b a_{j-b}
=(-1)^j\binom{j+3}{3}.
\tag{ST10}
\]
For example the root \(q^{-3}\) occurs with actual multiplicity four in degree \(-6\) and eight in degree \(-5\), so its visible Euler coefficient is \(4-8=-4\). These are cancellations between actual cohomology groups; no vector space of negative dimension is used.

For \(\mathcal X\), the unique admissible visible spectrum in the sense of F32 is consequently
\[
(1,24),\qquad
\left(q^{-(j+2)},16(-1)^j\binom{j+3}{3}\right),\quad j\ge0.
\tag{ST11}
\]
The support is bounded, discrete away from zero, and has the required convergent absolute moments by (ST9). F32's uniqueness therefore applies within precisely its stated class; the construction does not use uniqueness for regularized spectra. It realizes exactly the completion already displayed there, while the explicit unbounded cohomology explains why it does not contradict F26's finite-spectrum obstruction.

## 5. Actual Poincaré duality, and the missing dual bound

The smooth stack \(\mathcal Y\) has dimension \(-2\), so its dualizing complex is \(\mathbb Q_\ell(-2)[-4]\), and duality gives
\[
H_c^{-4-i}(\mathcal Y)
\simeq H^i(\mathcal Y)^\vee(2).
\tag{ST12}
\]
Equations (ST6)--(ST7) verify this term by term. In the pairing to \(\mathbb Q_\ell(2)\), a compact eigenvalue \(\alpha=q^{-(b+s+2)}\) is paired with ordinary eigenvalue
\[
\beta=q^{-2}/\alpha=q^{b+s}.
\]
Thus the actual ordinary spectrum is unbounded. After visible Euler grouping its roots are \(q^j\), with nonzero coefficients \((-1)^j\binom{j+3}{3}\), so no hidden cancellation makes that visible support bounded. The corresponding positive-geometric-Frobenius ordinary trace series is not convergent: its terms do not tend to zero. Equivalently the linear dual of the compact complex has the unbounded reciprocal eigenvalues \(q^{j+2}\).

There is therefore a genuine geometric duality here, but its dual object does not satisfy the independent bounded-spectrum upper-bound premise of F17/F32. Their two-sided purity conclusion is unavailable. The whole disjoint union \(\mathcal X\) has different dimensional components, so no common dimension-minus-two Tate pairing is asserted for it; its Verdier dual is computed component by component. For any fixed nonzero reciprocal factor, its full visible reciprocal support is still unbounded, exactly as F32 predicts.

## 6. Precise progress and remaining comparison

This closes one narrowly specified existence question: the actual normalized F26 scalar word-trace sequence, with the formal parameter evaluated extension by extension, is the constant-sheaf Frobenius Euler trace of an explicit finite-type Artin stack. Finite type for stacks permits the unbounded compact cohomology displayed above. The ordinary SGA scheme theory alone is extended here by the explicitly cited Laszlo--Olsson/Sun stack formalism.

It does not construct geometric operators representing the nonstandard generators or their products. In particular a geometric identity for the single number \(\operatorname{Tr}(e_1e_2)\) supplies no action, no simultaneous realization of all words, no convolution compatibility, no canonical basis, and no tensor-path output sign. The mixed weights and loss of a bounded visible reciprocal system are proved features of this specific model, not a no-go theorem against every stack or completed realization.

**Author check:** all stack dimensions, mass factors, cohomological degrees and Tate twists, absolute convergence, grouped signs, and duality normalizations were derived above and checked. The full F32 note was read before using its uniqueness/duality scope. General primary theorems are invoked with checked hypotheses, not claimed reproved. A fresh independent review of this report should precede the generated F35 fragment.
