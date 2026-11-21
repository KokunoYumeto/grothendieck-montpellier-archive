# Every multiplicity in the image of the outer-five canonical map

## R-031. Exact rank law, all degrees and all output partitions

Work over a field of characteristic zero. Write

\[
h_{d,e}:\operatorname{Sym}^{d}(\operatorname{Sym}^{e}V)
\longrightarrow\operatorname{Sym}^{e}(\operatorname{Sym}^{d}V)
\tag{OF.1}
\]

for symmetric-tensor inclusion, transpose of the \(d\times e\)
tensor grid, and symmetric projection, using averaging inclusions.
Let \(a_{d,e}^{\lambda}\) be the multiplicity of \(S_\lambda V\)
in its source. Define the actual image multiplicity

\[
\rho_n^\lambda=
\dim\operatorname{Hom}_{GL(V)}
  (S_\lambda V,\operatorname{im}h_{n,5}).
\tag{OF.2}
\]

For every integer \(n\ge1\), every partition \(\lambda\vdash5n\),
and every \(V\) with \(\dim V\ge\ell(\lambda)\),

\[
\boxed{
\rho_n^\lambda=
\begin{cases}
a_{n,5}^{\lambda},&1\le n\le4,\\
a_{5,5}^{\lambda}-\mathbf1_{\lambda\in\mathcal E},&n=5,\\
a_{5,n}^{\lambda},&n\ge6,
\end{cases}}
\tag{OF.3}
\]

where the finite set is exactly

\[
\begin{aligned}
\mathcal E=\{&
(14,7,2,2),\ (13,7,2,2,1),\ (12,7,3,2,1),\\
& (12,6,3,2,2),\ (12,5,4,3,1),\ (11,5,4,4,1),\\
& (10,8,4,2,1),\ (9,7,6,3)\}.
\end{aligned}
\tag{OF.4}
\]

The corresponding cokernel multiplicity is
\(a_{5,n}^{\lambda}-\rho_n^\lambda\). Thus its values are,
respectively, \(a_{5,n}^{\lambda}-a_{n,5}^{\lambda}\),
\(\mathbf1_{\lambda\in\mathcal E}\), and zero in the three
ranges of (OF.3). The rank on the full \(\lambda\)-isotypic space
is \(\rho_n^\lambda\dim S_\lambda V\).

These assertions assemble established results for the specified
canonical maps. The finite strict-partition table below and the exact
normalization check are given to make their application directly
reviewable. No historical novelty is claimed for the rank law.

## 1. The transpose map, including its scalar

Equip \(V^{\otimes N}\) and \((V^*)^{\otimes N}\) with their
ordinary tensor evaluation pairing. On every symmetric power use the
pairing induced by its averaged tensor inclusion. For example,

\[
\langle v_1\cdots v_e,\phi_1\cdots\phi_e\rangle
=\frac1{e!}\sum_{\sigma\in S_e}
  \prod_{i=1}^e\phi_i(v_{\sigma(i)}).
\tag{OF.5}
\]

Nested symmetric powers use the corresponding nested averaging. Let
\(i_{d,e}\) be their inclusion into \(V^{\otimes de}\), and
\(q_{d,e}\) the quotient that multiplies within rows and then among
rows. Their composite \(i_{d,e}q_{d,e}\) is the orthogonal averaging
idempotent for the row wreath group. Consequently
\(i_{d,e}^*=q_{d,e}\) and \(q_{d,e}^*=i_{d,e}\).
For the grid permutation \(\tau_{d,e}\), its transpose is its
inverse, which is \(\tau_{e,d}\). The exact identity is therefore

\[
h_{d,e}=q_{e,d}\tau_{d,e}i_{d,e},\qquad
h_{d,e}(V)^*=h_{e,d}(V^*).
\tag{OF.6}
\]

There is no additional scalar in (OF.6). It identifies the kernels,
cokernels and ranks used in the proof of (OF.3).

## 2. The fourth square base and its exact primary certificate

The original source is Juby Jacob, *Representation Theory of
Association Schemes*, RWTH Aachen dissertation (2004), **Definition
4.1.1, printed p.92; §4.2, printed pp.95–99; Table 4.4, printed
pp.104–106**. The source is

<https://publications.rwth-aachen.de/record/51990/files/Jacob_Juby.pdf>.

The final paragraph of §4 before §5 in Müller–Neunhöffer,
*Some computations regarding Foulkes’ conjecture* (2005), explicitly
attributes the fourth-square calculation to Jacob §4.2. The authors’
primary preprint is

<https://www.math.rwth-aachen.de/homes/Max.Neunhoeffer/Publications/pdf/foulkes.pdf>.

Here is the actual map between Jacob's matrix and (OF.1).
Take \(N=uv\), let \(e_1,\ldots,e_N\) be distinct basis vectors,
and consider the multilinear weight \((1^N)\). A basis of
\(\operatorname{Sym}^{v}\operatorname{Sym}^{u}\) at that weight
is indexed by partitions \(L=\{L_1,\ldots,L_v\}\) of
\(\{1,\ldots,N\}\) into \(v\) unordered blocks of size \(u\):

\[
q_L=\prod_{i=1}^{v}\left(\prod_{k\in L_i}e_k\right).
\tag{OF.7}
\]

The target basis has analogous vectors \(q_W\), where \(W\)
has \(u\) blocks of size \(v\). Jacob's matrix \(M_{u,v}\)
has entry one exactly when every intersection \(L_i\cap W_j\)
has one element. In the averaged inclusion of \(q_L\), every
ordered row arrangement has coefficient
\(1/[v!(u!)^v]\). For a fixed transverse \(W\), exactly
\(v!u!\) arrangements project to \(q_W\): choose the row
ordering and the column ordering, after which every cell is fixed.
All other \(W\) receive zero. Hence

\[
h_{v,u}(q_L)=(u!)^{1-v}\sum_W(M_{u,v})_{W,L}q_W.
\tag{OF.8}
\]

In particular, the multilinear matrix of \(h_{4,4}\) is precisely
\(24^{-3}M_{4,4}\).

Jacob computes the adjacency algebra for the permutation action of
\(S_{16}\) on these block partitions. Its orbital matrices
\(A_0,\ldots,A_{42}\) form a basis of the commutant, and
\(A_{42}=M_{4,4}\). They obey

\[
A_iA_j=\sum_k p_{ij}^{k}A_k.
\tag{OF.9}
\]

Jacob's **Definition 1.1.11, printed p.9**, defines the displayed
collapsed matrix to have row \(j\), column \(k\) equal to
\(p_{j,42}^{k}\). Thus the matrix of right multiplication
by \(A_{42}\), in the basis \(A_j\) and column coordinates,
is its transpose. On
printed p.99 Jacob records

\[
\det B_{42}=2^{223}3^{67}\ne0.
\tag{OF.10}
\]

This gives an inverse in the finite-dimensional unital adjacency
algebra: solve \(BA_{42}=A_0\). In its faithful matrix
representation that equation makes \(A_{42}\) invertible. It
therefore proves injectivity of the multilinear map in (OF.8).

For completeness, passage from multilinear weight to every vector
space retains the actual map. Schur–Weyl decomposition of
\(V^{\otimes N}\), followed by the row averaging idempotents,
writes (OF.1) as \(\bigoplus_\lambda
\operatorname{id}_{S_\lambda V}\otimes H_\lambda\).
For \(V=\mathbb Q^N\), the weight \((1^N)\) in its tensor
power has basis \(e_{\sigma(1)}\otimes\cdots\otimes
e_{\sigma(N)}\), a regular symmetric-group module. Applying
a primitive Young idempotent gives the nonzero Specht module of
shape \(\lambda\), exactly the multilinear weight in
\(S_\lambda\mathbb Q^N\). Every \(H_\lambda\) is therefore
injective when the multilinear map is injective. The same matrices
\(H_\lambda\) occur in every dimension, so \(h_{4,4}\) is
injective in every dimension.

The independent arithmetic receipt in this run extracts all 1,849
entries of Table 4.4, reconstructs its three column blocks, and
recomputes (OF.10) by fraction-free Bareiss elimination. Every exact
division is checked. Separate modular Gaussian eliminations give
determinants 82, 15 and 6627 modulo 101, 1009 and 10007. The matrix
and executable are `JACOB_2004_TABLE_4_4.tsv` and
`verify_jacob_fourth_base.py`; the receipt is
`JACOB_FOURTH_BASE_DETERMINANT_CHECK.txt`. The source's orbital
enumeration itself was not rerun. Its construction and the exact
matrix-to-map relation above were read and checked.

## 3. The remaining established canonical inputs

**Degree four.** Apply McKay's propagation proof to the established
injectivity of \(h_{4,4}\). The conclusion needed here is the
actual injectivity of \(h_{4,5}\). A full primary proof of the
propagation is Christian Ikenmeyer, *On McKay's propagation theorem
for the Foulkes conjecture*, **Theorem 1.3, printed p.2; proof in
§§2–6, printed pp.3–8**:

<https://arxiv.org/pdf/1509.04957>.

That paper's map definition on p.2 is (OF.1). Its full proof was
read in this run; R-024 §6 records the auxiliary raising-operator
normalizations and the retained spectator tensor factor. Those
corrections multiply only auxiliary injectivity maps by nonzero
scalars and retain the canonical grid map itself. This gives
\(\rho_4^\lambda=a_{4,5}^{\lambda}\).

**Degrees one, two and three.** At \(n=1\), \(h_{1,5}\)
is the identity on \(\operatorname{Sym}^5V\). For \(n=2,3\),
Sra's **Theorem 1.3, printed p.2**, in *The q-Foulkes problem III:
On Foulkes’ conjecture with a graded inner factor*, v1, states
surjectivity of \(h_{b,a}\) for every \(b\ge(a-1)^2\).
The exact two substitutions \((b,a)=(5,2),(5,3)\) satisfy this
bound. The full polarization/annihilator proof was read and audited
in R-021–R-024. Its primary text is

<https://suvrit.github.io/papers/qfoulkes3/qfoulkes3-v1.pdf>.

By (OF.6), these surjections transpose to injectivity of
\(h_{2,5}\) and \(h_{3,5}\). This proves the first line of
(OF.3) at every remaining positive degree. At degree zero the
canonical scalar map \(\mathbb Q\to\mathbb Q\) is also the
identity; it can be added separately with the empty partition.

**Degree five and every larger degree.** Cheung–Ikenmeyer–Mkrtchyan,
*Symmetrizing tableaux and the 5th case of the Foulkes conjecture*,
**Theorem 6(a),(b), printed p.3**, supplies injectivity of
\(h_{5,6}\) and the exact kernel

\[
\ker h_{5,5}=\bigoplus_{\lambda\in\mathcal E}S_\lambda V,
\tag{OF.11}
\]

with each listed summand once. The primary text is

<https://arxiv.org/pdf/1509.03944>.

Its p.2 definition again is (OF.1). The source proves its
computations using exact integer evaluation and representation
matrices. Its large original matrices were not recomputed in this
run. The stated maps, multiplicities and parameter range were
checked against the primary text and are used with their stated
scope. McKay propagation applied to the \((5,6)\) base gives
injectivity of \(h_{5,n}\) for every \(n\ge6\); (OF.6)
then gives surjectivity of \(h_{n,5}\) for every such degree.
This proves the remaining two lines of (OF.3).

The literature computations in sufficiently large dimension imply
the conclusions in every smaller dimension by the actual inclusion
\(V\hookrightarrow V\oplus W\), which commutes with all tensor
permutations and symmetric-power maps. The uniform Schur–Weyl
multiplicity matrices above give the same conclusion and show that
the kernel summands in (OF.11) are simply absent when their lengths
exceed the dimension. All maps and their ranks are defined over
\(\mathbb Q\); extension to any characteristic-zero field
preserves the ranks. This completes the proof of (OF.3).

## 4. Complete finite strict-chamber gate

Strict means \(\lambda_1>\lambda_2>\lambda_3>\lambda_4>
\lambda_5\ge0\), padding partitions to five entries. There are no
strict partitions of size below ten. At \(n=2\) there is one,
at \(n=3\) seven, and at \(n=4\) thirty. Every strict partition
has at least four nonzero rows. The actual averaging inclusion
\(\operatorname{Sym}^{n}\operatorname{Sym}^{5}V
\hookrightarrow(\operatorname{Sym}^{5}V)^{\otimes n}\), followed
by the usual successive Pieri decompositions, shows that its source
contains only shapes of length at most \(n\). Thus every strict
actual image is zero at \(n=2,3\), including the three nonzero
target multiplicities at \(n=3\).

The accompanying executable checks **every** partition of \(5n\)
of length at most five for \(1\le n\le4\): 313 partitions in
total. For both source and target it compares two exact calculations:

1. Expand the plethysm in power sums by its symmetric-group cycle
   index, and evaluate every irreducible character by literal
   rim-hook Murnaghan–Nakayama recursion.
2. Expand the monomial-multiset character
   \([t^d]\prod_{|\alpha|=e}(1-tx^\alpha)^{-1}\) in five
   variables; multiply by the Weyl alternant and extract each
   highest-weight coefficient. The total monomial character
   dimension is checked against
   \(\binom{\binom{e+4}{4}+d-1}{d}\).

All 626 coefficient comparisons agree. All 192 degree-four source
coefficients also agree with T-037's fixed positive polytope
evaluator, used with outer label \((4)\), inner degree five.
Partitions of greater length have zero source and target in these
degrees by the same averaging inclusion and Pieri argument.
These computations evaluate multiplicities; the map ranks follow
from the proved injectivity, not from numerical comparison alone.

The complete receipts are
`OUTER5_CANONICAL_LOW_DEGREE_CHECK.tsv` and
`OUTER5_CANONICAL_STRICT_LOW_DEGREES.tsv`, generated by
`verify_outer5_canonical_low_degrees.py`. The table below contains
all 38 strict cases. At degree four, 16 image multiplicities are one
and the other 14 are zero. Exactly four nonzero target components
are reached in full: \((13,4,2,1)\), \((9,8,2,1)\),
\((8,6,5,1)\) and \((7,6,4,3)\).

At degree five the four strict shapes in (OF.4) are
\((12,7,3,2,1)\), \((12,5,4,3,1)\),
\((10,8,4,2,1)\) and \((9,7,6,3,0)\); their image
multiplicities are exactly their target multiplicities minus one.
Every other strict degree-five target is reached in full. Every
strict target at degree at least six is reached in full. Together
with G-028's complete coefficient support, this resolves the actual
symmetric canonical-map gate on the entire strict five-row chamber.

| n | Strict partition | Source = actual image | Target | Cokernel |
|---:|---|---:|---:|---:|
| 2 | (4,3,2,1,0) | 0 | 0 | 0 |
| 3 | (9,3,2,1,0) | 0 | 0 | 0 |
| 3 | (8,4,2,1,0) | 0 | 1 | 1 |
| 3 | (7,5,2,1,0) | 0 | 1 | 1 |
| 3 | (7,4,3,1,0) | 0 | 1 | 1 |
| 3 | (6,5,3,1,0) | 0 | 0 | 0 |
| 3 | (6,4,3,2,0) | 0 | 0 | 0 |
| 3 | (5,4,3,2,1) | 0 | 0 | 0 |
| 4 | (14,3,2,1,0) | 0 | 0 | 0 |
| 4 | (13,4,2,1,0) | 1 | 1 | 0 |
| 4 | (12,5,2,1,0) | 1 | 2 | 1 |
| 4 | (12,4,3,1,0) | 0 | 1 | 1 |
| 4 | (11,6,2,1,0) | 1 | 2 | 1 |
| 4 | (11,5,3,1,0) | 1 | 2 | 1 |
| 4 | (11,4,3,2,0) | 0 | 1 | 1 |
| 4 | (10,7,2,1,0) | 1 | 2 | 1 |
| 4 | (10,6,3,1,0) | 1 | 2 | 1 |
| 4 | (10,5,4,1,0) | 1 | 2 | 1 |
| 4 | (10,5,3,2,0) | 0 | 1 | 1 |
| 4 | (10,4,3,2,1) | 0 | 0 | 0 |
| 4 | (9,8,2,1,0) | 1 | 1 | 0 |
| 4 | (9,7,3,1,0) | 1 | 2 | 1 |
| 4 | (9,6,4,1,0) | 1 | 3 | 2 |
| 4 | (9,6,3,2,0) | 1 | 2 | 1 |
| 4 | (9,5,4,2,0) | 1 | 2 | 1 |
| 4 | (9,5,3,2,1) | 0 | 1 | 1 |
| 4 | (8,7,4,1,0) | 1 | 2 | 1 |
| 4 | (8,7,3,2,0) | 0 | 1 | 1 |
| 4 | (8,6,5,1,0) | 1 | 1 | 0 |
| 4 | (8,6,4,2,0) | 1 | 3 | 2 |
| 4 | (8,6,3,2,1) | 0 | 1 | 1 |
| 4 | (8,5,4,3,0) | 0 | 1 | 1 |
| 4 | (8,5,4,2,1) | 0 | 1 | 1 |
| 4 | (7,6,5,2,0) | 0 | 1 | 1 |
| 4 | (7,6,4,3,0) | 1 | 1 | 0 |
| 4 | (7,6,4,2,1) | 0 | 1 | 1 |
| 4 | (7,5,4,3,1) | 0 | 1 | 1 |
| 4 | (6,5,4,3,2) | 0 | 0 | 0 |
