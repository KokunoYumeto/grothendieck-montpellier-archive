# The complete three-below family, including triple intersections

## T-051. Positive formulas for every possible power

Let \(k\ge2\), \(x,b,d\ge0\), and \(2b+x+k\ge9\). Put
\[
n=d+b+x+k-3,\qquad
\lambda=(d+3b+2x+3k-12,d+b+x+2k-3,d+b+x,d+x,d).
\tag{ET.1}
\]
Every coefficient \(p_{\mu,(n)}^\lambda\), \(\mu\vdash5\),
has the explicit positive formula in §4. It uses at most 55 bounded
integer polytopes of at most ten variables after selecting its
branch and residues. The new endpoints \(2\le k\le7\) use at
most seventeen polytopes of eight variables, or four of five
variables on branches with fixed \(b\).

The proof evaluates the entire exact arrangement restriction
complex. Three small endpoint sectors have a nonzero triple term;
their actual representations and quotient maps are retained rather
than omitted. The positive formula for \(k\ge8\) is T-048.
No historical novelty claim is made.

## 1. Actual jet comparison and the exact pair-to-triple sequence

Write \(a=b+x\), \(c=2k-3\), and
\(\alpha=(a+c,b+c,c)\). Then
\[
|\alpha|=2b+x+6k-9\ge5k.
\tag{ET.2}
\]
G-027 therefore gives its exact degree-\(|\alpha|\) restriction
complex. The determinant shift is
\[
S_\alpha Q=(\det E)^c\mathcal O(c)S_{(a,b)}Q
=\operatorname{sgn}_5\,\mathcal O(c)S_{(a,b)}Q,
\tag{ET.3}
\]
since \(c\) is odd. Also \(c\ge k-1\). The explicit
triangular jet-surjection proof in T-050 §1 consequently applies:
multiply scalar degree-\(c\) sections with arbitrary leading jets
through order \(k-1\) by global sections generating
\(S_{(a,b)}Q\), and prescribe the homogeneous jet layers in
order. Hence the singleton quotient in the arrangement complex is
the entire point-jet module, by the natural restriction map.

Since \(S_\alpha Q\) is acyclic in positive degrees, the same
cokernel comparison as (ER.8) gives the actual exact sequence
\[
0\longrightarrow H^1(\mathcal I^k(c)S_{(a,b)}Q)
\longrightarrow K_2\longrightarrow K_3\longrightarrow0,
\qquad H^{q\ge2}(\mathcal I^k(c)S_{(a,b)}Q)=0.
\tag{ET.4}
\]
Here \(K_s\) is the \(s\)-subset term of G-027, including its
orientation, and then tensored by \(\operatorname{sgn}_5\)
to undo (ET.3). The map \(K_2\to K_3\) is the signed
polynomial quotient map of that complex followed by the specified
Schur-component identifications. This defines every map in (ET.4).

The balanced flag map still has the original sign
\[
(S_\lambda\mathbf Q^5)_{(n^5)}
\simeq\operatorname{sgn}^{d+a}
H^0(\mathcal I^k(c)S_{(a,b)}Q).
\tag{ET.5}
\]
Indeed \(\lambda_2=d+a+c\), and the sign from (ET.3) cancels
its odd \(c\). The chart inverse and normal-order comparison
are the actual ones of G-027, with \(\lambda_2-n=k\).

## 2. The pair term in every power

For a pair, put \(P=\mathbf Q^2\), with the endpoint permutation
action, and \(W=\mathfrak h_3\) for its complement. The exact
pair module, after the sign in (ET.3), is
\[
\begin{split}
K_2\simeq\operatorname{Ind}_{S_2\times S_3}^{S_5}\bigl(
&\det P\otimes P\otimes S_{(a,b)}W\\
&\oplus\det P\otimes W^*\otimes S_{(a,b)}W\\
&\oplus S_{(a-1,b)}W\oplus S_{(a,b-1)}W\bigr).
\end{split}
\tag{ET.6}
\]
The third summand is omitted at \(x=0\), and the fourth at
\(b=0\). This is the already evaluated four-summand module of
T-047 at defect three, now obtained directly for every \(k\ge2\).

Here is the complete two-slot calculation establishing (ET.6).
The truncated slots have total degree at most \(2k-2=c+1\).
The complementary Cauchy partition has at most two rows, so those
slots must supply the third row of length \(c\). There are only
two degrees to examine.

At degree \(c\), the slot degrees are
\((k-1,k-2)\) or \((k-2,k-1)\). Multiplication onto
\(\operatorname{Sym}^cF\) and the determinant polynomial map
used in (ER.7) identify their contribution with
\(P\otimes S_{(a,b)}W\) after orientation and (ET.3).
The standard intertwiner
\[
v_1e_1+v_2e_2\longmapsto
(e_1\wedge e_2)\otimes(v_1e_2-v_2e_1)
\tag{ET.7}
\]
identifies this with \(\det P\otimes P\otimes S_{(a,b)}W\).

At degree \(c+1\), both slots have degree \(k-1\). Only the
two Schur types \((c+1)\) and \((c,1)\) can contribute.
Their slot-exchange signs are respectively plus and minus: their
highest polynomials are
\(u_1^{k-1}v_1^{k-1}\) and
\((u_1v_2-u_2v_1)u_1^{k-2}v_1^{k-2}\).
Remove one further box from either of the first two rows of
\(\alpha\). If \(x>0\), removing the end of its first row
leaves a skew row of length \(c\) and one box in a different
column, so both types occur once. If \(b>0\), the same holds
when removing the end of its second row. If \(b=0\), that
second-row box shares the last column of the third row, so only
\((c,1)\) occurs. At \(x=0\), first-row removal is not a
partition and contributes nothing. These are all cases.

The maps are the corresponding row symmetrizers and column
antisymmetrizers, fixed by the displayed highest coefficients,
followed by Cauchy extraction. Equivalently, use the explicit
rank-two dual Pieri decomposition of
\(W^*\otimes S_{(a,b)}W\). For \(b\ge1\), its summands
are \(S_{(a-1,b)}W\) when \(x>0\), and
\(S_{(a,b-1)}W\). At \(b=0\), its second summand is the
actual rational representation
\((\det W)^{-1}\operatorname{Sym}^{a+1}W\), and its first
is present precisely when \(a>0\). The multiplication and
determinant highest-vector maps for this rank-two decomposition
are those fully proved in T-047. Keeping this second summand at
\(b=0\), and using the two slot-exchange signs just computed,
gives exactly the last three terms of (ET.6). This proves the
formula also at \(x=0\), \(b=0\) and \(k=2\).

## 3. Every triple term and its exact action

For three selected slots, the complementary standard space is the
one-dimensional sign representation of \(S_2\). A complementary
Cauchy partition has one row. The truncated factor must therefore
supply at least
\(\alpha_2+\alpha_3=b+4k-6\) boxes, and can supply at most
\(3(k-1)\). Thus
\[
K_3=0\qquad\text{whenever }b+k\ge4.
\tag{ET.8}
\]
The remaining possibilities are precisely \((k,b)=(3,0),(2,1)\)
and \((2,0)\). In the following formulas the second subgroup is
the two-letter complement:
\[
\boxed{
K_3=\begin{cases}
\operatorname{Ind}_{S_3\times S_2}^{S_5}
(\operatorname{sgn}_3\otimes\operatorname{sgn}_2^x),&(k,b)=(3,0),\\
\operatorname{Ind}_{S_3\times S_2}^{S_5}
([2,1]\otimes\operatorname{sgn}_2^{x+1}),&(k,b)=(2,1),\\
\operatorname{Ind}_{S_3\times S_2}^{S_5}
(([2,1]\oplus\operatorname{sgn}_3)\otimes
 (\mathbf1\oplus\operatorname{sgn}_2)),&(k,b)=(2,0).
\end{cases}}
\tag{ET.9}
\]

For \((3,0)\), the only normal degree is six: each slot has
degree two and the required normal Schur type is \((3,3)\).
Its multiplicity is one. Indeed, among the shapes in
\(S_{(2)}F\otimes S_{(2)}F\), only \((3,1)\) can acquire
a horizontal two-strip to give \((3,3)\). Its actual highest
vector in three slot rows is the product of brackets
\([uv][uw][vw]\), using the first two column coordinates.
It has degree two in each row and changes by the sign of a row
permutation. The complementary row has degree \(x+3\).
The \(S_3\) orientation and the \(S_3\) part of (ET.3)
cancel; the complementary sign becomes
\((-1)^{x+3+1}=(-1)^x\). This proves the first line of
(ET.9), with its concrete highest-vector map.

For \((2,1)\), every selected slot has degree one. The lower
two rows of \(\alpha=(x+2,2,1)\) force the normal Schur
type \((2,1)\), whose multiplicity in \(F^{\otimes3}\)
is the literal Specht module \([2,1]\) under the Young
projector. The complementary row has degree \(x+2\), giving
the sign \((-1)^{x+3}\) after (ET.3). The two \(S_3\)
signs again cancel, proving the second line.

For \((2,0)\), normal degrees two and three both occur.
At degree two, choose two nonempty slots and extract
\(\Lambda^2F\). Their action is
\(\operatorname{Ind}_{S_2}^{S_3}\operatorname{sgn}_2
=[2,1]\oplus\operatorname{sgn}_3\), and the complementary
row has degree \(x+1\). At degree three, the skew diagram
\((x+1,1,1)/(x)\) has Schur types \((2,1)\) and
\((1,1,1)\), each once; the actual maps are their Young
symmetrizer projections on \(F^{\otimes3}\). The same
two multiplicity modules occur, while the complementary row has
degree \(x\). Validity here gives \(x\ge7\), so neither
skew-diagram boundary is exceptional. After orientation and (ET.3),
the two complementary signs are \((-1)^x\) and
\((-1)^{x+1}\). Their sum is the fixed two-letter permutation
module, proving the last line of (ET.9).

These arguments define the triple identifications by polynomial
highest vectors and the specified rational Young projectors.
The map in (ET.4) remains the actual signed quotient map, not an
unspecified map between equal-dimensional representations.

In the fixed seven-class order, the triple traces are respectively
\[
\begin{aligned}
Q^{30}(x)&=(10,-3+(-1)^x,-2(-1)^x,1,(-1)^x,0,0),\\
Q^{21}(x)&=(20,2(-1)^{x+1},0,-1,(-1)^x,0,0),\\
Q^{20}&=(60,-6,0,0,0,0,0).
\end{aligned}
\tag{ET.10}
\]
They can be checked directly by summing fixed two-letter
complements: a fixed pair of letters or a two-cycle, with the
literal sign or standard character on the remaining three letters.

## 4. Complete positive endpoint certificates

Let \(P_g(x,b,k;c)\) be the explicit three-term Euler expression
(ER.9), with \(c=2k-3\). Let \(J_g^{(3)}(x,b)\) be the
four-summand pair traces (F.6)–(F.7), and let \(Q_g(x,b,k)\)
be (ET.10) on its three sectors and zero elsewhere. Exactness of
(ET.4) proves the actual zeroth-cohomology trace
\[
P_g(x,b,k;2k-3)+J_g^{(3)}(x,b)-Q_g(x,b,k).
\tag{ET.11}
\]
The scalar degree \(c-2=-1\) at \(k=2\) is handled by the
acyclic line bundle \(\mathcal O(-1)\) and the already fixed
zero convention for \(h_g(-1)\). No value is extrapolated past
an unproved initial range.

T-048 proves a positive formula for every \(k\ge8\). For each
\(k\in\{2,3,4,5,6,7\}\), set
\[
R_k=9-k,\qquad B_k=\lceil R_k/2\rceil.
\tag{ET.12}
\]
Use one branch \(b=B+B_k,x=X\), \(X,B\ge0\), and for
each \(0\le b_0<B_k\) use the branch
\(b=b_0,x=X+R_k-2b_0\), \(X\ge0\). These six
two-variable branches and fifteen one-variable branches are
disjoint and cover every valid endpoint. The three nonzero
corrections (ET.10) occur only in the indicated fixed-\(b\)
branches.

Pair (ET.11) with each fixed \(S_5\) character row. On a
two-variable branch, every residue function modulo 60 has separate
degrees at most \((3,4)\) and total degree at most five; its
active orders are the seventeen pairs (ER.11). On a one-variable
branch its degree is at most three. These statements are verified
by exact symbolic identities in the certificate: the identity
Euler trace is
\[
\frac{(x+1)(b+x+2)(b+1)}{12}
\bigl[(c+1)(b+c+2)(b+x+c+3)-5k(k+1)(k+2)\bigr],
\qquad c=2k-3.
\]
Add the pair dimension
\(60(x+1)\) for \(b>0\) or \(50x+40\) for \(b=0\),
and subtract the triple dimension 10, 20 or 60 on the three sectors. After each
shift in (ET.12), all its ordinary coefficients are positive.
The nonidentity degree bounds are three, three and one on the
transposition, double-transposition and three-cycle classes;
the remaining classes are periodic. All negative arguments are
\(-1\) or \(-2\), where the fixed residue expressions equal
zero exactly.

Define the bounded constants by the finite difference (ER.13),
now using the actual trace (ET.11) and the 21 branches (ET.12).
`three_below_endpoints_certificate.py` verifies all 3,049,200
integers. Every constant is nonnegative; every positive active
order is strictly positive, with minimum 941. The maximum
constant is 5668963200, and the largest proved signed-64-bit
intermediate bound is 5188937807741952. Exact symbolic degree
checks, all hashes, extrema and zero residues are saved in
`THREE_BELOW_ENDPOINTS_SUMMARY.json`.

For \(\nu=\mu\) or \(\mu^t\) according as \(d+b+x\) is
even or odd, the positive formula is
\[
\boxed{p_{\mu,(n)}^\lambda
=\sum_{i\in\mathcal A_B}D_{\nu,B,r;i}
\prod_j\binom{q_j}{i_j},\qquad Z=r+60q.}
\tag{ET.13}
\]
Here \(Z\) is the free vector in its selected branch,
\(\mathcal A_B\) is (ER.11) or \(\{0,1,2,3\}\), and
\(D\) is the finite difference just defined. Newton's polynomial
identity proves equality for all parameter values, and the fixed
exhaustive certificate proves positivity. The complete literal
polytope matrices are (ER.15), with these parameters and constants.
The coefficient interval and increasing-chain bijection is
unchanged, proving the stated eight- or five-variable bounds.
Use T-048's already proved count for \(k\ge8\).

All first-order constants are positive, so the endpoint zero sets
are confined to their residue boxes. There are exactly 38 new
effective-label exceptions, retained as actual \((k,x,b)\)
triples in the fixed summary and obtained from its zero residues
by (ET.12). Together with T-048's seven valid exceptions, these
give a complete finite support decision for the whole family.
The evaluator performs precisely that branch and parity conversion.

## 5. Direct evaluator and proof status

`three_below_all_positive.py` computes (ET.13) using bounded
closed arithmetic constants and exports the complete integer
constraint matrices with `--polytopes`. It calls no representation
library, elimination routine or input-dependent multiplicity
oracle. Its direct continuation and branch checks passed 4312
comparisons, including both determinant parities. Its 147 literal
polytope checks verified all 398 witnesses. The receipt is
`THREE_BELOW_ALL_EVALUATOR_CHECK.json`.

The complete new proof has been read and checked independently by
the root, archive and rectangular agents. The rectangular agent independently
compared all 1561 valid \(2\le k\le7,n\le7\) coefficients,
for every outer label; 84 of those cases use an exceptional triple
module. Its comparison summed the literal cycle-stable three-subsets
and their restricted \(S_3\times S_2\) characters, rather than
calling (ET.10) or the endpoint evaluator. Every comparison passed;
the receipt is
`work/rectangular/OUTER5_THREE_BELOW_ENDPOINTS_CHECK.tsv`.
The archive agent independently reconstructed all 3,049,200 fixed
constants from the odd-sign-twisted ambient three-row Jacobi--Trudi
character, full point jets, literal fixed-pair induction and literal
fixed-triple induction. Its unbounded-integer successive-difference
calculation matched all 147 branch/label hashes, every active order
and extremum, and all 38 endpoint zeros. The independent receipt is
`work/archive/THREE_BELOW_ENDPOINTS_INDEPENDENT_RECEIPT.json`;
the complete proof review and reconstruction are recorded as A-056.
The source inputs
are G-027/T-049's exact arrangement construction, the signed tensor
Schur complex, and the explicitly proved Cauchy, Pieri and
rank-two maps in T-047. The added work is the all-power pair
calculation, all three actual triple modules, their quotient
sequence, the 21 positive endpoint branches and their direct
bounded-polytope implementation.
