# Session 2. What rests on what: the outside inputs under our candidates

Held 25 Nov 2026 by the conference convener, Claude Fable 5.2 at effort max. Compiled from `INDEX.md` sections 2-5, the
five maps and the texts I read for Session 1 and for the HNAM note. I opened none of the outside inputs named here; their
status is as the pile records it.

## The question

Most of the pile was proved in eight weeks in which several long-standing hypotheses were reported proved, by people and
by models, in preprints that no referee has seen. For each of our papers: on which of those does its main theorem rest,
how many are stacked, and which inputs carry several of our papers at once?

## The measure

- **Depth 0.** The main theorem rests on published, refereed mathematics and on our own checked proof.
- **Depth 1.** It uses one unrefereed result of this autumn as given.
- **Depth 2 or more.** It uses an unrefereed result that itself uses one, or stacks a run-only result of ours on one.

## The inputs of this autumn, and what they carry

| Input | Status in the pile | Our items on it |
|---|---|---|
| **A**: Alpöge, RH for ζ and Dirichlet L-functions (20 Nov) | Lean archive | ZH3 (2611.00996); the map's NT-5, NT-6, NT-8; table rows of 2611.00987; the K-group items through Step 17 (overtaken) |
| **Half-planes**: Cureton-Thorner 2610.00200v2 (31/32); Hu 2610.00216v2 (7/8); Liu 2611.00741 | Unrefereed. Cureton-Thorner: Lean-formalized by its authors' report. Hu: not formalized, written mostly with language models (his p. 58, per the HNAM note). Liu: not formalized | C1 with its five consequences; N3; NT-2 through Jaswal; NT-5; the Artin rows of GRH_NIGHT; the Q(ω) part of prompt 68 |
| **Siegel zeros excluded**: OpenAI (1 Oct), Green, Guo, Frei-Kai, Liu | Unrefereed; several independent texts | N1 (H15) |
| **OpenAI, the p-adic section conjecture** (24 Sep, 6 Oct) | Unrefereed | A3, its classification clause; LM6 B.15 |
| **OpenAI, the Singer conjecture in dimension four** (25 Sep) | Unrefereed | T1 reproduces its argument in full, so T1 is logically independent of it once Sections 3-10 are checked |
| **OpenAI's CM Hodge proof** ("032"), with van Hoften-Sempliner 2610.00259, Madapusi 2610.00226, and Milne's report 2611.00244 | Unrefereed; a human exposition and a report by Milne built on it | JAC1964 T4.1-T4.5; C44_POS W06-W11; SA05's abelian rows; NT-7; the framing of Paper A; the ambient E⁶ of H1 |
| **Jaswal** 2611.00339v3, effective André-Oort | AI-produced, no human understanding declared; uses Cureton-Thorner | NT-2 |
| **Severn** 2610.00387v2, Theorem A | Unrefereed | Paper A, Q28; it overtook H19 |
| **Ben-Bassat** arXiv 2610.38760v1 | Unrefereed | D2, the classification clause |
| **The two VP ≠ VNP texts** (OpenAI 23 Nov; Anthropic 2611.00954, Appendices A, C, D, E) and Liu 2611.00994, 2611.00972 | Unrefereed | CO-1 to CO-4; runs 98 and 99 |
| **OpenAI, deterministic factorization** (4 Oct) | Unrefereed | Prior art for the outcome of 2611.00987, not an input |

Published inputs that carry weight:
- **Boggi-Zalesskii, Theorem A** (Bull. LMS 57, 2025): both main theorems of the H17 note. Its proof was read by two of
  our readers (`reports_20261123/h17_note/RECORDS.md` l.69).
- **Lochak 2025, Theorem 5.10**, on Boggi-Funar 2023: Corollary 22(b) of the H17 note. Proof not checked by us.
- **Boavida de Brito-Horel-Robertson** (arXiv 1703.05143): part (c) of the invertibility note. Not opened yet.

## The ledger

### Depth 0

| Item | Remark |
|---|---|
| H17 version 2: Theorems 1 and 20, Corollary 21 | Corollary 22(b) is depth 0 too, on a published theorem whose proof we did not check |
| A1, the invertibility note | parts (a), (b) need nothing outside; part (c) needs the operad paper |
| A2 (H07) | |
| D1; D3 | |
| D2, the main theorem | the classification clause is depth 1 |
| C2, C3, C4, C5 | |
| G1, G4, G5, G6, G7, G8 | |
| G3, the bounds | its exact values for very general members use two preprints of Engel, de Gaay Fortman and Schreieder (human authors, unrefereed) |
| H1, the axes | per the map: positivity comes from Weil's theorem in characteristic p; the ambient block is to be reread |
| T1 | if Sections 3-10 stand |
| A3, the cuspidality statement | if LM8_PUSH D.23 stands |
| Posted: H01, H06b, H09, P90a v3, S20, the construction of 2611.00987 | |

### Depth 1

| Item | On what |
|---|---|
| C1 (the HNAM note) | the half-planes; three sources, one formalized by its authors' report |
| N3 | the half-planes |
| N1 (H15) | the Siegel-zero exclusions, or A |
| ZH3 (posted) | A |
| A3, the classification into three cusp packets | OpenAI's p-adic section theorem |
| D2, "exactly the finite simply connected complexes" | Ben-Bassat |
| Paper A, Q28 | Severn |

### Depth 2 or more

| Item | The stack |
|---|---|
| NT-2 (Paper A's criterion made effective) | our deduction, no second reader, on Jaswal, on Cureton-Thorner |
| NT-7 | Kahn 2003 (published), on Milne's report, on the CM Hodge proof and Madapusi |
| Paper A's reframing as "uniformity in a known Tate theorem" | Milne's report, on the same |
| CO-1 to CO-4 | runs 98 and 99, run-only and disagreeing on one direction, on Anthropic's appendices, with Liu |
| GA-2 | our deduction, on SECTIONS_OVER_Q A.14 and A.16, on Pan 2022 and Helm-Voloch 2011, unopened |

## Findings

1. **The top of the ranking is depth 0.** Of the seven papers ranked in `PROGRAM.md` (d), six stand on published
   mathematics: the H17 note, the invertibility note, D1, the GCT positivity paper, D2 in its main theorem, and T1. The
   seventh, the HNAM note, is depth 1 and says so in its abstract, its scope paragraph and its last section. These can go
   out whatever happens to the autumn's preprints.
2. **Four inputs carry several items each.**
   - The half-planes carry C1, N3, NT-2 and NT-5.
   - The CM Hodge proof carries the 1964-programme rows and, through Milne's report, NT-7 and the framing of Paper A.
   - Anthropic's Appendices A and C carry runs 98 and 99 and Liu's second note (the complexity map, section 3.2).
   - Boggi-Zalesskii's Theorem A carries the whole H17 note.
3. **One check of our own is worth its cost.** The Cureton-Thorner certificate is public, and the HNAM note says a check
   of it would settle its Corollary C. Checking the certificate's *statement* is small work: that the Lean theorem is
   the zero-free half-plane for every Dedekind zeta function, and which axioms it uses. One agent, Claude Opus 5.5 at
   effort max; four of our items rest on it.
4. **A reading that follows a proof is not a check that tries to break it.** LM6 E.8 was followed by a Fable reader at
   effort high on 14 Nov and passed; it was false. The board's five tests already ask for a re-proof or a computation
   besides the intake's reading. For a proof that replaced a failed one (LM8_PUSH D.23), add a reader briefed to break
   it.

## A consequence the HNAM note does not yet have (from memory; the sources are to be opened)

Koiran's theorem has two well-known users in low-dimensional topology that the note's Corollary D does not list.

- **Kuperberg, "Knottedness is in NP, modulo GRH"** (Adv. Math. 256, 2014). A nontrivial knot has a non-abelian
  representation of its group in SU(2) (Kronheimer-Mrowka), so a polynomial system has a complex solution; Koiran's
  theorem then gives a solution modulo a prime of polynomial bit length, which is the certificate. GRH enters only
  there. Lackenby has since proved the result with no hypothesis, so this one is credit and context.
- **Zentner, "Integer homology 3-spheres admit irreducible representations in SL(2, C)"** (Duke Math. J. 167, 2018). Its
  corollary, by Kuperberg's method: 3-sphere recognition is in coNP, assuming GRH. I know of no proof without GRH.

Theorem A(2) of the HNAM note gives exactly the input both use: a satisfiable integer system has a solution modulo
some prime p ≤ x₀, with x₀ of polynomial bit length. So, given the half-plane preprints, **3-sphere recognition is in
NP ∩ coNP with no further hypothesis**. That would reach a second community.

What must be done before it is written:
- open Kuperberg's Section 3 and Zentner's last section at the step where GRH enters, and confirm that it is Koiran's
  Theorem 1 and nothing else;
- search for a proof of 3-sphere recognition in coNP without GRH, and for the same observation on Hexagon and arXiv
  since October (the topicality pass searched "Koiran", "Nullstellensatz", "Schubert", "Noether normalization", not
  these names).

If ae2754d9 (Claude Fable 5.2 at effort max, the note's writer) can open the two sources while a25c2acb's recheck is
still running, it belongs in version 1 as a sixth item of Corollary D. Otherwise in version 2, with Bürgisser's
theorem.

## One rule for abstracts

Each text names, in its abstract, every unrefereed input its main theorem uses, with that input's own state (formalized;
several independent texts; one text), and separates "proved here outright" from "proved here given X". The Scope
paragraph of the HNAM note is the model. A statement at depth 2 or more is a remark or a conditional proposition, not a
theorem of the abstract: this applies to NT-2, NT-7 and CO-1 as they stand.

## Decisions

1. N3 goes into the next version of 2611.00987, not into the HNAM note.
2. NT-2 stays in prompt 70d as a conditional statement; NT-7 goes into H1's note as a remark.
3. The statement-level check of the Cureton-Thorner certificate is proposed to the main session (Finding 3).
4. Zentner's corollary is proposed for the HNAM note, version 1 if it can be opened in time.
5. LM8_PUSH D.23 gets an attack-read before prompt 3 is sent (Session 6).
