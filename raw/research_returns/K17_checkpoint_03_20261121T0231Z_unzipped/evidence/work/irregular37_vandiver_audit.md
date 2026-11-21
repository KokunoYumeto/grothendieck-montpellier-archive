# Independent audit of the prime-37 pole candidate

Reviewer: GPT-6 Astra Pro, agent /root/vandiver_k. Date: 2026-11-21 UTC. Effort setting: not exposed. Run: K17.

Reviewed document: work/irregular37_pole_candidate.md, initial complete version dated 01:01 UTC, read in full. The author was asked to make the linearization filtration explicit; that clarification is proved below. This report does not edit the candidate or root deliverables.

## Verdict and exact scope

**The complete candidate passes this independent mathematical review, using its stated arithmetic and rational-realization background theorems.** I found no failed implication in the module computation, compact free-basis construction, one-relator comparison, meromorphic coefficient equation, or ordered-pair localization argument. In particular, the possible cancellation between different noncommutative words is addressed by the proof, rather than assumed away.

The two points requiring the most care are valid: the quotient-ring calculation takes place in the bounded-denominator ring Z_37[[T_1,...,T_d]][1/37], and the arithmetic p-central relation can be linearized to an annihilator with initial term 37-3T. Detailed independent derivations are given below. The conclusion is the displayed kernel equality at p=37 as a deduction from the cited inputs. This is not a formal proof certificate, a new verification of Brown's theorem or Ferrero--Washington, a novelty claim, or a result for every irregular prime. It has no implication of integral free generation by odd-weight elements.

## 1. Arithmetic inputs and their scope

Let F=Q(mu_37), K=Q(mu_(37^infinity)), Omega be the maximal pro-37 extension of F unramified outside37, P=Gal(Omega/F), and H=Gal(Omega/K).

I reread Iwasawa, Riemann--Hurwitz formula and p-adic Galois representations for number fields, Tohoku Math. J.33 (1981), Theorem2, printed pp273--274, including its complete proof. It applies to a cyclotomic Z_p-field containing the p-power roots of unity, with S finite and containing all p-places. It states that the relevant maximal p-ramified Galois group is free pro-p exactly when mu=0. The preceding paragraph explicitly recalls Ferrero--Washington in the abelian case. Here K/Q is abelian and has one prime over37. A finite Galois p-extension over K descends, with its group and ramification conditions, to a sufficiently high cyclotomic layer; its normal closure over F is still a p-extension. Thus the maximal extension in that theorem is the same Omega used here. This gives freeness of this exact H, not of P.

Primary original PDF:
https://www.jstage.jst.go.jp/article/tmj1949/33/2/33_2_263/_pdf/-char/en

I reread the following relevant statements and proofs in Sharifi's primary-author Iwasawa notes: Theorem3.3.3 (finite generation and Lambda rank), Theorem3.3.4 (cyclotomic weak Leopoldt), Corollary3.3.14 and Proposition3.4.7 (the Kummer exact sequence and plus component), and Corollary3.4.8 (that component is Lambda-torsion). They give, for M=H_ab,

    rank_Lambda M=18,     M+ is Lambda-torsion.

Freeness of H gives Z_37-torsion-freeness of M. The two meanings of torsion are kept distinct.

https://www.math.ucla.edu/~sharifi/notes/iwasawa-ch03.html

McCallum--Sharifi, A cup product in the Galois cohomology of number fields, author version of 5 December2003, section8, printed pp22--23, gives the minimal generators and the explicit degree-two relation at37. I reread those pages, Theorem8.2 and its proof, Corollary8.3 and its proof, and section9 pp24--25. The required coefficients are 37 on y, -3 on [gamma,y], and -11 on [x_3,x_29]. The generator set has gamma, eighteen odd character directions, and the single even direction32. The hypothesis Vandiver37 and the fact that32 is the unique irregular index were independently certified earlier in this run. The MCS numerical cup-product theorem is used as a cited theorem; their larger class-group computation was not reproduced here.

https://www.math.ucla.edu/~sharifi/publ/pairing.pdf

Sharifi, Galois groups and fundamental groups, section2 p3 and Lemma2.1 pp3--4, gives commuting Delta/Gamma lifts and character-normalized lifts. I reread these passages and the lemma's proof. The projectors need only be applied to abelianizations for most of the candidate; exact nonlinear eigenlifts are available as well. Choosing chi(gamma)=1+37 is compatible with the construction by taking a unit Z_37-power of the Gamma lift.

The actual-image and rational freeness inputs are the same Hain--Matsumoto/Brown statements already checked in work/pro2_vandiver_audit.md: Hain--Matsumoto Proposition8.3/Theorem8.4, the cyclotomic-kernel density argument, and the filtered-to-weight-completed free-Lie passage. Their scope includes p=37. This report reuses that checked background and does not claim to reprove those theorems.

## 2. The exact Lambda-module shape

The chosen Gamma lift splits P->Gamma. Consequently its abelianization gives

    P_ab = M_Gamma direct sum Z_37 gamma.

This can be proved directly: the closed commutator subgroup of H semidirect Gamma is generated by [H,H] and gamma h gamma^(-1)h^(-1), and Gamma is abelian. It agrees with the continuous homology exact sequence, whose H_2(Gamma,Z_37) term vanishes. Because Delta commutes with gamma, this decomposition also respects the Delta characters.

Reduction modulo37 identifies M/(37,T)M with precisely the nineteen non-cyclotomic directions in P/Phi(P). Each odd Delta character occurs once; the only even character is32 and occurs once. Topological Nakayama applies because M is finitely generated over Lambda. It gives a surjection Lambda^18->M-. The rank of M- is18, since M+ has rank zero. The kernel has rank zero and is a submodule of a free module over the domain Lambda, so it is zero. Applying Delta idempotents gives one free rank-one Lambda summand in each odd character.

Similarly M+ is cyclic and nonzero. Its nonzeroness already follows from the one-dimensional even quotient modulo(37,T); one does not need an extra inference about a direct-limit class group at this point.

### 2.1 Why a degree-two p-central relation gives f(T)=37-3T modulo(37,T)^2

Let F_0 be the free pro-37 group on gamma and the nineteen non-cyclotomic generators. Its cyclotomic map sends gamma to a generator of Gamma and all other generators to1. Let H_0 be its kernel. The standard compact-orbit construction, or its abelian universal property, identifies

    H_0,ab = Lambda^19.

Write A=Lambda^19 and m=(37,T). Consider the quotient A semidirect Gamma. Give it the filtration

    Q_n = m^(n-1) A semidirect 37^(n-1) Gamma.

The image of Fil_n F_0 lies in Q_n. For the induction, raising an element of Q_n to its 37th power multiplies its A-coordinate by a sum of37 Gamma units, which belongs to m. Commuting it with an arbitrary element contributes either T times an element of m^(n-1)A or (gamma^b-1)A with b in37^(n-1)Z_37. The latter coefficient belongs to m^n. For instance, the binomial coefficient bound v_37(binomial(b,j))>=n-1-v_37(j), combined with j-v_37(j)>=1, proves this membership. The Gamma-coordinate also acquires the required factor37. This establishes the induction.

In particular, Fil_3 F_0 intersect H_0 maps into m^2 A. A relation with the MCS initial form has abelianized H_0-coordinate whose y-coefficient is

    37-3T modulo m^2.

All commutators between non-cyclotomic generators vanish in A. A gamma-only coefficient cannot survive because the relator has trivial cyclotomic image. Projecting from A to the exact even summand of M removes all odd linear terms. Thus this y-coefficient is an actual annihilator f(T) of a generator of M+, not merely a statement about its first finite quotient.

The generators can be replaced by lifts of their exact abelian Delta components without changing their classes in P/Phi(P). Such replacements alter a degree-two relation only in Fil_3: a 37th power of a Fil_2 correction lies in Fil_3, and a commutator with that correction does also. Unit rescaling of the one-dimensional character generators only rescales the displayed coefficients by nonzero constants. This justifies matching the exact module bases to MCS's normalized Frattini basis.

The coefficient of T in f is a unit and f(0) has valuation1. Weierstrass preparation therefore gives f=v(T)(T-beta), where v(T) is a unit, beta is in37Z_37, and v_37(beta)=1. Hence M+ is a quotient of Lambda/(f)=Z_37. A nonzero, Z_37-torsion-free cyclic quotient of Z_37 is Z_37 itself. Therefore

    M = (direct sum_(a odd mod36) Lambda e_a) direct sum Z_37 e_y,
    gamma(e_y)=alpha e_y,       alpha=1+beta.

No numerical lambda-invariant assumption is hidden in this derivation.

## 3. The compact free-basis lemma is valid

Let X be eighteen copies of Z_37 together with the isolated y. The inverse limit F_X of finite-rank free pro-37 groups on its finite partitions represents continuous maps from X to pro-37 groups. For a finite target quotient, the map from X factors through one finite partition; compatibility and uniqueness give the general pro-37 target. The canonical image of X topologically generates F_X.

Its abelianization represents the same functor on abelian pro-37 targets, so it is Z_37[[X]]=Lambda^18 direct sum Z_37. This proves the abelianization assertion without assuming that abelianization commutes with arbitrary inverse limits.

The orbit map x_(a,t)=gamma^t x_a gamma^(-t), together with y, induces f:F_X->H which is an isomorphism on abelianizations and hence on Frattini quotients. Its image is closed because F_X is compact. A proper closed subgroup of a pro-p group is contained in a proper open subgroup: separate an element outside it by a finite quotient; then place the resulting proper subgroup in a maximal subgroup of that finite p-group. Such a subgroup cannot surject on the Frattini quotient. Thus f is surjective.

Projectivity of the free pro-37 group H gives a continuous section s. Since f induces a Frattini isomorphism, s(H) surjects on F_X/Phi(F_X). It is again closed, and the same argument gives s(H)=F_X. Hence f is an isomorphism. No infinite-rank Hopfian claim is used.

The finite-partition integral Magnus embeddings are compatible and jointly injective. Give an x letter degree1 and y degree2. Their coefficients in a fixed pattern are bounded measures on the remaining x coordinates. A nontrivial element has a first nonzero finite weighted degree, and there are finitely many patterns and labels in that degree. The Amice transform identifies these measure modules with the corresponding integral power-series rings; its injectivity follows from density of the multivariate Mahler basis.

## 4. The actual one-relator presentation and cup coefficient

Let phi be conjugation by gamma on H and set E=phi(y)y^(-alpha). Its abelian class is zero, so E belongs to the closed commutator subgroup of H. The element phi(y), written in the compact free basis of section3, can be evaluated in the free pro-37 group on the finite set gamma,x_a,y by sending x_(a,t) to gamma^t x_a gamma^(-t). Let R denote gamma y gamma^(-1) times the inverse of that evaluated word.

This is a genuine one-relator presentation for P. To check it, take arbitrary elements gamma',x_a',y' of a pro-37 target satisfying R. The compact orbit map induces a homomorphism H->Q. It intertwines phi with conjugation by gamma' on every x_(a,t) automatically, and on y precisely by R. These elements generate H, so it intertwines on all of H. Continuity gives the same compatibility for all Gamma powers, and the map extends uniquely to H semidirect Gamma. This proves the presentation by its universal property.

In Fil_2/Fil_3 of the finite free group, the initial form of R is

    [gamma,y]+(1-alpha)y-E_2,

where E_2 is the ordinary quadratic Magnus term folded by augmentation of the orbit coordinates. Because E has zero ordinary linear term, no spurious [gamma,y] term arises from this folding. In particular, the x_a x_b coefficient is the constant Amice coefficient C_(a,b)(0,0), with only the harmless commutator sign convention to fix.

The degree-two image of the closed normal subgroup generated by R is its one-dimensional scalar span whenever this initial form is nonzero: conjugation is trivial in this graded quotient and pth powers of Fil_2 elements belong to Fil_3. MCS's nonzero initial relation lies in this image. Therefore the two initial forms are nonzero scalar multiples. The coefficient1 of [gamma,y] in R matches the unit -3 in MCS, so the coefficient corresponding to [x_3,x_29] is a unit because MCS's coefficient is -11. Thus C_(3,29)(0,0) is a37-adic unit.

This argument derives the whole one-relator presentation from the already established H-basis and actual Gamma action. It does not infer a nonlinear relation from a mere class-group order.

## 5. Rational realization and the coefficient equation

A rational Levi choice makes gamma's image the weight torus element u. To construct the needed conjugation, solve successively in each positive weight; u^w-1 is nonzero for w>0. The corrections converge in the weight completion. Delta commutes with gamma, and a unipotent element centralizing this torus element has zero image in its first nonzero weight, a contradiction. Hence Delta has no remaining unipotent component after that conjugation.

Every abelian target coordinate factors through M. It vanishes on y because y is even, and on every odd component with the wrong Delta character. On x_(a,t), the matching coordinate is a_m u^(mt). The constant a_m cannot be zero, since then the coordinate would vanish on the entire compact basis and thus on the dense image of H. Rescaling the rational free generator in each weight by a_m is valid in the weight completion. No uniform integral bound is needed for that operation.

In these coordinates, the target length-two coefficient B_(m,n) of y satisfies

    (u^(m+n)-alpha) B_(m,n)
       = C_(a,b)(u^m-1,u^n-1).

This follows by taking length two in phi(y)y^(-alpha). Its source ordinary linear term vanishes; at weighted degree2, only x,x terms contribute. Terms involving y in the closed commutator subgroup have weighted degree at least3. Therefore the right-hand side is exactly the integral two-variable Amice transform already defined, with no extra analytic regularity assumption.

The equation is valid even where the scalar on the left might vanish. Denominator clearing, rather than division at those grid points, is therefore the correct next operation.

## 6. Analytic identities and all ordered-word cancellations

Let a nontrivial kernel element have first weighted Magnus degree d. At that degree, each source word corresponds to a tiling of d ordered positions by singleton x letters and pairs representing y. The coefficient for a fixed tiling and singleton labels is an integral Amice series A_J in the unpaired variables only.

After substitution, terms of weighted source degree greater than d cannot contribute target length d; the lower source terms vanish identically. Each degree-d term contributes only the lowest possible target length of each letter. This gives the finite tiling identity in the candidate. It is valid coefficient by coefficient in every finite arithmetic weight quotient: continuous coefficient functions on the compact orbit spaces are bounded, and integration against bounded measures, locally constant approximation, and Fubini construct the multiplicative substitution. Equality on generators and continuity give equality with the actual representation. No free pro-p universal property is applied directly to the noncompact rational target.

Multiply by the product of all neighboring denominators D_j=(1+T_j)(1+T_(j+1))-alpha. The coefficient equation of section5 makes the cleared identity valid on every allowed integer grid point, including any point with a zero denominator. In each prescribed residue class, the points u^(a+36*37^n)-1 tend to an interior point of the open unit disc and are distinct. Successive one-variable analytic identities show that the cleared multivariable series is identically zero.

The resulting meromorphic identity is in the fraction field of

    R=Z_37[[T_1,...,T_d]][1/37].

This distinction is essential: in Q_37[[T_1,...,T_d]], a denominator with a nonzero constant would be invertible, and the pole argument would have no content. The ring R retains a uniform denominator bound and the needed divisors.

Choose a nonzero coefficient with the greatest number of y pairs and let J be its set of pair positions. Assign types3,29 to every selected pair and the actual singleton types to the remaining positions. The corresponding C factors are units. Put I_J=(D_j:j in J).

The pairs are disjoint. For each pair the change of coordinate

    S_(j+1)=T_(j+1)-[alpha/(1+T_j)-1]

is an automorphism of the (37,T)-adically complete integral power-series ring; the substituted constant lies in37Z_37. Each D_j is (1+T_j)S_(j+1). Thus the quotient by I_J is an integral power-series ring in the unpaired variables and one variable from each pair, with37 inverted. It is a domain, so I_J is prime and contains no power of37.

If k is not in J, positions k and k+1 are in different blocks. Their images depend, possibly by inversion, on two independent surviving variables. Their product is therefore not identically alpha. Hence D_k is not in I_J and is a unit in R localized at I_J.

For any competing tiling J', multiplication by the product of the D_j for j in J transforms its denominator into the quotient

    product_(j in J minus J') D_j / product_(k in J' minus J) D_k.

The denominator is a unit in the localization. If J' omits any pair of J, its term is zero modulo I_J. If it contains J properly, it has more y pairs and its coefficient is zero by the global maximality choice. The only surviving term is therefore the selected one:

    A_J product_(j in J) C_(3,29)(T_j,T_(j+1)).

Every C factor is a unit. The power-series ring in the unpaired variables injects into R/I_J, so A_J remains nonzero there and in its fraction field. This contradicts the zero identity. For J empty, maximality already removes all paired patterns and the identity directly forces its nonzero A_J to vanish.

This calculation checks the full ordered, noncommutative word problem. Antisymmetry of a y coefficient creates no cancellation: a fixed ordered target word is used, and different tilings have different surviving pole sets. It would be insufficient merely to discuss unordered pairings or a single total pole order; the candidate uses the stronger disjoint-pair prime ideal and is valid.

## 7. Conclusion and limits

The candidate's arithmetic hypotheses imply its abstract criterion, and the criterion's proof passes the review above. The actual rational representation is therefore faithful on H under the stated inputs. A kernel element of the pro-37 tripod outer action belongs to H by its cyclotomic character, and its rational image is trivial. Faithfulness on H then gives triviality, which is the candidate's stated equality Omega_37^*=Omega_37.

The proof uses a single even arithmetic direction of Z_37-rank1 and an explicit unit cup coupling. Multiple even directions or higher-degree annihilators are not covered by this audit. The integral image can still require an even degree32 generator; the checked MCS obstruction to integral generation by odd elements is fully compatible with this kernel conclusion.

This report has checked the new argument in full. It has not independently reproved the cited major arithmetic or motivic theorems, executed a formal proof checker, or established whether this prime37 deduction already occurs in the literature.
