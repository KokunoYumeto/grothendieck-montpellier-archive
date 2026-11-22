"""NN-C031: a fixed-F4 smooth projective hypersurface parity gate."""

def append_c031(add,E,SGATRACE,VV):
    sga1={'source':'SGA1, ExposeII, Section4',
          'locator':'Theorem4.10(iii) and Corollary4.12; smooth hypersurface interface used in NN-C030',
          'url':'https://grothendiecksga.com/read/sga1/fr/II-4.html'}
    weil={'source':'Deligne, La conjecture de Weil I, PMIHES43(1974),273--307',
          'locator':'Theorem1.6, printedp276',
          'url':'https://www.numdam.org/item/PMIHES_1974__43__273_0.pdf'}
    katz={'source':'Katz, Algebraic Solutions of Differential Equations, Invent.Math.18(1972),1--118',
          'locator':'Rank-one Special Case2.3.7.17, printedp36; full direct Cech proof in NN-C023',
          'url':'https://web.math.princeton.edu/~nmk/old/algsoln.pdf'}
    inputs=[{'source':'NN-C030','locator':'complete singular-parameter confinement lemma for pairwise degree-two P: every bad a lies in F_(2^(r ord_r2))'},
            {'source':'NN-C023','locator':'incidence-rail coefficient encoding; tautological factors for unused declared variables; one-dimensional coherent basis'},
            sga1,katz,SGATRACE,weil,VV,dict(E,locator='Theorem1.1; evaluator retains the source formula parameter before padding')]
    add('NN-C031','NEG_NIGHT-03',
        'Forced-variable padding puts the smooth rank-one parity gate over fixed F4',
r'''Fix once and for all
\[
 K=\mathbb F_4=\mathbb F_2[\omega]/(\omega^2+\omega+1).
\]
There is a deterministic polynomial-time reduction from parity-3-SAT to a family of smooth projective hypersurfaces over this fixed field. Each has a polynomial-size homogeneous arithmetic-circuit equation, and its top coherent cohomology is a canonically based one-dimensional space. The $4$-power Frobenius scalar on that line is the original satisfying-assignment parity $c$. Point-count parity is $1+c$.

The geometric statement is uniform: let $k\geq3$ be odd, $r=2^k-1$, $M=(r-1)/2$, and let $P$ be any nonzero polynomial over $\mathbb F_2$ homogeneous of degree two in every one of $M$ variable pairs. Then
\[
 X_P=V\left(z_0^r+\sum_{e=1}^{M}(z_{e,0}^r+z_{e,1}^r)
                         +\omega z_0P\right)
                       \subset\mathbb P^{r-1}_K
\]
is smooth projective. If $c$ is the squarefree coefficient of $z_0P$, its top coherent line has absolute-Frobenius coefficient $\omega c$ and $4$-Frobenius scalar $c$. The hard subclass has $P$ in the succinct rail-factor format, so its scalar and point-count parity are $\oplus\mathrm P$-complete under deterministic polynomial-time reductions. Polynomial-time extraction gives $\mathrm P=\oplus\mathrm P$ and $\mathrm{NP}=\mathrm{RP}$. No varying base field is needed.''',
        inputs,
r'''First prove the uniform smoothness statement. For $r=2^k-1$, the multiplicative order of $2$ modulo $r$ is exactly $k$. The exponent $k$ works, while for $0<i<k$ the positive integer $2^i-1$ is strictly smaller than $r$ and therefore cannot be divisible by $r$. NN-C030 confines every bad parameter in the Fermat pencil $H+u z_0P$ to
\[
                            \mathbb F_{2^{rk}}.
\]
Both $r$ and $k$ are odd. The element $\omega$ has degree two over $\mathbb F_2$, so it cannot lie in that odd-degree extension: otherwise the tower law would make two divide $rk$. Therefore the fiber at the fixed parameter $\omega$ is smooth. The same reasoning applies to its conjugate $\omega^2$. Projectivity follows from the homogeneous equation. The form is nonzero, since its rail pure-power terms are not divisible by $z_0$, whereas $z_0P$ is.

The coherent calculation from NN-C023 applies over $K$ without change. There is $H^0(\mathcal O)=K$, one other nonzero coherent group in degree $r-2$, and its canonical boundary/Cech basis has absolute-Frobenius coefficient equal to the full squarefree coefficient of the defining form. The Fermat terms do not contribute to that coefficient. Thus the coefficient is $\omega c$, with $c\in\mathbb F_2$. Iterating this semilinear map twice yields the $K$-linear $4$-power Frobenius with scalar
\[
                        (\omega c)^{1+2}=\omega^3c^3=c.
\]
There is no semilinear-versus-linear ambiguity: absolute Frobenius sends $ae$ to $a^2\omega c\,e$, while its second iterate sends $ae$ to $a c\,e$ because $a^4=a$ in $K$.

We next arrange this special degree with polynomial padding while preserving the original count. Start with the incidence-rail construction of NN-C023, with $M_0\geq1$ incidences and $r_0=2M_0+1$. Choose the least odd integer $k\geq3$ such that
\[
                  r=2^k-1\geq r_0,
                 \qquad M=(r-1)/2.
\]
This is computed from the binary length of $r_0+1$ and a parity check. The new degree is linear in the old one: if $k>3$, minimality gives $2^{k-2}-1<r_0$, hence $r<4(r_0+1)-1$; the bounded case $k=3$ also satisfies a constant-factor bound. Consequently $M-M_0=O(M_0)$.

Append exactly $M-M_0$ fresh Boolean variables, each with its own positive unit clause. Each new variable has exactly one allowed value, so every old satisfying assignment has exactly one extension. The number of satisfying assignments, and in particular its parity, is unchanged. Each such gadget adds one clause, one variable and exactly one incidence; no old occurrence is modified. Thus the new incidence count is exactly $M$. In the rail polynomial its clause factor and its two-term variable-consistency factor together have degree two in the new rail pair and squarefree coefficient one. All old factors remain unchanged. This verifies both the required multihomogeneity and the coefficient preservation directly at the polynomial level.

As in NN-C030, treat the elementary exceptional source instances before forming the rails. An empty clause has known parity zero; an instance with no declared variables has its one assignment directly testable. Replace it by the positive unit formula $x$ for parity one or the contradictory unit formula $x\wedge\neg x$ for parity zero. These are fixed instances with nonempty incidence sets. For all other inputs, tautological factors make every otherwise unused declared variable incident without restricting it. Tautological clauses and repeated literals can be simplified first. After these steps each local clause factor is nonzero and the product $P$ is nonzero over $\mathbb F_2$. No decision of the hard parity is used to choose a padding gadget.

The construction now has precisely $r$ coordinates and a degree-$r$ equation over the fixed two-bit field $K$. Every local clause factor has at most eight monomials; each variable-consistency factor has two. The number of factor incidences and their arithmetic-circuit descriptions is polynomial in the source formula size. Each pure power $z^r$ takes $O(\log r)$ multiplications by repeated squaring, so the entire sum of Fermat terms and the rail product has a polynomial-size arithmetic circuit. Its degree is itself polynomial in the source size. This assertion concerns the circuit/factor presentation; fully expanding its coefficients can still require exponentially many monomials.

The actual smooth hypersurface therefore satisfies
\[
 \#X_P(\mathbb F_4)\equiv1+c\pmod2,
 \qquad
 Z(X_P/\mathbb F_4,T)\equiv\frac{1-cT}{1-T}\pmod2,
\]
by SGA7 II XXII3.1--3.2, exactly as in NN-C024. Deligne's Theorem1.6 supplies purity of its l-adic cohomology because every output is smooth and projective. The proof uses the singular-parameter confinement to establish smoothness first; it does not infer smoothness or purity from a point-count congruence.

For a precise complete problem, use the syntactically specified incidence-rail factor format of NN-C023, with nonempty scopes, the displayed consistency factors, and an incidence count giving $r=2^k-1$ for odd $k\geq3$. These conditions are checkable in polynomial time, and fixed straight-line instructions generate the equation $H+\omega z_0P$ from that format. No identity test against an arbitrary purported equivalent circuit is part of the input validation. Every such input is smooth by the uniform theorem. Nondeterministically choose one monomial from each factor and check that the exponents sum to the full squarefree vector. The parity of the number of accepting choices is $c$, proving $\oplus\mathrm P$ membership for the Frobenius scalar on this class. The preceding padded reduction proves hardness. This is a complete problem on a specified geometric presentation family, not a general promise that every smooth hypersurface has a one-dimensional coherent top group.

Point-count parity belongs to $\oplus\mathrm P$ independently of the special coefficient format. Guess its $r$ coordinates in $K$, require the first nonzero coordinate to be one, and check the circuit equation. The chosen normalization gives exactly one vector for each projective rational point. There are $2r$ guessed bits, and all field operations have constant bit cost. The displayed parity formula converts this output to $c$ by adding one. Thus point-count parity on this smooth fixed-field family is also parity-counting complete. An algorithm correct on arbitrary smooth projective inputs in particular handles these guaranteed smooth instances, so polynomial time would give $\mathrm P=\oplus\mathrm P$. Valiant--Vazirani then gives $\mathrm{NP}=\mathrm{RP}$ with the scope already detailed in NN-C006.

E computes the parity by counting the source formula before the forced-variable padding. Its original variable count and clause-density hypotheses therefore remain the relevant parameters, with only polynomial overhead for building the padded geometric input. Running E instead on all geometric coordinates would lose that sharper statement. The field is the one fixed $\mathbb F_4$ throughout, and neither A nor M is used.''',
        'Complete fixed-field smoothness, exact padding, coherent-Frobenius and parity-completeness proofs; independent review pending.',
r'''The remaining varying-field qualification of NN-C030 is removed: the hard rank-one coherent Frobenius entry is realized deterministically on smooth projective hypersurfaces over fixed $\mathbb F_4$. The padding is linear and parsimonious at the Boolean count level. Neither total l-adic rank nor the fully expanded defining polynomial is claimed polynomially bounded; the geometric equation is succinct. This yields a strictly smaller effective gate than arbitrary field construction or random specialization. It supplies actual pure finite Weil realizations for the counting gadgets without evaluating the hard coefficient or identifying a GCT canonical basis.''',
r'''For every odd $k\geq3$, every nonzero pairwise-degree-two $P$ over $\mathbb F_2$ in $M=2^{k-1}-1$ pairs defines the smooth projective hypersurface
\[
 V\left(z_0^{2^k-1}+\sum_e(z_{e,0}^{2^k-1}+z_{e,1}^{2^k-1})
                        +\omega z_0P\right)/\mathbb F_4.
\]
The singular-parameter field from NN-C030 has odd degree $k(2^k-1)$ and therefore excludes the fixed quadratic parameter $\omega$. Its top coherent line is explicitly trivialized by the boundary/Cech construction. Absolute Frobenius has semilinear coefficient $\omega c$; $4$-power Frobenius has scalar $c$. The lower coherent groups are only the degree-zero field, and the proper zeta congruence is $(1-cT)/(1-T)$ modulo two. Exact classical interfaces are Katz2.3.7.17, SGA1 II4.10(iii)/4.12, SGA7 II XXII3.1--3.2 and Deligne Weil I1.6.

The forced-unit-clause padding turns any source formula into this geometric class while preserving its count exactly. Thus the field, smoothness and coherent basis are all supplied effectively, and the sole unknown scalar is parity-counting complete. This is an actual smooth projective finite-field construction, with pure l-adic cohomology, and a precise computational operation inside it. It does not assert a canonical representation-theoretic realization of permanent/determinant multiplicities.''',
        inputs)
