# The complete zero-twist wall in every ideal order

## G-033. A fixed positive formula for all orders on the wall

Let \(k,x,b,d\ge0\) with \(2b+x\ge5k\), and put
\[
\begin{aligned}
n&=d+b+x-k,\\
\lambda&=(d+3b+2x-5k,d+b+x,d+b+x,d+x,d).
\end{aligned}
\tag{ZW.1}
\]
For every \(\mu\vdash5\), the coefficient
\(p_{\mu,(n)}^\lambda\) has a fixed positive lattice-point
formula. The cases and their actual comparison maps are completely
specified in §5. In particular, this evaluates the entire wall
\(c=\lambda_2-\lambda_3=0\), for unbounded ideal order.

The new formulas are two adjacent chambers with respectively47
and34 selected polytopes, each with at most nine variables. They
complete the wall together with T054, the previously checked low
orders and the exact complementary-column maps. The overall formula
uses only the fixed formulas referenced in the exhaustive routing
table; it performs no input-sized representation computation.

## 1. Two parameter cones and their exact ideal modules

Define the following cones, with every displayed free parameter
nonnegative:
\[
\begin{array}{c|c|c|c|c}
&k&x&b&t=3k-3-b\\\hline
A&(T+6+K)&T+X&2T+15+3K&T\\
B&(X+2S+8+K)&X&2X+5S+20+3K&X+S+1.
\end{array}
\tag{ZW.2}
\]
Their partition gaps \(2b+x-5k\) are respectively \(X+K\)
and \(K\), so every parameter in these cones gives a valid
partition. They satisfy \(0\le t<k\) and \(b>2(k-1)\).

Put \(a=b+x\), \(E=\mathfrak h_5\), \(F=\mathbb Q^2\),
and \(J_k=\bigcap_i(\ell_i\otimes F)^k\). The actual
normal substitution and Young extraction of G027/T049 give
\[
M_{a,b,k}=\operatorname{Hom}_{GL(F)}(S_{(a,b)}F,(J_k)_{a+b}),
\qquad
(S_\lambda\mathbb Q^5)_{(n^5)}
\simeq\operatorname{sgn}^{d+a}\otimes M_{a,b,k}.
\tag{ZW.3}
\]
The inverse is the specified balanced homogenization
\(u^{-k}F(v(X))\). The normal-order proof establishes its
polynomial extension. Equivalently the module before the sign is
\(H^0(\mathcal I_Z^k\otimes S_{(a,b)}Q)\), through the
same quotient substitution and exterior-column pairing.

The signed restriction complex now has its three-subset term as
well as the singleton and pair terms. Its quotient maps and
orientation lines are G027/FA13–17. Terms at size at least four
have degree at most \(4(k-1)<a+b\) and vanish. The ambient,
singleton and pair traces are exactly the finite expression in
T054/VW9–12: the straightening involution in VW6 only requires
\(b\ge k-1\), and the pair exterior comparison requires
\(b\ge2(k-1)\). Both hold here. Denote their sum by
\(P_g^\circ(a,b,k)\). This is a known finite phase polynomial,
with its actual restriction maps fixed by T054. The remaining
term is evaluated next.

## 2. The exact high-tail character of every triple intersection

Fix a stable three-subset of a permutation \(g\). Let
\(\eta\) be its selected cycle type and let
\(\epsilon\in\{1,-1\}\) be the eigenvalue on the
one-dimensional complementary standard module. The normal
polynomial is
\[
P_\eta(U,V)=\prod_{\ell\in\eta}
\left(\sum_{i,j\ge0,\ i+j<k}U^{\ell i}V^{\ell j}\right).
\]
Write \(p_{r,s}=[U^rV^s]P_\eta\). Its Schur coefficient
at \((p,q)\) is \(p_{p,q}-p_{p+1,q-1}\), by the
rank-two alternant, including absent-monomial zeros.

The one-dimensional skew Schur factor is nonzero exactly when
\((a,b)/(p,q)\) is a horizontal strip. The actual Pieri
projection to the complementary line gives the value
\(\epsilon^{a+b-p-q}\) in that case. Its inequalities are
\(a\ge p\ge b\ge q\ge0\). Since the normal degree is
at most \(3(k-1)\) and \(b>2(k-1)\), the condition
\(q\le b\), and every ordering condition in the following
sum, are automatic when \(p\ge b\).

Set \(R_\eta(z)=P_\eta(\epsilon z,\epsilon)\).
The exact Schur sum telescopes in \(p\):
\[
\begin{aligned}
&\sum_{p=b}^{a}\sum_{q\ge0}
 (p_{p,q}-p_{p+1,q-1})\epsilon^{a+b-p-q}\\
&\qquad=\epsilon^{a+b}
\left([z^b]R_\eta(z)-[z^{a+1}]R_\eta(z)\right).
\end{aligned}
\tag{ZW.4}
\]
Indeed after multiplying by \(\epsilon^{p+q}\), the
second summand becomes the same coefficient array with
\((p,q)\) replaced by \((p+1,q-1)\). Its range cancels
every interior \(p\), leaving precisely the two boundary
columns. Negative \(q\) entries are zero. This proves every
sign in (ZW.4) by a literal finite reindexing.

Let \(M=3(k-1)\). Reverse each cyclic normal factor at its
highest \(z\)-degree. The factor for a cycle of length
\(\ell\) contributes the phase \(\epsilon^{\ell(k-1)}\)
and the reversed coefficient series
\[
\sum_{r=0}^{k-1}\sum_{j=0}^{r}
\epsilon^{\ell(j-r)}z^{\ell r}.
\]
Through any degree \(h<k\), the upper bound \(r<k\)
can be removed. Reindexing \(r=j+l\) sums two geometric
series and gives
\[
A_{\eta,\epsilon}(h)=
[z^h]\prod_{\ell\in\eta}
\frac1{(1-z^\ell)(1-\epsilon^\ell z^\ell)},
\qquad A_{\eta,\epsilon}(h)=0\ (h<0).
\tag{ZW.5}
\]
Thus \([z^{M-h}]R_\eta=\epsilon^M A_{\eta,\epsilon}(h)\)
for every needed \(h<k\). In (ZW.4) the deficits are
\(t\) and \(t-x-1\), and both cones have \(t<k\).
The selected triple's trace, before its orientation, is therefore
\[
\boxed{
\epsilon^{x+k-1}
\left(A_{\eta,\epsilon}(t)
      -A_{\eta,\epsilon}(t-x-1)\right).}
\tag{ZW.6}
\]
The exponent uses \(a+b+M\equiv x+k-1\pmod2\).
In cone A the second argument is \(-X-1\) and its term
vanishes. In cone B that argument is exactly \(S\).

Multiplying (ZW.6) by \((-1)^{\#\operatorname{cyc}(\eta)}\)
and summing over the at most ten stable three-subsets gives the
full section trace:
\[
\boxed{
P_g=P_g^\circ+
\sum_{\substack{|A|=3\\gA=A}}
(-1)^{\#\operatorname{cyc}(g|A)}
\epsilon_A^{x+k-1}
\left(A_{\eta_A,\epsilon_A}(t)
-A_{\eta_A,\epsilon_A}(t-x-1)\right).}
\tag{ZW.7}
\]
The orientation factor is the complex sign times the actual
three-subset orientation character. Thus (ZW.7) is the trace of
(ZW.3) through the given exact complex.

## 3. Fixed polynomial positivity certificates in both cones

Every denominator root in (ZW.5) has order dividing the period
of the full permutation \(g\). There are at most six denominator
factors, so each sequence has degree at most five on a residue
class. Its proper rational generating function gives that
polynomial from index zero. Six initial values at
\(r,r+L,\ldots,r+5L\) determine it exactly. This is a fixed
arithmetic construction of (ZW.5), with no varying summation.

Substitute (ZW.2) into T054's finite formulas and (ZW.7).
For cone A the input variables are \(Z=(X,T,K)\), and for
cone B they are \(Z=(X,S,K)\). The complete class polynomials
have respective separate-degree bounds \((3,3,4)\) and
\((3,2,4)\), and total degree at most five. In class order
\(1^5,2111,221,311,32,41,5\), their total degrees in each
cone are \((5,3,2,1,0,0,0)\). All449 phase polynomials in
each cone are specified by the above finite construction and
stored in the corresponding certificate.

For a nonzero mixed step60 order \(\delta\), subtract
from \(\Delta^\delta P_1\) the sum, over nonidentity
classes, of the class size times the coefficientwise maximum of
the absolute coefficients of \(\Delta^\delta P_g\) over
all its phases. This is precisely the rational domination
construction in T054§4. The following exhaustive facts hold:

| Cone | Nonzero active orders | Lowest constant margin | Largest total order |
|---|---:|---:|---:|
| A | 46 | 131670 | 5 |
| B | 33 | 8700 | 5 |

Every coefficient of every domination polynomial is nonnegative,
and every displayed constant margin is strictly positive. The
certificates record every polynomial and every order; the identity
polynomials also have only nonnegative coefficients. The scripts
expand affine substitutions, finite translations and rational
binomial coefficients exactly. Their parameter maps and phase keys
are part of the saved data.

The supporting files are `triple_defect_wall_check.py` with
`TRIPLE_DEFECT_WALL_CHECK.json`, and `inner_triple_wall_check.py`
with `INNER_TRIPLE_WALL_CHECK.json`. Each certificate is obtained
from the already independently checked T054 phase polynomials by
the explicit affine substitution (ZW.2) and the exact rational
series (ZW.5). All monomial supports are included in the checked
finite-difference order set, so every omitted order is zero.

For every irreducible character, \(|\chi_\nu(g)|\le\dim[\nu]\)
by the invariant positive Hermitian form. The certificate therefore
gives \(\Delta^\delta f_\nu(Z)>0\) for every nonzero active
order and every nonnegative \(Z\), by the exact inequality in
T054§4. The order-zero values are nonnegative because (ZW.7)
computes the actual module (ZW.3). All the Newton constants are
integers, since they are finite differences of integer multiplicities.
This proves positivity throughout both cones.

For clarity, every order-zero residue value has also been evaluated
independently of that positivity argument: each cone has
\(7\cdot60^3=1512000\) such constants. Every value is
nonnegative. The two receipts record all seven array hashes,
minima, maxima and the explicit signed-integer bounds used before
vectorized evaluation. These are finite integer checks with exact
rational class polynomials.

## 4. Positive polytopes and complete cone support

Let \(\nu=\mu\) or \(\mu'\) according as \(d+b+x\)
is even or odd. Write \(Z=r+60q\), \(0\le r_i<60\),
and let \(\mathcal D\) consist of zero and every active
order of the chosen cone. Define the fixed constants
\[
C_{\nu,r,\delta}=
\sum_{0\le h\le\delta}(-1)^{|\delta|-|h|}
\binom\delta h f_\nu(r+60h).
\]
All evaluation coordinates are bounded by359. The exact polynomial
Newton identity gives
\[
\boxed{p_{\mu,(n)}^\lambda=
\sum_{\delta\in\mathcal D}C_{\nu,r,\delta}
\prod_{i=1}^3\binom{q_i}{\delta_i}.}
\tag{ZW.8}
\]
For each positive constant, the bounded integer polytope is
\[
\begin{gathered}
60q_i=Z_i-r_i,\quad q_i\ge0,\quad0\le y<C_{\nu,r,\delta},\\
0\le z_{i,1}<\cdots<z_{i,\delta_i}<q_i\quad(1\le i\le3).
\end{gathered}
\tag{ZW.9}
\]
The selector and increasing subsets are an explicit bijection with
the associated summand. There are at most \(4+|\delta|\le9\)
variables and respectively47 or34 disjoint order tags. The literal
integer matrices and witness enumeration are the common constraint
map in T054/VW15, called on these exact constants by
`zero_twist_all_positive.py`.

Every first-order constant is strictly positive, so every zero
has all quotients zero. The complete effective-label exceptions are:

| Cone | Effective label | All zero parameter triples |
|---|---|---|
| A, coordinates(X,T,K) | \((5)\) | (0,0,0) |
| A | \((2,2,1)\) | (0,0,0) |
| A | \((1^5)\) | (0,0,0), (0,1,0), (0,2,0) |
| B, coordinates(X,S,K) | \((5)\) | (0,1,0), (0,3,0) |
| B | \((1^5)\) | (0,0,1), (0,1,0), (0,3,0), (0,5,0) |

All other parameters and labels in the two cones are positive.

## 5. Exhaustive wall routing and every complementary morphism

The following disjoint decisions cover (ZW.1). First use G021
for k=0, G026 for k=1, G030 for k=2 and G032/c=0 for k=3.
Now let k≥4.

For b≤2k+3, take H=λ₁ and the complementary partition
\(\lambda^c=(H-\lambda_5,H-\lambda_4,H-\lambda_3,
H-\lambda_2,0)\). The actual exterior-column pairing into
\((\det\mathbb Q^5)^H\) identifies the balanced weights,
and transposes the outer label exactly when H is odd. Its new
parameters are
\[
x'=2b+x-5k,\quad b'=0,\quad c'=b,\quad d'=0,
\qquad k'=\max(0,b-k).
\tag{ZW.10}
\]
When b<k, the extra first-row degree is k−b; multiplying by
\(u^{k-b}\) is the exact stable-chart isomorphism. Thus this
case uses k'=0 with twist c'=b. For k≤b≤2k, the twist is
\(c'\ge2k'\), so G021 applies. For b=2k+s, s=1,2,3,
the twist is \(c'=2k'-s\), covered respectively by T045,
T050 and T051. This proves the complementary branch with all
normalizations and outer-label signs retained.

It remains to treat b≥2k+4. For b≥3k−2 use T054. Otherwise
put \(t=3k-3-b\); then \(0\le t\le k-7\).
For x≥t, the inverse cone-A parameters are
\[
(X,T,K)=(x-t,t,k-t-6),
\]
all nonnegative. For x<t, the inverse cone-B parameters are
\[
(X,S,K)=(x,t-x-1,2b+x-5k),
\]
all nonnegative by the partition inequality. Direct substitution
in (ZW.2) recovers the original x,b,k in both cases. These
cases exhaust every remaining integer point. This proves the
complete-wall statement, with exact fixed positive formulas
on each branch.

For an arbitrary partition on the wall \(\lambda_2=\lambda_3\),
first set \(e=\max(0,n-\lambda_2)\),
\(n^0=n-e\), and
\(\lambda^0=(\lambda_1-5e,\lambda_2,\lambda_3,\lambda_4,\lambda_5)\).
The stable chart T032 identifies the original balanced module with
this one by multiplication by \(u^e\), with unchanged outer label.
The partition \(\lambda^0\) is valid: at positive e its first-row
gap is \(2\lambda_2-\lambda_4-\lambda_5\ge0\).
Its parameters \(d=\lambda_5,x=\lambda_4-\lambda_5,
b=\lambda_3-\lambda_4,k=\max(0,\lambda_2-n)\) are exactly (ZW.1).
This supplies the whole initial stable range as well.

The same result evaluates the entire second central wall
\(\lambda_3=\lambda_4\). Take \(H=\lambda_1\) and apply the
perfect complementary-column pairing above. The complementary
partition has \(\lambda^c_2=H-\lambda_4=H-\lambda_3=\lambda^c_3\),
so it is on the already completed wall. Its degree is \(H-n\),
and its outer label is transposed exactly when H is odd. Thus
both central equal-row walls have fixed positive formulas through
specified determinant and stable-chart morphisms.

The unified evaluator `zero_twist_all_positive.py` implements
these decisions, passes the complementary label and parameters
to the previously proved positive evaluators, and uses (ZW.8)
on the two new cones. It returns the original partition, exact
coefficient, selected branch and every requested polytope matrix.

## 6. Geometric transport and executed verification

The coefficient is the Schur-operation multiplicity of the actual
coherent section module in (ZW.3). Its signed restriction complex
has the literal quotient arrows; its triple trace uses the
Pieri projection to the complementary line followed by the
explicit finite reindexing (ZW.4). Thus the character and
polytope formula calculate the same exact representation class.
The coordinate, Proj and sheaf maps are EGA II2.4.1–2.4.2 and
2.5.2/2.5.4; the frame/comodule maps are SGA3 I4.5,4.7.2–4.7.3;
and the exact representation-to-sheaf class is SGA6 VI3.3.
Its λ-operation is SGA6 V4.2,4.4,4.8–4.9. The archive statement
is cote133/028, carried by A012's tensor-word, torus-weight and
Young maps. The complement in (ZW.10) is the actual determinant
pairing, and the low-order stable transport is multiplication
by the printed invariant section, so every routing step preserves
the stated geometric object through a specified morphism.

For each new cone, the class formula was compared with168 full
G027 restriction traces and84 actual balanced Schur coefficients,
including several orders above six. Every comparison passed.
Each cone's complete1,512,000-constant residue enumeration also
passed, with the exact zero lists above. The finite-difference
certificates check all46 and33 active orders and their complete
rational domination polynomials. Whole-proof readings and
independent reconstructions have their separate check events.

The unified evaluator passed1134 exact coefficient comparisons across all ten provider branches, including both determinant parities and70 direct zero-order balanced coefficients. It checked124 new-cone witness matrices and exercised every emitted-polytope provider. The receipt is `ZERO_WALL_ALL_ROUTES_CHECK.json`.
