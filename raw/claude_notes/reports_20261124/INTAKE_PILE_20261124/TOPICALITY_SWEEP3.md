# Topicality of the sweep-3 archive research runs (SWEEP3_A and SWEEP3_B)

Topicality pass of 24-25 Nov 2026, written by Claude Opus 5.5 at effort high, launched by the main session 329fb1e6
(Claude Opus 5.5 at effort max) under `TOPICALITY_BRIEF.md`. The runs themselves are by GPT-6 Astra (ChatGPT Pro mode); the
three polishing runs whose literature logs I used (POLISH_ALGEBRAIC_GEOMETRY cp35, POLISH_TOPOLOGY_PERIODS cp26,
POLISH_CRISTAUX final) are also GPT-6 Astra (ChatGPT Pro mode). Rows: `TOPICALITY_SWEEP3.tsv`. Running notes:
`<local>/Documents/agent_notes/20261124T2136Z_Topicality_sweep_3_NOTES.md`.

## How the searches were made

- **The window 13-24 Nov.** I ran a keyword scan (`scratchpad/topsweep3/scan.py`, 26 keyword groups, one or more per item)
  over the literature agent's full dumps:
  - 596 arXiv papers in math.AG, NT, AT, KT, CT and cs.CC;
  - 2,435 arXiv papers in 20 further categories (math.AC, CV, FA, GT, RA, LO among them);
  - all 600 Hexagon works to 24 Nov.

  Titles and abstracts were scanned. **No paper or Hexagon work of the window proves any item of either cluster.** The only
  hits are our own posts (2611.00936, 00937, 00939, 00940) and unrelated papers. Gap: arXiv after 23 Nov is not in the
  dumps. The AI laboratories' releases of the window are only VP ≠ VNP (LITERATURE_20261124.md §C), which bears on none of
  these items.
- **Older and classical literature.** The three polishing runs of 23-24 Nov had already searched most of these items with
  primary sources and hashes, in their `LITERATURE.md` files. I read the relevant sections and reopened the decisive sources
  myself where the verdict turns on them:
  - Ishii-Yoshida; Li-Wang; Scavia-Suzuki; Beckmann-de Gaay Fortman; Flach-Morin;
  - SGA 2 XIII §6; Stix (Nakamura's criterion); Elliott's MathOverflow edit;
  - Robert's EMS article; Yamagishi's survey;
  - the arXiv and journal records of Bhowmik-Pathak, Caradot-Lin, Jenča, Ma and Jiang et al.

  Where I relied on a polishing run's or an intake's reading without reopening the source, the row says so.
- **Hexagon status.** Taken from `field_experts/hexagon/HEXAGON_BOARD.tsv` (24 Nov 13:35) and the Hexagon dump. Both of our
  posts in these clusters (2611.00936 and 2611.00937) stand at version 2, published.

---

## 1. Items worth a paper now, ranked

1. **An excellent Dedekind domain on which Grothendieck's cd conjecture fails on every affine open** (RESEARCH_SA12
   A:A2-persistent-arithmetic-counterexample, with A:wild-affine-counterexample).
   - **What.** R is excellent, of characteristic 0, with 2 invertible and K = Frac R algebraic over Q. We have
     cd₂(K) = 1, while cd₂(U) = 2 and Pic(U)/2 is infinite for every nonempty affine open U. No residue field is
     orderable. The companion result: H³(Spec W(F̄₂)[[t]][1/t], F₂) ≠ 0.
   - **Why it still matters.** These are the first counterexamples to cote 31's conjectures (sheet 84) that avoid real
     residue fields. They answer the margin "égalité pour les ouverts assez petits ?" negatively, and the second answers
     the residual-characteristic question.
   - **Novelty evidence.** POLISH_ALGEBRAIC_GEOMETRY searched it (queries in its LITERATURE.md, 23 Nov) and found only
     neighbours:
     - Popescu, Math. Reports 24(74) (2022), §5, pp. 511-512: an eventually inert quadratic tower, with no class-group,
       Brauer or cd claim;
     - Claborn 1966, Thm 7: class-group realization only;
     - Guralnick-Jaffe-Raskind-Wiegand, Ex. 4.7: characteristic p;
     - Hexagon 2609.00105.

     My two web searches and the window scan found nothing. Still unopened: Hasse 1925, Schilling 1950 and Heitmann 1974,
     which Popescu cites.
   - **Where.** RESEARCH_SA12 `parts/A/quadratic_tower_A2_post05.tex`. It is already Paper 1 of POLISH_ALGEBRAIC_GEOMETRY
     (cp35 `workbench/papers/paper_01/`, Thms 1.1-1.2). Board row S12a.
2. **Jacobian summands of abelian surfaces and threefolds in every characteristic** (RESEARCH_SA06 C.4n, C.4p, C.4m).
   - **What.** s_J(A) divides gcd(2, δ(A)) for surfaces and gcd(6, δ(A)) for threefolds. Every ppav of dimension ≤ 5 has
     [2] factoring through a product of Jacobians, in all characteristics.
   - **Why it still matters.** Scavia-Suzuki (arXiv 2507.09821v2, Cor. 1.3) state that the direct-summand property for
     abelian varieties over F_q is open. Their Cor. 1.6 gets p^n only under the Tate conjecture for surfaces. These bounds
     are unconditional.
   - **What is not new.** Scavia-Suzuki Prop. 3.4, which I read, works over any field. Take θ with deg(θ^g/g!) prime to a
     set S of primes and θ^{g−1}/(g−1)! algebraic with Z_(S) coefficients. Then N_X factors through Jacobians with N prime
     to S. For g = 2 condition (ii) is automatic. Together with C.4i this already gives s_J | gcd(6, δ) for surfaces.
     - C.4i, s_J | (2g−1)!, is in substance Scavia-Suzuki Prop. 3.4 and Beckmann-de Gaay Fortman §3; the run derives it
       from them.
     - Over C, C.4m follows from Beauville's Pryms with Beckmann-de Gaay Fortman (arXiv 2202.05230, Thm 1.1, Thm 1.5).
   - **What is new.** The removal of 3 for surfaces; of 5 and of the excess 2-power for threefolds; and the char-2 Prym
     step. Engel-de Gaay Fortman-Schreieder (2512.04902, Dec 2025: the least algebraic multiple of the minimal class on a
     very general ppav 6-fold is 6) shows the field is active.
   - **Where.** `agents/frobenius/C4_additions.tex`, `C4_prym_addition.tex`, `C4_pt6_addition.tex`. Board S06b (stage W).
3. **A wild quasi-étale double cover over one smooth genus-two exceptional curve** (RESEARCH_SA12
   D:wild-genus2-single-curve, rows 433-435).
   - **What.** In characteristic 2 the surface b² + (t⁵ + t²a²)b + a⁵ = 0 has a cover that is étale off the point and
     wild along C: y² + y = x⁵, with C² = −1. So the graded-cone tameness theorem needs its formal-linearity hypothesis.
   - **Novelty evidence.** a3c8d7de's search: Artin 1975/1977, Lorenzini-Schröer, Ito-Schröer, Matsumoto,
     Carvajal-Rojas-Schwede-Tucker, Carvajal-Rojas-Stäbler, Hexagon. Cutkosky-Srinivasan 1993 was read at the source by
     the main session (prime-to-p results only). The window scan found nothing.
   - **Where.** `parts/B/D_wild_genus2_curve_B.tex`. Board S12d (stage W, a short note).
4. **Murre's announced locally quasi-finite representability criterion, proved with a corrected axiom 7** (RESEARCH_SA17
   A:pro7-representability, with A:main-counterexample).
   - **What.** The literal axioms of cote 131 sheet 13 admit P(B) = α_p(B^h_(t)), which is not representable. With the
     pro-modular axiom 7 the criterion holds over every locally noetherian base.
   - **Why it still matters.** Murre's Séminaire Bourbaki 294 (1965) p. 247 announces this analogue without statement or
     proof. The POLISH_ALGEBRAIC_GEOMETRY search found no later publication:
     - Alper's book shows that Mur95 is only the reprint;
     - Hall 2012/2013 and Hall-Rydh 2019 are different criteria;
     - 26 further queries are listed in its FRESH_P_H record.
   - **Gate.** An independent re-proof of the fpqc descent step (de Jong-Olander, JPAA 228 (2024), Thm 2, is the input).
   - **Where.** SA17 `sections/A_*`; POLISH_ALGEBRAIC_GEOMETRY `paper_03/representability.tex`.
5. **Grothendieck's admitted integral crystalline weak Lefschetz (cote 4, 8.3) fails in degree one** (RESEARCH_SA15
   prop:OC-product-integral-counterexample, on the SA14 A3 surface).
   - **What is known.** Zheng Thm 3.7; Mukai's iteration; and Cotner-Zavyalov (published 2024), Example 3.3.6 and
     footnote 4, which give flat-cohomology Lefschetz failures through Mukai and Totaro. The high-degree integral theorem is
     Bhatt-Morrow-Scholze Lemma 2.12.
   - **What is new.** No exact integral crystalline degree-one failure, and no saturation thresholds, were located
     (POLISH_CRISTAUX `audit/paper1/LITERATURE.md`).
   - **Where.** SA15 `sections/A_integral_counterexample.tex`; POLISH_CRISTAUX Paper 1. Board S15 (G1).
6. **The crystalline Dieudonné functor is not full over a reduced base** (RESEARCH_SA17 B:crystal-counterexamples).
   - **Known.** The non-reduced example over F_p[x,y]/(x,y)² is classical, per ac8bd2a2's note: Berthelot-Messing III
     4.4.1, Lau Rem. 3.4, Stacks 60.22.1. I did not reopen these.
   - **New.** The reduced (two-plane) example.
   - **Where.** A 7-page note is written: `reports_20261123/s17a_note/s17a_note.pdf`. Board S17a (stage W).
7. **Grothendieck's "transcendance forte" (cote 18:11) decided in corrected form** (RESEARCH_SA07 A.2.2-A.2.6, with C.1.5).
   - **What.** The v-invariant gives the full table of image dimensions, and five of his values fail unconditionally
     (h¹ of y² = x³ − x + 1).
   - **Known.** The ingredients are standard: Tannakian and orbit arguments, and the transported real Frobenius of
     Brown-Dupont, arXiv 1810.07682, Def. 2.6 / Prop. 2.9.
   - **New.** No assembled table was found (POLISH_TOPOLOGY_PERIODS Paper 3 classification).
   - **Where.** Board P91a: to be cut out as a short paper.
8. **The Hilbert-space trace formula proved in Grothendieck's hand** (RESEARCH_SA23 geo-H, cote 1 sheets 79-80 and
   111-112). The mathematics is Lidskii's theorem (1959), so this is a historical note.
   - **Why it still matters.** It contradicts the standard account. D. Robert, *On the traces of operators (from
     Grothendieck to Lidskii)*, EMS Newsletter, Sept. 2017, pp. 26-33, which I read, says Grothendieck "did not state the
     result explicitly" and "neither stated the result nor pursued the argument to the end".
   - **Gate.** Open the three printed sources: CR 1951 p. 1557, the 1955 memoir II-13 and the 1956 Erratum. Also open
     Pietsch, Quaestiones Math. 43 (2020).
   - **Where.** Board S23b (G1).
9. **The exact monodromy groups of H¹_et(C, F₂) over ordinary plane curves in characteristic 2** (RESEARCH_SA15
   thm:plane-char2-all-groups).
   - **Known.** The odd-degree obstruction, from Cais-Ellenberg-Zureick-Brown 2013 as the run cites it, and
     Castryck-Streng-Testa, AMC 8 (2014) 479-495; I opened its abstract, and it has no monodromy groups.
   - **New.** The groups in every degree: GL_g(F₂) for even d; the full stabilizer 2^{g−1}:GL_{g−1}(F₂) for odd d.
   - **Value.** Modest outside the archive; a short note.
10. **Metabelian local π₁ of normal surface singularities in characteristic p is finitely generated** (RESEARCH_SA14 F11).
    - **Novelty evidence.** No metabelian statement was found. Suzuki's nilpotent result (2207.01563) is the neighbour.
      The published Bright-Newton, Invent. 234 (2023), Thm 4.1 now replaces the Krishna-Majumder preprint input.
    - **Remaining gate.** Close the exact Kato-integrality dependency (CURRENT_GATES of POLISH_ALGEBRAIC_GEOMETRY), then
      write.

**Already published, no further paper needed:**
- SA14 A3, the very ample counterexample to Kodaira vanishing: hexagon:2611.00936, v2.
- SA20 B.022-B.024, Int(R) free for one-branch domains: hexagon:2611.00937, v2.

Both survive the week. The window holds no competing work; Ma 2604.05922 and Jiang et al. 2605.25259 have no newer
versions. For Int(R), the cusp case was announced by Elliott on MathOverflow 75202 (edit of 26 Dec 2013, read by me) without
a published proof, and v2 credits it.

**Not a paper now, but correction notes to authors (stage N):**
- Bhowmik-Pathak, Thm 1.11 (SA07 G.2.2). arXiv has only v1. The journal version, Acta Arith. 218 (2025) 1-23, has no
  erratum listed on the IMPAN page; its text is paywalled and not seen.
- Caradot-Lin, Prop. 3.10 (SA08 D-031, SA08_C3_D031 B-001). v4 of 20 Jun 2026 is still the latest version, with no journal
  reference.
- Chai, Chai-Oort and Partsch on the Igusa surface (SA14 D4), after an independent re-proof.
- Jenča, arXiv v1 Cor. 4.5 (SA21 A28), after checking the Order text.

## 2. Overtaken or known before

| Item | Verdict | Source (opened by me unless noted) |
|---|---|---|
| SA12 L6c, R¹f_*O_X = 0 | KNOWN BEFORE | Ishii-Yoshida, arXiv 2410.15282v3 (19 Apr 2025), Cor. 1.4: Y regular, X normal, φ proper birational of finite type, any characteristic |
| SA12 B.1, Pic^τ birational invariance | KNOWN BEFORE (as a consequence) | Li-Wang, arXiv 2604.23997, Cor. 4.6 (Nori and étale fundamental group schemes invariant for normal proper X to smooth Y over a perfect field), with Cartier duality and Moret-Bailly/Marrama purity (C. R. Math. 364 (2026) 431-435) |
| SA22 B:local-Hurewicz | KNOWN BEFORE | SGA 2 re-edition (math/0511279), Exp. XIII §6, Conj. A, printed pp. 155-156, editorial note (23): false by Hamm-Lê 1990, Ex. 3.1.3 (X = {z₁² + z₂³ + … + z_n³ = 0}, n ≥ 4), and true in modified form (their Thm 3.1.4). The run's cone over ΣRP² is one more counterexample. |
| SA05 prop:B-integral-errors and SA06 E.4b/E.4g (the Z/2 in 15:173) | KNOWN BEFORE | Flach-Morin, Doc. Math. 23 (2018), §5.8.3: H^i_W(Spec Z̄, Z(1)) is 0, 0, O^×, Cl, Z, 0 and Z(0) is 0, Z, 0, …, (O^×_tor)^D, 0; so for Q, H¹(Z(1)) = Z/2 and H³(Z(0)) = Z/2. It is a correction of Grothendieck's table only. |
| SA05 A:class / A:hasse (the F_p gerbe class) | KNOWN BEFORE | Milne, Gerbes and abelian motives (2003), per the POLISH_ALGEBRAIC_GEOMETRY cp12 intake and the run's withdrawal of its Paper 6; not reopened by me |
| SA06 C.4i, s_J divides (2g−1)! | KNOWN BEFORE (in substance) | Scavia-Suzuki Prop. 3.4 and Beckmann-de Gaay Fortman §3; the run's own derivation cites them |
| SA20 B.016 (two-branch failure) | KNOWN BEFORE | Jiang et al., arXiv 2605.25259v2, Thm 3.4 (failure of the multiplication tensor for the semilocal two-branch F₂ domain, as read by POLISH_TOPOLOGY_PERIODS), and Ma 2604.05922 (non-flatness) |
| SA09 B2.4 | KNOWN BEFORE | Schneps 1994 (the run confirms it) |

Partly covered, with what remains new:
- **SA12 A:canonical-Iwasawa.** The core is Iwasawa's theorem: G_S(k_∞)(p) is free iff μ = 0 (Iwasawa 1973, Thm 2, as
  recalled in Yamagishi, RIMS Kôkyûroku 884 (1994), intro (4); NSW Thm 11.3.7, cited by the run). New is only the
  translation to étale cd with arbitrary constructible sheaves.
- **SA06 C.3be.** The surface case is Artin's, Tanaka 2014 Thm 4.5, and Esser, PAMS 151 (2023) Thm 2.4 (cited by the run).
- **SA14 G1.** The positive half is Poonen-Rains, MRL 18 (2011), Prop. 3.12(f); the principal case is Fringuelli-Pirisi,
  MMJ 68 (2019), Thm C; Laga 2510.24678 lists d₂ even as known.
- **SA21 A27/A06.** The bounded case is Jenča, Order 40 (2023) 575-588.
- **SA23 EGA errata.** The III 4.3.6 and IV 20.1.3 counterexamples are published (EGA III/2 errata; Kleiman 1979), per the
  POLISH_ALGEBRAIC_GEOMETRY cp12 intake.
- **SA12 D:boundary-neighborhood.** The projective case is Drinfeld, Lemma C.2, and Esnault-Kindler, Prop. 6.2.
- **SA07 A.4.21.** It applies Howe, JTNB, Thm 1.2 / Rem. 1.3.
- **SA15 C-RD.** It comes after Ferrand-Raynaud and Olberding.
- **SA22 A2-explicit-limits.** Classical Jenkins-Strebel (Liu 2008).

## 3. Not settled

Each is listed with what would decide it:
- **SA14 C2.G (Pic(X) = Pic(X̂) when H¹(O_X) has finite length).** Not searched. Decide by checking Artin's approximation
  papers (1969) and SGA 2 XII for the statement.
- **SA14 E4.\*.** Only the full-Picard schematicity statement has a located prior (Achter-Casalaina-Martin, §1.7.2). Decide
  by checking Kleiman's *The Picard scheme* for E4.N/R/S/T.
- **SA15 thm:all-X-explicit-positive-rank.** Decide by reading Illusie 1990 (*Ordinarité des intersections complètes
  générales*), Ekedahl, and later generic-ordinarity papers.
- **SA06 C.3ap/C.3ak (local restriction table).** STILL NEW only provisionally: one web search, and rows read in part.
- **SA08 A-026 (no filtered numerical lift).** STILL NEW provisionally: Horel, Kubrak-Shuklin-Zakharov and Antieau were
  found by search, but not read in full.
- **SA07 F.3.32.** Nakamura's criterion (Stix 0809.0017, Thm 20, which I read) needs a cyclotomically normalized subgroup;
  F.3.32 assumes only an open normalizer. Decide by checking Tamagawa 1997, Mochizuki, and the
  Nakamura-Tamagawa-Mochizuki survey for the open-normalizer form.
- **SA22 A:04 and single-cap.** Provisionally new; the remaining gate is the comparison with the grafting literature (Gupta,
  Dumas, Scannell-Wolf).
- **SA17 C:BO_affine_lambda.** Needs a literature search with exact locators.
- **SA20 D.002 (Coxeter normalizer).** Decide against Curtis-Wiederhold-Williams 1974 and Adams-He on lifting Weyl-group
  elements.

## 4. Every item

### SWEEP3_A

| Run | Item | Verdict | Worth a paper now? | Hexagon |
|---|---|---|---|---|
| SA12 | A:A2-persistent-arithmetic-counterexample | STILL NEW (provisional; Popescu 2022 precursor) | yes (§1.1) | S12a, W |
| SA12 | A:canonical-Iwasawa | PARTLY (Iwasawa 1973 / NSW 11.3.7) | no: a section of Paper 1 | none |
| SA12 | D:wild-genus2-single-curve | STILL NEW (provisional) | yes (§1.3) | S12d, W |
| SA12 | L6c | KNOWN BEFORE (Ishii-Yoshida Cor. 1.4) | no | S12b, X |
| SA12 | B.1 | KNOWN BEFORE (Li-Wang Cor. 4.6 + purity) | no | S12b, X |
| SA12 | B.2u | UNSETTLED (not searched) | no | S12c, G2 |
| SA12 | A:wild-affine-counterexample | STILL NEW (provisional; conditional on Suzuki's locators) | with §1.1 | in Paper 1 |
| SA12 | A:Dedekind-Milnor-criterion | UNSETTLED (not searched) | no | none |
| SA12 | D:boundary-neighborhood | PARTLY (Drinfeld; Esnault-Kindler) | no: a section of Paper 1 | S12c, G2 |
| SA12 | D:fixed-boundary-gate | open problem, not a result | no | none |
| SA12 | C:literal-141 | archive reading, not assessed | no | none |
| SA06 | C.4n | PARTLY (Scavia-Suzuki Prop. 3.4 gives gcd(6, δ)) | yes (§1.2) | S06b, W |
| SA06 | C.4p | PARTLY (as above; new: 5 and 4 removed) | yes (§1.2) | S06b, W |
| SA06 | C.4i | KNOWN BEFORE (in substance) | no | S06b |
| SA06 | C.4m | PARTLY (C known; new in char p) | inside §1.2 | S06b |
| SA06 | C.3ap / C.3ak | STILL NEW (provisional) | not yet | S06, G2 |
| SA06 | C.3be | PARTLY (Artin; Tanaka; Esser) | no | none |
| SA06 | C.1f / C.1j / C.1k | STILL NEW (archive; provisional) | archive companion | S06, G2 |
| SA06 | E.3e / E.3u | UNSETTLED (not searched) | no | none |
| SA06 | E.4b / E.4g | KNOWN BEFORE (Flach-Morin §5.8.3) | no: archive note | none |
| SA06 | D.3b | UNSETTLED: probably within Milne 2003; open Milne to decide | no | none |
| SA06 | A.5c | not assessed (marginal, unranked) | no | none |
| SA07 | G.2.2 | STILL NEW (erratum) | no: note to the authors | S07, N |
| SA07 | F.3.32 | STILL NEW (provisional) | no: route to the LM expert | S07c, G1 |
| SA07 | A.2.2 / A.2.6 | PARTLY (standard ingredients; Brown-Dupont) | yes (§1.7) | P91a |
| SA07 | C.1.5 | STILL NEW (provisional; Totaro + Yoshinaga synthesis) | inside §1.7 | S07b, G1 |
| SA07 | D.5.2 | PARTLY (classical CM reciprocity, explicit example) | no | none |
| SA07 | E.1.2 | not assessed | no | none |
| SA07 | A.4.21 | PARTLY (Howe JTNB) | no | none |
| SA07 | A.3 / A.4c | open problems | no | none |
| SA08 | A-026 | STILL NEW (provisional) | no: archive companion, cote 136 | none |
| SA08 | D-031 | STILL NEW (erratum to Caradot-Lin v4) | no: note to the authors | none |
| SA08 | D006 / D006E | not assessed | no | none |
| SA08 | C17 / C.3 | open over Z | no | none |
| SA08_C3_D031 | B-001 | as D-031 | no | none |
| SA08_C3_D031 | A-S09-09..12 | not assessed (rests on Fu-Nuiten Thm C) | no | none |
| SA08_C3_D031 | A-CS / A-TL | open | no | none |
| SA09 | A1.3 / A1.7 | not assessed | no | none |
| SA09 | A3.4 | not assessed | no | none |
| SA09 | B3.1 | UNSETTLED (not searched) | no | none |
| SA09 | B2.4 | KNOWN BEFORE (Schneps 1994) | no | none |
| SA10 | A1.2 / A1.3 | STILL NEW (archive correction; elementary descent) | no: companion, cote 151 | none |
| SA10 | B2.2 | PARTLY (∞-topos van Kampen known) | no | none |
| SA10 | B6.1 | archive correction | no | none |
| SA10 | A4.3 / A4.5 | archive; agrees with EXIT_TOWER A.2 | no | none |
| SA10 | C5.08 | archive | no | none |
| SA05 | A:class / A:hasse | KNOWN BEFORE (Milne 2003, per POLISH_ALGEBRAIC_GEOMETRY) | no | S05, X |
| SA05 | prop:B-integral-errors | KNOWN BEFORE (Flach-Morin) | no | none |
| SA05 | prop:B-continuity | not assessed | no | none |
| SA05 | c:general-level-bound | archive, not assessed | no | none |
| SA05 | prop:B-diagonal-Chow-gate | conditional reduction, not assessed | no | none |
| SA05 | A:2026-abelian etc. | not assessed (rests on unrefereed 2026 preprints) | no | none |

### SWEEP3_B

| Run | Item | Verdict | Worth a paper now? | Hexagon |
|---|---|---|---|---|
| SA14 | A3 | STILL NEW | done | posted 2611.00936 v2 (P90a) |
| SA14 | D4o / D4s / D4a / D4b | STILL NEW (corrections to Chai, Chai-Oort, Partsch; supersingular case uncertified) | no: author notes | P90b, on hold |
| SA14 | G1 | PARTLY (Poonen-Rains 3.12(f); Fringuelli-Pirisi) | no | S14b, G1 |
| SA14 | F11 | STILL NEW (provisional) | yes, after the gate (§1.10) | S14b, G1 |
| SA14 | J1-Th5 (J5) | STILL NEW (archive: unpublished statement) | archive companion with H04/H11 | S14a, G1 |
| SA14 | J2a / J2b / J6C / J1-Th7 | STILL NEW (archive) | archive companion | S14a, G1 |
| SA14 | E4.N / R / S / H / T | UNSETTLED | no | none |
| SA14 | C2.G / C2.D | UNSETTLED | no | none |
| SA14 | H1 / I8 | UNSETTLED (not searched) | no | none |
| SA14 | A1 / A2 / SA14-H4 | open problem | no | none |
| SA15 | thm:plane-char2-all-groups | PARTLY (obstruction: CEZB 2013, CST 2014) | yes, short note (§1.9) | S15b, G1 |
| SA15 | prop:OC-product-integral-counterexample | PARTLY (Cotner-Zavyalov Ex. 3.3.6; Zheng; BMS) | yes (§1.5) | S15, G1 |
| SA15 | thm:all-X-explicit-positive-rank | UNSETTLED (Illusie 1990; Ekedahl) | not yet | S15d, G2 |
| SA15 | A2-EXACT / A2-UNIT | not assessed | no | none |
| SA15 | B-RD indices | not assessed (carried on in POLISH_CRISTAUX Paper 2) | no | S15h |
| SA15 | C-RD11 / C-RD4 / C-RD1 | PARTLY (Ferrand-Raynaud; Olberding) | no | S15e, G1 |
| SA17 | A:main-counterexample / A:pro7-representability | STILL NEW (provisional; Murre 1965 announcement) | yes (§1.4) | none |
| SA17 | B:crystal-counterexamples | PARTLY (non-reduced classical; reduced new) | yes, note written (§1.6) | S17a, W |
| SA17 | C:BO_affine_lambda etc. | UNSETTLED | no | S17b, W |
| SA17 | A4 (cote 128) | not assessed | no | none |
| SA20 | B.022 / B.023 / B.024 | PARTLY (Elliott's 2013 announcement for the cusp; proofs and the general case ours) | done | posted 2611.00937 v2 (S20) |
| SA20 | B.016 | KNOWN BEFORE (Jiang et al. Thm 3.4; Ma) | no | none |
| SA20 | A.104 / A.106 / A.111 / A.112 / A.101 | PARTLY (consequences of established concordance theory, per POLISH_TOPOLOGY_PERIODS) | no | none |
| SA20 | A.701 / A.703 | not assessed | no | none |
| SA20 | A.159 / A.160 | not assessed (partly open) | no | none |
| SA20 | D.002 / D.005 / D.021 / D.025 | UNSETTLED | no | none |
| SA21 | A27 / A27a / A26 | PARTLY (Jenča 2023, bounded case) | no | none |
| SA21 | A06 / A04 | PARTLY (Jenča 2023) | no | none |
| SA21 | A28 | STILL NEW (erratum to Jenča v1) | no: note after checking Order | none |
| SA21 | A14a | not assessed | no | none |
| SA21 | C08 / C06 | UNSETTLED (Björner 1984 unopened); C12 known (McCord) | no | none |
| SA21 | B-prime / B-M3 / B-Sigma | archive, not assessed | no | none |
| SA22 + run2 | A1-global-refutation / A:04 / A:04-exact-image | STILL NEW (provisional; elementary via Koebe) | archive note / Paper 4 | S22a, W |
| SA22 run2 | A:single-cap-all-lengths | STILL NEW (provisional) | not yet (grafting comparison) | P91b, G1 |
| SA22 | A2-explicit-limits | PARTLY (Jenkins-Strebel) | no | none |
| SA22 | 67/091 counterexample | internal correction | no | none |
| SA22 run2 | C:subject21-torsion-counterexample | UNSETTLED | no | S22c, G2 |
| SA22 run2 | B:local-Hurewicz | KNOWN BEFORE (SGA 2 XIII N.D.E. 23; Hamm-Lê 1990) | no | S22b, G2 (should go to X) |
| SA23 | geo-H-lidskii / geo-H-history | STILL NEW (archival; the mathematics is Lidskii 1959) | yes, historical note (§1.8) | S23b, G1 |
| SA23 | geo-H-determinant / continuity | PARTLY (extends Hochs-Kaad-Schemaitat 2018) | no | none |
| SA23 | EGA errata | PARTLY (III 4.3.6, IV 20.1.3 published) | no: edition errata | S23a, G2 |
| SA23 | A-16 | UNSETTLED | no | none |
| SA23 | cat:J8 | not assessed | no | none |

"Not assessed" marks marginal items that neither cluster file ranks among its most interesting. They are outside the
brief.

## 5. Corrections for the board

- **S22b** (local Hurewicz) should move to stage X. SGA 2's own editorial note 23 records the refutation (Hamm-Lê 1990),
  so the open gate "check the quotation against SGA 2's text" is closed.
- **S06b** should state which parts are new. The prime-to-δ part follows from Scavia-Suzuki Prop. 3.4, and C.4i is theirs
  in substance. The new content is the 3-part for surfaces, the 5- and 4-parts for threefolds, and characteristic 2.
- **S23b** should note that the archival finding contradicts Robert's EMS Newsletter account (2017).
