# THETA3-A6: direct balanced tensors of arbitrary even length

Author/checker: GPT-6 Astra Pro, agent `/root/theta_032`; the inherited reasoning-effort label is not separately exposed. Date: 21 November 2026. This is a research contribution for the parent, not a formal verification claim.

## Status and exact scope

The analytic construction extends from two factors on a ball surface to **n factors on an n-dimensional ball**, for every n >= 2. More significantly, the exact arithmetic source identification is available in arbitrary Hermitian rank m = n+1 from Liu, Theorems 4.15 and 4.18. It is not necessary to infer that identification from the weaker assertion that the Albanese is CM. The reflex-type argument in van Hoften--Sempliner, Corollary 3.1.13 and Proposition 4.1.8, is independent of the dimension of the ball.

Subject to those cited theorems, the resulting construction proves the algebraicity of a balanced 2n-factor CM embedding line directly, using a projective n-fold and explicit divisor contractions. It does not require reducing the tensor to four-factor relations. It does not, by itself, identify the resulting theta input with the iterated Bessel family in Alpoge's archive, bound its normalized common scalar, or supply an integral theta frame.

The detailed proof below is new synthesis and elementary extension of the attached arguments. The arithmetic oscillator classification, its Galois realization, the CM classification, and the special-theta theorem are cited inputs, not re-proved here.

## A6.1. Exact all-rank CM source dictionary

Let E be a Galois CM field, F=E^+, [F:Q]>=2, c its central complex conjugation, and v:Gal(E/Q)->{+1,-1} an odd sign function with v(1)=1. Write Phi(v)={g:v(g)=1}, and d(tau)=v(tau^{-1}). Let V have Hermitian rank m>=3, signature (m-1,1) at the distinguished real place and (m,0) at every other real place. These are precisely the coherent nearby spaces to the totally definite incoherent data in Liu's Section 4.2: replace the active signature by (m,0), keeping finite data, to obtain the incoherent space; its active nearby coherent space is V. Thus Liu's arbitrary-rank theorem applies to this compact Shimura tower.

Choose a unitary conjugate-symplectic Hecke character mu of weight one with

    mu|A_F^x = epsilon_{E/F},        Phi_mu = Phi(v)^{-1}.

Existence is van Hoften--Sempliner Lemma 3.1.5, pp.9--10. A skew-Hermitian line W=Ee with e^c=-e is admissible exactly when Im(tau(e))<0 for tau in Phi_mu; see Liu Definition 4.12, p.47. This is the same sign prescription as 032 equation (4.2) and Lemma 4.1: e=delta*h_W and sign(h_W)=-d(tau) sign(Im(tau(delta))). In particular W has active signature (0,1).

Liu Definition 4.3, p.41, sets mu_alg=mu |.|_E^{-1/2}. Its coefficient field M_mu contains the reflex field M'_mu of (E,Phi_mu), with reflex CM type Psi_mu. Definition 4.5, p.42, specifies the CM abelian variety A_mu, including its distinguished M_mu-inclusion eigenline and the Galois character mu_alg; Proposition 4.6, pp.42--43, supplies the CM datum. Theorem 4.15, pp.50--51, identifies the Galois character of every admissible oscillator component with this exact mu_alg in every rank m>=3. It is not merely a comparison of dimensions or infinity types.

Theorem 4.18, pp.52--54, identifies

    Hom_E(A_infty,A_mu)_Q tensor_{M_mu} C
        = direct_sum_{epsilon,chi} omega(mu,epsilon,chi),

where epsilon is mu-admissible. In the proof, the map is pullback of a basis of the distinguished M_mu-inclusion line in H^1(A_mu,C). Its finite-level assertion identifies K-invariants with Hom_E(A_K,A_mu)_Q. Here chi is the finite central automorphic character in Definition 4.11, not the splitting character mu and not the source U(1) character. Corollary 4.20, pp.54--55, is the weaker whole-Albanese isogeny statement; the precise componentwise Theorem 4.18 is the input used here.

Now let (E_0,Phi_0) be the primitive CM type inducing (E,Phi(v)). Then B(v) is isogenous to B_0^[E:E_0]. Since E is Galois and Phi_mu=Phi(v)^{-1}, the reflex pair (M'_mu,Psi_mu) is exactly (E_0,Phi_0). Consequently A_mu,C is isogenous to B_0^[M_mu:E_0]. This is the argument in van Hoften--Sempliner Corollary 3.1.13, p.12, with the selected-eigenline refinement in Proposition 4.1.8, pp.15--16. It yields, for that particular oscillator component,

    omega(mu,epsilon,chi) subset
    span_C { h(U(v)_1) : h:U(v)->H^1(X,Q) a rational Hodge map },

after a sufficiently deep common principal cover of a connected component. The proof with the primitive CM factor, the inclusion eigenline and Hom tensor products does not depend on m. This is the required exact source identification; it is stronger than saying that the Albanese happens to be CM.

### The local vector and scalar conventions

The first projected Taylor tensor in 032 is the ordinary linear theta gradient. In a real symplectic chart at a base point it is a nonzero scalar times a linear position function multiplied by the positive Gaussian, contracted with the cotangent basis. Under the Bargmann transform, linear position times the vacuum maps to a nonzero scalar times the corresponding linear Fock coordinate. The cochain is therefore the standard contraction

    psi_{1,0} = sum_{alpha=1}^{m-1} z''_alpha tensor xi'_{alpha,m}.

This is exactly the q=1 case of the published BMM Lemma 5.5, pp.43--44; their equation (5.11), p.54, defines its Schrodinger realization by the inverse Bargmann transform. The comparison can be made on a single base-point fibre and then transported by SU(V), since both tensors have the same covariance. The constant is nonzero; its numerical value depends on the chosen Gaussian/Bargmann and constant-line normalizations. Only membership in a complex span and nonvanishing are used, so no algebraicity of this scalar is required.

BMM Lemma 5.18, p.49, uniquely fixes the twist det^{(a-b)/2} on U(V) needed for the special cochain. Here a=0,b=1, so the twist is det^{-1/2} in their Fock convention. Do not replace this by the reciprocal half-determinant appearing in a covariant Taylor-value convention: the value representation and the oscillator representation are dual. On SU(V) the determinant twists are trivial. The circle lift and double lift agree there because their ratio is a continuous character of a connected semisimple real group, as in 032 Lemma 4.4, pp.20--21. At compact places the Gaussian is the trivial representation after the corresponding splitting, exactly the possibilities in Liu Lemma D.2(1), pp.127--128. At the active place the holomorphic component is omega_{m-1,1}^{-1,-,0} by Liu Lemma D.2(2).

The global source splitting nu_m satisfies nu_m|A_F^x=epsilon_{E/F}^m. Changing nu_m twists the source torus character; it does not change the indicated mu-component after that source twist. The source character remains a separate symbol, say pi. With the van Hoften--Sempliner integral convention one integrates theta(g,t) pi(t), without inserting an undocumented conjugation. Changing to a convention theta(g,t) eta(t)^{-1} means eta=pi^{-1}. No equality pi=mu or pi=chi is asserted.

At fixed finite level and prescribed archimedean type the compact torus quotient has only finitely many character components. Thus a raw first theta gradient is a finite sum of these integrated degree-one lifts. All its nonzero summands are in the above exact rational-Hodge span. The argument of van Hoften--Sempliner Proposition 4.1.8 applies in every m>=3: BMM Section 9.1 and Theorem 9.1, pp.72--75, require 3(a+b)+|a-b|<2m, which for a+b=1 is 4<2m. Their theorem is applied only in degree one, never to the top-degree wedge. The proof uses the polynomial-Fock generator and its source enveloping-algebra action; it is not a claim that every high-degree cohomology class is a special lift.

For a finite list of SU theta forms, construct these full U(V) lifts with the stated splittings and restrict them to a connected component. Their finite inputs have a common open stabilizer; a deep principal SU subgroup lies in it. The pullbacks of the rational Hodge maps therefore live on one common smooth projective cover. This avoids assuming that an arbitrary SU form has already been adelically extended.

### Split-local confirmation, not a substitute for the Galois theorem

Liu Lemma D.1, proof p.126, says at a split place E_v=F_v x F_v, mu=nu box nu^{-1},

    omega(mu,epsilon,chi)
       = normalized_Ind_{GL_{m-1} x GL_1}^{GL_m}
           ((nu o det) box chi nu^{1-m}).

After dividing all Satake eigenvalues by nu(varpi), the projective tuple is

    {q^{(m-2)/2}, q^{(m-4)/2}, ..., q^{-(m-2)/2},
       chi(varpi) nu(varpi)^{-m}}.

The exponent is -m, agreeing with -3 in 032. An inverse geometric Hecke convention inverts the tuple. This calculation verifies the rank parameter; the exact CM type is supplied by Theorems 4.15 and 4.18, not by the split tuple alone.

## A6.2. Analytic n-fold alternating product

Fix n>=2 and put m=n+1. Let v_1,...,v_{2n} be odd sign functions with v_i(1)=1 and

    sum_{i=1}^n v_i = sum_{i=n+1}^{2n} v_i.                    (A6.1)

Use a single rank-m Hermitian V of the above one-active-ball signatures. Choose skew-Hermitian multiplicity lines of the first n prescribed signs, or equivalent Hermitian lines P_i after fixing delta^c=-delta; set P=perp_{i=1}^n P_i. At the active place P is definite, of the sign giving

    F_P = (L tensor P) direct_sum (Q^* tensor P^*),
    Q=V_mu/L, rank Q=n.

As proved in A4, for multiplicity rank k,

    det F_P = L^{2k} (det V_mu)^{-k} (det P)^{2-m}

times compact constant factors. With k=n, the half-determinant is L^n times a constant line, trivial as an SU(V) representation after the displayed L factor is retained. Define

    Alt_n : Sym^n(Q^* tensor P^*) -> wedge^n Q^* tensor wedge^n P^*

by sending a symmetric product of decomposable tensors to the product of their two exterior wedges. Swapping two factors changes both wedge signs, so the map is well-defined. After the fixed constant-line trivializations, its target with the half-determinant is

    L^n tensor wedge^n Q^* = Omega_D^n.

Apply this projection to the degree-n completed Taylor tensor. For a decomposable finite input the completed theta series is a product of the n line theta series. In the divided-power Taylor convention, its degree-n coefficient is a sum indexed by k_1+...+k_n=n. If some k_i>=2, that summand contains at least two factors in the same multiplicity line and is annihilated by wedge^n P^*. The only surviving multi-index is (1,...,1). Hence its projected tensor is exactly the wedge of the n projected first tensors, with coefficient one. This also proves the finite-sum formula for arbitrary finite inputs, since finite-adelic Schwartz spaces on a direct sum are algebraic tensor products: a compactly supported locally constant function has a finite decomposition into rectangle indicators after choosing a common sufficiently fine open lattice.

For each prescribed first type, Gaussian isolation as in 032 Proposition 4.5, pp.21--22, spans every cotangent fibre in dimension m. Greedily choose one actual input from each of the n prescribed families so that their values form a basis at one point. This is possible because each individual family spans the whole n-dimensional cotangent fibre. The resulting holomorphic top form xi is nonzero. Choose a common principal level for the finitely many actual inputs. Compactness follows from the definite real place, and projectivity from the ball Shimura construction.

The positive top-form norm is

    i^{n^2} integral_X xi wedge conjugate(xi) > 0.             (A6.2)

The factor i^{n^2} is essential when n is odd. In local coordinates it converts dz_1...dz_n dbar(z_1)...dbar(z_n) into 2^n times the positive real volume form.

## A6.3. Balanced signs and a nearby rational orthogonal flag

Keep V, the total rational multiplicity space P, its rational symplectic realization, the finite total input, and the total SU level fixed. At each compact real place, equation (A6.1) says that the first n line signs and the last n line signs have the same number of plus and minus entries. Relabel the initial real orthogonal basis at that place so that its lines carry the desired last-n labels. This leaves the aggregate positive and negative multiplicity subspaces unchanged. At the active place all lines have the same sign, so any orthogonal decomposition gives the same total active positive Lagrangian.

The compact real orthogonal flags just chosen can be approximated simultaneously by rational orthogonal flags. Here is an elementary construction. Approximate their ordered bases by vectors in P(E), using weak approximation in E at its archimedean places. Apply Hermitian Gram--Schmidt. All denominators are the nonzero norms of the chosen orthogonal vectors; the conditions that these denominators remain nonzero and keep their prescribed signs are open. The resulting rational orthogonal vectors are therefore arbitrarily close and have the required signs at every real place. They give P=P_{n+1} perp ... perp P_{2n} over E.

On a compact parameter neighborhood, positive Gaussian majorants with polynomial derivatives give C-infinity continuity of the total projected theta tensor, exactly the domination used in 032 Proposition 4.6(iii), pp.22--24. The constant-line trivializations and multiplicity orientations can be chosen continuously near the reference point, matching the original at that point. Therefore

    i^{n^2} integral_X xi wedge conjugate(Xi_P(phi;t))

remains nonzero for a sufficiently close rational endpoint. Intermediate parameters need only give smooth forms. At a rational endpoint, finite tensor decomposition gives a finite sum of wedges of holomorphic first theta forms of the last n prescribed types. The endpoint eta is therefore holomorphic and closed. Selecting one term with nonzero mixed period, and taking a common principal cover for all selected first-tensor inputs, gives

    integral_X theta_1 wedge ... wedge theta_n
             wedge conjugate(theta_{n+1}) wedge ... wedge conjugate(theta_{2n})
       != 0.                                                (A6.3)

Covering multiplies this integral by its positive degree. It cannot destroy nonvanishing.

One may also make the full unitary splitting characters agree on the two decompositions. Choose mu_1,...,mu_{2n-1} of the prescribed types and set

    mu_{2n} = (product_{i<=n} mu_i)/(product_{n<i<2n} mu_i).

The restriction to A_F^x is epsilon^(n-(n-1))=epsilon, and the infinity exponents have weight one and the required CM type by (A6.1). Thus product_{i<=n} mu_i=product_{i>n} mu_i globally, not just at infinity. The common source splitting nu_m is retained. This is compatible with the tensor rule, although the SU analytic argument already has determinant twists removed.

## A6.4. From the period to a direct codimension-n cycle

By A6.1 each of the finitely many holomorphic theta classes in (A6.3) lies in the complex span of h(U(v_i)_1) for rational Hodge maps h. After conjugating the last n factors, it lies in the analogous span of h(U(v_i)_c). Expanding the finite spans and using nonvanishing selects rational Hodge maps

    h_i: U(v_i) -> H^1(X,Q)

and algebraic-Betti nonzero eigenvectors alpha_i in U(v_i)_{lambda_i}, with lambda=(1^n,c^n), for which the integrated product is nonzero. The arbitrary analytic scalars are coefficients in the finite expansion; the chosen alpha_i themselves can be chosen in Qbar-Betti eigenlines.

Realize h_i by morphisms f_i:X->B(v_i) after multiplying by positive integers, using the Albanese and rational Riemann theorem as in 032 Lemma 2.2, p.5. Put A=product_{i=1}^{2n} B(v_i), g=dim A, f=(f_i), and Z=cl(f_*[X]) in H^{2g-2n}(A,Q). If t_alpha is the product of the alpha_i in the 2n distinct H^1 slots, the projection formula gives

    integral_A Z cup t_alpha = k in Qbar^x.                  (A6.4)

For each i take a copied factor B(v_i)' and a nonzero algebraic-Betti beta_i in its conjugate embedding line c lambda_i. The pure Kunneth class D_i=alpha_i tensor beta_i in H^2(B_i x B_i',Qbar) is algebraic: every scalar conjugate has opposite Hodge types in its two factors, hence type (1,1); scalar descent and Lefschetz (1,1) give its exact class as a Qbar linear combination of divisor classes. No projection of an arbitrary divisor is being assumed.

Let A'=product B_i', let p,p' be the projections from A x A', and q_i select B_i x B_i'. Then

    K=product_i q_i^*D_i = (-1)^n t_alpha tensor t_beta,

because the number of odd-degree transpositions is (2n)(2n-1)/2=n(2n-1), of parity n. Consequently

    p'_*(p^*Z cup K) = (-1)^n k t_beta.                     (A6.5)

Its codimension is (g-n)+2n-g=n. Every operation on the left preserves algebraicity, and k is nonzero algebraic, so the beta line is algebraic. Scalar complex conjugation preserves the Qbar span of rational cycle classes and changes the labels back from (c^n,1^n) to (1^n,c^n). Identifying copied factors gives the original balanced line. This is a complete direct cycle extraction, not a functional-only statement.

## A6.5. Explicit family in every degree and transfer to Weil pieces

For every n>=2 choose a Galois CM field E with at least n+1 real pairs of embeddings; a sufficiently large cyclotomic field suffices. Choose n compact-place representatives tau_1,...,tau_n, in addition to the distinguished representative. Let v_0 be +1 on all chosen representatives and extend oddly. For i=1,...,n let v_i differ from v_0 only at tau_i. Let v_{n+1} differ from v_0 at all tau_1,...,tau_n, and let v_{n+2}=...=v_{2n}=v_0. Then

    sum_{i=1}^n v_i = v_{n+1}+(n-1)v_0.

No first-list type equals any second-list type for n>=2. The selected balanced 2n-factor embedding line is therefore not in the subalgebra generated by divisor classes. Indeed a divisor product contributing to this pure one-H^1-per-factor line would determine a perfect matching of the factors. At the distinguished embedding, every allowed pair must join one first-list factor to one second-list factor. For such a pair to be of type (1,1) in every scalar conjugate requires equality of the two corresponding v's, and no such equality holds. Thus the projection of every divisor product to this line is zero. A6 nevertheless constructs a codimension-n cycle on the product with nonzero component on, and indeed spanning, that line. This includes n>=4 and is not limited to four or six H^1 factors.

For a CM abelian variety of Weil type of dimension 2n with multiplication by an imaginary quadratic K, each of its two Weil lines over Qbar is a wedge of 2n CM embedding lines, exactly n holomorphic and n antiholomorphic at every scalar conjugate. Let s_i(g) be their complete type functions. Reorder them by Hodge type at the distinguished embedding, and put v_i=s_i for the first n and v_i=-s_i for the last n. Then v_i(1)=1 and (A6.1) holds. Each original eigenline has exactly the complete type of U(v_i)_{lambda_i}. The zero-extended embedding-line maps are Qbar linear combinations of rational Hodge maps by scalar descent (032 Lemma 2.4, p.8), hence of pullbacks of abelian morphisms by Lemma 2.2. Applying their tensor product and the cup-product map to the algebraic balanced tensor is an algebraic operation: expand the maps and pull back along the associated product morphisms from the target abelian variety. This proves algebraicity of the prescribed Weil line. No assumed algebraic Kunneth projector is needed for this transfer.

An explicit all-n CM Weil-type input can be obtained by taking a totally real Galois field F of degree 2n, putting E=F(i), and choosing a CM type with n embeddings above each embedding of Q(i). The resulting CM abelian variety has dimension 2n and K-signature (n,n); its two Weil lines are covered by the preceding argument. For example, choose a prime ell congruent to 1 modulo 4n, take the unique degree-2n real subfield of Q(zeta_ell), and then adjoin i. This specifies the field and type family; it is not a claim that all these varieties are simple or that their Weil classes are always outside the divisor algebra.

More generally the same embedding-line argument applies to every rational Hodge class of a CM abelian variety: decompose its exterior monomials into CM embedding lines, use rationality to see that every occurring monomial is balanced under all scalar conjugates, and apply the direct 2n-factor result. The new route bypasses the four-factor combinatorial reduction, while retaining Liu's deep all-rank theorem as a cited input.

## Remaining hypotheses and practical limits

The mathematical hypotheses are explicit: E must be enlarged to a Galois CM field with a definite real place available; m=n+1>=3; the exact admissible mu/epsilon conventions must be used; the cited Liu and BMM theorems supply the arithmetic source identification; all selected inputs are placed on a common principal cover. None is an unproved Hodge conjecture or an unproved general projector statement. The numeric coefficients in the first-gradient/Bargmann comparison need only be nonzero for this existence argument. They would need to be fixed for a quantitative Rallis or Bessel equality.

There remain different, genuinely open tasks for the intended Alpoge bridge: identifying the complete iterated tuple and its LawsX/Link conditions, proving the required normalizer comparison for these cohomological vectors, and supplying integral theta frames for the p-adic derivative estimate. Increasing the ball rank does not satisfy every-place signature conditions in the recovered tower theorem and does not turn an independent n-fold product into an iteration of theta operators.
