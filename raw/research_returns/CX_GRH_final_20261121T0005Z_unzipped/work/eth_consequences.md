# ETH branch: verified consequences and exact limits

Run CX_GRH, 2026-11-20 UTC / 2026-11-21 Europe/Berlin. Author/checker: GPT-6 Astra Pro, `/root/eth_consequences`; inherited effort setting not exposed. This branch uses the attached OpenAI theorem as stipulated. It does not claim to have rerun its Lean formalization or audited the full counting proof.

## Source register and exact locators

| Source ID | Result and exact locator | URL / supplied location | Verification in this run |
|---|---|---|---|
| E-S01 | OpenAI, *The Exponential Time Hypothesis is False*, revised 25 October 2026, Theorem 1.1, source label `thm:main` | `sources/LIT_OpenAI_ETH_is_False/main_full_version.tex`, theorem beginning source line 73; citation in attached README; https://github.com/openai/math/blob/main/preprints/The-Exponential-Time-Hypothesis-is-False-October-25-2026/paper.pdf | Whole statement and its quantifiers read; theorem accepted under task's convention, not re-proved |
| E-S02 | Same, Corollary 1.3, `cor:graph-counting` | Same source, line 151 | Whole statement and proof read |
| E-S03 | Same, Corollary 1.4, `cor:quantitative-circuits`; Appendix C.1 and `quantitative-circuits.tex` | Same source, line 183 and appendix source line 4237; full proof in separate attached file | Whole quantitative witness-circuit proof read, constants and hypotheses checked |
| E-S04 | Same, §1.1.1–1.1.3; Appendix C.1, Corollary C.1, `cor:consequence-circuits`; Appendix C.2, Corollary C.2, `cor:consequence-local-inversion` | Same source | Stated consequences and associated proofs read |
| E-S05 | Ryan Williams, *Improving Exhaustive Search Implies Superpolynomial Lower Bounds*, full author version dated 4 May 2010, Theorems 1.1 (printed p.2), 2.1 (p.7), 6.1 (pp.20–21); published SIAM J. Comput. 42 (2013), 1218–1244 | https://people.csail.mit.edu/rrw/improved-algs-lbs2.pdf ; DOI https://doi.org/10.1137/10080703X | Exact statements located; full proof of Theorem 6.1 read. The unary time hierarchy and general Circuit-SAT implication are cited background, not independently re-proved |
| E-S06 | H. Jahanjou, E. Miles, E. Viola, *Local reductions*, ECCC TR13-099, revision 2 (27 November 2013), Theorem 1 (printed p.2), Corollaries 2–3 (p.3), §6 (pp.17–20) | https://eccc.weizmann.ac.il/report/2013/099/revision/2/download/ | Exact locality/size statement checked against its use in E-S03; theorem itself carried as background |
| E-S07 | L. G. Valiant, *Completeness classes in algebra*, STOC 1979, Theorem 2, printed p.254 / PDF p.6; §3, pp.251–253 defines p-definability | https://sites.math.washington.edu/~billey/colombia/references/valiant.completeness.1979.pdf ; DOI https://doi.org/10.1145/800135.804419 | Exact permanent completeness statement located |
| E-S08 | P. Bürgisser, *Completeness classes in algebraic complexity theory*, arXiv:2406.06217v1 (10 June 2024), Definition 2.9 (p.6), Definition 2.25 (p.12), Theorems 2.20 (p.10), 2.29 (p.13), and 7.3 (p.37) | https://arxiv.org/pdf/2406.06217 | Definitions and distinctions VP/VBP/VNP/border checked; theorem statements used as background |
| E-S09 | K. Mulmuley, GCT V, attached revision: Theorem 1.7 (`tintronnldetnew`), Theorem 2.4 (`trussell2`), Theorem 5.11 (`tnnlexpfull`), Theorem 5.14 (`tequisdit`) | `sources/LIT_Mulmuley_GCT_V_Noether_normalization/main.tex`; theorem-number map supplied and independently verified by `/root/koiran_gct` | Relevant algebraic hypotheses read directly in attached source |

Web retrieval references, for parent use only: E-S05 `turn286897418view0`, `turn360371688view0`, `turn360371688view1`, `turn351462366view0`; E-S06 `turn286897418view1`, `turn360371688view2`, `turn360371688view3`; E-S07 `turn623673830view1`, `turn811385652view0`; E-S08 `turn623673830view0`, `turn811385652view1`–`turn811385652view4`, `turn351462366view1`. Parent must open refs itself before using web citation widgets. In the paper use ordinary bibliography and locators. Keep derivative prose from each external web source within its 200-word budget; the substantial arguments below are direct deductions from attached material or original elementary transfer proofs.

## E-S01: the quantitative premise

For each **fixed** integer (k\ge2), the attached Theorem 1.1 supplies a deterministic exact counter for a (k)-CNF with (n\ge20) declared variables and (m) input clauses, using

\[
 T_k(n,m)=(n+m)^{O_k(1)}\,2^{O_k(n\log\log n/\sqrt{\log n})},
 \qquad S_k(n,m)=(n+m)^{O_k(1)}.
\]

For each fixed (D>0), when (m\le Dn), its stronger bound is

\[
 T_{k,D}(n,m)=(n+m)^{O_{k,D}(1)}\,2^{O_{k,D}(n/\sqrt{\log n})}.
\]

The stated bit model and declared-variable convention matter for exact counts. There is no claimed uniform control in (k=k(n)). For a fixed (k), repeated clauses may be removed and tautologies discarded without changing the answer; there are at most \(\sum_{j=0}^{k}2^j\binom nj=n^{O_k(1)}\) distinct non-tautological clauses. Reading an arbitrarily repeated input still costs polynomial time in its supplied length. Everywhere below “subexponential” means (2^{o(n)}) in the explicitly named parameter, **not** the sometimes-used complexity class \(\bigcap_{\epsilon>0}\operatorname{DTIME}(2^{n^\epsilon})\).

## CX-E01 — Exact refutations of exponential-time hypotheses

**Finding.** E-S01 refutes deterministic ETH, \(\#\mathrm{ETH}\), SETH, counting SETH in its analogous fixed-width formulation, bounded-error randomized versions of these hypotheses, Gap-ETH, and NSETH. The logical conditional lower-bound theorems previously based on those hypotheses remain true implications; their premises no longer supply a hardness conclusion. The result itself supplies neither (\mathrm P=\mathrm{NP}) nor (\mathrm P\ne\mathrm{NP}).

**Proof.** For fixed (k), put (h_k(n)=C_k n\log\log n/\sqrt{\log n}), where (C_k) is a constant large enough for the exponent in E-S01. Since (h_k(n)/n\to0), exact counting takes (2^{o(n)}(n+m)^{O_k(1)}). Its count is positive exactly for satisfiable formulas and zero exactly for unsatisfiable formulas. Taking (k=3) therefore contradicts the asserted positive exponential rate in both ETH and \(\#\mathrm{ETH}\).

For SETH, use its precise quantifiers: for every (\epsilon>0), some fixed (k) has no algorithm of time (2^{(1-\epsilon)n}(n+m)^{O(1)}). Choose (\epsilon=1/2). For **each** fixed (k), the algorithm just obtained has (h_k(n)\le n/2) for all sufficiently large (n). Finitely many smaller values are absorbed into the (k)-dependent constant. Thus for every fixed (k) such an algorithm exists, with the same exponential coefficient (1/2); SETH is false. Its negation does not require the polynomial prefactor, constants, or threshold in (n) to be independent of (k). The same reasoning applies to the counting version.

A deterministic algorithm is also a randomized algorithm with error zero, so the corresponding bounded-error hypotheses are false. For Gap-ETH, on a promised instance return YES exactly when the count is positive. This distinguishes a satisfiable 3-CNF from every 3-CNF whose assignments all violate at least a fixed positive fraction of the clauses. In the usual linear-density promise (m=O(n)), the second bound of E-S01 is directly (2^{o(n)}\operatorname{poly}(n)); no approximation algorithm or reduction is needed. Finally, the zero-count test is a deterministic, hence nondeterministic, subexponential algorithm for fixed-width CNF unsatisfiability, refuting NSETH.

An implication (H\Rightarrow B), conjoined with (\neg H), entails neither (B) nor (\neg B): both assignments to (B) satisfy the two formulas. This proves the precise propositional limitation on using an old conditional lower bound after the refutation of its hypothesis. It is **not** a claim that independence of every target hardness conjecture has been proved. The given upper bound is not a polynomial bound: (n\log\log n/(\sqrt{\log n}\log n)\to\infty). An upper bound also supplies no superpolynomial lower bound for SAT. Consequently neither side of P versus NP is established by these deductions. □

**Scope.** This does not refute the statement that *unrestricted-width* CNF-SAT has no (2^{(1-\delta)n}\operatorname{poly}(n,m)) algorithm, because the theorem does not permit (k) to grow with (n). Nor does the loss of SETH logically refute OVC, 3SUM, APSP, or (\mathrm{FPT}\ne\mathrm{W[1]}). An implication from SETH to a weaker conjecture has the wrong direction for that inference. Unconditional bounds, NP-hardness reductions, and bounds conditional on independent assumptions remain as before.

## CX-E02 — What transfers to a target problem

**Finding.** Let a problem on inputs of length (L), with parameter (u), have a polynomial-time reduction to fixed-width (k)-CNF with (N\le a u+b) variables and at most (L^{O(1)}) clauses, where (a,b,k) are fixed constants. Then it is decidable in

\[
 L^{O(1)}2^{O(u\log\log u/\sqrt{\log u})}
\]

time and polynomial space. If the reduction is parsimonious, the same bound computes the associated witness count. If it additionally gives (M=O(N)), the “log log” factor is absent. Polynomially many such oracle queries are allowed. This is the requisite direction of reduction; a hardness reduction from SAT to a target is not a reduction from that target to SAT.

**Proof.** Construct the CNF, run E-S01, and map its answer back. For (N\le au+b), monotonicity beyond a constant threshold gives (N\log\log N/\sqrt{\log N}=O(u\log\log u/\sqrt{\log u})). The polynomial prefactor is (L^{O(1)}), since a polynomial-time reduction cannot produce more than polynomially many bits. For a parsimonious map the solution counts agree; no multiplicity correction is needed. The linear-clause assertion uses the second part of E-S01. Reusing the workspace between polynomially many calls preserves polynomial space, and their number is absorbed by the polynomial factor. □

If instead a reduction gives (N=\Theta(u^c)) with (c>1), its resulting exponent can be (\Theta(u^c\log\log u/\sqrt{\log u})), which is not (o(u)). Thus ordinary polynomial completeness alone does not establish a (2^{o(u)}) algorithm. Similarly, a running time (2^{o(v)}) in a graph's vertex count is not a bound (f(k)v^{O(1)}), and does not settle the FPT status of Clique with parameter (k). A treewidth-based lower bound also cannot be replaced by (2^{o(t)}\operatorname{poly}(v)) merely by constructing a formula with (O(v)) variables.

**Concrete transfers.** The attached Corollary 1.3 already gives (2^{o(v)}) exact counting for independent sets and fixed-(q) graph colorings, and (2^{o(v+e)}) counting of perfect matchings. Bounded-set-size Set Splitting has one Boolean variable per universe element and, for each set, the all-positive and all-negative clause; this is a direct fixed-width parsimonious encoding. These are actual algorithmic consequences. No subquadratic algorithm for Edit Distance, LCS, or arbitrary Orthogonal Vectors is produced merely by deleting their SETH premise.

**Additional proved example (optional in main paper).** Counting (k)-cliques in a graph with (v) vertices is possible in (\operatorname{poly}(v+e)2^{O(v\log\log v/\sqrt{\log v})}), uniformly in (0\le k\le v). Use one selection bit per vertex, impose a 2-clause (\neg x_u\vee\neg x_w) for every nonedge, and a circuit asserting that exactly (k) bits are 1. The population count can be computed by a balanced tree of binary additions with (O(v)) gates: at level (j), (O(v/2^j)) additions of (O(j))-bit numbers cost (O(vj/2^j)); summing over (j) is (O(v)). Comparison with the fixed input integer (k) adds (O(\log v)) gates. Give every gate its unique-value 3-CNF truth-table constraints. There are (O(v)) variables and (O(v^2)) clauses, each clique determines exactly one extension, and E-S01 applies. This is subexponential in (v), with no implied FPT running time in (k).

## CX-E03 — The exact Circuit-SAT speedup, and its limit

**Finding.** E-S01 yields a deterministic algorithm for satisfiability (and exact input-assignment counting) of an arbitrary fan-in-two Boolean circuit with (n) inputs and (s) noninput gates in time

\[
 (n+s)^{O(1)}2^{O((n+s)/\sqrt{\log(n+s)})}
\]

and polynomial space. In particular, (s=O(n)) gives (2^{o(n)}). This bound does not meet the all-polynomial-size Circuit-SAT premise of Williams's Theorem 1.1.

**Proof.** Introduce a Boolean variable for each input and each gate. A gate's two inputs and one output have eight truth-table assignments, exactly four inconsistent with its truth function; forbid each inconsistent assignment by a clause of width at most three. Constants and unary gates use at most this many clauses. Add the unit clause fixing the output to 1. Thus (N=n+s) variables and (M\le4s+1\le5N) clauses suffice. For every input assignment, the acyclic gate order fixes exactly one value for each gate, so the reduction preserves the number of accepting input assignments. Apply the fixed-density part of E-S01 with (k=3,D=5). □

Williams's Theorem 1.1 asks for a superpolynomial saving over (2^n\operatorname{poly}(n^a)) on circuits with (n) inputs and (n^a) gates **for every fixed (a)**. Substituting (s=n^a) in the proved bound, with (a>1), gives an exponent of order (n^a/\sqrt{\log n}), larger than (n). The exact computational saving needed by that theorem is therefore absent. This diagnoses a failed application; it does not prove that a different route to stronger circuit lower bounds is impossible.

## CX-E04 — A genuine quantitative Boolean circuit lower bound

**Finding.** The supplied result has the following unconditional consequence under the task's theorem convention:

\[
 \exists L\in\mathrm E^{\mathrm{NP}}\ \exists c>0\quad
 C_L(n)>c\,n\sqrt{\log n}\quad\text{for infinitely many }n,
\]

where circuits have arbitrary Boolean gates of fan-in at most two and unrestricted fan-out. In particular, (\mathrm E^{\mathrm{NP}}\not\subseteq\mathrm{SIZE}(O(n))). The stronger quantitative statement is **already** OpenAI Corollary 1.4, not a new result to attribute to this run. The qualitative implication is Williams's Theorem 6.1. The new finding here is the exact transfer/scope classification.

**Proof of the transfer.** The algorithm required by the attached Corollary 1.4 is the fixed-density decision version of E-S01, obtained by testing its count for positivity. The premise is therefore satisfied without GRH and without Masullo. The cited corollary gives the displayed statement. Since (n\sqrt{\log n}/n\to\infty), the same language has no eventual (O(n))-size circuit family. □

**Full-proof check of the cited corollary, not a reprint.** Its Appendix C.1 / `quantitative-circuits.tex` argument was read in full. The following dependencies and quantitative points were checked: Williams's stated unary hierarchy supplies (H\in\mathrm{NTIME}(2^n)\setminus\mathrm{NTIME}(2^{n/2})); Jahanjou–Miles–Viola Theorem 1 with locality parameter 2 gives a clause decoder of (O(n)) output bits, each depending on only a fixed number of the (q=n+O(\log n)) index bits. Support enumeration on constant-Hamming-weight inputs recovers an (O(n))-gate decoder in polynomial time. The bits of the lexicographically first accepting assignment, with (dn)-bit padded variable labels, form a language (W\in\mathrm E^{\mathrm{NP}}). A hypothetical size (s_n=\lfloor\eta n\lfloor\sqrt{\log_2 n}\rfloor\rfloor) circuit for (W) is guessed; three copies plus the decoder test whether a clause is violated. Its 3-CNF encoding has (U_n=(3\eta+o(1))n\sqrt{\log_2 n}) variables and at most (5U_n) clauses. The fixed-density SAT cost is (2^{(3A\eta+o(1))n}); choosing (\eta<1/(12A)) leaves sufficient margin below (2^{n/2}), including polynomial overhead. This contradicts the hierarchy and yields the claimed infinitely-often lower bound. No gap was found in this cited implication proof. The proof of the underlying counter, the unary hierarchy, and the local-reduction theorem was not independently re-proved here.

This is a lower bound in (\mathrm E^{\mathrm{NP}}), not one in NP; it is against linear or nearly linear Boolean circuits, not against every polynomial-size circuit family. It supplies no arithmetic-circuit lower bound for the permanent.

## CX-E05 — The permanent: a concrete sparse numerical consequence

**Finding.** If (A\in\{0,1\}^{r\times r}) has (e) nonzero entries, its integer permanent can be computed in

\[
 \operatorname{poly}(r+e)\,2^{O((r+e)/\sqrt{\log(r+e)})}
\]

time and polynomial space. In particular, (e=O(r)) gives (2^{O(r/\sqrt{\log r})}\operatorname{poly}(r)). This specializes and sharpens the displayed quantitative form of the already-cited matching consequence in OpenAI Corollary 1.3, using the sharper fixed-density part of Theorem 1.1.

**Proof.** View the matrix as a bipartite graph with (2r) vertices and (e) edges. Introduce an edge-selection bit (x_f) for each edge. At each vertex of degree (d), test that exactly one incident bit is 1 by maintaining two bits: (a_i), asserting that some of the first (i) edges is selected, and (b_i), asserting that at least two are selected. Initialize (a_0=b_0=0) and update

\[
 a_i=a_{i-1}\vee x_i,\qquad
 b_i=b_{i-1}\vee(a_{i-1}\wedge x_i).
\]

Then exactly one is selected precisely when (a_d\wedge\neg b_d=1). This costs (O(d+1)) fan-in-two gates. Sum degrees over all vertices to obtain (O(r+e)) gates, including conjunction of all vertex tests. An isolated vertex can instead be rejected immediately. Apply the parsimonious gate encoding of CX-E03. There are (N=O(r+e)) variables and (M=O(N)) clauses, and each perfect matching gives one satisfying assignment. Conversely every satisfying assignment selects a perfect matching, with uniquely determined gate values. The number of bipartite perfect matchings is the defining permutation sum \(\operatorname{per}(A)=\sum_{\sigma\in S_r}\prod_i A_{i,\sigma(i)}\). The fixed-density bound gives the result. □

For dense matrices (e=\Theta(r^2)), this particular encoding has (\Theta(r^2)) variables. It does not yield (2^{o(r)}) time in matrix dimension. It also does not provide an arithmetic circuit for the formal polynomial \(\operatorname{per}_r(X)\), whose (r^2) indeterminates are left symbolic. Numerical Boolean counting and symbolic polynomial computation are different assertions.

## CX-E06 — VP, VNP, and the surviving GCT hypotheses

**Finding (precise scope, not an independence claim).** Neither (\mathrm{VP}=\mathrm{VNP}) nor (\mathrm{VP}\ne\mathrm{VNP}), neither polynomial arithmetic circuits for the permanent nor a superpolynomial permanent lower bound, is established by CX-E01–E05. The SAT theorem does not discharge the border-hardness or black-box PIT assumptions used in GCT V Theorems 1.7, 2.4, 5.11 and 5.14.

**Dictionary and proof of the scope statement.** Fix a field (K). VP comprises polynomial-degree families with polynomial-size arithmetic circuits. VNP comprises the families obtained as Boolean-cube sums of such efficiently computed polynomial families. For characteristic other than two, the permanent is VNP-complete under polynomial projections (Valiant Theorem 2; modern statement Bürgisser Theorem 2.29). The determinant is complete for VBP, the weakly skew/branching-program subclass (Bürgisser Theorem 2.20); it should not be silently identified with the whole of VP. The border orbit-closure formulation concerns the closure of this model (Bürgisser Theorem 7.3).

The OpenAI algorithm accepts a finite bit-string description of a fixed-width CNF and returns one integer. Its theorem does not construct, from a symbolic arithmetic verifier \(g_n(X,Y)\), a small arithmetic circuit computing \(\sum_{Y\in\{0,1\}^{p(n)}}g_n(X,Y)\) as a polynomial in (X). The sparse numerical permanent reduction above also returns only the value at a supplied 0–1 matrix. The Boolean lower bound in CX-E04 is for a language in (\mathrm E^{\mathrm{NP}}) and a size threshold near (n\), and has neither the arithmetic model nor the target family of a permanent lower bound. Thus the premises of the cited algebraic implications are not supplied by these deductions.

There is also a separate quantitative mismatch. GCT V Theorem 1.7 assumes that for some fixed (\epsilon>0), the permanent cannot be approximated infinitesimally by affine-linear symbolic determinants of size at most (2^{r^\epsilon}). Even **if** a separate argument converted the SAT speedup into a symbolic upper bound (2^{O(r/\sqrt{\log r})}), it would not refute a lower bound (2^{r^\epsilon}) for (0<\epsilon<1), because

\[
 \frac{r/\sqrt{\log r}}{r^\epsilon}
 =\frac{r^{1-\epsilon}}{\sqrt{\log r}}\longrightarrow\infty.
\]

Moreover that symbolic conversion has not been established. Consequently the correct report is a missing arithmetic conversion/gate, not a claim of proved formal logical independence. □

The GCT consequences of removing GRH from a particular normalization theorem are a separate question from these hardness/PIT assumptions. Improving an upper bound for computing systems of parameters does not itself produce the orbit-closure noncontainment required for the permanent lower bound.

## CX-E07 — Exact scheme and K-theory formulation of the counting theorem

**Finding.** Every Boolean (k)-CNF (F) has an explicitly presented affine scheme

\[
 X_F=\operatorname{Spec}\frac{\mathbb Z[x_1,\ldots,x_n]}
 {(x_i^2-x_i\ (1\le i\le n),\;\prod_{\ell\in C}(1-\ell(x))\ (C\text{ a clause of }F))},
\]

where a positive literal is (\ell(x)=x_i) and a negative literal is (\ell(x)=1-x_i). It is the disjoint union of exactly \(\#F\) copies of \(\operatorname{Spec}\mathbb Z\). Hence (p:X_F\to\operatorname{Spec}\mathbb Z) is finite étale and

\[
 \operatorname{rank}_{\mathbb Z}p_*\mathcal O_{X_F}=\#F,
 \qquad [p_*\mathcal O_{X_F}]=\#F[\mathcal O]\in K_0(\mathbb Z).
\]

The theorem computes this rank from the displayed bounded-degree presentation with the same quantitative guarantees as E-S01. Decision asks whether the finite étale scheme is empty; witness search selects one component; exact counting computes its degree.

**Proof.** The ideals \((x_i)\) and \((x_i-1)\) in (\mathbb Z[x_i]\) are comaximal. Applying the Chinese remainder theorem in each variable gives

\[
 B:=\mathbb Z[x_1,\ldots,x_n]/(x_i^2-x_i)_i
 \simeq\prod_{a\in\{0,1\}^n}\mathbb Z,
\]

by evaluation at all Boolean assignments. The polynomial attached to a clause evaluates to 1 exactly at assignments violating that clause, and to 0 at assignments satisfying it. Quotienting a product factor by a 1 removes that factor; quotienting it by 0 leaves it. Imposing all clause polynomials thus leaves exactly the satisfying-assignment factors. Each surviving factor is a copy of (\mathbb Z\), proving the scheme, finite étale, rank and (K_0\) assertions. The same finite bit-string data determines the CNF and the displayed scheme, so running E-S01 computes this rank with no change in parameters beyond fixed encoding constants. □

**Further exact translations.** In the λ-ring of vector bundles on \(\operatorname{Spec}\mathbb Z\),

\[
 \lambda_t([p_*\mathcal O_{X_F}])=(1+t)^{\#F}.
\]

This follows because the bundle is free of rank \(\#F\), and its (j)-th exterior power is free of rank \(\binom{\#F}{j}\). On a finite field fiber all components are rational over the base field. Its geometric ℓ-adic cohomology (after base change to an algebraic closure) has (H^0) of dimension \(\#F\), Frobenius acts as the identity, and all other geometric cohomology vanishes. Its zeta function is \((1-t)^{-\#F}\); this is weight zero, without a new weight or purity theorem. Its reduced rank class in (K_0(\mathbb Z)\) is zero, so no nonzero γ-filtration class is being constructed by this translation. These statements can be proved directly from the disjoint-union decomposition; no motive beyond a sum of unit motives is needed.

Root should supply the exact Grothendieck archival/SGA locators from its dictionary section. The proof here is elementary and does not invent an archival attribution.

## CX-E08 — Why this dictionary does not manufacture a GCT obstruction

**Finding.** A fast computation of the rank in CX-E07 is not, by the displayed dictionary, a construction of a separating representation in an orbit-closure coordinate ring.

**Exact comparison.** Let (G=\mathrm{GL}_{m^2,\mathbb Z}\), let (V=\operatorname{Sym}^m((\mathbb Z^{m^2})^*)\), and take the schematic image/closure of the determinant orbit map (G\to V\). After base change to characteristic zero, a proposed containment of a padded permanent orbit closure in the determinant orbit closure gives a (G)-equivariant quotient map between their coordinate rings. In each finite homogeneous degree, semisimplicity in characteristic zero makes the target representation's multiplicity of every simple constituent at most that of the source. A reversed inequality would obstruct the containment. This is a statement about graded representation modules, hence their classes in the representation Grothendieck group with its λ-operations, not just their total ranks.

The input and output of CX-E07 are instead a bounded-degree Boolean presentation and one nonnegative integer \(\#F\). Its decomposition into unit components provides no graded (G)-representation, no map of coordinate rings, and no inequality of Schur multiplicities. Therefore no such obstruction is obtained from this dictionary. This is a verification of the data required by the two constructions; it does not preclude a new substantive construction relating them. The missing gate is precisely a proof producing those representations or coordinate-ring equations with the complexity required by GCT V. □

## Proof-check ledger for this branch

All proofs CX-E01–E08 were read from beginning to end after drafting. The check was a targeted mathematical proof check by the authoring agent, not an independent-agent reproof and not a formal certificate. Checked matters include SETH quantifier order, the input-clause polynomial factor, Gap-ETH promise direction, parsimonious gate constraints, exact-one verifier invariants, constant-density use, distinction of numerical and symbolic computation, the CRT over \(\mathbb Z\), and characteristic-zero semisimplicity in the optional GCT dictionary. No gap was found in those stated deductions. The source theorem E-S01 remains a stipulated theorem. No claim is made that the entire new OpenAI preprint, its Lean code, or any proof of ETH falsity was revalidated.

Questions of whether the theorem can be extended uniformly to growing width, improved to all polynomial-size Circuit-SAT in the number of *inputs*, converted to arithmetic-circuit compression, or turned into a GCT obstruction remain mathematical gates; no theorem of impossibility is claimed for those extensions. No untried elementary reduction in this branch is being silently called a nonimplication.
