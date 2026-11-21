# Initial pro-2 kernel candidate — audit history

**Update:** the complete argument has now passed two independent whole-proof agent audits and a parent review. The clean checked proof is `work/pro2_moment_proof.md`; the remaining pending-audit language below is preserved as the historical candidate record.

Author: GPT-6 Astra Pro, `/root/tripod_integral`; 2026-11-21 UTC. **Status: proposed complete argument, not yet certified.** This file isolates the new argument so that it can be checked without importing the status of the older memo. The currently cited literature usually states the kernel theorem only for odd regular primes; that discrepancy is a reason to audit every topology and realization step carefully. Do not promote the result merely because the argument looks plausible.

## Claim under investigation

Let `P=Gal(Q_{ {2} }(2)/Q)` be the maximal pro-2 Galois group unramified at every **finite** prime other than 2; real places may complexify. Let `rho_2:P -> Out(pi_1^et(P^1_Qbar - {0,1,infinity})^(2))` be the usual tripod representation (Ihara's ramification theorem makes this factorization available). The claim is that `rho_2` is injective. Equivalently, `Omega_2^*=Omega_2` for this convention on infinity.

The proposed proof uses no Alpöge/step-17 estimate and no integral free-generation assertion about the weight Lie algebra. It uses rational Deligne–Ihara/Brown, the free-product presentation of `P`, and a moment-separation lemma.

## Primary inputs and precise scope

1. **Pro-2 arithmetic presentation.** G. Gras and J.-F. Jaulent, *Note on 2-rational fields*, J. Number Theory 129 (2009), 495–498; https://arxiv.org/pdf/0805.1168 and author's copy https://www.math.u-bordeaux.fr/~jjaulent/Articles/2-rationalFields.pdf. Theorem 2, preprint p.3, says that for a 2-rational field with `r` real and `c` complex places the unrestricted-at-infinity maximal 2-ramified pro-2 group is the free pro-2 product of `1+c` copies of `Z_2` and `r` copies of `C_2`. For `Q`, this is `P=C_2 * Z_2`. The 2-rationality of `Q` can also be checked from their definition/theorem 0: a rational number locally square at 2 and with even valuations away from 2 is a rational square; the root-of-unity rank condition is immediate. **Verified from the primary PDF:** Theorem/Definition 0(iv), pp.1–2, has exactly these local-square and valuation conditions. For Q, write a candidate as `epsilon 2^e y^2` with `epsilon=+/-1` and `e=0 or 1`; its being square in Q_2 forces `e=0` by valuation and `epsilon=+1` because -1 is not a 2-adic square. Both the global and local 2-primary root-of-unity groups are `{+/-1}`, so both ranks are 1. Theorem 2 applies with `r=1,c=0`. Browser retrievals: `turn795825468view0`, `turn253246265view1`.
2. **Cyclotomic abelianization.** Kronecker–Weber gives `P^ab=Gal(Q(mu_(2^infinity))/Q)=Z_2^×=C_2 x (1+4Z_2)`. Thus the 2-adic cyclotomic character `chi:P->Z_2^×` is the abelianization map. The order-2 factor is complex conjugation. This use includes the equality of the maximal abelian pro-2 extension unramified outside 2 with the cyclotomic tower, not merely inclusion.
3. **Rational Galois-image Lie algebra.** R. Hain and M. Matsumoto, *Weighted completion of Galois groups and Galois actions on the fundamental group of P^1-{0,1,infinity}*, https://arxiv.org/pdf/math/0006158 (version 2; local `work/hain_matsumoto_weighted.pdf`). Introduction pp.1–3 gives, for **every** prime ell, the natural continuous weighted-completion map and the identification of the weight-graded Lie algebra of the Zariski closure of the arithmetic image with the rational Ihara Lie algebra. Theorem 7.2 p.21, Theorem 7.3 p.22, Proposition 7.1 p.21, Section 8 (especially the actual-image definition §8.3 p.25, Proposition 8.3 pp.25–26, Theorem 8.4 p.26 including its density assertion, Lemma 8.5 and Remark 8.6 p.27), and Theorem 9.8 p.33 handle the Galois action, its odd generators, and the absence of weight 1 in the tripod image. F. Brown, *Mixed Tate motives over Z*, Annals 175 (2012), 949–976, https://annals.math.princeton.edu/wp-content/uploads/annals-v175-n2-p10-p.pdf, Theorem 1.1 and the succeeding paragraph p.950 prove motivic faithfulness and hence rational Deligne–Ihara. Combined, the prounipotent radical `U` of the proalgebraic closure of the tripod image has Lie algebra the weight completion of a free `Q_2`-Lie algebra on one generator `s_m` in each odd weight `m>=3`; its abelianization has one copy of `Q_2(m)` for each such `m`.

For input 3 the proof can work with the **actual proalgebraic image** of the arithmetic representation, avoiding any unproved identification of an arithmetic lattice with a motivic lattice. An audit must verify that its natural `H -> U(Q_2)` map has Zariski dense image and is continuous in every finite weight quotient. These should follow from the weighted-completion construction and its image functor; Proposition 7.1 states density for the full weighted completion before taking the tripod quotient. No faithful arithmetic map is assumed here — that is what the argument tries to prove.

4. **Finite-rank Magnus fact.** A finite-rank free pro-2 group embeds by the integral Magnus map `g_i |-> 1+X_i` into the units of `Z_2<<X_1,...,X_d>>`, with the `(2,X)` topology. It suffices to use the familiar mod-2 Magnus embedding in `F_2<<X_1,...,X_d>>`; the integral one is then injective. Inspected primary research-paper locator: J. Mináč, F. Pasini, C. Quadrelli, N. D. Tân, *Koszul algebras and quadratic duals in Galois cohomology*, Advances in Math. 380 (2021), 107569, DOI 10.1016/j.aim.2021.107569, arXiv:1808.01695v3, §5.1 p.21 equation (5.1). It explicitly asserts the monomorphism of profinite groups and the completed group-algebra isomorphism for every prime p; its cited book locations are Koch §§4.2 and 7.6. Browser retrieval `turn606220497view0`. This is a cited theorem, not independently reproved in this run.

## Step A. Put the arithmetic group in an explicit form

Write `P=<c> * <gamma>`, with `c^2=1`, `<gamma> ~= Z_2`. After replacing the infinite free generator by `c gamma` if necessary, arrange `chi(c)=-1` and `u=chi(gamma) in 1+4Z_2`; `u` is a topological generator of `1+4Z_2` because the abelianization map is an isomorphism. Such a replacement is an automorphism of the free product (its inverse makes the same substitution).

Let `P_i=ker(P -> (Z/4)^×)`, the group over `Q(i)`. Pro-2 Reidemeister–Schreier, or the direct free-product normal form, identifies

`P_i = <gamma, c gamma c>`

as a free pro-2 group on these two generators. Set `h=(c gamma c) gamma^(-1)`. The pair `(h,gamma)` is again a free pro-2 basis of `P_i`. Since `chi(h)=1`,

`H=ker(chi:P->Z_2^×)=ker(P_i -> <u> ~= Z_2)`

is the normal closure of `h` in `P_i`; `gamma` splits the displayed quotient. The cyclotomic character detects every element outside `H` in the tripod action, so injectivity of `rho_2` reduces to injectivity on `H`.

### A1. The exact profinite basis of H

Take the **unpointed compact profinite space** `X=Z_2`. Let `F(X)` be its free pro-2 group in the following sense: a continuous map `X -> Q` into any pro-2 group `Q` extends uniquely to a continuous group homomorphism `F(X)->Q`. Its universal generators are denoted `h_x`.

This is not being confused with a chosen discrete basis converging to 1. Concretely, take the inverse limit over finite continuous partitions `X -> X_j` of the finite-rank free pro-2 groups `F(X_j)`. The induced map `X->lim F(X_j)` is continuous. Any map from `X` to a finite 2-group factors through one finite partition, and this verifies the required universal property for all pro-2 target groups by inverse limits. In particular the finite-partition projections jointly separate points of `F(X)`.

Translation `x |-> x+a` gives a continuous `Z_2`-action on `F(X)`: one may restrict to the cofinal partitions `X -> Z/2^n`, on which this is an action of a finite 2-group. Form the pro-2 semidirect product `F(X) rtimes Z_2`. It is freely generated as a pro-2 group by `h_0` and the generator `gamma` of the second factor. To verify this, for any two elements `h',gamma'` in any pro-2 group `Q`, the map

`x |-> (gamma')^x h' (gamma')^(-x)`

is continuous; the universal property extends it uniquely to `F(X)->Q`, and this extension is compatible with the `Z_2` action. Thus it extends uniquely to `F(X) rtimes Z_2 -> Q`. This is exactly the universal property of the free pro-2 group on the two indicated generators.

Consequently `P_i ~= F(X) rtimes Z_2`, and the subgroup `H` identifies with `F(X)`, with

`h_x = gamma^x h gamma^(-x)` for every `x in Z_2`.

Its abelianization is therefore the completed free `Z_2`-module on `X`:

`H^ab ~= Z_2[[Z_2]]`,

the module of bounded `Z_2`-valued measures on `Z_2`, with `h_x` corresponding to the Dirac measure at `x`. Under conjugation by `gamma` this is the rank-one Iwasawa module.

**Audit point:** the inverse-limit construction of free groups above must preserve the universal property. The proof only needs that maps into finite 2-groups factor through finite partitions; if that argument is insufficient, replace the construction with the standard free-pro-2-on-a-profinite-space theorem and prove its finite-partition separation explicitly.


### A2. Equivalent finite-quotient construction (removes any reliance on free-profinite-space terminology)

One can replace all of A1 by the following explicit inverse limit. In the free pro-2 group `P_i=<gamma,h>`, let `N_n` be the closed normal subgroup generated by `gamma^(2^n)` (`n>=1`). Then

`P_i/N_n ~= C_(2^n) * Z_2`.

Its map to `C_(2^n)` sends `gamma` to the finite cyclic generator and `h` to 1. The kernel `H_n` is the free pro-2 group on the finite set `h_i=gamma^i h gamma^(-i)` for `i mod 2^n`. This follows directly from the semidirect model: a free pro-2 group on these `2^n` symbols, acted on by the cyclic group by permutation, has semidirect product with the universal property of `C_(2^n)*Z_2`. In particular no infinite-rank Nielsen–Schreier theorem is needed.

The `N_n` are decreasing and have trivial intersection. Indeed, given an arbitrary finite 2-group quotient of `P_i`, the image of `gamma` has finite 2-power order, so `N_n` is contained in its kernel for all sufficiently large n. Residual finiteness of the pro-2 group then gives the trivial intersection. Compactness supplies surjectivity as well as injectivity of

`P_i -> lim_n P_i/N_n`:

a compatible tuple of cosets gives a nested family of nonempty closed subsets of the compact group `P_i`. Passing to kernels of the maps to `lim C_(2^n)=Z_2` gives

`H ~= lim_n H_n`.

The transition maps fold the finite basis by `i mod 2^(n+1) |-> i mod 2^n`. Thus the degree-r pieces of the compatible integral Magnus expansions are exactly

`lim_n Z_2[(Z/2^n)^r] = Z_2[[Z_2^r]]`.

This independently establishes the construction and point separation needed in B. It also proves that the conjugates `h_x` topologically generate `H`: every finite quotient of H factors through some H_n, whose indicated basis is their image.

For completeness, even the index-2 basis of `P_i` can be checked without a subgroup theorem. Let the involution swap the two basis elements `a,b` of a free pro-2 group. Its semidirect product with `C_2=<c>` has the universal property of `C_2*Z_2`, by sending `a` to `gamma` and `b` to `c gamma c`. The kernel of the quotient to `C_2` is precisely that free rank-2 group.

## Step B. An integral Magnus expansion with measure coefficients

For `r>=0`, let `M_r=Z_2[[X^r]]` (`M_0=Z_2`). Form

`T_hat(M)=product_(r>=0) M_r`,

with multiplication given by external product of measures followed by concatenation of variables, and its inverse-limit topology from finite partitions, finite degree truncations, and reduction modulo powers of 2. Equivalently, it is the inverse limit of the usual completed noncommutative power-series algebras for the finite partitions `X_j`.

There is a continuous Magnus homomorphism

`theta:F(X) -> 1+product_(r>=1) M_r`,

sending `h_x` to `1+delta_x`. This follows either from the universal property into the pro-2 group of units or from the finite-partition Magnus maps. It is injective: if `theta(g)=1`, every finite-partition projection has trivial finite-rank Magnus expansion and so is 1; the finite-partition projections separate points of `F(X)`.

Therefore, for every nontrivial `g in H`, there is a least **finite** integer `r>=1` for which the degree-r component `mu_r(g)` of `theta(g)-1` is nonzero. The degree filtration here is the ordinary Magnus variable degree, not the `(2,I)` valuation. The topological completion is `(2,I)`-type, but the decomposition by variable degree is still a product. Integral multiplication by arbitrarily large powers of 2 cannot create a nonzero element all of whose variable-degree components vanish.

**Audit point:** verify the displayed product description and that tensor coefficients are `Z_2[[X^r]]`, with inverse limits over independent partitions in each coordinate. Product partitions are cofinal among finite clopen partitions of the compact product, and one common refinement of the finitely many coordinate partitions suffices.

## Step C. The rational realization and the linear moments

Let `B` be the proalgebraic closure over `Q_2` of the arithmetic tripod action on the 2-adic unipotent geometric fundamental group. Its reductive quotient is `G_m`, induced by `chi`. Its prounipotent radical is `U`; the restriction gives a continuous map

`rho_U:H -> U(Q_2)`.

By weighted-completion input 3, the image is Zariski dense. Choose a Levi splitting (Hain–Matsumoto Lemma 3.7 p.9; apply compatibly to the negatively weighted proalgebraic extension) and a weight-homogeneous free generating system `s_m` of `Lie U`, one for each odd `m>=3`. Thus the completed universal enveloping algebra is the **weight-completed** free associative algebra on these symbols. Every finite weight truncation is finite-dimensional.

Let `ell_m:U(Q_2)->Q_2(m)` be the m-th abelianized coordinate; equivalently it is the coefficient of the generator `s_m` in `log(u)` or in `u-1`. For the latter two, the coefficient agrees in generator length 1. The coordinates are continuous group homomorphisms on `U`, and conjugation by a lift with cyclotomic character `v` acts on them by multiplication by `v^m`.

Set `a_m=ell_m(rho_U(h))`. Then for all `x in Z_2`,

`ell_m(rho_U(h_x)) = a_m u^(mx)`.

Moreover `a_m != 0` for every odd `m>=3`. Indeed, if `a_m=0`, the displayed formula makes `ell_m` vanish on every universal generator `h_x`, hence on all of `H` by continuity and topological generation. This contradicts the Zariski density of `rho_U(H)` in `U` and the nonzero m-th abelian quotient of `U`.

This proves the needed nonzero linear moments without assuming an integral primitive Soulé normalization, without dividing by a possibly nonunit integer inside `Z_2`, and without asserting that the actual integral image lattice is free on odd elements. Only `a_m in Q_2^×` is needed.

**Audit points:**

- Proalgebraic closure must be taken in the rational unipotent tripod automorphism group; explain why an element trivial in the pro-2 outer action is trivial in this rational action.
- Input 3 must give an actual prounipotent radical with the indicated free **completed** Lie algebra, not just a graded abstract isomorphism. A characteristic-zero Levi splitting and completeness should supply this from the graded statement.
- The arithmetic map from `P` exists because the original pro-2 action factors through `P`, not because `G_Q` itself is pro-2. The rational action is induced from the pro-2 action.
- On abelianization, conjugation by `gamma` is exactly `u^m`; any unipotent part of the lift acts trivially on this quotient. No diagonalization over `Z_2` is claimed.

## Step D. Lowest Magnus degree gives multivariate moments

Suppose `g in H` lies in `ker rho_U`, and suppose for contradiction that `g != 1`. Let `r` be its first nonzero Magnus degree and `mu=mu_r(g) in Z_2[[X^r]]`, as in Step B.

Write `Y_x=rho_U(h_x)-1` in the weight-completed free associative algebra. Its constant term is zero; its part of generator length 1 is

`sum_(m odd>=3) a_m u^(mx) s_m`.

Substitution `delta_x |-> Y_x` sends `theta(g)` to `rho_U(g)`. This can be justified coefficient by coefficient in each finite weight quotient. The relevant matrix coefficients are continuous functions of `x`; compactness makes them bounded in `Q_2`; integrals against a bounded `Z_2` measure therefore converge. At weight at most `N`, only the finitely many Magnus degrees `d<=N/3` can contribute, so no interchange of an uncontrolled depth series and a weight series is required. The universal property on the generators determines the resulting group homomorphism uniquely.

Because all Magnus terms of degrees less than `r` vanish, and each `Y_x` has positive generator length, the coefficient of the ordered word `s_(m_1)...s_(m_r)` in generator length `r` is exactly

`(a_(m_1)...a_(m_r)) * integral_(Z_2^r) u^(m_1 x_1)...u^(m_r x_r) dmu(x_1,...,x_r)`.

Higher Magnus degrees cannot contribute to generator length `r`. The order of the variables is retained — this is a noncommutative word coefficient, not a symmetrization. Since `rho_U(g)=1` and all `a_m` are nonzero, all these integrals vanish as `(m_1,...,m_r)` ranges independently over the odd integers at least 3.

**Audit point:** multiplication/substitution on the completed tensor algebra needs a direct continuity argument if the `Y_x` coefficients are not all integral in one global lattice. Finite weight suffices: choose a stable lattice in the finite-dimensional target under the compact image, or simply integrate the finitely many bounded coefficient functions. The proof does not require a single lattice uniform in all weights.

## Step E. Bounded measures are separated by the odd-weight grid

For any bounded `Z_2`-valued measure `mu` on `Z_2^r`, define its Amice transform

`A_mu(T_1,...,T_r) = integral product_j (1+T_j)^(x_j) dmu`.

The binomial coefficient expansion shows that `A_mu` lies in `Z_2[[T_1,...,T_r]]`. It converges whenever every `|T_j|_2<1`. The transform is injective: its coefficients are the moments against products of binomial polynomials, which form the multivariate Mahler basis of the continuous functions on `Z_2^r`. If all coefficients vanish, the measure vanishes. One can instead use the usual isomorphism `Z_2[[Z_2^r]] ~= Z_2[[T_1,...,T_r]]` sending a Dirac measure at x to `product(1+T_j)^(x_j)`.

For an odd integer `m>=3`, put `t_m=u^m-1`. As `u in 1+4Z_2`, all these points satisfy `|t_m|_2<=1/4`, strictly inside the radius-1 convergence disc. The set has an interior accumulation point: for `m_j=1+2^j` (`j>=1`) we have `m_j` odd and at least 3, and

`t_(m_j) -> u-1`.

They are distinct because `u` has infinite order (equivalently `log u != 0`). Thus a one-variable power series convergent on the open unit disc which vanishes at all `t_m` is identically zero: restrict to a closed disc of radius `1/2` containing these points and their limit, or translate about the interior point and use the ordinary nonarchimedean identity theorem.

The vanishing moments in Step D say

`A_mu(t_(m_1),...,t_(m_r))=0`

for every tuple of odd integers `m_j>=3`. Applying the one-variable identity theorem successively proves `A_mu=0`: fix grid values in variables 2 through r and conclude the series in variable 1 vanishes; then hold an arbitrary value of variable 1 in the disc fixed and apply the theorem in variable 2; continue. Alternatively apply the theorem to each coefficient after expanding in variable 1. Hence `mu=0`, contradicting Step B.

It follows that `rho_U` is injective on `H`. The pro-2 tripod action has kernel contained in `H` because its action on abelianization records `chi`. A pro-2 kernel element is trivial under the rational action, hence trivial under `rho_U`, hence 1. This would prove the claim.

## Checklist for independent whole-proof audit

The argument is deliberately reduced to five concrete issues; the analytic one appears elementary once its hypotheses are satisfied.

1. Does the exact arithmetic presentation with cyclotomic abelianization identify `H` with the free pro-2 group on the **compact** profinite orbit `Z_2` as asserted? Is the semidirect-product universal-property proof sound?
2. Does the finite-partition Magnus construction give an injective expansion with a first finite nonzero degree for every nontrivial `g`? In particular, is a subtle closure difference between powers of the augmentation ideal and the stated product grading relevant?
3. Does rational Deligne–Ihara plus Hain–Matsumoto provide the **actual continuous arithmetic image map** into a prounipotent group with completed free Lie algebra and all nonzero abelian coordinates, at ell=2? Are any comparison maps only isomorphisms after taking a graded object in a way that obstructs the completed free model?
4. Does the coefficientwise substitution correctly preserve lowest **generator length** even though the target is completed by **weight**, and despite denominators growing with weight? The finite-weight argument is intended to settle both.
5. Does the odd-grid analytic identity theorem separate bounded measures? The points lie in `4Z_2`, have accumulation at `u-1`, and the transform is analytic on the whole open unit disc, so this should not merely be a density assertion in the wrong topology.

No assertion of novelty is made. If all steps survive, search for an existing equivalent proof before advertising a new theorem; if one fails, record the exact failed implication and retain the correct p=2 status as unresolved in this run.


## First self-audit, 2026-11-21 00:33 UTC

Read the entire argument A–E from its statement, checking each dependency. No contradiction or fatal gap identified in this reading. The finite-quotient alternative A2 provides a direct repair for the most delicate presentation issue; it should be used in a final exposition. Primary input statements and the relevant proofs of Hain–Matsumoto Proposition 8.3 and Theorem 8.4, Lemma 8.5, plus Appendix A.6/A.9/A.10, were read; Brown's theorem is cited and not reproved. Gras–Jaulent Theorem/Definition 0 and Theorem 2 were read and the Q specialization checked directly. The finite-rank Magnus theorem was checked at the stated primary paper locator, not reproved. Independent audit by `/root/archive_kummer` remains pending. This is a genuine proof check event but not a claim of independent verification.
