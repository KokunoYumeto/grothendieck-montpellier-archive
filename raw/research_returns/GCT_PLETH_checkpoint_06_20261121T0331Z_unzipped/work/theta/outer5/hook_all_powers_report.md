# Every hook quotient power on the five-point quadratic ray

## T-043. Statement

Let \(a\ge1\), \(k,d\ge0\), and put
\[
n=d+a+k,\qquad
\lambda=(d+2a+3k+1,d+a+2k,d+a,d+a-1,d).
\tag{HA.1}
\]
Every outer coefficient \(p_{\mu,(n)}^\lambda\), \(\mu\vdash5\),
has a positive count in at most 54,000 fixed tagged polytopes, each
using at most eight variables. After selecting the two residues,
at most fifteen tags contribute. The coefficient is computed by a
fixed number of integer arithmetic operations from a complete fixed
table. Its support consists of all parameter pairs except the seventeen
untwisted zero pairs listed in §5.

This evaluates all point orders and all rank-three hook quotient
functors together. It includes T-041 at \(k=1\) and G-018 at \(a=1\).
The proof below establishes the actual sheaf comparison and all higher
cohomology before using a character formula.

## 1. The flag morphism and an exact sheaf complex

Let \(E=\mathfrak h_5\), \(Q\) be its tautological rank-three
quotient on \(\mathbf P(E)\), and \(\mathcal I\) the ideal of the
five canonical projective-frame points. Write
\[
D_{a,k}=H^0(\mathbf P(E),\mathcal I^k(2k)\otimes S_{(a,1)}Q).
\tag{HA.2}
\]
For (HA.1), the point order is \(\lambda_2-n=k\), the first gap is
\(2k\), and the quotient weight after complement is \((a,1,0)\).
The relative quotient-flag module before complement is
\(S_{(a,a-1)}Q^*\), and its first-line weight is \(a+2k\).
The actual complementary exterior-column pairing
\[
S_{(a,a-1)}Q^*\simeq(\det Q^*)^a\otimes S_{(a,1)}Q,
\quad\det Q^*=\det E^*\otimes\mathcal O(-1)
\]
leaves twist \(2k\) and determinant \(\epsilon^{d+a}\). Consequently
G-015 gives the specified equivariant isomorphism
\[
\boxed{(S_\lambda\mathbf Q^5)_{(n^5)}
\simeq\epsilon^{d+a}\otimes D_{a,k}.}
\tag{HA.3}
\]
Its inverse is \(F\mapsto u^{-k}F(v(X))\). G-015 proves that the
order-\(k\) ideal in (HA.2) is precisely the polynomial-extension
condition. These are the same relative frame maps proved for T-041;
the changed integer twist has been retained in each displayed factor.

Put \(H_a(V)=S_{(a,1)}V\), realized by the actual multiplication kernel
\(\ker(V\otimes\operatorname{Sym}^aV\to\operatorname{Sym}^{a+1}V)\).
T-041 proved the locally split hook resolution with maps
\(l^2v\mapsto l\otimes l\otimes v\) and
\(l\otimes e\otimes v\mapsto e\otimes lv-l\otimes ev\).
Tensor it with \(\mathcal I^k(2k)\). Its locally split exactness
preserves the complete complex
\[
\begin{split}
0\to&\mathcal I^k(2k-2)\otimes\operatorname{Sym}^{a-1}E\\
\to&\mathcal I^k(2k-1)\otimes E\otimes\operatorname{Sym}^{a-1}E\\
\to&\mathcal I^k(2k)\otimes H_a(E)\\
\to&\mathcal I^k(2k)\otimes H_a(Q)\to0.
\end{split}
\tag{HA.4}
\]
The maps are exactly the displayed hook maps multiplied by a local
section of the ideal. This specifies the entire complex, rather than
only its class in a representation group.

## 2. Complete higher-cohomology vanishing and its endpoints

For \(k\ge2\), A-029's linear-power result gives
\(H^1(\mathcal I^k(2k-1))=H^1(\mathcal I^k(2k))=0\).
For every twist \(c\ge0\), the ideal sequence with its zero-dimensional
fat-point quotient gives
\(H^i(\mathcal I^k(c))=H^i(\mathcal O(c))=0\) for \(i=2,3\).
In particular this applies also to \(c=2k-2\).

Let \(K\) be the image of the middle term into the next term in
(HA.4). In its first short exact sequence, the possible
\(H^1(\mathcal I^k(2k-2))\) contributes only to \(H^0(K)\).
All the groups forcing \(H^i(K)\), \(i\ge1\), vanish by the preceding
paragraph. The second short exact sequence, whose other term is
\(\mathcal I^k(2k)\otimes H_a(E)\), therefore proves
\[
H^i(\mathcal I^k(2k)\otimes H_a(Q))=0\quad(i\ge1,k\ge2).
\tag{HA.5}
\]
This argument does not assert that the leftmost ideal in (HA.4) is
acyclic; its possible first cohomology has been included exactly.

At \(k=1\), T-041 proves the actual isomorphism
\(D_{a,1}=U\otimes H_a(E)\), with \(U=[3,2]\), and proves all
higher cohomology zero. It does so by the five-point resolution and
the explicit identity map in top Čech cohomology of the negative
hook twists. At \(k=0\), (HA.4) has negative scalar twists
\(-2,-1\), both acyclic; it gives
\(D_{a,0}=H_a(E)\) and again no higher cohomology. Thus (HA.5) holds
for every \(k\ge0\), with its two endpoints established separately.

Taking the equivariant Euler characteristic of the actual complex now
computes its actual zeroth cohomology. For every \(a\ge1,k\ge0\),
\[
\boxed{
[D_{a,k}]=[H_a(E)]\chi(\mathcal I^k(2k))
+[\operatorname{Sym}^{a-1}E]
\bigl(\chi(\mathcal I^k(2k-2))
       -[E]\chi(\mathcal I^k(2k-1))\bigr).}
\tag{HA.6}
\]
Here \(\chi\) denotes the finite alternating sum of actual cohomology
modules. Its use on the leftmost ideal retains its possible first
cohomology. The final positive count in §4 removes the signs in this
intermediate character computation.

## 3. Explicit rational characters

For a cycle type \(\eta\vdash5\), let
\[
h_\eta(r)=[z^r]\frac{1-z}{\prod_{\ell\in\eta}(1-z^\ell)},
\quad h_\eta(r)=0\ (r<0),\qquad e_\eta=m_1(\eta)-1.
\tag{HA.7}
\]
The exact fat-point jet action is proved in T-042 §2: at a fixed point,
the canonical invariant affine chart has tangent representation
\(E/\mathbf Q\ell_i\), and the line twist has trivial stabilizer
character. The total jet trace is
\(m_1h_\eta(k-1)\). Therefore, for \(j=0,-1,-2\),
\[
\operatorname{tr}(\eta\mid\chi(\mathcal I^k(2k+j)))
=h_\eta(2k+j)-m_1h_\eta(k-1).
\tag{HA.8}
\]
This identity uses the ideal evaluation sequence as an Euler identity,
so it does not require its map on global sections to be onto at
\(j=-1,-2\). At \(k=0\), the negative scalar twists \(-1,-2\)
are acyclic, exactly matching the convention in (HA.7).

The hook trace is
\(\chi_{H_a(E)}(\eta)=e_\eta h_\eta(a)-h_\eta(a+1)\), by the
polarization splitting. Combining (HA.6)–(HA.8) specifies the complete
trace for every parameter. At the identity, it gives the useful check
\[
\boxed{\dim D_{a,k}=
\frac{a(a+2)}6\bigl[
a(4k^2+8k+3)+3k^3+13k^2+20k+9\bigr].}
\tag{HA.9}
\]
It specializes to \(a(a+2)(a+3)/2\) at \(k=0\) and to five times
that dimension at \(k=1\).

For a finite rational specification of the residue-polynomial bound,
let \(H(z)=\det(1-z\eta\mid E)^{-1}\), and put
\[
E_\eta(t)=\sum_{k\ge0}h_\eta(2k)t^k,\qquad
O_\eta(t)=\sum_{k\ge0}h_\eta(2k+1)t^k,\qquad
J_\eta(t)=m_1tH(t).
\]
They are obtained by the exact even and odd parts of \(H\). If
\(D(z)=\det(1-z\eta\mid E)\), the even numerator is
\((D(z)+D(-z))/2\) and the odd numerator is
\((D(-z)-D(z))/(2z)\), both over \(D(z)D(-z)\); replacing
\(z^2\) by \(t\) gives the two rational functions just defined.
For the nonnegative first parameter \(b=a-1\), the full bivariate
trace is
\[
\boxed{\begin{aligned}
\sum_{b,k\ge0}\chi_{D_{b+1,k}}(\eta)s^bt^k
={}&\frac{(e_\eta-s^{-1})H(s)+s^{-1}}s
                       (E_\eta(t)-J_\eta(t))\\
&+H(s)\bigl[tE_\eta(t)-e_\eta tO_\eta(t)
                              +(e_\eta-1)J_\eta(t)\bigr].
\end{aligned}}
\tag{HA.10}
\]
The apparent negative powers of \(s\) cancel: the numerator's
constant and linear terms vanish before division by \(s^2\).
Each of its four one-variable factors has denominator dividing
\((1-v^{60})^4\), with common numerator degree at most 239.
All 28 polynomial divisibilities for the seven classes are verified
exactly in the certificate, with the reduced factors retained in its
summary. The even/odd scalar series are separately checked against
direct permutation-cycle recurrences.

It follows, by the residue argument proved explicitly in T-040 §4
and T-042 §3, that on each residue pair \((r,s)\),
\(D_{1+r+60q,s+60p}\) has irreducible multiplicities polynomial of
degree at most three in each of \(q,p\), for all \(q,p\ge0\).
The initial range is included because the residue numerator has degree
at most three: its binomial coefficient polynomials vanish at every
required small value, not just eventually.

The bidegree \((3,3)\) coefficient is zero. Every nonidentity class
has pole order at most three in the standard-module variable, so its
\(b\)-residue degree is at most two. The identity dimension (HA.9)
has no monomial of bidegree \((3,3)\), even after replacing \(a\)
by \(b+1\). Thus the mixed third difference vanishes in every class.

## 4. Complete positive constants and actual polytopes

Let \(m_\nu(b,k)=[D_{b+1,k}:[\nu]]\). It is explicitly specified
by taking the inner product of (HA.6)–(HA.8) with the seven fixed
character rows in T-040 §4, of class sizes
\(1,10,15,20,20,30,24\). Define
\[
\boxed{c_{\nu,r,s;i,j}=
\sum_{u=0}^i\sum_{v=0}^j
(-1)^{i+j-u-v}\binom iu\binom jv
m_\nu(r+60u,s+60v),}
\tag{HA.11}
\]
for \(0\le r,s<60\), \(0\le i,j\le3\). The exact finite
certificate computes all 403,200 integers, proves each is nonnegative,
and finds \(c_{\nu,r,s;3,3}=0\). Every other positive-order constant
is strictly positive. Their minimum is 941; the maximum of all constants
is 1213066800, less than \(2^{31}\). All zeroth-order constants are
also nonnegative, as they are actual module multiplicities.

Every value is explicitly specified by (HA.7), (HA.8), the finite
character table, and (HA.11), and is supplied literally in
`HOOK_ALL_POWERS_TABLE.json`. The index is
`labels[nu][(a-1)_mod_60][k_mod_60][4*i+j]`.
The complete exact computation is `hook_all_powers_certificate.py`;
its summary contains every rational factor and all sixteen minima and
maxima for each label. The receipt is `HOOK_ALL_POWERS_CHECK.txt`.

Newton's identity and the rational degree bound prove, for all
\(q,p\ge0\),
\[
\boxed{m_\nu(r+60q,s+60p)=
\sum_{i,j=0}^3 c_{\nu,r,s;i,j}\binom qi\binom pj.}
\tag{HA.12}
\]
For the actual outer partition put \(\nu=\mu\) when \(d+a\) is
even and \(\nu=\mu^t\) when it is odd. For each tag
\((r,s,i,j)\ne(r,s,3,3)\), use the bounded rational polytope
\[
\begin{gathered}
60q=a-1-r,\qquad60p=k-s,\qquad q,p\ge0,\\
0\le z\le c_{\nu,r,s;i,j}-1,\\
1\le x_1<\cdots<x_i\le q,\qquad
1\le y_1<\cdots<y_j\le p.
\end{gathered}
\tag{HA.13}
\]
Omit an empty chain. Replace strict inequalities by difference-at-least-
one inequalities for the integer points. Zero constants give empty
polytopes. The chains choose subsets and the interval supplies the
constant factor, so the tagged count is exactly
\[
\boxed{p_{\mu,(n)}^\lambda=m_\nu(a-1,k).}
\tag{HA.14}
\]
Only one residue pair contributes. There are at most 54,000 uniform
tags and fifteen contributing tags; \(3+i+j\le8\) variables suffice.
All nonconstant witness coordinates have logarithmic bit length in
\(a+k+2\), and the fixed interval has an absolute 31-bit bound.

`hook_all_powers_positive.py` is the standalone evaluator and explicit
constraint-matrix exporter. It evaluates the fifteen binomial products
from the fixed table, validates \(a\ge1,k,d\ge0\), and requires no
runtime character or algebraic elimination computation.

## 5. Complete support

In terms of \(b=a-1\), the full untwisted zero sets are:

| \(\nu\) | zero pairs \((b,k)\) |
|---|---|
| \((5)\) | \((0,0),(0,1),(0,2),(1,0),(2,0)\) |
| \((4,1)\) | \((0,0)\) |
| \((3,2)\) | \((0,0)\) |
| \((3,1,1)\) | none |
| \((2,2,1)\) | \((0,0)\) |
| \((2,1,1,1)\) | \((0,0),(1,0)\) |
| \((1^5)\) | \((0,0),(0,1),(0,2),(1,0),(2,0),(3,0),(4,0)\) |

There are seventeen pairs across all rows. The finite residue table
checks the zeros in its 60-by-60 box. Outside it, at least one quotient
parameter is positive; the corresponding strictly positive first
difference in (HA.12) proves positivity. Apply the label conversion
preceding (HA.13) to obtain the complete support for any outer partition.

There is also the explicit small-box propagation check. Multiplication
by the invariant quadratic section \(\sigma_Q\in H^0(\operatorname{Sym}^2Q)\)
from (OS.19) preserves the hook kernel:
\(Q\otimes\operatorname{Sym}^aQ\to
Q\otimes\operatorname{Sym}^{a+2}Q\) sends its product to the old
product times \(\sigma_Q\), so zero products remain zero. The
multiplication is injective on every fiber, since \(\sigma_Q\) is
nonzero there. It gives an equivariant injection
\(D_{a,k}\hookrightarrow D_{a+2,k}\).
Multiplication by the invariant nonzero section \(e_2(T)\in\mathcal I^2(4)\)
gives \(D_{a,k}\hookrightarrow D_{a,k+2}\), exactly as in (OS.20).
The values with \(0\le b,k\le7\) already have exactly the displayed
zeros, and rows or columns six and seven are positive. Reduction by
even increments and these injections therefore prove the same entire
support from that smaller finite box.

In particular, for symmetric outer power and \(k\ge1\), positivity
is equivalent to \(a\ge2\) or \(k\ge3\). At \(k=0\), it is
equivalent to \(a\ge4\) in even parity \(d+a\), and to \(a\ge6\)
in odd parity. These are just the two relevant rows of the complete
zero table.

## Checks, source attribution, and next scope

`check_hook_all_powers_evaluator.py` passed 5222 evaluator comparisons:
1680 specializations to T-041 at \(k=1\), 2534 to the independently
proved G-018 at \(a=1\), and 1008 literal polytope counts. It checked
10,670 explicit matrix witnesses. Receipt:
`HOOK_ALL_POWERS_EVALUATOR_CHECK.txt`.

The rectangular agent independently checked all 392 actual plethysm
coefficients with \(a+k+d\le6\), for all seven outer labels. The
plethysm side uses cycle-index expansion and Murnaghan–Nakayama; the
proposed side uses direct Schur/Euler/jet traces, without the fixed
Newton table. All passed. Its receipt is
`work/rectangular/OUTER5_ALL_POWER_HOOK_INDEPENDENT_CHECK.tsv`.

The only ideal-power vanishing imported is the applied A-029 result,
with its actual ideal hypotheses checked against
[Kustin–Polini–Ulrich, formula (6.1.4), p. 1509, Lemma 6.3 and Corollary 6.4, p. 1510](https://msp.org/ant/2017/11-7/ant-v11-n7-p01-p.pdf).
The projective scalar vanishings and explicit Čech calculation are
[Stacks Project, Lemma 30.8.1](https://stacks.math.columbia.edu/tag/01XS).
The relative Schur convention and its dual comparison are those of
[Magyar, Propositions 1 and 4](https://arxiv.org/pdf/alg-geom/9411014),
with every determinant pairing spelled out above and in T-041.
The hook resolution itself was proved with its actual maps in T-041;
its ideal-tensored cohomology is proved here for all point orders.

This completes the hook quotient family on the quadratic ray. G-019
and T-042 evaluate symmetric quotient functors on the two adjacent
twists. More general two-row quotient shapes have a longer range of
parameters; no assertion about their positive residue constants is
assumed in the statements above.
