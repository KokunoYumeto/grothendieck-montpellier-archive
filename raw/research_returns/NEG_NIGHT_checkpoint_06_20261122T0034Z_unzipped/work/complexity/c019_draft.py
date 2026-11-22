"""NN-C019: an instance-dependent deterministic isolation consequence of E."""

def append_c019(add,E,SGAFINITE):
    mvv={'source':'Mulmuley--Vazirani--Vazirani, Matching is as Easy as Matrix Inversion, STOC1987',
         'locator':'Section3, Lemma1, printed p.347; compare Lemma2, p.348 for the unique-lowest-term valuation argument',
         'url':'https://people.eecs.berkeley.edu/~vazirani/pubs/matching.pdf',
         'access_note':'Author-hosted original STOC version, not the differently paginated Combinatorica version.'}
    add('NN-C019','NEG_NIGHT-03',
        'E constructs one polynomial-height isolating weight vector for each instance',
r'''Let $\mathcal F\subseteq\{0,1\}^n$ be a witness set whose prefix-restricted counts admit one of the exact algorithms NN-C001, NN-C002 or NN-C017. If $\mathcal F$ is nonempty, a deterministic algorithm in the same time bound up to a polynomial factor constructs a vector
\[
 w\in\{1,n+1\}^n\subseteq\{1,\ldots,2n\}^n
\]
and a unique minimum-weight witness $x^*\in\mathcal F$, with minimum weight at most $n$. It also identifies that witness. For fixed-width CNF, E Theorem1.1 gives $\operatorname{poly}(n+m)2^{O_k(n\log\log n/\sqrt{\log n})}$ time and polynomial space. For a fixed-density CNF, the construction retains the sharper $2^{O_{k,C}(n/\sqrt{\log n})}$ exponent.''',
        [{'source':'NN-C002','locator':'complete exact prefix-count self-reduction'},
         {'source':'NN-C017','locator':'fixed-field extension and prefix constraints'},
         dict(E,locator='Theorem1.1, including fixed-density statement'),mvv],
r'''Use exact prefix counts, with the bit order $0<1$, to find the lexicographically first witness $x^*$. Let $S=\{i:x_i^*=1\}$. No proper subset of $S$ is the support of a witness: its bit string would agree until its first removed one, where it has zero and $x^*$ has one, contradicting lexicographic minimality. Define $w_i=1$ for $i\in S$ and $w_i=n+1$ for $i\notin S$.

The weight of $x^*$ is $|S|\leq n$. If another witness has support $T\subseteq S$, then $T\ne S$ would contradict the preceding inclusion minimality; equality gives the same bit string. Every other witness therefore has an element outside $S$ and has weight at least $n+1>|S|$. Thus $x^*$ is the unique minimum. The argument also covers $S=\varnothing$. If the initial count is zero, the algorithm reports emptiness instead of claiming an isolated witness.

There are at most $n+1$ counting calls. In the sparse-system interfaces each prefix adds at most $n$ linear equations, with fixed degree and one or two monomials, so the corresponding bounds are preserved. For fixed-width CNF, a prefix consists of at most $n$ unit clauses; padding a unit clause by repeated literals keeps it within the width bound, or one substitutes its bit directly. The number of variables never increases, and an initial bound $m\leq Cn$ becomes at most $(C+1)n$ clauses if all variables are retained. Thus E's fixed-density exponent $2^{O_{k,C}(n/\sqrt{\log n})}$ is preserved as well. All counts, the current prefix, and the final weights use polynomial space.

MVV Lemma1 states that independent uniform weights in $[2n]$ isolate any nonempty family with probability at least $1/2$. The construction here selects a weight in that same range deterministically by first solving the instance at E's running time. It is not a polynomial-time replacement for the MVV random choice, and it is not one small weight family that works uniformly for all succinctly represented witness sets. It also does not eliminate signed cancellation at an unweighted specialization: isolating a term in a signed expression produces a nonzero leading term of a new weight-generating polynomial, whereas the original specialization can still vanish.''',
        'Complete deduction proved; complete self proof-check passed; independent review pending.',
r'''This makes the available deterministic NP-style isolation precise: instance-dependent isolation and witness recovery are mildly subexponential for the stated sparse interfaces, with polynomially bounded weights. A polynomial-size output does not imply polynomial construction time. It supplies neither $\mathrm{NP}=\mathrm{UP}$ nor $\mathrm{NP}\subseteq\oplus\mathrm P$ with polynomial uniformity. Hoza's logarithmic-seed layered-graph construction remains a different polynomial-time uniform theorem; NN-C007 states the missing NP transfer gates.''',
r'''The finite witness scheme has a diagonal grading operator with one basis vector of degree $w\cdot x$ for every witness. Its character is $\sum_{x\in\mathcal F}T^{w\cdot x}$, and the least-degree graded piece has rank one. Equivalently, $w$ exposes a single vertex of the convex hull of the witness bit vectors and selects one monomial in the initial form of the positive generating polynomial. The count/character interpretation follows directly from the component-idempotent basis and the finite-trace formalism of SGA4 XVII6.2.3. These are finite-set and torus-grading statements; they do not construct a GCT canonical basis or make a signed structure-constant formula positive. A numerical signed specialization forgets the grading and can reintroduce cancellation.''',
        [E,mvv,SGAFINITE])
