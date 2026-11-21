# Complete nonvanishing for outer degree five

## G-031. Every shape, every outer label and every inner degree

Let \(n\ge0\), \(\mu\vdash5\), and \(\lambda\vdash5n\).
The following fixed procedure decides exactly whether
\(p_{\mu,(n)}^\lambda\) is positive. It uses a fixed table of344
integer vectors, the explicit strict-chamber rule G028, and a
bounded number of integer operations. No plethysm coefficient
remains to be evaluated by this decision procedure.

For length greater than five the coefficient is zero: the actual
Young projector embeds \(S_\mu(\operatorname{Sym}^n V)\)
in \((\operatorname{Sym}^n V)^{\otimes5}\), and repeated Pieri
allows at most five rows. Otherwise pad to five entries and put
\[
d=\lambda_5,\qquad g_i=\lambda_i-\lambda_{i+1}\quad(1\le i\le4).
\tag{NW.1}
\]
Use the effective label \(\nu=\mu\) at even \(d\) and
\(\nu=\mu^t\) at odd \(d\).

For \(g=0\), the only nonzero effective label is \((5)\),
with multiplicity one. For all four gaps positive, G028 gives
the exact rule: the five middle labels always occur; both extreme
labels vanish on \(g=(L,1,1,1)\) and \(g=(1,1,1,L)\),
\(L\ge1\), \(L\equiv1\pmod5\); the effective trivial label
also vanishes at \(g=(1,2,2,1),(2,1,1,2)\). There are no
other strict-chamber zeros.

For every other gap vector use the following normal form. Write
\(g=(a,b,c,e)\), and first test the first line:
Set \(L_1=\max(1,3b+2c+e)\) and
\(L_4=\max(1,a+2b+3c)\). Then
\[
N(g)=
\begin{cases}
(L_1+(a-L_1)\bmod10,b,c,e),&a\ge L_1,\\
(a,b,c,L_4+(e-L_4)\bmod10),&e\ge L_4,\\
g,&\text{otherwise}.
\end{cases}
\tag{NW.2}
\]
The first applicable line is used. The fixed catalog in §5
contains344 distinct vectors \(z\), each with its complete set
of zero effective labels. The exact decision is
\[
\boxed{\ p_{\mu,(n)}^\lambda=0
\ \Longleftrightarrow\
N(g)\text{ is a catalog vector and }\nu
\text{ is one of its listed zero labels}.\ }
\tag{NW.3}
\]
This formula applies to the proper nonempty gap supports; the two
other cases were explicitly settled above. The supplied JSON and
TSV also give all seven exact multiplicities at every catalog
vector. They remain those values on its stable rays and on their
normal-form preimages.

This completes the full outer-five nonvanishing question. The
positive coefficient formulas already proved remain available in
their full stated regions. The present finding supplies a support
decision for every remaining coefficient, with all comparison maps
and a finite proof of exhaustion.

## 1. Exact stable maps in both end directions

Determinant multiplication gives the actual sign conversion in
(NW.1). Its normalized shape is
\[
\lambda^0=(a+b+c+e,b+c+e,c+e,e,0),\qquad
n_0=(a+2b+3c+4e)/5.
\tag{NW.4}
\]
The weighted sum is divisible by five. The first stable region
\(a\ge3b+2c+e\) is precisely \(\lambda^0_2\le n_0\).
The actual G027 quotient-section chart identifies its balanced
module with
\[
\operatorname{sgn}^{\,b+c+e}
S_{(b+c+e,b+c,b)}\mathfrak h_5.
\tag{NW.5}
\]
Increasing \(a\) by five multiplies the balanced expression
by \(u=\prod_iX_{i1}\); the shared full section space gives its
inverse on the image. Hence it is an isomorphism and preserves
every multiplicity.

For the second stable region use the perfect exterior-column
pairing in width \(H=a+b+c+e\). It identifies the balanced
module with the dual module of the reversed gap vector
\((e,c,b,a)\), times \(\operatorname{sgn}^H\).
The first stable inequality of that reversed vector is precisely
\(e\ge a+2b+3c\). Increasing \(e\) by ten increases \(H\)
by ten and the first gap of the complementary shape by ten.
Thus the same actual chart isomorphism and the unchanged
determinant sign preserve every multiplicity. A step of five in
this last direction instead transposes the effective label; using
ten in (NW.2) retains its complete vector.

The lower bound one in (NW.2) preserves the positive support
coordinate on a one-axis face. All subtractions are nonnegative
multiples of ten. They retain both the congruence and every zero
gap, and the maps just proved establish equality of all
coefficients before and after normalization.

Both stable inequalities can hold together only when \(b=c=0\)
and \(a=e\). At such a point each individual end direction has
its stated stable ray. These two rays must both be retained; their
interaction is explicitly checked below.

## 2. Every seed and every allowed increment

Fix a nonempty proper support \(S\subset\{1,2,3,4\}\).
For \(i\in S\), write
\(g_i=1+p_i+2t_i\), with \(p_i\in\{0,1\}\) and
\(t_i\ge0\); outside \(S\) put zero. Select a componentwise
minimal \(u\le t\) for which the weighted sum of
\((1+p_i)+2u_i\) is divisible by five.

Every such minimal \(u\) has total at most four. A list of five
indexed weights has two equal partial sums among its six partial
sums modulo five. It therefore contains a nonempty zero-sum
subvector, whose removal from a vector of total at least five
would contradict minimality. Enumeration of the finitely many
parities and \(u\) with total at most four gives all the seeds
used here. There are172 seeds across the fourteen supports.

The difference \(t-u\) belongs to
\[
M_S=\{v\in\mathbf Z_{\ge0}^{S}:\ \sum_iiv_i\equiv0\pmod5\}.
\tag{NW.6}
\]
Every indecomposable nonzero element has total at most five:
a vector of greater total has a proper nonempty zero-sum
subvector of length at most five by the same partial-sum argument.
Thus enumerating total at most five and keeping the
componentwise minimal nonzero solutions gives the complete
generator list. Recursive subtraction proves generation.
Both these enumerations are literal fixed loops in
five_row_face_exploration.py, and all their outputs are retained.

For each generator \(h\), G024 gives an actual invariant-section
embedding from gap vector \(g\) to \(g+2h\), preserving
each outer label. To identify its highest weight explicitly,
put \(\eta_i=\sum_{j\ge i}h_j\), \(\eta_5=0\).
Then \(|\eta|=\sum_iih_i=5q\), so G024 multiplies by
the specified nonzero invariant section of weight \(2\eta\).
The tensor and chart degree increases are exactly the changes
in (NW.4). Every shape with all seven labels positive remains
fully positive after any later generator sequence.

## 3. Complete finite closure, including interacting rays

A catalog node is deficient: at least one of its seven
multiplicities is zero. Each node contributes its point. It
also contributes a ray \(z+10q\,e_j\), \(q\ge0\), for each
stable end axis \(j=1,4\) that it has. The union of these
points and rays will be denoted \(D_S\).

The algorithm starts from every deficient seed in support \(S\),
after normalization. For every retained node \(z\) and generator
\(h\), it evaluates \(N(z+2h)\). A fully positive value is an
exit. Every deficient value is retained and its transitions are
examined. In addition it makes the following finite checks for
each stable axis of every retained node.

Set \(w=z+2h\), and let
\[
L_1(w)=\max(1,3w_2+2w_3+w_4),\qquad
L_4(w)=\max(1,w_1+2w_2+3w_3).
\]
For the selected stable axis \(j\), put
\[
Q(z,h,j)=\max\left(0,\left\lceil
\frac{L_j(w)-w_j}{10}\right\rceil\right).
\tag{NW.7}
\]
The algorithm checks every \(q=0,\ldots,Q(z,h,j)\) in
\[
N(w+10q\,e_j).
\tag{NW.8}
\]
All are exits or retained deficient nodes.
Every generator has total at most five, and its largest
coefficient in either threshold is three. Since \(z\) was
already stable in direction \(j\), its threshold deficit
after adding \(2h\) is at most30. Hence \(Q\le3\).

For every \(q\ge Q\), \(w+10q e_j\) is stable in that same
axis. Its normal form is constant, because its other coordinates
are fixed and its varying coordinate has constant residue modulo
ten. At the possible equality of both stable inequalities,
\(w_2=w_3=0,w_1=w_4\), either normalization fixes the equality
point; the subsequent original-axis normalization has the same
value. This proves constancy also at that endpoint.
Thus (NW.8) exhausts the entire ray transition, including a
generator that raises its stability threshold or switches which
stable direction is selected. No commutation of normalization
with other increments is assumed.

The algorithm terminates with the following exact counts.
Support indices in this table refer to \(g_1,g_2,g_3,g_4\).
The ray-base count counts both directions at a node that has both.

| Support | Seeds | Nodes | Point transitions | Ray checks | Isolated points | Ray bases |
|---|---:|---:|---:|---:|---:|---:|
| 1 | 2 | 2 | 2 | 2 | 0 | 2 |
| 2 | 2 | 6 | 6 | 0 | 6 | 0 |
| 3 | 2 | 6 | 6 | 0 | 6 | 0 |
| 4 | 2 | 2 | 2 | 2 | 0 | 2 |
| 1,2 | 8 | 52 | 208 | 160 | 32 | 20 |
| 1,3 | 8 | 16 | 64 | 56 | 8 | 8 |
| 1,4 | 6 | 30 | 90 | 160 | 0 | 40 |
| 2,3 | 6 | 10 | 30 | 0 | 10 | 0 |
| 2,4 | 8 | 16 | 64 | 56 | 8 | 8 |
| 3,4 | 8 | 52 | 208 | 160 | 32 | 20 |
| 1,2,3 | 30 | 24 | 192 | 192 | 12 | 12 |
| 1,2,4 | 30 | 52 | 416 | 552 | 16 | 36 |
| 1,3,4 | 30 | 52 | 416 | 552 | 16 | 36 |
| 2,3,4 | 30 | 24 | 192 | 192 | 12 | 12 |
| Total | 172 | 344 | 1896 | 2084 | 158 | 196 |

Here is the full exhaustion proof. Every input starts at one
of the proved seeds and is obtained by a finite generator
sequence. A fully positive seed or intermediate exit stays
positive, by the explicit multiplication injection. A deficient
seed belongs to \(D_S\), by normalization. For a point in
\(D_S\), the recorded point transition classifies its next
increment. For a ray point, (NW.7)–(NW.8) classify every next
increment, including its unbounded tail. A deficient target
normalizes to a retained node and hence belongs to its point
or stable ray. Induction along the finite generator sequence
proves that every deficient input belongs to \(D_S\).

Conversely every retained point has its computed deficient
vector; every ray has the same vector by the actual stable
isomorphisms. Thus every point of \(D_S\) is deficient.
Every retained node is already normalized, and normalizing
any of its ray points returns that node. Conversely (NW.2)
identifies every normal-form preimage with that node.
Consequently deficiency is exactly membership of \(N(g)\)
in the fixed node table. Its individual zero entries prove
(NW.3), including the determinant-label conversion.

## 4. Reproducible certificate, evaluator and geometric meaning

The complete source, normalized targets, raw targets, all seven
cycle traces and all seven multiplicities of every seed and
transition are in ALL_WALL_SUPPORT_GRAPH.json. The executable
all_wall_support_graph.py specifies every finite test just proved.
It checks all1896 point transitions and all2084 ray cases.
There are2218 distinct normalized evaluated gap vectors; the
largest normalized inner degree in those transitions is67.
These are finite character evaluations using the exact balanced
cycle-alternant/Pieri algorithm of G025, with the infinite input
range exhausted by the preceding proof.

ALL_WALL_SUPPORT_NODES.tsv gives every full vector in the344-node
catalog. FIVE_ROW_SUPPORT_INDEX.json is the fixed small evaluator
index, and five_row_support.py implements exactly (NW.1)–(NW.3)
and G028's strict rule. Its arithmetic count is fixed independently
of the input sizes; its integer bit cost is polynomial in their
bit lengths. It does no input-size representation computation.
The initial evaluator verification compared3640 actual support
entries on all congruent gap vectors in \(\{0,\ldots,5\}^4\),
including both determinant parities. Every exact exceptional
vector returned there also agreed. The independent reconstruction
and whole-proof reviews are recorded separately as they finish.

Every edge of this support proof is a specified invariant-section
map, and each normalization is the specified quotient-section
isomorphism or its perfect complementary-column pairing. The
frame action is SGA3 I4.5,I4.7.2–4.7.3; the Schur operations
are SGA6 V4.2,4.4,4.8–4.9 and cote133/024–029 via A010.
The frame and its five linear ideals have models over
\(\mathbf Z[1/5]\); in each fixed degree the rational Young
projectors are defined after additionally inverting the relevant
factorials. The rank statements here concern their characteristic-zero
generic fibers. This specifies the integral construction and its
scalar extension, without asserting equal ranks in every residue
characteristic.

EGA II2.4.1–2.4.2 gives the actual Proj charts, and
II2.5.2,2.5.4 the exact associated-sheaf functor. G027§6's
finite equivariant free resolutions carry the coherent complexes
to locally free \(K_0\) in SGA6 VI3.3. Thus the table decides
nonzero Schur-component ranks of those exact section modules.
For the symmetric canonical map, R031 then determines the actual
image rank by its source at \(n\le4\), its target minus the
eight stated kernel copies at \(n=5\), and its full target at
\(n\ge6\). These use the EGA I9.5.2 graded coordinate-image
scheme of that same normalized map.

## 5. Complete catalog of proper-face zero labels

The axes column lists stable end directions; a dash means an
isolated point. Each listed axis permits every nonnegative
increment of ten in that one coordinate. At a node with both
axes, take the union of the two rays. The finite closure proof,
including the bounded transition checks, also covers sums of
increments in different axes. Labels are written compactly:
41 means \((4,1)\), 11111 means \((1^5)\), and so on.
The effective-label convention is (NW.1).


### Gap support 1

| Normalized gaps | axes | All zero effective labels |
|-------------------------|------|-----------------------------------------|
| (5,0,0,0) | 1 | 41, 32, 311, 221, 2111, 11111 |
| (10,0,0,0) | 1 | 41, 32, 311, 221, 2111, 11111 |

### Gap support 2

| Normalized gaps | axes | All zero effective labels |
|-------------------------|------|-----------------------------------------|
| (0,5,0,0) | — | 5, 41, 32, 221, 2111, 11111 |
| (0,10,0,0) | — | 311, 2111 |
| (0,15,0,0) | — | 5, 221, 11111 |
| (0,25,0,0) | — | 5, 11111 |
| (0,35,0,0) | — | 5, 11111 |
| (0,45,0,0) | — | 11111 |

### Gap support 3

| Normalized gaps | axes | All zero effective labels |
|-------------------------|------|-----------------------------------------|
| (0,0,5,0) | — | 5, 41, 32, 221, 2111, 11111 |
| (0,0,10,0) | — | 311, 2111 |
| (0,0,15,0) | — | 5, 32, 11111 |
| (0,0,25,0) | — | 5, 11111 |
| (0,0,35,0) | — | 5, 11111 |
| (0,0,45,0) | — | 5 |

### Gap support 4

| Normalized gaps | axes | All zero effective labels |
|-------------------------|------|-----------------------------------------|
| (0,0,0,5) | 4 | 5, 41, 32, 311, 221, 2111 |
| (0,0,0,10) | 4 | 41, 32, 311, 221, 2111, 11111 |

### Gap support 1,2

| Normalized gaps | axes | All zero effective labels |
|-------------------------|------|-----------------------------------------|
| (1,2,0,0) | — | 5, 41, 311, 221, 2111, 11111 |
| (1,7,0,0) | — | 5, 2111, 11111 |
| (1,12,0,0) | — | 11111 |
| (1,17,0,0) | — | 11111 |
| (2,4,0,0) | — | 311, 2111, 11111 |
| (2,9,0,0) | — | 5, 11111 |
| (2,19,0,0) | — | 11111 |
| (3,1,0,0) | 1 | 5, 32, 311, 221, 2111, 11111 |
| (3,6,0,0) | — | 11111 |
| (3,11,0,0) | — | 11111 |
| (4,3,0,0) | — | 5, 221, 2111, 11111 |
| (4,8,0,0) | — | 11111 |
| (4,13,0,0) | — | 11111 |
| (5,5,0,0) | — | 2111, 11111 |
| (6,2,0,0) | 1 | 311, 221, 2111, 11111 |
| (6,7,0,0) | — | 11111 |
| (7,4,0,0) | — | 2111, 11111 |
| (7,9,0,0) | — | 11111 |
| (8,1,0,0) | 1 | 5, 32, 311, 221, 2111, 11111 |
| (8,6,0,0) | — | 11111 |
| (8,11,0,0) | — | 11111 |
| (9,3,0,0) | 1 | 221, 2111, 11111 |
| (9,8,0,0) | — | 11111 |
| (10,5,0,0) | — | 2111, 11111 |
| (11,2,0,0) | 1 | 311, 221, 2111, 11111 |
| (11,7,0,0) | — | 11111 |
| (12,4,0,0) | 1 | 2111, 11111 |
| (12,9,0,0) | — | 11111 |
| (13,6,0,0) | — | 11111 |
| (13,11,0,0) | — | 11111 |
| (14,3,0,0) | 1 | 221, 2111, 11111 |
| (14,8,0,0) | — | 11111 |
| (15,5,0,0) | 1 | 2111, 11111 |
| (16,7,0,0) | — | 11111 |
| (17,4,0,0) | 1 | 2111, 11111 |
| (17,9,0,0) | — | 11111 |
| (18,6,0,0) | 1 | 11111 |
| (18,11,0,0) | — | 11111 |
| (19,8,0,0) | — | 11111 |
| (20,5,0,0) | 1 | 2111, 11111 |
| (21,7,0,0) | 1 | 11111 |
| (22,9,0,0) | — | 11111 |
| (23,6,0,0) | 1 | 11111 |
| (23,11,0,0) | — | 11111 |
| (24,8,0,0) | 1 | 11111 |
| (26,7,0,0) | 1 | 11111 |
| (27,9,0,0) | 1 | 11111 |
| (28,11,0,0) | — | 11111 |
| (29,8,0,0) | 1 | 11111 |
| (32,9,0,0) | 1 | 11111 |
| (33,11,0,0) | 1 | 11111 |
| (38,11,0,0) | 1 | 11111 |

### Gap support 1,3

| Normalized gaps | axes | All zero effective labels |
|-------------------------|------|-----------------------------------------|
| (1,0,3,0) | — | 5, 41, 32, 221, 11111 |
| (1,0,8,0) | — | 11111 |
| (1,0,13,0) | — | 5, 11111 |
| (1,0,23,0) | — | 5 |
| (2,0,1,0) | 1 | 5, 41, 32, 221, 2111, 11111 |
| (2,0,11,0) | — | 5, 11111 |
| (3,0,9,0) | — | 5 |
| (4,0,2,0) | 1 | 311, 2111, 11111 |
| (4,0,7,0) | — | 5, 11111 |
| (5,0,5,0) | — | 5, 11111 |
| (6,0,3,0) | 1 | 5, 11111 |
| (7,0,1,0) | 1 | 5, 41, 32, 221, 2111, 11111 |
| (9,0,2,0) | 1 | 311, 2111, 11111 |
| (10,0,5,0) | 1 | 5, 11111 |
| (11,0,3,0) | 1 | 5, 11111 |
| (15,0,5,0) | 1 | 5, 11111 |

### Gap support 1,4

| Normalized gaps | axes | All zero effective labels |
|-------------------------|------|-----------------------------------------|
| (1,0,0,1) | 1,4 | 5, 41, 32, 311, 221, 11111 |
| (1,0,0,6) | 4 | 5, 32, 311, 221, 2111, 11111 |
| (2,0,0,2) | 1,4 | 311, 221, 2111, 11111 |
| (2,0,0,7) | 4 | 5, 41, 32, 311 |
| (3,0,0,3) | 1,4 | 5, 41, 32 |
| (3,0,0,8) | 4 | 221, 2111, 11111 |
| (4,0,0,4) | 1,4 | 2111, 11111 |
| (4,0,0,9) | 4 | 5, 41 |
| (5,0,0,5) | 1,4 | 5, 41 |
| (5,0,0,10) | 4 | 2111, 11111 |
| (6,0,0,1) | 1 | 5, 41, 32, 311, 221, 11111 |
| (6,0,0,6) | 1,4 | 11111 |
| (6,0,0,11) | 4 | 5 |
| (7,0,0,2) | 1 | 311, 221, 2111, 11111 |
| (7,0,0,7) | 1,4 | 5 |
| (7,0,0,12) | 4 | 11111 |
| (8,0,0,3) | 1 | 5, 41, 32 |
| (8,0,0,8) | 1,4 | 11111 |
| (8,0,0,13) | 4 | 5 |
| (9,0,0,4) | 1 | 2111, 11111 |
| (9,0,0,9) | 1,4 | 5 |
| (9,0,0,14) | 4 | 11111 |
| (10,0,0,5) | 1 | 5, 41 |
| (11,0,0,6) | 1 | 11111 |
| (11,0,0,11) | 1,4 | 5 |
| (11,0,0,16) | 4 | 11111 |
| (12,0,0,7) | 1 | 5 |
| (13,0,0,8) | 1 | 11111 |
| (14,0,0,9) | 1 | 5 |
| (16,0,0,11) | 1 | 5 |

### Gap support 2,3

| Normalized gaps | axes | All zero effective labels |
|-------------------------|------|-----------------------------------------|
| (0,1,1,0) | — | 5, 41, 32, 311, 2111, 11111 |
| (0,1,6,0) | — | 5, 32, 11111 |
| (0,1,16,0) | — | 5, 11111 |
| (0,2,2,0) | — | 311, 2111 |
| (0,2,7,0) | — | 5, 11111 |
| (0,3,8,0) | — | 5, 11111 |
| (0,6,1,0) | — | 5, 221, 11111 |
| (0,7,2,0) | — | 5, 11111 |
| (0,8,3,0) | — | 5, 11111 |
| (0,16,1,0) | — | 5, 11111 |

### Gap support 2,4

| Normalized gaps | axes | All zero effective labels |
|-------------------------|------|-----------------------------------------|
| (0,1,0,2) | 4 | 5, 41, 32, 221, 2111, 11111 |
| (0,1,0,7) | 4 | 5, 41, 32, 221, 2111, 11111 |
| (0,2,0,4) | 4 | 311, 2111, 11111 |
| (0,2,0,9) | 4 | 5, 41, 311 |
| (0,3,0,1) | — | 5, 41, 32, 221, 11111 |
| (0,3,0,6) | 4 | 5, 11111 |
| (0,3,0,11) | 4 | 5, 11111 |
| (0,5,0,5) | — | 5, 11111 |
| (0,5,0,10) | 4 | 5, 11111 |
| (0,5,0,15) | 4 | 5, 11111 |
| (0,7,0,4) | — | 5, 11111 |
| (0,8,0,1) | — | 5 |
| (0,9,0,3) | — | 5 |
| (0,11,0,2) | — | 5, 11111 |
| (0,13,0,1) | — | 5, 11111 |
| (0,23,0,1) | — | 5 |

### Gap support 3,4

| Normalized gaps | axes | All zero effective labels |
|-------------------------|------|-----------------------------------------|
| (0,0,1,3) | 4 | 5, 32, 311, 221, 2111, 11111 |
| (0,0,1,8) | 4 | 5, 41, 32, 311, 221, 11111 |
| (0,0,2,1) | — | 5, 41, 32, 311, 2111, 11111 |
| (0,0,2,6) | 4 | 311, 221, 2111, 11111 |
| (0,0,2,11) | 4 | 5, 41, 32, 311 |
| (0,0,3,4) | — | 5, 41, 32, 11111 |
| (0,0,3,9) | 4 | 221, 2111, 11111 |
| (0,0,3,14) | 4 | 5, 41, 32 |
| (0,0,4,2) | — | 311, 2111, 11111 |
| (0,0,4,7) | — | 5, 41 |
| (0,0,4,12) | 4 | 2111, 11111 |
| (0,0,4,17) | 4 | 5, 41 |
| (0,0,5,5) | — | 2111, 11111 |
| (0,0,5,10) | — | 5, 41 |
| (0,0,5,15) | 4 | 2111, 11111 |
| (0,0,5,20) | 4 | 5, 41 |
| (0,0,6,3) | — | 5 |
| (0,0,6,8) | — | 11111 |
| (0,0,6,13) | — | 5 |
| (0,0,6,18) | 4 | 11111 |
| (0,0,6,23) | 4 | 5 |
| (0,0,7,1) | — | 5, 2111, 11111 |
| (0,0,7,6) | — | 5 |
| (0,0,7,11) | — | 11111 |
| (0,0,7,16) | — | 5 |
| (0,0,7,21) | 4 | 11111 |
| (0,0,7,26) | 4 | 5 |
| (0,0,8,4) | — | 11111 |
| (0,0,8,9) | — | 5 |
| (0,0,8,14) | — | 11111 |
| (0,0,8,19) | — | 5 |
| (0,0,8,24) | 4 | 11111 |
| (0,0,8,29) | 4 | 5 |
| (0,0,9,2) | — | 5, 11111 |
| (0,0,9,7) | — | 11111 |
| (0,0,9,12) | — | 5 |
| (0,0,9,17) | — | 11111 |
| (0,0,9,22) | — | 5 |
| (0,0,9,27) | 4 | 11111 |
| (0,0,9,32) | 4 | 5 |
| (0,0,11,3) | — | 11111 |
| (0,0,11,8) | — | 5 |
| (0,0,11,13) | — | 11111 |
| (0,0,11,18) | — | 5 |
| (0,0,11,23) | — | 11111 |
| (0,0,11,28) | — | 5 |
| (0,0,11,33) | 4 | 11111 |
| (0,0,11,38) | 4 | 5 |
| (0,0,12,1) | — | 5 |
| (0,0,13,4) | — | 5 |
| (0,0,17,1) | — | 11111 |
| (0,0,19,2) | — | 5 |

### Gap support 1,2,3

| Normalized gaps | axes | All zero effective labels |
|-------------------------|------|-----------------------------------------|
| (1,1,4,0) | — | 5, 11111 |
| (1,2,5,0) | — | 5 |
| (1,3,1,0) | — | 5, 11111 |
| (1,8,1,0) | — | 11111 |
| (2,1,2,0) | — | 5, 11111 |
| (2,2,3,0) | — | 5, 11111 |
| (3,2,1,0) | — | 5, 11111 |
| (3,3,2,0) | — | 11111 |
| (4,4,1,0) | — | 5, 11111 |
| (5,1,1,0) | 1 | 5, 2111, 11111 |
| (6,3,1,0) | — | 11111 |
| (7,1,2,0) | 1 | 11111 |
| (8,2,1,0) | 1 | 5, 11111 |
| (8,3,2,0) | — | 11111 |
| (9,4,1,0) | — | 11111 |
| (10,1,1,0) | 1 | 5, 2111, 11111 |
| (11,3,1,0) | 1 | 11111 |
| (12,1,2,0) | 1 | 11111 |
| (13,2,1,0) | 1 | 5, 11111 |
| (13,3,2,0) | 1 | 11111 |
| (14,4,1,0) | 1 | 11111 |
| (16,3,1,0) | 1 | 11111 |
| (18,3,2,0) | 1 | 11111 |
| (19,4,1,0) | 1 | 11111 |

### Gap support 1,2,4

| Normalized gaps | axes | All zero effective labels |
|-------------------------|------|-----------------------------------------|
| (1,1,0,3) | 4 | 5, 41, 11111 |
| (1,1,0,8) | 4 | 5, 2111, 11111 |
| (1,2,0,5) | 4 | 5 |
| (1,2,0,10) | 4 | 11111 |
| (1,3,0,2) | — | 11111 |
| (1,4,0,4) | — | 11111 |
| (1,5,0,1) | — | 5, 11111 |
| (1,10,0,1) | — | 5 |
| (2,1,0,4) | 4 | 5, 11111 |
| (2,1,0,9) | 4 | 5, 11111 |
| (2,2,0,1) | — | 5, 41 |
| (2,3,0,3) | — | 5 |
| (2,5,0,2) | — | 11111 |
| (2,7,0,1) | — | 5 |
| (3,1,0,5) | 4 | 5 |
| (3,1,0,10) | 4 | 11111 |
| (3,2,0,2) | — | 11111 |
| (3,2,0,7) | 4 | 5 |
| (3,2,0,12) | 4 | 11111 |
| (3,4,0,1) | — | 5 |
| (4,1,0,1) | 1 | 5, 41, 32, 11111 |
| (4,1,0,6) | 4 | 11111 |
| (4,1,0,11) | 4 | 5 |
| (4,2,0,3) | — | 5 |
| (5,1,0,2) | 1 | 2111, 11111 |
| (5,3,0,1) | — | 5 |
| (6,1,0,3) | 1 | 5 |
| (6,3,0,2) | — | 11111 |
| (6,5,0,1) | — | 5 |
| (7,1,0,4) | 1 | 11111 |
| (7,2,0,1) | 1 | 5, 41 |
| (8,1,0,5) | 1 | 5 |
| (8,2,0,2) | 1 | 11111 |
| (8,4,0,1) | — | 5 |
| (9,1,0,1) | 1 | 5, 41, 32, 11111 |
| (9,2,0,3) | 1 | 5 |
| (10,1,0,2) | 1 | 2111, 11111 |
| (10,3,0,1) | 1 | 5 |
| (11,1,0,3) | 1 | 5 |
| (11,3,0,2) | 1 | 11111 |
| (11,5,0,1) | — | 5 |
| (12,1,0,4) | 1 | 11111 |
| (12,2,0,1) | 1 | 5, 41 |
| (13,1,0,5) | 1 | 5 |
| (13,2,0,2) | 1 | 11111 |
| (13,4,0,1) | 1 | 5 |
| (14,2,0,3) | 1 | 5 |
| (15,3,0,1) | 1 | 5 |
| (16,3,0,2) | 1 | 11111 |
| (16,5,0,1) | 1 | 5 |
| (18,4,0,1) | 1 | 5 |
| (21,5,0,1) | 1 | 5 |

### Gap support 1,3,4

| Normalized gaps | axes | All zero effective labels |
|-------------------------|------|-----------------------------------------|
| (1,0,1,4) | 4 | 5, 41, 32, 11111 |
| (1,0,1,9) | 4 | 5, 221, 2111, 11111 |
| (1,0,2,2) | — | 2111, 11111 |
| (1,0,2,7) | 4 | 5, 41 |
| (1,0,2,12) | 4 | 2111, 11111 |
| (1,0,3,5) | — | 11111 |
| (1,0,3,10) | 4 | 5 |
| (1,0,3,15) | 4 | 11111 |
| (1,0,4,3) | — | 5 |
| (1,0,4,8) | — | 11111 |
| (1,0,4,13) | 4 | 5 |
| (1,0,4,18) | 4 | 11111 |
| (1,0,5,1) | — | 5, 11111 |
| (1,0,5,6) | — | 5 |
| (1,0,5,11) | — | 11111 |
| (1,0,5,16) | 4 | 5 |
| (1,0,5,21) | 4 | 11111 |
| (1,0,7,2) | — | 5 |
| (1,0,10,1) | — | 5 |
| (2,0,1,5) | 4 | 2111, 11111 |
| (2,0,1,10) | 4 | 5, 41 |
| (2,0,2,3) | — | 5 |
| (2,0,2,8) | 4 | 11111 |
| (2,0,2,13) | 4 | 5 |
| (2,0,3,1) | — | 11111 |
| (2,0,3,6) | — | 5 |
| (2,0,3,11) | 4 | 11111 |
| (2,0,3,16) | 4 | 5 |
| (2,0,5,2) | — | 5 |
| (3,0,1,1) | 1 | 5, 2111, 11111 |
| (3,0,1,6) | 4 | 5 |
| (3,0,1,11) | 4 | 11111 |
| (3,0,2,4) | — | 11111 |
| (3,0,2,9) | 4 | 5 |
| (3,0,2,14) | 4 | 11111 |
| (3,0,3,2) | — | 5 |
| (4,0,1,2) | 1 | 5, 11111 |
| (4,0,1,7) | 4 | 11111 |
| (4,0,1,12) | 4 | 5 |
| (4,0,4,1) | — | 5 |
| (5,0,1,3) | 1 | 11111 |
| (5,0,1,8) | 4 | 5 |
| (5,0,1,13) | 4 | 11111 |
| (5,0,2,1) | 1 | 5 |
| (6,0,1,4) | 1 | 5 |
| (7,0,2,3) | 1 | 5 |
| (8,0,1,1) | 1 | 5, 2111, 11111 |
| (9,0,1,2) | 1 | 5, 11111 |
| (10,0,1,3) | 1 | 11111 |
| (10,0,2,1) | 1 | 5 |
| (11,0,1,4) | 1 | 5 |
| (12,0,2,3) | 1 | 5 |

### Gap support 2,3,4

| Normalized gaps | axes | All zero effective labels |
|-------------------------|------|-----------------------------------------|
| (0,1,1,5) | 4 | 5, 41, 11111 |
| (0,1,1,10) | 4 | 5, 2111, 11111 |
| (0,1,2,3) | — | 5, 11111 |
| (0,1,2,8) | 4 | 5, 11111 |
| (0,1,2,13) | 4 | 5, 11111 |
| (0,1,3,1) | — | 5, 11111 |
| (0,1,3,6) | — | 11111 |
| (0,1,3,11) | 4 | 5 |
| (0,1,3,16) | 4 | 11111 |
| (0,1,4,4) | — | 5, 11111 |
| (0,1,4,9) | — | 11111 |
| (0,1,4,14) | 4 | 5 |
| (0,1,4,19) | 4 | 11111 |
| (0,1,8,1) | — | 11111 |
| (0,2,1,2) | — | 5, 11111 |
| (0,2,1,7) | 4 | 11111 |
| (0,2,1,12) | 4 | 5 |
| (0,2,3,3) | — | 11111 |
| (0,2,3,8) | — | 5 |
| (0,2,3,13) | 4 | 11111 |
| (0,2,3,18) | 4 | 5 |
| (0,3,2,2) | — | 5, 11111 |
| (0,4,1,1) | — | 5, 11111 |
| (0,5,2,1) | — | 5 |
