"""NN-C023: a one-dimensional coherent Frobenius matrix can encode parity-SAT."""

def append_c023(add,E,SGATRACE,VV):
    katz={'source':'Katz, Algebraic Solutions of Differential Equations (p-Curvature and the Hodge Filtration), Inventiones Mathematicae18(1972),1--118',
          'locator':'Equations2.3.7.12--2.3.7.13 and Algorithm2.3.7.14, p.35; rank-one Special Case2.3.7.17, p.36',
          'url':'https://web.math.princeton.edu/~nmk/old/algsoln.pdf',
          'access_note':'Original scan visually read. The cited algorithm assumes smoothness. The proof below independently verifies the coherent calculation for the possibly reducible hypersurfaces used here.',
          'evidence':'work/complexity/katz_algsoln72_source_excerpt.pdf; katz_algsoln72_page35.png; katz_algsoln72_page36.png'}
    add('NN-C023','NEG_NIGHT-03',
        'Parity hardness persists when the coherent Frobenius matrix has only one entry',
r'''There is a deterministic polynomial-time construction taking a 3-CNF $\Phi$ to a nonzero homogeneous polynomial $F$ of degree $r$ in exactly $r\geq3$ variables over $\mathbb F_2$, given by an arithmetic formula of size $O(n+m)$, such that for the proper hypersurface
\[
 X_\Phi=V(F)\subset\mathbb P^{r-1}_{\mathbb F_2}
\]
one has
\[
 H^0(X_\Phi,\mathcal O)=\mathbb F_2,\qquad
 H^{r-2}(X_\Phi,\mathcal O)=\mathbb F_2,
\]
with all other coherent cohomology zero, and absolute Frobenius acts on the latter one-dimensional space by the scalar
\[
 \#\operatorname{SAT}(\Phi)\pmod2.
\]
Here $r=O(n+m)$, and the basis of the one-dimensional space has an explicit universal description. Consequently computing this single Frobenius entry is $\oplus\mathrm P$-complete on the specified factored class. A polynomial-time algorithm for that entry would imply $\mathrm P=\oplus\mathrm P$ and $\mathrm{NP}=\mathrm{RP}$. E computes it in subexponential time on this class. The hypersurfaces are allowed to be singular and reducible; no smoothness or purity assertion is part of the theorem.''',
        [{'source':'NN-C005','locator':'parsimonious Boolean gate encoding and parity-counting completeness'},
         {'source':'NN-C006','locator':'effective Frobenius-data gate being sharpened'},katz,SGATRACE,
         dict(E,locator='Theorem1.1'),VV],
r'''First suppose $\Phi$ has no empty clause and at least one variable. Regard each clause as a Boolean relation on its distinct variable scope. Add a tautological unary relation to every unused variable; this does not change the satisfying assignments and ensures every variable occurs. Let $\mathcal I$ be the set of factor--variable incidences and put $M=|\mathcal I|$. Then $n\leq M\leq3m+n$ after these additions. For each incidence $e=(f,i)$ introduce two distinct variables $z_{e,0},z_{e,1}$. Define integer polynomials
\[
 P_f(z)=\sum_{a\in\{0,1\}^{I_f}:\,a\text{ satisfies }f}
              \prod_{i\in I_f}z_{(f,i),a_i},
 \qquad
 Q_i(z)=\prod_{f:\,i\in I_f}z_{(f,i),0}
             +\prod_{f:\,i\in I_f}z_{(f,i),1}.
\]
Every $P_f$ is homogeneous of degree $|I_f|$ with at most eight distinct monomials. Every $Q_i$ is homogeneous of its positive incidence degree and has two distinct monomials. Put
\[
 P=\prod_f P_f\prod_i Q_i,\qquad
 Z=\prod_{e\in\mathcal I}z_{e,0}z_{e,1}.
\]
Both $P$ and $Z$ have degree $2M$. In a choice of one term from every factor contributing to the coefficient $[Z]P$, the choice of the second or first term of $Q_i$ forces every adjacent $P_f$ to choose the complementary rail. Thus all occurrences encode a single Boolean value of variable $i$. The chosen local assignment must satisfy each clause. Conversely every satisfying assignment makes exactly one consistent choice of all $P_f$ and $Q_i$ terms. All coefficients are positive integers equal to one before expansion, so this proves the exact identity
\[
 [Z]P=\#\operatorname{SAT}(\Phi)
\]
over $\mathbb Z$, including its reduction modulo two.

Adjoin $z_0$, set $r=2M+1$ and $F=z_0P$, and reduce coefficients modulo two. No $P_f$ or $Q_i$ is zero: their monomials are distinct and every clause has a satisfying local assignment. A polynomial ring over $\mathbb F_2$ is an integral domain, so $F\ne0$. It is homogeneous of degree $r$ in $r$ variables. Each rail occurs in exactly two factors, and the total number of factor incidences and multiplication gates needed to describe $F$ is $O(M)$; the eight-term local sums cost only a constant per clause. Moreover
\[
 [z_0Z]F=\#\operatorname{SAT}(\Phi)\pmod2.
\]
If an empty clause was present, use instead $F=z_1^3$ in three variables, whose relevant coefficient is zero. For the finitely many zero-variable cases use $z_1^3$ or $z_1z_2z_3$ according as the count is zero or one. These are again nonzero homogeneous degree-three equations.

We give the coherent calculation, which does not require smoothness. For every nonzero homogeneous degree-$r$ form $F$ in $r$ variables, its multiplication map on projective space is injective and gives
\[
 0\longrightarrow\mathcal O_{\mathbb P^{r-1}}(-r)
 \xrightarrow{\,F\,}\mathcal O_{\mathbb P^{r-1}}
 \longrightarrow\mathcal O_X\longrightarrow0.
\]
On the standard coordinate affine cover, the top Cech cohomology of $\mathcal O(-r)$ is represented by homogeneous Laurent monomials of total degree $-r$ having every exponent negative; monomials with a nonnegative exponent lie in a lower intersection and are zero in the top quotient. There is exactly one remaining monomial,
\[
 b=\frac1{z_1\cdots z_r}.
\]
The same Cech complex, split by Laurent monomial, is acyclic in intermediate degrees: for each exponent pattern other than the all-negative top pattern or the all-nonnegative global-section pattern, its nonzero components form the augmented simplex complex on the coordinates that may be inverted. Pairing subsets by adjoining a fixed admissible coordinate gives a contracting homotopy. Consequently $H^{r-1}(\mathbb P^{r-1},\mathcal O(-r))$ is the one-dimensional span of $b$, all its other cohomology groups vanish, and $\mathcal O$ has only $H^0=\mathbb F_2$. The long exact sequence gives the displayed cohomology of $X$ and the canonical boundary identification of its top group with the span of $b$.

The Frobenius square map on $\mathcal O_X$ lifts to the square map on $\mathcal O_{\mathbb P^{r-1}}$ and the map
\[
 a\longmapsto F a^2
\]
on $\mathcal O(-r)$, because $F(Fa^2)=(Fa)^2$. The latter map has the correct degree $-r$ when applied to a homogeneous section of degree $-r$. Naturality of the boundary map therefore identifies Frobenius on the top group with
\[
 b\longmapsto\frac{F}{(z_1\cdots z_r)^2}.
\]
In the top Cech quotient a numerator monomial survives only when every exponent is at most one. Since the numerator has total degree exactly $r$, that monomial must be $z_1\cdots z_r$. Thus the map is multiplication by $[z_1\cdots z_r]F$. This is precisely the rank-one version of Katz's coefficient formula, now verified for this possibly singular hypersurface. Relabeling $z_1,\ldots,z_r$ as $z_0$ and the rails proves the Frobenius assertion. SGA7 II XXII Corollary3.2 also yields
\[
 \#X_\Phi(\mathbb F_2)\equiv1+\#\operatorname{SAT}(\Phi)\pmod2.
\]

For hardness, the construction is a polynomial-time reduction from parity-3-SAT; that problem is $\oplus\mathrm P$-complete by the parsimonious circuit encoding in NN-C005. For membership on the specified factored class, nondeterministically choose one monomial from each displayed factor, and accept exactly when their exponent vectors sum to the all-one vector. There are constantly many choices at each factor, and exponent checking takes polynomial time. The number of accepting choices is the coefficient, so its parity is in $\oplus\mathrm P$. A polynomial-time Frobenius-entry algorithm therefore decides every $\oplus\mathrm P$ language, giving $\mathrm P=\oplus\mathrm P$; Valiant--Vazirani then gives $\mathrm{NP}=\mathrm{RP}$ as in NN-C006.

For E's upper bound one may simply count the original $\Phi$. There is also a direct bound from the factored input: encode the constant number of monomial choices of each factor by a constant number of bits, add validity constraints, and impose for every rail that exactly one of its two adjacent factors selects it. These are constant-arity Boolean constraints on $O(n+m)$ choice bits. There are $O(M)$ constraints, and $M=O(n+m)$, so their truth-table CNF has fixed width and bounded density. E Theorem1.1 gives time $2^{O((n+m)/\sqrt{\log(n+m)})}$ up to polynomial factors. Thus the single entry has E's subexponential algorithm, while its polynomial-time computation remains the precise parity-counting gate.''',
        'Complete construction and singular coherent calculation proved; full self-check and finite coefficient/point-count checks recorded; independent review pending.',
r'''This strictly sharpens the effective-presentation issue in NN-C006. Exponential cohomology rank is not the only obstruction: here the relevant basis and rank are explicitly known and the entire missing matrix is one bit, yet computing that bit is parity-counting complete. A compact equation, a one-dimensional coherent cohomology group, and the existence of a trace formula do not constitute an efficient algorithm for Frobenius. The result concerns a succinct factored input; expansion into all monomials may already cost exponential time. It gives neither a lower bound for unrestricted arithmetic circuits nor a claim that the smooth hypersurface case is hard. A and M do not supply the missing entry.''',
r'''The construction is already a scheme-theoretic theorem: parity-3-SAT is encoded in the absolute-Frobenius endomorphism of an explicitly trivialized rank-one coherent cohomology space of a projective hypersurface. Its sheaf-theoretic exact sequence and Cech basis prove the dictionary directly. Katz's original pp.35--36 locate the corresponding smooth Hasse--Witt formula, and SGA7 II XXII3.1--3.2 locate the zeta congruence and trace-point-count identity for arbitrary proper schemes. These reducible hypersurfaces are not asserted to furnish pure l-adic realizations of canonical bases, and their one-dimensional coherent Frobenius space is not a GCT representation multiplicity. The theorem identifies an effective arithmetic operation inside the geometric formalism, rather than importing Boolean hardness merely by analogy.''',
        [E,katz,SGATRACE,VV])
