<!-- Saved by the main session (Claude Opus 5.5 Max) from the agent's final message, 18 Nov 2026: the harness refused the sub-agent's own write of this file. Agent a28ea31fa17dd65e1, Claude Opus 5.5 at effort max. -->

**SUMMARY.md** (by Claude Opus 5.5 at effort max, sweep 1, scope `sections`; the returns are by GPT-6 Astra in ChatGPT Pro mode)

**1. Counts**
- **Rows:** 2,087 register rows from 11 runs, plus 18 rows of the SECTION_GHOSTS final: 1,802 Proved, 131 Refuted, 101 Known, 64 Open, 7 Unresolved. About 20 of the Proved rows should be Conditional.
- **Placement:** I.1 has 88 rows, I.3 has 22, I.4 has 1,417 and I.5 has 578, over 20 sections. No row is left unplaced.
- **Merges (343):** 302 same, 26 refines, 11 stronger, 3 corrects, 1 refuted by.
  - 121 come from ANABELIAN_A1 ids carried into its successor (109 unchanged, 12 rewritten).
  - 168 come from the `checks` column of the SECTION_GHOSTS final.
  - 20 come from FERMAT_SUCCESSOR's audit of R1–R20.
  - 32 main-line merges were read by hand.
- **Flag verdicts (338):**
  - 79 "proved row cites a refuted row": all sound.
  - 243 dangling-dependency tokens:
    - 99 are literature locators;
    - 78 are sub-labels inside a proof;
    - 66 are another run's id.
  - 16 flags I added ("proved row uses an Open row"): none is a real dependency.
- **My checks:** 31 events in CHECK_EVENTS.tsv: 2 computations (`tools/y1_7_check.py`, `tools/tate_constant_check.py`), 14 targeted checks, 15 hypothesis checks of Tool (1) rows.

**2. Corrections that matter most** (details in CORRECTIONS.md)
1. **Conditional rows registered as Proved.** These rest on Tool (1) or on another stipulated input:
   - LM6 B.7, B.15, B.19, B.29, B.30, B.32, B.33, B.35, B.38–B.41 and F.31;
   - LM6 E.12, last two sentences;
   - FERMAT_SUCCESSOR A.20 and A.31;
   - LM6 B.18 and B.23 (another stipulated input);
   - FERMAT_SUCCESSOR C.13 (rests on LM7_PUSH D.20, D.21, D.51, D.52).

   The runs themselves say so; the register's status normalization dropped it.
2. **LM6 E.8 and Steklov's preprint.**
   - The Legendre Tate parameter is λ²/256 times a principal unit, so the cusp class carries a −8κ(2) term and is not divisible by ℓ at 2.
   - The statement of E.8 survives with FERMAT_SUCCESSOR's repaired proof (A.3–A.6).
   - Y₁(7)(Q) is not empty: (0,0) has order 7 on y² − xy − 4y = x³ − 4x².
   - Both errors are outreach items to Steklov; drafts go to the user first.
3. **The Fermat Selmer theorem.**
   - FERMAT_SUCCESSOR A.11 proves it for odd n ≥ 3 and A.16 for the classical curve and every n ≥ 3.
   - It overlaps Steklov's Theorem A for prime exponents ≥ 7. What is ours: the repaired proof, ℓ = 5, powers of 3 and 5, and the even classical curves. His Theorem A and Kriz–Li need checking before any novelty claim.
   - LM6 E.12 should be split into three items: Selmer ⇒ cuspidal (proved), no sections for even n (proved, strengthened by SECTION_GHOSTS E.100), every section is Selmer (conditional on Tool (1)).
4. **Δ on GT̂ may be settled.**
   - SECTION_GHOSTS E.191 proves Δ|GT̂ = 0 for the character of GT_TOWER_CHECK A.7.
   - E.198 proves GT̂ ⊊ ker Δ ⊊ GT̂₀ with an explicit witness.
   - If this is the same CM parity as LM7_PUSH E.3/E.65, then E.3 and FERMAT_SUCCESSOR C.15 are settled, as EXIT_TOWER E.49 claimed. E.201 suggests it is, but I only read statements.
5. **A1 is settled.**
   - ANABELIAN_149_PUSH A.30 and A.C2.6, and FLAGGED_149 B9, are superseded by ANABELIAN_A1(_SUCCESSOR) A.1 = ANABELIAN_SUCCESSOR A.3.
   - The finite certificates the experts asked for are now in the successor (A.50, B.85, B.88), and so is the non-nilpotent test (A.51).
   - Still owed: a reading of A.CF1–A.CF2 by a model outside both families.
6. **Mixed rows.** LM6 F.24, D.8, C.12, A.22 and FLAGGED_149 D7 hold proved parts that proved rows use. D7's DVR half is true and was re-proved by ANABELIAN_A1_SUCCESSOR B.102. Each should be split.
7. **The register itself.**
   - It is one return behind for SECTION_GHOSTS.
   - Escaped underscores in TeX (`\_`) make it miss cross-run lineage.
   - When runs cite each other's ids, it creates false within-run edges.

**3. Per chapter: proved, open, strongest reduction**
- **I.4.2 (finite fields):**
  - Proved: A1 (A1_SUCC A.1), and its extension to finitely generated fields of characteristic p (A1 A.33). SECTION_GHOSTS E.218 separates point sections from cusp sections over every F_q.
  - Open, each with its strongest reduction:
    - A12 (A.28): there is a Frobenius-order criterion, but the return action that would make orders unbounded is not determined (A.53–A.61).
    - B1 (B.5): genus-two families are done (B.141, B.145), and no bound depending only on p and g can exist (B.89).
    - B2 (B.12): excluded on two loci (B.130).
    - B4 (B.24): no uniform finite list of degrees (B.87).
    - B5 (B.67): partial results in B.82–B.86.
    - B6 (B.32): partial results in B.80, B.81, B.145.
- **I.4.5 (Conjecture A for the tripod over Q):**
  - Open. The same question appears as SECTIONS_OVER_Q A.1, ANABELIAN_149_PUSH D.U1, LM6 B.27 and SECTION_GHOSTS D.3.
  - Strongest reduction: (FS)_nil implies Conjecture A and birational lifting for locally ordinary sections (SECTION_GHOSTS A.5, D.2); A.4 (Stix) covers the rational-abelian-pair case.
  - On (FS)_nil itself, at regular odd ℓ:
    - the fixed-S H² obstruction vanishes in every weight (E.209);
    - the H¹ correction modules are exact (E.210);
    - a failed matching step is witnessed at no more than two places (E.212).

    ℓ = 2 and irregular ℓ remain.
  - Legendre route (A.24): open, but explicit parameters are recognized (A.41, A.54, A.64, A.79, A.87, A.70).
- **I.4.6 (nilpotent quotients and section ghosts):**
  - Open: A.2, A.7, B.1–B.3, C.7, E.120 and E.1.
  - New in the final: E.214 and E.215. Varying ghost families are not compact (A.101).
- **I.4.7 (birational lifting):**
  - Open. The same question appears as SECTIONS_OVER_Q B.15, ANABELIAN_149_PUSH D.U4, LM6 F.15 and FLAGGED_149 ZD10.
  - Reduction: D.2. N3 (B.97–B.105, B.124–B.125) settles the inertia question.
- **I.4.8 (reconstruction, B8):**
  - Open: B.52 = ANABELIAN_SUCCESSOR F.18 = ANABELIAN_149_PUSH F.9.
  - Positive classes: Q^solv (F.31), B.139–B.143, B.146–B.147.
  - Negative classes: B.144, B.49–B.54. Slimness is necessary.
- **I.4.10 (normalizers):**
  - Open: N2 (LM6 A.22 = A1_SUCC B.118). A surviving candidate must lie in a strictly smaller residual intersection (B.111–B.117).
  - Also open: LM6 A.12, FLAGGED_149 ZCF6.
- **I.4.4 (number fields):** finiteness of Sec is open (LM6 D.8).
- **I.4.9:** holds N4 (one of his claims), which is false (B.90–B.96).
- **I.4.3, I.4.11:** no open rows.
- **I.5.3 (Fermat Selmer sections):**
  - Proved: A.11 and A.16; E.100 for even n. "Every section is Selmer" is conditional (A.20). Complete twist tables (A.37–A.43).
  - Open:
    - A.30: level ≤ 16 plus cofinal descent is proved to suffice (A.46–A.58).
    - A.45: only integers survive the level-3 test (A.59–A.71).
- **I.5.4 (nilpotent quotients of Fermat curves):**
  - Open: FERMAT_SUCCESSOR B.13, B.14, LM6 E.21, LM7_FERMAT_TOWER E.23.
  - Reductions: B.27, B.42, B.6.
- **I.5.5 (GT̂ and the Fermat tower):**
  - Open: FERMAT_SUCCESSOR C.7, C.9, C.12, C.20, C.22.
  - Reductions: C.18; C.19 shows the multiplier-one group is torsion-free.
- **I.5.2:** LM7_FERMAT_TOWER D.13 and D.19 are open.
- **I.1.5:** Δ on GT̂ is open in its runs but possibly settled by SECTION_GHOSTS E.191/E.198 (see 2.4). GT_TOWER_CHECK A.4.57 is pending.
- **I.1.4:** LM6 C.12 (involutions for g ≥ 3; smallest open type (3,0)) is open.
- **I.3.2:** FLAGGED_149 Z142g is open.

**4. Returns no intake had read, and what is in them**
- **SECTION_GHOSTS:**
  - The ledger lists cp07, but the final has since arrived (13:05 UTC, 228 rows). The run stopped under the two-review rule.
  - It contains the reductions above, the Δ results, and an audit of 90 earlier claims: 87 confirmed, 2 repaired, 1 pending.
- **ANABELIAN_A1_SUCCESSOR cp05:**
  - 210 rows. It keeps all 121 of ANABELIAN_A1's rows (no status changes) and adds 89.
  - It gives a direct characteristic-p proof of A1, the certificates, N1, N3, N4 shown false, and the B8 and B1 families.
  - The chat transcript holds results from after cp05 that are in no checkpoint (the run ended on "Message delivery timed out"):
    - an F₅ witness: a degree-31 cover over F₁₂₅ with relative class number 128³⁰;
    - a stronger cover with 5-rank-zero primitive part, still being checked;
    - a reconstruction result over discretely valued fields;
    - drafts B.148–B.151.
- **FERMAT_SUCCESSOR cp06:**
  - 144 rows: the repaired Selmer theorem, the twist tables, the quintic prosolvable result, the class-2/3 laws, the CM and GT computations, and the dictionary for cote 145 checked against the scans.
  - Its audit of R1–R20 is effectively the corrections ledger for LM6 and LM7.
- **Thinly read before, now placed:** LM7_FERMAT_TOWER (0 of 229 rows named by any intake), SECTIONS_OVER_Q (18/245), ANABELIAN_SUCCESSOR (1/157), ANABELIAN_A1 (7/121).

Files are in `C:\Users\user\Documents\results_register\sweep1_sections\`:
- PLACEMENT.tsv
- MERGES.tsv
- FLAG_VERDICTS.tsv
- CORRECTIONS.md
- CHECK_EVENTS.tsv
- tools\
