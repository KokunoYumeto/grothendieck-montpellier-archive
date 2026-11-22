"""NN-C035: formal characteristic-two weights after exact zero-set compression."""

def append_c035(add,E,ALGTRACE):
    inputs=[
        dict(E,locator='Lemma6.3 disjoint sparsification on the original declared variables; Lemmas6.1--6.2 and Proposition6.4, especially the exact no-false-survivor conclusion'),
        {'source':'NN-C001','locator':'deterministic compression of quasilinear sparse F2 equation lists to at most6n equations, preserving their full Boolean zero set'},
        {'source':'NN-C034','locator':'reviewed growing-scope extension: explicit polynomial lists, polylogarithmic scopes, linear total input degree, and one formal integral circuit identity over every coefficient ring'},
        ALGTRACE]
    add('NN-C035','NEG_NIGHT-01;NEG_NIGHT-04;NEG_NIGHT-09',
        'Exact zero-set compression yields formal weighted CNF circuits in characteristic two',
r'''Fix a clause width $k\ge2$. For any $k$-CNF $F$ on $n$ declared variables with $m$ clauses, the full satisfying-assignment polynomial
\[
 A_F(z)=\sum_{x\models F}\prod_{i=1}^n z_{i,x_i}
                       \in\mathbb F_2[z_{1,0},z_{1,1},\ldots,z_{n,0},z_{n,1}]
\]
has a deterministically constructible constant-free arithmetic circuit of size and bit construction time
\[
 (n+m)^{O_k(1)}\,
      2^{O_k(n(\log\log n)^2/\sqrt{\log n})}.
\]
Its formal degree is $O_k(n)$. The parameter is the original number of Boolean variables; no verifier wires are added. This is equality of formal polynomials, valid after base change to every commutative ring of characteristic two.

More generally, one may replace the product of the $n$ displayed unary weights by at most $Cn$ explicitly listed polynomial factors in $x$, with independent coefficient parameters, polylogarithmic scopes, and total input-degree budget at most $Cn$, for fixed $C$ and scope exponent. The same bound holds with a polynomial factor in their description length and with the constants depending on these fixed parameters.

In particular, for every graph $G$ on $n$ vertices, with no sparsity or maximum-degree restriction, its full multivariate independence polynomial
\[
                       I_G(y)=\sum_{S\text{ independent}}\prod_{i\in S}y_i
                                      \in\mathbb F_2[y_1,\ldots,y_n]
\]
has such a circuit in the original vertex parameter. The two-rail polynomial $A_F$ is formally nonzero exactly when $F$ is satisfiable, even though its value at all weights equal to one records only the parity of the satisfying count.''',
        inputs,
r'''We first retain the exact scope of the imported compression theorem. Its rows are selected by numerical zero counts for the supplied Boolean equations. They depend on $F$, but they do not depend on any of the formal weight parameters introduced here. NN-C001 proves equality of the whole Boolean zero set, not just equality of its cardinality. That stronger assertion is what permits symbolic weights.

Handle an empty clause by outputting zero. A formula with no clauses has the explicit circuit $\prod_i(z_{i,0}+z_{i,1})$ in the two-rail case. Bounded exceptional sizes may be expanded directly. For the general case put $\lambda=\lceil\log_2 n\rceil$ and apply E Lemma6.3 with the rational parameter
\[
                         \sigma=1/\lceil\sqrt\lambda\rceil.
\]
The lemma produces a tree of at most $\operatorname{poly}_k(n)2^{O(n/\sqrt{\log n})}$ nodes on the same $n$ declared variables. Its leaf satisfying sets partition the satisfying set of $F$. In every leaf each variable has occurrence at most
\[
 B=O_k\bigl([\sigma^{-1}\log(2/\sigma)]^{k-1}\bigr)
                                  =(\log n)^{O_k(1)}.
\]
The input normalization costs $\operatorname{poly}_k(n,m)$ and the numerical parameter has $O(\log\log(n+2))$ bits. Thus every nontrivial leaf has $n(\log n)^{O_k(1)}$ clauses, while the number of Boolean variables is still $n$.

For a leaf $F_t$, take the usual clause-violation polynomial
\[
                  v_C(x)=\prod_{\ell\in C}(1-\ell(x))
                                         \quad\hbox{over }\mathbb F_2,
\]
where the affine literal polynomial has value one exactly when that literal is true. A clause has at most $k$ literals, so its expanded violation polynomial has degree at most $k$ and at most $2^k$ monomials. It vanishes exactly when the clause is satisfied. Apply NN-C001 to these equations. The resulting list
\[
                   p_{t,1},\ldots,p_{t,b_t},\qquad b_t\le6n,
\]
has degree at most $k$, polylogarithmic monomial sparsity and hence polylogarithmic scopes, and satisfies
\[
 x\models F_t\quad\Longleftrightarrow\quad
              p_{t,j}(x)=0\text{ for every }j
                     \qquad(x\in\{0,1\}^n).
\]
Its construction takes $\operatorname{poly}_k(n)2^{O_k(n\log\log n/\sqrt{\log n})}$ bit operations. This uses only the numerical equations, so all coefficient-parameter symbols remain untouched.

Now work in the polynomial coefficient algebra $\mathbb F_2[z]$. For a Boolean assignment, each $p_{t,j}(x)$ is either zero or one. Therefore
\[
                e_t(x)=\prod_{j=1}^{b_t}(1+p_{t,j}(x))
\]
is exactly the indicator of $F_t$ on the Boolean cube. Use the unary interpolation factors
\[
                   W_i(x_i)=(1-x_i)z_{i,0}+x_i z_{i,1}.
\]
The sum-product
\[
              Z_t(z)=\sum_{x\in\{0,1\}^n}e_t(x)\prod_iW_i(x_i)
\]
therefore equals $\sum_{x\models F_t}\prod_i z_{i,x_i}$ as a formal polynomial over $\mathbb F_2$. This assertion follows term by term before any evaluation of $z$.

There are at most $7n$ factors. The sum of their degrees in the Boolean inputs is at most $(6k+1)n$, and every scope is polylogarithmic. Each factor is explicitly listed, and the list lengths are polynomial in $n$. These are precisely the hypotheses of the growing-scope part of NN-C034. To use its universal coefficient form, first place independent formal coefficients on each monomial occurrence of these factors. Construct the universal integral circuit supplied there. Then apply the coefficient-ring homomorphism to $\mathbb F_2[z]$ which sends the constraint coefficients to their known zero-one values and the weight coefficients to the displayed linear parameters. Thus the descended circuit computes $Z_t$ as a formal polynomial. The intermediary integral universal identity is being specialized to characteristic two; the characteristic-two indicator equality is not asserted as an integer equality.

The block compilation in NN-C034 gives a constant-free circuit of formal degree $O_k(n)$ after these specializations: each genuine coefficient input becomes a constant or a linear expression in a weight parameter, and only $O_k(n)$ factor blocks are used. In characteristic two subtraction is addition. The resulting size and construction time per leaf are bounded by $\operatorname{poly}_k(n)2^{O_k(n(\log\log n)^2/\sqrt{\log n})}$. All representation and control choices are discrete or depend on the known clause coefficients; there is no symbolic identity test and no evaluation/interpolation in the weight parameters.

Sum these circuits over the sparsification leaves. Disjointness is essential: every satisfying assignment occurs in exactly one leaf, and every nonsatisfying assignment in none. Consequently the sum is exactly $A_F(z)$, with no multiplicity introduced by the decomposition. Adding the leaf-count exponent $O_k(n/\sqrt{\log n})$, and the smaller compression-construction exponent, preserves the displayed bound. An additive sum of the leaf circuits does not increase formal degree.

For the general weighted statement, replace $\prod_iW_i$ by the supplied factor product. The compressed constraint factors add at most $6kn$ to its total input degree and at most $6n$ to its factor count. The maximum scope remains a fixed power of $\log n$, and direct list evaluation has polynomial cost in the stated description length. NN-C034 therefore applies with changed fixed constants. The same indicator identity and disjoint leaf sum prove the formal weighted equality. In this version distinct assignments can yield the same weight monomial, whose coefficient correctly counts their contributions modulo two.

For the graph application take
\[
                         F_G=\bigwedge_{uv\in E(G)}(\neg x_u\vee\neg x_v).
\]
Its satisfying assignments are exactly the characteristic vectors of independent vertex sets. It has $n$ variables and $|E(G)|$ width-two clauses; no edge variable is introduced. Specializing $z_{i,0}=1$ and $z_{i,1}=y_i$ gives $I_G(y)$. The construction time is polynomial in $n+|E(G)|$ times the displayed original-$n$ exponential.

Finally, different assignments give different two-rail monomials, each with coefficient one. Hence $A_F$ is the zero formal polynomial if and only if the satisfying set is empty. The specialization $z_{i,b}=1$ collapses all these monomials to the same constant and records only their sum modulo two. These are different readout operations. The construction is mildly subexponential, not polynomial, so even a polynomial-time PIT algorithm applied to its output would not by itself yield a polynomial-time SAT algorithm. Nor does a circuit over $\mathbb F_2$ for a zero-one-coefficient polynomial automatically provide an integral circuit for its chosen zero-one coefficient lift: reduction loses multiples of two, and no coefficientwise lifting operation is supplied here. NN-C036 separately constructs the integral polynomial for this CNF family by slower disjoint sparsification and exact integer clause indicators, with a weaker exponent.''',
        'Complete characteristic-two symbolic-weight deduction proved; independent review pending.',
r'''This closes the bounded-density restriction for formal weighted fixed-width CNF counting in characteristic two while retaining the original witness variables. Numerical compression is legitimately reused because it preserves the entire Boolean solution set and ignores weight parameters. The result is stronger than a parity value at a single specialization and weaker than a polynomial-size circuit theorem. This characteristic-two construction does not itself give a characteristic-zero circuit for the chosen zero-one coefficient lift; NN-C036 subsequently supplies a direct integral construction for this family at a weaker exponent. Neither result gives general PIT derandomization or a VP/VNP collapse. The dense-graph independence-polynomial example has an explicit original-vertex bound, unlike an encoding that charges every graph edge as a witness bit.''',
r'''Let $Y_F$ be the finite etale subscheme of $\operatorname{Spec}(\mathbb F_2[x_1,\ldots,x_n]/(x_i^2-x_i))$ cut out by the clause-violation equations. Put $B=\mathbb F_2[z_{i,b}]$ and $\mathscr A_F=\mathcal O(Y_F)\otimes_{\mathbb F_2}B$. It is finite locally free over $B$, with one rank-one summand for every satisfying assignment. For
\[
                           w=\prod_i\bigl((1-x_i)z_{i,0}+x_i z_{i,1}\bigr),
\]
the multiplication trace $\operatorname{Tr}_{\mathscr A_F/B}(w)$ is $A_F(z)$ in the component-idempotent basis. For fixed clause width, this regular function has a deterministically constructible constant-free circuit of size $(n+m)^{O_k(1)}2^{O_k(n(\log\log n)^2/\sqrt{\log n})}$ and formal degree $O_k(n)$. This statement remains true after every base change to a characteristic-two coefficient ring. The same trace theorem holds for the explicitly listed weight factors with polylogarithmic scopes and linear total input degree stated above.

The compressed equations define the same closed subscheme inside the Boolean scheme, because its product coordinate algebra has ideals determined by their vanishing components. The sparsification leaves form a disjoint union decomposition of $Y_F$, and multiplication trace adds over that decomposition. The nonzero two-rail coefficient records an actual component; trace at all weights equal to one is only its rank modulo two. Every point of $Y_F$ is $\mathbb F_2$-rational, so Frobenius on $H^0_{\mathrm{et}}(Y_F\times\overline{\mathbb F}_2,\mathbb Q_\ell)$, for $\ell\ne2$, is the identity. This weight-zero purity does not compute the symbolic trace. The exact classical multiplication-trace and base-change locator is EGA IV4,18.2.1--18.2.2, printed p111, equation18.2.1.2. No reductive-group multiplicity or canonical GCT object is asserted.''',
        inputs)
