# Intake of ZETA_TWO (prompt 35, "RH for the zeta functions of schemes over Z and of motives over Q, from the two proofs"), final, 21 Nov 2026

Intake by Claude Opus 5.5 at effort high, launched by the main session (Claude Opus 5.5 at effort max) on 21 Nov 2026.
The run: GPT-6 Astra (ChatGPT Pro mode), a root and three delegated readers of the same model (the run writes "GPT-6
Astra Pro, effort not exposed"). Work began about 20 Nov 23:50 UTC; final package 21 Nov 00:32 UTC (about 42 minutes;
no checkpoint was due, no three-hour review was reached).

Notation as in the run and in the CX_GRH intake: **A** = Alpöge's five endpoint declarations of `ALPOGE_Main.lean`
(RH, GRH for Dirichlet L-functions; a theorem). **M** = GRH for the Hecke L-functions of every continuous unitary
idele-class character of every number field (Masullo's draft claim; conditional). **U** = unconditional before either.

## 0. What was read, and the scope

- **Return folder:** `research_returns\ZETA_TWO_final_20261121T0032Z_unzipped` (the final; no checkpoint of this run
  exists). Newest present at start and at end of this intake.
- **Prompt as sent:** `SENT\35_ZETA_TWO_RH_for_schemes_and_motives_from_the_two_proofs\PROMPT.md` (read in full). From
  its ZIP I opened `BRIDGES_20261120.tex` (F1, F2, Q01-Q04) and page 12 of `MASULLO_the-music-of-the-primes.pdf`
  (§1.2: the character is "the arbitrary continuous character of C_F", so M as the run states it is the draft's claim).
- **Read:** `ZETA_TWO.tex` in full (2318 lines); `LEDGER.md`, `README.md`, `DELIVERY_RECORD.txt`, `TRANSCRIPTION_NOTES.tsv`,
  the first 12 kB of `IMPLICATIONS.md`, `QUESTIONS.tsv` (all rows, state column), the check-event types of the main ids in
  `CHECK_EVENTS.tsv`. Not read: `FLAG_AUDIT.tsv` (575 rows), `INTAKE_INVENTORY.tsv`, `CONDITIONAL_AUDIT.tsv` (85 rows),
  `METHOD_STATEMENTS.tsv`, the `audit\` reviews.
- **Read in full, every step checked (21):** ZT01, ZT02, ZT03, ZT04, ZT05, ZT06, ZT07, ZT08, CM01, IA03, IA06, IA07,
  IA08, IA09, SV01, SV02, AR01, ML01, ML02, ALP01, ALP02 (ALP02 as a consequence of the quoted Lean statement).
- **Recomputed independently (scratch script):** IA06 (value −1.4525092396456447), IA07 (resultant of x^11+1 and the
  reduced S equals −3072·23^10; h^- = 3 numerically from the eleven B_{1,χ}), IA08 (2 log φ/√5, φ^4 = 6.854101966…),
  IA09 (mean of |L(1,χ)|^2 over odd χ mod 101 equals π²(p−1)(p−2)/(6p²) = 1.59640; minimum |L(1,χ)| = 0.5368 < π/√6).
- **Read at the level of the statement (constants and locators carried, not checked against their sources):** IA02
  (Lamzouri-Li-Soundararajan constants), IA04 (Ihara-Murty-Shimura R_-(D), Habegger-Jones-Masser height normalization),
  IA05 (Wei's Corollary 4.3 and Proposition 4.7; the Stark-descent logic I checked), CM01's input (Anderson 1986,
  Cor. 5.7.2, Rem. 5.7.3), IA01 and MDOC01 (documentary), the cote 60 readings (scans 3, 5, 7, 9; I did not view them),
  Part II (method statements; no proofs there).

## 1. Verdicts, finding by finding

| Id | Statement (short) | Input | Verdict |
|---|---|---|---|
| ZT01 | exact Artin-Tate counts #X(F_{p^r}) = Σ p^{ir} Tr(F^r \| V_i^{I_p}) at every p ⇒ ζ_X = ∏ L(V_i, s−i); abelian case: non-integer divisor on Re s = i+1/2 | U (identity); A (RH) | **confirmed** (targeted proof check). It is F1 of the bridges run (and ALPOGE_BRIDGES BR-AT-01) restated with inertia invariants, so it covers the non-abelian Artin part as an identity. |
| ZT02 | M ⇒ every virtual Artin L(V,s) has zeros and poles in 0<Re s<1 only on Re s = 1/2; no holomorphy | M (finite-order Hecke characters suffice) | **confirmed**. Standard Brauer argument; identical to the "Brauer remark" of the CX_GRH intake §3. Not new against our intakes. |
| ZT03 | Spec O_K has exact Artin-Tate counts (permutation representation C[Hom(K, Q̄)]); M ⇒ RH for every ζ_K; A for K abelian | A / M | **confirmed**. One correction to the run's wording: F2 of the bridges run already handled ramified primes (its proof uses #X(F_{p^r}) = \|G/I_p\|[f\|r] and primitive characters), so ZT03 is not a repair of F2. |
| ZT04 | identity only off a finite S ⇒ ζ_X = R_{X,S}·∏ L(V_i,s−i), R_{X,S} a finite product of rational functions of p^{−s}, divisors on vertical progressions | U | **confirmed** (elementary). |
| ZT05 | Spec Z[1/p]: ζ = (1−p^{−s})ζ(s) has zeros 2πik/log p, k≠0, on Re s = 0 | U | **confirmed**. Key consequence for ALPOGE_BRIDGES CC-F01b, see §5.2. |
| ZT06 | every finite-type X/Z: ζ_X = ∏_{p∈S} Z(X_p,p^{−s}) · ∏ L^S(H^j(Y_a),s)^{±n_a}, Y_a smooth projective over Q (Bittner, Thm 3.1; EGA IV_3 (8.8.2) spreading out; Weil I Thm 1.6 for convergence) | U | **confirmed as an algebraic reduction** (it is Serre 1965's reduction made precise with Bittner's generators). **Gap in one clause:** "under M every known CM factor in this finite list satisfies its RH condition": the H^j(Y_a) are not given as sums of CM and non-CM pieces. Splitting off a CM summand needs a decomposition of the compatible system (Faltings' semisimplicity and Tate theorem when Y_a is an abelian variety, Deligne's absolute Hodge cycles for its motive), which the proof does not supply in general. Read the clause as: for each summand of H^j(Y_a) that is known to lie in Anderson's category, CM01 applies. |
| ZT07 | E/Q, smooth proper model over Z[1/S]: ζ_E = ζ^S(s)ζ^S(s−1)/L^S(E,s); under A, in 1/2<Re s<3/2 off Re s = 1, ord ζ_E = −ord L(E,s) | A | **confirmed** (I checked each local factor: deleted good factors on Re s = 1/2, multiplicative on Re s = 0, deleted factors of ζ^S(s−1) on Re s = 1). Elementary but useful: an off-line zero of L(E,s) cannot hide in ζ_E. |
| ZT08 | det(1−tF) = Σ(−t)^j Tr ∧^j, Tr ψ^r = Tr F^r: the Euler factor is a λ-ring invariant, blind to extensions and lattices | U | **confirmed** (standard; SGA 6 V §2). |
| CM01 | M ⇒ for every pure motive of weight w in Anderson's category (absolute Hodge motives generated by Artin motives and potentially CM abelian varieties), every zero or pole of L(M,s) in w/2<Re s<w/2+1 is on Re s = (w+1)/2 | M, **all unitary Hecke characters, including infinite order** | **confirmed** given Anderson's Cor. 5.7.2 (same-weight factorization L(M,s) = ∏ L(ψ_a,s)^{m_a}, m_a ∈ Z), which I did not open. Normalization ψ ↦ ψ\|·\|^{−w/2}, gamma factors and boundary poles checked. Scope point checked on Masullo p. 12: §1.2 takes an arbitrary χ in the unitary dual of C_F, so M as used is the draft's claim. Its Theorem 13.3.1.2 is empty (MDOC01). |
| IA01 | audit: of 575 BRIDGE_FLAGS rows only two mention RH/GRH, neither an unmet GRH hypothesis; "Siegel" occurs in none of the four intakes | — | **statement level** (documentary; agrees with the bridges ledger of 20 Nov: "2 RH/GRH rows, neither depends on RH over Q"). |
| IA02 | A ⇒ LLS v3 Thm 1.5 bounds V(q)^{-1} ≤ \|L(1,χ)\| ≤ U(q) for q ≥ 10^10; h(−D) bounds; n(p) < (log p)² (p ≥ 5); P(a,q) ≤ (φ(q) log q)² (q>3); h_K R_K bounds for abelian K | A (Dirichlet only) | **statement level, scope confirmed.** The inputs are Dirichlet GRH only, so A suffices; constants carried from LLS. The run's point that a bound on h_K R_K is not a bound on h_K without a regulator lower bound is correct and bears on SA06 B.4e. |
| IA03 | S_p (supersingular j in F_p) = c_p h(−D_p), (D_p,c_p) = (4p,1/2), (p,1), (p,2) for p ≡ 1 mod 4, 7 mod 8, 3 mod 8; explicit bounds for D_p ≥ 10^10 | A | **confirmed** (Delfs-Galbraith count as I know it; the three discriminants are fundamental). |
| IA04 | CM elliptic Faltings height, h_F = ¼log(Df²) + ½L'/L(1,χ_{−D}) − … ; explicit error < ½R_-(D) | A | **statement level** (identity and R_-(D) carried; the substitution step checked). |
| IA05 | A removes the no-Siegel-zero gate for CM heights: quadratic Dirichlet GRH + Stark's descent of an exceptional zero of a normal field to a quadratic subfield; with an individual Colmez formula, h_F^st(A) < (75/4) g ((2g)!)² log(\|D_K\|^{1/[K:Q]}) − (g/4)(γ+log 4π) | A (+ Colmez where not abelian) | **logic confirmed, constants statement level.** The dependency reduction M → A is right: Stark's lemma moves any exceptional zero of a normal field into a quadratic Dirichlet L-function. |
| IA06 | full CM by Z[ζ_5]: h_F^st = ½log5 − (3/2)log(Γ(1/5)/Γ(4/5)) − ½log(Γ(2/5)/Γ(3/5)) = −1.45251… | U | **confirmed** (L(0,χ) = (3+i)/5 and L'/L(0,χ) rederived by hand; value recomputed). Colmez normalization carried from Wei Thm 4.8. |
| IA07 | h(Q(ζ_23)) = 3 from det = −3072·23^10, h^- = 3, h^+ = 1 (Miller); K̃_0(Z[C_23]) ≅ Z/3 (Rim) | U | **confirmed** by independent computation (resultant and numeric h^-). |
| IA08 | L(1,χ_5) = 2 log φ/√5, φ^4 = (7+3√5)/2 | U | **confirmed** (computation). |
| IA09 | for every odd p some odd χ mod p has \|L(1,χ)\| ≤ π/√6; refutes the SA20 shorthand L(1,χ) ≍ log log q | U | **confirmed** (rederived and computed for p = 101). Elementary. |
| SV01, SV02 | unramified Euler factors depend only on [V] ∈ K_0; Kummer extension of Q(0) by Q(1) for the unit 2 over Z[1/2] has L^S = ζ^S(s)ζ^S(s+1), same as the split object | U | **confirmed.** Same point as ALPOGE_BRIDGES BR-MIX-01 (good-prime L-data see only gr^W), with an explicit pair. |
| AR01 | reciprocal symmetry of det(1−tf) does not force \|eigenvalue\| = √a | U | **confirmed** (trivial). |
| MDOC01 | Masullo Thm 13.3.1.2 (PDF p. 522) has no statement or proof | — | **statement level**; third witness after CX_GRH and ALPOGE_BRIDGES. |
| ML01 | local factors of a unitary Hecke character at places of distinct residue characteristic share at most one pole; for finite order, a pole s ≠ 0 at ≤ [F:Q] places | U | **confirmed** (elementary; independently checks Masullo 1.7.1.1(1),(3)). |
| ML02 | (ψ∗ψ*)\|_H = 0 with 1 ∈ H forces ψ = 0; so the test domain φ\|_{C_F^1} = 0 of Masullo 12.5.1.1 contains no Weil-positivity test | U | **confirmed** (trivial; the draft says so itself, §1.7.2). |
| ALP01 | ε(D^p(FG)) ∈ pR when ε(F) = ε(G) = 0; D^p a derivation in characteristic p | U | **confirmed** (Leibniz and p \| binom(p,j)). |
| ALP02 | from Alpöge's Lean `GlobalTheory.T.detDepth_lower_bound_saturated_even_type` (rank one, no odd type): v(d^c/dt^c f(exp_G(tu))\|_{t=0}) ≥ cp/(p²−1) − log_p c − 1 | U (cited Lean statement) | **confirmed as a formal consequence** (j = 0 forces r_0 = 0). The Lean statement itself is statement level. DP_MULT DP6 improves the error −log_p c − 1 to −1 in the one-dimensional height-two case (see the DP_MULT intake). |
| Archive | cote 34 scan 64 (Rem. 1.17 struck, "plausible", "semblerait"), scan 74 ((2.5.5), dimension one by Riemann-Weil); cote 60 scans 3, 5, 7, 9 (determinant algebra; scan 9 assumes "satisfaisant aux conj. de Weil") | — | 34/64 and 34/74 **agree with our text of record** (`text_of_record\pages\34\34_scan064.tex` line 13-17, inside `\deleted{}`; `34_scan074.tex` line 11, `=1`). Cote 60: statement level. |
| TN-AR-01 | (2.5.5): manuscript "=1", our bridges paper "=0" | — | **not a text-of-record misreading.** Our text of record already reads `H^1(\bar X',\mathbb Z_\ell)^{\pi_0}=1`. Only `BRIDGES_20261120.tex` (table row Q04) writes 0. |

**Counts.** 29 rows. Confirmed with every step checked: 21 (four of them also by independent computation). Confirmed as a
reduction with a gap in one clause: 1 (ZT06). Statement level: 6 (IA01, IA02, IA04, MDOC01, the cote 60 readings, IA05's
constants). Refuted: 0. The transcription note: reclassified as an edit to our bridges paper, not to the text of record.

## 2. What is new

- **Against the literature:** nothing here is a new theorem of number theory. ZT01-ZT03, ZT06, ZT08, CM01 are standard
  consequences (Serre 1965; Brauer; Deligne 1979 §8 and Anderson 1986 for CM motives); IA02-IA08 are transfers of
  published GRH-conditional bounds or classical evaluations. Their value is the exact scope, which is what prompt 35
  asked for.
- **Against our own results and tonight's runs:**
  - ZT01 = bridges F1 = ALPOGE_BRIDGES BR-AT-01, extended to the non-abelian Artin part as an identity.
  - ZT02 = the Brauer remark of the CX_GRH intake §3 (no new content).
  - **CM01 is new for our files:** the CM part of Q02 closes under M, and it needs M for **infinite-order** unitary Hecke
    characters. The CX_GRH remark spoke of finite-order characters only; that does not reach CM motives.
  - **The gate of Q01/Q02 is refined**: from "RH in positive weight" (bridges ledger, 21 Nov update) to "non-CM geometric
    monodromy up to Tate twist"; Sym²h¹(E)(1) has weight 0 and is non-CM.
  - **ZT05 bears on ALPOGE_BRIDGES CC-F01b** (§5.2): the intake's gloss of CC-F01b as "RH for ζ_X of every Λ-scheme" is
    false for Spec Z[1/p], which is a Λ-scheme (a binomial ring; DP_MULT DP11 gives the criterion).
  - **IA05** moves the no-Siegel-zero gate for CM heights from M to A. Our intakes of 20 Nov carried it as "beyond A".
  - SV02 = ALPOGE_BRIDGES BR-MIX-01 with an explicit example; MDOC01 = CX_GRH and ALPOGE_BRIDGES.
  - ALP02 overlaps DP_MULT DP6 (see the DP_MULT intake, §2).

## 3. The scope of the two proofs

- **A (theorem):** ZT01 (abelian case), ZT03 for abelian K, ZT07, IA02, IA03, IA04, IA05 (zero gate; the individual
  Colmez identity for non-abelian CM types is a separate input, B), the abelian h_K R_K bound.
- **M (conditional):** ZT02, ZT03 for non-abelian K, ZT06's CM clause, CM01, IAQ-008-012, IAQ-039 (effective Chebotarev in
  division fields, Lagarias-Odlyzko type), IAQ-040-059 (ring-class fields: generalized dihedral, their non-genus
  characters are Hecke characters of the imaginary quadratic field).
- **M needs more than finite order** only in CM01 (Größencharaktere of the reflex/CM fields). The run states this
  correctly; it should go into our scope tables (§5.3).
- **Beyond both:** non-CM RH (L(E,s), non-CM eigenforms of weight ≥ 2, Sym^n), Artin holomorphy (ZT02 and CM01 control
  the location of signed orders, never their sign), individual Colmez for non-abelian CM types, every exact special
  value (regulators, Bernoulli numbers, integral K-groups, Ext groups: SV01, SV02).
- **No statement claims more than its input gives**, except the ZT06 clause noted in §1.
- **DEG_L** (added 21 Nov 2026 after the intake of DEG_L, Claude Opus 5.5 at effort high): the L-values in the Rallis
  degree formulas are at 3/2, in absolute convergence (DEG_L T6.11, with B1's unconditional bounds), or are U(2) standard
  L-values at 1 (T6.12-T6.13); neither A nor M bears on the 032 degrees.
- **Masullo's draft, located defects** (added 21 Nov 2026 after the intakes of GRH_NIGHT and TRACE_DET, Claude Opus 5.5
  at effort high): gaps at §9.3.2 (pp. 425-426: MT-M01, MT-M02, MT-M05), §11.3 (p. 495, F-SM-19, repaired), §12.3-§12.4
  (the intertwiner, ALPOGE_BRIDGES), (10.3.2.4) p. 454 off by one at odd s (MAS-BOUND), and Theorem 13.3.1.2 (p. 522)
  blank. Every "conditional on M" above carries this note.

## 4. In the language of algebraic geometry and Grothendieck's frameworks

The run does this throughout, and correctly: ZT01 as a class [Rf_!Q_ℓ] = Σ[𝒱_i(−i)] in K_0(D^b_c(Spec Z[1/Sℓ], Q_ℓ))
with finite monodromy (SGA 4 XVII §§5.1-5.3; SGA 5 XV §3 n°2; Grothendieck, Bourbaki 279, Thm 5.1); ZT08 and SV01 as
λ_t([V]) = ∏ λ_t([gr_j V]) (SGA 6 V §2, (7.1.1)); ZT06 by EGA IV_3 (8.8.2); purity by Weil I 1.6 and Weil II 3.3.1;
CM01 in Deligne's absolute Hodge motives. Two translations it did not give:
- **ZT05 in Grothendieck's language:** the local factor at p of ζ_X is det(1 − F t | RΓ_c(X_{F̄_p}, Q_ℓ))^{(−1)}, and for an
  open X ⊂ Spec O_K it equals the inertia-invariant formula only if X_p = (Spec O_K)_p; removing a fibre multiplies ζ_X by
  Z(X_p, p^{−s})^{−1}, whose divisor lies on Re s = (local weight)/2, not on the global line (w+1)/2.
- **Where it lives in the archive:** cote 60 (Fonctions L, équation fonctionnelle, cas géométrique) scans 3-9 for ZT08;
  cote 34 scans 64 and 74 for the Riemann-Weil remarks (unchanged readings).

## 5. Integration: the edits, and what each finding now makes possible

Make no edit outside this folder; these are the edits for the coordinator.

### 5.1 Bridges run, `reports_20261120\alpoge_rh\bridges\`
- **QUESTIONS.tsv / LEDGER.md, rows Q01 and Q02.** Replace the state "remaining gate: RH for motives of positive weight
  that are not Artin-Tate" with: "A: abelian Artin-Tate (F1 = ZT01). M: every Artin-Tate count, every Spec O_K (ZT02,
  ZT03) and every pure motive in Anderson's CM category (CM01; needs M for infinite-order unitary characters). Q01 for
  general X reduces to finitely many L^S(H^j(Y_a)) and the bad fibres (ZT06). Remaining gate: RH for the non-CM summands,
  up to Tate twist (first case h¹(E), E non-CM; ZT07: its off-line zeros cannot cancel in ζ_E); not a weight condition."
  - How it bears: Q01 is now one finite list per scheme. The attack it makes possible: for a given X, compute the list
    (Bittner witness + Faltings' semisimplicity on the abelian pieces) and so state exactly which non-CM L-functions its
    RH waits on. For curves and abelian varieties over Q this is the list of GL_2-type and higher Galois orbits.
- **BRIDGES_20261120.tex, table row Q04:** write "(2.5.5) H^1(X̄',Z_ℓ)^{π_0} = 1 (multiplicative notation for the trivial
  group; = 0 additively)". The text of record is already right (§1, TN-AR-01).
- **ZT05 caution on F1:** add to F1's statement "all primes, including those dividing the conductors; an identity off a
  finite S gives only ZT04's form".

### 5.2 ALPOGE_BRIDGES (prompt 22) and its intake
- **CC-F01b** (ALPOGE_BRIDGES `research\consequences_criteria.md` line 14) says: the rational compactly supported
  cohomology of every separated finite-type Λ-scheme over Z splits into finite abelian characters and Tate twists; "bad-fiber
  model zeta functions require separate treatment". That statement is untouched by ZETA_TWO. But the ALPOGE_BRIDGES intake,
  §4 item 2, glosses it as "CC-F01b turns 'X has a Λ-structure' into 'RH for ζ_X holds unconditionally'". **That gloss is
  false.** Spec Z[1/p] is a Λ-scheme (Z[1/p] is a binomial ring: binom(a,n) ∈ Z[1/p], i.e. a^ℓ ≡ a mod ℓ for every prime ℓ;
  DP_MULT DP11 is the criterion), and by ZT05 its zeta function has the non-real zeros 2πik/log p on Re s = 0, on no line
  i + 1/2.
  - Edit for that intake (§4 item 2, line 129): "CC-F01b gives RH for L(H_c(X_Q̄), s) with its canonical (inertia-invariant)
    Euler factors, A_D; ζ_X itself differs by the finite factor R_{X,S} of ZETA_TWO ZT04, whose divisors lie on lines
    Re s = v/2 (Weil II 3.3.1 on the bad fibres) and can be non-real (ZT05: Spec Z[1/p])."
  - The attack this opens (prompt 22's successor, CC-F01b): **decide the bad fibres of Λ-schemes.** Conjecture to test:
    for a Λ-scheme X flat of finite type over Z, every bad-fibre factor of R_{X,S} is a product of (1 − ζ p^{j−s})^{±1}
    with ζ a root of unity and j ∈ Z. It holds for Spec Z[1/n], Spec of abelian rings of integers and their localizations,
    and split tori. If true, ζ_X of every Λ-scheme has all non-real divisors on Re s ∈ ½Z: on i + 1/2 from Dirichlet L
    (A), on integers from the fibres. This is the correct unconditional "RH for Λ-schemes", and Borger's Frobenius lifts
    at the bad prime p (ψ_p lifts the absolute Frobenius of X_p) are the tool to try first.
  - Also for CC-F01b: ZT01 shows that an all-prime identity is what makes ζ_X equal to the Dirichlet product; for a
    proper flat Λ-scheme this asks whether Borger's splitting holds for RΓ_c(X_{F̄_p}) at the bad p as well.

### 5.3 CX_GRH intake, §3 "Remark for our own scope tables"
- Add: "For CM motives (Q02) the Hecke characters are algebraic of weight w; after the unitary twist they have infinite
  order. So the CM case needs M for all unitary Hecke characters (ZETA_TWO CM01), which is what Masullo §1.2 (PDF p. 12)
  claims; GRH for finite-order Hecke characters does not suffice."

### 5.4 The intakes of 20 Nov (`field_experts\intake_20261120\intakes\` and `results_register\horizontal\sweep3\`)
- **SA06 A.8a** (cote 15, scan 70 per the intake; not reopened): replace "Littlewood bounds for supersingular counts
  under GRH" by IA03: for p > 3 and D_p ≥ 10^10, c_p√D_p/(πV(D_p)) ≤ S_p ≤ c_p√D_p U(D_p)/π, unconditional by A. The
  geometric count ⌊p/12⌋ + ε_p is a different quantity.
- **SA06 A.8c:** gate stays (the ring R is undefined in the intake); if R is the maximal order of Q(√−p), IA02 applies with
  D = p or 4p.
- **SA06 B.4a-B.4e:** add "A bounds h_K R_K for abelian K (IA02); a bound on h_K needs a regulator lower bound; B.4c stays
  refuted as worded".
- **SA07:** no Faltings-height or Colmez row exists in that intake (IA01). Add IA04 and IA05 as new rows of the CM-heights
  topic, with IA05's dependency A (zero gate) + individual Colmez (B, except abelian CM types). Rows E.2.1-E.2.6 (ring-class
  fields): RH for their Dedekind zeta functions is M.
- **SA20 A5.011:** h(Q(ζ_23)) = 3 and K̃_0(Z[C_23]) ≅ Z/3 are U (IA07); replace the shorthand "L(1,χ) ≍ log log q" by
  V(q)^{-1} ≤ |L(1,χ)| ≤ U(q) under A (IA02), and note IA09 (no uniform lower bound of size log log q).
- **REVLOC I.8b:** the number 6.8541… is φ^4 = (7+3√5)/2, and L(1,χ_5) = 2 log φ/√5 (U). I.5 stays "refuted as worded".

### 5.5 Grothendieck's texts
- **No reading changes.** Cote 34 scans 64 and 74 agree with our text of record. Cote 60 scans 3-9 (determinant algebra
  before the Weil-conjecture hypothesis on scan 9) are consistent with ZT08 and AR01: the determinant functional equation
  carries no purity; Grothendieck states purity as a hypothesis there. A reading note for cote 60 scan 9 in the
  companion: "the passage from det-identities to the weight-normalized functional equation assumes the motive satisfies
  the Weil conjectures; AR01 shows the identities alone give no absolute values."

### 5.6 Successor prompts (30-36 and the runs' successors)
- **33 (TRACE_DET):** ML02 and MDOC01; the test domain φ|_{C_F^1} = 0 of Masullo 12.5.1.1 has no positivity test; with
  ALPOGE_BRIDGES R-MAS-KERNEL this is where our runs can test the draft.
- **34 (DP_MULT):** ALP02 (the Lean depth bound, error −log_p c − 1) and the recovered Lean paths: DP_MULT DP6 already
  sharpens it (see that intake).
- **30 (GRH_ANABELIAN):** IAQ-039 (effective Chebotarev in division fields is M) and IA05 (Stark descent: under A no normal
  number field has an exceptional zero in Stark's region).
- **31 (STEP17):** SV01, SV02 and the DG (2.1.3) rational Ext computation: zero location cannot see integral K-groups; the
  gate stays Vandiver.
- **32 (HODGE_SIGN):** ZT07 and the Q02 gate: the sign-only route has to reach non-CM h¹ to move Q02.

## 6. Prompt updates: what a successor of ZETA_TWO needs

1. **Main question: the non-CM gate, and the Stark corollary.** The run answered the transfer questions in 42 minutes. Its
   successor should push on what A makes newly possible:
   - (a) **Effective Brauer-Siegel for normal fields under A.** Stark (Invent. Math. 23, 1974; Lemma 8 and Theorem 1′, to be
     checked) puts every exceptional zero of a normal K in a quadratic subfield; A excludes it. State and prove the
     resulting effective lower bound for h_K R_K for every normal K (and, through the Galois closure, for CM fields of fixed
     degree), with constants. Then decide which known proofs become effective: the Galois-orbit lower bounds for CM points
     in A_g (Tsimerman's André-Oort, with the averaged Colmez formula), and Siegel-type class-number bounds for CM fields.
   - (b) **Λ-schemes:** the bad-fibre question of §5.2, with Borger's Frobenius lifts at the bad primes.
   - (c) **Non-CM:** for X a curve or an abelian variety over Q, compute the ZT06 list exactly (Faltings' semisimplicity)
     and name the non-CM L-functions RH for ζ_X waits on.
2. **Attach** Anderson 1986 (§5.7), Stark 1974, Borger 2009, and DP_MULT's DP11, so that CM01 and the Λ-question can be
   checked against the sources.
3. **Do not redo** IA01's audit or the A/M dependency tables; cite `CONDITIONAL_AUDIT.tsv`.
4. **Model and effort:** the run writes "GPT-6 Astra Pro, effort not exposed"; it is GPT-6 Astra (ChatGPT Pro mode).
5. **The run stopped at 42 minutes** with Q02-GENERAL and the general Q01 at reduced gates, before any three-hour review.
   The prompt's push rule allowed this, since every item had a proved reduction. A successor that wants the non-CM gate
   attacked must make it the main question (item 1), not the transfer tables.
