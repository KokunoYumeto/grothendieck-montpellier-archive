# All-dimensional component comparison through PD

Independent audit by /root/lie_theory, 19 November 2026. This is a comparison-map audit, not a claim that smooth and PL pseudoisotopy components agree in low dimensions.

## Original source opened

Burghelea–Lashof, The homotopy type of the space of diffeomorphisms I, Transactions AMS 196 (1974), 1–36. Complete author-uploaded article text opened at https://www.researchgate.net/publication/259582790_The_homotopy_type_of_the_space_of_diffeomorphisms_I (web ref turn569067271view0). Printed pp1–2 define the relative, parameter-preserving PL and PD complexes and assert that the triangulation-induced PL-to-PD map is a homotopy equivalence. Theorem1.1(c), p8, gives the corresponding comparison and cites Whitehead triangulation in its proof. This comparison has no dimension exclusion. The separate smooth-to-PL pseudoisotopy component isomorphism in PartII is not used.

## Typed construction and proof

Let M be a compact smooth manifold and K the prescribed fixed boundary portion, using a rounded corner model and compatible smooth triangulation t:|M| to M. Let P_PL be the parameter-preserving PL homeomorphism complex relative t^{-1}(K), and let P_PD be the corresponding piecewise differentiable homeomorphism complex from |M| to M relative t. Its comparison j:P_PL to P_PD sends p to t composed with p. The map i from the smooth homeomorphism complex to P_PD sends h to h composed with t. Define on components c=(pi0 j)^{-1} composed with pi0 i.

Although P_PD need not be a group, c is a group homomorphism. If h_i composed with t is PD-isotopic to t composed with p_i for i=1,2, then h1 h2 t is PD-isotopic first to h1 t p2 and then to t p1 p2. The first path uses the smooth left action; the second uses the PL right action. Thus c([h1 h2])=[p1 p2]. This also establishes independence of chosen representatives, using injectivity of pi0 j.

Forgetting the piecewise differentiable structure converts each such path to a topological isotopy. Consequently the triangle from pi0 Diff through pi0 PL to pi0 TOP commutes with the ordinary forgetful map. Any subgroup of smooth components whose image in TOP is injective therefore maps injectively into PL. This conclusion needs no smooth-to-PL injectivity theorem.

The original source restricts its complexes to homeomorphisms homotopic to the identity as maps of the boundary pair, fixed on K. A pseudoisotopy H of B times I satisfies that convention. First deform its interval coordinate linearly to t, leaving the B-coordinate pr_B H(x,t) unchanged. Then use the maps (pr_B H(x,s t),t) as s runs from1 to0. All maps preserve the two boundary faces, fix the bottom, and fix the vertical boundary if H does. Thus the convention causes no restriction on the pseudoisotopy classes in question.

Outcome: PASS for existence, multiplicativity and TOP compatibility of this component triangle in every dimension where the stated smooth and PL objects are defined. No low-dimensional smoothing equivalence is inferred.
