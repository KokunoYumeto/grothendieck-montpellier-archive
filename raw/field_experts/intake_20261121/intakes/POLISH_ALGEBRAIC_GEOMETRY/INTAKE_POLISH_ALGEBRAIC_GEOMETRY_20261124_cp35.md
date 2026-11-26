# Intake by diff: POLISH_ALGEBRAIC_GEOMETRY, checkpoint 24 → checkpoint 35

By Claude Opus 5.5 at effort high (agent a018e2d2, field expert), 24 Nov 2026, ~11:00–12:00 UTC. The main session
(Claude Opus 5.5 at effort max) asked for it. The brief `INTAKE_WAVE_20261123_EVENING.md` holds. The run is GPT-6 Astra
(ChatGPT Pro mode), "inherited reasoning settings". It is **still running**: review 24 (03:00 UTC) found movement and
review 22 was its only no-movement review; checkpoint 35 was saved late, after 03:15 UTC.

Previous intake: `..._20261123_cp24.md`. Work file: `agent_notes/a018e2d2e3e7a279f_NOTES.md`.

## 0. Scope: what I read

- **Return:** cp35 (cp25 and cp26 were filed into it; their manifests are under `_from_earlier_checkpoints/`),
  diffed against cp24. The ledger was read from review 16 (19:02) to the "Checkpoint35 delay" entry (03:16).
- **Diff:**
  - Papers 1, 3 and 4 are byte-identical.
  - Paper 5 has a two-line editorial change (the run re-read it in full at 00:49).
  - Paper 2 grew from 100 to 152 pages. It has ten new inputs (about 150 KB) and changes to `main.tex`,
    `positive_square_picard_strictness.tex` (682 lines) and four small files.
- **Read in full:**
  - the Section 1 statements of Paper 2;
  - the proof of **Theorem positive-excess-picard** (the main induction and the NS lift);
  - the new dossier entries: the Hexagon qualification and Esnault Remark 2.3(2);
  - the Esnault LaTeX line, and pp. 15–16 of Mukai, already read earlier.
- **Statement level:**
  - the three lemmas behind the positive-excess proof (resolution loss, root genus, resolved transfer);
  - the odd strictness, the characteristic-2 boundary corollary, internal Cartier descent;
  - the seven "endpoint" sections (smallest endpoint: geometry, global structure, numerical restrictions, strict
    canonical; elliptic and inseparable-Albanese endpoint geometry; boundary Albanese restrictions).

  My context guard was past 70 %, so I did not open those proof bodies.

## 1. What is new, usefulness first

The whole A2 line (Picard kernels on geometric points; Kweon Q7.7(i)) moved from **equality** to **positive excess**.

1. **Theorem positive-excess-picard.** Confirmed: the induction and the NS lift. The lemmas are at statement level.
   - **Statement.**
     - Hypotheses: X normal projective; Y smooth in the smooth locus with d = Y² > 0; M of order p, trivial on Y, of
       exact log order m; r = v_p(m); [M] ∈ p^r NS(X) (every algebraically trivial M qualifies).
     - Conclusion: δ = 2g(Y) − 2 − md satisfies (Q_r − 1)δ ≥ md, where Q_r = ∏_{j≤r}(1 + 2(p−1)m/p^j).
       - For r = 1: δ ≥ pd/(2(p−1)).
       - For odd p and r = 1 the inequality is strict.
   - **Mechanism.** If M = P^{p^r}:
     1. Take successive normalized μ_p-covers and resolve them suitably.
     2. Each step keeps the genus. The new curve's square drops by at most 2(p−1)δ, because the conductor gives
       (p−1)δ = ℓ + 2Δ and the resolution loses at most 4Δ.
     3. So the excess grows by at most a factor (1 + 2(p−1)m_{i+1}).
     4. If Q_r δ < G, all squares stay positive. The final order m/p^r is then prime to p, which closedness forbids.
   - **Use.** It is the first *quantitative* restriction on positive excess. Any nontrivial algebraically trivial
     p-torsion class killed by a curve forces the genus up by at least a fixed fraction of Y². It holds on any normal
     surface, with only Y² > 0. This is the cleanest and most general result of the run's A2 line. It supersedes the
     cp24 equality theorem, which is now its corollary.
2. **Characteristic-2 boundary.** Statement level. Take p = 2, m = 2a with a odd, [M] ∈ 2NS and δ = d. Then
   T = ω_Y ⊗ N^{−(2a+1)} has exact order 2 (a = 1) or is trivial (a ≥ 3), and Pic(Y)[2] ≠ 0. So when Y has no
   2-torsion, δ > d.
3. **The smallest endpoint** (characteristic 2, m = 2, algebraically trivial M, Albanese degree two). Statement level.
   - d = 4χ, 2d < K² < 3d, and 1 ≤ c₂ ≤ d − 1.
   - The finite Stein factor has 2t = d + ε and 4c₂t ≥ d².
   - The very-ample endpoint needs d ≥ 12.

   These are necessary conditions on a branch no one has shown to be nonempty. Their usefulness is for whoever tries
   to construct or exclude the example. They are not separate results for readers.
4. **Internal Cartier descent** (characteristic 2, internal centre: [M] ∉ 2NS) and **odd first-valuation
   strictness**. Statement level.

**Withdrawn or refuted:** none in the papers. The earlier equality theorem is retained as a corollary.

**Verdicts (mine):**
- 2 targeted checks (the positive-excess induction, and Esnault Remark 2.3(2));
- 1 own-result refinement (our Theorem 2, dimension 0);
- several at statement level;
- 0 refuted in the run.

## 2. The three e-mail drafts and the new corrections

- **Zheng, Mukai, Esnault (Lemma 2.2 and Prop. 2.5):** the dossier entries are **unchanged** from cp24 to cp35. The
  drafts stand.
- **New, to published work: Esnault Remark 2.3(2), p. 4. Holds** (my check).
  - The remark says the étale locus of σ is non-empty if L is not a p-power. Under §2's standing p | n this is false.
  - Each geometric fibre is (t^m − a)^{p^r}, nonreduced, so σ is nowhere étale.
  - The run's example over 𝔽₂, O_E(T − O) on Y²Z + XYZ = X³ + X²Z + Z³, has E(𝔽₂) = {O, T}, which I rechecked.
  - **Folded into `EMAIL_DRAFT_Esnault_20261123.md` as point 3.**
- **New, to our own posted work: hexagon:2611.00936 v1, Theorem 2. Holds.**
  - Connectedness of the root cover needs dim X > 0. For X = Spec k, Q = O_X and m = 3, Y is three points.
  - Our proof's step H⁰(Q⁻ʳ) = 0 assumed positive dimension silently.
  - **Corrected in `p90a_note_v2` (Theorem 3)**, rebuilt with 0 overfull boxes. The surface theorem is unaffected.
  - Posting v2 now also repairs this. It is for the main session and the user.

## 3. Each paper as a posting candidate: what still blocks it

"Box 8" is HOW.md's required "Proof overview" section; **no paper of the run has it**.

| Paper | Statement | My check | Blocker |
|---|---|---|---|
| 1 | Thms 1.1, 1.2, 1.4 | confirmed (cp12) | box 8; the title names a known result; the Hasse/Schilling literature leads |
| 2 (152 pp.) | as a whole | — | **not postable**: four topics; current-PDF readings at 0/152; the endpoint research still moves hourly |
| 2 | positive-excess theorem and its corollary | confirmed (induction), lemmas at statement level | my read of the three lemma proofs; stability (stable since 20:09 UTC 23 Nov, with a statement-only reconstruction PASS); a literature pass (Langer; Esnault 2006) |
| 2 | conductor-equality structure, a ≠ 6 | confirmed (cp24) | Gu–Sun–Zhou, Shepherd-Barron and Furukawa unread by me |
| 2 | endpoint sections | statement level | not a posting unit on their own |
| 2 | G1 / E4 / local groups | as at cp24 | unchanged |
| 3 | Thm 1.2 | confirmed except Prop. integral-descent | box 8 (the run re-read the paper at 00:41) |
| 4 | Thms 1.1–1.2 | confirmed (algebra part) | box 8; module lemmas; Thm 1.3 |
| 5 | Thm 1.1 | confirmed | box 8; Thms 1.2–1.3; the three bibliography locators |

## 4. Board rows

| id | Title | Statement | Adds | Gate left |
|---|---|---|---|---|
| P90a (update) | A very ample counterexample to Kodaira vanishing on a surface, answering a question of Raynaud | v2 = Kweon corollary + Theorem 3 restricted to positive dimension | answers Kweon Q7.7(ii); fixes the dimension-0 gap of v1 | the user's word to post v2 |
| P90e (revised) | p-torsion line bundles trivial on a curve of positive self-intersection: a genus excess bound | Thm positive-excess-picard (with its equality corollary) | a quantitative Picard-kernel obstruction on any normal surface | my read of the three lemmas; a literature pass; a short note of its own |
| P90b | Picard kernels of very ample curves (conductor equality structure) | as at cp24 | — | stability; sources |

## 5. P vs NP fleet

No new bridge. AG-06 and AG-05 → L-pcx-071 stand.

## 6. Integration

Applied, with backups in `integration_backups/20261123/POLISH_ALGEBRAIC_GEOMETRY/`:
- `p90a_note_v2` (dimension fix);
- the Esnault draft (point 3);
- RECORDS.md (a note);
- PRIMER (updated in place; backup `PRIMER_..._before_cp35.md`).

For the main session: posting v2, the board rows, and sending the three drafts (each awaits the user's yes).
