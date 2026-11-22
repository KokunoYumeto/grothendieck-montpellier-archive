# Full intake of RESEARCH_SA09 (final 20261119T1146Z), statement by statement

- **The run.** GPT-6 Astra (ChatGPT Pro mode); its return is
  `research_returns/RESEARCH_SA09_final_20261119T1146Z_unzipped/RESEARCH_SA09`, with a 41-page paper.
- **This intake.** Claude Opus 5.5 at effort max (agent a34c04448e8299803), 21-22 Nov 2026, as asked by the coordinator
  (the user, 21 Nov ~23:5x UTC: [the user's words, omitted]).
- **The list.** All 43 statements of the register, from `field_experts/INTAKE_LEDGER.md` section 9.
- **Check events.** 44 events in `INTAKE_RESEARCH_SA09_20261121_full_CHECK_EVENTS.tsv`.
- **Computations.** `intake_scripts/full_intake_sa09_checks.py` (A1.9, A2.5, A3.1, A4.4) and
  `intake_scripts/intake_checks_sa09_B.py` (B2, B4), each with its output. Neither runs a program of the return.
- **Earlier intake.** `INTAKE_RESEARCH_SA09_20261119.md` (17 events, INT-SA09-E01-E17), by the same agent. Its events
  are re-entered here under their exact statement ids, citing their earlier numbers.

## 1. What was checked

Every statement was read with its proof in the paper (`sections/A1.tex` ... `B4.tex`).

| Check type | Events |
|---|---|
| targeted proof check | 21 |
| independent re-proof | 10 |
| computation or formal certificate | 7 |
| carried as background without fault found | 6 |

The six background rows are the known results the run cites: A1.1 (Roby), A2.6 (Happel), A3.3 (Horel, Mandell, Toën),
A4.1 (Dold-Puppe), A4.3 (Stacks 066Z) and B0.1 (dessins). Their sources were not opened. A4.5's criterion (Stacks 0G99)
is carried too, but its counterexample is re-proved.

**Read in full and confirmed.** Every proof that carries the run's answers:
- **Part A (cote 137).**
  - The polynomial-law category (A1.2).
  - The refutation of L1 (A1.3).
  - The Hom-law Γ^p for all modules (A1.4).
  - Independence of the unit axiom (A1.5), with the F_2 exterior-power model.
  - Failure of the printed equivalence (A1.6), with the F_3 twist c_{p,q} = t_{pq}/(t_p t_q^p).
  - Failure of automatic enrichment (A1.8), with the cubing counterexample over F_4.
  - The scalar-weight valuations (A1.9), re-proved, with 1001 numerical tests and no mismatch.
  - The essential image over every ring and over PIDs (A2.2, A2.3), and its exact-category versions (A2.4).
  - The Sex1-2 counterexample (A2.5), computed.
  - The test objects R_n (A3.1) and the reconstruction from the full Γ-action (A3.2).
  - The lens spaces (A3.4) and the binomial operations (A3.5).
  - The rank criterion and Prop. 1(e) (A4.2, A4.4, A4.6).
- **Part B (cote 138).**
  - The pinned-map count and the kernel classification (B1.1-B1.3).
  - The three sextic trees and their field Q(∛2) (B2.1-B2.5), recomputed.
  - The cellwise holomorphic groups (B3.1-B3.4).
  - The Kummer images (B4.1-B4.4).
- **Where the run is brisk:**
  - A1.7's converse, the equivalence of categories, is asserted in two sentences;
  - the associativity of (A1.14) in A1.8 is accepted from the run's cancellation argument;
  - the cited theorems (Bühler; Schinzel 1977, Thm 2; Perucca-Sgobba; Wendl) were not opened.

## 2. Refuted or corrected

- **By this intake:** nothing. No statement of the run is refuted.
- **The run's own refutations, all confirmed:**
  - L1 (A1.3);
  - the printed equivalence (A1.6) and automatic enrichment (A1.8);
  - L3 for the nonnegative source category (A2.1);
  - Sex1-2 sufficiency (A2.5);
  - the cohomology-only reading of L2 (A3.4) and binomial operations as polynomial laws (A3.5);
  - Prop. 1(e) both ways (A4.4);
  - pinned rigidity (B1.2);
  - the δ-collision reading (B2.5).
- **Corrections to our own study and prompt**, all confirmed:
  - L1 conflated polynomial laws with Γ^d P;
  - L3 assumed the bounded complexes in all degrees;
  - "cubic P" is the raw quintic δ·p;
  - R6's prime inversion is sufficient, not necessary (A1.9).

## 3. What is new

- **Against the literature.** The cote-137 statements are answered with classical tools (Roby, Dold-Puppe,
  Friedlander-Suslin, Happel, Horel, Mandell). New are the precise answers to Grothendieck's questions:
  - the exact failure and the repair of his "⊗-pd-catégories" axioms (A1.5-A1.8);
  - the all-ring essential image of the Σ-exact theorem (A2.2-A2.5);
  - the reading of the "structure supplémentaire" of 137:38 as the full natural Γ-action, with reconstruction (A3.2).
- **Part B.** The sextic cubic is in Schneps (1994), as the run says. The complete list of cellwise holomorphic groups
  of clean dessins (B3.1: Aff⁺(R), R_{>0} for every orange, C_2 for the genus-g bouquets) has no source that the run
  found. I did no literature search of my own.
- **Against our results.** The run agrees with RESEARCH_SA08:
  - A3.3 and A-018/D006M recover the same homotopy type of nilpotent spaces of finite type;
  - A3.5 is the elementary relative of A-026.

## 4. Errata

None in the run's mathematics. The run's own errata of our study are listed in section 2.

## 5. Hexagon readiness (field_experts/HEXAGON_CANDIDATES.md, the five tests)

**No finding of this run is ready.** The closest is B3.1-B3.3, the complete list of cellwise holomorphic automorphism
groups of clean Belyi maps, with explicit models.
- **Complete:** yes.
- **Self-contained:** yes; it rests on B1.3, standard uniformization and the finiteness of automorphisms of pointed
  curves.
- **Stable:** yes; nothing of ours runs on it.
- **Checked:** this intake's targeted checks, plus the run's finite certificate for genera 1-8.
- **Of interest now:** weak. It also needs a literature search for the cellwise list before posting, since the run
  found none and I did none.

The Kummer and Fermat-fibre indices (B4.1-B4.3) are classical, and the cote-137 answers are corrections to the archive,
not results of general interest.
