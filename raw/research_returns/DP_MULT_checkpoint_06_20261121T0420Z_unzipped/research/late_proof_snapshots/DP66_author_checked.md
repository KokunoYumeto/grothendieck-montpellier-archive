# DP66 — adaptive prime choices, exact coefficient cost, and the fixed row interface

Author: /root/formal_bound, GPT-6 Astra Pro. Date: 2026-11-21 UTC. Reasoning effort is not exposed. This memo proves arithmetic statements about explicit coefficientwise valuation certificates. It does not upper-bound an actual theta value, rule out cancellation, or identify a coefficient height with every cost in the source construction.

## 1. The adaptive gain is real before one asks for a global operator

Let \(E=\mathbf Q(\zeta_7)\) and \(\Phi=\{1,2,3\}\). For a rational prime \(p\nmid14\), write \(a=p\bmod7\), and for \(i\in\Phi\) put
\[
 c_{i,p}=\sum_{r\ge1}\mathbf1_{a^r i\notin\Phi}p^{-r},
 \qquad
 E_{i,p}(n)=\sum_{r\ge1}\mathbf1_{a^r i\notin\Phi}
                         \left\lfloor n/p^r\right\rfloor .
 \tag{AC1}
\]
These are the bare directional slopes and integer certificates already proved for the actual integral cyclic CM models in DP40/43/45/49/53. Here the three labels agree with the global differential basis \(dx/y,x\,dx/y,x^2dx/y\) on \(y^2=x^7-1\), as checked in DP53. The following arithmetic calculation only needs (AC1).

The first outside-label sets and the exact maximum slope are:
\[
\begin{array}{c|c|c|c}
a&\{i\in\Phi:ai\notin\Phi\}&\max_i c_{i,p}&
  \text{one maximizing label}\\ \hline
1&\varnothing&0&1\\
2&\{2,3\}&(p^2+p)/(p^3-1)&3\\
3&\{2\}&p^3(p^2+p+1)/(p^6-1)&2\\
4&\{1,3\}&(p^2+p)/(p^3-1)&3\\
5&\{1\}&p^3(p^2+p+1)/(p^6-1)&1\\
6&\{1,2,3\}&p/(p^2-1)&1
\end{array}
\tag{AC2}
\]
To verify the entries, on a cycle of length \(f\) the numerator for direction \(i\) is
\(\sum_{1\le r\le f,\ a^ri\notin\Phi}p^{f-r}\), with denominator \(p^f-1\).
For \(a=2\) the three numerators are \(p,p^2,p^2+p\); for \(a=4\) they are \(p^2,p,p^2+p\). For \(a=3\) they are \(p^3+p^2+p,\ p^5+p^4+p^3,\ p^4+p^3+p^2\), and for \(a=5\) the first two interchange. For \(a=6\) they are all \(p\). These positive-polynomial comparisons prove the maxima for every \(p>1\), not just for a tested prime.

For each fixed label \(i\), exactly three of the six first-step residues send \(i\) outside \(\Phi\). The maximum over labels instead has first coefficient one in five residue classes. Therefore, with any fixed finite exceptional set containing \(2,7\),
\[
 \sum_{p\le X}\max_i c_{i,p}\log p=\frac56\log X+O(1).
 \tag{AC3}
\]
For the integer certificates put \(Y=\max\{1,\min(X,n)\}\). Uniformly in \(n\ge0\) and \(X\ge2\),
\[
 \begin{split}
 B_i(n,X)&:=\sum_{p\le X}E_{i,p}(n)\log p
       =\frac n2\log Y+O(n),\\
 A(n,X)&:=\sum_{p\le X}\max_iE_{i,p}(n)\log p
       =\frac{5n}{6}\log Y+O(n).
 \end{split}
 \tag{AC4}
\]
All prime sums in this memo omit the specified fixed exceptional set.

Here is a direct proof of the second formula, including its uniformity. If \(b_p=\max_i\mathbf1_{pi\notin\Phi}\), then
\[
 b_p\lfloor n/p\rfloor
 \ \le\ \max_iE_{i,p}(n)
 \le b_p\lfloor n/p\rfloor+\frac{n}{p(p-1)}.
 \tag{AC5}
\]
The first term is supported on the five residue classes in (AC2). The fixed-modulus weighted prime theorem gives its main term; the rounding error is \(O(\sum_{p\le\min(X,n)}\log p)=O(n)\). The higher-power error is \(O(n)\), because \(\sum_p\log p/[p(p-1)]\) converges. The first formula is the same proof with three classes. Both expressions are zero when \(n=0,1\). Thus a claim that prime-dependent selection has the same uncharged bare average as a fixed direction would be false.

Known analytic input, cited rather than reproved: Zeév Rudnick, *Primes in Arithmetic Progressions: Fixed Modulus*, May 26, 2015, §2, p.2, equation (1), and the immediately preceding fixed-modulus PNT. The exact primary page was reopened and read in this pass:
https://www.math.tau.ac.il/~rudnick/courses/sieves2015/fixed%20progressions.pdf .
No RH hypothesis is used.

## 2. A vector-power cost does not apply to an arbitrary polynomial

Let \(S\) be a finite set of rational primes and let \(\boldsymbol a=(a_1,\ldots,a_r)\in\mathbf Z^r\) have exactly these \(r\) nonzero components. Suppose that at every \(p\in S\), its reduction is a nonzero multiple of a single coordinate vector. Then
\[
 \prod_{i=1}^r|a_i|\ge\prod_{p\in S}p^{r-1},
 \qquad
 \log\max_i|a_i|\ge\frac{r-1}{r}\sum_{p\in S}\log p.
 \tag{AC6}
\]
Indeed \(p\) divides at least \(r-1\) of the nonzero integer coefficients. Multiplying these divisibilities and using \(\prod|a_i|\le(\max|a_i|)^r\) proves (AC6). No claim is made for zero components that were omitted from the support. The coefficient of \(Z_i^n\) in \((\sum_i a_iZ_i)^n\) is \(a_i^n\), so the coefficient log-height of this vector-power construction is at least \(n\log\max_i|a_i|\).

This does not obstruct an arbitrary homogeneous symbol of degree \(n\). Put \(Q=\prod_{p\in S}p\) and prescribe labels \(i(p)\). For \(n\ge1\), there is a primitive polynomial
\[
 P=\sum_{i=1}^r c_i Z_i^n,\qquad
 P\equiv Z_{i(p)}^n\pmod p\quad(p\in S),
 \qquad
 \log\max_i|c_i|\le\log Q+O(\log r),
 \tag{AC7}
\]
whose bound is independent of \(n\). For \(i<r\), choose centered CRT representatives for \(c_i\equiv\mathbf1_{i=i(p)}\pmod p\), and set \(c_r=1-\sum_{i<r}c_i\). All congruences hold; \(\sum c_i=1\) proves primitivity; and the displayed bound follows from \(|c_i|\le Q/2\) for \(i<r\) and \(|c_r|\le1+(r-1)Q/2\).

The existence step by CRT also applies to a fixed integral module of harmonic polynomials with one fixed row multidegree, if the prescribed local targets are reductions of elements of that module. Linear combinations preserve the module. Bounds in a chosen integral generating system must include the coefficient sizes of those generators and targets; no uniform height assertion for that changing module is inferred from (AC7). This statement does not presume that every polynomial solving the harmonic equations modulo \(p\) lifts to an integral harmonic polynomial. Nor does it allow one to combine distinct fixed row-degree components.

The constraints in (AC6) need only be imposed at the primes actually used. In the example, labels \(1,2\) already cover the five nontrivial first-step residue classes; requiring all three vector components, or imposing a pure-direction condition at class \(1\), can therefore overstate the cost of a chosen construction.

## 3. Modulo-p approximation is insufficient for high divisibility: an actual local counterexample

Take the actual strict height-\(h\) line \(G\) and its actual Cartier dual \(H\) in the arbitrary-unit singleton/complement cyclic model of DP32/40/43/46. Work over an unramified coefficient DVR, normalize \(v_p(p)=1\), and let \(q=p^h\), \(h\ge3\). Write \(D_G\) for the primitive line derivation and \(D_1\) for the first normalized dual eigendirection. At \(n=q^r\), \(r\ge1\), the checked operator and coefficient formulas give
\[
 D_G^n\bigl(R[[G\times H]]\bigr)
   \subseteq p^{c_h(n-1)}R[[G\times H]],\quad
 c_h=\frac1{p-1}-\frac1{q-1},
 \qquad
 v_p(D_1^nX_1(0))=\frac{p(n-1)}{q-1}.
 \tag{AC8}
\]
Here \(X_1\) is the first integral coordinate on \(H\); \(D_GX_1=0\). These are actual integral group coordinates and derivatives. In particular, for
\[
 P_B=D_G^n+p^B D_1^n,\qquad B\ge1,
\]
one has \(P_B\equiv D_G^n\pmod p\), but exactly
\[
 v_p(P_BX_1(0))=B+\frac{p(n-1)}{q-1}.
 \tag{AC9}
\]
It is below the first operator's universal certificate unless
\[
 B\ge\left(c_h-\frac p{q-1}\right)(n-1)
     =\frac{(p^2+\cdots+p^{h-1})(n-1)}{q-1}.
 \tag{AC10}
\]
For \(p=11,h=3,n=1331\), the first certificate is \(132\), the dual coordinate derivative has valuation \(11\), and \(B=1\) gives valuation \(12\). Preserving \(132\) on this coordinate requires \(B\ge121\).

More generally, if the target operator has a lower certificate \(b_p\) and every possible error operator in a chosen integral lattice has lower certificate \(\ell_p\), congruence modulo \(p^{B_p}\) preserves the target lower bound provided \(B_p+\ell_p\ge b_p\). Preserving a specified nonzero value of exact valuation \(b_p\) by this argument requires strict inequality. The example proves that a precision proportional to the derivative order can really be necessary. It does not prove necessity for every selected section, and it does not refute a correctly chosen higher-precision CRT construction.

## 4. The exact product-formula bound for coefficientwise certificates

Fix a nonempty finite support \(I\), nonzero integers \(c_i\), a finite prime set \(S\), and real numbers \(e_{i,p}\). Define
\[
 T_p=\min_{i\in I}\{v_p(c_i)+e_{i,p}\},
 \qquad H_\infty(\boldsymbol c)=\log\max_{i\in I}|c_i|.
\]
Then
\[
 \boxed{\quad
 \sum_{p\in S}T_p\log p-H_\infty(\boldsymbol c)
 \le \min_{i\in I}\sum_{p\in S}e_{i,p}\log p .
 \quad}
 \tag{AC11}
\]
For every fixed \(i\), \(T_p\le v_p(c_i)+e_{i,p}\). Since \(c_i\) is a nonzero integer,
\[
 \sum_{p\in S}v_p(c_i)\log p\le\log|c_i|\le H_\infty(\boldsymbol c).
\]
Sum the first inequality over \(p\), subtract \(H_\infty\), and then minimize over \(i\). This proves (AC11) without an asymptotic limit, CRT hypothesis, or primitivity assumption.

Suppose the \(e_{i,p}\) are integers, and put \(e_p^*=\max_{i\in I}e_{i,p}\). The inequality is sharp in the strongest elementary sense. Set
\[
 c_i=\prod_{p\in S}p^{\,e_p^*-e_{i,p}}.
 \tag{AC12}
\]
These are positive integers. At each \(p\), at least one exponent is zero, so \(\gcd_i c_i=1\). For every \(i,p\),
\(v_p(c_i)+e_{i,p}=e_p^*\). Consequently
\[
 T_p=e_p^*,\qquad
 H_\infty(\boldsymbol c)
 =\sum_{p\in S}e_p^*\log p
       -\min_{i\in I}\sum_{p\in S}e_{i,p}\log p .
 \tag{AC13}
\]
Conversely, (AC11) says that every vector with the same prescribed nonzero support and \(T_p\ge e_p^*\) has height at least (AC13). Thus (AC13) is the exact minimum for that fixed support. Different smaller supports that still cover all the desired local maxima can change the finite lower-order term; no unique optimal support is asserted.

For \(n\ge1\), apply this to \(I=\{1,2,3\}\), \(e_{i,p}=E_{i,p}(n)\), and \(p\le X\). It constructs a primitive homogeneous degree-\(n\) polynomial whose termwise certificate realizes every local maximum. Its minimum coefficient log-height for this support is
\[
 A(n,X)-\min_iB_i(n,X)
       =\frac n3\log\bigl(\max\{1,\min(X,n)\}\bigr)+O(n).
 \tag{AC14}
\]
For any smaller support capable of realizing the same maxima, the same leading lower bound holds, since all three fixed-label budgets have the same main term. Thus the apparent extra \(1/3\) leading coefficient is exactly spent by the coefficient height in this certificate calculation. This proves existence and its arithmetic cost; it does not assert that an actual value cannot have additional cancellation.

### Number-field and projective form

Let \(K\) be a number field of degree \(d\). At each place use the extension of the usual absolute value, normalized by \(|p|_v=p^{-1}\) at \(v\mid p\), with weights \(n_v=[K_v:\mathbf Q_v]/d\), including \(2/d\) at a complex place. For \(\boldsymbol c=(c_i)_{i\in I}\in(K^\times)^I\), put
\[
 M_v=\max_i|c_i|_v,\qquad h([\boldsymbol c])=\sum_v n_v\log M_v.
\]
For finite \(v\mid p\) define \(m_v=\min_i v_p(c_i)\), and for prescribed real \(e_{i,v}\) set
\[
 T_v^{\rm prim}=\min_i\{v_p(c_i)-m_v+e_{i,v}\}.
\]
For any finite collection \(S_f\) of finite places,
\[
 \boxed{\quad
 \sum_{v\in S_f} n_vT_v^{\rm prim}\log p
       -h([\boldsymbol c])
 \le \min_i\sum_{v\in S_f}n_ve_{i,v}\log p .
 \quad}
 \tag{AC15}
\]
Indeed the product formula for any fixed nonzero \(c_i\) gives
\[
 h([\boldsymbol c])=\sum_v n_v\log(M_v/|c_i|_v).
\]
Every summand is nonnegative. At \(v\mid p\), it equals
\(n_v(v_p(c_i)-m_v)\log p\). Keeping just \(S_f\), and using the definition of \(T_v^{\rm prim}\), proves (AC15).

The subtraction of \(m_v\) is local primitive-lattice normalization; it is invariant under multiplying all coefficients by a common element of \(K^\times\). It does not assume that the coefficient-content ideal is principal or that one can simultaneously divide by a single global generator. Over \(\mathbf Q\) with primitive integral coefficients it reduces exactly to (AC11). An unnormalized integral vector is instead covered by the affine statement (AC11), or its archimedean-height analogue over \(K\). Scaling and denominator ideals cannot silently be discarded.

The height in these statements is a genuine coefficient cost. For a homogeneous polynomial in a monomial basis with \(J\) supported monomials, at any complex embedding its supremum on the unit polydisc satisfies
\[
 \max_\alpha|c_\alpha|\le\|P\|_{\mathrm{polydisc}}
     \le J\max_\alpha|c_\alpha|.
 \tag{AC16}
\]
The upper bound is the triangle inequality. For the lower bound integrate \(P(e^{it_1},\ldots,e^{it_d})e^{-i\alpha\cdot t}\) over the unit torus; orthogonality recovers \(c_\alpha\), whose modulus is at most the supremum. Thus the associated projective adelic polydisc height differs from coefficient height by between zero and \(\log J\). This supplies a direct comparison for this specified norm. It does not identify it with an uninspected source norm, a period normalization, or an automorphic section height.

## 5. All homogeneous coefficientwise bare certificates obey the fixed leading bound

Fix a cyclotomic modulus, a CM type, and a finite exceptional set as in DP64. A direction label \(i\) has the periodic certificate \(E_{i,p}(n)\) of (AC1), with \(p^r i\) interpreted through that fixed abelian Galois action. Allow any finite number of copies or columns, and let
\[
 P=\sum_{\alpha\in I}c_\alpha Z^\alpha,\qquad
 \sum_{i,b}\alpha_{i,b}=N,\quad c_\alpha\in\mathbf Z\setminus\{0\}.
\]
For an integral coefficientwise model define
\[
 e_{\alpha,p}=\sum_{i,b}E_{i,p}(\alpha_{i,b}),\qquad
 T_p(P)=\min_{\alpha\in I}\{v_p(c_\alpha)+e_{\alpha,p}\}.
\]
The interpretation is literal: each invariant differential monomial has this lower certificate, and the nonarchimedean triangle inequality gives \(T_p(P)\) for their sum. Then, uniformly in the support, the number of columns, \(N\), and \(X\),
\[
 \boxed{\quad
 \sum_{p\le X}T_p(P)\log p-H_\infty(P)
 \le \frac N2\log\bigl(\max\{1,\min(X,N)\}\bigr)+O(N).
 \quad}
 \tag{AC17}
\]
The constant depends on the fixed modulus and exceptional set.

For each fixed monomial, DP64(CB3) gives
\[
 \sum_{p\le X}e_{\alpha,p}\log p
 =\frac12\sum_{i,b}\alpha_{i,b}
    \log\bigl(\max\{1,\min(X,\alpha_{i,b})\}\bigr)+O(N).
\]
The one-direction \(O(n)\) constant is uniform over the finitely many labels. Summing it therefore gives \(O(N)\) even when the number of columns varies. Each logarithm is at most \(\log(\max\{1,\min(X,N)\})\). Apply (AC11) to obtain (AC17). This argument needs only an upper bound; it does not use DP64(CB4)'s two-sided comparison for a fixed number of directions.

The normalized number-field version follows from (AC15) whenever the certificates at every place over \(p\) are the same displayed \(e_{\alpha,p}\), and \(S_f\) contains all places over the rational primes in question: \(\sum_{v\mid p}n_v=1\). More general place-dependent geometric labels require their own prime-sampling statement. Nothing here assumes that arbitrary reflex or nonabelian place sampling has the cyclotomic average.

The leading coefficient \(1/2\) is attained within this coefficientwise class, up to \(O(N)\), by one fixed pure derivative with coefficient one, using (AC4) or DP64. Thus (AC17) is not merely a weak estimate for the certificate class. Nevertheless \(T_p(P)\) is a lower certificate, not the actual valuation of a selected theta expression. A selected value can be strictly more divisible than \(T_p(P)\), including by cancellation or special geometry.

## 6. Exact restrictions from the recovered theta source

The source identifies a variable by a CM embedding, a row within its multiplicity, and a column. These three labels cannot be interchanged.

In Formalism/LocalToGlobal/ProjectiveLattices/RowDeg.lean:
- Line 11 defines the variable set as the sum, over embeddings \(\sigma\), of row and column indices.
- Lines 21–30 define the summed column contractions and the harmonic module.
- Lines 32–38 define invariance under adding an earlier row to a later row.
- Lines 40–41 require, for **every supported monomial** and **every embedding and row**,
\[
 \sum_{\text{columns }b}\alpha_{\sigma,i,b}=a(\sigma,i).
 \tag{AC18}
\]
- Lines 43–48 impose harmonicity, row invariance, these row degrees, and integral coefficients simultaneously.

The source bridge from the prescribed HC data to \(a(\sigma,i)\) is DP61, with exact declarations DataKap, AMiEqAMinusQ, FWExist.kapTop, and PartitionExtendByZeroAntitone.wtA. In particular, fixing a source datum fixes these totals. Switching a degree-\(N\) pure monomial from one CM embedding to another changes (AC18), so the simple polynomial in (AC7) or (AC12) generally does not lie in that one prescribed component. Columns may be rearranged, and coefficients within that component may vary. Harmonicity and row invariance are linear conditions, and the span of monomials of one row multidegree is also linear. Thus CRT inside the actual integral component remains possible, subject to genuine liftability of its local targets. The row condition is not an assertion that all adaptive arithmetic constructions are impossible.

In IsThRule.lean:
- Lines 20 and 55 specify the one-column and all-column variables using the actual complex embeddings of \(E\).
- Lines 57–58 extract the derivative multiindex for each column.
- Lines 66–70 evaluate one polynomial \(P\), with its global coefficients, by a sum of products of column jets and the common factor \(M^{-\deg P}\).
- Lines 72–78 allow faithfully flat base change and permitted section tuples, while retaining that same \(P\).
- Lines 80–82 require the resulting rule at every test ring and frame point for this fixed \(P\).
- Lines 84–91 require \(P\) to lie in the specified integral harmonic component before it defines a theta generator.

Consequently independent polynomials \(P_p\) cannot be substituted into different primes of this global rule without first producing one permitted global \(P\). Period selection does not change that quantifier. Conversely, the definitions do not forbid one global \(P\) whose coefficients have carefully chosen local residues, and they do not forbid extra cancellations in its selected values. The common scalar \(M^{-\deg P}\), exponential gauge, and geometric section data have separate valuation and norm effects; (AC17) is not a replacement for computing them.

The precise remaining route after DP66 is therefore a global polynomial in the **fixed** source row component, together with its permitted section/period realization, whose actual selected values improve the explicit coefficientwise certificates by quantified cancellation or geometry, with all normalization and norm costs included. DP66 supplies no such object and proves no universal upper bound on those actual values.

## 7. Source and dependency record

The two exact source modules were read at their displayed ranges in this pass. Their SHA-256 values are:
- RowDeg.lean: 5bfd910715a5fb61ac23df068f6e10106fa14c042cb3810fc1fc04003150ba9f.
- IsThRule.lean: d0570a0398b32df4c732c4b0d5051d27cda119195187e74377f4f0e40cfeb11e.

The complete saved DP64 memo and complete saved DP61 memo were read in this pass before applying their conclusions. The periodic formulas and actual-pair witnesses are proved in DP40/43/46 and are used here as previously checked results, rather than reproved. Rudnick's primary p.2 was reopened and read. The product-formula and CRT arguments above are elementary complete proofs.

A small exact-rational Python enumeration was actually run to independently recover all six residue cycles and numerator exponent sets in (AC2); it evaluated the maximizing label at \(p=11\) only as a consistency check. The displayed symbolic positive-polynomial comparison, not that computation, proves the maximum for every prime. No Lean compilation, formal proof assistant validation, or TeX compilation was run.

Complete saved-version author and independent reading events are recorded separately only after they occur.
