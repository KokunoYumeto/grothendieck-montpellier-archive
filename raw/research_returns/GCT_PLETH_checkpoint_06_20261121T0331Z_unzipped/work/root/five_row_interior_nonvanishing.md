# All five-row shapes with consecutive gaps at least two

## G-025. Every outer label occurs, and the actual canonical image is nonzero

Let \(\lambda\vdash5n\) have at most five parts, padded by zeros,
and suppose
\[
\lambda_i-\lambda_{i+1}\ge2\qquad(1\le i\le4).
\tag{IN.1}
\]
Then every \(\mu\vdash5\) satisfies
\[
\boxed{p_{\mu,(n)}^\lambda\ge2.}
\tag{IN.2}
\]
The actual canonical map
\[
h_{n,5}:\operatorname{Sym}^n(\operatorname{Sym}^5V)
\longrightarrow\operatorname{Sym}^5(\operatorname{Sym}^nV)
\tag{IN.3}
\]
has a nonzero \(S_\lambda V\) component in every dimension at least
the number of positive parts of \(\lambda\). For \(n\ge5\) it
is surjective on that whole isotypic component, and its multiplicity
rank is the target coefficient. At \(n=4\) the only possible shape
is \((8,6,4,2)\); its target multiplicity is three and its actual
image multiplicity is one. No shape satisfies (IN.1) at \(n<4\).

Thus any vanishing coefficient in outer degree five lies on a region
where at least one consecutive gap is zero or one. This is a consequence
of the explicit embeddings below. All claims concern the stated
Schur labels and the specified grid map.

## 1. Reduction to seventy-six fully specified seeds

Put \(d=\lambda_5\), and let \(g_i=\lambda_i-\lambda_{i+1}\).
Write
\[
g_i=2+p_i+2t_i,\qquad p_i\in\{0,1\},\quad t_i\ge0.
\tag{IN.4}
\]
The size condition is
\(\sum_{i=1}^4 i g_i=5(n-d)\). Choose a coordinatewise minimal
\(u\le t\) among the nonnegative integer vectors satisfying
\[
\sum_{i=1}^4 i(2+p_i+2u_i)\equiv0\pmod5.
\tag{IN.5}
\]
Such a vector exists because \(t\) is admissible and its coordinate
box is finite.

Every such minimal vector has \(\sum_i u_i\le4\). To prove this,
list \(u_i\) copies of the nonzero residue \(i\) modulo five.
Any five entries have a nonempty subsequence summing to zero: the
six successive partial sums, including zero, have a repeated residue.
Removing the intervening entries decreases at least one coordinate
and preserves (IN.5). Five entries would therefore contradict
minimality. This proves the bound, with an explicit removable
subsequence whenever the bound is exceeded.

The seed list is consequently obtained by the following finite rule:
enumerate all sixteen \(p\), enumerate all seventy vectors
\(u\in\mathbf Z_{\ge0}^4\) of total at most four, retain (IN.5),
and retain the coordinatewise minimal ones for that \(p\).
There are seventy-six retained pairs. Their gap vectors and shapes are
\[
a_i=2+p_i+2u_i,\qquad
\sigma=(a_1+a_2+a_3+a_4,a_2+a_3+a_4,a_3+a_4,a_4,0).
\tag{IN.6}
\]
Each has size \(5n_\sigma\). The complete finite calculation in
§2 and the final table prove that every one has all seven
multiplicities at least two.

The difference
\[
\eta=\tfrac12(\lambda-d\mathbf1-\sigma)
\tag{IN.7}
\]
is an integral partition: its last part is zero and its consecutive
gaps are \(t_i-u_i\ge0\). The size relation
\(2|\eta|=5(n-d-n_\sigma)\) implies \(5\mid|\eta|\), since
five is odd. Write \(|\eta|=5q\). Multiplication by the actual
polynomial \(f_\eta\) of G-024 injects \(B_\sigma\) into
\(B_{\sigma+2\eta}\). Multiplication by \(\det^d\) then gives
the actual \(B_\lambda\), with outer labels transposed at odd
\(d\). Every seed has every label with multiplicity at least two,
so the two maps prove (IN.2) for all inputs.

## 2. Exact finite character calculation for every seed

The following method evaluates every class trace without interpolation
or a presumed support pattern. For any \(\alpha\vdash5n\), let
\(T_c(\alpha,n)\) be the trace of a permutation of cycle type
\(c\) on \((S_\alpha\mathbf Q^5)_{(n^5)}\).
The seven classes and their sizes are
\[
(1^5),(2,1^3),(2^2,1),(3,1^2),(3,2),(4,1),(5),
\qquad 1,10,15,20,20,30,24.
\tag{IN.8}
\]

For a single cycle of length \(\ell\), pad a shape \(\alpha\)
to \(\ell\) parts and put \(e_i=\alpha_i+\ell-i\).
Its trace is zero when the residues \(e_i\bmod\ell\) repeat.
Otherwise it is
\[
\operatorname{sgn}(e_1\bmod\ell,\ldots,e_\ell\bmod\ell)
(-1)^{\ell(\ell-1)/2},
\tag{IN.9}
\]
where the sign of a list of distinct residues is the sign of its
permutation relative to increasing order. Shapes of length greater
than \(\ell\) give zero. Indeed apply the Weyl determinant at the
cycle eigenvalues \(z\zeta_\ell^j\). Repeated residues make its
rows proportional. Otherwise the numerator differs from the
denominator's descending-residue determinant by precisely that row
permutation; the power of \(z\) is \(\ell n\), so extracting the
balanced coefficient gives (IN.9).

To remove a fixed point from a cycle type, use
\[
T_{(c,1)}(\alpha,n)=
\sum_{\beta:\ \alpha/\beta\text{ a horizontal }n\text{-strip}}
T_c(\beta,n).
\tag{IN.10}
\]
Only shapes with at most \(|c|\) rows enter. This is an exact trace
identity: a cycle of length \(\ell\) on
\((\operatorname{Sym}^nV)^{\otimes\ell}\) has trace
\(h_n(X_1^\ell,X_2^\ell,\ldots)\). A fixed point multiplies that
character by \(h_n\), and the Pieri decomposition has one summand
for each displayed strip. Equivalently it is the actual direct-sum
branching in the balanced Cauchy module of T-003. Such strips are
enumerated exactly by
\(\alpha_i\ge\beta_i\ge\alpha_{i+1}\) and
\(|\beta|=|\alpha|-n\); those are the bounds used in the code.

Two residual cycle types require explicit two-variable determinants.
For \(c=(2,2)\), pad \(\alpha\) to four parts, put
\(e_i=\alpha_i+4-i\), and separate the descending exponent list
into its even and odd members. Unless both groups have two members,
the trace is zero. Otherwise write their halved lists as
\((A_1,A_2)\) and \((B_1,B_2)\), using
\(A=e/2\) and \(B=(e-1)/2\). Set
\[
\rho=(A_1-1,A_2),\quad \tau=(B_1-1,B_2),\quad
\epsilon=(-1)^{N+3},
\tag{IN.11}
\]
where \(N\) counts pairs in which an odd exponent precedes an even
exponent in the original list. The exact trace is
\[
T_{(2,2)}(\alpha,n)
=\epsilon\max\{0,\min(\rho_1,n-\tau_2)
                 -\max(\rho_2,n-\tau_1)+1\}.
\tag{IN.12}
\]
For the proof, evaluate at \((z,-z,w,-w)\). Adding and subtracting
the columns belonging to each pair separates even and odd rows.
The denominator has residue list \((1,0,1,0)\), with three
inversions. Dividing the resulting two determinants by their
denominators gives
\(s_\alpha(z,-z,w,-w)=\epsilon s_\rho(z^2,w^2)s_\tau(z^2,w^2)\).
Each two-variable Schur polynomial has every exponent from its second
part to its first part with coefficient one. Their balanced product
coefficient is the interval intersection in (IN.12).

For \(c=(3,2)\), use five exponents \(e_i=\alpha_i+5-i\).
For each three-element subset \(I\subset\{1,2,3,4,5\}\), let
\(J\) be its complement; preserve the original descending order
in each list. Terms with repeated residues modulo three on \(I\)
or modulo two on \(J\) vanish. For every other term put
\[
 A=(\sum_{i\in I}e_i-3)/3,\qquad
 B=(\sum_{j\in J}e_j-1)/2.
\tag{IN.13}
\]
Its sign is the Laplace sign \((-1)^{\sum_{i\in I}i+6}\)
times the residue-permutation signs relative to descending order
in lengths three and two. Sum that sign over exactly the terms
satisfying
\[
A=n+2v+2,\qquad B=n-3v,\qquad v\in\mathbf Z_{\ge0}.
\tag{IN.14}
\]
This sum is \(T_{(3,2)}(\alpha,n)\). To verify it, expand the
five-by-five numerator determinant by its three-cycle columns.
After division by both within-cycle Vandermondes, its terms are the
signed monomials \(T_1^AT_2^B\) in (IN.13). The remaining cross
Vandermonde is \(T_1^2-T_2^3\), with positive sign. The expansion
\[
(T_1^2-T_2^3)^{-1}
=\sum_{v\ge0}T_1^{-2v-2}T_2^{3v}
\]
shows that its balanced coefficient is exactly (IN.14). This is a
coefficient identity in a Laurent-series field; the Schur quotient
is a polynomial, so its polynomial coefficient is the same.

Equations(IN.9)–(IN.14), recursively removing every fixed point,
evaluate all seven classes in (IN.8). Averaging with the complete
seven-by-seven character table in G-019 gives each integer
\[
\frac1{120}\sum_c|c^{S_5}|\chi_\mu(c)T_c(\alpha,n).
\tag{IN.15}
\]
The delivered `five_row_cycle_trace.py` implements exactly these
formulas, including the length, size, parity and zero-residue cases.
The reproducing enumeration is `five_row_gap2_certificate.py`.
The file `FIVE_ROW_GAP2_SEEDS.json` contains every seed, every trace
and every multiplicity. A separate literal cycle-index and
Murnaghan–Nakayama program checks all315 multiplicities of the45
seeds with \(n\le7\); its receipt is
`FIVE_ROW_GAP2_SEEDS_MN_CHECK.tsv`. All76 seeds are additionally reconstructed independently by literal
Jacobi–Trudi determinants and two-cycle interpolation over the field
with61 elements, with the exact bounded-degree coefficient recovery
recorded in `work/archive/GAP2_SEEDS_INDEPENDENT_RECEIPT.json`.
The displayed determinant/Pieri algorithm and the final table certify
every seed value. No input-dependent positivity assumption is used.

## 3. The actual map in every degree of this family

At \(n\ge6\), Cheung–Ikenmeyer–Mkrtchyan,
*Symmetrizing tableaux and the 5th case of the Foulkes conjecture*, arXiv:1509.03944v1,
**Theorem6(a), p.3**, and Ikenmeyer,
*On McKay's propagation theorem for the Foulkes conjecture*,
arXiv:1509.04957, **Theorem1.3, p.2**, give surjectivity of the
actual map (IN.3). The exact grid conventions and normalized
transpose are audited in R-024, (P.3),(P.25); that proof establishes
the precise comparison used here.

At \(n=5\), the same Cheung–Ikenmeyer–Mkrtchyan paper,
**Theorem6(b), p.3**, gives the eight kernel labels displayed in
R-024, (P.27). Each has a consecutive gap zero or one. Therefore
none satisfies (IN.1), and the square map is injective, hence
surjective, on every isotypic component under consideration. This
proves the claimed full multiplicity rank at every \(n\ge5\).

At \(n=4\), the weighted gap sum is already at least twenty;
equality forces \(d=0\) and every gap equal to two. Thus the only
shape is \((8,6,4,2)\). Its target multiplicity is three by G-023
at \(r=2,d=0\). Its source multiplicity is one, as certified by
the literal cycle-index/Murnaghan–Nakayama calculation recorded
with the polarization certificate below.

Here is a direct nonzero image, using actual polarization rather than
an inference from source and target multiplicities. In a four-by-four
matrix \(X\), let \(p_I\) denote the flag minor with row indices
\(I\) and the first \(|I|\) columns. Put
\[
F_0=p_1p_4p_{12}p_{34}p_{234}p_{123}(\det X)^2,
\qquad F=\frac1{24}\sum_{g\in S_4}gF_0.
\tag{IN.16}
\]
The row degree of \(F_0\) is five in each row. Its right highest
weight is \(2\omega_1+2\omega_2+2\omega_3+2\omega_4
=(8,6,4,2)\); row permutations preserve that weight. Thus \(F\)
belongs to the source's indicated highest-weight space.

For five covectors \(v_j\), the normalized grid-map evaluation is
\[
h_{4,5}(F)(v_1,\ldots,v_5)
=\frac1{(5!)^4}
\left[\prod_{i=1}^4\prod_{j=1}^5t_{ij}\right]
F_0\left(\sum_jt_{1j}v_j,\ldots,\sum_jt_{4j}v_j\right).
\tag{IN.17}
\]
Indeed polarizing degree five in each row yields the factor
\((5!)^4\); column symmetrization changes no evaluation because
the four covectors in a column are equal. Permuting the four rows
leaves the coefficient unchanged, so the average defining \(F\)
has exactly the coefficient of \(F_0\). This derives (IN.17) from
the inclusion–grid-permutation–projection definition.

Take \(v_j=(1,j,j^2,j^3)\) over \(\mathbf F_{1000003}\), for
\(j=1,\ldots,5\). The exact coefficient in (IN.17) is
\[
21,210,071,040\quad\text{over }\mathbf Z,\qquad
7410\pmod {1000003}.
\tag{IN.18}
\]
The independent integer reconstruction gives the normalized value
\(115072/1125\). It uses three-row cofactors and four-row Laplace
expansion in `work/archive/check_n4_polarization_integer.cpp`; the
explicit intermediate bound is below \(2^{118}\), so its signed
128-bit arithmetic is exact. The receipt is
`work/archive/N4_POLARIZATION_INTEGER_RECEIPT.json`.
The complete integer-modular computation is
`five_row_n4_polarization.cpp`. It evaluates the polynomial at all
\(2^{20}=1,048,576\) Boolean choices of the twenty variables and
takes the alternating sum. This equals the desired coefficient:
inclusion–exclusion kills a monomial missing any variable, and total
degree twenty forces every surviving monomial to contain each
variable exactly once. The code uses only explicit two-, three-
and four-by-four determinant formulas and integer modular arithmetic.
Its complete receipt is `FIVE_ROW_N4_POLARIZATION_CHECK.txt`.
The prime divides neither24 nor \((5!)^4\); hence (IN.18) proves
that the rational characteristic-zero image is nonzero. The source
multiplicity one now makes its image multiplicity exactly one.

All maps are polynomial functors and commute with inclusion of the
four-dimensional coordinate subspace. The vector just constructed
therefore proves the assertion in every larger dimension as well.
Together with the degree-five square-kernel audit and full
degree-six propagation, this proves the entire actual-map statement.

## 4. Geometric and lambda-ring statement

The embeddings (IN.7),(EI.4) and determinant multiplication are maps
of the balanced Schur components of the same flag-cone coordinate
ring. The finite normalizer projector realizes the plethysm
operation of cote133/024–029 in the representation \(K_0\), with
the exact dictionary A-010 and T-003. Equation(IN.17) is the
coordinate pullback for multiplying five linear forms; its nonzero
image is an actual graded section on the Chow coordinate-image
scheme, as in G-003 and EGA I9.5.2. The sheaf/frame transport is
SGA3 I4.5,4.7.2–4.7.3, and the Schur composition and \(K_0\)
operations are SGA6 V4.2,4.4,4.8–4.9 and VI3.3. Clearing the
displayed averaging denominators gives the specified integral models.
The positivity and multiplicity statements refer to their
characteristic-zero fibers.

## 5. Complete seed multiplicities

The labels are ordered
\((5),(4,1),(3,2),(3,1,1),(2,2,1),(2,1,1,1),(1^5)\).
Each row gives the gap vector of its seed in (IN.6), its balanced
degree, and all seven multiplicities. The parity of the gaps
identifies its \(p\); subtracting \(2+p\) and dividing by two
recovers its minimal \(u\). Thus the table and the finite rule in
§1 specify every seed without an implicit choice.

| Seed gaps | Degree | Multiplicities in the stated order |
|---|---:|---|
| (2, 2, 2, 2) | 4 | (3, 9, 11, 9, 9, 6, 2) |
| (2, 2, 2, 7) | 8 | (4, 17, 24, 28, 27, 23, 7) |
| (2, 2, 4, 3) | 6 | (5, 20, 27, 32, 29, 24, 7) |
| (2, 6, 2, 5) | 8 | (18, 70, 91, 108, 95, 77, 21) |
| (2, 10, 2, 3) | 8 | (21, 84, 108, 128, 111, 90, 24) |
| (4, 4, 2, 3) | 6 | (10, 40, 53, 64, 56, 47, 13) |
| (8, 2, 2, 3) | 6 | (7, 31, 42, 52, 46, 39, 11) |
| (2, 2, 3, 10) | 11 | (7, 34, 45, 57, 48, 41, 11) |
| (2, 2, 5, 6) | 9 | (11, 49, 63, 80, 66, 55, 14) |
| (2, 2, 7, 2) | 7 | (6, 32, 40, 52, 41, 35, 8) |
| (2, 4, 3, 4) | 7 | (11, 49, 61, 77, 62, 51, 12) |
| (2, 8, 3, 2) | 7 | (15, 66, 81, 101, 81, 66, 15) |
| (4, 2, 3, 2) | 5 | (4, 21, 26, 35, 27, 23, 5) |
| (2, 2, 3, 5) | 7 | (7, 26, 31, 36, 29, 22, 5) |
| (2, 2, 9, 3) | 9 | (18, 69, 84, 99, 81, 63, 15) |
| (2, 6, 3, 3) | 7 | (17, 66, 82, 98, 81, 65, 16) |
| (4, 2, 5, 3) | 7 | (17, 65, 79, 93, 76, 59, 14) |
| (6, 4, 3, 3) | 7 | (27, 105, 129, 154, 127, 101, 25) |
| (10, 2, 3, 3) | 7 | (19, 74, 91, 107, 88, 69, 16) |
| (2, 3, 2, 4) | 6 | (5, 23, 27, 35, 26, 21, 4) |
| (2, 3, 8, 2) | 8 | (15, 66, 81, 101, 81, 66, 15) |
| (2, 7, 2, 2) | 6 | (8, 35, 41, 52, 40, 32, 6) |
| (4, 3, 4, 2) | 6 | (12, 51, 62, 77, 61, 49, 11) |
| (6, 5, 2, 2) | 6 | (14, 55, 66, 80, 63, 49, 11) |
| (10, 3, 2, 2) | 6 | (11, 41, 48, 57, 45, 34, 7) |
| (2, 3, 2, 9) | 10 | (9, 41, 51, 65, 52, 43, 10) |
| (2, 3, 4, 5) | 8 | (13, 56, 70, 87, 71, 58, 14) |
| (2, 3, 10, 3) | 10 | (31, 126, 157, 190, 157, 126, 31) |
| (2, 5, 2, 3) | 6 | (6, 30, 38, 49, 40, 34, 8) |
| (4, 3, 6, 3) | 8 | (31, 125, 156, 190, 157, 128, 32) |
| (6, 3, 2, 3) | 6 | (9, 41, 53, 67, 56, 46, 12) |
| (2, 3, 3, 2) | 5 | (5, 18, 23, 26, 23, 19, 5) |
| (2, 3, 3, 7) | 9 | (13, 54, 67, 81, 68, 55, 14) |
| (2, 3, 5, 3) | 7 | (12, 48, 60, 72, 60, 48, 12) |
| (2, 7, 3, 5) | 9 | (36, 144, 180, 216, 180, 144, 36) |
| (2, 11, 3, 3) | 9 | (40, 160, 200, 240, 200, 160, 40) |
| (4, 5, 3, 3) | 7 | (23, 93, 117, 140, 117, 93, 23) |
| (8, 3, 3, 3) | 7 | (24, 94, 117, 141, 117, 94, 24) |
| (3, 2, 2, 8) | 9 | (11, 39, 46, 52, 42, 31, 7) |
| (3, 2, 4, 4) | 7 | (13, 47, 56, 64, 53, 40, 10) |
| (3, 2, 10, 2) | 9 | (24, 90, 111, 128, 108, 84, 21) |
| (3, 4, 2, 2) | 5 | (7, 24, 29, 32, 27, 20, 5) |
| (5, 2, 6, 2) | 7 | (21, 77, 95, 108, 91, 70, 18) |
| (7, 2, 2, 2) | 5 | (7, 23, 27, 28, 24, 17, 4) |
| (3, 2, 2, 3) | 5 | (3, 13, 18, 23, 20, 18, 5) |
| (3, 2, 3, 6) | 8 | (9, 41, 53, 67, 56, 46, 12) |
| (3, 2, 5, 2) | 6 | (6, 30, 38, 49, 40, 34, 8) |
| (3, 6, 3, 4) | 8 | (31, 125, 156, 190, 157, 128, 32) |
| (3, 10, 3, 2) | 8 | (31, 126, 157, 190, 157, 126, 31) |
| (5, 4, 3, 2) | 6 | (13, 56, 70, 87, 71, 58, 14) |
| (9, 2, 3, 2) | 6 | (9, 41, 51, 65, 52, 43, 10) |
| (3, 2, 3, 11) | 12 | (18, 68, 83, 98, 79, 61, 14) |
| (3, 2, 5, 7) | 10 | (25, 98, 119, 141, 115, 90, 21) |
| (3, 2, 7, 3) | 8 | (19, 74, 90, 107, 87, 68, 16) |
| (3, 4, 3, 5) | 8 | (24, 94, 116, 138, 114, 90, 22) |
| (3, 8, 3, 3) | 8 | (35, 138, 173, 207, 172, 137, 34) |
| (5, 2, 3, 3) | 6 | (11, 43, 52, 61, 50, 39, 9) |
| (3, 3, 2, 10) | 11 | (19, 74, 91, 107, 88, 69, 16) |
| (3, 3, 4, 6) | 9 | (27, 105, 129, 154, 127, 101, 25) |
| (3, 3, 6, 2) | 7 | (17, 66, 82, 98, 81, 65, 16) |
| (3, 5, 2, 4) | 7 | (17, 65, 79, 93, 76, 59, 14) |
| (3, 9, 2, 2) | 7 | (18, 69, 84, 99, 81, 63, 15) |
| (5, 3, 2, 2) | 5 | (7, 26, 31, 36, 29, 22, 5) |
| (3, 3, 2, 5) | 7 | (9, 39, 50, 61, 52, 43, 11) |
| (3, 3, 8, 3) | 9 | (34, 137, 172, 207, 173, 138, 35) |
| (3, 7, 2, 3) | 7 | (16, 68, 87, 107, 90, 74, 19) |
| (5, 3, 4, 3) | 7 | (22, 90, 114, 138, 116, 94, 24) |
| (7, 5, 2, 3) | 7 | (21, 90, 115, 141, 119, 98, 25) |
| (11, 3, 2, 3) | 7 | (14, 61, 79, 98, 83, 68, 18) |
| (3, 3, 3, 8) | 10 | (24, 94, 117, 141, 117, 94, 24) |
| (3, 3, 5, 4) | 8 | (23, 93, 117, 140, 117, 93, 23) |
| (3, 3, 11, 2) | 10 | (40, 160, 200, 240, 200, 160, 40) |
| (3, 5, 3, 2) | 6 | (12, 48, 60, 72, 60, 48, 12) |
| (5, 3, 7, 2) | 8 | (36, 144, 180, 216, 180, 144, 36) |
| (7, 3, 3, 2) | 6 | (14, 55, 68, 81, 67, 54, 13) |
| (3, 3, 3, 3) | 6 | (10, 38, 47, 57, 47, 38, 10) |
