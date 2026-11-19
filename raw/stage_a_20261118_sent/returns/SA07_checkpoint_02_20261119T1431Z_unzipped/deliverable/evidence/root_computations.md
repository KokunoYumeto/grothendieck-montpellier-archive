# Supplementary Codex checks: derivations and certificate scope

Checked on 19 November 2026 by GPT-6 Astra Pro; reasoning effort is not exposed. All source line numbers refer to the supplied diplomatic `.tex` files. No archive scan was supplied or altered. A mathematical counterexample below can show that a transcription is false literally; it cannot decide whether the cause is the author’s slip, a transcription error, or an omitted qualification.

The exact arithmetic programs are `code/root_computations.py` and `code/root_lattice_checks.py`; their complete JSON outputs are adjacent to this file. The computations concern particular algebraic identities, finite objects, and counterexamples. The general arguments written below are separate from the finite certificates. External results used without a new proof are explicitly identified by bibliography key.

## 1. Projective envelopes and scalar extension

**CL-SA07-701–706.** Fix an A-linear additive category and an object X with ring o=End(X). If P is a finite projective right o-module, choose an idempotent e in M_n(o) representing it. Where idempotents split, define P⊗_o X as eX^n. For a second projective Q=f o^m, morphisms are the corner fM_{m,n}(o)e. This is exactly the module Hom corner; it proves full faithfulness of the projective-envelope realization. A functor preserving the designated external tensors is determined on those objects and on these corner matrices by its o-object F(X). Conversely that o-object and the existence of the required tensor objects define the functor. This is the restricted evaluation statement actually needed; it does not say that an arbitrary generator determines arbitrary functors.

For finite projective P, let P^∨=Hom_o(P,o), with the opposite variance. A dual basis expresses the identity as Σp_i⊗λ_i. Inserting this identity gives the usual mutually inverse tensor/Hom maps. The construction on free modules is the identity on finite powers; passing to e-summands proves independence of the dual-basis presentation. Yoneda is checked separately: a natural transformation Hom(−,X)→Hom(−,Y) is composition with its value on id_X. The target subcategory of coadmissible functors must contain the representables for this to be the claimed embedding.

On a stack over affine Zariski opens, a locally free rank-one right R-module P is given by copies of R and invertible transition elements. Apply their action to X; effectiveness of descent constructs the twist. Morphisms glue because the Hom presheaf is a sheaf. If R=End(X), the local Hom comparison is an isomorphism, hence so is the global one. Finite local rank uses matrices and additivity. This checks the claimed descent construction conditional on localizability; it does not prove that every A-linear category is localizable.

**CL-SA07-707.** Let A=Z, R=Z[T]/(T(T−2)), X=Z with T acting as0, and Y=Z with T acting as2. The polynomial relation holds in both modules. R is free of rank2 over Z, and both underlying modules are free of rank1. A Z-linear map is multiplication by c. R-linearity says 2c=0, hence c=0. After tensoring with F₂, both actions become0, so every F₂-linear map is R⊗F₂-linear. The source of the purported Hom comparison is0 and its target isF₂. This is a full counterexample, not a failure caused by an infinite presentation.

**CL-SA07-708–709.** For finitely many algebra generators r_i of R, R-linear Hom is the kernel of the finite tuple of commutators h↦(hr_i−r_i h)_i. Flat tensor extension preserves this kernel and the finite direct sum, giving the Hom comparison. Essential surjectivity is a different question. For example C is the category of finite projective Z-modules, R=Z[T], and A′=Z[1/2]. A rank-one R⊗A′-module on A′ with T acting by1/2 cannot be obtained by extending a rank-one R-action over Z: an isomorphic rank-one module over the commutative ring retains the same scalar action, which would have to be an integer. This example uses R finitely generated as an algebra, not finite as an A-module; the nonflat Hom counterexample above satisfies even the latter condition. A fibrewise stack of R-actions has effective descent of actions because morphisms descend, but it is not automatically the naive scalar extension category retaining only global actions. The manuscript’s Spec R locality question therefore remains distinct from the valid Spec A Hom calculation.

## 2. Brandt categories, norm data and the real obstruction

**CL-SA07-711–713,723,725–729.** An invertible O-bimodule P represents the functor P⊗_O−. Tensoring bimodules composes functors, and P⁻¹ gives an inverse. Central scalar λ acts on a determinant/norm of degree n by λ^n, so preserving its chosen trivialization leaves μ_n(A). The separate full exact sequence with ramification quotient is not proved merely by this observation: its norm-surjectivity and order hypotheses remain explicit in CL-SA07-712. For maximal quaternion orders the unnormalized class sequence is the exact published formula Voight(18.4.9), used as an external theorem.

If local conjugators g_i implement an automorphism, on overlaps g_j⁻¹g_i centralizes O and hence lies in the relevant central units. These ratios form a line-bundle cocycle. A global conjugator exists precisely when that cocycle can be killed by compatible local central scalars. This proves the Picard obstruction mechanism, with the appropriate center and descent site fixed.

For a connecting bimodule P, L↦PLP⁻¹ transports two-sided ideals. Associativity and P⁻¹P=O give

\[
(PLP^{-1})(PMP^{-1})=P(LM)P^{-1}.
\]

Under the explicit commuting-ideal condition C, this also transports the symmetry. Changing a chosen equivalence conjugates its automorphism category; the Picard symmetry supplies a coherent isomorphism between these transports. This checks canonicity up to coherent isomorphism. It is not a canonical strict equality and does not choose an object of a torsor. Ferrand2012 is used for the precise bitorsor/band formulation. The page’s generator-independence proof is therefore retained as a proof with stated conditions, rather than misclassified as wholly unproved.

**CL-SA07-715–716.** In the ramified maximal quaternion order over Q_p, the two-sided prime ideal has reduced norm p and its square is the central ideal pO. Quotienting valuations of two-sided ideals by central valuations therefore leaves Z/2. At odd p, squaring is an automorphism of1+pZ_p by Hensel lifting, and F_p^× is cyclic of even order; hence Z_p^×/Z_p^{×2} has order2. At2, the unit quotient has order4, and should not be folded into the odd-prime statement. The residue calculations modulo9,25,49,8,32 in the JSON are checks of those examples only. Hensel lifting, not those finite tables, supports the local-field assertion.

Write the displayed comparison group abstractly as A×U×(Z/2)×R, where all factors have exponent2. The distinguished f has third coordinate1 and other coordinates [p]. The map (a,u,e,r)↦(a[p]^(−e),u,r[p]^(−e)) is a homomorphism onto A×U×R. Its kernel is exactly{1,f}. At the real place p>0, so[p]=1. This proves the quotient identification independently of any choice of point in the comparison torsor.

**CL-SA07-717,720–722.** A groupoid with μ₂ as automorphism group cannot have objects unique up to unique isomorphism. Pinning may reduce the automorphisms, but that requires a specified pinning action; the manuscript’s second-sign question is not resolved by a group-order calculation. For the real obstruction, assume a purported tensor fibre functor sends a supersingular h¹ to a real vector space of dimension2 and includes all its geometric rational endomorphisms. Voight42.1.9 gives the definite quaternion algebra B_{p,∞}; after tensoring with R it is H. Any nonzero finite-dimensional left H-module is free over the division ring H, so its real dimension is a positive multiple of4. It cannot be R². The same obstruction holds at every real embedding of a totally real coefficient extension. This argument must not assume that every geometric endomorphism is already defined over an arbitrary small finite base field.

For characteristic p>3, a short Weierstrass equation y²=x³+b (b≠0) has automorphisms (x,y)↦(u²x,u³y) with u⁶=1, giving6 at j=0. For y²=x³+ax (a≠0), u⁴=1, giving4 at j=1728. These are the two exceptional cases relevant to the transcribed reversal. The characteristic2 and3 cases are not covered by this argument.

## 3. Finite fields and the failed canonical quotient

**CL-SA07-718–719.** Over F₂,

\[
\Phi_7(T)=(T^3+T+1)(T^3+T^2+1).
\]

The script checks the exact product. Both cubics take nonzero values at0 and1, hence have no F₂ root and are irreducible. They are distinct and coprime. The Chinese remainder theorem gives F₂[T]/Φ₇≅F₈×F₈, with64 elements. This contradicts the proposed F₈ quotient while satisfying p=2,n=3 exactly.

More generally, primitive (p^n−1)st roots in an algebraic closure have Frobenius orbit of length ord_{p^n−1}(p)=n: p^n≡1, and for0<d<n the positive integer p^d−1 is smaller than p^n−1 and cannot be divisible by it. The case p=2,n=1 has modulus1 and is treated directly by Φ₁=T−1. Thus choosing one irreducible factor gives degree n; choosing the whole cyclotomic polynomial usually gives several factors. Even these individual choices do not specify embeddings for all extensions, let alone a canonical compatible algebraic closure. ConradFiniteFields is the opened reference for the quotient and cyclic-group facts.

**CL-SA07-769.** If F_p^×=⟨g⟩ and p is odd, −1=g^((p−1)/2). It is a square exactly when (p−1)/2 is even, equivalently p≡1 mod4. The finite residue table is illustrative, not the general proof.

## 4. Positive involutions and compact norm-one groups

**CL-SA07-730–733.** We use MilneCM2020 Proposition1.39 for the classification, rather than claiming an independent proof of that theorem: a finite commutative Q-algebra with positive involution is a product of totally real identity factors and CM conjugation factors. Over R it becomes R^r×C^s, with identity or complex conjugation. The norm-one equation gives signs on the real factors and unit circles on the complex factors. Consequently the identity component is(S¹)^s, a compact torus; the entire group need not be connected. The tensor-unit example B=Q is a positive-involution algebra but not CM. For a noncommutative algebra A=M₂(Q) with transpose, aa*=1 instead gives O₂, whose full algebraic group is not a torus. Neither calculation identifies a motivic Hodge cocharacter uniquely; weight, involution and Hodge data are kept separate.

## 5. Analytic continuation, paths and primitives

**CL-SA07-735–739.** The real/complex analytic identity theorem propagates vanishing Taylor coefficients along a connected domain. For Banach-valued functions, apply continuous linear functionals; they separate vectors. On a real p-plane in C^p, derivatives in the real coordinate directions recover the holomorphic Taylor coefficients, so vanishing on an open piece implies local vanishing. In one variable an analytic function with a first nonzero Taylor coefficient has isolated zeros; the accumulation-point criterion is therefore valid only with an accumulation point inside the domain. The connectedness of pairwise overlaps is used before gluing, not inferred afterwards.

The square-root branches on15/064 obey the stated sign rules by direct substitution of θ′=θ+2π or θ′=θ. They give opposite conclusions on the two overlap components, explaining both the connectedness hypothesis and the proposed H′ reading. For a chain of single-valued extensions of a fixed function, the union of the domains is connected and the functions agree because the chain is ordered by extension. Their union is analytic locally, providing an upper bound for Zorn. Uniqueness on a fixed domain follows from the identity theorem; uniqueness of the maximal domain does not follow.

**CL-SA07-740–742.** On a convex ball, a closed C¹ real one-form ω=Σf_i dx_i has local primitive

\[
g(x)=\int_0^1\sum_i f_i(a+t(x-a))(x_i-a_i)\,dt.
\]

Differentiate under the integral. Symmetry ∂_j f_i=∂_i f_j makes the derivative integrand a t-derivative, yielding ∂_j g=f_j(x). This works for Banach-valued coefficients by continuous integration and differentiation. Cover the compact image of an endpoint-fixed homotopy by finitely many such balls and subdivide its parameter square. Integrals along shared edges cancel; each cell has zero boundary integral because ω has a local primitive there. Thus the two boundary paths have the same integral. On a domain with every loop null-homotopic, this gives path independence and a global primitive. This is the meaning of the manuscript’s “contractile”; no contraction of the whole space is used.

Open connected subsets of Euclidean space are polygonally connected: the set reachable from a is open, and its complement is open by the same small-ball argument. A compact path can be replaced by chord segments inside finitely many convex balls, with straight homotopies keeping endpoints fixed. The displayed interpolation must have the constant denominator t_{α+1}−t_α; the printed moving denominator becomes z/(1−z) on[0,1] and diverges at the right endpoint. This calculation checks the reading alarm, not the ink.

The star-shaped contraction a+(1−s)(γ(t)−a) remains in the domain. For concatenation, two independently chosen homotopies need their common endpoint to agree for every s. Agreement only at s=0 and1 does not define a continuous concatenated homotopy at intermediate times. This is a valid construction warning, but it is narrower than the literal existence claim in the remark on15/035. If deformation means unrestricted homotopy of maps from an interval, every path γ contracts to its initial point by H(t,s)=γ((1−s)t). Any two paths whose images lie in the same path component are therefore freely homotopic, by connecting their initial points. In that interpretation the claimed failure of existence of a homotopy between the concatenations is false. If both individual homotopies fix their endpoints, the concatenation exists as well. A version concerning loops while preserving loop closure, or prescribed endpoint tracks, can have a genuine obstruction; those additional restrictions are not stated in the supplied remark. CL-SA07-771 records this distinction rather than silently replacing the source with the valid construction warning. Hatcher2002, §1.1 pp.25–26, provides the exact endpoint-fixed comparison.

## 6. ODE coefficients, Frobenius and p-adic qualifications

**CL-SA07-743.** Put δ=x−x₀ and solve

\[
v'_j(t,\delta)=\sum_i\delta_i U_{ij}(x_0+t\delta,v),\qquad v(0,\delta)=y_0.
\]

Let w_{kj}=∂_{δ_k}v_j−tU_{kj}. Differentiating in δ_k and then subtracting the t-derivative of tU_{kj} gives

\[
w'_{kj}=\sum_{i,h}\delta_i(\partial_{y_h}U_{ij})w_{kh}
+t\sum_i\delta_i\left(\partial_{x_k}U_{ij}-\partial_{x_i}U_{kj}
+\sum_h U_{kh}\partial_{y_h}U_{ij}-\sum_h U_{ih}\partial_{y_h}U_{kj}\right).
\]

The bracket is exactly the Frobenius compatibility condition. It vanishes; w(0)=0, so uniqueness for a linear ODE gives w=0. At t=1 this yields the required partial derivatives. The script’s generic2×2 indeterminates certify the signs and contractions for that size. The displayed indexed derivation, not numerical sampling, proves the cancellation for arbitrary p,q. The corrected factor U_ih in the last summand is forced. Penot1970 Theorem1.1 is used for the general analytic/Banach theorem, including its hypotheses; no proof over arbitrary non-Archimedean open sets is inferred.

**CL-SA07-744–746.** Comparing coefficients in y′=f(x,y,z) gives m h_i(m,μ) as a finite sum of right-hand-side coefficients and products of h_j(s,ν). Each product factor belongs to the jth unknown whose power was substituted. Because every unknown has zero x-constant term, s≥1 for a nonzero factor. The equation m−1=n+Σs and the parameter exponent equations imply that each involved coefficient has smaller total degree than m+|μ|. Division by m in characteristic zero therefore gives formal existence and uniqueness recursively. A proof of convergence must be separate.

For ordinary real/complex analytic functions, the positive majorant argument gives a sufficiently small convergence neighborhood and analytic parameter dependence. Uniqueness gives composition of local flows and the inverse-time identity. Any finite bound used in that proof is taken on a smaller bounded neighborhood where it is valid; an arbitrary open product need not have a maximum.

Here is an independent proof of the non-Archimedean convergent-germ version in CL-SA07-746, including finitely many parameters. Let K be complete of characteristic zero with a nontrivial rank-one non-Archimedean absolute value. Translate the initial point to the origin and the initial value to zero. Shrink and rescale x=a t, y=b u and parameters z=c v inside a polydisc on which the right-hand side has an absolutely convergent power series. Choose b and c first, then a sufficiently small. The coefficients of F(t,u,v)=(a/b)f(at,bu,cv) then all lie in the valuation ring O_K: on a smaller polydisc the rescaled coefficients are bounded, and the additional a/b factor makes that bound at most1. For vector-valued y one may use a common b.

On O_K[[t,u,v]] the derivation D=∂_t+Σ_j F_j∂_{u_j} preserves integral coefficients, because every integer has absolute value at most1. Put b_{n,j}(v)=(D^n u_j)|_{t=u=0}, so every coefficient of b_{n,j} has norm at most1. The formal series

\[
U_j(s,v)=\sum_{n\ge0}\frac{b_{n,j}(v)}{n!}s^n
\]

solves U′=F(s,U,v), U(0,v)=0. Indeed, the iterated Leibniz rule makes exp(sD) multiplicative coefficient by coefficient; after evaluation at t=u=0, exp(sD)t=s and exp(sD)u=U. This proves the formal differential equation. All coefficient operations are finite for each fixed monomial, so the argument does not assume analytic convergence.

The restriction of the absolute value to Q is either trivial or a positive power of a p-adic absolute value. In the first case |1/n!|=1. In the second, v_p(n!)≤n/(p−1), so |1/n!|≤A^n for A=|p|^(−1/(p−1)). It follows that the displayed series converges absolutely for |s|<A^−1 and each |v_i|<1; the polynomial number of parameter monomials of a fixed degree is absorbed by any strict radius bound. Shrinking once more keeps U inside its original coordinate polydisc. The coefficient recurrence gives uniqueness as a formal series and hence as an analytic germ. This proves the required local solution and analytic parameter dependence, without asserting an optimal radius or uniqueness among all locally analytic functions on a fixed disconnected p-adic domain. Discretely valued fields such as Q_p are included; “nontrivial absolute value” must not be confused with “nondiscrete value group.” KedlayaFoundations supplies the independently opened p-adic exponential comparison. Lutz1937 was checked only at the level of publisher metadata and is not used as a substitute for this proof.

**CL-SA07-747–748.** For y′=0 on Z₃, let v(x)=3^N on1+3Z₃ and0 on the other residue classes. Each class is open and closed, so v is constant on a neighborhood of every point, locally analytic, and has derivative0. It has initial value0 at0 and differs from the zero solution. Given a smaller ball U=3^mZ₃, use3^m+3^{m+1}Z₃ instead; given any target neighborhood V of0, choose N large enough that3^N∈V. Thus shrinking U,V never creates uniqueness among all locally analytic functions on that fixed domain. These solutions have the same germ at0, so the counterexample does not refute germ uniqueness.

For y′=1+y, y(0)=0, the unique formal solution begins x+x²/2+…. Over Q₂ the norm of the coefficient1/2 is2. The corresponding real exponential majorant coefficient1/2 cannot dominate it. The missing factor is |1/m|_K, with appropriate radius control; the displayed non-Archimedean majorization is literally false.

## 7. Implicit majorants and analytic-series estimates

**CL-SA07-749–751.** In the symmetric majorant system all v_i are equal. Multiplying the denominator in equation(9) and rearranging equation(10) gives v−av²=b, a=qμ(1+qMμ), b=M((1−μΣt_j)^(−1)−1). Substitution of (1−sqrt(1−4ab))/(2a) yields zero exactly, as checked symbolically. Its zero branch at the origin is analytic in a sufficiently small real neighborhood. The local uniqueness argument estimates the maximum difference by ε times itself, with ε<1, forcing equality. It cannot be interpreted as an order comparison over an arbitrary field.

The generalized binomial recurrence gives

\[
\sqrt{1-4x}=1-\sum_{n\ge1}\frac{\binom{2n}{n}}{2n-1}x^n.
\]

Removing the denominator2n−1 makes the x² residual of the squared series equal−8. The program checks the candidate through degree8, but the general proof is the binomial coefficient identity (or the coefficient recursion from y²=1−4x with y(0)=1 and invertible2). Over a non-Archimedean field the convergence neighborhood depends on valuations of denominators. The implicit theorem at y=1 uses derivative2, so characteristic2 is excluded.

**CL-SA07-752–755.** If ||b_nm||r^(|n|+|m|)≤M and |m|≥2, then

\[
\|b_{nm}u^n w^m\|\le M r^{-2}t^2\,2^{-|n|}(t/r)^{|m|-2}
\]

for ||u||≤r/2 and ||w||≤t. The factor r^(−2) is compulsory. With f=z²,u=0,r=1/4,t=1/16,M=1/16, the actual remainder is1/256. Even allowing the displayed upper bound to sum over all n≥0,m≥2, its dimensionless sum is2·(1−1/4)^(−1)=8/3; the literal bound is1/1536, still too small. The corrected bound is valid. Thus the counterexample does not rely on ignoring other terms of the stated sum.

Polynomial coefficient weights do not preserve convergence at a fixed boundary point: Σ(n+1)^(−2) converges at radius1 but multiplication by n+1 gives the divergent harmonic series. On every smaller radius ρ<r, n^β(ρ/r)^n is bounded and summable after a further harmless geometric factor. This repairs derivative and primitive estimates. For a closed form, equality of mixed derivatives gives n_j c_{k,n−e_k}=n_k c_{j,n−e_j}; division then defines consistent coefficients b_n, with the constant chosen separately. The bound on |1/n| is absorbed by a smaller radius, giving a local primitive. It does not force uniqueness on an entire disconnected p-adic domain.

Composition and continuous multilinear operations are justified by absolute sums and the bound ||B(v₁,…,v_m)||≤||B||∏||v_i||. Re-expansion at an interior point follows by binomial expansion inside a smaller polydisc where the translated absolute majorant converges. Derivative series converge on smaller polydiscs and may be iterated. These are the exact mechanisms checked in CL-SA07-753,756–757; none asserts arbitrary boundary convergence.

For CL-SA07-758, the two points1 and exp(2πi/13) both lie in |z−1|<1/2 because their distance is2sin(π/13)<2π/13<44/91<1/2. They have the same13th power. The derivative13z¹² never vanishes on this disc, which excludes0. Thus a local inverse need not be a global inverse. A vanished Jacobian only supplies local rank reduction near a point of maximal rank; it cannot on its own give global polynomial dependence. For example z and exp z are algebraically independent as entire functions: a polynomial relation becomes a finite sum Σp_k(z)e^{kz}=0, and along the positive real axis the largest exponential degree dominates all smaller ones after division, forcing its polynomial coefficient to vanish, then inductively all coefficients.

## 8. Root-lattice exercises

The separate exact program constructs the simply laced Cartan matrices with arm lengths(2,2,1) and(3,2,1). Their determinants are3 and2. Reflection closure of the simple roots produces72 and126 roots. No floating-point approximation or root database is used. Modulo3 or2 the Cartan radical has dimension1. Taking its quotient models Q/3P or Q/2P, respectively.

For the E₆ reconstruction, all72 roots have distinct quotient images, exactly the norm-one vectors. The generated permutation group has order51840; adjoining minus identity gives103680, and minus identity was not in the original Weyl group. The full orthogonal group order in dimension5 overF₃ is2·3⁴(3²−1)(3⁴−1)=103680. This verifies the intended finite orthogonal realization. The orientation subgroup has half the Weyl-group order,25920. The exact Q/3P construction and the distinguishing index-two subgroup occur in BourbakiLie4to6, ChapterVI §4 Exercise2(a–c), pp.242–243 in the opened2002 English translation of the1968 French work. Hamm2016§7.1 supplies the PSp₄(3) name. The program does not certify simplicity. The missing manuscript heading is supplied as an identification, supported by this exact published parallel, not as an emendation of the transcription. Collective Bourbaki authorship is not evidence of sole Grothendieck authorship.

For E₇, the126 roots have63 nonzero quotient images, identifying each root with its negative. The Weyl group on the full roots has order2903040, while its quotient image has order1451520. The kernel has order2 and contains−identity; hence it is exactly{±1}. The symplectic order formula gives

\[
|\operatorname{Sp}_6(\mathbf F_2)|=2^9(2^2-1)(2^4-1)(2^6-1)=1451520.
\]

Since det(−I)=−1 in rank7, the determinant-one Weyl subgroup maps isomorphically onto this quotient. The exact Q/2P statement, kernel and determinant-one restriction are BourbakiLie4to6, ChapterVI §4 Exercise3(a–c), p.243; Hamm2016§8.1 supplies a later comparison. The alternate E₈ argument suggested by the sheet is not recorded as a second completed proof.

## 9. The coherent-cohomology fragment

CL-SA07-762 uses the actual displayed exact segment

\[
H^i(V,O_V(-E_\varphi)[nE])\longrightarrow H^i(V,O_V[nE])
\longrightarrow H^i(V,K[nE]).
\]

Its assumption H^i(V,K[nE])=0 for i≥1 and n≥n₀(K) makes the first map surjective. The identification O_V(−E_φ)≅O_V(−E) gives the claimed inequality of finite dimensions with (n−1)E. There is no shift to H^{i+1}(K[nE]) in this fragment, and K is not silently replaced by a kernel. The supplied final sentence breaks off; no stronger vanishing or stabilization conclusion is manufactured.

## Scope of the checks

The sources on Frobenius, Deuring’s theorem, positive involutions, root-group simplicity, and general cohomology are used at the locators recorded in the bibliography/search ledger. The local algebra, norm quotient, counterexamples, coefficient identities and exact finite actions above were actually checked in this run. Neither a source abstract nor a finite numerical sample is counted as an independent proof of a general external theorem.
