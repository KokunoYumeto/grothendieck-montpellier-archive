# The complete first adjacent central walls

## G-034. A fixed positive formula for both central gaps equal to one

Let \(x,b,k,d\ge0\) and \(2b+x+3\ge5k\). Put
\[
\begin{aligned}
n&=d+b+x+1-k,\\
\lambda&=(d+3b+2x+4-5k,d+b+x+1,d+b+x,d+x,d).
\end{aligned}
\tag{OW.1}
\]
For every \(\mu\vdash5\), the coefficient
\(p_{\mu,(n)}^\lambda\) has a fixed positive lattice-point
formula. The disjoint routing in §5 covers every parameter in
(OW.1), including every ideal order. The same formula, through
the explicit stable and complementary-column maps below, evaluates
every partition with \(\lambda_2-\lambda_3=1\) or
\(\lambda_3-\lambda_4=1\). Partitions with more than five rows
have coefficient zero by the Schur antisymmetrizer on \(\mathbb Q^5\);
the formulas below use the five-row padding of every other partition.

The two new cones use respectively47 and34 disjoint polytopes,
each with at most nine integer variables. T055 covers the upper
chamber and T056 its adjacent strip. All remaining routes use
the already proved fixed positive formulas. Every coefficient
and inequality in a chosen formula is obtained from fixed data;
there is no representation calculation whose size depends on
the input. The new theorem is proved below, together with the
rank-three triple-intersection identity needed for its maps.

## 1. The actual section module and two lower cones

Put \(a=b+x\), \(E=\mathfrak h_5\), \(F=\mathbb Q^3\),
and \(J_k=\bigcap_i(\ell_i\otimes F)^k\). The normal-order
and balanced homogenization maps of G027/T049 give
\[
\begin{aligned}
M&=\operatorname{Hom}_{GL(F)}
 \bigl(S_{(a+1,b+1,1)}F,(J_k)_{a+b+3}\bigr),\\
(S_\lambda\mathbb Q^5)_{(n^5)}
 &\simeq\operatorname{sgn}^{d+a+1}\otimes M.
\end{aligned}
\tag{OW.2}
\]
The inverse map is \(u^{-k}F(v(X))\), whose extension is
the proved normal-order statement. This is the same module as
T055/OT3, retaining its determinant twist and literal quotient
arrows in the oriented restriction complex.

Define the following cones with every free coordinate nonnegative:
\[
\begin{array}{c|c|c|c|c}
&k&x&b&\tau=3k-5-b\\\hline
A&T+7+K&T+X&2T+16+3K&T\\
B&X+2S+9+K&X&2X+5S+21+3K&X+S+1.
\end{array}
\tag{OW.3}
\]
Their partition gaps \(2b+x+3-5k\) are respectively
\(X+K\) and \(K\). Both have \(b+1\ge2k\).
The ambient, singleton and pair terms are therefore exactly
T055/OT6–9: the singleton involution requires \(b\ge k-1\),
and the pair comparison requires \(b+1>2(k-1)\).
Denote their sum by \(P_g^\circ(a,b,k)\). Terms with at
least four selected points vanish: four independent truncated
blocks have degree at most \(4(k-1)<a+b+3\).
The remaining triple term is computed next.

## 2. A complete rank-three triple telescope

The following calculation holds for every \(c\ge0\),
\(a=b+x\), \(k\ge1\), and \(b+c\ge2k\). It is used
here at \(c=1\). Fix a stable selected triple, its cycle
type \(\eta\vdash3\), and the eigenvalue
\(\epsilon\in\{1,-1\}\) of its complementary standard
line. Let \(N=a+b+3c\), \(M_0=3(k-1)\), and
\(t=M_0-b\). Define
\[
\begin{aligned}
P_\eta(U,V,W)&=
 \prod_{\ell\in\eta}\ 
 \sum_{i+j+h<k}U^{\ell i}V^{\ell j}W^{\ell h},\\
A_{\eta,\epsilon}(r)&=[z^r]
 \prod_{\ell\in\eta}
 [(1-z^\ell)(1-\epsilon^\ell z^\ell)]^{-1},\\
h_\eta(c)&=[z^c]\frac{1-z}{\prod_{\ell\in\eta}(1-z^\ell)}.
\end{aligned}
\tag{OW.4}
\]
Coefficients with negative indices in these power series are zero. The normal
Schur coefficient of shape \(\rho=(p,q,r)\) is the coefficient
of \(U^pV^qW^r\) in
\[
P_\eta(U,V,W)(1-V/U)(1-W/U)(1-W/V).
\]
This is the three-row alternant identity. The actual complementary
Pieri projection contributes \(\epsilon^{N-|\rho|}\)
exactly for
\[
a+c\ge p\ge b+c\ge q\ge c\ge r\ge0.
\tag{OW.5}
\]
Its target is the weight \(N-|\rho|\) in the specified line.
These are the horizontal-strip inequalities for
\((a+c,b+c,c)/\rho\), with the normal Young projector
retained.

Set \(P_\epsilon=P_\eta(\epsilon U,\epsilon V,\epsilon W)\)
and \(F_\epsilon=P_\epsilon(1-V/U)(1-W/U)\).
Every normal weight has total degree at most \(M_0\). For
\(p\ge b+c\ge2k\), the total remaining degree is at most
\(k-3\). Thus the upper bound \(q\le b+c\) is automatic;
the other dominance conditions follow from \(q\ge c\ge r\)
and this same degree bound. The coefficient arrays of
\(F_\epsilon\) have the identical total-degree bound, even
though their exponent of \(U\) can be negative.

Write \(f_{p,q,r}=[U^pV^qW^r]F_\epsilon\). It is symmetric
in \(q,r\), and has nonnegative exponents of \(V,W\).
For fixed \(p\), the exact finite cancellation is
\[
\begin{aligned}
\sum_{q\ge c,\ 0\le r\le c}
 (f_{p,q,r}-f_{p,q+1,r-1})
 &=\sum_{q\ge c}f_{p,q,c}
   +\sum_{r=0}^{c-1}f_{p,c,r}\\
 &=\sum_{q\ge0}f_{p,q,c}.
\end{aligned}
\tag{OW.6}
\]
The last equality is precisely the symmetry of the two boundary
sums; negative indices contribute zero. Consequently the full
selected Schur sum equals
\[
\epsilon^N[W^c]
 \bigl([U^{b+c}]-[U^{a+c+1}]\bigr)
 P_\epsilon(U,1,W)(1-W/U).
\tag{OW.7}
\]
Here summation over \(p=b+c,\ldots,a+c\) cancels the factor
\(1-1/U\), leaving its two boundary columns. This proves
every sign by literal coefficient reindexing.

Reverse the exponent of \(U\) at \(M_0\), writing \(z=U^{-1}\).
For a cycle of length \(\ell\), put
\(i=k-1-j-h-s\). Its contribution is
\(\epsilon^{\ell(k-1)}U^{\ell(k-1)}\) times the sum of
\(z^{\ell j}(Wz)^{\ell h}(\epsilon z)^{\ell s}\)
over \(j,h,s\ge0\), \(j+h+s<k\). Every required
reversal deficit is at most \(M_0-b-c\le k-3<k\).
Within these coefficients the last truncation can be removed
and each factor is exactly a product of three geometric series.
Multiplication by \(1-Wz\) now gives
\[
[W^c]\frac{1-Wz}{\prod_{\ell\in\eta}(1-(Wz)^\ell)}
 =z^c h_\eta(c).
\]
The other two series give \(A_{\eta,\epsilon}\). Substitution
into (OW.7) proves the exact selected-triple trace
\[
\boxed{
\epsilon^{x+c+k-1}h_\eta(c)
 \left(A_{\eta,\epsilon}(t-2c)
       -A_{\eta,\epsilon}(t-x-2c-1)\right).}
\tag{OW.8}
\]
The phase is \(\epsilon^{N+M_0}\), which is the displayed
power because their exponents differ by an even integer.
This calculation also covers empty ranges: the two boundary
coefficients and their negative-index conventions give zero.

At \(c=1\), \(h_\eta(1)=m_1(\eta)-1\) and
\(t-2=\tau\). The signed restriction trace is therefore
\[
\begin{aligned}
P_g={}&P_g^\circ+
\sum_{\substack{|A|=3\\gA=A}}
 (-1)^{\#\operatorname{cyc}(g|A)}
 \epsilon_A^{x+k}(m_1(g|A)-1)\\
&\hspace{19mm}\cdot
 \left(A_{\eta_A,\epsilon_A}(\tau)
       -A_{\eta_A,\epsilon_A}(\tau-x-1)\right).
\end{aligned}
\tag{OW.9}
\]
The sign is the complex sign multiplied by the selected-triple
orientation. In cone A the second argument is \(-X-1\);
in cone B it is \(S\). Formula (OW.9) thus computes the
character of the actual module (OW.2).

## 3. Fixed rational certificates and positivity

The coefficients of (OW.4) are quasipolynomials of period
dividing the order of \(g\), with degree at most five.
Indeed their proper rational generating function has at most
six root-of-unity denominator factors; partial fractions give
the residue polynomial from index zero. Six values on each
residue class determine it exactly. This is fixed arithmetic.

The immutable input `ONE_TWIST_UPPER_INPUT.json` contains
T055's physical phase table in coordinates
\((X_o,B_o,K_o)=(x,b-3k+3,k-3)\). The exact substitutions are
\[
\begin{array}{c|ccc}
&X_o&B_o&K_o\\\hline
A&T+X&-T-2&T+4+K\\
B&X&-X-S-3&X+2S+6+K.
\end{array}
\tag{OW.10}
\]
Their validity follows from the actual singleton and pair maps
in §1, before polynomial substitution. Each phase is selected
using the original \((a,b,k)\), and then (OW.9) is added.
The scripts `one_twist_triple_a_check.py` and
`one_twist_triple_b_check.py` save all449 phase polynomials
per cone, their supports, and every complete rational domination
polynomial. In class order \(1^5,2111,221,311,32,41,5\),
the total degrees are \((5,2,1,1,0,0,0)\). Separate degree
bounds are \((3,3,4)\) on A and \((3,2,4)\) on B.

For each nonzero mixed step60 difference, the domination
polynomial subtracts from the identity difference the sum of
class sizes times the coefficientwise maximum absolute
nonidentity coefficients over all phases. The complete results
are:

| Cone | Nonzero active orders | Least constant margin | Largest total order |
|---|---:|---:|---:|
| A | 46 | 427680 | 5 |
| B | 33 | 29700 | 5 |

Every coefficient in every margin is nonnegative, and every
constant is positive. The identity polynomials have nonnegative
coefficients. The checked order sets contain the downward
closures of all monomial supports, so all omitted differences
are zero. `ONE_TWIST_TRIPLE_A_CHECK.json` and its B counterpart
contain the complete finite certificate, including every rational
coefficient and phase key; the preceding formulas reconstruct it.

The invariant Hermitian bound \(|\chi_\nu(g)|\le\dim[\nu]\)
now makes each nonzero multiplicity difference strictly positive
on the nonnegative orthant, by termwise comparison of the exact
class inner product. Order-zero values are multiplicities of
(OW.2), hence nonnegative; all differences are integers. The
separate residue check also evaluated all \(7\cdot60^3\)
base constants in each cone, proving signed-integer operation
bounds before evaluation. The maximum class-numerator bounds
are140893736676 and57770632800. Per-label hashes and all zeros
are saved in the two `ONE_TWIST_TRIPLE_*_RECEIPT.json` files.

## 4. The positive formula and its exact support

The effective label is \(\nu=\mu\) for even \(d+b+x+1\),
and \(\nu=\mu'\) for odd \(d+b+x+1\). Write the cone
coordinates \(Z=r+60q\), \(0\le r_i<60\), and let
\(\mathcal D\) consist of zero and its active orders. Define
the fixed nonnegative integers
\[
C_{\nu,r,\delta}=\sum_{0\le h\le\delta}
 (-1)^{|\delta|-|h|}\binom\delta h f_\nu(r+60h).
\]
All evaluation coordinates are bounded by359. Polynomial
Newton expansion gives
\[
\boxed{p_{\mu,(n)}^\lambda=
 \sum_{\delta\in\mathcal D}C_{\nu,r,\delta}
 \prod_{i=1}^3\binom{q_i}{\delta_i}.}
\tag{OW.11}
\]
For each positive constant, take the bounded integer polytope
\[
60q_i=Z_i-r_i,\quad q_i\ge0,\quad0\le y<C_{\nu,r,\delta},
\qquad0\le z_{i1}<\cdots<z_{i,\delta_i}<q_i.
\tag{OW.12}
\]
Replace each strict inequality by an integer gap of one. The
selector and increasing subsets give a literal bijection with
the summand in (OW.11). There are at most \(4+|\delta|\le9\)
variables, and47 or34 disjoint order tags. Their input bit size
is logarithmic in the parameters; all other data are fixed.

Every first-order difference is strictly positive. Thus a zero
must lie in the base residue cube. The complete base check shows
that cone A has only the two zeros at \((X,T,K)=(0,0,0)\),
with effective labels \((5)\) and \((1^5)\). Cone B has
no zero for any label or parameter. These facts give the full
support of the new cones.

## 5. Exhaustive routing, stable range and the second wall

Use G021 at \(k=0\), T045 at \(k=1,c=1\), T051 at
\(k=2,c=1\), and G032 at \(k=3,c=1\). Let \(k\ge4\).
For \(b\le2k+1\), take \(H=\lambda_1\) and the
complement \(\lambda^c=(H-\lambda_5,H-\lambda_4,
H-\lambda_3,H-\lambda_2,0)\). The perfect exterior-column
pairing into \((\det\mathbb Q^5)^H\) gives degree \(H-n\)
and transposes \(\mu\) exactly when \(H\) is odd. The
new parameters, after stable first-row removal, are
\[
x'=2b+x+3-5k,\quad b'=1,\quad c'=b,\quad d'=0,
\qquad k'=\max(0,b+1-k).
\tag{OW.13}
\]
At \(b+1<k\), the removed stable power is \(k-b-1\);
its actual inverse is multiplication by \(u^{k-b-1}\).
For \(b\le2k-2\), \(c'\ge2k'\) and G021 applies.
For \(b=2k-2+s\), \(s=1,2,3\), one has
\(c'=2k'-s\), treated respectively by T045, T050 and T051.

It remains that \(b\ge2k+2\). Use T055 at \(b\ge3k-3\),
and T056 at \(b=3k-4\). In the latter branch the two
inequalities imply \(k\ge6\), within T056's proved range.
Otherwise \(\tau=3k-5-b\ge0\). The two inverse parameter
maps are
\[
\begin{array}{c|c}
x\ge\tau&(X,T,K)=(x-\tau,\tau,k-\tau-7),\\
x<\tau&(X,S,K)=(x,\tau-x-1,2b+x+3-5k).
\end{array}
\tag{OW.14}
\]
Every coordinate is nonnegative: in the first row
\(K=b-2k-2\), and in the second it is the partition gap.
Substitution into (OW.3) recovers the original parameters.
This exhausts every integer point of (OW.1).

For an original partition with \(\lambda_2=\lambda_3+1\)
and degree \(5n\), put \(e=\max(0,n-\lambda_2)\),
\(n^0=n-e\), and
\(\lambda^0=(\lambda_1-5e,\lambda_2,\lambda_3,
\lambda_4,\lambda_5)\). At positive \(e\), its first gap is
\(3\lambda_2-\lambda_3-\lambda_4-\lambda_5\ge0\).
T032's actual stable-chart isomorphism is multiplication by
\(u^e\), with unchanged outer label. The normalized partition
has the parameters in (OW.1). For
\(\lambda_3=\lambda_4+1\), the perfect complementary-column
map above makes \(\lambda^c_2-\lambda^c_3=1\); apply the
first-wall formula with its specified determinant parity. This
proves the whole statement for both adjacent walls.

`one_twist_all_positive.py` implements these exact routes,
including a direct partition entry and all literal inequality
matrices. Its special degree-one coin tags are passed to the
already proved T045 weighted-sum polytopes; all Newton tags use
the corresponding fixed increasing-subset constraint map.

## 6. Geometric dictionary and executed checks

The actual Schur section module is (OW.2), with G027/T049's
normal substitution, balanced homogenization, Young projector
and oriented quotient arrows. The triple's horizontal-strip
projection is an actual Pieri map into the complementary line;
(OW.6)–(OW.8) compute its exact character by finite reindexing.
Thus the positive polytopes count this same representation
class. The coordinate and sheaf constructions are EGA II2.4.1–
2.4.2 and2.5.2/2.5.4, the frame/comodule transport is
SGA3 I4.5/4.7.2–4.7.3, and its representation-to-sheaf K0
morphism is SGA6 VI3.3. Its Schur/λ operation uses SGA6
V4.2,4.4,4.8–4.9. Cote133/028 is carried to these exact
tensor-word, torus-weight and Young maps by A012. The two
wall transports retain the explicit determinant pairings and
invariant-section multiplication, including their signs.

The general triple identity was checked against13230 complete
normal-Schur/horizontal-strip sums with varied \(k,c,x,t,\eta\)
and both complementary eigenvalues. Each new cone also passed
168 full G027 restriction traces,84 actual balanced Schur
coefficients, and1512000 residue constants. These computations
supplement the exact proof and certificates above. Complete
proof readings, independent reconstructions, and unified
evaluator checks have their own separately dated events.

The unified evaluator passed1120 exact coefficient comparisons across all nine provider routes, including42 direct zero-order balanced coefficients and both determinant parities. It verified140 new-cone witness matrices and exercised every polytope provider. The initial exporter omitted the degree-one coin-tag variant; the final exporter preserves that variant and all rerun checks pass. The receipt is `ONE_WALL_ALL_ROUTES_CHECK.json`.

The direct partition entry passed672 actual Schur coefficients at96 original partitions, covering both adjacent walls, determinant shifts and stable first-row powers zero and three. Every partition also exported its selected polytope provider. The receipt is `ONE_WALL_PARTITION_ENTRY_CHECK.json`.
