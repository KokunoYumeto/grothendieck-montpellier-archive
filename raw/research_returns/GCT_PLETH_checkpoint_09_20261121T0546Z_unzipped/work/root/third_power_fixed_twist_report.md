# Positive formulas through the complete third ideal order

## G-032. All three remaining twists at order three

Let \(x,b,d\ge0\), \(c\in\{0,1,2\}\), and
\(2b+x+3c\ge15\). Put
\[
\begin{aligned}
n&=d+b+x+c-3,\\
\lambda&=(d+3b+2x+4c-15,\ d+b+x+c,\\
&\hspace{30mm}d+b+x,\ d+x,\ d).
\end{aligned}
\tag{FT.1}
\]
Every \(p_{\mu,(n)}^\lambda\), \(\mu\vdash5\), has the
fixed positive formula (FT.9). For each twist, the branch \(b\ge8\)
uses at most seventeen selected bounded integer polytopes, with at most
eight variables. Each branch \(0\le b\le7\) uses at most four
polytopes with at most five variables. Every fixed constant is specified
by the finite formulas below, and all 1,552,320 constants are certified
nonnegative. The exact zero sets are recorded in §5.

Together with the previously proved twist families, this completes
**every ideal order at most three**. In the original partition variables
it gives a fixed positive coefficient formula whenever
\(\lambda_2\le n+3\) or \(\lambda_4\ge n-3\), through
the explicit maps in §6. No historical priority claim is made.

## 1. The actual rank-three representation and sheaf maps

Set \(a=b+x\), \(E=\mathfrak h_5\), \(F=\mathbb Q^3\),
\(\alpha=(a+c,b+c,c)\), and \(N=2b+x+3c\). Let
\(\ell_i=e_i-\frac15\sum_j e_j\) and
\(J_3=\bigcap_{i=1}^5(\ell_i\otimes F)^3\) in
\(\operatorname{Sym}(E\otimes F)\). The actual normal substitution,
Young extraction and inverse balanced homogenization of G027/T049 give
\[
\begin{aligned}
M_{x,b,c}&=\operatorname{Hom}_{GL(F)}(S_\alpha F,(J_3)_N),\\
(S_\lambda\mathbb Q^5)_{(n^5)}
&\simeq\operatorname{sgn}^{d+a+c}\otimes M_{x,b,c}.
\end{aligned}
\tag{FT.2}
\]
The inverse polynomial chart is \(u^{-3}F(v(X))\), with the
normal-order membership proved in G027. It is a map into the original coordinate ring.

For the five-point ideal sheaf \(\mathcal I_Z\) on
\(\mathbf P(E)\) and its tautological quotient \(Q\), the same
comparison is
\[
M_{x,b,c}\simeq\operatorname{sgn}^{c}\otimes
H^0(\mathcal I_Z^3(c)\otimes S_{(a,b)}Q).
\tag{FT.3}
\]
Indeed the exterior-column pairing gives
\(S_\alpha Q=(\det Q)^c\otimes S_{(a,b)}Q\), and
\(\det Q=\det E\otimes\mathcal O(1)\), with
\(\det E=\operatorname{sgn}\). This gives both the displayed
line twist and its exact constant-group character. The sign in (FT.2)
therefore agrees with G021's sign \(\operatorname{sgn}^{d+a}\)
after (FT.3).

Write \(\nu=\mu\) when \(d+a+c\) is even and
\(\nu=\mu'\) when it is odd. The desired coefficient is
\([\nu:M_{x,b,c}]\).

## 2. A finite exact character with every normal term specified

For a cycle type \(\gamma\), define
\[
h_\gamma(t)=[z^t]\frac{1-z}{\prod_{\ell\in\gamma}(1-z^\ell)},
\qquad h_\gamma(t)=0\quad(t<0).
\]
For \(\rho\subseteq\alpha\) with at most three rows put
\[
K_\gamma(\alpha;\rho)
=\det\bigl(h_\gamma(\alpha_i-\rho_j-i+j)\bigr)_{1\le i,j\le3},
\tag{FT.4}
\]
and set it to zero when \(\rho\not\subseteq\alpha\). This is
the skew Schur trace on the actual complementary standard module.
The precise known identity is Macdonald, *Symmetric Functions and Hall
Polynomials*, second edition, Chapter I §5, equations (5.3)–(5.4),
printed p.70, and containment convention (5.7), p.71. Its primary
text and derivation were read for G030.

The normal factor is
\(T_3(F)=\mathbb Q\oplus F\oplus\operatorname{Sym}^2F\).
For each selected cycle type \(\eta\) of total size at most three,
its literal cyclic tensor trace is the finite polynomial
\[
P_\eta(X_1,X_2,X_3)=
\prod_{\ell\in\eta}
\bigl(1+h_1(X_1^\ell,X_2^\ell,X_3^\ell)
       +h_2(X_1^\ell,X_2^\ell,X_3^\ell)\bigr).
\tag{FT.5}
\]
Let \(\delta=(2,1,0)\). All its Schur coefficients are specified
by the six-term formula
\[
c_\eta(\rho)=
\sum_{\sigma\in S_3}\operatorname{sgn}(\sigma)
[X^{\rho+\delta-\sigma\delta}]P_\eta(X),
\qquad \rho_1\ge\rho_2\ge\rho_3\ge0.
\tag{FT.6}
\]
A negative exponent contributes zero. Multiplication by the Vandermonde
alternant proves (FT.6): the coefficient at the strictly decreasing
exponent \(\rho+\delta\) in each Schur alternant is its diagonal
term, and no other dominant weight contributes. Each polynomial has
degree at most six. In particular \(\rho_1\le6\),
\(\rho_2\le3\), \(\rho_3\le2\). The complete finite
expansions for \(\eta=\varnothing,1,11,2,111,21,3\) are saved
in the certificate. For example, the last one is
\[
\begin{aligned}
P_{(3)}={}&1+s_{111}-s_{21}+s_{222}+s_3-s_{321}\\
&+s_{33}+s_{411}-s_{51}+s_6.
\end{aligned}
\]
Thus the formula retains negative normal characters even where the
corresponding initial monomial is absent.

The G027 restriction complex has, at a selected subset \(A\) of
size \(s\le3\), the actual module
\(T_3(F)^{\otimes s}\otimes\operatorname{Sym}(\mathfrak h_{5-s}\otimes F)\)
with its orientation line. Every term at size at least four is already a quotient by four
independent truncated blocks, whose total available degree is at most
eight. Thus every such term vanishes in degree \(N\ge15\). The exact quotient and
restriction maps, including the dependent last normal, are G027/FA13–17.
Consequently its alternating Schur extraction gives the actual trace
\[
\begin{aligned}
t_g(x,b,c)=
\sum_{\substack{A\subseteq\{1,\ldots,5\}\\ |A|\le3,\ gA=A}}
(-1)^{\#\operatorname{cyc}(g|A)}
\sum_{\rho}c_{\operatorname{cyc}(g|A)}(\rho)
K_{\operatorname{cyc}(g|A^c)}(\alpha;\rho).
\end{aligned}
\tag{FT.7}
\]
The sign is \((-1)^s\) from complex degree times
\((-1)^{s-\#\operatorname{cyc}(g|A)}\) from its orientation.
The complete trace becomes the integer coefficient
\[
f_\nu(x,b,c)=\frac1{120}\sum_{[g]}|[g]|\chi_\nu(g)t_g(x,b,c).
\tag{FT.8}
\]
The seven class sizes and character rows are the fixed table in T044,
also reproduced by the executable evaluator. Thus (FT.4)–(FT.8)
specify all numerical data using finite products, determinants and
fixed character sums; no plethysm oracle is involved.

## 3. The polynomial domains, including every initial boundary

Fix \(c\in\{0,1,2\}\). Every root in the generating series
for \(h_\gamma\) has order dividing60. Partial fractions therefore
make each nonnegative-index sequence polynomial on every residue
class modulo60. For the empty-subset identity contribution, the exact
dimension is
\[
\frac{(x+1)(b+x+2)(b+x+c+3)(b+1)(b+c+2)(c+1)}{12}.
\]
It has total degree five and separate degrees at most \((3,4)\)
in \((x,b)\).

Here are sufficient bounds for every other term, with their degree
cancellations checked. Expanding (FT.4) along its third row makes it a
linear combination of two-by-two determinants whose row arguments are
\(b+x+c+u\) and \(b+c+v\), with fixed shifts. For a nonidentity
class on \(E\), the only eigenvalue with multiplicity three is
\(1\) for a transposition; its complete trace has a quadratic part
with constant leading coefficient. The degree-four products in each
two-by-two determinant agree and cancel. All other eigenvalues have
multiplicity at most two. Hence every nonidentity empty-subset term
has total degree at most three and degree at most two in \(x\).

At a singleton subset, the complementary identity complete traces
are quadratic, with the same leading-term cancellation; their total
degree is at most three. The other complementary classes have at most
linear complete traces. At a two-element subset the identity complete
traces are linear and the degree-two products cancel, leaving total
degree at most one; other complementary traces are periodic. At a
three-element subset the complementary module is a line and all its
nonnegative-index traces are periodic. These arguments hold on each
fixed residue class, where all root-of-unity factors are constants.
Thus the total and separate bounds \(5,(3,4)\) hold throughout the
bulk.

For that bulk put \(b=B+8\), \(B\ge0\). Every index in the
first two rows of (FT.4) is nonnegative, since \(\rho_1\le6\).
The third-row indices and the condition \(\rho_3\le c\) are
fixed. Therefore the stated polynomial bounds hold from the origin
of each whole bulk residue class.

For \(0\le b\le7\), put
\[
x=X+q_{b,c},\qquad q_{b,c}=\max(0,15-3c-2b),\qquad X\ge0.
\]
The least value of \(\alpha_1=b+x+c\) on these24 branches is
seven. Thus every varying first-row index is nonnegative and every
first-row containment condition is automatic. The second and third
rows, including their exact zero values at negative indices and their
containment tests, are fixed independently of \(X\). Each boundary
residue polynomial therefore starts at \(X=0\) and has degree at
most three. This verifies all initial-range issues needed for Newton
interpolation, including the branches with \(q_{b,c}=0\).

## 4. All positive constants and their actual bounded polytopes

For the bulk let \((x,B)=r+60Q\), \(0\le r_i<60\), and set
\[
\begin{aligned}
C^{c}_{\nu,r;i,j}={}&
\sum_{u=0}^i\sum_{v=0}^j
(-1)^{i+j-u-v}\binom iu\binom jv\\
&\hspace{8mm}\cdot f_\nu(r_1+60u,r_2+60v+8,c),
\qquad 0\le i\le3,\ 0\le j\le4.
\end{aligned}
\]
For a boundary \(b\), let \(X=r+60Q\) and define
\(D^c_{\nu,b,r;i}=\sum_{u=0}^i(-1)^{i-u}\binom iu
f_\nu(r+60u+q_{b,c},b,c)\), \(0\le i\le3\).
The exact finite Newton identity now gives
\[
\boxed{
\begin{aligned}
p_{\mu,(n)}^\lambda
 &=\sum_{i=0}^3\sum_{j=0}^4C^c_{\nu,r;i,j}
                \binom{Q_1}{i}\binom{Q_2}{j} &&(b\ge8),\\
p_{\mu,(n)}^\lambda
 &=\sum_{i=0}^3D^c_{\nu,b,r;i}\binom Qi &&(b\le7).
\end{aligned}}
\tag{FT.9}
\]
Here \(\nu\) is exactly the parity-adjusted label after (FT.3).

The finite certificate evaluates the complete domains of every
constant, using (FT.4)–(FT.8) and integer arithmetic. For each twist
it checks \(7\cdot60^2\cdot4\cdot5=504000\) bulk constants
and \(8\cdot7\cdot60\cdot4=13440\) boundary constants.
Every constant is nonnegative. The active bulk orders are precisely
\[
\{(0,j):0\le j\le4\}\ \cup\
\{(1,j):0\le j\le4\}\ \cup\
\{(2,j):0\le j\le3\}\ \cup\
\{(3,j):0\le j\le2\}.
\]
Every active constant of positive order is strictly positive, as are
all boundary constants of orders one through three.

The proof certificate is `third_power_fixed_twist_certificate.py`
with its complete arithmetic specification in
`fixed_twist_arrangement.py`; the receipt is
`THIRD_POWER_FIXED_TWIST_CERTIFICATE.json`. Every array hash, minimum,
maximum, zero set and operation bound is recorded. Before every
vectorized multiplication and accumulated trace, the script proves an
absolute bound from the maxima of the factors. Before taking differences,
it checks \(2^7\max|f|<2^{63}\) in the bulk and the corresponding
\(2^3\) bound at a boundary. Hence every integer operation is exact.
The largest trace-operation bound in these computations is
4,176,326,138,215,440, strictly below \(2^{63}\). This receipt is
an exhaustive finite arithmetic certificate, not a sampled positivity
claim.

For a positive bulk constant \(C\) and order \((i,j)\), use
integer variables
\[Q_1,Q_2,y,z_{1,1},\ldots,z_{1,i},z_{2,1},\ldots,z_{2,j},\]
with the exact constraints
\[
\begin{gathered}
60Q_1=x-r_1,\quad60Q_2=B-r_2,\quad Q_1,Q_2\ge0,\quad0\le y<C,\\
0\le z_{1,1}<\cdots<z_{1,i}<Q_1,\qquad
0\le z_{2,1}<\cdots<z_{2,j}<Q_2.
\end{gathered}
\tag{FT.10}
\]
The chain with length zero is omitted. The choices of the two subsets
and of \(y\) give a literal bijection with the corresponding summand
of (FT.9). Replace strict integer inequalities by a difference of at
least one to obtain closed integral halfspaces. The equations fix
\(Q_1,Q_2\), all remaining variables are bounded, and
\(i+j\le5\), proving the eight-variable bound. The one-chain
boundary construction gives five variables. Zero constants give empty
sets and are omitted; distinct order/residue tags give a disjoint union.
`third_power_fixed_twist_positive.py` writes the literal matrices,
evaluates the formula and emits actual witness tuples.

## 5. Complete support in the three slices

A positive-order constant is strictly positive in every residue class.
Thus every point with at least one positive bulk quotient, or a positive
boundary quotient, has positive multiplicity. The bulk exceptions are
only \(c=0,\nu=(1^5),(x,B)=(0,0),(0,1)\). In the boundary
catalog below, an omitted row has no zeros; the listed integers are
exact \(X=x-q_{b,c}\), not congruence classes repeated periodically.

| Twist c | Boundary b | Shift q | Effective label | All zero X |
|---|---|---|---|---|
| 0 | 0 | 15 | \((5)\) | 1 |
| 0 | 0 | 15 | \((4,1)\) | 0 |
| 0 | 0 | 15 | \((3,2)\) | 0, 1 |
| 0 | 0 | 15 | \((3,1,1)\) | 0, 1, 2 |
| 0 | 0 | 15 | \((2,2,1)\) | 0, 1, 2, 3 |
| 0 | 0 | 15 | \((2,1,1,1)\) | 0, 1, 2, 3, 4, 5 |
| 0 | 0 | 15 | \((1^5)\) | 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 11 |
| 0 | 1 | 13 | \((5)\) | 0, 1 |
| 0 | 1 | 13 | \((3,2)\) | 0 |
| 0 | 1 | 13 | \((3,1,1)\) | 0 |
| 0 | 1 | 13 | \((2,2,1)\) | 0, 1 |
| 0 | 1 | 13 | \((2,1,1,1)\) | 0, 1, 2 |
| 0 | 1 | 13 | \((1^5)\) | 0, 1, 2, 3, 4, 5 |
| 0 | 2 | 11 | \((3,1,1)\) | 0 |
| 0 | 2 | 11 | \((2,2,1)\) | 0 |
| 0 | 2 | 11 | \((2,1,1,1)\) | 0, 1 |
| 0 | 2 | 11 | \((1^5)\) | 0, 1, 2, 3 |
| 0 | 3 | 9 | \((2,2,1)\) | 0 |
| 0 | 3 | 9 | \((2,1,1,1)\) | 0 |
| 0 | 3 | 9 | \((1^5)\) | 0, 1, 2 |
| 0 | 4 | 7 | \((2,1,1,1)\) | 0 |
| 0 | 4 | 7 | \((1^5)\) | 0, 1 |
| 0 | 5 | 5 | \((2,1,1,1)\) | 0 |
| 0 | 5 | 5 | \((1^5)\) | 0, 1 |
| 0 | 6 | 3 | \((1^5)\) | 0 |
| 0 | 7 | 1 | \((5)\) | 0 |
| 0 | 7 | 1 | \((2,1,1,1)\) | 0 |
| 0 | 7 | 1 | \((1^5)\) | 0, 1 |
| 1 | 0 | 12 | \((5)\) | 0, 1, 2, 3, 4 |
| 1 | 0 | 12 | \((4,1)\) | 0, 1 |
| 1 | 0 | 12 | \((3,2)\) | 0 |
| 1 | 0 | 12 | \((2,2,1)\) | 0 |
| 1 | 0 | 12 | \((2,1,1,1)\) | 0 |
| 1 | 0 | 12 | \((1^5)\) | 0, 1, 2 |
| 1 | 1 | 10 | \((5)\) | 0, 1 |
| 1 | 1 | 10 | \((2,1,1,1)\) | 0 |
| 1 | 1 | 10 | \((1^5)\) | 0, 1 |
| 1 | 2 | 8 | \((5)\) | 0 |
| 1 | 2 | 8 | \((1^5)\) | 0 |
| 1 | 3 | 6 | \((1^5)\) | 0 |
| 1 | 4 | 4 | \((5)\) | 0 |
| 1 | 4 | 4 | \((1^5)\) | 0 |
| 1 | 6 | 0 | \((5)\) | 0 |
| 1 | 6 | 0 | \((2,2,1)\) | 0 |
| 1 | 6 | 0 | \((1^5)\) | 0 |
| 2 | 0 | 9 | \((3,1,1)\) | 0 |
| 2 | 0 | 9 | \((2,1,1,1)\) | 0 |
| 2 | 0 | 9 | \((1^5)\) | 0, 1, 3 |
| 2 | 1 | 7 | \((1^5)\) | 0 |
| 2 | 3 | 3 | \((1^5)\) | 0 |
| 2 | 5 | 0 | \((1^5)\) | 0 |

## 6. Completion of the third order and the exact complement map

For ideal order three, the cases c=0,1,2 are exactly (FT.1).
The remaining twists are c=3 by T051, c=4 by T050, c=5 by T045,
and c≥6 by G021. These disjoint cases cover every nonnegative twist.
G026/G030 and their already proved boundary families cover orders one
and two. At order zero the stable chart is onto, with multiplication
by the exact invariant section u carrying every extra first-row degree.
Consequently every shape with λ₂≤n+3 is evaluated.

For the complementary range use H=λ₁ and
\(\lambda^c=(H-\lambda_5,H-\lambda_4,H-\lambda_3,
H-\lambda_2,0)\), of size 5(H−n). The actual perfect pairing
\(S_\lambda\mathbb Q^5\otimes S_{\lambda^c}\mathbb Q^5
\to(\det\mathbb Q^5)^H\) is exterior contraction on each
complementary column followed by the paired Young projectors.
Restricting to balanced weights pairs the two weights n and H−n,
and the constant symmetric group acts on the target by sgn^H.
The rational invariant Gram pairing identifies every finite symmetric-group dual. Thus the effective outer label is transposed precisely
when H is odd. The complementary order is
\(\max(0,(H-\lambda_4)-(H-n))=\max(0,n-\lambda_4)\).
This proves the claimed coverage λ₄≥n−3, with every map and sign fixed.

The remaining direct coefficient-formula gate in these coordinates is
therefore k≥4 and 0≤c≤2k−4, after also removing the complementary
range and the separately completed staircase and other families.
G031 continues to decide every zero even throughout that remaining gate.

## 7. Grothendieck-language transport and proof checks

The scheme and sheaf content is the actual coherent section module
(FT.3), carried by the quotient substitution and exterior determinant
pairings of (FT.2). The ideal inclusions, restrictions and diagonal
quotient are equivariant coordinate-ring morphisms; their affine and
projective schemes use EGA II2.4.1–2.4.2, p.28, and2.5.2/2.5.4,p.31.
Every Young and finite-group projector is a rational direct summand.
The frame-torsor functor sends these equivariant maps to the identical
associated-bundle maps, as in SGA3 I4.5 and4.7.2–4.7.3. Their exact
representation and locally free sheaf classes are carried by SGA6
VI3.3; SGA6 V4.2,4.4,4.8–4.9 specify the universal λ-operation and
finite-rank evaluation. The restriction complex therefore gives the
stated class through actual coherent modules, and (FT.10) counts its
Schur coefficient. In the archive, this evaluates the Schur/tensor
composition of cote133/028 through the explicit tensor-word, torus
weight and Young maps of A012. The appendix's locator register states
the scope of each cited Grothendieck construction.

The scalar implementation was independently compared with literal
balanced Schur cycle traces on3353 actual coefficients, including
all valid k=1,2,3,c=0,1,2,b≤8,x≤7 inputs. This checks all determinant
and sign conventions across the rank-two and rank-three boundaries.
The complete finite positivity calculation checks1,552,320 constants.
These computations and the full proof readings are recorded as
separate events. No random sample is used to establish the theorem.

The direct evaluator additionally passed2310 exact value comparisons,2282 literal witness-matrix checks and84 exhaustive small-witness enumerations; the receipt is `THIRD_POWER_EVALUATOR_CHECK.json`.
