# Global consistency of the register: sweep 2

Written by Claude Opus 5.5 at effort max (sweep 2), 18 Nov 2026. The rows are by GPT-6 Astra (ChatGPT Pro mode) unless
another model is named. Sources: the register (7,032 rows), plus the 695 rows of FINMON, which the register misses; my
closed graph `GRAPH_EDGES.tsv`; the scripts in `tools/`; and the proofs I opened, each named below. "Read at statement
level" means I read the rows and their dependency fields, not the proof.

## 1. Contradictions between runs or lines

**None found.** No row of one run refutes or contradicts a Proved row of another run among the candidates I read.

The script proposed 33 cross-run "refutes" and 12 "corrects" edges, read from the words around a reference. I read all
of them. Every one is a false positive of the keyword rule, or the refutation is aimed at a paraphrase, a lead, or a
converse, and not at the row it names. The edges now carry what I read: their `how` column in GRAPH_EDGES.tsv begins
"sweep 2 read"; `tools/relabel.py` applies this. The other 146 relation edges from the keyword rule are marked
"unverified".

| Refuting or correcting rows | Rows named | What is refuted or corrected |
|---|---|---|
| ANABELIAN_149_PUSH F.1, F.17; F.31, F.37 | LM5 F.3–F.7, F.38, F.46–F.50 | The prompt's paraphrase R27 dropped "closed-point-preserving" from "pinned". Under that reading the statements are false; LM5's own statements stand. F.7 re-proves LM5 F.50, and F.37 extends it to Q^solv. |
| SECTION_GHOSTS E.100 (final) | LM6 E.16, E.25, E.31–E.34, E.38; LM7 E.25, E.32; LM8_LIE F.21 | The unqualified reading of the prompt's R8: "every Fermat curve has noncuspidal sections in all these quotients". The rows themselves stand. |
| FERMAT_SUCCESSOR C.14 | LM6 A.10, A.49, A.56–A.59, A.66, A.67 | The prompt's paraphrase R18 said "no lift at all". The rows say "no commuting third-derived lift", which is correct. |
| LM7_PUSH B.2 | LM7_FERMAT_TOWER E.19 | The exclusion proposed in Lead 1. E.19 (the three cusp sections are pairwise nonconjugate) stands. |
| PRETOT E.5 | TOTAL_ASPHERICITY G.3 | The converse of G.3. |
| ANABELIAN_149_PUSH B.9 | FLAGGED_149 B5 | The prompt's lead L4. |
| ANABELIAN_SUCCESSOR F.7 | ANABELIAN_149_PUSH F.45 | F.45 is an input of F.7's refutation, not its target. |
| GT_TOWER_CHECK A.3 | EXIT_TOWER E.49 | A repair of two label comparisons in E.49's written proof; the statement stands. |
| INDLOCAL C.27 | PRETOT F.4 | An independent corrected proof; the statement stands. |

Two pairs look contradictory by status alone but state the same mathematics:
- S6_02_PUSH A.3.2 (Proved) and S6_06_BLIND P2.11 (Refuted). Both prove that Engel's Conjecture 8.2 is false. The
  blind run's row is marked Refuted because the conjecture is.
- LM5 F.12 (Proved) and LM8_LIE E.11 (Refuted). Both prove that the inverse 2-limit of the small topoi of shrinking
  punctured disks is degenerate, with the covering germ B Z^r.

So "Refuted" in the register means two things: the row's own statement is false, or the row proves that someone's claim
is false (see §5).

## 2. Proved rows resting on open or refuted rows

| | Within a run | Across runs |
|---|---|---|
| Proved row uses an Open or Unresolved row | 71 | 6 |
| Proved row uses a Refuted row | 488 | 14 |

The within-run rows are the sweep-1 agents' to verdict; they found them sound (tower 83 + 15, sections 79 + 16,
derivateurs 64 + 11, s6 73).

**Across runs, all 20 are sound**, read at statement level:
- LM8_PUSH C.19, C.21, C.24 use LM7_PUSH E.3 (Open) only as the question they reduce. C.21 proves that E.3 is
  equivalent to Δ|GT̂ ≠ 0. E.3 is now decided (§4, SC01).
- ANABELIAN_149_PUSH D.2 and B.15u use CYCLOTOMIC_KERNEL E4 (Open). E4 is a mixed row: H2(a) is proved and H2(b) is
  open. D.2 and B.15u use the proved half, through prompt row R15. E4 should be split (SC17).
- S2COUNT E:boundedtransport uses CATHOT E.17 (Open). E.17 is settled true by INDLOCAL B.1 (SC10).
- The 14 uses of another run's Refuted row each use the counterexample that the Refuted row states:
  - DER_FOLLOWUP F.1, D.4, D.8 use the witnesses Δ_inj (TOTAL_ASPHERICITY C.10) and C_δ (TOTEX2 A.1);
  - DER_FOLLOWUP G.1 uses REVLOC F.1;
  - REVLOC G.3 uses GALOIS B.6;
  - LM6 F.13 uses CYCLOTOMIC_KERNEL B8 (his formulas (32)–(33), scan 127) and confirms it;
  - LM6 F.43 uses LM5 F.22;
  - LM5 F.30 uses STRATA C.7 as its loss-of-mapping-path example;
  - STRATA C.10 uses TOTAL_ASPHERICITY F.18;
  - S2COUNT E:A13, E:matrixobstruction, E:onepair and TASK.E1 use CATHOT E.5, E.13, E.14 and INDLOCAL E.1.

**Three gates carry many proved rows.** Each is unrefereed outside GPT-6 Astra:
- **G1. The p-adic local section theorem** (SC03). 73 rows rest on it, 66 of them Proved
  (`tools/local_theorem_rows.tsv`): LM6 22, LM8_PUSH 21, SECTIONS_OVER_Q 11, SECTION_GHOSTS 6, FERMAT_SUCCESSOR 3,
  ANABELIAN_149_PUSH 2, and others.
  - Its source is OpenAI's preprint "The p-adic section conjecture" (6 Oct 2026, Theorem 1.1). The prompt row R24 of
    ANABELIAN_149_PUSH calls it unrefereed with no formal proof.
  - LM8_PUSH D.54 and D.56 re-derive it, from the preprint's Sections 3–6 and Mochizuki–Tsujimura 2024, Theorem F(i)
    and Proposition 2.4(iv).
  - The sweep-1 agents disagree on its status. Sweep1_tower lists "the full section set of U_n/Q is the three cusp
    packets" as proved, through LM8_PUSH D.23 with D.56. Sweep1_sections lists it as conditional (FERMAT_SUCCESSOR A.20).
  - Both are right about their own rows. The item is proved relative to D.56, and D.56 is the gate. It should read
    Conditional until D.54/D.56 or the preprint is refereed.
- **G2. The gates of Δ|GT̂ = 0** (SC01):
  - route 1 rests on EXIT_TOWER E.44, 𝒥(A) = A, through Boggi–Zalesskii Theorem A(iii) for C₂². I read E.44's whole
    proof and checked its genus-zero algebra and geometry (CHECK_EVENTS). What remains is the exact statement of
    Boggi–Zalesskii 2024 Theorem A (i), (iii) at p = 2, and EXIT_TOWER E.28;
  - route 2 rests on SECTION_GHOSTS E.179–E.181: every normalized GT̂ element satisfies relation (IV) of
    Nakamura–Schneps 2000, and so, by Schneps 2006 p. 670, lies in the group Λ of Hatcher–Lochak–Schneps 2000.

  If E.181 is right, it settles whether every element of GT̂ lies in those groups, a question those papers leave open.
  It must be set against Lochak–Nakamura–Schneps 2026 (arXiv 2602.12462), which proves actions on Γ̂_{g,0} and Γ̂_{g,1}
  and keeps them apart from the full sewing compatibility.
- **G3. GT̂ acts on the full tower** (EXIT_TOWER E.42, with GT_TOWER_CHECK A.6). Both Δ routes use the genus-one part of
  this action; it goes beyond LNS 2026 in the same way.

## 3. Cycles

My parse first gave 63 cycles. Four were my own error: file names such as `ANABELIAN_A1_SUCCESSOR_paper.tex` in
where_proved were read as the id A.1. With that fixed there are **59 cycles, all inside single runs**
(`CYCLES.tsv`). None crosses runs.

- **30 come from summary rows** (22 entirely; in 8, a smaller cycle of proved rows remains). An open or main-question
  row lists in its depends_on the rows that bear on it, and those rows cite it back. The hubs include:
  - LM4_FINITE_GROUP_ACTIONS C.12 (55 out-edges) and D.12 (37);
  - LM7_PUSH B.6, D.51, D.52;
  - EXIT_TOWER E.23;
  - ANABELIAN_149_PUSH F.9;
  - three S6_06_BLIND P3F rows.

  This is a column-semantics problem, not a circular argument. The register needs a relation "bears on", kept apart
  from "uses".
- **29 are mutual citations among proved rows.** I read 10 of them at statement level:
  - a forward reference or a consumer listed as a dependency: TOTEX2 A.24 ↔ A.34, LM4_SUCCESSOR A.96 ↔ A.97,
    LM6 A.49 ↔ A.56;
  - a row that states two things, each used by the other row, so both rows should be split: FERMAT_SUCCESSOR C.4 ↔ C.5,
    EXIT_TOWER E.11 ↔ E.26;
  - EXIT_TOWER E.37 ↔ E.44. This pair sits at the Δ gate: E.37 proves that the outer-group compatibility is equivalent
    to 𝒥(A) = A, E.44 proves 𝒥(A) = A, and each states the combined conclusion. At statement level the argument is not
    circular; the gate still needs its referee.

  Four still have to be read in the TeX: TOTEX2 C.10 ↔ C.27 (possibly a simultaneous induction over stages),
  TOTAL_ASPHERICITY F.2 ↔ F.3, DELTA_ON_GT A.35 ↔ A.37, and DELTA_ON_GT A.97/A.99/A.110. I found no genuinely
  circular argument, but I have not cleared all 29.

## 4. Two statuses for one cluster

`CLUSTERS.tsv` holds 21 clusters across runs, scopes or lines, with 117 member rows. In nine of them the register gives
one piece of mathematics two statuses:

| Cluster | Register statuses | What is the case |
|---|---|---|
| SC01, Δ on GT̂ | LM7_PUSH E.3 Open; DELTA_ON_GT A.84 Open; GT_TOWER_CHECK A.7 Proved; SECTION_GHOSTS E.191 Proved | Decided, Δ|GT̂ = 0, by two routes with named gates. Both runs use the same character: E.191 uses the frames of E.95, whose check column reads "GT_TOWER_CHECK A.7: confirmed", and A.7 uses "the character of the refereed LM7_PUSH E.65". This answers the question sweep1_sections left open. |
| SC10, CATHOT E.17 | Open | Settled true for U-small filtered indexes (INDLOCAL B.1, with GALOIS B.12 and the Dérivateurs expert's OWN_RESULTS Theorem 3.2, Claude Fable 5.2 at effort max). It fails for V-small indexes (B.5). |
| SC11 and SC12, CATHOT G.17 | Open | Two of its three questions are answered by FINMON: the RP² poset minimum is 49 (C3), and K(Z,2) has no finite category or monoid model (E1). The intrinsic classification stays open. |
| SC13, CATHOT D.6 | Open | Answered no by S2COUNT A.M1 and, independently, by FINMON E4. |
| SC02, the Fermat theorem | LM6 E.8 Known; LM6 E.12 Proved; FERMAT_SUCCESSOR A.4 Refuted | E.8's statement stands, but the divisibility step in its cited proof is false, found independently by LM8_PUSH D.22 and FERMAT_SUCCESSOR A.4. E.12 is a mixed row with a conditional third part. |
| SC17, CYCLOTOMIC_KERNEL E4 | Open | Mixed row: half proved, half open. |
| SC18, SC19 | Proved and Refuted | The same statement under two conventions (§1). |
| SC03, the local theorem | Proved in LM8_PUSH; "stipulated" in FERMAT_SUCCESSOR | One theorem, two statuses: a gate (§2). |

## 5. What the register's model needs

These follow from §1–§4. The details are in `CORRECTIONS.md`.
1. **Split "Refuted".** Make two linked items: the claim, which is refuted (his, a conjecture's, or a prompt's), and our
   statement, which is proved. Sweep1_derivateurs (C8) and sweep1_tower reached the same conclusion inside their scopes.
   Across scopes it explains both apparent contradictions.
2. **Register prompt rows and leads as items** (PROMPT:RUN:R27). A refutation of a paraphrase then attaches to the
   paraphrase, and the source rows keep their status. Three paraphrases in this corpus were wrong: R27, R8 and R18.
3. **Keep "bears on" apart from "uses"**, so that summary rows make no cycles.
4. **Mark conditional rows.** The status normalization of sweep 0 drops "conditional on the stated local theorem".
5. **Split mixed rows**: CYCLOTOMIC_KERNEL E4, LM6 E.12, EXIT_TOWER E.11, FERMAT_SUCCESSOR C.4.
6. **Bare ids are ambiguous in successor runs** that number like their sources. For example, SECTION_GHOSTS E.100's
   "E.16, E.31" are LM6's ids, but SECTION_GHOSTS has an E.16 of its own. My rule prefers the run's own id. Sweep 3
   should write the run name with every cross-run id.
