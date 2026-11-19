# Sweep 1, scope `derivateurs`: corrections and refinements

Claude Opus 5.5 at effort max, sweep 1, 18 Nov 2026. Scope: the 15 runs of the Dérivateurs line in `REGISTER.tsv`
plus TOTEX and PRETOT (1,586 rows). All the returns are by GPT-6 Astra (ChatGPT Pro mode), unrefereed. "Sure" says
how sure I am; "read" says what I read. Row tags are the register's draft tags RUN:ID.

## A. Mathematics and status

**C1. TOTAL_ASPHERICITY:C.9, C.10 — status of the exactness of Δ_inj.**
- What: the register has C.9 Proved and C.10 Refuted (the refutation of II ms. 36ter). The exactness half of C.10
  (filtered integral affinization, exact abelian colimits) is Isbell–Mitchell, Bull. AMS 79 (1973) 994–996, Th. 3;
  TOTEX:A.3 already marks the same statement Known.
- Fix: the handbook item "Δ_inj is exact and not filtered" is Known (Isbell–Mitchell 1973, Th. 3), with the return's
  proof as an independent proof; the refuted item is his claim at II ms. 36ter (total ⇒ filtered), refined item C.10.
- Sure: high. Read: the Dérivateurs expert's knowledge handoff (`pro_reviews_max_20261112/DERIVATEURS_EXPERT/
  KNOWLEDGE_HANDOFF.md`, "Settled so far"; review by Claude Fable 5.2 at effort max, 12 Nov), the TOTEX:A.3 row.

**C2. XVI ms. 118, footnote 56: the two intakes disagree; the later one is right.**
- What: `pro_prompts_max_20261112_work/INTAKE_S2COUNT_REVLOC_20261117.md` (Claude Fable 5.2 at effort high), §3 and
  §4.1, says that REVLOC F.1 "decides Grothendieck's doubt at XVI ms. 118, footnote 56 … in his favour". The footnote
  is attached to Corollaire 7.7.2, `Loc (6' a, 8, 9) ⇒ Loc (1 ter, 3 bis)`, and reads "Loc (3 bis) pas prouvé,
  probablement faux". REVLOC:F.1 concerns the axioms without Loc (6' a); REVLOC:F.1.1, DER_FOLLOWUP:G.9 and
  DER_LOCALIZERS:A5.4 prove Loc (3 bis) from Loc (6' a) and Loc (8), without Loc (9). So the corollary holds and the
  footnote's guess is wrong. The later intake (`INTAKE_DER_FOLLOWUP_FINMON_20261117.md`, §10; Claude Fable 5.2 at
  effort max) already lists this record for change; it has not been changed.
- Fix: correct §3 and §4.1 of the S2COUNT/REVLOC intake note (or add a dated note there); in the handbook, footnote
  56 is a his-claim item (or an editors' note: who wrote the footnote is to be checked in the edition) with status
  refuted, refined item REVLOC:F.1.1. The companion's block at XVI ms. 118 should say the same.
- Sure: high. Read: `packages/DER_XVI/DER_XVI_text.tex` lines 2224–2226; REVLOC `sections/F12.tex` (F.1 in full); the
  rows REVLOC:F.1.1, DER_FOLLOWUP:G.9, DER_LOCALIZERS:A5.3, A5.4. Check events in `CHECK_EVENTS.tsv`.

**C3. Twenty-one open rows are answered by later runs; their status lines must follow.**
- What and fix (open row → answering row; details and reasons in `MERGES.tsv`):
  - total ⇒ exact (TOTAL_ASPHERICITY:D.7, TOTEX:A.7, D.16, D.20, B.7, RESIDUE:F.5) → refuted by TOTEX2:A.3 (C_δ);
  - TOTEX:C.6 (survival of the K* class) → proved, TOTEX2:C.37;
  - PATHS:A.8, RESIDUE:F.7 (universal Cat-colimit shapes) → componentwise filtered, PRETOT:F.1, F.4;
  - TOTAL_ASPHERICITY:F.27, RESIDUE:F.6 (hunch H3 and the dwyérienne-sieve questions) → refuted, PRETOT:A.5, B.2;
  - PRETOT:C.4 → refuted, DER_FOLLOWUP:A.9; PRETOT:E.9 → settled, DER_FOLLOWUP:C.1–C.4; PRETOT:F.10 → refuted,
    DER_FOLLOWUP:D.7 (the residual C_δ case is open: FREX G.1/G.2);
  - PRETOT:F.16, CATHOT:E.26 → proved, PATHS:C.P1–C.P3; CATHOT:E.6 → Hot-class version proved (INDLOCAL:D.1),
    Cat_hot-class version refuted (INDLOCAL:D.19); CATHOT:D.6 → refuted, S2COUNT:B:main;
  - POLES:A.16 → refuted (BISITE:A.32, RESIDUE:B.3, REVLOC:F.1, DER_FOLLOWUP:G.1–G.2); POLES:F.14 (1) → refuted,
    DER_LOCALIZERS:A.7 (and the expert's `RESULT_REVERSIBLE_NOT_STABLE.md`);
  - GALOIS:B.13 → decided relative to set theory: yes under Vopěnka's principle (REVLOC:H.2), no if there are no
    measurable cardinals (REVLOC:H.3); not decided in ZFC alone. GALOIS:B.14 → settled for K(n) and KU (REVLOC:E.7,
    E.9: not proper), open for general E.
- Sure: high for the statements (each answering row says what it answers, or its statement matches the open row
  exactly); the answering proofs were not followed except REVLOC:F.1. RESIDUE:C.8 is **not** answered: RESIDUE:C.3
  gives five objects as an upper bound; minimality is open.

**C4. TOTEX:F.2 — last clause out of date.** Its "the two intermediate inclusion questions remain separately
undecided" is superseded by TOTEX2:D.1 (filtered ⊊ exact ⊊ total ⊊ quasi-filtered; witnesses Δ_inj, C_δ, repaired
K*). Fix: status line of the clause. Sure: high.

**C5. FREX corrects three findings of the Dérivateurs expert (its own prompt's Leads).** Credit the expert (Claude
Fable 5.2 at effort max, 13 Nov, `KNOWLEDGE_HANDOFF.md`, "Referee reading of TOTAL_EXACT_2 and the prompt
FRAISSE_EXACT") where confirmed; correct the records where not.
- Lead 7 / finding 6, `E_U ≃ B(U/G_F)`: needs F nonempty; for F = ∅ the conclusion is `BE_G ≃ BA` (FREX:B.8).
- "(Rig) and (St) imply (Op)": needs the intersection condition (Int) (FREX:B.14, refuted as stated).
- N2 of `NEXT_PROMPT_ITEMS.md`, "exact iff amenable": false in both directions. Exact over every ring and not
  amenable: finite posets with an independent order (FREX:A.11). Total, amenable and Q-exact but not exact over F_2
  or Z: ordered punctured F_2-vector spaces (FREX:A.19, A.33). The expert had refuted one direction (Lead 6, A.7–A.8).
- FE-1 (exactness in every odd characteristic) is false (FREX report, "Corrections recorded").
- Confirmed: findings 1–2 (EHN Theorem 3.8 applies to C_δ: the shadow graph is 2-sparse and the stabilizer orbits are
  infinite; EHN Remark 3.2 is false as written): FREX:D.7.
- Sure: high (statements read; proofs not followed). Read: FREX cp10 `FREX_report.md` (first 18 kB),
  `PROGRESS_LEDGER.md`, rows B.8, B.14, A.11, A.19, A.33, D.7.

**C6. Literature: Oberst 1968.** FREX reports Oberst II.4.1 assumes F2-prime and that the unrestricted conjecture and
the monoid reduction of II.4.4 are false (checked from the Göttingen digitization). TOTEX:F.5 (bodies of Oberst,
Isbell–Mitchell 1976, Gabriel–Ulmer not obtained) is thereby partly answered. Fix: Part 0 citations of Oberst carry
this. Sure: medium (FREX's report, not read in the source).

## B. The register (sweep 0 script) and the item model

**C7. Cross-run citations parsed as same-run edges (23), and 71 cross-run citations missing from EDGES.tsv.**
- What: `build_register.py` reads "PRETOT F.1", "TOTASPH C.6", "GALOIS C.7 and C.13", "PATHS A.2" in `depends_on` as
  ids of the citing run. Examples: TOTEX:A.2 gets an edge to its own open C.6 (it cites TOTASPH C.6); DER_LOCALIZERS:
  D.6 to its own C.7, C.13 (it cites GALOIS); DER_FOLLOWUP:B.1, C.4, D.5, D.7, F.3, G.1. Some FLAGS rows are partly
  artifacts of this (TOTEX:A.6 → TOTEX:A.5, F.3).
- Fix: when a `depends_on` clause names a run (aliases TOTASPH, PRESHEAF_TOTALITY, TOTAL_EXACT, TOTAL_EXACT_2,
  REVERSIBLE_LOCALIZERS, FRAISSE_EXACT and the run names), attribute its ids to that run. The 71 edges, with the 23
  wrong ones marked, are in `XREF_EDGES.tsv` (ranges such as C.19–C.28 are given by their endpoints only).
- Sure: high (script, then the 23 read).

**C8. 211 Refuted rows: most state the counterexample, not the refuted claim.** By a heuristic over the statements:
165 are phrased as the counterexample (a true statement), 17 as the corrected statement, 29 as the refuted claim
(note column of `PLACEMENT.tsv`). Every one of the 64 "proved row cites a refuted row" flags of this scope is a sound
use of such a true statement (`FLAG_VERDICTS.tsv`). Fix for the handbook's item model: split each such row into the
refuted item (his claim, or a lead, with status refuted) and the proved counterexample or corrected item that refines
it; then the flag fires only on real uses of a refuted claim. Sure: high on the pattern; the heuristic misfiles a few
rows.

**C9. Open questions missing from the register.** FREX (cp10) and DER_FOLLOWUP (cp03) have no Open rows, yet their
reports keep main questions open: FREX A.3 (iii), C.4, G.1, G.2 (INCOMPLETE in its ledger); DER_FOLLOWUP's free-monoid
question over C_δ (reductions D.8–D.10). TOTEX2 likewise records no open row. Fix: sweep 0 should also read the
runs' ledgers and reports for INCOMPLETE/open task rows and make each an open item with its strongest proved reduction.
Sure: high.

**C10. Rows that are not statements, and duplicates.**
- S2COUNT TASK.* (16 rows) are task-status rows; TASK.B3's "Refuted" is the universal countability claim. They become
  no items; `MERGES.tsv` maps each to the statement row it reports.
- Same-run duplicates: INDLOCAL:D.U1 = D.19, D.U2 = D.18 (earlier checkpoint ids kept); TOTAL_ASPHERICITY:A.15 is the
  first clause of E.1; CATHOT:F.1 repeats G.1 (McCord).
- REVLOC holds titles only for its 152 rows; the statements must be filled from `sections/*.tex` before sweep 2.
- Sure: high.

## C. Names and notation (one name per object in the handbook)

**C11. W† and W̃ each name two different classes.** REVLOC:F.1 calls its four-test class W† (`\Wt = W^{\dagger}` in
`sections/F12.tex`); DER_FOLLOWUP:G.1–G.8 and the FINMON/DER_FOLLOWUP intake call the same class W̃. RESIDUE:B.1 uses
W† for a different, component-dependent class; POLES:D.4 uses W̃ for the stability intersection of all modern
fundamental localizers. Fix: one fresh name for the four-test class (e.g. W_4t); keep W̃ for POLES:D.4 or rename it.
Sure: high (definitions read in REVLOC; the others at statement level).

**C12. T_n means two things.** TOTEX:D.10's T_n is the class of shapes whose homotopy colimits preserve n-truncated
spaces (T_1 = T_2 = …); DER_FOLLOWUP:A.9's T_n is total W_n-asphericity (T_1 ⊋ Q_2 ⊋ T_2 ⊋ …). POLES:H.2 writes
T_W(A) for total W-asphericity. Not a contradiction; fix the notation (e.g. P_n for TOTEX's class). Sure: high.

**C13. "Total" without a localizer.** Most rows say "total" for total W_∞-asphericity, but FREX:A.21 has a category
exact over Q and "not total": consistent only because exactness over Q gives total W_Q-asphericity (TOTAL_ASPHERICITY:
D.5), not total W_∞-asphericity. Fix: the handbook writes the localizer every time. Sure: high.

## D. Placement remarks

**C14. Moduli rows belong to Part I.** STRATA F (17 rows), BISITE F.15–F.17 and RESIDUE H.3–H.6 compute exit-path
and entrance categories of the strata of M̄_{g,n}, the forgetful and clutching functors, and the Teichmüller groupoid
with its Lego presentation (STRATA:F.17). They are placed in Part I.2 (the tower and its Lego) with cross-references
from II.3.5 and IV.1. The strongest forgetful statement is RESIDUE:H.5 (every stable (g,n): W_∞-proper); STRATA:F.11
(always W_∞-smooth) is refuted, consistently with BISITE:F.16. Sure: medium (a placement choice).

**C15. Stratified rows go to Part IV.1**, the derivator recollement rows (STRATA D.1–D.2) to II.3.1, the local-system
rows (STRATA E, RESIDUE A, PATHS E.6, E.11) to II.2.8. Sure: medium (a placement choice).
