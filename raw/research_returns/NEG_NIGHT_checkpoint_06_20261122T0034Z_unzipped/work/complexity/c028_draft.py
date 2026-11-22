"""NN-C028: actual pure Tate embedding comparison, after checkpoint03 freeze."""

def append_c028(add,E):
    pp={'source':'Aaronson, Quantum Computing, Postselection, and Probabilistic Polynomial-Time (2005)',
        'locator':'Author manuscript Section1, printedp1, definition of PP by strict-majority acceptance; the reduction below is proved directly',
        'url':'https://www.scottaaronson.com/papers/pp.pdf'}
    sga={'source':'SGA4, ExposesXVII--XVIII',
         'locator':'XVII Theorem5.2.6 and Proposition5.2.8; XVIII equation2.8.1 and Theorem2.9; used through the complete global sheaf proof in NN-C027',
         'url':'https://grothendiecksga.com/read/sga4/fr/XVII-5.html',
         'additional_url':'https://grothendiecksga.com/read/sga4/fr/XVIII-2.html'}
    inputs=[{'source':'NN-C027','locator':'smooth integral sparse cubic construction and actual compact-support Tate decomposition; both arithmetic zeta identities'},
            {'source':'NN-G015','locator':'work/gct/chapter.tex subsectionNN-G015; support-versus-count comparison is background, not re-registered'},
            {'source':'NN-C006','locator':'Toda main-theorem locator and resulting PH collapse'},pp,sga,
            dict(E,locator='Theorem1.1, original-CNF-variable count and bounded-density specialization')]
    add('NN-C028','NEG_NIGHT-04;NEG_NIGHT-12',
        'Embedding comparison for actual pure Tate cohomology is PP-complete',
r'''There is a polynomial-time construction from a pair of Boolean verification circuits to two smooth geometrically integral affine schemes $X_1,X_2/\mathbb Z$, each defined by one sparse cubic equation. They have equal relative dimension $V+H$, and
\[
 H_c^{2H}(X_{j,\overline{\mathbb F}_p},\mathbb Q_\ell)
          =\mathbb Q_\ell(-H)^{N_j},\qquad
 H_c^{2(V+H)}=\mathbb Q_\ell(-V-H),
\]
with all other groups zero and $N_j$ the corresponding acceptance count. For any fixed prime $p$ and any fixed $\ell\ne p$, deciding whether a Frobenius-equivariant linear injection
\[
 H_c^{2H}(X_1,\mathbb Q_\ell)
       \hookrightarrow H_c^{2H}(X_2,\mathbb Q_\ell)
\]
exists is PP-complete on this encoded family. Hardness persists when $N_1,N_2>0$, so the Frobenius eigenvalue support, the cohomological degree support and the two weights agree. The same comparison holds simultaneously at every prime, and for the literal quadratic-character variants over $\mathbb Z[1/2]$ at every odd prime.

This is existence of a linear map between actual geometric cohomology representations. It is not a claim that the map is induced by a morphism, correspondence, or containment between the schemes. Under A the global zeta factors have the same shifted critical lines; their multiplicity comparison is still the PP-complete operation.''',
        inputs,
r'''Start with two verification circuits. The gate construction of NN-C027 gives systems $f_{j,1},\ldots,f_{j,h_j}$ on $v_j$ Boolean input and gate coordinates, with
\[
 Y_j=V(f_{j,1},\ldots,f_{j,h_j})\simeq
             \coprod_{N_j}\operatorname{Spec}\mathbb Z.
\]
Each gate extension is unique. The equations have degree at most two and constant monomial sparsity, and each system retains $x_1^2-x_1$ among its equations. A fixed dummy coordinate constrained to zero can be introduced first if necessary to make every coordinate list nonempty.

The geometric parameters can be matched without multiplying either count. Put $V=\max(v_1,v_2)$. For each missing coordinate append a new variable $z$ and the two equations $z^2-z=0$, $z=0$. These force its unique value zero, so $Y_j$ and $N_j$ are unchanged. Let the resulting numbers of equations be $h'_1,h'_2$, and put $H=\max(h'_1,h'_2)$. Pad the shorter list by repeated copies of its retained Boolean equation until both lists have exactly $H$ entries. Repeating an equation does not change its common-zero scheme. All of this uses only polynomially many coordinates, equations and constant-size coefficients. Apply NN-C027 to the padded lists:
\[
 X_j:\quad t^2-t=\sum_{i=1}^H y_i f_{j,i}(x).
\]
Its proof applies unchanged to redundant equations and gives the displayed actual cohomology. In particular the lower Frobenius operator is the scalar $p^H$ on a vector space of dimension $N_j$. Every linear map between these two lower groups therefore commutes with Frobenius. Such a map can be injective exactly when
\[
                         N_1\leq N_2.
\]
This proves the assertion simultaneously at all primes; no explicitly listed exponential-size cohomology basis is required in the input. In the quadratic-character version the common scalar is $\chi_{-4}(p)p^H$, so the same equivalence holds at every odd prime. The equal top Tate lines can also be included if one asks for an injection of the full graded compact-support representation.

For hardness, take a Boolean circuit $C$ on $n\geq1$ bits, with $a$ accepting assignments. On a tagged input $(b,x)\in\{0,1\}^{n+1}$ define two polynomial-size verifiers. The right verifier accepts when $b=0$ and $C(x)=1$, or when $b=1$ and $x=0^n$. Its count is $N_R=a+1$. The left verifier accepts when $b=0$ and $x_1=0$, or when $b=1$ and $x$ is one of the two distinct strings $0^n,e_1$. Its count is
\[
             N_L=2^{n-1}+2.
\]
Both counts are positive. The injection from the left lower group to the right exists precisely when
\[
  2^{n-1}+2\leq a+1
       \quad\Longleftrightarrow\quad a>2^{n-1}.
\]
Strict-majority circuit acceptance is PP-complete directly from the definition: unroll a polynomial-time probabilistic verifier on its fixed input, using its independent fair coin bits as circuit inputs, and pad the coin count if needed. The circuit accepts on exactly the machine's accepting coin strings. Thus the entire reduction to the two sparse cubics is polynomial and proves PP-hardness, including the positive-rank restriction. An input circuit with no coin bits can be given an ignored bit without changing its majority status.

For completeness, here is a direct PP-membership construction that handles equality rather than silently replacing $\leq$ by $<$. Let $P,Q$ be the two acceptance predicates, with counts $A,B$, padded to a common witness length $w$ by requiring every added bit to be zero. Add a new bit $r$ and define
$P'(r,x)=[r=0]P(x)$, $Q'(r,x)=[r=0]Q(x)$.
Their common domain has size $M=2^{w+1}$, while their counts remain $A,B$. On a selector bit $b$ and this domain, accept when
\[
          (b=0\ \hbox{and }Q'=1)
            \quad\hbox{or}\quad(b=1\ \hbox{and }P'=0).
\]
There are $M+B-A$ accepting strings among $2M$. The string $b=0,r=1,x=0^w$ is always rejecting. Add a fresh free bit $u$, doubling all paths, and override exactly the one path $u=0,b=0,r=1,x=0^w$ to accept. The number of accepting paths becomes
\[
                   2M+2(B-A)+1
\]
among $4M$. This exceeds half exactly when $B-A\geq0$. The whole test is a polynomial-size Boolean predicate. It proves PP membership on the encoded family, and hence PP-completeness. The circuit-and-equation format can be checked syntactically; the assertion is not a promised PP upper bound for arbitrary sparse cubic schemes whose provenance is absent.

The associated arithmetic zeta functions are
\[
             \zeta_{X_j}(s)
                 =\zeta(s-V-H)\zeta(s-H)^{N_j}.
\]
When $N_1,N_2>0$ the types of nontrivial factors, cohomological degrees and eigenvalue supports agree. At any fixed nonreal nontrivial zero $\rho$ of $\zeta$, NN-C027 gives
\[
 \operatorname{ord}_{s=H+\rho}\zeta_{X_j}(s)
                 =N_j\operatorname{ord}_\rho\zeta.
\]
Consequently the same embedding comparison is comparison of those two analytic orders. The order identity is unconditional; A fixes the common shifted critical lines. For the quadratic variant replace the lower factor by $L(s-H,\chi_{-4})$ and remove the upper prime-two Euler factor as in NN-C027. The same conclusion holds at its nonreal nontrivial zeros.

E decides the comparison by computing the two original counts and comparing their binary integers. For fixed-width source CNFs it keeps the original variable parameters, regardless of the padding of the geometric schemes. For a general verification circuit of size $s$ on $n$ inputs, the parsimonious gate-to-3-CNF encoding has $O(n+s)$ variables and a linear number of clauses, so Theorem1.1's bounded-density form gives a bound $\operatorname{poly}(n+s)2^{O((n+s)/\sqrt{\log(n+s)})}$ for that source circuit. No bound solely in the original coin count $n$ is inferred for arbitrary circuits with many gates.''',
        'Complete actual-cohomology comparison, parameter matching and strict-majority proofs; complete deduction-level self-reading passed; independent review pending.',
r'''This turns NN-G015's abstract support-versus-dominance example into a comparison of actual pure geometric representations of smooth integral cubic schemes. The representation type and analytic critical lines are fixed; deciding which multiplicity is larger is PP-complete. A polynomial-time injection-existence procedure on this succinct family would give $\mathrm P=\mathrm{PP}$, and hence $\mathrm{PH}=\mathrm P$ by Toda. This is a conditional implication, not an unconditional lower bound. E supplies a subexponential evaluator of the comparison, and A does not evaluate the multiplicities. The result does not transfer PP-hardness to the permanent/determinant orbit-closure multiplicities or establish a GCT multiplicity obstruction.''',
r'''The algebraic-geometric assertion is that, for the explicitly padded Boolean systems $Y_j\simeq\coprod_{N_j}\operatorname{Spec}\mathbb Z$, the two cubic schemes
\[
 X_j=V\left(t^2-t-\sum_{i=1}^H y_i f_{j,i}(x)\right)
          \subset\mathbb A^{V+H+1}_\mathbb Z
\]
are smooth with geometrically integral fibers, and their actual lower compact-support realizations are $\mathbb Q_\ell(-H)^{N_j}$. In the category of rational l-adic Frobenius representations, an injection between these realizations exists if and only if $N_1\leq N_2$. This equivalence holds for every prime with identical geometric parameters, and for the anti-invariant quadratic-character realizations at every odd prime. The scheme construction, relative trace and projectors are those proved in NN-C027, with exact SGA4 XVII5.2.6/5.2.8 and XVIII2.8.1/2.9 interfaces. Parsimonious padding proves that the geometric dictionary preserves the relevant counts and common Tate twist.

Thus even on this actual pure Tate subcategory, a succinct defining-equation presentation can make the existence of a subrepresentation PP-complete. The explicit matrices, once supplied, would be scalar and their rank comparison elementary; obtaining their multiplicities from the equations is the hard operation. Their zeta factors have A-controlled shifted critical lines, but the orders at a fixed nonreal lower-factor zero give precisely the same comparison. This is a theorem about linear injections of cohomology realizations, not about scheme morphisms, algebraic correspondences or orbit-closure containment. No fullness statement for a realization functor is assumed.''',
        inputs)
