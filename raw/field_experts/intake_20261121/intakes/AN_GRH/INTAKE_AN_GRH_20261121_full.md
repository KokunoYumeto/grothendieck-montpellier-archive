# Full intake of AN_GRH (prompt 30), final return of 21 Nov 2026, 08:21 UTC

By Claude Opus 5.5 at effort max (agent a28ea31fa17dd65e1), 22 Nov 2026, at the main session's request (Claude Opus 5.5
at effort max), following the user's request of 21 Nov (~23:5x UTC): [the user's words, omitted]. The run is by
GPT-6 Astra (ChatGPT Pro mode). The earlier intake of this run, by af2a18f6, is in this folder; it recorded no
check events.

- **Check events:** `INTAKE_AN_GRH_20261121_full_CHECK_EVENTS.tsv`, 87 rows, run = AN_GRH in the who column.
- **Working files:** `_work_a28ea31f/`, with my own scripts `check_A06.py`, `check_A09.py`, `check_A13.py`,
  `check_A16.py`, `check_A27.py`, `check_A39.py`, the A05 re-proof `A05_steps12_reproof.md`, and the event batches
  ev_01-ev_38.
- **Running notes:** `agent_notes/a28ea31fa17dd65e1_NOTES.md`.

## 1. Scope: the statements of this run

The ledger's list of 304 ids for AN_GRH was LM8_PUSH cp17's register. The ledger builder had taken the first results
CSV in the return, `final/recovered/LM8_PUSH_cp17_text/LM8_PUSH_results.csv`, which the run had recovered as source
material. The id sets match exactly. The main session fixed the builder on 22 Nov.

AN_GRH's own statements are the 69 "Finding" paragraphs of `AN_GRH.tex`, plus the cited and rechecked result A28:
- S01-S02;
- A01-A52 (A28 is a "Cited and rechecked result", the recovered successor A.26);
- G01-G06;
- T01-T07;
- R01-R03.

That makes 70 statements, and all 70 have check events. Section 6 gives AN_GRH's own audit verdicts on the 304 LM8
rows.

## 2. What was checked, by type and depth

**Events by type (108 in all, after the second and third passes of 22 Nov; the first pass had 87):**

| Type | Events |
|---|---:|
| Targeted proof check | 79 |
| Computation or formal certificate | 24 |
| Independent re-proof | 4 |
| Carried as background without fault found | 1 |

- The four independent re-proofs are A05 Step 1, A05 Step 2, A10 and G04.
- The one background event is A28, the cited recovered result.
- The 24 computations are my own scripts, never the run's.
- Some findings carry several events (a partial check followed by its completion, or a proof check together with a
  computation). Every one of the 70 statements has at least one event.

**By depth (the state after the third pass):**
- **Every step re-derived** (independent re-proof, or a targeted check that re-derives the whole proof):
  - A01-A05, A07-A31, A33-A35, A37-A49 and A51-A52;
  - G01-G05;
  - T01-T05 and T07;
  - R03.
- **My own computations confirm the finite content** of A06, A09, A13, A15, A16, A20, A24, A27, A31, A32 (the table
  OR.9), A33 (the RM example), A36 (the table NF.5), A39 (the identities, and the Riemann-Roch rank certificate
  together with RPT.12), A43 (ring identities), A44 (the example numbers), A45 (the degree-39 example), A50 (the code
  weights PP.7), A98-type certificates, G06, T03, T05 and T07. Specifically:
  - point counts, Weil polynomials and resultants;
  - norm identities over F_8, F_16 and F_256;
  - the order tables, and genus-two Cantor arithmetic over F_256;
  - the 53 unit-generation moduli of T05;
  - the LLS enclosures of T07.
- **Still partial:**
  - A35 (its RM refinement only);
  - G06 (the Mayle-Wang constant only);
  - R01 and R02 (counts not all recounted);
  - A49 (proof re-derived, its certificate not rerun);
  - A45's exponents (ND.19) and ordinarity step (ND.21)-(ND.22), which rest on BE.8 and on the Deligne-Katz
    comparison.
- **Statement read only:** none remain.

## 3. Refuted, corrected, errata

- **No finding of the run is refuted.** I found no mathematical error in any proof I checked.
- **Places a publication should spell out** (correct, but terse):
  - A05 Step 1: that the image of H in Aut(L^(r)) has pro-r closure (the Frattini-kernel fact at every characteristic
    level);
  - A05 Step 1: Λ ∩ T' ⊂ ker(Λ → Q), which needs Λ ∩ H = L.
- **Not settled by this intake:**
  - A33: the absolute simplicity of its RM-free example;
  - A06: the stronger B.23 claim, whose certificates the run reran and I did not;
  - A45: the conductor-39 example;
  - the tables named under "Partial" above.
- **One slip of my own, corrected in the TSV:** a transcription of T07's digits. The run's enclosures are right.

## 4. What is new

These are the run's results against our records. The literature status of each is the run's own, except where a gate
is named.

- **A46, the new criterion.** One pointed, geometrically cyclic étale cover of odd degree n prime to p, whose
  primitive factor has no rational p-power torsion, separates the point section of P from every other point. It holds
  in every genus and every positive characteristic, with no elliptic or ordinarity exception.
  - The decisive step is new and short: the integral ±1 signs of the projector divisor A(Q'-P') are incompatible with
    the involution of a degree-two quotient (Aσ^(-j) = -A in Z[G]).
  - A47 and A52 generalize it to bounded torsion exponent and to arbitrary small annihilators, with an exact wild
    elliptic obstruction.
- **A05, A1 without GRH.** This is a reconstruction of our recovered ANABELIAN_A1 later-run proof: cuspidal
  transport, the integral Frobenius trace comparison, and Saïdi-Tamagawa's finite exceptional set. Our records listed
  A1 as open. The run claims no originality.
- **Criteria and counterexamples for the older theta route:**
  - A03 and A11: the theta-incidence bridges, in prime and prime-power form;
  - A15 and A18: composite conductors;
  - A29 and A34: canonical-class and actual-exponent criteria;
  - A06, A07, A08, A14, A21, A22, A37 and A44: refutations or limits of the universal assertions, and generic
    avoidance;
  - A09, A13, A16 and A31: explicit witnesses;
  - A23, A25, A27, A30, A36, A38, A41 and A43: failures of the sufficient numerical tests.
- **Analytic-input accounting:**
  - S01: the GRH draft's Theorem 13.3.1.2 has no statement; I re-extracted page 522 of the source PDF;
  - S02, A02, A17 and A24 (densities conditional on M);
  - G01-G06: effective Chebotarev under GRH, with explicit constants;
  - T01-T07: Bach and LLS, and unconditional certificates;
  - R01-R03: source coverage and flag audit.

## 5. Hexagon readiness (field_experts/HEXAGON_CANDIDATES.md, the five tests)

**H07 = A05 (A1 without GRH).**
- **Complete:** yes. The proof is written in full, and the two terse places above should be spelled out in a post.
- **Self-contained:** yes. Its inputs are SGA 1 (III 7.4; X 3.8-3.9; XIII 2.9-2.12, 5.2), Weil I, and Saïdi-Tamagawa
  2009 (Prop. 1.8(vi), Lemma 1.7, Rem. 1.2). It uses no GRH and no Masullo.
- **Checked:** yes, as of this intake. Steps 1-2 are independently re-proved and Steps 3-6 have a targeted check, with
  check events A05.Step1, A05.Step2 and A05. Before submission, every page of the post text must still be read.
- **Of interest now:** yes.
- **One gate is left: the literature search (test 3).** Is point separation in the geometrically pro-prime-to-p
  arithmetic fundamental group already known for curves over finitely generated fields of characteristic p?
  - The search should be anchored on Saïdi-Tamagawa's work on prime-to-p anabelian geometry over finite fields and on
    Tamagawa's results.
  - The run itself calls ST2009's exceptional-set theorem "already known".
- H07 is therefore one gate away. Test 5 is strong, so it should be flagged to the user now.
- **Test 3, the result of the search (22 Nov; section 8).**
  - In the sources we could read, A05 is new. It removes Saïdi-Tamagawa's exceptional set (ST2009, Prop. 1.8;
    ST2018, introduction, pp. 4-5) for rational points.
  - One source is unread: Stix, LNM 2054, Ch. 7, which is paywalled; a library check would close the search.
  - The post should cite ST2009 and ST2018 as the state of the art and claim nothing beyond them.

**A46.**
- **Complete:** yes; my targeted check found no gap.
- **Self-contained:** yes; its input is Poonen's Castelnuovo-Severi consequence (Gonality of modular curves,
  Prop. 2.1, Lemma 2.2, Cor. 2.3).
- **Stable:** yes, within the run. A47 and A52 extend it and recover it as a special case.
- **Checked:** half. It has a targeted check, every step re-derived, with numeric checks of the group-ring identities.
  It still needs an independent re-proof.
- **Gates:** a literature search (point separation by small-degree functions on odd cyclic covers; Pop-Saïdi;
  Sarashina), and an independent re-proof.
- **The search of 22 Nov (section 8):** no reference was found, so the question is not settled. The independent
  re-proof is still to be done. A47 and A52, now re-derived in full, extend A46 and recover it as a special case.
  That confirms the statement's stability, but it is not a second proof of A46 itself.

## 6. AN_GRH's audit verdicts on the 304 LM8_PUSH cp17 rows (QUESTIONS.tsv, AUDIT:LM8_PUSH:*)

AN_GRH screened LM8's rows for analytic inputs only; it did not check their proofs. Its verdicts:

| Verdict | Rows |
|---|---:|
| "No curated analytic input identified by term/dependency screen; not a proof-independence certificate" | 254 |
| "Analytic input already unconditional; this hypothesis change ..." | 48 |
| The qualitative open-image and commutator Zariski-density rows A.32 and A.33 (refined numerically by G06) | 2 |

- 50 of the rows are linked to findings: see `_work_a28ea31f/lm8_audit_extract.tsv`.
- I filed no LM8_PUSH check events, because I checked none of LM8's proofs.
- I did read row A.69's text, to confirm R02's reading of "DS/RH" as Deuring-Shafarevich and Riemann-Hurwitz.

## 7. What a further pass should do

Items 1-3 and 5 of the first-pass list were done on 22 Nov (sections 8-9):
- A49-A52 checked in full;
- the tables of A32 and A36, and A39's Riemann-Roch certificate, recomputed;
- A40, A41, A43, A44, A45, A47 and A48 finished;
- the H07 search done, except Stix's LNM 2054, Ch. 7, which is paywalled.

What remains:
1. Make an independent re-proof of A46 (Hexagon test 4).
2. Rerun A49's certificate from a separate folder.
3. Recompute A45's (ND.19) and (ND.21)-(ND.22).
4. Recount R01 and R02, and finish the RM refinement of A35 and G06's Mayle-Wang constant.
5. Read Stix, LNM 2054, Ch. 7 (by library access), to close the H07 search.
6. Check the run's remark on Asvin2023, Lemma 11, against that paper.

## 8. Literature for H07 (A05) and A46 (search of 22 Nov 2026, freely available sources)

### H07 (A05): partly known, and the full statement appears open in the literature checked

**Known: the full profinite case.** Separation of points by decomposition groups or sections in the full arithmetic
fundamental group π_1(X) is known: Tamagawa for affine hyperbolic curves over finite fields, Mochizuki for proper ones.
Saïdi-Tamagawa state this in the introduction cited below.

**Only "almost injective" in the prime-to-p case.** Saïdi-Tamagawa, "A prime-to-p version of Grothendieck's anabelian
conjecture for hyperbolic curves over finite fields of characteristic p > 0", Publ. RIMS 45 (2009), 135-186
(arXiv:0801.1452):
- In the introduction (p. 3 of the arXiv PDF) they say that the map x ↦ [D_x], from closed points to conjugacy classes
  of decomposition groups in the geometrically prime-to-p group Π_X, is known to be injective in the full profinite
  case. In their case they are "only able to prove that the above map is almost injective, i.e., injective outside a
  finite set E_X".
- The exceptional set is that of their Definitions 1.3, 1.5, 1.10 and Proposition 1.8(vi). A05 Step 4 uses exactly
  this.

**Still outside exceptional sets in 2018.** Saïdi-Tamagawa, "A refined version of Grothendieck's anabelian conjecture
for hyperbolic curves over finite fields", J. Algebraic Geom. 27 (2018), 383-448 (arXiv:1708.08773).
- A secondary summary (the Exeter repository record) describes its bijection between closed points as one "outside
  their exceptional sets".
- I did not verify this in the full text.

**No later removal found.** The search found no paper that removes the exceptional set, or that proves injectivity on
all rational points, for the geometrically prime-to-p (or pro-Σ) quotient. The 2024 arXiv paper 2407.09906 (Yamaguchi,
metabelian genus-zero Grothendieck conjecture) does not address it.

**Verdict: new as far as this search reached; one more search before a post.** A05 removes the exceptional set for
rational points over finitely generated fields of characteristic p. Its means are cuspidal transport with integral
Frobenius information, plus Saïdi-Tamagawa's almost-injectivity. Against the Saïdi-Tamagawa line this looks new.

Not yet searched:
- Stix, Rational points and arithmetic of fundamental groups (LNM 2054), the injectivity chapter;
- Mochizuki's and Tamagawa's later work;
- Saïdi-Tamagawa's later papers on the "tame" or "Σ" versions.

H07 can go forward once that search is done. Its post should cite Saïdi-Tamagawa 2009, introduction and Prop. 1.8, as
the almost-injective state of the art.

### A46: not settled; no reference found in this search

- I found no published statement of A46's criterion: one pointed odd cyclic cover whose primitive factor has no
  rational p-power torsion separates points, in every genus and characteristic.
- The run attributes the composite-projector argument to our recovered ANABELIAN_SUCCESSOR A.14 (AC.11), which carries
  an extra elliptic-quotient hypothesis. The sign argument that removes that hypothesis is new against our records.
- A dedicated search is still needed: separation of points by p-rank-zero or new-ordinary cyclic covers (Pop-Saïdi;
  Tamagawa's p-rank arguments; Sarashina), and Castelnuovo-Severi methods in anabelian geometry.
- A46 also still needs an independent re-proof (section 5).

## 9. Second pass, 22 Nov: the tables

The tables of A32 and A36 are now recomputed exactly by my own genus-two Cantor arithmetic over F_256
(`_work_a28ea31f/cantor_f256.py`, independent of the run's implementations):
- A32: Δ has order 13, and the occupancies (44,19,18,18,16,19,16,16,19,16,18,18,19) are as stated in (OR.9).
- A36: Δ has order 5, and the occupancies (76,45,45,45,45) are as stated in (NF.5).

Both findings are therefore fully computed. (A39's Riemann-Roch certificate was recomputed in the third pass, below.)
- Second pass, also done:
  - A49 is now a targeted check, every step re-derived; its certificate was not rerun.
  - A50: the norm bound was re-derived, and my own computation reproduces the weight distribution (PP.7) of the
    length-31 code exactly.
- The items left open by the second pass were all done in the third pass (below).

### Third pass, 22 Nov: the partial rows completed

Every item the coordinator listed is now checked. The events are in the TSV, ev_42-ev_54 of the work folder.

- **A39, the Riemann-Roch certificate, recomputed** (`_work_a28ea31f/check_A39_rr.py`). My own Laurent-series code
  over F_256 computes the expansions at P and at Q and builds the basis (RPT.9): 31 functions per character, 155 in
  all, each V̄_i Hensel-lifted and checked.
  - The 160 × 155 system has rank 155. So no function has divisor 32(4Q − Σσ^jP), and 32Z_{R_t} ≠ 0.
  - The positive certificate (RPT.12) gives order 4 with leading coefficient 189 at P and at Q, as stated.
  - Step 4 is re-derived. A39 now holds in full.
- **A40 and A41**: every step re-derived. ord_4159(2) = 2079 was computed, and the bound of at most 34 excluded
  parameters, and with it the at least 95 good ones, was rechecked.
- **A43**: every step re-derived. The ring identities (RWI.8), (RWI.12) and (RWI.15) were checked by a Gröbner basis
  (`check_A43.py`).
- **A44**: every step re-derived, including the odd auxiliary-prime supplement. My computation (`check_A44.py`)
  confirms the example numbers:
  - #A(F_{2^16}) = 65760² and S_A = {3,5};
  - the identity (CT.15), and that the model is the A13 curve.
- **A45**: every step re-derived, including the semilinear descent (SD). Its degree-39 example was recomputed with my
  own Cantor arithmetic (`check_A45.py`):
  - all 256 labels and the counts (ND.17);
  - the Frobenius multiplier 34 on every point, and the four k-points;
  - (ND.20) and the Bezout certificate.

  Not recomputed: the exponents (ND.19), which come from the module argument BE.8, and the ordinarity step
  (ND.21)-(ND.22), which rests on the Deligne-Katz comparison as in A32.
- **A47 and A48**: every step re-derived, including the coarse-Weil limitation and the twist obstruction.
- **A51 and A52**: every step re-derived, including all supplements (FX, TD, FI, WV; TN, PD, CP).
- Citations inside these findings are carried as background, not checked at their locators. These are Poonen 2007,
  the Stacks tags, Milne, Katz, Deligne, Crew, Ozman-Pries, Waterhouse, Diem and Kumar-Mukamel.
- **One point for the record (A51 supplement).** The run says that Lemma 11 of Asvin G. (Asvin2023) fails integrally.
  Its counterexample is correct: [ℓ]^* = ℓ on H^1(E, Z_ℓ), with cokernel (Z/ℓ)². I did not check the remark against
  that paper itself. Before it is used or reported, someone should read Lemma 11 and its proof in the paper.
- No finding is refuted in this pass.

### H07, the search continued (22 Nov, third message)

**Saïdi-Tamagawa 2018, the text itself** (arXiv:1708.08773; J. Algebraic Geom. 27 (2018), 383-448), introduction,
pp. 4-5 of the arXiv PDF:
- The local theory gives "a set-theoretic bijection" between the closed points of X and Y "outside some 'exceptional
  sets' E_X ⊂ X^cl and E_Y ⊂ Y^cl", compatible with decomposition groups.
- The paper adds that "at this stage we are even not able to prove that the exceptional sets E_X and E_Y are finite.
  This causes a very serious difficulty", which it overcomes for the isomorphism theorem by a refined fundamental
  theorem of projective geometry (§5).
- So in their geometrically pro-Σ setting the exceptional sets are not removed, and not even known to be finite.
  Injectivity of points into decomposition groups is not claimed.

**Stix, Rational Points and Arithmetic of Fundamental Groups: Evidence for the Section Conjecture**, LNM 2054
(Springer 2013), Chapter 7, "Injectivity in the Section Conjecture" (doi:10.1007/978-3-642-30674-7_7).
- The book is not freely available, and I found no free copy, so only the chapter abstract was read.
- The abstract covers the injectivity of the profinite Kummer map in the arithmetically relevant cases, and two
  approaches, the second being Mochizuki's anabelian one. Nothing in it indicates the geometrically prime-to-p
  positive-characteristic case, where the abelian Kummer map kills J(K)[p^∞] and A05's nonabelian argument is needed.
- The p-adic transfer of the injectivity argument is in Stix, arXiv:0910.5009.

**Later work.**
- The search found no paper after 2009 that removes the prime-to-p exceptional set.
- arXiv:2407.09906 (Yamaguchi, the metabelian genus-zero Grothendieck conjecture) does not address it.
- arXiv:2610.24986 (The section conjecture for generic pointed curves, 2026) was not examined.

**Verdict for the post.**
- Point separation by the full profinite arithmetic fundamental group is classical (Tamagawa; Mochizuki).
- For the geometrically prime-to-p quotient over finite fields, Saïdi-Tamagawa proved only that points are separated
  outside a finite exceptional set: Publ. RIMS 45 (2009), introduction and Prop. 1.8. Their refined pro-Σ version of
  2018 still works outside exceptional sets that it cannot even show to be finite: J. Algebraic Geom. 27 (2018),
  introduction, pp. 4-5 of arXiv:1708.08773.
- **A05 removes Saïdi-Tamagawa's exceptional set for rational points.** For a smooth hyperbolic curve over a field
  finitely generated over F_p, distinct rational points have non-conjugate sections of the geometrically prime-to-p
  arithmetic fundamental group, with no exceptional set and no analytic input. It does so by cuspidal transport in the
  cuspidally pro-r configuration quotient (whose Steps 1-2 are independently re-proved here) combined with integral
  r-adic Frobenius information.
- In the sources we could read, this statement is new. The one source we could not read is Stix's LNM 2054,
  Chapter 7, which is paywalled; a library check of it would close the search.
- The post should present A05 as removing the exceptional set of Saïdi-Tamagawa 2009, Prop. 1.8, for rational points.
  It should cite that proposition and the 2018 introduction as the state of the art, and should not claim priority
  beyond them.
