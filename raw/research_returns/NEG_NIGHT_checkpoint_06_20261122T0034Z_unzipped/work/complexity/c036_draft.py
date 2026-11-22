"""NN-C036: integral arbitrary-density CNF weights by slower sparsification."""

def append_c036(add,E,ALGTRACE):
    inputs=[
        dict(E,locator='Lemma6.3 disjoint sparsification, exact occurrence bound B=O_k((sigma^-1 log(2/sigma))^(k-1)); Section3.1 total input degree and Proposition3.4 with the actual q=floor(dR/Q); complete Lemmas4.7--4.8'),
        {'source':'NN-C034','locator':'integral swap-matrix and cyclotomic Hasse routine, explicit polynomial coefficient-height bounds, formal coordinate descent and constant-free block compilation; the construction is reused below with a larger actual degree parameter'},
        {'source':'NN-C035','locator':'faster characteristic-two formal weighted construction, retained as a distinct bound'},
        {'source':'NN-C015','locator':'constant-free coefficient-norm induction at polynomial formal degree; used for exact rational specialization bit bounds'},
        {'source':'Grochow--Pitassi, Circuit Complexity, Proof Complexity, and Polynomial Identity Testing: The Ideal Proof System',
         'locator':'Author JACM manuscript Definition1.1 printed draftp1:4; Lemma4.2 full proof pp1:26--1:28, equations(4)--(6); classical first-violation identity',
         'url':'https://www.cs.toronto.edu/~toni/Papers/jacm-gp.pdf'},
        {'source':'NN-C029','locator':'classical first-violation coefficient factorization and the integral unit-ideal affine coordinate formulas'},
        ALGTRACE]
    add('NN-C036','NEG_NIGHT-01;NEG_NIGHT-04;NEG_NIGHT-06;NEG_NIGHT-09',
        'Slower sparsification gives integral symbolic weights and ideal certificates for arbitrary-density CNFs',
r'''Fix $k\ge2$. For every $k$-CNF $F$ on $n$ declared variables with $m$ clauses, the integral satisfying-assignment polynomial
\[
       A_F(z)=\sum_{x\models F}\prod_{i=1}^n z_{i,x_i}
                      \in\mathbb Z[z_{i,b}:1\le i\le n,\ b\in\{0,1\}]
\]
has a deterministically constructible division-free integral circuit of size and bit construction time
\[
 (n+m)^{O_k(1)}
  2^{O_k\!\left(n(\log\log n)^{1+1/k}/(\log n)^{1/(2k)}\right)}
                                                    = (n+m)^{O_k(1)}2^{o(n)}.
\]
The circuit can be made constant-free with polynomial formal degree. It computes the formal polynomial over $\mathbb Z$, so the same circuit works after every commutative-ring base change. The number of original Boolean variables remains $n$.

The same assertion holds for a product of $O(n)$ explicitly listed weight factors with independent coefficient parameters, polylogarithmic scopes, and linear total input degree; include a polynomial factor in their description length and allow the constants to depend on the fixed scope and degree bounds. Thus arbitrary-density fixed-width CNFs admit symbolic integral weighted counting at a mildly subexponential original-variable bound. Arbitrary rational specializations of the weights can also be evaluated within the displayed time times a polynomial in their full bit length.

In particular the full multivariate independence polynomial of every $n$-vertex graph, with no edge-density restriction, has an integral constant-free circuit of size
\[
 \operatorname{poly}(n+|E|)\,
       2^{O\!\left(n(\log\log n)^{3/2}/(\log n)^{1/4}\right)}
\]
and polynomial formal degree. The characteristic-two construction of NN-C035 retains its sharper exponent. This integral construction does not lift an arbitrary characteristic-two circuit; it uses a different decomposition of the original Boolean problem.

For every unsatisfiable normalized width-$k$ CNF, the same bound constructs ordinary integral multipliers $h_j$ with $\sum_jv_jh_j=1$ for its clause-violation polynomials $v_j$, without Boolean axioms or extra variables. One has $\deg h_j\le n-|S_j|$ for clause scope $S_j$, and the resulting Hilbert-like IPS circuit has actual degree at most $n+1$ and polynomial formal degree. The associated hypersurface $t^2-t=\sum_jy_jv_j(x)$ admits explicit integral affine-space coordinate maps of the same circuit bound, of forward degree at most $n+2$ and inverse degree at most $n+2k+2$.''',
        inputs,
r'''The construction uses the integral clause-satisfaction polynomial instead of compressing the constraints in characteristic two. For a clause $C$, let $\ell(x)$ be the affine integer polynomial for each literal and put
\[
                   c_C(x)=1-\prod_{\ell\in C}(1-\ell(x))\in\mathbb Z[x].
\]
For every Boolean assignment this factor is exactly one when $C$ is satisfied and zero otherwise. Its degree is at most the clause width and its expanded list has at most $2^k+1$ terms. These are literal integer equalities, valid after every coefficient-ring map. An empty clause gives output zero. A formula without clauses has the explicit two-rail circuit $\prod_i(z_{i,0}+z_{i,1})$. Bounded exceptional input sizes are expanded directly.

We choose a slower sparsification parameter than the one used for the characteristic-two theorem. Put
\[
 \lambda=\lceil\log_2 n\rceil,\qquad
 \nu=\lceil\log_2\lambda\rceil,
 \qquad s=\max\{t\in\mathbb Z_{\ge0}:t^{2k}\nu^{2k+2}\le\lambda\}.
\]
For sufficiently large $n$, one has $s\ge2$ and
\[
 \frac1s=\Theta_k\!\left(
             \frac{\nu^{1+1/k}}{\lambda^{1/(2k)}}\right)=o(1).
\]
The integer $s$ is computed exactly by integer comparisons in polynomial time in $\log n$ for fixed $k$. Sizes with $s<2$ form a finite range. Apply E Lemma6.3 with $\sigma=1/s$. Its leaf satisfying sets partition that of $F$, its tree has $\operatorname{poly}_k(n,s)2^{n/s}$ nodes, and its explicit leaf occurrence bound satisfies
\[
 B=O_k\bigl((s\log(2s))^{k-1}\bigr)
       =O_k(s^{k-1}\nu^{k-1}).
\]
We may increase $B$ to at least one. The choice of $s$ implies
\begin{equation}\label{eq:C036-balance}
     \frac{B\nu^2}{\sqrt\lambda}
       =O_k\!\left(\frac{s^{k-1}\nu^{k+1}}{\sqrt\lambda}\right)
       =O_k(1/s),
\end{equation}
because $s^k\nu^{k+1}\le\sqrt\lambda$. This estimate balances the cost per leaf against the number of leaves.

Fix a nontrivial leaf $F_t$. It has at most $nB$ nonempty clauses and total clause-incidence length at most $nB$. Its product of satisfaction factors has independent-incidence input degree at most $nB$, since each factor's degree is bounded by its number of literals. Multiply by the $n$ unary factors
\[
                       W_i(x_i)=(1-x_i)z_{i,0}+x_i z_{i,1}.
\]
The desired leaf polynomial is exactly
\[
 Z_t(z)=\sum_{x\in\{0,1\}^n}\left(\prod_{C\in F_t}c_C(x)\right)
                                      \prod_iW_i(x_i)
                          \quad\hbox{in }\mathbb Z[z].
\]
For the more general weight factors, their specified linear total-degree budget adds $O(n)$ to the same bound. In either case the number of factors is $O(n(B+1))$, the total input degree is $d=O(n(B+1))$, and the total list length is polynomial in $n$ and the supplied weight-list length. The crucial difference from the literal theorem statement of NN-C034 is that $B$ now grows. We therefore reuse its construction with the actual $d$, rather than invoking its linear-degree corollary outside its hypotheses.

The clause scopes are constant, and their maximum variable incidence is at most $B$. General weight scopes may be polylogarithmic and have uneven incidences. If needed, append the degree-zero dummy factors and branch on high-incidence variables exactly as in NN-C034, using the full total scope length $M$ and threshold
\[
                   \max(1,\lceil M/n\rceil)\lceil\sqrt\lambda\rceil.
\]
There are at most $n/\sqrt\lambda$ branched bits. Every remaining instance has $n'=n-O(n/\sqrt\lambda)=\Theta(n)$ variables, polylogarithmic scopes and maximum incidence, and input degree $d=O(n'B)$. The unbranched unary-weight case already has this layout regime. A fixed exponent $\beta$, depending only on $k$ and the fixed weight-scope exponent, bounds the maximum scope and incidence by $(\lceil\log_2n'\rceil)^\beta$ for all sufficiently large $n$. This is possible because $B$ and every added weight-incidence threshold are fixed powers of $\log n$.

Apply the exact layout parameters of E Lemma4.8 to $n'$, writing $\lambda'=\lceil\log_2n'\rceil$ and $\nu'=\lceil\log_2\lambda'\rceil$. They satisfy
\[
 \frac RQ=O_\beta(\nu'/\sqrt{\lambda'}),\qquad
 \log(2Q/R)=O(\nu'),\qquad
 \tau\log(2D+1)+\frac1r=O_\beta((\nu')^2/\sqrt{\lambda'}).
\]
The source constructs and checks the numerical hypotheses exactly; its finite exceptional range is handled by direct expansion. The interpolation polynomial has degree at most $dR$. Set
\[
                         q=\lfloor dR/Q\rfloor,\qquad J=q+1.
\]
E Proposition3.4 supplies the enumeration factor
$2QrC_q(2D+1)^{2\tau n'}2^{2n'/r}$, where
$C_q=\sum_{j\le\min(q,n')}2^j\binom{n'}j$.
Its finite-difference estimate with $\eta=R/Q$ gives
\[
 \log_2 C_q
   \le q\log_2(Q/R)+n'\log_2(1+2R/Q)
   =O\!\left(n'B\frac RQ\log\frac{2Q}{R}\right).
\]
Consequently all three exponential costs are
\[
           O_{k,\beta}\!\left(n'B\frac{(\nu')^2}{\sqrt{\lambda'}}\right)
                       =O_{k,\beta}(n/s)
\]
by \eqref{eq:C036-balance} and $n'=\Theta(n)$. The high-incidence branching contributes at most $n/\sqrt\lambda=O(n/s)$ to the exponent. In particular $q,J,Q,R,D$ remain polynomially bounded in $n$; no numerical parameter with exponentially long encoding has entered the construction.

We check the additional hypotheses of the integral implementation. Take the same finite free cyclotomic algebra, unit-separated nodes, integral swap matrix and exact integer measurement fibers as NN-C034. Their construction depends on the layout, not on having only $O(n)$ factors. A clause factor evaluates by its at most $2^k+1$ monomials. A supplied weight factor evaluates directly from its list. Every substituted monomial has degree at most $d=O(nB)$ and is a product of that many row Taylor inputs at worst. The coefficient-norm estimates in NN-C034 bound the bit height of each row and each unit inverse polynomially in $n$. Repeated multiplication of $O(nB)$ such scalar inputs, in a polynomial-length truncated Taylor array, adds only a polynomial to the logarithmic norm. The factor count $O(nB)$ and $B=\operatorname{polylog}n$ are themselves polynomial in $n$. Hence all local scalar preprocessing has polynomial bit cost. The explicit Hasse cardinal recurrence has polynomial bit cost in $Q,J$, exactly as before.

All identities in the integer-fiber separation, Boolean-difference formula, Taylor readout and cyclotomic interpolation hold formally in the weight variables. Store symbolic ring operations as shared gate references, and descend by taking the scalar coordinate in the finite free algebra. This constructs an integral circuit for $Z_t$, with size and bit construction time a polynomial factor times $2^{O_{k,\beta}(n/s)}$. There is no symbolic identity test and no reduction modulo a prime. For constant-free compilation one may first put independent coefficient symbols on every monomial of every factor, use the same factor-block construction, and then specialize each clause coefficient to its fixed integer value and each weight coefficient to its specified parameter. Its formal degree is $O(nB+n)$, since the factor count is $O(nB+n)$ and every such coefficient specialization is constant or linear. This is polynomial in $n$. The scalar-height estimates justify replacing all integer scalar multiplications by binary doubling and addition/subtraction at polynomial overhead. This is the same explicit integral compilation as NN-C034, now with a polylogarithmic factor-count multiplier.

Sum the resulting integral circuits over the disjoint sparsification leaves. Every satisfying assignment contributes its weight exactly once, as an integer polynomial, and no other assignment contributes. The output is therefore $A_F$ over $\mathbb Z$, or the stipulated general weighted sum. The tree count, leaf work and high-incidence branches all have exponent $O_{k,\beta}(n/s)$. Polynomial preprocessing and input normalization give the asserted full time bound. An additive sum of leaf circuits preserves their polynomial formal-degree bound. Formal equality over $\mathbb Z$ proves all coefficient-ring base changes simultaneously.

For completeness, rational specialization of the two-rail weights also has the asserted bit-time bound, without an unproved bound on intermediate arithmetic values. Let the circuit have $S$ gates and formal degree $D=\operatorname{poly}(n)$, and let $L$ be the total bit length of the rational inputs. Choose a common input denominator $Q_0$ by multiplying their denominators, so $\log Q_0\le L$. The constant-free coefficient-norm induction of NN-C015 gives coefficient norm at most $2^{SD}$ at every gate. After evaluation, a denominator divides $Q_0^D$ and the numerator has bit length $O(D(S+L+1))$. Exact rational arithmetic therefore evaluates all $S$ gates in $\operatorname{poly}(S,n,L)$ bit operations. Taking a fixed polynomial power of $S$ preserves the displayed $2^{O_k(n/s)}$ bound. The same argument applies to the general weight coefficients. We make no polynomial-working-space claim from this circuit evaluation argument.

For the independent-set example use the width-two CNF $\bigwedge_{uv\in E}(\neg x_u\vee\neg x_v)$ on the original vertex bits and then substitute $z_{i,0}=1$, $z_{i,1}=y_i$. Setting $k=2$ gives the stated exponent. Its coefficients are the integer zero-one indicators of independent subsets. This proves an integral circuit for their chosen lift by direct integer clause indicators; it is not a generic procedure for lifting circuits from $\mathbb F_2$ to $\mathbb Z$. The sharper characteristic-two bound of NN-C035 is therefore retained alongside this result.

\paragraph{Ordinary integral ideal certificates without a density bound.}
Let $F=C_1\wedge\cdots\wedge C_m$ be an unsatisfiable fixed-width
$k$-CNF on $n$ declared variables.  Use the standard clause encoding:
delete repeated literals, discard tautological clauses, and let
$v_j(x)$ be the product of the distinct falsifying literal factors
of $C_j$.  Empty clauses have $v_j=1$ and give an immediate
certificate.  Then one can deterministically construct integral
constant-free circuits for polynomials $h_j$ such that
\[
                 \sum_{j=1}^m v_j(x)h_j(x)=1
                              \quad\hbox{in }\mathbb Z[x_1,\ldots,x_n],
\]
without adding Boolean equations or verifier variables.  Their
total size and bit construction time are
\[
 (n+m)^{O_k(1)}
  2^{O_k(n(\log\log n)^{1+1/k}/(\log n)^{1/(2k)})}.
\]
If $S_j$ is the scope of $C_j$, the multipliers may be chosen
with $\deg h_j\le n-|S_j|$, so each product $v_jh_j$ has actual
degree at most $n$.  The circuit formal degree is polynomial
in $n$; it is not identified with the sharper actual degree.

The ideal identity is the classical first-violated-clause
certificate of Grochow--Pitassi, \emph{Circuit Complexity, Proof
Complexity, and Polynomial Identity Testing: The Ideal Proof
System}, author JACM manuscript, Lemma~4.2 and equations
(4)--(6), printed draft pp.~1:26--1:28; the primary file is
\url{https://www.cs.toronto.edu/~toni/Papers/jacm-gp.pdf}.
Its Definition~1.1 is on printed draft p.~1:4.  These are
the author manuscript's page markers, not an asserted match
with the final journal pagination.  The new consequence is
the constructive original-$n$ circuit bound for all clause
densities, obtained by the following exact factorization of
those classical multipliers.

Suppose there is no empty clause.  For each $j$, let
$b^{(j)}\in\{0,1\}^{S_j}$ be the unique assignment falsifying
$C_j$.  Restrict the prefix $C_1\wedge\cdots\wedge C_{j-1}$
by these fixed bits, keeping all the remaining $n_j=n-|S_j|$
declared variables.  Call the resulting width-at-most-$k$
CNF $R_j$.  Simplified false or empty prefixes are handled
by the same direct cases as in the main theorem.  Apply
NN-C036 to its full two-rail polynomial
\[
 H_j(z)=\sum_{a\models R_j}\prod_{i\notin S_j}z_{i,a_i},
\]
and specialize $z_{i,0}=1-x_i$, $z_{i,1}=x_i$.  The output is
\[
 h_j(x_{[n]\setminus S_j})=
 \sum_{a\models R_j}\prod_{i\notin S_j}
                       x_i^{a_i}(1-x_i)^{1-a_i}.
\]
Thus $h_j$ is exactly the coefficient of the $j$th placeholder
in the cited first-violation certificate: fixing the falsifying
tuple leaves precisely the assignments satisfying all earlier
clauses.  Multiplication by $v_j$ restores the missing factors
on $S_j$.  In the notation
$\delta_b(x)=\prod_i x_i^{b_i}(1-x_i)^{1-b_i}$, this identifies
$v_jh_j$ with the sum of $\delta_b$ over the first-violation
class of clause $j$.  Equations (4)--(6) of the cited classical
proof therefore give the displayed ordinary integral identity.
No identity merely modulo $x_i^2-x_i$ is substituted for it.

For $n>2k$, each nontrivial call uses $n-k\le n_j\le n$,
so $n_j=\Theta(n)$ and its exponent is bounded by the same
displayed expression in $n$.  There are at most $m$ calls,
and forming all restricted prefixes has polynomial cost
in $n+m$.  The fixed small range of $n$ is handled by direct
expansion.  Each coefficient substitution is a constant-free
linear expression, hence preserves the polynomial formal-degree
bound.  This proves the total circuit and construction bounds.
The displayed expression for $h_j$ proves its actual degree
bound without expanding it.  A uniform algorithm may first
use E Theorem~1.1 to decide satisfiability, reporting that
case or constructing the certificate when the answer is
negative; E's decision cost is absorbed by this weaker exponent.

With placeholders $u_1,\ldots,u_m$, the circuit
\[
                    C(x,u)=\sum_j u_jh_j(x)
\]
is a Hilbert-like IPS certificate: $C(x,0)=0$ and
$C(x,v(x))=1$.  It has actual degree at most $n+1$,
polynomial formal degree, and the same circuit-size bound.
The certificate works over every commutative ring by base
change from its integral identity.  These superpolynomial
size bounds do not make the system polynomially bounded,
give polynomial-time deterministic PIT verification, or
imply a corresponding small monomial-PC derivation.''',
        'Integral dense-CNF construction, optimized parameter bound and ordinary ideal-certificate consequence proved; independent review pending.',
r'''This closes the specific integral formal-weight gate for arbitrary-density fixed-width CNFs and arbitrary-graph independence polynomials. The cost is a weaker exponent than the characteristic-two compressed construction: it balances disjoint sparsification with the actual larger interpolation degree and does not lift a finite-field circuit. It also constructs ordinary integral Hilbert-like IPS certificates without Boolean axioms and explicit affine coordinate maps at the original-variable bound, for every clause density. The construction is uniform and preserves the original Boolean variables, but remains superpolynomial. It supplies no polynomial-size IPS or arithmetic circuits, no general deterministic polynomial-time PIT, and no VP/VNP or P/NP collapse. Generic verifier reductions still charge their gate variables before this theorem is applied.''',
r'''Let $F$ be a fixed-width CNF on $n$ declared Boolean coordinates. Its integral Boolean scheme is
\[
 Y_F=\operatorname{Spec}\!\left(
 \mathbb Z[x_1,\ldots,x_n]/(x_i^2-x_i,\ 1-c_C(x):C\in F)\right).
\]
Here $c_C=1-\prod_{\ell\in C}(1-\ell(x))$ is the integral clause-satisfaction indicator. The scheme is the disjoint union of one $\operatorname{Spec}\mathbb Z$ for each satisfying assignment. Put $B=\mathbb Z[z_{i,b}]$, $\mathscr A_F=\mathcal O(Y_F)\otimes_{\mathbb Z}B$, and
\[
                         w=\prod_i((1-x_i)z_{i,0}+x_i z_{i,1}).
\]
Then the finite locally free multiplication trace $\operatorname{Tr}_{\mathscr A_F/B}(w)$ equals the integral assignment polynomial $A_F$. For fixed width $k$, this regular trace function has a deterministically constructible integral constant-free circuit of size $(n+m)^{O_k(1)}2^{O_k(n(\log\log n)^{1+1/k}/(\log n)^{1/(2k)})}$ and polynomial formal degree. The same circuit computes the trace after every base change, including all characteristics and nonreduced coefficient rings. Explicit weight factors with polylogarithmic scopes and linear total input degree have the same bound with their description length and fixed parameters included.

Disjoint sparsification is a decomposition of $Y_F$ into clopen finite etale subschemes over $\mathbb Z$, and the trace adds over it. The construction retains the actual integer component multiplicities, rather than only their residues. Equivalently, the torus with one character $z_{i,b}$ per literal rail has an effective module with one basis vector of character $\prod_i z_{i,x_i}$ for each satisfying assignment; its character is computed by the integral circuit using virtual differences. For a graph, this yields the effective independent-subset character after setting the zero rails to one. The exact trace/base-change source is EGA IV4,18.2.1--18.2.2, printed p111, equation18.2.1.2; the split-torus character and Grothendieck-ring locators are those in NN-S019. This is an effective statement for these presented finite schemes and characters, not a theorem about general GCT multiplicities.

For an unsatisfiable normalized width-$k$ CNF with clause
polynomials $v_1,\ldots,v_m$, the closed subscheme
$V(v_1,\ldots,v_m)\subseteq\mathbb A^n_{\mathbb Z}$ is empty,
and its unit ideal has the displayed explicit integral
circuit certificate of size
$(n+m)^{O_k(1)}2^{O_k(n(\log\log n)^{1+1/k}/(\log n)^{1/(2k)})}$.
No Boolean equations occur in that ideal.  The multipliers
have degree at most $n-|S_j|$ and integral constant-free
circuits of polynomial formal degree.

For the affine hypersurface
\[
 X_F=\{t^2-t=\sum_{j=1}^m y_jv_j(x)\}
                          \subseteq\mathbb A^{n+m+1}_{\mathbb Z},
\]
the same certificate gives the explicit isomorphism
$X_F\simeq\mathbb A^{n+m}_{\mathbb Z}$ by the unit-ideal
coordinate formulas already proved in NN-C029:
\[
 z_j=y_j+h_j(x)(2t-t^2),\qquad
 t=\sum_jv_j(x)z_j,\qquad
 y_j=z_j+h_j(x)(t^2-2t).
\]
The first formula is the map from $X_F$ to coordinates
$(x,z)$, and the last two define its inverse.  The equality
$\sum_jv_jh_j=1$ makes $\sum_jv_jz_j=t$ on $X_F$ and
$\sum_jv_jy_j=t^2-t$ on the inverse image; substitution
then gives both identity composites.  These calculations
use no division and hold over every base ring.  The forward
map has degree at most $n+2$ and the inverse has degree at
most $n+2k+2$, since $\deg(\sum_jv_jz_j)\le k+1$.
Sharing the common sum and multiplier circuits gives both
maps the same mildly subexponential original-$n$ circuit
bound and polynomial formal degree.  This is an effective
integral trivialization for the stated empty clause systems,
not a general recognition theorem for affine space.''',
        inputs)
