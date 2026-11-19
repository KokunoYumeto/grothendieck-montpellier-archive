# Independent checks of cote 84, scans 2–96

These are this consolidation run's arguments, not words restored to the manuscript. Physical source locators are in `root_reading_notes.md`; symbolic certificates are in `programs/root_computations.py` and `outputs/root_computations.json`. The base ring is commutative with identity. No division by 2 is used unless a hypothesis explicitly permits it. References are matched separately in the claims and search ledgers.

## P01. The graded monoid and the seven subalgebras

Write the two sorts as R0 and R1, with alpha:R0→R1 and beta:R1→R0. The even–even and even–odd products use the given multiplications and alpha; odd–odd uses beta. Enumerating the eight parities of three inputs reduces associativity to the two compatibility identities displayed on scan2. Certificates R01 cover precisely those eight cases. The factor-four realization satisfies both identities by ordinary multiplication of line-valued sections. The powers of a formal odd element produce the integer floor(n/2); negative powers require invertibility. This does not define an Arf invariant of every quadratic bundle: the manuscript has not supplied such a construction or all its hypotheses.

For A_i=R[u_i]/(u_i²+c_i), the eight square-free monomials form a basis of A1⊗A2⊗A3. Each nonzero vector in F2³ specifies one monomial and a rank-two subalgebra; each two-dimensional subspace gives a rank-four subalgebra. There are seven of each. Closure is checked by adding exponents mod2 and using u_i²=-c_i. The proposed tensor product of the even-monomial algebra and the complementary algebra has determinant a sign times (c1c2c3)² (R03), so it is an isomorphism if all c_i are units. However A_i is étale iff its discriminant -4c_i is a unit. Thus the manuscript's equivalence between c_i being units and étaleness requires 2 invertible. In characteristic2, conjugation is the identity here, so fixed-ring interpretations by sign involutions cannot be carried over unchanged.

## P02. Similarity, wedge duality and primitive forms

Over a local ring, two nonzero vectors u,v generating the same cyclic submodule differ by a unit. Indeed v=ru and u=sv; if r is a nonunit then 1-sr is a unit and (1-sr)u=0 forces u=0. The zero vector is harmless. An injection from an invertible module into a finite locally free module is universally injective precisely when its coordinates generate the unit ideal: the necessity follows by passage to each residue field, and the sufficiency gives a local splitting. This is the primitive, rather than merely faithful, condition.

For a rank-two free E with basis (e1,e2), put u=[[a,b],[c,d]]. The form x↦x∧u(x) has coefficients (c,d-a,-b) in the determinant basis; u(x)∧x is its negative. Its kernel as a map End(E)→Sym²(E∨)⊗det(E) is exactly the scalars, and it is surjective coefficient by coefficient. The statement glues naturally under basis change. Cayley–Hamilton proves closure of O+Ou under multiplication. If the resulting binary form is primitive at a point, u is nonscalar over that residue field. A nonscalar operator on a two-dimensional vector space has a cyclic vector over any field: if every line were stable, testing two independent vectors and their sum would make it scalar. Lift a cyclic vector; its determinant remains a unit in a neighbourhood. E is then free of rank one over O[u]. This proves the primitive correspondence locally without excluding F2.

For q=αx²+βxy+γy² choose u_q=[[0,-γ],[α,β]]. It satisfies u_q²-βu_q+αγ=0 and q(vx)=det(v)q(x) for v in O[u_q] (R08–R09). Wood's local module convention uses the dual V=E∨: her generator acts as u_q^t-βI. R10 checks this convention. Identifying the two constructions without this duality would be inaccurate.

## P03. Norm torsors: the topology matters

Let A be a finite locally free quadratic algebra. Its unit group Res_{A/S}Gm is the open norm-nonzero locus in the rank-two vector bundle A, hence smooth over S. The determinant norm to Gm is an epimorphism for the fppf topology: adjoining a square root of any unit and using the corresponding scalar unit gives a finite locally free cover. Thus 1→G_A→Res Gm→Gm→1 is an exact sequence of fppf sheaves, even when the kernel G_A is not smooth.

The claimed equality of fppf and étale classifications on scan27 fails. Set k=F2(t), A=k[ε]/ε², and q=t x² on E=A with coordinates x+yε. The form is primitive because t is a unit; its associated quadratic algebra is the dual-number algebra. Norm(a+bε)=a², so q(vz)=N(v)q(z). Its norm-one-frame torsor is x²=t^-1 with y arbitrary. It is nonempty after the finite flat extension k(√(t^-1)), but has no point over any separable algebraic extension of k. A field étale cover only supplies separable extensions. Thus it is a genuine fppf G_A-torsor that is not étale locally trivial. The fppf version of the classification survives; the étale version requires an additional smoothness hypothesis (e.g. A étale, or 2 invertible). This is a counterexample to the parenthesis, not to the entire primitive-form correspondence.

The Hilbert–90-like surjection A×→ker(N), u↦u/bar(u), also fails for arbitrary nonétale algebras. In characteristic2 for A=k[ε]/ε², conjugation is the identity, so this map is constant1, whereas every 1+bε has norm1. For an étale quadratic algebra the standard torsor statement applies; the nonétale case cannot be inferred from it.

## P04. The withdrawn square-root identification

For E invertible over a quadratic A, End_O(E)/A has the tensor-square description E⊗_A E⊗(det_O E)∨, with the relevant conjugation on the dual action. There is no general isomorphism with E, even up to tensoring by a line on the base. On S=P1, let A=O×O and E=O⊕O(1), with the two factors acting on the two summands. The quotient of the endomorphism algebra by the diagonal A is O(-1)⊕O(1), in the two off-diagonal entries. A base-line twist E⊗O(k) has summands O(k),O(k+1). These cannot simultaneously equal O(-1),O(1), nor their interchange. The square formula gives exactly those two off-diagonal line bundles. This confirms the author's explicit retraction on scan32; it does not license reading his abandoned premise as a final theorem.

## P05. Reflections and characteristic-two uniqueness

For A=R[u]/(u²+bu+c), multiplication by u is U=[[0,-c],[1,-b]]. Canonical conjugation is S=[[1,-b],[0,-1]]. Direct calculation gives S²=I, SU=bar(U)S. Every conjugate-linear endomorphism is m_z S after a local A-basis of E is chosen, and det(m_zS)=-N(z). This exhibits the conjugate-linear maps as an invertible A-module and their determinant -1 locus as a norm-one torsor. The formula σ_e(x)=B(e,x)e-x for Q(e)=1 is conjugation in the basis defined by e, so preserves Q and squares to the identity. R11–R17 verify these polynomial identities.

In A=F2×F2 both identity and swap induce -1=1 on A/O. They are distinct algebra automorphisms. Therefore the corollary on scan36 is false if it characterizes conjugation only by this quotient action. A nonidentity-on-characteristic-two-fibres condition repairs the étale case. The main statement contains an overwritten qualification whose exact wording remains an ink question.

The valid covariance is f(uD)=(u/bar(u))f(D), with action conventions fixed. Replacing u/bar(u) by bar(u)² or its inverse requires N(u)=1 and the correct left/right placement. R12–R14 support the first formula, not an unrestricted trailing simplification.

## P06. Discriminant, parity and the trace lattice

Use δ=T²-4N. In a rank-two pointed norm space, the polar determinant is -δ. With the source's definition of φ_N, Q(φ_N(x))=-δN(x), not +δN(x). The local calculation R19–R24 checks the sign, the trace lattice and its norm simultaneously; Q(T)=-δ. These are mathematical alarms for the transcribed signs, not a decision about the ink.

Assume multiplication by2 is injective on O_S. A quadratic algebra determines L=(A/O)∨, δ∈L² and T0∈L/2L with T0²=δ mod4. Locally choose a lift T and define n=(T²-δ)/4, which is unique. The algebra is O[u]/(u²-Tu+n). A change T↦T+2r changes n by rT+r² and is implemented by u↦u+r (with consistent direction). These changes glue under line trivializations; the local descriptions prove existence and uniqueness of the classification. The trace-coordinate lattice b≡rT0 mod2 has multiplication and norm as on scan51; divisibility is built into that lattice, so one need not invert2. A section corresponds to a root z of z²=δ satisfying z≡T0 mod2 via x=(T+z)/2 on a 2-regular base.

The regularity condition is essential. Over F2, the split algebra F2×F2 and F4 both have trace parity1 and discriminant1, but are not isomorphic. R26 checks the two multiplication tables and splitting behaviour. One cannot extend the triple classification to arbitrary 2-torsion bases by formal base change.

## P07. Why the congruence subgroup is not representable

Consider the functor F(R)={λ∈R×:λ²=1 and λ-1∈2R}. At its identity section, on the square-zero algebra A⊕M its tangent functor is

    T_F(M) = 2M ∩ M[2].

Suppose A is local, 2 is nonzero, and 2 is not a unit. Put M=A/4A. Then 2M≠0: if 2=4a in A, the unit 1-2a would annihilate2, a contradiction. The exact sequence 0→M[2]→M→2M→0 has both outside modules killed by2, so their tangent groups are zero, while T_F(M)=2M is nonzero. Hence this tangent functor is not left exact. For a represented functor, the tangent functor at a section is Hom_A(e*Ω,M), which is left exact. The same assertion follows directly by taking derivations in an affine neighbourhood; it imposes no finite type hypothesis. This contradiction proves nonrepresentability by schemes (and, by étale-local cotangent descent, by algebraic spaces).

For a root-congruence functor z²=δ, z≡T0 mod2, a chosen root has tangent {m∈2M:2zm=0}. On M=A/4A this is again 2M; on the outside modules it is zero. The required flat cover must respect parity: choose a local liftT and c with δ=T²+4c, adjoin x with x²+Tx−c=0, and put z=T+2x. This is a finite free rank2 cover and gives the required congruent root. Faithful flatness keeps2 nonzero somewhere above the chosen local point; the same local argument applies. This gives an independent proof of the manuscript's nonrepresentability obstruction. R50 records the concrete A=Z/4 case; the module argument proves the general assertion. A second reader independently checked the tangent and torsor arguments and supplied this explicit parity-compatible root cover.

## P08. Characteristic-two group schemes and pointed norms

In characteristic2, F_T(u)=u²+Tu is additive and monic of degree2, so the corresponding map of affine lines is finite locally free of rank2 and fppf-surjective. Its derivative is T; it is étale exactly where T is invertible. The root cover of v²+Tv+N is a torsor under G_T=ker(F_T), since translation by a root of F_T preserves that equation and acts simply transitively after an fppf root extension. For two such groups the map (u,u')↦T'u+Tu' lands in G_{TT'}, as direct expansion shows (R27–R29). This is the additive branch of the order-two group-scheme theory, not a claim that every quadratic cover is étale.

A quadratic norm on a rank-two module with a primitive distinguished unit and N(1)=1 recovers multiplication. In basis(1,u), put t=B_N(1,u), n=N(u), and impose u²-tu+n=0. Its determinant norm is the given norm, coefficient by coefficient. Consequently the trace must be B_N(-,1). The weaker requirement that 4N-T² descend to the quotient line squared loses information in 2-torsion: the offending mixed coefficient can be nonzero while four times it vanishes (R35). The source itself adds the missing polar condition.

## P09. The integral product of quadratic algebras

For A_i=R[u_i]/(u_i²+b_i u_i+c_i), put

    b=b1*b2,
    c=b2²*c1+b1²*c2-4*c1*c2,
    U=b2*u1+b1*u2+2*u1*u2.

R30 proves U²+bU+c=0 universally over Z[b1,b2,c1,c2] modulo the two monic relations. R31 proves b²-4c=(b1²-4c1)(b2²-4c2), and R32 verifies associativity of the coefficient formula. These are polynomial identities, so hold after every base change; dividing a discriminant calculation by4 is unnecessary. The algebra defined by this equation is not always the image subalgebra in A1⊗A2: in characteristic2 with b1=b2=0, U=0 although the product algebra has rank2. Injectivity and flatness must be checked separately.

Voight's generator in Construction3.14 is w=U+b1b2 after t=-b1 and s=-b2; it equals u1u2+bar(u1)bar(u2). This translation is needed for an exact comparison of the displayed relations.

## P10. The chi-trivialized extension product

Let 0→L→E→O→0 be exact, with a lift T of χ. Then π(x)=χx-Tψ(x) lies in L and restricts to χ id_L. Conversely such a retraction gives the lift. This uses exactness, without cancellation byχ. The product is the pushout of the natural tensor filtration under the prescribed maps on L1⊗E2 and E1⊗L2; the restrictions agree on L1⊗L2. Locally E_i=L_i⊕O x_i and T_i=χx_i-b_i. With these coordinates the product is

    (l1,s1)*(l2,s2) =
      (χ l1⊗l2 + s2 l1⊗b2 + s1 b1⊗l2, s1s2),
    T12=(-b1⊗b2,χ).

R36–R40 verify the retraction, associativity and χT12=T1*T2. This last relation therefore holds for allχ, including zero divisors. The coefficient formula is symmetric, has the displayed unit (R41), and both bracketings act by the identical polynomial on three inputs. Fourfold bracketings likewise have the same multilinear expansion, so the pentagon commutes; the symmetry gives the hexagon. This completes the elementary coherence argument for this early product, not the separate later comparison of two fixed-endpoint constructions.

The universal property must specify a pair (f,α), with α:L1⊗L2→M. For χ=0 and b1=b2=0 the product map on the kernel terms is zero, so f need not determine α. Thus deleting α from the universal data loses uniqueness. If L is invertible, the object is invertible precisely when the class of b generates L/χL: locally either χ is a unit (change the splitting freely), or b is a unit by Nakayama; in either case choose coordinates giving the unit object. This explains the source's criterion and its locality.

## P11. Coinvariants and the failure at two simultaneous ramification points

For line kernels, the tensor-to-product map in compatible bases has matrix

    F = [[2,b2,b1,0],[0,0,0,1]].

It is surjective exactly when (2,b1,b2)=R. The simultaneous involution satisfies F(σ1⊗σ2-I)=0 (R44). If2 is a unit, the usual idempotent decomposition identifies the coinvariants. If b1 or b2 is a unit, normalize that coefficient and eliminate: R46–R47 explicitly express a basis of ker(F) as columns of σ1⊗σ2-I. This proves the isomorphism over rings, not merely equality of dimensions over fields. Conversely its failure of surjectivity at a residue field where2=b1=b2=0 precludes an isomorphism. In characteristic2 with both b_i=0, all involutions are identity while F kills the first three basis vectors (R45).

For arbitrary finite locally free kernels of **positive** rank, the source's final generating condition forces one kernel to have rank1 near any characteristic2 point. The ring proof then works with L1=Rb1 and arbitrary L2=L: use tensor coordinates(a,r,v,s)∈L⊕R⊕L⊕R. The map is F(a,r,v,s)=(2a+rb2+v,s), and its kernel consists of(a,r,−2a−rb2,0). The involution differences of x1⊗v and x1⊗x2 are(v,0,−2v,0) and(b2,−1,−b2,0). They generate that entire kernel. This supplies a full ring argument for positive ranks, including the higher-rank case the source justified only by ranks.

There is nevertheless a literal rank-zero defect in the final statement. OverF2 take L1=0,E1=F2,T1=0 and L2=F2,E2=F2²,T2=0. Then T1 generates the zero module, so the printed OR-condition holds. Both involutions are identity; the coinvariants have dimension2 while E1*E2 has dimension1. Thus surjectivity does not imply the asserted kernel equality in this case. The exact corrected condition at a characteristic2 point is: **either both kernels have rank0, or one kernel has rank1 and its trace section generates it**. Indeed if exactly one kernel has rank0, the quotient is E_j/(2L_j+Rb_j), which equalsO exactly under that generating condition for the other kernel. This is a mathematical omission of a hypothesis, not a proposed alteration of any transcribed word. Certificate R51 records the counterexample.

The dual invariant assertion follows by dualizing the actual locally split exact sequence under the stated finite locally free hypotheses. It is not justified by a generic fibre dimension count or by an unjustified claim that invariants commute with every base change.

For the map X1×X2→X1∧X2, if one factor is étale, split it étale locally as R×R. The product algebra becomes the other factor, and the source becomes its direct product with itself; this is finite locally free rank2. If both factors are nonétale over an algebraic closure, both are dual numbers. In characteristic≠2 the product generator maps to2xy in k[x,y]/(x²,y²); multiplication by that image has rank1. A free rank-two module over k[z]/z² would have multiplication-by-z rank2. Hence this map is not flat. In characteristic2 the image of z is zero, so it is not even injective (R48–R49). The faithful-flat locus excludes simultaneous nonétaleness in every characteristic, exactly as the author's corrected wording requires. Passage from fibres to the finite-presentation relative locus uses the usual fibrewise flatness criterion; the elementary counterexamples need none of that criterion.

## P12. Limits on the reference comparison

The 2026 Mondal–Venkata Balaji paper gives a further Clifford-algebra formulation of the primitive correspondence. Its Theorem3.12 is used only as a separately identified formulation; Wood already supplies the needed general theorem. Some ancillary prose cannot be carried as established: a degenerate binary form q=0 over a characteristic-zero field has a full Clifford algebra with nilpotents (an exterior algebra), so it cannot satisfy a simultaneous definition as a quaternion algebra with two unit-square generators and anticommutation. This is a check of that ancillary definition/example combination, not a purported refutation of the paper's main correspondence. No priority or dependence claim concerning Grothendieck's undated algebraic pages follows from these later papers.
