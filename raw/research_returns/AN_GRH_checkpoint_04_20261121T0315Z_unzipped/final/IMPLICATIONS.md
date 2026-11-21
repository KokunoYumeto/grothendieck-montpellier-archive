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

The separate constant-twist route in recovered ANABELIAN_A1 B.28–B.29 was also read in full. It provides a rational relative-class-number witness for some split base point, without Artin's conjecture in genus two. It does not prescribe that point. The retained audit checks why applying its good-point density estimate on a further cover does not force a good point in the chosen fibre, and why translating the Abel base point changes the Frobenius twist. For curves on which the alternative large-Jacobian-prime-factor criterion is numerically possible, it still retains its actual factorization and primitive-root conditions. A23 proves that universal success of that numerical criterion is impossible.

## 2. Which original rows change analytic status

The required row tables preserve every supplied flag and every recovered register entry. The canonical detailed classification is ROW_ANALYTIC_LEDGER.tsv, with 108 curated entries. ROW_FULL_REGISTER_AUDIT.tsv retains all 800 recovered statements, original statuses and declared dependencies. An original status label is metadata, not an independent proof certification.

| Rows or family | Finding or source | Consequence |
|---|---|---|
| ANABELIAN_A1 A.1; A.31–A.33 | A01, A05 | Point injectivity and its covering formulation hold without number-field GRH. The later A1-successor proof files are still unavailable. |
| Intake §3.3(3), §5(a), route 2 | A02–A04, A06–A25 | Arithmetic primitive-root density and the explicit composite candidate family follow conditionally on M. The universal simple theta bridge is false. An arbitrary odd primitive-rank-zero cover suffices in characteristic two; genus-two incidence is a finite exact test for each finite prime support, but a successful support must depend on the curve: A22 rules out every fixed finite pool. A23 separately rules out universal forcing of the older prime-quotient size test. |
| ANABELIAN_SUCCESSOR A.16; ANABELIAN_A1 B.39 / B.LIT7 | A08; A09; A21–A22 | Finite-list avoidance is made explicit and strengthened to all odd orders generically and every fixed finite prime support over finite fields, including fixed rank one; the rank-one degree-13 example receives a new exact divisor certificate. |
| ANABELIAN_SUCCESSOR final A.14 / working AC.11 | A15; A16; A18 | Rank one automatically excludes the exceptional elliptic double quotient; A18 removes that geometric exception in characteristic two in all genera. The arbitrary odd primitive-factor criterion permits positive-rank proper-conductor factors, as the exact degree-15 example verifies. The rational-only hypothesis remains separately scoped. |
| ANABELIAN_SUCCESSOR A.10–A.11 | A12–A14; A25 | An explicit geometric pure-primary theta test and an ordinary witness are proved; a fixed-prime limitation is identified. The distinct source rational-cover criterion retains its own factorization and primitive-root hypotheses. |
| ANABELIAN_A1 B.3, formula(B.CL.2) | A23 | Its sufficient inequality cannot be forced universally: an ordinary curve violates it over every constant extension while retaining a valid theta witness. |
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
