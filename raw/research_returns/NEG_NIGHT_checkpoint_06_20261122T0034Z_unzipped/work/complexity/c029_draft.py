"""NN-C029: E constructs ordinary ideal multipliers as rational arithmetic circuits."""

def append_c029(add,E,ALGTRACE):
    gp={'source':'Grochow--Pitassi, Circuit Complexity, Proof Complexity, and Polynomial Identity Testing: The Ideal Proof System',
        'locator':'Author JACM manuscript, Definition1.1 and Hilbert-like terminology, printed draftp1:4; Lemma4.2 and complete proof, printed draftpp1:26--1:28, equations(4)--(6)',
        'url':'https://www.cs.toronto.edu/~toni/Papers/jacm-gp.pdf',
        'access_note':'Author primary manuscript read directly. Its draft page numbers are not asserted to be the final JACM65(6), Article37(2018) pagination. The classical first-violation identity is background, not a new finding.',
        'evidence':'work/complexity/grochow_pitassi_author.pdf;grochow_pitassi_author.txt lines1463--1593'}
    inputs=[{'source':'NN-C016','locator':'complete coefficient-independent symbolic partition construction, fixed arity and linear factor density'},
            dict(E,locator='Proposition3.4 over every commutative Q-algebra; Lemma4.6 replacement-row denominator (R-1)!Q!; Lemmas4.7--4.8 and equation parameter-QR; AppendixB Hermite matrix in subsection rational-readout; coefficient-independent measurement separation'),
            gp,ALGTRACE,
            {'source':'NN-S016','locator':'ordinary integral Bezout identity and explicit affine-space coordinate formulas; work/complexity/c027_degree_addendum.tex and work/root/chapter8.tex'},
            {'source':'NN-C027','locator':'quadratic AND/NOT verifier equations with all Boolean axioms and the associated smooth integral cubic'}]
    add('NN-C029','NEG_NIGHT-06;NEG_NIGHT-04;NEG_NIGHT-10e',
        'E constructs subexponential ordinary ideal certificates and affine trivializations',
r'''Fix a density constant $C$. Let $f_1,\ldots,f_h\in\mathbb Z[x_1,\ldots,x_v]$, $h\leq Cv$, be the Boolean, AND/NOT-gate and acceptance equations of NN-C027. In particular all $x_j^2-x_j$ are retained, each equation has degree at most two, scope at most three and constant coefficient size, and its Boolean values belong to $\{0,1,-1\}$. If the system is unsatisfiable, E deterministically constructs division-free arithmetic circuits over $\mathbb Q$ for integral polynomials $a_i(x)$ satisfying the ordinary polynomial identity
\[
                  \sum_{i=1}^h a_i(x)f_i(x)=1,
          \qquad \deg a_i\leq v.
\]
The total circuit size and construction time are
\[
 S(v)=\operatorname{poly}(v)\,
 2^{O_C(v(\log\log v)^2/\sqrt{\log v})},
\]
and every rational constant has polynomial bit length. Thus $\sum_i a_i(x)z_i$ is a Hilbert-like IPS certificate with a constructible $S(v)$-size proof over $\mathbb Q$. Its coefficient polynomials are integral; the circuit representation is allowed rational constants.

For fixed-width $k$-CNFs with $m\leq Cn$ clauses there is a stronger specialization on the original $n$ input variables: writing $g_i$ for the product of the clause's falsifying literals, E constructs integral $A_i$ with $\sum_i A_i g_i=1$, without Boolean axioms, in size and time $S(n)$, with constants also depending on $k$. The first-violated-clause identity itself is classical Grochow--Pitassi Lemma4.2; the deduction here is the E-based circuit bound and its ordinary-ideal extension to the quadratic verifier presentation.

In the empty case, E also constructs $S(v)$-size rational arithmetic circuit descriptions of mutually inverse integral polynomial maps
\[
 X=\left\{t^2-t=\sum_i y_i f_i(x)\right\}
       \simeq\mathbb A^{v+h}_{\mathbb Z}.
\]
Their degrees are at most $v+2$ and $v+6$. For a verifier on $n$ input bits with $s$ gates, the parameter is $v=n+s$, up to harmless constant additions. No original-$n$ bound for arbitrary long verifier circuits is asserted.

There is an explicit large-characteristic transfer. Put
$B(v)=\max(2,\lceil\log_2 v\rceil)$. The multiplier circuits can be chosen with constants in $\mathbb Z[1/B(v)!]$. Hence they give circuits of the same size over every field of characteristic $p>B(v)$, with construction bit overhead polynomial in $\log p$. The same statement holds for C016's universal partition polynomials and for the sparse-CNF specialization with $v$ replaced by $n$. This original localization argument does not cover fixed small characteristic as the input size tends to infinity. NN-C033 subsequently closes that limitation by a modified integral-swap-matrix and extension-node construction; NN-C034 then constructs integral circuits over Z itself.''',
        inputs,
r'''Bounded values of the parameters can be handled by direct expansion. We first prove the ordinary-ideal assertion for the quadratic verifier list. For a bit vector $b$ put
\[
 e_b(x)=\prod_{j:b_j=1}x_j\prod_{j:b_j=0}(1-x_j),
 \qquad
 a_i^{(0)}(x)=\sum_{b\in\{0,1\}^v}e_b(x)f_i(b)
                  \prod_{j<i}(1-f_j(b)^2).
\]
The factors $1-f_j(b)^2$ are exactly the indicators of $f_j(b)=0$. At any bit vector $b$, unsatisfiability guarantees a first index $i$ with $f_i(b)\ne0$. Its coefficient in the displayed sum is $f_i(b)\in\{1,-1\}$, and all other first-violation coefficients vanish. Therefore
\[
                    \sum_i a_i^{(0)}(b)f_i(b)=1.
\]
Each $a_i^{(0)}$ is an integral multilinear polynomial of degree at most $v$. The Boolean equations themselves have zero values and hence zero preliminary multipliers.

The preliminary multipliers are symbolic bounded-arity partition functions. Their summation variables are the $v$ bits $b$. There are at most $h$ prefix factors with tables $1-f_j(b)^2$, one local factor with table $f_i(b)$, and $v$ unary factors with respective weights $x_l$ at $b_l=1$ and $1-x_l$ at $b_l=0$. Every scope has size at most three and there are $O(v)$ factors and incidences. The fact that the unreduced expression $1-f_j^2$ can have degree four is harmless: its Boolean table, interpolated on at most three variables, has degree at most three. The coefficient algebra is $\mathbb Q[x_1,\ldots,x_v]$, with the $x_l$ treated as formal coefficients rather than extra summation variables.

Apply NN-C016 separately to these $h$ partition functions and specialize its independent factor weights to the indicated constants or linear polynomials. These are constant-size substitutions, so they preserve the bound $S(v)$. The factor count, rather than an unproved bound on each variable's incidence, supplies the hypothesis: the total number of incidences is $O(v)$, and C016 explicitly branches on high-incidence variables. Multiplying by $h=O(v)$ changes only the polynomial prefactor. Its construction makes no identity tests on the coefficient algebra and introduces no division by a polynomial in the $x_l$. Its only inversions are of explicit rational interpolation constants, whose bit lengths are polynomial. This yields circuits for every $a_i^{(0)}$ within the claimed time and size.

An ordinary polynomial identity still requires Boolean-ideal correction; evaluating correctly on the cube alone is insufficient. Here locality makes that correction cheap without globally expanding the circuit. Let $I_i$ be the scope of $f_i$ and $t_i=|I_i|\leq3$. Since $a_i^{(0)}$ is multilinear, its local interpolation is
\[
 a_i^{(0)}(x)=\sum_{\sigma\in\{0,1\}^{I_i}}
        A_{i,\sigma}(x_{\overline I_i})e_\sigma(x_{I_i}),
 \qquad A_{i,\sigma}=a_i^{(0)}\big|_{x_{I_i}=\sigma}.
\]
At most eight circuit specializations compute these polynomials, and their degrees are at most $v-t_i$. In the constant number of local variables the polynomial
\[
       e_\sigma f_i-f_i(\sigma)e_\sigma
\]
has zero multilinear remainder. Its degree is at most $t_i+2$. Explicit integral monomial division therefore gives
\[
 e_\sigma f_i-f_i(\sigma)e_\sigma
      =\sum_{j\in I_i}r_{i,\sigma,j}(x_{I_i})(x_j^2-x_j),
      \qquad \deg r_{i,\sigma,j}\leq t_i.
\]
For completeness, this division uses only
\[
 x^\alpha-x^{\epsilon}=\sum_j
  \left(\prod_{l<j}x_l^{\epsilon_l}\right)
  (x_j^{\alpha_j}-x_j^{\epsilon_j})
  \left(\prod_{l>j}x_l^{\alpha_l}\right),
 \quad \epsilon_l=\min(\alpha_l,1),
\]
and $x_j^a-x_j=(x_j^2-x_j)\sum_{r=0}^{a-2}x_j^r$ for $a\geq2$.
There are constantly many local monomials and coefficients of bounded size. Thus all $r_{i,\sigma,j}$ have constant-size integral circuits. Empty scopes give no correction.

Write $\mathrm{ML}$ for the unique Boolean multilinear remainder and put
\[
 Q_{i,j}=\sum_{\sigma\in\{0,1\}^{I_i}}
                       A_{i,\sigma}r_{i,\sigma,j}.
\]
The local identities imply
\[
 a_i^{(0)}f_i-\mathrm{ML}(a_i^{(0)}f_i)
              =\sum_{j\in I_i}Q_{i,j}(x)(x_j^2-x_j).
\]
The asserted remainder really is multilinear: its local factor is
$\sum_\sigma f_i(\sigma)e_\sigma$, with the corresponding coefficients $A_{i,\sigma}$ involving only the other variables. Its values are those of $a_i^{(0)}f_i$. Each $Q_{i,j}$ has degree at most $(v-t_i)+t_i=v$. Summing over $i$, the sum of the remainders is the unique multilinear polynomial whose Boolean values are all one, hence is identically one over $\mathbb Z$. Consequently
\[
 1=\sum_i a_i^{(0)}f_i-
             \sum_{j=1}^v\left(\sum_i Q_{i,j}\right)(x_j^2-x_j).
\]
Subtract the indicated $Q$ sum from the multiplier of each retained Boolean equation. This produces the promised integral $a_i$ and an ordinary identity in $\mathbb Z[x]$. Constantly many specializations and local products per equation, followed by $O(v)$ additions, keep the total circuit size and construction time within $S(v)$. In particular, no exponential multilinear expansion is being silently treated as a polynomial-time operation. The preliminary coefficient norm is bounded by $3^v$ in total, and the local correction introduces only a fixed factor per equation, so the resulting integer coefficients have $O(v+\log(v+1))$ bits; integrality is a property of the output polynomials, not of every rational circuit gate.

This construction can be made unconditional as an algorithm that either reports satisfiability or produces the certificate. Each local relation $f_i(b)=0$ is a constant-scope Boolean table, convertible to at most eight forbidden-assignment clauses. The resulting fixed-width CNF has the same $v$ variables and $O(v)$ clauses. E first decides it within its bounded-density running time, which is absorbed by $S(v)$. When it is satisfiable the algorithm reports that outcome; when it is not, the displayed construction applies. The circuit $C(x,z)=\sum_i a_i(x)z_i$ satisfies $C(x,0)=0$ and $C(x,f(x))=1$, exactly Definition1.1 of IPS, and is linear in the placeholders. Its actual polynomial degree is at most $v+1$. If a syntactic variable-degree bound is desired, retain homogeneous components $0,\ldots,v$ at every gate of each multiplier circuit: addition is componentwise and multiplication uses the truncated convolution. There is no variable division, so discarded higher components cannot contribute to a later lower component. Since the output degree is at most $v$, their sum is exactly the same multiplier. This uses $O(v^2 S(v))$ gates and no identity test, with syntactic degree at most $v$ when rational constants have variable-degree zero. It is not the different constant-free formal-degree convention in which constant leaves have degree one.

For the stronger sparse-CNF specialization, delete tautological clauses and repeated literals. An empty clause has the immediate certificate $1\cdot1=1$. Otherwise let $I_i$ be the distinct-variable scope of clause $i$, let $\alpha_i$ be its unique falsifying assignment, and set $g_i=e_{\alpha_i}(x_{I_i})$. Define
\[
 A_i(x_{\overline I_i})=
    \sum_{b\in\{0,1\}^{\overline I_i}}
       e_b(x_{\overline I_i})
       \prod_{j<i}\bigl(1-g_j(b,\alpha_i)\bigr).
\]
Upon multiplying by $g_i$, this is precisely the sum of the full idempotents $e_c(x)$ over assignments whose first violated clause is $i$. For an unsatisfiable CNF these sets partition the entire cube, so
\[
              \sum_i A_i g_i=\sum_c e_c
                   =\prod_{l=1}^n(x_l+(1-x_l))=1
\]
as an ordinary integral polynomial identity. In particular $\deg A_i\leq n-|I_i|$ and every product $A_i g_i$ has degree at most $n$. This is the classical identity of Grochow--Pitassi Lemma4.2, equations(4)--(6), specialized by fixing the falsifying local assignment. Its E consequence is as follows. Each $A_i$ is a partition function on $n-|I_i|$ summation bits, with at most $m+n$ factors of arity at most $k$. For fixed $k,C$ and $n>2k$, its variable count is at least $n/2$ and the factor density remains bounded. C016 therefore constructs all of them in size and time $S(n)$. Small $n$ is handled directly. No Boolean correction, auxiliary gate variable, or expansion in the original $n$ variables is required in this specialization. For dense CNFs this particular argument does not preserve the same original-$n$ bound; compiling into verifier gates changes the relevant parameter to their total number. NN-C036 subsequently supplies an original-$n$ integral circuit certificate for arbitrary-density fixed-width CNFs by slower disjoint sparsification, with its explicitly weaker exponent.

We next prove the asserted large-characteristic transfer, including a uniform denominator bound across every high-incidence branch. In a branch with $u$ remaining summation variables, E Lemma4.8 uses
\[
 \lambda=\lceil\log_2u\rceil,\quad
 \nu=\lceil\log_2\lambda\rceil,\quad
 Q=\left\lfloor\frac{\lambda}{128\nu}\right\rfloor,
\]
and every successful layout has $R<Q$. Since $u\leq v$, both $Q$ and $R$ are at most $B(v)$. The high-incidence branching introduces no new summation variables. For fixed density and arity, only finitely many input sizes fail the layout's numerical checks; direct expansion handles them using only integral constants. The branch sizes are $v-O(v/\sqrt{\log v})$, so this fallback affects only a fixed finite range and preserves the asymptotic bound. Thus the single localization
\[
                       A_v=\mathbb Z[1/B(v)!]
\]
works for every branch, preliminary multiplier and local correction. In the sparse-CNF specialization each summation dimension is at most $n$, so $A_n$ works uniformly there.

Here is why all arithmetic-circuit constants may be chosen in that localization. E Lemma4.6 gives the exact common denominator $(R-1)!Q!$ for every replacement row. Its prime divisors are at most $B(v)$, so these row coefficients lie in $A_v$. Taylor substitution and Boolean differences introduce only binomial integers and signs. Factor interpolation on the Boolean cube uses only zero, one and minus one. All subsequent sums and products therefore remain in $A_v$ until the final Hasse-Hermite interpolation.

That interpolation also needs only this localization. Let the multiplicity of each node be $J$ and put $M=QJ$. The evaluation-of-jets map is
\[
 A_v[T]\big/\!\left(\prod_{t=1}^{Q}(T-t)^J\right)
       \longrightarrow\prod_{t=1}^{Q} A_v[z]/(z^J),
 \qquad P\longmapsto(P(t+z))_{t=1}^{Q}.
\]
For two distinct nodes, their nonzero difference is an integer of absolute value less than $Q$, and is a unit in $A_v$. The corresponding linear ideals are comaximal, and so are their $J$th powers: expanding a relation $a+b=1$ to exponent $2J-1$ expresses one as a sum of an element of each power. The Chinese remainder theorem therefore makes this map an isomorphism. Monic division gives the free basis $1,T,\ldots,T^{M-1}$ on the left; the right uses the local powers $1,z,\ldots,z^{J-1}$. In these bases its matrix is exactly E's Hasse-Hermite matrix
\[
  \mathsf V_{(t,j),u}=\binom uj t^{u-j}\quad(u\geq j),
               \qquad \mathsf V_{(t,j),u}=0\quad(u<j).
\]
Its inverse thus has entries in $A_v$. Compute those final entries over $\mathbb Q$ as before and put them in the circuit as constants; intermediate elimination pivots are not circuit gates. Their polynomial bit-height bound is unchanged. This reasoning does not divide by $j!$ and imposes no bound $J<p$.

Consequently the C016 circuit is a circuit over $A_v$ for a polynomial with integer coefficients in its independent weights. Equality with that universal partition polynomial holds in $\mathbb Q[y]$, and hence in $A_v[y]$ by the injective inclusion into $\mathbb Q[y]$. For every prime $p>B(v)$ there is a homomorphism $A_v\to\mathbb F_p$. Apply it to every constant and gate: equality survives, and integer-weight specializations, local corrections and homogeneous-component constructions survive as well. The resulting output is exactly the reduction of each integral multiplier, not merely a polynomial agreeing with it on a finite set. Reducing polynomial-bit numerators and denominators and inverting their nonzero residues uses polynomial bit cost per constant in $v+\log p$. The compiled circuit uses only prime-field constants and is valid over every extension field of that characteristic. This proves the size and construction claims. No procedure choosing a prime, and no assertion for a fixed prime below the threshold, is hidden in the argument.

Finally apply the ordinary identity to the smooth cubic of NN-C027. Retain $x$ and define
\[
 z_i=y_i+a_i(x)(2t-t^2).
\]
On $X$, the scalar product $\sum_i f_i z_i$ equals
$(t^2-t)+(2t-t^2)=t$. Conversely, for free coordinates $(x,z)$ set
\[
 t=\sum_i f_i(x)z_i,
 \qquad y_i=z_i+a_i(x)(t^2-2t).
\]
Then $\sum_i f_i y_i=t+(t^2-2t)=t^2-t$, and direct substitution shows both composites are identities. These are integral polynomial maps over $\mathbb Z$. The first has degree at most $v+2$; the second has degree at most $v+6$, because $t$ has degree at most three. Shared circuit substitution adds only polynomially many gates to the multiplier circuits. This proves the effective geometric assertion. The rational syntax in this original proof describes integral polynomial maps; it is not a license to reduce a rational constant modulo a prime dividing its denominator. The later integral compilation in NN-C034 supplies a different circuit valid after arbitrary base change.''',
        'Complete construction of ordinary ideal multipliers, local correction, sparse-CNF specialization and integral affine trivialization; independent review pending.',
r'''This closes a specific algebraic-certificate gate left by NN-C009: for bounded-density local verifier systems, E yields actual ordinary ideal multipliers with subexponential rational arithmetic circuits. It strengthens the transcript conclusion of NN-C008 and makes NN-S016's empty-case affine trivialization effective in this circuit model. It gives neither polynomial-size certificates nor a polynomial-time verifier for arbitrary supplied IPS circuits; verification still presents polynomial identity tests. It therefore implies no $\mathrm{NP}=\mathrm{coNP}$ collapse and no VP=VNP conclusion. The exponential monomial-size polynomial-calculus lower bounds in NN-C021 remain compatible with these shared circuits. The denominator audit here gives circuits in every characteristic greater than $\max(2,\lceil\log_2 v\rceil)$. NN-C033 subsequently supplies a different construction over every prime field, including constant-free circuits of polynomial formal degree. Semantic integrality alone did not justify reducing the original rational constants at denominator primes. NN-C034 subsequently closes the integral-gate question over $\mathbb Z$ by cyclotomic interpolation and supplies constant-free circuits of polynomial formal degree.''',
r'''The algebraic-geometric theorem is constructive in the following precise representation. For the split Boolean coordinate algebra
\[
 B=\mathbb Z[x_1,\ldots,x_v]/(x_j^2-x_j)
                 \simeq\prod_{b\in\{0,1\}^v}\mathbb Z,
\]
let $Y=V(f_1,\ldots,f_h)$ be the closed subscheme cut out by the local verifier equations. If $Y$ is empty, E produces rational arithmetic circuits representing integral polynomials $a_i$ of degree at most $v$ whose ordinary ideal combination is one in $\mathbb Z[x]$. The first-violation construction partitions the component idempotents of $B$; the constant-scope division above lifts that partition to the ambient affine coordinate ring. It thereby constructs an integral polynomial isomorphism
\[
 V\left(t^2-t-\sum_i y_i f_i(x)\right)
        \longrightarrow\mathbb A^{v+h}_{\mathbb Z},
 \quad (x,y,t)\longmapsto(x,y+a(2t-t^2)),
\]
with the explicitly proved inverse and degree bounds. Its circuit description has the displayed $S(v)$ bound. Moreover that description is defined over the explicit open arithmetic base $\operatorname{Spec}\mathbb Z[1/B(v)!]$: the Hasse-jet Chinese-remainder isomorphism proves the interpolation denominators are invertible there. Thus the same effective presentation of the ideal identity and affine trivialization base-changes to every field of characteristic $p>B(v)$. The integral morphisms exist at all primes; only their claimed arithmetic-circuit presentation has this restricted base.

The symbolic preliminary multipliers are finite-algebra traces of products of local weights, so C016's trace construction and base change apply, with exact classical locator EGA IV4, printedp111,18.2.1--18.2.2 and equation18.2.1.2. The passage from quotient identities to ordinary ideal multipliers is proved here by local interpolation, without invoking an unproved effectivity theorem. In the sparse-CNF case, the classical first-violation partition already gives the ordinary identity without the Boolean equations. These are integral geometric statements with localized arithmetic-circuit presentations; no efficient circuit presentation at every prime, motivic equivalence theorem, or GCT representation-theoretic lower bound is inferred.''',
        inputs)
