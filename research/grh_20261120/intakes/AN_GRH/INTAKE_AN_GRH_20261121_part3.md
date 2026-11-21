# Intake of AN_GRH (prompt 30), part 3: the final return, 21 Nov 2026

Intake by Claude Opus 5.5 at effort high (agent af2a18f62da23b48e), launched by the main session (Claude Opus 5.5 at
effort max). The run: GPT-6 Astra (ChatGPT Pro mode); it writes "effort not exposed". Parts 1-2 read checkpoints 02 and
03.

## 0. What was read, and the scope

- **Return folder:** `research_returns\AN_GRH_final_20261121T0821Z_unzipped`, the run's own final. Its root AN_GRH.tex is
  byte-identical to `final/AN_GRH.tex`: 15,616 lines, a 185-page PDF, findings A01-A52 (no A28), 1,400 question rows and
  1,391 check events.
- **Stopping:** the run stopped by our rule at review 06 (08:15 UTC), after two consecutive reviews without main-route
  movement. All four workstreams are stopped.
- **Read:**
  - README.md (all);
  - LEDGER.md from the A51 integration (07:37) to the final freeze (08:18), including the stopping review and its state
    table;
  - in AN_GRH.tex, **A46 in full** (lines 10396-10682), **A33's statement and proof steps 1-2** (lines 5767-5960), the
    statements of A45 and A52, and the Faltings/Tamagawa comparison (lines 14900-14935);
  - the A05 rows of CHECK_EVENTS.tsv.
- **Statement level:** A21-A27, A29-A32, A34-A44, A47-A51, from the README summary and the ledger only. I did not open
  their proofs.
- **Changes to parts 1-2:** none. A01-A06, A18, A19 and T01 are unchanged in content: A05 is still at 289 lines, and no
  ledger entry corrects any of them. A05's check events in the final are three same-model targeted proof checks, by the
  run's /root/effective_galois agent twice and by /root once.

## 1. What the run settled, and what it left open

**Settled.**
- **A1 (cote 149, scans 35-36)** holds without GRH (A05), for hyperbolic curves over fields finitely generated over F_p,
  with the prime-to-p geometric quotient and the full arithmetic quotient. Unchanged since part 1.
- **The requested Hooley route** is precisely located: M supplies Hooley's Kummer Dedekind-GRH (A02), but the geometric
  supply of a suitable cover is not proved.
- **The sufficient criterion is now clean in every genus and characteristic (A46):** one geometrically cyclic étale cover
  of odd degree prime to p, pointed over P, whose actual primitive subvariety P_n has P_n(L)[p^∞] = 0, separates P from
  every other point. Geometric p-rank zero of P_n suffices.
- **The finite GT certificates** (T01-T07; 53 moduli, 4,825 unit words) and **the effective Galois bounds** (G01-G06),
  as in parts 1-2.
- **The obstructions,** each with an exact failure point:
  - A06: the universal primitive-root theta bridge fails;
  - A07, A21, A22: no fixed finite prime support works;
  - A23, A27: the older numerical tests fail over all extensions;
  - A36-A43: a single prescribed reflection cover can fail the detector;
  - A48: twists cannot repair a fixed pointed group;
  - A50-A52: integral-operator and lattice-index limits.

**Left open.**
- A universal supply theorem: for every curve and point, an allowed pointed cover with P_n(L)[p^∞] = 0 (A46), or a small
  integral annihilator (A52), or another separating mechanism.
- In characteristic 2 and genus 2, the residual target is ordinary genus-two Jacobians with Rosati-fixed O₅ = Z[(1+√5)/2]
  real multiplication (A33).
- The row audit: 390 register statements and 209 LM7 proof blocks are missing.
- The full GT register and its actual quotient maps.

**The central point for our records.** Everything open in this run concerns an *alternative mechanism* for A1, the route
through covers and theta incidence. A1 itself is proved by A05. Route 2 is now a question about the arithmetic geometry of
cyclic covers: whether primitive Prym factors of p-rank zero, or p-primary-trivial ones, always exist pointed over a given
point. It is not a gate on any statement of Grothendieck's.

## 2. Verdicts on the new findings

| id | statement (short) | verdict |
|---|---|---|
| **A46** | the rational primitive criterion in all characteristics and genera, with no ordinarity or elliptic-quotient hypothesis and no constant deck group needed | **confirmed in full.** p_n = n·e_n ∈ Z[G] with c_n(a) = Σ_{d\|(n,a)} d μ(n/d) (Ramanujan sums) is Galois-stable, so P_n is defined over L. A·p_n = nA, so A·δ = 0 from P_n(L)[p^∞] = 0. A(Q′ − P′) is a divisor with 2^{ω(n)} simple zeros and poles; f is separable. Poonen Cor 2.3 gives e \| d and g(M) ≤ (d/e − 1)²; n > (d − 1)² excludes e = 1; the G-action on Z is free, so e = 2. **The new step:** the quadratic involution τ commutes with G and swaps the two deck orbits, τP′ = σ^jQ′. τ-invariance of div f gives Aσ^{−j} = −A in Z[G], and iterating over the odd order of σ^j gives A = −A, impossible. I checked the orbit-coefficient comparison. The sign argument works in characteristic 2 because it uses integral divisor coefficients. This removes A18's Deuring-Shafarevich computation. |
| A33 | in characteristic 2, point separation for all genus-two curves reduces to ordinary genus-two curves E whose Jacobian has Rosati-fixed O₅ multiplication | **steps 1-2 confirmed; step 3 statement level.** Checked: the lift τ of the hyperelliptic involution inverts σ and τ² = 1 (2a = 0 mod 5); g(E) = 2 from the different count 10 = 2·2 + 6; 𝓑 ~ J_E × J_E; f_𝓑 ∈ {0, 4}, since F₂[Z/5] has only the trivial simple module and one of dimension 4 (ord₅ 2 = 4); T = v_*σv^* satisfies T² + T − 1 = 0 by (σ + σ^{−1})² + (σ + σ^{−1}) − 1 = Σσ^i = 0 on 𝓑; T is Rosati-fixed. Step 3, the transfer of one collision to two collisions on E, was not read. **Weight:** since A05 proves A1, (DR.1) is already true. A33 reduces only the route-2 mechanism. |
| A45, A47, A52 | bounded-exponent and integral-annihilator criteria: a collision with n > (2M − 1)² or (‖A‖₁ − 1)² < n forces a separable wild map C → E of degree p^a ≤ g − 1 totally ramified at P and Q; hence separation when 2 ≤ g ≤ p | statement level. The mechanism is the A46 argument with bounded instead of zero p-primary torsion. |
| A21-A27, A29-A32, A34-A44, A48-A51 | examples (degrees 7, 13, 15, 19, 39, 4159), detectors, and failures of shortcuts | statement level (README and ledger summaries). |
| Faltings 840 comparison | Tamagawa's full-π₁ point-separation argument (Faltings, Bourbaki exp. 840, §3 Thm 3, pp. 134-135) uses a level annihilating the whole J(F_q); at prime-to-p levels it leaves the p-primary residual | **accepted as a literature locator.** This is exactly the gap that A05's Kummer step 5 closes, so it is the key comparison for A05's novelty. |

**Counts for part 3.**
- Confirmed with every step checked: 1 (A46).
- Partly confirmed: 1 (A33, steps 1-2).
- Statement level: about 30 (A21-A52, apart from A46 and A33).
- Gaps: 0. Refuted: 0. Changes to parts 1-2: none.

## 3. What is new

- **A46** is the clean form of the route-2 criterion. It is new as stated in our work and plausibly in the literature; not
  searched.
- **A33's O₅ reduction** brings real multiplication by Q(√5) into the characteristic-2 genus-two problem through a quintic
  reflection quotient. That is a nice structural fact. The construction (a dihedral D₅ cover of P¹) is classical in
  spirit: Humbert surfaces, and the Prym of a cyclic quintic cover.
- **The Faltings 840 comparison** is the right literature anchor for A05: Tamagawa (full π₁) versus A05 (prime-to-p
  geometric group with the full arithmetic quotient).

## 4. The scope of the two proofs

Nothing new uses A_D or M, except where A02 and A17 already did (Hooley under M). A05, A33, A45-A52 and the examples are
unconditional. No statement claims more than its input gives.

## 5. Integration

1. **Our anabelian ledger**, intake of 14 Nov (`INTAKE_ANABELIAN_149_FINAL_20261114.md`, §3.3(3), §5(a)):
   - A1: "proved, AN_GRH A05 (from ANABELIAN_A1 cp03 A.2-A.5, A.14-A.19, A.30-A.33), unconditional";
   - route 2: "not needed for A1; as an alternative mechanism, reduced to A46 (any genus and characteristic) and A33
     (characteristic 2, genus 2: ordinary O₅-RM Jacobians)".
2. **Cote 149, scans 35-36.** In the transcription notes:
   - Grothendieck's characteristic-p question is answered yes for curves (A05);
   - his "covering condition forces P = Q" is A01's covering formulation;
   - the "cover of X" → "cover of Y" reading fix of TRANSCRIPTION_NOTES.tsv still needs a visual check of scan 36.
3. **Successor rows (ANABELIAN_A1_SUCCESSOR A.14/AC.11, A.4, A.37; A1 B.40):** A46 supersedes A.14's elliptic-quotient
   exclusion; A33 extends B.40's reflection method from degree 3 to degree 5.
4. **GT shadow computations:** cite T01 (3 log² N under A_D) and T05 (the 53 moduli) for the cyclotomic coordinate.

## 6. Prompt updates for the successor (what it needs)

1. **Do not ask for A1 again.** State A1 as proved (A05) and attach A05's proof source
   (`final/proof_sources/a1_section.tex`) and ANABELIAN_A1 checkpoint 03.
2. **Ask for the next anabelian question in Grothendieck's line**, after cote 149 scan 36:
   - section surjectivity, the section conjecture, for the prime-to-p quotient over finite fields;
   - point separation in higher dimension (hyperbolic polycurves, Artin neighbourhoods), with A05's configuration method
     as the starting point.

   These are the open statements A05 explicitly leaves.
3. **If route 2 is kept, set it as a geometric question, not as a gate on A1:**
   - (a) for an ordinary genus-two curve E over F̄₂ with Rosati-fixed O₅ multiplication, and a point P, construct a
     pointed odd cyclic cover with primitive factor of 2-rank 0 (A33 + A46);
   - (b) or prove that such covers fail for some (E, P);
   - give A45-A52's criteria and the failures A36-A44 as known data, so that none is rediscovered;
   - the named next steps are a universal exponent or index bound for the actual primitive p-primary group (A51, A52),
     and prescribed reflection-orbit incidence (A36-A43).
4. **Recover the missing registers** (ANABELIAN_A1_SUCCESSOR's 210 and GT_TOWER_CHECK's 180 statements, the 209 LM7 proof
   blocks) and attach them, so that the row audit can finish.
5. Write the run's model as "GPT-6 Astra (ChatGPT Pro mode)".

## 7. Hexagon register changes (no edit made; for the main session)

**H07 (AN_GRH A05: A1 without GRH).** What the final return does to each test:
1. **Complete:** yes, unchanged; the final proof source is A05 at lines 630-918.
2. **Self-contained:** yes. Its inputs are SGA 1 (III 7.4, X 3.8-3.9, XIII 2.9-2.12, 5.2) and Saïdi-Tamagawa 2009
   (Prop 1.8(vi), Lemma 1.7, Remark 1.2). There is no A_D or M input.
3. **Stable:** now **yes on our side**: the run has ended and A05 did not change. **Literature still not searched.** The
   final adds the key locator: Tamagawa's full-π₁ theorem (Faltings, Bourbaki 840, §3 Thm 3) does not cover the prime-to-p
   case, as the run checked. The search should cover:
   - Saïdi-Tamagawa (2009 and later prime-to-p papers);
   - Hoshi and Mochizuki on cuspidalization;
   - Sawada;
   - any prime-to-p point-injectivity statement for curves over finite fields.
4. **Checked:** three same-model whole readings in AN_GRH, and this intake's full read (Steps 3-6 in full, Steps 1-2 at
   the level of the argument). **Gate: an independent re-proof of Steps 1-2** (the exactness (A05.1) of the cuspidally
   pro-r configuration sequence, and cusp transport) by a reader in anabelian geometry. That could be a field expert of
   ours, or an independent Pro run on A05 alone.
5. **Of interest now:** moderate to high (anabelian geometry); not tied to tonight's news.

**Gates left for H07:** the literature search, and the independent re-proof of Steps 1-2.

**H08 (ALPOGE_BRIDGES BR-12302):** not in this run; see ALPOGE_BRIDGES part 4.

**New candidate from this run: A46**, the rational primitive criterion.
- 1, complete: yes. 2, self-contained: yes (Poonen 2007). 4, checked: my full check.
- 3, stable: yes, the run has ended; but no literature search.
- 5, interest now: low on its own. It is best posted as a lemma inside the A05 note ("two mechanisms for prime-to-p point
  separation").

Not a separate entry.
