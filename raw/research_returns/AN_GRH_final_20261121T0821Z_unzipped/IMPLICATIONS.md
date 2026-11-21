# Implications for the anabelian and Galois programme

Date: 21 November 2026. Analytic convention: **A** is the stipulated Alpöge Dirichlet-GRH theorem. **M** is Masullo's all-number-field Hecke-GRH draft claim. Every M-dependent conclusion remains conditional on M. The checked deductions below do not constitute a verification of M.

## 1. Cote 149 and A1

**A1 itself is proved without A or M** in Finding A05, by a checked reconstruction of ANABELIAN_A1 A.2–A.5, A.14–A.19 and A.30–A.33. Its exact scope is rational-point injectivity for a smooth geometrically connected hyperbolic curve over a field finitely generated over its prime field. In characteristic p, the geometric fundamental group is completed away from p while the entire arithmetic Galois quotient is retained. This is not section surjectivity, a full higher-dimensional Hom theorem, or a theorem for the prime-to-p completion of the entire arithmetic group.

For cote 149 scans 33–36, A01 identifies the finite-field covering formulation: equality of sections is equivalent to the stated condition on compatible pointed covers and p-primary Jacobian differences, with all constant extensions allowed. A05 settles the curve point-separation question stated in scan 36. Scans 37–38 supply the surrounding generalized-Jacobian geometric context. The displayed maps (*) and (**) begin before the supplied pages; their missing original text has not been invented.

The decisive new ingredient in the recovered proof is preservation of the relative cuspidally pro-r configuration fibre, followed by arithmetic point-count transport, a finite exceptional-set theorem, and an integral Kummer difference cocycle. It uses finite-field trace and weight results, not a number-field analytic hypothesis. The full proof, including specialization and the open genus-zero/genus-one cases, is in the paper. Whole-proof readers and their exact scopes are recorded in CHECK_EVENTS.tsv.

### What happens to route 2

A02 gives exactly the Hooley consequence of M: GRH for the Dedekind zeta functions of Q(zeta_n,2^(1/n)), for squarefree n, yields the usual positive primitive-root density and asymptotic. The fields are generally nonabelian; Q(zeta_3,2^(1/3)) already has group S3. The stipulated Dirichlet theorem does not supply this family.

A03 proves the sufficient genus-two characteristic-two geometric criterion. A04 refutes the density inference that would combine arithmetic primitive-root primes with an arbitrary positive-density theta-support set. A06 gives a stronger, explicit obstruction: on the recovered B.23 curve over F_(2^38), **no prime ell with 2 primitive modulo ell has a nonzero theta point of order ell**. Its proof reduces to the six primes 191, 229, 419, 457, 571, 647; only 419 is primitive-root compatible, and three ordered pairs in the mandatory orbit have the same nonzero difference, contradicting the genus-two difference bound.

This disproves a universal geometric bridge that the proposed Hooley route would require in its simple form. It does not disprove A1. The example has p-rank zero and is already handled by ordinary Kummer theory. A route that first handles zero-rank curves separately would still need a new incidence theorem on the positive-rank locus; that theorem is not supplied here. **No proof of A1 through Hooley is claimed.** The unconditional cuspidal proof settles A1 by another route.

The stronger recovered B.23 theorem excludes every nontrivial odd cyclic etale cover with zero primitive p-rank on that example. Its complete conductor and polynomial certificates passed replay. B.24, which allows degree one, remains a separate open problem for positive-p-rank curves. A05 does not imply that every sufficient covering criterion is universally realizable.

### The strengthened positive-rank analysis

A07 separates the generic-field and finite-field questions. Ozman–Pries Theorem 1.1(2), equivalently Theorem 8.3, supplies a geometric generic genus-two curve in either positive-rank stratum whose theta divisor contains no odd prime-order point. Finite-coefficient descent makes this a counterexample over a field finitely generated over F2. Its moduli are transcendental; it is not a finite-field counterexample. For the ordinary generic curve, Yang Theorem 3.5, with zero ramification divisors, excludes all nonzero odd-order theta points.

A08 turns each prescribed finite list into a finite-field obstruction by spreading the generic curve and removing finite closed incidence loci. For rank one or two, no fixed finite list of primes suffices for every curve over finite extensions of F2. In the ordinary case, the same argument avoids all nonzero n-torsion for any finite list of odd integers n. The source credit is ANABELIAN_SUCCESSOR A.16 for the ordinary finite-prime-list obstruction. The fixed-rank-one and explicit relative-theta formulations are included here with full proofs. The exact Grothendieck framework is EGA IV3, Theorems 8.8.2 and 9.7.7, and EGA III2, Theorems 7.7.5(I) and 7.9.4. The finite-field extension may depend on the list; no interchange with a single curve avoiding every order is made.

A09 verifies a positive example from ANABELIAN_A1 B.39 (working label B.LIT7) with a new principal-divisor certificate. On C: Y²+X²Y=X⁵+X, an explicit F16-point R satisfies div(F)=13(R−P) for the displayed function F. The cover W^13=F is pointed over F16 and has constant cyclic deck group over F4096. The curve has rank one, #C(F2)=#C(F4)=4 and #J(F2)=8. Thus its four rational points have equal prime-to-two abelian Kummer classes, while the covering argument separates their full point-section classes. This precise Kummer model is not asserted to equal the older Lang-cover arithmetic model.

A10 shows that order three can never supply such a witness on a nonordinary genus-two curve. A11 proves that the sufficient incidence condition can nevertheless be weakened: an exact theta order n=ell^r and <2,-1>=(Z/n)^× suffice. The zero Frobenius arrows at a class and its inverse kill every primitive-character orbit; the prime-power condition identifies that primitive part with the whole final degree-ell Prym. Its rank zero then gives the degree-two-pencil contradiction for a proposed collision. This is a strictly smaller sufficient gate than requiring a primitive-root prime.

The tested projection approach uses Poonen Theorem 1.8. It supplies theta order ell^r m with the chosen ell-primary component and with every prime of m outside a density-one set. It does not make m=1. Multiplication by m need not preserve theta; an intermediate cover retains proper-conductor blocks. On a nonordinary base with ell=3 and r=1, A10 proves that m must actually be greater than one. These are limitations of the projection and intermediate-cover strategies.

**A15 gives a further, strictly weaker geometric gate for rank-one genus-two bases.** A primitive factor of rank zero at any odd cyclic degree is sufficient; the proper-conductor factors may have positive rank. The proof refines recovered ANABELIAN_SUCCESSOR final A.14, working identifier AC.11. A product of deck operators gives a low-degree separable function, and Poonen's Castelnuovo–Severi consequence forces a separable elliptic double quotient if two point sections collide. Deuring–Shafarevich excludes that quotient in rank one. The same criterion applies to any genus-two base independently known to have no separable elliptic double quotient. The strongest equivalent incidence condition is that theta meet every primitive doubling orbit in one cyclic torsion subgroup. A single theta point suffices when <2,-1> is the full unit group, but that single-point condition allows at most two distinct odd prime factors.

A16 makes the distinction concrete. On the stated rank-one curve over F8, an exact norm identity gives a point of order 15. Its degree-15 cover has genus 16 and 2-rank 7: the primitive factor has rank zero, whereas the conductor-3 and conductor-5 factors have ranks 2 and 4. A15 separates point sections despite those surviving factors. The example does not assert that its base lacks a prime-power witness. A separate degree-five comparison is also proved.

**A18 removes the geometric elliptic-double-quotient exception, and works in every genus at least two in characteristic two.** In the exceptional case, the cover must be the actual pullback of an odd cyclic isogeny of a genus-one curve along a separable double map from the base curve. If that double map has r geometric ramification points, Deuring–Shafarevich gives f(D_m)=2f(E)−1+mr for every intermediate cyclic degree m. Conductor decomposition and Möbius inversion force the primitive rank to be r·phi(n)>0. This contradicts the assumed geometric primitive rank zero. In genus two the whole new factor in the exceptional diagram is ordinary, so even a rational primitive 2-primary group of zero together with a nonordinary primitive factor suffices. A rational torsion condition alone retains its distinction. The universal genus-two gate is now theta coverage in one cyclic subgroup of any odd order, with no elliptic-quotient exclusion. The one-dimensional theta-arrow argument is not extended to higher genus.

A12 gives an unconditional finite-field test: for H contained in J(F_Q), with index a, the number of theta points in H is at least the nonnegative part of ceil((Q+1−floor(2(a+1)sqrt(Q)))/a). A13 applies it to the ordinary curve y²+y=x+x⁻¹+(x−1)⁻¹ and obtains at least four exact-order-4159 theta points over F128. Here #J(F128)=4·4159, and 2 has order 2079, so adjoining −1 generates the full unit group. A14 proves that this sufficient test cannot eventually succeed by extending constants at one fixed odd prime. It does not assert that theta torsion disappears. The recovered Successor A.10 rational prime-cover criterion has a distinct cofactor inequality and the stronger primitive-root hypothesis; A12 is not asserted to optimize it.

Under M, A17 proves that the primes q congruent to 5 modulo 8 for which 2 is primitive have natural density Artin constant/2. Every corresponding composite order n=3q satisfies <2,-1>=(Z/n)^×. The exact analytic family is the Kummer Dedekind zeta functions already used in A02; Lenstra Theorem 3.1 and Section 3.2 handle the fixed congruence condition. This is an arithmetic supply of candidate orders. No theorem in the package places a theta point of such an order on every positive-rank finite-field curve. Poonen's projection theorem bounds a density contribution from the extra prime factors, not their number, and does not force its cofactor to be one of these primes.

A19 makes the remaining search effective for each fixed finite set S of odd prime factors. If d makes Q-power Frobenius^d act trivially on J[ell] for all ell in S, every geometric S-primary theta point is already rational over F_(Q^d). One explicit choice is the least common multiple of the orders of GL4(F_ell). The proof isolates a prime component of any purported nonrational point and produces an entire odd translation orbit on theta; a genus-two theta curve meets any nonzero translate in at most two geometric points, giving a contradiction. The complete intersection is therefore found by a finite Jacobian computation. This controls all exponents at once, with no assertion of practical running time or universal successful support.

A20 proves an exact obstruction beyond order three. For the rank-one curve of A09, the Frobenius polynomial divides T^20−1 modulo 3, while #J(F_(2^20))=1099812538656 has 3-adic valuation four. Its rational 3-primary group is therefore exactly J[3]. A19 and A10 imply that theta contains no nonzero geometric point of any order 3^a. The curve's order-13 witness remains valid. Thus a fixed-prime-power repair at 3 cannot settle the universal positive-rank incidence problem.

A21 extends generic avoidance to **every nonzero odd order on both positive-rank strata**. The full symplectic images at different odd primes are independent by the simple-quotient and Goursat argument. Transitivity on points of exact order n would make a single theta point bring an entire odd translation orbit into theta, violating the intersection bound. Every connected odd cyclic cover of the generic curve consequently has ordinary whole new factor. This is a generic-field statement, with no interchange of an infinite collection of opens and one finite-field specialization.

A22 gives the corresponding stronger finite-field obstruction for each **fixed finite prime support S**, allowing every exponent and mixed product. With N the product of S, first avoid J[N] on a nonempty moduli open. A full level-N² torsor and an explicit affine Frobenius twist realize a fibre on which Phi−I is ell times an invertible matrix for every ell in S. Its rational S-primary subgroup is exactly J[N]; A19 then captures all geometric S-primary theta points there. These avoidance curves occur in every nonempty open of either positive-rank stratum. The field and curve depend on S. Thus no finite pool of primes, even with unlimited exponents, can serve uniformly. The framework is the relative Picard scheme and finite etale level torsors of SGA1 V4.1 and IX6.1, with effective affine descent and unconditional finite-field Lang–Weil.

A23 closes another universal numerical strategy negatively. For the ordinary A13 curve overF4, write Q=4^m and let e_m=Q+1−t_m, where t_0=2,t_1=1,t_m=t_(m−1)−4t_(m−2). Then #J(F_Q)=e_m² and #C(F_Q)=2e_m−(Q+1). Every prime divisor ell of #J divides e_m, so ell*#C(F_Q)<2#J(F_Q) for every m. This contradicts the first size inequality of recovered ANABELIAN_A1 B.3 at every extension, independently of any primitive-root requirement. Yet the order4159 theta witness persists overF_(4^7). A prime-factor theorem therefore cannot make this specific sufficient test universal. It does not refute A12 or direct geometric incidence.

A24 identifies a necessary arithmetic restriction for the ordinary A13 curve. Every actual eligible prime-power theta order lies over a prime splitting in Q(sqrt(-15)) or one of its ramified primes3,5. The signed Frobenius orbit in an unramified quadratic torsion module would otherwise exceed the genus-two difference bound. Under M, the split candidates still have density72*Artin_constant/95 for the signed-doubling condition, or48*Artin_constant/95 for2 itself primitive. These are explicit surviving candidates, not a sufficiency theorem for theta incidence. The exact4159 witness belongs to the split classes.

A25 sharpens the numerical Lang gate. For primitive2 primes, a successful prime-level test has rational r-torsion rank at most2 once r>=11 (or r>=17 forG[3r]); under signed doubling the cutoffs are29 and41. A larger rational subspace would force mu_r to be rational by the principal-polarization Weil pairing, making Q exponentially large relative to r and defeating the required subgroup-size inequality. Thus rationalizing all r-torsion does not force the test. In the remaining rank-two case the prime must be at least on the Q^(3/4) scale, improved by at most factor9 when adjoining3-torsion. The checked primitive-divisor and greatest-prime-factor results do not provide this size together with the order condition on2; their exact scopes and quantitative shortfall are recorded in evidence/LANG_ARITHMETIC_GATE.md.

A26 removes the pair-count inequality from a separate rational criterion when the point count is even, as it is for every rank-one genus-two curve: for primitive2 prime r, |J(FQ)/rJ(FQ)|>#C forces a prescribed-point quotient witness. A27 shows that this numerical improvement is still not universally forceable. Its explicit rank-one F4 curve has |J(F_(4^m))/rJ|<#C(F_(4^m)) for every m and every primitive2 prime. The proof covers all extension degrees, rather than extrapolating a search, and does not rule out the covers themselves.

**A29 strictly improves the prescribed-point canonical-class gate without any GRH assumption.** The prime criterion is the already-proved successor final A.26, cited and whole-read as A28. Put kappa_P=[K_C−2P]. It is now enough that kappa_P have a nonzero r-primary component for an odd r distinct from the characteristic p with even ord_r(p); it need not survive in J(k)/rJ(k). A detecting cyclic r^a quotient has all faithful character L-values prime to p. Their product is the rational order of the top-step Prym, which gives point separation by the free odd-deck argument. On the actual A09 curve, after rationalizing a13-division point of the canonical class at its order13 point, every prime-level canonical detector fails while A29 still supplies a13^a witness. This proves strictness of the criteria on a curve, without claiming failure of every actual prime cover.

The canonical residual is explicit: this detector does not treat classes supported on p and odd primes at which p has odd multiplicative order; prime2 in odd characteristic is separately outside its odd-deck hypothesis. In characteristic2 it includes Weierstrass points and points with purely2-primary canonical class. Constant extensions cannot alter the finite order or primary support of that fixed class. Other geometric or rational covers may still work. A29 is an additional route to the prescribed-point cover required in cote149 scans35–36, not a universal Hooley incidence theorem.

A30 closes the proposed direct higher-genus symmetry repair negatively. On a genus-three rank-one curve overF4, a detecting cubic quotient has even relative class number; its reduced character polynomial has a genuine quadratic term. This refutes the rule that every detecting quotient works. It does not exclude other covers. The tempting unramified2-cover that moves one genus-two branch point to a non-Weierstrass point is also unavailable in the pro-odd fundamental group, and descended odd characters kill the relevant lifted difference.

A31 supplies an exact geometric witness on the very curve used in A27. After an explicit change of coordinates, F=(X+u)Y+X has norm (X+1)^7 and divisor7(R−W). The exact differential dX/X² identifies B on the Frobenius twist, and <2,−1>=U7 supplies the rank-zero new factor. Thus this curve's numerical failures do not hide an absence of actual covers. Moreover #J(F4)=28 shows that all six original rational points remain outside A29's canonical detector after every constant extension, yet the geometric7 cover can be pointed at any of them after a finite extension. This is an exact residual-case example, not a universal incidence claim.

A32 gives an exact rational witness with a geometrically ordinary new factor: the A27 curve overF256 has a split constant13cover, new dimension12, and reduced numerator1+T4+T12. Its relative class number is odd exactly over constant extensions whose degree is not divisible by7. This clarifies the distinction between rational units and geometric rank0 and does not enlarge the universal existence claim by itself.

**A33 reduces the characteristic-two genus-two point-section part to ordinary genus-two curves with integral Rosati-invariant real multiplication by O_(Q(sqrt5)).** For any cyclic5cover, the reflection quotient has genus2 and its Jacobian squared is isogenous to the Prym. Irreducibility of Phi5mod2 forces new rank0or4. The ordinary alternative carries T=v_*sigma v* with T²+T−1=0 and T†=T. Two quotient maps applied to one common lifted section collision separate the two lifts. This is a genuine reduction of the point-section assertion; it does not settle the literal primitive-cover questions ANABELIAN_A1 B.24/B.5/B.32, and it does not reduce higher-genus A1 to genus2.

**A34 strictly enlarges the rational cyclic-cover test.** If n is the odd cover degree and M is the actual exponent of the rational2primary Prym group, n>(2M−1)^2 suffices in genus2. The proof combines the cited Poonen controlled-field bound with a new cyclic four-point/wild-different endgame. An actual A27 cyclic19cover overF_(64^7) has rational2primary group(C2)^18. Its even relative class number fails the unit test for this cover, while M=2 satisfies19>9. Two independent arithmetic implementations agree on all60rational point images at the definingF64 level. The coarse Weil bound for M is redundant against recovered B.3; no analytic theorem here forces the required actual exponent.

**A35 makes the pure2canonical residual set finite over an explicit small extension.** All geometric2primary Raynaud theta points are rational over the field fixing geometricJ[4]. Its degree is at most2 in rank1 and at most6 in rank2 (the degree4 case means a common degree6field is not valid in general). A common degree12field always works. On A33’s ordinaryO5 targets the degree divides6, so Fq6 suffices. Since kappa_R=−2[R−B], this captures every pure2canonical residual point and every purely2primary hyperelliptic-pair difference. It does not control arbitrary point differences or residual odd-primary support at primes where2has odd order.

The separate constant-twist route in recovered ANABELIAN_A1 B.28–B.29 was also read in full. It provides a rational relative-class-number witness for some split base point, without Artin's conjecture in genus two. It does not prescribe that point. The retained audit checks why applying its good-point density estimate on a further cover does not force a good point in the chosen fibre, and why translating the Abel base point changes the Frobenius twist. For curves on which the alternative large-Jacobian-prime-factor criterion is numerically possible, it still retains its actual factorization and primitive-root conditions. A23 proves that universal success of that numerical criterion is impossible.

## 2. Which original rows change analytic status

The required row tables preserve every supplied flag and every recovered register entry. The canonical detailed classification is ROW_ANALYTIC_LEDGER.tsv, with 108 curated entries. ROW_FULL_REGISTER_AUDIT.tsv retains all 800 recovered statements, original statuses and declared dependencies. An original status label is metadata, not an independent proof certification.

| Rows or family | Finding or source | Consequence |
|---|---|---|
| ANABELIAN_A1 A.1; A.31–A.33 | A01, A05 | Point injectivity and its covering formulation hold without number-field GRH. The later A1-successor proof files are still unavailable. |
| Intake §3.3(3), §5(a), route 2 | A02–A04, A06–A35 | Arithmetic primitive-root density and the explicit composite candidate family follow conditionally on M. The universal simple theta bridge is false. An arbitrary odd primitive-rank-zero cover suffices in characteristic two; genus-two incidence is a finite exact test for each finite prime support, but a successful support must depend on the curve: A22 rules out every fixed finite pool. A23 separately rules out universal forcing of the older prime-quotient size test. |
| ANABELIAN_SUCCESSOR A.16; ANABELIAN_A1 B.39 / B.LIT7 | A08; A09; A21–A22 | Finite-list avoidance is made explicit and strengthened to all odd orders generically and every fixed finite prime support over finite fields, including fixed rank one; the rank-one degree-13 example receives a new exact divisor certificate. |
| ANABELIAN_SUCCESSOR final A.14 / working AC.11 | A15; A16; A18 | Rank one automatically excludes the exceptional elliptic double quotient; A18 removes that geometric exception in characteristic two in all genera. The arbitrary odd primitive-factor criterion permits positive-rank proper-conductor factors, as the exact degree-15 example verifies. The rational-only hypothesis remains separately scoped. |
| ANABELIAN_SUCCESSOR A.10–A.11 | A12–A14; A25 | An explicit geometric pure-primary theta test and an ordinary witness are proved; a fixed-prime limitation is identified. The distinct source rational-cover criterion retains its own factorization and primitive-root hypotheses. |
| ANABELIAN_A1 B.3, formula(B.CL.2) | A23 | Its sufficient inequality cannot be forced universally: an ordinary curve violates it over every constant extension while retaining a valid theta witness. |
| ANABELIAN_SUCCESSOR A.26; ANABELIAN_A1 B.13–B.14 | A28–A29 | The prime canonical criterion is credited and rechecked. A29 replaces nondivisibility modulo r by a nonzero r-primary component using a prime-power top Prym; actual-curve strictness is proved. Residual canonical supports remain open for this construction. |
| ANABELIAN_SUCCESSOR A.10,A.35; ANABELIAN_A1 B.2 | A26–A27 | Even augmentation removes an extra pair-count hypothesis, but the new sufficient size test still fails over every extension on an explicit rank-one curve. |
| ANABELIAN_A1 B.28–B.29 | Checked source and pointing audit | The unspecified-base-point rational twist theorem is unconditional; its prescribed-point conversion remains unproved. The good-point density estimate alone does not force a point in a chosen lifted fibre. |
| ANABELIAN_A1 B.5, B.24, B.32; ANABELIAN_SUCCESSOR A.15, A.96 | R03 and source-specific gates | Prescribed-point witness, degree-one-permitted primitive-cover, and remaining minimum problems are not closed by A or M. |
| ANABELIAN_SUCCESSOR A.38 | R03 | Finite-field Chebotarev controls closed parameter points, not prime-order torsion with conditions on all nonzero multiples. |
| LM7 A.25 | G05.1 | Its arithmetic progression predicate acquires an explicit prime bound under A, including finite exclusions. The missing original pro-three proof is not thereby verified. |
| LM7 A.16 | G05.2 | The noncube predicate acquires an explicit prime bound conditionally on M, via the degree-18 field Q(zeta_9,cuberoot(3)). |
| LM8 C.30, D.1, D.58 | G01, row ledger | Quantitative versions use cyclotomic fields and fit A. Original qualitative existence was already unconditional. |
| LM8 A.16; B.20, B.22; D.3, D.8, D.11, D.28, D.44, D.48, D.60–D.71, D.73, D.78–D.87, as individually listed | G01–G03 and exact row fields | Finite-stage least-prime bounds follow conditionally on M after specifying the actual image field and excluded places. No uniform tower-depth or Hilbert-specialization bound is inferred. |
| LM8 A.32–A.33 | G06; G-LOMBARDO; G-MW1 | Their actual factors F_(±6): y²=x³−3x±6 descend to Q. Existing qualitative openness and the stated adelic-index bound are unconditional. Under M, the mod-ell Q-image is full for ell>964 log6+5760; its restriction to L has index at most[L:Q]. |
| LM8 A.46–A.48; D.25 | Source crystalline comparison; Faltings finiteness | These are not finite Faltings–Serre tests, and do not become effective height/point bounds through GRH. |
| LM8 A.69; S6_SERIES_GRIND maps:src:F.2.36 | R02 | RH means Riemann–Hurwitz in the first; the other excerpt reports GRH=false. Neither identifies a conditional theorem newly discharged by A. |
| Intake D.30–D.31 | U04 and row ledger | Finite ramification, local-section/modularity premises and finite cusp-label exclusion remain separate gates. |

The table above is an overview, not a replacement for the row-level conditions. In particular a range label does not assert that every intervening row has the same direct analytic input. The TSV files give exact IDs, finite objects and hypotheses.

## 3. Finite gentle GT levels

Bach's cited **Theorem 3** supplies the general coprime-generator bound **p < 3(log N)^2** under Dirichlet GRH. The coefficient 2 in his Theorem 2 permits a nonunit witness. T01 corrects that attribution; it does not assert that the stronger numerical coefficient-2 unit-generation property is false.

T07 records the corrected LLS v3 Theorem1.1 criterion B(N)<(sqrt(2)−1)logN and proves that it suffices for every integer N≥exp(300), under A. Exact interval checks show why the displayed LLS expression does not give a uniform coefficient2 simply by checking N<3000. They are evaluations of a bound, not counterexamples to actual generation. The huge remaining interval has not been checked.

T03 proves coefficient-2 prime-generator bounds elementarily for every N=2^a3^b and every N=5^b. T05 supplies exact unconditional certificates at 53 explicit moduli, with 4,825 literal unit words, checked by a separate read-only verifier and exact rational logarithm intervals.

T04 maps actual source definitions to scalar precision: the LM7 homology cusp has order 12j; selected refinements have scalar precision 72, 144, 288, 360 or 576 as individually described; LM8 C.14 uses multiplier 24; C.18 uses 15; C.33–C.38's scalar correcting character has exact conductor p^(k+1). Matrix levels, orders of finite targets, relative coefficient depths and multiplier moduli are not interchangeable. LM8 C.49's frame computations at 24/60 are on multiplier one.

T02 states what such certificates prove: generation of a subgroup image or testing a known homomorphism/character of U_N. They do not certify the f-coordinate, cycle equations, pentagon or a compatible profinite lift. The supplied LM7 E.58/E.65 example is carried with its recorded verification limits: Delta is nonzero on ker(lambda), and ker(Delta) is proper despite having the same full cyclotomic image. Bach certificates cannot settle that noncyclotomic distinction.

## 4. Effective number-field consequences, with constants

Bach–Sorenson Theorem 5.1 gives a degree-one prime with prescribed finite Galois conjugacy class and norm at most

    B(L) = (4 log |D_L| + (5/2)[L:Q] + 5)^2.

The selected theorem needs RH for zeta_L and zeta_Q; it does not assume Artin holomorphy. For a finite excluded rational-prime set S, set m=rad(2 product(S)) and replace L by L(sqrt(m)). This forces the selected prime outside S and 2. A supplies these assumptions for abelian L/Q; M supplies them for arbitrary L, conditionally.

G03 proves a full adic semisimplification test. For integral rank-d representations over a coefficient DVR with residue field size q, unramified outside S, put

    N = 2(q^(2d^2)-1),
    B(d,q,S) = [4((N-1) log m + N log N) + (5/2)N + 5]^2.

Under M, equality of their exact Frobenius traces at every p not dividing m with p ≤ B(d,q,S) is equivalent to equality of their full trace functions and hence to isomorphism of semisimplifications. G04 shows explicitly why arbitrary extension classes are not determined. The construction uses the representation-generated algebra modulo its own uniformizer multiple, not entrywise matrix reduction.

For non-CM E/Q, Mayle–Wang Theorem 1 gives surjectivity modulo ell whenever

    ell > 964 log rad(2 N_E) + 5760.

For non-CM E1,E2/Q that are not Q-isogenous, their Theorem 2 gives a good trace-distinguishing prime

    p ≤ [482 log rad(2 N_E1 N_E2) + 2880]^2.

The two Mayle–Wang numerical statements are conditional on M in this report. The qualitative open-image and isogeny theorems were already unconditional. No uniformity theorem for all elliptic curves, CM curve or higher-dimensional abelian variety is inferred.

For the actual LM8 A.32–A.33 factors F_(±6):y²=x³−3x±6, G06 checks non-CM by ordinary reductions at5and11, and computes rad(2N)=6. Thus the stated Q-bound is explicitly ell>964 log6+5760. For their field L, restriction gives image index at most[L:Q], rather than necessarily full GL2.

Lombardo's published Corollary9.3 supplies the unconditional general-number-field bound, with d=[K:Q] and stable Faltings height h_F:

    [GL2(Zhat):rho_E(G_K)] < exp(10^21483) d^(2.4*10^10)
                             max{1,h_F(E),log d}^(4.8*10^10).

For the actual factors descending to Q, restriction improves its dependence on L to

    [GL2(Zhat):rho_F(G_L)] < [L:Q] exp(10^21483)
                             max{1,h_F(F)}^(4.8*10^10).

This is an explicit index bound, not a computation of the exact image. The source is Lombardo, Algebra & Number Theory9(10)(2015), Corollary9.3, p2393; the smaller constants in Remark9.4 involving then-unpublished input were not substituted.

## 5. Source and verification limits

The six summaries report 1,190 rows. We recovered 800 complete register statements and 591 numbered source blocks. The missing sources are ANABELIAN_A1_SUCCESSOR checkpoint 05 (210 rows), GT_TOWER_CHECK checkpoint 10 (180 rows), and 209 LM7 proof blocks. The available 47 and 50 identifiers from the two missing registers are individually recorded. Exact, variant and broad source searches were attempted; prior-context retrieval was disabled.

The requested exhaustive audit is **INCOMPLETE** at this evidence boundary; the requested Hooley proof also remains unestablished. The paper records the completed deductions and the remaining gates separately. A1's unconditional proof and A06's counterexample are separate checked results. CHECK_EVENTS.tsv reports proof readings, source-scope checks, computations, retained-verifier replays and carried background without promoting one into another. All agents were GPT-6 Astra Pro. The runtime did not expose an effort setting. No different-model or formal verification is claimed.

## Further checked real multiplication results

**The ordinary real multiplication target is now checked to be nonempty and proper.** The A13 Jacobian has an integral Rosati O5 action overF2, proved using its full two-torsion group scheme. The ordinaryF4curve y²+y=x+u/x+u²/(x+1) has geometric endomorphism field whose Rosati fixed field isQ(sqrt2), so it never enters this target after extending constants.

**A36 rules out the forced-five repair on an actual reflection quotient.** A constant pointed quintic cover of A27 overF256 has an ordinary genus2 reflection target E with #J_E=2^10*3^4. Every fixed rational canonical class and both inhomogeneous correspondence constants have zero5part. The exact identity on Pic^d is (T²+T−1)L=dF, giving b0=(T+3)a and (2−T)b0=5a. This does not exclude a3primary detector or5primary classes of new points over larger fields.

**A37 closes the finite-support proposal on this precise target.** On ordinary Hilbert–Blumenthal genus2 moduli for O5, the geometric generic Raynaud theta has no nonzero odd-order point. For every finite odd support, including5, a Zariski-dense collection of finite-field curves avoids all nonzero geometric theta points with that support, with all powers and products allowed. The proof uses the full joint integral level torsor, an inverse-different pairing at5 and exact-field Frobenius specialization. Variable-prime witnesses on an individual curve and the prescribed-image canonical problem remain open.

The A34 degree19cover also has an exact constant-degree rule: its rational2primary Prym exponent is1 if7 does not divide m,2 if7 divides odd m, and2^(v2(m)+2) if14 divides m. Its sufficient separation inequality holds exactly when14 does not divide m. This refinement alone is not counted as a new main-gate reduction.

## A38 checked at 2026-11-21 04:39:42 UTC

The unrestricted ordinaryO5 canonical-forcing assertion is refuted: all126 non-Weierstrass F128 points on A13 have canonical class exact order4159, with odd order2079 for2 modulo4159. This uses the already established integral RM5 action and explicit arithmetic; an additional direct field enumerator retains all coordinates. Root read the full proof and script. The narrower assertion for prescribed quintic-transfer images remains open, and the example itself has the geometric theta witness of A13. A new matching paper build is now ready to start.

## A39 and A40 integrated at 2026-11-21 05:00:39 UTC

**A39 certifies actual pointed successes on the fixed A27/A36 example.** Complete Kummer and Riemann–Roch certificates prove a useful3primary canonical class for both original Weierstrass points overF256, through degree15or45 composites. The independent verifier reconstructs the full160x155matrix and checks binaryrank1240; full proof readings also verify that this matrix is the complete required function space. This example is not counted as universal gate movement by itself.

**A40 closes broad inverse-image membership.** Every ordinary genus2 curve with the specified integral RosatiO5 action occurs as a reflection quotient of an etale cyclic5cover of another genus2 curve. The residual theta correspondence is proved integral and generically smooth for each fixed curve, with exact positiveT normalization. After finite constants every prescribed point is an actual image of a rational split lift. Applied to A38, this refutes canonical good-prime forcing even for actual transferred images. Source-rank/Weierstrass restrictions and the existence of a suitable choice of another cover remain separate.

The canonical114-page A38 source/PDF remain matched pending the next assembly. A quantitative refinement bounding the bad inverse-construction parameters is being written and checked; it is not promoted by this entry.

## A41 integrated at 2026-11-21T05:12:26.605429+00:00

The complete quantitative inverse-family proof is checked by four same-model readers. The critical divisor contributes at most28badparameters and the vertical locus at most6, hence at least95parameters overF128 give smooth covers. Each has at least11rational split source points for which all five images of every lift have exact canonical order4159, whose doubling order2079is odd. This refutes the actual fixed-cover lift/reflection repair. It does not refute existence through a different cover, prescribe source two-rank, or produce a section collision.

A39–A41 are now in the modular proof sources and ledgers. The canonical A38 standalone source/PDF stay matched until the next fully checked build is installed. Every newly used proof has a whole-proof reading recorded, and later citation deltas are distinguished from new mathematical reviews.

## A42 and A43 integrated at 2026-11-21T05:38:44.294289+00:00

**A42 makes finite-primary projection quantitative using one fixed Lang cover.** For extension degrees coprime to an explicit integer, the selected rational primary subgroup is unchanged. Each prescribed component then has the stated exact splitting count and square-root error. The actual Raynaud theta corollary gives a dense set of odd-order points and, after rationalizing a useful odd torsion class, a dense set of canonically detectable points. It neither forces a prescribed finite transfer fibre to meet that set nor controls the other prime factors of the whole order. The auxiliary characteristic-primary cover is used for counting; A29 separately supplies allowed odd-degree detectors.

**A43 resolves the rank-one and Weierstrass qualifications for the special A41 family.** At least 95 parameters over F128 give sources of two-rank one. Both Weierstrass points are rational and split, and every reflection image of every lift above either has canonical class of exact order 4159. The complete proof includes the exact length-two tangency, the two-rank calculation and both explicit five-lift orbits. The author's whole proof and additions were read by two other same-model readers; an independent integer-ring calculation checks 15 identities. No independent-model or formal verification claim is made.

The existing fixed-cover forcing row was already refuted at review03. Strengthening its scope is not automatically a new status change, and A42 density does not reduce the existential cover-selection gate. That gate, and the separate higher-genus and other-characteristic inputs, remain open. The canonical 123-page A41 source/PDF remain matched until the next staged build is checked and installed.

## A44 and the A43 general-target supplement integrated at 2026-11-21T05:52:23.145659+00:00

A44 proves a finite eligible-prime obstruction in the pro-two constant tower for every characteristic-two abelian surface. The explicit integer L_A contains all eligible primes, and one explicit finite field captures every primary exponent. A separate full argument proves infinitely many odd theta points in the same tower. Thus the proposed abundance-to-unbounded-eligible-support inference fails. This is not absence of all useful points: a direct norm/divisor identity gives four exact-order3 theta points on A13 over F16. The finite symbolic verifier has an unchanged byte-identical isolated replay; its reference to the separate220-record RR probe is not presented as an independent recomputation.

The A43 supplement proves that the special order-three automorphism is actually absent on some ordinary integral Rosati-O5 targets, using the checked A37 avoidance statement and the functorial actual Raynaud characteristic. This blocks that proposed universal extension of the special inverse-family calculation, while retaining all other cover choices as possible.

Root, author and another same-model reader have read every new proof in full. The current main existential gate is unchanged by these two exploratory mechanism results; neither newly added question label is automatically counted as review movement. The canonical130-page A43 source/PDF remain matched while these checked sections await the next staged build. A nonconstant-deck refinement of the actual-exponent criterion is being investigated and is not promoted in this entry.

## A46 integrated at 2026-11-21T06:12:46.159052+00:00

A46 removes the elliptic-quotient qualification of the rational primitive-factor criterion. For every finite-field curve of genus at least two and every characteristic p, a pointed geometrically cyclic etale cover of odd degree prime to p suffices when its actual primitive conductor factor has no rational p-primary torsion over the specified field. The geometric deck group may be nonconstant. The proof uses the integral Ramanujan projector and a reduced quadratic fibre; the involution would send a nonzero integral projector to its negative by an odd-order shift, which is impossible. Geometric primitive rank zero is therefore sufficient in every characteristic after descent and pointing.

Four same-model readers read the entire new proof; root and author checked the final citation-only cleanup. This is neither independent-model verification nor a formal proof. The already-open qualification in the main sufficient witness gate is removed. The universal existence of a suitable cover is not established, and Masullo still supplies arithmetic candidate orders rather than the missing universal geometric construction. The canonical A43 TeX/PDF pair remains matched while these checked modular additions await the next staged build.

## A45 and the A44 odd-tower supplement integrated at 2026-11-21T06:19:53.808826+00:00

A45 proves the original-field actual-exponent criterion for nonconstant cyclic deck groups in every characteristic. The inequality n>(2M−1)^2 separates in genus2<=g<=p; in larger genus it leaves precisely a separable p-power elliptic map of degree at most g−1, totally ramified at both points. Complete integral semilinear descent shows that each actual primitive conductor factor has the same p-primary exponent over its own minimal deck field. Proper factors can grow in the longer full deck extension. The exact pointed degree39 twist overF4 has whole exponents2 and16 overF4 andF256, respectively. Two separate arithmetic implementations agree on all256 quotient labels. Four same-model readers have read the whole new mathematical proof and recorded its final precision deltas.

The A44 odd-tower supplement proves a necessary form c*ell^a for compatible new orders, with c in an explicit finite list and at most one new prime. Poonen's bounded-index subgroup does not impose that one-prime restriction. This does not prove or disprove universal theta incidence. These results remain conditional only where an explicitly identified arithmetic M consequence is used; their geometric and finite computations are unconditional. No example, new label, packaging, or repeated same-gate restriction is automatically counted as review movement. The canonical source/PDF pair remains matched pending the staged build throughA46.

## A47 integrated at 2026-11-21T06:23:02.986283+00:00

The weighted integral-sign argument allows a bounded positive rational exponent on the actual primitive factor: n>(2^omega(n)M_n−1)^2. It separates for2<=g<=p; in any genus a collision forces a separable elliptic map of p-power degree e>1 dividing M_n and at most g−1, totally ramified at both points, with the original cyclic cover an actual etale elliptic pullback. M_n=1 recovers A46 in every genus. The positive-power principal divisor can occur in that elliptic geometry, so the remaining obstruction is stated rather than suppressed.

The comparison with A45 is precise: the primitive threshold is smaller when the whole exponent exceeds2^(omega(n)−1)times the primitive exponent. Neither numerical test is uniformly stronger for all composite degrees. The older literal rank-zero/unit existence questions remain open. A new question label or an example already handled by the union of earlier tests is not automatically main-gate movement. The portable A45 certificate bundle has also been copied with both implementations, exact outputs, path-only diff, hashes and honest rerun scope.

## A48 and A47 coarse-bound supplement integrated at 2026-11-21T06:29:39.192180+00:00

A48 proves at least n−f_n good unpointed constant twists, and hence at least n−phi(n)>0 in genus two. The prescribed point selects one twist. A constant extension that points any other twist makes it isomorphic to the original pointed model; the exact affine calculation proves the same statement for nonconstant deck group. Therefore any originally present rational primitive p-primary torsion persists. This settles that fixed-cover twisting mechanism, not universal supply by changing the geometric cover. The complete final proof has author, root and a separate same-model whole reading.

A47's supplement proves that the coarse Weil bound, even rounded to a power of two and using full cyclotomic-module multiplicity, cannot certify its sufficient inequality. This is an obstruction to the estimate, not a lower bound for actual torsion. The one degree117 strictness probe found primitive exponent1 and is already covered by A46; it is not counted as new positive-exponent success. The Pop–Saidi primary scope was reread and confirms the already recorded A07 coprime-order qualification, with no new finding for that old correction. Sources are now ready for a single staged build throughA48.

## A48 pullback-iteration supplement integrated at 2026-11-21T06:40:16.166848+00:00

Connected prime-to-p base change retaining the cyclic conductor injects the actual old primitive p-primary group into the new one, geometrically and over every common finite field, by equivariance of integral projectors and norm–pullback[d]. Thus neither the old geometric stable rank nor rational exponent decreases. The same-n A46/A47 input cannot be repaired by this pullback alone, despite Raynaud's simultaneous pulled-back theta incidences. The proof and exact scope have whole readings by author, root and another same-model reader. Fresh cyclic covers upstairs remain possible; this is not counted as universal main-gate movement.

## A49 and the actual A48 geometric corollary integrated at 2026-11-21T06:52:59.204319+00:00

A49 proves an exact original-field Fourier criterion on any prescribed odd abelian quotient killing the canonical class and satisfying the signed-unit condition. A nonuniform augmentation element is equivalent to some cyclic quotient having a rational-unit actual primitive factor. The size bound |H|>#C with p not dividing #C+1 is sufficient. On the retained A45 twist, the full nine-primary quotient succeeds although the prime-level size test fails: the primitive-nine order is103041 and the proper-three order is36. Complete whole-proof readings and the exact small algebra certificate distinguish retained curve inputs from new norm arithmetic. Both retained examples already had witnesses; this is not automatically a strict reduction of the full earlier universal gate.

The A48 geometric corollary gives actual finite-field curves with every primitive Frobenius arrow singular but positive primitive stable rank. Raynaud's degree5*3^a cover,13<=a<=65, is disjoint from A32's degree13 cover. All12 primitive theta incidences coexist with rank between12 and12(d-1). This is an existence construction after finite descent, not an explicit large curve equation or exact new rank computation. It strengthens an inference already refuted by A04 and is not counted as main movement by itself.

The canonical158-page A48 source/PDF pair remains matched and validated until the next staged build is checked. Universal pointed-cover supply remains open. The geometric tower probe found no applicable exponent upper bound in the cited abelian/constant-field class-number theorem; its exact scope is retained.

## A49 unrestricted supply supplement and A50 integrated at 2026-11-21T07:12:02.302491+00:00

The A49 supplement proves that a nonuniform odd quotient can be supplied after suitable constant extensions outside any finite prime support. A fixed kernel and the genus-two difference bound give both a nonzero singleton and an empty coset. This yields one unit character and its signed p-orbit; repeating gives pairwise coprime conductors. It does not guarantee the unit-group hypothesis or unit values for all faithful characters of one conductor. The joint geometric witness gate therefore remains open.

A50 proves a cyclotomic-norm lower bound for integral approximations to a partial p-adic projector and an exact abstract finite-module obstruction. Two separately authored1024-word enumerations give minimum weight10; the exponent-eight module has exact minimum nonzero integral annihilator norm8, which fails the degree31 comparison. No actual Jacobian or collision realizes this module in the statement. Complete whole-proof readings, scripts, every word and packaged replays are retained. New labels and this auxiliary obstruction are not counted as main-gate movement.

The primary noncyclic/tower checks obtained no applicable prescribed-point rational-unit or bounded primitive-exponent theorem. A fixed-field semilinear tower can have bounded rational p-generator rank, but the descent hypotheses alone do not bound exponent. These are exact scope limitations, not a global nonexistence claim. The validated canonical162-page A49 source/PDF remain matched until the next checked build.

## Norm-compatibility and tower attempt recorded at 2026-11-21T07:29:21.176273+00:00

A51 proves the exact split norm/lcm formulas for actual compatible point differences and the invisibility of faithful product-conductor torsion to proper-quotient norms. It proves a uniform bound on the rational p-primary generator count in a specified Frobenius-stable rank-one tower. The corresponding exponent remains uncontrolled; both arbitrary-exponent constructions are expressly abstract and not asserted to come from curves or section collisions. The split-fibre point count is a lower bound, not the missing upper bound. This is a completed auxiliary attempt and does not reset the review clock.

The complete finite-field Theorem3 of Faltings840 was read from its source pages. Its annihilator step uses the full geometric group, including characteristic-primary levels. Restricting to prime-to-characteristic levels recovers only the known p-primary residual. A fresh full reading of A05 found no new gap in the separate cuspidal/configuration proof; it does not provide the requested Hooley proof. The quintic-iteration probe identifies no Hecke correspondence for the reflection move: the natural cross-Jacobian map is zero, and the finite set of first-step covers does not force a prescribed transferred point into the sufficient canonical locus.

The main route remains at the review05 gate. Next actual review is08:15UTC; if it again has no substantive movement, the stopping rule applies. Canonical167-page source/PDF remain matched pending the next checked build.

## A51 matrix and full-transitivity endpoints integrated at 2026-11-21T07:37:35.397699+00:00

The completed-coefficient construction proves that finite semilinear matrix size alone allows arbitrary abstract primitive p-exponents. A separate fixed-rational-function proof gives eventual constant cross-prime valuation, conditional on the missing actual geometric determinant identification. Exact source checks separate profinite presentations, completed Fox coefficients, tower-prime congruences and rational-measure hypotheses. The natural integral-image inference in Asvin Lemma11 fails for [ell] on an elliptic curve; only that precise inference is refuted, not the independent abstract section3.

For actual genus-two primitive factors in characteristic2 with fully transitive deck Frobenius, geometric two-rank is zero or full; in the full case rational two-rank is exactly one. The Frobenius polynomial has the displayed cyclic form and its return valuation is still unknown. Thus full arithmetic transitivity does not force the ordinary primitive factor to be a rational unit. Over the tower's minimal deck field, the prescribed quotient is too small for the A49 empty-coset construction and its kernel is unbounded. The full proofs and their exact scope have author and peer whole-proof readings.

The additional Mellin/unit-L-function passage check gives no fixed character-parameter determinant. None of these auxiliary endpoints closes an earlier universal row or strictly reduces the full main gate. Review05's no-movement count remains1; the actual next review is08:15UTC.

Checkpoint filtering was narrowed to specific externally downloaded primary-source caches and source-page images. Generated work PDFs, their metadata and certificate requirements are retained in forthcoming snapshots. Earlier immutable checkpoint bytes remain untouched.

## A51 reflection-field endpoint and pre-build freeze at 2026-11-21T07:39:46.532303+00:00

All geometric pointed quintic/reflection choices at depth j have representatives over the explicit field F_(q^(187200000^j)); their constant-degree prime support is contained in{2,3,5,13}. That restriction does not exclude good canonical points. For every fixed target inside the same constant extension, a fixed3-primary Lang quotient and degree5^m extensions give asymptotic density(d-1)/d of points with nonzero3-primary canonical class. The prescribed iterated-image incidence remains unproved. This completes the field-support attempt without claiming main movement.

The main A51 proof and all three supplements have complete author and root readings; independent same-model audits are retained or being merged. The Fox supplement's final source-premise wording delta is checked. The sources are ready for a matched build; canonical167-page pair remains unchanged until checked installation.

## A51 weighted-Weil and A52 operator endpoint at 2026-11-21T08:00:09.849568+00:00

The checked weighted-Weil supplement constructs actual ordinary principally polarized abelian varieties with the stated cyclic Frobenius polynomial and rational generator count but exponent q^f. It supplies no Jacobian-cover or compatible-tower counterexample.

A52 proves that any small integral annihilator with nonzero faithful evaluation gives the exact wild elliptic obstruction, and thus separation for2<=g<=p. A fixed integral basis of the stable cyclotomic fixed field gives norm at most2min(M,C_E floor(W^(1/h))). The actual index W remains uncontrolled. In the fully transitive case this is exactly the old2M bound. The actual orbit module gives a matching-order norm lower bound, and conductor-isolating operators have exact minimum2m in the stated transitive scope. Faithful-zero relations descend by integral traces, so inflating them does not improve the degree inequality.

These are newly checked sufficient tests and boundaries, with complete proof-reading records. No universal arithmetic witness supply, actual witness outside the full previous union, previously open universal-row closure, or strict main-gate shrink is asserted. They do not reset the scheduled08:15review.

## Final bounded main-route probes at 2026-11-21T08:12:26.921977+00:00

The actual point-divisor logarithmic differential is nonzero and regular, but has tracezero at a strict order jump. The forced wild ramification contributions cancel the function-degree term in the elementary lower estimate, so no upper order bound results. Finitely many already obtained good signed packets can be preserved while further A49 packets are supplied. Exact common-cover norms, including every line quotient of C_ell squared, still leave missing signed orbits within one rational character block uncontrolled by the other quotient norms. No universal cancellation obstruction is claimed.

Both complete endpoint proofs have author, root and independent same-model whole readings. Neither closes an earlier open universal row, constructs a new separating witness outside the full prior union, or strictly shrinks the main gate. The08:15review decision remains due; mathematical probes are now finished and final typesetting continues.

## Final stopping review at 2026-11-21T08:15:00.023157+00:00

The two consecutive no-movement reviews stop the requested Hooley-route investigation. The checked A1 theorem by A05 is unchanged, and the requested route is not established. A52 adds a sufficient integral-lattice criterion without a universal supply bound. All Masullo-dependent consequences remain conditional. The full row/source, GT-target and concrete-Galois-application gates are exactly those in review06 and QUESTIONS.tsv.
