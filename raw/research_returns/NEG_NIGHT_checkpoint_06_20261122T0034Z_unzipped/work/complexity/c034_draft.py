"""NN-C034: integral cyclotomic interpolation and universal ring transfer."""

def append_c034(add,E,ALGTRACE):
    bertrand={'source':'Erdos, Beweis eines Satzes von Tschebyschef, Acta Litt. Sci. Szeged5(1932),194--198',
              'locator':'Section5, printed pp197--198: for every integer n>1 a prime lies strictly between n and2n; Q=1 handled directly',
              'url':'https://www.renyi.hu/~p_erdos/1932-01.pdf'}
    inputs=[{'source':'NN-C033','locator':'integral swap-matrix generating identity and the complete integer-measurement-fiber Taylor routine over a coefficient ring'},
            {'source':'NN-C016 and NN-C029','locator':'universal bounded-arity partition polynomial; ordinary integral ideal multipliers, sparse-CNF identity and affine coordinate maps'},
        {'source':'NN-C021','locator':'fixed-density mod-three Tseitin 3-CNF family with exponential monomial-PC lower bounds over F2; full repaired source reduction and size-degree deduction'},
            dict(E,locator='Section3.1 independent-incidence total degree; complete Lemmas3.2--3.3, Proposition3.4 and Lemmas4.1--4.8; same discrete layouts, exact parameter checks and three exponential costs'),
            {'source':'Servedio--Wan, Computing sparse permanents faster, author manuscript18 June2005',
             'locator':'Section2, printed p3, first display: Rysers inclusion-exclusion identity; original definition p1',
             'url':'https://www.cs.columbia.edu/~atw12/papers/perm.pdf'},
            bertrand,ALGTRACE,
            {'source':'Integral interpolation construction below','locator':'Explicit two-prime cyclotomic quotient, integral unit inverses, Hasse cardinal polynomials and coefficient-size proof; proposed by root and developed here'}]
    add('NN-C034','NEG_NIGHT-04;NEG_NIGHT-06;NEG_NIGHT-10e',
        'Cyclotomic interpolation gives integral constant-free symbolic circuits over every ring',
r'''Fix factor arity $w$ and density $C$. The full integral universal partition polynomial
\[
 Z_H(y)=\sum_{x\in\{0,1\}^n}\prod_f y_{f,x|I_f}
                              \in\mathbb Z[y]
\]
of every $n$-variable, $m\leq Cn$-factor instance has a deterministically constructible division-free arithmetic circuit with integer constants, of size and bit construction time
\[
 S(n)=\operatorname{poly}(n)\,
       2^{O_{w,C}(n(\log\log n)^2/\sqrt{\log n})}.
\]
All integer constants have polynomial bit length. The circuit can be made constant-free, with only $0,1,-1$ as constant leaves, at polynomial overhead and with polynomial syntactic formal degree. For the universal polynomial one may take formal degree at most $\max(m,1)$ when subtraction gates are allowed and have the same degree rule as addition.

More generally, let $m\leq Cn$ factors be explicit monomial lists $\Phi_f=\sum_j y_{f,j}x^{\alpha(f,j)}$ of full bit length $L$, with independent coefficient blocks, declared scope at most $(\lceil\log_2n\rceil)^a$ and total input-degree budget $\sum_f\max_j|\alpha(f,j)|\leq Cn$, for fixed $C,a$. Their symbolic sum-product has size and bit construction time $\operatorname{poly}(n,L)2^{O_{C,a}(n(\log\log n)^2/\sqrt{\log n})}$, with the same integral and constant-free conclusions and formal weight degree at most $\max(m,1)$. This includes fixed-degree polylogarithmically sparse factors and preserves the original $n$ Boolean variables.

As a concrete application, the symbolic permanent of an $r\times r$ matrix with at most $Cr(\lceil\log_2r\rceil)^a$ allowed entries in total, for fixed $C,a$, has such an integral constant-free circuit in the original matrix-order parameter $r$, of formal degree at most $2r$. No individual row- or column-degree restriction is needed.

This is an identity over $\mathbb Z$, so the very same circuit computes the universal partition polynomial after base change to \emph{every} commutative ring with identity. No characteristic choice, finite-field construction, modulus factorization or rational denominator remains in that circuit.

Consequently the ordinary integral Nullstellensatz multipliers of NN-C029, and its mutually inverse integral affine-space coordinate maps in the empty case, have deterministically constructible integral-gate and constant-free circuits at the same subexponential parameter bound, with polynomial formal degree. For local verifiers the parameter is $v=n+s$ including wires; for fixed-width linear-clause CNFs the stronger original-$n$ certificate still omits Boolean axioms. These are ordinary polynomial identities over $\mathbb Z$, not only separate certificates over each finite field.

On the fixed-density 3-CNF family of NN-C021, this yields an exponential ratio between ordinary monomial-PC proof size and circuit-IPS proof size over the same field $\mathbb F_2$: the former is $2^{\Omega(n)}$, while the latter is at most $S(n)=2^{o(n)}$, with $n$ the original CNF variable count. The circuit certificates retain actual degree at most $n+1$ and polynomial formal degree.''',
        inputs,
r'''The argument uses the integral matrix and exact integer measurement fibers proved in NN-C033. The new step is to carry out all interpolation inside an explicit finite free integral algebra with sufficiently many nodes whose differences are integral units. Coordinate simulation will then return to $\mathbb Z$.

Let $Q\geq2$ be the number of interpolation nodes in one layout. Choose primes
\[
                   Q<p<2Q<q<4Q.
\]
Bertrand's theorem, in the exact primary source cited above, supplies them. Trial division of every candidate up to $4Q$ finds them deterministically in polynomial time in $Q$; no fast primality theorem is needed. For $Q=1$ take $p=2,q=3$. Put $N=pq$ and
\[
 \Phi_N(T)=\frac{(T^N-1)(T-1)}{(T^p-1)(T^q-1)},\qquad
 a=(p-1)(q-1),\qquad A=\mathbb Z[\zeta]=\mathbb Z[T]/(\Phi_N(T)).
\]
Here the notation for $A$ means this explicit quotient; no computation of a ring of integers is required. We verify the polynomial facts used about it.

Over $\mathbb C$, the denominator's roots occur in the numerator with at least the same multiplicities: the common root one has multiplicity two, and the remaining $p$th and $q$th roots occur once. Thus the quotient is a monic polynomial of degree $a$. Polynomial division by a monic integer polynomial takes place over $\mathbb Z$, and its complex remainder is zero, proving $\Phi_N\in\mathbb Z[T]$. Its roots are exactly the primitive $N$th roots, each with multiplicity one, because $N$ is the product of the two distinct primes. Its value at one is
\[
                    \Phi_N(1)=\frac{N}{pq}=1,
\]
by canceling the two factors $T-1$, or equivalently by evaluating the resulting geometric sums. Also $\Phi_N$ divides $T^N-1$ over $\mathbb Z$, so $\zeta^N=1$ in $A$. The algebra $A$ is free over $\mathbb Z$ with the explicit basis
$1,\zeta,\ldots,\zeta^{a-1}$, of rank $a=O(Q^2)$. In particular its scalar inclusion is injective. Irreducibility of $\Phi_N$ is not needed anywhere in the argument.

If $\gcd(d,N)=1$, taking $d$th powers permutes the primitive roots. Therefore $\Phi_N(T)$ divides $\Phi_N(T^d)$ for a nonnegative representative of $d$ modulo $N$. Monic division again shows the divisibility over $\mathbb Z$. Hence $\Phi_N(\zeta^d)=0$ in $A$. Define the integral polynomial
\[
                     U(T)=\frac{\Phi_N(T)-1}{T-1}.
\]
It is integral because its numerator vanishes at one. The identity
\[
                   (1-\zeta^d)U(\zeta^d)=1
                 \qquad(\gcd(d,N)=1)
\]
proves that $1-\zeta^d$ is an integral unit with a displayed inverse.

Take the $Q$ nodes $\alpha_s=\zeta^s$, $1\leq s\leq Q$. Each is a unit because $\zeta^N=1$. For $i\ne j$, the nonzero integer $i-j$ has absolute value less than $Q<p,q$, so it is coprime to $N$. Thus
$\alpha_i-\alpha_j=\zeta^j(\zeta^{i-j}-1)$ is also a unit, with an inverse obtained from the displayed formula and a power of $\zeta$. All these nodes and inverses are elements of the original integral quotient $A$; no localization has occurred. The quotient may ramify after reduction at $p$ or $q$, but this has no effect on these unit identities.

The integral swap matrix $M_0$ from NN-C033 now gives rows
\[
 \varphi_{u,y}(T)=\prod_{s\in E_{u,y}}(1-T/\alpha_s),\qquad
 P_u(T)=\delta_u(I-M_0)+\sum_yM_0[u,y]\varphi_{u,y}(T)\delta_y
                             \quad\hbox{in }A[T]^{1\times D}.
\]
Division by $\alpha_s$ here means multiplication by its explicit integral unit inverse. Their degree and zero-at-mismatched-node properties are unchanged. The exact integer-kernel identity for $M_0$ gives invariance on the same integer Boolean measurement fibers after mapping integers into $A$. This is all that the fiber proof of E Lemma3.2 uses. The ring-valued Boolean-difference identity of Lemma3.3, fixed substitutions, and Taylor truncations therefore compute all jets
\[
                  h_i(z)=H(\alpha_i+z)\bmod z^J
                              \quad\hbox{in }A[y][z]/(z^J)
\]
with the same operation bound as NN-C033. Every equality is formal in the independent weights $y$, and $H(0)=Z_H(y)$ as an element of $A[y]$.

We give the entire final Hasse interpolation explicitly, so that there is no unexamined inverse-matrix or denominator step. Put
\[
 B_i(T)=\prod_{j\ne i}
             \left((T-\alpha_j)(\alpha_i-\alpha_j)^{-1}\right)^J,
 \qquad b_i(z)=B_i(\alpha_i+z).
\]
Then $b_i(0)=1$. Its inverse modulo $z^J$ is the polynomial
$c_i(z)=\sum_{k=0}^{J-1}c_{i,k}z^k$ determined by
\[
 c_{i,0}=1,\qquad
 c_{i,k}=-\sum_{l=1}^k[z^l]b_i(z)\,c_{i,k-l}\quad(1\leq k<J).
\]
This recurrence uses only integer-algebra additions and multiplications. Define
\[
 \widetilde H(T)=\sum_{i=1}^Q B_i(T)
      \left([h_i(z)c_i(z)]_{<J}\right)_{z=T-\alpha_i}.
\]
Its degree is at most $(Q-1)J+J-1=QJ-1$. At node $\alpha_i$ its jet is $h_i$, because $b_ic_i=1\bmod z^J$; at every other node the factor $B_i$ vanishes to order at least $J$. The ideals $(T-\alpha_i)^J$ are pairwise comaximal in $A[T]$, since the differences are units. Their intersection equals their product, generated by the monic polynomial $\prod_i(T-\alpha_i)^J$ of degree $QJ$. A polynomial of smaller degree in this ideal is zero, even over a ring with zero divisors, by monic polynomial division. Therefore the jets uniquely determine a polynomial of degree less than $QJ$. As $\deg H<QJ$, one has $\widetilde H=H$ as a formal identity in $A[y][T]$.

In particular $H(0)$ is computed by the displayed formula using only fixed integral scalars and the jet entries. All interpolation constants are in $A$. This uses neither Gaussian pivots nor division by a derivative factorial, and remains valid after every coefficient-ring homomorphism. No assertion about equality of numerical functions is substituted for polynomial equality.

Here are explicit size and coefficient-height bounds for the scalar computations. The rank $a$ and $N$ are $O(Q^2)$. Since the roots of $\Phi_N$ have complex absolute value one, the sum of absolute values of its coefficients is at most $2^a$ by the elementary-symmetric bounds $\binom ak$. Monic division therefore constructs it in polynomial bit time. Division of $\Phi_N-1$ by $T-1$ gives $U$ of coefficient norm at most $a2^{a+1}$. Evaluating its finitely many needed powers of $\zeta$, and reducing to the monic basis, involves only polynomially many powers and operations of degree polynomial in $Q$.

More quantitatively, let $\|u\|$ be the sum of absolute coordinates of an element $u\in A$ in the monic basis, and let
\[
 K=\max\left(1,\max_{0\leq i,j<a}\|\zeta^{i+j}\|\right).
\]
Then $\|uv\|\leq K\|u\|\|v\|$. Repeated monic reduction of powers of degree at most $2a-2$, using coefficient bounds $2^a$, gives $\log_2 K=O(a^2+1)$. The unit inverses above have coordinate bit height polynomial in $Q$: reduce exponents first modulo $N$, using $\zeta^N=1$, and then reduce the polynomial of degree below $N$ in the monic basis. This requires at most $N$ monic reductions, each with coefficient growth bounded by $1+\|\Phi_N\|$, so its logarithmic norm is polynomial in $Q$.

The coefficients of $B_i(\alpha_i+z)$ are formed from $O(QJ)$ factors with these bounded norms. Extend $\|\cdot\|$ to polynomials by summing coefficient norms. The same multiplication inequality applies, so these coefficients have logarithmic norm polynomial in $Q,J$. Let $B\geq1$ bound the norms of the nonconstant coefficients of $b_i$, uniformly in $i$. If $C_k=\|c_{i,k}\|$, the recurrence gives
\[
 C_0=1,\qquad C_k\leq KB\sum_{l=0}^{k-1}C_l,
          \qquad C_k\leq KB(1+KB)^{k-1}\quad(k\geq1).
\]
Thus $\log(1+C_k)=O(J\log(2+KB))$, still polynomial in $Q,J$. The cardinal-polynomial formula then gives polynomial bit bounds for every final scalar coefficient as well. All scalar computations take polynomial bit time: they involve polynomially many operations on arrays of polynomial length and on integers of these polynomial bit heights. The same estimates apply to rows, shifted Taylor coefficients and a local factor evaluator, because their degrees and scope sizes are polynomially bounded. No integer of superpolynomial bit length is being hidden in a unit inverse.

Use the same high-incidence branches, labels, integer measurements and layout parameters as in NN-C033. Its proof gives $S(n)$ operations over $A[y]$. Each fixed-layout scalar table and each local coefficient evaluation has polynomial bit cost; repeated local evaluations are included in the $S(n)$ operation bound. Store each symbolic result as an arithmetic-gate reference. Replacing an $A$-valued gate by its $a$ coordinates gives an integer arithmetic circuit: addition is coordinatewise and multiplication uses the integer structure constants for the monic quotient basis. There are at most polynomially many coordinate gates per original operation. Their constants have the polynomial bit bounds just proved. Hence the total size and construction bit time remain $S(n)$.

The coordinate descent is exact. The polynomial initially specified as $Z_H(y)$ has integer coefficients, and every step proved that the computed element equals its image in $A[y]$. Since $A$ is free with basis beginning in one, that image has first coordinate $Z_H(y)$ and all other coordinates zero. Take the first output coordinate. This gives the original integral polynomial with integer-gate syntax, without computing its exponentially many coefficients and without a symbolic identity oracle. Its image under any map $\mathbb Z\to R$ is therefore the universal partition polynomial over the arbitrary target ring $R$.

We finally justify the constant-free and formal-degree assertions without assuming that semantic integrality alone eliminates denominators. The integral construction just obtained already has only integer scalar constants of polynomial bit length. It may be arranged homogeneous in the factor-weight blocks: every local factor is linear in its own block, a group product uses exactly its assigned factors, every group sum retains that block degree, and the final Taylor and interpolation sums have total weight degree $m$. In constructing a local evaluator, precompute its scalar Taylor coefficients and then form the linear combinations of its factor weights; all these scalar coefficients have the height bounds above. Empty group products contribute one, and their sums are integer counts at most $2^n$, also of polynomial bit length. Thus all degree-zero operations may be performed as explicit scalar preprocessing. After coordinate simulation, each remaining product either combines positive-degree homogeneous pieces or multiplies one piece by a known integer scalar. Its degree bookkeeping is known from this construction and requires no identity test.

For an integer scalar of bit length $L$, multiplication of a symbolic input by that scalar can be implemented with $O(L)$ doubling and addition/subtraction gates. These gates do not increase formal degree. Integer constant outputs themselves can be built from $1$ and $-1$ by such additions, with formal degree one. Replacing all scalar multiplications this way leaves only products of positive-degree pieces. Induction then bounds formal degree by the positive weight degree, and hence by $m$; the constant case uses degree one. This gives the stated constant-free bound at polynomial overhead. If one's convention permits only addition and multiplication, maintain both signs of each value; the same construction has formal degree at most $2\max(m,1)$, which is still polynomial.

Apply these integral circuits to the exact universal-partition specializations in NN-C029. Preliminary multipliers, their constantly many local specializations, and their fixed-scope integral division corrections now all use integral gates. Their ordinary identity over $\mathbb Z$ is the already-proved first-violation and local-remainder identity, with exactly the same specified multiplier polynomials. Each substituted weight is a constant or a degree-one expression, and each local correction has bounded degree and size, so the constant-free formal-degree bound stays $O(v)$, even without identifying it with the sharper actual degree bound $\deg a_i\leq v$. The IPS polynomial adds its placeholder variables with one multiplication per term. The explicit affine coordinate maps use only these multipliers and the displayed low-degree formulas of NN-C029, preserving subexponential circuit size and polynomial formal degree. This proves all assertions over $\mathbb Z$ and hence after arbitrary base change.

\paragraph{Extension to sparse polynomial factors with growing scopes.}
The same integral construction applies beyond constant arity.
Fix integers $C,a\ge1$.  Suppose there are $n\ge2$ Boolean variables
and $m\le Cn$ factors, each given by an explicit monomial list
\[
 \Phi_f(x)=\sum_{j=1}^{\ell_f}y_{f,j}x^{\alpha(f,j)},
 \qquad d_f=\max_j|\alpha(f,j)|,
 \qquad \sum_f d_f\le Cn.
\]
The coefficient symbols $y_{f,j}$ are independent; repeated
monomials in a list are permitted.  An empty list means the zero
factor and is handled immediately.  Let $L$ be the full bit length
of these lists, including their variable indices and binary
exponents.  Suppose each declared scope $I_f$ has size at most
$\lambda^a$, where $\lambda=\lceil\log_2 n\rceil$.
The degree bound is imposed on these explicitly supplied
polynomials before Boolean reduction.  Then
\[
 Z_{\Phi}(y)=\sum_{x\in\{0,1\}^n}\prod_f\Phi_f(x)
\]
has an integral division-free circuit of size and deterministic
bit construction time
\[
 \operatorname{poly}(n,L)\,
 2^{O_{C,a}(n(\log\log n)^2/\sqrt{\log n})}.
\]
Its integer constants have polynomial bit length in $n,L$.
It admits the same constant-free compilation of formal degree
at most $\max(m,1)$, with subtraction gates assigned the
addition degree rule.  The output is the formal polynomial
over $\mathbb Z[y]$, so this single circuit identity transfers
to every commutative coefficient ring.

In particular, fixed-degree factors with a polylogarithmic
number of monomials satisfy these hypotheses after changing
the fixed constants: if the degree is at most $k$ and the
list length at most $(\log n)^b$, the scope is at most
$k(\log n)^b$, and the total degree is at most $kCn$.
This preserves the original number $n$ of Boolean variables.
There are no auxiliary verifier variables, and no truth table
on the entire growing scope is constructed.

We prove the exact quantitative interface.  Append one
dummy factor equal to one, with declared scope $\{i\}$, for
each variable $i$.  These factors contribute no coefficient
symbols and have input degree zero; they only ensure that
every variable has a declared incidence.  If $M_0$ is the
resulting total scope length, then
\[
              n\le M_0\le n+Cn\lambda^a.
\]
Put
\[
 B_0=\max(1,\lceil M_0/n\rceil)\lceil\sqrt\lambda\rceil,
 \qquad H=\{i:\deg_{\rm inc}(i)>B_0\}.
\]
Double-counting incidences gives
$|H|\le M_0/B_0\le n/\sqrt\lambda$.
Sum over all $2^{|H|}$ assignments to these variables.  On a
branch, substitute the chosen bits in the explicit monomial
lists and remove them from each declared scope.  Keep the
remaining declared scopes even if some monomial becomes
zero.  This uses only the syntactic list and chosen bits,
with no test of a formal polynomial identity.

Let $n'=n-|H|$.  For sufficiently large $n$ one has
$n/2\le n'\le n$.  Each surviving variable has incidence at
most $B_0$, every scope still has size at most $\lambda^a$,
and the dummy factors ensure $n'\le M'\le B_0n'$ for the
remaining total incidence $M'$.  Factors with empty scope
can be multiplied outside the branch's counting routine;
their polynomials in the $y$ variables are explicit linear
forms.  This removal does not change $M'$.

Choose a fixed integer $\beta$ larger than $a+2$, increasing
the threshold of the exceptional finite range to absorb
$C$.  With $\lambda'=\lceil\log_2 n'\rceil$, both the maximum
scope and $B_0$ are at most $(\lambda')^\beta$ for all
sufficiently large $n$.  E Lemma~4.8, with
$\nu'=\lceil\log_2\lambda'\rceil$, therefore supplies
\[
 r=\left\lfloor\frac{\sqrt{\lambda'}}{(\nu')^2}\right\rfloor,
 \quad Q=\left\lfloor\frac{\lambda'}{128\nu'}\right\rfloor,
 \quad R=(\beta+3)\lceil\sqrt{\lambda'}\rceil,
 \quad \tau=\frac1{r\lambda'},\quad D=r^{2Q}.
\]
Its exact numerical checks and E Lemma~4.7 construct the
layout in polynomial time.  Input sizes failing those
checks form a finite range depending only on the fixed
constants; direct expansion handles that range within
the asserted asymptotic bound.

The independent-incidence degree in E Section~3.1 is bounded
by the sum of the factor degrees, because replacing the
same Boolean variable in different factors by distinct
indeterminates does not increase any factor's total degree.
Consequently, on every branch,
\[
       d\le\sum_f d_f\le Cn\le 2Cn'.
\]
This is the crucial degree hypothesis; the possibly larger
number $M'$ of incidences is not substituted for $d$.
The interpolation polynomial has degree at most $dR$.
Taking $q=\lfloor dR/Q\rfloor$ and $J=q+1$ gives $QJ>dR$.
E Proposition~3.4 has the explicit enumeration bound
\[
       2Qr\,C_q(2D+1)^{2\tau n'}2^{2n'/r},\qquad
       C_q=\sum_{s=0}^{\min(q,n')}2^s\binom{n'}s.
\]
Put $\eta=R/Q$.  The source's finite-difference estimate
$\eta^qC_q\le(1+2\eta)^{n'}$ yields
\[
 \log_2 C_q
 \le q\log_2(Q/R)+n'\log_2(1+2R/Q)
 =O_C\!\left(n'\frac RQ\log\frac{2Q}{R}\right).
\]
Together with E Lemma~4.8 this bounds all three exponential
costs by
\[
 O_{C,a}\!\left(\frac{n'(\nu')^2}{\sqrt{\lambda'}}\right).
\]
The additional branching cost has logarithm
$|H|\le n/\sqrt\lambda$.  Since $n'=\Theta(n)$, their sum
is $O_{C,a}(n(\log\log n)^2/\sqrt{\log n})$.

It remains to verify the factor and coefficient costs,
which an arity statement alone would not justify.  After
the fixed Boolean substitutions in E Lemma~3.3, evaluate
each listed monomial directly in the truncated algebra
$A[z]/(z^J)$, using its binary exponents or at most
$\sum_i\alpha(f,j)_i\le Cn$ multiplications.  Sum these
values with their formal coefficients $y_{f,j}$.
This takes polynomially many algebra operations in
$n,J,L$; it never enumerates the $2^{|I_f|}$ local
assignments.  Before multiplication by the formal
coefficients, each such substituted monomial is a
scalar Taylor polynomial.  The rows and unit inverses
have the polynomial coordinate heights already proved
for the cyclotomic construction.  A product of at most
$Cn$ such scalar inputs, followed by Taylor truncation,
still has polynomial bit height by the same multiplicative
coordinate-norm bound.  Adding at most $L$ listed terms
increases logarithmic norm by at most $O(\log(L+1))$.
All local scalar preprocessing is therefore polynomial
in $n,L$, and $Q,R,J,D$ are polynomially bounded in $n$.

Use the integral swap matrix, integer measurement fibers,
unit-separated cyclotomic nodes and explicit Hasse
interpolation proved above.  Their correctness depends on
the layout and the degree estimate, not on constant scope
size.  They give formal identities over $A[y]$ at each
stage.  The same coefficient-independent choices of
representatives and branches allow circuit unrolling,
and taking the coordinate of one in $A$ descends the
formal output to $\mathbb Z[y]$.  Each genuine factor
remains linear in its own coefficient block.  Group
products, sums, empty-scope multiplication and the final
sum over branches retain the same block degree.  The
constant-free compilation therefore has formal degree
at most $\max(m,1)$, just as in the constant-arity case.
This finishes the construction and its bit bound.

The hypotheses delimit the extension.  A general truth
table on $\operatorname{polylog} n$ variables can have
interpolation degree equal to its scope size; $O(n)$ such
factors need not have total degree $O(n)$.  In that case
the actual $q=\lfloor dR/Q\rfloor$ must be retained and
the displayed bound has not been proved.  Nor does a
coefficient-dependent compression of a numerical equation
system automatically preserve this universal formal
polynomial in independent parameters.

\paragraph{A sparse permanent application in the matrix-order parameter.}
Fix $a\ge1$ and $r\ge2$.  Let $\Omega\subseteq[r]\times[r]$ be a prescribed
matrix support with at most $(\lceil\log_2 r\rceil)^a$ entries in
each row, and give the allowed entries independent variables
$a_{ij}$.  The matrix has zero elsewhere.  Its permanent polynomial
has a deterministically constructible integral constant-free circuit
of size and bit construction time
\[
 \operatorname{poly}(r)\,
       2^{O_a(r(\log\log r)^2/\sqrt{\log r})},
\]
with formal degree $O(r)$.  No column-degree restriction is imposed.
The same claim allows a fixed multiplicative constant in the
row-support bound, by increasing the fixed scope exponent and
handling bounded sizes directly.  The parameter is the matrix
order $r$, rather than the number of allowed matrix entries.

Import Ryser's classical inclusion--exclusion identity in the
exact form reproduced in Servedio--Wan, \emph{Computing sparse
permanents faster}, author manuscript dated June~18, 2005,
Section~2, printed p.~3, first display:
\[
 \operatorname{per}(A)=(-1)^r\sum_{S\subseteq[r]}(-1)^{|S|}
                          \prod_{i=1}^r\sum_{j\in S}a_{ij}.
\]
The primary manuscript is
\url{https://www.cs.columbia.edu/~atw12/papers/perm.pdf}.
It states the identity for real or complex matrices.  Both sides
are polynomials with integer coefficients in independent matrix
entries, so agreement for all complex entries is an identity in
$\mathbb Z[a_{ij}]$ and hence after every ring base change.
This uses that a polynomial vanishing on all complex tuples is
the zero polynomial; it does not reprove the classical formula.

For the characteristic vector $x$ of $S$ one has
$(-1)^{|S|}=\prod_{j=1}^r(1-2x_j)$.  Consequently
\[
 \operatorname{per}(A)=(-1)^r
 \sum_{x\in\{0,1\}^r}
       \left(\prod_{j=1}^r(1-2x_j)\right)
       \left(\prod_{i=1}^r\sum_{j:(i,j)\in\Omega}a_{ij}x_j\right).
\]
This is a sum-product on exactly $r$ Boolean variables with $2r$
linear factors.  Its independent-incidence degree is at most
$2r$, each row factor has polylogarithmic scope, and the unary
sign factors have scope one.  The list description has polynomial
size.  A zero row gives the zero permanent immediately, and the
empty matrix has permanent one.  Apply the growing-scope theorem
of NN-C034 to the nontrivial cases, specializing the unary factor
coefficients to $1,-2$.  These are fixed integer constants, with
$-2=(-1)+(-1)$ available in the constant-free syntax.  Its integral
descent proves the full permanent identity; it does not merely
compute its values modulo a prime.  The factor-block formal degree
is at most $2r$, and the outer sign can be implemented by subtraction
from zero.  This proves the claimed circuit and construction bounds.

An allowed column may occur in every row.  The total-incidence
branching already proved in NN-C034 removes at most
$r/\sqrt{\log r}$ such high-incidence variables before applying
the layout, so unbounded column degree introduces no extra witness
parameter.  In particular, the conclusion covers supports with
$r\operatorname{polylog} r$ allowed entries at the original matrix
order.  It makes no claim for an arbitrary dense support: its
row scopes can have size $r$, outside the hypothesis.

\paragraph{Only a total support bound is necessary.}
Fix $C,a\ge1$ and $r\ge2$.  For a prescribed support
$\Omega\subseteq[r]\times[r]$ with
\[
                     |\Omega|\le Cr(\lceil\log_2r\rceil)^a,
\]
the full permanent polynomial has a deterministically
constructible integral constant-free circuit of size and
bit construction time
\[
 \operatorname{poly}(r)\,
       2^{O_{C,a}(r(\log\log r)^2/\sqrt{\log r})},
\]
and formal degree at most $2r$, with the subtraction convention
used above.  Thus no bound on any individual row or column
degree is needed.  The original parameter is still the
matrix order $r$.

Here is the full reduction to the preceding row-scope result.
Let $\lambda=\lceil\log_2r\rceil$, set
$T=\lceil\lambda^{a+2}\rceil$, and let $H$ be the set of
rows containing more than $T$ allowed entries.  If $h=|H|$,
then counting allowed entries gives
\[
                          h\le Cr/\lambda^2.
\]
For sufficiently large $r$, this is at most $r/2$.
Expand the definition of the permanent by first specifying
the columns matched to the rows of $H$.  It gives the exact
integral polynomial identity
\[
 \operatorname{per}(A)=
 \sum_{\substack{\pi:H\hookrightarrow[r]\\(i,\pi(i))\in\Omega}}
       \left(\prod_{i\in H}a_{i,\pi(i)}\right)
       \operatorname{per}\bigl(A_{[r]\setminus H,\,[r]\setminus\pi(H)}\bigr).
\]
This is simply the partition of the permutations in the
permanent definition according to their restrictions to
$H$; each full permutation occurs in exactly one summand.
There is no sign and no multiplicity factor.  If $H$ is
empty the sum has its one empty restriction, and its
weight is one.  Enumerating at most $r^h$ functions and
retaining the allowed injections constructs the sum
deterministically with polynomial overhead per term.

Every minor has order $r'=r-h\ge r/2$.  Its remaining
row supports have size at most $T$, and deleting columns
cannot increase them.  Since
$\lceil\log_2r'\rceil\ge\lambda-1$, one has
\[
                   T\le(\lceil\log_2r'\rceil)^{a+3}
\]
for sufficiently large $r$.  The preceding row-scope
permanent construction therefore applies to every minor,
with a fixed changed scope exponent.  Zero rows can be
detected from the prescribed support and give zero terms.
The finitely many exceptional matrix orders, including
orders zero and one, are computed directly.

The logarithm of the number of restrictions is at most
\[
                   h\log_2r=O_C(r/\log r),
\]
which is absorbed by
$O_{C,a}(r(\log\log r)^2/\sqrt{\log r})$.
The minor construction has that same bound because
$r'=\Theta(r)$.  Multiplication by the $h$ selected entry
variables and summation of all terms add only the stated
overhead.  Each minor circuit has formal degree at most
$2r'$, so each term has formal degree at most
$2r'+h\le2r$, and summation takes the maximum.  All scalar
constants retain their polynomial bit lengths.  This
proves the total-support theorem as an integral formal
identity, and therefore over every commutative coefficient
ring by base change.

There is a concrete proof-size separation on the family already audited in NN-C021. Use its mod-three Tseitin 3-CNF contradictions, with $n$ denoting the number of variables of the resulting CNF and with $O(n)$ clauses. Every ordinary polynomial-calculus refutation over $\mathbb F_2$ has explicitly written monomial size at least $2^{\kappa n}$ for some fixed $\kappa>0$. The sparse-CNF specialization just proved constructs a constant-free Hilbert-like IPS circuit over $\mathbb F_2$ of size $S(n)=2^{o(n)}$ for the same clause polynomials, without introducing verifier wires or Boolean axioms into that IPS identity. If $M_{\rm PC}(n)$ and $C_{\rm IPS}(n)$ are the minimum sizes in these two specified models, then for all sufficiently large $n$,
\[
       \frac{M_{\rm PC}(n)}{C_{\rm IPS}(n)}
           \geq\frac{2^{\kappa n}}{S(n)}
           \geq 2^{\kappa n/2}.
\]
This is the precise exponential ratio. The numerator counts explicit monomials throughout an ordinary PC derivation; the denominator counts gates in a circuit IPS certificate. The latter certificate has actual polynomial degree at most $n+1$ and a constant-free circuit of formal degree $O(n)$. These degree statements neither identify the two size measures nor contradict the linear PC degree lower bound. The deduction uses the classical monomial-PC lower bound and E's designated algorithmic input, and implies no polynomially bounded proof system or $\mathrm{NP}=\mathrm{coNP}$ collapse.''',
        'Complete integral cyclotomic-node, Hasse interpolation, height, symbolic descent and certificate proof; independent review pending.',
r'''The remaining integral-gate obstacle in NN-C029 and NN-C033 is closed for the stated symbolic families, including polynomial-list factors with polylogarithmic scopes and linear total input degree. List length and coefficient bit cost are explicit; generic growing-scope truth tables need not satisfy the degree budget. The construction is over Z itself, with polynomial-bit integer constants and a constant-free presentation of polynomial formal degree, so it transfers to every coefficient ring through one universal identity. It makes actual integral ideal multipliers and empty-case geometric coordinate maps effective at E's subexponential bound. It does not give polynomial-size circuits or IPS certificates, deterministic polynomial-time PIT, NP=coNP, or $VP^0=VNP^0$. Dense permanent encodings and long verifier circuits retain their actual edge/wire parameter overhead. The finite free cyclotomic algebra is an explicit computational extension, not an assumed canonical GCT object.''',
r'''Let $B=\mathbb Z[y]$ and
\[
 \mathscr A=B[x_1,\ldots,x_n]/(x_i^2-x_i),\qquad
                       a=\prod_f\Phi_f(x).
\]
The finite locally free multiplication trace $\operatorname{Tr}_{\mathscr A/B}(a)$ is the universal partition polynomial. The theorem supplies an integral arithmetic circuit for this regular function on $\operatorname{Spec}B$ in size $S(n)$, with a constant-free presentation of polynomial formal degree. The auxiliary extension $B\to A\otimes_{\mathbb Z}B$ is finite free and faithfully flat. It contains the required distinct unit-separated interpolation sections; these differences remain units after every base change, including ramified residue characteristics. Exact interpolation and coordinate projection descend the computed regular function to $B$.

Fix $C,a\ge1$.  Let $m\le Cn$ explicit polynomial lists
$\Phi_f=\sum_j y_{f,j}x^{\alpha(f,j)}$ have description
length $L$, declared scopes of size at most
$(\lceil\log_2n\rceil)^a$, and total degree budget
$\sum_f\max_j|\alpha(f,j)|\le Cn$.  Put $B=\mathbb Z[y]$ and
\[
 \mathscr A=B[x_1,\ldots,x_n]/(x_i^2-x_i),\qquad
                       u=\prod_f\Phi_f(x).
\]
The finite locally free algebra $\mathscr A$ has rank $2^n$.
Its multiplication trace
$\operatorname{Tr}_{\mathscr A/B}(u)=Z_\Phi(y)$, as is
seen in the orthogonal Boolean-idempotent basis.  This
regular function on $\operatorname{Spec}B$ has an integral
circuit of size and bit construction time
$\operatorname{poly}(n,L)2^{O_{C,a}(n(\log\log n)^2/\sqrt{\log n})}$,
with polynomial-bit integer constants and a constant-free
compilation of formal degree at most $\max(m,1)$, with $n$
the original number of Boolean coordinates.  For every map
$B\to R$ the same circuit computes the base-changed
multiplication trace over $R$; coordinate descent from
the finite free cyclotomic extension proves the identity
before any specialization.  The exact classical trace
and base-change interface is EGA IV4, 18.2.1--18.2.2,
printed p.~111, including equation 18.2.1.2.  This is an
effective theorem for these specified regular trace
functions, not a claimed polynomial-time algorithm for
general finite algebra traces or GCT multiplicities.

For a support $\Omega\subseteq[r]\times[r]$ satisfying
$|\Omega|\le Cr(\lceil\log_2r\rceil)^a$, put
$B=\mathbb Z[a_{ij}:(i,j)\in\Omega]$ and
$\mathscr A=B[x_1,\ldots,x_r]/(x_j^2-x_j)$.  The regular
function
\[
 \operatorname{Tr}_{\mathscr A/B}\left(
     (-1)^r\prod_j(1-2x_j)
                 \prod_i\sum_{j:(i,j)\in\Omega}a_{ij}x_j\right)
                              =\operatorname{per}(A)
\]
has an integral constant-free circuit of size
$\operatorname{poly}(r)2^{O_{C,a}(r(\log\log r)^2/\sqrt{\log r})}$
and formal degree at most $2r$, valid after every base
change.  Ryser's identity identifies this signed trace,
while the heavy-row decomposition constructs it using
smaller trace functions with polylogarithmic row scopes.

For the split torus with characters indexed by $\Omega$,
let $\mathcal V_\Omega$ have one basis vector of character
$\prod_i a_{i,\sigma(i)}$ per allowed perfect matching.
Its effective character is the same permanent polynomial.
The restriction partition above gives the actual direct-sum
decomposition
\[
 \mathcal V_\Omega\simeq
  \bigoplus_{\pi}
    \chi_\pi\otimes\mathcal V_{\Omega_\pi},
 \qquad \chi_\pi=\prod_{i\in H}a_{i,\pi(i)},
\]
where $\Omega_\pi$ is the remaining minor support and its
characters are included in the original torus.  Applying
the integral minor circuits to these summands gives the
stated character circuit; positivity of the decomposition
does not remove the virtual differences inside the minor
circuits.  The precise classical trace and character-ring
interfaces remain EGA IV4, 18.2.1--18.2.2, printed p.~111,
and the SGA3/SGA6 locators already stated in NN-S019.

For the unsatisfiable local-verifier scheme, the same circuits give an ordinary global ideal identity $\sum_i a_if_i=1$ over $\mathbb Z$ and the explicit mutually inverse maps identifying its smooth counting cubic with affine space. The maps have the actual degree bounds from NN-C029, integral coefficient circuits of size $S(v)$, and polynomial formal degree after removing all large constant leaves. Thus these are effective integral geometric trivializations, valid after arbitrary base change, with no denominator-prime exclusion. On the empty Boolean equation schemes of NN-C021, these circuit ideal certificates over $\mathbb F_2$ have size $2^{o(n)}$, while deriving their unit ideal by ordinary monomial polynomial calculus requires size $2^{\Omega(n)}$. This compares specified presentations of the unit-ideal proof, not different underlying zero schemes or different cohomological degrees. The exact classical multiplication-trace and base-change locator is EGA IV4,18.2.1--18.2.2, printed p111, equation18.2.1.2. All node, inverse, flat scalar-extension and polynomial-identity calculations are proved above; no unverified Grothendieck archive cote or GCT canonical-basis functor is invoked.''',
        inputs)
