# The HODGE cluster: Hodge classes, algebraic cycles, positivity

By Claude Opus 5.5 at effort high, a cluster reader of the intake pile of 24-25 Nov 2026, launched by the main session
329fb1e6 (Claude Opus 5.5 at effort max). Runs: HODGE_SIGN (prompt 32), HODGE_DIVISION (46, with 46b), C44_POS (51),
HODGE_BOUNDED_CYCLES (70) and HODGE_FINISH (70c). Every run is GPT-6 Astra (ChatGPT Pro mode); the runs record their
effort as "not exposed".

- **Check events of this pile:** `INTAKE_<RUN>_20261124_CHECK_EVENTS.tsv` beside this file.
- **Items:** `HODGE_ITEMS.tsv`.
- **Work file:** `agent_notes\20261124T2111Z_Intake_pile_Hodge_cluster_NOTES.md`.

**State of the pile.** Every newest return of the five runs has already had an intake, in
`field_experts\intake_20261121\intakes\<RUN>\`, each with a PRIMER of 23 Nov. No return newer than those intakes exists in
`research_returns`. (`INTAKE_LEDGER.md` still marks all five "not taken in", which is stale.) What is new here:
- six spot checks;
- one status disagreement between two of our records (H19 against Paper A's Q28);
- one removable hypothesis in Paper A (André–Oort);
- the ranking below.

## The cluster's most interesting items, by usefulness

1. **A sign-only proof of Deligne's weight bound (HODGE_SIGN SG-08 to SG-11).**
   - *Statement:* for X over F_q and F pointwise of weight ≤ w, every Frobenius eigenvalue on H_c^i(X, F) has weight
     ≤ w + i. With duality this gives purity for smooth proper X.
   - *The idea:* after one global sign (−1)^{D−1}, the remainder qN − M^k of a generic hyperplane section of a path form
     on U^k is the class of an actual module. That module is the Gysin kernel K_k plus H_c^d(U)^{⊗k}. Effective power
     sums and tensor amplification then finish.
   - *Why it matters:* a few-page proof of the central theorem of Weil I/II, with no monodromy, no Rankin–Selberg and no
     Hodge standard conjecture.
   - *In Grothendieck's terms:* K_k is his evanescent E^{n−1} = Ker φ (cote 16, scans 034 and 036).
   - *Checked by:* the intake (Claude Opus 5.5 at effort high); an independent re-proof by Claude Fable 5.2 at effort max
     (a3ccbc11); this pile re-derived SG-08 once more.
   - *Where:* published as hexagon:2611.00789 (v5, `reports_20261120\deligne_sign_only_paper\deligne_sign_only_v5.tex`).
     **Done; nothing to decide.**
2. **All the standard conjectures and Tate on every power of explicit non-abelian fourfolds in characteristic p (C44_POS
   A13, A28, A30, A30a, A42b; Hexagon H26).**
   - *The varieties:* axes B of Lefschetz pencils of |tH| on E⁶, with E: y² = x³ − x, through Y = E² × {o}⁴.
   - *The result:* on a Zariski-dense set of closed points, B^N satisfies the Hodge standard conjecture for product
     polarizations, Lefschetz type, D, and Tate in every codimension.
   - *The source of positivity:* a generic Frobenius torus (Chin) makes the algebraic classes pair tensors of Frobenius
     graphs. Their Gram form is Tr(a ā) on a product of CM fields, positive by Weil's RH alone.
   - *Why it matters:* unconditional cases of the standard conjectures beyond abelian varieties are rare, and here the
     positivity does not come from lifting to characteristic 0.
   - *Checked by:* targeted proof check by the intake (a8d75352). This pile independently re-derived the positivity
     mechanism, including why the sign of the form on W never enters (it appears squared).
   - *Unrefereed inputs:* none.
   - *Gates:* the hypotheses of Chin's Th. 5.7 and the ambient block by a second reader; a literature search; a written
     paper. The paper prompt 64 was folded into sent prompt 76, whose cp13 lists the C44 row "NOT YET ACTIVE".
3. **The Hodge conjecture for abelian varieties as a uniform degree bound over finite fields, with an explicit Weil
   engine (HODGE_FINISH Paper A; H25).**
   - *The equivalence (Q01):* published inputs only; the CM Hodge manuscripts are not inputs.
   - *The engine:*
     - quadratic extraction (Q02): one detector gives the whole Weil plane;
     - detectors of degree 48, 192 and 36 on principal Gaussian and Eisenstein fourfolds (Q03);
     - stabilization from 2n + 2 to every determinant in 2n (Q04);
     - one principal family per field and dimension (Q10);
     - an exact Ext² test for semiregularity (Q12).
   - *Why it matters:* it turns "is this Hodge class algebraic" into a bounded search with explicit constants. The
     equivalence itself is close to standard (Baire, Hilbert schemes, spreading out); its novelty is bounded by
     Cattani–Deligne–Kaplan p. 483 and Bhattacharjee–Bhattacharya, both cited. The explicit numbers are the run's own.
   - *Checked by:*
     - targeted checks of Q01–Q04, Q10, Q12 and Q24 (abcaba9b and its copy aaf69461);
     - a non-blind independent re-proof of Q01 with one repair (a8d75352);
     - no blind check.
   - *Gates:* Schoen 2007 for the 36; the page view; a literature search for Q12.
4. **A Severn-free proof for split Eisenstein eightfolds (HODGE_DIVISION run A, D-G34-01 to 07; H19).**
   - *What it proves:* from Severn's numerical data, checked by an exact certificate, and published inputs only (Davis,
     Dettweiler–Wewers, Schmid, Schoen, Brauer, Milne), the run proves:
     - the G₃₄ Hurwitz family has period rank 16;
     - Schoen's exceptional-divisor step is repaired;
     - the Weil lines are algebraic;
     - with an explicit, astronomically large D₈(Δ).
   - *Checked by:* this pile read D-G34-03 to 06 (the open H19 gate) and found no fault.
   - **The two records disagree:** HODGE_FINISH Paper A (Q28) cites Severn for the same geometric input and calls its
     bound conditional (Problems, below).
5. **A coniveau-one criterion for Mumford's exceptional classes (HODGE_FINISH Paper B, Q29).**
   - *Statement:* a nonzero coniveau-one part of an explicit rank-16 level-one summand P ⊂ H³ of a split Weil sixfold
     gives the rational Hodge conjecture on every power of the Hodge-generic Mumford fourfold.
   - *Why it matters:* it reduces Mumford's exceptional classes to one instance of the generalized Hodge conjecture.
   - *Checked by:* targeted proof check in this pile, no fault. The premise is open (Q08).
6. **Grothendieck's cote 44 Th. 5 fails as displayed, and its correction (HODGE_SIGN AR-01; C44_POS T05; H04 with S14a's
   J5).**
   - *The counterexample:* on P²×P², the flag-threefold pencil gives a missing term of one unit per nodal fibre.
   - *The correction:* C44-T05 assembles it; A42b gives it with sign on whole groups for powers of an elliptic curve.
   - *Why it matters:* the archive companion's main correction to the 1964 programme. It is complete; the gate is the
     scan-004 image check.
7. **The Galois-orbit and flat-detector criteria (Paper A, Q27).**
   - *Statement:* a relative-Weyl special point with a degree-D detector and a Galois orbit larger than B_S(H(D)) forces
     detectors on the whole family; one flat detector, even in characteristic p, does the same.
   - *Checked by:* this pile (both propositions), no fault. The paper's hypothesis "André–Oort for powers of S" is a
     theorem for abelian type, so it can be dropped.
   - *Why it matters:* it is the base of the unsent prompt 70d (Alpöge plus H15). The effective gate is B_S and H(D),
     not the orbit size (Relations, HODGE_FINISH).

## HODGE_SIGN (prompt 32)

**Return:** `research_returns\HODGE_SIGN_final_20261121T0057Z_unzipped\HODGE_SIGN.tex`. A 42-minute run on 21 Nov.
**Prompt:** `TO_SEND\PRO\1_Archive_research_by_topic\SENT\32_HODGE_SIGN_...`. **Earlier intake:**
`field_experts\intake_20261121\intakes\HODGE_SIGN\` (INTAKE, CHECK_EVENTS, PRIMER).

1. **Useful.** It gives a new short proof of Deligne's bound and precise archive corrections. Its main result is
   published (H01).
2. **What it proved.**
   - **SG-08 (effective Gysin remainder).**
     - *Hypotheses:* U/F_q smooth affine of pure dimension d ≥ 1; F lisse; X = U^k, D = kd; Y ⊂ X a smooth affine
       hypersurface with restriction H^a(X, F_k^∨) → H^a(Y, ·) bijective for a < D − 1 and injective for a = D − 1.
     - *Conclusion:* (−1)^{D−1}(q^n N_{k,n} − M_n^k) = Tr(F^n | H_c^d(U,F)^{⊗k}) + Tr(F^n | K_k), with
       K_k = ker(H_c^{D−1}(Y)(−1) → H_c^{D+1}(X)).
   - **SG-09:** the affine middle-degree bound, via Katz ACT (JAMS 6, 1993), Appendix A.3–A.5 on the graph immersion.
   - **SG-10 and SG-11:** smooth proper purity, and the weight bound for H_c.
   - **HS-01 to HS-03:** the analytic lemmas.
   - **HS-04 and HS-05:** counterexamples showing that genericity and the sign are needed.
   - **SG-01:** the sign is an effectivity sign in K₀, not the Hodge-index sign; the identification is refuted.
   - **AR-01:** cote 44 Th. 5 fails as displayed.
   - **Q3-04:** the corrected cote 34 scan 064.
   - **SL-04 to SL-09:** the Lefschetz sl₂ against the Arthur SL₂.
   - **Checks:** 29 targeted proof checks by the intake (Claude Opus 5.5 at effort high, 21 Nov); an independent
     re-proof of HS-01 to SG-11 by Claude Fable 5.2 at effort max (a3ccbc11,
     `reports_20261120\deligne_sign_only_check\CHECK_a3ccbc11_20261121.md`: no gap; one citation route for SG-09 fixed in
     v5); this pile re-derived the SG-08 identity.
3. **New since the last intake.** No new return. This pile adds the third reading of SG-08. The v5 paper adopts the
   corrected SG-09 citation (v5 lines 328–347, 512–515).
4. **Open.**
   - U-01: trace data alone cannot give scan 049's positivity (SIGN_NEXT SN-14).
   - U-02: CM positivity, conditional on 032.
   - U-04 and U-05: an integral sl₂ intertwiner on Grothendieck's exterior model (Φ₀ on ΛM₀).
   - Cote 16, scans 049–050: conditions C, A and I(X×X), in general.
5. **Relations.**
   - *Our runs:* it supplies hypothesis (S2) of GCT_NSRH F03/F04/F17. It continues into SIGN_NEXT and JAC1964 (the
     per-fibre term of AR-01: SN-44-01, H9-T1) and C44_POS (T05).
   - *Literature:* Alpöge's footnote 3 (the idea); Katz ACT Cor. 3.4.1, p. 181, and Appendix A; Weil I 1.6;
     Weil II 3.3.1; SGA 4 XIV 3.1.
   - *Grothendieck:* weights, and the hyperplane induction of cote 16, scans 034–040, without the C/A/I route of scans
     049–050.
6. **Candidates.** None new. H01 is posted; H04 waits on the scan-004 image check. A v2 of H01 is listed on the board
   (F50, SN-14, AM-S1–S3).
7. **Problems.** None found in the mathematics. SG-04 ("H^{r,r}(E^n) spanned by products of (1,1) classes") rests on
   classical results quoted from memory (Tate, Murasaki, Imai): open a source before it is used in print.

## C44_POS (prompt 51)

**Return:** `research_returns\C44_POS_final_20261122T1020Z_unzipped\C44_POS.tex` (398 pp.). It ran 21 Nov 23:13 to
22 Nov 10:20 UTC and stopped by two reviews without movement. **Earlier intake:** `...\intakes\C44_POS\` (a8d75352) and
the seed `reports_20261122\paper_seeds\SEED_C44_POS.md`.

1. **Useful.** It gives unconditional instances of all the standard conjectures and Tate on all powers of non-abelian
   varieties in characteristic p. It locates the obstacle to the general fixed-axis sign exactly.
2. **What it proved.**
   - **C44-A13.**
     - *Setting:* A = E⁶, E: y² = x³ − x, H = Σh_i, Y = E² × {o}⁴.
     - *Statement:* for t large, the axes B_u = D₀ ∩ D_u in |tH| are smooth axes of Lefschetz pencils containing Y.
       For infinitely many p ≡ 3 (mod 4), a Zariski-dense set of closed points over F̄_p has A_B = Qw, with
       w = [Y]_B − t^{−2}κ*α₀ and ∫w² = 6t² − 1/(4t²).
     - *Ranks:* V has rank 3600t⁶ − 165; W = V ⊖ Qw has rank 3600t⁶ − 166. The variable h^{4,0} is 62t⁶ − 5 > 0.
   - **C44-A28 and C44-A30.** On a dense set of these axes, for every N, every ℓ ≠ p and every product polarization:
     - the Hodge standard conjecture on B^N;
     - Lefschetz type and D;
     - Tate in every codimension over every finite extension;
     - Frobenius semisimple;
     - a positive adjoint trace on degree-zero correspondences (cote 16, scan 049).
   - **A30a:** every rational ample class on B, by Ancona's fourfold signature argument (Invent. Math. 223, 2021,
     Prop. 3.15).
   - **A42b, with JAC1964 H9-T7 and JAC-P07:** for X a power of one elliptic curve, with positive axis form, the signed
     height on CH^m(Y)_hom ⊗ Q is positive semidefinite with radical H₀.
   - **A14:** a smooth determinantal surface S ⊂ E⁴ (p ≡ 3 mod 4) that does not lift to characteristic 0.
   - **A29, A31s, A31t:** positive classes with w² > 0 that lift to no model of ramification e ≤ 5 (p = 3), or
     e ≤ 3p (p ≥ 7).
   - **T05:** the consolidated corrected Th. 5.
   - **W05:** Theorem W in characteristic p needs balance of the p-divisible group.
   - **W12:** deg(Z·Z′) ≤ deg(h^rZ)·deg(h^{g−r}Z′)/(r!(g−r)!χ(L)), sharp.
   - **Conditional on 032 and Milne's report:** JAC-T4.3 and W06–W11.
   - **Checks:**
     - targeted proof checks by the intake (a8d75352) of A01, A05, A06, A12, A13, A14, A18, A28, A30, A30a, A42b, T05 and
       W05, with its own recomputations;
     - the run's 793 check events are same-model;
     - this pile: an independent re-derivation of A28(2) and of the A30 core.
3. **New since the last intake.** No new return. This pile adds:
   - the re-derivation above;
   - the parity check: V is odd and W even, so a root-of-unity-free orthogonal Frobenius on W is possible;
   - the prompt state: prompt 64 was superseded inside sent 76, NIGHT_GROTHENDIECK_QUESTIONS, whose cp13 (24 Nov 00:37)
     holds the row "C44-positivity … NOT YET ACTIVE".
4. **Open.**
   - **QH9-axis, the fixed-axis sign in general.** Gate: axes with a small Frobenius torus. Untried routes:
     - supersingular specialization of the ambient;
     - a uniform A06;
     - moving along the class's locus;
     - smaller tori.
   - **QH9-axis-lift:** ramification above the bounds, and two unproved steps of the final section.
   - **QH9-cover-primitivep;** **QFermat-AJ at F07;** **QScan050;** **QT4-abeliantype;** **QT4-specialCI.**
5. **Relations.**
   - *Our runs:* it continues JAC1964 and SIGN_NEXT; it absorbs SA14/SA19's J5, J2a, J2b and J6C at their scopes.
   - *Literature:*
     - Chin, JAMS 17 (2004), Th. 5.7;
     - Milne, Ann. of Math. 155 (2002), Rem. 3.7–3.8;
     - Ancona 2021, Prop. 3.15;
     - Entin, IMRN 2021, Th. 3;
     - SGA 7 XIX 3.4; Weil II 4.4.1; SGA 1 XIII 2.9–2.12;
     - Shimada (Hermitian Fermat varieties; this is why core 51's Fermat candidate already has I).
   - *Grothendieck:* cote 44 (the 1964 programme, Th. 4 and Th. 5); cote 16, scans 048–050 (conditions C, A, I; the
     positive adjoint trace of scan 049); motives and correspondences (the algebraic projectors A28.7–A28.9); weights
     (the Frobenius torus).
6. **Candidates.**
   - **A Hexagon note (H26):** "Hodge type on all powers of fourfold axes" (A13, A28, A30, A30a, A42b). It needs a
     second reader for Chin's hypotheses and the ambient block, and a literature search. The generic-Frobenius
     mechanism resembles Milne's Lefschetz-class and Tate-for-powers arguments; look there first.
   - **A next prompt:** a check of the chain A22–A31r, and a written proof of INT-C44-2. Both are listed in the seed and
     not yet scheduled.
7. **Problems.**
   - INT-C44-2 and INT-C44-3 are intake deductions, self-checked only. INT-C44-3 quotes Ancona from memory.
   - The chain A22–A31r behind non-liftability is unread by anyone but the run.
   - Three third-party extracted texts sit in `work\arithmetic\` (`ent2022_issue.txt`, `geisser_hasse_2019.txt`,
     `shioda_katsura1979.txt`): never to GitHub.

## HODGE_FINISH (prompt 70c): Papers A and B, the paper of record of the Hodge line

**Return:** `research_returns\HODGE_FINISH_final_20261123T1713Z_unzipped\`. Paper A is
`workbench\work\UNFILED-A\v1\paper\main.tex` (66 pp.), Paper B is the same path under `UNFILED-B` (88 pp.). 113 register
tags; 29 numbered theorems. Its own state: "No human has checked the work". **Earlier intake:**
`...\intakes\HODGE_FINISH\` (aaf69461, 23 Nov).

1. **Useful.**
   - Paper A is the strongest packaged result of the Hodge line: a criterion plus explicit constants.
   - Paper B is mostly construction-specific negatives, plus two real criteria for Mumford's classes (Q23, Q29).
2. **What it proved.**
   - **Q01 (Thm family; Thm global).**
     - *Setting:* S is a connected Shimura variety at neat level, mapping to A_{g,N} (N ≥ 3) by a morphism of Shimura
       data; t is a flat section of R^{2p}f_*Q(p) of type (p,p) everywhere;
       c_t(s) = min max(M, deg Z⁺, deg Z⁻) over M t_s = cl Z⁺ − cl Z⁻.
     - *Equivalent:* (i) every t_s algebraic; (ii) c_t bounded; (iii) c_t bounded on one Zariski-dense set; (iv) one D
       such that, at every CM point and every number-field model, infinitely many good places carry
       sp(t_x) = (cl Z⁺ − cl Z⁻)/M with deg Z^± ≤ D (M free).
     - *Global form:* the Hodge conjecture for all complex abelian varieties ⟺ (ii) on CM points, or (iv), in every
       special family.
   - **Q02:** δ_W ≤ c_t ≤ ⌈2·16^n/n!⌉·δ·⌈√T⌉·Nm(a)^{n(2n+1)}·δ_W².
   - **Q03:** 48, 192 and 36.
   - **Q04, Q10:** stabilization, and the principal quotient deg q = (t_K f)^{2n}Δ, with m_K ≤ (2/π)√|disc K|.
   - **Q12:** strong semiregularity ⟺ dim Ext²(E,E)^G = 2n(2n−1).
   - **Q24:** class [−3] Gaussian sixfolds: 3 | Δ and δ_W ≤ (Δ/3)ℬ.
   - **Q09, Q28:** relative to Perry and Severn.
   - **Q27:** the Galois-orbit and flat-detector propositions.
   - **Paper B:** Q23 (the half-twist obstruction; the Lie-block criterion), Q29 (the coniveau criterion), and the
     obstructions and refutations Q11, Q13, Q16, Q17, Q20, Q21, Q30. Q18 and Q32 are positive trace networks with
     6,272 and 8,960 exact equations.
   - **Checks:** see the items table. Q27 and Q29 were checked in this pile.
3. **New since the last intake.** No new return. This pile adds:
   - targeted proof checks of Q27 (both propositions) and Q29;
   - the Q12 rank count;
   - the Q28/H19 disagreement;
   - the André–Oort remark.
4. **Open.**
   - **Q06 and Q07, the main question:** split eightfolds over K ≠ Q(ω), and uniform detectors. Gate: the principal
     Gaussian U⁴; a gluable perfect object with invariant Ext² = 56.
   - **Q08:** Mumford's family (the Lie-block or coniveau premise).
   - **Q19, Q22, Q25, Q26:** for Q26, a fixed complete-intersection multiple ⟺ bounded δ_W.
   - **Q27:** effective forcing.
5. **Relations.**
   - *Our runs:* it supersedes HODGE_BOUNDED_CYCLES and the constants of HODGE_DIVISION; it uses GHOSTS' dichotomy (now
     Q05); H15 (NIGHT_AFTER_ALPOGE) and Alpöge enter only through 70d.
   - *Literature:*
     - Markman, ICM Th. 1.2, p. 587;
     - Voisin, Bourbaki 1248, Th. 1.3;
     - Cattani–Deligne–Kaplan p. 483;
     - Brünjes–Serpé Th. 3.4;
     - van Geemen 1996 (Math. Z. 221);
     - Schoen 1988, 1998, 2007;
     - Severn (Hexagon 2610.00387v2);
     - Perry (preprint);
     - Bolognesi–Laterveer Th. 4.4, Prop. 6.2;
     - Scanlon, *Automatic uniformity*, Th. 4.2;
     - Chai–Oort Lemma 6.3.
   - *Grothendieck:* schemes over Z (spreading out; Hilbert schemes, FGA 221; SGA 6 XIII 6.11); the cycle class in
     families (SGA 4 XVIII 2.9, SGA 4½ Cycle); correspondences (the projector P(a*+ā*) is an algebraic correspondence;
     cote 16 conditions A, C, I, with the projector as the algebraic inverse); K-theory (Q12 detects Weil classes by
     e^B ch(E) of perfect complexes).
   - **On prompt 70d** (unsent, `TO_SEND\PRO\1_Archive_research_by_topic\70d_HODGE_EFFECTIVE\`). Paper A itself says
     that an orbit lower bound supplies no detector membership (main.tex 3302). Prop. galois-witness needs three things
     effective:
     - (a) the degree H(D) of the locus D_D, for which closedness gives no growth bound;
     - (b) Scanlon's B_S(H), a degree-uniform count of isolated special points, ineffective as it stands;
     - (c) the detector at the point.

     H15's orbit bound is one ingredient of the comparison, not the comparison. The prompt's item 1 also joins the
     Galois-orbit criterion to the per-fibre exceptional set of Prop. lift, which is a different mechanism (Paper A
     3331–3333). Worth a sentence in the prompt before it goes.
6. **Candidates.**
   - **Hexagon:** H25 (Paper A); H25b (the Q24 lattice lemma, after a Hermitian-lattice literature search: Jacobowitz,
     Kirschmer); H25c (Paper B, after Bolognesi–Laterveer is opened).
   - **Next prompt:** 70d, with the caution above.
   - **Corrections to Paper A:**
     - drop or justify the André–Oort hypothesis (3279–3283): André–Oort is known for Shimura varieties of abelian type
       (Pila–Shankar–Tsimerman, arXiv 2109.08788; my memory, to be confirmed);
     - decide Q28's status against D-G34 (below).
7. **Problems.**
   - **Q28 against H19.** Paper A, main.tex 1967–1971: "The geometric input is the G₃₄ family of Severn's unrefereed
     preprint [Severn, Prop. 8.5, §9 and Appendix A]". At 2018–2019: "These are the statements proved in [Severn §9]".
     At 3339: "The Eisenstein eightfold estimate is conditional on Severn's unrefereed geometric input". HODGE_DIVISION
     run A, `g34_section.tex` 22–29 and 596–600, proves the same input with "no Severn theorem premise" (read here, no
     fault). Either Paper A imports D-G34-01 to 06 and drops the condition, or the board's H19 ("from published inputs")
     must say why the paper of record does not. Note also that Paper A recalls the D-G34-03 argument in 2021–2039 but
     still credits it to Severn's Lemmas 8.2–8.4.
   - **Schoen 2007** (behind the 36) was not obtained by the run or by any intake. Bolognesi–Laterveer is unopened.
     Neither paper's pages have been viewed by us.

## HODGE_BOUNDED_CYCLES (prompt 70)

**Return:** `research_returns\HODGE_BOUNDED_CYCLES_final_20261123T0508Z_unzipped\` (a 120-page paper, 32 register rows).
**Earlier intakes:** cp02 and final (abcaba9b, 23 Nov).

1. **Not useful as a separate item: superseded.** Its register (Q01–Q32) and mathematics continue unchanged into
   HODGE_FINISH. The finishing fixes of the final intake (state of the field, abstract, proof overview, the split into
   two papers) were all made there, except the Schoen 2007 locator.
2. **What it proved:** Q01–Q05, Q09–Q12, Q14, Q15, Q18, Q20, Q28, Q29 and Q31; it refuted Q13, Q16, Q17, Q21 and Q30.
   The intake made targeted checks of Q01–Q05, Q10 and Q12. This pile recounted the rank in Q12.
3. **New since the last intake:** none.
4. **Open:** as HODGE_FINISH.
5. **Relations:** the seed `reports_20261122\paper_seeds\SEED_HODGE_DIVISION.md` leads to this run, and this run to 70c.
6. **Candidates:** none of its own.
7. **Problems:** none beyond those carried into HODGE_FINISH.

## HODGE_DIVISION (prompt 46, with 46b)

**Two runs under one name.**
- **Run A:** `research_returns\HODGE_DIVISION_checkpoint_34_20261122T1208Z_unzipped\`.
- **Run B:** `HODGE_DIVISION_checkpoint_28_20261122T1240Z_unzipped\`. This is the second run of prompt 46, not an older
  checkpoint.
- **The filing:** run A's `_from_earlier_checkpoints` mixes in run B's checkpoints.

**Earlier intakes:** parts 1–3 and cp34 (abcaba9b), and the PRIMER.

1. **Marginal now, with one useful part.**
   - Its division constants and detectors (HD-U, HD-D01/D02, HD-Q03/Q04, HD-F1-S07/T05, HD-COMP) are superseded in form
     by Paper A.
   - Its 112 later exclusion rows (run A since cp16) moved no gate.
   - What Paper A did not take over is **D-G34**: a Severn-free proof for split Q(ω) eightfolds.
2. **What it proved (D-G34).**
   - *D-G34-01:* the reflections s_i of ten explicit roots generate G₃₄ (order 39,191,040, by orbit lengths
     756·80·12·9·6 and containment of Davis's generators). Riemann existence gives a G₃₄-cover with 20 branch points,
     g(C) = 156,764,161; Chevalley–Weil gives an eightfold factor of signature (4,4).
   - *D-G34-02:* an exact parabolic cocycle certificate: 17 boundary twists, −DX_j positive semidefinite, sum positive
     definite, K-minor 1728.
   - *D-G34-03:* the period map has rank 16 and is dominant onto the split component.
   - *D-G34-04:* faithful-character vanishing on Schoen's exceptional divisors.
   - *D-G34-05:* cyclic suppliers are simple.
   - *D-G34-06:* Brauer induction makes both Weil lines algebraic.
   - *D-G34-07:* δ_W ≤ D₈(Δ) = (4G⁸Δ)⁸B₀, and D₈(f^{16}Δ) for an order of conductor f.
   - **Checks:** the run's whole-proof checks (same model); the script rerun PASS (cp34 intake); targeted proof check
     of D-G34-03 to 06 in this pile.
3. **New since the last intake.** No new return. This pile read D-G34-01 to 07, the H19 gate left open since 21 Nov.
4. **Open.**
   - Run A's Q2i and run B's T2-OTHER: nonsplit sixfolds. By stabilization they follow from split eightfolds.
   - Q5i: the RM-fourfold seed; its bridge Q5au is unproved.
   - The main question is that of HODGE_FINISH.
5. **Relations.**
   - *Our runs:* HECKE_DIV (SQ1–SQ7, supplying the arithmetic estimates of D-G34-07, not read here); GHOSTS (R12's
     132,269,760, superseded by 36).
   - *Literature:* Davis, Th. 5.1, pp. 312–313; Dettweiler–Wewers; Schmid (4.12) and (6.16); Schoen 1998, Th. 2.0,
     Lemmas 2.2–2.8, Cor. 3.1; Serre §10.5; Milne (Lefschetz classes), Th. 3.2.
   - *Grothendieck:* correspondences and Lefschetz classes; monodromy and degeneration (SGA 7).
6. **Candidates.**
   - **H19:** its first gate is met by this pile's reading. What remains:
     - the common-sign step through Dettweiler–Wewers;
     - SQ1–SQ7;
     - a literature comparison with Severn's Theorem A, which claims the same split eightfold result;
     - Paper A's status sentence.
   - **A correction to report to the source:** Schoen 1998, p. 18. The choice of a prime p | m whose degree-p quotient
     stays ramified fails for m = 12 and local exponent 6 (checked here). Severn's exceptional-divisor correction may
     already address it: compare before writing.
7. **Problems.**
   - "2^324 d^57 Δ⁶" (run A HD-CM6) hides d = 4mL², with L = lcm(1..2^2048): misleading, though not false.
   - The mixed filing of the two runs.
   - The earlier statements in `HODGE_DIVISION_ATTACK_20261121.md` that cp34's intake listed as false or stale; that
     file now carries a "superseded in part" note.

## What I read, what I did not

**Read:**
- the brief;
- all ten earlier intake and primer files of the five runs;
- the INTAKE_LEDGER rows; HEXAGON_CANDIDATES rounds 8–9; the board rows;
- the head of prompt 70d;
- HODGE_FINISH's CURRENT_STATE and QUESTIONS;
- Paper A: 36–60, 100–135, 205–230, 1965–2060, 3275–3345;
- Paper B: 5264–5640;
- HODGE_DIVISION run A, `g34_section.tex` 1–677;
- C44_POS.tex: 27076–27240, and greps for the ranks;
- HODGE_SIGN.tex: 225–300;
- the a3ccbc11 check and the H25 independent check (heads).

**Not opened:**
- any cited outside paper;
- the other sections of Papers A and B;
- C44_POS A22–A31r;
- HECKE_DIV;
- the runs' programs.
