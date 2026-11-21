# The exterior quotient bundle on the five-point ray

## G-018. An exact kernel and positive formula

For \(k,d\ge0\), put
\[
n=d+k+1,\qquad
\lambda=(d+3k+3,d+2k+1,d+1,d,d).
\tag{W.1}
\]
For every \(\mu\vdash5\), the coefficient \(p_{\mu,(n)}^\lambda\)
is a count in at most 240 fixed bounded rational polytopes, with at most
five integer variables. The fixed table and every inequality are given
below. Its support is particularly simple: after setting
\(\nu=\mu\) for odd \(d\) and \(\nu=\mu'\) for even \(d\), it is
positive exactly in the following ranges:
\[
\begin{array}{c|c}
\nu&\text{range}\\\hline
(3,1,1)&k\ge0\\
(4,1),(3,2),(2,2,1),(2,1,1,1)&k\ge1\\
(5),(1^5)&k\ge3.
\end{array}
\tag{W.2}
\]
In particular the symmetric outer coefficient is positive exactly when
\(k\ge3\), independently of \(d\).

## 1. The flag morphism and the multiplication kernel

Use \(E=\mathfrak h_5\), its invariant form, the five-point ideal
\(\mathcal I\), and the tautological quotient bundle \(Q\) from
G-015 and T-038. Define
\[
W_k=H^0(\mathbf P(E),\mathcal I^k(2k)\otimes\Lambda^2Q).
\tag{W.3}
\]
For (W.1), the point order is \(\lambda_2-n=k\), the first-line
twist after relative duality is \(\lambda_2-\lambda_3=2k\), and the
quotient Schur weight is
\((\lambda_3-\lambda_5,\lambda_3-\lambda_4)=(1,1)\).
Explicitly, after the determinant factor \((\det E^*)^d\) the relative
flag weight is \((1,0,0)\), with first-line twist \(2k+1\).
The exterior pairing
\(Q^*\simeq\Lambda^2Q\otimes\det Q^*\) and
\(\det Q^*=\det E^*\otimes\mathcal O(-1)\) therefore give
\[
(S_\lambda\mathbf Q^5)_{(n^5)}\simeq\operatorname{sgn}^{d+1}\otimes W_k.
\tag{W.4}
\]
These relative Schur evaluations and the inverse balanced chart
\(f\mapsto u^{-k}f(v(X))\) are the actual maps in G-015 and T-039 §1.

Set \(C_{j,k}=H^0(\mathcal I^k(2k+j))\), for \(j=1,2\).
A-029 proves \(C_{j,k}=(I^k)_{2k+j}\) for \(k\ge2\); saturation of
\(I\) proves the same for \(k=1\), and \(k=0\) is immediate.
The ideal \(I^k\) is generated in degree \(2k\). Hence multiplication
by linear forms gives a surjection
\[
E^*\otimes C_{1,k}\longrightarrow C_{2,k}.
\tag{W.5}
\]
In coordinates it sends \(\sum e_i^*\otimes f_i\) to \(\sum z_if_i\).
The dual tautological sequence, tensored by \(\mathcal I^k(2k+1)\),
identifies its kernel with
\(H^0(\mathcal I^k(2k+1)\otimes Q^*)\). The exterior isomorphism
\(\Lambda^2Q\simeq Q^*\otimes\det Q\), where
\(\det Q=\operatorname{sgn}\otimes\mathcal O(1)\), consequently gives
the actual exact sequence
\[
\boxed{0\longrightarrow\operatorname{sgn}\otimes W_k
\longrightarrow E^*\otimes C_{1,k}
\longrightarrow C_{2,k}\longrightarrow0.}
\tag{W.6}
\]
The first map is the dual tautological inclusion followed by the specified
exterior pairing. Thus the character difference used next is the trace
of a concrete kernel of a surjective map.

## 2. Exact traces from the five fat-point jets

For a permutation \(g\in S_5\), let \(m_1(g)\) be its number of fixed
letters and let \(s_r(g)=\operatorname{tr}(g\mid\operatorname{Sym}^rE)\),
with \(s_r=0\) for \(r<0\). These traces are completely specified by
\[
\sum_{r\ge0}s_r(g)z^r
=\frac{1-z}{\prod_{\ell\in\operatorname{cyc}(g)}(1-z^\ell)}.
\tag{W.7}
\]
A-029 gives \(H^1(\mathcal I^k(2k+j))=0\) for \(j\ge0\), including
the separately verified \(k=0,1\). Therefore the evaluation sequence
for the fat points is exact on global sections in the degrees used here.

We specify the jet action, including its trivializations. The stabilizer
of \([\ell_i]\) fixes the affine vector \(\ell_i\) and decomposes
\(E=\mathbf Q\ell_i\oplus\mathfrak h_4\). The linear functional
equal to one on \(\ell_i\) and zero on \(\mathfrak h_4\) is invariant
under that stabilizer. Its affine chart trivializes every \(\mathcal O(c)\)
with trivial fiber character, and its normal coordinates transform by
\(\mathfrak h_4^*\). Thus the order-\(k\) jet module at that point is
\(\bigoplus_{r=0}^{k-1}\operatorname{Sym}^r\mathfrak h_4^*\).
Transport by the canonical affine representatives gives the induced
\(S_5\)-module of these jets. Only fixed points contribute to the trace
of \(g\); each contributes the same value. For a fixed point the
restriction \(E=\mathbf1\oplus\mathfrak h_4\) identifies the sum of
the first \(k\) symmetric powers with the trace of
\(\operatorname{Sym}^{k-1}E\). Hence the full jet trace is
\[
\operatorname{tr}(g\mid J_k)=m_1(g)s_{k-1}(g).
\tag{W.8}
\]
This proves, through the actual evaluation sequence,
\[
\operatorname{tr}(g\mid C_{j,k})=s_{2k+j}(g)-m_1(g)s_{k-1}(g).
\tag{W.9}
\]
Combining (W.6) and (W.9) gives
\[
w_k(g)=\operatorname{sgn}(g)\left[
(m_1-1)\{s_{2k+1}-m_1s_{k-1}\}
-\{s_{2k+2}-m_1s_{k-1}\}\right].
\tag{W.10}
\]
Every scalar on the right is specified by the finite rational function
(W.7). At the identity this gives
\[
\dim W_k=\frac{(k+2)(k+3)(3k+2)}2,
\qquad
\sum_{k\ge0}\dim W_k t^k
=\frac{6+6t-4t^2+t^3}{(1-t)^4}.
\tag{W.11}
\]
The initial value \(W_0=\Lambda^2E\) has label \((3,1,1)\), as required.

## 3. Fixed positive Newton data and its complete finite certificate

Let
\[
b_\nu(k)=\frac1{120}\sum_{g\in S_5}\chi_\nu(g)w_k(g).
\tag{W.12}
\]
This is the multiplicity of \([\nu]\) in the actual module \(W_k\).
The sum can equivalently be taken over the seven cycle types with sizes
\(1,10,15,20,20,30,24\), in the order of (Q.22).

For \(0\le r<60\) and \(0\le j\le3\), define the fixed integer
\[
c_{\nu,r,j}
=\sum_{h=0}^j(-1)^{j-h}\binom jh b_\nu(r+60h).
\tag{W.13}
\]
These 1680 integers are specified by (W.7), (W.10), (W.12), and (W.13),
using only symmetric groups of order at most 120 and indices at most
239. `FIVE_POINT_WEDGE2_NEWTON_TABLE.json` lists every one.

Here is the exact verification that extends this fixed data to every
input. Taking even and odd parts of (W.7) gives the rational series
\(\sum_ks_{2k}t^k\) and \(\sum_ks_{2k+1}t^k\). Subtracting its
constant term and dividing by \(t\) gives the series for \(s_{2k+2}\).
For each of the seven explicitly listed cycle types, substitution into
(W.10) shows that its denominator divides \((1-t^{60})^4\) and its
numerator has degree at most 239. These seven exact polynomial
divisibilities are checked in `five_point_wedge2_certificate.py`, with
their reduced rational functions retained in the JSON certificate.
The script also computes (W.7) directly by the seven cycle recurrences,
independently of the even/odd rational extraction.

A numerator degree at most 239 implies that, on a fixed residue \(r\),
the coefficient is a polynomial of degree at most three in
\(q=(k-r)/60\), for every \(q\ge0\). To check the initial endpoints,
each numerator exponent is \(r+60h\), \(0\le h\le3\), and its
contribution is \(\binom{q-h+3}{3}\). The polynomial expression is
zero also for \(0\le q<h\le3\), since its upper integer is then zero,
one, or two. Thus no delayed-onset term is lost. Newton interpolation
at \(q=0,1,2,3\) proves the identity
\[
\boxed{b_\nu(60q+r)=\sum_{j=0}^3 c_{\nu,r,j}\binom qj\quad(q\ge0).}
\tag{W.14}
\]

All 1680 integers (W.13) were computed exactly and are nonnegative;
the following minima over all 60 residues make their signs reviewable.

| \(\nu\) | min \(c_0\) | min \(c_1\) | min \(c_2\) | min \(c_3\) |
|---|---:|---:|---:|---:|
| \((5)\) | 0 | 2877 | 16560 | 16200 |
| \((4,1)\) | 0 | 11693 | 66540 | 64800 |
| \((3,2)\) | 0 | 14725 | 83400 | 81000 |
| \((3,1,1)\) | 1 | 17787 | 100260 | 97200 |
| \((2,2,1)\) | 0 | 14880 | 83700 | 81000 |
| \((2,1,1,1)\) | 0 | 12003 | 67140 | 64800 |
| \((1^5)\) | 0 | 3032 | 16860 | 16200 |

The accompanying TSV has one row for each label and residue, with all
four entries. Its generating code contains the full exact finite check,
not a random or asymptotic test. Direct evaluation of (W.12) through
\(k=359\) also agrees with (W.14) in every case. This extra finite
check is recorded separately from the rational identity that proves
the formula in all degrees.

For each tag \((r,j)\) with \(c=c_{\nu,r,j}>0\), use integer variables
\(q,y,t_1,\ldots,t_j\) and inequalities
\[
60q+r=k,\quad q\ge0,\quad0\le y<c,\quad
1\le t_1<t_2<\cdots<t_j\le q.
\tag{W.15}
\]
For \(j=0\), the last list is empty. Replace strict integer inequalities
by \(y\le c-1\) and \(t_i+1\le t_{i+1}\) to obtain the rational
polytope. Its lattice count is exactly \(c\binom qj\), by the bijection
with a choice of \(y\) and a \(j\)-element subset of \(\{1,\ldots,q\}\).
Every variable is bounded. Summing these 240 tagged sets proves the
positive formula for (W.1) using the sign twist (W.4).

The fixed zeroth entries in residues zero through 59 have zeros exactly
at the excluded degrees in (W.2). For \(k\ge60\), the positive
first differences in the table and \(q\ge1\) prove positivity.
This proves the complete support statement, including all endpoints.

## Geometric transport

This result is the global-section representation of the ideal-twisted
exterior quotient bundle (W.3). The flag chart (W.4), dual tautological
inclusion (W.6), and affine jet trivializations (W.8) specify every
comparison. Associated bundles along the frame torsor carry the Schur
operations to the SGA 6 representation-group dictionary; the point
scheme, ideal powers, and their evaluation maps give the EGA/FGA
objects. The exact framework locators are listed in the separate
geometric dictionary. All representation assertions here are over
characteristic-zero fields.
