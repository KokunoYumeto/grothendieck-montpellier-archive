"""NN-C021: E transcripts cannot uniformly be converted to short natural refutations."""

def append_c021(add,E,SGATRACE):
    bgip={'source':'Buss--Grigoriev--Impagliazzo--Pitassi, Linear Gaps between Degrees for the Polynomial Calculus Modulo Distinct Primes, JCSS62(2001),267--289',
          'locator':'Author-hosted journal-final manuscript: Section2 pp.5--6; Lemma3 pp.7--8; Theorem15 p.17; Corollaries21--22 and proof p.19',
          'url':'https://mathweb.ucsd.edu/~sbuss/ResearchWeb/lineargaps/journalfinal.pdf',
          'access_note':'The quoted manuscript page numbers are its printed1--28 pagination, not inferred journal pagination.'}
    bsw={'source':'Ben-Sasson--Wigderson, Short Proofs Are Narrow: Resolution Made Simple, JACM 48 (2001), 149--169',
         'locator':'Lemma4.2 p.155; Theorem4.4 and Corollary4.5 p.156; size-width Corollary3.6 p.155; proof of Theorem4.4 Section6.1 p.161',
         'url':'https://people.inf.ethz.ch/emo/SatSem05/Papers/BensassonWidgerson01.pdf'}
    ips={'source':'Impagliazzo--Pudlak--Sgall, Lower Bounds for the Polynomial Calculus and the Groebner Basis Algorithm, Computational Complexity8(1999),127--144',
         'locator':'Author-hosted accepted manuscript: Section6, Theorem6.2 and complete proof p.13; Corollary6.3 pp.13--14',
         'url':'https://iuuk.mff.cuni.cz/~sgall/ps/pcalc.ps',
         'access_note':'Downloaded original author-hosted PostScript and converted locally to PDF; manuscript pagination is1--18, not inferred journal pagination.',
         'evidence':'work/complexity/ips99_source_excerpt.pdf; ips99_page13.png; ips99.txt'}
    add('NN-C021','NEG_NIGHT-06',
        'E computation transcripts have no polynomial-size translation to general resolution or polynomial calculus',
r'''For the computation-transcript proof system of NN-C008, there is no fixed polynomial upper bound converting the size of every transcript refutation into the size of a resolution refutation of the same CNF. The analogous statement holds for ordinary polynomial calculus over $\mathbb F_2$, when proof size counts explicitly written nonzero monomials. More concretely, there are fixed-density 3-CNF contradictions on $N$ variables whose E transcripts have size
\[
 2^{O(N/\sqrt{\log N})},
\]
while every refutation in the relevant natural system has size $2^{\Omega(N)}$. The resolution and polynomial-calculus lower-bound families may be different. These natural-system lower bounds are classical inputs; the stated comparison with E's new transcript system is the deduction.''',
        [dict(E,locator='Theorem1.1, bounded-clause-density exponent'),
         {'source':'NN-C008','locator':'complete computation-transcript proof-system construction'},bgip,bsw,ips],
r'''For resolution, take 3-regular connected expanding graphs with an odd total vertex charge and the associated Tseitin CNFs. BSW Lemma4.2 gives at most four clauses per graph vertex and one variable per edge, hence $O(N)$ clauses of width three. Their Corollary4.5 gives resolution size $2^{\Omega(N)}$; equivalently, combine their linear width lower bound Theorem4.4 with Corollary3.6. E Theorem1.1 nevertheless counts each such fixed-density 3-CNF in $2^{O(N/\sqrt{\log N})}$ time and polynomial space. Its count is zero. Recording all configurations as in NN-C008 multiplies the time by only a polynomial, absorbed by the same exponent. This gives the asserted transcript upper bound on this family.

For polynomial calculus over $\mathbb F_2$, use BGIP's Boolean mod-$p$ Tseitin family with $p=3$, over a fixed-degree expanding graph. Their Corollary21 states a linear degree lower bound for this Boolean encoding over characteristic two, and Corollary22's proof explicitly states that its 3-CNF translation has $O(N)$ clauses and variables and exponential monomial-size lower bounds. There is, however, a directional omission in the printed proof of Corollary21: its appeal to Lemma2 supplies a reduction from the Boolean system to the root-of-unity system, whereas the definition and Lemma1 require the reverse reduction to transfer the cited hardness. We supply that reverse reduction here instead of using that inference as printed.

Work in the fixed field $F=\mathbb F_4$, choose a primitive cube root $\omega$, and use BGIP's root-of-unity system $\operatorname{TS}_n(3)$ in edge variables $y_e$. Define the Boolean indicator substitutions
\[
 x_{e,i}=\delta_i(y_e),\qquad
 \delta_i(T)=\frac13\sum_{j=0}^{2}\omega^{-ij}T^j
 \quad(0\leq i<3).
\]
The scalar $3$ is invertible in characteristic two. On $T=\omega^a$ this polynomial is one for $a=i$ and zero otherwise. Every substituted Boolean axiom and clause of $\operatorname{BTS}_{n,3}$ involves only a fixed number $s$ of edge variables and has fixed degree. Include the domain equations $y_e^3-1$ for these variables and the corresponding local root-of-unity vertex or reverse-edge constraints $g_1,\ldots,g_t$. These local equations force exactly the local Boolean constraint in question.

Here is a complete constant-degree derivation argument. The algebra
\[
 F[y_1,\ldots,y_s]/(y_1^3-1,\ldots,y_s^3-1)
 \cong\prod_{a\in\{1,\omega,\omega^2\}^{s}}F
\]
has distinct roots in every coordinate. Let $q$ be the substituted Boolean constraint polynomial. At a tuple where all $g_j$ vanish, $q$ vanishes. At every other tuple, choose the first nonzero $g_j$ and set the value of $h_j$ to $q/g_j$, setting the other $h$ values to zero. Lagrange interpolation gives representatives $h_j$ of individual degree at most two, hence total degree at most $2s$, and
\[
 q=\sum_j h_jg_j+\sum_{e=1}^{s}u_e(y)(y_e^3-1).
\]
The last equality is an equality of ordinary polynomials: reduce the difference successively by the monic equations $y_e^3-1$. The remainder has individual degrees below three and vanishes at every root tuple, so it is zero. Since $s$, all input degrees and all interpolation degrees are fixed, the degrees of every displayed product are bounded by a constant $C$. Expand each multiplier into its finitely many monomials; each monomial multiple of an axiom is derivable by successive single-variable multiplication, and their linear combination gives $q$ in PC degree at most $C$. This proves a $(2,C)$ reduction from $\operatorname{TS}_n(3)$ to the Boolean system in the exact sense of BGIP's definition and Lemma1. Substitution of a degree-$d$ Boolean PC refutation therefore gives a root-of-unity refutation of degree at most $\max(C,2d)$.

BGIP Theorem15 bounds that latter degree below by $\Omega(n)$. A refutation over $\mathbb F_2$ is also one over $F$, so the Boolean system requires degree $\Omega(n)$ over $\mathbb F_2$. Its numbers of variables and clauses are $O(n)$ and its clause width is fixed. BGIP Lemma3 and its proof turn this into a 3-CNF with $O(n)$ variables and clauses while preserving the degree lower bound up to a constant factor. Impagliazzo--Pudlak--Sgall Theorem6.2 says that a proof with $M$ nonzero monomials gives a proof of degree at most $\max(d_0,2\lceil\sqrt{N\log M}\rceil+1)$, where $d_0$ is the initial degree. For constant $d_0$ and minimum refutation degree $d=\Omega(N)$, this implies $M=2^{\Omega(d^2/N)}=2^{\Omega(N)}$. This is also the exact size-degree chain invoked in BGIP Corollary22's proof. Apply E Theorem1.1 and NN-C008 to this 3-CNF family exactly as before.

Now suppose a fixed polynomial $P$ bounded the length of a natural-system refutation in terms of the length $L$ of every E transcript for the same formula. On one of the corresponding hard families,
\[
 P(L)\leq2^{O(N/\sqrt{\log N})}=2^{o(N)},
\]
contradicting the classical $2^{\Omega(N)}$ lower bound. This excludes even a universal polynomial size bound, and therefore in particular excludes a polynomial-time proof translation of that kind. The argument compares proofs of the same formula under its stated encoding; it does not forbid changing the target proof system by extension axioms or new inference rules.

For the familiar parity Tseitin equations over $\mathbb F_2$ themselves, summing all vertex equations already yields the contradiction in low degree. Thus the polynomial-calculus example deliberately uses mod three constraints over characteristic two, as in BGIP; the resolution example alone cannot justify a characteristic-two polynomial-calculus lower bound. This field distinction is essential.

No lower bound on unrestricted satisfiability algorithms follows from these proof lower bounds. BGIP Corollary22's algorithmic conclusion concerns implementations that explicitly represent polynomials as sums of monomials and generate the corresponding polynomial-calculus derivation. E's interpolation and global count computation need not produce such a derivation. NN-C009's compact semantic identity likewise does not constitute a short polynomial-calculus refutation.''',
        'Complete deduction and reverse low-degree reduction proved; primary source clauses and printed directional omission checked; independent review of the added repair pending.',
r'''This gives a concrete obstruction at the proof-system interface left open by NN-C009. E removes the exponential-time hypothesis but does not remove exponential resolution or characteristic-two polynomial-calculus proof-size lower bounds. The transcript system is still not polynomially bounded on all tautologies, so this comparison does not imply $\mathrm{NP}=\mathrm{coNP}$ or separate those classes.''',
r'''For every hard contradiction, the Boolean-coordinate equation scheme is empty; its finite algebra has rank and Frobenius trace zero. E computes this vanishing efficiently relative to the former exhaustive exponent. Resolution width and polynomial-calculus degree/monomial size concern the cost of deriving the unit ideal from the chosen generators in specified syntactic systems. Thus the same zero scheme can have a short computation transcript and a long ideal-derivation certificate. The finite trace dictionary is SGA7 II XXII Corollary3.2, but that identity places no bound on the chosen presentation's derivation complexity. This is an effective distinction between a geometric zero object and an explicit proof of emptiness in a fixed calculus, not a new failure of purity or a representation-theoretic multiplicity statement.''',
        [E,bgip,bsw,ips,SGATRACE])
