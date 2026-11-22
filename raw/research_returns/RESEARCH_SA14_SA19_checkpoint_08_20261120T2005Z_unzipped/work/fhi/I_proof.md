# Part I: degree zero in general, and a full presentation for every regular local surface

## I.1 — Proved: degree-zero off-diagonal terms vanish

Let A be a regular noetherian local ring and write E_p=E_A(A/p). Normalize its residual complex so that K^i=⊕_{ht(p)=i}E_p. For any p,q, Hom_A(E_p,E_q)=0 unless p⊆q. Indeed, if a∈p\q, each element of E_p is killed by some power of a, whereas multiplication by a is invertible on E_q. Applying a sufficiently large power to the image of each element proves that every homomorphism is zero. Here the first assertion follows from E_p being pA_p-torsion, and the second from the natural A_q-module structure of E_q.

Distinct primes of the same height are incomparable. A map between the direct sums in one degree is consequently diagonal: its projection to every distinct target summand vanishes, and the coordinate projections detect every element of a direct sum. Matlis' endomorphism theorem then gives

    End_A^0(K)=∏_{p∈Spec A} Â_p.

The finite topology on Hom means pointwise convergence when source and target modules are discrete. On End_A(E_p), it is exactly the pA_p-adic topology of Â_p. On End_A^0(K) it is the product of these topologies. The same containment argument proves End_A^i(K)=0 for i<0. Thus there are no hidden degree-zero off-diagonal homomorphisms for a regular local ring. The diagonal assertion is established independently of the conjectural presentation.

Opened reference for the Matlis endomorphism theorem: Sastry, *A pointwise criterion for dualizing pairs*, Astérisque 208 (1992), proof of Lemma 2, p.123, https://www.numdam.org/article/AST_1992__208__117_0.pdf . The proof below also uses Schenzel, *A note on the Matlis dual of a certain injective hull*, Theorem 1.1, p.1, https://arxiv.org/pdf/1306.3311 .

## I.2 — Proved: the complete two-dimensional case, including degree two and topology

**The precise category.** A is given the discrete topology as base ring. Degree-zero local completions carry their usual adic topologies. Graded topological A-algebras have continuous addition and jointly continuous multiplication; morphisms are continuous, unital graded A-algebra homomorphisms. In the universal problem the prescribed degree-zero algebra is identified with the degree-zero part, and θ has degree one. We may restrict to separated complete algebras, since the endomorphism algebra constructed below is separated complete. This makes the completion convention explicit; it is not an assertion that the ambiguous handwritten symbols on 43:65 define this category uniquely.

**Theorem.** Let A=k[[s,t]], F=Frac(A), m=(s,t), P_1={p⊂A:ht(p)=1}, and let K be the residual resolution of A. Give End_A^*(K) the finite topology. Then End_A^*(K), with its differential θ, is the universal separated complete graded topological A-algebra with

    B^0=F × (∏_{p∈P_1}Â_p) × A,
    θ²=0,
    e_q θ e_p=0 unless p⊂q is an immediate specialization.

In particular the canonical map from the algebra so defined by the universal property to End_A^*(K) is an isomorphism, including degree two. No extra algebraic relations are needed in this case. The topology of the arrows ending at m is essential and is not the adic topology of Â_p.

### 1. The residual resolution and its individual arrows

A is a two-dimensional regular complete local ring, hence a UFD and Gorenstein. Its normalized residual resolution is

    0→A→F --d0→ I=⊕_{p∈P_1}E_p --d1→E→0,       (1)

where E=E_A(k), E_p=F/A_p, and the p-component of d0 is the quotient map. Let δ_p:E_p→E be the corresponding component of d1. Choose a generator f_p of the height-one prime p, and put R_p=Â_p and F_p=Frac(R_p).

By Schenzel's Theorem 1.1, D(E_p)=Hom_A(E_p,E) is free of rank one over R_p, since dim(A/p)=1 and A/p is complete. The map δ_p is a generator, not just a nonzero element. To see this, apply Hom_A(A/p,−) to (1). Only the last two terms survive, giving the complex

    κ(p) --δ_p→ Hom_A(A/p,E).

The free resolution 0→A --f_p→ A→A/p→0 shows that this differential is surjective with nonzero kernel A/p. In particular its restriction to κ(p) is nonzero. The kernel of the restriction D(E_p)→D(κ(p)) is f_p D(E_p), by dualizing 0→κ(p)→E_p --f_p→E_p→0. Consequently δ_p is not divisible by f_p in the free rank-one R_p-module D(E_p), so is a basis. We henceforth use this basis, obtaining

    Hom_A(E_p,E)=R_p,  c↦δ_p∘c.                 (2)

Also

    Hom_A(F,E_p)=F_p.                            (3)

One proof is to apply Hom_{A_p}(−,E_p) to 0→A_p→F→E_p→0 and then localize the resulting exact sequence at f_p. The Hom module in (3) is already an F-vector space, and its submodule End(E_p)=R_p localizes to F_p. Explicitly a∈F_p corresponds to h_a(f)=fa mod R_p, using E_p≅F_p/R_p.

### 2. Restricted products and all graded pieces

Define the ring of restricted tuples

    𝔄={ (a_p)∈∏_p F_p : a_p∈R_p for all but finitely many p },
    P=∏_p R_p.

Every element of 𝔄 has one global denominator: 𝔄=S^{-1}P for S=A\{0}. Indeed, the finitely many negative valuations can be cleared by a product of powers of the corresponding f_p. Conversely a nonzero element of A has only finitely many prime divisors.

A family of maps F→E_p comes from a map F→⊕E_p precisely when, for every f∈F, only finitely many components are nonzero on f. Taking f=1 in (3) proves that the coefficients must be integral almost everywhere; this condition is sufficient because every f has finitely many poles. Hence

    End^1_A(K)=𝔄 ⊕ P.                            (4)

The first summand is F→I and the second is I→E, in the bases (2) and (3).

Apply the exact functor D=Hom_A(−,E) to (1). Matlis duality gives D(E)=A and D(A)=E, so

    0→A→P→D(F)→E→0.                             (5)

The map A→P is the diagonal map, because it sends a to the family aδ_p. Localize (5) at S. The module E is S-torsion, while D(F) is already an F-vector space. We obtain

    End^2_A(K)=D(F)≅𝔄/F,                        (6)

where F is diagonally embedded. All higher degrees vanish. For c∈P representing I→E and a∈𝔄 representing F→I, composition is

    c∘a=[(c_p a_p)_p]∈𝔄/F.                     (7)

The remaining products of two positive-degree arrows vanish by their endpoints. Formula (7), together with the diagonal actions, describes the entire algebra. The differential is θ=(1,1) in (4), and θ²=[1]=0. Conversely the kernel in (6) is exactly the diagonal F; it is not the direct sum of separate relations at the intermediate primes.

### 3. The topology on the arrows to the closed point

Give 𝔄 in the first summand of (4) the usual restricted-product topology: P, with its product of p-adic topologies, is an open subgroup. This is exactly the finite topology, since vanishing at 1/u∈F means that (a_p) lies in uP. Such uP form a basis of zero-neighborhoods.

The second summand P has the product of different topologies τ_p on R_p. A basis of τ_p is

    uA+f_p^n R_p,   u∈A\p, n≥1.               (8)

Equivalently one can use

    m^N A+f_p^n R_p,   N,n≥1.                  (9)

We prove (8), rather than assume a topology on an iterated completion. Exactness of (1) and factoriality imply

    ker(δ_p)=(A[1/f_p]+A_p)/A_p ⊂ F/A_p.

Indeed, an element of F whose components in F/A_q vanish for every q≠p has no prime divisors in its denominator except f_p, hence lies in A[1/f_p]. Every finite set of elements of E_p lies in the cyclic A-submodule generated by 1/(u f_p^n) for some u∉p and n. In the identification (2), vanishing on this generator is equivalent to

    c/u mod f_p^n R_p belonging to A/f_p^n A.

This is exactly c∈uA+f_p^n R_p, proving (8). For the equivalence with (9), (u,f_p^n) is m-primary, so some m^N is contained in it; conversely one can choose u∈m^N\p. These inclusions show the two families are cofinal.

For p=(s), after choosing the usual coefficient field, R_p=k((t))[[s]]. Topology τ_p is coefficientwise t-adic convergence. In particular t^Nδ_p→0. In the s-adic topology on the ring R_p, t^N does not tend to zero. Thus giving this arrow module only its p-adic topology contradicts the actual finite topology and would lose the continuity forced by the A-component at m.

For degree two, the subgroup

    H={h∈D(F):h(1)=0}

is open and is topologically P_τ/A, where P_τ denotes P with the product of (8). Here is a useful general proof of the quotient-topology assertion. If M'⊂M are modules over a noetherian ring and E is injective, restriction D(M)→D(M') is surjective. For a finitely generated N⊂M, the image of the annihilator of N consists exactly of maps M'→E vanishing on M'∩N: the prescribed map on M'+N, zero on N, extends by injectivity. The intersection M'∩N is finitely generated. Thus restriction is an open map for the finite topologies. Apply this to M'=F/A⊂I from (1). Its dual is H and the kernel of restriction is D(E)=A. This proves the claim. Since every element of E is killed by a nonzero element of A, D(F)=⋃_{u≠0}u^{-1}H; multiplication by each u is a topological automorphism. This specifies the topology of (6) completely, without giving 𝔄/F an unjustified quotient of the ordinary adelic topology.

### 4. Universality and absence of further relations

Let C be any graded topological A-algebra with the prescribed continuous degree-zero algebra B^0 and an element T∈C^1 satisfying the incidence relations and T²=0. Write e_η,e_m,e_P for the three block idempotents. Finite sums of the individual height-one idempotents converge to e_P. Continuity and the incidence relations therefore imply

    T=e_P T e_η+e_m T e_P.                      (10)

For a=b/u∈𝔄 with b∈P and u∈A\{0}, and c∈P, define

    α_C(a)=b T e_η u_η^{-1},
    β_C(c)=e_m T c,
    γ_C([a])=e_m T b T e_η u_η^{-1}.            (11)

Here elements of P are placed in the height-one block of B^0, and u_η^{-1} is the element 1/u in its generic block. The A-linearity of T shows that these expressions are independent of the chosen common denominator. If a∈F is diagonal, write a=v/u with v∈A. Its last expression is v e_m T e_P T e_η u_η^{-1}, which is zero by (10) and T²=0. Thus γ_C is well-defined on 𝔄/F.

The formulas define an algebra homomorphism End^*(K)→C. To check multiplication, the only product of two degree-one terms with matching endpoints is β_C(c)α_C(a)=γ_C([ca]); this agrees with (7). All others vanish by the idempotents. The left A-action on β and γ and the right F-action on α and γ agree because T is A-linear. The degree-zero actions in the height-one block agree directly with (11). This checks every possible product since degrees greater than two in the source vanish.

We check continuity, the crucial step. The map α_C is continuous on the open subgroup P with its product p-adic topology by continuous multiplication, hence on every u^{-1}P and on 𝔄. For β_C, continuity from the product p-adic topology is immediate, but insufficient. Given a zero-neighborhood U in C^1, first choose a smaller neighborhood V with V+V⊂U. Continuity from the product p-adic topology provides a finite set T_0 of primes and powers f_p^{n_p} such that β_C sends tuples satisfying these finitely many divisibilities into V. This controls all coordinates outside T_0 uniformly. For each p∈T_0, the map

    A_m=A→C^1,  a↦a e_m T e_p,

is continuous for the m-adic topology. Choose N large enough that the sum of its images of m^N over these finitely many p lies in V. Any tuple with c_p∈m^N A+f_p^{n_p}R_p for p∈T_0 splits into a tuple already controlled by the first condition plus these finitely many m^N A terms. Its image under β_C lies in U. This proves continuity from P_τ.

The map c↦β_C(c)T e_η is consequently continuous on P_τ and vanishes on diagonal A. The open-quotient description H=P_τ/A proves continuity of γ_C on H. Multiplication by u_η^{-1} proves continuity on each u^{-1}H, so γ_C is continuous globally. Thus (11) gives a continuous graded algebra homomorphism.

It sends θ to T by (10). It is unique because the expressions (11), with T=θ, represent every element of End^1 and End^2, while degree zero is prescribed. Finally, the finite topology makes End^*(K) separated and complete: each Hom space is a closed subgroup of a product of discrete target modules, its defining A-linearity equations being closed; composition is jointly continuous by controlling the finitely many intermediate images of a finite set of inputs. The degree-zero topology is the required product of adic topologies by I.1. This proves the theorem. ∎

## I.3 — Proved extension to every regular local surface

The same universal presentation holds for a regular noetherian local ring A of dimension two, without assuming completeness. Here is a complete replacement for the rank-one step; it also specifies the necessary completion explicitly.

Put B=Â, F=Frac(A), S=A\{0}, E=E_A(A/m), E_p=F/A_p, R_p=Â_p, and P=∏_{ht(p)=1}R_p. The residual resolution (1) still holds, while D(E)=B. For each p=(f_p) give R_p the topology τ_p with neighborhoods uA+f_p^nR_p, u∉p, equivalently m^N A+f_p^nR_p. Let C_p be its separated completion and put C=∏_p C_p. We will prove, with the natural actions,

    C_p ≅ Hom_A(E_p,E),
    End^1_A(K)=S^{-1}P ⊕ C,
    End^2_A(K)=S^{-1}C / S^{-1}B.                (12)

The coefficient module C need not be identified with P, and no such identification is assumed.

**Density and completion.** The map R_p→Hom(E_p,E), c↦δ_p c, is injective. A nonzero c is a unit times a power of f_p and hence acts surjectively on E_p; if δ_p c=0, then δ_p=0, contradicting the residual resolution (or the surjectivity below). As in the complete case, kerδ_p=(A[1/f_p]+A_p)/A_p, by factoriality and exactness. Thus the induced finite topology on R_p is exactly τ_p, with the same annihilator calculation (8).

To prove density, let h:E_p→E and choose a finite set of inputs. It is contained in the cyclic A-submodule generated by e=1/(u f_p^n) for some u∉p. The value h(e) is killed by f_p^n. Applying Hom_A(A/f_p^n,−) to the residual resolution gives a surjection

    E_p[f_p^n] --δ_p→ E[f_p^n],

because the only nonzero terms are those displayed and Ext²_A(A/f_p^n,A)=0 (the quotient has a length-one free resolution). The source is generated by e over A_p, so there is c∈A_p⊂R_p with δ_p(c e)=h(e). The map δ_p c agrees with h on all the prescribed inputs. Therefore the image is dense. The Hom space is separated complete for the finite topology, as a closed subgroup of a product of discrete copies of E. It is consequently the separated completion C_p, with no additional kernel. Taking products gives C=Hom(I,E) and a dense embedding P_τ→C.

The first summand in (12) is unchanged from the complete case: Hom(F,I)=S^{-1}P with its ordinary restricted-product topology. Dualizing the residual resolution now gives the exact sequence

    0→B→C→D(F)→E→0.

Its first map sends b to (bδ_p)_p. After localization it gives the second formula in (12), and proves that the entire degree-two kernel is S^{-1}B. In particular no extra degree-two kernel is being suppressed. The topology of D(F) has the open subgroup H={h:h(1)=0}=C/B, with the quotient topology by the open-restriction argument already proved. Again D(F)=⋃_u u^{-1}H.

**Universal morphism, with completion justified.** Let a target algebra Q have the prescribed degree-zero algebra F×P×B and an element T satisfying incidence and T²=0. The map P→Q¹, c↦e_mTc, is continuous for the product of τ_p: the finite-coordinate/m^N A argument in I.2 uses only continuity of the left B-component and right P-component, and works verbatim. It is a continuous homomorphism of additive groups, hence uniformly continuous, and extends uniquely to the separated completion C because Q¹ is complete. Denote its extension β_Q:C→Q¹.

This extension is left B-linear and right P-linear. For the right action, use density of P_τ and continuity of composition. For the left action, first use A-linearity on the dense P, then approximate b∈B by elements a_j∈A in the m-adic topology. On Hom(I,E), multiplication by a_j converges pointwise to multiplication by b, since each of its finitely many tested values is killed by some power of m. The corresponding multiplication in Q is continuous. Passing to limits gives β_Q(bc)=bβ_Q(c), first on the dense subset and then on C. In particular β_Q((bδ_p)_p)=b e_mTe_P.

For α_Q use the previous formula α_Q(b/u)=bTe_ηu_η^{-1}, with b∈P. Define on degree two

    γ_Q([c/u])=β_Q(c) T e_η u_η^{-1},  c∈C.

Clearing denominators proves independence of representation. A diagonal b/u∈S^{-1}B maps to b e_mTe_PTe_ηu_η^{-1}=0, so the map factors through precisely the module in (12). The composition rule is β(c)α(b/u)=[cb/u], where C has its natural right P-action. All other products and diagonal actions agree as in I.2. The map is continuous on H=C/B because the map from C is continuous and vanishes on B; continuity extends over every u^{-1}H. The completed positive-degree pieces are topologically generated by P and θ, so density gives uniqueness of the continuous morphism. End(K) is itself separated complete, as before. This proves the universal presentation for every regular local surface. ∎

## I.4 — Proved: every individual adjacent arrow is an explicit completion

Let A be a regular noetherian local ring, let p⊂q be an immediate specialization, and let δ_pq:E_p→E_q be the corresponding residual differential. Put R=A_q, m=qR, and T=Â_p=widehat(R_p). Then

    T → Hom_A(E_p,E_q),   c ↦ δ_pq c

is an injective dense map. The induced topology on T has a basis

    m^N R + (pR_p)^n T,       N,n≥1.

Consequently Hom_A(E_p,E_q) is the separated completion of precisely this topological additive group. This establishes the arrow topology in every dimension, independently of the full presentation conjecture.

**Proof.** Both modules are R-modules, so A-linearity is equivalent to R-linearity. Write h=ht(pR); then dim R=h+1. The regular local ring R_p is Gorenstein and its injective hull is its top local cohomology. Choose a regular system of parameters x_1,...,x_h of R_p. The cyclic R_p-submodules generated by the generalized fractions

    e_n=[1/(x_1...x_h)^n]

exhaust E_p. The annihilator of e_n over R_p is J_n=(x_1^n,...,x_h^n). These ideals are cofinal with powers of pR_p. For h=0, take J_n=0 and e_n=1 in Frac(R). For any finite subset of E_p one can choose n and clear its finitely many R_p-coefficients by a common u∈R\p, so that the subset lies in the cyclic R-submodule R(e_n/u).

Let I_n=J_n∩R. It is pR-primary. Hence R/I_n has dimension one and positive depth, and therefore depth one. The finite-free-resolution bound for regular local rings gives pd_R(R/I_n)≤h; see Stacks, Proposition 10.110.1, Tag 00O7. Applying Hom_R(R/I_n,−) to the residual resolution of R leaves only the terms

    E_p[I_n] --δ_pq→ E_q[I_n]

in degrees h and h+1. The last map is surjective because Ext_R^{h+1}(R/I_n,R)=0. Its kernel W_n=Ext_R^h(R/I_n,R) is a finite R-module.

Given f:E_p→E_q and finitely many inputs contained in R(e_n/u), the value f(e_n/u) lies in E_q[I_n]. Surjectivity supplies a preimage in E_p[I_n]. The latter is generated by e_n/u over R_p, since R_p/J_n is an Artinian complete intersection and its injective dual is cyclic. Thus some c∈R_p satisfies δ_pq(c e_n/u)=f(e_n/u), giving agreement on the prescribed inputs. This proves density, already using coefficients in R_p⊂T.

The map from T is injective. Each nonzero c∈T acts surjectively on E_p: by Matlis duality its dual is multiplication by c on the regular complete local domain T, which is injective. The differential δ_pq is nonzero by the preceding surjection. Thus δ_pq c=0 implies c=0.

It remains to identify the induced topology. Through the cyclic generator e_n, identify E_p[I_n] with (R/I_n)_p. The finite kernel W_n embeds in this ring and localizes to the whole ring: the other term E_q[I_n] vanishes upon localization at p. Accordingly W_n and R/I_n are commensurable R-lattices. Explicitly, finite generation clears denominators in W_n to give b_n∉p with b_n W_n⊂R/I_n; and W_n,p=(R/I_n)_p supplies a_n∉p with a_n(R/I_n)⊂W_n.

The condition δ_pq(c e_n/u)=0 is exactly

    c mod J_nT ∈ u W_n ⊂ T/J_nT=(R/I_n)_p.

As u ranges over R\p, commensurability shows these subgroups are cofinal with uR+J_nT. Because (u,I_n) is m-primary, each such subgroup contains m^N R+J_nT for some N. Conversely m^N is not contained in p, so one can choose u∈m^N\p and obtain uR+J_nT⊂m^N R+J_nT. Finally the J_n are cofinal with the p-adic powers in T. This proves the stated basis.

The target Hom space is a closed subgroup of a product of discrete copies of E_q, hence separated complete. An injective dense map with the induced topology identifies it with the separated completion. ∎

The standard Gorenstein and top-local-cohomology facts used here are recorded in Stacks, Section 47.21, Lemmas 47.21.3 and 47.21.7 and the proof of Lemma 47.21.10; the proof explicitly identifies the injective hull with top local cohomology. Opened URLs: https://stacks.math.columbia.edu/tag/00O7 and https://stacks.math.columbia.edu/tag/0DW6 . Matlis' endomorphism theorem is the same one cited in I.1.

## I.5 — Proved: the diagonal algebra and differential generate densely in every dimension

For every regular noetherian local A, the graded subalgebra of End_A^*(K) generated by End_A^0(K) and θ is dense for the finite topology in each degree. Equivalently, finite sums of saturated-path operators with diagonal coefficients approximate every graded endomorphism on every finite set of inputs.

**Proof.** First fix comparable primes p⊂q and prove the analogous assertion for Hom(E_p,E_q) by induction on ht(q)−ht(p). For gap zero it is the diagonal statement I.1. For gap one it is I.4.

For gap at least two, work over R=A_q of dimension d. Given f:E_p→E_q and a finite set of inputs, choose e=e_n/u as in I.4 so that all inputs lie in Re. Put I=Ann_R(e); this is pR-primary. Since pR≠m_R, the finite R-module R/I has positive depth. Stacks Proposition 10.110.1 therefore gives pd_R(R/I)≤d−1. The last differential of Hom_R(R/I,K_R) is consequently surjective:

    ⊕_{ht(rR)=d−1, p⊂r⊂q} E_r[I] → E_q[I].

Choose a preimage of f(e). It has finitely many nonzero components y_r. For each such r, the assignment e↦y_r gives a well-defined map Re→E_r, since I kills y_r. Extend it to g_r:E_p→E_r using injectivity of E_r over R. The finite sum Σ_r δ_rq g_r agrees with f on Re. By the induction hypothesis, each g_r can in turn be approximated on the original finite inputs by a finite sum of saturated-path operators. Composing with δ_rq gives the required approximation to f.

Finally consider an arbitrary homogeneous endomorphism of the whole direct sum K. A finite set of inputs involves only finitely many source summands E_p, and its images involve only finitely many target summands E_q. For those finitely many pairs, apply the result just proved to the component maps, with the same finite sets of source components as inputs. Insert the endpoint idempotents and sum. The resulting operator has exactly the prescribed values on the original finite set. This proves density globally. ∎

**What these two propositions do not prove.** Dense generation is weaker than a presentation of the completed algebra. A complete domain may map densely, without surjectively, to another complete topological group. Moreover, to construct a morphism from End(K) to every candidate target algebra, the morphism defined on the dense path subalgebra must be uniformly continuous for the finite topology. Neither continuity for each individual arrow nor the existence of an adelic action automatically proves this for arbitrary families or identifies the entire closed ideal of relations. The exact remaining gate is the corresponding quotient-topology theorem together with the assertion that the closed relations are generated by θ² and the incidence relations.

Yekutieli's *The Action of Adeles on the Residue Complex*, Theorem 1.14, p.9 of arXiv:math/0205018v2, constructs a DG action; Lemma 1.11, pp.7–8, gives a useful approximation statement. These results were opened and read. An action does not itself establish the missing kernel or quotient-topology statements, so it is not used as a proof of freeness. URL: https://arxiv.org/pdf/math/0205018 .

## I.6 — Proved: residual columns are exact after closing images

Let R be a regular noetherian local ring of dimension d, p a nonmaximal prime of height h, and K_R its residual resolution. Give each Hom_R(E_p,K_R^j) the finite topology and use postcomposition with the residual differential. Then for j>h,

    closure(im[Hom(E_p,K_R^{j−1})→Hom(E_p,K_R^j)])
      = ker[Hom(E_p,K_R^j)→Hom(E_p,K_R^{j+1})].

At j=h the kernel is zero. In particular the last differential has dense image. This is a precise statement about relations among operators in the actual endomorphism algebra; it does not identify the closed two-sided ideal in an independently completed free algebra.

**Proof.** The differential is continuous, so the closure of the image is contained in the kernel. For the converse let f:E_p→K_R^j be a cycle and fix a finite set of inputs. By the cyclic generalized-fraction construction in I.4, these inputs lie in N=Re for e=e_n/u, and I=Ann_R(e) is p-primary with I R_p=(x_1^n,...,x_h^n). The module

    M=Ext_R^j(R/I,R)

is finite over R. Its localization at p is zero for j>h, because R_p/I R_p has the length-h Koszul free resolution. Consequently some v∈R\p annihilates all of M.

The element e/v is defined in E_p and has the same annihilator I as e. The restriction of f to R(e/v), identified with R/I, is a cycle in Hom_R(R/I,K_R). Restriction to Re multiplies its cohomology class by v, since f(e)=v f(e/v). That class is zero because vM=0. Therefore there is a map b:Re→K_R^{j−1} whose differential equals f on Re.

The cyclic source Re is finitely generated, so b has only finitely many nonzero component maps into the summands E_r of K_R^{j−1}. Extend each such component to E_p by injectivity of E_r, and sum the finitely many extensions to obtain g:E_p→K_R^{j−1}. Its differential agrees with f on all the prescribed inputs. Thus every finite neighborhood of f meets the image, proving the asserted equality.

For j=h, only the summand E_p can receive a map from E_p among height-h primes. Hence this Hom group is T=ÂR_p. Choose any prime r immediately above p and contained in the maximal ideal. Proposition I.4 says c↦δ_pr c is injective, so the next differential has zero kernel on T. ∎

For a height-gap-two interval p⊂q, apply this with R=A_q and j=h+1. It says that the kernel of postcomposition from the full adjacent-arrow family to Hom(E_p,E_q) is the closure of the family obtained by precomposing the residual differential with an element of ÂA_p. Thus the quadratic relation controls this particular kernel after passing to the actual Hom topologies. The additional quotient-topology and universal-map continuity problem remains: it is not legitimate to conclude that the same closure is obtained inside every candidate completed free algebra.

## Earlier higher-dimensional gate — superseded in the open-left-ideal category by I8

The preceding theorems establish the explicitly requested first case A=k[[s,t]], including degree two, and then all regular local surfaces; I.1 establishes the degree-zero assertion in all dimensions. Arbitrary dimension remains a gate. The dual of a longer Cousin resolution gives several intermediate modules, so an argument identifying all higher relations with consequences of θ² is still required. Citing a construction of the residual complex or the residue theorem does not fill that gate. Schenzel's rank-one criterion explains why replacing C_p by R_p without completion in the noncomplete case would have been wrong; the density/completion argument in I.3 repairs exactly that point.

The transcriptions on 43:65–66 do not fully specify a category of topological modules or a tensor-product completion. The theorem states an explicit universal interpretation and proves it; it does not claim that the uncertain transcription uniquely forces that interpretation. A purported proof using a p-adic topology for every arrow has a concrete failure at p=(s), because t^N→0 on the target A_m while t^N is a p-adic unit on the arrow ring.


# I7: complete-ring residual columns are actually exact, and strict above the first arrow

Full proof is in I_complete_columns.tex.

For a complete regular local A and p≠m, Ext_A^j(E_p,A)=0 for every j. Indeed A=Hom_A(E_m,E_m), so tensor–Hom adjunction with an arbitrary projective resolution gives Ext_A^j(E_p,A)=Hom_A(Tor_j(E_p,E_m),E_m). Choose u∈m\p. The source is A_u-local and (E_m)_u=0, so all these Tor groups vanish. Therefore Hom_A(E_p,K_A) is exact as an abstract complex, strengthening I6's closed-image statement in the complete case.

For degree j>ht(p)+1, the map onto cycles is open in the finite topology. Given finite inputs inside N=Ae, take v∉p annihilating the finite module Ext_A^(j−1)(A/Ann(e),A), and enlarge inputs to N'=A(e/v). A cycle f vanishing on N' has a global preimage g by exactness. Its restriction g|N' is a cycle, and restriction to N multiplies that class by v, hence kills it. An injective extension of a local boundary corrects g to vanish on N. Thus the image of Ann(N) contains the open subgroup Ann(N')∩cycles.

The first-arrow topology is deliberately excluded from this strictness assertion. The proof also does not settle simultaneous families of intermediate primes or construct the full continuous universal map in every dimension.


# I8: full universal presentation in the finite-topology category

The complete proof is in I_universal_linear.tex. It establishes the all-dimensional universal property, including every closed relation and quotient-topology issue, for separated complete graded algebras with a basis of open left ideals.

The new argument uses all discrete representations, not only columns in End(K). For any discrete Cousin complex M and any vector v at p, multiply by a outside p to kill its finitely supported differential. Choose a regular sequence J of length ht(p) in Ann(v). The map A/J to the cycles of M sending 1 to av extends uniquely from the complete-intersection Cousin resolution K[J]=Hom(A/J,K). This extension is constructed by localization at successive target primes and exactness of the last residual differential. It hits v after division by a in the p-component. Hence sums of these K[J] map onto every M.

All K[J] are preserved by End(K). The kernel of the surjection onto M is invariant under diagonals and theta. For one kernel vector, involving finitely many inputs in copies of K, I5 approximates an arbitrary residual endomorphism exactly on those inputs by a word polynomial. Thus that endomorphism also preserves the kernel. The quotient M obtains a unique continuous End(K)-action. This proves every relation on every discrete Cousin representation.

For a complete target Q with an open-left-ideal basis, every discrete quotient Q/L is a sum of shifted Cousin complexes. The compatible maps End(K) to Q/L obtained by evaluation at 1 pass to the inverse limit Q. Density proves multiplicativity and uniqueness. This is the required universal map.

The proof does not silently identify all possible topological-algebra conventions. The literal transcription on 43:66 says separated complete graded topological algebra, while 43:64 mentions several possibly incompatible linear topologies. If the intended free object uses the intrinsic open-left-ideal topology of endomorphism rings, the full statement is now proved. If one instead quantifies over arbitrary topological algebras without such a basis, I8 does not settle that enlarged category. I2–I3 do settle it in dimensions at most two.
