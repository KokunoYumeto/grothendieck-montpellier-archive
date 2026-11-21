# A-085. Whole-proof and independent symbolic audit of R045

**Status: PASS.** I read the complete `work/rectangular/double_four_tail_canonical_block.md`, DF.1–DF.28 and all seven sections, together with the two symbolic source programs and their saved receipts. I independently reconstructed all sixteen moment-matrix entries, every full polynomial residual, all four split-form rows, six finite relations, five canonical endpoint minors and both cubic scalars. Every check passes.

## 1. Actual invariant generators and finite-row bound

Each of the four polynomials is a sum of products of four two-row brackets. The identity
$z_i^t\operatorname{adj}(S)z_j=\sum_k[z_i,z_k][z_j,z_k]$
gives this directly for the two contracted generators. Thus their $GL_2$ character is $\det^4$, and their lower highest weight is $(4,4)$. Common centering gives translation invariance.

For a fixed original row, the leading parts of any two centered rows are scalar multiples of the same vector. The quadratic term in their bracket is zero, so every bracket has separate row degree at most one. Every generator consequently has row degree at most four and extends by the specified separate homogenization for $n\ge4$.

For the transpose shape $(2,2,2,2)$, the exact invariant-algebra surjection has three exterior-degree-zero contributions, with separate determinant exponents 0, 1 and 2. Exterior degree two gives one more: after its determinant factor, the paired shape is $(1,1,0,0)$ and the vertical two-strip occupies rows three and four. Exterior degree four already has determinant power three; odd exterior degree has the wrong parity. The actual Pieri and column maps therefore bound the invariant multiplicity by four.

The ordered-pair factors in DF.6 are correct. In particular expanding the brackets gives twice
$M_{02}(M_{30}M_{12}-M_{21}^2)
-M_{11}(M_{30}M_{03}-M_{21}M_{12})
+M_{20}(M_{21}M_{03}-M_{12}^2)$
for $Q_2$, and twice
$M_{40}M_{04}-4M_{31}M_{13}+3M_{22}^2$ for $Q_3$.

## 2. Injective independent-row morphism and its filtration

The diagonal evaluation on $a$ identical functionals is injective on symmetric row polynomials: each coefficient is a nonzero multinomial multiple of its row-orbit coefficient, equivalently rational polarization recovers every multilinear evaluation.

For a normalized functional $L$, write $v=(L(w_1),L(w_2))$ and set $L_0(p)=L(p(w-v))$. Then $L_0(1)=1$, its first moments vanish, and common translation invariance gives
$L^{\otimes a}f=L_0^{\otimes a}f$.
For a general functional with $L(1)\ne0$, first divide by $L(1)$ and restore the factor $L(1)^a$. Hence vanishing on normalized zero-mean functionals gives vanishing on the dense open set $L(1)\ne0$, then everywhere. This proves DF.8's restricted injectivity through an explicit recentering map.

The exact filtration assertion DF.9 also follows. A centered moment of degree at most $q$ is a polynomial in raw moments of degree at most $q$ and the two first moments. Thus an expression on the normalized zero-mean slice involving only moments through $q$ remains independent of higher moments after recentering any normalized functional. Homogeneity then gives this independence on $L(1)\ne0$ for the full homogeneous diagonal polynomial. Polynomial density makes it global. The coefficient identification from polarization places $f$ in the actual separate-row-degree-at-most-$q$ subspace. The forward inclusion is immediate from evaluation. This verifies the equality of subspaces required for the later cubic extension.

## 3. Entire universal moment identity

The central-to-raw formula is the binomial expansion of each centered monomial. For a product of raw row sums, the equality partition of its labeled factors specifies the occupied rows; its contribution is the falling factorial $(a)_{|\pi|}$ times the product of the corresponding block moments. These are finite polynomial identities over $\mathbb Q(a)$.

My independent implementation uses a different enumeration of these partitions. It chooses the block containing the first labeled factor by submultisets of the remaining factor types, weights a choice by the product of the corresponding binomial coefficients, and recurses on the remaining factors. It never imports the source reconstruction program or a proposed moment matrix.

The raw generator expansions have 15, 52, 34 and 47 monomials. Every coefficient of every resulting moment polynomial was reconstructed. All moments of degree greater than four cancel. All sixteen recovered matrix entries equal DF.11, and all four complete residual polynomials are zero. The determinant is exactly

$$
\det C_a=\frac{(a-5)(a-4)^2(a-3)^3}{a^6}.
$$

The four formal moment expressions are independent by their distinct degree patterns $2+2+2+2$, $2+2+4$, $2+3+3$, $4+4$. Thus the generators are independent at $a\ge6$, attaining the invariant bound. The actual finite-row restriction maps preserve each centered moment polynomial and its power-sum generator with scalar one, so they span the smaller invariant spaces.

I reconstructed all six finite relations at $a=3,4,5$ and the ranks 1, 2, 3. Restricted diagonal-evaluation injectivity turns the left-kernel relations into polynomial identities. At $a\le2$, the two-row column antisymmetrizer on $\mathfrak h_a$ is zero. This establishes exactly $r_a=\min(4,\max(0,a-2))$.

## 4. Split-form substitution and actual canonical rank

I independently substituted the printed second-, third- and fourth-moment formulas into all four formal generators. The whole polynomial substitution gives DF.18, with no untested selected-coefficient step. In particular the pure fourth-moment Wick part is $24Q_0$, its mixed polarization is $6Q_1$, and the actual fourth part is $Q_3$. Substitution of Wick minus six times the actual tensor gives
$24Q_0-36Q_1+36Q_3$.
The cubic row has scalar $-4$, and the second row has $8Q_0-6Q_1$ with the stated denominator ratio.

The determinant is $864u_n^3v_n$, nonzero for $n\ge4$. The scalar-one grid pairing then gives the actual matrix identity
$h_{a,n}\widehat Q_a=c_{a,n}C_aH_n\widehat Q_n$.
When an individual right-side homogenization has degree above its slot degree, only the displayed combinations are asserted to extend; equality with the polynomial left side proves that extension. The dense chart remains sufficient for detecting linear relations.

Restricted injectivity of independent-row evaluation shows that the rank is exactly $\operatorname{rank}(C_aH_nC_n)$. Invertibility proves the full and mixed large-row cases. The five remaining endpoint minors were independently reconstructed as
$16$, $320/27$, $-27/4$, $-110/27$, and $-32768/28125$,
with the printed ranks. Transposition is the actual pure-power pairing, so the reverse directions have the same rank.

The column-coordinate inverse in DF.23 has the correct factor order. On every proved surjective component the alternative adjoint expression is also an actual right inverse: the tensor pairing is positive definite, so the target composition is nonsingular and its rational inverse is given by adjugate over determinant.

## 5. Entire cubic space and quadratic endpoint

The exact filtration lemma makes the cubic extension precisely the kernel of the two fourth-moment columns of $C_a$. Their patterns are independent, so both coefficients must vanish. The forbidden-column rank is one at $a=3,4$ and two for $a\ge5$, with the nonzero minor in DF.24. This gives extension dimension one at $a=4,5$ and two for $a\ge6$.

I independently checked that the explicit $J_a,K_a$ annihilate both forbidden columns, their finite relations $K_4=4J_4$, $K_5=8J_5$, and their complete surviving expectation rows. Their separate cubic degree follows from the proved subspace equality. At three split factors,
$F_0=Q_{0;3}/1296$ and $F_2=Q_{0;3}/81$;
the latter uses the actual relation $Q_{2;3}=-2Q_{0;3}/3$.
The resulting scalars are exactly

$$
\frac{(a)_3(a-3)}{72},
\qquad
\frac{(a)_3(a-3)(a^3-9a^2+56a-108)}{648}.
$$

The first is nonzero for every valid $a\ge4$, and the centered simplex gives $Q_{0;3}=9$. The transposed source has multiplicity one, so the actual cubic rank is exactly one.

At degree two the principal-minor vector
$\Delta_1^{a-6}\Delta_3^2$
has the asserted weight and degree. The previously checked LDL chart and normalized polarization prove its unique highest line. Its three-row weight has zero multiplicity in the twofold one-row tensor source, giving the actual image zero.

## 6. Exact computation scope

The independent executable is `check_double_four_independent.py`. Its receipt `DOUBLE_FOUR_INDEPENDENT_RECEIPT.json` records all sixteen universal entries, four zero full-polynomial residuals, four complete split substitutions, both determinants, six finite relations, five finite canonical minors and both cubic scalars. Every comparison passed using exact symbolic rational arithmetic; no interpolation in $a$ was used.

The original 180 full-matrix pairings, 20 cubic pairings and 21 target/source coefficient comparisons were read and remain attributed to the original source programs. They were not repeated in this independent audit.
