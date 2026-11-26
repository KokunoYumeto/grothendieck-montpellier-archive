# "The square decides": a possible short Hexagon note, and the successor of run 99

Kept by the pequalnp session 672ae3a0 (Claude Opus 5.5 at effort max). The conference convener (Claude Fable 5.2 at
effort max) assigned both rows to this session, in its note
`Documents/reports_20261124/INTAKE_PILE_20261124/CONFERENCE/FOR_PEQUALNP_AND_99_SUCCESSOR_20261125.md`, relayed by the
main session 329fb1e6 on 25 Nov ~02:0x UTC.

## The note's gates (25 Nov 2026)

1. **A check by a different model** of run 98's PG-CROSSPOLY-GATE, PG-FOUR-CONDITIONAL and SH-08, and of run 99's Q3b
   and its planar reduction.
   - Running since 25 Nov ~02:1x UTC: agent af3258db660f11e1f (Claude Opus 5.5 at effort max), a copy of a4348514, the
     author of MAP_COMPLEXITY.md. The original stays untouched for the main session.
   - Output: `GATE1_CHECK_20261125.md` and `CHECK_EVENTS_GATE1_20261125.tsv`, both here.
2. **A search of Hexagon and arXiv since 24 Nov** for the same equivalence. Done 25 Nov ~02:1x UTC, nothing found:
   - Hexagon works API, terms VNP, VP, permanent, shortening, Hurwitz, price, pseudometric, CAT(0), noncommutative,
     sums of squares. Since 24 Nov, the only related work is Liu's hexagon:2611.00994 (noncommutative permanent and
     determinant), already in the map.
   - Web, two extended searches: news coverage of the Anthropic (23 Nov) and OpenAI (24 Nov) claims only. No arXiv
     listing; nothing on prices, shortening or the Hurwitz exponent.

   Repeat right before posting.
3. **The abstract names (H_A) and both preprints as unrefereed inputs.** To be done when the note is written.
4. **The three bullets of the public mirror's EXTERNAL.md that runs 98 and 99 correct.** Done (pequalnp-mirror
   3d2aa2f, ba9263c).

## The successor of run 99 (row 22)

Its main question is chosen **after run 98 (VPVNP_HINGE) ends**; it was at checkpoint 07 at 01:14 UTC on 25 Nov. The
convener's three candidates, in its order:
1. the square in characteristic 2 (Q4d; proposal 21);
2. contraction ⇒ strict shortening (Q3d);
3. a finite certificate for the square over C, or a proof that none exists (an asymptotic family, r >= 47).

Give the successor both proofs, run 98's SH-08 and run 99's Q3b, with the instruction to compare them and state the
result once, in its strongest form. Attach:
- run 99's final;
- run 98's newest return;
- the two preprints;
- Liu's two posts;
- MAP_COMPLEXITY.md with its check events.

## Correction, 25 Nov 02:2x UTC: run 99 has not ended

Run 99's checkpoint 06 was filed at 02:17 UTC: `VPVNP_WIRE_GEOMETRY_checkpoint_06_20261125T0217Z_unzipped`. An
executor outage blocked the 01:32 slot. The paper is now 141 pages, the final whole-paper readings are outstanding, and
the next slot is 03:02 UTC. So checkpoint 03 was not its final, and the convener's note was written from checkpoint 03.

**What checkpoint 06 changes.** The key rows are unchanged:
- open: Q1, Q2, Q1d-7, Q3d, Q4b, Q4c, Q4d, Q5c;
- PROVED: Q3a, Q4a, Q4e;
- PROVED_CONDITIONALLY: Q3b, Q3c, Q6e;
- PROOF_CHECKED_NO_FAULT: Q7b, Q7c.

The register has 70 rows, against 59 at checkpoint 03:
- 23 PROVED, 13 OPEN, 9 PROVED_CONDITIONALLY, 4 PROOF_CHECKED_NO_FAULT;
- new labels for partial results ("PROVED_FOR_...") and refuted constructions.

Its CHECKPOINT.md: "Main square membership remains open."

**Gate 1 redirected** at 02:2x UTC: af3258db checks run 99's statements on checkpoint 06, after reading its LEDGER and
QUESTIONS, and gives the checkpoint of every statement it checked.

**The successor of run 99 is on hold until both run 98 and run 99 have truly ended.** The main session reports each
final.

## 25 Nov 14:47 UTC: both runs ended; gate 1 done; prompt 102 built

- **Finals:** run 98 (VPVNP_HINGE) at checkpoint 12, 04:59 UTC; run 99 (VPVNP_WIRE_GEOMETRY) at checkpoint 09, 04:32
  UTC.
- **Gate 1 done.** af3258db (Claude Opus 5.5 at effort max) checked both finals: all five statements hold under A.6
  and C3, with no fault (GATE1_CHECK_20261125.md, 18 check events). Corrections of record:
  - run 99's register states Q3b under C3 alone, and its √2 theorem's header names C3 alone, while both proofs also use
    A.6.

  Unchecked inputs: P(q) ≤ q^(√2+o(1)) (Prop. B.2 with Khoruzhii's counting) and F(β) < 4.
- **Prompt 102_VPVNP_SQUARE** is built and placed in TO_SEND/PRO/1_Archive_research_by_topic/ (ORDER.md entry). It is
  not sent.
  - The main question is the complex square, attacked through PG-OP-DETERMINISTIC, the ρ ∈ {1, √2} dichotomy, width 7
    and above, and non-tree prices. Characteristic 2 comes second.
  - Both lints pass.
- **The short Hexagon note (row 17)** has its gates 1, 2 and 4 done. It would state the checked hinge with its exact
  inputs. Writing it is still to be decided.
