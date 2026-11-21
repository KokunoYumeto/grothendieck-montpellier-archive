# All two-row quotient shapes one degree below the quadratic ray

## T-045. Statement and exact family

Let \(k\ge1\), \(x,b,d\ge0\), with \(2b+x+k\ge3\). Put
\[
\begin{aligned}
n&=d+b+x+k-1,\\
\lambda&=(d+3b+2x+3k-4,d+b+x+2k-1,
                    d+b+x,d+x,d).
\end{aligned}
\tag{B.1}
\]
These inequalities make \(\lambda\) a partition of \(5n\).
For every \(\mu\vdash5\), its plethysm coefficient has the positive
polytope formulas in §4. For \(k\ge2\), selecting three residues
leaves at most 55 polytopes with at most ten integer variables.
For \(k=1,b\ge1\), there are at most seventeen contributing
polytopes with at most eight variables. For \(k=1,b=0\), validity
means \(x\ge2\), and the coefficient is given by the explicit
rank-four hook table already proved in T-041.

This reaches line twist \(c=2k-1\) for every valid shape, including
the first-power endpoint. Every map and exceptional cohomology group
needed for that endpoint is specified below. No assertion about
\(c\le2k-2\) is included here.

## 1. Exact flag transport

Retain \(E=\mathfrak h_5\), \(Z\), \(\mathcal I\), \(L\), and
\(Q\) from T-044, and put \(a=b+x\). Define
\[
N_{x,b,k}=H^0(\mathbf P(E),\mathcal I^k(2k-1)S_{(a,b)}Q).
\tag{B.2}
\]
The relative quotient flag has weight \((a,x,0)\) on \(Q^*\)
and first-line twist \(a+2k-1\), after removing determinant power
\(d\). The perfect exterior-column pairing
\(S_{(a,x)}Q^*=(\det Q^*)^aS_{(a,b)}Q\), together with
\(\det Q^*=\det E^*\mathcal O(-1)\), gives
\[
\boxed{(S_\lambda\mathbf Q^5)_{(n^5)}
 \simeq\epsilon^{d+b+x}\otimes N_{x,b,k}.}
\tag{B.3}
\]
The point order is \(\lambda_2-n=k\), and the inverse chart map
is \(F\mapsto u^{-k}F(v(X))\). The same independent transverse
coordinates of G-015 identify regular extension with \(\mathcal I^k\).
The partition inequality in (B.1) is exactly \(\lambda_1\ge\lambda_2\).

## 2. Complete vanishing for \(k\ge2\)

Tensor the locally split Schur complex (R.4), with its specified signed
tensor differential, by \(\mathcal I^k(2k-1)\). Its scalar twists
are now \(2k-1,2k-2,2k-3\). A-029 gives
\(H^1(\mathcal I^k(2k-1))=0\) for \(k\ge2\), since the ordinary
power has a \(2k\)-linear resolution. Its other positive cohomology
also vanishes. Every scalar term has no \(H^2\) or \(H^3\): its
twist is at least one, and the quotient has finite support.
Only the earlier terms can have \(H^1\), in total degrees zero and
minus one. The exact complex therefore proves
\[
H^{i>0}(\mathcal I^k(2k-1)S_{(a,b)}Q)=0\quad(k\ge2).
\tag{B.4}
\]
This retains, rather than discards, possible first cohomology of
\(\mathcal I^k(2k-2)\) and \(\mathcal I^k(2k-3)\).

## 3. The actual first-power map

At \(k=1\) the scalar top twist is one. The five evaluation
sequences give
\[
H^1(\mathcal I(1))=\mathbf Q,\qquad
H^1(\mathcal I)=E,\qquad
H^1(\mathcal I(-1))=\mathbf Q\oplus E,
\tag{B.5}
\]
and every zeroth cohomology group in these three twists is zero.
There is no \(H^2\) or \(H^3\). These identifications are actual
maps, as follows. Point evaluation identifies the five fibers with
\(P=\mathbf Q^5\), using the literal fixed representatives
\(\ell_i\) to trivialize each line. For twist zero the constant
image is \(\mathbf Q\mathbf1\); the map
\[
P/\mathbf Q\mathbf1\longrightarrow E,
\qquad[(c_i)]\longmapsto\sum_i c_i\ell_i
\tag{B.6}
\]
is an equivariant isomorphism. For twist one, the linear evaluation
image is the zero-sum subspace of \(P\); its cokernel is identified
with \(\mathbf Q\) by \((c_i)\mapsto\frac15\sum_i c_i\).
At twist minus one the entire fiber space is the cokernel.

In these identifications, multiplication by a linear form \(\phi\)
induces
\[
H^1(\mathcal I)\longrightarrow H^1(\mathcal I(1)),
\qquad v\longmapsto\frac15\phi(v).
\tag{B.7}
\]
Indeed its fiber values are \(c_i\phi(\ell_i)\); averaging them
is exactly the displayed expression after (B.6).

Apply (B.7) to the actual tensor-slot differential. The last map of
the row of first cohomology in the Schur complex is
\[
\frac15D:
E\otimes\bigl(S_{(a-1,b)}E\oplus S_{(a,b-1)}E\bigr)
\longrightarrow S_{(a,b)}E,
\tag{B.8}
\]
where \(D\) is the sum of the specified Schur insertion maps; invalid
partition summands are omitted. It is onto for \(a+b>0\).
Here is a right inverse with its scalars fixed in the same tensor
model. On a degree-\(a+b\) tensor, mark each tensor position in turn,
remove its vector into an extra factor \(E\), and replace that
position by the formal line position. Sum over the positions, apply
the primitive Young projector, and use the inverse branching matrices
of (S.4). This is the polarization map
\(\delta:S_{(a,b)}E\to E\otimes(S_{(a-1,b)}E\oplus S_{(a,b-1)}E)\).
Inserting the marked vector back into its position gives the original
projected tensor in each of the \(a+b\) terms. Thus
\(D\delta=(a+b)\operatorname{id}\), so
\(5\delta/(a+b)\) is a right inverse of (B.8).

The only positive total-degree cohomology of the Schur complex is the
cokernel of (B.8). It is zero. Thus (B.4) also holds at \(k=1\)
for every nonempty shape \((a,b)\). At the empty shape the target
is \(\mathcal I(1)\), with first cohomology \(\mathbf Q\); that
case is excluded by \(2b+x+k\ge3\). Every valid endpoint is now
proved by an explicit map.

For \(b=0\) the complex has only two terms. Its zeroth cohomology is
the kernel of ordinary multiplication, so for \(x=a\ge2\),
\[
\boxed{N_{x,0,1}=S_{(x-1,1)}E.}
\tag{B.9}
\]
The multiplication is split by the same polarization. This is an
actual module isomorphism, not just a character equality.

## 4. Exact traces, positive constants and polytopes

Use the seven closed traces and fixed character rows (R.6)–(R.7).
With the same \(A_g,B_g,C_g,J_g\), the just-proved vanishing gives
the actual character
\[
\boxed{P_g^-(x,b,k)=A_g(h_g(2k-1)-J_g(k))
-B_g(h_g(2k-2)-J_g(k))+C_g(h_g(2k-3)-J_g(k)).}
\tag{B.10}
\]
This formula also computes the Euler character at the excluded empty
shape. In every domain used below it computes the actual module.

### All \(k\ge2\)

Write \(k=K+2\). On each residue class in \((x,b,K)\), (B.10)
is a polynomial of separate degrees at most \((3,4,3)\). Its
identity dimension is
\[
\frac{(x+1)(b+x+2)(b+1)}{12}
\bigl[(2K+4)(b+2K+5)(b+x+2K+6)
       -5(K+2)(K+3)(K+4)\bigr].
\tag{B.11}
\]
All nonzero ordinary coefficients are positive. Its total degree is
six and its nonzero difference orders are precisely the 55-element
set (R.10). The exact nonidentity phase-polynomial checks are the
same substitutions as in T-044, with the new scalar arguments. The
only possible negative indices are \(-1,-2\) in the Schur terms,
already included in (R.6)'s extension convention. Every scalar ideal
twist is positive in this shifted range.

Define constants by the finite difference (R.9), replacing its module
multiplicity by that from (B.10) and replacing the third parameter
by \(K\). `two_row_below_ray_certificate.py` runs the independently
specified three-product calculation with point shift two and degree
shift three. It checks all 120,960,000 constants. They are all
nonnegative; all 54 nonconstant active orders are strictly positive,
with minimum 899. The maximum is 167679396000, below \(2^{38}\).
There are exactly 25 identically zero difference orders. The maximum
proved signed-64-bit weighted bound is 20121529140000; all divisions
are exact. Complete minima, maxima, phase degrees, zero triples,
intermediate bounds and hashes are in `TWO_ROW_BELOW_RAY_SUMMARY.json`.

The positive formula is therefore (R.11), with \((x,b,K)\) in place
of \((x,b,k)\), and the same effective label
\(\nu=\mu\) or \(\mu^t\) according to \(d+b+x\). The actual
polytopes are exactly (R.12), with the new finite constants. The
proof of the subset-chain bijection gives at most 55 contributing
polytopes and at most ten variables. The sole invalid triple
\((x,b,K)=(0,0,0)\) has zero section module but is excluded from
the partition statement. The summary contains the complete 34 zero
triples, including that harmless invalid one in each label's row.

### The first power with \(b\ge1\)

Put \(b=B+1\), \(B\ge0\). The scalar classes in (B.5) give
\[
\operatorname{tr}N_{x,B+1,1}
 =-A_g+\chi_E(g)B_g-(1+\chi_E(g))C_g.
\tag{B.12}
\]
The same residue formulas prove degrees at most \((3,4)\), total
degree five at the identity, and at most three for all nonidentity
phase polynomials. The seventeen active orders are
\[
\begin{gathered}
(0,0),(0,1),(0,2),(0,3),(0,4),\\
(1,0),(1,1),(1,2),(1,3),(1,4),\\
(2,0),(2,1),(2,2),(2,3),(3,0),(3,1),(3,2).
\end{gathered}
\tag{B.13}
\]
The exact certificate `two_row_first_power_boundary.py` checks all
\(7\cdot60^2\cdot4\cdot5=504000\) constants; all are nonnegative.
The maximum is 899449200, below \(2^{30}\). All first directional
constants are positive. The complete minima, maxima, zero pairs and
hashes are retained in `TWO_ROW_FIRST_POWER_SUMMARY.json`.

The two-variable Newton formula and subset-chain construction give
at most seventeen contributing polytopes with variables
\(q_1,q_2,y\) and at most five chain coordinates. This is the
promised bound of eight variables. Every constant is explicitly
computed from (B.12), the fixed seven rows, and the finite difference
with indices at most \((3,4)\).

### The first power with \(b=0\)

Use the actual identification (B.9). The seven rational hook series
and all their positive tags were proved in T-041. More explicitly,
the multiplicity of \([\nu]\) in \(S_{(x-1,1)}E\) is the sum of
the counts \(2z_2+3z_3+4z_4+5z_5=x-1-j\), one for each shift
\(j\) in its row of the fixed `FOUR` table in
`five_point_hook_positive.py`; for the trivial row, also use the
three shifts 5,6,7 with weights 2,3,5. Every variable is nonnegative.
There are at most eighteen tags, each of dimension at most four.
Repeated shifts are separate tags. The relevant effective label is
again \(\mu\) or \(\mu^t\) according to \(d+x\).

These three disjoint parameter domains cover (B.1). Each formula is
an unconditional equality with an explicit bounded lattice count.

`two_row_positive.py --ray below` evaluates these three branches and
exports every matrix of the selected polytopes. The first-power hook
coin counts are evaluated through the fixed positive numerator over
\((1-t^{60})^r\), so its arithmetic count also has boundedly many
operations rather than a loop up to the input degree. The shared
evaluator check, extended through T-046, passed 1882 exact continuation,
branch and fixed-coin comparisons and 57 literal matrix witnesses.

## 5. Source and check record

The exact Schur construction is (S.1)–(S.5) in the fully checked
archive appendix. The only scalar regularity input is the applied
A-029 result based on
[Kustin–Polini–Ulrich, formula (6.1.4), p.1509, Lemma 6.3 and Corollary 6.4, p.1510](https://msp.org/ant/2017/11-7/ant-v11-n7-p01-p.pdf).
Projective scalar cohomology is
[Stacks Project, Lemma 30.8.1](https://stacks.math.columbia.edu/tag/01XS).
The first-power extension is proved here by (B.6)–(B.8), not inferred
from that regularity result. The precise relative Schur convention is
[Magyar, Propositions 1 and 4](https://arxiv.org/pdf/alg-geom/9411014),
with determinant transport written in §1.

The computations are exact integer and rational certificates, with
the finite constants fully specified by the displayed expressions;
they are not proof-assistant formalizations. T-044 and G-021 supply
independent overlap at the adjacent twist. The remaining lower twists
have actual line-obstruction cohomology, whose maps are a separate
active problem and are not assumed evaluated by this theorem.

The rectangular agent independently checked all 1337 valid actual
plethysm coefficients with \(n\le6\), for all seven outer labels,
including both first-power branches. It used cycle-index expansion
and Murnaghan–Nakayama on the plethysm side and direct Schur/Euler/jet
traces on the proposed side, without the Newton constants. All passed;
its receipt is `work/rectangular/OUTER5_BELOW_RAY_INDEPENDENT_CHECK.tsv`.
