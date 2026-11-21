# A checked nonlinear proof at p=37: ordered poles detect the extra even direction

Status: 21 November 2026. **Checked deduction developed in this run.** The initiating researcher, two independent agents, and the parent researcher each read the whole argument and found no remaining mathematical gap. This is not a literature attribution, novelty claim, machine verification, or all-irregular-primes theorem. The candidate and separate audit notes preserve the check trail. Researcher `/root/tripod_integral`, GPT-6 Astra Pro; effort not exposed. The argument below develops the nonlinear route beyond the failure of odd linear moments. It proves the tripod kernel-field equality at37, consistently with the separate failure of integral odd generation at37.

## 1. An abstract pole-separation criterion

Let p be odd, Gamma=<gamma>~=Z_p, Lambda=Z_p[[Gamma]], and u in 1+pZ_p a topological generator. Let H be free pro-p, equipped with a continuous Gamma action. Suppose its abelianization has a Gamma-compatible decomposition

    H_ab = (direct sum over a in A of Lambda e_a) direct sum Z_p e_y,

where A is a finite set of odd residue classes modulo p-1, and Gamma acts on e_y as multiplication by alpha in 1+pZ_p. Suppose a finite prime-to-p group Delta commuting with Gamma acts on e_a by its odd character a and acts evenly on e_y. We only need its eigenspaces to distinguish the odd orbit types; the scalar alpha is independent of Delta.

Choose lifts x_a,y in H of these exact abelian classes and put

    x_(a,t) = gamma^t x_a gamma^(-t),    t in Z_p.

Assume there is an actual continuous homomorphism rho:H->U(Q_p), equivariant for Gamma and Delta, such that:

1. Lie(U) is the weight-completed free Lie algebra on s_m for odd m>=3.
2. After a rational Levi choice, Gamma acts on s_m by u^m, and Delta acts by character m.
3. The image is Zariski-dense in U.
4. Every odd class modulo p-1 occurs in A (with one orbit per class).

The parity assumption makes the generator-length-one component of rho(y)-1 zero. Write

    E = (gamma y gamma^(-1)) y^(-alpha) in closure([H,H]).

All commutator subgroups here are closed. The abelian class of E is zero by the definition of alpha. The quadratic Magnus coefficients of E involving only odd orbit letters define measures mu_(a,b) on Z_p^2, and hence integral Amice transforms

    C_(a,b)(T_1,T_2) = integral (1+T_1)^t (1+T_2)^v dmu_(a,b)(t,v).

**Cup/nonlinear hypothesis:** for some ordered pair (a_0,b_0), the constant term of C_(a_0,b_0) is a p-adic unit.

Under these hypotheses, rho is injective, as proved below.

### 1.1 The compact orbit basis is genuinely free

Let X be the disjoint union of the finitely many compact sets {a} times Z_p and one isolated point y. Form the inverse limit F_X of the finite-rank free pro-p groups on

    X_n = (A times Z/p^n) disjoint union {y},

with transition maps folding t modulo p^n. This group has the universal property for continuous maps from X into a pro-p group: compose any such map with a finite quotient of the target, where it factors through an X_n, and use the finite free universal property. Its abelianization is the compact free Z_p-module

    Z_p[[X]] = Lambda^(|A|) direct sum Z_p.

This abelianization assertion follows from the same universal property restricted to abelian pro-p targets; it does not assume that abelianization commutes with an arbitrary inverse limit.

The indicated map X->H therefore induces a continuous map f:F_X->H. It is an isomorphism on abelianizations by construction. In particular its image surjects on H/Phi(H), so it is onto H: any proper closed subgroup of a pro-p group is contained in a proper open subgroup (separate a point from it in a finite quotient), and then in a maximal open subgroup. It therefore cannot surject on the Frattini quotient.

Because H is free pro-p it is projective, and f has a continuous section s:H->F_X. The closed subgroup s(H) surjects on F_X/Phi(F_X), because f induces an isomorphism on that quotient. The same Frattini argument forces s(H)=F_X. Hence f is an isomorphism.

Thus H has precisely the compact orbit basis above. This uses projectivity of the arithmetic H, not an invalid infinite-rank Hopfian assertion.

Apply the integral finite-rank Magnus embeddings at every X_n. They are compatible and injective in the inverse limit. Give each orbit letter degree1 and the isolated y letter degree2. Every nontrivial element g of H has a first finite nonzero degree d for this weighted Magnus expansion, since positive letter weights lie in {1,2}. For each pattern of singletons and y's, the coefficient is a bounded Z_p-measure on the coordinates of the singleton letters. There are finitely many patterns and orbit types in any given d.

### 1.2 The length-two kernel of y is meromorphic, with a controlled pole

Let ell_m be the mth abelian coordinate of U. Equivariance and the Delta decomposition give

    ell_m(rho(x_(a,t))) = a_m u^(mt)   if m is in class a,
                         0            otherwise.

Each a_m is nonzero: if it were zero, ell_m would vanish on all orbit generators and on y, hence on H, contradicting density. Rescale the free letter s_m by a_m. This is an allowed weightwise Q_p change of basis; no integral or uniformly bounded change of lattice is asserted. In these letters the linear component of rho(x_(a,t))-1 is exactly the sum of u^(mt)s_m over m of class a.

Let B_(m,n) be the coefficient of s_m s_n in rho(y)-1. Since rho(y)-1 has no linear component, taking the length-two component of E gives

    (u^(m+n)-alpha) B_(m,n) = C_(a,b)(u^m-1,u^n-1),       (1)

where a,b are the classes of m,n. Indeed Gamma scales a word by its total weight, the power y^alpha contributes alpha times the length-two component, and in E's first nonzero source Magnus degree only the pairs of orbit letters can contribute in target length2. Terms involving y in [H,H] have weighted degree at least3.

Set

    D(T_1,T_2) = (1+T_1)(1+T_2)-alpha.

The formal meromorphic kernel for y in an (a,b) target pair is therefore C_(a,b)/D. Equation (1), including at any special grid points where D vanishes, is all that will be used. Division by D is only made in the formal fraction field after denominators are cleared.

The numerator for (a_0,b_0) is a unit of Z_p[[T_1,T_2]], since its constant term is a unit. The divisor D=0 lies in the open unit polydisc: solve T_2=alpha/(1+T_1)-1; alpha-1 is in pZ_p. Hence this numerator does not cancel the divisor.

### 1.3 From a kernel element to a finite sum over ordered tilings

Suppose rho(g)=1 and g is nontrivial. Let d be the first nonzero weighted Magnus degree of g-1. A source word of degree d is described by a subset J of {1,...,d-1} with no two adjacent elements. Each j in J denotes a y occupying target positions j,j+1; all other positions are singleton orbit letters. Thus J is an ordered tiling of d positions by length-one and length-two blocks.

For fixed singleton orbit types, let A_J be the multivariate Amice transform of that source coefficient measure. It is an integral power series in precisely the unpaired variables. The coefficient of any ordered target word s_(m_1)...s_(m_d), with specified odd residue classes, yields an identity

    sum_J A_J(T_i : i unpaired by J)
          product_(j in J) C_(a_j,a_(j+1))(T_j,T_(j+1))/D_j = 0,      (2)

on the grid T_i=u^(m_i)-1, whenever the displayed divisions are permitted. Here D_j=(1+T_j)(1+T_(j+1))-alpha. Equivalently, multiply by all D_j for 1<=j<d. The resulting integral analytic identity is valid at every grid point by (1), with no division.

Why higher source terms do not intervene: every orbit letter maps to target length at least1 and y maps to length at least2. Source terms of weighted degree greater than d therefore have target length greater than d. Terms of smaller degree vanish by the choice of d. For terms of degree d only each letter's lowest permitted length contributes. This is why generator length, not arithmetic weight, is used in (2).

Substitution itself is justified exactly as in the checked pro-2 proof. At a finite arithmetic weight cutoff N only finitely many source degrees contribute. All coefficient functions of the continuous compact orbit maps are bounded Q_p-valued functions. Integration against the bounded source measures, uniform locally constant approximation, and Fubini give a continuous multiplicative substitution. Equality with rho follows on the compact generators and hence on H. No pro-p universal property is applied to the noncompact Q_p target.

For each fixed odd residue class a, the permissible integers m=a+(p-1)p^n, for sufficiently large n, give distinct grid points tending to u^a-1 inside pZ_p. Iterating the one-variable identity theorem in every variable shows that the denominator-cleared version of (2) vanishes identically. Therefore (2) is an identity in the fraction field of

    R = Z_p[[T_1,...,T_d]][1/p].

The ring choice is essential: its coefficient denominators have a common finite bound. We do not replace it by Q_p[[T_1,...,T_d]], in which a divisor with nonzero constant term would become a unit through an inverse with unbounded denominators.

### 1.4 The ordered-pair pole lemma

Choose, among all nonzero degree-d coefficient measures and all orbit-type patterns, one with the maximum number of y letters. Let its tiling be J. If J is empty, the same argument below simply says its coefficient must vanish. For each y pair in this chosen pattern assign target types (a_0,b_0), for which C is a unit; at each singleton assign its specified source orbit type. This fixes one identity (2) in which its A_J is nonzero. No tiling with more y pairs has a nonzero coefficient, by the global maximum choice.

Consider the ideal

    I_J = (D_j : j in J) in R.

It is prime. The pairs are disjoint, and imposing each relation substitutes

    T_(j+1) = alpha/(1+T_j)-1.

This is a valid substitution in Z_p[[T]] because its constant term alpha-1 is p-adically topologically nilpotent. The quotient is the corresponding formal power-series ring in the unpaired variables and one variable from each pair, with p inverted, so it is a domain.

For k not in J, D_k does not belong to I_J. Its two neighboring positions lie in different blocks of the tiling, so their remaining free variables are independent; their product is not identically alpha. Hence every such D_k is a unit in R localized at I_J.

In that localization multiply (2) by product_(j in J) D_j and reduce modulo I_J. Every other tiling J' omitting a j in J vanishes. A tiling containing J properly has more y letters and has zero coefficient by maximality. Thus only J remains, giving

    A_J times product_(j in J) C_(a_0,b_0)(T_j,T_(j+1)) = 0

in the fraction field of R/I_J. Each C factor is a unit. A_J depends only on unpaired variables, whose power-series ring embeds in R/I_J, so it remains nonzero. Contradiction.

For J empty, maximality says every nonzero coefficient has no y letters; the identity is just A_empty=0 for its chosen singleton types, also a contradiction.

This proves the abstract criterion.

## 2. Arithmetic verification for p=37

Let F=Q(mu_37), K=Q(mu_(37^infinity)), Omega the maximal pro-37 extension of F unramified outside37, P=Gal(Omega/F), and H=Gal(Omega/K). Let Gamma=Gal(K/F), and choose gamma lifting its generator with chi(gamma)=u=1+37. The finite group Delta=Gal(F/Q) can be lifted so as to commute with a generator gamma_0; Sharifi's procyclic construction does this. Replace gamma_0 by gamma_0^v, with v=log(1+37)/log(chi(gamma_0)) in Z_37^times, to obtain the prescribed chi(gamma)=1+37 while preserving commutation. Its order36 is prime to37.

### 2.1 H is free, and M=H_ab has the required arithmetic module shape

Iwasawa1981 Theorem2 pp273–274 plus Ferrero–Washington gives freeness of H, as established and source-checked in work/irregular_moment_gate.md. Thus M has no Z_37-torsion. Kummer duality identifies M+ with (A_infinity−)^vee(1), so it is a torsion Lambda-module and is nonzero at37. Weak Leopoldt gives rank_Lambda M=18. Exact locators in Sharifi's primary-author notes are Theorems3.3.3 and3.3.4 and Proposition3.4.7.

MCS §8 pp22–23 gives a minimal generating set of P consisting of gamma, x_m for the18 odd m with3<=m<=37, and a single even y of character32. Vandiver37 was separately certified; 32 is its only irregular index. The mod-(p,T) quotient of M has precisely these19 non-cyclotomic directions, by

    0 -> M_Gamma -> P_ab -> Gamma ->0,

whose exactness follows from H_2(Gamma,Z_p)=0 (or the split semidirect-product abelianization). The odd part therefore has18 minimal Lambda generators. As M+ is Lambda-torsion, M− has rank18. A surjection Lambda^18->M− has kernel of rank zero; a submodule of the free module over the domain Lambda has no such nonzero kernel. Therefore

    M− ~= direct sum_(a odd mod36) Lambda e_a.                        (3)

The plus part has one minimal Lambda generator, represented by y. By Nakayama it is cyclic, and it is nonzero already because this mod-(p,T) quotient is one-dimensional. MCS Corollary8.3 gives the initial relation

    37 y -3[gamma,y] -11[x_3,x_29] -[x_7,x_25] + ... =0

in the second term of the descending p-central graded group. Choose lifts of the odd/even abelian character classes as in MCS §9 pp24–25. Abelianize H and project to its plus part. The odd commutators vanish. The coefficient of y in the full relation is a power series f(T) annihilating its class, and the displayed initial relation gives

    f(T) = 37 -3T modulo (37,T)^2.                                  (4)

Higher descending-p-central terms contribute coefficients in (37,T)^2 after this linearization. Explicitly, first linearize the free presentation group into A_free semidirect Gamma, where A_free is the free Lambda-module on the non-cyclotomic generators. Use the filtration ((p,T)^(n-1)A_free) semidirect p^(n-1)Gamma. Commutators and pth powers send filtration degrees to the required subsequent degrees; the key elementary containment is (1+T)^(p^(n-1))-1 in (p,T)^n. Thus the image of the third descending p-central subgroup has its A_free coordinate in (p,T)^2 A_free. Read the y coefficient there before passing to the arithmetic quotient M; this proves the coefficient congruence rather than merely a congruence after imposing relations. The possible gamma-only term vanishes because the original relator is in the cyclotomic kernel; odd linear terms vanish on the plus projection.

By Weierstrass preparation f is a unit times T-beta for beta in37Z_37, with v_37(beta)=1. Consequently M+ is a quotient of Lambda/(f)~=Z_37. It is nonzero and Z_37-torsion-free, hence

    M+ ~= Z_37,     gamma acts as alpha=1+beta.                       (5)

In particular this module shape is deduced from the explicit initial relation; it does not assume an unverified numerical lambda-invariant formula or infer it merely from a nonzero class group.

Choose orbit lifts x_a of the bases in (3) and y of a Z_37-basis in (5). Section1.1 then gives the actual compact free pro-37 basis required by the abstract criterion. These lifts can preserve the previously chosen Frattini classes: project their abelian classes with the integral Delta-idempotents and lift back through H->M. The projections preserve the specified residual characters. Replacing generators by elements with the same Frattini classes is induced by an automorphism of the finite-rank free presentation group (surjectivity by the Frattini criterion and injectivity by finite-generated profinite Hopficity), and this automorphism is the identity in descending p-central degree2: pth powers and commutators of the generators retain their degree2 classes. Allowing a unit scalar in each one-dimensional eigenspace merely rescales the relevant classes and cup coefficients by units. Thus the displayed f(T) congruence and nonzero cup coefficient are preserved by the required generator choices.

### 2.2 Why the odd–odd cup coefficient supplies the required unit C

Write E=gamma y gamma^(-1) y^(-alpha). Its abelian class in H is zero. The semidirect product P=H semidirect Gamma has a presentation on gamma,x_a,y with the single relation

    R = gamma y gamma^(-1) phi(y)^(-1),

where phi is the actual Gamma automorphism of H and phi(y)=E y^alpha. To verify this presentation, given images of gamma,x_a,y satisfying R, send every compact orbit generator x_(a,t) to gamma^t x_a gamma^(-t). The free compact-space universal property supplies a map from H. Gamma compatibility is automatic on all x_(a,t) and holds on y by R, so it extends to the semidirect product. Thus this is a genuine presentation, not a formal extra relation guessed from the graded group.

In the second descending p-central quotient, R has the form

    [gamma,y] +(1-alpha)y - E_2,

where E_2 is the ordinary quadratic Magnus term of E after all orbit parameters are folded to their augmentation. In particular its x_a x_b coefficient is, up to the sign convention for commutators, C_(a,b)(0,0).

The displayed presentation has one defining relator. In the degree-two quotient, conjugation fixes its class and pth powers of the relator vanish, so every relation has initial term equal to a scalar multiple of its class modulo p. No freeness or asphericity statement about the full relation module is needed. MCS's nonzero initial relation is therefore a nonzero scalar multiple of that of R. Its coefficient of [gamma,y] is -3, a unit; its coefficient of [x_3,x_29] is -11, also a unit. Hence

    C_(3,29)(0,0) is a 37-adic unit.                                 (6)

Any unit changes of the chosen eigenspace bases preserve this assertion. This is the exact information needed in the pole lemma; no claim about all higher cup or Massey products is inserted.

### 2.3 The rational representation is the actual tripod image

Hain–Matsumoto Proposition8.3 and Theorem8.4, together with Brown's rational Deligne–Ihara theorem, give the actual continuous dense representation H->U(Q_37) and the completed free Lie algebra on odd s_m, as in the checked pro-2 proof. It factors from the pro-37 outer action, and the cyclotomic character detects any kernel outside H.

One may arrange that the image of gamma is in a Levi torus by a unipotent conjugation: solve successively in each positive weight, using that u^w-1 is nonzero in Q_37 for w>0. The construction converges in the weight completion. Since Delta commutes with gamma, its image then centralizes that torus element; the unipotent centralizer is trivial for the same weight reason. Thus Delta also acts by the stated weight characters. This is a rational conjugation only and asserts nothing about the integral image lattice.

Each odd linear target coordinate is nonzero on its single matching Lambda orbit by density; y has no odd linear coordinate by parity. All abstract hypotheses are therefore matched by (3), (5), and (6).

## 3. Conclusion and completed audit scope

The abstract criterion applies at37 and proves

    Omega_37^* = Omega_37.

It remains compatible with the already checked assertion (g_37^ab)_32 !=0 and failure of integral odd generation. The even arithmetic direction is detected by a non-removable pole in the quadratic moment kernel, rather than by an odd linear Soulé coordinate.

The whole-proof reviews checked the following specific points:

1. The compact orbit free-basis lemma, including the Frattini/projectivity step for the possibly infinitely generated H.
2. The actual module deduction (4) from the descending p-central initial relation, and the exact invariants/coinvariants used in (3).
3. The relation presentation and passage from the MCS odd–odd cup coefficient to the constant term of E's degree-two measure kernel.
4. The target Levi normalization and normalized coefficient equation (1).
5. The ordered-tiling localization lemma, especially the claim D_k notin I_J for k outside J and the injection of the unpaired-variable coefficient ring.
6. Analytic grid separation after clearing denominators, and continuity of the finite-weight substitution.

No independently checked result for other irregular primes is claimed. Multiple even generators or higher Lambda-torsion rank would require a matrix/higher-pole version and cannot be silently covered by the one-generator lemma.

## 4. Primary locators actually consulted

- Iwasawa, Riemann–Hurwitz formula and p-adic Galois representations for number fields, Tohoku33(1981)263–288, Theorem2 pp273–274; exact original PDF https://www.jstage.jst.go.jp/article/tmj1949/33/2/33_2_263/_pdf/-char/en . Already read in full for the criterion.
- McCallum–Sharifi, A cup product in the Galois cohomology of number fields, author version https://www.math.ucla.edu/~sharifi/publ/pairing.pdf : §8 pp22–23, Theorem8.2 and Corollary8.3, and §9 pp24–25. These pages were reread for the present candidate. Local work/mccallum_sharifi_pairing.txt.
- Sharifi Iwasawa notes https://www.math.ucla.edu/~sharifi/notes/iwasawa-ch03.html : Theorem3.3.3 (Lambda rank), Theorem3.3.4 (weak Leopoldt), Proposition3.4.7 (Kummer plus part). Fresh retrievals turn684819127view0, turn684819127view1, turn684819127view2, turn684819127view3.
- Sharifi galstr.pdf §2 p3: commuting Delta/Gamma lifts from a procyclic cyclotomic lift; the same MCS §9 source permits character-normalized generators.
- Hain–Matsumoto and Brown inputs: exact locators and actual-image audit already in work/pro2_moment_proof.md and work/pro2_independent_audit.md.
