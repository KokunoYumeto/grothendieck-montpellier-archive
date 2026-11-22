"""NN-C022: original-seed rather than verifier-size cryptographic bounds."""

def append_c022(add,E,SGAFINITE,ALGTRACE):
    goldreich={'source':'Goldreich, Candidate One-Way Functions Based on Expander Graphs, 2011 revision of ECCC TR00-090',
               'locator':'Section2, equation(1), printedp.78; Section2.2, equation(2), printedp.79; fixed versus logarithmic locality explicitly distinguished in Section2',
               'url':'https://www.wisdom.weizmann.ac.il/~oded/PDF/ow-cand.pdf',
               'access_note':'The present consequence applies to fixed locality, and to the separately stated fixed-degree sparse algebraic variant; it does not silently treat the revision\'s logarithmic-locality random predicates as fixed width.'}
    add('NN-C022','NEG_NIGHT-07',
        'Local-map inversion and image distinguishing retain the original seed parameter',
r'''Fix $k$. Let $F:\{0,1\}^n\to\{0,1\}^m$ be specified by a list of output scopes of size at most $k$ and their Boolean truth tables. For every target $y$, the number $|F^{-1}(y)|$, image membership, an inverse when one exists, and exact uniform sampling from a nonempty fiber are computable in
\[
 \operatorname{poly}_k(n+m)\,
 2^{O_k(n\log\log n/\sqrt{\log n})}
\]
time and polynomial space; sampling has this expected-time bound. If $m\leq Cn$, replace the exponent by $O_{k,C}(n/\sqrt{\log n})$. The number of output coordinates may be polynomially larger than $n$ in the first bound.

When $m>n$, these algorithms give a deterministic distinguisher for $F(U_n)$ against $U_m$, with advantage at least $1-2^{n-m}$ and the same time bound. Thus fixed-locality maps with polynomial output length cannot have $2^{\Omega(n)}$ inversion security or pseudorandom-generator security. This conclusion concerns the original seed length and does not assume expansion, random scopes, injectivity, or regular fibers.''',
        [dict(E,locator='Theorem1.1, arbitrary-density and bounded-density counting bounds'),
         {'source':'NN-C002','locator':'prefix-count self-reduction and exact conditional sampling proof'},
         {'source':'NN-C001','locator':'quasilinear fixed-degree polylog-sparse systems, for the logarithmic-locality extension'},goldreich],
r'''For each output coordinate $i$, enumerate the at most $2^k$ assignments $a$ to its scope $I_i$ for which $F_i(a)\ne y_i$. Exclude each one by the single clause
\[
 C_{i,a}=\bigvee_{j\in I_i}
 \begin{cases}x_j,&a_j=0,\\ \neg x_j,&a_j=1.\end{cases}
\]
This clause is false precisely on the forbidden local assignment. The conjunction $\Phi_y$ has exactly $n$ original variables, at most $2^k m$ clauses, and width at most $k$. Constant false coordinates give an immediate empty fiber; constant true constraints may be omitted. E applies with fixed width $\max(2,k)$. The satisfying assignments of $\Phi_y$ are exactly $F^{-1}(y)$, with no auxiliary gate variables or multiplicities. This proves the displayed counting bounds.

To find an inverse, keep the same $n$ declared variables and repeatedly count after fixing the next bit to zero, choosing that branch when its count is positive. There are at most $n$ extra unit clauses and $n+1$ counting calls. The bounded-density hypothesis remains bounded density when $m=O(n)$. Exact sampling uses the two child counts as probabilities; binary rejection sampling of a uniform integer below their sum has expected fewer than two trials. The proof in NN-C002 applies verbatim, including polynomial space. A nonempty fiber is inverted with certainty, for every target in the image; the argument is not merely an average-case attack.

Set $D_F(y)=1$ exactly when the fiber count is positive. Then
\[
 \Pr[D_F(F(U_n))=1]=1,\qquad
 \Pr[D_F(U_m)=1]=\frac{|\operatorname{im}F|}{2^m}
 \leq2^{n-m}.
\]
Subtracting gives the claimed advantage. In particular one bit of stretch already gives advantage at least one half, and larger stretch improves it. For polynomially bounded $m$, the polynomial description/read-time factor is $2^{o(n)}$, so both algorithms run in $2^{o(n)}$. If the map family is uniformly constructible, the attack is uniform; otherwise its given description is part of the input, or polynomial advice for that family. This refutes an exponential-in-$n$ security claim for this model, while allowing the possibility of hardness against all polynomial-time attacks.

Goldreich's equation(1) has exactly this form when the local predicate has a fixed number of arguments, regardless of the chosen expanding graph. His alternative equation(2) publishes the predicate table as part of the output; conditioning on that published table likewise leaves only the $n$ seed bits unknown. The paper also permits locality growing like $\log n$. An arbitrary truth table of that arity produces growing-width clauses, for which E's constants are not uniform in the width; the fixed-locality result alone does not cover that regime.

There is a useful algebraic extension of that boundary. Suppose the output predicates, although they may depend on $O(\log n)$ coordinates, have multilinear algebraic normal form over $\mathbb F_2$ of a fixed degree $d$, and suppose $m\leq n(\log n)^a$. Each such form has at most $\sum_{j=0}^{d}\binom{O(\log n)}j=(\log n)^{O_d(1)}$ monomials. Subtracting $y_i$ preserves this bound, so NN-C001 applies on the same $n$ original bits. The same inverse and image distinguisher therefore have $2^{O(n\log\log n/\sqrt{\log n})}$ time. Computing the algebraic normal forms from the explicit $2^{O(\log n)}$ truth tables takes polynomial time by Boolean finite differences. No assertion is made for a logarithmic-locality predicate of growing algebraic degree.

More generally, suppose some output coordinates are fixed-locality tables while all remaining coordinates are supplied by a Boolean circuit containing $s$ gates. Give a variable only to each of these $s$ gates and impose its constant-width Tseitin constraints, together with the requested output bits. The extension is unique for every seed. All local coordinates are still encoded without auxiliary variables. The resulting width-$\max(k,3)$ formula has $N=n+s$ variables and $O_k(m+s)$ clauses, hence costs
\[
 \operatorname{poly}_k(n+m+s)\,
 2^{O_k(N\log\log N/\sqrt{\log N})},
\]
with the sharper exponent $O(N/\sqrt{\log N})$ when $m+s=O(N)$. Thus it is the size of the genuinely nonlocal circuit part that enlarges the witness parameter, not the total number of local output constraints. All search and distinguishing conclusions persist with this explicit parameter substitution.''',
        'Complete deduction proved from E and NN-C001/002; self-check recorded; independent review pending.',
r'''This narrows the cryptographic gate left by a generic Cook--Tseitin reduction: arbitrarily many polynomially listed local observations do not enlarge the unknown seed space. In particular, expansion can obstruct specific local or sequential inversion heuristics while failing to establish exponential security against E's global counting method. The conclusion does not refute the existence of ordinary one-way functions or pseudorandom generators, does not estimate E's constants at a practical key size, and does not make a claim for arbitrary dense multivariate-quadratic maps or logarithmic-locality random predicates of growing degree. The image test uses the original nonnegative integer fiber count; parity alone cannot replace it when a fiber has positive even cardinality.''',
r'''Let $X_n=\operatorname{Spec}\mathbb Z[x_1,\ldots,x_n]/(x_j^2-x_j)$, the disjoint union of $2^n$ copies of $\operatorname{Spec}\mathbb Z$. Each Boolean output table has a unique integer multilinear interpolation which is an idempotent in this algebra, so $F$ defines a morphism $X_n\to X_m$. Over a Boolean target section $y$, its fiber is the finite split scheme with coordinate algebra $\mathbb Z^{|F^{-1}(y)|}$. The local clauses give a concise presentation of this same fiber. Its finite-locally-free rank, or trace of the identity, is the inverse count; reduction to $\mathbb F_2$ gives only the parity of that rank. E computes the rank without expanding the exponential product algebra. This is the explicit multiplication-matrix trace of EGA IV4,18.2.1--18.2.2, and the finite trace formalism of SGA4 XVII6.2.3. The image distinguisher compares support in the finite target with its uniform counting measure; the image has at most the source's number of components. No zeta-function estimate, cohomological purity theorem, or orbit-closure representation is needed, and A or M does not alter this parameter calculation.''',
        [E,goldreich,SGAFINITE,ALGTRACE])
