# Intake of AN_GRH (prompt 30, "GRH and the anabelian line: Hooley, Chebotarev, cote 149"), checkpoint 02, 21 Nov 2026

Intake by Claude Opus 5.5 at effort high (agent af2a18f62da23b48e), launched by the main session (Claude Opus 5.5 at
effort max). The run: GPT-6 Astra (ChatGPT Pro mode), a parent and three delegated agents (the run writes "effort not
exposed"). It started 21 Nov 00:15 UTC and is still going. The coordinator directed this intake to checkpoint 02, which
supersedes checkpoint 01.

## 0. What was read, and the scope

- **Return folder:** `research_returns\AN_GRH_checkpoint_02_20261121T0144Z_unzipped` (checkpoint 02, 01:44 UTC).
  - Its `final/` holds the six deliverables assembled so far: AN_GRH.tex (2,991 lines), QUESTIONS.tsv (1,352 rows),
    LEDGER.md, CHECK_EVENTS.tsv, IMPLICATIONS.md and TRANSCRIPTION_NOTES.tsv, with certificates and evidence.
  - `_from_earlier_checkpoints/` holds only checkpoint 01's GT manifest, which I did not need.
- **Prompt as sent:** `SENT\30_GRH_ANABELIAN_Hooley_Chebotarev_and_cote_149\PROMPT.md`. I read the task, its four items
  and "where our files stand".
- **Read:** AN_GRH_SESSION_STATE.md, final/README.md, final/LEDGER.md (all), and in AN_GRH.tex lines 206-806 (A01 to A06
  in full), 1132-1150 and 1296-1330 (the A09 and A11 statements), 1511-1530 (G01), 1728-1745 (G06) and 1801-1862 (T01,
  T07).
- **Read in full, with every step checked:** A01, A02, A03, A04, A05, A06, T01. A06 also has my own recomputation of all
  its finite arithmetic and of its polynomial identity over F₂.
- **Statement level:** S01, S02, A07, A08, A09, A10, A11, G01 to G06, T02 to T07, R01 to R03.
- **Not read:** the row-audit TSVs (1.2 MB and more), the B23 Bézout certificates and the A09 scripts. The in-progress A12
  to A15 are not in the paper yet.

## 1. Verdicts

| id | statement (short) | uses | verdict |
|---|---|---|---|
| A01 | over a finite field, the covering formulation of A1 (for every pointed prime-to-p Galois cover D → C_L, a lift Q' with [Q' − P'] ∈ J_D(L)[p^∞]) is equivalent to equality of point-section classes | none | **confirmed**. The prime-to-p Kummer kernel of a finite J_D(L) is its p-part. Uniqueness of the lift (Hilbert 90 and an orbit-length count) and compactness of compatible lifts are both checked. |
| A02 | under M, Hooley's theorem for base 2: #{ℓ ≤ x : ord_ℓ 2 = ℓ − 1} = A·Li(x) + O(x log log x/log²x), with Artin's constant A | M (ζ of K_n(2) = Q(ζ_n, 2^{1/n}), non-abelian; K₃(2) has group S₃) | **confirmed as a transfer**; Hooley 1967 §7 and Fan-Pollack Thm 1.1 not opened. A_D does not supply it. |
| A03 | the theta route needs T(C): a prime ℓ with 2 a primitive root and a nonzero ℓ-torsion line bundle on the Raynaud theta divisor; T(C) with A01 gives point separation | none | **confirmed**. One singular arrow on a single Frobenius orbit makes Frobenius on the new factor nilpotent; then two-rank 0, the degree-two pencil, and no odd-order free automorphism of a hyperelliptic curve. The higher-genus remark (one singular arrow need not give nilpotence) is correct. |
| A04 | positive density of theta-supporting primes would not combine with Hooley: for ℓ ≡ 1 (8), both 2 and −1 are squares | none | **confirmed**. |
| **A05** | **A1 holds**: for a hyperbolic curve X over a field K finitely generated over F_p, X(K) → Sec(Π_X → G_K)/Δ_X is injective, where Π_X keeps the whole G_K and replaces only the geometric group by its prime-to-p completion; the analogue holds in characteristic 0 | none (neither A_D nor M) | **read in full; no gap found at the level of the argument. Steps 3-6 confirmed; Steps 1-2 confirmed modulo standard comparisons** (SGA 1 XIII Cor 2.9, §2.10, Lemma 2.11, Prop 5.2; the free pro-r lemma), whose details I did not re-derive. The chain of the proof: (1) exactness of the cuspidally pro-r configuration sequence (A05.1); (2) a conjugacy of the sections s_P, s_Q gives β: G_P ≅ G_Q over Π_C, preserving cusps; (3) equal point counts of corresponding open covers by the trace formula; (4) by compactness β carries point sections to point sections, and Saïdi-Tamagawa (Prop 1.8(vi)) pins them down outside a finite exceptional set E_C; (5) for f with div f = p^e(P − Q), κ_r(f) = p^e χ + κ_r(a) and χ is a coboundary at good points, so f(R)/a has trivial r-primary Kummer class at every good R. Choosing R with f(R) = aζ, ζ a nontrivial r-power root of unity, avoiding the finite excluded values, gives a contradiction. Step 6 handles the finitely generated base, genus 0 and 1, and characteristic 0. **Provenance:** this is a checked reconstruction of our own run ANABELIAN_A1, checkpoint 03 (A.2-A.5, A.14-A.19, A.30-A.33), recovered by AN_GRH. It is not new to AN_GRH, and the run says so. |
| A06 | T(C) fails for an explicit genus-two curve over F_{2^38}: y² + y = A(u)³, A = (u² + t²u + t)/(t³ + 1); Frobenius = [−2^{19}]; no primitive-root prime ℓ has a nonzero ℓ-torsion point on Θ | none | **confirmed, with independent computation of mine**. The polynomial identity (u² + t²u + t)³ + (tu² + u + t²)³ = d(u³ + 1)² + d²(u³ + 1) holds over F₂[t,u] (sympy, modulus 2). The prime list ℓ = 19m + 1 ≤ 704 is 191, 229, 419, 457, 571, 647, with ord_ℓ 2 = 95, 76, 418, 76, 114, 323. At ℓ = 419, g = 2^{19} = 119, and the pairs (1,418), (71,69), (350,348) all have difference 2 (I also found a difference with 6 representations in H ∪ {0}), against the bound of 2. The geometric claims (two-rank 0, Θ = C − P, J_C ~ E²) are carried from the run and its B.23 source. It refutes our own route 2, not A1. |
| A07 | generic positive-rank counterexamples to prime-order incidence over finitely generated fields (transcendental moduli) | none | statement level. |
| A08 | over finite fields no fixed finite list of primes serves every curve of 2-rank one or two; ordinary case: no finite list of odd degrees | none | statement level (credited to Successor A.16). |
| A09 | C/F₂: Y² + X²Y = X⁵ + X; R = (u,v) over F₁₆; O(R − P) has order 13 and lies on the Raynaud theta divisor; ord₁₃ 2 = 12 | none | statement level. The run records two independent implementations and a point-count check; I did not run them. ord₁₃(2) = 12 is right. |
| A10 | order 3 is excluded on every nonordinary genus-two base | none | statement level. |
| A11 | the sufficient condition weakens to theta torsion of exact odd prime-power order n with ⟨2, −1⟩ = (Z/n)^×; the primitive factor is Prym(D_n/D_{n/ℓ}) | none | statement level (the run records three whole-proof readings). |
| G01 | effective Chebotarev avoiding a finite set S, by adjoining √m (m = rad(2∏S)) so that every p ∈ S ramifies | ζ of L(√m), ζ_Q: M in general, A_D if L(√m)/Q is abelian | statement level; the √m device is correct and the scope is right. |
| G02-G05 | finite trace comparison; an explicit uniform trace bound; the limit of trace separation; explicit prime bounds for two LM7 predicates | M (A_D for abelian fields) | statement level. |
| G06 | LM8 A.32-A.33 factors y² = x³ − 3x ± 6 (non-CM, bad primes {2,3}): under M, mod-ℓ surjective for ℓ > 964 log 6 + 5760 (Mayle-Wang); an unconditional adelic index bound (Lombardo) | M; none | statement level. Scope right: Mayle-Wang's GRH is for the division fields, which are non-abelian. |
| T01 | under A_D, for N ≥ 3 the primes p ∤ N below 3(log N)² generate (Z/N)^× (Bach 1990 Thm 3, p. 372); the prompt's coefficient 2 is Thm 2, which allows non-units | A_D | **confirmed** (the U₁₂ example, {1,5} omitting 2 but not 7, is right). Agrees with CX_GRH CX-N02 and ALPOGE_BRIDGES CC-C04. **This corrects our prompt and the Fable suggestion 7.** |
| T02-T07 | finite cyclotomic certificates for the 53 identified GT moduli (4,825 unit words below the strict coefficient-2 bound); LLS v3 criterion; coefficient 2 for N ≥ exp(300) under A_D | A_D; none for the finite checks | statement level; the computations were not rerun by me. |
| R01-R03 | row audit: 800 full statements, 591 proof blocks; the RH/GRH flags are false positives for conditional dependence; fixed-prime criteria are not Artin-existence theorems | — | statement level. **Incomplete by the run's own count:** 390 register statements and 209 LM7 proof blocks are missing. |

**Counts.**
- Read in full and confirmed: 7 (A01, A02 as a transfer, A03, A04, A05 at the level of the argument, A06 with
  computation, T01).
- Statement level, no fault found: 20.
- Gaps: 0. Refuted: 0. The run's own refutations (A04, A06, and R02 on the flags) are correct where I read them.

## 2. What is new

- **A1 is proved, and without GRH (A05).** This is the main fact of the checkpoint for us. The prompt asked for A1 through
  Hooley and Masullo, and it assumed A1 open with route 2. In fact our own later run ANABELIAN_A1 (checkpoint 03)
  already had an unconditional proof. AN_GRH recovered it, rebuilt it in full, and had it whole-read. Our records were
  behind our runs.
  - **Literature:** Saïdi-Tamagawa (2009) prove separation of decomposition groups only outside a finite exceptional set
    E_C. The Kummer step 5 removes the exceptional set. Whether this full injectivity for the prime-to-p geometric
    quotient is known (Tamagawa 1997 has it for the full π₁ over finite fields; later work by Saïdi, Tamagawa and others)
    is the gate. Not searched by me.
- **Route 2 is now precisely obstructed.** A06 gives an explicit curve on which the universal theta-primitive-root
  condition fails, though A1 holds there (two-rank 0). A11 weakens what route 2 would need, to prime-power order with
  ⟨2, −1⟩ = units. A07 and A08 show that no uniform prime list works.
- **T01 corrects a constant we gave the run** (2 → 3 for generation by units). Three runs of tonight agree on it.
- G01 to G06 are standard effective-Chebotarev and Galois-image material with correct scope. G06 puts actual constants on
  the LM8 factors.

## 3. The scope of the two proofs

- **None:** A01, A03 to A11, R01 to R03, the finite GT checks T02 to T05, and A05, the main result.
- **A_D:** T01, T07, and G01 when L(√m) is abelian.
- **M:** A02 (Hooley; the Kummer fields K_n(2) are non-abelian), G01 to G05 in general, G06's surjectivity bound.
- **Beyond both:** nothing used. Artin holomorphy is not needed for Hooley's argument, which needs only Dedekind zeta
  functions.
- **Masullo locators:** the run cites §1.2 and records 13.3.1.2 as blank, in agreement with CX_GRH, ZETA_TWO and
  ALPOGE_BRIDGES. No formula from Masullo's body is used, so no mistranscription check arises.
- **Flags:** none of the statements I read claims more than its input gives.

## 4. Integration, with the attack each finding opens

1. **The A1 status in our records.** The anabelian intake of 14 Nov (`INTAKE_ANABELIAN_149_FINAL_20261114.md`, §3.3(3)
   and §5(a), route 2) and every ledger carrying A1 as open should read:
   - "proved, unconditionally: ANABELIAN_A1 checkpoint 03, A.2-A.5, A.14-A.19, A.30-A.33; reconstructed and whole-read
     as AN_GRH A05 (21 Nov)";
   - route 2 is not needed.

   The main session should check whether ANABELIAN_A1 checkpoint 03 was ever taken in. If it was not, that intake is due,
   and its paper is the source of record.
2. **Cote 149, scans 35-36.** Grothendieck's question, whether point separation holds in characteristic p with the
   prime-to-p geometric group and whether the covering condition forces P = Q, is answered **yes** for curves (A05 with
   A01). TRANSCRIPTION_NOTES.tsv records a reading fix: "a cover of X" on scan 36 must be read as a cover of Y. That fix
   needs a visual check of scan 36 before it goes into the transcription. The next attack is the higher-dimensional and
   section-surjectivity forms, which A05 explicitly leaves open.
3. **Route 2 as mathematics in its own right.** T(C), the positive-2-rank theta incidence with ⟨2, −1⟩ = units, is now a
   clean question about genus-two curves in characteristic 2 (A11; A09 gives an instance). The attack it opens:
   - decide whether every ordinary genus-two curve over F̄₂ carries theta torsion of some odd prime-power order n with
     ⟨2, −1⟩ = (Z/n)^×;
   - the run's A12-A14 (Lang-cover dominance, the order-4159 example, polynomial growth of fixed-ℓ primary parts) are
     working on exactly this.

   It no longer bears on A1.
4. **GT̂₀ certificates (T01-T07).** Our GT shadow computations should cite T01 (coefficient 3, A_D) and T05 (the 53 moduli
   checked directly) as the certificate for the cyclotomic coordinate of each finite level. Fable's suggestion 7 and the
   bridges notes that say "2 log² N" must say "3 log² N" for units.
5. **LM7 and LM8 rows.** G05 and G06 give the explicit bounds. G06's ℓ > 964 log 6 + 5760 is under M, and Lombardo's index
   bound is unconditional. Mark the LM8 A.32-A.33 rows "M for the explicit surjectivity bound; unconditional index
   bound".
6. **Prompt 30's successor:**
   - drop item 1 (A1 via Hooley) as settled;
   - re-aim at the positive-rank theta incidence (A11 to A15);
   - finish the row audit once the 390 missing register statements are recovered from the ANABELIAN_A1_SUCCESSOR and
     GT_TOWER_CHECK finals.

## 5. Prompt updates for the successor

- Attach ANABELIAN_A1 checkpoint 03 and the successor finals directly, so that no recovery search is needed.
- State A1 as proved (cite A05) and ask for the next question in the line: section surjectivity, or point separation in
  higher dimension for the prime-to-p quotient (cote 149, the text after scan 36).
- Keep the theta-incidence problem as a separate main question, with A06, A09, A10 and A11 as the known data.
- Correct the Bach constant in the prompt text (3, not 2).

## 6. Hexagon readiness (the five tests)

- **A05 (A1: prime-to-p point separation for hyperbolic curves over finitely generated fields of characteristic p, with
  the full arithmetic quotient).**
  - 1, complete: yes, in the reconstruction.
  - 2, self-contained: yes; its inputs are SGA 1 and Saïdi-Tamagawa 2009. No A_D or M.
  - 3, stable: the run's final may refine the write-up. **No literature search yet.** This is the decisive gate: if the
    removal of Saïdi-Tamagawa's exceptional set is known, it fails.
  - 4, checked: ANABELIAN_A1 itself, AN_GRH's whole-proof readings, and this intake's full read, with Steps 1-2 at the
    level of the argument. An independent re-proof of Steps 1-2 by a reader in anabelian geometry is still wanted.
  - 5, interest now: moderate to high in the anabelian community. It is not tied to tonight's RH news.
  - **Candidate: one gate (literature) plus a re-proof of Steps 1-2.** Worth flagging to the user as the strongest
    post-ready result of this round, but not as urgent.
- **A06 (an explicit curve refuting the theta-primitive-root condition).** It is complete and checked by computation, but
  it refutes a condition internal to our programme. Fails test 5. Not a post on its own; it belongs as an example in a
  post on A1 or on theta incidence.
- **A09 / A11 (theta incidence).** Not stable: A12 to A15 are in progress. Wait.
- **T01 / G-findings:** known material with constants; they fail 3 or 5.
