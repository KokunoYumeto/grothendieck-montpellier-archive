# Two exact symmetric common-polarization kernels

Statement ID **R-011**. Written and checked on 2026-11-20 UTC by GPT-6 Astra Pro, agent `/root/rectangular_cases`; the inherited effort setting is not exposed. The statements below are finite, unconditional computational theorems. They do not assert a classification at arbitrary parameters.

## The actual maps and results

For a complex vector space $V$, use four separately homogeneous vector slots $v_1,\ldots,v_4$, of degree $b$ each, and an additional vector slot $x$. Define the natural linear map

\[
\begin{gathered}
T_{L,b}:\operatorname{Sym}^4(\operatorname{Sym}^bV)
 \longrightarrow \operatorname{Sym}^{4L}V\otimes
 \operatorname{Sym}^4(\operatorname{Sym}^{b-L}V),
 \\
 T_{L,b}(f)=[t_1^L\cdots t_4^L]
 f(v_1+t_1x,\ldots,v_4+t_4x).
\end{gathered}
\]

Equivalently, $T_{L,b}=(L!)^{-4}\prod_{i=1}^4(x\cdot\partial_{v_i})^L$. The polynomial description means the canonical multihomogeneous tensor model; using coordinate functions replaces $V$ throughout by its dual and gives the same natural map after that explicit substitution. Permuting the four slots commutes with coefficient extraction. Consequently the displayed target has its stated fourth symmetric power. Each term has $x$-degree $4L$ and residual degree $b-L$ in every slot.

**Theorem R-011.** The two maps $T_{1,3}$ and $T_{2,7}$ are injective for every finite-dimensional complex vector space $V$.

Both parameters satisfy $b=4L-1$. The ranks were established on every source highest-weight multiplicity space, not inferred from source and target multiplicities.

| $L,b$ | Source dimension on $\mathbb C^4$ | Distinct source constituents | Sum of source multiplicities | Largest source multiplicity | Certified image rank on highest-weight spaces |
|---|---:|---:|---:|---:|---:|
| $1,3$ | 8,855 | 12 | 12 | 1 | 12 |
| $2,7$ | 9,078,630 | 173 | 319 | 6 | 319 |

This verifies the first two requested common-power boundary cases for four symmetric slots. It supplies finite evidence relevant to, but no theorem about, the general even-$r$ boundary $\prod_{i=1}^r(x\cdot\partial_{v_i})^r$ at $b=r^2-1$. The actual case $r=L=4,b=15$ is now separately proved and independently certified as R-012 in polarization_r4_boundary_and_geometry.md.

## Complete proof by exact certificates

### 1. Reduction to multiplicity spaces in dimension four

The source is the invariant part of $(\operatorname{Sym}^b V)^{\otimes4}$ under permutation of its four factors. Iterated Pieri multiplication of four one-row Schur characters has at most four rows: adding a horizontal strip to a diagram with $k$ rows creates at most one additional row. Hence every source Schur functor is $S_\lambda V$ with $\ell(\lambda)\le4$.

The construction of $T_{L,b}$ uses permutations, symmetrizations and contraction of slot labels in tensor powers, so its matrices on the multiplicity spaces of the Schur functors are independent of $\dim V$ once $\dim V\ge4$. This can also be seen by the tensor model $V^{\otimes4b}$: the same element of the rational permutation algebra acts on each $V^{\otimes4b}$, and Schur–Weyl decomposition identifies its multiplicity matrices with matrices between the corresponding fixed symmetric-group modules. Since every source $S_\lambda\mathbb C^4$ is nonzero, injectivity for $V=\mathbb C^4$ proves injectivity for every dimension at least four. Inclusion of a smaller $V$ in $\mathbb C^4$ and the naturality square proves it for dimensions below four.

Over $\mathbb C$, a nonzero kernel of a $GL_4$-equivariant map contains an irreducible summand and hence a nonzero highest-weight vector. It therefore suffices to exhibit, for each source highest weight $\lambda$, exactly its source multiplicity many vectors with linearly independent images.

### 2. Exact source multiplicities, checked by two constructions

Let $W_b$ be the set of all quadruples of nonnegative integers summing to $b$. The coefficient $M(\alpha)$ of the weight $\alpha$ in the source character is exactly the number of unordered multisets of four elements of $W_b$ having sum $\alpha$. This follows directly by choosing the monomial basis of $\operatorname{Sym}^b\mathbb C^4$ and then its degree-four monomial basis. With $\rho=(3,2,1,0)$, the multiplicity of $S_\lambda\mathbb C^4$ equals

\[
 m_\lambda=\sum_{\sigma\in S_4}\operatorname{sgn}(\sigma)
 M(\lambda+\rho-\sigma\rho).
\]

To derive the formula, multiply the Schur-character expansion by $\prod_{i<j}(1-x_j/x_i)$. The Weyl alternant formula turns $s_\mu$ into the signed orbit of $\mu+\rho$, translated by $-\rho$. The coefficient at a dominant $\lambda$ is $1$ for $\mu=\lambda$ and $0$ otherwise because $\mu+\rho$ is strictly decreasing and has a unique dominant permutation.

The producer `polarization_candidates.py` obtains $M$ from Newton's exact recurrence $h_i=i^{-1}\sum_{k=1}^i h_{i-k}p_k$, where $p_k=\sum_{\alpha\in W_b}x^{k\alpha}$. The C++ verifier independently enumerates all unordered four-multisets of $W_b$, with no use of Newton's recurrence, and recomputes every required $m_\lambda$. It checks equality with the supplied table in each block. The producer also checks

\[
 \sum_\lambda m_\lambda\prod_{1\le i<j\le4}
 \frac{\lambda_i-\lambda_j+j-i}{j-i}
 =\binom{\binom{b+3}{3}+3}{4}.
\]

All partitions of $4b$ of length at most four are enumerated, so zero source multiplicities are included in the extraction process. The resulting positive-multiplicity lists and dimensions are those in the table above.

### 3. Explicit integral highest-weight vectors in the source

Use a $4\times4$ variable matrix $X$, whose columns are the slots $v_i$. For a nonempty subset $I\subseteq\{1,2,3,4\}$, let $d_I(X)$ be the determinant of the submatrix with the first $|I|$ rows and the columns $I$, in increasing order. There are fifteen such flag minors. A product

\[
 F_c(X)=\prod_{I\ne\varnothing}d_I(X)^{c_I}
\]

has highest weight $\lambda_i=\sum_{|I|\ge i}c_I$, and its degree in slot $j$ is $\sum_{I\ni j}c_I$. The highest-weight assertion follows explicitly by applying a raising operator: replacing a row indexed $j\le |I|$ by an earlier row creates two equal rows in its determinant; a row $j>|I|$ is absent. Thus every raising operator annihilates every factor and hence the product.

For each tableau of shape $\lambda$ with content $(b,b,b,b)$, its columns give such a product with slot degrees $b$. The producer sums its twenty-four slot permutations, including the signs caused by sorting the columns within each determinant. Dividing all integral coefficients by their common divisor gives a nonzero integral symmetric highest-weight vector, or the zero sum is discarded. It removes repeated resulting coefficient lists. The input files record each remaining vector as an explicit integer linear combination of the fifteen-minor monomials. No claim that these lists form a basis is needed: exhibiting $m_\lambda$ independent images already suffices.

The independent checker verifies the weight and all four degrees of every recorded monomial. A separate independent adjacent-transposition check verifies that each selected vector is fixed by the three generators of $S_4$; it uses the explicit determinant signs rather than the producer's permutation table. It passed on all 12 and 319 selected vectors respectively.

### 4. Exact image evaluation and a nonzero integer minor

Work modulo the prime $P=1,000,003$. Each certificate includes its integral evaluation points $X,x$, its selected candidate indices, the selected evaluation rows, the entire square evaluation matrix, and its nonzero determinant modulo $P$. The points were chosen by a fixed deterministic generator; the proof depends only on the printed points and their nonzero determinants.

For every flag minor,

\[
 d_I(v_1+t_1x,\ldots,v_4+t_4x)
 =d_I(X)+\sum_{j\in I}t_jd_{I,j}(X,x),
\]

where $d_{I,j}$ replaces column $j$ by $x$. Terms involving two $t$'s vanish because two columns are then equal to $x$. Multiplying these explicitly linear polynomials, truncating each $t_i$-exponent above $L$, and reading coefficient $(L,L,L,L)$ therefore evaluates exactly $T_{L,b}(F_c)$. Truncation cannot affect that coefficient because all exponents are nonnegative. The calculation then adds the candidate's signed integral terms.

The C++ program finds a nonsingular $m_\lambda\times m_\lambda$ submatrix in every block, prints all entries and verifies its determinant. A matrix of integral polynomial evaluations with nonzero determinant modulo a prime has a nonzero integer determinant. Hence the corresponding image polynomials are linearly independent over $\mathbb Q$ and over $\mathbb C$. All source multiplicity spaces are thus injective, proving R-011.

### 5. Independent entry-by-entry recheck

`recheck_polarization_certificates.py` never calls the C++ evaluator. It computes the small flag determinants by recursive Laplace expansion, and computes Taylor coefficients using four-dimensional NumPy arrays and axis shifts. It recomputes every entry of every selected square matrix, compares with the certificate, and recomputes each selected determinant by Laplace expansion. All selected determinants have size at most six. Integer intermediates in each array step are bounded by $5(P-1)^2<2^{63}$, so the `int64` operations are exact before reduction.

The independent receipt is:

```
POLARIZATION_R4_L1_B3: PASS; 12 blocks; 12 independently recomputed entries; 95 Taylor evaluations
POLARIZATION_R4_L2_B7: PASS; 173 blocks; 787 independently recomputed entries; 13865 Taylor evaluations
```

The prime was independently checked by exact primality testing. The calculations use no probabilistic inference: randomness only selected points, and every determinant value is an exact certificate.

## Reproduction and artifact inventory

Run from this directory:

```
python polarization_candidates.py
g++ -O3 -std=c++17 check_polarization_ranks.cpp -o check_polarization_ranks
./check_polarization_ranks POLARIZATION_R4_L1_B3.input
./check_polarization_ranks POLARIZATION_R4_L2_B7.input
python recheck_polarization_certificates.py
```

The two `.tsv` tables list the exact source and target multiplicities and candidate counts. The two `.input` files specify all candidate polynomials. The `_RANKS.tsv` files list every achieved rank and determinant. The `_CERTIFICATES.txt` files give all points, selected candidates and square matrices. `POLARIZATION_INDEPENDENT_RECHECK.txt` records the independent entry-by-entry checks. These files, the source code and this proof together provide a finite certificate of R-011.

The source of the motivating general polarization bound and determinant obstruction is Sra, *The q-Foulkes problem III: On Foulkes’ conjecture with a graded inner factor*, Theorem 1.3 and supplement S8, p. 36, audited in `boundary_and_prime_blocks.md`, R-010. R-011 is a finite computation of these explicit maps; it does not attribute its rank calculation to that source or claim a literature priority search.
