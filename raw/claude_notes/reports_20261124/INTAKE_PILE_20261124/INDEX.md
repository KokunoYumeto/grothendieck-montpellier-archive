# The intake pile of 24 November 2026: index for the conference

Written 24 Nov 2026, ~22:3x-22:4x UTC, by agent a88af1f4fbcac932c (Claude Opus 5.5 at effort high) for the main session
329fb1e6 (Claude Opus 5.5 at effort max). It is the first file Claude Fable 5.2 reads for its conference on the pile after
the user's weekly reset; Fable then writes the papers for what survives. Nothing here was sent or published. Some files
in this folder say "25 Nov" in their headers; the clock said 24 Nov when they were written.

**One fact the reader must have first.** The Riemann hypothesis for ζ and for every Dirichlet L-function is proved: L.
Alpöge, *Remark* (alpo.ge/remark.pdf, 20 Nov 2026), with a Lean formalization. The pile calls this theorem **A**. It does
not cover Hecke L-functions of fields other than Q, Artin L-functions, or the grand RH. **M** is GRH for Hecke L-functions
as claimed by A. M. Masullo's 940-page draft (20 Nov): it is not a proof, and nothing in the pile rests on it as true.

**Models.** Every research run named here is GPT-6 Astra (ChatGPT Pro mode), unless it is named otherwise. The October
answers (Q-series) ran before 24 Oct, so at reasoning effort ultra by the standing default. Codex is GPT-6.2 Astra at
reasoning effort ultra. Checkers are named with model and effort as their records give them. "No second reader" means
that only one model instance outside the run has checked the step.

---

## 1. What the pile is

On 24 Nov the user asked for everything to be taken in, sorted by interest, and checked for topicality ("they're like a
week old, which in AI mathematics terms means basically 4 decades"). Ten cluster readers (Claude Opus 5.5 at effort high)
read the research runs of 10-24 Nov cluster by cluster: what each proved, its checks, its relations and problems, with
spot checks recorded as check events. A literature agent listed what appeared from 14 to 24 Nov, with all 531 Hexagon
posts of the window. Four topicality agents (Claude Opus 5.5 at effort high) then searched Hexagon, arXiv and the AI
laboratories' releases item by item and gave each a verdict (STILL NEW, PARTLY, KNOWN BEFORE, OVERTAKEN, UNSETTLED) and a
yes or no on a paper now. Two finders (Claude Opus 5.5 at effort high) went back for older runs and notes that never
reached Hexagon.

Then five connection-map agents (Claude Opus 5.5 at effort max) and the pequalnp session 672ae3a0 (Claude Opus 5.5 at
effort max) looked for links across everything, including outside results, and proved several new statements on the
way; one of them (Koiran's Nullstellensatz theorem without GRH) has already had an independent check. Prompt updaters
(Claude Opus 5.5 at effort high and max) carried the findings into the prompts still waiting in TO_SEND, and version-2
work on our posted notes began. This index merges all of it.

**The files** (all in this folder unless a path is given):

| File | What it holds |
|---|---|
| `BRIEF.md` | The brief of the ten cluster readers. |
| `ALPOGE.md` (+ `_ITEMS.tsv`, `ALPOGE_s5cert_check.py`) | Cluster: NIGHT_AFTER_ALPOGE, BEYOND_DIRICHLET, CX_GRH, ALP_CONNES, ALP_MACHINE, ALPOGE_BRIDGES, MOONSHINE and kin; Ihara at Vandiver primes, CM orbits, S₅ Artin. |
| `ZETA_GRH.md` (+ `_ITEMS.tsv`) | Cluster: GRH_ALGORITHMS(_FINISH) (the 67c paper), ZETA_NEXT, ZETA_HEAT, SIGN_NEXT, HECKE_DIV, GRH_NIGHT. |
| `ZETA_GRH_67C_CODEX.md` | Codex's nine reviews of 67c and its post-freeze COFACTOR_LAYERS result, taken in and checked. |
| `HODGE.md` (+ `_ITEMS.tsv`) | Cluster: HODGE_SIGN, C44_POS, HODGE_FINISH Papers A/B, HODGE_DIVISION, THETA3, cote 44. |
| `GCT.md` (+ `_ITEMS.tsv`) | Cluster: GCT_POS, GCT_PLETH, GCT_KRON, GCT_OBS, GCT_NSRH, CUE_GCT, BR_PENCIL, GCT_GINEQ, DP_MULT. |
| `AG_POLISH.md` (+ `_ITEMS.tsv`) | Cluster: POLISH_ALGEBRAIC_GEOMETRY, POLISH_TOPOLOGY_PERIODS, POLISH_CRISTAUX, COUNTING_VARIETIES, SPLIT_ZERO_AFTER_FGJM, KTOWER, NGQ; its "Follow-up 25 Nov" (written 24 Nov) takes in COUNTING_VARIETIES cp02-03 and SPLIT_ZERO cp10. |
| `SWEEP3_A.md`, `SWEEP3_B.md` (+ `_ITEMS.tsv`) | The sweep-3 archive runs RESEARCH_SA05-SA23. |
| `LONGUE_MARCHE_A.md`, `LONGUE_MARCHE_B.md` (+ `_ITEMS.tsv`) | La Longue Marche runs: LM2-LM8, GT and Fermat towers (A); section ghosts, anabelian A1, sections over Q, EXIT_TOWER (B). |
| `DERIVATEURS.md` (+ `_ITEMS.tsv`) | Les Dérivateurs runs: FREX, S2COUNT, BISITE, RESIDUE, REVLOC, DER_LOCALIZERS. |
| `INTAKE_<RUN>_20261124_CHECK_EVENTS.tsv` (about 100 files; two `_20261125` for COUNTING_VARIETIES and SPLIT_ZERO, written 24 Nov) | The cluster readers' and finders' check events, one file per run. |
| `*_checks/`, `checks_GCT/`, `*_scripts/` | The readers' and mappers' check programs. |
| `LITERATURE_20261124.md` (+ `.tsv`) | What appeared 14-24 Nov that bears on the pile; appendix: all 531 Hexagon posts of the window. |
| `TOPICALITY_BRIEF.md` | The brief of the topicality pass. |
| `TOPICALITY_GCT_AG_DER.md` (+ `.tsv`, 47 rows) | Verdicts for GCT, AG_POLISH, DERIVATEURS. |
| `TOPICALITY_NT_HODGE.md` (+ `.tsv`, 48 rows) | Verdicts for ALPOGE, ZETA_GRH, HODGE; the October outside results that most verdicts rest on. |
| `TOPICALITY_SWEEP3.md` (+ `.tsv`, 95 rows) | Verdicts for SWEEP3_A and SWEEP3_B. |
| `TOPICALITY_LONGUE_MARCHE.md` (+ `.tsv`, 139 rows) | Verdicts for both Longue Marche clusters (nothing overtaken). |
| `OLDER_RUNS.md` (+ `.tsv`) | Older runs and the October answers never posted: Singer in degree one (Q02), TOTEX2; the board by stage. |
| `OLDER_NOTES.md` (+ `.tsv`, `_CHECK_EVENTS.tsv`) | Our notes and the user's corpus: finite monoids, benzels, Asvin G.'s towers. |
| `MAP_BRIEF.md` | The brief of the connection maps. |
| `MAP_COMPLEXITY.md` (+ `.tsv`, `_CHECK_EVENTS.tsv`) | GCT and VP/VNP: runs 98 and 99, the two VP ≠ VNP claims, Liu's two Hexagon posts; "the square decides". |
| `MAP_GALOIS_ANABELIAN.md` (+ `.tsv`, `_CHECK_EVENTS.tsv`, `_scripts/`, `_sources/`) | GT̂, Ihara, sections, Fermat; Lochak 2025; H17 corrections. |
| `MAP_GEOMETRY.md` (+ `.tsv`, `_CHECK_EVENTS.tsv`) | AG, crystals, cycles, Picard, Int(R); very ample Kodaira failure in every characteristic. |
| `MAP_HOMOTOPY_CATEGORIES.md` (+ `.tsv`, `_CHECK_EVENTS.tsv`) | Derivators, localizers, topoi, finite categories. |
| `MAP_NUMBER_THEORY.md` (+ `.tsv`, `_CHECK_EVENTS.tsv`) | Quasi-RH half-planes and what they unlock; Koiran without GRH; Λ-schemes. |
| `CHECK_HN_AM_20261124.md` (+ `_CHECK_EVENTS.tsv`) | Independent check of MAP_NUMBER_THEORY NK-1 (HN ∈ AM without GRH): holds. |
| `FLEET_MAP.md` (+ `.tsv`) | The pile against the pequalnp.com fleet's lemma graph; nodes our results settle. |
| `PENDING.md` | Unfinished intake work, e-mails, prompts and decisions as of 24 Nov ~21:2x UTC (since then: 98 cp02 and 99 cp01 were filed and read by MAP_COMPLEXITY). |
| `PROMPT_UPDATE_BRIEF.md` | The brief of the prompt updaters. |
| `PROMPT_UPDATES/*.md` (+ `68_sources/`, `70d_sources/`) | One report per updated (or held) waiting prompt, with proposals for new prompts. |
| `67c_v2/` | Version 2 of hexagon:2611.00987: CHANGELOG_v2.md, FABLE_FRAMING.md (Claude Fable 5.2 at effort max), FRAMING_DRAFT_aa83.md, source/, build/, pages/. In progress. |
| `v2/2611.00939/` | Version 2 of H06b: v2_edits.py, h06b_note_v2.tex, the sources checked. In progress. |
| `v2/_read_sources/` | arXiv sources fetched for the other v2s: 2611.30749 (Zhang, for H01), 2611.25978 and 2609.20002 (Katagiri, for H09). |
| `INDEX.md` | This file. |

---

## 2. The candidates worth a paper now

Merged from the four topicality files, OLDER_RUNS, OLDER_NOTES and the maps; deduplicated; grouped by field and ranked
by usefulness within each field. "Board" is `field_experts/hexagon/HEXAGON_BOARD.tsv` (109 rows, 24 Nov 13:35 local).
RR = `grothendieck_archive_transcription_20261110/research_returns/`; LMP = `longue_marche_pro_pilot_20261104/answers/`;
DCP = `derivateurs_companion_20261109/pro_prompts_max_20261112_work/`.

### 2.1 Complexity and GCT

**C1. Hilbert's Nullstellensatz is in AM, with no hypothesis** (and with it DIM_C, the parametric Nullstellensatz HNP,
Schubert vanishing in types A-D in AM ∩ coAM, and GCT V's transfers CX-K02, K05).
- *Statement.* Given a zero-free half-plane Re s > θ (θ < 1 fixed) for every Dedekind zeta function, which Cureton-Thorner
  (2610.00200v2, θ = 31/32, Lean-formalized), Hu (2610.00216v2, Cor. 9.6, θ = 7/8) and Liu (2611.00741, θ_G ≈ 0.8733)
  supply, HN ∈ AM ∩ RP^NP ⊆ Π₂^P (Koiran 1996 had it under GRH). A is not used.
- *Proof.* `MAP_NUMBER_THEORY.md` NK-1 (the half-plane prime ideal theorem; Koiran's Thm 9 without GRH; threshold
  x₀^{c/(1−θ)}).
- *Checks.* Deduction by aaf57cd5 (Claude Opus 5.5 at effort max), events E01-E05; independent check by a25c2acbb3a6f11f7
  (Claude Opus 5.5 at effort high), `CHECK_HN_AM_20261124.md`: items 1-5 hold (DIM_C rests on Koiran 1997, unopened;
  PR24b unopened; CX-K06 stays at statement level).
- *Topicality.* STILL NEW (`TOPICALITY_NT_HODGE.md` item 4; Hexagon catalogue of 1,530 works, arXiv, web). The fleet has
  no node on HN or AM (`FLEET_MAP.md` §1).
- *Board.* None (replaces CX_GRH CX-K03).
- *Gates.* An ECCC search; Koiran 1997 and Pak-Robichaux's coAM paper opened; explicit constants in the write-up.
  Unrefereed inputs (CT, Hu, Liu) must be named as such.

**C2. Numerical PH3 fails for Kronecker coefficients (H02b; GCT_POS K-023, R-NEW-004, K-024, PNEW-013).**
- *Statement.* For every n ≥ 2, Σ_s g((sⁿ),(sⁿ),(sⁿ)) tˢ has a pole at a primitive root of unity of order 2ⁿ⁻¹·3ʳ; the
  denominators of every positive form grow exponentially. This also refutes Mulmuley's relaxed "modular index" form in
  his erratum appendix to Briand-Orellana-Rosas (arXiv 0810.3163).
- *Proof.* RR/`GCT_POS_final_20261122T0219Z_unzipped/branches/plethysm/modular_pole_transfer.tex` and the kronecker
  branch; the paper must carry ALPOGE_GCT P-F23, P-F27, P-F30.
- *Checks.* Main session e0d20ada (Claude Opus 5.5 at effort max), every proof read and computations rerun:
  `reports_20261122/gct_pos_ph3_check/CHECK.md`.
- *Topicality.* STILL NEW (`TOPICALITY_GCT_AG_DER.md` A.1).
- *Board.* H02b, stage W. Its "next" (prompt 56) is stale: 56 and 56c were sent and rejected (ORDER.md).
- *Gates.* Cite the BOR appendix and replace 1.6.7 by 3.3.4; Hexagon search; the self-contained text.

**C3. Explicit occurrence obstructions for perₙ against detₙ with no padding (H13; GCT_KRON A-030, A-034, O-030).**
- *Statement.* For every n ≥ 3, λ = (n+q+1, 3, 2^{n²−2}), q = n²(n−2), in degree n² + 1, occurs in the coordinate ring of
  the permanent's orbit closure and has Kronecker coefficient zero; every stretch gives a strict gap; O-030 a
  three-parameter family.
- *Proof.* RR/`GCT_KRON_checkpoint_07_20261121T0415Z_unzipped/GCT_KRON_work/GCT_KRON.tex` l.8382, 9001-9330, 9423-9764.
- *Checks.* A-030: targeted proof check by the intake and a computation; the GCT cluster reader (Claude Opus 5.5 at effort
  high) recomputed F-024 at 15 pairs including A-030's point and re-proved the Kronecker zero; A-034: the intake's targeted
  check only (`GCT.md` l.120-128, 357-367).
- *Topicality.* STILL NEW; per₃/det₃ in degree 12 is Landsberg-Manivel-Ressayre's (A.2).
- *Board.* H13, stage W (reframe per the pequalnp check: LMR and the fleet's L-gct-070/074 cited, "best refereed").
- *Gates.* The reframing; literature (Bürgisser-Ikenmeyer-Panova 1604.06431, BIH 1501.05528); an independent re-proof.

**C4. All zeros of plethysm coefficients in outer degree five; positive polytope formulas in outer degrees four and five
(H20; GCT_PLETH G-031, G-036, T-037).**
- *Proof.* RR/`GCT_PLETH_checkpoint_09_20261121T0546Z_unzipped/GCT_PLETH.tex` from l.20109; `work/root/FIVE_ROW_SUPPORT_INDEX.json`.
- *Checks.* No reader outside the run has read the exhaustion proof or G-036's three providers.
- *Topicality.* G-031 STILL NEW (Kahle-Michałek 1408.5708 name the zero locus as open); G-036/T-037 PARTLY (only
  positivity is new) (A.7).
- *Board.* H20, stage G2. *Gates.* Proof checks; literature.

**C5. Four-row multiplicity obstructions under genuine padding (H14; CUE_GCT R-14 with R-13).**
- *Statement.* z^{n−m}perₘ against detₙ for the pairs (8,9) to (16,22); four-row gaps exist exactly when n² ≤ 2m² − m + 1.
- *Proof.* RR/`CUE_GCT_checkpoint_08_20261121T0649Z_unzipped/deliverables/CUE_GCT.tex` l.1238-1360.
- *Checks.* Intake only; R-27 (the exact √2 ceiling) unread by any intake.
- *Topicality.* STILL NEW (A.5). *Board.* H14, stage G1.
- *Gates.* Write the narrow version (m = 8-16); recompute the m = 11-16 certificates; the pequalnp reframing.

**C6. GCT VIII errata (H23; GCT_POS N-012, N-002, N-003, N-009; GCT_NSRH F57, F58, F67).**
- *Statement.* Conjecture 3.2 has no minimum as printed; the unimodality clause of the Positivity conjecture fails at
  rank 3 in both sign readings; strict positivity fails at rank 4; the printed b₂ sign.
- *Topicality.* STILL NEW (A.10). *Board.* H23 (stage N) and S93b.
- *State.* The e-mail to K. D. Mulmuley was sent 24 Nov 11:54 UTC (`reports_20261124/EMAILS_SENT_20261124.md` no. 6).
- *Gates.* His reply; an independent re-run of P-F-E3-01; a short note only if wanted.

**C7. Edge-function circuits for the fleet (SPLIT_ZERO_AFTER_FGJM paper 4).**
- *Statement.* thm:threemissing: for a four-cycle-free graph G, every circuit computing a polynomial in Sup(G) with at most
  three edges lacking a quadratic witness has ≥ |E| + vc(G) − 1 gates (exact). The one-sided theorem settles the fleet's
  L-meta-647; planes give L-meta-2239 (read-1 circuits on planes of order q need exactly N(q+2) − 1 gates).
- *Proof.* RR/`SPLIT_ZERO_AFTER_FGJM_checkpoint_10_20261124T2110Z_unzipped/workbench/papers/paper4/main.tex` l.85.
- *Checks.* First run read step by step by a2fedc2a (Claude Fable 5.2 at effort max); second run: a same-model re-proof by
  the run, and an exhaustive small-graph search by the AG_POLISH reader a4f5fd04 (Claude Opus 5.5 at effort high)
  (`AG_POLISH.md`, Follow-up). Mirror entries X-meta-005 (d1464a4) and X-meta-006 (f8123ad) are public.
- *Topicality.* Not passed through topicality; the fleet mirror shows both nodes open and unattempted (`FLEET_MAP.md` §2).
- *Gates.* Paper 4 must cite the fleet's L-meta-2237; filing with the fleet is the user's call. A paper only once the run
  ends.

**C8. Border rank of det₄ and per₄ (H03), only with the newest bound.** BR_PENCIL's 43 and GCT_OBS's 44 are superseded
inside the project by Codex's BORDER_RANK (≥ 52, not opened by any reader here). One paper on the newest checked bound,
with R-01 and P-01 as its method; 43 alone is not worth a paper (`TOPICALITY_GCT_AG_DER.md` A.11). Board H03, stage G1
(the 25 border-apolarity cases need an independent check). BORDER_RANK is Codex's run.

### 2.2 Number theory

**N1. Galois orbits of CM points in A_g with exponent 1/(4g) (H15; NIGHT_AFTER_ALPOGE A.ORBIT).**
- *Statement.* |Gal·x| ≥ c_g D_x^{1/(4g)}, explicit c_g, for every CM point of A_g and every centre order.
- *Proof.* RR/`NIGHT_AFTER_ALPOGE_checkpoint_13…/workbench/schemes-and-moduli-workbench/papers/cm-orbits/main.tex`; note
  `reports_20261123/h15_note/h15_note.pdf` (8 pp.).
- *Checks.* Step by step by ad855737 (Claude Opus 5.5 at effort high).
- *Topicality.* STILL NEW; Jaswal's effective André-Oort (2611.00339v3, Prop. 3.3) has a far smaller exponent; A is no
  longer needed, since the October Siegel-zero exclusions serve: present A as one input among several
  (`TOPICALITY_NT_HODGE.md` item 1).
- *Board.* H15, stage W: waits for the user's word (modest gain over Gaudron-Rémond Thm 1.9(5), which gives 1/(4g²)).

**N2. Artin's conjecture in Calegari's S₅ family under a weaker real-zero hypothesis (BEYOND_DIRICHLET BD-S25/S26).**
- *Statement.* If B = ζ_H/ζ_F and C = ζ_J′/ζ_J have no common off-centre real zero, Artin holds; central zeros of any
  order allowed; strictly weaker than Calegari's ζ_H(σ) ≠ 0 on (0,1).
- *Proof.* RR/`BEYOND_DIRICHLET_checkpoint_10…/workbench/papers/paper_II/main.tex` l.76-108, 334-405.
- *Checks.* ALPOGE cluster reader (Claude Opus 5.5 at effort high), `ALPOGE_s5cert_check.py`; no second reader.
- *Topicality.* STILL NEW; the four explicit fields (8249, 60061, 30301, 48976) UNSETTLED against Dwyer 2014's table
  (not opened: 403).
- *Board.* None. *Gates.* Open Dwyer 2014; cite Calegari §5 and Dwyer for the method.

**N3. Class groups generated in polylogarithmic size from a half-plane (MAP_NUMBER_THEORY NK-3).** Cl(K) is generated by
prime ideals of norm ≪ (log d_K)^{1/(1−θ)} (exponent 8 with Hu, 7.89 with Liu, 32 with CT); Q02's auxiliary prime
ℓ ≪ (r² log rp)^8. A two-line corollary of Hu's Cor. 9.6; deduction by the number-theory mapper (Claude Opus 5.5 at
effort max), events E06, E14; no second reader. Not a paper alone: a section of the 67c v2 or of an H29 note
(`PROMPT_UPDATES/68_CONNES_AFTER_RH_UPDATE.md` P2).

### 2.3 Hodge theory and cycles

**H1. The standard conjectures and Tate on all powers of explicit non-abelian fourfold axes in characteristic p (C44_POS
A13, A28, A30, A30a; H26).**
- *Statement.* On a dense set of Lefschetz-pencil axes B in E⁶ (E: y² = x³ − x) over F̄_p: the Hodge standard conjecture
  on Bᴺ and Tate on its powers.
- *Proof.* RR/`C44_POS_final…/C44_POS.tex` l.2627-2946, 27076-27466, 27722-28166.
- *Checks.* Targeted check by a8d75352 (Claude Opus 5.5 at effort high).
- *Topicality.* STILL NEW: Milne (hexagon:2611.00244, Thms 3.1, 3.5) covers abelian varieties over finite fields, so the
  ambient E⁶ but not the axes; Sun's Tate claim (arXiv 2611.28178) is unverified (`TOPICALITY_NT_HODGE.md` item 3).
- *Board.* None (H26 candidate). *Gates.* A second reading of Chin's Th. 5.7's hypotheses and of the ambient block; cite
  Milne's report.

**H2. The Hodge conjecture for abelian varieties as a uniform degree bound over finite fields, with explicit detectors
(HODGE_FINISH Paper A; H25).**
- *Statement.* Q01 (iv): HC for abelian varieties ⟺ a uniform numerator-degree bound at infinitely many good places of
  every CM point; detectors of degree 48, 192, 36; quadratic extraction; stabilization; the Ext² test.
- *Proof.* RR/`HODGE_FINISH_final…/workbench/work/UNFILED-A/v1/paper/main.tex` (66 pp.).
- *Checks.* HODGE_FINISH intake (aaf69461, Claude Opus 5.5 at effort high), fixes 1-7 made.
- *Topicality.* PARTLY: Q01 (i)⟺(ii)⟺(iii) is in substance Bhattacharjee-Bhattacharya 2610.00315v2 (Thm 1.1-1.2) and
  Cattani-Deligne-Kaplan; the degree form (iv) and the detectors are new.
- *New from the maps.* NK-2 (MAP_NUMBER_THEORY): the Galois-orbit criterion holds without André-Oort, with effective
  bounds through Jaswal (and Pila-Shankar-Tsimerman 2109.08788 makes the hypothesis a theorem anyway); Milne's report
  makes (iv) a uniform version of a known Tate theorem (reframe the abstract). Both are in prompt 70d now.
- *Board.* H25, stage G2. *Gates.* Restate novelty against 2610.00315; the Schoen 2007 page; drop André-Oort; settle Q28's
  Severn status.

**H3. Paper B: a coniveau-one criterion for Mumford's exceptional classes (HODGE_FINISH Paper B, 88 pp.; H25c).** Board
G2: open Bolognesi-Laterveer before the half-twist remark; a check of the overview; after H25.

### 2.4 Algebraic geometry and commutative algebra

**G1. An excellent Dedekind domain on which Grothendieck's cd conjecture (cote 31, sheet 84) fails on every affine open
(S12a; RESEARCH_SA12 A:A2-persistent-arithmetic-counterexample, A:wild-affine-counterexample).**
- *Statement.* R excellent, characteristic 0, 2 invertible, K = Frac R algebraic over Q: cd₂(K) = 1, cd₂(U) = 2 and Pic(U)/2
  infinite for every nonempty affine open U; no residue field orderable. Companion: H³(Spec W(F̄₂)[[t]][1/t], F₂) ≠ 0.
- *Proof.* SA12 `parts/A/quadratic_tower_A2_post05.tex`; it is Paper 1 of POLISH_ALGEBRAIC_GEOMETRY (cp35
  `workbench/papers/paper_01/`, Thms 1.1-1.2).
- *Checks.* SA12 intakes (a203d72b, a3c8d7de, Claude Opus 5.5 at effort max); POLISH_AG intakes (a018e2d2, Claude Opus 5.5
  at effort high).
- *Topicality.* STILL NEW (`TOPICALITY_SWEEP3.md` item 1); Hasse 1925, Schilling 1950, Heitmann 1974 unopened.
- *Board.* S12a, stage W. *Gates.* Those three sources; the locator fix (31/085 is a PDF page; sheet 84); a Proof
  overview; the run's final.

**G2. Very ample line bundles violate Kodaira vanishing on surfaces in every characteristic.** See section 5 (P90a v3):
it closes the open item of our posted note.

**G3. Jacobian summands of abelian varieties (S06b; RESEARCH_SA06 C.4n, C.4p, C.4m; with MAP_GEOMETRY NK2).**
- *Statement.* s_J(A) | gcd(2, δ(A)) for abelian surfaces and | gcd(6, δ(A)) for threefolds, in every characteristic; every
  ppav of dimension ≤ 5 has [2] factoring through Jacobians. New from the map: s_J | m | s_J² for every complex ppav (m the
  least algebraic multiple of θ^{g−1}/(g−1)!), so for a very general ppav s_J = 2 in dimensions 4 and 5 and 6 in
  dimension 6.
- *Proof.* SA06 `agents/frobenius/C4_additions.tex`, `C4_prym_addition.tex`, `C4_pt6_addition.tex`; NK2 in
  `MAP_GEOMETRY.md` (proved there, no second reader); POLISH_AG Paper 5 Thm 1.3.
- *Topicality.* PARTLY: C.4i is Scavia-Suzuki Prop. 3.4 and Beckmann-de Gaay Fortman §3; new are the removal of 3 for
  surfaces, of 5 and the excess 2-power for threefolds, and the char-2 Prym step (`TOPICALITY_SWEEP3.md` item 2).
- *Board.* S06b, stage W. *Gates.* Open BdGF 2202.05230 and EdGFS 2507.15704/2512.04902 at the statements; a second
  reader for NK2.

**G4. Murre's announced locally quasi-finite representability criterion, with a corrected axiom 7 (RESEARCH_SA17
A:pro7-representability, A:main-counterexample).** The literal axioms of cote 131 sheet 13 admit P(B) = α_p(B^h_(t)), not
representable; with the pro-modular axiom 7 the criterion holds over every locally noetherian base. Murre's Bourbaki 294
(1965) p. 247 announces it without proof. Proof: SA17 `sections/A_*`; POLISH_AG `paper_03/representability.tex`.
STILL NEW (`TOPICALITY_SWEEP3.md` item 4). Board: none. Gate: an independent re-proof of the fpqc descent step (de
Jong-Olander, JPAA 228 (2024), Thm 2).

**G5. A quantitative bound on Picard kernels (P90e; POLISH_AG Paper 2 thm:positive-excess-picard).** δ ≥ pd/(2(p−1)) for a
nontrivial order-p class trivial on a curve with Y² = d > 0, on any normal surface. Proof: RR/`POLISH_ALGEBRAIC_GEOMETRY_checkpoint_35_20261124T0416Z_unzipped/workbench/papers/paper_02/main.tex`
l.151, `positive_square_picard_strictness.tex`; full check by a018e2d2 (Claude Opus 5.5 at effort high). STILL NEW
against Cotner-Zavyalov (Compositio 160 (2024), Ex. 3.3.6) and Bhatt-de Jong (A.8). Board P90e, stage M. Gates: a
literature pass; the run's final.

**G6. Integral crystalline weak Lefschetz fails in low degree (POLISH_CRISTAUX Paper 1; RESEARCH_SA15
prop:OC-product-integral-counterexample; board S15).** X with a smooth ample Y such that H^i_cris(X/W) → H^i_cris(Y/W) is
not injective or not saturated, at every prime; Grothendieck's admitted 8.3 (cote 4) fails in degree one. Proof:
RR/`POLISH_CRISTAUX_checkpoint_33_20261124T2056Z_unzipped/…/workbench/papers/paper1/`. Every step checked by a512cf71
(Claude Opus 5.5 at effort max). STILL NEW, thin search (A.9; `TOPICALITY_SWEEP3.md` item 5). Board S15, stage G1. Best
written together with G2 (the same surface).

**G7. A wild quasi-étale double cover over one smooth genus-two exceptional curve (S12d; RESEARCH_SA12
D:wild-genus2-single-curve, rows 433-435).** In characteristic 2, b² + (t⁵ + t²a²)b + a⁵ = 0 has a cover étale off the
point and wild along C (y² + y = x⁵, C² = −1): the graded-cone tameness theorem needs its formal-linearity hypothesis.
Proof: `parts/B/D_wild_genus2_curve_B.tex`. STILL NEW (a3c8d7de's search; Cutkosky-Srinivasan 1993 read at the source by
the main session). Board S12d, stage W: a short note.

**G8. The crystalline Dieudonné functor is not full over a reduced base (S17a; RESEARCH_SA17 B:crystal-counterexamples).**
New: the two-plane example (the non-reduced one is classical). Note written: `reports_20261123/s17a_note/s17a_note.pdf`
(7 pp., ac8bd2a2, Claude Opus 5.5 at effort max). MAP_GEOMETRY NK9 adds the boundary: finite projective dimension of
differentials gives full faithfulness on reduced bases of finite type (Mok-Xu hexagon:2611.00721 + Anschütz-Le Bras;
abstracts only). Board S17a, stage W. Gates: a second re-proof; the Stacks 60.22.1 p = 2 correction after posting.

**G9. Smaller, each a short note.**
- P91a, Grothendieck's "transcendance forte" (cote 18:11) decided in corrected form (SA07 A.2.2-A.2.6): PARTLY; cut out of
  POLISH_TOPOLOGY_PERIODS Paper 3.
- SA15 thm:plane-char2-all-groups, exact monodromy of H¹_et(C, F₂) over ordinary plane curves in characteristic 2: PARTLY
  (odd-degree obstruction known: Cais-Ellenberg-Zureick-Brown 2013); board S15b; modest. MAP_GEOMETRY NK8 links it to
  POLISH_CRISTAUX Paper 21 (a conjectural template).
- SA14 F11, metabelian local π₁ of normal surface singularities in characteristic p is finitely generated: STILL NEW
  provisionally; board S14b; gate: the Kato-integrality dependency (Bright-Newton, Invent. 234 (2023), Thm 4.1 replaces the
  Krishna-Majumder preprint).
- MAP_GEOMETRY NK4 (cote 133): over a quadratic field, Φ_O is an isomorphism iff O = O_K and h_K = 1; proved in the map from
  SA17 C and NGQ A133 (no second reader); with board A133a/A133b (stage M, the NGQ run's final).
- MAP_GEOMETRY NK5: Int(D_q) is never flat for the two-branch domains, every q (extends Ma 2604.05922, q = 2); proved in the
  map; for an S20 v3 (the one-branch/two-branch dichotomy).

### 2.5 Galois theory, anabelian geometry, Grothendieck-Teichmüller

**A1. Lochak-Schneps 2006, Question 1.1, answered: unit hexagon solutions are automorphisms, and the profinite GT monoid is
a group (LM4_SUCCESSOR C.29, C.30, C.31).**
- *Statement.* C.30: a pair (λ, f), λ ∈ Ẑ^×, f ∈ F̂′, with duality and hexagon defines an automorphism of F̂₂ with no
  invertibility hypothesis (an arbitrary unit pair need not: f = [x,y]²). C.31: every object-fixing endomorphism of
  profinite PaB has unit λ. C.29: a peripheral-preserving endomorphism of a profinite surface group with boundary is an
  automorphism.
- *Proof.* LMP/`LM4_SUCCESSOR_checkpoint_40_20261117T1814Z_unzipped/LM4_SUCCESSOR/historical_data.tar`,
  `work_CE/C_further.tex` l.474-740.
- *Checks.* C.29, C.30 and C.31's torsion argument step by step by the LONGUE_MARCHE_A reader (Claude Opus 5.5 at effort
  high); Boavida de Brito-Horel-Robertson inputs (arXiv 1703.05143) unopened.
- *Topicality.* STILL NEW; Dolgushev-Guynee 2401.06870 Def. 2.5 still imposes invertibility (`TOPICALITY_LONGUE_MARCHE.md`
  item 1; residual risk: C.29 folklore in profinite rigidity).
- *Board.* None. *Gates.* BdBHR at Def. 6.4, Lemma 7.1, Props 7.3, 7.7, 8.1; goodness; a check of C.29 against Wilkes and
  Boggi-Zalesskii. A Claude note, not a Pro run (`PROMPT_UPDATES/LONGUE_MARCHE_PROPOSALS_AND_95.md` §2.3).

**A2. A1: rational points of curves in characteristic p are separated by the prime-to-p fundamental group (H07;
ANABELIAN_SUCCESSOR A.3, ANABELIAN_A1 A.1, A.33, A.CR10, ANABELIAN_A1_SUCCESSOR A.1).**
- *Statement.* For genus ≥ 2 over a finite field (and hyperbolic curves over fields finitely generated over F_p) the
  point-section map into the geometrically prime-to-p group is injective; the Saïdi-Tamagawa exceptional set is empty.
- *Proof and note.* `reports_20261123/h07_note/h07_note_v3.pdf` (9 pp., a2fedc2a, Claude Fable 5.2 at effort max).
- *Checks.* Two copies of the Longue Marche expert (Claude Fable 5.2 at effort max) read the chain; Steps 1-2 re-proved by
  a28ea31f (Claude Opus 5.5 at effort max); Steps 3-6 and Cor. 2 by the main session (Claude Opus 5.5 at effort max).
- *Topicality.* STILL NEW (`TOPICALITY_LONGUE_MARCHE.md` item 4; `OLDER_RUNS.md` A.3).
- *Board.* H07, stage W: waits for the user's look and word. *Gates.* Stix LNM 2054 ch. 7 (credit only); Mochizuki's
  journal reference; SGA 1 / Weil I locators.

**A3. Fermat's theorem for Selmer sections, for every odd exponent, with a correct proof (LM6 E.12; LM8_PUSH D.22, D.23;
FERMAT_SUCCESSOR A.1-A.11, A.52).**
- *Statement.* Every Selmer section of the affine Fermat curve U_n/Q is cuspidal for every odd n ≥ 3; with OpenAI's p-adic
  section theorem (6 Oct) the section set is the three cusp packets; none for even n.
- *Proof.* LMP/LM6 final (E.6-E.12; E.8 carries the false step), the repair in LMP/`LM8_PUSH_checkpoint_17_20261116T0252Z_unzipped/sections/D.tex`
  l.1560-1790, FERMAT_SUCCESSOR cp06 `deliverable/`.
- *Checks.* E.6-E.12 followed by Claude Fable 5.2 at effort high (14 Nov), who passed the false step; D.22 recomputed and
  D.23's local part read by the cluster reader (Claude Opus 5.5 at effort high); A.52 (n = 5) unchecked.
- *Topicality.* PARTLY: Steklov (arXiv 2602.17746v2, Thm A = 5.14) claims prime ℓ ≥ 7 with two faults our runs found (the
  Kummer-divisibility step at the cusp; "Y₁(7)(Q) = ∅" is false); n = 3, 5, 7 and composite n are ours.
- *Board.* None. *Gates.* A full read of D.23 and of n = 3, 5, 7; an e-mail to Steklov under the outreach rule.

**A4. Where GT̂ sits inside GT̂₀ (LM8_PUSH C.31, C.33, C.35, C.39; LM2 B.g2-B.g4; GT_TOWER_CHECK A.7, B.2.25-B.2.30;
SECTION_GHOSTS E.198; LM7_PUSH E.65, E.58, D.50).**
- *Statement.* GT̂₀/⟨⟨GT̂⟩⟩ maps onto C₅ × C₇ × C₁₃ × C₂^ℕ: Drinfeld's two relations do not imply the pentagon profinitely;
  GT̂ ⊊ ker Δ ⊊ GT̂₀; the graded algebra W is strictly larger than grt₁ from weight 7.
- *Checks.* LM7_PUSH E.65, E.58, D.50 refereed by Claude Opus 5.5 at effort max (14 Nov); B.g3 recomputed two ways by the
  cluster reader; unchecked outside the run: the passage from W to the group (LM8_PUSH P.2-P.4, C.30, C.32) and the C.35
  pentagon certificate. MAP_GALOIS_ANABELIAN N5 (no second reader): C.34's a_n = dim W_n, with d₁₂ = 1, d₁₄ = 10, ….
- *Topicality.* STILL NEW (`TOPICALITY_LONGUE_MARCHE.md` item 3; Ihara's special-derivation papers and Harbater-Schneps
  2000 unopened).
- *Board.* None. *Gates.* The referee pass first.

**A5. Étale reconstruction beyond sub-p-adic fields (LM5 F.50, F.49; ANABELIAN_149_PUSH F.45; ANABELIAN_A1_SUCCESSOR
B.137-B.147, B.49-B.55; ANABELIAN_SUCCESSOR F.3, F.7).** PARTLY: Carlson-Stix (arXiv 2410.22474v2, Thms A, B) and
Carlson-Haine-Wolf (2407.19920) cover the sub-p-adic members; new are fields containing μ_∞ (F.50, F.45, B.137-B.143) and
the negative classes. Checks: F.47 and half of F.45 read by Claude Fable 5.2 at effort high; B.46-B.50 for sense by Claude
Fable 5.2 at effort max; B.123-B.147 run only. Gate: a proof read of F.50, F.45, B.137-B.143.

### 2.6 Topology

**T1. Degree-one Singer vanishing in every dimension n ≥ 3 (Q02, October answer).**
- *Statement.* For a finite connected aspherical integral Poincaré complex of formal dimension n ≥ 3, b₁⁽²⁾ = b_{n−1}⁽²⁾ = 0;
  hence for every closed aspherical topological n-manifold. Group form: finitely presented integral PD(n) groups, n ≥ 3.
- *Proof.* `pro_batch_20261022_open_questions/answers/Q02-solution.tex` (Statement E l.60-70, Thm `thm:group` l.86-91):
  OpenAI's finite-energy-boundary argument (*The Singer conjecture in dimension four*, 25 Sep 2026) with its Section 2
  replaced by reductions valid in every dimension.
- *Checks.* One referee report, Claude Opus 5.5 at effort max (Message Batches API), 23 Oct
  (`F:\user\Documents\claude_open_courses_20260926\plan\pro_checks_20261023\Q02-check.md`); the new Section 2 and
  Bowditch's Lemma 1.4 checked by a24b3bc642b5dfddf (Claude Opus 5.5 at effort high), `INTAKE_Q02_20261124_CHECK_EVENTS.tsv`.
  Sections 3-10 (OpenAI's argument as reproduced) and the Treelike citations of Section 6 unchecked since October.
- *Topicality.* STILL NEW; Di Cerbo-Hunter-Thrasher (2601.08804) treat degree one as open (`OLDER_RUNS.md` A.1).
- *Board.* Not on the board: to add. *Gates.* An independent read of Sections 3-10; the Section 6 locators; credit to
  OpenAI and to the Reddit observation of 10 Oct.

### 2.7 Homotopy theory, categories, Les Dérivateurs

**D1. Exact colimits, total asphericity and filteredness (TOTEX2 A.1-A.3, D.1, D.2; TOTAL_ASPHERICITY C.5, C.13; PRETOT F.3;
DER_FOLLOWUP Part A; with FREX A.9-A.11, A.17-A.19, A.33, C.10-C.13).** One paper.
- *Statement.* The category C_δ of ordered 3-uniform hypergraphs with δ(U) = 2|U| − 3e(U) > 0 is small, connected and total
  (colimits of simplicial sets over it are homotopy colimits), yet colim over it is not exact over Q nor any F_p: among
  connected small categories, filtered ⊊ exact ⊊ total ⊊ quasi-filtered; Grothendieck's "totalement W∞-asphérique ⇒
  filtrante" (Les Dérivateurs II ms. 36ter) is false. FREX: exactness of colimits and amenability are independent both ways
  for Fraïssé categories (ordered posets exact over every ring, non-amenable; independently ordered F₂-spaces amenable,
  exact over Q, not over F₂ or Z).
- *Proof.* DCP/`TOTAL_EXACT_2/checkpoints/TOTEX2_checkpoint_03_20261113T1144Z_unzipped/TOTEX2/sections/main_question.tex`;
  `FRAISSE_EXACT/FREX_final_20261118T1235Z_unzipped/FREX/sections/A.tex`, `C.tex`, `D.tex`.
- *Checks.* TOTEX2: intake a5ead5c6 (Claude Fable 5.2 at effort high), referee afbbdefd (Claude Fable 5.2 at effort max);
  TOTASPH all 107 items by a0a83137 (Claude Fable 5.2 at effort max); PRETOT by abe075dc (Claude Opus 5.5 at effort max);
  a computation on all 31,176 objects of C_δ with 3-7 points (evidence, not proof) by a24b3bc6 (Claude Opus 5.5 at effort
  high). FREX: every step by its intake (Claude Opus 5.5 at effort max).
- *Topicality.* STILL NEW for total ⇏ exact and the four-term chain (filtered ⊊ exact is Isbell-Mitchell 1973); FREX STILL
  NEW (`OLDER_RUNS.md` A.2; `TOPICALITY_GCT_AG_DER.md` A.4).
- *Board.* None. *Gates.* Keep Rosický's "totally aspherical" (math/0509655) apart; a specialist look at Dwyer-Kan, Chorny,
  Raptis for C.5; for FREX, whether A.9-A.10's signed averaging is a Z-valued Harman-Snowden measure (Invent. Math. 2026;
  Snowden 2609.02021 opened, silent); MAP_HOMOTOPY_CATEGORIES K3 reads FREX's exactness as a topos property (Caramello
  2014, to open).

**D2. Classifying spaces of finite monoids (CATHOT OWN_RESULTS §§1-2; S2COUNT A.M1, B:main, B:smallcategories,
CD:alltargets; FINMON).** One paper.
- *Statement.* If a finite monoid M has H_k(M; Z) = 0 for all large k, its universal group is trivial; BM is homotopy-finite
  ⟺ homotopy finite-dimensional ⟺ bounded homology, and then simply connected. With Ben-Bassat (arXiv 2610.38760v1,
  Fiedorowicz's conjecture) the types BM with bounded homology are exactly the finite simply connected complexes; his
  Conj. 7.1 (RP² realizable) fails. S2COUNT: a six-arrow monoid with BM₁ ≃ ⋁_{n≥2} Sⁿ, |[BM₁, S²]| = 2^ℵ₀, six arrows
  minimal. FINMON: a 23-element CP² monoid.
- *Proof.* `derivateurs_companion_20261109/pro_reviews_max_20261112/1_CATHOT/OWN_RESULTS.md` §§1-2 (Claude Fable 5.2 at
  effort max, 12 Nov); DCP/`S2COUNT/S2COUNT_final_20261116T0841Z_unzipped/S2COUNT/sections/` (`A_agent.tex`, `B_root.tex`,
  `CD_agent.tex` l.300-440).
- *Checks.* OWN_RESULTS re-derived by a second Claude Fable 5.2 at effort max (same family) and targeted-checked by the
  older-notes finder (Claude Opus 5.5 at effort high); S2COUNT followed step by step by the DERIVATEURS reader (Claude Opus
  5.5 at effort high); FINMON's 23-element monoid rests on the run's own verifiers.
- *Topicality.* STILL NEW (provisional) for OWN_RESULTS; S2COUNT PARTLY (Sweeney 2502.05276v2 Ex. 5.2-5.3 computes the
  homology, not the homotopy type) (`OLDER_NOTES.md` item 1; `TOPICALITY_GCT_AG_DER.md` A.3).
- *Board.* None. *Gates.* Full-text search of Ben-Bassat, Martinian-Steinberg, Sweeney, Fiedorowicz 1984, McDuff; a
  re-proof by another model family; an exact check of FINMON's monoid; whether Ben-Bassat answered our note of 12 Nov.
  Prompt 05_FINMON_CP2_night now carries Ben-Bassat (waiting).

**D3. Footnote 56 and Corollaire 7.7.2 of Les Dérivateurs XVI: absolute Theorem A does not give relative Theorem A (BISITE
A.32 → RESIDUE B.2-B.4 → REVLOC F.1, F.1.1 → DER_LOCALIZERS A5.1-A5.4).** A class separating weak fundamental localizers
from fundamental ones for the literal axioms, with the exact dependence on Loc (6′a), (8), (9); Maltsiniotis (Astérisque
301 §1.1) gives no such class. Proofs: BISITE `sections/A.tex:434`, RESIDUE `sections/B.tex:54,138`, REVLOC `F12.tex`,
DER_LOCALIZERS `A5.tex`, checked step by step by the intakes. STILL NEW. Gate: Cisinski 2006 (Astérisque 308) §§4.2, 6.1;
the corrected priority order (DERIVATEURS.md P1).

### 2.8 Combinatorics and history

- **Propp's benzel Problems 6 and 7** (the user's corpus, `Papors/Chatnotes/Benzel/3/benzels_standalone_illustrated_preprint.tex`,
  24 May; GPT-5-series Pro model by date): T₁₀₃(n, 2n−3) ≥ 2·3^{n−5} by a shell recursion; T₁₀₃(n, 2n) = 1; T₁₀₃(n, 2n−4)
  ≥ 33·3^{n−5}. Counts for n ≤ 8 reproduced by the older-notes finder's code; STILL NEW as far as seen; modest; gates: read
  DLPY and DFLPY for b = 2a; re-read the general-n forcing; use only the 24 May text (`OLDER_NOTES.md` item 2).
- **The Hilbert-space trace formula proved in Grothendieck's hand** (S23b; RESEARCH_SA23 geo-H, cote 1 sheets 79-80,
  111-112): a historical note against D. Robert's account (EMS Newsletter, Sept. 2017); gate: open CR 1951 p. 1557, the
  1955 memoir II-13, the 1956 Erratum, Pietsch 2020.

---

## 3. New knowledge from combining items (the maps)

Status words follow each map: "proved here" means one map agent (Claude Opus 5.5 at effort max) wrote and checked the
proof, and **no second reader has seen it**, unless a second check is named.

| # | Statement | From | Status |
|---|---|---|---|
| NT-1 | HN ∈ AM (and DIM_C, HNP, Schubert vanishing, CX-K02/K05) given a uniform zero-free half-plane: unconditional now | CX_GRH × Koiran 1996 × CT/Hu/Liu | Proved (MAP_NUMBER_THEORY NK-1); **independently checked: holds** (`CHECK_HN_AM_20261124.md`, a25c2acb, Claude Opus 5.5 at effort high) |
| NT-2 | Paper A's Galois-orbit criterion without André-Oort, with effective bounds via Jaswal | HODGE_FINISH × Jaswal 2611.00339v3 × PST | Deduction (E07); no second reader; now in 70d |
| NT-3 | Cl(K) generated by primes of norm ≪ (log d_K)^{1/(1−θ)}; Q02's auxiliary prime | GRH_ALGORITHMS × Hu Cor. 9.6 | Deduction (E06, E14); no second reader |
| NT-4 | THETA3-C32: an integral Weil class of self-intersection 128; THETA3's cycle is 24 times it | THETA3 | Proved (E08); no second reader |
| NT-5 | BEYOND_DIRICHLET rows "under Dirichlet GRH" or "under zeta RH" are unconditional by A; content exponent 0.2494 | BD × A × Liu | Computation (E09-E10) |
| NT-6 | A is the Riemann hypothesis of Borger's F₁-geometry: zeros of ζ_X for smooth proper Λ-schemes lie on Re s = j + ½ or j | BD-R83 × Borger × A | Proof sketch; gate: Borger §6 |
| NT-7 | Rational and numerical equivalence agree for varieties of abelian type over finite fields | Kahn 2003 × Milne 2611.00244 | Two-line corollary; Kahn's abstract only opened |
| NT-8 | De Bruijn-Newman Λ = 0 (A with Rodgers-Tao); Ogg's cutoff 4300 unconditional; three Hexagon posts' hypotheses removed | A × outside | Small |
| GE-1 | Very ample Kodaira failure on surfaces in every characteristic (closes P90a v2's open item) | POLISH_CRISTAUX Paper 1 × P90a | Re-derived at reading level; a512cf71 targeted check of Thm 1.2 ranges; needs a different-model check of `prop:polarization` (odd p) |
| GE-2 | s_J \| m \| s_J² for complex ppav; very general s_J = 2 (g = 4, 5), 6 (g = 6) | SA06 C.4 × POLISH_AG Paper 5 × EdGFS | Proved; no second reader |
| GE-3 | Shift law for the inertia-character index (POLISH_CRISTAUX Paper 2); the merge run's v = 0 gate closed by thread A | POLISH_CRISTAUX threads | Conjecture; consistency computed |
| GE-4 | Cote 133 over quadratic orders: polynomial generation iff O = O_K and h_K = 1 | SA17 C × NGQ A133 | Proved; no second reader |
| GE-5 | Int(D_q) never flat for the two-branch domains, all q | Ma 2604.05922 × SA20 B.016 | Proved (re-proof of Ma's q = 2 plus the extension); no second reader |
| GE-6 | One congruence explains the three Q(√−23) phenomena of cote 15 | SA06 × ARCH_ALG × NGQ | Proved; classical Honda-Tate |
| GE-7 | Picard kernels at three levels; scheme-level "noyau nul" (cote 57:97-100) fails for ample divisors | P90a, Paper 1, Cotner-Zavyalov | Comparison; point level open |
| GE-8 | Hasse-Witt monodromy in char 2: one template, two instances | SA15 × POLISH_CRISTAUX Paper 21 | Conjecture |
| GE-9 | Dieudonné full faithfulness on reduced bases with pd Ω < ∞ | Mok-Xu 2611.00721 × ALB | Chain of cited results; abstracts |
| GA-1 | Out*(Γ̌_{g,[n]}) ≅ GT̂ for every generic type; Lochak's chain collapses | H17 Thm 1 × Lochak 2025 Thm 5.10 | Proved (MAP_GALOIS N1); no second reader |
| GA-2 | Tripod sections over Q integral at every odd prime: the three points −1, 2, 1/2 (S = {2}); recognition reduced to potentially multiplicative cusp places | SECTIONS_OVER_Q × Stix 2015 | Proved (N2, `checks_su_irr.py`); no second reader |
| GA-3 | The section-tower obstruction is K_{2r}(Z) ⊗ Z_ℓ; vanishes unless irregular pair or Vandiver failure | SECTION_GHOSTS × Herbrand-Ribet × Mok-Zheng | Proved (N3), mostly classical |
| GA-4 | G_Q = GT̂ ⟺ Λ₀ = G_{K₂}; Galois-trivial characters are abelian tests decided on Λ₀ | H17 × Hatcher-Lochak-Schneps | Proved (N4); no second reader |
| GA-5 | LM8_PUSH C.34's a_n = dim W_n (LM2); d_{p−1} candidate characters at each p ≥ 13 | LM8_PUSH × LM2 | Computation (N5); no second reader |
| CO-1 | "The square decides": under ANT's A.6 and C.3, a strict shortening of some crossing tensor ⟺ the Euclidean unit square is not a price ⟺ every price is a tree pseudometric | runs 98, 99 × ANT × OAI × Liu 2611.00994 | Conditional on unrefereed appendices; runs 98 and 99 disagree on one direction (98 SH-08 vs 99 Q3b) |
| CO-2 | Shape of a GCT certificate for the claimed separation (no four-row obstruction; a highest-weight vector, 99 Q6e) | OAI Cor. 1.2 × CUE_GCT × GCT_KRON × BIP | Conditional on OAI |
| CO-3 | Exponents 5/4 and 4/3 come from two cost accountings | runs 98, 99 | Two runs agree |
| CO-4 | Moment-polytope spectral points give only tree prices (distance (√2 − 1)/2 from the square) | run 99 × SDW 2601.21553v2 | Run-only |
| CO-5 | Height of the Artin-Mazur formal group of X_φ is 1 iff #SAT ≢ 0 (mod p) | COUNTING_VARIETIES cp01 | Our observation; not in the run |
| HC-1 | The C.3 problem is the contractibility of one nerve | SA08 C × DERIVATEURS | Proved (K1) |
| HC-2 | Pushouts of ordinary topoi compute shapes iff the homotopy pushout is aspherical | SA10 B2 × LM5 C.3 | Proved for discrete groups (K2); check Moerdijk, HTT 7.1.6 |
| HC-3 | FREX's exactness is a property of the topos Cont(Aut M) | FREX A.1 × Caramello 2014 | Dictionary; Caramello to open |
| HC-4 | Finite categories realize types outside finite posets (S2COUNT) | S2COUNT × McCord × Hora 2611.00879 | Comparison |
| FL-1 | L-meta-647 and L-meta-2239 of the pequalnp fleet settled on paper; 608/612 sharpened | SPLIT_ZERO paper 4 × fleet L-meta-2237 | See C7 |

---

## 4. Outside results that change our items

| Outside result (locator, date) | Our items | How |
|---|---|---|
| OpenAI, deterministic polynomial factorization over F_p (`openai/math`, 4 Oct 2026; "PF26") | 67c / GRH_ALGORITHMS P144/P145/P149, P125/P126; CX_GRH CX-N01-N04, N13, N15 | Outcome known before (with Shoup); CX-N15 overtaken; the 67c v2 must say so in its abstract |
| Siegel zeros excluded: OpenAI (1 Oct); Green hexagon:2610.00311; Guo 2610.00461; Frei-Kai 2610.00466; Liu 2611.00080v2 | H15 (A.ORBIT); ZETA_NEXT NX01/NX02, NC01-NC04 | A not needed there; present A as one input |
| Zero-free half-planes: Cureton-Thorner 2610.00200v2 (31/32); Hu 2610.00216v2 (7/8, Cor. 9.6); Liu 2611.00741 (θ_G) | CX-K01-K06; GRH_ALGORITHMS Q02, Q03; BD window; MOONSHINE Q1; GRH_NIGHT Artin rows | NT-1, NT-3, NT-5; odd 2-dim Artin L-functions zero-free for Re s > θ_G |
| Mok-Zheng hexagon:2611.00998 (K_{4m}(Z) = 0, m ≤ 30); Pintar hexagon:2611.00829v3 (to degree 104) | KTOWER K12-K80; NIGHT_AFTER_ALPOGE C.K12/K80; H18; H06a | Overtaken; credit chain: Pintar's joint representation theorem is our KTOWER K17-S17-JOINT (MAP_NUMBER_THEORY §2) |
| Milne hexagon:2611.00244v1 (Tate and Hodge standard for abelian varieties over F_q) | Paper A Q01(iv); C44_POS ambient E⁶; SA05 B.1 | Reframe Paper A; C44's axes remain new; NT-7 |
| Severn hexagon:2610.00387v2 Thm A | HODGE_DIVISION D-G34-01..07 (H19) | Known before |
| Bhattacharjee-Bhattacharya 2610.00315v2 | Paper A Q01 (i)-(iii); HECKE_DIV R21-R23 | Partly known |
| Jaswal 2611.00339v3; Pila-Shankar-Tsimerman 2109.08788 | Paper A Q27; H15 comparison | NT-2 |
| D. Zhang, arXiv 2611.30749 | H01 (hexagon:2611.00789) | First outside exposition; cites our Lemma 3; no error reported; read before v2 |
| Katagiri, arXiv 2611.25978 and 2609.20002 | H09 (hexagon:2611.00938) | To cite in a v2 (`TOPICALITY_GCT_AG_DER.tsv`) |
| Lochak, Algebra i Analiz 37:2 (2025), Thm 5.10 | H17; SECTION_GHOSTS E.177-E.181; EXIT_TOWER E.43-E.45 | GA-1; H17 v2 must cite him |
| Furusho, RIMS Kôkyûroku 1267 (2002) | H17's open question on (III′) | Gives (III′) explicitly |
| Dolgushev-Guynee 2401.06870 | LM4_SUCCESSOR C.30/C.31; H17 l.158 | Invertibility still imposed; H17's "known" unsupported |
| Boggi arXiv 2011.15075v6 | EXIT_TOWER E.45, E.14 | Claims Out^{I₀} ≅ Σ_n × GT̂; GA-1 gives the Out* part without his Prop. 6.9 / Lemma 6.16 |
| Steklov arXiv 2602.17746v2 | Fermat for Selmer sections (A3) | Claims ℓ ≥ 7 with two faults |
| Carlson-Stix 2410.22474v2; Carlson-Haine-Wolf 2407.19920 | Reconstruction items (A5) | Partly covered |
| Stix, Invent. Math. 199 (2015); Betts-Kumpitsch-Lüdtke 2305.09462v2; Li-Lüdtke 2608.20615; Zehavi 2611.18218 | SECTIONS_OVER_Q A.24; the tripod section conjecture | GA-2; special cases by Chabauty-Kim, to cite |
| Ishii arXiv 2312.04196v3 | C.IHARA (H06b); LM8_PUSH Part A; SA07 F.3.32 | Same object (CM once-punctured curve); H06b v2 locators |
| Gaifullin 2611.20353; Pshenichnyi 2611.24813 | EXIT_TOWER D.50-D.106 | Neighbours for the genus-three Torelli chain |
| Najman hexagon:2611.00991 | LM6 B.15 | Torsion part of its input |
| Ben-Bassat arXiv 2610.38760v1 | Finite monoids (D2); FINMON | Our theorem is its converse; his Conj. 7.1 fails |
| Sweeney 2502.05276v2 | S2COUNT A.M1 | Homology known; homotopy type new |
| Harman-Snowden (Invent. Math. 2026); Snowden 2609.02021 | FREX | The gate before writing D1 |
| Ishii-Yoshida 2410.15282v3; Li-Wang 2604.23997 | SA12 L6c; SA12 B.1 | Known before |
| Flach-Morin, Doc. Math. 23 (2018) §5.8.3 | SA05 / SA06 Weil-étale table of cote 15:173 | Known before (a correction of Grothendieck's table only) |
| Scavia-Suzuki 2507.09821v2; BdGF 2202.05230; EdGFS 2507.15704, 2512.04902 | S06b; POLISH_AG Paper 5 | Partly known; GE-2 sharpness |
| Ma 2604.05922v2; Jiang et al. 2605.25259v2 | SA20 B.016; S20 | B.016 known; GE-5 extends Ma |
| Mok-Xu hexagon:2611.00721 | SA17 B.3 (S17a) | GE-9 |
| Cotner-Zavyalov 2204.06121 (Compositio 2024) Ex. 3.3.6 | P90e; SA14 A1/A2 | Nearest literature; scheme-level failure for ample divisors |
| SGA 2 re-edition, Exp. XIII §6 note (23); Hamm-Lê 1990 | SA22 local Hurewicz | Known before |
| OpenAI "VP and VNP are different" (23 Nov); Anthropic "VP ≠ VNP over every field" (hexagon:2611.00954) | GCT items; fleet L-gct-011, 026, 028 | Implied fleet nodes if either holds; fixed-size and positivity items unchanged; CO-2 |
| Liu hexagon:2611.00994 and 2611.00972 | Runs 98, 99; border-rank items | CO-1; Anthropic's Appendices A/C now carry four bodies of work |
| Sakabe-Doğan-Walter 2601.21553v2; Botero et al. 2604.18283v2; Alman-Li-Pratt 2604.01386v2 | Run 99; our 24 Nov integration's "Fact 2" | CO-4 |
| Kharel-La Rosa-Wiese 2206.08116 | BD-S23 | Known before |
| Richardson 1987 Lemma 5.1; Kleiman 1968 Th. 2.13 | BR-12302 (H08); SIGN_NEXT SN-C04 | Known before |
| Derksen 1308.3860 Cor. 1.10 | GCT_GINEQ F-05 | Known before |
| Riba 1903.04396 Cor. 4.1 (Sah 1974) | POLISH_CRISTAUX Paper 8 thm:sections | Known before |
| OEIS A058129; Fiedorowicz 1984 | RESIDUE A.5 | Known before |
| Jansen arXiv 2611.09392 | October answer Q03 | Overtaken |
| Dasgupta-Hruska 2204.02463; Loring 2014 | Q22; Q21 | Partly |
| Hora hexagon:2611.00879; Sun hexagon:2611.00648; Pongrácz hexagon:2611.00444 | LM5, SA10, FREX, S2COUNT | Context (HC-4, K3) |

---

## 5. Our posted notes and their v2s

| Note | Hexagon | State on 24 Nov | Next |
|---|---|---|---|
| **67c** (H29/H29b), *Finite fields of prime degree from small cyclotomic cofactors* | 2611.00987v1 (committed 11:25 UTC, 191 pp.); publication not recorded | v2 in `67c_v2/`: CHANGELOG lists (1) framing by PF26 (FRAMING_PENDING; `FABLE_FRAMING.md` written 22:34 UTC by ae2754d9, Claude Fable 5.2 at effort max: PF26 with Shoup gives Theorems 1.1-1.5 and 1.10 in outcome, 1.6, 1.8, 1.11-1.14 in part, not 1.7; to be checked and merged by aa83ec927e8d41694, Claude Opus 5.5 at effort high); (2) Remark 16.4, Codex's COFACTOR_LAYERS, checked with an independent program (`ZETA_GRH_67C_CODEX.md`); (3) [KB:K] = p − 1; (4) a "Checks recorded for version 2" paragraph. BUILD_PENDING. Codex's nine reviews found nothing against v1. | Merge the framing, build, the main session checks changed pages, 672ae3a0 deposits. Optional: NT-3 as a section (68 update P2). Tang passages stay unread and byte for byte. |
| **H01**, *A short proof of Deligne's bound for Frobenius eigenvalues, after Alpöge* | 2611.00789v1 (21 Nov) | STILL NEW. Zhang's exposition (2611.30749) fetched to `v2/_read_sources/`; no v2 text on disk. | v2: add GCT_NSRH F50, SN-14, AM-S1-S3 (a phase replaces the sign only if it commutes with Frobenius), once checked; possibly the sign-only Gauss-sum remark (`GCT.md` l.593); cite Zhang. |
| **H06b**, Ihara's kernel question at Vandiver primes | 2611.00939v1 (23 Nov) | STILL NEW. v2 drafted in `v2/2611.00939/` (`v2_edits.py` → `h06b_note_v2.tex`): Sharifi 2002's theorem number, Ishii's locators (Thm A) and a remark on his statement, Sharifi 2019 quoted at p. 221, date line; sources checked in `sources_checked/` (incl. Mok-Zheng). Not yet read by a second agent. | Check v2, then deposit; research question P4 (component-local kernel from K_{4m}(Z) = 0, m ≤ 30) goes to a prompt, not the note. Author notices (Sharifi; Wake, Wang-Erickson; Fukaya, Kato; Ishii): no drafts. |
| **H09**, divisibility of invariant derivatives on formal groups of every height | 2611.00938v1 (23 Nov) | STILL NEW. Katagiri's two papers fetched to `v2/_read_sources/`; no v2 text on disk. | v2: cite Katagiri 2611.25978 and 2609.20002. Author notices (Katz, Bannai-Kobayashi, Boxall, Berger): no drafts. |
| **H17**, relation (IV) of Nakamura-Schneps on GT̂; Δ = 0 on GT̂ | 2611.00940v1 (23 Nov) | STILL NEW (Lochak-Nakamura-Schneps 2602.12462 call it unclear). The v2 is a49aabbf's job (Claude Fable 5.2 at effort max; `PROMPT_UPDATES/LONGUE_MARCHE_PROPOSALS_AND_95.md`); nothing on disk. | v2 (MAP_GALOIS N1, N6): cite Lochak 2025 and EXIT_TOWER E.43-E.44; fix l.158 ("GT̂ ⊊ GT̂₀ is known" has no citation); add GA-1 as a corollary; Corollary 4's inputs LM7_PUSH E.65, E.58; DELTA_SEXTIC Prop. 3 as a remark; settle (III′) with Furusho 2002 and Nakamura-Schneps §6 before calling it open. |
| **P90a**, *A very ample counterexample to Kodaira vanishing on a surface* | 2611.00936v2 (published 24 Nov 16:29 UTC) | v2 lists odd characteristic as open (`reports_20261123/p90a_note/p90a_note_v2.tex` l.467-469). **POLISH_CRISTAUX Paper 1, `thm:all-primes` and `prop:polarization`** (RR/`POLISH_CRISTAUX_checkpoint_33_…/workbench/papers/paper1/main.tex` l.115, l.210) proves the generated polarization for every p (MAP_GEOMETRY NK1). | v3, or a merged note with Paper 1 (also carrying G6's integral crystalline failure on the same surface). Gates: a different-model check of `prop:polarization` for odd p (the map's is at reading level); Zheng 2017 §2.2. The Kweon, Mukai, Zheng e-mails went out after v2 (Zheng bounced). |

Also posted and standing: S20 (2611.00937v2; GE-5 gives a v3 with the dichotomy), H22 (2611.00993), ZH3 (2611.00996; STILL
NEW against Knausgård, Lamzouri, Suzuki, Andrews-Connes-La Gatta).

---

## 6. Questions for the conference

Merged from the five maps and FLEET_MAP, by region crossings.

1. **Koiran without GRH, and what else rests on it** (MAP_NT T1). Write NT-1 as a Hexagon note now, or as a Pro run that also
   decides Bürgisser's "Cook's versus Valiant's hypothesis" (TCS 235, 2000) under the half-plane?
2. **Effective special points and Weil classes** (MAP_NT T2, MAP_GEOMETRY 8). Fold NT-2 and Milne's report into Paper A v2;
   is H(D) computable?
3. **What quasi-RH buys in algorithmic number theory** (MAP_NT T3): NT-3 beside PF26 in the 67c v2.
4. **The cubic rung** (MAP_NT T4): BEYOND_DIRICHLET, ALP_CONNES, ALP_MACHINE, MOONSHINE, GRH_ALGORITHMS all stop at RH for
   cubic characters of Q(ω); why Liu's method stops at θ_G (the pole of 1/ζ(3s)), and whether a reweighting with ζ(3s) in the
   numerator can cancel it; where an order-3 analogue of Alpöge's sign step would act.
5. **K-groups of Z after Step 17 and the Galois action on π₁(P¹ − 3 points)** (MAP_NT T5, MAP_GALOIS P5): a component-local
   Anderson-Ihara statement from K_{4m}(Z) = 0 (m ≤ 30)?
6. **F₁ and where A stops** (MAP_NT T7): NT-6 after BD-R83 is compared with Borger §6.
7. **The procongruence Teichmüller tower is governed by genus zero** (MAP_GALOIS P1): H17 v2 with GA-1.
8. **GT̂ inside the gentle group** (MAP_GALOIS P2, with A4): GA-4 as the frame, GA-5 as the dictionary; the next computation is
   weight 16 over F₁₇ (37 candidates).
9. **Sections of the tripod over Q** (MAP_GALOIS P3): what the Legendre route leaves after GA-2 and GA-3; first case S = {2, 3}.
10. **π₁ of the once-punctured CM elliptic curves** (MAP_GALOIS P4): Ishii's kernel question with the C.IHARA method.
11. **Very ample Kodaira failure in every characteristic** (MAP_GEOMETRY 1): v3 of P90a or a merged note with POLISH_CRISTAUX
    Paper 1.
12. **Integral Jacobian factors** (MAP_GEOMETRY 2): G3 with GE-2.
13. **Representation rings over orders, cote 133** (MAP_GEOMETRY 3): GE-4 beyond quadratic orders (the semilocal-completion
    step).
14. **Integer-valued polynomials, one branch against two** (MAP_GEOMETRY 4): GE-5 and the flatness conjecture.
15. **Picard kernels: points against schemes** (MAP_GEOMETRY 7): Grothendieck's boxed "noyau nul si n ≥ 4" at the point level.
16. **Inertia-index shift law; Hasse-Witt monodromy in characteristic 2** (MAP_GEOMETRY 5, 6): GE-3 and GE-8 as successor
    questions for POLISH_CRISTAUX.
17. **"The square decides"** (MAP_COMPLEXITY T1): CO-1 as a note after a different-model check of 98's PG-CROSSPOLY-GATE,
    PG-FOUR-CONDITIONAL, SH-08 and 99's planar reduction, and run 99's final.
18. **GCT after VP ≠ VNP** (MAP_COMPLEXITY T2, T3, T6): what a representation-theoretic certificate must look like (CO-2); the
    GCT VIII errata in one message.
19. **Counting in coherent cohomology** (MAP_COMPLEXITY T4): CO-5; does a_{p²} encode a further count?
20. **Fleet circuit bounds** (MAP_COMPLEXITY T5, FLEET_MAP §2): C7 and the remaining four-missing-witness case of 608/612.
21. **Border rank against asymptotic rank** (MAP_COMPLEXITY T7): first compute the local ranks of the det₄/per₄ formats.
22. **Spec Z and characteristic 2 for price certificates** (MAP_COMPLEXITY T8).
23. **Common sources and the nerve of a category of theories** (MAP_HOMOTOPY 1, HC-1).
24. **Shapes of pushouts of topoi and hole filling** (MAP_HOMOTOPY 2, HC-2): the profinite case with LM5 C.3.
25. **Constructible sheaves on M̄_{g,n} through exit categories** (MAP_HOMOTOPY 3).
26. **Exactness of colimits as a topos invariant** (MAP_HOMOTOPY 4, HC-3, D1).
27. **Integral cochain models in tame ranges** (MAP_HOMOTOPY 5).
28. **Finite categories and the S² question** (MAP_HOMOTOPY 6, D2).

---

## 7. Not to pursue

Overtaken, known, or dropped, with the evidence, so the conference does not redo them.

| Item | Why | Evidence |
|---|---|---|
| KTOWER / NIGHT_AFTER_ALPOGE K_{4k}(Z) = 0, k ≤ 20 (H18); H06a | Overtaken | Mok-Zheng hexagon:2611.00998; Pintar 2611.00829v3 |
| 67c outcome as new; GRH_ALGORITHMS P125/P126, P128/P131, P074, P092 outcomes; CX-N01-N04, N13 | Known before (the routes are new) | PF26 + Shoup |
| CX-N15 (factoring over F_q under M) | Overtaken | PF26 |
| BD-S23 (Calegari without the condition at 5) | Known before | Kharel-La Rosa-Wiese 2206.08116 Thm 1.2 |
| HODGE_DIVISION D-G34-01..07 (H19) | Known before | Severn 2610.00387v2 Thm A |
| BR-12302 (H08) | Known before | Richardson 1987 Lemma 5.1 |
| BR-AT-01 | Immediate from A | — |
| SN-C04 | Known in substance | Kleiman 1968 Th. 2.13 |
| MOONSHINE.004/005/009; the moonshine atlas's "new" rows | Known | unary theta series; Saias-Weingartner 2009, Nakamura-Pankowski 2016; standard CM identities (`OLDER_NOTES.md`) |
| GCT_GINEQ F-05 | Known before | Derksen 1308.3860 Cor. 1.10 |
| POLISH_CRISTAUX Paper 8 thm:sections | Known before | Riba 1903.04396 Cor. 4.1 |
| RESIDUE A.5 | Known before | OEIS A058129; Fiedorowicz 1984 |
| SA12 L6c (S12b); SA12 B.1 | Known before | Ishii-Yoshida 2410.15282v3 Cor. 1.4; Li-Wang 2604.23997 Cor. 4.6 |
| SA06 C.4i | Known in substance | Scavia-Suzuki Prop. 3.4; BdGF §3 |
| SA05/SA06 integral Weil-étale table of 15:173 | Known before | Flach-Morin 2018 §5.8.3 |
| SA05 F_p gerbe class (S05) | Known | Milne 2003 |
| SA20 B.016 | Known before | Jiang et al. 2605.25259v2 Thm 3.4; Ma 2604.05922 |
| SA22 local Hurewicz (S22b) | Known before | SGA 2 re-edition Exp. XIII §6 note (23); Hamm-Lê 1990 |
| SA09 B2.4 | Known | Schneps 1994 |
| CYCLOTOMIC_KERNEL D2, D5; SECTIONS_OVER_Q C.3 | Known in substance | Tsujimura 2022; Clark 2006 |
| SECTION_GHOSTS E.209-E.210 | Classical (label as known) | Shafarevich; Koch; NSW Ch. X |
| LM6 E.8, E.10; EXIT_TOWER E.60; LM4_FGA D.21; LM7_FERMAT_TOWER B.10 | Known or elementary (E.10 matters only as the correction of Steklov) | `TOPICALITY_LONGUE_MARCHE.md` |
| S15f (POLISH_CRISTAUX Paper 3) | Known in substance; an exposition | Ogus 1975; Katz-Messing |
| H30 (chain length in Alpöge's proof) | Not useful (the user, 23 Nov) | board |
| H27 (Connes's trace formula over Q ⟺ Dirichlet GRH) | A specialization of Connes 1999; no post (the user) | board; 68 update |
| H05 (RH for CM motives under Masullo) | Void: Masullo's draft is not a proof | the user, 22 Nov |
| ZH2 | Superseded by ZH3 (posted) | board |
| GPK08 | Absorbed in H02b | board |
| BR_PENCIL 43, GCT_OBS 44 as papers alone | Superseded inside the project by Codex's BORDER_RANK | `TOPICALITY_GCT_AG_DER.md` A.11 |
| October answers Q03; Q11 | Overtaken / known | Jansen 2611.09392; Srivastava, Yavari |
| H16 (tangential sections) as a paper | Partly Stix 2012; archive companion only | `OLDER_RUNS.md` B |
| Dérivateurs answers of 10-11 Nov, INDLOCAL, FINMON statement rows, LM1/LM3, sweeps 1-2 | Companion or archive material | `OLDER_RUNS.md` B |
| Masullo-defect prompts | Demoted by the user (22 Nov) | RUNBOOK |
| Asvin G.'s towers as a paper | A correction to his paper; route is the author | `OLDER_NOTES.md` item 3 |
| Weight barrier for L-meta-606/608; Kan-Thurston without small quotients; filtered = colimits of 1-types | Marginal or companion material | `OLDER_NOTES.md` |

---

## 8. Proposals for new prompts (for the main session to decide)

**Prompts already changed** (each report in `PROMPT_UPDATES/`; backups in `TO_SEND/PRO/_backups_20261125/`):
- 70d_HODGE_EFFECTIVE (geometry mapper, Claude Opus 5.5 at effort max): Q27's comparison half settled; Milne's framing; the
  main question moved to the real gate; THETA3 index 24; lints PASS.
- 95_GT_AFTER_H17 (Galois mapper, Claude Opus 5.5 at effort max): GT̂ inside GT̂₀ questions; H¹(Λ₀, F₂) computation; lints PASS.
- 94_THETA_CIRCUIT_SIZE (Codex's) and 96_FLEET_HARD_LINKS (a4348514, Claude Opus 5.5 at effort max): a way out removed in 94,
  the fleet's newer bounds and SPLIT_ZERO cp10 in 96; lints PASS.
- 05_FINMON_CP2_night, 29_SA32_Drivateurs, the four cote-105 working-through prompts 027, 081, 135, 189 (a34c0444, Claude Opus
  5.5 at effort max): Ben-Bassat as input; a rules correction; lints pass.
- F_Archive_working_through_200 and E small prompts 24, 32-37 (ae43bbdc, Claude Opus 5.5 at effort high).
- 28_SA30, 30_SA31, 31_SA28 and INTAKE_A/B/C (a7e00c63, Claude Opus 5.5 at effort high): "settled since" sections; `--lint`
  passes; `--lint-math` fails on six of them, as it did on their 19 Nov backups (the push rule is absent in these intake and
  notes prompts): the main session should decide whether that check applies.
- 68_CONNES_AFTER_RH: left unchanged (held), with a proposed 68 v2 (below).

**New-prompt proposals** (none built):

| # | Proposal | Main question | Source |
|---|---|---|---|
| 1 | KOIRAN_WITHOUT_GRH | Koiran's Theorem 1 with explicit x₀ from a uniform half-plane; HN, DIM_C, HNP, Schubert vanishing, GCT V transfers; Bürgisser's Cook vs Valiant under the half-plane. Or a Claude note after the check now done. | 68 update P1 |
| 2 | 68 v2 (CONNES_AFTER_RH) | The exact limit of Connes's cutoff defect as a sum over all zeros of the strip, with no hypothesis, for every primitive Dirichlet character; then over Q(ω) for Hecke characters with the off-line band from θ_G | 68 update §3 |
| 3 | FERMAT_SECTIONS_PAPER | Fermat for Selmer sections for every odd n with every step written; prosolvable, metabelian, pro-3 versions; LM6 B.15 for Y₁(N) | LM proposals §2.1 |
| 4 | GT0_GAP_PAPER | GT̂₀/⟨⟨GT̂⟩⟩ onto C₅ × C₇ × C₁₃ × C₂^ℕ with every step; is it abelian; the graded statement (may become part of 95) | LM proposals §2.2 |
| 5 | Claude note, not a prompt | LM4_SUCCESSOR C.29-C.31 (Lochak-Schneps Q1.1) | LM proposals §2.3 |
| 6 | RECONSTRUCTION_BEYOND_SUBPADIC | Pinned étale reconstruction over fields containing μ_∞; classify the fields of finite transcendence degree that reconstruct | LM proposals §2.4 |
| 7 | Tripod sections, the case left by GA-2 | A noncuspidal Selmer section locally cuspidal at a potentially multiplicative prime: is it the section of λ₀? First S = {2, 3}. The check part goes into INTAKE_A | 95 update |
| 8 | (FS)_nil successor | (FS)_nil at an irregular coefficient prime: ℓ = 37, r ≡ 31 (mod 36), obstruction group K₆₂(Z)₃₇ ≠ 0 | 95 update |
| 9 | CM once-punctured elliptic π₁ | The kernel field of the pro-p outer action of G_{Q(i)} on π₁(E₀ ∖ O) at Greenberg-type primes (Ishii's question, C.IHARA method) | MAP_GALOIS P4 |
| 10 | Component-local Anderson-Ihara | From K_{4m}(Z) = 0 (m ≤ 30), kernel equality on the sub-extension cut out by those components; belongs to NIGHT_AFTER_ALPOGE's unstarted Part C | 68 update P4 |
| 11 | Shapes of pushouts of profinite topoi | When the pushout of classifying topoi of profinite groups computes the shape; hole filling for étale π₁ | 05_FINMON update 1 |
| 12 | Nerve of admissible PD theories | Is B𝒜 contractible (A-CS, A-TL in the strongest form)? Into the next C.3 prompt if one waits | 05_FINMON update 2 |
| 13 | Exit categories of M̄_{g,n} | Forgetting a mark is not W_∞-smooth for every n ≥ 4; exit-category description where infima exist | 05_FINMON update 3 |
| 14 | FREX successor | A.3(iii) and the total version of C.4, with the topos dictionary and the Harman-Snowden gate | 05_FINMON update 4; DERIVATEURS.md |
| 15 | Cote 57:97-100, "noyau nul si n ≥ 4" | Universal point injectivity Pic(X)(k) → Pic(Y)(k) for smooth ample Y in dimension ≥ 4 (reduced to n = 4) | F_Archive update 1 |
| 16 | Cote 100:3 2) | Grothendieck's extension assertion for reduced bases with finite normalization | F_Archive update 2 |
| 17 | Cote 14:106-112 | Finish the C.3 local restriction table (C.3bl, C.3bt, C.3bu-bw) and the rational top quotient in characteristic 0 | F_Archive update 3 |
| 18 | POLISH_CRISTAUX shift law | A follow-up message to the running 92c merge thread: GE-3 stated exactly, with the v = 0 closure | 70d update proposal 1 |
| 19 | Cote 133 over orders | GE-4 beyond quadratic orders; a new prompt, or Part A′ of NIGHT_GROTHENDIECK_QUESTIONS' unstarted Parts B/C | 70d update proposal 2 |
| 20 | Coherent counting, second order | Does a_{p²} encode a further count (hardness at height ≥ 3)? | MAP_COMPLEXITY T4 |
| 21 | The char-2 hinge | Make the characteristic-2 square (permanent = determinant) a main question of a 99 successor; give 99's successor 98's SH-08 proof | MAP_COMPLEXITY T8, §5 |
| — | Folds, not prompts | NT-3 into the 67c v2; NT-4 into the next THETA3 or Paper A prompt; POLISH_CRISTAUX's GL₈ block via SA15's primitive-prime-divisor route into its successor | 68 update P2, P3; MAP_GEOMETRY 6 |

Also from MAP_COMPLEXITY §5, for the main session: our public pequalnp mirror (`extension/EXTERNAL.md`, "What we observe",
l.133-141) and `fleet_map/VPVNP_INTEGRATION_20261124.md` carry three bullets that runs 98 and 99 correct; a correction
commit is the main session's decision.

---

## Pending (marked for the final pass)

- **PROMPT_UPDATES:** the coordinator expects reports from four updaters; the list in section 8 is as of 24 Nov ~22:3x UTC.
  Reports may still land, and the proposals table must then be extended.
- **CHECK_HN_AM_20261124.md:** in; it confirms NK-1 (sections 2.1 C1 and 3).
- **v2 folders:** `67c_v2/` (framing to merge, build pending); `v2/2611.00939/` (H06b v2 drafted, not checked); H01 and H09 v2
  (sources fetched, no text yet); H17 v2 (a49aabbf, nothing on disk); P90a v3 (not started).
- **Runs still producing:** run 99 (VPVNP_WIRE_GEOMETRY, cp01), the 92c merge run (POLISH_CRISTAUX cp34 seen by MAP_GEOMETRY),
  COUNTING_VARIETIES (cp03), SPLIT_ZERO_AFTER_FGJM second run (cp10), BEYOND_DIRICHLET (cp10), MOONSHINE_AFTER_ALPOGE (cp01).
