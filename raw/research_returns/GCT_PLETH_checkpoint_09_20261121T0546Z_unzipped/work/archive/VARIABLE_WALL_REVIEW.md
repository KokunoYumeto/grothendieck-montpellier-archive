# A068 — enlarged variable-order wall: full proof and independent reconstruction

Reviewed by GPT-6 Astra Pro, effort setting not exposed, run `/root/archive_audit`, on 2026-11-21 UTC. I read the complete final T054 report `work/theta/outer5/variable_wall/variable_wall_report.md`, VW.1–VW.15, and its polynomial, residue, and positive-evaluator implementations. **PASS** for the enlarged chamber \(k\ge3,\ x\ge0,\ b\ge3k-2,\ 2b+x\ge5k\).

Independent reconstruction passed all **449 phase polynomials**, all **45 coefficientwise difference margins**, and all **1,512,000 zeroth-residue constants**. It agrees with both the directly regenerated theta data and the root's independently transformed data. The proof and computations are recorded separately below.

## 1. Actual modules, all signs, and the enlarged singleton range

FA.5 applied to VW.1 gives the rank-two Schur shape \((a,b)\), ideal order \(k\), and character \(\operatorname{sgn}^{d+a}\). The specified quotient substitution and inverse balanced chart are the actual maps already proved in G027/T049. The partition condition becomes \(K+2B+X\ge1\) in VW.2; its only nonnegative-coordinate failure is the origin.

For three selected rows, the complementary standard module is one-dimensional. The skew shape can be a horizontal strip only when the first normal part is at least \(b\); the normal total degree is at most \(3(k-1)<b\). Thus that entire extracted module vanishes. The higher selected terms vanish in the stated exact degree range as well.

The singleton Pieri decomposition is the actual sum over \(i+j<k,\ i\le x\). The remaining interlacing inequality is automatic because \(j<k\le b\). The formal extra pairs with \(i>x\) are matched by
\[
(i,j)\longmapsto(x+j+1,i-x-1).
\]
This preserves their nonnegative triangular domain and is an involution. The transformed pair of complete-function indices is \((q-1,p+1)\) when the original pair is \((p,q)\), so the two Jacobi–Trudi determinants are exact negatives. Fixed points have zero determinant. This proves the full triangular trace formula for every \(x\ge0\); it does not replace the actual singleton module by a sum of unordered Schur labels. All complete-function arguments used on the triangle are nonnegative, with the critical lower one at least \(2k-2\).

## 2. Pair action and the excluded origin

For each normal \(\rho=(p,q)\), \(p\le2(k-1)<b\). The determinant-column duality rewrites \(S_\rho W^*\) as \((\det W)^{-p}\operatorname{Sym}^{p-q}W\). Consequently the target of the comparison in VW.7 is polynomial. Its binary Clebsch–Gordan maps are the alternating contractions and symmetric multiplications specified in the report, normalized on their nonzero highest tensors. Their distinct summands are the same Littlewood–Richardson summands of the skew extraction. This gives the actual representation isomorphism with the asserted determinant power.

Applying these maps on each normal Schur component preserves its multiplicity space. In particular it preserves the literal interchange of the two normal tensor factors. The pair orientation is \(\operatorname{sgn}_2\), and the complementary standard determinant is retained as \((\det W)^b\). Thus the fixed-pair trace is the square of the truncated trace, whereas the swapped-pair trace is the truncated trace of the squared complementary operator. All signs in VW.8–VW.10 follow.

At \(X=B=K=0\), the component has \(k=3,(a,b)=(7,7)\), total degree fourteen. T049's all-degree product-ideal map gives zero there. The full tail-product character supplies the same equality: selected-four terms have maximum degree eight; the fully selected term, including the two-variable exterior factor, has maximum degree twelve; the selected-three Schur extraction vanishes because \(b>3(k-1)\). Hence the three surviving trace terms really give zero at the formal origin, without assigning a plethysm coefficient to its invalid partition. The independent computation found all seven origin traces zero.

## 3. Phase-degree bounds and exact initial ranges

The complete-character rational functions are proper. Their poles have periods dividing the cycle least common multiple, so their nonnegative-index sequences are exact residue polynomials from index zero. VW.11 therefore gives their full phase functions, not only eventual formulas.

For the singleton triangle, the complementary period is at most four. Splitting \(i,j\) into residues gives \(M=\lfloor(k-1-s-t)/L\rfloor\ge-1\). The binomial-basis convolution in VW.12 is exact, and its polynomial is zero at \(M=-1\). Thus no short initial triangle is missed.

For an independent polynomial reconstruction I used the following safe total-degree bounds, before any cancellation was inferred from the saved data:
\[
(5,3,3,2,0,2,0)
\]
in the seven-class order. The identity ambient term has degree five; its singleton summand has degree three before triangular summation and hence degree at most five afterward; its pair term has degree five. For a transposition the quadratic leading products in the ambient determinant cancel, and the complementary linear-leading products in its singleton determinant cancel, giving degree at most three. For class \(221\), the complementary \(22\) complete trace is \((-1)^n(\lfloor n/2\rfloor+1)\); the products of its leading signs agree in both determinant terms, giving the safe degree-three bound after summation. For classes \(311\) and \(41\), their singleton summands are periodic, so their triangular sums have degree at most two. The remaining classes have periodic ambient and pair terms and no singleton term. These arguments prove the listed bounds throughout the enlarged chamber.

For every phase \((a,b,k)\bmod L\), I chose its corresponding nonnegative residue in \((X,B,K)\), evaluated the literal restriction trace on a unisolvent simplex of that degree, and reconstructed the ordinary polynomial by rational multivariate Newton interpolation. The degree bounds just proved make this an exact reconstruction. It is not an inference from a few test values.

All 449 reconstructed polynomials match both saved constructions. Their actual degrees are
\[
(5,3,2,1,0,0,0).
\]
The reconstruction used **1,627** exact simplex trace values.

## 4. Independent computational paths and results

The source for the reconstruction is `check_variable_wall_independent.py`. It imports no theta or root Python implementation. Its trace path uses:

- the literal selected unions of permutation cycles;
- the unexpanded rank-two truncated normal polynomials;
- the two Weyl coefficient shifts;
- closed formulas for complementary complete traces;
- exact rational binomial-basis conversion of the phase simplex data.

The reconstructed polynomials are saved in `VARIABLE_WALL_POLYNOMIALS_INDEPENDENT.json`.

For every nonzero allowed difference order, I recomputed the differences by repeated literal translations \(P(Z+60e_i)-P(Z)\), rather than the source Stirling formula. The independent coefficientwise phase maxima and class-size sums reproduce every margin. All **45** margins have nonnegative coefficients and positive constant; the smallest constant is **1,288,865**.

I then evaluated the entire residue cube with Python unbounded integers for all polynomial products and character sums. All **1,512,000** constants, all seven saved array hashes, all extrema, and every support entry match. There are exactly **13 valid effective-label zeros**. The source's separately proved int64 bounds are therefore not needed by this independent replay.

The complete receipt is `VARIABLE_WALL_INDEPENDENT_RECEIPT.json`. Its source hashes identify both the theta and root polynomial inputs.

## 5. Positivity, Newton counts, and actual evaluator checks

The identity polynomial has nonnegative ordinary coefficients and support exactly the stated order set except its zero constant. The nonidentity phase degrees are at most three. The 19 low-order margins and the 26 remaining identity-only differences therefore establish all 45 strict bounds. For every irreducible label, the invariant Hermitian form gives \(|\chi_\nu(g)|\le\dim[\nu]\); applying the triangle inequality to the coefficientwise bounds gives precisely the positive lower bound in §4 of the report. Step sixty preserves all class phases.

Order-zero values are actual multiplicities at every valid residue, and the only excluded residue has the actual zero arrangement component proved above. Thus every fixed Newton coefficient is a nonnegative integer. The three first-order coefficients are strictly positive, which forces every zero to have quotient vector zero and justifies the finite support catalog.

The order set has 46 elements: 15 with first exponent zero, then 15, 10, and 6 with first exponent one, two, and three. Its maximum total order is five. Three quotient variables, one selector, and those at most five chain variables give the stated nine-variable bound. The strict-chain inequalities have the exact subset-count interpretation in VW.15, including zero-length chains and infeasible short quotients.

A second script, `check_variable_wall_evaluator.py`, independently checks every printed identity coefficient row, every printed margin row, and the complete support table. All **17 identity rows**, **19 margin rows**, and seven support-label rows match the reconstructed data. It also checks ten parameter triples, including continuation well beyond the base residue cube and the support boundaries, in both determinant parities and all labels. **140 coefficients**, **6,426 literal matrix systems**, and **2,620 witness tuples** pass. The invalid origin is rejected by the evaluator.

These results are saved in `VARIABLE_WALL_EVALUATOR_RECEIPT.json`. They verify the actual integer matrix bounds and equalities, the selector range, every chain gap, the complete binomial count, and the declared variable limit.

The full report's formal-origin argument, exact pair maps, determinant parity, complete support interpretation, and finite-certificate scope all pass this review. The other agents' balanced-coefficient sweeps were not rerun or counted as mine.

