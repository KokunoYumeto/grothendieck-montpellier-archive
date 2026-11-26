# Topicality of the intake pile: group NT_HODGE (clusters ALPOGE, ZETA_GRH, HODGE)

Written 24–25 Nov 2026 by Claude Opus 5.5 at effort high, launched by the main session 329fb1e6 (Claude Opus 5.5 at
effort max), following `TOPICALITY_BRIEF.md`. The runs themselves are GPT-6 Astra (ChatGPT Pro mode); the cluster files
give their checkers. Rows: `TOPICALITY_NT_HODGE.tsv` (48 rows). Running notes:
`agent_notes/20261124T2136Z_Topicality_number_theory_and_Hodge_NOTES.md`.

**How the searches were made.**
- **Hexagon:** the whole corpus, 1,530 works from 1 Sep to 24 Nov 2026, pulled through `/api/v1/works`. Titles,
  abstracts and tags were grepped per item (patterns are in the notes). Every work I rely on was opened as a PDF at its
  statement.
- **arXiv:** the API, then arxiv.org/search once the API rate-limited me. Queries are listed per row in the TSV.
- **The laboratories:** `openai/math`, through history.md and the list of 752 preprints, with the TeX of the relevant ones
  opened. `anthropics/formal-math` has released nothing in this window except `vp-vnp` (LITERATURE §C).
- **Classical sources** named as gates: Calegari 2013, Kharel–La Rosa–Wiese, Rojas 2003 and Michler 1992 were opened.
  Dwyer 2014 could not be opened (Wiley and ResearchGate returned 403); only its abstract was seen, in a search snippet.
- **Not opened:** Qiyue Tang's hexagon 2611.00135 (*Deterministic polynomial-time factorization over finite fields*),
  because the user asked that it not be read. Nothing below rests on it.

## What changed around this group (the evidence most verdicts rest on)

1. **Deterministic polynomial factorization over F_p is unconditional (OpenAI, 4 Oct 2026).**
   - Source: `openai/math`, `preprints/Deterministic-Polynomial-Factorization-over-Prime-Fields-October-4-2026`:
     `build/main.tex` abstract, l.50–58; `sections/00-introduction.tex`, theorem `thm:factorization`, l.27–38 ("no
     integer-factorization oracle, primitive-root oracle, or GRH assumption").
   - With Shoup's reduction and iterated root extraction, it settles in outcome:
     - Lenstra's problem of constructing F_{p^r};
     - r-th nonresidues, both in F_p and in a supplied F_{p^m};
     - primitive roots, given the factorization of p−1.
   - It predates CX_GRH and GRH_ALGORITHMS. CX_GRH.tex never cites it (a grep finds only the ETH preprint).
2. **Landau–Siegel zeros are excluded unconditionally (October).**
   - OpenAI, *Uniform exclusion of Landau–Siegel zeros*, 1 Oct.
   - Green, hexagon 2610.00311.
   - Guo, 2610.00461: (1−β) log q > 1/100, explicit.
   - Frei–Kai, 2610.00466: Hecke L-functions.
   - Liu, 2611.00080v2, Thm 1.1 (pdf l.116): every real zero of every ζ_K satisfies (1−β){log D_K + n log 2n + 6n + 1} ≥
     1/1370.
   - So every use of Alpöge's theorem (A) that only removes a Siegel zero no longer needs A.
3. **Zero-free half-planes beyond Dirichlet.**
   - Cureton–Thorner, 2610.00200v2, Thm 1.1 (pdf l.169), 12 Oct: ζ_K ≠ 0 for Re s > 31/32, for every number field K.
   - Boyang Hu, 2610.00216: 7/8 for unitary Weil L-functions.
   - Liu, 2611.00741, 20 Nov: θ_G = 0.873332637… for Hecke, Artin and Weil L-functions.
   - Bhattacharya, 2610.00178, 11 Oct: a 155-page record of what OpenAI's 7/8 theorem makes unconditional. It includes
     deterministic root extraction (§47), Miller's equivalences (§46), Rónyai splitting (§§48–49), and CM and André–Oort
     items (§§33–42).
4. **Abelian varieties over finite fields.** Milne, hexagon 2611.00244v1, Thm 3.1 and Thm 3.5 (pdf l.297–475): the full
   Tate conjecture and the Hodge standard conjecture now hold for all abelian varieties over finite fields. This combines
   Milne's reductions with OpenAI's CM Hodge proof (human proof: van Hoften–Sempliner, 2610.00259) and the rationality
   conjecture (Madapusi, 2610.00226).
5. **Weil classes.**
   - Severn, 2610.00387v2, 20 Oct, Theorem A (pdf l.84): Weil classes are algebraic on every Q(√−3) Weil eightfold with
     split discriminant. The proof (l.1326) uses G₃₄ and 17 boundary curves.
   - Severn, 2610.00386 and 2610.00477, and Hippeläinen, 2610.00371 and 2610.00662: further sixfold cases.
   - Bhattacharjee–Bhattacharya, 2610.00315v2, Thm 1.1–1.2, 1.5 (pdf l.138–330): Hodge-locus dichotomies.
   - OpenAI withdrew its split-eightfold paper on 7 Oct.

---

## Items worth a paper now (ranked)

1. **Galois orbits of CM points with exponent 1/(4g) (NIGHT_AFTER_ALPOGE A.ORBIT; note H15).** STILL NEW.
   - *What:* |Gal·x| ≥ c_g D_x^{1/(4g)} with explicit c_g, for every CM point of A_g and every centre order.
   - *Why it still matters:* it is the only explicit polynomial exponent of this quality we found. The nearest
     competitor is Jaswal's effective André–Oort (2611.00339v3, Prop. 3.3, pdf l.772), whose explicit orbit exponent
     μ = 1/(16·t·s·n_T(n_T−1)) is far smaller.
   - *Novelty evidence:* arXiv "Galois orbits" + CM, Hexagon grep "CM point|Galois orbit|André–Oort", Bhattacharya
     §§33–35 (Y(1)^n only). Nothing newer proves it.
   - *A caution for the paper:* A is no longer needed, because the Siegel-zero exclusions of October serve. The H15 draft
     already says so (`reports_20261123/h15_note/h15_note.tex` l.52–54, 156–157, 391). The note should present A as one
     of several inputs, not as the reason the result is new.
   - *Proof:* `NIGHT_AFTER_ALPOGE_checkpoint_13…/workbench/schemes-and-moduli-workbench/papers/cm-orbits/main.tex`,
     checked step by step by ad855737 (Claude Opus 5.5 at effort high). Hexagon: drafted, not posted.
2. **Artin's conjecture in Calegari's S₅ family when B and C have no common off-centre real zero (BEYOND_DIRICHLET
   BD-S25/S26).** STILL NEW.
   - *What:* the hypothesis is strictly weaker than Calegari's ζ_H(σ) ≠ 0 on (0,1), and central zeros of any order are
     allowed.
   - *Novelty evidence:*
     - Calegari's Thm 1.2 (arXiv 1112.1152) needs the full nonvanishing;
     - Kharel–La Rosa–Wiese (2206.08116, Thm 1.2 and l.213–217) remove only the condition at 5, as Dwyer had remarked;
     - Dwyer 2014 (BLMS 46(1) 51–58, doi 10.1112/blms/bdt075), from his abstract, gives examples, not a weaker
       hypothesis;
     - no 2026 work on S₅ Artin was found on arXiv or Hexagon.
   - *Effect of Liu's θ_G (2611.00741):* the open window α ∈ (½, θ_G] for Q02 shrinks slightly, since θ_G < B* =
     0.873345856.
   - *Proof:* `BEYOND_DIRICHLET_checkpoint_10…/workbench/papers/paper_II/main.tex` l.76–108, 334–405.
   - *Gates:*
     - The four explicit fields (8249, 60061, 30301, 48976) are **UNSETTLED** against Dwyer's table. The method itself
       is known: Calegari §5 did the field of discriminant 1609 through Booker. Present them as new only after Dwyer's
       list is opened; otherwise present them as further instances.
     - The paper must cite Calegari §5 and Dwyer for the method.
3. **The standard conjectures and Tate on all powers of explicit non-abelian fourfold axes in characteristic p (C44_POS
   A13, A28, A30, A30a; H26).** STILL NEW.
   - *Why it still matters, after Milne's report:* the report (2611.00244, Thm 3.1, 3.5) makes Tate and the Hodge
     standard conjecture theorems for **abelian** varieties over finite fields. That covers the ambient E⁶ but not the
     axes B, whose variable middle cohomology is not of abelian type. Unconditional cases beyond abelian varieties remain
     rare.
   - *Novelty evidence:* arXiv "Hodge standard conjecture" (only Ancona–Marmora, Ito–Ito–Koshikawa, Koshikawa); Hexagon
     grep "standard conjecture|Tate conjecture".
   - *Sun's claim:* Sun, arXiv 2611.28178, claims Tate over finite fields. It is unverified and would cover only the
     Tate part.
   - *Proof:* `C44_POS_final…/C44_POS.tex` 2627–2946, 27076–27466, 27722–28166, with a targeted check by a8d75352
     (Claude Opus 5.5 at effort high).
   - *Gates:* a second reading of the hypotheses of Chin's Th. 5.7 and of the ambient block; the paper should cite
     Milne's report for the abelian case.
4. **New candidate from this pass: Hilbert's Nullstellensatz in AM, unconditionally (replaces CX_GRH CX-K03).** STILL NEW
   as far as searched, but UNSETTLED until the deduction is checked.
   - *The deduction:*
     - CX-K01 is right that Koiran needs only zero information for ζ_E of the solution field.
     - Cureton–Thorner (Thm 1.1, pdf l.169) give a zero-free half-plane Re s > 31/32 for every ζ_K.
     - Rojas (arXiv math/0301111, Thm 1) proves HN ∈ AM under GIPIT, a short-interval prime ideal theorem with explicit
       dependence on the field.
     - A uniform zero-free half-plane with the unconditional zero count appears to give GIPIT. The interval exponent
       1−1/a, with a ≍ κ log(n log d), exceeds 31/32 for large κ.
   - *If it holds:* HN ∈ AM ⊆ Π₂, with no hypothesis. That is far more than CX-K03's abelian-witness version, and it is
     the kind of statement a complexity theorist would want.
   - *Searches:* arXiv "Koiran AND Nullstellensatz", "Nullstellensatz polynomial hierarchy"; Hexagon grep
     "Koiran|Arthur–Merlin|Nullstellensatz"; a web search. Nothing states it.
   - *Gates:* a careful write-up of the GIPIT deduction, including the uniformity in n_K and d_K; a search of ECCC.
     Cureton–Thorner is unrefereed but Lean-formalized (AxiomProver).
5. **The Hodge conjecture for abelian varieties as a uniform degree bound over finite fields, with explicit detectors
   (HODGE_FINISH Paper A: Q01 with Q02–Q04, Q10, Q12; H25).** PARTLY.
   - *Known:* the dichotomy part of Q01 ((i)⇔(ii)⇔(iii)) is in substance Bhattacharjee–Bhattacharya 2610.00315v2,
     Thm 1.1–1.2 (17 Oct), and Cattani–Deligne–Kaplan p. 483.
   - *New:* the finite-field degree form (iv) and the explicit detectors (48, 192, 36; quadratic extraction;
     stabilization; the Ext² test). Severn's and Hippeläinen's papers prove algebraicity in these families without degree
     bounds.
   - *Proof:* `HODGE_FINISH_final…/workbench/work/UNFILED-A/v1/paper/main.tex`.
   - *Gates:* restate the novelty against 2610.00315; the Schoen 2007 page; drop the André–Oort hypothesis of Q27;
     settle Q28's Severn status (below).

**Already posted; they survive but need no new paper:**
- the Anderson–Ihara question at Vandiver primes (C.IHARA, hexagon 2611.00939): STILL NEW, with v2 fix-ups;
- the sign-only Deligne bound (SG-08–SG-11, hexagon 2611.00789): STILL NEW. Dingxin Zhang's exposition (arXiv
  2611.30749) should be read before a v2;
- the finite simplicity test (ZETA_HEAT, hexagon 2611.00996): STILL NEW against Knausgård, Lamzouri, Suzuki and
  Andrews–Connes–La Gatta;
- the 67c paper (hexagon 2611.00987): its outcome is KNOWN BEFORE through PF26, and the paper says so. A v2 should state
  this in the abstract.

**Corrections still owed to their sources** (no source has been revised):
- Thakur, arXiv 2001.00210: v1 only;
- BIMS, arXiv 1702.00558: v1 only;
- Guo, thesis arXiv 1706.10028v2: the cited version is the latest.

---

## Every item with its verdict

Evidence and locators for each row are in the TSV; what follows gives the reason in one line.

### ALPOGE

| Item | Verdict | Reason | Paper now? | Hexagon |
|---|---|---|---|---|
| C.IHARA | STILL NEW | no newer work (arXiv Ihara/pro-p, Anderson–Ihara, Vandiver; Hexagon) | posted; v2 | 2611.00939 |
| A.ORBIT | STILL NEW | Jaswal's explicit exponent much weaker; A replaceable by October Siegel-zero exclusion | **yes** | H15 drafted |
| C.K12/K80 | **OVERTAKEN** | Mok–Zheng 2611.00998 (to degree 120), Pintar 2611.00829 (to 104) | no | H18: withdraw |
| BD-S25/S26 | STILL NEW | no work weakens Calegari's hypothesis to common zeros | **yes** | none |
| BD-S12/14/15/16 | UNSETTLED | method known (Calegari §5, Dwyer 2014); Dwyer's list unopened | inside BD paper | none |
| BD-S23 | KNOWN BEFORE | Kharel–La Rosa–Wiese Thm 1.2; Dwyer | no | none |
| BD-K01 / BD-R20 | STILL NEW | no K-group computation of this field found | no (not now) | none |
| BD-R83 | UNSETTLED | not compared with Borger §6 | no | none |
| CX-N01–N04 | **KNOWN BEFORE** | PF26 (4 Oct); Bhattacharya §§46–47; AKS | no | none |
| CX-N13 | **KNOWN BEFORE** | PF26 + Berlekamp's reduction | no | none |
| CX-N15 | **OVERTAKEN** | PF26: unconditional, stronger | no | none |
| CX-K01/K03 | PARTLY | Cureton–Thorner + Rojas/Koiran appear to give all of HN ∈ AM (unwritten) | new note, gated | none |
| MA-FQ-004 | PARTLY | superseded by BD-S26 | no | none |
| ALP-LIFT-54/55 | PARTLY | m ≍ x^{1/2} already in Jaswal 2611.00799, R. Zhang 2611.00809 | no | H30 |
| AM-LIFT-110/112/113 | STILL NEW | small; no source | no | H30b |
| AC-T51 | PARTLY | Connes's statement; ⇒ direction from A | no | H27 |
| BR-15 (Thakur) | STILL NEW | Thakur v1 unrevised | correction | A15c |
| BR-12302 | KNOWN BEFORE | Richardson 1987 | no | none |
| BR-AT-01 | KNOWN BEFORE | immediate from A | no | none |
| MOONSHINE.004/005/009 | KNOWN BEFORE | unary theta series; Saias–Weingartner; Nakamura–Pańkowski | no | none |

### ZETA_GRH

| Item | Verdict | Reason | Paper now? | Hexagon |
|---|---|---|---|---|
| GRH-P144/P145/P149 | **KNOWN BEFORE** (outcome) | PF26 + Shoup construct F_{p^r} unconditionally; routes new | posted | 2611.00987 |
| GRH-P125/P126, P128/P131, P074, P092 | **KNOWN BEFORE** (outcome) | same | no | in 2611.00987 |
| Q03 table | PARTLY | Bhattacharya 2610.00178 covers much under the 7/8 QRH | no | in 2611.00987 |
| CX-ALG-016/017 (BIMS) | STILL NEW | arXiv v1 only | correction | none |
| GRH-P163 (Guo) | STILL NEW | v2 is latest | correction | none |
| MT-S506 | PARTLY | Heilbronn characters (Foote–Murty, Foote–Wales, Michler 1992) | no | none |
| MT-M20/M23 | PARTLY | rests on HKMS 2107.03269 | no | none |
| ZETA_HEAT simplicity test | STILL NEW | proportions only elsewhere | posted | 2611.00996 |
| ZETA_HEAT cosine lower rate | STILL NEW | Andrews–Connes–La Gatta give the upper side only | no | none |
| NX01/NX02 | PARTLY | effective form from October Siegel-zero exclusion (Liu 2611.00080); only "173" needs A | no | via H15 |
| NC01–NC04 | PARTLY | as NX01; exponent superseded by A.ORBIT | no | via H15 |
| NX-L01/L06 | STILL NEW | no hit | no | none |
| NG01 | UNSETTLED | Commelin, André not searched | no | none |
| THETA3-C32 | STILL NEW | no computed Weil-cycle self-intersection found | no | none |
| SN-C04 | KNOWN BEFORE | Kleiman 1968, Th. 2.13 | no | none |
| SN-44-01 / AR-01 / T05 | PARTLY | new as a correction; the form is Shioda / Faltings–Hriljac (from memory, not opened) | no | H04 |
| HECKE_DIV R21–R23 | PARTLY | Bhattacharjee–Bhattacharya Thm 1.2; CDK | no | none |
| DEG_L B19–B21, S-05/S-06 | STILL NEW | no hit | no | none |

### HODGE

| Item | Verdict | Reason | Paper now? | Hexagon |
|---|---|---|---|---|
| SG-08–SG-11 | STILL NEW | ours; outside exposition by D. Zhang | posted | 2611.00789 |
| C44 A13/A28/A30/A30a | STILL NEW | abelian case now known (Milne report); axes are not abelian | **yes** | H26 candidate |
| INT-C44-2 | UNSETTLED | unwritten intake deduction | no | none |
| C44 A29/A31s/A31t | UNSETTLED | chain unread | no | none |
| Paper A Q01 | PARTLY | (i)–(iii) in 2610.00315 and CDK; (iv) new | **yes** (Paper A) | H25 candidate |
| Paper A Q02–Q04, Q10, Q12 | STILL NEW | no explicit detector degrees anywhere | in Paper A | H25 |
| Paper B Q29 | STILL NEW | 2610.00315 Thm 1.5 is a different link | in Paper B | H25c |
| Q27 | STILL NEW | André–Oort hypothesis removable | in Paper A | none |
| D-G34-01–07 | **KNOWN BEFORE** | Severn 2610.00387v2 Theorem A, same 17 curves | no | H19: drop |
| D-G34-04 (Schoen p.18) | UNSETTLED | compare Severn's treatment first | correction, later | none |

**Consequence for Paper A's Q28 and board H19.** The disagreement the HODGE cluster recorded (Paper A calls the
eightfold bound conditional on Severn; H19 calls D-G34 Severn-free) is moot. Both rest on Severn's Theorem A, which D-G34
only re-derives from his data. Q28 should say "conditional on Severn's Theorem A (unrefereed), independently re-derived
in HODGE_DIVISION D-G34", and H19 should be dropped as a separate posting.

---

## Overtaken or known before
- **OVERTAKEN:**
  - C.K12/K80, by Mok–Zheng 2611.00998 and Pintar 2611.00829;
  - CX-N15, by PF26.
- **KNOWN BEFORE:**
  - CX-N01–N04 and CX-N13 (PF26; Bhattacharya; AKS);
  - the outcome of the 67c/GRH_ALGORITHMS constructions (PF26 + Shoup);
  - BD-S23 (Kharel–La Rosa–Wiese; Dwyer);
  - D-G34 (Severn, Theorem A);
  - BR-12302 (Richardson);
  - BR-AT-01;
  - SN-C04 (Kleiman);
  - the moonshine L-function items.
- **PARTLY:**
  - NX01/NX02 and NC01–NC04: A replaceable by the October zero exclusions;
  - Q03;
  - MT-S506 and MT-M20/M23;
  - HECKE_DIV R21–R23 and Paper A Q01 (i)–(iii) (Bhattacharjee–Bhattacharya);
  - ALP-LIFT-54/55 (readers' guides);
  - AC-T51;
  - SN-44-01/AR-01/T05 (classical form);
  - CX-K01/K03 (superseded in scope by the Cureton–Thorner deduction);
  - MA-FQ-004.

## Unsettled, and what would decide each
- **BD-S12/14/15/16:** whether 8249, 60061, 30301 and 48976 are in Dwyer 2014's table (doi 10.1112/blms/bdt075; access
  needed).
- **The HN ∈ AM deduction:** a written check that a uniform zero-free half-plane gives Rojas's GIPIT, or Koiran's count,
  with the needed uniformity; plus a search of ECCC.
- **BD-R83:** Borger, *Λ-rings and the field with one element*, §6.
- **NG01:** Commelin's thesis §4.13–4.16 and André's books on motives.
- **INT-C44-2 and C44 A29–A31t:** a written proof, and a reading of the chain A22–A31r.
- **D-G34-04's Schoen correction:** Severn 2610.00387v2's treatment of Schoen's exceptional divisor.
- **SN-44-01's classical form:** open Shioda 1990 and Hriljac 1985 at the height formula, to cite them correctly in the
  H04 companion.
