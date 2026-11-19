# Mathematical checks for the two middle SA08 packets

Checked 2026-11-19 by GPT-6 Astra Pro; effort not exposed by runtime; SA08/middle.

This appendix separates direct arguments from finite certificates and source comparisons. `middle_math_checks.py` is the retained program; its actual output is `computation_results.json` and `logs/middle_math_checks.log`. No computation decides an uncertain manuscript reading. P denotes `MPL_136_095-141_transcription.tex`; Q denotes `MPL_136_189-234_transcription.tex`. Neither original manuscript scans nor a second-pass transcription were supplied. Published scans used for source comparison are not scans of these archival leaves.

## 1. Flat acyclicity, explicit homotopy, and the special algebra

**C104; P scan100, lines132–137.** Fix a prime p and let F be the direct sum of copies of Z with basis e_n, n≥0. Define u(e_n)=e_n−p e_(n+1) and v(e_n)=p^(−n) in Z[1/p]. Then

\[
0\longrightarrow F\xrightarrow{u}F\xrightarrow{v}\mathbb Z[1/p]\longrightarrow0
\]

is exact. Injectivity of u follows by looking at the highest nonzero index in a finitely supported vector. The cokernel has the presentation e_n=p e_(n+1), hence is Z[1/p]; v is onto. All three terms are flat. A section of v would give a nonzero map Z[1/p]→F, but an image of 1 would have to be divisible by every p^n in F and must therefore be zero. Thus the exact complex is not contractible: a contraction would split the terminal surjection. This is an independent counterexample to the *chain-complex* inference acyclic and flat ⇒ contractible. It does not silently identify the manuscript's universally flasque sheaf notion with ordinary acyclicity. The writer's retraction already appears on the page. No finite numerical computation was used for this proof.

**C101, C153.** For a module extension kT→Φ→Ψ, the free alternating graded PD algebra is Γ(Φ)⊗Λ(Ψ), with the selected PD ideal. The quotient q:Φ→Ψ defines dφ=qφ and dψ=0. The extension to divided powers is dγ_n(φ)=γ_(n−1)(φ)qφ, and the exterior sign rule defines d on products. On generators d²=0; on a divided power the possible extra factor contains qφ∧qφ=0. The universal property then gives the canonical map whenever the target satisfies these same graded PD identities. This proves the universal algebra construction. It does not prove a comparison theorem from flatness alone or fill every inhomogeneous axiom asked about on Q217.

**C105; P102.** Evaluation in simplicial degree0 has a right adjoint sending M to the simplicial module with degree-n value M^(n+1), with coordinate maps induced by maps of vertices. A simplicial map A→M^(•+1) is determined by its degree0 component A_0→M: the j-th coordinate in degree n is the composite with the j-th vertex. Conversely those coordinates satisfy all simplicial identities. This is a natural bijection on Hom sets, hence the adjunction. It does not establish any higher uniqueness of the localization category.

**C166; Q227.** A simplicial homotopy is a collection of maps satisfying specified equalities between composites of faces, degeneracies, and homotopy maps. Applying *any ordinary functor* preserves those equalities. Consequently an explicitly given simplicial contraction remains a contraction after applying Γ^i, Sym^i or Λ^i, for i>0, since these functors send the zero object and zero map to zero. This applies to the actual Φ contraction on the page. It is not an assertion that nonadditive functors preserve arbitrary quasi-isomorphisms.

## 2. Representability and coefficient structures

**C117–123, C189–192; P123–135.** For any k-module M, the affine functor V(M)(R)=Hom_k(M,R) is represented by Sym_k(M). Its R-module structures are natural in commutative k-algebras R. An R-bilinear multiplication on V(M)(R), natural in R, corresponds to a map M→M⊗M: bilinearity forces degree1 in each family of affine coordinates. Associativity, commutativity, and a unit translate by Yoneda into coassociativity, cocommutativity, and a counit. The same reasoning with homogeneous polynomial operations translates γ_i into a map M→Sym^i(M). The homogeneity assertion follows from γ_i(a x)=a^iγ_i(x), tested over R[a]; equality of coefficients of powers of a separates the homogeneous degrees even over rings with torsion. These are statements about natural affine operations, not arbitrary functions on k-points.

Eliminate X_n by t−Σ_(j<n)X_j and dX_n by −Σ_(j<n)dX_j. A completed form has one coefficient for each ordinary monomial index and exterior subset. Hence its representing module is

\[
S\otimes_k k[Y_0,\ldots,Y_{n-1}]\otimes_k\Lambda(y_0,\ldots,y_{n-1}).
\]

Its linear dual into R is a product indexed by those monomials. A linear dual of an infinite direct sum is a product, with no finite-projective assumption needed for that elementary equality. One must not replace it by an ordinary polynomial direct sum. Multiplication, differential, PD operations and simplex maps on the functor give the asserted coalgebra, codifferential and coPD structure on the representing module by the same Yoneda argument. All equations must already hold on the algebra-valued functor; Yoneda does not create a missing compatibility equation. This delimits the independent formal proof of the “all structures” assertion on P133.

**C118.** Restriction Hom_k(S,R)→Hom_k(Sbar,R) need not be onto when Sbar→S is injective. For 2Z⊂Z and R=Z it is multiplication by2 after identifying each Hom group with Z, hence misses1. This is a counterexample to the implied Hom-exactness step, not an example satisfying every coPD coefficient axiom. A split inclusion, as in k⊂k[u], removes that particular problem.

**C119–120.** For an ordinary diagram D of modules, Hom(colim D,R)=lim Hom(D,R), naturally. Thus extension from the simplex category by the stated ordinary colimit has the formal representing property. For the empty simplicial set the colimit is0, so a claimed injection of a fixed nonzero Sbar into every such object requires an exception or different definition. Preservation of structured coefficient colimits, derived invariance, and exactness of completion do not follow from this Hom identity.

For primitive u, Δu=u⊗1+1⊗u, and therefore Δu^n=Σ binom(n,a)u^a⊗u^(n−a). Dual basis elements T^(a) multiply by binom(a+b,a). The program recomputes the coefficients2,6,10,35,70 at selected indices. Weight of X^(i) is i times the weight of X; d preserves total weight and raises exterior degree. Scalar extension on the free integral model commutes with its ordinary colimit. An arbitrary coefficient abelian group has external pairings into tensor-product coefficients; no internal ring product is supplied without a multiplication on that group.

**C188; P121.** If each admissible augmented theory is already known to have the two natural τ∞ comparison isomorphisms on every X, a morphism of admissible theories respecting augmentation induces a map between two objects identified with τ∞RΓ(X,S_k). The commutative comparison diagram and two-out-of-three make that map an isomorphism. This proves the formal implication under the stated comparison axioms. It does not establish the manuscript's proposed τ∞ category: the earlier negligible/thick claim has a separate defect recorded by the early-package agent. Nor does it produce common refinements or equalizers.

## 3. Translation invariants and exterior degree

**C125; P139.** Let D=Σ∂/∂Y_i−∂/∂U and define its Hasse operators by the coefficients in f(Y_i+h,U−h). Set Z_i=U+Y_i. This is an invertible change of polynomial coordinates, over any base ring. It transforms the translation to Z_i fixed, U→U−h. If all positive Hasse operators vanish, f(Z,U−h)=f(Z,U). The coefficient of the highest power of h contributed by a positive highest U-degree term is its nonzero leading coefficient up to sign; equality forces that coefficient to vanish, a contradiction. Thus f is independent of U. Conversely every polynomial in the Z_i is invariant. This proves the all-Hasse assertion over arbitrary rings. The program checks a degree5 invariant and verifies that in characteristic5 the ordinary derivative of U^5 is0 whereas its fifth Hasse derivative is1. A kernel-of-D-only version is false in characteristic p.

**C126; P139.** In V*=k^(n+1), the kernel K of coordinate summation has basis e_j−e_n, 0≤j<n. Appending e_n gives a unimodular basis of V*. Thus K is free of rank n, and Λ(V/k·Σe_i)^* identifies degreewise with ΛK. Its top degree is n, not n−1. With the chosen volume/orientation the determinant relation uses Λ^nK and Λ^(n+1)V*. Six exact determinant computations give1; the displayed triangular basis proves the assertion for every n and every k. Signs still require a fixed orientation, and no ink is changed.

## 4. Simplex integral and the final recurrence

**C127; P141.** On the positively oriented simplex x_j≥0, Σx_j≤1,

\[
\int x_0^{i_0}\cdots x_{n-1}^{i_{n-1}}\,dx_0\cdots dx_{n-1}
=\frac{\prod_j i_j!}{(n+\sum_j i_j)!}.
\]

One proof integrates x_(n−1) first and repeatedly uses the elementary beta identity ∫_0^1 t^a(1−t)^b dt=a!b!/(a+b+1)!, itself proved by integration by parts and the b=0 base case. Dividing the monomials by the i_j! and multiplying by the total-weight factorial gives γ=1. The retained code actually performs iterated symbolic integration in39 cases, dimensions1–3 and each exponent0–2; it does not merely insert the beta formula. General validity rests on the induction, not those39 cases.

**C128.** Adopt the explicitly stated reconstruction C_ab=binom(a+b,a). Put r=n−1, A=r+Σ_(j<r)i_j and m=i_(n−1)+1. Assuming lower-dimensional γ=1, collect the final live recurrence by L=Σell_j. Its inner product of binomial coefficients sums to binom(A+L−1,L), by multiplying (1−t)^−(i_j+1). The inserted remaining factor is binom(A+m,m−L). The recurrence sum is therefore

\[
\sum_{L=0}^{m}(-1)^L\binom{A+L-1}{L}\binom{A+m}{m-L}
=[t^m](1+t)^{A+m}(1+t)^{-A}=1.
\]

For n=1 there are no ell variables and the recurrence gives1 directly. This proves the final recurrence in all dimensions under the specified coefficient/sign reading. The program verifies84 cases, n≤3 and all input exponents≤3. Removing the inserted factor gives0 at (0,0); retaining the cancelled outer sign gives−1 there. These failures flag the reading; they do not determine where a pale handwritten insertion lies.

**C124.** Stokes with a consistent orientation gives a chain map. This run collated Cartan's integration theorem and recomputed the normalization, but did not independently reconstruct every partly cancelled κ sign on P137. Its check event is source use plus a bounded computational check, not a complete proof of the manuscript's dual Stokes display.

## 5. Interval automorphisms and the retraction

**C144; Q190–192.** Reversing the vertices sends x to T−x and dx to−dx. In the divided-power basis, the induced triangular formula is

\[
C_i=\sum_{j\le i}(-1)^{j+1}T^{(i-j)}B_j.
\]

Applying it twice gives coefficients of (T−T)^(m), or equivalently the binomial convolution Σ_j(−1)^j binom(m,j), equal to0 for m>0 and1 for m=0. The program squares the8×8 symbolic matrix and obtains the identity. That calculation fixes the coefficient convention; the all-index proof is the convolution.

**C145; Q194,198–202.** Work over Z with one even variable x and one odd variable dx, with dx²=0, differential d(x)=dx. The underlying one-odd-variable ring is commutative because its odd ideal squares to zero. The map

\[
\xi_i=x^{(i)}+x^{(i-1)}dx\quad(i\ge1),\qquad\phi(dx)=dx
\]

is the PD substitution x↦x+dx under the manuscript's inhomogeneous square-zero convention. Pascal's identity proves ξ_iξ_j=binom(i+j,i)ξ_(i+j), and differentiation proves compatibility with d. It fixes T, takes the second barycentric coordinate to T−x−dx, and preserves both endpoint maps because dx restricts to0. The program computes36 product identities for0≤i,j≤5.

In a larger simplex two such even-coordinate images would include x+dx and y+dy. Their ordinary commutator is

\[
(x+dx)(y+dy)-(y+dy)(x+dx)=2\,dx\,dy,
\]

nonzero over Z in the free exterior algebra. The sparse superalgebra routine computes exactly this coefficient. Thus the unrestricted interval-extension assertion, when morphisms may forget grading/parity, is false. This explains the genuine force of the manuscript's 2B_i=0 repair. It proves necessity in the relevant example; a universal sufficiency theorem still needs the full relation and naturality check. Grading-preserving maps are a different category.

**C146.** If a=1+terms of positive weight and ab=0, choose the least weight m with b_m≠0. The weight-m component of ab is b_m, contradiction. Hence a is not a zero-divisor in the direct-sum graded algebra. In its separated complete product it is invertible by Σ_(r≥0)(1−a)^r, whose coefficient in a fixed weight is a finite sum. This proves the cancellation; it does not require a domain or characteristic zero.

**C147.** The cumulative coordinates U_r=X_0+⋯+X_r are obtained from x on the interval by all monotone cuts [n]→[1]. If an extension commutes with these maps, its values on the U_r are fixed, and X_r=U_r−U_(r−1) determines its values on every generator. This proves uniqueness conditional on existence. It does not prove that those forced values satisfy all mixed relations.

**C148–150.** A coefficient change consists of u:S→S′ and λ with u(t)=λt′. Sending X_i,dX_i to λX_i,λdX_i respects the simplex relations and PD homogeneity. Composition is (u′u,u′(λ)λ′). In the scalar power-series case the induced multiplication is therefore substitution, λ′(T)λ(Tλ′(T)), not ordinary multiplication. For λ=1+T and λ′=1+2T the program computes unequal polynomials.

In the divided-power coefficient ring, T·Σλ_iT^(i)=Σ(i+1)λ_iT^(i+1). Thus Tλ=T forces λ_0=1 and (i+1)λ_i=0 for i>0. Over a torsion-free coefficient ring it forces λ=1; over F_p, λ=1+aT^(p−1) satisfies it. Nevertheless λX_0 generally differs from X_0 in the simplex ring: after expressing T as X_0+X_1, the coefficient of X_0X_1^(p−1) is a. The code expands these products modulo2,3,5,7 and records a nonzero monomial. This proves the displayed torsion intersection; it prevents a naive semidirect product with trivial intersection. Polynomial and completed settings, and monoids versus units, remain distinct.

## 6. Four de Rham/Koszul complexes

**C155–164; Q219–223.** Give both x and dx weight1. For total weight n>0, the rank-one complexes have a single map between rank-one modules:

| Algebra and operator | Basis map | Integer coefficient |
|---|---|---:|
| Sym, de Rham d | x^n→x^(n−1)dx | n |
| Sym, Koszul δ | x^(n−1)dx→x^n | 1 |
| Γ, de Rham d | x^(n)→x^(n−1)dx | 1 |
| Γ, Koszul δ | x^(n−1)dx→x^(n) | n |

The saved program obtains these maps from its monomial/exterior differential routines for n=1,…,8. Thus ordinary de Rham and PD Koszul need integer denominators for the elementary contraction, whereas ordinary Koszul and PD de Rham are contractible in each positive weight for a free rank-one module. Tensoring the explicitly contracted free factors proves the latter two assertions for finite free modules. Filtered colimits are exact in modules, and Γ, Sym, Λ and the displayed complexes commute with them. Lazard's theorem, opened at Stacks058G, therefore extends this result to flat modules. No unrestricted nonflat assertion is inferred from that reduction.

Both d and δ are odd derivations. Their graded commutator dδ+δd is an even derivation taking x↦x and dx↦dx. The divided-power rule gives its value n on each total-weight-n monomial. Hence

\[
d\delta+\delta d=n\,\mathrm{id}
\]

on that weight. If n is a unit, δ/n contracts the d-complex, and d/n contracts the δ-complex. This works without flatness. A Q-algebra makes every positive n a unit; characteristic zero alone does not. In degree0 the identity δd=n proves injectivity of d when n is a unit and answers the H^0 question on Q223. The code checks18 ordinary and18 PD rank-two matrices, weights1–6 and exterior degrees0–2. These are finite certificates accompanying the derivation proof.

In F_p[x], d(x^m)=m x^(m−1)dx. Consequently H^0=F_p[x^p] and H^1=F_p[x^p]x^(p−1)dx. In particular H^1 is nonzero although the cohomological degree1 is invertible. The Euler index is *total weight*, not cohomological degree. For finitely many variables the free tensor decomposition gives the coordinate Cartier description. The coordinate-free formulation involves Frobenius twist; no full system of unspecified operations in Q219–220 is claimed proved.

For finite projective modules, homogeneous-degree pairings identify (Sym^nM)^* with Γ^n(M^*) and the dual of Λ^rM with Λ^r(M^*). With the chosen ordered wedge bases, transpose sends ordinary de Rham d to PD Koszul δ, and PD de Rham d to ordinary Koszul δ. The code checks12 matrix pairs; the general identity follows termwise because the exponent coefficient in an ordinary derivative becomes the PD multiplication coefficient. This uses finite *homogeneous* degrees, avoiding an infinite direct-sum dual error.

The natural map Sym(M)→Γ(M) sends x^n to n!x^(n). Multivariable coefficients are products of factorials. The identities n(n−1)!=n! and (a+1)a!=(a+1)! prove compatibility with d and δ;24 computed squares verify the conventions. Over Q it is an isomorphism. For nonzero rank-one free M, an integral isomorphism of this particular map would require those factorials to be units. The regular-sequence Koszul criterion is checked against Stacks062D, not independently reproved here; its converse requires the recorded Noetherian local and maximal-ideal hypotheses.

## 7. Normalization and derived powers

**C168,170; Q229–231.** The standard Ψ=Φ/k has Ψ_n=Z^n. The normalized summand N_qΛ^iΨ is a direct summand of a finite free abelian group and is therefore free. Dold–Kan's integral splitting gives

\[
\binom ni=\operatorname{rank}\Lambda^i\Psi_n
=\sum_{q=0}^n\binom nq\operatorname{rank}N_q\Lambda^i\Psi.
\]

Binomial inversion implies rank1 at q=i and0 elsewhere. Thus the normalized complex is Z[i] after choosing its generator/orientation, and the idempotent splitting commutes with arbitrary base change to k. The code verifies the inversion for i=1,…,5 and n≤7; the equation proves every i,n. Eilenberg–Zilber then identifies N(A⊗Λ^iΨ) up to chain homotopy with N(A)⊗k[i]. The free shift factor makes this valid for arbitrary A. We use the standard Eilenberg–Zilber theorem as background, rather than claiming a new proof of it.

**C167.** This computes the Dold–Puppe derived exterior power at k[1]. BMT Proposition3.5 gives the precise finite-projective integral décalage among derived Γ, Λ and Sym. The expression “termwise Λ²(k[1])=0” refers only to taking the ordinary exterior square of the sole rank-one *module* and leaving it in its original degree. It must not be confused with a graded exterior convention or the derived operation, which can produce k[2]. The general projective-complex formula on the page is not proved merely by that distinction.

**C169.** For K(Z,1)_2=Zx⊕Zy, take faces d_1(x)=d_1(y)=z, d_2(x)=z,d_2(y)=0, d_0(x)=0,d_0(y)=z. In Sym², normalized degree2 is generated by xy−y² and d_0 sends it to−z². In Γ² it is generated by xy−2γ_2(y), and d_0 sends it to−2γ_2(z). The actual integral matrices in the program produce coefficients−1 and−2. There is no normalized component above degree2: a degree-two monomial supported on more than two nondegenerate coordinates is impossible, and degeneracies account for all such summands by Dold–Kan decomposition. Thus the former complex is acyclic, while the latter has H_1=Z/2 and H_2=0. This refutes the *natural simplicial quadratic reading* of the unclear NB as K(Z,2). It neither decides the handwritten symbols nor excludes an intended dual/cosimplicial statement.

**C171.** On the constant simplicial Z module, an unsigned sum has degree2 differential3 and degree1 differential2, with composite6. The alternating sum gives0. The saved multiplication6 is a literal-sign diagnostic only.

**C172–173.** At fixed weight p, A^(p,i)=Γ^(p−i)Φ⊗Λ^iΨ. For i<p, the positive Γ factor has the explicit simplicial contraction; at i=p the normalized exterior factor is k[p]. This is the source of the exceptional top term. To compute through degree p by a resolution, use the good truncation ending in Z^p=ker(d:A^p→A^(p+1)), not a brutal replacement that changes H^p. Γ of sheaves is left exact, so it commutes with this kernel. With the required acyclicity of lower terms this gives the inclusive boundary i=p. The complete theorem and product normalization are source-matched to Cartan§7. Garvín's later explicit Theorem4.2 establishes a strict p<q range in his stated theorem; it is not cited as proof of an inclusive endpoint. Completion at Q233 alone does not justify passing to inverse limits; the continuation235–239 imposes an associated-graded isomorphism and contains its own degenerate counterexample.

## 8. Earlier-run diagnostics, kept separate from author claims

**SA08-230 (CP²).** Suppose an ordinary unweighted integral differential algebra computes the cohomology *ring* of CP² and has compatible divided powers on every positive even cocycle. A cycle z representing the degree2 generator c satisfies z²=2γ_2(z), and dγ_2(z)=γ_1(z)dz=0. Then c² is divisible by2 in H^4≅Z, impossible. This conditional obstruction requires γ_2 on the chosen cycle and differential compatibility; it does not require proving operations descend for all representatives. It does not apply directly to the weighted comparison, where products acquire binomial factors.

**SA08-235.** Differential compatibility alone does not make PD operations on cohomology independent of representatives. In A=Γ_Z(x)⊗Λ(y), |x|=2,|y|=1, dy=x, dx=0, the element x is a boundary, but d(yγ_(n−1)x)=nγ_nx. Thus H^(2n)(A)=Z/n on γ_nx and γ_2(x) is a nonzero class although x is a boundary. Each weight has exactly the two displayed basis elements, so the conclusion follows from that integer map. The program records n=1,…,6 and the map coefficients; no statistical inference is involved.

**SA08-231.** A unital map Γ_Z(T)→Z with T↦1 is impossible: T²=2T^(2) would imply1=2a. This does not prohibit a linear weight extraction. At the point, weight pieces remain copies of Z; the diagnostic is about a ring specialization.

**SA08-314, the separate represented-point diagnostic.** At n=0 the explicit representing-module formula in section2 is S, with no Y or exterior generators. If exterior degree is the chain degree, S=k[u] is in degree0 and its differential is zero, so H_0=S. Ordinary k-chains on that represented simplex instead have H_0=k. A claimed comparison before specifying coefficients, grading or extraction therefore has a mismatch. Assigning u positive total chain degree, applying a specified τ extraction, or confusing a represented simplex with a terminal semisimplicial presheaf changes the question. This is a conditional diagnostic, not a contradiction to every manuscript comparison.

**SA08-232.** If weight-(r,s) multiplication corresponds to binom(r+s,r) times cup product, suitable products across several weights recover it integrally when their coefficients have gcd1. The program computes6+3·10−35=1 for weights(2,2),(2,3),(3,4). More generally, for any fixed lower bounds and any prime p choose distinct sufficiently large p-powers r,s. In characteristic p, (1+t)^(r+s)=(1+t^r)(1+t^s), so binom(r+s,r)≡1 mod p. Therefore no prime divides every admissible coefficient; their gcd is1 and a finite subset has a Bézout relation. This requires the relevant weights to be admissible and compatible comparison identifications. A single fixed positive weight is not closed under weight-additive multiplication.

**SA08-234.** The poset of nonempty faces of the boundary of a tetrahedron has nerve the barycentric subdivision of S². Its groupoid completion is connected with trivial isotropy, because S² is simply connected, but its nerve has H_2=Z and is not contractible. The program computes the boundary matrices of the tetrahedral sphere: ranks C_0,C_1,C_2=4,6,4; boundary ranks3,3; Betti numbers1,0,1. The π_1 assertion comes from the sphere identification, not from H_1 alone. This demonstrates the gap between groupoid uniqueness and higher contractibility; the latter is not attributed to the manuscript.

**SA08-284.** If an external reconstruction criterion used only finite locally constant objects, a point and S² have the same such category because both are simply connected, while their higher homotopy differs. This is only a conditional test of the *quoted* criterion. The external WG source is unavailable, so no actual theorem from that project is refuted here.

Ordinary binomial operations and divided powers also differ: over Q, binom(2,2)=1 while γ_2(2)=2²/2=2. The code records this elementary distinction. It prevents transferring Horel/Ekedahl numerical/binomial statements merely by renaming the operations.

## 9. Donor mathematics and limits of verification

**C134.** For a nodal dual graph, write a cycle as integer edge coordinates z_e and give each node positive thickness m_e. The monodromy quadratic form is Σm_e z_e². It is positive definite on the real cycle space because every coefficient is positive; reversing an edge replaces z_e by−z_e and preserves the form. The program gives Gram values3 for a unit triangle,6 for thicknesses1,2,3 on that triangle,2 for two parallel unit edges, and rank0 for a bridge. The nodal hypothesis matters: a multi-branch singularity cannot be replaced by a complete graph without changing cycles. This checks the graph formula, not the geometric reduction from Jacobians or the full SGA7 integral monodromy theorem.

**C181, group-theoretic part only.** If every element of a group has square1, then ab=(ab)^−1=b^−1a^−1=ba. The semiabelian torsion-congruence lemma itself is compared with SGA7 IX4.7 and not independently reproved.

The analytic exponential, BT rigidity/full faithfulness, all-primes orthogonality, component duality, uniformization and Gorenstein openness are exact source comparisons with their hypotheses recorded in claims and references. Reading their proofs is not a computational certificate. In particular de Jong Criterion2.5 must be read with the1999 correction to the semistable definition; his Corollary1.2 has no p-basis restriction. The unpublished-looking integrality and dual-embedding sign questions actually persist in SGA7 IX9.7 and14.1.12. Their survival in1972 and failure of this bounded search to locate a later exact answer do not establish that they remain open in2026.
