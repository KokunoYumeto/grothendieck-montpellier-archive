# Independent audit: cyclic even modules and higher poles

Date: 2026-11-21 UTC. Reviewer: GPT-6 Astra Pro, `/root/archive_kummer`; effort setting not exposed.

## Verdict

The complete current `work/multieven_pole_candidate.md` and `work/sharifi_cup_parity_bridge.md` pass this independent mathematical review relative to their stated cited arithmetic and rational-image inputs. The conditional theorem is: for an odd prime satisfying Vandiver, surjectivity of the cup product from the odd part of H^1(P,F_p) onto H^2(P,F_p) implies faithfulness of the pro-p tripod action. The argument covers several even character components, arbitrary finite positive lambda ranks and repeated roots. The cited finite computations supply the hypotheses for every odd prime below 1000.

This is a full paper-proof review, not a formal certificate, a rerun of the cited modular-symbol or Vandiver computations, or a priority claim. No conclusion for primes outside the stated hypothesis follows. The independently checked finite integral-2 calculation and the present faithfulness statement are different results.

Both files were read in full. I independently reconstructed the exact relation-space comparison, the formal scalar change and the multivariate Laurent argument, rather than inferring validity from the earlier prime-37 audit. The large Cartesian test-weight tails in the current version are sufficient to avoid every numerical denominator zero.

## ME-STRUCT: module structure and companion bases

The arithmetic group H is the exact free pro-p group covered by Iwasawa's theorem over the infinite cyclotomic field, as checked in the prime-37 audit. Ferrero--Washington applies for every odd p here because the tower is abelian over Q. Thus H is free and M=H_ab has no Z_p-torsion. The Iwasawa rank is r=(p-1)/2. Kummer duality identifies the plus part up to finite groups with the involution/Tate twist of the minus unramified Iwasawa module. The vanishing of mu makes that module finitely generated over Z_p; finite kernel and cokernel preserve this property. Therefore M+ is a finite free Z_p-module and has Lambda rank zero.

The MCS minimal generating set under Vandiver, together with the split abelianization P_ab=M_Gamma direct sum Z_p gamma, gives r minimal odd Lambda generators, one in each odd Delta character, and one minimal generator in each nonzero even character. Nakayama yields Lambda^r onto M-. Its kernel is a rank-zero submodule of a free module over the domain Lambda, so it is zero. Each even component T_e is cyclic over Lambda.

For a cyclic generator v_e, let lambda_e be the Z_p-rank and q_e the characteristic polynomial of gamma. Its reduction is (z-1)^(lambda_e): the image of the pro-p group Gamma in GL(T_e/p) is a finite p-group, so gamma is unipotent modulo p. Gamma acts invertibly, hence q_e has unit constant coefficient. Cayley--Hamilton makes the span of v_e through gamma^(lambda_e-1)v_e stable under gamma and gamma inverse. This finite Z_p span is compact and thus closed; it contains the full Lambda span of v_e. Its surjection onto a free Z_p-module of equal rank is an isomorphism. This proves the companion basis without assuming a simple-root characteristic polynomial.

Exact nonlinear Delta eigenlifts are permitted by Sharifi's Lemma 2.1. The averaging operation preserves an exact already projected abelian eigenclass. Starting in H keeps every iterate in H, and the commuting Gamma lift ensures that all the companion conjugates retain the same eigenproperty. Thus the claimed simultaneous choices do not impose an additional arithmetic splitting hypothesis.

The compact free source on the odd Gamma orbits and finitely many isolated companion lifts has exactly the required abelianization. Its map to H is Frattini-surjective and therefore onto; projectivity of free H gives a section whose closed image is again Frattini-surjective. This forces an isomorphism. The proof uses no infinite-rank Hopficity assertion.

## ME-REL: the universal presentation and exact relation quotient

The companion error E_e is a word in the actual compact basis of H and has zero abelian class. Evaluating that word in the finite free group on gamma,x_a,y_e is legitimate by the compact free universal property. It sends each companion letter to the corresponding gamma conjugate.

The displayed R_e really present H semidirect Gamma. Given images of the finite generators satisfying all R_e, the odd orbits and all companion letters determine a map from H. Gamma compatibility is automatic along the odd orbits and at every intermediate companion letter. The final compatibility in the e chain is precisely R_e. The homomorphism extends uniquely to the semidirect product. This universal-property argument establishes the whole presentation; it does not assume that the relators happen to generate a known relation ideal.

Each R_e belongs to the Frattini subgroup of the finite free group. Its gamma exponent is zero, its other odd exponents are zero, and its y_e exponent modulo p is q_e(1)=0 modulo p. The evaluated E_e is a commutator word. Thus this is a minimal presentation.

The exact relative abelianization of the free group's cyclotomic kernel is A_free, one free Lambda summand for each x_a and each y_e. Evaluation is a homomorphism from H into that kernel, so the evaluated E_e maps to zero in A_free because E_e belongs to the closed commutator subgroup of H. Consequently the image of R_e is exactly q_e(gamma)Y_e, before imposing any arithmetic relation.

The closed image of the normal relation subgroup is therefore

    R_linear = direct sum_e q_e(gamma) Lambda Y_e.

Each summand is free of rank one: q_e is nonzero and Lambda is a domain. Its image in A_free is compact and closed. Conjugation by gamma supplies the Lambda action, while conjugation by every other finite generator is trivial in this abelianization. This verifies both inclusions in the claimed image formula.

Linearization descends to a surjection

    R / closure(R^p [R,F_free]) -> R_linear/(p,T)R_linear.

The source is generated by the s defining-relator classes; the target has dimension s, where s is the number of nonzero even characters. Hence this map is an isomorphism. The target is the quotient of the image module by its own maximal-ideal multiple; it is not being confused with the image of R inside A_free/(p,T)A_free, which would be zero.

The exact nonlinear eigenlifts give a Delta action on the finite free group: map each generator to its specified Teichmuller-unit power and fix gamma. These are automorphisms and have the requisite finite order, since their inverse maps and iterates are given by the inverse and iterated scalar powers on the free generators. The quotient to P and its relative abelianization are equivariant. Therefore the isomorphism just proved labels the class of R_e by character e.

There is also a direct way to finish the cup argument without matching a particular normalization of an MCS relator. Minimal-presentation transgression identifies the relation quotient with the dual of H^2(P,F_p). Every R_e has a nonzero class. Since the odd-odd cups span H^2, evaluation by that class is nonzero on some odd-odd cup. The standard cup/relator formula, inspected in MCS, makes the matching initial odd-odd commutator coefficient nonzero modulo p. The companion part of R_e uses only gamma and y_e, so has no odd-odd coefficient. Thus the corresponding constant term of C_e is a unit. This proves the exact required numerator assertion for every e, with no relation-module freeness or asphericity assumption.

## ME-QUAD: target equations, colors and exceptional grid points

The actual-image theorem and Brown provide a continuous dense map into the weight-completed free odd Lie group. The rational Levi normalization is valid weight by weight; the commuting Delta lift then lies in the same Levi torus because its unipotent centralizer is zero. Density makes every odd linear coefficient nonzero, so the stated weightwise rational rescaling is permitted.

Parity makes each companion generator have target generator length at least two. Its exact conjugate definition gives B_(e,j)=z^j B_(e,0), z=u^(m+n). Hence the companion relation gives q_e(z)B_(e,0)=C_e. Products and p-adic powers introduce no extra length-two cross terms because all their factors have no length-one part.

The set of positive integers w with u^w a root of any q_e is finite. Restricting every test weight m to a sufficiently large ordinary integer tail excludes all such pair sums, while retaining the residue-class sequences m=a+(p-1)p^n with an interior p-adic accumulation point. Thus every division used on the numerical grid is justified.

A wrong even Delta color has zero length-two coefficient for the prescribed target residue classes. More explicitly, the quadratic equation makes its C numerator zero on the complete residue-class tail grid; the successive analytic identity theorem makes that numerator identically zero as a power series. This supplies the formal, and not merely numerical, color exclusion used later.

## ME-PF: partial fractions are a legitimate coefficient-algebra change

After one finite splitting-field extension L, every root alpha is congruent to 1 in the maximal ideal of O_L. The functions z^j/q_e(z), for 0<=j<lambda_e, form the usual space of strictly proper rational functions with denominator dividing q_e. Their partial-fraction basis consists of (z-alpha)^(-k), for all roots and all orders through their multiplicities. The change matrix is constant and invertible over L, including when roots repeat.

Applying this matrix to the finite isolated-letter subspace of the source completed tensor algebra is valid even if its entries are not integral. It is not asserted to change the pro-p group basis. It preserves assigned degree and is invertible on every coefficient space. At any fixed degree, only finitely many isolated letters occur, so multiplication by its tensor powers introduces a finite common denominator. Bounded measure coefficients remain bounded L-valued measure coefficients. The first nonzero source degree and injectivity of its coefficient representation are preserved.

The common numerator C_e is the same for all j in its companion chain. Therefore the transformed leading kernels have exactly C_e/(z-alpha)^k, rather than unrelated numerators that would require another arithmetic nonvanishing result.

## ME-ANALYTIC: first degree and exact formal embedding

The first nonzero assigned source degree d still maps only to target length at least d: odd orbit letters have length at least one and isolated even letters length at least two. Terms of larger degree cannot contaminate a length-d coefficient. Its finitely many colored ordered tilings have bounded L-valued measure coefficients. The Amice transform is injective on these measures, so a nonzero chosen coefficient has a nonzero transform.

Substitution at a finite arithmetic weight cutoff is continuous and multiplicative by integration against bounded continuous coefficient functions on the compact orbit spaces. Uniform locally constant approximation and finite Fubini justify products. This is the same valid finite-cutoff construction used in the independently checked one-even proof, not a pro-p universal property applied to a noncompact rational group.

Clearing the finitely many denominators of the length-d coefficient identity leaves a power series with a common finite coefficient denominator. It vanishes on the Cartesian residue-class tail grid. Applying the one-variable identity theorem in each variable makes it the zero series. The resulting identity lies in the fraction field of O_L[[T_1,...,T_d]][1/pi], retaining the bounded-denominator condition.

For a selected disjoint-pair pattern, put S_j=(1+T_j)(1+T_(j+1))-alpha_j. The displayed inverse substitutions are formal automorphisms of the complete (pi,T)-adic integral power-series ring: their constant terms alpha_j-1 are topologically nilpotent, and the pairs are disjoint. Group the remaining variables into B. There is an injective map

    O_L[[B,S]][1/pi] -> K_base[[S]],
    K_base = Frac(O_L[[B]][1/pi]),

obtained by viewing a multivariate series as a series in S with coefficients in the B series ring. This map does not require uniform denominator bounds on every later formal inverse in K_base[[S]]; the analytic identity has already been established before making this further algebraic embedding.

Selected denominators are powers of the individual S_j. Every other denominator has nonzero constant term in K_base: a different root at the same location gives a nonzero root difference, while a different location joins different blocks and depends on independent surviving block coordinates. These are units in K_base[[S]]. Therefore the finite rational identity embeds into K_base[[S]][S_j^(-1):j in J], whose exponents have a finite lower bound in every variable. Multivariate Laurent coefficient extraction is well-defined here, without selecting an order of iterated Laurent fields.

## ME-LAURENT: maximal patterns really separate

Select a nonzero pattern with a maximum number of even letters. Fix its pair positions and root/character colors; among those nonzero patterns choose a componentwise maximal pole-order vector k. The finite set guarantees existence. Set each selected target pair to its character's unit-coupling pair and its singletons to their source types.

A term missing a selected position, or using a different root there, has no negative exponent in that selected S variable, and cannot contribute to the coefficient of the product S_j^(-k_j). Wrong character colors vanish identically as proved above. A pattern containing all selected positions and any extra pair has larger even count and zero coefficient by the first maximality choice.

For a remaining pattern on the same positions and colors to contribute, its pole orders k' must dominate k coordinate by coordinate: analytic numerators and unit-denominator inverses can only increase exponents. The Pareto choice excludes every strictly dominating vector. Incomparable vectors also cannot contribute because at least one coordinate has insufficient pole order. A pattern with the same vector and different singleton types is excluded by its zero linear target coefficient. Thus exactly the selected coefficient remains.

That contribution is its nonzero A(B_singletons) times the restrictions at S=0 of the selected C numerators. The singleton ring injects into K_base. Each selected C stays a unit after substitution, because it was an integral unit and all substituted constant terms lie in the maximal ideal. The product is nonzero, contradicting the zero identity. If there are no even letters, the argument reduces to ordinary odd-moment separation. This covers repeated roots without requiring a simple-pole residue argument.

## ME-PARITY: the p-unit input is the required odd cup input

The parity bridge was independently checked in full. For a p-unit u of F=Q(mu_p), u/c(u) has zero valuation everywhere, including at the unique p-prime. Every complex conjugate has absolute value one. Its positive powers have monic integer polynomials of bounded degree and bounded coefficients, so only finitely many powers occur; it is a root of unity. Consequently the minus part of the p-unit quotient modulo pth powers is exactly the one-dimensional mu_p line. Nontriviality of that line follows because a pth root of a primitive pth root of unity in F would give mu_(p^2) in F.

The Kummer sequence and Vandiver identify the plus part of the p-unit quotient with H^1(P,mu_p)^+. The p-prime is principal, so passing to p-integers does not change the class group. The Brauer group of p-integers has no p-torsion: the global invariant condition has only one possible nonzero finite local summand and no real summands, forcing that invariant to vanish. Hence H^2(P,mu_p^2)=A tensor mu_p, a plus space under Vandiver.

Mixed-parity cups have zero image in this plus target. The alternating cup on the one-dimensional minus line is zero because p is odd. Thus the full p-unit cup image equals the plus-plus cup image. Untwisting the two inputs turns that plus part into H^1(P,F_p)^-, and untwisting the target gives H^2(P,F_p). The character bookkeeping a+b=e matches MCS's relation convention. No cyclotomic-unit-index hypothesis is inserted.

## ME-RANGE: what the verified literature supplies

I freshly read Sharifi, *Iwasawa theory and the Eisenstein ideal*, arXiv:math/0501236v4, Theorem 1.2 on printed page 2; Theorem 5.6 and its complete proof on pages 25--26; Theorem 5.7 and its described exact modular-symbol computation; and Corollaries 5.8--5.9 on page 27. Local primary files are `work/sharifi_eisenstein_2007.pdf` and `.txt`. Corollary 5.9 gives the full p-unit cup surjectivity for every odd p<1000, with target A tensor mu_p. Its stronger specified pairing value is not needed for the conditional theorem.

Buhler--Harvey, *Irregular primes to 163 million*, arXiv:0912.2121v2, page 1 and the Vandiver verification discussion in section 4, were freshly retrieved from https://arxiv.org/pdf/0912.2121 . They supply Vandiver throughout the required small range. Only the implication for odd p<1000 is used here, not any ancillary claim about the full structure of higher class groups or simple Iwasawa roots.

The cited computations were not rerun in this audit. Combined with the independently checked conditional proof and parity bridge, they give its stated finite-range corollary. A pro-p tripod kernel element is cyclotomically trivial, hence belongs to H; functorial rational completion sends it to the identity, and the proved injectivity on H forces it to be trivial. This is the exact final kernel implication.
