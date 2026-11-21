# Complete support on the two outer equal-row walls

## G-029. Two full wall classifications

Let \(\lambda\vdash5n\), padded to five entries. This theorem
classifies every outer-label coefficient on either wall
\[
\lambda_1>\lambda_2>\lambda_3>\lambda_4=\lambda_5,
\qquad
\lambda_1=\lambda_2>\lambda_3>\lambda_4>\lambda_5.
\tag{EW.1}
\]
The exact exceptional values are the twelve finite points and six
rays in §3, after the following specified transformation.

Put \(d=\lambda_5\) and \(g_i=\lambda_i-\lambda_{i+1}\).
On the first wall use \((a,b,c)=(g_1,g_2,g_3)\) and \(e=d\).
On the second use \((a,b,c)=(g_4,g_3,g_2)\) and
\(e=d+g_2+g_3+g_4\). Take the effective outer label
\(\nu=\mu\) at even \(e\), and \(\nu=\mu^t\) at odd \(e\).
The tables give all seven exact multiplicities at their listed
points and rays. Every coefficient at every other input on these
walls is strictly positive. Thus they give a complete nonvanishing
decision, with no unevaluated coefficient.

The proof uses a closed graph of 24 deficient states and 192
verified generator transitions, together with actual section embeddings
and stable-section isomorphisms. The graph and all its integer traces
are delivered, and its finite closure is proved to exhaust the
infinite parameter set.

## 1. Actual normalization, complementary pairing and stable maps

On the first wall determinant removal gives
\[
\lambda^0=(a+b+c,b+c,c,0,0),\qquad
n_0=(a+2b+3c)/5.
\tag{EW.2}
\]
Multiplication by the determinant section to power \(d\) identifies
the balanced modules with sign twist \(\epsilon^d\).
For the second wall, remove the same determinant and put
\(H=g_2+g_3+g_4\). Its normalized shape is
\((H,H,g_3+g_4,g_4,0)\). The perfect exterior-column pairing
in width \(H\) sends it to the dual of
\((H,g_2+g_3,g_2,0,0)\), tensored by \(\det^H\).
Its gaps are exactly \((g_4,g_3,g_2,0)\), and balanced content
changes from \(n-d\) to \(H-(n-d)\). Every S5 irreducible is
self-dual. This proves the stated transformation and exponent \(e\)
by actual pairings, including both signs.

For (EW.2), G-027 gives
\[
k=\max(0,b+c-n_0),\qquad
\alpha=(b+c,b+c,b).
\tag{EW.3}
\]
Consequently \(k=0\) is exactly \(a\ge3b+2c\). In this range
the actual quotient-section and balanced-chart maps give
\[
(S_{\lambda^0}\mathbf Q^5)_{(n_0^5)}
\simeq\epsilon^{b+c}S_{(b+c,b+c,b)}\mathfrak h_5.
\tag{EW.4}
\]
The right side is independent of \(a\). Increasing \(a\) by five
increases \(n_0\) by one and leaves (EW.3), the sign and that
module unchanged. On the chart the comparison multiplies by
\(u=\prod_iX_{i1}\); its inverse is the common section model.
This is an isomorphism because both section spaces have that same
unconstrained \(k=0\) model. Thus each stable step uses a specified map.

For the finite graph use the parity-preserving normal form
\[
N(a,b,c)=
\begin{cases}
(a,b,c),&a<3b+2c,\\
(3b+2c+((a-3b-2c)\bmod10),b,c),&a\ge3b+2c.
\end{cases}
\tag{EW.5}
\]
The subtraction is a nonnegative multiple of ten, and (EW.4)
proves equality of every coefficient before and after it.
All congruences and positive-gap conditions are preserved.

## 2. Finite seeds, generators and proof of exhaustion

Write \((a,b,c)=(1,1,1)+p+2t\), with
\(p\in\{0,1\}^3\). Choose a componentwise minimal \(u\le t\)
such that the weighted sum of \((1,1,1)+p+2u\) is zero modulo five.
Its total is at most four: five indexed residues have two equal
partial sums among the six partial sums, giving a nonempty zero-sum
subvector whose removal would contradict minimality. Enumerating
the eight parities and those bounded vectors gives exactly thirty
seeds. Every input is a seed plus twice an element of
\[
M_3=\{(v_1,v_2,v_3)\in\mathbf Z_{\ge0}^3:
v_1+2v_2+3v_3\equiv0\pmod5\}.
\tag{EW.6}
\]
Every indecomposable has total at most five: a longer vector has a
proper nonempty zero-sum subvector of length at most five by that
same argument. The complete bounded enumeration gives eight generators:
\[
\begin{gathered}
(0,0,5),(0,1,1),(0,5,0),(1,0,3),\\
(1,2,0),(2,0,1),(3,1,0),(5,0,0).
\end{gathered}
\tag{EW.7}
\]
Recursive subtraction decomposes every element of (EW.6).
Each increment has the actual injective invariant-section map
of G-024. A state with all seven coefficients positive remains
so after every later increment.

The exact program three_row_support_graph.py begins with the
fourteen deficient seeds among the thirty. For every retained state
\(g\) and every generator \(h\) it forms \(g+2h\), applies
(EW.5), and computes all seven traces and multiplicities. A fully
positive target is marked as an exit. Every other target is retained
and its eight transitions are examined. This enumeration terminates
with exactly 24 deficient states and 192 transitions. All seeds,
multiplicities, raw targets, normal targets and exit tests appear
in THREE_ROW_SUPPORT_GRAPH.json. The integer traces use the exact
cycle-alternant/Pieri algorithm proved in G-025. Their independent
Jacobi–Trudi reconstruction is recorded separately.

Here is why finite closure exhausts the infinite domain. Retain each
unstable deficient node as one point, and each stable deficient node
with all its nonnegative first-gap increments of ten. Start with
the thirty minimal seeds. Every fully positive seed and all its
later increments have full support by the injection. Every deficient
seed normalizes to a listed node, through the isomorphism (EW.4).

For one further generator from a listed point, its recorded transition
either exits to a fully positive module or normalizes to a listed
deficient node. Start instead at a stable ray point
\(g+10q(1,0,0)\), \(q\ge0\), and add a generator. The actual
multipliers commute in the same polynomial domain, so the order is
\[
(g+2h)+10q(1,0,0).
\tag{EW.8}
\]
The first part is its stored transition. The second is \(q\)
applications of the generator \((5,0,0)\), also present in the
graph. Intermediate normalizations preserve all multiplicities.
An exit at any step makes every later module fully positive.
Otherwise each step is another listed node with its prescribed
stable first-axis offset. This also treats a generator that raises
\(b,c\) and hence the stability threshold: no commutation of the
normal-form operation with that change is assumed. A finite generator
decomposition and this argument show that every deficient input is
a listed point or ray.

Conversely every listed point has its computed deficient vector, and
every point on a listed ray has the same vector by (EW.4). Hence
all of them are actually deficient. Both directions are proved,
with no unproved cutoff on the original infinite inputs.

## 3. All exceptional values

The vector order is
\((5),(4,1),(3,2),(3,1,1),(2,2,1),(2,1,1,1),(1^5)\).
The twelve finite exceptional triples are:

| \((a,b,c)\) | Complete multiplicity vector |
|---|---|
| \((1,1,4)\) | \((0,1,2,2,2,1,0)\) |
| \((1,2,5)\) | \((0,3,4,6,4,4,1)\) |
| \((1,3,1)\) | \((0,1,1,1,1,1,0)\) |
| \((1,8,1)\) | \((1,3,3,4,3,3,0)\) |
| \((2,1,2)\) | \((0,1,1,2,1,1,0)\) |
| \((2,2,3)\) | \((0,3,3,6,3,3,0)\) |
| \((3,2,1)\) | \((0,1,1,2,1,1,0)\) |
| \((3,3,2)\) | \((1,4,5,5,4,3,0)\) |
| \((4,4,1)\) | \((0,3,3,5,3,2,0)\) |
| \((6,3,1)\) | \((1,3,3,3,3,2,0)\) |
| \((8,3,2)\) | \((2,8,9,10,7,5,0)\) |
| \((9,4,1)\) | \((1,5,5,7,5,3,0)\) |

The twelve parity-preserving stable graph nodes combine into six
rays. Here \(q\) is every nonnegative integer.

| \((a,b,c)\) | Complete multiplicity vector |
|---|---|
| \((5+5q,1,1)\) | \((0,1,1,1,1,0,0)\) |
| \((7+5q,1,2)\) | \((1,3,3,3,2,1,0)\) |
| \((8+5q,2,1)\) | \((0,2,2,3,1,1,0)\) |
| \((11+5q,3,1)\) | \((1,4,4,4,3,2,0)\) |
| \((13+5q,3,2)\) | \((3,10,11,11,8,5,0)\) |
| \((14+5q,4,1)\) | \((1,6,6,8,5,3,0)\) |

Every displayed triple satisfies the weighted congruence. The start
of each ray is its stable threshold, and its two graph nodes differ
by five, so (EW.4) proves the merger into the step-five ray.
None of the twelve finite points is on a stable ray. Apply the
specified transformation to use these tables on either original wall,
including every determinant shift and outer label.

The four effective labels \((4,1),(3,2),(3,1,1),(2,2,1)\)
always occur on the normalized first wall. The effective label
\((2,1,1,1)\) fails exactly on the first ray. The two extreme
labels have precisely the zero entries in the tables. Every
remaining input has all seven labels.

## 4. Geometric transport and canonical ranks

Each graph edge is multiplication by the explicit invariant section
of G-024. Each stable contraction is the exact G-027 quotient-section
isomorphism followed by the fixed inverse balanced chart; the first-gap
step multiplies by \(u\) or \(u^2\). The complementary wall
uses the perfect exterior-column pairing, with its determinant
local system and balanced-content change specified in §1.

These are equivariant section maps for the SGA3 I4.5,4.7.2–4.7.3
frame action. Their Schur operations are SGA6 V4.2,4.4,4.8–4.9
and cote133/024–029 via A-010. Their coherent coordinate models use
the EGA II2.4.1–2.4.2 Proj charts and the exact associated-sheaf
functor II2.5.2,2.5.4. The finite equivariant resolution map of
G-027 §6 carries these coherent classes to the locally free K0 of
SGA6 VI3.3 on the stated base. Thus these support assertions compute
nonzero ranks of explicitly identified section components.

For the actual symmetric canonical map, R-031 supplies the complete
rank law, with its literal adjoint identity and verified fourth-square
normalization. It applies to both walls: the image is the source
multiplicity at \(n\le4\), the target with the eight specified
kernel copies removed at \(n=5\), and the full target at \(n\ge6\).
These are the graded EGA I9.5.2 coordinate-image ranks of the same
map. The support tables above concern every outer Schur label with
the actual sign conversions already proved.

