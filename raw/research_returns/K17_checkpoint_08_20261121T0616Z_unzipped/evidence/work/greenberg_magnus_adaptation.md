# Rational Iwasawa coordinates in the full Magnus pole argument

Researcher `/root/archive_kummer`, GPT-6 Astra Pro, 21 November 2026. Effort setting not exposed. Complete proof candidate for independent review. This note keeps the entire arithmetic group and does not replace it by a subgroup whose abelianization merely has finite index. The separate cup/extension lemma has passed its independent audit in `work/cup_ext_archive_audit.md`.

## 1. Algebraic statement

Let p be odd. Let H be a second-countable free pro-p group, with commuting continuous actions of `Gamma=<gamma> isomorphic to Zp` and `Delta isomorphic to F_p^times`. Write c for the order-two element of Delta, `Lambda=Zp[[Gamma]]`, `R=Lambda[1/p]`, and `M=H_ab`. Suppose:

1. M is finitely generated over Lambda. Its minus part U has, after inverting p, one free R summand in each odd Delta character. Its plus part T is finite free over Zp. Each nonzero even component `T_e[1/p]` is cyclic over R.
2. Exact Delta-eigenlifts of abelian eigenclasses can be chosen in H, including inside arbitrarily small Delta-stable neighborhoods. This is the finite-order averaging lemma already used for the arithmetic group.
3. There is a continuous Gamma-times-Delta-equivariant representation rho into the weight-completed free prounipotent group over Qp on one letter s_m in each odd weight `m>=3`. After a rational Levi normalization, gamma acts on s_m by `u^m`, where `u=chi(gamma)` topologically generates `1+pZp`, and Delta acts by `omega^m`. The image of H is Zariski dense in every finite weight quotient.
4. For each nonzero T_e choose an integral multiple v_e of a rational cyclic generator, an exact Delta-eigenlift y_e, its conjugates `y_(e,j)=gamma^j y_e gamma^(-j)`, and its characteristic polynomial `q_e(z)`. Express the odd–odd quadratic coefficient of the actual companion error in any rational R-basis of U. For every root alpha of q_e, over a finite splitting field, at least one matching ordered odd-character coefficient satisfies

       C_(e;a,b)(T,alpha/(1+T)-1) != 0.

Then rho is injective. In particular this assertion does not require U to be integrally Lambda-free or T_e to be integrally cyclic. It allows repeated roots of every q_e.

The coefficient spaces in this statement are always bounded-denominator power series, such as `O[[T1,T2]][1/p]`. No identification with power series having unbounded rational coefficients is intended.

## 2. An actual compact free basis of the entire H

Every compact torsionfree Zp-module is a product of copies of Zp: its Pontryagin dual is a divisible p-primary group, hence a direct sum of copies of Qp/Zp. Here H is free, so M is Zp-torsionfree. It is metrizable, and the product bases can be chosen countable. Decompose under the integral Delta idempotents. Choose a pointed convergent Zp-basis in each U_a and an ordinary finite Zp-basis of each T_e.

The quotient map H to M is an open map of profinite groups. The basis vectors in U tend to zero, so their lifts can be chosen to tend to 1. Apply the exact Delta-eigenlift construction inside a nested basis of Delta-stable open neighborhoods. It preserves the required abelian class and convergence. Choose exact eigenlifts of the finite T basis as well.

Let F be the free pro-p group on this pointed convergent sequence and the finite even set. Its abelianization is the product Zp-module with those basis vectors. The resulting homomorphism `F -> H` is therefore an isomorphism on abelianizations. Its image is compact and maps onto `H/Phi(H)`, hence equals H. For completeness, a proper closed subgroup of any pro-p group is contained in a proper open subgroup, and that open subgroup lies in an index-p subgroup; it therefore cannot be Frattini-surjective. No finite-generation hypothesis is needed for this observation.

Since H is free, this surjection has a continuous section. The section is inverse on abelianizations, so its closed image is Frattini-surjective in F and is all of F. Thus `F -> H` is an isomorphism. We have an actual compact free basis of the whole H, rather than an unspecified finite-abelian-index subgroup.

Assign weight 1 to the odd basis variables X_i and weight 2 to the finite even basis variables Y_l. The Magnus expansion is injective with these weights. One elementary verification uses the projections killing all but finitely many convergent basis elements. Every finite quotient of F kills a tail of that sequence, so F is the inverse limit of these finite-rank free pro-p groups. The ordinary finite-rank Magnus embedding detects each nonidentity element in some finite rank, and hence in some finite assigned degree. At a fixed degree its coefficient module is a finite sum of completed Zp tensor products of U and T, with their specified assigned weights.

## 3. Bounded rational coordinates in the odd variables

Fix a character-preserving R-isomorphism

    phi: U[1/p] -> direct sum_(a odd) R e_a.

Finite generation over Lambda gives fixed powers of p clearing phi and its inverse. Equivalently there are continuous integral maps between U and `Lambda^r` whose two compositions are multiplication by the same power of p. Continuity follows from the compact finitely generated Lambda-module topologies. On every completed tensor power of degree d the two induced compositions are multiplication by the corresponding d-th power. These completed tensor modules are torsionfree over Zp: using the product bases above they are products of copies of Zp. Therefore the maps are injective, and become inverse isomorphisms after inverting p.

It follows that each fixed Magnus degree can be expressed in the orbit coordinate modules

    Zp[[Gamma^s]][1/p] = Zp[[T1,...,Ts]][1/p],

one copy for each choice of odd characters and finite even-letter positions. These are the Amice transforms of bounded measures on Gamma^s. The denominator bound may grow with the assigned degree. At the first nonzero degree used in the proof it is a single finite bound, which is all that is needed.

The weight-m target linear coefficient is a continuous additive map from M to Qp. Parity kills T and character equivariance kills U_a unless `a=m modulo p-1`. Gamma equivariance on the remaining rank-one R module makes this coefficient a scalar multiple of evaluation at `T=u^m-1`. This follows first for polynomials in gamma and then by continuity for bounded power series. Density of rho implies that the scalar is nonzero: otherwise the weight-m coordinate on the abelianization of the target would vanish on its dense image. Rescale each s_m by that nonzero scalar. In the new target coordinates every odd singleton kernel is exactly

    f(T) -> f(u^m-1)

for its matching character. Such independent rescaling is an automorphism of the weight-completed free Lie algebra, because every finite weight quotient has finitely many generators.

## 4. Rational companion letters and the quadratic change of variables

Fix e and write `lambda_e=rank_Zp T_e`. Its rational cyclic generator v_e may be multiplied by a power of p to lie in T_e. The classes

    v_e, gamma v_e, ..., gamma^(lambda_e-1) v_e

are a Qp-basis of `T_e[1/p]`. They need not form an integral basis. Gamma acts invertibly and continuously on T_e; its characteristic polynomial q_e is monic integral with unit constant term and reduces modulo p to `(z-1)^lambda_e`. In particular every root is congruent to 1 in a splitting field's maximal ideal, and the polynomial is also the minimal polynomial of this rational cyclic module.

Choose an actual eigenlift y_e and the actual conjugates y_(e,j). Since their abelian classes lie in T, their assigned Magnus degree is at least 2 and their target generator length is at least 2. Let Z_(e,j) be the assigned-degree-two part of `y_(e,j)-1` in the original free-basis tensor algebra. It has the form

    Z_(e,j) = sum_l b_(j,l) Y_(e,l) + A_(e,j)(X),

where b is a finite invertible matrix over Qp and A is a completed quadratic odd tensor. In original integral coordinates b and A are integral; after the odd rational change they retain a common bounded denominator. There are no other terms of assigned degree two. The ordinary commutator description, or primitiveness of a first Magnus coefficient, makes A alternating, although alternation is not needed for invertibility of the change.

Replace the finite variables Y by the variables Z using this formula. This is a homogeneous triangular automorphism of the completed tensor algebra with assigned weights: it fixes the odd variables and has inverse

    Y=b^(-1)(Z-A(X)).

At every fixed degree only finitely many even variables occur, so the inverse changes coefficient denominators by a finite bound. It preserves a nonzero first degree. This construction is purely in the rational coefficient algebra. It does not assert that the rational companion classes are an integral group basis.

Its compatibility with rho is exact at leading degree. By definition Z_(e,j) is the leading assigned component of the actual element y_(e,j). Thus the associated graded substitution for rho sends Z_(e,j) to the target length-two component of that actual conjugate. With `z=u^(m+n)`, its ordered coefficient is

    B_(e,j;m,n)=z^j B_(e,0;m,n).

Write `q_e(z)=z^lambda_e-sum_j c_(e,j) z^j` and form the actual companion error

    E_e=(gamma^lambda_e y_e gamma^(-lambda_e))
        (product_j y_(e,j)^(c_(e,j)))^(-1).

It belongs to the closed derived subgroup because its abelian class is q_e(gamma)v_e=0. The assigned-degree-two part is the alternating odd tensor C_e. Products of the even conjugates have no target length-one terms, so comparison of length two gives exactly

    q_e(z) B_(e,0;m,n)
      = C_(e;a,b)(u^m-1,u^n-1),
    a=m modulo p-1, b=n modulo p-1.

This C_e is the same actual extension class as in the separately audited cup/extension lemma. The assigned-degree-two extension is independent of the choices of actual free lifts. Exact Delta eigenlifts make C_e have character e, so its coefficient in a pair (a,b) is zero if a+b differs from e; alternatively the target identity on the full residue grid gives the same zero by the analytic identity theorem.

## 5. Partial fractions and legitimate substitution

Choose a finite splitting field L for all q_e, with integers O. The rational functions `z^j/q_e(z)` form the finite-dimensional space with alternative basis

    (z-alpha)^(-k), 1<=k<=multiplicity_e(alpha).

Apply this constant invertible partial-fraction change to the finite Z variables. It preserves assigned degree and degreewise bounded denominators. The resulting even formal letter indexed by (e,alpha,k) has leading target kernel

    C_(e;a,b)(T1,T2) / ((1+T1)(1+T2)-alpha)^k.

The common numerator within an e component is retained. No simplicity of roots is required.

There are only finitely many positive integers w with `u^w` a root of any q_e. Restrict all test weights m to a sufficiently large ordinary integer tail. This excludes every zero denominator at a pair sum while leaving, in every fixed odd residue class, infinite sequences with an interior p-adic accumulation point. For example choose a sufficiently large fixed positive representative m0 and the tail `m0+(p-1)p^n`. The representation's coefficient identities are therefore valid on the necessary Cartesian grids before any division is made.

Substitution of the fixed-degree coefficient algebra into each finite arithmetic-weight quotient of the target is continuous. This can be checked in the original actual basis: truncate the convergent free sequence, apply ordinary finite-rank Magnus substitution, and pass to the limit. Every finite group quotient kills a tail; these truncations converge to the identity map of H in its profinite topology. The continuous image of H in the finite target quotient is compact, so all of its coefficient functions are bounded. The resulting finite tensor operations and evaluations converge. Bounded rational changes in a fixed source degree preserve this continuity. In the orbit coordinates it is equivalently integration of continuous bounded functions against the bounded measures, with the usual finite Fubini rule.

Consequently if g is nonidentity, d is its first nonzero assigned degree after the invertible changes, and rho(g)=1, the length-d target coefficient is obtained from that homogeneous degree alone. Larger source degrees have larger target length, and all smaller source degrees are zero. At any finite target weight this is an ordinary finite calculation followed by the justified compact limit.

## 6. Complete separation at the first nonzero degree

Decompose that nonzero degree-d coefficient into ordered tilings of d positions. A singleton is an odd character coordinate and a pair is one finite letter (e,alpha,k). For any fixed target residue assignment its vanishing image gives a finite sum

    sum_patterns A_pattern(T_i at singleton positions)
       product_pairs C_(e;a_j,a_(j+1))(T_j,T_(j+1)) / D_(j,alpha)^k = 0,

where `D_(j,alpha)=(1+T_j)(1+T_(j+1))-alpha`. Every A is a bounded-denominator power series. Clear all denominators. The resulting analytic function vanishes on a Cartesian grid of large odd weights, so repeated one-variable identity theorems make it identically zero. We hence obtain an identity in the fraction field of `O[[T1,...,Td]][1/p]`.

Among nonzero patterns choose one with the largest number of pairs. Fix its pair positions J and its root and even-character labels. Among nonzero patterns with those positions and labels choose a componentwise maximal vector of pole orders k. At each selected pair choose the ordered odd types supplied by hypothesis 4, and at each singleton choose its source type. These choices are independent because the selected pairs are disjoint.

Set `S_j=D_(j,alpha_j)` for j in J and retain every singleton variable and the left variable of every selected pair as base variables. The substitutions

    T_(j+1)=(alpha_j+S_j)/(1+T_j)-1

are an automorphism of the complete integral power-series ring. Let K_base be the fraction field of the bounded-denominator base-variable ring. The identity embeds in the ring of power series over K_base in the S_j with finitely bounded negative exponents.

Every denominator except a selected S_j has nonzero constant term there. At the same position a different root gives a nonzero root difference. At a different position it joins variables from distinct selected blocks, whose surviving variables are independent, so its product is not identically a prescribed constant. Wrong even characters are already zero for the fixed target types. These other denominators are therefore units in `K_base[[S_j]]` and cannot supply a negative S_j exponent.

Extract the coefficient `product_j S_j^(-k_j)`. A pattern missing a selected pair or using a different root there cannot contribute. A pattern containing every selected pair and any additional pair would have more pairs, so its coefficient is zero by the first maximality choice. For the remaining same-position and same-root patterns, contribution requires the pole-order vector to dominate k componentwise. The second maximality choice excludes every strict domination, and an incomparable vector has an insufficient pole order in at least one variable. Singleton types must match as well. Hence the only contribution is

    A_selected(singleton variables)
      product_(j in J) C_selected(T_j,alpha_j/(1+T_j)-1).

It is nonzero in K_base. The first factor is nonzero by selection and injectivity of the bounded coefficient representation. Each other factor is nonzero by hypothesis 4. A field has no zero divisors. This contradicts the zero identity. If J is empty, the same argument is the ordinary singleton moment identity, with no Laurent variables. Thus rho is injective.

## 7. Arithmetic hypotheses under one-variable Greenberg

The intended arithmetic hypothesis is that the unramified cyclotomic Iwasawa module X+ of Q(mu_(p^infinity)) is finite. It is not a multivariable pseudo-nullity assertion. We take p>=5 here; p=3 and p=2 are covered by the already checked separate results.

The source input that H is free for this abelian cyclotomic tower, using Iwasawa and Ferrero–Washington, and the actual-image Hain–Matsumoto/Brown description of rho are the same already fully audited inputs of the main pole proof. The following verifies precisely what changes without Vandiver.

Choose a finite Delta lift by the coprime complement theorem. The fiber over a generator of Gamma is a Delta-stable H-torsor because the cyclotomic quotient is abelian. The coprime identity H1(Delta,H)=1 follows from the finite complement theorem and compactness, and gives a Delta-fixed lift gamma. Its procyclic closure maps isomorphically to Gamma and supplies the commuting section.

The finite-level Kummer sequence makes H1(P,Fp) finite dimensional, so P is finitely generated and H is second-countable. Adjust finitely many generators of P by the chosen Gamma section to obtain elements h_i in H. Their closed normal closure has procyclic quotient surjecting onto Gamma with its indicated generator, so that quotient is Gamma and the normal closure is H. The abelian classes of the h_i therefore generate M over Lambda. This gives the finite-generation hypothesis directly.

First R is a PID. Lambda is a two-dimensional regular local UFD, its only height-two prime contains p, and localization at p therefore leaves a one-dimensional noetherian UFD. Such a ring is a PID. The notation R still means bounded-denominator power series, rather than Qp[[T]].

For an odd character a different from omega and omega^(-1), the complete duality calculation in Wake–Wang-Erickson, *Ordinary pseudorepresentations and modular forms*, Proposition 2.2.6, gives

    Ext^1_Lambda(M_a^#(1),Lambda)=X_(omega a^(-1)),
    Ext^2_Lambda(M_a^#(1),Lambda)=0.

Here the left-hand M is the p-ramified module, the source's fraktur X, and the right-hand X is unramified. Invert p. Greenberg kills the right-hand even component. Over the PID R, zero Ext1 into R means that the torsion summand of a finitely generated module is zero. The module is therefore free; the source's local/global unit exact sequence gives rank one. The involution and Tate twist are ring automorphisms and do not affect freeness.

The two exceptional odd characters are handled directly by the Coleman exact sequence

    0 -> Zp(1) -> U_local -> Zp[[Delta x Gamma]] -> Zp(1) -> 0.

The global minus units are exactly the root-of-unity term. Stickelberger gives `X_omega=X_(omega^(-1))=0`. Thus the omega^(-1) part of M is free of rank one; in the omega part M is the kernel of `Lambda -> Zp(1)`, namely the principal ideal `(gamma-u)`, again free of rank one. These are distinct components when p>=5. The unique valuation direction at the p-prime is even and does not affect this odd-component calculation.

Sharifi's Kummer comparison identifies T up to finite groups with `(Xminus)^iota(1)`. Ferrero–Washington gives finite generation over Zp, and H free excludes Zp-torsion, so T is finite free. Greenberg implies that Xminus is pseudocyclic character by character. After inverting p, finite kernels and cokernels disappear; hence every `T_e[1/p]` is cyclic. Repeated roots remain permitted. This proves all required rational module hypotheses.

The needed finite-level cup surjectivity is also supplied under this same Greenberg hypothesis. In Wake–Wang-Erickson, *Pseudo-modularity and Iwasawa theory*, Corollary 8.1.3(2), the assumptions are exactly that `X_chi(1)[1/p]` is cyclic over `(Lambda/xi)[1/p]` and

    X_theta tensor_Lambda (Lambda/xi)[1/p]=0.

The localization `[1/p]` on this second expression is essential. Greenberg and their section 2.1 give both hypotheses. The conclusion is an integral isomorphism

    varpi:(Hminus/I Hminus)/(p-primary torsion) -> X_chi(1).

Thus varpi itself is surjective. Fukaya–Kato §§7.1.8–7.1.10 imply generation of each finite-level H2 component by cyclotomic p-unit symbols. At tame level one the source assumptions are exactly `theta != 1,omega^2`. The omitted characters have `chi=omega^(-1),omega`, whose unramified modules vanish by Stickelberger and whose finite minus class groups vanish by the surjective norm projections. Components with unit characteristic power series also have zero target: the source's Xminus is p-torsionfree, so it has no nonzero finite submodule. All even H2 components are therefore covered, and WWE's running nonunit assumption is applied only to the nonzero ones.

At level `F_(n+1)=Q(mu_(p^(n+1)))`, FK gives generation with coefficients p^(n+1), and reduction gives generation with coefficients p^n as used for `P_n=H semidirect Gamma^(p^n)`. Their §7.1.9 gives the explicit class-group quotient description of this reduction. The unique omitted finite prime and absence of real places make the Brauer contribution zero. At every level the negative c part of p-units is the cyclic root-of-unity line; its self-cup is zero and mixed cups have negative parity. Hence the even target is generated by c-even unit cups. This conclusion needs no Vandiver identification of the whole H1 with units.

## 8. Exact passage from étale cups to pro-p group cups

Let `S_n=Spec O_(F_(n+1))[1/p]`, and let G_n be its full étale fundamental group. Its maximal pro-p quotient is P_n. To check that the fixed field Omega used here is also maximal over F_(n+1), take any finite Galois p-extension of F_(n+1) unramified outside p and form its normal closure over F. The conjugate extensions have a p-group compositum over F_(n+1), and F_(n+1)/F itself has p-power degree. The normal closure is a p-extension of F unramified outside p, so it lies in Omega. This proves the asserted equality of the pro-p quotient with the chosen P_n.

We need only an injection in degree two and an isomorphism in degree one; a full arithmetic K(pi,1) theorem is unnecessary. Put `N=ker(G_n -> P_n)`, and let A be a finite p-primary coefficient module whose action factors through P_n, such as the required Tate twists. A P_n-equivariant homomorphism `N -> A` with nonzero image would have a G_n-normal kernel. The resulting quotient of G_n would be an extension of P_n by a nonzero finite p-group, hence a pro-p quotient strictly larger than P_n. This contradicts maximality. Therefore

    H1(N,A)^(P_n)=0.

The five-term Hochschild–Serre sequence now gives

    H1(P_n,A) = H1(G_n,A),
    H2(P_n,A) injects H2(G_n,A).

For completeness, all actions here are continuous, the character kernel is closed, and an extension of a pro-p group by a finite p-group is pro-p because every finite quotient has p-power order. Thus this argument is valid without finite generation of N.

The universal finite étale tower over S_n has zero H1 with finite locally constant coefficients: after trivializing the coefficients, an H1 torsor is finite étale and becomes trivial at a later stage of that same tower. Equivalently use the classification of finite étale torsors and the continuity of finite étale objects under affine limits. The Cartan–Leray spectral sequence for this tower consequently gives

    H1(G_n,A) = H1_et(S_n,A),
    H2(G_n,A) injects H2_et(S_n,A).

The maps are compatible with cup products and Delta. This is precisely the low-degree consequence of the full universal-cover spectral sequence, not a claim that all its higher rows vanish. A freshly checked primary reference for the sequence and profinite-tower passage is Milne, *Lectures on Étale Cohomology*, Theorem 14.9, Remark 14.10 and Example 14.11, printed pp96–97, together with Proposition 14.13 p98 for H1 of a simply connected cover.

Every p-unit Kummer class on S_n therefore has a unique lift to group H1(P_n,Z/p^n(1)). Their cups map to their étale symbol cups. Section 7 proves that the c-even part of the étale H2 target is spanned by such cups with even input parity. Since the group H2 map is injective, this makes it an isomorphism on the even part and proves exactly the finite-level group cup-surjectivity hypothesis required in the bridge. One can also see the surjectivity directly: lift each generator and sum its lifted cups. Injectivity then makes every group class equal that sum.

This addresses all tower levels and the coefficient p^n convention explicitly. Although those Tate coefficients are already trivial over F_(n+1), the more general factor-through-P_n argument above also covers any needed shifted convention. Scalar extension from Zp to the integers O of a finite splitting field preserves the statements because O is finite free over Zp.

## 9. Combination with the cup/extension theorem

The separately proved cup/extension lemma now gives hypothesis 4 for the same actual companions and rational coordinates. Its root quotient is dual to the alpha-socle, with eigenvalue `u^2/alpha` and Delta exponent `2-e`; it covers repeated roots and uses one uniform denominator at all levels. Sections 1–6 therefore give injectivity of rho under the one-variable Greenberg hypothesis.

A kernel element of the original pro-p tripod action is cyclotomically trivial, lies in H, and maps to 1 under rho by rational completion. Injectivity kills it. This is the proposed conditional conclusion `Omega_p^*=Omega_p` under Greenberg. It is not a proof of Greenberg, and no converse implication is claimed. The all-Vandiver theorem remains the established explicit sufficient special case.

## 10. Exact primary locators and status

- Wake–Wang-Erickson, *Pseudo-modularity and Iwasawa theory*, arXiv:1505.05128v3, 7 September 2017, https://arxiv.org/pdf/1505.05128: section 2.1, Corollary 2.1.3 and Conjecture 2.1.5 p8; full Corollary 8.1.3 and proof pp48–49. Local `work/wake_wang_erickson_pseudo.pdf` and `.txt`.
- Wake–Wang-Erickson, *Ordinary pseudorepresentations and modular forms*, arXiv:1510.01661v4, https://arxiv.org/pdf/1510.01661v4: Proposition 2.2.6 and full proof pp3–4; Lemma 5.2.7 p13 for the explicit exceptional Stickelberger statement. Local `work/wake_wang_erickson_ordinary.pdf` and `.txt`. The fraktur/unramified notation was checked against the author's rendered PDF in the earlier source audit.
- Sharifi, *Iwasawa Theory* notes, https://www.math.ucla.edu/~sharifi/iwasawa.pdf: full Proposition 3.4.1 and proof pp90–91, Proposition 3.4.7 and Corollary 3.4.8 p92, Theorem 5.5.31 p148 and Proposition 6.1.1 pp151–152. Local `work/sharifi_full_iwasawa.pdf` and `.txt`.
- Fukaya–Kato, *On conjectures of Sharifi*, author version 15 August 2012, https://www.math.ucla.edu/~sharifi/sharificonj.pdf: §6.1.5 p76, §§7.1.8–7.1.10 p86, Theorem 7.2.8 p89. Local `work/fukaya_kato_sharificonj.pdf` and `.txt`. The final 2024 publication was not inspected; these locators deliberately refer to the retrieved author version.
- Milne, *Lectures on Étale Cohomology*, version 2.21, 22 March 2013, https://www.jmilne.org/math/CourseNotes/LEC.pdf: Theorem 14.9, Remark 14.10, Example 14.11 and Proposition 14.13, printed pp96–98. Freshly retrieved as `turn523991638view0` and `turn594276933view0`; the complete spectral-sequence proof, tower discussion and H1 proposition were read. The group-kernel argument in section 8 is given explicitly here.

All the listed statements and the complete proofs relevant to the indicated implications have been read. The algebraic proof and its full combination with the separately audited cup/extension bridge are awaiting the requested independent whole-proof review. No simple-root hypothesis, Vandiver converse, or unconditional Greenberg assertion is included.
