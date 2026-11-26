# Intake pile, cluster LONGUE_MARCHE_B: anabelian geometry and the Grothendieck–Teichmüller side of "La Longue Marche"

By Claude Opus 5.5 at effort high, cluster reader of the intake pile of 24–25 Nov 2026, launched by the main session
329fb1e6 (Claude Opus 5.5 at effort max). Written 24–25 Nov 2026. Brief: `BRIEF.md` in this folder. Work file:
`<local>/Documents\agent_notes\20261124T2112Z_Intake_pile_Longue_Marche_second_half_NOTES.md`.

All ten runs are by GPT-6 Astra (ChatGPT Pro mode); everything stated as a run's result is that model's claim unless a
check by someone else is named. "Checked here" means a check I made in this intake; each one has a row in the
`INTAKE_<RUN>_20261124_CHECK_EVENTS.tsv` files of this folder. Row-by-row table: `LONGUE_MARCHE_B_ITEMS.tsv`.

Where the runs are (all under `<local>/Documents\longue_marche_pro_pilot_20261104\answers\`; none is in
`research_returns`):

| Run | Newest return (folder) | Register (Proved/Known/Refuted or False/Open) | Rows checked by an intake (ledger, 24 Nov) |
|---|---|---|---|
| ANABELIAN_149_PUSH | `ANABELIAN_149_PUSH_final_20261114T1558Z_unzipped\ANABELIAN_149_PUSH\` | 221: 188 / 15 / 11 / 7 unresolved | 155 |
| FLAGGED_149 | `FLAGGED_149_unzipped\` (12 Nov) | 107: 57 / 15 / 31 / 4 | 19 |
| ANABELIAN_SUCCESSOR | `ANABELIAN_SUCCESSOR_final_20261116T1243Z_unzipped\` | 157: 138 / 6 / 8 / 5 | 19 |
| ANABELIAN_A1 | `ANABELIAN_A1_checkpoint_03_20261117T0413Z_unzipped\ANABELIAN_A1\` (final by the user's word) | 121: 105 / 1 / 8 / 7 | 8 |
| ANABELIAN_A1_SUCCESSOR | `ANABELIAN_A1_SUCCESSOR_checkpoint_05_20261118T0610Z_unzipped\` | 210: 190 / 2 / 10 / 8 | 1 |
| SECTIONS_OVER_Q | `SECTIONS_OVER_Q_checkpoint_17_20261116T1754Z_unzipped\` (account froze) | 245: 227 / 1 / 13 / 4 | 33 |
| SECTION_GHOSTS | `SECTION_GHOSTS_final_20261118T1305Z_unzipped\SECTION_GHOSTS\` | 228: 201 / 15 / 3 / 9 | 21 (but see §SECTION_GHOSTS: E.176–E.191 were refereed on 18–23 Nov outside the register) |
| EXIT_TOWER | `EXIT_TOWER_checkpoint_28_20261116T1443Z_unzipped\extracted_20261116\` | 283: 250 / 12 / 18 / 3 | 128 |
| DELTA_ON_GT | `DELTA_ON_GT_checkpoint_05_20261116T0650Z_unzipped\DELTA_ON_GT\` | 221: 175 / 15 / 17 / 14 | 91 |
| GT_TOWER_CHECK | `GT_TOWER_CHECK_checkpoint_10_20261117T0945Z_unzipped\GT_TOWER_CHECK\` (checkpoint 11 too large to save) | 180: 165 / 2 / 0 / 13 | 94 |

Prompts as sent: ANABELIAN_149_PUSH, ANABELIAN_A1, ANABELIAN_A1_SUCCESSOR (`04_`) and EXIT_TOWER in
`TO_SEND\_RAN_OR_NOT_YOURS\9_Archive_maths_prompts\ALREADY_RAN\`; ANABELIAN_SUCCESSOR in
`TO_SEND\_RAN_OR_NOT_YOURS\1_LM_maths_5_prompts_SEND_AT_NIGHT\ALREADY_RAN\`; SECTIONS_OVER_Q, SECTION_GHOSTS,
DELTA_ON_GT, GT_TOWER_CHECK in `longue_marche_pro_pilot_20261104\pro_prompts_draft_20261111\ALREADY_RAN\`. I did not
locate FLAGGED_149's prompt in a bounded search. I took the questions from the runs' own item tables and did not reread
the prompts in full.

---

## The cluster's most interesting items, ranked by usefulness

**1. Relation (IV) of Nakamura–Schneps holds on all of the profinite GT̂; every element of GT̂ is a Galois element times
an element of the Hatcher–Lochak–Schneps group Λ** (SECTION_GHOSTS E.177–E.181). Nakamura and Schneps (Invent. Math.
141, 2000) defined the subgroup of GT̂ cut out by (III′) and (IV), proved it acts on all profinite mapping class groups,
and left open whether it is all of GT̂. The run proves (IV) for every element; with Λ's action this gives the action of
GT̂ itself on the whole pure mapping-class tower. Status: proved by the run; refereed by Claude Fable 5.2 at effort max
(agent a49aabbf) on 18 Nov (E.176–E.181, every step, two citations to supply) and by Claude Opus 5.5 at effort max on
18 Nov (E.181). Written up as a Hexagon note, `<local>/Documents\reports_20261123\h17_note\h17_note.tex` (v2,
16 pp., workbench id WB0007, not posted as of 23 Nov), with a second reader, Claude Opus 5.5 at effort max (ae4ae3dc):
no mathematical error. The note replaces E.176 (Smith theory) by Boggi–Zalesskii's Theorem A. The register of the run
does not yet carry these check events, so the ledger shows SECTION_GHOSTS as 21 of 228 checked; it is far better
checked than that on its main line. Both readers are Claude models; no reader of another family has checked it.

**2. A1: for every smooth proper curve of genus ≥ 2 over a finite field of characteristic p, the point-section map into
the arithmetic group with geometrically prime-to-p quotient is injective, with the whole G_k and over every finite
extension; extended to hyperbolic curves over fields finitely generated over F_p.** First proof ANABELIAN_SUCCESSOR A.3
(16 Nov); the version read end to end is ANABELIAN_A1 A.1 and A.33 (17 Nov); ANABELIAN_A1_SUCCESSOR A.1 (18 Nov) gives
a direct characteristic-p route (A.42–A.49, B.68) without Saïdi–Tamagawa's finiteness or Boxall. It answers
Grothendieck's question on cote 149, scans 35–36 ("Il est cependant possible que l'injectivité de (*) reste valable sans
hyp. de caractéristique"), and gives emptiness of the Saïdi–Tamagawa exceptional set for every J_C-large set of primes
(ANABELIAN_A1 A.CR10, in A1_SUCCESSOR A.22), where the literature has finiteness. Status: the cp03 chain was read in full
and judged sound by two copies of the Longue Marche expert, Claude Fable 5.2 at effort max (ab3f12f2, a2fedc2a;
`pro_intake_20261117\EXPERT_A1_SECOND_READING*_20261117.md`), and rebuilt as AN_GRH A05, whose intakes (Claude Opus 5.5
at effort high) confirmed its Steps 3–6. **Checked here:** the finite certificate the expert asked for, A1_SUCCESSOR
A.50. For C: y² + x(x+1)y = x⁵ + 1 over F₂, P = (0,1), Q = (1,0), my own program (GF(64) and Cantor arithmetic) gives
#J(F₈) = 76, [P − Q] of order 2, Q split in the P-based cyclic-19 Lang cover, and relative class number
12284193340665686881 at P and Q and 81428104953590501 at the other six affine points, exactly as stated. I re-derived
why an odd relative class number with both fibres split separates the two sections. The Hexagon register's H07 says
"ANABELIAN_A1 cp03, which our records list as open" and asks whether cp03 was taken in: it was (above), and the first
proof is ANABELIAN_SUCCESSOR's.

**3. Δ vanishes on GT̂, and GT̂ ⊊ ker Δ ⊊ GT̂₀; the characters of GT̂₀ that vanish on GT̂ form a space of dimension ℵ₀**
(GT_TOWER_CHECK A.7, A.3, B.2.25–B.2.30; SECTION_GHOSTS E.191, E.198; EXIT_TOWER E.49). Δ is the level-twelve "CM
parity" character of LM7_PUSH E.65, which compares how an element moves the two elliptic points of the modular curve.
DELTA_ON_GT left Δ|GT̂ = 0 open (A.84); EXIT_TOWER E.49 claimed it with a label gap, repaired in GT_TOWER_CHECK A.3; the
h17 note proves it on normalized elements by the Λ route (E.182–E.191), with no use of EXIT_TOWER E.42–E.44 or
GT_TOWER_CHECK A.6. E.191 was re-proved independently from E.190.4 by Claude Fable 5.2 at effort max
(`reports_20261120\delta_sextic\DELTA_SEXTIC_20261121.md`, Theorem B); E.182–E.190 refereed on 23 Nov. The step from
"normalized elements" to all of GT̂ (Corollary 4 of the note) needs LM7_PUSH E.65 and E.58, which no one has refereed.
The strict inclusions and the ℵ₀ family are run-only. These are the first structural facts we hold about where GT̂ sits
inside the gentle group GT̂₀.

**4. The Legendre route for sections of the tripod over Q** (SECTIONS_OVER_Q A.12–A.24, A.34–A.37, A.45, A.63, A.78).
For a noncuspidal Selmer section with finitely ramified Legendre representation, the section is realized by an actual
Legendre curve E_{λ₀}, λ₀ ∈ Q, and A1 for such sections reduces to one recognition step (A.24, open), localized to the
locally cuspidal places and to one square class. **Checked here:** the key step of A.16 (the integral realization): the
halving points R₁, R₂ and all twelve sign-change translates (numerically, by the chord law), the mod-4 matrix (A.16.2),
its Legendre specialization (A.16.3), and the invariance that forces e₂ − e₁ to be a square. A.14 rests on Pan's
Theorem 1.0.4 and Helm–Voloch's Proposition 6, which no one on our side has opened; the general intake
(`pro_intake_20261119\GENERAL_INTAKE_SECTIONS_OVER_Q_cp17_20261119.md`, Claude Opus 5.5 at effort max) ranks this first
among what to check next, and I agree.

**5. Section ghosts: where they can and cannot be separated** (SECTIONS_OVER_Q A.32, A.44, A.65, A.201; SECTION_GHOSTS
A.2, E.101, E.102, E.174, E.209–E.215; GT_TOWER_CHECK Part C). An ordinary completed pair (κ-images of a would-be point)
with finite support is a rational point; ordinary pairs with infinite support exist and survive every fixed finite
level; locally matching class-two sections lift to class three; for regular odd coefficient primes the fixed-ramification
H² vanishes in every weight, so the only all-depth obstruction is simultaneous support matching. The main question
(FS)_nil (a pair surviving the whole pronilpotent tower has finite support) is open; the current gate is matching for
the global class-eight lift of the primitive-five family (E.215). Status: SOQ rows read at statement level by the general
intake with ~16 small checks; SECTION_GHOSTS Parts P, A–D and E outside E.176–E.191 were read by no intake before this
one (I read the report and register).

**6. Single-prime collisions over finite fields, found twice independently** (SECTION_GHOSTS E.150; ANABELIAN_A1 A.27 =
A.CR14). Over F_q (3 ∤ q), Galois-conjugate points of U = P¹ − {0,1,∞} over an extension of degree d with
gcd(d, 3e) = 1 have the same full geometrically pro-3 section; explicit pairs over F₆₂₅ and F₃₁₂₅. ANABELIAN_A1 found
the same mechanism for a genus-two curve and the prime 3. This marks exactly why A1 needs all primes other than p (or a
J_C-large set): a single prime fails. **Checked here:** E.150 re-proved independently (Hall subgroups of the prosolvable
group F ⋊ Ẑ, and the action of the 3′-part through an element of order e), and both examples verified.

**7. Reconstruction of schemes from étale topoi over fields: the answer to cote 149, scan 52** (ANABELIAN_149_PUSH F.37,
F.43–F.49; ANABELIAN_SUCCESSOR F.3–F.50; ANABELIAN_A1 B.46–B.50; ANABELIAN_A1_SUCCESSOR B.43–B.66, B.123, B.135–B.147).
With the closed-point ("pinned") definition: reconstruction holds over finitely generated fields, Q̄(t), Q^solv-type
fields, every fixed finite-class nilpotent extension K_{p,c} of the strict henselization at p and their subfields, and
the normal-core classes of B.139–B.147; it fails over Q̄, real closed fields, Laurent-series and henselian
residue-characteristic-zero fields (B.49–B.55), and for a countable transcendence-degree-two field with trivial
centralizers (B.50, refuting the prompt's candidate criterion). The general classification is open (A1_SUCCESSOR B.52).
Status: F.45 half read (Claude Fable 5.2 at effort high); B.46–B.50 read for sense (Claude Fable 5.2 at effort max);
B.123–B.147 run-only.

**8. EXIT_TOWER's genus-three Torelli chain and its finite Lego models** (EXIT_TOWER D.50–D.106; B.12–B.25). If the chain
holds, it describes the kernel of Î₃ → Γ̂₃ with its arithmetic action, the obstruction behind the congruence question
that gates E.45 (surjectivity of GT̂ → Out^{I₀} in genus ≥ 3) and E.24 (G_Q = GT̂). The Lego models (542 objects, 1620
arrows, 1080 relators for cote 148) are the best checkable material we have for the edition notes of cotes 146 and 148.
Status: Torelli chain unchecked by anyone outside the run; counts checked by the general intake (Claude Opus 5.5 at effort
max).

**9. Short negative results in profinite group theory that correct published statements** (EXIT_TOWER E.54, E.60,
E.48, E.14; SECTION_GHOSTS P.3). E.54: completed induction does not reflect finite generation (a counterexample to an
assertion in the introduction of Corob Cook–Vannacci, and to property FIM of Wilkes at the prime 3 for free and surface
completions). **Checked here:** the first construction of E.54 in full (sound). P.3: Hoshi–Tsujimura 2021, Proposition
1.4(ii) omits the cusp at ∞ (not checked at the source). E.48: the diagonal Bers model in the proof of Boggi 2014,
Theorem 6.3, is not injective; E.14: three printed assertions of Boggi 2026 and Boggi–Funar 2026 fail.

**10. The audit of Grothendieck's own doubts in cote 149 (and 142)** (FLAGGED_149). Each "sauf erreur", "à vérifier",
"je n'arrive pas à le prouver" of cote 149 gets a verdict with exact scope: about thirty refutations of literal
statements (open-subset lemma false in type (1,1), B4; Mordell–Weil finite-generation assertion false, F6; centralizer
proposition false in type (0,2), F10c; self-normalization of inertia false for arbitrary valuations, D6) and corrected
true forms. Material for the companion notes of cote 149. Its one open mathematical row, B9 (prime-to-p injectivity),
is now closed by item 2.

---

## ANABELIAN_149_PUSH (final, 14 Nov)

1. **Useful or not.** Useful in its time; now largely superseded on its main item. It gave the first reduction of A1 to
   an existence statement about covers (A.C2.20) and the first conditional results toward Conjecture A for the tripod
   (D.30–D.31). A1 was then proved by another route (item 2), and the existence statement it reduced to is false for
   some curves (ANABELIAN_SUCCESSOR A.86, A1_SUCCESSOR B.23). Its Part F (scan 52) remains useful.
2. **What it proved.**
   - A.C2.20: every p, genus ≥ 2: A1 holds for C if C has, geometrically, a connected cyclic étale cover of odd degree
     n prime to p whose primitive factor P_n = im ∏_{ℓ|n}(1 − σ^{n/ℓ}) has p-rank zero. With A.C2.7 (a colliding
     p-primary class has a free deck orbit), A.C2.5, A.C2.19. Checked: sound, Claude Fable 5.2 at effort high
     (`pro_intake_20261114\INTAKE_ANABELIAN_149_FINAL_20261114.md`, §1.1).
   - A.C2.26: A1 for every genus-two curve over F₄ (64 geometric classes), on certificates (A.C2.22, A.C2.25 with a cover of
     degree 2454499369). Not reproduced by anyone.
   - D.30: for a non-cuspidal section of the tripod over Q, the Legendre representation ρ_{s,ℓ} is absolutely
     irreducible; finite ramification of one ρ_{s,ℓ} (ℓ ≥ 5) ⇔ integrality of almost all local points, and then the
     system is that of an elliptic curve over Q. D.31: with almost-everywhere integrality and one cusp label, s is a
     rational point. Both sound as far as followed (same intake), conditional on Pan 2022 and on D.6 (which uses the
     unrefereed local p-adic section theorem of 6 Oct 2026).
   - F.45: reconstruction over every finitely generated extension of Q̄ of positive transcendence degree (first half
     sound, same intake; second half unread). F.47–F.48: henselian residue-characteristic-zero fields fail.
   - Unresolved at the end: A.30 (A1), A.C2.6, D.U1–D.U4, F.9.
3. **New since the last intake.** Nothing in the run (final). Outside it: A1 proved (item 2); the existence route E(C)
   refuted for degrees n > 1 (ANABELIAN_SUCCESSOR A.86, A1_SUCCESSOR B.23); D.30–D.31 are taken further in
   SECTIONS_OVER_Q A.14–A.24.
4. **Open.** A.30 is closed by other runs. D.U1–D.U4 (Conjecture A and its variants for the tripod): gate = finite
   ramification of one ρ_{s,ℓ}, plus two cusp labels (SECTIONS_OVER_Q A.24 is the current form). F.9 (classification of
   reconstructing fields): open, now A1_SUCCESSOR B.52.
5. **Relations.** Cote 149 scans 35–36 (A), 52 (F), 56, 59–63, 126–127 (D). LM5_MULTI_GALOIS_TOPOI F.50 must be cited
   with the closed-point definition (F.1, F.17). AN_GRH (prompt 30) A05/A18/A46 continue Part A. Literature named by
   the run: Raynaud (theta divisor), Tamagawa 2003, Pop–Saïdi 2003, Poonen 2007, Crew 1984, Pan 2022, Helm–Voloch 2011,
   Stix 2015, Carlson–Haine–Wolf 2024.
6. **Candidates.** No new prompt: its items continue in the anabelian successors. Companion note to cote 149, scans 35–36
   and 52 (proposed by the 14 Nov intake, §3.1), now to be written from item 2 and item 7.
7. **Problems.** None found by the earlier intake. The run's A1 route is a sufficient criterion only; nothing in the run
   overclaims it. Its "Proved" for A.C2.26 rests on unreproduced certificates.
   - Spot check: none new. The main new theorem (A.C2.20) was followed in full by the 14 Nov intake, and the item it
     served is now settled by another proof.

## FLAGGED_149 (return, 12 Nov)

1. **Useful or not.** Useful for the edition of cote 149 (and the cote 142 pages it touches): a line-by-line verdict on
   each passage Grothendieck flagged as doubtful, with corrected statements and sources. Marginal as new mathematics.
2. **What it proved** (selected; table F1–F20 of `FLAGGED_149_report.md`): F2 true (the trivial centre of scan 14, with the
   involution classification and its exact centralizer, A2); F3, F4 true with stated hypotheses; F5: the open-subset translation lemma of scan 37 is
   false in type (1,1) (B4), with the exact curve correction (B3, B5); F6: the Mordell–Weil finite-generation assertion
   of scans 32–35 is false (B1), Théorème 3 proved in characteristic 0 (B2); F7: full (*) and (**) proved, prime-to-p
   (**) refuted, prime-to-p (*) open (B9); F9: 1-faithfulness true over the stated base, unrestricted fullness false;
   F10: false in type (0,2) (F10c), true for hyperbolic types including (0,3); F17: a ⇔ b proved, c,d ⇒ a and e ⇒ a
   false; F19–F20: self-normalization of inertia false for arbitrary valuations (D6, D7). Explicit genus-two tests
   separated: B14 (y³ − y = x + 1/x over F₃) and B15 (y² = x⁵ + (x² + 1)² over F₅). Status: 19 of 107 rows checked by the
   14 Nov intakes (Claude Fable 5.2 at efforts high and medium; `pro_intake_20261114\debate_20261114\RESPONSE_INTAKE.md`,
   `recent_results_20261114\INTAKE_HUA_MATHEMATICS_20261114*.md`).
3. **New since the last intake.** Nothing in the run. Outside it: B9 is closed by item 2 (proper curves) and its
   specialization (A.33 of ANABELIAN_A1).
4. **Open.** B9 (closed elsewhere), ZCF6 (existence assertions after the centralizer computation), ZD10 (birational
   lifting, conjecture (b) of scans 126–127; SECTION_GHOSTS D.2 makes it conditional on (FS)_nil), Z142g.
5. **Relations.** ANABELIAN_149_PUSH (same cote, same items, D3 of FLAGGED_149 is A1_SUCCESSOR B.99); CYCLOTOMIC_KERNEL
   B1 (used for F8). Literature: SGA 1 XIII, Milne, Saïdi–Tamagawa 2009/2017, Stix, Hoshi–Mochizuki 2011,
   Minamide–Tsujimura 2022, Tamagawa, Carlson–Stix, CHW.
6. **Candidates.** The companion notes of cote 149 (and 142, scans 5–21: G1–G11, Z142a–g): one note per flagged passage,
   from the report's table. No prompt.
7. **Problems.** None found. **Checked here:** B15's premise that [P − Q] has exact order five (y − (x² + 1) has divisor
   5P − 5∞, since its product with y + (x² + 1) is x⁵). The separating cover of degree 16 was not checked.

## ANABELIAN_SUCCESSOR (final, 16 Nov)

1. **Useful or not.** Useful: it holds the first proof of A1 (A.3 = AR.3), with the non-injectivity of the full
   prime-to-p configuration fibre map (A.87) as a separate result, and the first refutation of the cover-existence
   route (A.86).
2. **What it proved.**
   - A.3: A1 (statement as in item 2), with A.87–A.90 (cuspidally pro-r exactness, diagonal boundary transport). First
     check: "sound as read", conditional on Saïdi–Tamagawa 2009 Prop. 1.8 (vi), by Claude Fable 5.2 at effort max
     (ab3f12f2; `pro_intake_20261116\EXPERT_A1_ANABELIAN_20261117.md`); literature search by the main session (Claude
     Opus 5.5 at effort max; `LITERATURE_A1_MAIN_20261117.md`): no source proves emptiness of the exceptional set;
     Wakabayashi 2016 (pro-ℓ cuspidalization over finite fields) not cited by the run. The conditional input was removed
     in ANABELIAN_A1.
   - A.98: absence of collisions after every constant extension ⇔ emptiness of the exceptional set.
   - A.86 (Refuted, i.e. a counterexample): an explicit supersingular genus-two curve over F_{2^38} for which every
     nontrivial connected cyclic étale cover of odd degree has primitive part of positive 2-rank (Bezout certificates
     exclude the only possible conductors 191 and 229); at least 274,515,649,064 such parameters. Run only.
   - A.70, A.34: on y² + y = x⁵ over F₁₆ (Frobenius the scalar [−4]) a degree-13 P-split cover over F₄₀₉₆ has odd
     relative class number although its new part is ordinary: p-rank zero is not necessary for a class-number witness.
   - Part F: F.7 (candidate F3(b) false, already for four punctures), F.3 (finite-field counterexample to
     closed-point-preserving reconstruction), F.13, F.50; positive classes K_p, T_p, K_p^ab, K_{p,c}.
3. **New since the last intake.** The intakes named one or two rows (A.3). Not read by any intake: A.86, the A3–A7, A10
   items, Part F. This intake: report and register read; two premises checked (below).
4. **Open.** A.15 (A3, the nontrivial-cover existence assertion), A.57 (A5, supersingular correspondences), A.96
   (quartic censuses), A.103 (A10: free norm vectors in genus two, char 2), F.18 (sufficiency of candidate F3(a)).
5. **Relations.** Item 2; ANABELIAN_149_PUSH A.C2.20 (A.86 is its limit); A1_SUCCESSOR B.23 confirms A.86. Literature:
   Saïdi–Tamagawa 2009, 2017; Mochizuki 2007 and 2014 comments; Wakabayashi 2016; Mochizuki–Tamagawa 2008.
6. **Candidates.** See item 2's Hexagon candidate (H07), whose provenance line should name ANABELIAN_SUCCESSOR A.3
   (16 Nov) and ANABELIAN_A1 A.1 (17 Nov).
7. **Problems.** None found in what I read. **Checked here:** A.70's premise (#C₀(F₁₆) = 33, so the four Frobenius
   eigenvalues, each of absolute value 4, sum to −16 and are all −4: Frobenius is [−4]); and the report's elementary
   example y² + y = x + 1/x + 1/(x+1) over F₂ (genus 2, #C(F₂) = #C(F₄) = 3, L(T) = 1 − T² + 4T⁴, #J(F₂) = 4; the group
   structure (Z/2)² not checked).

## ANABELIAN_A1 (checkpoint 03, 17 Nov; final by the user's word)

1. **Useful or not.** Useful: the version of A1 that has been read end to end.
2. **What it proved.** A.1 = A.R1 (A1), A.33 = A.R5 (hyperbolic curves over fields finitely generated over F_p),
   A.CR10 (exceptional set empty for every J_C-large Σ, also with p ∈ Σ), A.CF9 (the full prime-to-p configuration fibre
   sequence is not left exact), controls A.24 = A.CR11 (genus one fails where it must), A.25 = A.CR12 (y² + x(x+1)y =
   x⁵ + 1 over F₂: an abelian collision, the first case where A.1 says something new), A.27 = A.CR14 (single prime fails),
   B.50 (refutes the prompt's reconstruction criterion B7). Checks: A.CF1–CF12, A.CR1–CR14, A.R1, A.R4, A.R5 read and
   judged sound by Claude Fable 5.2 at effort max (ab3f12f2, a2fedc2a; `pro_intake_20261117\EXPERT_A1_SECOND_READING*`);
   B.46–B.50 read for sense. AN_GRH A05 (a rebuild) confirmed in Steps 3–6 by Claude Opus 5.5 at effort high.
3. **New since the last intake.** None in the run. Outside: the experts' requests 2 and 3 were answered by
   A1_SUCCESSOR A.50 (finite certificate, now reproduced here) and A.51 (a non-nilpotent fibre quotient of order 75).
4. **Open.** A.CR15 = item A12: prime sets that are neither a singleton nor J_C-large (A1_SUCCESSOR A.28, A.53–A.61).
5. **Relations.** Cote 149 scans 35–36; Saïdi–Tamagawa 2009, 2017; Mochizuki–Tamagawa 2008 Prop. 2.2; SGA 1 XIII
   2.9–2.12, 4.3–4.4, 5.2; Stix 2005 Prop. 2.7; Bellingeri 2004.
6. **Candidates.** Hexagon (H07, with the provenance corrected); still wanted: a reader of another model family for
   A.CF1–CF2 (the expert's request 1; AN_GRH's Claude intakes went part of the way), and the SGA 1 XIII citations opened.
7. **Problems.** None. **Checked here:** A.25 by hand (div x = 2P − 2∞ and div(x + 1) = 2Q − 2∞, both points ramified),
   and by my program ([P − Q] ≠ 0, 2[P − Q] = 0).

## ANABELIAN_A1_SUCCESSOR (checkpoint 05, 18 Nov)

1. **Useful or not.** Useful. A1 by a direct characteristic-p route; the finite certificates; a body of refutations of
   cote 149 and 142 statements; and the largest positive results on reconstruction over local-type fields.
2. **What it proved.**
   - A.1 with A.42–A.49, A.13, B.68: A1 without the lifting comparison and without the finite exceptional set; A.45–A.48
     prove the exactness input directly in characteristic p. Run only (no intake has read the new route).
   - A.50: the cyclic-19 certificate (item 2). **Checked here** (computation and re-proof).
   - B.85, B.88: a cubic cover over F₁₆ split at P and Q with relative class number 81 and a supersingular elliptic
     quotient, and a degree-3⁷ pointed pro-3 separator of the same pair. Run only.
   - A.51: a fibre quotient of order 75 (non-nilpotent) with a non-central cusp, dominated by a quotient of order
     9·5⁴⁰: the test of the exactness on a non-nilpotent quotient the expert asked for (K5). Run only.
   - B.23 (False as stated): confirms ANABELIAN_SUCCESSOR A.86 independently. B.87: no finite list of odd cyclic degrees
     suffices even for ordinary genus two.
   - C.2 (False as stated): the characteristic-p extension of cote 149, scan 32, Théorème 3, fails (y² + xy = x³ + 1 over
     F₂, O and T = (0,1)); the exact replacement: the kernel is G(K)[p^∞].
   - B.93 (False as stated): the uniqueness expectation of cote 142, scan 096, fails for finite markings; B.90–B.96
     (N4) with a nonisotrivial four-punctured line over Q(t).
   - B.141, B.145: B1 for the genus-two family y² = x⁶ + 1 at p ≡ 2, 5 (mod 9), an automorphism-eigencharacter criterion
     in every genus and a genus-three instance over F₂₇.
   - B.137–B.147: reconstruction over K_{p,nil} for every p, over relative local fields and normal-core fixed fields;
     B.144 explicit negative wild-procyclic fields, slimness necessary. B.134: on y² = x³ − x at p = 5, a nonzero
     geometric Kummer class vanishing at every point (a limit of the evaluation lemma).
3. **New since the last intake.** No intake read cp05 (0 of 210 rows named). Everything above is new to our records
   except A1 itself.
4. **Open.** A.28 (A12: universal order unboundedness of the omitted-prime Frobenius; A.53–A.61 give the criterion and a
   first jump), B.5 (B1), B.12 (B2), B.24 (B4, the degree-one-allowed existence assertion), B.67 (B5), B.32 (B6),
   B.52 (B8, general classification), B.118 (N2), S4 (journal numbering of Stix 2005).
5. **Relations.** Items 2 and 7; FLAGGED_149 D3 = B.99; LM5 (reconstruction); cote 142 scans 5–21 and 96 (B.93);
   cote 149 scans 11, 32, 75, 79, 120 (B.124–B.125 elementary towers). Literature: Tamagawa 2003 Lemma 3.9 (corrects a
   Raynaud 1982 citation in A.57), Lepage, AHLS 2024, Milne Prop. 9.1.
6. **Candidates.** Into the H07 write-up: A.50 as the finite certificate (now reproduced independently), A.51. A next
   prompt (if any) on A12 only; nothing else in this run calls for one.
7. **Problems.** None found in what I read. The report says the 121 carried rows had "a targeted reading in this
   writing"; that is the same model.

## SECTIONS_OVER_Q (checkpoint 17, 16 Nov; account froze)

1. **Useful or not.** Useful: the most concrete reduction we have of Grothendieck's section conjecture for the tripod
   over Q in the finitely ramified case, and the theory of ghosts that the later runs build on.
2. **What it proved.** As summarized in item 4 and item 5; the full statement-level account is the general intake (Claude
   Opus 5.5 at effort max, a28ea31f, 19 Nov, every row). Key ids: A.12–A.13 (irreducibility), A.14 (four equivalent forms
   of bounded ramification, via Pan and Helm–Voloch), A.16 (integral Legendre realization), A.17 (square-class
   multiplier), A.24 (recognition, Open), A.32 (finite support ⇒ point), A.44 (infinite-support ghosts), A.65 (survival at
   every fixed depth), A.145 (a quotient of order 512 excludes a continuum), A.160 (finite Sha of E_b/Q(√2)), A.178
   (fixed abelian cover + metabelian quotient detect finite support, every hyperbolic curve over a number field), A.201
   and A.204 (lifting class 2 → 3), C.3 (failure over Q(μ_∞)), D.1 (finite descent, conditional on the 6 Oct local
   theorem). A.20 corrects LM6_POINTS_AS_SECTIONS E.8. Checks: the general intake's computations (A.8, A.19, A.28,
   A.53, A.98, A.103, A.138, A.144, A.149, A.150, A.156, A.189) and targeted checks (A.17, A.35, A.40, A.114, A.205, C.1).
3. **New since the last intake.** Nothing in the run. **Checked here:** A.16's key step (item 4).
4. **Open.** A.1 (A1 and A11 themselves), A.24 (recognition: the three missing steps), B.15 (birational/valuative
   remainder), D.8.
5. **Relations.** ANABELIAN_149_PUSH D.30–D.31 (the same route, earlier); SECTION_GHOSTS (audits 16 of its rows in E.2,
   all confirmed; E.101–E.103, E.20, E.41–E.43); GT_TOWER_CHECK Part C; LM6_POINTS_AS_SECTIONS. Cote 149 scans 56,
   126–127. Stix 2015 Cor. 5, Harari–Stix, Pan 2022, Helm–Voloch 2011.
6. **Candidates.** A referee prompt (or an intake read) on A.14 against Pan's Theorem 1.0.4 and Helm–Voloch's
   Proposition 6, then A.201/A.204 and A.178 against Harari–Stix Thm 2.1, as the general intake lists. The unsent Pro
   intake prompt `TO_SEND\PRO\7_Longue_Marche_intakes\18_Pro_intakes_Longue_Marche_thin_runs\INTAKE_A_ANABELIAN_SECTIONS`
   would cover these runs; it should be checked against this pile before it goes.
7. **Problems.** The general intake noted that A.14 uses Pan and Helm–Voloch beyond their stated forms (the conductor
   bound uses only residual ramification support and wild-inertia image; I read that passage, lines 227–273 of
   `sections\legendre_agent.tex`, and the use looks right, but I did not open the sources). D.1 inherits the unrefereed
   local theorem.

## SECTION_GHOSTS (final, 18 Nov)

1. **Useful or not.** Very useful, for one reason beyond its question: E.176–E.191 (item 1, item 3). Its own question
   ((FS)_nil) stays open, with a precise gate.
2. **What it proved.**
   - E.176–E.181: (IV) on GT̂ and the normalization to Λ; E.182–E.191: Δ = 0 on normalized elements. Checks: see item 1
     and item 3 (`reports_20261123\h17_note\RECORDS.md` §2: E.176–E.181 targeted proof check 18 Nov, Claude Fable 5.2 at
     effort max; E.181 18 Nov, Claude Opus 5.5 at effort max; E.191 independent re-proof 21 Nov, Fable; E.182, E.184,
     E.188, E.189, E.190 targeted proof check 23 Nov, Fable, E.189 given Hoshi–Minamide–Mochizuki; E.183 independent
     re-proof 23 Nov, Fable).
   - E.195: a finite five-point level excludes the parity-one locus (the existence statement of GT_TOWER_CHECK A.4.1).
     E.198: GT̂ ⊊ ker Δ ⊊ GT̂₀, witness the square of E.197's element, pentagon defect seen in an 11-primary quotient.
   - E.150: distinct finite-field points with the same full pro-3 section (item 6). **Checked here** (independent
     re-proof).
   - E.192, E.194, E.218: over every F_q and ℓ ≠ char, an explicit finite pro-ℓ quotient Π/(Π^{ℓ^N}Γ_{c+1}) separates
     every interior point section from every cusp section.
   - E.209–E.210: for odd ℓ with ℓ ∤ h(Q(ζ_ℓ)), H²(G_{Q,{ℓ,∞}}, Z/ℓⁿ(w)) = 0 for all w, and the global H¹ correction
     groups; so the only all-depth obstruction above a matched predecessor is simultaneous support matching (B.26). The
     vanishing is classical in substance (regular primes; Soulé, Iwasawa theory); the run proves it directly.
   - E.174: an infinite-support ordinary pair with all-prime class-two support matching. E.214: selected outputs of the
     factorial construction lift to class three and fail at class four (pro-5). E.215: a primitive-five family matched
     through class 7 with a global class-8 lift.
   - E.98–E.100: full pronilpotent and metabelian non-cuspidal Fermat sections for n = 3^r, 5^r; and for every even n the
     plus Fermat curve has no pro-2 abelian section (real obstruction), so the prompt's input R8 ("every Fermat curve
     has non-cuspidal sections in all these quotients", from the LM6/LM7/LM8 line) is false as stated.
   - P.3: correction of Hoshi–Tsujimura 2021, Prop. 1.4(ii) (cusp at ∞ omitted); the corrected four-case criterion.
   - Historical audit: 90 earlier claims (SECTIONS_OVER_Q, GT_TOWER_CHECK Part C, the prompt's inputs): 87 confirmed,
     2 repaired (R8), 1 pending (GT_TOWER_CHECK A.4.57, the literal finite compiler).
3. **New since the last intake.** The main-session note `claude_math_notes\RUNS_NIGHT_20261118.md` named four rows; the
   h17 work refereed E.176–E.191. Parts P, A, B, C, D and E outside E.176–E.191 had no intake; this intake read the
   report and the whole register and checked E.150.
4. **Open.** A.2 (the main question, with its single-prime versions; gate: one fixed ordinary pair passing support
   matching in all weights, now weight eight for the E.215 family), A.7 (first nonzero higher obstruction), B.1–B.3,
   C.7 (uniform target / countersign), D.3 (manuscript outcome), E.120 (pro-3 question), E.1 (verification of imported
   inputs).
5. **Relations.** SECTIONS_OVER_Q, GT_TOWER_CHECK (audited), EXIT_TOWER E.49 (= E.184–E.191 by another route), LM7_PUSH
   E.65/E.58 (the definition of Δ and the Δ = 1 witness), DELTA_ON_GT, LM4 (E.50–E.59 audit LM4 rows A.18, A.70, A.74,
   B.42–B.45), ANABELIAN_A1 (E.150 vs A.27). Cote 149 scan 56 and scans 126–127 (D.2: conditional implications).
   Literature: Nakamura–Schneps 2000; Hatcher–Lochak–Schneps 2000; Boggi–Zalesskii 2025; Hoshi–Minamide–Mochizuki 2022;
   Stix 2015; Hoshi 2010; Hoshi–Tsujimura 2021; Wickelgren; Jannsen.
6. **Candidates.** The Hexagon note WB0007 (gates in its RECORDS.md §5: the user's word, the line of authors, a check of
   Corollary 4's inputs LM7_PUSH E.65 and E.58). A correction note to Hoshi–Tsujimura (P.3), after opening their paper.
   The H17 row of `field_experts\HEXAGON_CANDIDATES.md` predates the note and should point to it.
7. **Problems.** The report's E.209 presents a classical vanishing as a new proof without saying it is classical (the
   register labels it Proved, not Known). Its own wording is careful elsewhere. Part of the post-checkpoint text is a
   transcription from chat, not the lost working files (the run says so; E.214's checker bytes lost).

## EXIT_TOWER (checkpoint 28, 16 Nov)

1. **Useful or not.** Useful, broad: the exit-path category of M̄_{g,n} for cotes 147, 150; finite models of cotes 146,
   148; the GT action on the whole tower (E.16, E.23, E.27, E.44); a long genus-three Torelli chain; corrections to
   cotes 143 and 150 and to published statements.
2. **What it proved.** See `pro_intake_20261119\GENERAL_INTAKE_EXIT_TOWER_cp28_20261119.md` (Claude Opus 5.5 at effort
   max, ae4ae3dc, every row) and `pro_intake_20261117\GT_LINE_INTAKE_20261117.md` (Claude Fable 5.2 at effort high).
   Key: E.44 (𝒥(A) = A on GT̂, confirmed by GT_TOWER_CHECK A.1), E.49 (Δ|GT̂ = 0; label gap repaired in GT_TOWER_CHECK
   A.3), E.47, E.48 (Boggi 2014 Thm 6.3's diagonal Bers model is not injective), E.77, B.25 (542/1620/1080), A.11/A.13
   (cote 150 raw faces refuted), E.T2, E.X1 (cote 143), D.45 (exact connectivity), D.50–D.106 (Torelli), E.54, E.60.
3. **New since the last intake.** Nothing in the run. Outside it: the h17 note proves Δ = 0 on normalized GT̂ without
   E.42–E.44. **Checked here:** E.54's first construction (sound) and E.60's surjectivity and non-trivial kernel.
4. **Open.** E.24 (G_Q = GT̂), E.45 (GT̂ → Out^{I₀}(Γ̌_{g,[n]}) surjective for g ≥ 3), E.T3.
5. **Relations.** Cotes 143, 146, 147 §§7–10, 148, 150; RESEARCH_SA20, RESEARCH_SA22 (general intake §4); LM4_SUCCESSOR;
   GT_TOWER_CHECK; DELTA_ON_GT; SECTION_GHOSTS. Literature: Jansen (exit paths), Boggi 2014/2026, Boggi–Funar 2026,
   Boggi–Zalesskii, Lochak 2025, Hoshi–Mochizuki–Tsujimura 2025, Minahan 2025, Corob Cook–Vannacci, Wilkes 2017.
6. **Candidates.** The Torelli chain D.50–D.106 to a referee before anything is built on it (general intake §2.1).
   E.54 and E.60 as a short self-standing note after a source check of Corob Cook–Vannacci's sentence (v3, p. 4) and the
   two-generated variant; informing Boggi (E.48, E.14) after a referee, under the outreach rule. Edition notes for cotes
   143, 146, 148, 150. The unsent Pro intake prompt `INTAKE_B_TOWERS` (same folder as INTAKE_A) covers this run.
7. **Problems.** E.49's written proof has the label gap (GT_TOWER_CHECK A.3); its proof of record is GT_TOWER_CHECK
   A.3 or the h17 note. The proofs of E.29, E.32, E.33, E.35, E.38 were absent from the attachment GT_TOWER_CHECK
   received (GT_LINE §1.1).

## DELTA_ON_GT (checkpoint 05, 16 Nov)

1. **Useful or not.** Marginal now: its main question (A.84) was settled by other runs, and much of it shows what does
   not see Δ. What stays useful: the reduction A.103/A.112 (Δ = 0 on GT̂ ⇔ ν₄ = κ_d mod 2), the detecting
   representation A.98/A.110, B.15 (a Δ = 1 element with parities (0,1)), B.14 (frame images), the cote 148 counts
   B.31–B.34, the manuscript dictionary R11/B.24–B.25.
2. **What it proved.** As in GT_LINE §1.2. 17 Refuted rows refute leads of our own prompt.
3. **New since the last intake.** Nothing in the run. **Checked here:** the S₄ half of A.112 (FP.37): with p = (123),
   t = (1234), for R = v p^a in A₄ the element pR⁻¹tR has order four exactly when v ∈ {1, t²} (all twelve cases), so ν₄
   is well defined, and the composition law gives a homomorphism; the pentagon half (FP.37.6, 24 matrix cases over
   Z[ω]/4) was not reproduced. A.98's numerical premise: Γ(12)/±1 has index 576 in PSL₂(Z) and is free of rank
   1 + 576/6 = 97.
4. **Open.** A.84 (settled elsewhere on normalized elements; all of GT̂ with LM7_PUSH E.65/E.58), A.85, A.86, B.28, B.33
   (closed for one realization by EXIT_TOWER B.25), B.38–B.41 (B.40 answered no by GT_TOWER_CHECK B.2.25), P.6, A.24,
   A.51, A.53, A.70.
5. **Relations.** GT_TOWER_CHECK, EXIT_TOWER, SECTION_GHOSTS, LM7_PUSH E.65/E.58/D.46, LM4_SUCCESSOR, DELTA23 and
   DELTA_SEXTIC (later work, `reports_20261120\delta_sextic\`). Cote 148.
6. **Candidates.** None of its own. Its report's "the R2 witness" and "the repaired D.46 lift" should read as families
   (GT_LINE §3.3), wherever they are quoted.
7. **Problems.** The wording above. The register carries titles only; statements are in `sections\`.

## GT_TOWER_CHECK (checkpoint 10, 17 Nov; the run ended when checkpoint 11 was too large to save)

1. **Useful or not.** Useful: the audit that made E.49 a proof of record, and the structure results of item 3.
2. **What it proved.** A.7 (Δ|GT̂ = 0; G_Q ⊆ GT̂ ⊊ ker Δ ⊊ GT̂₀); A.3 (E.49 with two repairs); A.1, A.1.2, A.9 (E.44
   confirmed; solvable case in genus zero); A.5 (d₂ = 0 and e₃ = 0 on GT̂); A.6 (E.200 is Lochak's (5.1); full
   completions); B.1.8 (D_L = id, D_P(F) = cFc on GT̂); B.2.1–B.2.3 (GT̂ ⊊ ker Δ via an 11-primary weight-nine witness;
   first separation at class eight; h₇); B.2.24–B.2.31 (𝒳 has dimension ℵ₀); B.5 (the 542/1620 realization re-derived;
   **cote 148, folios 30–32: the lower fractional twist is 1/4 where our first-pass transcription has 1/3**); Part C
   (ghosts). Checks: GT_LINE §6 (Claude Fable 5.2 at effort high: the algebra of A.C6, the conjugation table, the last
   step of A.3, B.2.2's orders against the expert's dimensions); E.49/A.C13–A.C17 parity algebra re-proved exhaustively
   over Z/12 by Claude Opus 5.5 at effort max (ae4ae3dc, 22 Nov; h17 RECORDS).
3. **New since the last intake.** Nothing in the run (the transcript's post-cp10 work is unsaved). **Checked here:**
   A.4.1 (= SECTION_GHOSTS E.195): the compactness argument (Δ⁻¹(1) closed in compact GT̂₀, the pentagon map continuous,
   1 not in the image because Δ = 0 on GT̂, so an open normal subgroup avoids the compact image) is sound, conditional on
   A.7.
4. **Open.** A.4 (an independent finite census: not obtained; A.4.57 pending), A.8, B.1 (C^φ ⊆ ker Δ), B.2, B.3 = B.6
   (every involution of GT̂ conjugate to c), B.4 = B.7 (a separator of G_Q from GT̂), C.1–C.5.
5. **Relations.** EXIT_TOWER (audited), DELTA_ON_GT (A.84, A.103, B.40 answered), SECTION_GHOSTS (E.2 audits fifty Part C
   rows, all confirmed), LM4_SUCCESSOR (A.13, B.12, B.42–B.45), LM7_PUSH E.65. Literature: Boggi–Zalesskii, Lochak 2025,
   Enriquez 2007 Thm 8.1, Nakamura–Tsunogai, Lochak–Nakamura–Schneps 2026, Basualdo Bonatto–Robertson 2026.
6. **Candidates.** A correction to the cote 148 transcription (1/3 → 1/4 at folios 30–32), after our own look at the
   scans (GT_LINE §3.2 said it was still due). B.3/B.6 (involutions) and B.4/B.7 as the natural next GT questions, if a
   prompt is wanted.
7. **Problems.** A.4.57 is a finite form of the proof, not an independent computation (the run says so). "The element of
   E.46/E.58" is a family (A.2).

---

## What I checked (all recorded in this folder's check-event files)

| Run | Statement | Type | Outcome |
|---|---|---|---|
| ANABELIAN_A1_SUCCESSOR | A.50 | computation (own program `LONGUE_MARCHE_B_checks\a50_check.py`) | confirmed: every number |
| ANABELIAN_A1_SUCCESSOR | A.50 (separation inference) | independent re-proof | confirmed |
| ANABELIAN_A1 | A.25 | independent re-proof (by hand) and computation | confirmed |
| ANABELIAN_SUCCESSOR | A.70 (premise), A.34 (premise) | independent re-proof | confirmed |
| ANABELIAN_SUCCESSOR | report example (M_P^F) | computation by hand | confirmed (group structure not checked) |
| FLAGGED_149 | B15 (order five) | independent re-proof | confirmed; the cover not checked |
| SECTIONS_OVER_Q | A.16 | targeted proof check, with numeric verification | confirmed, given A.14 |
| SECTION_GHOSTS | E.150 | independent re-proof | confirmed, both examples |
| SECTION_GHOSTS / GT_TOWER_CHECK | E.195 / A.4.1 | targeted proof check | confirmed, given Δ = 0 on GT̂ |
| EXIT_TOWER | E.54 | targeted proof check (first construction) | confirmed; source wording not checked |
| EXIT_TOWER | E.60 | targeted proof check (part) | surjectivity and kernel confirmed; finite presentation not checked |
| DELTA_ON_GT | A.112 | targeted proof check (part) | S₄ definition and homomorphism confirmed; pentagon half not reproduced |
| DELTA_ON_GT | A.98 | computation by hand (premise) | confirmed |

The program for A.50 is `LONGUE_MARCHE_B_checks\a50_check.py` in this folder (standard library), with its output in
`LONGUE_MARCHE_B_checks\a50_check_output.txt`: #C(F₈) = 9, #C(F₆₄) = 87, #J(F₈) = 76 by
enumeration and by the zeta function, [P − Q] of order 2, #J(F₈)[2^∞] = 4, Q split in the P-based cover, relative class
number 12284193340665686881 (based at P or Q) and 81428104953590501 (each of the six other affine rational points).

## What I did not read

The prompts in full (questions taken from the runs' item tables); the PDFs (no page rendered); the runs' code (none run);
any source of the literature; FLAGGED_149's proofs; ANABELIAN_149_PUSH beyond the 14 Nov intake and register;
EXIT_TOWER's proofs beyond E_induction_reflection.tex lines 1–230; DELTA_ON_GT beyond FP.37 and the register; GT_TOWER_CHECK
beyond the GT_LINE intake and the register counts; SECTIONS_OVER_Q's proofs beyond legendre_agent.tex lines 200–435;
SECTION_GHOSTS' proofs (I read its report, README and register, and the historical audit's repaired and pending rows);
ANABELIAN_A1_SUCCESSOR's proofs (report and register only). The sub-intake of AN_GRH (prompt 30) is outside this cluster.
