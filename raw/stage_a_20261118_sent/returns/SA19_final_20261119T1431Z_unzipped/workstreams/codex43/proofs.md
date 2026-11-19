# Mathematical checks on the Codex cote 43 passages

These are checks and repairs of existing statements, not developed research directions. The source locators refer to the immutable supplied transcriptions. A finite computation is distinguished from a proof of an unrestricted assertion. `exact_checks.py` uses exact arithmetic; its complete stdout is `exact_checks_output.txt`.

## C1. Ray groups, representative signs and completion (4, 7, 10, 13)

For a number field K and modulus m, the idelic subgroup outside the finite support of m is the product of local **unit groups**, not all K_v^*. Otherwise the associated ideal valuations outside m are killed and the advertised ideal-class quotient is lost. With the standard divisor map v, if an idele has component x at v and one chooses a global a congruent to x at v and to 1 at the other modulus places, dividing the idele by a removes its modulus components and gives valuations −v_w(a) outside the modulus. Thus the ideal representative is div(a)^{-1}, unless the reciprocity/divisor convention is inverted throughout. The mod-5 calculation distinguishes 2 from 2^{-1}=3, so the sign matters. It does not decide the handwriting.

For subgroups P,D of an abelian group, the elementary isomorphism is (P+D)/P ≅ D/(P∩D). It is not P∩D ≅ (P+D)/P. The source's E_0 line therefore has an incorrect intermediate identification under its printed definitions.

For a nonarchimedean local field, v:K^*→Z is continuous and surjective. K^* is not compact, whereas Gal(K^ab/K) is profinite and compact. Consequently they are not isomorphic as the indicated topological groups. Reciprocity identifies the profinite completion of K^* with the abelian Galois group and gives isomorphisms at finite norm quotients. This does not contest the finite-level Artin maps on the sheets.

The claim that every finite-index subgroup of a number field's unit group contains a congruence subgroup is indeed supported by Chevalley's 1951 Theorem I: if H has finite index in E, choose m killing E/H; then E^m⊂H and choose the congruence modulus supplied for E^m. This step is not an error.

## C2. Witt-series identities (37–38)

In a ring of characteristic p, the freshman's-dream identity gives f(t)^p=Σ a_i^p t^{pi}. If F acts on coefficients and V substitutes t^p, then FV(f)=VF(f)=f^p. Since addition in the series model is multiplication of series, this is [p]. The exact program checks every series 1+a_1t+a_2t²+a_3t³ over F_p for p=2,3,5, modulo t^{3p+3}; the algebraic identity proves the untruncated result for every characteristic-p ring, not merely a finite field. The plus-sign λ-series convention must be transported to the usual inverse Euler-product convention by f(t)↦f(−t)^{-1}; one must not mix the two choices of Teichmüller generator.

For additive polynomials, a monomial t^n is additive precisely when all interior binomial coefficients binom(n,i) vanish mod p. Writing n in base p and using (1+T)^n=∏(1+T^{p^j})^{n_j} shows that this happens exactly when n is a power of p. Linear independence of distinct total degrees proves that additive polynomials are finite sums Σa_jt^{p^j}, over any F_p-algebra. The code confirms the binomial criterion through degree 49 for four primes; the base-p argument proves all degrees.

## C3. The constant sheaf Z over a finite field (40–43)

Let G=Gal(F_q^sep/F_q)=Zhat act trivially on discrete coefficients. Every continuous map from G to Z has finite image, so H¹(G,Z)=0. Rational coefficients have zero positive continuous cohomology: cochains factor through finite quotients and averaging kills their positive cohomology. The exact sequence 0→Z→Q→Q/Z→0 then gives

H²(G,Z) ≅ H¹(G,Q/Z) = Hom_cont(Zhat,Q/Z) ≅ Q/Z.

Thus the blanket positive-degree vanishing is false. At finite cyclic level H²(C_n,Z)=Z/n; inflation C_nm→C_n multiplies a representative by m, producing the directed union Q/Z. The program checks the compatible embeddings in three exact examples. For a finite étale group with Frobenius F, H¹ is the **coinvariant** group M/(F−1)M. The rational points are the invariants M^{F=1}. Equal orders do not give a functorial identification; the constant-module case does, after the distinguished arithmetic Frobenius convention is fixed.

## C4. The failed Hom/filtered-colimit step (51)

Take R=k[[t]], K=k((t)), p=(0), q=(t). R is a complete noetherian DVR, hence meets the local regular hypotheses. The indecomposable injectives at p and q can be chosen K and E=K/R. Put E_n=t^{-n}R/R. Then E=colim_n E_n, and every E_n is finite over R. The source module K is finite over R_p=K, as required by the page, but not finitely presented over R.

Every R-linear f:K→E_n is zero: for x∈K, write x=t^n y; then f(x)=t^n f(y)=0. Nevertheless the quotient q:K→K/R is R-linear and q(t^{-1})≠0. Therefore

colim_n Hom_R(K,E_n)=0, while Hom_R(K,colim_n E_n)≠0.

The usual finite-presentation hypothesis on the **source over R** repairs the colimit interchange. Finite generation over R_p does not. The finite output records the annihilation calculation; the preceding proof establishes the counterexample, including its nonzero limit map.

## C5. Flag algebra, topology and differential signs (45–69)

For a saturated finite chain, path multiplication is concatenation when endpoints meet and zero otherwise. Threefold concatenation is independent of parentheses; the source supplies this check on scan63. The code exhausts all triples of increasing paths on four vertices (3,375 triples). A quotient by the two-sided ideal generated by Θ² remains associative. In that quotient the **graded commutator** d(u)=Θu−(−1)^{|u|}uΘ satisfies d²(u)=Θ²u−uΘ²=0 and the graded Leibniz rule. The printed plus variant sends 1 to 2Θ; in characteristic different from2 this prevents it from being a derivation. A 2×2 nilpotent matrix makes the failure explicit. This conclusion does not authorize changing the ink.

If d' and d'' commute and both square to zero, (d'−d'')²=−2d'd''. The four-dimensional exact matrix example in the code has d'd''≠0. A totalization needs a degree-dependent sign or anticommuting differentials. Infinite sums over arrows additionally require the restricted product/topology actually chosen; a finite test does not establish convergence in the manuscript's unspecified topology.

In the regular two-variable model, (t−s)^{-1}=Σ_{j≥0}s^j t^{−j−1} exists in k((t))[[s]]. Its coefficients have unbounded negative t-order, so it is not in k[[t,s]][t^{-1}]. The latter only allows a uniform bound on denominators t^N. This proves that localization followed by completion cannot simply be replaced by ordinary localization of the completed two-variable ring. The code multiplies finite partial sums and records the exact last remainder.

## C6. Zariski local cohomology and an invalid change of topology (71–79)

If X=Spec(R) with R local, any Zariski open containing the closed point is X itself. Hence a locally surjective map of sheaves is surjective on Γ(X,−); Γ is exact and all positive Zariski sheaf cohomology vanishes on X. This statement is about the local **space**, not all affine schemes and not the étale/fppf topology.

For a regular local ring of dimension d, a regular parameter sequence is R-regular. Its Čech complex identifies local cohomology H_m^i(R); the regular-sequence computation gives zero for i≠d. For d≥2, the localization triangle yields H^i(X\{m},O)=H_m^{i+1}(R) for i≥1 and Γ(X\{m},O)=R. In dimension1, the boundary is K/R; dimension0 must be treated separately. The same linear calculation underlies the split-unipotent induction on the pages, but it does not by itself establish a representing pro-algebraic Jacobian for every coefficient group.

An unrestricted fppf assertion that the positive cohomology of every connected linear group disappears is false. Let A=C[x,y]_(x), a regular DVR, and K=C(x,y). The quaternion class (x,y) in Br(K)[2]=H²_fppf(K,G_m)[2] has tame residue y in C(y)^*/C(y)^{*2}, which is nonzero since the valuation of y at0 is odd. Here G_m is connected and linear. This is a counterexample only to that unrestricted interpretation; the unclear qualifier and the changed 'Weil' topology on scan77 must be resolved before applying it to the intended statement.

## C7. Supports and Ext (161–162)

For a noetherian ring R, ideal J, finite module M and injective I, Γ_J(I) is injective. At degree0, a map M→I whose image is J-power torsion is killed by one common J^n, because M is finitely generated. Thus Hom(M,Γ_J I)=colim_n Hom(M/J^nM,I). Resolve the second argument injectively; filtered colimits are exact, and the two complexes give the indicated Ext-with-support isomorphism. Localization of a finite presentation and a locally finite resolution gives the quasi-coherent sheaf version. The global noetherian hypothesis permits commuting the relevant filtered colimit through sheaf cohomology. The finite-generation and quasi-coherence assumptions are real; they are not discarded in the modern statement.

## C8. Elementary entries of the Hom/Ext tables (162–165)

For any abelian sheaf G, a homomorphism Z/n→G is determined by the image of1, which is an n-torsion section; Hom(Z,G)=G. This proves two entire finite rows and the Z row, functorially. A map from a geometrically connected group to an étale group which preserves identity is zero. A map from an abelian scheme to an affine group is zero by the constancy of global functions and the identity condition. Hom(G_m,G_m) is the locally constant integral exponent sheaf.

Over R=k[ε]/ε², the polynomial 1+εt is an invertible, nonconstant group-like element of R[t]: (1+εx)(1+εy)=1+ε(x+y). Thus internal Hom(G_a,G_m) is nonzero, although its geometric field points are zero. The analogous issue affects Ga→μ_p and α_p→G_m. Cartier duality gives Hom(α_p,G_m)=α_p and Hom(μ_p,G_m)=Z/p, **as sheaves**, not their k-points.

The restricted-Lie adjunction gives Hom(α_p,G)={x∈Lie(G):x^[p]=0} and Hom(μ_p,G)={x:x^[p]=x}; this requires characteristicp and the group/Lie conventions stated by SGA3 VIIA7.2. For G=A an abelian variety over an algebraically closed field, the first kernel has k-dimension a(A) but its scheme also has infinitesimal factors; replacing it by only its tangent-space dimension loses data.

For the formal Cartier dual V=D(G_a), the hyperalgebra is k[t] with t primitive. A compatible Hopf map into H(G) is specified by a primitive element, giving the formal-category Hom(V,G)=Lie(G). This is not a proof that V is a finite-type algebraic group. Conversely Hom(G_a,V)(k)=Bilin(G_a×G_a,G_m)(k)=0, because k[x,y]^*=k^*. Therefore the questioned Ga→V entry cannot be the full Ga sheaf. The dual formulation and the ind/formal category on scan189 are essential.

Over an algebraically closed field k of characteristic p, begin with the exact Dieudonné-module extension 0→k→M→k→0. The operators F and V map M into the submodule and vanish on that submodule, so FV=VF=0 and hence pM=0. Therefore M is a two-dimensional k-vector space with fixed subobject ke_1 and quotient ke_2. Write Fe_1=Ve_1=0, Fe_2=a e_1 and Ve_2=b e_1, with the usual σ/σ^{-1} semilinearity. Changing the lift e_2 by c e_1 changes neither a nor b; Baer addition adds these parameters (with the convention's semilinear identifications). Thus Ext¹(α_p,α_p)≅k⊕k as additive groups, with labelled kernel and quotient. It is not the set of isomorphism classes of middle groups. The finite code checks the relation for every pair over F_2,F_3,F_5.

For geometric Yoneda Ext with algebraically closed base, the resolution 0→Z→Z→Z/n→0 yields Ext¹(Z/n,G)=G(k)/nG(k), since Ext¹(Z,G)=H¹(k,G)=0 for the represented smooth/finite coefficients in the table. This formula is not the internal Ext sheaf formula over an arbitrary base. For connected smooth G=G_a,G_m,A, a Z-torsor is trivial: its monodromy is a continuous map from a profinite group to torsion-free discrete Z. A normalized multiplication on the trivial torsor has its cocycle in the constant group Z, hence zero on connected G×G; therefore Ext¹(G,Z)=0 in this setting.

## C9. Primitive torsors and extensions (167–170)

Let G,γ be commutative flat group sheaves represented over S, and let P→G be a γ-torsor with a chosen identity section above e. A primitive class supplies an isomorphism between pr_1^*P+pr_2^*P and m^*P. Normalize it at both axes. Differences between two such isomorphisms are maps G²→γ vanishing at the axes. Assume these are zero, and assume the corresponding normalized rigidity for G³ and G. The normalized multiplication is unique. Its two triple composites differ by a map G³→γ vanishing at the identity; rigidity gives associativity. The swapped multiplication agrees by uniqueness, giving commutativity. Each translation P_g→P_{g+h} is a γ-equivariant isomorphism of torsors, so the fiber over −g supplies a unique inverse to a given element. This constructs the extension; it also shows injectivity after forgetting its group structure. Geometrically connected fibers for G and étale γ give the required rigidity. Without these hypotheses 'primitive' alone need not control the associator.

For the Artin–Schreier case over a perfect field k, H¹(G_a,Z/p)=k[t]/(F−1)k[t]. A primitive class can be represented by an additive polynomial. Modulo coboundaries a t^{p^r} reduces to a^{p^{-r}}t, so the group of primitive extension classes is k; over a nonperfect coefficient ring the appropriate statement involves perfection, and arbitrary-base representability is a separate issue. Grothendieck's Chevalley exposé7, final pages, really does contain the primitive Artin–Schreier argument; the citation is not rejected merely because its title concerns Cartan subgroups.

## C10. Finite local pairings and topology (143–146)

For K=F_q((t)), fppf exact sequences give H¹(K,α_p)=K/K^p and H¹(K,μ_p)=K^*/K^{*p}; the Artin–Schreier sequence gives H¹(K,Z/p)=K/(F−1)K. In the residue formula Res(t^i d(t^j))=j·δ_{i+j,0}; exponents divisible byp vanish, explaining why the pairing descends through pth powers. The code constructs nondegenerate finite diagonal blocks for exponents prime top. This is a consistency check of the formula, **not** a replacement proof of topological local duality. The nine-term global theorem needs restricted products and modified Tate groups at real places. The finiteness of Sha for arbitrary abelian varieties is not deduced by writing the analogous sequence.

## C11. Integral lattices, finite-model monodromy and subgroup germs (148–158)

For a continuous representation of a profinite group Γ on finite-dimensional Q_l-space V, choose a lattice L. Its stabilizer is open, hence has finite index. The sum of the finitely many translates of L is a Γ-stable lattice. Tensoring with Q_l is M→V, so the opposite arrow in the display on149 conflicts with its formula and with150.

A finite-index closed subgroup of an l-adic Lie group has the same Lie algebra. More generally a finitely generated extension of fields has finite algebraic constants, so restriction of a Galois representation changes its image by finite index. This supports the finite-model construction. It does **not** say that an arbitrary infinite extension preserves the actual image Lie algebra: the l-adic cyclotomic representation over Q has one-dimensional image Lie algebra, and over Qbar its actual Galois group is trivial. A 'Serre algebra' obtained by retaining models can therefore differ from the actual limit monodromy.

For a compact l-adic analytic group G and a closed subgroup H such that each g has a positive power in H, use a sufficiently small logarithm chart. For x in Lie(G), exp(l^n x) is defined for n large. A positive power in H then implies x∈Lie(H), since the logarithm is a nonzero scalar multiple of x. Thus Lie(H)=Lie(G), so H is open and has finite index. Analyticity cannot be omitted: G=∏_{n≥1}Z/2 and H={0} satisfy g²=1∈H, but the index is infinite. This checks exactly the necessary category distinction.

## C12. Coalgebras, pro-objects and finite presentation (185–193)

Over a field, a finite list in a coalgebra lies in a finite-dimensional subcomodule. Expressing its coaction in a basis produces finitely many matrix coefficients c_ij with Δc_ij=Σc_ir⊗c_rj. Their span is a finite-dimensional subcoalgebra containing the original list after applying the counit. In a commutative Hopf algebra, adjoining their antipodes and taking the generated algebra gives a finitely generated Hopf subalgebra, since S²=1. This proves the field approximation used on192. Over rings, tensor injections and finite projective subobjects require additional conditions; the field proof alone gives no general-ring theorem.

The question whether artinian objects suffice for Pro(C)→C' to be fully faithful is false. Take C=finite sets, C'=sets and X_n={0,1}^n. Every object of C is artinian for its subobjects. A pro-morphism to {0,1} factors through a finite projection. The function δ_0 on lim X_n={0,1}^N, equal to1 only at the zero sequence, factors through no finite projection: a sequence with its first1 later has the same chosen prefix. It is a set map but not a pro-map. If an abelian example is desired, take finite-dimensional F_p-vector spaces inside all F_p-vector spaces; a noncontinuous linear functional on the product exists by extending a basis of the direct-sum subspace, whereas every pro-functional depends on finitely many coordinates. The finite-set example already meets the actual general-category question on191.

For affine schemes over a qcqs base, finite **presentation** gives the required Hom/limit interchange. 'Finite type' is interchangeable with it over a noetherian base, but not over arbitrary nonnoetherian bases. The group laws, identity and inverse are finite diagrams and descend under the finite-presentation hypotheses. This does not make any arbitrary cofiltered system of finite-type approximations a system of group schemes automatically.

## C13. The socle criterion (195–196)

Let k be any field, V an infinite-dimensional k-vector space, and R=k⊕V with V²=0. The category Mod(R) is a Grothendieck abelian category: it has a generator R and exact filtered colimits. Its only simple module up to isomorphism is k=R/V. For every module M, VM is killed by V, hence lies in soc(M). The quotient M/soc(M) is killed by V and is a k-vector space, hence semisimple. Therefore F_1(M)=M for every M in the source's socle filtration.

But R is not a union of finite-length submodules. A submodule of the regular module containing1 must be all R, and R has the infinite-dimensional semisimple submodule V, so has infinite length. More explicitly, every finite-length ideal is contained in V; an element a+v with a≠0 is a unit, and an ideal containing it is R. The sum of finite-length submodules is V, whereas the finite-socle-stage union is R. This also separates the two proposed 'Krull dimension0' subobjects. The source's stated AB5 hypothesis is satisfied by the counterexample.

If the ambient Grothendieck category is **locally noetherian**, finite socle exhaustion does imply local finite length: a noetherian object is contained in one finite socle stage by stabilization; each semisimple subquotient is noetherian and therefore a finite sum of simples. Hence that noetherian object has finite length. Every object is a union of such noetherian subobjects. The repaired statement does not contradict the valid equivalence between small length categories and locally finite-length Ind categories on195.

## C14. Dieudonné normal forms and nonuniform nilpotence (197–202)

With coefficients on the left, Fw=σ(w)F, Vw=σ^{-1}(w)V and FV=VF=p. Consequently

F(w+Σ_{i≥1}a_iF^i+Σ_{j≥1}b_jV^j)
=σ(w)F+Σσ(a_i)F^{i+1}+pσ(b_1)+Σ_{j≥2}pσ(b_j)V^{j−1},

and

V(w+Σa_iF^i+Σb_jV^j)
=σ^{-1}(w)V+pσ^{-1}(a_1)+Σ_{i≥2}pσ^{-1}(a_i)F^{i−1}+Σσ^{-1}(b_j)V^{j+1}.

These are formal coefficient identities wherever the stated topology makes the series converge. The program tests exact finite normal forms in the specialization σ=id; the displayed derivation checks the semilinear coefficients. Localizing at F writes V=pF^{-1}; it does not automatically invertp.

For U assembled from all ker(F^k:W_n→W_n), no fixed F^r kills all U: already in W_1=G_a the subgroup α_{p^{r+1}} has a nonzero F^r. Nor does a fixed p^r kill the whole union. In W_{r+1} over R=k[x]/x^{p^{r+1}}, the vector (x,0,...,0) is F^{r+1}-nilpotent, while p^r acts as V^rF^r and has last coordinate x^{p^r}≠0. Each finite-stage element has some bound; the union has no common bound. The disputed line must be read as local nilpotence or corrected mathematically.

## C15. Tame symbols and the last unfinished pairing (204–208)

For a discretely valued field with residue k(x), writing f=t^a u,g=t^b v gives (f,g)_x=(−1)^{ab}u(x)^b/v(x)^a. Bilinearity and (f,g)(g,f)=1 follow at once. The diagonal is (f,f)=(−1)^{a²}, so 'alternating' must not be substituted for skew symmetry without its sign convention. On P¹, factorization into linear terms proves the product formula, including the contribution at infinity; the code checks three exact examples with overlapping support and poles.

The claimed orthogonality against U fails if U means **all** ordinary unit ideles: take f=t and u with component2 at0 and1 elsewhere. The product is1/2. If U means strict units with residue1, each local symbol with a rational function is1; combined with Weil reciprocity this gives the inclusion against UK^* asserted by the page.

For a Poincaré divisor Θ, replacing Θ by Θ+div(h) changes a divisor-evaluation trivialization on a disjoint cycle z by h(z). Such a factor is not identically1 for unrestricted h and cycles. The canonical biextension pairing uses the accompanying change of rational section/trivialization, which cancels that factor. Scan208 leaves its independence verification unfinished. We therefore record a missing compatibility requirement, not a theorem that every intended pairing is false. The modern Picard–Brauer pairing H¹(S,A)×A∨(S)→H²(S,G_m) is a separate, correctly defined construction.
