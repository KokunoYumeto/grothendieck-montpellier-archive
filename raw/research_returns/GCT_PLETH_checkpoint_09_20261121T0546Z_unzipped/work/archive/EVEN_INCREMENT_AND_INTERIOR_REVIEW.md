# Independent review of even increments and the five-row interior

Statements **A-046** and **A-047**. Complete proof checks performed
on 21 November 2026 by GPT-6 Astra Pro, run /root/archive_audit;
effort setting not exposed. All original sources used below were
opened and read at the specified locations. The original large
CIM evaluation matrices were not regenerated.

## A-046. Actual even-increment embeddings, G024

**Result: complete proof PASS.** The entire report
work/root/even_increment_transport.md, equations EI1–EI5, was
read. Let \(R=\operatorname{Sym}(E\otimes F)^U\) be the actual
flag algebra, with the row permutation action of \(S_m\), and
write \(B_\lambda(n)\) for its right highest-weight component
of weight \(\lambda\) and left weight \((n^m)\).
For every partition \(\eta\) of \(mq\) with at most \(m\)
parts, the report constructs a nonzero invariant
\[
f_\eta\in B_{2\eta}(2q)
\]
and the actual injection
\[
B_\lambda(n)\longrightarrow B_{\lambda+2\eta}(n+2q),
\qquad v\longmapsto f_\eta v.
\tag{ER1}
\]
The domain property of the polynomial ring proves injectivity;
the element's literal \(S_m\)-invariance proves equivariance.
Taking the finite-group multiplicity functor therefore gives
the claimed inequality simultaneously for every outer label.

Here is an independent constructive check that the required
balanced tableau exists. For a partition \(\eta\vdash mq\),
choose integers
\[
\eta_{i+1}\le\beta_i\le\eta_i\quad(1\le i<m),
\qquad |\beta|=(m-1)q.
\]
The lower-end sum is \(mq-\eta_1\le(m-1)q\);
the upper-end sum is \(mq-\eta_m\ge(m-1)q\).
Every integer between these two sums is realized by choosing
coordinates in the indicated integer intervals, and the
interlacing inequalities make \(\beta\) a partition.
The skew diagram \(\eta/\beta\) is a horizontal strip of size
\(q\). Label that strip by \(m\), and repeat on \(\beta\).
This gives a semistandard tableau with exactly \(q\) copies
of each label. The construction includes \(q=0\).

Its product of flag minors \(h_T\) has the required right
weight \(\eta\) and balanced row content. At the matrix
\(X_{ij}=i^{j-1}\), each selected initial-column minor is a
nonzero Vandermonde determinant. Hence \(h_T(X)\ne0\).
The explicit element
\[
f_\eta=\sum_{g\in S_m}(g h_T)^2
\]
has weight \(2\eta\), content \((2q)^m\), and is invariant
under literal row permutation. Its value at that real
matrix is positive, because one summand is already positive.
This proves nonvanishing over \(\mathbf Q\) without any
unidentified projection. At \(q=0\), it is the nonzero
constant \(m!\).

Multiplication by a determinant power gives the stated
additional translation and the sign twist
\(\operatorname{sgn}^d\). The translated staircase families
therefore follow from the already checked G022/G023 by
composition of actual injections.

For historical comparison, the primary Bürgisser–Christandl–
Ikenmeyer author PDF, Weintraub's conjecture on plethysms,
16 November 2010, was opened. The unnumbered theorem in §1.1
on printed p. 1 and Lemma 2.1 with its proof on printed p. 4
were read. Lemma 2.1 supplies the balanced weight through
Kostka dominance. The constructive strip proof above and
the sum-of-squares morphism (ER1) establish the precise
statement used here.
Source: https://www3.math.tu-berlin.de/algebra/work/weintraub.pdf .

## A-047. Every five-row interior weight, G025

**Result: complete proof PASS; all seventy-six seeds and the
degree-four canonical-map witness independently recomputed.**
The entire report work/root/five_row_interior_nonvanishing.md,
equations IN1–IN18 and the complete seed table, was read.
For a partition \(\lambda\vdash5n\), padded to five parts,
all four gaps at least two imply all seven outer
multiplicities are at least two. The proof also establishes
the asserted nonzero canonical image, with the stated
full-component surjectivity for \(n\ge5\) and the separate
rank-one result at \(n=4\).

### The finite reduction and its actual transport

Write the four gaps as \(2+p_i+2t_i\), with \(p_i\in\{0,1\}\).
Choose a coordinate-minimal \(u\le t\) satisfying the stated
size congruence modulo five. Such a minimal vector has
\(\sum_i u_i\le4\): from any five residues among \(1,2,3,4\),
two of the six partial sums coincide, giving a nonempty
zero-sum submultiset. Subtracting it preserves the congruence
because two is invertible modulo five, contradicting
coordinate minimality. This proves the completeness of
the finite enumeration over sixteen parity vectors and
seventy vectors of total size at most four.

For the resulting minimal partition \(\sigma\), put
\(d=\lambda_5\) and
\(\eta=(\lambda-d\mathbf1-\sigma)/2\).
Its consecutive gaps are \(t_i-u_i\), so it is a partition.
Its size is a multiple of five, since
\(2|\eta|=5(n-d-n_\sigma)\).
Thus the exact injection (ER1), followed by determinant
multiplication, transports every seed multiplicity to
the desired component, with its precise sign twist.

### Independent sign and coefficient checks

The single-cycle alternant has exponents
\(e_i=\alpha_i+\ell-i\). Repeated residues modulo \(\ell\)
give zero. Distinct residues give the row-permutation
sign relative to ascending residues, multiplied by
\((-1)^{\ell(\ell-1)/2}\), the denominator's descending
order sign. Total degree \(\ell n\) then gives exactly
the power \(T^n\). Fixed-point removal is the actual
Pieri expansion by a horizontal \(n\)-strip, with
interlacing and total-size constraints. Its branching
formula has no extra cycle sign.

For two two-cycles, separating the even and odd exponents
in the four-row determinant gives the two two-variable
Schur factors in IN10. The permutation sign is
\((-1)^{N+3}\), where \(N\) counts odd-before-even pairs;
the denominator has three such pairs. The interval
coefficient formula therefore has the displayed sign
and endpoint constraints.

For a three-cycle and a two-cycle, Laplace expansion on
the first three columns has sign
\((-1)^{\sum_{i\in I}i+6}\), with one-based row indices.
The cross resultant is \(T_1^2-T_2^3\), with positive
leading term. Its Laurent expansion is
\[
(T_1^2-T_2^3)^{-1}
=\sum_{v\ge0}T_1^{-2v-2}T_2^{3v}.
\]
Consequently the numerator exponents satisfy
\(A=n+2v+2,\ B=n-3v\), exactly as in the report.
The ten row subsets give the claimed finite expression.
The program's zero-based exponent differs from the
one-based expression by an even integer, so the signs agree.

The independent program check_gap2_seeds_independent.py
does not use these alternant residue formulas. It
enumerates minimal congruence vectors independently,
uses interlacing strips, evaluates literal integer
Jacobi–Trudi determinants for single cycles, and uses
Jacobi–Trudi interpolation over \(\mathbf F_{61}\) for
the two-cycle cases. The interpolated degree is at most
twenty-four. The actual two-two trace has absolute
value at most \(n+1\le13\), and the three-two trace
has absolute value at most ten. Centering the residue
therefore recovers the unique exact integer.

The execution compared all seventy-six seeds, all
532 class traces and all 532 multiplicities. It used
1,394 single-cycle determinants and 976 two-cycle
interpolations. Every result agrees; the smallest
multiplicity is two and the largest seed inner degree
is twelve. The separate degree-four source and target
multiplicities are one and three. The full receipt is
GAP2_SEEDS_INDEPENDENT_RECEIPT.json.

### Exact degree-four grid-map calculation

The polynomial \(F_0\) in IN16 is a product of the stated
initial-column minors. Its row degrees are five each,
and its right highest weight is \((8,6,4,2)\). Averaging
over the four rows therefore produces the stated
highest-weight vector in \(\operatorname{Sym}^4
(\operatorname{Sym}^5 V)\).

Polarizing each row gives the coefficient of all twenty
auxiliary variables. The coefficient equals \((5!)^4\)
times the normalized multilinear value. Row permutation
does not change this coefficient, so averaging over
the twenty-four row permutations introduces no extra
factor in that coefficient. Evaluation on five identical
fourth-power column covectors then agrees with the
normalized transpose-grid projection. Thus the
denominator in IN17 is exactly \((5!)^4\).

The independent program check_n4_polarization_integer.cpp
uses precomputed three-row cofactors and a first-row
Laplace expansion, and carries out the entire Boolean
inclusion-exclusion sum in exact signed 128-bit integers.
It gives
\[
[t_{11}\cdots t_{45}]F_0
=21,210,071,040,
\]
with 1,048,576 Boolean points, 502,432 nonzero summands,
and largest observed absolute four-row determinant
\(432\). An a priori absolute sum bound is
\[
2^{20}\,25(2\cdot5\cdot15)^2
(6\cdot5\cdot15\cdot55)^2
(24\cdot5\cdot15\cdot55\cdot225)^2
=179270269770240000000000000000000000.
\]
This is a 118-bit integer, strictly less than \(2^{127}\);
all signed 128-bit products and partial sums are safe.
The normalized grid value is therefore exactly
\[
\frac{21,210,071,040}{(5!)^4}
=\frac{115072}{1125}\ne0.
\]
Its raw coefficient reduces to \(7410\) modulo \(1000003\),
agreeing with the original certificate. The receipt is
N4_POLARIZATION_INTEGER_RECEIPT.json. Source multiplicity
one makes the actual image multiplicity exactly one.
The unique interior partition at \(n=4\) is \((8,6,4,2,0)\);
none exists for \(n<4\).

### Exact primary-source range and propagation

Cheung–Ikenmeyer–Mkrtchyan, Symmetrizing tableaux and the
5th case of the Foulkes conjecture, arXiv:1509.03944v1,
defines its map on printed p. 2 by symmetric-tensor
inclusion, transpose of the rectangular tensor grid,
and symmetric projection. This is the actual map used
in G025. Theorem 6(a), printed p. 3, proves injectivity
at \((5,6)\). Theorem 6(b), at the same location, lists
the eight kernel weights at \((5,5)\). Each of the
eight has a consecutive gap zero or one after padding
to five rows. Thus none lies in the present interior.
Both statements and the map definition were opened
and read. Their original large evaluation matrices
were not regenerated in this run.
Source: https://arxiv.org/pdf/1509.03944 .

Christian Ikenmeyer, On McKay's propagation theorem for
the Foulkes conjecture, arXiv:1509.04957, defines the
same grid map on printed p. 2. Theorem 1.3 is on that
page, and its complete proof is §§2–6, printed pp. 3–8.
All of this proof was read. The following precise
normalization clarifications make its auxiliary maps
literal without changing any kernel:

1. In tensor degree \(D=ab\), the source defines
   \(\phi_{ij}=D^{-1}\sum_p\zeta_{ij}^{(p)}\).
   Hence its two-operator coefficient is \(D^{-2}\),
   rather than the printed \(1/[D(D-1)]\). Terms with
   the same tensor position vanish, and the remaining
   double sum commutes term by term.
2. Removing the \(a\) fixed \(f_b\) positions in §4
   multiplies the lower raising product by exactly
   \(((b-1)/b)^{a(b-1)}\). This scalar is nonzero.
3. In §5, fixing positions of the other letters leaves
   their spectator factor tensored with
   \((\mathbf Q^2)^{\otimes(b+i-1)}\). The displayed
   \(GL_2\) computation applies on every copy. On the
   summand \(\det^{\eta_2}\operatorname{Sym}^{b+i-1-2\eta_2}\),
   the weight vector maps with coefficient
   \((b-\eta_2)/D\). Since
   \(\eta_2\le i-1<a<b\), it is nonzero.

One can also identify the source's raising map with
the normalized transversality map exactly. Index a
source basis by unordered partitions into \(a\)
blocks of size \(b\), and a target basis by unordered
partitions into \(b\) blocks of size \(a\); use averages
over the block labels. The raising-product entry is
\(b!/D^D\) precisely when every source-target block
intersection has size one, and zero otherwise.
Normalized group averaging has the same incidence
entry \(b!/(b!)^a\). The two maps differ by the explicit
nonzero scalar \((b!)^a/D^D\). Under the symmetric
tensor pairings this is the transpose-grid map on
the Schur multiplicity spaces. The propagation proof
therefore establishes injectivity of the actual
specified map at every \((5,n)\), \(n\ge6\).
Source: https://arxiv.org/pdf/1509.04957 .

The normalized symmetric-tensor projectors are
self-adjoint, so transposition gives surjectivity of
the opposite map \(h_{n,5}\). At \(n=5\), absence of
the interior types from the exact square kernel
gives the same componentwise conclusion. Rationality
and the actual inclusion into larger vector spaces
give the stated dimension and characteristic-zero
extensions. This completes the independent audit
of every asserted range in G025.
