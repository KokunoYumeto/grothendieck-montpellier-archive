# Part C and B.6: checked working mathematics

AI-produced by GPT-6 Astra (OpenAI, ChatGPT Pro mode), delegated run `/root/topos`, 2026-11-19. No priority claim. These are full proof notes for merger into the paper; the final status table must distinguish the unrestricted uniqueness question from the false strict equalization claim.

## Conventions and manuscript locators

We write `sMod_k` for simplicial modules over a **constant** commutative ring k, `Ch_{>=0}(k)` for homological complexes, and N for normalized chains. In the simplicial topos, a sheaf is called *flasque* in the sense of SGA4 V Definition 4.1 when H^q(sSet/X,A|_X)=0 for every simplicial set X and q>0. This is already a condition on every slice. We call it *tensor-universally flasque* when A tensor_k M is flasque for every simplicial k-module M. Absolute Gamma-acyclicity is a different, much weaker property.

Relevant input files:

* `MPL_136_047-094_transcription.tex`, scan80 lines1483ff: conditions (a),(b), with (b) explicitly stable under tensoring with **every abelian sheaf**. Scan89 lines1891ff gives the stronger all-M,N divided-power version. Scan91 lines2000ff has the underlined Non.
* `MPL_136_095-141_transcription.tex`, scan98 lines98ff: conditional punctuality proposition. Scan100 lines146ff: flat/projective overwritten reading and explicit margin `faux tel quel, à arranger`. Scan102 lines211ff gives coinduction zigzag. Scans117,119,121 formulate eventual quasi-resolution, eventual flasqueness, groupoid uniqueness and stronger common-source/equalizer conjectures.
* `K136-02_transcription.tex`, scan348 lines317ff defines half-algebras; scan350 lines402ff gives C^i=Lambda^{i+1}Phi, differential T wedge; scan352 lines459ff asks for extension of exterior multiplication and identifies its putative linear ambiguity.

All these statements below are formulated independently of doubtful words. In scan100, **both readings** are treated: flat is insufficient for additive contraction, projective is sufficient. At scan352 we use only the unambiguous diagrams and half-algebra axioms of scan348.

## C01. Cosimplicial obstruction (L6): proved, stronger form

**Theorem.** Let k be a nonzero commutative ring and E=Set^Delta the topos of cosimplicial sets. There is no monomorphism of cosimplicial k-modules u:k_const -> Phi such that Phi tensor_k M is Gamma-acyclic for every cosimplicial k-module M. Consequently the hypotheses of scan80 cannot hold; no assumptions on the cokernel or higher divided/exterior powers are needed for this obstruction.

**Proof.** Let V be the cosimplicial k-module given by denormalization of the cohomological complex k[1]. Thus V^0=0, V^1=k, and the generator v in V^1 is a normalized 1-cocycle. Put t_n=u_n(1). Naturality gives d^i(t_1)=t_2 for each coface [1]->[2]. Therefore

  d(t_1 tensor v)=t_2 tensor (d^0 v-d^1 v+d^2 v)=0.

It is normalized because V^0=0. The tensor t_1 tensor v in Phi^1 tensor k=Phi^1 is nonzero because u_1 is injective and 1 != 0. There are no degree-zero cochains at all: (Phi tensor V)^0=0. Hence it gives a nonzero H^1 of normalized cosimplicial cochains. The derived global-section functors of a cosimplicial module are precisely normalized cohomology: this follows from the dual Dold-Kan equivalence and the projective resolution of the constant object by the cosimplicial representables (or from the elementary injective-disk resolution). Thus Phi tensor V is not Gamma-acyclic. QED.

This proves the manuscript's Non under the actual tensor-universal condition. It does not assert that no injective cosimplicial module contains the constant module; such an assertion would be false.

## C02. Exact meaning of slice acyclicity: proved

**Theorem.** For A in sMod_k, the following conditions are equivalent:

1. A is flasque in SGA4's sense: H^q(sSet/X,A|_X)=0 for all X and q>0.
2. N(A) is an acyclic homological complex, including H_0=0.

If the terms A_n are projective k-modules, these conditions imply an additive simplicial contraction. Without projectivity an additive contraction need not exist.

**Proof.** The projection p_X:sSet/X -> sSet has an exact left adjoint on module sheaves (pointwise direct sum over each fiber). Its inverse image therefore preserves injectives, and the adjunction identifies

  H^q(sSet/X,p_X^*A) = Ext^q_{sMod_k}(k[X],A).

Dold-Kan transports this to Ext in Ch_{>=0}(k). The normalized complex P=N(k[X]) is free in every degree, with basis the nondegenerate simplices of X.

For completeness, if P is degreewise projective, take the projective epimorphism

  D(P)=P_0[0] direct_sum (direct_sum_{n>=1} D^n(P_n)) -> P,

where D^n(P_n) is the identity disk in degrees n,n-1. In degree n the map is (a,b) -> a+d_P b from P_n direct_sum P_{n+1}. Its kernel is the shifted truncated complex P_{n+1} with differential -d_P. Iteration gives a projective resolution. After applying Hom(-,A) it identifies the positive-degree Ext groups with the positive-degree cohomology of the internal Hom complex

  Hom(P,A)^q=product_{n>=0} Hom_k(P_{n+q},A_n).

If A is acyclic, every cocycle in positive degree is a boundary: solve the chain-homotopy equations inductively on the source degree, lifting into boundaries with projectivity of P_n. This proves (2)=>(1), without any finiteness restriction on X; the recursive construction handles the displayed products.

Conversely take X=Delta[m+1]/boundary Delta[m+1]. Its normalized free complex is k[0] direct_sum k[m+1]. The same resolution gives

  H^1(sSet/X,A|_X) = H_m(N(A))

for each m>=0. Thus (1)=>(2).

If N(A)_n is projective, exactness splits successively from degree zero upward: Z_0=N(A)_0 is projective, so N(A)_1->Z_0 splits; then Z_1 is a direct summand of N(A)_1 and is projective; continue. The splittings give a chain contraction, which is an additive simplicial homotopy under Dold-Kan. Each N(A)_n is a direct summand of A_n, so projectivity of A_n suffices. QED.

## C03. L5 is false for additive contraction: finite counterexample

Let k=Z (or regard the same modules as modules over Z/4). Let C have C_2=Z/2, C_1=Z/4, C_0=Z/2 and differentials d_2(x)=2x, d_1(y)=y mod2. All other terms are zero. It is exact. Let A=DK(C). By C02 it is acyclic on every slice. A chain contraction would give a right inverse h_0:C_0->C_1 of d_1. But a homomorphism Z/2->Z/4 sends 1 to 0 or2, and both have image0 under d_1. Hence no contraction exists. Underlying simplicial sets are weakly contractible (indeed contractible in their Kan homotopy category); the false assertion is specifically the additive simplicial contraction needed to apply nonadditive functors to the homotopy.

The complete finite check is `code/C_finite_obstructions.py`, output `logs/C_finite_obstructions.txt`. It checks exactness and exhausts every possible right inverse. This is a finite normalized complex and specifies all simplicial degrees via the explicit standard Dold-Kan formula.

## C04. Flatness does not repair additive contraction: explicit example

Let b_j=1 if j is a perfect square and b_j=0 otherwise, and put a_n=sum_{0<=j<n} b_j 2^j. In Q^2 let z=(1,0), x_n=(a_n/2^n,1/2^n), and let E be the subgroup generated by z and every x_n (n>=0). We have 2x_{n+1}=x_n+b_n z. The second-coordinate map gives an exact sequence

  0 -> Z z -> E -> Z[1/2] -> 0.

Indeed any finite linear combination can be rewritten c z+m x_N, and if its second coordinate is zero then m=0. E is torsionfree, hence flat over Z; both other terms are flat too. A section would send 1 to x_0+c z for some integer c. Divisibility by 2^n in E would force c congruent to a_n modulo 2^n for every n. But the 2-adic digits b_j have infinitely many zeroes and infinitely many ones, whereas an ordinary nonnegative integer has eventually-zero digits and a negative integer has eventually-one digits. Thus there is no section.

Place this exact sequence in homological degrees2,1,0 and apply Dold-Kan. All simplicial modules are flat, C02 makes the result flasque, but no additive contraction exists. Since its terms and cycles are flat, tensoring with any simplicial module remains acyclic by Eilenberg-Zilber (the tensor complex is exact by a bounded-below filtration). Thus the example is even tensor-universally flasque.

This is the valid correction to the flat reading on scan100. The supplied reading CE036/R11 used the constant module k as a counterexample, but that module is only absolutely Gamma-acyclic, not flasque in SGA4's terminology. The body of HUNCHES.md H4, which asks only that all homotopy groups vanish, is correct by C02; the header and additive-contraction consequence require the distinction just made. In fact global sections of any simplicial module are evaluation in degree0, so absolute Gamma-acyclicity is automatic and gives no relevant condition.

## C05. The conclusion needed on scan100 still holds: proved

**Theorem.** If A is a degreewise flat simplicial k-module and N(A) is acyclic, then Gamma^r(A) and Lambda^r(A), r>0, are degreewise flat and tensor-universally flasque. More generally any reduced functor on modules that preserves filtered colimits and takes free modules to flat modules has this property when applied levelwise, provided it preserves simplicial homotopies (as every ordinary functor does).

**Proof.** The cycles of N(A) are flat, by induction starting with Z_0=N(A)_0 and using the exact sequences 0->Z_n->N(A)_n->Z_{n-1}->0. Christensen--Holm, *The direct limit closure of perfect complexes*, Theorem7.3 in the opened 20 May2013 preprint (Theorem7.2 in the published version), expresses N(A) as a filtered colimit of bounded contractible complexes of finitely generated free modules. One can take all complexes nonnegative: use the standard right-adjoint smart truncation at0 on the indexing complexes. On a contractible complex of projectives, this truncation is still contractible and projective, and commutes with the filtered colimit whose target is already nonnegative. Dold-Kan commutes with filtered colimits.

Every reduced functor preserves an additive simplicial homotopy when regarded simply as a collection of maps satisfying the simplicial homotopy identities: applying the functor preserves all the identities, and the zero map factors through0. Hence its value on a simplicially contractible module is contractible. Gamma^r and Lambda^r preserve filtered colimits and take finite free modules to finite free modules. Exactness of filtered colimits therefore makes their values on A acyclic, and flatness follows by the usual Lazard argument degreewise. Finally an acyclic nonnegative complex of flat modules has flat cycles, so its tensor product with every nonnegative complex is acyclic; Eilenberg-Zilber transfers this to levelwise simplicial tensor products. C02 proves the universal flasqueness claim. QED.

**Caution on the general-functor sentence.** Flatness of the values needs the functor to take the free modules occurring after denormalization to flat modules. For Gamma and Lambda this is explicitly satisfied. We make no claim for functors that fail this hypothesis.

## C06. Repaired punctuality proposition of scan98: proved

For the simplicial topos and any constant commutative ring k, the localization at all morphisms of the category of special tensor-universally flasque PD de Rham structures is equivalent to the terminal category. Its nerve is in fact contractible. Here special means the literal bigraded conditions of scan94: 0<=q<=p, k=A^{00}, marked T, all terms k-flat, and the augmentation S=k{T}->A is a weightwise resolution; flasqueness is required in q<p.

**Proof.** Put Phi_A=A^{10}, Psi_A=A^{11}. Specialness gives the pure exact sequence0->kT->Phi_A->Psi_A->0. Form E(A)=Gamma(Phi_A) tensor Lambda(Psi_A) with its standard differential. The free PD-alternating universal property gives a natural map E(A)->A. The relative PD Koszul lemma shows E(A) special; it can be checked after filtered colimits of split finite free extensions, where it is the ordinary divided-power Poincare homotopy. C05 shows E(A) is universally flasque since Phi_A is flat and flasque, and the complementary-degree-positive terms contain Gamma^r Phi_A, r>0.

Let Phi_std,n=k^{n+1}. Evaluation at0 has right adjoint i_{0*}(M)_n=M^{n+1}; the adjunction unit is the vertex-evaluation map Phi_A->i_{0*}((Phi_A)_0). Form Q(A)=DR(i_{0*}((Phi_A)_0),T). Its marked sequence is pure with flat quotient: levelwise the quotient is a direct sum of (Phi_A)_0/kT and copies of (Phi_A)_0. The coinduced module is simplicially contractible, and flat; C05 applies. There are natural morphisms

  A <- E(A) -> Q(A) <- DR(Phi_std,T).

All four objects belong to the same category. After inverting all morphisms this is a natural isomorphism from the constant functor at DR(Phi_std,T) to the identity. For any arrow f:A->B, naturality forces f=eta_B eta_A^{-1}; therefore every Hom set is a singleton and all objects are isomorphic. The same zigzag of natural transformations contracts the nerve before localization. QED.

For a general ringed topos, the corresponding conditional statement must include **nonemptiness** as well as preservation of flat universal flasqueness by positive divided powers. Subject to those hypotheses it has the same proof with a fixed admissible elementary embedding and the functor Phi -> (Phi amalg_k Phi_0) tensor Phi_0; the two factors map naturally into this common target. Without nonemptiness it is an empty category, not a point. C01 supplies the relevant obstruction for cosimplicial sets with the tensor-universal condition.

## C07. Strict equalization conjecture121(b): false over every nonzero ring

This strengthens the initially discovered rational example. Let k be any nonzero commutative ring, S=k{T}, and F=DR(Phi,T) the standard theory. Set W=Phi amalg_k Phi, V=Phi tensor_k W, and B=DR(V,T tensor T). The natural map j:W->V sends w to T tensor w and is split in each simplicial degree (evaluate the first factor at a vertex). All terms and cokernels are free. V is simplicially acyclic because Phi is contractible and flat; its quotient by the marked line is flat. Thus B is special and tensor-universally flasque by C05 and the relative PD Poincare argument.

The induced map DR(W,T)=F tensor_S F -> B is injective: split the underlying module inclusion and its marked line degreewise; divided and exterior powers of an inclusion into a direct sum are injective. Therefore the two inclusions i1,i2:F->B have equalizer S. The latter assertion follows by writing F_n as a free S-module on divided-power/exterior monomials including1 and comparing the basis a tensor1 versus1 tensor a.

Any admissible H->F equalizing the two maps would factor through constant S. On sections over X=Delta[1]/boundary, that factorization kills degree-one cohomology. But every morphism between admissible theories induces the canonical ordinary-cohomology isomorphism in the shadow category, by the augmentation comparison diagram. H^1(X;k)=k is nonzero. Contradiction.

Thus121(b) is false in every nonzero coefficient ring, even in the special universally flasque category whose localization is a point by C06. This explicitly shows that strict common-source equalization is not equivalent to localization being connected and simply connected.

The earlier rational construction used B0=F tensor_S F directly. Its admissibility over Q was checked via Gamma^r(W) acyclic for r>=2, since N(W) is an identity disk plus k[1]. The new embedding B0->DR(Phi tensor W) removes the rational hypothesis and strengthens the counterexample. The earlier method is retained here only as a documented successful intermediate approach.

## C08. Rational positive uniqueness statement: proof under explicit admissibility conditions

Over a Q-algebra k, take the category of theories satisfying the uniform eventual resolution condition(3) and eventual flasqueness condition(4) of scans117,119 (and the stated bigrading and flatness conditions where tensor products are used). Tensoring with the standard F produces an admissible theory, so the natural zigzag C -> F tensor_S C <- F contracts its nerve and its localization.

Detailed mechanism: filter F over S by polynomial degree in Phi_std/kT=Psi. In each weight the filtration is finite and its associated graded is S tensor Sym^r(Psi) tensor Lambda^s(Psi). It is split as an S-module in each simplicial degree, so tensoring with any C preserves the filtration and its associated graded. Since N(Psi)=k[1], Sym^r(Psi) is acyclic for r>=2 (averaging and the sign action, valid over any Q-algebra). For r=0,1, each fixed exterior degree q of F tensor_S C involves only C^{a,b} with b<=q and a=p-r-s tending to infinity with total weight p. The eventual flasqueness of C therefore makes every associated-graded term flasque when p is sufficiently large relative to q. Finite dévissage proves condition(4). The augmentation C->F tensor_S C is a simplexwise quasi-isomorphism because the polynomial de Rham complex F_n has an S-linear contraction to S preserving weight, obtained by dividing the radial homotopy by positive polynomial-plus-exterior degree. Thus condition(3) also transfers, uniformly. The zigzag gives the categorical conclusion as in C06.

At this writing the analogous unrestricted integral uniqueness assertion for the entire eventual-admissible category has **not** been proved here. The rational argument uses Gamma^r(Psi)=Sym^r(Psi). Outside Q the associated graded instead involves Gamma^r(Psi), whose homotopy need not vanish in arbitrarily high weights. The statement that Sym^r(K(k,1)) itself fails to be acyclic was incorrect: for rank-one free k and r>1 the Sym--Lambda decalage makes it acyclic integrally as well. This is an exact gate, not a completed general theorem. The strict equalization conjecture itself is already completely refuted by C07. An attempt to use an unfiltered tensor product over S in arbitrary characteristic therefore cannot be presented as a proof of the full conjecture.

## B601. Half-differential structure on the standard exterior resolution: impossible

**Theorem.** For every nonzero commutative ring k, let Phi_n=k^{n+1}, T=1, Psi=Phi/kT, C^i=Lambda^{i+1}Phi with d=T wedge, and identify Z^i(C)=Lambda^iPsi by z -> T wedge a lift. There is no natural simplicial k-bilinear map

  sigma_{0,1}: C^0 tensor Z^1 -> C^1

that restricts to the exterior product on Z^0 tensor Z^1 and satisfies d sigma(c,z)=(dc) wedge z under the prescribed exterior multiplication on cocycles. In particular there is no half-differential algebra of scans348--352, and no full DGA extending those products.

**Proof.** On the one-simplex write c=(c_0,c_1) and let the element of Psi_1 be represented by v=(v_0,v_1). Both Psi_1 and Lambda^2Phi_1 have rank1; bilinearity gives unique a,b in k with

  sigma(c,bar v)_{01}=(a c_0+b c_1)(v_1-v_0).

The marked-unit condition gives a+b=1. On the two-simplex, naturality along the three edge inclusions forces the same formula on every edge. Hence

  (d sigma(c,bar v))_{012}
   = a(c_1-c_0)(v_2-v_1)+b(c_1-c_2)(v_1-v_0).

On the other hand the prescribed product on cocycles gives

  ((dc) wedge bar v)_{012}
   = (c_1-c_0)(v_2-v_1)+(c_1-c_2)(v_1-v_0).

Take c=(0,1,1), v=(0,0,1), yielding a=1. Take c=(0,0,1), v=(0,1,1), yielding b=1. Together with a+b=1 these equations give1=0. QED.

This argument uses only the first operation, degree0/1, only Delta[1] and Delta[2], and holds with all torsion allowed. The finite certificate enumerates all coefficient pairs and all function pairs for k=Z/2,Z/3,Z/4. It finds no operation in any of these cases; the scalar identity (a+b-1)-(a-1)-(b-1)=1 certifies the universal obstruction.

## B602. Exact corrected extension/indeterminacy statement

For a fixed pure extension0->kT->Phi->Psi->0, set Z^i=Lambda^iPsi and C^i=Lambda^{i+1}Phi. Before imposing associativity, the requested map sigma_{ij} is a morphism of the two short exact sequences

  0->Z^i tensor Z^j -> C^i tensor Z^j -> Z^{i+1} tensor Z^j ->0,
  0->Z^{i+j} -> C^{i+j} -> Z^{i+j+1} ->0,

with outside maps the exterior products. The flatness of Psi guarantees the first sequence is exact. Such a middle map exists iff the pushout of the first extension along the lower product equals the pullback of the second extension along the upper product in Ext^1_k(Z^{i+1} tensor Z^j,Z^{i+j}) in the relevant sheaf/module category. This is the defining classification of Yoneda extensions: an equality of extension classes is exactly an isomorphism between the pushout and pullback, whose comparison yields the middle map, and conversely a middle map produces that equivalence.

When nonempty, the set of middle maps is a torsor under

  Hom_k(Z^{i+1} tensor Z^j,Z^{i+j}).

Indeed the difference vanishes on Z^i tensor Z^j and has image in Z^{i+j}; hence it factors uniquely through the stated quotient. Conversely adding any such factor preserves both outside conditions. The manuscript's linear indeterminacy is correct **only conditional on existence**, and associativity imposes further equations; in the simplicial standard example the torsor is empty already at(i,j)=(0,1).

If a splitting s:Psi->Phi is supplied as part of the data, there is a half-algebra: define c circle z=c wedge Lambda^j(s)(z), and define left products by graded commutativity. Exterior associativity, the unit, the prescribed product on cycles, and the differential identity follow immediately from d=T wedge. It is functorial under maps preserving the chosen splitting. This gives the precise positive replacement; the standard simplicial extension has no compatible choice with the required identities, as B601 proves.

A half-algebra is not a cup-1 structure. Its operations have degree0 and are defined only when at least one argument is a cocycle. Cup-1 has degree-1 and expresses a chain homotopy between a cup product and its graded transpose. The Eilenberg-Zilber/Alexander-Whitney/shuffle data of scans357--361 can support the latter higher coherent structure on ordinary cochains, but cannot solve the incompatible scalar equations above. This is a structural distinction, not a claim that E-infinity operations on ordinary cochains fail to exist.

## C09. Further progress: full explicit-eventual uniqueness over Z_(p)-algebras

The complete proof is now in `sections/C_part.tex`, Statement C09. For k a Z_(p)-algebra and N=p^e, S=k{T} is finite free over R_N=k{U}, U maps to T^(N), on basis T^(r),0<=r<N. The coefficient of U^(m)T^(r) in T^(mN+r) is

  ((mN)!/(m!(N!)^m)) binom(mN+r,r),

which has p-adic valuation zero by Legendre and absence of base-p carries. Thus G_N=S tensor_{R_N}DR(Phi,U) is admissible, with flasqueness for q<floor(weight/N).

For any theory A satisfying scan119's eventual flasqueness, A^{N,0} is acyclic for N large. Since N(Phi)=D^1(k), lifting the marked T^(N) through its normalized boundary constructs G_N->A without any flatness assumption on A^{N,0}/kT^(N). This eliminates the earlier provisional quotient-flatness gate.

Two maps G_N->A become equal after localization: their restrictions extend from W=Phi amalg_k Phi to V=Phi tensor W because V/W has projective normalized terms and A^{N,0} is acyclic. The corresponding H_N=S tensor DR(V,U) is admissible. A fold followed by pointwise multiplication gives a common retraction H_N->G_N, so its two inclusions become equal after inversion. Compare different N with a larger p-power. This produces a canonical natural isomorphism from the constant standard theory to the identity in the localization.

Thus the explicit-eventual category has terminal localization and common sources over every Z_(p)-algebra. Strict equalization still fails by C07. The unrestricted integral/arbitrary-ring descent remains a gate; no claim to settle it is made.

## B605. Full ambiguity with finite-rank quotient

For a locally free constant finite-rank quotient Psi of rank r in the ringed topos, a half-algebra exists exactly when the original marked extension splits. Every full half-algebra is determined by independent retractions p_i:C^i->Lambda^iPsi, 0<=i<r, of the cycle inclusions. The set, when nonempty, is a torsor under product_i Hom(Lambda^(i+1)Psi,Lambda^iPsi).

Proof is now in sections/C_B6.tex B605. From the half-action, recover p_i(c) by p_i(c) wedge z=c circle z in Lambda^rPsi for every z in Lambda^(r-i)Psi. The top pairing is perfect. Associativity with two cycles forces p(cz)=p(c)z; Leibniz forces dbar(cz)=dbar(c)z. Thus (p,dbar) identifies the action with diagonal exterior multiplication on A^i plus A^(i+1), differential(a,b)=(b,0). Conversely any retractions give these formulas and all axioms. The standard simplicial Psi is only degreewise finite free with varying ranks, so it does not satisfy this global finite-rank hypothesis; B601 still refutes its natural structure.
