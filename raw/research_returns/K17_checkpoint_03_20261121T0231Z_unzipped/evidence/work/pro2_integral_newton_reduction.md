# K17-2-NEWTON-BASIS: an exact all-weight reduction

Researcher: /root/vandiver_k, GPT-6 Astra Pro; effort not exposed. Date: 2026-11-21 UTC.

## Scope

The following is a proved conditional reduction. It shows that no separate all-weight Hall-stability calculation is needed once the primitive Newton lower bound is attained in every odd weight. The checked finite calculation establishes no such infinite assertion. The subsequent independently audited parity induction in work/pro2_integral_allweights_candidate.md supplies the lifting hypothesis by a separate all-weight argument.

Use the already checked presentation P=C_2*Z_2, its cyclotomic kernel H, and the faithful rational tripod realization with the canonical normal form

    h=exp(a), gamma=exp(-a/2)u, u=5, a=sum_(m>=3 odd) s_m.

Write M=H_ab=Lambda=Z_2[[T]], with gamma=1+T and the class of h identified with 1. This is an isomorphism of compact Z_2-modules. Put

    m_i=2i+3, r_i=5^(m_i)-1,
    f_i(T)=product_(0<=j<i)(T-r_j), f_0=1,
    delta_i=f_i(r_i).

Then v_2(delta_i)=3i+v_2(i!). The linear weight-m coordinate of an element with abelian class F(T) is F(5^m-1), in the stated normalized rational coordinates.

## Proposition: primitive odd lifting suffices

Assume that, for every i>=0, there is g_i in H whose rational weight is at least m_i, and whose abelian class is f_i(T)b_i(T), where b_i belongs to Lambda^times. Then:

1. The g_i, viewed as a sequence converging to 1, form a compact free pro-2 basis of H.
2. Their weight-m_i leading classes sigma_i freely generate the entire integral weight-graded Lie algebra of H over Z_2.
3. Via the checked outer-filtration saturation lemma, this is the actual integral tripod graded Lie algebra.

Equivalently, it suffices that the actual primitive odd image ideal in every weight m_i attain the Newton lower bound v_2(delta_i), with no additional factor of 2.

### Proof of the equivalence of lifting formulations

An element of actual weight at least m_i has zero linear coordinate in every earlier odd weight. Successive division by the monic factors T-r_j shows that its abelian class is divisible by f_i. If its m_i linear coordinate has valuation exactly v_2(delta_i), write that class f_i b_i. Evaluation at r_i gives delta_i b_i(r_i), so b_i(r_i) is a unit. Since r_i lies in 4Z_2, b_i(r_i) modulo 2 is b_i(0) modulo 2. Thus b_i is a Lambda unit. The converse is immediate.

### Proof that the abelian classes form a compact basis

Each r_j is in 4Z_2, hence f_i belongs to (2,T)^i and f_i(T) modulo 2 equals T^i. For arbitrary coefficients a_i in Z_2, the sum

    sum_(i>=0) a_i f_i(T)b_i(T)

converges in Lambda. Indeed, the coefficient of T^k in f_i is divisible by 2^(2(i-k)) when i>k; multiplying by an integral b_i retains the needed convergence for every fixed coefficient. This defines a continuous map from the product of countably many Z_2 to Lambda.

Modulo 2 this map is the triangular formal-series map with columns T^i b_i(T), each having unit leading coefficient. It is an isomorphism over F_2: each successive coefficient determines the next a_i. Lift modulo 2, subtract, divide by 2, and repeat to prove surjectivity over Z_2. The resulting successive approximations converge in the product topology and in Lambda. If an element maps to zero, the modulo-2 isomorphism makes every coefficient even; dividing and repeating makes every coefficient zero. Thus the map is an isomorphism of compact Z_2-modules.

This argument does not confuse the product topology with the uniform 2-adic topology. The successive 2-adic corrections converge in both the product and the coefficientwise topology, and continuity of the displayed map is supplied by the increasing (2,T)-adic order of its columns.

### Proof of the compact free basis assertion

The elements g_i converge to 1 in H. Their actual weights tend to infinity, so their faithful rational images converge to 1 in every fixed weight truncation. H is compact, and its continuous faithful map into the Hausdorff inverse limit of those truncations is a homeomorphism onto its image. Hence this convergence holds in H itself.

Take the free pro-2 group on the pointed compact sequence {g_i} union {1}, with the sequence tending to its basepoint. It can be realized as the inverse limit of the finite-rank free pro-2 groups on g_0,...,g_n, with the next generator killed by each transition map: any map of the convergent sequence into a finite group kills its tail, which verifies the universal property on finite quotients and hence on pro-2 targets. This also supplies Magnus injectivity by projection to finite-rank groups. Its universal property gives a map to H, and its abelianization is the compact free Z_2-module on that sequence, namely the product used above. The map is therefore an isomorphism on abelianizations. It is Frattini-surjective and consequently surjective. Since H is free pro-2, projectivity provides a section. The section has closed Frattini-surjective image in the free source, so that image is the whole source. The map is an isomorphism. This is the same projectivity/Frattini argument used in the checked odd-prime compact basis construction; no infinite Hopficity is assumed.

### Proof of integral Hall generation

Give the abstract Magnus variable X_i=g_i-1 weight m_i. In the completed integral associative Magnus algebra, a nonidentity group element has a first nonzero weighted term. That term is primitive for the associated graded tensor coproduct, because the full element is grouplike. The primitive elements in this tensor algebra over Z_2 are exactly the free Z_2 Lie algebra on the X_i. One may see the integral assertion from the triangular Hall--Lyndon basis: its leading associative coefficients are units, so the integral Lie module is saturated in the rational primitive space. Only finitely many variables and words occur in each fixed arithmetic weight.

Under the actual rational realization, the first term of X_i is sigma_i. Its indecomposable s_(m_i) coordinate is the nonzero scalar delta_i b_i(r_i). Every remaining term in that weight is a bracket in strictly lower odd weights. Thus the homogeneous map from the rational free Lie algebra on the X_i to the rational free Lie algebra on the s_m, sending X_i to sigma_i, is triangular with nonzero diagonal and is an isomorphism. In particular it cannot annihilate the first nonzero integral Magnus term.

It follows that the actual rational weight of every element is exactly its abstract weighted Magnus degree. Its leading class is an integral Lie polynomial in the sigma_i. Conversely every Hall bracket in the sigma_i is realized by the corresponding group commutator. Therefore the full graded lattice is the free Z_2 Lie algebra on the sigma_i. The exact integral/rational outer-filtration comparison supplies the last assertion. QED.

## What this does and does not resolve

The scalar Newton calculation is necessary because it describes the simultaneous kernels of the preceding linear moments. The proposition shows that attaining it in every odd weight is also sufficient for all-weight integral freeness. It removes a second independent Hall-stability gate once these lifts exist.

This reduction itself does not prove the lifting hypothesis. A raw iterated Newton word can have lower even or decomposable terms. To move it into the required weight one must remove those terms by actual integral group commutators. The finite collection algorithm does that through weight 18; the later parity induction proves the required corrections in all weights. Treating the scalar abelian calculation alone as a proof of those nonabelian corrections would be circular.

The proposition also does not say that a finite set of attained odd minima automatically certifies every intervening even lattice: elements corresponding to later Newton directions might project to lower commutator weights. The complete finite closure certificate remains the appropriate proof for the finite-range statement.

## A symmetry route that needs care

Complex conjugation sends h to h inverse, but it does not send every gamma conjugate of h to its inverse. In fact c gamma c=h gamma. In the rational normal form, the torus action tau differs from actual gamma conjugation by Ad(exp(a/2)). That half-power need not preserve the integral compact group. Therefore replacing actual D by the diagonal tau, or imposing exact c-inversion on every desired Newton lift, is an additional requirement and cannot be used without proof. The checked algorithm keeps actual D and all Baker--Campbell--Hausdorff denominators.
