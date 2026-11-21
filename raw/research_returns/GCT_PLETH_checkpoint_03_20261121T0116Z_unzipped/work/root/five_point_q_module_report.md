# A positive five-point quotient-bundle family in every multiplicity

## G-017. A fixed positive formula on a varying five-row family

For integers \(k,d\ge0\), put
\[
n=d+k+1,\qquad
\lambda=(d+3k+2,d+2k+1,d+1,d+1,d).
\tag{Q.1}
\]
The parts sum to \(5n\) and are weakly decreasing. Let \(\mu\vdash5\),
and put \(\nu=\mu\) for odd \(d\) and \(\nu=\mu'\) for even \(d\).
For an integer \(R\), define the bounded polytope
\[
\mathscr P(R)=\{x\in\mathbf R_{\ge0}^4:
2x_1+4x_2+6x_3+10x_4=R\},\qquad
N(R)=\#(\mathscr P(R)\cap\mathbf Z^4).
\tag{Q.2}
\]
It is empty for \(R<0\). The following formula is positive, with fixed
nonnegative integers \(h_{\nu,j}\) displayed in §6:
\[
\boxed{p_{\mu,(n)}^\lambda
=\sum_{j=0}^{19}h_{\nu,j}N(k-j).}
\tag{Q.3}
\]
Equivalently, use \(h_{\nu,j}\) distinct tags for the polytope
\(\mathscr P(k-j)\). There are at most 216 tagged polytopes, and exactly
36 tags for the symmetric or alternating outer partition. Their dimension,
coefficients, and number are independent of both parameters. The evaluator
in §7 uses a fixed number of integer arithmetic operations.

The proof constructs the relevant geometric section module, its explicit
matrix presentation, and an equivariant free multiplication map over four
invariant parameters. The finite character calculation only determines the
graded types of the actual quotient module at the end of this construction.

## 1. The exact flag comparison and its determinant twist

Let \(E=\mathfrak h_5\), with the invariant pairing and projective-frame
vectors \(\ell_i=e_i-\frac15\mathbf1\) fixed in G-015. On \(\mathbf P(E)\)
let \(Q\) be the tautological rank-three quotient, and let \(\mathcal I\)
be the ideal sheaf of the five points \([\ell_i]\). Define
\[
M_k=H^0\bigl(\mathbf P(E),\mathcal I^k(2k)\otimes Q\bigr),
\qquad M=\bigoplus_{k\ge0}M_k.
\tag{Q.4}
\]
G-015 gives the actual balanced-chart map for (Q.1), since
\(\lambda_2-n=k\). After removing the full determinant factor
\((\det E^*)^d\), the relative quotient-flag weight is \((1,1,0)\)
and the first-line weight is \(2k+1\). The relative Plücker evaluation,
the exterior pairing \(\Lambda^2 Q^*\simeq Q\otimes\det Q^*\), and
\(\det Q^*\simeq\det E^*\otimes\mathcal O(-1)\) therefore identify the
pushforward with
\[
(\det E^*)^{d+1}\otimes\mathcal O(2k)\otimes Q.
\]
These maps are exactly those in (5F.6)–(5F.9) for relative weight
\((1,1,0)\); their local quotient-frame definitions glue and commute
with tensoring the base ideal, as proved in T-039 §1. Consequently
\[
\boxed{(S_\lambda\mathbf Q^5)_{(n^5)}
\simeq\operatorname{sgn}^{d+1}\otimes M_k.}
\tag{Q.5}
\]
The inverse chart sends a flag polynomial \(f\) to \(u^{-k}f(v(X))\).
Its extension to a polynomial is equivalent to the ideal membership in
(Q.4) by the transverse-order proof G-015. Thus (Q.5) includes the map,
the sheaf condition, and its group linearization.

## 2. An invariant section and five exact relations

Use \(\ell_1,\ldots,\ell_4\) as a basis, and write its coordinates as
\(z_1,\ldots,z_4\). The fifth point has coordinates \([1:1:1:1]\).
Write
\[
\begin{aligned}
f_A&=z_1z_3-z_1z_2,& f_B&=z_1z_4-z_1z_2,\\
f_C&=z_2z_3-z_1z_2,& f_D&=z_2z_4-z_1z_2,&
f_E&=z_3z_4-z_1z_2.
\end{aligned}
\tag{Q.6}
\]
Let \(U=\langle f_A,f_B,f_C,f_D,f_E\rangle=[3,2]\), and set
\[
S=\mathbf Q[A,B,C,D,E],\quad
F=AD(E-B-C)-BC(E-A-D),\quad C=S/(F).
\tag{Q.7}
\]
Each variable in \(S\) has degree one. By T-038, substitution
\(A\mapsto f_A,\ldots,E\mapsto f_E\) has kernel exactly \((F)\),
and \(F\) has sign character. Hence \(C\) acts on (Q.4) by multiplication.

The class of \((z_1^2,z_2^2,z_3^2,z_4^2)\) modulo the tautological line
defines
\[
\theta\in M_1.
\tag{Q.8}
\]
At every coordinate point and at \((1,1,1,1)\) this vector is proportional
to the point vector, so it vanishes in the quotient fiber. To verify its
linearization, write \(q=\sum z_i\ell_i\) and \(s=\sum z_i\). The
\(S_5\)-equivariant quadratic map
\(q\mapsto(q_i^2-\frac15\sum_jq_j^2)_i\) has coordinates
\(z_i^2-\frac25sz_i\) in this basis. Its quotient class is (Q.8).
Therefore \(\theta\) is invariant under the actual \(S_5\) action.

Here is a small polynomial matrix that specifies all the relations. Put
\[
K=\begin{pmatrix}
0&E-B&0&-C&-BC+BD+CD-DE\\
0&A-E&D&0&-AC+AD-CD+CE\\
D-E&0&0&A&-AB+AD-BD+BE\\
E-C&0&-B&0&AB+AC-AE-BC\\
C-D&B-A&0&0&-AD+BC
\end{pmatrix},\qquad
P=\frac{\operatorname{adj}K}{F}.
\tag{Q.9}
\]
All entries of \(\operatorname{adj}K\) are divisible by \(F\).
The first four rows of \(P\), denoted by \(\Phi\), have degree two;
its last row is \((-A,-B,-C,-D,-E)\). Expansion of the determinants gives
\[
\det K=3F^2,\qquad PK=KP=3F I_5,\qquad\det P=81F^3.
\tag{Q.10}
\]
These are identities in the polynomial ring \(S\). They are also
reproduced by exact symbolic arithmetic in `five_point_q_module.py` and
`FIVE_POINT_Q_RELATIONS.json`; (Q.9) specifies the matrix independently
of those files.

For complete verification of the substitution relations, put
\[
\begin{aligned}
h_A&=f_A(z_1+z_2+z_3-2z_4),&
h_C&=f_C(z_1+z_2+z_3-2z_4),\\
h_B&=f_B(z_1+z_2+z_4-2z_3),&
h_D&=f_D(z_1+z_2+z_4-2z_3),\\
h_E&=z_3z_4(z_3+z_4-2z_1-2z_2)
      -z_1z_2(z_1+z_2-2z_3-2z_4).
\end{aligned}
\tag{Q.11}
\]
The twenty polynomial identities, for \(1\le i\le4\) and
\(j\in\{A,B,C,D,E\}\), are
\[
f_jz_i^2-\Phi_{ij}(f_A,f_B,f_C,f_D,f_E)=z_i h_j.
\tag{Q.12}
\]
They follow by substituting (Q.6) into the minors in (Q.9) and expanding;
the right sides (Q.11) give their explicit line corrections. Thus the
columns of \(P\) are actual relations on the constant sections \(E\)
and the section \(\theta\), not just relations on their dimensions.

The relation space carries the representation \(U\). Indeed the map
\(E\otimes\operatorname{Sym}^2U\to M_2\) is injective. A kernel
would be a vector polynomial in the tautological line, hence a multiple
\(z h\) with \(h\in H^0(\mathcal I^2(3))\). A cubic double at all four
coordinate points is a linear combination of the four squarefree cubics.
At \((1,1,1,1)\), let their coefficients be \(c_i\), indexed by the
missing variable. Its four first derivatives are \(\sum_jc_j-c_i\).
Their simultaneous vanishing implies \(c_i=\sum_jc_j\) for every
\(i\), whence \(3\sum_jc_j=0\) and every coefficient is zero. Also
\(\operatorname{Sym}^2U\to C_2\) is injective because the first relation
\(F\) has degree three. This proves the asserted injectivity. It makes
the coefficient \(\Phi(f)\) in \(f\theta=\Phi(f)\) unique. Applying
an element of \(S_5\) to that equality shows that its five-dimensional
relation space is the image of the equivariant map from \(U\).

Define the graded module
\[
\mathcal M=\operatorname{coker}\left[
S(-2)\otimes U\xrightarrow{P}
(S\otimes E)\oplus S(-1)\right].
\tag{Q.13}
\]
The determinant (Q.10) makes the displayed map injective. Equations
(Q.12) define an equivariant graded map \(\mathcal M\to M\), and
\(PK=3FI\) shows that \(F\mathcal M=0\).

## 3. The presentation injects into the section module

We first verify that \(\mathcal M\) has no torsion over the integral
domain \(C\). Let \(g\in S\) have nonzero image in \(C\), and suppose
\(gv=Pw\) for polynomial column vectors. Multiplication by
\(\operatorname{adj}P\) gives
\[
g\operatorname{adj}P\,v=81F^3w.
\]
The irreducible polynomial \(F\) does not divide \(g\). Unique
factorization implies that every entry of \(\operatorname{adj}P\,v\)
is divisible by \(F^3\). Therefore
\(u=\operatorname{adj}P\,v/(81F^3)\) is a polynomial vector and
\(Pu=v\). The class of \(v\) in the cokernel is zero, which proves
torsion-freeness.

Its rank over \(C\) is three. Here is an elementary local calculation
of that rank. Localize \(S\) at the prime \((F)\), a discrete valuation
ring with uniformizer \(F\). Successive row and column operations clear
an entry of minimum valuation and then its row and column, giving the
diagonal elementary-divisor form of \(P\). The identity \(PK=3FI\)
implies that each diagonal exponent is at most one, and \(\det P=81F^3\)
implies that their sum is three. Thus exactly three diagonal entries
have exponent one. Reducing modulo \(F\) gives rank two for \(P\),
and dimension three for its cokernel over \(\operatorname{Frac}C\).
For an additional finite check, all 100 three-by-three minors of \(P\)
are divisible by \(F\), and its upper left two-by-two minor is
\(-3AB(AD-BC)\), which is not divisible by \(F\).

Embed \(C\) into \(\mathbf Q[z_1,z_2,z_3,z_4]\) by (Q.6), and pass
to the latter fraction field \(L\). Section evaluation embeds \(M\)
degreewise in the generic quotient \(L^4/Lz\), which has dimension
three. The four constant generators in (Q.13) span this quotient.
Consequently \(\mathcal M\otimes_C L\to L^4/Lz\) is a surjection
between three-dimensional spaces and is an isomorphism. The kernel of
\(\mathcal M\to M\) is therefore \(C\)-torsion and, by the preceding
paragraph, is zero. This proves the actual injection
\[
\mathcal M\hookrightarrow M.
\tag{Q.14}
\]

## 4. The cohomological dimension proves surjectivity in every degree

The precise regularity result needed here is proved in A-029: for the
ideal (Q.6), every \(I^k\), \(k\ge2\), has a \(2k\)-linear free
resolution. A-029 verifies its height-three Gorenstein presentation,
every local generator condition, and the exceptional degree in the
known symmetric-power complexes. Its cited inputs are Kustin–Polini–Ulrich,
*The equations defining blowup algebras of height three Gorenstein
ideals*, Algebra & Number Theory 11 (2017), formula (6.1.4), p. 1509,
Lemma 6.3 and Corollary 6.4, p. 1510, with the proof on p. 1511. The
ordinary-power resolution follows there by the actual torsion sequence,
whose kernel is the degree-zero module
\(\operatorname{sgn}\otimes\operatorname{Sym}^{k-3}U\).

In particular the saturation agrees with the ordinary power in degree
\(2k\), and \(H^1(\mathcal I^k(2k-1))=0\) for \(k\ge2\). Thus
\[
\begin{aligned}
h^0(\mathcal I^k(2k))
 &=\dim C_k=\binom{k+4}{4}-\binom{k+1}{4},\\
h^0(\mathcal I^k(2k-1))
 &=\binom{2k+2}{3}-5\binom{k+2}{3}
 =\frac{k(k+1)(k-2)}2 \quad(k\ge2).
\end{aligned}
\tag{Q.15}
\]
The second equality uses the length of five order-\(k\) fat points,
which is \(5\binom{k+2}{3}\). Tensoring the tautological sequence
with \(\mathcal I^k(2k)\) and taking global sections now gives
\[
\dim M_k=4\dim C_k-\frac{k(k+1)(k-2)}2
=\frac{(k+1)(k+2)(3k+4)}2\quad(k\ge2).
\tag{Q.16}
\]
At \(k=1\), the degree-one evaluation \(E\to\operatorname{Perm}_5\)
has a one-dimensional trivial cokernel, and
\(H^0(\mathcal I(1))=0\). The same cohomology sequence gives
\(\dim M_1=4\cdot5+1=21\). At \(k=0\), \(M_0=E\) has dimension four.
These values agree with (Q.16).

The injective free presentation (Q.13) has Hilbert series
\[
\operatorname{Hilb}_{\mathcal M}(t)
=\frac{4+t-5t^2}{(1-t)^5}
=\frac{4+5t}{(1-t)^4}
=\sum_{k\ge0}\frac{(k+1)(k+2)(3k+4)}2t^k.
\tag{Q.17}
\]
Equality of every graded dimension in (Q.14) proves
\(\mathcal M\simeq M\). This establishes generation and the entire
relation module; neither was inferred solely from a low-degree test.

## 5. Four invariant parameters and the actual free multiplication map

Use the six linear forms of T-038:
\[
\begin{array}{lll}
t_1=A+B-C+D-E,&t_2=-A+B+C-D-E,&t_3=-A+B+C-D+E,\\
t_4=-A-B-C+D+E,&t_5=A-B-C-D+E,&t_6=A-B+C+D-E.
\end{array}
\tag{Q.18}
\]
They satisfy \(\sum t_i=0\) and \(\sum t_i^3=-24F\), so their third
elementary symmetric polynomial is \(e_3=-8F\). The verified action
is sign times the permutation action on the six Sylow-five subgroups.
For a homogeneous elementary symmetric polynomial \(e_j\), the sign
twist consequently multiplies it by \(\operatorname{sgn}^j\). Hence
\[
B=\mathbf Q[e_2,e_4,e_6,e_5^2]
\tag{Q.19}
\]
consists of invariant elements, of degrees \(2,4,6,10\).

We record an algebraic freeness proof sufficient for the regularity
assertion about this module. For six independent variables, start with
the universal monic polynomial having coefficients \(e_1,\ldots,e_6\).
Adjoin its first ordered root, divide the polynomial by that root
factor, and successively adjoin a root of the remaining monic polynomial
of degrees five through one. At each step the quotient by a monic
polynomial is free over the preceding coefficient ring, with the powers
below that degree as a basis. The resulting ring is
\(\mathbf Q[t_1,\ldots,t_6]\): its defining equations identify the
coefficients with the elementary symmetric polynomials and allow those
coefficients to be eliminated. This proves freeness of rank \(6!\)
over \(\mathbf Q[e_1,\ldots,e_6]\), including algebraic independence.

Quotient by \(e_1\). The linear forms in (Q.18) have rank five, so
\(S\simeq\mathbf Q[t_1,\ldots,t_6]/(e_1)\). Replace the polynomial
variable \(e_5\) by \(e_5^2\), retaining the free basis \(1,e_5\).
Finally substitute \(e_3=-8F\). It follows that \(S\) is free of
rank 1440 over the polynomial ring \(B[F]\). In particular, after
quotienting by any initial segment of the four parameters in (Q.19),
both the next parameter and \(F\) are nonzerodivisors in the resulting
free coefficient module.

The four parameters are a regular sequence on \(M\). To prove this
directly, work modulo any preceding parameters and denote the next by
\(p\). The matrix \(P\) remains injective even after quotient by \(p\),
because its determinant is \(81F^3\), a nonzerodivisor there; multiplying
by its adjugate proves injectivity. In a relation \(pv=Pw\), reduce
modulo \(p\) to conclude \(w=pw'\). Since \(p\) is a nonzerodivisor
on the ambient free modules, it follows that \(v=Pw'\). This proves
that multiplication by \(p\) has zero kernel on the cokernel. The
argument applies in turn to all four parameters.

Set \(H=M/B_+M\). It is finite-dimensional: \(M\) is finite over
\(C=S/(F)\), which is finite over \(B\). The regular sequence gives
\[
\operatorname{Hilb}_H(t)
=(4+5t)\prod_{r\in\{2,4,6,10\}}(1+t+\cdots+t^{r-1}).
\tag{Q.20}
\]
It has degree 19 and total dimension 4320. Choose any graded linear
section \(H\to M\) and average it over \(S_5\). Multiplication defines
an equivariant map
\[
B\otimes H\longrightarrow M.
\tag{Q.21}
\]
It is surjective by induction on degree, because the section lifts the
quotient modulo \(B_+M\). The regular-sequence Hilbert identity makes
source and target dimensions equal in every degree. Thus (Q.21) is an
actual isomorphism. All four variables in \(B\) have trivial action.

## 6. The fixed positive tag table

Here is the complete table \(h_{\rho,j}=[H_j:[\rho]]\). Each row is
listed in increasing degree \(j=0,\ldots,19\):

| \(\rho\) | \((h_{\rho,0},\ldots,h_{\rho,19})\) | total |
|---|---|---:|
| \((5)\) | \(0,1,1,1,2,2,3,3,3,4,3,3,3,2,2,1,1,1,0,0\) | 36 |
| \((4,1)\) | \(1,1,2,5,6,9,11,12,14,14,14,13,12,10,8,6,3,2,1,0\) | 144 |
| \((3,2)\) | \(0,1,3,5,8,11,13,16,17,17,18,17,15,13,10,7,5,2,1,1\) | 180 |
| \((3,1,1)\) | \(0,1,3,5,9,12,16,19,20,22,21,21,19,16,13,9,6,3,1,0\) | 216 |
| \((2,2,1)\) | \(0,1,2,4,7,10,13,15,17,18,18,17,16,14,11,8,5,3,1,0\) | 180 |
| \((2,1,1,1)\) | \(0,0,1,3,5,8,10,12,14,14,15,14,13,12,9,7,4,2,1,0\) | 144 |
| \((1^5)\) | \(0,0,0,1,1,1,3,3,3,4,3,4,4,2,3,2,1,1,0,0\) | 36 |

For reproducibility, the seven rational characters of \(M\) calculated
from (Q.13), in the indicated class order, are
\[
\begin{array}{c|c|r}
\text{cycle type}&\sum_k\operatorname{tr}(g\mid M_k)t^k&\text{class size}\\\hline
1^5&(4+5t)/(1-t)^4&1\\
2\,1^3&(2-t)/((1-t)^3(1+t))&10\\
2^2\,1&t/(1-t^2)^2&15\\
3\,1^2&1/(1-t^3)&20\\
3\,2&-1/(1-t^3)&20\\
4\,1&t/(1-t^4)&30\\
5&-(1-t)/(1-t^5)&24.
\end{array}
\tag{Q.22}
\]
Indeed the character before cancellation is
\[
\frac{\chi_E(g)+t-\chi_U(g)t^2}{\det(1-tg\mid U)},
\quad \chi_E(g)=m_1-1,\quad
\chi_U(g)=\binom{m_1}{2}+m_2-m_1,
\tag{Q.23}
\]
where \(m_i\) counts \(i\)-cycles. The latter character follows from
the permutation action on two-element subsets minus the five-point
permutation module, as identified in T-038. Newton's identities applied
to \(\chi_U(g^r)\), \(1\le r\le5\), give every denominator in
(Q.22). Multiplying by
\(D(t)=(1-t^2)(1-t^4)(1-t^6)(1-t^{10})\) gives the polynomial
character of the actual module \(H\), by (Q.21). Inner products with
the fixed seven irreducible characters give the displayed table.
The exact scripts `five_point_q_tags.py` and
`check_q_module_characters.py` perform this finite calculation by
independent expressions, and compare all 140 entries. No table entry
depends on \(k\) or \(d\).

At \(t=1\), the six nonidentity polynomial characters vanish and
the identity value is 4320. Thus, as an ungraded module, \(H\) has
character \(36\) times the regular character of \(S_5\). This checks
all row totals: \(\sum_jh_{\rho,j}=36\dim[\rho]\). Taking the
\([\nu]\)-summand of (Q.21) and using (Q.5) proves (Q.3).

## 7. Exact support and a fixed-arithmetic evaluator

All parameter weights in (Q.2) are even, and one is two. The first two
consecutive nonzero entries in each row of the table therefore determine
the complete support:
\[
\begin{array}{c|c}
\nu& p_{\mu,(n)}^\lambda>0\\\hline
(4,1)&k\ge0\\
(5),(3,2),(3,1,1),(2,2,1)&k\ge1\\
(2,1,1,1)&k\ge2\\
(1^5)&k\ge3.
\end{array}
\tag{Q.24}
\]
Before the indicated first degree every tag vanishes. At and above it,
choose a tag of the correct parity among those first two degrees and
use the weight-two variable to fill the remainder. This proves both
directions. In particular, for symmetric outer degree five, positivity
holds exactly for odd \(d\) with \(k\ge1\), or even \(d\) with
\(k\ge3\).

For completeness the count in (Q.2) needs no loop of length depending
on the input. It is zero for odd \(R\). For \(R=2N\ge0\), its weights
are \(1,2,3,5\). Write each variable uniquely as
\[
x_w=(30/w)q_w+r_w,\qquad0\le r_w<30/w.
\]
Define the fixed positive polynomial
\[
G(t)=\prod_{w\in\{1,2,3,5\}}
\left(\sum_{r=0}^{30/w-1}t^{wr}\right)
=\sum_{j=0}^{109}g_jt^j.
\tag{Q.25}
\]
Its coefficients count exactly the residue tuples. For a tuple of
residue weight \(j\), the four nonnegative \(q_w\) sum to
\((N-j)/30\), so stars and bars gives the positive identity
\[
N(2N)=
\sum_{\substack{0\le j\le\min(N,109)\\j\equiv N\pmod{30}}}
g_j\binom{(N-j)/30+3}{3}.
\tag{Q.26}
\]
There are at most four terms. The notation on the left is the counting
function of (Q.2); the integer \(N\) on the right is half its argument.
The factor degrees in (Q.25) are \(29,28,27,25\), whose sum is 109.
Thus (Q.3) uses a fixed table, at most 80 cubic-binomial evaluations,
and integer inputs of bit length \(O(\log(k+2)+\log(d+2))\). Ordinary
integer arithmetic gives a polynomial bit-cost bound; with schoolbook
multiplication the count itself costs \(O(\log^2(k+2))\).

## 8. Algebraic-geometric and lambda-ring dictionary

The object counted by (Q.3) is the \([\mu]\)-covariant summand of the
section space of the explicit ideal-twisted flag line bundle in G-015.
The morphism (Q.5) carries that section space to the balanced weight of
the Schur functor, and the normalizer projector T-003 carries it to the
plethysm coefficient. In the representation category its class is
\([S_\mu(\operatorname{Sym}^n)]\), with composition interpreted in
the lambda-ring of polynomial representations. The equality is lifted
here to actual modules and maps by (Q.5), (Q.13), and (Q.21).

The geometric construction is defined over \(\mathbf Q\); the frame,
quadrics, cubic, and polynomial matrices are defined over
\(\mathbf Z[1/30]\) after the stated invariant-form identifications.
The averaging section additionally uses \(1/120\), already in that
ring. The characteristic-zero cohomology and representation conclusions
have been proved over \(\mathbf Q\) and by extension over
characteristic-zero fields; no assertion of all-fiber exactness in
positive characteristic is inferred from the rational proof. The exact
base-extension morphism is tensoring the displayed complexes and maps.

The ideal powers are those of a specified closed subscheme of projective
space, and all bundles are Schur functors of tautological locally free
sheaves. The determinant pairings and exact-sequence classes are the
operations in the SGA 6 dictionary, and the concrete ideal and its
graded quotients define the associated Hilbert functors in the FGA
dictionary. The exact archive/SGA/FGA locators and coefficient-category
maps are recorded in the separate geometric dictionary; this result
uses those same maps, with the additional explicit matrices (Q.9).
No new weight, purity, or motivic comparison is required by this proof.
