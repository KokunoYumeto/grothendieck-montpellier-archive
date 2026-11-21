# Exact nonvanishing for every strictly decreasing five-row output

## G-028. Complete support on the strict chamber

Let \(\lambda\vdash5n\), pad it to five entries, and assume
\(\lambda_1>\lambda_2>\lambda_3>\lambda_4>\lambda_5\ge0\).
Put \(d=\lambda_5\), \(\lambda^0=\lambda-d\mathbf1\), and
\(g_i=\lambda_i-\lambda_{i+1}\). For every outer label
\[
\mu\in\{(4,1),(3,2),(3,1,1),(2,2,1),(2,1,1,1)\},
\qquad p_{\mu,(n)}^\lambda\ge1.
\tag{SC.1}
\]
The other two labels have exactly the following support:

* At gap vectors \((L,1,1,1)\) or \((1,1,1,L)\), where
  \(L\ge1\) and \(L\equiv1\pmod5\), both coefficients for
  \((5)\) and \((1^5)\) are zero.
* At \(\lambda^0=(6,5,3,1,0)\) or \((6,4,3,2,0)\), the
  coefficient for \((5)\) is zero at even \(d\), and that for
  \((1^5)\) is zero at odd \(d\). The other extreme label has
  coefficient exactly one.
* At every remaining strictly decreasing input, both extreme
  coefficients are positive.

These are exact zero sets, including all determinant shifts. The
proof uses the explicit even-increment injection G-024 and finite
integer certificates, followed by exact evaluation of the two rays.

For the actual symmetric canonical map \(h_{n,5}\), all target
components are reached at \(n\ge6\). At \(n=5\), on this
strict chamber the rank equals the target multiplicity except at
the four entries in §4, where it equals the target multiplicity
minus one. In particular \((12,5,4,3,1)\) has target multiplicity
one and actual image multiplicity zero. The source, target and
kernel comparison in that assertion is the specified canonical map.
No complete rank assertion for \(n=3,4\) is added here.

## 1. Minimal parity seeds and the actual multiplication map

Write each positive gap uniquely as
\(g_i=1+p_i+2t_i\), \(p_i\in\{0,1\}\), \(t_i\ge0\).
Choose a componentwise minimal \(u\le t\) with
\[
\sum_{i=1}^4 i(1+p_i+2u_i)\equiv0\pmod5.
\tag{SC.2}
\]
Such a vector exists because \(t\) has this congruence. It has
\(\sum u_i\le4\): among any five of its indexed residues,
the six partial sums modulo five have a repeated value, so a
nonempty subsequence sums to zero; removing it contradicts
minimality. Enumerate the sixteen parity vectors and all
\(u\ge0\) with \(\sum u_i\le4\), retaining just the minimal
ones in (SC.2). This gives exactly 76 seeds \(\sigma\), whose
last entry is zero and whose gaps are \(1+p_i+2u_i\).

The gap vector \(v=t-u\) defines a partition \(\eta\) with
last entry zero, \(|\eta|=\sum_iiv_i\) divisible by five,
and
\[
\lambda=d\mathbf1+\sigma+2\eta.
\tag{SC.3}
\]
The exact G-024 map multiplies a balanced flag polynomial by the
invariant section \(f_\eta=\sum_{g\in S_5}(g h_\eta)^2\),
then by the determinant section to the power \(d\). Its
Vandermonde nonzero value proves injectivity in the polynomial
domain. It preserves the outer label in the even increment, and
tensors it by sign in each odd determinant increment. Thus all
seed lower bounds transfer through this specified map.

`five_row_strict_certificate.py` enumerates every seed and computes
its seven exact traces by the cycle-alternant/Pieri algorithm proved
in G-025. The resulting complete table is
`FIVE_ROW_STRICT_CERTIFICATE.json`. Every seed has all five middle
outer labels positive. Seventy-one have every label positive.
The remaining five have the following complete multiplicity vectors,
in order \((5),(4,1),(3,2),(3,1,1),(2,2,1),(2,1,1,1),(1^5)\):

| Gaps | Normalized partition | Multiplicities |
|---|---|---|
| \((1,1,1,1)\) | \((4,3,2,1,0)\) | \((0,1,1,1,1,1,0)\) |
| \((1,1,1,6)\) | \((9,8,7,6,0)\) | \((0,2,3,3,3,2,0)\) |
| \((6,1,1,1)\) | \((9,3,2,1,0)\) | \((0,2,3,3,3,2,0)\) |
| \((1,2,2,1)\) | \((6,5,3,1,0)\) | \((0,2,3,4,4,3,1)\) |
| \((2,1,1,2)\) | \((6,4,3,2,0)\) | \((0,2,3,3,3,2,1)\) |

All the enumeration and arithmetic bounds are fixed: sixteen
parities, four coordinates of total at most four, seven class traces
and the integral S5 character inner product. The certificate is a
finite exhaustive calculation with unbounded integers. It carries
the same complete alternant signs and actual branching maps as
G-025; the independent reconstruction is logged separately.

## 2. Every non-ray increment reaches a positive seed

The zero-sum monoid of subsequent gap increments is
\[
M=\{v\in\mathbf Z_{\ge0}^4:\ v_1+2v_2+3v_3+4v_4
\equiv0\pmod5\}.
\tag{SC.4}
\]
Every nonzero indecomposable element has total at most five. For
a longer element, the same five-residue partial-sum argument gives
a nonempty zero-sum subvector of length at most five, which is
proper. Subtraction and induction then decompose every element.
Checking all vectors of total at most five gives precisely
\[
\begin{gathered}
(0,0,0,5),(0,0,1,3),(0,0,2,1),(0,0,5,0),\\
(0,1,0,2),(0,1,1,0),(0,3,0,1),(0,5,0,0),\\
(1,0,0,1),(1,0,3,0),(1,2,0,0),(2,0,1,0),\\
(3,1,0,0),(5,0,0,0).
\end{gathered}
\tag{SC.5}
\]
The fixed enumeration in the certificate verifies both congruence
and indecomposability of every item and excludes every other item
in this proved finite range.

For each of the five deficient seeds, add twice each of these
fourteen gap vectors and compute all seven coefficients. All seventy
cases are in the certificate. Every resulting coefficient is
positive except in the following four cases:
\[
\begin{array}{c|c}
\text{seed gaps}&\text{increment vector}\\\hline
(1,1,1,1)&(5,0,0,0),(0,0,0,5)\\
(1,1,1,6)&(0,0,0,5)\\
(6,1,1,1)&(5,0,0,0).
\end{array}
\tag{SC.6}
\]
The two other deficient seeds therefore become fully positive after
any nonzero increment in \(M\): select one generator in a
decomposition, and apply the injective map for its remaining sum.
The same argument for the second and third rows leaves only repeated
increments in the single displayed axis.

For the first row, any generator other than the two displayed axes
already gives full positivity. A sum using both axes also dominates
\((1,0,0,1)\); subtracting that vector is still nonnegative and
still in \(M\). The already positive seed for that generator
therefore injects into the mixed-axis sum. Only the two pure axes
remain. Combining their two parities with the other two deficient
seeds leaves exactly the two ray families of the statement, and
the two isolated normalized partitions. This proves positivity
everywhere outside the listed cases, with actual embeddings.

## 3. Exact evaluation of the surviving rays

Write \(L=5t+1\). The first ray has normalized partition
\(\rho_t=(5t+4,3,2,1,0)\) and inner degree \(t+2\).
At \(t\ge1\), the exact G-027 flag dictionary has \(k=0\),
\(\alpha=(3,2,1)\), and sign exponent three. Hence
\[
(S_{\rho_t}\mathbf Q^5)_{((t+2)^5)}
\simeq\epsilon\otimes S_{(3,2,1)}\mathfrak h_5.
\tag{SC.7}
\]
This is the quotient-section isomorphism (FA.7) followed by the
explicit balanced chart; all dependence on the first row is carried
by the specified power of \(u\) in its inverse.

The three-by-three Jacobi–Trudi determinant on the standard
permutation eigenvalues gives the seven traces
\[
\operatorname{tr}S_{(3,2,1)}\mathfrak h_5
=(64,0,0,-2,0,0,-1).
\tag{SC.8}
\]
For a fully explicit verification, substitute
\(h_q=[z^q](1-z)/\prod_{c\in\gamma}(1-z^c)\) into
\(\det(h_{(3,2,1)_i-i+j})_{i,j=1}^3\), for the seven
cycle partitions \(\gamma\) of five. Only indices \(-1\)
through five occur; \(h_{-1}=0\). Expanding its six terms
gives (SC.8), and the fixed character inner product gives
\((0,2,3,3,3,2,0)\). Sign leaves this vector unchanged.
At \(t=0\), the first row of the seed table supplies the exact
vector \((0,1,1,1,1,1,0)\).

For the reversed ray \((L+3,L+2,L+1,L,0)\), take rectangle
width \(H=L+3\). The actual perfect exterior-column pairing
identifies its Schur module with \(\det^H\) times the dual of
the module for \((L+3,3,2,1,0)\). On balanced weights it sends
content \((n^5)\) to \(((H-n)^5)\), with the slot action
multiplied by \(\epsilon^H\). The finite symmetric-group
irreducibles are self-dual, and the two displayed vectors are
unchanged by transpose. This evaluates the reversed ray exactly
as well. Finally determinant multiplication contributes
\(\epsilon^d\). Both extreme labels remain zero on the rays,
and it interchanges the two extreme labels on the isolated seeds.
This proves every support assertion, including the exact coefficient
one at the isolated shapes.

## 4. Actual canonical-map consequences

Use Cheung–Ikenmeyer–Mkrtchyan, *Symmetrizing tableaux and the fifth
case of the Foulkes conjecture*, arXiv:1509.03944v1,
Theorem6(a),(b), p.3, and Ikenmeyer, *On McKay's propagation
theorem for the Foulkes conjecture*, arXiv:1509.04957,
Theorem1.3, p.2. The exact normalized-transpose and propagation
maps, including the nonzero scalar factors, were audited in R-024
and G-025. They give full target rank for \(h_{n,5}\) at
\(n\ge6\), and the explicitly listed eight multiplicity-one
kernel components for \(h_{5,5}\).

Exactly four of those eight shapes are strictly decreasing after
padding to five entries. The independent balanced-character
calculation gives:

| Strict \(n=5\) shape | Target multiplicity | Kernel multiplicity | Actual image multiplicity |
|---|---:|---:|---:|
| \((12,7,3,2,1)\) | 2 | 1 | 1 |
| \((12,5,4,3,1)\) | 1 | 1 | 0 |
| \((10,8,4,2,1)\) | 3 | 1 | 2 |
| \((9,7,6,3,0)\) | 2 | 1 | 1 |

The other four kernel shapes have an equal consecutive pair.
On every other strict shape the known kernel is zero, so image
rank equals its target multiplicity. This proves the asserted rank
formula and its single positive-target/zero-image strict component.
The calculation uses the actual kernel of the literal canonical
map, with the exact source theorem and transpose convention stated
above; positivity alone is never used to infer its rank.

## 5. Geometric restatement and verification scope

The maps in (SC.3) are multiplication by explicit invariant sections
in the flag-coordinate domain. Their equivariance is the SGA3
I4.5,4.7.2–4.7.3 frame action, and their Schur classes evaluate
the composition on cote133/024–029 via A-010 and SGA6
V4.2,4.4,4.8–4.9. They define effective cokernel classes in the
representation category. For the coherent geometric model, use
the finite equivariant resolution map into the locally free
\(K_0\) specified in G-027 §6, with exact SGA6 VI3.3 locator.
The perfect complement pairing in §3 and the G-027 chart prove
the corresponding identifications of actual sections, including
the determinant local systems and all vanishing assertions.

The canonical ranks in §4 are ranks of the inclusion–grid permutation–
projection map on those Schur components. Its scheme-theoretic
coordinate image for multiplication of linear forms is the specified
EGA I9.5.2 image of G-025. The zero rank at \((12,5,4,3,1)\)
therefore describes the absence of that degree-five coordinate-image
component despite its one-dimensional target multiplicity space.
This is an exact statement about that morphism and its kernel.

All 76 seed vectors, all fourteen monoid generators, all seventy
increment vectors, the seven fixed ray traces and the four canonical
target calculations are stored in the complete integer certificate.
Whole-proof readings and independent reconstructions are recorded
separately in `CHECK_EVENTS.tsv`, with their actual scope.
