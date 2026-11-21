# The complete two-below family in every power

## T-050. Actual cohomology and positive counts for all \(k\ge2\)

Let \(x,b,d\ge0\), \(k\ge2\), and \(2b+x+k\ge6\). Set
\[
\begin{aligned}
n&=d+b+x+k-2,\\
\lambda&=(d+3b+2x+3k-8,d+b+x+2k-2,d+b+x,d+x,d).
\end{aligned}
\tag{ER.1}
\]
For every \(\mu\vdash5\), the coefficient
\(p_{\mu,(n)}^\lambda\) is given by the positive formulas below.
After selecting its parameter branch and residues modulo 60, it is
a sum of at most 55 bounded integer-polytope counts, each with at
most ten variables. The endpoint branches \(k=2,3,4\) need only
seventeen polytopes with at most eight variables, or four with at
most five variables when \(b\) is fixed.

The new actual cohomology comparison is as follows. Put
\(E=\mathfrak h_5\), let \(Q\) be the tautological quotient
on \(\mathbf P(E)\), let \(\mathcal I\) be the ideal of the
five frame points, and write \(a=b+x\), \(c=2k-2\). Then
\[
\boxed{H^1(\mathcal I^k(c)S_{(a,b)}Q)
\simeq\operatorname{Ind}_{S_2\times S_3}^{S_5}
       (\operatorname{sgn}_{S_2}\otimes S_{(a,b)}\mathfrak h_3),
\qquad H^{q\ge2}(\mathcal I^k(c)S_{(a,b)}Q)=0.}
\tag{ER.2}
\]
The isomorphism is induced by the exact polynomial restriction
complex of G-027, as described in §§1–3. It does not enlarge the
asserted range of the different geometric line-restriction map in
T-046 without checking that map. The positive formulas for
\(k\ge5\) are exactly those already proved in T-046; the new
finite branches complete every remaining valid power.

## 1. The actual section and point-jet maps

Set
\[
\alpha=(a+c,b+c,c),\qquad N=|\alpha|=2b+x+6k-6.
\tag{ER.3}
\]
The validity inequality in (ER.1) says exactly \(N\ge5k\).
The determinant shift for Schur bundles gives the actual isomorphism
\[
S_\alpha Q=(\det Q)^c\otimes S_{(a,b)}Q
\simeq\mathcal O(c)\otimes S_{(a,b)}Q,
\tag{ER.4}
\]
because \(\det Q=\det E\otimes\mathcal O(1)\) and the
constant \(S_5\) character \((\det E)^c\) is trivial for
even \(c\). The column-pairing map and chart inverse in G-027
therefore identify the balanced module with
\[
(S_\lambda\mathbf Q^5)_{(n^5)}
\simeq\operatorname{sgn}^{d+a}
H^0(\mathcal I^k(c)S_{(a,b)}Q).
\tag{ER.5}
\]
Here \(\lambda_2-n=k\), and the inverse balanced chart map is
the already specified multiplication by \(u^{-k}\) after the
normal-order condition. The partition, degree and sign are thus
transported by the same actual maps as G-027.

We need the first quotient term of its restriction complex to be
the full point-jet module. This follows from an explicit jet
surjection. The quotient map from \(S_{(a,b)}E\) generates
\(S_{(a,b)}Q\) at every point. Fix a point and choose global
sections whose values span its fiber. For every \(0\le j<k\),
every degree-\(j\) tangent monomial is the leading jet of a
global section of \(\mathcal O(c)\) vanishing to order \(j\),
because \(c=2k-2\ge k-1\). In an affine chart with the point
at its origin, use the corresponding homogeneous monomial times
the nonvanishing chart coordinate to degree \(c-j\).
Multiplying these scalar sections by the chosen quotient-bundle
sections prescribes arbitrary degree-\(j\) jets without changing
lower degrees. Induction on \(j\) prescribes every jet of order
below \(k\).

Consequently the natural map from global sections of (ER.4) onto
the jet space at one point is surjective. G-027's normal-order
substitution proves that its kernel is precisely the Schur
component of \(I_i^k\) in the auxiliary polynomial ring.
Thus its quotient component is the entire point-jet module, by
this specified map. Doing this for all five points gives the
\(S_5\)-equivariant identification of the singleton term of the
restriction complex with the direct sum of the full jet spaces.
Choices of local spanning sections prove surjectivity; the map
itself is the canonical restriction map and hence commutes with
frame permutations.

## 2. Exactly one pair summand and no triple summands

Use \(F=\mathbf Q^3\) in G-027. A subset of size \(s\)
contributes the \(S_\alpha F\) component of
\[
T_k(F)^{\otimes s}\otimes
\operatorname{Sym}(\mathfrak h_{5-s}\otimes F),
\qquad T_k(F)=\bigoplus_{j=0}^{k-1}\operatorname{Sym}^jF.
\tag{ER.6}
\]
The total degree in the first factor is at most \(s(k-1)\).

For \(s=3\), the complementary standard space has dimension one,
so its Cauchy partition has one row. To obtain \(\alpha\),
the truncated factor must supply at least
\(\alpha_2+\alpha_3=b+4k-4\) boxes. This exceeds
\(3(k-1)\) for every \(k\ge2\). Hence the triple term is
zero. Larger subsets already have zero degree-\(N\) component
in the exact complex, since \(N\ge5k\).

For \(s=2\), put \(W=\mathfrak h_3\). A Cauchy partition
from \(\operatorname{Sym}(W\otimes F)\) has at most two rows.
Therefore the truncated factor must supply at least the entire
third row of \(\alpha\), which has length \(c=2k-2\).
But \(2(k-1)=c\) is also its maximum degree. Equality is forced:
both tensor factors have degree \(k-1\), the complementary
partition is \((a+c,b+c)\), and the skew diagram removed is
one horizontal row of length \(c\). Its only Schur type is
\((c)\). Multiplication
\[
\operatorname{Sym}^{k-1}F\otimes\operatorname{Sym}^{k-1}F
\longrightarrow\operatorname{Sym}^{c}F
\tag{ER.7}
\]
therefore induces an isomorphism on the required Schur component;
the kernel has no such component by the just-proved degree and
horizontal-strip calculation. Swapping the two factors fixes this
multiplication, so it introduces no additional \(S_2\) character.

The final Pieri identification also has an explicit polynomial
map. If \(v\) is the row from \(\operatorname{Sym}F\) and
\(z_1,z_2\) are the two rows from \(W\otimes F\), multiply
the usual Cauchy copy of
\(S_{(a,b)}W\otimes S_{(a,b)}F\) in the \(z\) variables by
\(\det(v,z_1,z_2)^c\). This injects into the required component
and gives
\((\det W)^c S_{(a,b)}W\) on its multiplicity space.
The horizontal-strip multiplicity is one, so the injection is
surjective onto that component. Since \(c\) is even,
\((\det W)^c\) is the trivial \(S_3\) character. Finally the
ordered-subset orientation contributes
\(\operatorname{sgn}_{S_2}\). Inducing over the ten pairs gives
exactly the right side of (ER.2).

## 3. The cohomology comparison is an actual cokernel map

Extract the \(S_\alpha F\) component of the exact restriction
complex G-027. Sections 1 and 2 turn it into
\[
0\longrightarrow H^0(\mathcal I^kS_\alpha Q)
\longrightarrow S_\alpha E
\longrightarrow\bigoplus_i\operatorname{Jets}^{<k}_{\ell_i}
 (S_\alpha Q)
\longrightarrow C_2\longrightarrow0,
\tag{ER.8}
\]
where \(C_2\) is the pair module identified by (ER.7) and its
determinant multiplication map. The last arrow in (ER.8) is the
signed quotient map to the pair intersections followed by these
specified Schur-component maps.

The quotient-bundle Young complex in G-027 proves
\(H^0(S_\alpha Q)=S_\alpha E\) and
\(H^{q>0}(S_\alpha Q)=0\). The ideal/jet exact sequence has
the same first restriction map as (ER.8), so its cohomology exact
sequence identifies \(H^1(\mathcal I^kS_\alpha Q)\) with
the same cokernel. The induced map to \(C_2\) is an isomorphism
by exactness of (ER.8). Higher cohomology vanishes because the jet
sheaf has finite support. This proves (ER.2), including its actual
map and every \(k=2,3,4\) endpoint.

## 4. Closed traces and the eight finite endpoint branches

Use the class order \(1^5,21^3,2^21,31^2,32,41,5\) and the
seven character rows fixed in T-044. Write \(h_g(t)\) for the
closed symmetric-power traces there, with \(h_g(t)=0\) for
negative \(t\), and let \(f_g\) be the number of fixed letters.
Put \(a=b+x\),
\[
\begin{aligned}
A_g&=h_g(a)h_g(b)-h_g(a+1)h_g(b-1),\\
B_g&=h_g(a-1)h_g(b)-h_g(a+1)h_g(b-2),\\
C_g&=h_g(a-1)h_g(b-1)-h_g(a)h_g(b-2),\\
U_{g,j}&=h_g(2k-2-j)-f_gh_g(k-1).
\end{aligned}
\tag{ER.9}
\]
The signed tensor Schur complex in the archive appendix computes
the Euler trace as \(A_gU_{g,0}-B_gU_{g,1}+C_gU_{g,2}\).
Its scalar jet trace is \(f_gh_g(k-1)\): at a fixed frame point,
\(E=\mathbf1\oplus\mathfrak h_4\), so the sum of the local
symmetric powers of degrees below \(k\) is
\(\operatorname{Sym}^{k-1}E\) as a stabilizer module. The fiber
of \(\mathcal O(t)\) there is fixed. All three scalar degrees
in (ER.9) are nonnegative when \(k\ge2\).

By the actual isomorphism (ER.2), add the pair trace
\[
\begin{aligned}
L_g(x,b)={}&\bigl(10(x+1),\ 3(-1)^b\mathbf1_{2\mid x}-(x+1),\\
&\quad-2(-1)^b\mathbf1_{2\mid x},\ \tau(x),-\tau(x),0,0\bigr),\\
\tau(x)={}&(1,-1,0)_{x\bmod3}.
\end{aligned}
\tag{ER.10}
\]
Thus the actual zeroth-cohomology trace is
\(A_gU_{g,0}-B_gU_{g,1}+C_gU_{g,2}+L_g\) for every valid
\(k\ge2\). The original T-046 positive formula already treats
all \(k\ge5\). The remaining validity regions are the following
disjoint eight branches; every displayed free variable is
nonnegative.

| Branch | Actual parameters | Free variables |
|---|---|---|
| 1 | \(k=2,\ b=B+2,\ x=X\) | \(X,B\) |
| 2 | \(k=2,\ b=1,\ x=X+2\) | \(X\) |
| 3 | \(k=2,\ b=0,\ x=X+4\) | \(X\) |
| 4 | \(k=3,\ b=B+2,\ x=X\) | \(X,B\) |
| 5 | \(k=3,\ b=1,\ x=X+1\) | \(X\) |
| 6 | \(k=3,\ b=0,\ x=X+3\) | \(X\) |
| 7 | \(k=4,\ b=B+1,\ x=X\) | \(X,B\) |
| 8 | \(k=4,\ b=0,\ x=X+2\) | \(X\) |

For an effective outer label \(\nu\), let \(M_{\nu,B}(Z)\)
be the ordinary seven-class inner product of (ER.9)–(ER.10) on
branch \(B\), at its free parameters \(Z\). This definition
uses only the explicitly fixed closed arithmetic functions and
character rows. Every argument needed in the constants below is
bounded by an absolute constant.

On a two-variable branch, \(M\) is polynomial on each residue
class modulo 60, of separate degrees at most \((3,4)\) and
total degree at most five. The active order set is
\[
\mathcal A=\{(i,j):0\le i\le3,\ 0\le j\le4,\ i+j\le5\},
\qquad |\mathcal A|=17.
\tag{ER.11}
\]
On a one-variable branch its degree is at most three. These are
exact polynomial bounds: substitute the parity and third-residue
formulas for \(h_g\) into (ER.9). At the identity, twelve times
the trace is
\[
(x+1)(b+x+2)(b+1)
\bigl[(2k-1)(b+2k)(b+x+2k+1)-5k(k+1)(k+2)\bigr]
 +120(x+1).
\tag{ER.12}
\]
After every branch shift, all its ordinary coefficients are
positive. Transposition and double-transposition traces have total
degree at most three, three-cycle traces at most one, and the other
classes are periodic. The certificate verifies these symbolic
identities for every phase. The polynomial extensions at \(-1\)
and \(-2\) equal zero, so no omitted initial phase is present.

## 5. The complete positive formula and support

For a branch with free parameter vector \(Z=r+60q\), define
\[
D_{\nu,B,r;i}=\sum_{0\le u\le i}
(-1)^{|i|-|u|}\prod_j\binom{i_j}{u_j}\,
M_{\nu,B}(r+60u).
\tag{ER.13}
\]
The exact certificate `two_below_endpoints_certificate.py` checks
all 1,520,400 constants: three two-variable branches and five
one-variable branches, all residues and all seven labels. Every
constant is a nonnegative integer. Every positive active order is
strictly positive, with minimum 1957; the maximum constant is
3227506200. The proved largest signed-64-bit intermediate bound is
2953681817436672. Exact phase bounds, all per-label hashes, extrema,
active orders and zero residues are saved in
`TWO_BELOW_ENDPOINTS_SUMMARY.json`.

Take \(\nu=\mu\) if \(d+b+x\) is even, and \(\nu=\mu^t\)
otherwise. The endpoint formula is
\[
\boxed{p_{\mu,(n)}^\lambda
=\sum_{i\in\mathcal A_B}D_{\nu,B,r;i}
\prod_j\binom{q_j}{i_j},}
\tag{ER.14}
\]
where \(\mathcal A_B=\mathcal A\) on a two-variable branch
and \(\{0,1,2,3\}\) on a one-variable branch. Newton's exact
finite polynomial identity proves (ER.14) for all parameters;
the exhaustive fixed certificate proves the signs of its constants.

For complete literal inequalities, introduce the fixed quotient
variables \(q_j\), one integer \(y\), and increasing chains
\(z_{j,1},\ldots,z_{j,i_j}\). The polytope for one tag is
\[
60q_j=Z_j-r_j,\quad q_j\ge0,\qquad
0\le y<D_{\nu,B,r;i},\qquad
0\le z_{j,1}<\cdots<z_{j,i_j}<q_j.
\tag{ER.15}
\]
Strict integer inequalities are replaced by upper bounds minus one.
Its integer points choose one coefficient copy and one subset of
size \(i_j\) in each interval, proving the lattice-count
bijection. The maximum chain length is five in the two-variable
branches and three in the others, giving eight or five variables.
The previously proved \(k\ge5\) branch has the stated 55-tag,
ten-variable bound. Every witness has logarithmic bit length in
the input parameters, plus fixed absolute constants.

Because every first-order constant is positive, endpoint zeros
are confined to the residue boxes. In actual coordinates, the
complete eighteen new exceptions are:

| Effective label \(\nu\) | \((k,x,b)\) |
|---|---|
| \((5)\) | \((2,0,3)\), \((2,2,1)\), \((3,1,1)\), \((4,0,1)\) |
| \((3,2)\) | \((4,0,1)\) |
| \((3,1,1)\) | \((2,0,2)\), \((2,4,0)\) |
| \((2,1,1,1)\) | \((2,0,2)\), \((2,4,0)\) |
| \((1^5)\) | \((2,0,3)\), \((2,1,2)\), \((2,2,1)\), \((2,4,0)\), \((2,5,0)\), \((2,7,0)\), \((3,1,1)\), \((3,4,0)\), \((4,0,1)\) |

The labels \((4,1)\) and \((2,2,1)\) have no endpoint zero.
Together with the six valid exceptions in T-046, this is the
complete support description for the whole family. Convert the
effective label by the sign rule preceding (ER.14).

## 6. Direct evaluator, independent checks and scope

`two_below_all_positive.py` selects the branch, evaluates only the
fixed bounded constants, and returns (ER.14), or the already proved
T-046 count for \(k\ge5\). With `--polytopes` it exports all
constraint matrices in (ER.15). It calls no representation library,
elimination routine or input-dependent coefficient oracle.
Its continuation and branch checks passed 1960 comparisons,
including both determinant parities, and its 49 literal polytope
checks verified every one of 51 witnesses. The receipt is
`TWO_BELOW_ALL_EVALUATOR_CHECK.json`.

The rectangular agent independently checked all 791 valid
\(k=2,3,4\) coefficients through \(n\le6\), for every outer
label, by the cycle-index/Murnaghan–Nakayama calculation on the
actual plethysm side and literal fixed-pair induction on the
proposed side. All passed; the receipt is
`work/rectangular/OUTER5_TWO_BELOW_ENDPOINTS_CHECK.tsv`.
The complete proof above has been read and checked independently
by the rectangular and archive agents. The archive agent also
independently reconstructed all 1,520,400 constants using ambient
three-by-three Jacobi–Trudi characters, actual point jets, literal
fixed-pair induction and successive quotient-index differences.
All 56 per-branch/per-label hashes, extrema, active sets and the
eighteen endpoint exceptions agree; its receipt is
`work/archive/TWO_BELOW_ENDPOINTS_INDEPENDENT_RECEIPT.json`.
The whole-proof readings and the finite reconstructions are
recorded as distinct check events.

The primary inputs are the exact Cauchy and Young-projector maps,
the G-027 restriction complex and T-049 product-ideal comparison,
and the fully specified signed tensor Schur complex in the archive
appendix. Their source locators and complete proofs are retained in
those reports. The new work is the exact degeneration of the
restriction complex to (ER.8), the actual endpoint cohomology map,
the eight exhaustive positive branches, and the complete support
extension. No historical novelty claim is made.
