#!/usr/bin/env python3
"""Readable source of the complexity working register and LaTeX fragment."""
import csv, json, pathlib
BASE=pathlib.Path(__file__).resolve().parent
findings=[]

def add(id, question_id, title, statement, inputs, proof, status, complexity_impact, geometry_translation, sources):
    findings.append(dict(id=id, question_id=question_id, title=title, statement=statement,
                         inputs=inputs, proof=proof, status=status,
                         complexity_impact=complexity_impact,
                         geometry_translation=geometry_translation, sources=sources))

E={'source':'E: The Exponential Time Hypothesis is False, supplied LaTeX',
   'path':'sources/LIT_OpenAI_ETH_is_False/'}
SGATRACE={'source':'SGA 7 II, Expose XXII', 'locator':'Theorem 3.1 (3.1.1); Corollary 3.2 (3.2.1)',
          'url':'https://grothendiecksga.com/read/sga7/fr/22-3.html',
          'access_note':'Verified text edition; no archive cote or scanned-manuscript claim.'}
ALGTRACE={'source':'EGA IV, fourth part, Publications Mathematiques IHES32 (1967)',
          'locator':'Printed p.111,18.2.1--18.2.2; base-change equation18.2.1.2; primary PDF page110 (zero-based109)',
          'url':'https://www.numdam.org/item/PMIHES_1967__32__5_0.pdf',
          'access_note':'Original NUMDAM scan downloaded and visually checked; full text on printed p.111 agrees with the locator. No Grothendieck archive cote asserted.',
          'evidence':'work/complexity/ega_trace_original_page.png; ega_trace_original_excerpt_with_frontmatter.pdf'}
SGAFINITE={'source':'SGA 4, Expose XVII','locator':'Theorem 6.2.3, trace in relative dimension zero',
           'url':'https://grothendiecksga.com/read/sga4/en/XVII-6.html'}
VV={'source':'Valiant--Vazirani, NP is as easy as detecting unique solutions, TCS 47 (1986), 85--93',
    'locator':'Theorem 1.1; Corollaries 3.1--3.4, especially Corollary 3.2 p.91',
    'url':'https://ics.uci.edu/~vazirani/ValVaz.pdf'}

add('NN-C001','NEG_NIGHT-01','Quasilinear sparse systems compress on their original variables',
r'''Fix integers $k,a,b\geq1$. Given $m\leq n\lceil\log_2 n\rceil^a$ polynomials $f_e\in\mathbb F_2[x_1,\ldots,x_n]$, each listed with at most $\lceil\log_2 n\rceil^b$ monomials of degree at most $k$, one can deterministically construct at most $6n$ linear combinations of the $f_e$ having precisely the same common zeros in $\mathbb F_2^n$. Each combination has polylogarithmically many monomials, of degree at most $k$. Construction and exact counting take
\[
 \operatorname{poly}_{k,a,b}(n+m)\,
 2^{O_{k,a,b}(n\log\log n/\sqrt{\log n})}
\]
bit operations and polynomial space. The construction introduces no auxiliary Boolean variables. This is preservation of the Boolean zero set, not equality of ideals in the unrestricted polynomial ring.''',
[dict(E,locator='Section 6, Lemmas 6.1--6.2; Appendix D Lemma D.2 (lem:tensor-sparse-query)')],
r'''Handle $m=0$ and bounded $n$ directly. Put $B=\max(1,\lceil m/n\rceil)$, $\mu=\lfloor\log_2m\rfloor+1$, $P=20000B^2\mu^2$ and $D_0=320000B^2\mu^3$. Apply E, Lemma 6.1, to construct $A^{(0)}$ with at most $3n$ rows and row weight at most $D_0$, such that every nonzero vector in its kernel has weight at least $m/P$. This lemma concerns arbitrary vectors of bits; it never uses the clause origin of those bits.

For $x\in\mathbb F_2^n$, set $v(x)=(f_1(x),\ldots,f_m(x))$. Write $S=\{x:v(x)=0\}$ and let $D(A)$ be the number of $x\notin S$ with $Av(x)=0$. The count returned by a common-zero query is $N(A)=|S|+D(A)$. At a stage, enumerate all $P$-tuples of pairs $(e,c)\in[m]\times\mathbb F_2$, interpreted as a row $h$ with repeated indices combined modulo two. Every false survivor has at least $m/P$ nonzero coordinates. A uniform tuple hits such a coordinate with probability at least $1-(1-1/P)^P>1/2$. Conditional on one hit, the independent coefficient of that occurrence makes $h\cdot v(x)$ a uniform bit, even if other occurrences repeat the same coordinate. Thus its rejection probability is at least $1/4$.

Consequently $\mathbb E_hD(A;h)\leq(3/4)D(A)$. Evaluate $N(A;h)$ for every tuple and append a minimizer. Since $|S|$ is the same for all candidates, this also minimizes $D$. After $3n$ rounds the false survivor count is at most $2^n(3/4)^{3n}=(27/32)^n<1$, and hence is zero. Every original zero survives every row, proving exact equality of the Boolean zero sets.

A tested system has at most $6n$ equations, degree at most $k$, and at most $\lceil\log_2n\rceil^b\max(P,D_0)$ monomials per equation. This is the interface of Lemma D.2 for one fixed constant depending only on $k,a,b$. There are at most $3n(2m)^P+1=\exp((\log n)^{O_{a,b}(1)})$ counter calls. Initial code construction has the same kind of overhead. Every fixed polylogarithm is $o(n\log\log n/\sqrt{\log n})$, so multiplying these costs gives the stated bound. Enumerate candidates sequentially, retaining only the current matrix, candidate, best candidate and counts; Lemma D.2 then preserves polynomial space.''',
'Proved from designated input E; self-check recorded; independent review pending.',
r'''Extends the linear-number-of-equations core to a quasilinear number of sparse equations while keeping the original witness parameter $n$. It supplies no polynomial-time hitting set: selection itself uses the expensive exact counter and depends on the particular map $v$. It does not preserve all zeros over extension fields and does not turn a signed circuit into a monotone circuit.''',
r'''In the Boolean coordinate algebra $B_n=\mathbb F_2[x]/(x_i^2-x_i)$, evaluation gives $B_n\cong\prod_{x\in\mathbb F_2^n}\mathbb F_2$. An ideal in this product is determined by the coordinates on which it vanishes. Hence the original and compressed equations do generate the same ideal after passage to $B_n$, and define the same finite reduced, finite etale zero-dimensional scheme. The resulting isomorphism and its count are computed without listing its possibly $2^n$ components. The trace dictionary is SGA7 II XXII Corollary 3.2; the relative finite trace is SGA4 XVII 6.2.3. There is no new reductive-group action or representation multiplicity attached by this compression.''',
[E,SGATRACE,SGAFINITE])

add('NN-C002','NEG_NIGHT-01','Fixed characteristic-two fields and exact preimage tasks',
r'''For every fixed $r,k,a,b$, NN-C001 extends to sparse systems over $\mathbb F_{2^r}$ in $n$ field variables, with $m\leq n(\log n)^a$ equations and at most $(\log n)^b$ monomials per equation. Counts, lexicographically first witnesses and exact uniform sampling from a nonempty zero set are available in $\operatorname{poly}(n)2^{O(n\log\log n/\sqrt{\log n})}$ time and polynomial space; the sampling time is expected. The same bounds apply to the fibers of a map with those coordinate-polynomial bounds.''',
[{'source':'NN-C001','locator':'full proof in this register'},dict(E,locator='Appendix D Lemma D.2; Theorem 1.1 for background self-reduction')],
r'''Fix once and for all an $\mathbb F_2$-basis of $K=\mathbb F_{2^r}$ and its multiplication table. Write each variable as $x_i=\sum_{j=1}^r x_{ij}b_j$. A monomial of degree at most $k$ expands in each coordinate as a sum of at most $r^k$ products of at most $k$ bits, with coefficients determined by this fixed multiplication table. Thus each equation gives $r$ equations in $N=rn$ bits, of degree at most $k$ and polylogarithmic sparsity; the number of equations remains at most $N(\log N)^{O(1)}$. This is a bijective coordinate encoding, so it is parsimonious. Apply NN-C001 and absorb the fixed factor $r$ in the asymptotic constants.

For witness search keep all $N$ declared bits. At stage $j$, add the equations fixing the already chosen prefix and test the count after setting the next bit to zero. If that count is positive choose zero; otherwise choose one. Provided the original count is positive, at least one branch is nonempty. At most $N$ further linear equations and $N+1$ counts are required, so the same bounds hold. For a fiber $F(x)=y$, subtract the fixed coordinate $y_e$ from each polynomial; this adds at most one monomial.

For exact sampling, let $A_0,A_1$ be the two child counts at a prefix. Draw an integer uniformly from $\{0,\ldots,A_0+A_1-1\}$ by rejection from $\lceil\log_2(A_0+A_1)\rceil$ random bits. Its expected number of trials is below two. Take branch zero precisely if the integer is below $A_0$. The probability of any full satisfying assignment telescopes to $1/|S|$. The largest counts have at most $N+1$ bits and only $O(N)$ queries are needed. When the count is zero the algorithm reports that sampling is unavailable. This proves the expected-time and space claims.''',
'Proved from NN-C001; exact field/running-time parameters stated.',
r'''The field degree $r$ is fixed. Letting $r$ grow changes both the Boolean witness count and the monomial expansion $r^k$. The proof uses characteristic two essentially: field coordinates are $\mathbb F_2$-linear. It is not a same-parameter theorem for sparse equations over arbitrary odd-characteristic fields. Search and sampling do not imply that an NP language has a polynomial-time unambiguous verifier.''',
r'''The field-coordinate construction is the elementary affine coordinate description of restriction of scalars for the finite separable extension $K/\mathbb F_2$, restricted to rational points. To obtain the finite counting scheme one also imposes $x_i^{2^r}-x_i=0$, or equivalently all bit relations $x_{ij}^2-x_{ij}=0$. Its coordinate algebra is a product indexed by the actual field-valued solutions. Counting is rank/trace; conditional sampling is repeated restriction to clopen subsets. No purity beyond the trivial weight-zero Frobenius representation on these rational components is required. SGA4 XVII 6.2.3 supplies the finite trace formalism; no claim of a canonical GCT representation is made.''',
[E,SGAFINITE,SGATRACE])

add('NN-C003','NEG_NIGHT-01','Exact rational weighted partition functions with controlled bit cost',
r'''Fix a finite alphabet size $q$, arity $w$ and density constant $C$. Given $n$ variables with $q$ states and at most $Cn$ explicitly tabulated rational factors, each depending on at most $w$ variables, their sum-product partition function is computable exactly in
\[
 \operatorname{poly}(L+n)\,
 2^{O_{q,w,C}(n(\log\log n)^2/\sqrt{\log n})}
\]
time and polynomial space, where $L$ includes every numerator and denominator bit. Signs and zero weights are allowed. The number of factors, rather than only the number of variables, is part of the hypothesis.''',
[dict(E,locator='Proposition 3.4; Lemmas 4.7--4.8; high-incidence branching in Section 5; Appendix B Lemma B.1 and its bit-height method')],
r'''Encode each $q$-state variable by $t=\lceil\log_2q\rceil$ bits and add a unary-in-the-state validity factor which is one on the $q$ chosen codes and zero on the other codes. Replace each local table by its multilinear interpolation polynomial on its at most $wt$ bits, using
\[
 \Phi(x)=\sum_{a\in\{0,1\}^{I}}\Phi(a)
 \prod_{i:a_i=1}x_i\prod_{i:a_i=0}(1-x_i).
\]
Here $t,w$ are fixed, so table sizes, polynomial degrees and scopes are bounded constants. Invalid encodings contribute zero and valid encodings correspond bijectively to assignments in the original alphabet. Let $N=tn$. The number of factors and total number of factor--variable incidences are $O(N)$, and the total product degree in independent incidence variables is $O(N)$.

If a bit belongs to more than $b_0=\max(1,\lceil M/N\rceil)\lceil\sqrt{\log_2N}\rceil$ scopes, branch on it. There are at most $M/b_0\leq N/\sqrt{\log_2N}$ such bits. Each branch has $N'=N-O(N/\sqrt{\log N})$, still $\Theta(N)$, and maximum incidence bounded by a fixed power of $\log N'$. Empty scopes are scalars. Add factors equal to one to declare any unused bits. Lemmas 4.7--4.8 supply a layout for Proposition 3.4. Its incidence degree is $O(N')$ and its coefficient algebra can be $\mathbb Q$. The resulting sum-product cost is $\operatorname{poly}(N)2^{O(N'(\log\log N')^2/\sqrt{\log N'})}$. Branching multiplies by $2^{O(N/\sqrt{\log N})}$ and hence does not change the displayed exponent.

For bit complexity, let $D_{\rm in}$ be the product of all positive table-entry denominators. Then $\log_2D_{\rm in}\leq L$, and every table coefficient has denominator dividing $D_{\rm in}$. Let $f=O(N)$ be the number of factors after validity and neutral factors are included, and let $w'$ be their fixed maximum bit arity. E Section 5, Proposition 5.3, and Appendix B use the explicit common denominator $d_{\rm den}=(R-1)!Q!$ for replacement-row coefficients. Taylor substitution introduces binomial integers but no additional denominators. Each evaluated factor therefore has denominator dividing $D_{\rm in}d_{\rm den}^{w'}$, and every group-product term and final sum can use the single denominator
\[
 \Omega=(D_{\rm in}d_{\rm den}^{w'})^f.
\]
Its bit length is at most $f(L+w'\log_2d_{\rm den})$, polynomial in $N+L$. After this common denominator is cleared, a term's numerator is a product of $O(fw')$ input and substitution coefficients, each with polynomial bit length in $N+L$. Summing the enumerated terms adds only the logarithm of their number to that bit bound, even if signs cancel.

For readout, Appendix B's Hermite matrix $\mathsf V$ has dimension $M_H=QJ=\operatorname{poly}(N)$ and entries $\binom uj t^{u-j}$, of $O(M_H\log(Q+2))$ bits. Multiplying the Taylor data by $\Omega$ makes them integral. Cramer's rule gives the requested constant term as $\det\mathsf V^{(0)}/(\Omega\det\mathsf V)$. An $h\times h$ minor with entry bit bound $B$ has bit length at most $hB+\log_2(h!)+O(1)$; this bounds all fraction-free elimination intermediates and gives polynomial bit cost. Unlike the unweighted integer application, the final answer here may remain rational, which is allowed. Each branch and its interpolation therefore use polynomial-bit arithmetic; sequential processing preserves polynomial space. The final denominator divides the product of the individual factor denominators and the output numerator also has polynomial bit length. No unit-cost assumption on large rational weights is used.''',
'Proved extension of E Proposition 3.4; uses its weaker exponent, not an unproved extension of D.1.',
r'''Gives signed or rational weighted CSP partition functions, bounded-arity spin models and bounded-density weighted model counting. Arbitrary weights of $B$ bits do not automatically fit D.1 with precision $P_0=O(n)$: a product can need $\Theta(nB)$ bits. This proof keeps that cost in the polynomial arithmetic overhead by using the rational-algebra routine and its weaker exponent. Dense instances with superlinear numbers of factors are not covered by this statement.''',
r'''For the finite split scheme $X=\operatorname{Spec}(\mathbb Q^{q^n})$, the product of local factors is an element $W\in\Gamma(X,\mathcal O_X)$, and its sum over assignments is the trace of multiplication by $W$ in that finite etale algebra. In the idempotent basis of this product algebra, multiplication by $W$ is diagonal with entries $W(x)$, so its trace is exactly the displayed sum. EGA IV4, printed p.111,18.2.1--18.2.2 is the original finite-algebra trace construction; equation18.2.1.2 states base-change compatibility. SGA4 XVII 6.2.3 provides the relative-dimension-zero trace formalism. This is a weighted endomorphism trace, not automatically a point count or a pure Frobenius trace: arbitrary rational or negative weights need not be eigenvalues of a geometric Frobenius with the desired weight. The natural basis is indexed by assignments; there is no promised short basis for the whole exponential-dimensional algebra.''',
[E,ALGTRACE,SGAFINITE])

add('NN-C005','NEG_NIGHT-03','Parity is a top Boolean coefficient, with a hard sparse quadratic boundary',
r'''For polynomials $f_1,\ldots,f_m\in\mathbb F_2[x_1,\ldots,x_n]$, let $N$ count their common zeros in $\mathbb F_2^n$ and let $\operatorname{ML}$ denote reduction modulo $(x_i^2-x_i)$. Then
\[
 N\bmod2=[x_1\cdots x_n]\operatorname{ML}\!\left(\prod_{i=1}^m(1+f_i)\right).
\]
If $\sum_i\deg f_i<n$, this parity is zero. Nevertheless computing this coefficient is $\oplus\mathrm P$-complete already for $m=O(n)$ quadratic equations with at most three monomials per equation. Exact counting on the same class is $\#\mathrm P$-complete under parsimonious polynomial-time reductions.''',
[{'source':'Elementary Boolean-coordinate-algebra calculation','locator':'full proof below'},
 {'source':'Katz, On a theorem of Ax, AJM 93 (1971), 485--499','locator':'Theorem 1.0 and definition 0.3',
  'url':'https://web.math.princeton.edu/~nmk/old/ax.pdf'},dict(E,locator='Appendix D Lemma D.2, algorithm for this hard class')],
r'''On each bit assignment, $\prod_i(1+f_i(x))$ equals one exactly at a common zero. For a squarefree monomial $x^S$, its sum over all bit assignments equals $2^{n-|S|}$, reduced modulo two. This is one for $S=[n]$ and zero otherwise. Summing the multilinear representative proves the coefficient identity. Reduction to squarefree monomials never increases degree, so the top coefficient vanishes when the displayed degree sum is below $n$.

For hardness, take an arbitrary polynomial-time Boolean witness verifier and compile it, on a fixed instance, into an AND/NOT circuit. Keep its $u$ witness-input bits and introduce one bit $z_g$ for each of its $s$ gates. Encode an AND gate by $z_g+ab=0$, a NOT gate by $z_g+a+1=0$, and acceptance by $z_{\rm out}+1=0$. Constants can be substituted directly. There are $N'=u+s$ variables and $s+1=O(N')$ equations, each of degree at most two and with at most three monomials. For every assignment to the witness bits, all gate bits are uniquely determined, in topological order. The equations have one extension if that witness accepts and none otherwise. This is a parsimonious reduction from every $\#\mathrm P$ verifier; taking parity proves the $\oplus\mathrm P$ claim. Membership follows by guessing the bit assignment and checking the equations.

This also explains why the low-degree divisibility theorem does not solve the general hard instances. Over $\mathbb F_q$, Katz's Theorem 1.0 states $q^\mu\mid N$ with $\mu=\max(0,\lceil(n-\sum_i d_i)/\max_i d_i\rceil)$ for nonconstant defining polynomials of degrees $d_i$. If $\mu=0$ it imposes no divisibility. Even when $\mu>0$, the congruence does not distinguish zero from a positive multiple of $q^\mu$. In the circuit encoding the sum of degrees generally meets or exceeds the number of variables. Adding all Boolean relations to make a finite scheme also destroys the small degree-sum hypothesis. E provides the stated subexponential algorithm for the hard class, not a polynomial coefficient-extraction algorithm.''',
'Identity and reduction proved in full; Katz divisibility used by exact classical locator.',
r'''Identifies the precise computational gate behind a mod-two cohomological count. Low individual degree and constant monomial sparsity do not make parity easy when the number of equations grows linearly. E changes the exponential running time, while $\oplus\mathrm P$-completeness remains valid.''',
r'''The Boolean quotient is the coordinate algebra of a finite split etale scheme. The coefficient functional above is its sum-of-evaluations trace over $\mathbb F_2$, expressed in the squarefree monomial basis. This basis has $2^n$ elements. Its finite scheme has weight-zero Frobenius but the trace modulo two is still $\oplus\mathrm P$-complete from a succinct equation presentation. SGA7 II XXII Corollary 3.2 gives exactly the coherent trace congruence, with properness satisfied for this finite scheme. It gives no polynomial algorithm for constructing an explicit cohomology basis.''',
[E,SGATRACE,ALGTRACE])

add('NN-C006','NEG_NIGHT-03','The effective Frobenius-data gate and the correct affine boundary',
r'''Suppose a deterministic polynomial-time procedure, on every sparse quadratic system in NN-C005, outputs polynomially many explicitly represented $\mathbb F_2$ matrices of polynomial total dimension whose alternating trace equals the number of common bit zeros modulo two. Then $\mathrm P=\oplus\mathrm P$ and $\mathrm{NP}=\mathrm{RP}$. If it instead outputs the exact integer rank/count in polynomial time, then $\mathrm{FP}=\#\mathrm P$ and $\mathrm{PH}=\mathrm P$. The mere existence of finite coherent or etale cohomology is insufficient. For a nonproper affine scheme, use a proper compactification and its boundary, or compactly supported etale cohomology, rather than the ordinary affine coherent $H^0$.''',
[{'source':'NN-C005','locator':'parsimonious sparse-quadratic reduction'},VV,
 {'source':'Toda, PP is as Hard as the Polynomial-Time Hierarchy, SIAM J. Comput. 20 (1991), 865--877',
  'locator':'main theorem PH subset P^PP; publisher abstract verified, internal numbering not claimed',
  'url':'https://epubs.siam.org/doi/10.1137/0220053'},SGATRACE,
 {'source':'SGA 5, Expose III','locator':'equation 6.13.2; Theorem 6.13.3',
  'url':'https://grothendiecksga.com/read/sga5/en/III-6.html'}],
r'''The trace of an explicit matrix is the sum of its diagonal entries. Therefore the assumed construction followed by polynomially many field operations decides the parity problem in polynomial time. By NN-C005 every language in $\oplus\mathrm P$ reduces to that problem in polynomial time, yielding $\oplus\mathrm P\subseteq\mathrm P$; the reverse containment is immediate. Valiant--Vazirani's one-sided randomized isolation reduction maps an unsatisfiable formula only to unsatisfiable formulas and maps a satisfiable formula to a uniquely satisfiable formula with inverse-polynomial probability. A parity oracle always rejects the former and accepts the latter. Polynomial amplification gives SAT in RP. Since RP is contained in NP and SAT is NP-complete, NP=RP.

For the integer version, the parsimonious reduction makes all $\#\mathrm P$ functions polynomial-time computable; all polynomial-time nonnegative polynomial-output-length functions can also be counted by choosing a binary integer below their value, so the standard functional equality follows. A PP comparison is then polynomial-time computable. Toda's main theorem puts PH in $\mathrm P^{\mathrm{PP}}$, which now equals P. This integer conclusion is stronger than the parity conclusion and must not be inferred from a single residue.

The classical trace expressions are mathematically valid without any efficiency claim. For the finite Boolean solution scheme, $H^0(\mathcal O)$ is $\mathbb F_2^N$, all higher coherent cohomology vanishes, and Frobenius acts as the identity. That matrix can have exponential dimension. An arbitrary affine scheme does not satisfy the proper coherent formula: for example $H^0(\mathbb A^1,\mathcal O)=\mathbb F_q[x]$ is infinite-dimensional. If $U\subseteq\overline U$ is an open immersion into a proper finite-type scheme and $D=(\overline U\setminus U)_{\rm red}$, then $|U(\mathbb F_q)|=|\overline U(\mathbb F_q)|-|D(\mathbb F_q)|$. Applying SGA7 XXII Corollary 3.2 to both proper schemes gives the correct difference of coherent traces modulo $p$. Alternatively SGA5 III 6.13.3 supplies the compact-support $\mathbb F_p$ etale trace formula. Neither operation supplies polynomial-size matrices or an algorithm to construct them.''',
'Conditional gate proved; classical trace hypotheses audited; no unconditional complexity collapse claimed.',
r'''Separates purity/existence from effective presentation. A, M and a Boolean support object do not by themselves provide the hypothesized matrix construction. The parity reduction would derandomize an NP decision only to RP through Valiant--Vazirani; claiming NP=P at this point would require an additional deterministic isolation gate.''',
r'''The dictionary is literal: solution set to finite etale scheme, count to rank, parity to coherent Frobenius trace, and affine restriction to proper object minus boundary. On the representation side $H^0$ is a direct sum of trivial Frobenius representations indexed by solutions. Weight zero controls eigenvalue magnitude but not the cost of extracting the number of summands from equations. SGA7 II XXII 3.1--3.2 and SGA5 III 6.13 are the exact locators; no Grothendieck archive document is invented.''',
[SGATRACE,VV,ALGTRACE])

add('NN-C007','NEG_NIGHT-03','Exact deterministic-isolation gates and why logspace isolation does not transfer automatically',
r'''A polynomial-time computable polynomial-length list of witness restrictions, each forbidding all witnesses on no-instances and containing an odd number of witnesses for at least one list member on each yes-instance, would imply $\mathrm{NP}\subseteq\oplus\mathrm P$. If all these parity tests were in P it would imply NP=P. A single polynomial-time restriction that always has at most one witness and preserves nonemptiness would imply NP=UP. E supplies such a single isolating restriction only at its subexponential running time. Hoza's short seed generator does not give the required polynomial-size list for arbitrary NP computations.''',
[VV,{'source':'Hoza, NL = UL, ECCC TR26-323, supplied PDF','locator':'Theorems 1.1 and 1.3; Definition 1.2; Section 1.2'},
 dict(E,locator='Theorem 1.1 and Appendix D Lemma D.2, conditional-count self-reduction')],
r'''Let the list have $t=t(|x|)$ members with witness counts $a_1,\ldots,a_t$. In $\mathbb F_2$ the OR of their parities is
\[
 1+\prod_{i=1}^t(1+a_i).
\]
This expression is a $\#\mathrm P$ count modulo two: a nondeterministic machine has one distinguished accepting branch, and on the other branch independently chooses, for each $i$, either one dummy option or an accepting witness for restriction $i$. It accepts exactly the valid tuples. There are $1+\prod_i(1+a_i)$ accepting paths, and the total nondeterministic witness length is polynomial. On no-instances every $a_i=0$, so the parity is zero; on yes-instances some $a_i$ is odd, so the parity is one. This proves the $\oplus\mathrm P$ inclusion. If each list parity is deterministically computable in polynomial time, ordinary OR decides the NP language in P.

For the single-restriction assertion, guess its restricted witness and check it. The global promise of at most one witness makes this an unambiguous polynomial-time verifier, and preservation of nonemptiness gives the original language. Hence every NP language lies in UP; the reverse inclusion is definitional. A list with some uniquely satisfiable member is not enough for this argument: other members can accept and there is no supplied unambiguous way to select the first good member. The parity-list argument does not cure that uniqueness problem.

E counts under added unit equations. Repeatedly count the zero branch of the next prefix bit, choosing a nonempty branch, until one satisfying assignment remains. At most $n$ count queries and $n$ unit constraints suffice; an unsatisfiable input can be sent to a fixed inconsistent restriction. The construction thus preserves nonemptiness and yields at most one witness, but its time is E's subexponential bound, not polynomial.

Hoza's Theorem 1.3 gives a seed length $O(\log(wn))$ for width-$w$, length-$n$ layered graphs, hence a polynomial-size seed list when the graph has polynomial width and length. An NP verifier can have a configuration width $2^{\operatorname{poly}(N)}$ on inputs of length $N$. For that graph the seed bound is polynomial in $N$, allowing exponentially many seeds. The min-isolation test also uses the specific Reinhardt--Allender unambiguous reachability machinery cited in Hoza Section 1.2; it is not a generic polynomial-time test that an arbitrary NP witness restriction is unique. These two parameter/interface gaps prevent the proposed automatic NP transfer.''',
'Conditional implications and E self-reduction proved; Hoza parameter gate audited.',
r'''Makes the desired NP analogues concrete and reviewable. Randomized Valiant--Vazirani plus efficient parity yields NP=RP; deterministic polynomial-list odd isolation yields NP subset parity-P; globally unique deterministic isolation yields NP=UP. These are different conclusions with different extra hypotheses.''',
r'''A restriction cuts a finite Boolean solution scheme by additional equations, equivalently selects a clopen collection of its rational components. Odd isolation asks that one selected finite scheme have odd degree; unique isolation asks for degree at most one. The finite trace of SGA4 XVII 6.2.3 records these degrees. A weight function's unique minimum is a combinatorial selection on this set, not a consequence of Frobenius purity. In the representation dictionary, direct sums encode alternative restrictions and tensor products encode simultaneous witness choices; the displayed parity OR uses their mod-two rank arithmetic.''',
[VV,SGAFINITE,E])

add('NN-C008','NEG_NIGHT-06','Subexponential computation-transcript proofs, without a natural-system size claim',
r'''There exists a Cook--Reckhow propositional proof system in which an unsatisfiable fixed-width $k$-CNF with $n$ variables and $m$ clauses has a refutation of length $\operatorname{poly}_k(n+m)2^{O_k(n\log\log n/\sqrt{\log n})}$; at fixed clause density the sharper exponent $O(n/\sqrt{\log n})$ applies. Every tautological Boolean formula of size $L$ has a proof in this system of length $\operatorname{poly}(L)2^{O(L/\sqrt{\log L})}$. Analogous computation certificates certify emptiness of the sparse systems of NN-C001.''',
[dict(E,locator='Theorem 1.1, including polynomial space and fixed-density bound'),
 {'source':'Cook--Reckhow proof-system definition','locator':'Polynomial-time decidable proof relation, constructed explicitly below'}],
r'''Fix E's deterministic exact counting machine, including a standard binary implementation of its arithmetic, and encode each complete configuration by a polynomial number of bits in the input length. A certificate for a CNF consists of its full computation transcript ending with count zero. Check that the first configuration is the prescribed start configuration, every successive pair obeys the fixed local transition relation, and the final output is zero. Verification is polynomial in the transcript length. Soundness follows from determinism and correctness of E: an accepted transcript is its actual computation and a zero count means unsatisfiability. Completeness follows by recording that computation for an unsatisfiable formula. If the run has $T$ steps and space $S$, the transcript length is $O(TS)$ up to encoding overhead. Since $S$ is polynomial, this has the asserted size.

To obtain a proof system for all tautologies, an input proof additionally contains a formula $\varphi$ and the canonical Tseitin encoding of a circuit for $\neg\varphi$, with the output forced to one. For a size-$L$ formula this has $O(L)$ variables and $O(L)$ clauses of width at most three. Local gate constraints have a unique extension for every assignment to the original variables, so the CNF is unsatisfiable exactly when $\varphi$ is a tautology. The verifier checks this deterministic encoding and an E transcript for it. Fixed-density Theorem 1.1 gives $2^{O(L/\sqrt{\log L})}$ up to polynomial factors. On invalid proof strings the Cook--Reckhow output-function version returns a fixed tautology, so its range is exactly TAUT. Replacing E's CNF solver by NN-C001 similarly gives polynomially checkable computation certificates of sparse-system emptiness.''',
'Proved existence of an algorithm-dependent proof system; no claim about resolution, PC, Frege or IPS.',
r'''The proofs are superpolynomial in general, so this does not imply NP=coNP. The verification procedure checks a Turing computation; it supplies no bound on width, degree, monomial count or size in a pre-existing algebraic or propositional proof system.''',
r'''Unsatisfiability is emptiness of the finite Boolean solution scheme. A computation transcript certifies this from its equations; it is not automatically an effective Nullstellensatz identity or a short free resolution of its coordinate algebra. In the finite etale model, emptiness means rank zero and zero $H^0$, while SGA7 II XXII 3.2 only identifies a residue of that rank. E computes the integer rank through its own algorithm, not through a claimed small cohomological presentation.''',
[E,SGATRACE])

add('NN-C009','NEG_NIGHT-06','Small semantic quotient certificates do not supply short polynomial-calculus proofs',
r'''Every unsatisfiable Boolean polynomial system has a small shared-circuit identity proving $1$ belongs to its generated ideal in the Boolean function algebra. However checking that identity modulo the Boolean ideal is coNP-hard, even when the defining equations are the sparse quadratics in NN-C005. E does not supply a polynomial bound for ordinary Nullstellensatz or polynomial-calculus certificates.''',
[{'source':'NN-C005','locator':'Boolean quotient and parsimonious gate encoding'},dict(E,locator='Theorem 1.1 / Lemma D.2 for the algorithmic distinction')],
r'''In characteristic two put $g_i=\prod_{j<i}(1+f_j)$. A telescoping product gives the formal polynomial identity
\[
 \sum_{i=1}^m f_i g_i=1+\prod_{i=1}^m(1+f_i).
\]
If there is no common bit zero, the product on the right vanishes at every Boolean assignment and is zero in $B_n=\mathbb F_2[x]/(x_i^2-x_i)$. Thus $\sum_i f_i g_i=1$ in $B_n$. All prefix products can share intermediate gates, so the collection of the $g_i$ and the displayed sum has size linear in the total supplied circuit size plus $m$.

This compact expression is not a polynomial-time checkable proof of the crucial vanishing assertion. Given any Boolean verifier circuit, construct the equations of NN-C005 and their product $P=\prod_i(1+f_i)$. The circuit for $P$ has polynomial size. It represents the zero element of $B_n$ if and only if the original verifier has no accepting input. Therefore deterministic polynomial-time verification of these semantic quotient identities would decide UNSAT in P, and hence P=NP. The construction itself does not solve that check.

In the ordinary polynomial ring, an actual Nullstellensatz certificate requires additional polynomials $h_j$ satisfying
\[
 1=\sum_i f_i g_i+\sum_{j=1}^n h_j(x)(x_j^2-x_j).
\]
The vanishing product is indeed in the Boolean ideal because $B_n$ is the algebra of all Boolean functions, but the above small circuit expression has not constructed small $h_j$ or a small derivation of membership. Expansion or multilinear reduction can involve exponentially many monomials. A transcript of E as in NN-C008 is a valid algorithmic certificate; changing its proof system to polynomial calculus, resolution or an ideal-proof system requires an additional simulation theorem with quantitative bounds. NN-C029 subsequently supplies subexponential ordinary ideal multipliers over $\mathbb Q$ for bounded-density local verifier systems by a different construction. NN-C033 supplies the fixed-characteristic circuit transfer, and NN-C034 constructs integral constant-free certificates valid after every base change. None of these gives polynomial-size multipliers or a subexponential ordinary monomial-PC simulation; NN-C021 and NN-C034 instead exhibit an exponential ratio between monomial-PC and circuit-IPS size on the same family.''',
'Explicit identity and verification hardness proved; later NN-C029--NN-C034 supply ordinary circuit certificates while retaining the distinction from monomial polynomial calculus.',
r'''Blocks the inference that detecting or removing supported arithmetic zeros automatically produces short algebraic refutations. It identifies the missing effective ideal-membership/derivation gate, without claiming an impossibility result for every potential simulation of E.''',
r'''The quotient $B_n$ is the coordinate algebra of a finite split scheme; its idempotent decomposition makes semantic ideal membership transparent after all components are listed. The telescoping identity is an ideal-theoretic statement on that finite scheme. Producing polynomial-ring correction terms is a presentation problem, analogous to replacing an abstract zero object by an explicit exact complex. Rank or Frobenius-trace identities in SGA7 XXII do not control those presentation sizes. The translation is algebraic; no unproved categorical purity theorem is used.''',
[E,SGATRACE])

add('NN-C004','NEG_NIGHT-01','Fixed algebraic tensor alphabets and exact quantum amplitudes',
r'''Fix a finite set $\Omega$ of algebraic numbers and a constant maximum tensor arity. A tensor network with $s$ Boolean wires and entries from $\Omega$ has an exact deterministic contraction algorithm in $\operatorname{poly}(s+L)2^{O_\Omega(s/\sqrt{\log s})}$ time and polynomial space. Consequently a $q$-qubit, $g$-gate circuit from any fixed bounded-arity algebraic gate set has each specified computational-basis amplitude computable exactly in $\operatorname{poly}(q+g)2^{O((q+g)/\sqrt{\log(q+g)})}$ time and polynomial space. A fixed field representation and complex embedding specify the exact output.''',
[dict(E,locator='Appendix D Theorem D.1, coefficient ring and precision hypotheses; its equality-tree and bipartite subdivision encoding'),
 {'source':'J.S. Milne, Fields and Galois Theory, v5.10 (2022)','locator':'Theorem5.1, pp.61--62, primitive element theorem','url':'https://www.jmilne.org/math/CourseNotes/FT.pdf'}],
r'''Enlarge the fixed alphabet by its complex conjugates if probabilities will be requested, and let $K$ be the resulting fixed number field. By Milne Theorem5.1 choose a primitive element $\beta$ for $K$. If $a_dT^d+\cdots+a_0$ is an integer polynomial annihilating $\beta$ with $a_d\ne0$, then $\alpha=a_d\beta$ is integral: multiply the relation by $a_d^{d-1}$ to obtain a monic integer equation for $\alpha$. It still generates $K$. Its degree $d$ is constant. There is a fixed positive integer $c$ such that every $\omega\in\Omega$ can be written
\[
 \omega=c^{-1}\sum_{j=0}^{d-1}a_{\omega,j}\alpha^j,
 \qquad a_{\omega,j}\in\mathbb Z.
\]
Remove isolated tensors, multiplying their entries separately at the end. The remaining number of vertices $v$ is at most $2s$. Introduce a formal variable $V$ and replace each tensor entry by its integer polynomial $\sum_j a_{\omega,j}V^j$. The contraction is an integer polynomial $H(V)$ of degree at most $(d-1)v$. If $A=\max(1,\max_\omega\sum_j|a_{\omega,j}|)$, then
\[
 \|H\|_1\leq 2^s A^v.
\]
Thus choose $\ell>(d-1)v$ and $P_0$ with $2^{P_0-1}>2^sA^v$; both are $O_\Omega(s)$. Reduction modulo $V^\ell$ loses no coefficient, and reduction modulo $2^{P_0}$ permits unique signed-integer recovery of every coefficient.

Subdivide every edge with an equality tensor to make the graph bipartite. Its wire count changes by a factor two, its maximum degree stays bounded and it has $O(s)$ nonisolated vertices. Its local entries are computable in polynomial time in the required ring $(\mathbb Z/2^{P_0}\mathbb Z)[V]/(V^\ell)$. All hypotheses of D.1 hold after increasing its fixed constant $C$. Recover $H$ coefficientwise, evaluate $H(\alpha)/c^v$, reduce to the fixed basis of $K$, and multiply the removed scalar tensors. This last arithmetic has polynomial output height and polynomial cost in the full description length.

For the quantum specialization, insert each gate as its input/output tensor and each fixed initial or final basis state as a unary tensor. A bounded-arity circuit has $O(q+g)$ wire segments: the sum of numbers of incidences at gates is $O(g)$, and each qubit contributes its initial segment. The tensor contraction is the path-sum formula for the specified amplitude. Apply the preceding result. A probability for a fixed outcome is obtained by multiplying the exact amplitude by its complex conjugate in the fixed field, with polynomial extra work.''',
'Proved from E D.1 with explicit precision and algebraic-height bounds.',
r'''This is a subexponential algorithm in total circuit size $q+g$, not an efficient simulation in the input-qubit parameter for arbitrary polynomial-size circuits. It gives no BQP=P consequence. The fixed finite algebraic alphabet is essential to the stated exponent: variable coefficient heights or growing number-field degree require separate accounting. The result concerns numerical contraction, not a small symbolic arithmetic circuit for all tensor entries.''',
r'''The contraction is composition of evaluation/coevaluation pairings in finite-dimensional $K$-vector spaces, and can also be written as the finite-algebra trace of a diagonal weighted assignment operator as in NN-C003. The diagonal matrix calculation in NN-C003 supplies that algebraic trace dictionary directly; SGA4 XVII 6.2.3 is the verified finite-trace comparison. The temporary $V$ is a coefficient-encoding device; it is not a Frobenius coordinate, deformation of a motive, or canonical-basis parameter. Fixed algebraicity ensures exact arithmetic but does not imply purity or a representation-theoretic obstruction.''',
[E,ALGTRACE,SGAFINITE])

BUR={'source':'Burgisser, Completeness and Reduction in Algebraic Complexity Theory, Springer 2000, Chapter 4',
     'locator':'Theorem 4.5(A), Corollary 4.6(1), pp.64--65; Theorem 4.12 and Remark 4.17, pp.71--75; Theorem 4.18 and Corollary 4.19, p.76; proof of 4.5(A3), pp.77--78',
     'url':'https://link.springer.com/chapter/10.1007/978-3-662-04179-6_4',
     'text_url':'https://www.scribd.com/document/1064260688/B-Completeness-and-Reduction-in-Algebraic-Complexity-Theory-Burgisser',
     'access_note':'Exact monograph numbering audited in reproduced primary text; do not identify these numbers with those of the TCS article.'}
add('NN-C010','NEG_NIGHT-09','Burgisser transfer: the exact Dedekind family and the one-way conclusion',
r'''The characteristic-zero Cook--Valiant transfer needs RH for Dedekind zeta functions of the bounded-degree, bounded-height number fields furnishing algebraic solutions to the constant-replacement systems in its proof. These fields are generally arbitrary number fields, not necessarily abelian or normal. Conditional on M, the needed RH is available, and Burgisser's transfer gives
\[
 \mathrm{VP}_{\mathbb C}=\mathrm{VNP}_{\mathbb C}
 \ \Longrightarrow\ \#\mathrm P/\mathrm{poly}=\mathrm{FP}/\mathrm{poly},
\]
with the stronger Boolean-part and nonuniform-collapse conclusions at the cited classical locators. Its contrapositive is a Boolean nonuniform counting lower bound implying an algebraic separation. A suffices for the restricted proof route when those witness fields can be chosen abelian with the same quantitative bounds; no supplied theorem establishes that restriction in general. No converse transfer is supplied.''',
[BUR,
 {'source':'A: supplied Alpoge Lean archive','locator':'DirichletLNonvanishingRightOfHalf; DirichletLZerosOnLine; LFunction_ne_zero_of_half_lt_re; LFunction_eq_zero_re; Remark p.4 step20'},
 {'source':'M: Masullo claimed general Hecke GRH','locator':'Thm12.5.1.1 pp.519--520; Thm13.3.1.1 p.522; all uses conditional on M'},
 {'source':'Prior CX register','locator':'CX-K01--CX-K03: analogous Koiran witness-field audit, used as background only'}],
r'''The classical proof to be imported is Burgisser, Chapter 4, proof of Theorem 4.5(A3), with Theorem 4.12 and the root-modulo-primes estimate of Corollary 4.19. It replaces arbitrary circuit constants by variables and imposes agreement on all Boolean inputs. A bounded algebraic solution is represented in one number field $K=\mathbb Q(\alpha)$. The prime-ideal theorem used in Section 4.6 assumes RH for $\zeta_K$; degree-one prime ideals yield roots modulo rational primes. The proof does not pass to a Galois closure. The constants of one sufficiently large finite-field specialization become polynomial-length nonuniform advice. Theorem 4.5(A) and Corollary 4.6(1) state the resulting transfer and collapse. These are exact classical proof locators, rather than an asserted new proof of that theorem.

For the new premise audit, if $K/\mathbb Q$ is finite abelian, its Dedekind zeta function is a product of the corresponding primitive Dirichlet $L$-functions. A therefore gives its RH. If $K$ is arbitrary, the trivial Hecke character of $K$ has $L$-function $\zeta_K$, so M supplies precisely the missing input, conditional on M. Neither statement requires holomorphy of a nontrivial Artin $L$-function. The existence of algebraic solutions alone does not make their fields abelian: for example $X^3-2=0$ has roots generating non-Galois cubic fields; none is contained in an abelian extension of $\mathbb Q$, since every subextension of an abelian Galois extension is Galois. This example illustrates the field-class gap, not a proof that any logically possible consequence of A cannot cover it.

Finally take the contrapositive of the displayed implication. E's supplied lower bound concerns near-linear circuits for a language in $\mathrm E^{\mathrm{NP}}$. It is not a superpolynomial lower bound for the Boolean functions computing $\#\mathrm P$ values, and hence does not instantiate the antecedent. Uniform $\mathrm P\ne\mathrm{NP}$ alone also does not state a nonuniform counting lower bound. Conversely, an algebraic separation does not reverse an implication whose antecedent is algebraic equality. Thus the combination closes the analytic premise only under M (or a separately proved abelian-witness promise), leaving the Boolean lower-bound gate intact.''',
'Classical transfer by exact locator; field-family audit proved; general characteristic-zero use conditional on M.',
r'''Use function notation $\#\mathrm P\not\subseteq\mathrm{FP}/\mathrm{poly}$, or explicitly encode output bits as Boolean functions, rather than silently writing a counting class as a decision class. Under the same classical hypothesis, Corollary 4.6(1) also gives $\mathrm{NC}^3/\mathrm{poly}=\mathrm P/\mathrm{poly}=\mathrm{NP}/\mathrm{poly}=\mathrm{PH}/\mathrm{poly}$ and a uniform second-level collapse of PH if VP=VNP. These do not assert VP=VNP, and E does not choose an alternative.''',
r'''The constant-replacement equations define an affine scheme over $\mathbb Z$. A closed point of its characteristic-zero fiber supplies $\operatorname{Spec}K$; reductions with residue degree one give rational points over finite fields. Its finite permutation representation has Dedekind zeta function $\zeta_K$. The relevant trace counts prime-ideal splitting, not satisfying assignments. The elementary matrix trace of multiplication supplies the finite-algebra language, and Burgisser Section 4.6 supplies the exact arithmetic estimate. A covers abelian character decompositions; the general field need not admit a decomposition into Dirichlet characters. This is the same type of analytic field gate as Koiran, but the output here is nonuniform circuit simulation.''',
[BUR,ALGTRACE])

add('NN-C011','NEG_NIGHT-07','Inversion and collision attacks for sparse low-degree maps',
r'''Fix $r,k,a,b$. Let $F_n:\mathbb F_{2^r}^n\to\mathbb F_{2^r}^{m(n)}$ have $m(n)\leq n(\log n)^a$ explicitly given coordinate polynomials of degree at most $k$ and sparsity at most $(\log n)^b$. There is a deterministic $2^{O(n\log\log n/\sqrt{\log n})}\operatorname{poly}(n)$ algorithm that inverts every image point. The same bound finds a collision whenever one exists, and counts ordered unequal colliding pairs. Thus these maps cannot have $2^{\Omega(n)}$ inversion or collision security against all algorithms in a security parameter proportional to $n$. This does not rule out ordinary polynomial-time one-wayness.''',
[{'source':'NN-C001--NN-C002','locator':'quasilinear sparse-system counting and search'},
 dict(E,locator='Appendix C Corollary C.2 is the previously known constant-locality special case, not newly claimed here')],
r'''For inversion solve the equations $F_{n,e}(x)-y_e=0$. The parameter bounds and exact preimage search are those of NN-C002. The algorithm succeeds for every $y$ in the image, so in particular its success probability is one when $y$ is sampled as $F_n(x)$ under any distribution on $x$.

For collisions introduce two input vectors $x,x'$, giving $2n$ field variables, and impose $F_{n,e}(x)-F_{n,e}(x')=0$. The coordinate degree remains at most $k$ and sparsity at most twice the original bound. After conversion to the fixed binary basis there are $2rn$ bits. Partition the unequal pairs according to the first bit position $j$ where the binary encodings differ. In branch $j$, add linear equations $x_i+x'_i=0$ for $i<j$ and $x_j+x'_j+1=0$. These at most $rn$ equations preserve the quasilinear equation bound. Every unequal pair belongs to exactly one branch. Count each branch with NN-C001 and sum to obtain the ordered unequal-pair count; search any nonempty branch for a collision. There are only $rn$ branches and replacing $n$ by $2rn$ changes the exponent by a fixed factor. If the field-output length is smaller than the field-input length, a collision exists by the pigeonhole principle; otherwise the algorithm can correctly report none.

For every fixed $c>0$, the algorithm's exponent divided by $n$ tends to zero, so its running time is eventually below $2^{cn}$. This contradicts a claimed lower bound against every algorithm at that exponential security scale, including an average-case claim requiring negligible attack success, because the inversion attack succeeds on every image. A security parameter with an unrelated scaling must be substituted explicitly. A subexponential algorithm is still superpolynomial, so the standard definition of a one-way function, which excludes only polynomial-time adversaries, is not contradicted.''',
'Proved attack consequence for the stated representation and parameter; no blanket claim about deployed cryptosystems.',
r'''Extends E's constant-locality inversion corollary to polylogarithmic monomial sparsity and a quasilinear output length, and adds a direct collision-counting construction. Dense multivariate quadratics with $\Theta(n^2)$ monomials per coordinate are outside this theorem. A generic polynomial-size Boolean circuit encoding has $n+s$ variables and can lose subexponentiality in the intended security parameter; the input representation is part of the result.''',
r'''An inversion fiber is a rational-point fiber of the polynomial map $F_n$. Collisions are rational points of its fiber product with itself, with the diagonal removed; the first-differing-bit decomposition is a disjoint clopen stratification of this finite Boolean scheme. Counts are degrees of those finite etale pieces, with trace formalism SGA4 XVII 6.2.3. This construction supplies an algorithm for the succinct fibers, not a theorem that GRH or purity makes arbitrary fibers easy.''',
[E,SGAFINITE,SGATRACE])

CGGM={'source':'Chukhin--Gajulapalli--Golovnev--Mihajlin, A Little Derandomization Goes a Long Way, ECCC TR26-313, 5 Nov 2026',
      'locator':'Theorem 1 p.5; Theorem 1.1 and definition of NSUBEXP p.3; Theorem 8.8 and proof of Theorem 1 pp.46--47',
      'url':'https://eccc.weizmann.ac.il/report/2026/313/download/',
      'access_note':'Primary preprint statements and cited proof route audited; no independent proof validation of the complete new preprint claimed.'}
add('NN-C012','NEG_NIGHT-02','PIT transfer fails at both the identity interface and the time quantifiers',
r'''E's Boolean sparse-system algorithm does not, through the stated reductions, satisfy the Kabanets--Impagliazzo formal-PIT hypothesis. First, vanishing on the Boolean cube differs from polynomial identity. Second, $2^{O(N\log\log N/\sqrt{\log N})}$ is a mildly subexponential bound, not the stronger $\mathrm{NSUBEXP}=\bigcap_{\epsilon>0}\mathrm{NTIME}(2^{N^\epsilon})$ bound used by the cited PIT transfer. Third, general circuit encodings charge their gates in the witness variable count. A current independent unconditional arithmetic/Boolean lower-bound disjunction remains a disjunction and does not close these gates.''',
[dict(E,locator='Appendix D Lemma D.2; Corollary 1.4 and Appendix C Corollary C.1'),
 {'source':'Kabanets--Impagliazzo, Derandomizing Polynomial Identity Tests Means Proving Circuit Lower Bounds, Computational Complexity 13 (2004), 1--46',
  'locator':'Main theorem as stated on author research page; refined statement at CGGM26 Theorem 1.1',
  'url':'https://www.cs.sfu.ca/~kabanets/Research/poly.html'},CGGM],
r'''The nonzero polynomial $x^2-x$ is zero on both Boolean inputs. Thus any procedure whose only assertion is whether a circuit or polynomial vanishes on the Boolean cube cannot serve as formal PIT. Over a finite field one can instead evaluate in a sufficiently large extension field, but then a reduction must encode that extension and every arithmetic gate; the constant-degree sparse-polynomial interface is not an automatic encoding of an arbitrary formal circuit.

The time issue is independent. Set $g(N)=N\log\log N/\sqrt{\log N}$. For every fixed $0<\epsilon<1$,
\[
 \frac{g(N)}{N^\epsilon}
 =N^{1-\epsilon}\frac{\log\log N}{\sqrt{\log N}}\longrightarrow\infty.
\]
Therefore the upper bound supplied by E cannot be replaced by $2^{N^\epsilon}$ for every $\epsilon>0$. This is a statement about what the known bound guarantees, not a lower bound against possible future faster algorithms. Even a linear reduction into E's interface would not supply the required NSUBEXP guarantee.

For circuit encodings, an $n$-input circuit with $s$ gates has the parsimonious sparse quadratic encoding in $n+s$ variables from NN-C005. Taking $s=n^d$ gives a bound exponential in approximately $n^d/\sqrt{\log n}$, not the all-polynomial-circuit-size $2^n/\operatorname{poly}(n)$ type saving required by standard stronger SAT-to-lower-bound transfers. The already supplied E circuit corollary is valid at its own exact near-linear scale; it cannot be promoted by dropping $s$.

For current-source completeness, CGGM26 Theorem 1 states the unconditional alternative $\mathrm{NE}\not\subseteq\mathrm{SIZE}[2^n/(2n)]$ or $\mathrm{VP}_{\mathbb Z}^{0}\ne\mathrm{VNP}_{\mathbb Z}^{0}$. This theorem is independent of E and A. It does not select the algebraic alternative, and its constant-free formal-degree-bounded classes must not be silently replaced by ordinary $\mathrm{VP}_{\mathbb C}$ and $\mathrm{VNP}_{\mathbb C}$. Its precise quantitative PIT gates are useful further research targets, but E has not met them here.''',
'Explicit counterexample and asymptotic/interface audit proved; no formal independence claim.',
r'''Prevents conflating ETH-style $2^{o(n)}$ savings with the stronger SUBEXP quantifier, and numerical Boolean evaluation with symbolic arithmetic identity. No PRG, hitting set or BPP=P conclusion follows from the supplied E circuit lower bound alone. CGGM26 supplies an up-to-date background disjunction, not a new consequence counted as ours.''',
r'''Formal identity asks whether a regular function is zero in an affine coordinate ring. Boolean testing asks whether its restriction to the finite reduced subscheme cut out by $x_i^2-x_i$ is zero. The restriction map has a nonzero kernel, as the example shows. A trace on the finite subscheme forgets still more data. Finite-algebra matrix traces and the SGA7 XXII trace statement therefore do not identify formal PIT with Boolean zero testing. On the representation side, one must retain the polynomial family and its arithmetic circuit model; the finite evaluation representation is only a quotient.''',
[E,ALGTRACE,SGATRACE,CGGM])

add('NN-C013','NEG_NIGHT-01','Full energy histograms and sharper Hamming-weight enumerators',
r'''Fix $k,w,C,d$. Let $F$ be any $k$-CNF on $n$ declared variables. Suppose an energy $E(x)$ is the sum of at most $Cn$ explicitly tabulated nonnegative integer local costs, each on at most $w$ bits, with total possible range at most $M\leq n^d$. The entire polynomial
\[
 Z_F(T)=\sum_{x:F(x)=1}T^{E(x)}
\]
is computable coefficientwise in $\operatorname{poly}(n+m+M)2^{O(n(\log\log n)^2/\sqrt{\log n})}$ time and polynomial space. Hence minimum/maximum feasible energy and the numbers of optimizers are computable within that bound. For Hamming weight $E(x)=\sum_i x_i$, a separate linear-size addition-tree encoding improves the exponent to $O(n\log\log n/\sqrt{\log n})$. In particular, the full independence polynomial of an arbitrary graph has that sharper bound in its number of vertices.''',
[dict(E,locator='Proposition 3.4; Lemmas 4.7--4.8, 5.1--5.2, 6.1--6.3; Appendix B; Theorem 1.1'),
 {'source':'NN-C001','locator':'compression preserves the full solution set, not merely its cardinality'}],
r'''Apply E's disjoint sparsification lemma with a rational parameter of reciprocal polylogarithmic size, for example $\sigma=1/\lceil\sqrt{\log_2n}\rceil$. For fixed $k$, the leaves have $n(\log n)^{O_k(1)}$ clauses on the original variables, their satisfying sets partition that of $F$, and their number is at most a polynomial times $2^{\sigma n}$. Compress each leaf as in NN-C001. The final equations $P_i=0$ have count $a=O(n)$, fixed degree and polylogarithmic sparsity, and their Boolean zero set is exactly that leaf's satisfying set.

Set $\ell=n+1$ and work in the finite-dimensional commutative $\mathbb Q$-algebra
\[
 \mathcal A=\mathbb Q[V,T]/(V^\ell,T^{M+1}).
\]
For each $P_i$ use the parity-lift factor from E Lemmas 5.1--5.2,
\[
 B_i(x,V)=\sum_{j<\ell}e_j(L_i(x))\,[L_i(x)(L_i(x)-1)]^jV^j,
\]
where $L_i$ is its integer monomial lift. For a local cost table $c_h$ insert the multilinear interpolation factor $W_h(x,T)$ whose value on a bit assignment is exactly $T^{c_h(x)}$. Its input-variable degree is at most $w$, regardless of the exponent of $T$. The product of parity factors has incidence degree at most $k(a+2(\ell-1))=O(n)$ after the global $V$ truncation, and the cost factors add at most $wCn=O(n)$ incidence degree. If $M_{\rm inc}$ is the total scope size, then $M_{\rm inc}=n(\log n)^{O(1)}$. Set
\[
 b_0=\max\{1,\lceil M_{\rm inc}/n\rceil\}\lceil\sqrt{\log_2n}\rceil.
\]
Branch on all variables whose incidence exceeds $b_0$. There are at most $M_{\rm inc}/b_0\leq n/\sqrt{\log_2 n}$ such variables, and the remaining incidence is polylogarithmic. Lemmas 4.7--4.8 and Proposition 3.4 then evaluate the sum of the full product in the asserted weaker-exponent time.

After evaluating on Boolean assignments, apply the coefficient-sum map in $V$ only. This map is used after multiplication and is not treated as a ring homomorphism. Every dropped term of $V$-order at least $\ell$ is divisible by $2^\ell$ at integer arguments. Consequently the resulting integer polynomial in $T$ is coefficientwise congruent modulo $2^\ell$ to the leaf energy enumerator. Each genuine coefficient is between zero and $2^n$, so the least nonnegative residues recover it exactly. The $T$ truncation loses nothing because the sum of the local maximum energies is at most $M$. The algebra dimension is $(n+1)(M+1)$, polynomial in the stated parameters. E's rational height argument applies coordinatewise: only polynomially many bits are needed, and algebra operations have polynomial overhead. Process leaves and branches sequentially, adding their recovered coefficient arrays. Disjointness proves the final polynomial is exactly $Z_F$ and keeps every final coefficient at most $2^n$.

For the sharper Hamming specialization, form a balanced tree adding the $n$ one-bit inputs. At level $j$ there are $O(n/2^j)$ additions of $O(j)$-bit integers, using $O(j)$ Boolean gates per addition. The total gate count is $O(n\sum_{j\geq1}j/2^j)=O(n)$. Equality of the final binary sum to a chosen $h\in\{0,\ldots,n\}$ uses $O(\log n)$ further gates. Its Tseitin clauses have a unique extension for every original assignment and introduce $O(n)$ variables. Conjoin these clauses with $F$, obtaining fixed width $\max(k,3)$ and $O(n)$ variables, even when $F$ is dense. E Theorem 1.1 computes the coefficient of $T^h$ with the sharper general-density exponent. Repeat for $n+1$ values of $h$. For a graph use $F=\bigwedge_{uv\in E}(\neg x_u\vee\neg x_v)$; the coefficient counts independent sets of each cardinality. The polynomial input prefactor includes the edge list.''',
'Proved coefficient-algebra extension; Hamming specialization separately sharpened by a parsimonious linear-size circuit.',
r'''Gives complete polynomial-size distributions and exact optimization, not only a single unweighted count. Polynomially bounded total energy and $O(n)$ bounded-scope cost tables are essential. Arbitrarily many cost factors or exponentially many output coefficients fall outside the bound. The independence polynomial can be evaluated at any supplied rational activity with polynomial extra bit cost; this uses its $n+1$ coefficients and does not assert a general arbitrary-weight shortcut for dense CSPs.''',
r'''On the finite Boolean solution scheme, the energy partitions the rational components into clopen subsets $X_j$. The enumerator is $\sum_j\operatorname{rank}H^0(X_j,\mathcal O)T^j$, equivalently the character of the graded vector space with one basis vector per solution in its energy degree. The finite-algebra trace is immediate in the component idempotent basis; SGA4 XVII 6.2.3 supplies the verified finite-trace formalism. The variable $T$ records this chosen grading; it does not turn $T^j$ into a Tate twist or a geometric Frobenius eigenvalue without a separate realization. Thus the result produces an effective graded rank computation but no plethysm multiplicity formula or GCT obstruction.''',
[E,ALGTRACE,SGAFINITE])

add('NN-C014','NEG_NIGHT-02','Two unconditional limits on universal hitting-set interpretations of E',
r'''A set $H\subseteq\mathbb F_2^n$ meeting the nonempty zero set of every system of $n$ sparse linear Boolean equations must equal the entire cube. Also, a fixed $a\times m$ binary matrix with $a<m$ cannot preserve the Boolean zero set of every $m$-tuple of sparse linear polynomials by replacing $f$ with $Af$. Therefore E's small collection of parity checks is necessarily instance dependent; its theorem is not a universal subexponential assignment hitting set or a universal rank-deficient linear sketch of violations.''',
[{'source':'Elementary singleton and kernel arguments','locator':'complete proof below'},
 dict(E,locator='Section 6, Lemmas 6.1--6.2, instance-dependent greedy completion')],
r'''For each $b=(b_1,\ldots,b_n)\in\mathbb F_2^n$, take the $n$ equations $x_i+b_i=0$. Their common zero set is exactly $\{b\}$, and each equation has degree one and at most two monomials. If $H$ meets every such nonempty set then $b\in H$ for every $b$, so $H=\mathbb F_2^n$. This is an information-theoretic obstruction to the specified point-query hitting-set model; it says nothing against algorithms that manipulate the supplied equations.

For the second assertion, let $A$ have fewer rows than columns. Choose a nonzero vector $z\in\ker A$. For $n\geq1$ set $f_i(x)=z_i x_1$. Every $f_i$ has degree at most one and at most one monomial. The original system vanishes exactly on $x_1=0$, since some $z_i=1$. Yet $Af(x)=(Az)x_1=0$ identically, so the compressed system accepts the whole cube. Thus no such fixed matrix preserves zero sets for all instances. Equivalently a universal linear sketch separating every possible nonzero violation vector must have trivial kernel and at least $m$ rows.

E's Lemma 6.1 is consistent with this obstruction: its universal initial checks exclude only vectors of small support. Lemma 6.2 then selects additional checks using the particular image $\{f(x):x\in\mathbb F_2^n\}$ and exact survivor counts. The completed matrix only needs its kernel to avoid the nonzero vectors in that image. NN-C001 retains precisely this dependence and computational cost.''',
'Proved structural limitation; independent review pending for this newly added row.',
r'''Separates E's conditional-expectation construction from a black-box SAT hitting set and from formal PIT hitting sets. A uniform efficient constructor depending on the instance is a different question; no P versus NP lower bound is inferred from the two elementary impossibility statements.''',
r'''Each singleton system defines one rational reduced point, a proper finite etale scheme of degree one. A universal set of evaluation points must meet every such closed subscheme of the Boolean scheme, forcing every component to occur. In its coordinate algebra $\mathbb F_2^{2^n}$, these are the primitive coordinate idempotents. The sketch counterexample changes the ideal and doubles the selected clopen locus. Finite trace and degree are as in SGA4 XVII 6.2.3; weight-zero purity does not remove the need to retain each possible component in a universal evaluation set.''',
[E,SGAFINITE])

add('NN-C015','NEG_NIGHT-09','The constant-free model removes the analytic constant-elimination gate',
r'''For constant-free integer arithmetic circuits with polynomial size and polynomial formal degree, the implication
\[
 \mathrm{VP}_{\mathbb Z}^{0}=\mathrm{VNP}_{\mathbb Z}^{0}
 \quad\Longrightarrow\quad \#\mathrm P\subseteq\mathrm{FP}/\mathrm{poly}
\]
holds without A or M. Thus the arbitrary-constant characteristic-zero transfer in NN-C010 and the constant-free alternative of CGGM26 have different analytic requirements. A separation for these constant-free classes does not itself establish $\mathrm{VP}_{\mathbb C}\ne\mathrm{VNP}_{\mathbb C}$. This is a classical model refinement, with a direct proof supplied here, not a claimed new theorem from E.''',
[{'source':'Definitions of VP^0_Z and VNP^0_Z','locator':'CGGM26 p.5: constant-free circuits of polynomial size and formal degree'},
 dict(CGGM,locator='Proposition 8.1 p.40, coefficient-norm bound; Theorem 1 p.5'),
 BUR],
r'''Let $R(x,w)$ be any polynomial-time witness verifier defining a $\#\mathrm P$ function. For each input length, build a polynomial-size AND/NOT verifier circuit and introduce a Boolean variable for each gate. Over $\mathbb Z$, the gate-validity indicator for $z=ab$ is
\[
 zab+(1-z)(1-ab),
\]
and that for $z=1-a$ is $z(1-a)+(1-z)a$. Each is a constant-free bounded-degree polynomial, equal to one exactly when the corresponding Boolean gate is correct. Multiply all these indicators and the output bit. The resulting polynomial $Q(x,w,z)$ has a constant-free circuit of polynomial size and formal degree. For each $x,w$ there is exactly one consistent assignment to the gate variables, and its product is one precisely when $R(x,w)$ accepts. Hence $\sum_{w,z\in\{0,1\}^{\operatorname{poly}(n)}}Q(x,w,z)$ belongs to $\mathrm{VNP}_{\mathbb Z}^{0}$ and equals the desired count on Boolean $x$.

Assume equality of the two constant-free classes. Its counting polynomial has a constant-free arithmetic circuit with $s=\operatorname{poly}(n)$ gates and formal degree $d=\operatorname{poly}(n)$. Here constants have formal degree one, multiplication adds formal degrees, and addition or subtraction takes their maximum. Write $\|P\|_1$ for the sum of absolute coefficient values. A direct induction in topological gate order gives $\|P_g\|_1\leq2^{t d_g}$ at gate number $t$: addition increases the larger norm by at most a factor two, while multiplication multiplies the two bounds and adds formal degrees. The leaves $0,1,-1$ and variables satisfy the base case. Thus every used gate has coefficient norm at most $2^{sd}$. At Boolean inputs its integer value has at most $sd+O(1)$ bits. Ordinary integer addition and schoolbook multiplication evaluate the whole circuit in polynomial time. The circuit description is polynomial-length advice, proving the functional containment.

The formal-degree restriction matters for this characteristic-zero height argument: repeatedly squaring the constant two produces $2^{2^s}$ from $O(s)$ gates despite ordinary polynomial degree zero. Its formal degree grows exponentially and is excluded from that argument. NN-C020 gives a different modular simulation of bounded integer outputs which does not require this restriction. Finally, constant-free polynomial-formal-degree circuits form a more restrictive model than arithmetic circuits with arbitrary complex constants. Hardness against the former does not imply hardness against the latter. The proof above uses explicit integer arithmetic and never chooses a prime or a residue-field specialization, so it has no hidden GRH assumption.''',
'Classical model refinement proved directly; independent review pending.',
r'''Explains the restricted transfer underlying the current unconditional win--win. It does not convert E's near-linear $\mathrm E^{\mathrm{NP}}$ lower bound into the required nonuniform counting lower bound. It also does not supply a converse from ordinary algebraic separation to Boolean separation.''',
r'''The verifier product gives a finite Boolean scheme together with its acceptance idempotent; summing the idempotent is the finite-algebra trace. Over $\mathbb Z$, the supplied integer presentation and formal-degree bound make all intermediate coefficients effectively bounded. The trace dictionary follows directly by using the component idempotent basis, as in NN-C003; compare SGA4 XVII 6.2.3. By contrast NN-C010 starts with arbitrary complex constants, whose replacement by finite-field data uses number-field points and Dedekind zeta estimates. These are different effective presentations of related rank/count constructions, not different purity statements.''',
[CGGM,ALGTRACE,SGAFINITE,BUR])

add('NN-C016','NEG_NIGHT-04','A genuine symbolic transfer for bounded-arity partition polynomials',
r'''Fix arity $w$ and factor density $C$. For a factor hypergraph with $n$ Boolean variables and $m\leq Cn$ factors of scope at most $w$, attach an independent formal weight $y_{f,a}$ to every local assignment $a$ of factor $f$. Its full partition polynomial
\[
 Z_H(y)=\sum_{x\in\{0,1\}^n}\prod_f y_{f,x|I_f}
\]
has a deterministically constructible arithmetic circuit over $\mathbb Q$ of size
\[
 \operatorname{poly}(n)\,2^{O_{w,C}(n(\log\log n)^2/\sqrt{\log n})}.
\]
The rational constants have polynomial bit length. In particular the symbolic perfect-matching polynomial of a graph of bounded maximum degree has subexponential arithmetic circuit size in its vertex/edge parameter. This is a restricted symbolic consequence of E's full common routine; it is stronger than what follows merely by regarding E as a numerical SAT counter.''',
[dict(E,locator='Proposition 3.4, especially algebra-operation count and rational Hermite interpolation; Lemmas 4.7--4.8; Section 3.1 product interface and measurement-separation proof')],
r'''Use the coefficient algebra $\mathcal A=\mathbb Q[y_{f,a}]$. For each factor take its Boolean multilinear interpolation
\[
 \Phi_f(x_{I_f})=\sum_{a\in\{0,1\}^{I_f}}y_{f,a}
       \prod_{i:a_i=1}x_i\prod_{i:a_i=0}(1-x_i).
\]
It is linear in the formal weights and has degree at most $w$ in its Boolean inputs. The sum-product is exactly $Z_H(y)$, and its independent-incidence input degree is at most $wm=O(n)$. The number of incidences is also $O(n)$. Branch on variables of incidence above $\max(1,\lceil M_{\rm inc}/n\rceil)\lceil\sqrt{\log_2n}\rceil$, as in NN-C003, and retain the original scopes even if a substitution makes some coefficient zero. There are at most $n/\sqrt{\log_2n}$ branched bits and every resulting layout satisfies Lemmas 4.7--4.8.

Proposition 3.4 explicitly allows every commutative $\mathbb Q$-algebra, counts polynomially many operations in that algebra per enumerated vector, and permits final interpolation by the inverse of a rational Hermite matrix. Implement an algebra element as a pointer to a gate in a shared arithmetic directed acyclic graph. Each addition, subtraction or multiplication in $\mathcal A$ creates one arithmetic gate; truncated Taylor arrays have polynomial length and require polynomially many such gates per operation. Factor evaluation takes $O(2^w)$ times a polynomial number of algebra operations because $w$ is fixed. For interpolation compute the inverse matrix over $\mathbb Q$ once and use its entries as rational constants, followed by linear combinations of the symbolic Taylor data. Do not run fraction-free elimination with symbolic pivot entries: no division by an element involving $y$ is needed.

All control choices are independent of symbolic coefficients. The layout construction uses only the scopes. The measurement-separation scans select representatives by their integer measurements and fixed input bits, not by comparing values in $\mathcal A$. Branching fixes declared Boolean variables and does not ask whether a symbolic factor is zero. Therefore the complete computation can be unrolled into a circuit without a symbolic identity oracle. Proposition 3.4 and Lemma 4.8 bound the number of operations by the displayed exponential times a polynomial, including all high-incidence branches. Layout and Hermite constants have polynomial bit length by E's row-coefficient and Appendix B bounds. Circuit construction time is polynomial in its output size; storing algebra elements as gate references avoids expansion into monomials. The output polynomial has degree $m$ in the weights, even though it may have exponentially many monomials.

For a bounded-degree graph, put one bit $x_e$ on each edge. At every vertex insert the fixed-arity indicator that exactly one incident edge is selected. On each edge insert the unary factor $(1-x_e)+y_e x_e$. The product is zero off perfect matchings and equals $\prod_{e\in M}y_e$ on a perfect matching. With maximum degree fixed, the number of bits, factors and incidences is $O(v+e)$; isolated vertices immediately give the zero polynomial when they must be matched. Thus this is a specialization of the partition construction, preserving circuit size. In the bipartite case it is the permanent polynomial with the graph's forbidden entries set to zero.''',
'Proved symbolic extension from E Proposition 3.4; independent review pending.',
r'''This corrects an overly broad counting-only objection in this restricted setting. It does not give a polynomial-size circuit or VP=VNP. A dense $r\times r$ permanent encoded by edge bits has $\Theta(r^2)$ Boolean variables, so substituting that size into the result gives no useful subexponential bound in $r$ (and is worse than the usual $2^{O(r)}$ upper bound). Compression through parity lifts does not automatically preserve this characteristic-zero symbolic argument: coefficientwise reduction modulo a power of two is not an arithmetic-circuit operation over $\mathbb Q$. This original construction uses rational constants. NN-C033 subsequently proves a modified construction over every prime field, and NN-C034 gives integral constant-free circuits of polynomial formal degree over Z itself. These are strengthened constructions; the original rational circuit is not simply reduced modulo a denominator prime.''',
r'''The partition polynomial is the trace of multiplication by $\prod_f\Phi_f$ on the finite free algebra $\mathbb Q[y][x]/(x_i^2-x_i)$ over the parameter scheme $\operatorname{Spec}\mathbb Q[y]$. In the orthogonal idempotent basis indexed by bit assignments, this multiplication matrix is diagonal with the corresponding factor products on the diagonal. Its trace is their sum. Applying a coefficient-ring homomorphism entrywise commutes with summing the diagonal, proving the claimed base-change compatibility directly. The original EGA IV4, printed p.111,18.2.1--18.2.2 records this trace, with base change in equation18.2.1.2; compare the relative-dimension-zero formalism in SGA4 XVII 6.2.3. Specializing formal weights commutes with the trace and with the constructed arithmetic circuit. This is an actual family-level symbolic computation, unlike a single numerical rank. It still does not provide orbit-closure multiplicity obstructions, border lower bounds, or a finite Weil realization of nonstandard canonical bases.''',
[E,ALGTRACE,SGAFINITE])

from c017_draft import append_c017
append_c017(add,E,SGATRACE,SGAFINITE)
from c018_draft import append_c018
append_c018(add,E,SGATRACE,SGAFINITE)
from c019_draft import append_c019
append_c019(add,E,SGAFINITE)
from c020_draft import append_c020
append_c020(add,ALGTRACE,BUR)
from c021_draft import append_c021
append_c021(add,E,SGATRACE)
from c022_draft import append_c022
append_c022(add,E,SGAFINITE,ALGTRACE)
from c023_draft import append_c023
append_c023(add,E,SGATRACE,VV)
from c024_draft import append_c024
append_c024(add,E,SGATRACE,VV)
from c025_draft import append_c025
append_c025(add,E,SGAFINITE,ALGTRACE,VV)
from c026_draft import append_c026
append_c026(add,E,SGATRACE,VV)
from c027_draft import append_c027
append_c027(add,E,VV)
from c028_draft import append_c028
append_c028(add,E)
from c029_draft import append_c029
append_c029(add,E,ALGTRACE)
from c030_draft import append_c030
append_c030(add,E,SGATRACE,VV)
from c031_draft import append_c031
append_c031(add,E,SGATRACE,VV)
from c032_draft import append_c032
append_c032(add,E,SGATRACE,VV)
from c033_draft import append_c033
append_c033(add,E,ALGTRACE)
from c034_draft import append_c034
append_c034(add,E,ALGTRACE)
from c035_draft import append_c035
append_c035(add,E,ALGTRACE)
from c036_draft import append_c036
append_c036(add,E,ALGTRACE)

def tex_escape(s):
    escapes={'\\':r'\textbackslash{}','&':r'\&','%':r'\%','$':r'\$',
             '#':r'\#','_':r'\_','{':r'\{','}':r'\}',
             '~':r'\textasciitilde{}','^':r'\textasciicircum{}'}
    return ''.join(escapes.get(c,c) for c in s)

def write_outputs():
    findings.sort(key=lambda x:x['id'])
    independently_read={f'NN-C{i:03d}' for i in range(1,37)}
    for f in findings:
        if f['id'] in independently_read:
            f['status']=f['status'].replace('; independent review pending for this newly added row','').replace('; independent review pending','')
            f['status']=f['status'].replace('; independent review of the added repair pending','')
            f['status']=f['status'].replace('; self-check recorded; independent review pending','; self-check recorded')
            f['status']=f['status'].rstrip('.')+'. Independent complete deduction-proof review by root: passed; imported input theorems are not claimed independently proved.'
        f['check_status']={'self':'complete deduction-level proof reading; finite examples where recorded',
                           'independent':'Root reported full deduction-proof review passed; source-interface review separately recorded' if f['id'] in independently_read else 'pending',
                           'formal_verification':'not performed'}
    (BASE/'consequences.json').write_text(json.dumps(findings,indent=2,ensure_ascii=False)+'\n')
    rows=[]
    for f in findings:
        rows.append([f['id'],f['question_id'],f['title'],f['status'],
                     f['check_status']['independent'],
                     'See consequences.json and chapter.tex; exact inputs attached'])
    with (BASE/'QUESTIONS.tsv').open('w',newline='') as out:
        w=csv.writer(out,delimiter='\t');w.writerow(['finding_id','question_id','question','status','verification','next_step']);w.writerows(rows)
    head=r'''% Standalone fragment: requires amsmath, amssymb, amsthm, hyperref.
% Uses only standard theorem/proof environments. No custom mathematical macros.
\section{Complexity consequences and effective gates}
\label{sec:nn-complexity}
E and A are designated input theorems. Every use of M is conditional.
The preceding CX catalogue is background; its ETH refutations and Koiran rows
are not counted again. A proof marked below is a proof of the stated deduction
from those inputs, not an independent verification of the full input theorem.

'''
    chunks=[head]
    for f in findings:
        chunks.append(r'\subsection{'+tex_escape(f["id"]+' --- '+f['title'])+'}\n')
        chunks.append(r'\begin{proposition}['+tex_escape(f['id'])+']\n'+f['statement']+'\n'+r'\end{proposition}'+'\n')
        chunks.append(r'\paragraph{Exact inputs.}'+'\n')
        for x in f['inputs']:
            chunks.append(tex_escape(x.get('source',''))+'. '+tex_escape(x.get('locator',''))+'.\n\n')
        chunks.append(r'\begin{proof}'+'\n'+f['proof']+'\n'+r'\end{proof}'+'\n')
        chunks.append(r'\paragraph{Status and complexity impact.}'+'\n'+tex_escape(f['status'])+' '+f['complexity_impact']+'\n\n')
        chunks.append(r'\paragraph{Geometric and representation dictionary.}'+'\n'+f['geometry_translation']+'\n\n')
    (BASE/'chapter.tex').write_text(''.join(chunks))
    src={}
    for f in findings:
        for s in f['sources']+f['inputs']:
            key=(s.get('source',''),s.get('locator',''))
            src[key]=s
    (BASE/'SOURCE_LOCATORS.json').write_text(json.dumps(list(src.values()),indent=2,ensure_ascii=False)+'\n')
    print(f'Wrote {len(findings)} findings, chapter.tex, QUESTIONS.tsv and SOURCE_LOCATORS.json')

if __name__=='__main__': write_outputs()
