# Intake of RESEARCH_SA21: the supports, the axiom systems and the maquettes of cote 156 (Vers une géométrie des formes, 1986)

- **The run.** GPT-6 Astra (ChatGPT Pro mode), on the prompt as sent: `pro_prompt_builds/RESEARCH_SA21/PROMPT_as_sent_20261119.md`, 4,256 words, uploaded as `PROMPT(20261119-110210).md`. It worked from 11:02:40 to 12:42 UTC on 19 Nov 2026.
- **The return** is filed at `grothendieck_archive_transcription_20261110/research_returns/RESEARCH_SA21_final_20261119T1242Z_unzipped/RESEARCH_SA21/`. It contains:
  - a report of 16,354 words;
  - the paper `RESEARCH_SA21_paper.tex`, with the parts `parts/supports`, `axioms`, `bmodels` and `maquettes`;
  - a results register of 92 statements: 53 proved, 31 refuted, 6 known, 2 proved under stated hypotheses, none open;
  - `RESEARCH_SA21_corrections.tsv`, with 108 rows;
  - `CHECK_EVENTS.tsv`, and programs in `code/`.
- **Taken in by** Claude Opus 5.5 at effort max (agent a6d42bf6fe2b0d8a8, which built the prompt), on 19 Nov 2026. A short pass was finished at 13:10 UTC; the finishing pass, at the main session's request, was finished at 13:26 UTC.
- **What I read:**
  - the report's main classifications, subtask register and source-access record;
  - the definitions and theorems of `parts/supports/supports.tex`, with the proofs of the Boolean criterion (SA21-A04, A06) and the crown (A07) in full;
  - the gate theorem and countermodel statements in `parts/axioms/axioms.tex` (2.17-2.18);
  - all 108 rows of the corrections register;
  - the five ink points, on the scans;
  - the literature named in section 6.
- **What I did not read:** the remaining proofs of `parts/axioms`, `bmodels` and `maquettes` in full; the run's own check events; its programs.
- **Files beside this one:**
  - `INTAKE_RESEARCH_SA21_20261119_CHECK_EVENTS.tsv`: 24 events.
  - `INTAKE_RESEARCH_SA21_20261119_checks.py` and `_checks2.py`, with their `.out`. Both are independent of the run's programs.
  - `readings/INTAKE_SA21_ink_second_pass_20261119.md`: the ink readings, in second-pass form.

## 1. The main answers

**A.1 (main): which ordered sets have an orthomodular or a Boolean support lattice.**
- **The general criterion.** For any orthoset, the support lattice is orthomodular exactly when every maximal orthogonal subset of every closed set generates that closed set. This is Dacey's criterion, cited through Jenča (SA21-A03). Booleanity has an exact point-neighbourhood test (SA21-A04).
- **The interval magasin M(L).**
  - For finite L, Σ(M(L)) is orthomodular exactly when L is a *conditional lattice*: every upper-bounded pair has a join, and every lower-bounded pair a meet.
  - For every L, finite or infinite, it is Boolean exactly when the nonisolated points of L form a chain (SA21-A06, A26).
- **The comparability disjoncteur of L itself.** A cograph comparability graph is sufficient for orthomodularity, and strictly so. The Sumner-normality equivalence the prompt proposed is refuted (SA21-A25).
- **Checked:**
  - **By computation, on all 87 posets with at most 5 elements:** both M(L) classifications and the A04 test, with 0 disagreements. Cograph sufficiency holds, and it is strict: one orthomodular non-cograph poset on 5 points. The four-point crown has 8 strata and 20 supports and is not orthomodular, yet its orthogonality graph satisfies Sumner's clique condition. That separates the two notions, as the run says.
  - **By reading the proof:** the infinite-L Boolean criterion (E01-E07, E08, E17).
- **Placement in the literature.** For a finite *bounded* poset, the interval-only version of A.1 is a published theorem. Jenča, *Orthogonality spaces associated with posets* (arXiv:2206.08113; Order 40 (2023) 575-588), proves that for a finite bounded poset P:
  - P is a lattice iff its space Q(P) of proper quotients is Dacey, iff L(Q(P)) is orthomodular;
  - P is a chain iff L(Q(P)) is Boolean.

  Q(P) is the interval part of M(L), with the same orthogonality. The run's new content is the extension:
  - to M(L) with its point symbols;
  - to unbounded finite posets (conditional lattices);
  - to arbitrary L for Booleanity.

  It cites Jenča for the bounded theorem. Its correction to Jenča's v1 is right: the corollary [x<y]^⊥⊥ = [x<y]^↓ is stated "for every poset" there, but its proof uses boundedness, and two disjoint two-element chains refute it (E18).
- **Our lead L2** (fences and "repairs") is replaced by these criteria.

**A.3, his Question of 156-9/3.** Every lieu support is an atom exactly when L is an antichain or has no isolated points. Checked by computation up to 5 elements (E06).

**A.2, A.4 and A.5.** The A.4 characterization of the Théorème of 156-7/94 by the two-neighbourhood condition, and the incidence-coverage clause for (d), were read in statement form only.

**B: the axiom systems.**
- **C4.** It fails in Fig(L) from |L| = 2, and the run's classification of the incidence components is exact. By computation with our reader A's 156-5 definitions, the component counts for |L| = 1 to 4 are 1, 3, 5 and 6: the whole set isolated, a two-object component for each co-singleton, and one more component for |L| ≥ 3 (E16). The true global statement uses refinement components (B-K45, B-K46).
- **At9Σ + At10 ⇒ At12.** The gate theorem reduces At12 exactly to membership of the common-refinement deployment in Σ (E23). The countermodel was read but not recomputed.
- **At14bis.** The object is not unique, but the abstract deployment is (E24).
- **L1, refuted and replaced.** The finite contrées that are event-configuration domains are exactly the locally distributive ones: the binary-conflict prime event structures with finite causes. This follows from Nielsen-Plotkin-Winskel 1981, p. 102, which I opened, and Birkhoff's finite representation (E20, E22).
- **L5, settled.** The run settles it with closed-support generalized cells, with no Hauptvermutung needed. Not checked here: its triangulation source (Coste, Theorem 4.4) could not be downloaded, because the host was unreachable from here.
- **R8 and L6.** R8 is overbroad, and L6 is false (B-K29, B-K30).

**C: the maquettes.**
- **L4 is false.** The run's torus with a formal top cell is a counterexample. My 3 × 3 torus has diamonds, zero-sum signs and a connected boundary of the top cell, and that boundary has Euler characteristic 0, not 2 (E15). So it is not the face poset of a regular CW complex.
- **The corrected theorem (SA21-C08)** asks for finite principal ideals, spherical lower intervals, unique immediate oriented lifts and coherent signs. That is Björner's CW-poset criterion with orientations. The locator, Björner 1984, Prop. 3.1, is confirmed through two secondary sources, Clark-Tchernev (arXiv:1310.2315) and Hersh (arXiv:1411.1296); I could not open the original (E21).
- **The simplicial characterization (C09-C12)** was read in statement form only.

## 2. His text

**Decided on the scans** (the full readings are in `readings/INTAKE_SA21_ink_second_pass_20261119.md`):
- **156-6 (1.20), scan 12, the decisive point.** The ink reads "X str^t. irréductible pour ≤, i.e. X ≤ Sup_i F_i ⇒ ∃ i avec X ≤ F_i". That is the prime condition. **His 156-6 representation (deployment) theorem therefore holds as written.**
  - Scan 17 renames C1-C3 as At 1-At 3.
  - What fails is the equality-based irreducibility of 156-4 (scans 54-57) and of the later independent atlas list of 156-8 (scans 20-21). There M3 is a model, and the claimed equivalence with atlases of clique down-sets needs the prime repair (B-K01, B-K05, BM-K30).
- **156-6 scan 88.** The quantifier of At14bis runs over all of F̃′. The run's exterior version is a mathematical correction (B-K24): the literal clause forces order reflection.
- **156-8 scan 31, Mag 4′.** It has no negation, and our earlier reading stands. In that positive form it is weaker than Mag 4 of scan 8 (our K8-03; B-K34).
- **156-8 scan 4, Magor 2 b).** The superscript is X^ε.
- **156-9 scan 113.** The set is {E ∈ 𝔓(I) | i, i′ ∈ E or i, i′ ∉ E or E = {i} or E = {i′, j, k}}. It is the ten-element ortholattice he draws, and it is not orthomodular. This is computed: lattice, orthocomplemented, 14 covers, 4 failures of the orthomodular law (E14).

**The rest of his text, from the corrections register (108 rows, all read).** The run's main findings on his pages:
- 156-5/13-15: C4 "est automatique" is false.
- 156-4: missing hypotheses and a false infinite admissibility shortcut (scan 27; the tail family A_n). C8₀ and the final C8 are different axioms (B-K13).
- 156-6/78-80: At9Σ + At10 does not give At12.
- 156-6/88: At14bis object uniqueness fails.
- 156-6/34: the shortened At* list omits the membership clause.
- 156-8: divisibility is weaker than local detection (B-K31). The Proposition-Scholie lacks internal transitivity (B-K32; this confirms ours). There is a variable mismatch on scan 30, corrected by scan 31 (B-K33). The later Mag div 3 tests comparable pairs only (B-K36).
- The maquette sources: the literal reversal axiom conflicts with oriented inequality (C-K01), and the variable reading of 1′(b) matters (C-K03).

## 3. Ours (corrections to our study, our checks and the prompt)

- **R12 and our check events SA21-C3-05 and -06 ("holds") are wrong** for the literal 156-4 definition. They need bounded-join primality; the exact class is the locally distributive one (B-K02, BM-K03 to K05). For 156-6 they are right, because of (1.20).
- **Our SA21-R6-12 is upheld** (BM-K11).
- **Our reading 156-6.md, line 31, cites (1.20) without its "i.e." clause.** The clause is in the ink and in the transcription.
- **R8 is overbroad, and L6 is false** (B-K29, B-K30).
- **H1 lacks primality** and the binary-conflict qualification (BM-K07).
- **H6-2: extension needs no Hauptvermutung** (BM-K15 to K17).
- **Our prediction about tame global incidence components is false** (BM-K19).
- **Our reading of Mag 4′ (no negation) stands** on the scan. The run did not decide it.

## 4. New results

- The extension of Jenča's bounded theorem to the interval magasin with points and to unbounded finite posets.
- The Boolean criterion for arbitrary L.
- The atom theorem (A.3).
- The A.4 characterization.
- The exact event-structure class of contrées (B.3).
- The o-minimal atelier (B.4).
- The all-dimensional oriented-maquette theorem with its torus counterexample (C.1-C.2).

The run claims no priority, and records its searches. The correction to Jenča's v1 corollary concerns a published preprint. It belongs on the outreach list ("informing authors"), and it should go out only after the journal version (Order 2023) has been checked for the same statement.

## 5. Ink claims for a reader

All five points named in the short intake were decided on the scans (section 2). Three readings change and wait for the next second pass of cote 156:
- 156-9/113: "i, i′ ∉ E";
- 156-9/113: 𝔓(I);
- 156-8/4: X^ε.

## 6. Literature locators

| Source | Opened? | Outcome |
|---|---|---|
| Jenča 2022, arXiv:2206.08113v1 | yes (LaTeX) | Dacey's theorem; main theorem; Boolean theorem; corollary error as the run says (E18) |
| Paseka-Vetterlein, arXiv:2003.03313v2 | yes (LaTeX) | Definition of normality (E19) |
| Sumner 1974, J. Austral. Math. Soc. 18, p. 492 | yes (publisher PDF) | Dacey graph defined via the orthomodular logic; clique condition taken as the definition (E19) |
| Nielsen-Plotkin-Winskel 1981, TCS 13, p. 102 | yes (author PDF) | Event structures ⟷ prime algebraic coherent orders (E20) |
| Björner 1984, Eur. J. Combin. 5, Prop. 3.1 | no (403; the mirror needs a login) | Confirmed through Clark-Tchernev and Hersh (E21) |
| Coste, *An introduction to o-minimal geometry*, Th. 4.4 | no (host unreachable from here) | Not checked; it bears on B.4 only |

## 7. Is a further prompt warranted?

**No research prompt.** The run reports no open item. My checks agree with it wherever I could check:
- the computations on all small cases;
- the infinite Boolean proof;
- the decisive (1.20) reading;
- the literature behind A.1.

What remains is checking in use, and folding into the record:
- the long proofs I did not read: the remaining axiom-atlas implications and models, the o-minimal model, and C08-C12;
- the countermodel of 2.18, by recomputation;
- the Coste and Björner originals, when they can be opened;
- the three ink changes, at the next second pass of cote 156;
- sections 2 and 3, into SA21's STUDY, HUNCHES, CORRECTIONS and CHECK_EVENTS at the next rebuild.

None of this needs a Pro slot.
