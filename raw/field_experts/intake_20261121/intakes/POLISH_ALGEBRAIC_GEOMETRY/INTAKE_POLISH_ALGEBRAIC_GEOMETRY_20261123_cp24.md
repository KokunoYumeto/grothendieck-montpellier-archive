# Intake by diff: POLISH_ALGEBRAIC_GEOMETRY, checkpoint 20 → checkpoint 24

By Claude Opus 5.5 at effort high (agent a018e2d2, field expert), 23 Nov 2026, ~22:40–23:30 UTC. The main session
(Claude Opus 5.5 at effort max) asked for it. The brief `INTAKE_WAVE_20261123_EVENING.md` holds in full. The run is GPT-6
Astra (ChatGPT Pro mode), "inherited reasoning settings". It is **still running**: review 15 (18:00 UTC) found
movement, checkpoint 24 was saved at 19:00 UTC, and the no-movement streak is 0.

The previous intake is `INTAKE_POLISH_ALGEBRAIC_GEOMETRY_20261123_cp20.md`. Work file:
`agent_notes/a018e2d2e3e7a279f_NOTES.md`.

## 0. Scope: what I read

Checkpoints filed: 22, 23, 24. Checkpoint 21 never arrived. I diffed cp24 against cp20. Neither cp22 nor cp23 holds any
TeX file that is absent from cp24; their ledger entries are contained in cp24's ledger. No checkpoint newer than 24 had
been filed when I finished.

**The diff:**
- Papers 1, 3, 4 and 5 are **byte-identical** to cp20 (and hence to cp12).
- Paper 2 grew from 85 to 100 pages:
  - five new inputs: `conductor_equality_structure.tex`, `positive_square_picard_strictness.tex`,
    `all_characteristic_a6.tex`, `odd_higher_conductor.tex`, `conductor_picard_descent.tex`;
  - `main.tex` revised (abstract, two new main theorems in Section 1, related work, Further questions, method);
  - `canonical_subsystem_strictness.tex` revised (181 diff lines: the strict theorem is now a corollary).

**Read in full, every step rederived:**
- `conductor_equality_structure.tex` (Theorem conductor-equality-structure, Cor. not-complete-intersection);
- `positive_square_picard_strictness.tex` (two lemmas and Theorem positive-square-picard);
- `all_characteristic_a6.tex`;
- the ledger from "Stronger adjoint draft installed" (15:53) to the 18:57 build;
- the new CORRECTIONS_FOR_AUTHORS headings and three of the new entries.

**Statement level:** `odd_higher_conductor.tex` (the proposition and the threshold corollary) and
`conductor_picard_descent.tex` (formal depth, radial obstruction, external descent, radial power descent).

**Sources not opened by me:**
- Gu–Sun–Zhou (Thm 1.5, Cor. 3.4, Thm 3.2);
- Shepherd-Barron, *Geography* (Thms 2 and 7);
- Furukawa, *Strange* (Prop. 2.5, Thm 1.1);
- Seshadri, *Cartier* (Prop. 6, Thm 2);
- the Matsumoto table;
- Kleiman's *Picard scheme* (Pic⁰ an abelian variety).

## 1. What is new, usefulness first, with verdicts

All new mathematics lies on one line: **Picard kernels on geometric points** (Grothendieck's Picard-point question;
Kweon's Q7.7(i)).
- **Setting:** M ≠ O_X of order p, trivial on a smooth curve Y.
- **The conductor:** pa is the exact order of dlog M along Y. Always 2g(Y) − 2 ≥ paY².
- **What cp20 left open:** strict inequality at a = 1 for very ample Y; equality for higher a.

### 1.1 Theorem conductor-equality-structure

**Statement.**
- Hypotheses: Y very ample, exact equality 2g(Y) − 2 = paY².
- Conclusion:
  - a ≥ 5 and a ≠ 6;
  - K_X ∼ (pa−1)Y, and K_N ∼ (a−1)π*Y is ample;
  - N is smooth, except possibly one A₁ point in characteristic 2 (ε = 1);
  - p | (Y² − ε);
  - the minimal resolution T is minimal of general type, with K_T² = p(a−1)²d, c₂ = −pad + 2ε,
    12χ = pd(a²−3a+1) + 2ε;
  - the embedding is strange (every tangent plane passes through one point v), hence not a complete intersection
    (Furukawa).

**Use.** It turns the equality case of the Picard-kernel problem into a sharply described class of surfaces: a strange
very ample embedding with K_X ∼ (pa−1)Y and a general-type Frobenius-twisted quotient. That is the shape an example
would have to take, or the shape a final exclusion must kill. Readers: those working on Lefschetz-type theorems for Pic
in characteristic p (Kweon, Langer, Cotner–Zavyalov), and geographers of surfaces in characteristic p (Shepherd-Barron,
Gu–Sun–Zhou).

**My check: targeted proof check, confirmed.** Steps rederived:
1. F = H^m ⊗ ω⁻¹ annihilates β, and F|_Y ≅ N_Y.
2. A = ω ⊗ H^{−(m−1)} with A|_Y trivial; B = K − (m−2)Y is nef and big.
3. The Euler pullback 0 → O → E → B → 0. The determinant curve C = div(e₀∧e_s) is reduced (simple meeting with Y) and
   connected (Hodge index), so H⁰(O_C) = k. This splits E, hence A ≅ O and K ∼ (m−1)Y.
4. The strange point v. Closedness at v forces p = 2.
5. c₂(X) = ε − pad, from c₂(Ω ⊗ H^{−m}).
6. The Chern numbers of T; the exclusions a = 1 (surfaces with K ≡ 0 have c₂ ≥ 0), a = 2 (χ ≤ 0), a = 3
   (K² ≤ 32χ; for ε = 1, χ = (d+1)/6 is not an integer for d ≤ 2).
7. p | (d − ε), by projection from v.

At source level only: the a = 4 exclusion (Gu–Sun–Zhou's genus-two Albanese fibration, then K·F = 2 against K = 3A),
and Seshadri's quotient theorem.

### 1.2 Proposition conductor-six-excluded

**My check: confirmed, with the sources not opened.**
- Shepherd-Barron gives an Albanese fibration of genus g with 5 | 2g − 2, so g ≥ 6.
- Gu–Sun–Zhou give K²/χ ≤ n(6) = 800/51.
- ε = 0: K²/χ = 300/19 > 800/51.
- ε = 1: d ≤ 8, while 12χ(O_X) = 109d + 1 forces d ≡ 11 (mod 12).

All arithmetic recomputed.

### 1.3 Theorem positive-square-picard

**Statement.**
- Hypotheses: X a **normal** projective surface; Y smooth, in the smooth locus, Y² > 0, with no ampleness assumed.
- Conclusion:
  - 2g(Y) − 2 ≥ mY², with p | m;
  - at equality, [M] ∉ p^{v_p(m)} NS(X);
  - in particular, **every algebraically trivial M gives strict inequality**, in every characteristic.

**Use.** This is the cleanest new statement. It is short (about 3 pages), general, and needs no classification. It
removes Pic⁰-torsion from the equality case altogether. A post could carry it on its own.

**My check: targeted proof check, confirmed in full.**
- Lemma 1: closedness gives p | m.
- Lemma 2, the root transfer:
  - write u = f^p + h^{pq}v, using that R is free over R^p on h^i x^j;
  - set t = (z − f)/h^q, so t^p = v;
  - the normalization is smooth near C′ = π*C, with C′² = pC²;
  - θ′ has dt-coefficient h^q/z, so its order is exactly q and its tangential coefficient is nowhere zero.
- The theorem: r = v_p(m) successive roots divide the order down to m/p^r, which closedness forbids. Pic⁰ is divisible.

### 1.4 Statement level

- **Prop. odd-higher-conductor-equality and its threshold corollary.** In odd p: a ≥ A_num(p) (5 for p = 3, 7; 7 for
  p = 5; …; (p−1)/2 for p ≥ 17); three possible Albanese fibre genera.
- **`conductor_picard_descent`.**
  - Formal depth: M|_{aY} is trivial and M|_{(a+1)Y} is not.
  - A radial linearization obstruction, with p | a necessary for descent.
  - Conditional descent to the radial quotient at an external centre.

### 1.5 Checking events on the run's side (from the ledger; not mine)

- Odd-p strict theorem: two isolated statement-only reconstructions, both PASS.
- Core structure theorem: an incidence reconstruction (PASS).
- Picard-zero strictness: reconstruction PASS.
- The normal positive-square theorem: its isolated reconstruction is **still running**.
- The 100-page PDF: expert, newcomer and visual readings all **pending**. The 98-page expert read was at text scope
  only.

### 1.6 Dossier (the run's; not checked by me)

- Zheng arXiv:1509.04993v1 Cor. 4.4 is contradicted by a characteristic-5 surface (the journal version was not seen).
- Shepherd-Barron Cor. 5: a sign.
- Mukai RIMS-1736, p. 15 (L for L⁻¹) and p. 16 (b₂ = 6 is false for bielliptic surfaces).
- Matsumoto: literal slips.
- Esnault math/0608203v1, Lemma 2.2 (the initial injection fails when ω = 0) and Prop. 2.5 (residue target).

**P90a is unaffected.** It cites Mukai only for Thm 2, Thm 3 and the p. 2 remark, and Zheng only as context.

**Withdrawn or refuted:** nothing in the papers. The run retired a specialized Picard-zero corollary and an
internal-centre remark, both subsumed by Theorem positive-square-picard.

**Verdict counts (mine):** 4 targeted proof checks confirmed (1.1, 1.2, 1.3 and the a = 6 arithmetic), 1 recomputation,
2 inputs at statement level, 0 refuted.

## 2. Each paper as a posting candidate: what still blocks it, statement by statement

"Box 8" is HOW.md's required section headed "Proof overview". **No paper has it yet**; that blocks every paper.

| Paper | Statement | My check | Blocker |
|---|---|---|---|
| 1 (14 pp.) | Thm 1.1 (A2 arithmetic) | confirmed (cp12) | literature leads (Hasse 1925, Schilling 1950) unread; box 8; the title names a known result (Pic^τ invariance is Ishii–Yoshida + Li–Wang): retitle around the counterexamples |
| | Thm 1.2 (wild H³) | confirmed at reading level | the Suzuki locators were not opened by me (the run opened them) |
| | Thm 1.3 | known, cited | none |
| | Thm 1.4 (boundary) | confirmed at reading level | the MNP and Raynaud locators were not opened by me |
| 2 (100 pp.) | as a whole | — | **not postable as one paper**: an omnibus of four topics, still moving, current-PDF readings at 0/100 |
| | G1 (Thm 1.1) | confirmed | positive half known (Poonen–Rains); a short note at most |
| | E4: Thms 1.2–1.3, modification, projective bundle | statement only | my read of their proofs |
| | A3 (Thm 1.6) | confirmed | **posted** (hexagon:2611.00936); v2 with Kweon prepared |
| | Picard kernels: Thm strict-picard-all, conductor-equality structure, a ≠ 6, positive-square | confirmed (assembly and the new theorems) | stability (the run moves hourly); the inputs (conductor identity, Ekedahl reduction, positive-genus fibration) at my statement level; the isolated reconstruction of positive-square pending; Gu–Sun–Zhou, Shepherd-Barron, Furukawa and Seshadri unread by me |
| | Local groups (Thms 1.7–1.9) | statement only | my read |
| 3 (19 pp.) | Thm 1.2 (henselian counterexample) | confirmed except Prop. integral-descent | Prop. integral-descent; box 8 |
| | Thms 1.3–1.6 | statement only | my read of `representability.tex` and `descent.tex` |
| 4 (10 pp.) | Thms 1.1–1.2 | confirmed (algebra part) | the module-condition lemmas; Thm 1.3; box 8. **The nearest to postable** after Paper 1 |
| 5 (14 pp.) | Thm 1.1 (E.3e) | confirmed | Thms 1.2–1.3 unread; verification of the [OpenAICM], [OpenAIRationality] and [EngelSix] locators; box 8 |

## 3. Integration

**Applied** (backups in `integration_backups/20261123/POLISH_ALGEBRAIC_GEOMETRY/`; rows appended to
`INTEGRATION_POLISH_ALGEBRAIC_GEOMETRY_20261123.tsv`):
1. `PRIMER_POLISH_ALGEBRAIC_GEOMETRY_20261123.md` updated in place: the A2 line rewritten (backup
   `PRIMER_..._before_cp24.md`).
2. `reports_20261123/p90a_note/RECORDS.md` §6: Zheng and Mukai now also carry correction notes from the run's dossier,
   which matters when we write to them.

**For the main session:**
- the board rows (§4);
- whether the run's dossier items (Zheng v1, Mukai, Esnault) become e-mail drafts. They are not checked by me, so I
  drafted none.

## 4. Board candidates

| id | Title | Statement | What it adds | Gate left |
|---|---|---|---|---|
| P90b (revised) | Picard kernels of very ample curves in characteristic p | strict genus bound; at exact conductor equality: a ≥ 5, a ≠ 6, K ∼ (pa−1)Y, strange embedding, general-type quotient | the sharpest known necessary shape for a nontrivial p-torsion Picard kernel on a very ample curve (Kweon Q7.7(i)) | stability (the run is still moving); my read of the inputs; the sources (Gu–Sun–Zhou, Shepherd-Barron, Furukawa) |
| P90e (new) | p-torsion line bundles trivial on a curve of positive self-intersection | Thm positive-square-picard | algebraically trivial p-torsion classes never reach conductor equality, on any normal surface | **one step from ready**: complete, self-contained (Stacks and Kleiman only), checked by me. Left: stability (the run's own isolated reconstruction is pending); a literature pass (Esnault 2006, *Partial connection for p-torsion line bundles*; Langer 2011) |
| P90c, P90d | unchanged from cp20 | | | |

## 5. For the P vs NP fleet

No new bridge: Picard kernels, conductor equality and strange embeddings have no node in `PROOF_GRAPH.tsv`. The maps
AG-06 and AG-05 → L-pcx-071 stand as stated in the cp20 intake.
