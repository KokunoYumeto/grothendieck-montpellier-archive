# A.1: independent proof and convention correction

2026-11-19, GPT-6 Astra, root. Working proof; hypotheses and remaining gates below.

Let k be any commutative ring, S=Γ_k(T)=⊕_{w≥0}kT^[w], I_r=⊕_{w≥r}kT^[w]. Let Φ_n=k^{n+1} with simplicial operators restriction of functions, constant section T=(1,...,1), Ψ=Φ/kT. Put A_w^q=Γ^{w-q}(Φ)⊗Λ^qΨ (zero for q>w), with d(X^[a])=X^[a−1]dX. A^q=⊕_{w≥q}A_w^q.

There are THREE distinct cochain conventions:

1. C_w^q(X)=Hom_sSet(X,A_w^q); C_gr=⊕_w C_w. This is a genuine weight-graded complex.
2. C_lit^q(X)=Hom_sSet(X,A^q). Weight supports need only be finite on each simplex. This is the literal definition of scans7–9 and the convention used in inherited R2.
3. C_hat^q(X)=Hom_sSet(X,∏_{w≥q}A_w^q)=∏_w C_w^q(X).

## Proposition A-001: universal resolution and acyclicity

For each r≥0, F^r A=⊕_{w≥r}A_w is an exact resolution of the constant simplicial S-module I_r. For q<r, the simplicial k-module F^r A^q is contractible by k-linear simplicial homotopies and is Γ_X-acyclic for every X.

Proof of exactness: in simplicial degree n choose the basis (T,X_1,...,X_n) of Φ_n. Then A_n≅S⊗Γ_k(X_1,...,X_n)⊗Λ_k(dX_1,...,dX_n). The one-variable complex has differential X^[a+1]↦X^[a]dX and the explicit contraction h(X^[a]dX)=X^[a+1], h(X^[a])=0, onto its constant term. The tensor contraction in n variables preserves total weight (variables and differentials have weight1), so restricts to F^r and leaves exactly I_r in degree0. This is an objectwise proof, and the augmenting inclusion I_r→F^r A is simplicial.

Proof of contractibility: Φ is the simplicial module of arbitrary vertex values, with normalized chain complex k→k (identity) in homological degrees1,0. Its explicit k-linear contraction gives a simplicial k-linear homotopy. Applying Γ^a to its component maps gives a simplicial homotopy Γ^aΦ→Γ^a0=0 for a>0. Tensoring with Λ^qΨ and taking direct sums preserves this homotopy. When q<r, every summand has a=w−q>0.

Proof of Γ_X-acyclicity: an acyclic simplicial k-module V is acyclic for the left-exact functor Γ_X(V)=Hom_sSet(X,V). Embed V in an injective simplicial k-module J. Injectivity implies that every map ∂Δ[n]→J extends to Δ[n], because k[∂Δ[n]]→k[Δ[n]] is a monomorphism. Thus J is an acyclic Kan complex. The quotient J/V is acyclic by the homotopy exact sequence, and J→J/V is a trivial Kan fibration. Hence every X→J/V lifts, proving the first derived vanishing. Repeat with J/V for every higher derived functor. We only use this implication; we do not identify acyclicity with an additive contracting homotopy for arbitrary V.

## Theorem A-002: the literal multiplicative comparison

There is a natural isomorphism of cohomologically graded S-algebras

H^*(C_lit(X)) ≅ ⊕_{i≥0} H^i(X; I_i),

where the product uses the ordinary cup product with coefficient pairing I_i⊗_k I_j→I_{i+j} from multiplication in S. This holds for every simplicial set X and ring k.

Proof of the additive assertion, including i=0 and endpoint: the exact resolution F^i A of I_i has Γ_X-acyclic terms in degrees0,...,i−1. If Z^i=ker(d:F^iA^i→F^iA^{i+1}), dimension shifting in the exact sequence 0→I_i→F^iA^0→...→F^iA^{i−1}→Z^i→0 identifies coker(Γ_X F^iA^{i−1}→Γ_X Z^i) with R^iΓ_X(I_i)=H^i(X;I_i). The left side is H^i(Γ_X F^iA). For i=0 it is simply Γ_XI_0. There is a direct decomposition of simplicial complexes A=F^i A⊕⊕_{w<i}A_w; because the latter sum is finite, Γ_X preserves it. Every lower-weight summand vanishes in cochain degrees≥i, and its differential out of degree i−1 is zero. Thus H^i(Γ_XF^i A)→H^i(Γ_XA) is an isomorphism.

Proof of products: F^iA⊗_k F^jA→F^{i+j}A is a map of nonnegative complexes of simplicial k-modules over I_i⊗I_j→I_{i+j}. All terms are degreewise free k-modules. The tensor complex resolves I_i⊗I_j: filter its first-quadrant double complex and use exactness of the two resolutions and flatness of their degree0 cohomology. Hence this multiplication represents the indicated coefficient pairing in the derived category of simplicial k-modules. Apply the standard derived-sections cup-product comparison (it can be constructed with a functorial cosimplicial acyclic resolution and its Alexander–Whitney product). The edge comparison Γ_X(F^iA)→RΓ_X(I_i) is compatible with products by naturality of that double-complex construction. Its degree-i component is the dimension-shifting isomorphism just proved. Consequently multiplication becomes cup product with the coefficient pairing, with no invertibility or torsion restriction on k.

Equivalent subring description: the natural comparison to H^*(X;S) is injective, with degree-i image ker[H^i(X;S)→H^i(X;S/I_i)]. Indeed S=I_i⊕S_{<i} splits as k-modules, so the coefficient cohomology sequence splits. The degree-i cokernel is H^i(X;S/I_i)=⊕_{w<i}H^i(X;k).

## Theorem A-003: fixed weights and finite-weight cochains

Naturally and compatibly with products,

H^i(C_w(X)) = H^i(X;k) for 0≤i≤w, and 0 for i>w.

Under the canonical identification using the augmenting section T^[w],

[x]_w [y]_v = binom(w+v,w)[x cup y]_{w+v},

T^[a][x]_w=binom(w+a,a)[x]_{w+a}.

The proof repeats A-001/A-002 in a single weight. The multiplying map covers T^[w]T^[v]=binom(w+v,w)T^[w+v] on the resolved constant coefficient modules. Thus L1 is true for C_gr:

H^*(C_gr(X))=⊕_i H^i(X;k)⊗_k I_i.

For C_lit the canonical inclusion of this ring is an isomorphism if H^i(X;−) commutes with the countable direct sum of k in each required degree. In particular this holds if X has finitely many nondegenerate simplices in each degree, or if integral homology in degrees i and i−1 is finitely generated for every i (apply the natural universal coefficient exact sequence over Z).

## Counterexample A-004: literal L1 for arbitrary X is false

Take k=Z and the constant discrete simplicial set X=N. Its positive-dimensional nondegenerate simplices are absent. Literal C_lit^0=∏_{n≥0}S and C_lit^{q>0}=0. The proposed right side in degree0 is (∏_n Z)⊗S=⊕_{w≥0}∏_n Z. Its canonical image has one uniform finite weight bound. The sequence (T^[n])_n belongs to the literal ring and not to that image. Thus the claimed canonical coefficient comparison is not surjective. This is an infinite counterexample, so no finite exhaustive program is a certificate for it; the argument proves the failure directly.

This is a correction to L1, to the literal interpretation of study/STUDY.md's weightwise-to-global assertion, and to any simultaneous use of inherited R2's unbounded convention with the direct-sum formula. It does not refute R1 weight by weight.

## Proposition A-005: universal completion

For the total-weight completion, C_hat=∏_w C_w; Hom commutes with products. Products of k-modules are exact, so

H^i(C_hat(X))=∏_{w≥i}H^i(X;k)=H^i(X;∏_{w≥i}kT^[w]).

The algebra law is the binomial Cauchy law: coefficient of weight n in xy is Σ_{w+v=n}binom(n,w)x_w cup y_v. Each sum is finite. This settles universal completion, but not yet the nonsplit filtered-base completion.

## Status update after the initial proof notes

The three initial gates below were subsequently closed in this run. The arbitrary PD triple is computed by the consecutive derived-tail image in A-006; completion without graded regularity is A-007; graded regularity gives the ordinary consecutive-tail image in A-008, retaining Bockstein effects. The multiplication comparison is proved in sections/A_main.tex and uses the opened Stacks Project sections 20.31 and 21.33 for the derived cup product. These notes are retained as the initial proof record; the numbered paper and results register state the current scope.

Cartan (1976), section 7, already gives the universal all-X tail comparison, the fixed-weight endpoint, binomial multiplication and recovery over Z. Our universal arguments are independent re-proofs and coefficient extensions, with no priority claim. The arbitrary-PD-base and completed derived-tail formulas are separately stated and proved here.
