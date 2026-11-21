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

The strongest tested projection approach uses Poonen Theorem 1.8. It supplies theta order ell^r m with the chosen ell-primary component and with every prime of m outside a density-one set. It does not make m=1. Multiplication by m need not preserve theta; an intermediate cover retains proper-conductor blocks. On a nonordinary base with ell=3 and r=1, A10 proves that m must actually be greater than one. This is a concrete obstruction to treating the extra factors as harmless.

## 2. Which original rows change analytic status

The required row tables preserve every supplied flag and every recovered register entry. The canonical detailed classification is ROW_ANALYTIC_LEDGER.tsv, with 108 curated entries. ROW_FULL_REGISTER_AUDIT.tsv retains all 800 recovered statements, original statuses and declared dependencies. An original status label is metadata, not an independent proof certification.

| Rows or family | Finding or source | Consequence |
|---|---|---|
| ANABELIAN_A1 A.1; A.31–A.33 | A01, A05 | Point injectivity and its covering formulation hold without number-field GRH. The later A1-successor proof files are still unavailable. |
| Intake §3.3(3), §5(a), route 2 | A02–A04, A06–A11 | Arithmetic primitive-root density follows conditionally on M. The universal theta bridge is false; a weaker sufficient prime-power gate is proved and remains undecided for arbitrary positive-rank finite-field curves. |
| ANABELIAN_SUCCESSOR A.16; ANABELIAN_A1 B.39 / B.LIT7 | A08; A09 | Finite-list avoidance is made explicit in families, including fixed rank one; the rank-one degree-13 example receives a new exact divisor certificate. |
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
