"""NN-C018: fixed finite rings, with a restricted weighted extension."""

def append_c018(add,E,SGATRACE,SGAFINITE):
    abelian={'source':'J.S. Milne, Group Theory, v4.01 (2025)',
             'locator':'Theorems1.54 and1.57(c), pp.25--27, finite abelian groups as products of prime-power cyclic groups',
             'url':'https://www.jmilne.org/math/CourseNotes/GT.pdf'}
    add('NN-C018','NEG_NIGHT-01',
        'Sparse polynomial equations over every fixed finite commutative ring',
r'''Let $R$ be any fixed finite commutative ring. Fix $k,a,b$. Exact counting, witness search, and exact uniform sampling for systems of at most $n(\log n)^a$ degree-at-most-$k$ polynomials over $R$, with at most $(\log n)^b$ monomials per equation, have the NN-C017 time bound
\[
 \operatorname{poly}(L+n)\,
 2^{O_{R,k,a,b}(n(\log\log n)^2/\sqrt{\log n})}
\]
and polynomial space. Sampling has expected running time. In a fixed $p$-primary ring, the same bound computes a weighted sum over the solutions when there are $O(n)$ bounded-arity factors whose rational table entries lie in a fixed finite alphabet. For a general $R$, this weighted assertion holds when the factors separate as products over its primary components. Arbitrary input-height rational weights and weights coupling distinct primary components are not included in this weighted assertion.''',
        [{'source':'NN-C017','locator':'complete prime-field Boolean-system counter and p-ary equation compression'},
         abelian,
         dict(E,locator='Proposition3.4; Lemmas4.7--4.8 and5.1--5.2; AppendixB')],
r'''The zero ring is trivial, so assume $R$ has at least two elements. Write its characteristic as $M=\prod_p p^{a_p}$. The elementary integer Chinese remainder construction gives integers $e_p$ which are one modulo $p^{a_p}$ and zero modulo every other prime-power divisor of $M$. Their images in $R$ are orthogonal central idempotents with sum one. Hence
\[
 R\longrightarrow\prod_p R_p,\qquad R_p=e_pR,\qquad
 x\longmapsto(e_px)_p
\]
is a ring isomorphism: its inverse adds the components, and the identities just stated check both compositions and multiplication. Every equation therefore holds exactly when all its component equations hold. Variables in distinct components are independent. Thus the solution set is the Cartesian product of the component solution sets, and the exact counts multiply. There are only a fixed number of components. It suffices to handle a fixed $p$-primary ring.

By the stated finite-abelian-group theorem, fix additive generators $b_1,\ldots,b_d$ of this ring with unique coordinates
\[
 x=\sum_{j=1}^d z_jb_j,
 \qquad0\leq z_j<p^{a_j},\qquad
 (R,+)\cong\bigoplus_{j=1}^d\mathbb Z/p^{a_j}\mathbb Z.
\]
The multiplication table $b_ib_j=\sum_t c_{ijt}b_t$, with fixed integer representatives for the $c_{ijt}$, is part of this fixed presentation. Expanding one degree-$k$ monomial in these coordinates introduces only a constant depending on $R,k$ many integer monomials, all of degree at most $k$. Constant coefficients in $R$ are handled by the same fixed multiplication table. Consequently a ring equation is equivalent to $d$ congruences
\[
 L_t(z)\equiv0\pmod{p^{a_t}},
\]
where $L_t$ is an integer polynomial of fixed degree and polylogarithmic monomial sparsity. Intermediate reductions modulo the coordinate moduli are unnecessary: the additive relations $p^{a_t}b_t=0$ ensure that the final coordinate congruence gives the correct element.

Encode each coordinate by $\lceil\log_2(p^{a_j})\rceil$ bits and impose its fixed-size validity table, as in NN-C017. This gives $N=\Theta_R(n)$ Boolean variables. Every coordinate polynomial after substitution still has fixed degree and polylogarithmic sparsity. We next replace divisibility by $p^{a_t}$ by a fixed number of genuinely sparse $\mathbb F_p$ polynomial equations, taking care not to invert a factorial divisible by $p$.

For every integer $u$ and $j\geq0$, define the integer-valued polynomial
\[
 D_j(u)=\binom{u}{p^j}.
\]
For fixed $a$ and $j<a$, this is periodic modulo $p$ with period $p^a$. Indeed the formal power series identity
$(1+T)^{u+p^a}=(1+T)^u(1+T)^{p^a}$ holds also for negative integer $u$, with integral binomial coefficients. Modulo $p$, the last factor is $1+T^{p^a}$, by repeated Frobenius. Thus coefficients below degree $p^a$ do not change. For $0\leq u<p^a$, write $u=\sum_{i<a}u_ip^i$ with $0\leq u_i<p$. Then
\[
 (1+T)^u\equiv\prod_{i<a}(1+T^{p^i})^{u_i}\pmod p.
\]
The coefficient of $T^{p^j}$ is $u_j$: the maximum total exponent available from the lower factors is $p^j-1$, and any higher factor has exponent greater than $p^j$. By periodicity, for every integer $u$ the residues $D_0(u),\ldots,D_{a-1}(u)$ are exactly the base-$p$ digits of $u\bmod p^a$. In particular,
\[
 p^a\mid u\quad\Longleftrightarrow\quad
 D_j(u)\equiv0\pmod p\quad(0\leq j<a).
\]

Apply this to each $L_t(x)$. As a rational polynomial,
$D_j(L_t)=\prod_{h=0}^{p^j-1}(L_t-h)/(p^j)!$ has fixed degree and polylogarithmic monomial sparsity: $p^j$ is a constant depending only on $R$. Expand it over $\mathbb Q$, replace every positive bit power $x_i^h$ by $x_i$, and collect like monomials. The resulting multilinear polynomial has \emph{integer} coefficients. To prove this, for any rational polynomial $Q$ taking integer values on the Boolean cube, its unique multilinear representative has coefficient
\[
 [x^S]\operatorname{ML}(Q)
   =\sum_{T\subseteq S}(-1)^{|S|-|T|}\,Q(\mathbf1_T),
\]
where coordinates outside $T$ are zero. This is the inversion of
$Q(\mathbf1_T)=\sum_{S\subseteq T}[x^S]\operatorname{ML}(Q)$ and is an integer. Here $Q=D_j(L_t)$ is integer-valued because $L_t$ has integer Boolean values. Computationally one simply expands and collects the sparse polynomial; the coefficient formula proves integrality and does not require enumerating all assignments on the polylogarithmic scope. All rational denominators before collection divide the fixed factorial, and coefficient bit lengths are polynomial in the input length. Reduce the resulting integer coefficients modulo $p$ only after this collection.

The final Boolean system has $N(\log N)^{O(1)}$ equations, fixed degree, and polylogarithmic monomial sparsity. The number of coordinate and digit equations per original equation is fixed. It includes the constant-size validity equations. NN-C017 applies and is parsimonious with respect to valid coordinate encodings. The primary-component counts multiply as above; their outputs have $O_R(n)$ bits. Self-reduction and sampling work componentwise, and independent uniform component samples give the uniform distribution on their Cartesian product. This proves the unweighted claims.

For the weighted $p$-primary assertion, first compress the constraint system by the \emph{unweighted} NN-C017 counter; the selected equations preserve its exact Boolean zero set. Let the fixed rational weight alphabet have a common positive denominator $D$, and let $A\geq1$ bound the absolute values of all the integer weights obtained by multiplying by $D$. If there are $f\leq Cn$ weight factors, the numerator of the weighted sum after this scaling has absolute value at most $2^N A^f$. Choose $\ell=O_{R,C,A}(N)$ so that
\[
 p^\ell>2^{N+1}A^f.
\]
Express each scaled table by its integer multilinear interpolation polynomial on its fixed number of coordinate bits. Fill invalid codes by zero; the validity constraints already exclude them. Multiply these weight factors by the constraint factors in the same algebra $\mathbb Q[V]/(V^\ell)$ used in NN-C017. At Boolean points every omitted order-$\ell$ term remains divisible by $p^\ell$ after multiplication by the integer weight. The total incidence degree is still $O(N)$: the compressed constraint contribution is $O(m+\ell)$ and the $O(n)$ weight factors each have bounded degree and scope. The added scopes preserve polylogarithmic total incidence. The same layout, coefficient-height, interpolation, and space proof applies. The residue has a unique representative in $(-p^\ell/2,p^\ell/2)$ within the stated magnitude bound; this is the desired signed numerator. Divide by $D^f$ to recover the rational weighted sum.

If the ring has several primary components and each weight factor is a product of factors in the individual components, the full weighted summand and the solution domain separate, so the total partition function is the product of the computed component partition functions. Without that hypothesis, the product-of-counts argument does not apply. Likewise a variable $B$-bit weight alphabet can require $\ell=\Theta(n+nB)$, so this proof cannot simply hide arbitrary weight height in a polynomial overhead while retaining the same exponent.''',
        'Complete deduction proved; complete self proof-check passed; independent review pending.',
r'''Nilpotents and fixed composite characteristic do not by themselves obstruct the sparse-equation algorithm: the digit reduction keeps the number of variables, equation degree and monomial sparsity within the required fixed-parameter interface. This is a theorem for each fixed ring, including fixed prime-power residue rings, not an algorithm uniform in a growing modulus such as an RSA modulus. The weighted restrictions are substantive, and the full rational bounded-arity theorem NN-C003 remains a different interface.''',
r'''A polynomial solution over a finite nonreduced ring is an $R$-point of the affine equation scheme, not in general a geometric point of a reduced scheme. The primary decomposition is a decomposition of $\operatorname{Spec}R$ into clopen components; its functor of points turns the equation solution set into the displayed Cartesian product. Additive coordinates and binomial digits then present this finite set by a finite reduced Boolean scheme over $\mathbb F_p$. That presentation preserves the set and its rank, not the nilpotent structure, tangent spaces or deformation theory of the original equation scheme. Counting is the trace of the identity on the product algebra indexed by these points, and weighted counting is the diagonal multiplication trace; these assertions follow directly in the idempotent basis, with SGA4 XVII6.2.3 as the finite-trace dictionary. SGA7 II XXII Corollary3.2 applies to the resulting finite scheme for its mod-$p$ trace, not automatically to the original nonreduced ring-valued functor. No canonical-basis or orbit-closure positivity is inferred.''',
        [E,abelian,SGATRACE,SGAFINITE])
