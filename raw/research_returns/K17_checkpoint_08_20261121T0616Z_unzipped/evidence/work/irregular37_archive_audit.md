# Independent review of the prime-37 pole proof

Reviewer: GPT-6 Astra Pro, `/root/archive_kummer`; effort setting not exposed. Date: 2026-11-21 UTC.

## Verdict and scope

The complete proof in `work/irregular37_pole_candidate.md`, including its explicit linearization and one-relator presentation, passes this independent mathematical review relative to the cited arithmetic and rational-image theorems. The conclusion supported by this argument is faithfulness at the single prime 37. No assertion about all irregular primes, integral generation by odd elements, formal verification, or priority follows from the review.

I read the candidate in full before developing the checks below. The particular focus was to try to break the arithmetic module deduction, the simultaneous Gamma/Delta choices, and the transfer from the published minimal relation to the actual nonlinear action on the even generator. I also independently checked the entire abstract criterion. Earlier agreement by the other reviewers was not used as an input to these deductions.

## IR37-INPUT: primary inputs and their precise roles

The following primary passages were inspected during this review.

* Iwasawa, *Riemann--Hurwitz formula and p-adic Galois representations for number fields*, Tohoku Math. J. 33 (1981), 263--288: the definition of a cyclotomic Z_p-field in section 4, the class-group structure discussion in section 5, and Theorem 2 with its complete proof on printed pages 273--274. The theorem gives freeness of the maximal p-ramified group over the infinite cyclotomic field when mu is zero. The preceding paragraph explicitly records the Ferrero--Washington result for abelian fields. Local source: `work/iwasawa_riemann_hurwitz.pdf` and its text. Journal URL: https://www.jstage.jst.go.jp/article/tmj1949/33/2/33_2_263/_pdf/-char/en .
* McCallum--Sharifi, *A cup product in the Galois cohomology of number fields*, author version dated 5 December 2003: introduction pages 1--3 for the maximal pro-p group and descending p-central conventions; section 8 pages 21--23, including the complete proof of Theorem 8.2 and Corollary 8.3; and the character-normalized generator paragraph of section 9 pages 24--25. Author URL: https://www.math.ucla.edu/~sharifi/publ/pairing.pdf .
* Sharifi, *Relationships between conjectures on the structure of pro-p Galois groups unramified outside p*: section 2 page 3 for commuting lifts, and Lemma 2.1 with its proof on pages 3--4. Author URL: https://www.math.ucla.edu/~sharifi/publ/galstr.pdf .
* Sharifi, *Iwasawa Theory*, Chapter 3: Theorems 3.3.3 and 3.3.4, Corollary 3.3.14, Proposition 3.4.7 and Corollary 3.4.8 were checked for the rank, finite generation and plus-module assertions. Author URL: https://www.math.ucla.edu/~sharifi/notes/iwasawa-ch03.html .

The actual-image and rational-freeness input is the Hain--Matsumoto/Brown input independently checked earlier in `work/pro2_independent_audit.md`: Hain--Matsumoto Proposition 8.3, Theorem 8.4 and the cyclotomic-kernel density argument, together with Brown's rational Deligne--Ihara theorem. This review reuses that already inspected input and does not claim a fresh proof of those theorems. The Vandiver-37 certificate and unique irregular index 32 are the previously supplied arithmetic inputs; the McCallum--Sharifi cup-product computation is used as its published theorem, not rerun.

The crucial source point is that the proof of McCallum--Sharifi Theorem 8.2 starts with an actual relator in a free presentation and computes it modulo the third descending p-central subgroup. Corollary 8.3 is therefore usable before passing to the arithmetic quotient. It supplies coefficients 37 on y, -3 on [gamma,y], and -11 on [x_3,x_29], with the displayed conventions. It is not merely an unexplained linear dependence in the quotient graded group.

## IR37-FIELD: the exact free group and the commuting lifts

Put F=Q(mu_37), K=Q(mu_(37^infinity)), and let Omega be the maximal pro-37 extension of F unramified outside 37. The maximal pro-37 extension of K with that ramification restriction is also Omega. Indeed, a finite Galois p-extension of K descends, with its finite Galois action, to a sufficiently high finite cyclotomic layer F_n. Its normal closure over F is a compositum of conjugate p-extensions over F_n, followed by the p-extension F_n/F, and is still a p-extension. Ramification away from p cannot disappear on passage from F_n to the cyclotomic tower, which is unramified at those primes. Thus the descended extension lies in Omega. The reverse inclusion is immediate.

Iwasawa's theorem consequently applies to the exact H=Gal(Omega/K) used in the candidate. K is a cyclotomic Z_p-field in his sense and is abelian over Q. Ferrero--Washington gives mu=0, so H is free pro-p. Its abelianization M is therefore torsion-free as a Z_p-module. This is not a claim that M is torsion-free as a Lambda-module.

The simultaneous lifts can be made exactly as asserted. Choose tau in Gal(Omega/Q) lifting a topological generator of Gal(K/Q). Sharifi's construction gives delta=lim tau^(p^i), of order p-1, and gamma_0=tau^(p-1), commuting with delta. The cyclotomic value of gamma_0 generates 1+pZ_p. A unique unit Z_p-power of gamma_0 has cyclotomic value u=1+p; replace gamma_0 by that power. Delta=<delta> still commutes with the resulting gamma. The closed procyclic subgroup generated by gamma maps isomorphically to Gamma, so P=Gal(Omega/F) is H semidirect Gamma with this section.

The character action on M is consequently an honest action commuting with Lambda. Integral Delta idempotents are available because p-1 is a unit in Z_p. The argument only needs these projectors on the abelianization; it does not incorrectly treat a group-ring idempotent as an action on a nonabelian group. Sharifi's stronger nonlinear eigenlift lemma is available but is not necessary for most of this construction.

## IR37-MODULE: recovering the complete module shape

For a split semidirect product H semidirect Gamma, abelianization gives

    P_ab = M_Gamma direct sum Z_p gamma.

One can prove this directly: the closed commutator subgroup is generated by [H,H] and the elements gamma h gamma^(-1)h^(-1). The splitting is compatible with Delta because gamma and Delta commute. Hence reduction modulo p identifies M/(p,T)M with the non-cyclotomic part of P/Phi(P).

The inspected MCS generating set at 37 has one such direction in every odd Delta character modulo 36 and one even direction, character 32. There are eighteen odd directions. The rank theorem gives rank_Lambda M=18; the Kummer plus-module description gives rank_Lambda M+=0. Thus M- has rank eighteen and eighteen minimal Lambda generators. Nakayama gives a surjection Lambda^18 onto M-. Its kernel has rank zero and is a submodule of the free module over the domain Lambda. A nonzero element of such a submodule remains nonzero after tensoring with the fraction field, so the kernel is zero. Applying Delta projectors produces a rank-one free Lambda summand in every odd character.

The plus module has one minimal generator and is cyclic by Nakayama. It is already nonzero because its quotient modulo (p,T) has dimension one. Thus its nonzeroness does not require a further assertion about class-group capitulation.

### Exact adjustment of the MCS generators

The generators may be placed in H and made pure in their abelian character components without losing the initial relation. First remove the cyclotomic component of each non-cyclotomic generator by a power of gamma. Since its cyclotomic coordinate was zero modulo p in the minimal Frattini basis, this changes it only by an element of Phi(P). Project its class in M to the required Delta eigenspace and choose a group lift of the resulting class. The difference again has trivial image in P/Phi(P). The new gamma chosen above has the same normalized trivial-character Frattini class: that eigenspace is one-dimensional and its cyclotomic image fixes the scalar.

A homomorphism between the two free presentation groups obtained by choosing preimages of the old generators in the new presentation therefore induces the identity on their first graded quotients. On the second descending p-central quotient it also induces the identity: that quotient has the basis of pth powers and pairwise commutators of the first generators, and these operations depend only on the first graded classes. Equivalently, corrections in Fil_2 contribute only in Fil_3 to these expressions. Thus the MCS initial relator transfers to the exact abelian lifts. Unit changes of the chosen one-dimensional bases preserve all the required nonzero coefficients. This argument can be made without invoking an infinite-rank Hopfian assertion.

### Linearizing Fil_3 before imposing arithmetic relations

Let F_0 be the finite free pro-p presentation group on gamma, x_a, y. Map it to

    Q = A semidirect Gamma,     A=Lambda^19,

by sending the non-cyclotomic generators to the standard basis and gamma to Gamma. This is a continuous homomorphism to a pro-p group. Write m=(p,T), and define

    Q_n = m^(n-1) A semidirect p^(n-1) Gamma.

The image of Fil_n F_0 lies in Q_n. Here is a direct induction. If an element of Q_n is raised to the pth power, its A-coordinate is multiplied by a sum of p Gamma units; that sum lies in m. Its Gamma coordinate acquires a factor p. A commutator with an arbitrary element has A-coordinate consisting of a multiple of T times an element of m^(n-1) A, together with a multiple of ((1+T)^b-1)A for b in p^(n-1)Z_p. The latter power series lies in m^n. For instance, the integral identity

    j * binom(b,j) = b * binom(b-1,j-1)

gives v_p(binom(b,j)) >= n-1-v_p(j). Combining this with j-v_p(j)>=1 gives the required total (p,T)-adic order for every j>=1. These observations also show that the displayed filtration consists of subgroups with the required commutator and power containments.

Consequently Fil_3 maps into m^2 A in the A-coordinate. The actual MCS relator has zero cyclotomic coordinate. Its A-coordinate maps to zero in M, and its y coefficient is

    f(T) = p - 3T modulo m^2.

The odd-odd commutators disappear in this abelian linearization. Projecting to M+ kills all the odd linear coordinates, so f(T) annihilates the selected generator of M+. This is a congruence computed in the free module A before taking the quotient M, which rules out a circular use of the unknown annihilator.

The constant term of f has valuation one and its T coefficient is a unit. Weierstrass preparation gives f=v(T)(T-beta), where v(T) is a unit, beta is in pZ_p, and v_p(beta)=1. Hence M+ is a quotient of Lambda/(f), which is Z_p with T acting by beta. A nonzero torsion-free Z_p quotient of Z_p is Z_p: a nonzero kernel ideal would give a finite torsion quotient. Therefore

    M = (direct sum over the eighteen odd a of Lambda e_a) direct sum Z_p e_y,
    gamma e_y = alpha e_y,     alpha=1+beta in 1+pZ_p.

This proves the required full module statement without assuming a numerical lambda-invariant beyond the displayed initial relation.

## IR37-BASIS: compact orbit basis and Magnus coefficients

Choose x_a and y lifting these exact abelian bases, and let x_(a,t)=gamma^t x_a gamma^(-t). The free pro-p group F_X on the compact space X consisting of eighteen copies of Z_p and one isolated point is represented by the inverse limit of the finite free groups on the reductions of that space. A continuous map from X to a finite p-group factors through a finite partition; the finite free universal property then proves the asserted universal property, and passage to finite target quotients proves it for arbitrary pro-p targets.

The abelianization of F_X is Z_p[[X]]=Lambda^18 direct sum Z_p by the same universal property restricted to abelian targets. There is no need to assert that abelianization commutes with an arbitrary inverse limit. The indicated map F_X to H is an isomorphism on abelianizations and hence on Frattini quotients. Its image is closed. A proper closed subgroup of a pro-p group is contained in a proper open subgroup, and then in an index-p maximal open subgroup; it cannot surject on the Frattini quotient. The map is therefore onto.

Freeness of H makes it projective, so this surjection splits. The image of the section also surjects on the Frattini quotient of F_X, and is closed; the same argument makes it all of F_X. Thus the map is an isomorphism. This is valid for the infinite group and avoids a false appeal to infinite-rank Hopficity.

Finite-partition Magnus maps are compatible and injective in their inverse limit. Giving orbit letters degree one and y degree two still detects every nontrivial element in a finite first degree, because the two weights are positive. The coefficient of each fixed pattern is a bounded Z_p-measure on the corresponding product of orbit spaces. These measures and their Amice transforms are therefore legitimate, including for patterns with no singleton variables.

## IR37-CUP: the actual nonlinear coefficient

Let phi be conjugation by gamma on H, and E=phi(y)y^(-alpha). Its abelian class is zero, so E belongs to the closed commutator subgroup. Express phi(y) in the compact basis just proved, and evaluate that word in the finite free group on gamma,x_a,y by replacing every orbit generator by gamma^t x_a gamma^(-t). The element

    R = gamma y gamma^(-1) * (evaluated phi(y))^(-1)

is an actual defining relator for P, and it is the only required relator. To verify this assertion, take arbitrary proposed images of the finite generators in any pro-p target satisfying R. The compact orbit map gives a homomorphism from H. It intertwines phi with conjugation by the proposed gamma on every x_(a,t) automatically, and on y by R. Since these elements generate H, it intertwines on all of H. Continuity extends this compatibility from integer powers to Gamma. It therefore extends uniquely to H semidirect Gamma, which proves the presentation by its universal property.

In Fil_2/Fil_3, R has coefficient 1 on [gamma,y], the term (1-alpha)y (meaning coefficient (1-alpha)/p on the basis vector p y), and the negative of the folded quadratic coefficient of E on each odd-odd pair. Terms involving orbit parameters can be folded here because each x_(a,t) has the same first Frattini class x_a. Higher ordinary Magnus degree cannot contribute to degree two. Thus the coefficient on the ordered x_a x_b term is, up to the fixed commutator sign, C_(a,b)(0,0).

The image of the closed normal subgroup generated by R in Fil_2/Fil_3 is the scalar span of the initial class of R: conjugation acts trivially there, and pth powers of Fil_2 elements lie in Fil_3. The transferred MCS initial relation lies in that image and is nonzero. It must therefore be a nonzero scalar multiple of R's initial form. Comparing the [gamma,y] coefficients fixes a nonzero scalar because -3 is a unit modulo 37. The MCS coefficient -11 on [x_3,x_29] then forces C_(3,29)(0,0) to be a unit. Neither freeness of a relation module nor an asphericity assertion is being smuggled into this argument.

## IR37-REAL: rational normalization and the exact quadratic equation

The rational actual image supplies a continuous dense map H to U(Q_p), with weight-completed free Lie algebra on one generator s_m in each odd weight m>=3. A unipotent conjugation puts gamma in a Levi torus: solve successively at each finite weight using the nonzero scalars u^w-1. The process converges in the weight completion. Delta commutes with gamma, so its unipotent component after this conjugation lies in the unipotent centralizer of gamma, which is trivial by the same weight argument. It therefore acts by the stated weight characters.

On target generator length one, y has zero image by parity, and x_(a,t) has only coordinates m congruent to a, with value a_m u^(mt). Density forces a_m nonzero for every m; otherwise that abelian target coordinate would vanish on all the compact generators. Weightwise rescaling of rational letters removes these constants. It is not a bounded change of integral lattice.

Since y has no linear term, the length-two coefficient of the equality E=phi(y)y^(-alpha) is exactly

    (u^(m+n)-alpha) B_(m,n)
      = C_(a,b)(u^m-1,u^n-1).

There is no omitted cross term from the power of y. A term involving y in E has source weighted degree at least three and cannot enter this equation. Thus the proposed meromorphic expression C/D is justified as an equation after denominators are cleared, including at points where an individual displayed denominator vanishes.

## IR37-ANALYTIC: coefficient identities and bounded denominators

For a hypothetical kernel element, take its first nonzero weighted Magnus degree d. Every orbit letter has target generator length at least one; y has length at least two. Higher weighted source degrees cannot contribute to target length d. The degree-d source coefficients are indexed exactly by ordered tilings of d positions by singletons and adjacent y pairs. For each target word the candidate's finite tiling identity follows.

Substitution is legitimate at every finite arithmetic weight cutoff. Only finitely many target letters and word lengths remain, and the coefficient functions on the compact orbit spaces are continuous and bounded in Q_p. Integrating bounded source measures against these functions, using uniform locally constant approximation and finite Fubini, gives the multiplicative substitution. Agreement on the compact generators identifies it with the actual continuous representation. This avoids applying a pro-p universal property to a noncompact Q_p group.

Multiply the identity by all neighboring denominators D_j. The result has integral, hence uniformly bounded, coefficients. In a fixed odd residue class, the integers m=a+36*37^n give distinct points u^m-1 converging to the interior point u^a-1. Fixing the other variables at grid points and applying the one-variable identity theorem successively proves that the cleared analytic series vanishes identically.

The algebraic identity lies in the fraction field of R=Z_p[[T_1,...,T_d]][1/p]. This precise bounded-denominator ring is essential. Replacing it with all of Q_p[[T_1,...,T_d]] would invert a denominator with nonzero constant term using unbounded coefficients and would invalidate the intended pole argument. No such replacement is made.

## IR37-POLE: isolating a maximal tiling

Choose a nonzero first-degree coefficient with the greatest number of y letters. Let J be its disjoint adjacent-pair set. Give every y pair the good target types (3,29), and give its singletons their prescribed types. The coefficient A_J remains nonzero in this identity.

The ideal I_J=(D_j:j in J) is prime in R. Before inverting p, the change of coordinates

    S_(j+1) = T_(j+1) - (alpha/(1+T_j)-1)

is valid in the complete (p,T)-adic ring: the substituted constant alpha-1 lies in pZ_p. The pairs are disjoint, so these changes are independent. Since D_j=(1+T_j)S_(j+1), the quotient is the power-series ring in the unpaired coordinates and one free coordinate for each pair, followed by inversion of p. It is a domain, and the unpaired-coordinate ring injects into it.

For k outside J, D_k joins different blocks. After the substitutions its two remaining coordinates are independent, so D_k is not identically zero in this quotient. For example, across two paired blocks it becomes a unit multiple of the difference of their free coordinates. Thus D_k is a unit after localization at I_J.

In that localization multiply the tiling identity by the product of D_j for j in J and reduce modulo I_J. Every other tiling omitting a member of J vanishes. A tiling properly containing J has more y pairs and has zero coefficient by the maximal choice. Only the chosen term remains. Its A_J is still nonzero by the injection just proved; all its C_(3,29) factors are units because their integral constant terms are units. The resulting product cannot vanish. This is the contradiction. If J is empty, maximality leaves only the singleton coefficient and the analytic identity directly says it is zero, again a contradiction.

This argument checks ordered pairings rather than assuming that arbitrary residue intersections separate all tilings. It is the maximality condition and localization at the selected disjoint-pair ideal that perform the separation.

## IR37-CONCLUSION: exact implication and limitations

The arithmetic calculations provide every hypothesis of the abstract criterion, including the actual unit nonlinear numerator. The criterion makes the rational representation injective on H. A kernel element of the pro-37 tripod outer action lies in H because its action on the abelian fundamental group detects the cyclotomic character. Its image in the rational outer action is trivial by functoriality. Injectivity on H therefore forces that element to be trivial, giving the candidate's equality Omega_37^*=Omega_37.

The proof uses one even direction of Z_p-rank one and a unit odd-odd coupling. It does not extend without additional work to several even generators or a higher-degree Lambda annihilator. It is compatible with an additional even integral generator in arithmetic weight 32, and proves no integral odd-generation statement. All substantial external arithmetic and motivic results remain cited inputs. The local audit is a full paper-proof review, not a machine certificate or a claim that the deduction is absent from the literature.
