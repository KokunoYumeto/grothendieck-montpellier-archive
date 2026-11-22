# Pending A131: explicit effective simplicial models and all homotopy-group presentations

Status: construction under independent audit, not promoted and not counted as progress. The target is a complete effective presentation, not finite invariant factors or a decision procedure for isotopy.

## 1. Finite input and precise target

Input: a finite abstract simplicial complex K, with ordered vertex set {1,...,v}, promised to be a closed PL manifold when manifold comparison theorems are used. The coding algorithm itself works for every finite polyhedron and does not need an algorithm recognizing the manifold promise.

Realize each vertex as the corresponding standard basis vector of Q^v. Put Z=|K|×I and A=|K|×{0}. For q≥0 put D_q=Z×Δ^q, using the standard rational simplex with q+1 barycentric coordinates. The q-simplices of the target concordance group are homeomorphisms D_q→D_q preserving the complete Δ^q coordinate, fixing A×Δ^q pointwise, and preserving the top Z_top=|K|×{1} setwise. In the manifold case the last condition is automatic; it is convenient to include it explicitly. Top is not fixed pointwise. For this first theorem B is closed, so no side-boundary convention is needed.

F=Q^rc, the ordered field of real algebraic numbers. Each element has a finite canonical code: primitive irreducible polynomial in Z[T] with positive leading coefficient, together with the ordinal of its real root. Arithmetic, sign, equality and enumeration are effective (Sturm/root-isolation algorithms). No arbitrary real constants are used.

## 2. PL graph codes, with only linear arithmetic

A raw q-code is a finite list of finite nonempty lists of points in F^(2(v+1)+q+1). Each list spans a closed simplex; degenerate lists can either be rejected by affine-rank testing or retained as convex polytopes. The union Γ lives in coordinates (z,z',t), so the parameter is literally shared.

Requirements, expressed as finite first-order LINEAR formulas over F:

1. Every point of Γ has z,z'∈Z and t∈Δ^q.
2. For every (z,t)∈D_q there is exactly one z' with (z,z',t)∈Γ.
3. For every (z',t)∈D_q there is exactly one z with (z,z',t)∈Γ.
4. If z∈A then z'=z; conversely the bijection then fixes A pointwise.
5. z lies on the top if and only if z' does.

Simplex membership is a barycentric-coordinate formula using constant algebraic vertex coordinates; all variable occurrences are linear. Domain membership is a finite union of fixed rational simplex×interval×simplex predicates. Linear quantifier elimination, for example exact Fourier–Motzkin with Boolean normal forms and equality handling, decides every requirement and equality of two graphs. Full polynomial CAD is not required for PL.

WHY THIS IS PL: each projection Γ→D_q is bijective. Its restriction to every input simplex is therefore affine and injective, so its inverse on the projected simplex is affine. Projected simplices form a finite polyhedral cover. Refining all their mutual intersections and triangulating gives a finite PL subdivision over F; the maps and inverse are affine on its cells. Finite closed-cover gluing proves continuity without assuming ordinary compactness of an arbitrary real closed field. Thus no untested homeomorphism, local-flatness, isotopy, or manifold-recognition predicate is hidden in validity.

A finite union of graph simplices is allowed even when the raw list is not already a complex. Equality of graphs is decidable. Give raw finite strings an explicit length-lexicographic enumeration. A canonical code is the least valid code for that graph. Given a raw valid code c, canonicalization scans finitely many strings ≤c. Equivalently the canonical-code predicate is decidable.

## 3. Effective strict simplicial group operations

Inverse: swap z,z'.

Product (p after q): Γ_pq(x,z,t) iff ∃y [Γ_q(x,y,t) and Γ_p(y,z,t)]. This is still linear definable. It is the graph of a PL map because finite polyhedral intersections refine both affine maps. It therefore has a finite graph-simplex code with coefficients in F.

For an order-preserving α:[m]→[q], the induced affine simplex map α_*:Δ^m→Δ^q has integer coefficients. Pullback is Γ_α(x,y,s) iff Γ(x,y,α_*(s)). It includes the D_m constraints. This covers both face and degeneracy operators, including noninjective α. It is again a bounded finite semilinear graph and hence has a finite graph-simplex code over F.

To output a code after any operation, enumerate all valid raw codes of the target arity and stop at the first whose graph equals the displayed formula. Equality is decidable; existence follows from the finite polyhedral proof, so the search halts. This is an actual total algorithm, not an assumed ability to find a triangulation. The first successful code is canonical. Graph equality makes all group and simplicial identities strict on canonical codes.

Call the resulting explicitly coded simplicial group G_PL(K). It is literally isomorphic to the PL concordance simplicial group over F. A115 supplies the weak equivalence to the real PL concordance group and the comparison over every real closed field.

## 4. SA graph codes

Replace finite graph simplices by finite Boolean formulas in polynomial equalities/inequalities with coefficients in F. Quantifiers in raw formulas are harmless, since RCF QE removes them; one can restrict codes to quantifier-free formulas from the start.

Require the same graph, bijection, parameter, bottom and top conditions. Add joint continuity of graph-function AND inverse, expressed with epsilon-delta first-order formulas, for example for every graph pair (x,y,t), every epsilon>0 admits delta>0 such that every other graph pair within delta in (x,t) has its (y,t) image within epsilon. Use squared Euclidean distances so every condition is a polynomial formula. This excludes merely fibrewise-continuous families. RCF QE decides validity and equality.

Composition, inverse and simplicial pullback are finite formulas. Continuity and homeomorphism closure prove validity; QE/canonical search outputs a least equivalent valid code. This gives G_SA(K), literally the semialgebraic concordance simplicial group over F. A116 supplies its weak equivalence to the real SA group, and all real-closed-field SA groups. PL graph formulas give a computable strict simplicial homomorphism G_PL(K)→G_SA(K), not an unproved weak equivalence.

## 5. Explicit presentations of every homotopy group

For a coded simplicial group G, define Z_0=G_0. For r≥1 define Z_r={a∈G_r : d_i a=1 for 0≤i≤r}. For r≥0 define N_{r+1}={u∈G_{r+1}: d_i u=1 for 1≤i≤r+1}. These sets of canonical codes are decidable, and all indicated products and faces are computable.

The Moore theorem identifies π_r|G| with Z_r / d_0 N_{r+1} (with the usual r=0 convention). The boundary subgroup is normal; d0 N_{r+1} is generally only recursively enumerable, not decidable.

Presentation Π_r(K):
- one generator x_a for every a∈Z_r;
- x_1=1;
- x_a x_b=x_(ab) for every a,b∈Z_r;
- x_(d0 u)=1 for every u∈N_{r+1}.

All indices and relators are generated by a uniform algorithm from (K,r). It presents the WHOLE quotient, not just a subgroup. For r≥1 the resulting group is abelian; one can equivalently output the countable integer relation matrix with rows e_a+e_b−e_ab and e_(d0u). No claim of a terminating word problem, finite presentation, finite rank, invariant factors, or efficient computation is made.

A113 identifies Π_0^PL(K) with π0 of the stipulated definable concordance group for every real closed field and fixed o-minimal expansion. In real dimension≥5 the checked PL–TOP weak equivalence identifies ALL Π_r^PL(K) with the corresponding TOP homotopy groups. In the low-dimensional excluded TOP ranges this does not assert such a comparison. Every Π_r^SA(K) computes the SA group by A116, independently of whether PL→SA is surjective.

## 6. Critical scope: what is and is not a computation

This produces finite integer/algebraic combinatorial syntax, a terminating validity/equality checker, total algorithms for every operation, and a complete recursively enumerable presentation of every homotopy group. It is stronger than saying 'the answer is the concordance group' or indexing relations by unspecified isotopies: every proposed simplex and every relator has a finite decidable algebraic certificate, and the input is only the finite K.

It remains a universal exhaustive presentation. It does not reveal a finite invariant decomposition, solve its word problem, or give a structural K-theoretic calculation. The group presentations use the Moore construction once the independently effective simplicial model is built. Whether this meets the user's intended 'compute' criterion should be judged explicitly by the parent; it must not be quietly promoted as if all structural invariants were now evaluated.

The arbitrary o-minimal higher-space problem remains: A116 concerns semialgebraic families, and arbitrary expansions need not have a real model. No arbitrary-definable higher simplicial group has been effectively reduced to real-algebraic graph formulas here. Likewise the PL→SA weak-equivalence decision remains separate, even though its entire map is explicitly coded.

## 7. Independent finite checker target

Tensor/finite agent is implementing a rational instance of the PL graph checker. Suggested nontrivial joint-family test for B=point, Z=I:
 h_t(x)=x+epsilon min(x,1−x,t,1−t), 0<epsilon<1.
This is jointly PL in (x,t), fixes x=0,1, and restricts to identity at t=0,1. Its 2-simplex analogue uses min(x,1−x,t0,t1,t2). Test graph validity, both projections, equality under subdivision, multiplication, inverse, faces, degeneracy pullback, and rejection of folding/non-surjective/discontinuous or wrong-parameter candidates. This is not a test of the entire infinite theorem, but an actual executable verification of the finite code mechanism.
