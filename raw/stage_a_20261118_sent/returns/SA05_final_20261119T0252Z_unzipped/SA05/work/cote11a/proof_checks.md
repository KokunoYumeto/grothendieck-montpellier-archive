# Targeted mathematical checks — cote 11a

Date: 2026-11-19. These checks are current reconstructions. They do not alter a diplomatic reading and are not claims to have checked the ink. The executed finite computations are in `check_calculations.py` and `calculation_output.txt`. A finite test is not a proof of a universal claim.

## 1. The kernel construction, with explicit hypotheses

Work in a category with finite products, with a contravariant commutative-algebra functor A, functorial additive pushforwards for the maps used, a projection formula, and base change for the product, graph and diagonal squares used below. In this paragraph either everything is ungraded or all the pushforward degree shifts are even, so no omitted Koszul exchange sign is being asserted.

For u∈A(X×Y), v∈A(Y×Z), put v∘u=(p_XZ)_*((p_XY)^*u·(p_YZ)^*v). On X×Y×Z×W both bracketings of three kernels become (p_XW)_*(u_XY v_YZ w_ZW): base change replaces each inner pushforward by a pushforward after adjoining the remaining factor, projection formula moves the remaining factor inside, and functoriality combines the pushes. This checks associativity under the stated axioms. It does not prove that arbitrary Poincaré algebra maps satisfy those base-change axioms.

For the diagonal class e_X=(δ_X)_*1, the product/diagonal square identifies the pullback of e_X with the class of the locus where two X factors coincide. Projection formula and p∘j=id then give u∘e_X=u and e_Y∘u=u. The same graph square gives Γ_g∘Γ_f=Γ_(gf), where Γ_f⊂X×Y for f:X→Y. The action u(a)=(p_Y)_*(u·p_X^*a) satisfies (v∘u)(a)=v(u(a)); Γ_f acts as f_* and its factor transpose as f^*. Stacks 0FFZ uses the opposite graph convention for f:Y→X, so a factor flip is necessary when comparing its graph lemma.

Factor permutation gives (v∘u)^t=u^t∘v^t in the same even convention. External products of two kernels commute with composition by the product base-change square and projection formula. The assertion for arbitrary graded shifts is left conditional on an explicit symmetric monoidal convention; scan 5's signs and scan 29's retraction forbid silently extrapolating.

The identity u(a) adjoint to u^t(b) follows by pairing: κ_Y(u(a)b)=κ_(X×Y)(u·p_X^*a·p_Y^*b). Graded reordering can contribute a sign when u is not central. This explains precisely why the page17 condition on u is not disposable.

For the terminal object e, a coefficient c∈A(e) acts on A(X) by p_X^*c. Pullbacks commute with this action by functoriality. Projection formula gives f_*(p_X^*c·a)=p_Y^*c·f_*a, proving coefficient-linearity of pushforwards and hence of kernel composition/action. Identifying End(e)=A(e×e)=A(e) uses the terminal-product isomorphism. No equality A(e)=a separately fixed ground field is needed.

## 2. Adjoint pushforward and product in the wider commutative category

Let A,B be unital commutative k-algebras with linear functionals κ_A,κ_B. Write φ_B(b)(y)=κ_B(yb). If φ_B is injective and (f^*)^tφ_A(A) lies in imφ_B, there is a unique f_* satisfying κ_B(y f_*x)=κ_A(f^*y·x). Pairing f_*(f^*z·x) and zf_*x with arbitrary y proves the projection formula by associativity and multiplicativity of f^*. Setting y=1 proves κ_Bf_*=κ_A. Composition is the adjoint of the composite pullback by the same identity and uniqueness. Surjectivity of φ_B makes the image condition automatic. This proves the actual weakened criterion on scan 34, including possibly degenerate A.

For finite projective Poincaré A,B, the canonical (A⊗B)^∨≅A^∨⊗B^∨ shows the product trace is perfect. If E is any commutative gauged algebra and E→A,E→B are bivariant morphisms, their pullbacks uniquely extend to an algebra map h:A⊗B→E by h(a⊗b)=h_A(a)h_B(b). Since A⊗B is Poincaré, h has a unique adjoint E→A⊗B. Its composites with the two canonical projections have the specified pullbacks and hence the specified pushes by uniqueness. Thus A⊗B is a product even in this wider commutative category. For a noncommutative E the extension exists only if the factor images commute; this ambient qualification is necessary. Without Poincaré targets the existence of an adjoint can fail.

If f^*:B→A is an algebra isomorphism, put c=f_*1. The projection formula gives f_*x=(f^*)^(-1)(x)c. Thus the bivariant map is invertible iff c is a unit, and is a good isomorphism (push inverse to pull) iff c=1. This verifies the manuscript's warning that an isomorphism need not preserve its trace under pullback.

For homogeneous x,y with |y|=j and push degree δ, reversing the right projection formula gives the factor (-1)^(ij+j(i+δ))=(-1)^(δj). All eight parity cases were executed. If κ_A is supported in degree d_A and κ_B in d_B, duality gives i′=i+d_B−d_A. Both formulas agree with the later even-degree restriction. The tensor-adjoint parity test in code is tied to its stated ordinary tensor-trace convention; it is not promoted to a canonical correction of uncertain ink.

## 3. Cartesian squares need not satisfy exchange

For λ∈Q^× let Q_λ denote Q with trace κ_λ(x)=λx, concentrated in degree 0. There is a unique bivariant morphism Q_λ→Q_μ with pullback id and pushforward λ/μ. It obeys both projection formulas and trace compatibility and is invertible.

Take a commutative square with upper-left Q_2 and the other three objects Q_1. All underlying pullbacks are id; upper and left pushes are2, lower and right pushes are1. Both composite pushes from Q_2 to Q_1 equal2, so this is a commutative square of the manuscript's bivariant morphisms. Every arrow is an isomorphism. Any commutative square of isomorphisms is Cartesian: for a compatible cone, compose its map to the upper-right corner with the inverse upper arrow; compatibility gives the other component, and invertibility gives uniqueness.

The two exchange composites are multiplication by 1 and by 2. All dimensions are0, satisfying the proposed additive dimension relation. Thus cartesianness plus that relation does not imply exchange. This does not refute base change for the geometric cohomological squares for which it is an axiom or a theorem. The refinement is to impose the relevant base-change axiom (or compatible gauge normalization) separately.

## 4. Why specialness cannot be dropped

For a nonempty finite set I let Part(I) be its finite set of set partitions and let B(I)=Q^Part(I), with pointwise product and sum trace. For α:I→J, let r_α:Part(J)→Part(I) pull back an equivalence relation. Define α^*:B(I)→B(J) by precomposition with r_α and α_*:B(J)→B(I) by summing over each fiber of r_α. Pullbacks are unital algebra maps; the fiber-sum formula gives α_*(α^*a·b)=aα_*b and preserves the sum trace. Pullback of equivalence relations and finite summation give functoriality for both maps. Every B(I) has a perfect diagonal pairing.

Let C be the constant Q system with identity maps. There is a natural bivariant transformation C→B whose pullback B(I)→Q is evaluation at the indiscrete partition and whose pushforward Q→B(I) is the delta function at that partition. The indiscrete partition pulls back to the indiscrete partition, so naturality holds for both maps; projection formula and trace compatibility follow directly. The component for a singleton is an isomorphism, while B({1,2}) has dimension 2. The Künneth map B(1)⊗B(1)→B(2) has one-dimensional image. Hence evaluation cannot be an equivalence on unrestricted systems; this checks the earlier run's counterexample and its variance. Code enumerated 56 set maps and 1618 composition/naturality cases for cardinalities≤3, supplementing this general proof.

With special Künneth isomorphisms and multiplicative traces, every component is canonically a tensor power of the singleton component, its pullbacks are generated by the singleton insertions, and its pushes are uniquely their adjoints. This proves the commutative ungraded reconstruction. Hua2026 §1 Theorem 1.2 gives the same restricted prose theorem and proof. Its reported Lean compilation was not repeated here. Empty sets must be added explicitly to discuss the tensor unit; the manuscript first uses nonempty finite sets.

## 5. Diagonal and dual numbers

For A=Q[t]/(t²), deg(t)=2, κ(t)=1 and κ(1)=0, the pairing matrix on (1,t) is [[0,1],[1,0]]. The adjoint of multiplication is Δ_*(1)=1⊗t+t⊗1 and Δ_*(t)=t⊗t. The code checks coassociativity, cocommutativity and the two counits. In general these follow by taking adjoints of associativity, commutativity and the unit, using perfect tensor pairings. The projection formula gives Δ_*(a)=(a⊗1)Δ_*(1), so Δ_*(1) determines Δ_* within this Frobenius setting.

For kernel u=a+b t_1+c t_2+d t_1t_2, integration over the first factor gives operator matrix [[b,a],[d,c]]. The symbolic convolution computation gives M_(v∘u)=M_v M_u and Δ=t_1+t_2 maps to the identity. These are exact polynomial calculations. This model also gives the relation Δ=t_1+t_2 on P¹×P¹, so the various tautological generator lists on later scans cannot be independent for every X. No assumption earlier in this scope excludes this Poincaré algebra or H*(P¹).

## 6. Stable subfamilies and the literal cycle-generator defect

A family closed under the actual operations used in §1 restricts their category structure. Conversely the graph actions recover pullbacks/pushforwards once the graphs, transposes and requisite symmetries belong to the subcategory. Intersections of closed families remain closed; generated families exist by intersection. The multilinear operations on scan 23 compose by applying the kernel-convolution identity with one factor for each input. This needs no separate existence theorem beyond the axioms.

The literal set {f_*1_Y} is not already a ring. At X=Spec k over an algebraically closed field of characteristic 0, CH_Q(X)=Q. For connected smooth proper Y of positive dimension, proper Chow pushforward of its fundamental cycle to the point is 0; in dimension 0 it is a nonnegative degree (a finite disjoint union gives a nonnegative integer). Thus −1 is absent. Taking the additive/Q-linear span repairs this example. Resolution in characteristic 0 shows every irreducible cycle is the pushforward of the fundamental class of a smooth proper resolution, hence yields generation; it does not justify the literal single-value assertion. Resolution is invoked only under characteristic 0 and properness; the dossier does not infer arbitrary-characteristic resolution.

## 7. Earlier-run linear algebra, not an attached cote 16 witness

If v:V→W and u:W→V are isomorphisms, w=uv implies w^(-1)u=v^(-1) by multiplying on the right by v. For a polynomial a_0+a_1t+…+a_nt^n annihilating w with a_0≠0, multiplying by w^(-1) gives w^(-1)=−(a_1+a_2w+…+a_nw^(n−1))/a_0. The saved rational matrices verify one example and its Cayley–Hamilton polynomial.

On a Lefschetz string e_j=L^ja, 0≤j≤m, define Λe_j=e_(j−1) for j>0 and Λe_0=0. The classical lowering sends e_j to j(m−j+1)e_(j−1). Defining D(e_0)=e_0 and D(e_j)=j(m−j+1)e_j gives classicalΛ=ΛD and Λ=classicalΛ D^(-1). Iterating from top to bottom gives unit factor1 versus (m!)². Code checks m≤15; the general proof is the product of the displayed coefficients. No unavailable manuscript location is claimed.

In a formal additive enlargement, End(X⊕Y) is the matrix ring whose entries are the corresponding Hom groups. Multiplication is matrix multiplication with categorical composition. With e_X=diag(1,0), e_Y=diag(0,1), the map u∈Hom(X,Y)↦[[0,0],[u,0]] identifies Hom(X,Y) with e_Y End(X⊕Y)e_X, and taking the lower-left entry is its inverse. These idempotents select objects, not cohomological degrees. The saved symbolic matrix test supplements this general entrywise argument.

## 8. GIT calculations

For a finite weight set S(x) and manuscript convention μ(x,λ)=max_(χ∈S(x))〈χ,λ〉, μ(x,λ_1+λ_2)≤μ(x,λ_1)+μ(x,λ_2) follows termwise. Rational attainment of a positive optimum is a finite rational polyhedral optimization statement; the manuscript leaves the argument as an exercise. It needs a nonempty weight set and a nonzero direction space. Taking S=∅ does not produce a positive optimizing 1-PS, so “every S” requires the contextual nonempty qualification. Kempf's normalized optimality theorem supplies a much stronger instability statement under its own norm hypotheses; it is not an automatic proof for arbitrary convex sets in a building.

If a family of weights satisfies μ_0≥ε||λ|| and |μ_1|≤K||λ||, then μ_1+(n−n_0)μ_0>0 for n>n_0+K/ε. The exact integer choice floor(n_0+K/ε)+1 was tested for 27 rational triples. Finite root/weight test cases do not replace the manuscript's general root-group proof of P_λ invariance.

For λ_2=−λ_1, every character vanishing on λ_1 also vanishes on λ_2. Thus a character-separation argument requiring one value0 and the other nonzero must distinguish negative parallel rays, even though these are distinct positive rays. This is a proof-gap alarm on scan 26, not an assertion that the building injection theorem is false.

## 9. EGA reused sheets

For A=R[[X,Y]]/(X²+Y²), the quadratic has no factor over R and the completed quotient is a domain. Its complexification has the two nonzero factors X±iY whose product is 0, and is a finite étale A-algebra because C/R is finite separable. The completed node has a single real normalization point with residue C, explaining unibranch but not geometrically unibranch. The power-series brackets are reconstructed from the word “complet”, not read from scans.

The literal modern formulation “A excellent geometrically unibranch” does not imply reducedness: A=B=Q[ε]/(ε²), identity map, is flat local Noetherian and excellent; its closed fiberQ is geometrically integral, and A_red=Q makes it geometrically unibranch under Stacks15.108.1. Yet B is not a domain. This refutes only the unqualified reading. It does not settle the intended normal/reduced-base question in the deleted EGA draft; Murayama2022 Cor4.1 controls geometric punctual integrality of fibers, not by itself domainhood of all of B.

For a DVR A with uniformizerπ, ∩_(i≥1)(π^i)=0 by finite valuation of every nonzero element. B=A[1/π] is a flat finitely presented A-algebra, and (π^i)B=B for everyi, so extension fails to commute with this infinite intersection. No faithful-flatness is claimed.

For nilpotent lifting of schematic density, the published SGA3 IX4.2 proof identifies J^nO_X with (J^n/J^(n+1))⊗O_(X_0) by flatness and then uses local freeness of the coefficient module to preserve the jointly injective family of restrictions. Consequently that local-freeness hypothesis cannot simply be erased from the theorem comparison. It is present in both the opened SGA and EGA statements and absent from the supplied draft.

## Limits of the checks

No original scans were available. No Lean project or Hua certificate was compiled. No general odd-degree repair, complete axiom system for gauged monoids, unspecified universal construction, or solution of the intended EGA normal-base integrality question was developed. These are recorded as precise residuals, not silently certified by nearby results.
## 10. The K-class comparison, with explicit modern hypotheses

This is a current comparison, not a reconstruction of the unavailable cote 47 pages. Let X→S be proper and flat of finite presentation, let Y be an S-scheme, and let L be perfect on X×_S Y. Stacks 0FYP, Lemma 57.8.4(3), ensures that Φ_L(F)=Rp₂*(Lp₁*F⊗ᴸL) is perfect for perfect F. All three operations are exact on the relevant perfect derived categories. Therefore the induced map on their Grothendieck groups is, by the definitions of pullback, multiplication and proper pushforward, [F]↦p₂*([L]·p₁*[F]). This checks the operator pattern reported by the earlier note without claiming access to its cote 47 endpoint. For smooth proper schemes, Stacks 0G0F checks the convolution associativity by derived base change and projection formula. No equivalence of derived categories follows from equality of the displayed operator patterns.

## Addendum to §9: a counterexample to the omitted nilpotent-layer hypothesis

Let R=Q[x,ε]/(ε²,xε), S=Spec R, J=(ε), and S₀=Spec Q[x]. Set X=S and Z=D(x)⊂X. The structure map X→S is the identity and Z→S is an open immersion, so both are flat. The map Z₀→X₀ is schematically dominant because Q[x]→Q[x,x⁻¹] is injective. However, R→R[x⁻¹] kills ε since xε=0. The element ε is nonzero: the map R→Q[ε]/ε² sending x to 0 retains it. Thus Z→X is not schematically dominant. The ideal J is square-zero and J/J²≅Q[x]/(x), which is not locally free at x=0. The saved Groebner reductions independently check the nonzero/zero relations. This meets every hypothesis stated in the draft’s first assertion and refutes it. It does not meet universal density over S₀: base change to x=0 makes Z₀ empty. Accordingly it does not refute the separate relative-universal version.

