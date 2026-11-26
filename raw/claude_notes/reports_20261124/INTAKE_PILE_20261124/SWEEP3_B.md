# SWEEP3_B: the archive research runs of sweep 3, second half

Cluster reader: Claude Opus 5.5 at effort high, launched by the main session 329fb1e6 (Claude Opus 5.5 at effort max) on
24 Nov 2026 for the intake pile. Brief: `BRIEF.md` in this folder.

**Runs:** RESEARCH_SA14_SA19, RESEARCH_SA15, RESEARCH_SA17, RESEARCH_SA20, RESEARCH_SA21, RESEARCH_SA22,
RESEARCH_SA22_run2, RESEARCH_SA23. All are by GPT-6 Astra (ChatGPT Pro mode), on prompts built in sweep 3 from the
Montpellier readings (`pro_prompt_builds/RESEARCH_SAxx/PROMPT.md`). They returned on 19-20 Nov 2026. Every return is either
INCOMPLETE by its own report or a final after the stopping rule.

**Files beside this one:**
- `SWEEP3_B_ITEMS.tsv`: 43 items.
- `INTAKE_<RUN>_20261124_CHECK_EVENTS.tsv`: 18 check events, filed for SA14_SA19, SA15, SA17, SA20, SA21, SA22_run2 and
  SA23.
- `SWEEP3_B_scripts/`: my scripts and their output.
- Running notes: `agent_notes/20261124T2111Z_Intake_pile_sweep_3_second_half_NOTES.md`.

## 0. First, a correction to the ledger

`field_experts/INTAKE_LEDGER.md` §0/§9 lists many unchecked statements for these runs (for example SA15: 955 of 1018).
**For seven of the eight runs that count is stale.** The full intakes of 21-22 Nov wrote a check event for every listed
id. Their files are in `results_register/horizontal/sweep3/SAxx/INTAKE_*_full*_CHECK_EVENTS.tsv`, and the ledger marks
them "latest not filed": the register was never rebuilt with them. I compared the §9 id lists with those files by script,
by exact id match. Result: **0 ids are missing for SA14_SA19, SA15, SA17, SA20, SA22, SA22_run2 and SA23.**

Some of those events are not checks under the rubric. They record "statement read only":
- SA15 full part 2: 248 rows, later raised in its round 2;
- SA20 full: 10 rows left after round 3;
- SA22: 24 rows; SA22_run2: 51-67 rows;
- SA17 full: 13 rows.

**RESEARCH_SA21 is the one real gap.** 89 of its 91 listed ids have no event under their register ids. The 19 Nov intake
(a6d42bf6, Claude Opus 5.5 at effort max) filed 24 events under other id forms and read the main proofs; the rest stayed
at statement level. This pile adds 7 events for SA21 (section 5).

To make the ledger match, run `results_register/build_check_register.py` with the `*_full*` files and this pile's files
included.

## 1. The cluster's most interesting items, ranked by usefulness

1. **Int(F2[[t^2,t^3]]) and Int(F2+tF4[[t]]) are projective, hence flat: Elliott's conjecture is false (SA20 B.022,
   B.023, B.024).**
   - **What it is.** For R = F_q + t^m F_q[[t]], for R = k + t^m l[[t]], and for every finite-conductor subring of a DVR
     with finite residue field, Int(R) is a projective R-module. The proof is Milnor patching of the free V-module
     Int(R,V) with a k-space along a gluing that is unipotent mod t^m. An elementary-matrix trick (B.021) makes the patch
     projective in infinite rank.
   - **Why it matters.** Elliott recorded the conjecture that Int(D) is not flat for exactly these two domains, as
     "still open" (arXiv 1109.3921 v1, p. 2). **I opened that page; the locator holds.**
   - **The 2026 literature, found today.** Ma (arXiv 2604.05922, v2 27 May 2026) and Jiang et al. (arXiv 2605.25259)
     give a non-flat Int(D) and so answer Cahen-Fontana-Frisch-Glaz Problem 19 negatively. Their domain is the
     two-branch domain F2 + t(t+1)T, which is the run's own B.016 domain. That domain is not one of Elliott's two, so
     there is no conflict. The two together sharpen the picture: one branch gives projective Int, two branches can make
     Int non-flat.
   - **Check status.**
     - acf08879 (Claude Opus 5.5 at effort max): a computation and a targeted check of the whole Part B chain.
     - This pile: a targeted check of B.022 and B.021 (every step), and the locator verified.
   - **Gates before a Hexagon note or a letter to Elliott:**
     - a search for work since 2011 on these two domains;
     - a second route, for example a direct regular-basis argument at m = 2.
   - **Where:** `RESEARCH_SA20_final_.../RESEARCH_SA20/agents/tensor_and_finite/part_B.tex` 1186-1420.

2. **A very ample counterexample to Kodaira vanishing for H^1 on a surface (SA14 A3), and through it the failure of
   Grothendieck's admitted integral weak Lefschetz (SA15 prop:OC-product-integral-counterexample).**
   - **The surface.** A3 builds a smooth projective surface Y in characteristic 2 with L very ample and h^1(Y,L^-1) = 1
     (h^0(L) = 562, h^1(O_Y) = 565). It is a Raynaud-type triple cover of a P^1-bundle over the curve y^2+y = x^15,
     followed by a cover by 9th roots of a generic basis of H^0(Q^9).
   - **The same surface does a second job.** SA15 uses it, embedded in P^561, to show that for Z = X x P^1 and a smooth
     Y in |A(x)O(m)| the torsion of H^2_cris(Y/W) is not the image of that of Z. So the "nous admettrons" of 8.3 on
     cote 4 is false in degree one.
   - **Literature, two web searches today.** Lauritzen-Rao (alg-geom/9604012) record Raynaud's 1978 question, whether
     vanishing can fail for a very ample bundle. They answer it only in dimension >= 6, and with the penultimate group
     H^{dim-1}(L^-1), not with H^1. They remark that Raynaud's own example is a surface (ample, not very ample). I found
     no very ample surface example. Not opened: Mukai 2013 and Zheng 2017, which the runs cite for the input surface.
   - **Check status.**
     - A3: every step by a262249a (Claude Opus 5.5 at effort max), and its certificate rerun.
     - The SA15 chain: targeted checks, plus an independent re-proof by a8d07e78 (Claude Opus 5.5 at effort max).
   - **Gate:** a fuller literature search, starting with Mukai's and Zheng's papers.
   - **Where:** SA14 `sections/A.tex`; SA15 `sections/A_integral_counterexample.tex`.

3. **Flatness of Pic^τ for every Artinian deformation of an Igusa surface, against three published claims (SA14 D4o,
   D4s, D4a, D4b, D4-gap).**
   - **The result.** In both the ordinary case (hull W[[t,s,u,v]]/(s^2+2s)) and the supersingular case (hull
     W[[t,s,u,v]]/(s^4-ts^2-2s)), Pic^τ is flat over every Artinian base. What fails over k[ε] is an abelian subscheme
     lifting Pic^var (D4a). The Albanese fibration of a Jacobian Igusa surface need not lift (D4b).
   - **The published claims it contradicts:** the first-order non-flatness of Chai-Oort §3.9(iv) and Chai Th. 2.4(iii),
     and Partsch 2013 (Prop. 6.6, Th. 6.7, Prop. 6.9).
   - **Check status.**
     - Targeted checks by a262249a, given Katz 1981 Th. 2.1, which nobody has opened.
     - D4-gap (the μ_2-torsor with tangent dimension 4 under a group of tangent dimension 5) is independently re-proved
       here.
   - **Gate:** open Katz 1981 and Chai. Then these become corrections to report to the authors, not Hexagon posts.
   - **Where:** SA14 `sections/D.tex`.

4. **Grothendieck's monodromy question 8.6 (cote 4) for plane curves in characteristic 2 (SA15
   thm:plane-char2-all-groups).**
   - **The answer.** The monodromy of H^1_et(C,F2) over ordinary smooth plane curves of degree d >= 4 is:
     - GL_g(F2) for even d;
     - for odd d, the full stabilizer 2^{g-1}:GL_{g-1}(F2) of a canonical covector.
   - So in odd degree the answer is not the one he hoped for.
   - **Correction to the 22 Nov intake's Hexagon note.** That note says no one has searched whether the obstruction is
     known. **The run's own text answers it:** it cites Cais-Ellenberg-Zureick-Brown 2013 Th. 4.2 and
     Castryck-Streng-Testa 2014 for the odd-degree obstruction, which compares the canonical char-2 theta
     characteristic with O((d-3)/2). The obstruction is known. The exact groups in every degree are the new part.
   - **Check status.**
     - Full check of the chain by a1cf7c6b (Claude Opus 5.5 at effort max), within the cited group classifications.
     - This pile: the obstruction re-proved, and the explicit quintic recomputed by my own script. My Hasse-Witt matrix
       equals the run's entry by entry, and the point counts and traces agree for m <= 6.
   - **Where:** SA15 `sections/A_char2_uniform.tex`, `A_monodromy.tex`.

5. **The capping maps of 67/074-082 are not isomorphisms: the (0,4) fibre is the punctured disc 0 < |q| < 16 (SA22
   A1-global-refutation, SA22_run2 A:04, A:04-exact-image, A:alltypes, A:single-cap-all-lengths).**
   - **The result.** The bound is Koebe's quarter theorem; the sharp constant is the slit domain C∖[1,∞) of conformal
     radius 4. On every nodal stratum the image is bounded. Run 2 adds that one cap determines every boundary length.
   - **Check status.** The two runs prove it independently. af3526fc (Claude Opus 5.5 at effort max) checked it on
     20 and 22 Nov, and sweep 3 had a third check. This pile checked the Koebe step and the sharp constant.
   - **Gate:** a literature search, with Michel Hua's project as a witness only.
   - **Where:** `RESEARCH_SA22_run2_final_.../RESEARCH_SA22/sections/part_A1234.tex`, `A1_radius_domain.tex`.

6. **The Hilbert-space trace formula proved in Grothendieck's hand (SA23 geo-H).**
   - **The finding.** Cote 1, sheets 79-80 and 111-112, carry a complete proof that trace = sum of eigenvalues for
     trace-class operators. In print he announced the result without proof (CR 1951 p. 1557; 1955 memoir II-13) and
     removed it in the 1956 Erratum. Lidskii 1959 is the first printed proof.
   - **A side result.** The corrected determinant Δ_τ(A) = exp τ(log|A|) on 1+L^1 extends Hochs-Kaad-Schemaitat 2018
     to non-invertible elements.
   - **Check status.** Checked by acadc29d (Claude Opus 5.5 at effort max) and in sweep 3. Here: the continuity
     counterexample.
   - **Gate:** open the three printed sources. The note states facts, not priority.
   - **Where:** SA23 `sections/geometry_H.tex`.
   - **Relation:** the later prompt `SENT/33_TRACE_DET_cote_1...` works on this.

7. **The representability criterion of cote 131 (scan 14) corrected (SA17 A:main-counterexample,
   A:pro7-representability).**
   - **The counterexample.** P(B) = α_p(B^h_(t)) over F_p[t] satisfies conditions 1-8 with the literal 7, but has no
     separated locally quasi-finite representation.
   - **The corrected theorem.** With the pro-modular 7, his first wording, the criterion holds over every locally
     noetherian base. That is a proof of the locally quasi-finite analogue announced in Murre (Séminaire Bourbaki 294).
   - **Check status.** Targeted checks by a512cf71 (Claude Opus 5.5 at effort max). Here: the non-representability step
     (Artin-Schreier pole argument, faithfully flat coefficient comparison, ZMT).
   - **Gates:** an independent re-proof of the fpqc descent (de Jong-Olander, unopened), and a literature search.

8. **The crystalline Dieudonné functor is not fully faithful over F_p[x,y]/(x,y)^2 (SA17 B:crystal-counterexamples,
   B:finite-PD, B:PD-not-QSyn).**
   - **Check status.** Checked and partly re-proved by a512cf71.
   - **Literature.** My web search found only positive results: Berthelot-Messing (bases with a p-basis), full
     faithfulness up to isogeny for lci schemes, and quasisyntomic rings. It found no such counterexample. F_p[x,y]/(x,y)^2
     is neither lci nor quasisyntomic, so nothing known is contradicted.
   - **Gate:** one, a proper literature search.

9. **F11: every metabelian quotient of the local π_1 of a complete normal surface singularity in char p is finitely
   generated (SA14 F7-F13h).**
   - The strongest partial result toward his local Lefschetz conjecture of 58:19.
   - Checked by a262249a, given the Krishna-Majumder preprint (arXiv 2601.12177).

10. **G1: Pic^δ has a universal section over the moduli of type D iff at most one d_i is odd (SA14).** A clean statement;
    one gate (literature).

11. **The EGA errata of SA23 (D-3/D-4, D-6, D-11, D-12, D-13, D-15, C-9).**
    - Useful for our EGA editions.
    - D-6 is independently re-proved here, by depth sensitivity.
    - Gates: the printed pages, and a script certificate for the finite examples.

12. **SA21 A27/A06/A28: the support lattices of cote 156.**
    - The interval magasin of a finite L is orthomodular iff L is a conditional lattice, and Boolean iff the
      non-isolated points form a chain. This extends Jenča (Order 40, 2023) to unbounded posets.
    - A28 corrects Jenča v1 Cor. 4.5.
    - My brute force over all posets with up to 7 elements finds 0 mismatches.
    - Niche, but complete.

## 2. The runs

### RESEARCH_SA14_SA19 (cotes 43-44, 57-60: Picard schemes, Lefschetz for Pic, Jacobians, the 1964 programme)

Return: `research_returns/RESEARCH_SA14_SA19_checkpoint_08_20261120T2005Z_unzipped` (cp08, INCOMPLETE).

1. **Useful.** It produced explicit answers to most of the leaves 57:97-315 and 44:2-9, and several results a specialist
   would want: A3, D4o/D4s, G1, E4.T, C2.G and F11.
2. **What it proved.**
   - **A3, A4/A4b, R3u.** The kernel of Pic(X)->Pic(Y) is a finite unipotent infinitesimal p-group (his 57:100 reading).
     It can be nonzero for a very ample embedding of a surface.
   - **B2.** Seshadri's question: lci + R_2 suffices. R_2 is not necessary, and no criterion on fibre types alone
     exists.
   - **C2.G.** Pic(X) = Pic(X^) over an excellent henselian base when H^1(O_X) has finite length.
   - **D1-D4.** Both signs of h^01 - h^10 on threefolds (A×Q)/Γ in char 2; non-flat Pic^τ; the Igusa items of §1.3.
   - **E4.***. Explicit families against 57:308-315; E4.T: Pic^τ is closed for geometrically integral fibres.
   - **F5-F13h**, culminating in F11.
   - **G1-G3.**
   - **H1**: pd J_∞ <= 1.
   - **I8**: the residual-complex presentation.
   - **J**: counterexamples to Th. 3, 4, 5, the Th. 6 middle clause and Th. 7 of the 1964 programme; J6L, J6P and J6Z
     positive in stated scopes.
   - **Check status.** All 242 rows have intake events: the cp05 intake of 20 Nov and the full intake of 22 Nov, both by
     a262249a (Claude Opus 5.5 at effort max), 257 events. This pile adds J1-Th5 (a scripted computation) and D4-gap (an
     independent re-proof).
3. **New since the last intake:** no new return. The cp08 rows were all taken in on 22 Nov.
4. **Open.**
   - A1/A2/SA14-H4 (the boxed "noyau nul si n >= 4"). Gate: a smooth fourfold with a nonzero class in H^1(Y,U_N) or
     in im δ_N. The question is reduced to n = 4 (A1r), and the kernel is a finite p-group (A4b).
   - F/F-full (58:19). Gate: derived length >= 3 without the Swan cutoff, and non-solvable wild quotients.
   - E4 / SA14-H7: schematicity of Pic over an arbitrary base for normal or integral fibres.
   - I-all: a reading question on 43:64-66.
5. **Relations.**
   - SA15 uses the A3 surface.
   - The J rows meet the later runs JAC1964 and C44_POS (pile files `INTAKE_JAC1964_...`, `INTAKE_C44_POS_...`;
     prompts `SENT/40_HODGE_JACOBIANS_1964_cote_44`, `SENT/51_C44_POS`).
   - Literature named by the run:
     - Raynaud 1978 / Mukai / Zheng (A3);
     - Katz 1981, Chai-Oort, Chai, Partsch 2013 (D4);
     - SGA 2 XI-XIII (A, B, F);
     - Kleiman, *The Picard scheme* (E4);
     - Saito 1979 and ACMV (J).
   - Frameworks: Picard schemes and motives (algebraic representatives Ab^i; J6 is Lefschetz for incidence
     correspondences); Tate twists enter F only as μ_n coefficients.
6. **Candidates.**
   - Hexagon: A3 (literature gate); G1 (literature gate); J5/J2b, after coordination with the JAC1964 entry H11.
   - Corrections to report: Chai-Oort, Chai, Partsch, after Katz and Chai are opened.
   - Next prompt: a fourfold for A1/A2, and the derived-length-3 gate for F.
7. **Problems.**
   - C2-char0 states "H^1(X, m^n O_X) = 0 for n >> 0" (citing Perling-Schröer Prop. 1.2). That is false for flat proper
     X over k[[t]] with torsion H^1(O_X). The statement is saved by C2.D/C2.G.
   - J5 refutes only the literal Th. 5: the planes meet the base locus in lines.

### RESEARCH_SA15 (cotes 4-9 and 100: crystalline weak Lefschetz, Hasse-Witt monodromy, inertia and torsion, extension of abelian schemes)

Return: `research_returns/RESEARCH_SA15_checkpoint_37_20261120T0635Z_unzipped` (cp37, INCOMPLETE; 1018 register rows).

1. **Useful.** The 8.6 answer for plane curves in char 2, the integral weak Lefschetz failure, and the generic positivity
   of the unit-root rank bear directly on cote 4. Part B is sharp but specialized.
2. **What it proved.**
   - **thm:plane-char2-all-groups** (§1.4).
   - **prop:OC-product-integral-counterexample** (§1.2).
   - **thm:all-X-explicit-positive-rank**: the "n° 7" of 8.5.8.
   - **A2-EXACT / A2-UNIT**: 8.5 in every degree.
   - **thm:ss-all-odd-full-groups**: E×E supersingular, p = 2, the full groups.
   - **Part B**:
     - B-RD3: the ordinary case of 9:14;
     - B-RD4: Lead B' false as stated;
     - B-RD6: the cas test is negative;
     - the exact indices B-RD73, B-RD98-exact-five, B-RD100-exact, B-RD27-exact-three.
   - **Part C**: C-RD11 and C-RD4 (counterexamples to 100:3 2)); C-RD1 (Corollary 3 of 100:25 holds).
   - **Parts D-E**: the crystal/stratification questions of cotes 5-8.
   - **Check status.** Intakes of 20 Nov (two parts) and 22 Nov (three parts), by SA15-c9_c100-part2, afcdf31b, a8d07e78
     and a1cf7c6b (all Claude Opus 5.5 at effort max). Every id has an event. A part-2 slice of 248 statement-only rows was
     raised in round 2. Nothing of the run was refuted. This pile adds two events on the odd-degree obstruction.
3. **New since the last intake:** no new return.
4. **Open.**
   - Part C: 100:3 2) for reduced S with finite normalization (his boxed hypothesis, 100:7).
   - Part B: the general least index of B.4.
   - Part A: A.3-A.4 for general X.
5. **Relations.**
   - SA14 (the A3 surface).
   - POLISH_CRISTAUX (another cluster), for the crystals of cotes 5-8.
   - Literature named by the run: Ogus 1975; Katz-Messing 1974; Illusie 1979; Cais-Ellenberg-Zureick-Brown 2013;
     Castryck-Streng-Testa 2014; Achter-Pries 2008; Churikov-Vasil'ev-Zvezdina 2022.
   - Weights: A2-UNIT counts p-adic units among Weil numbers of weight i (Katz-Messing, from Weil I).
6. **Candidates.**
   - Hexagon:
     - "integral crystalline weak Lefschetz fails" (literature gate);
     - the plane-curve exact groups (literature on the groups only, since the obstruction is known);
     - generic positivity of the unit-root rank (literature against Illusie 1990 and Ekedahl).
   - Next prompt: the Part C reduced case with finite normalization.
7. **Problems.**
   - Errata listed by the 22 Nov intake: "-candidate" labels on proved rows, undefined symbols in two corollaries, a
     misattributed reason in lem:B-RD92-tame25.
   - The 22 Nov Hexagon note on the plane-curve obstruction overlooks the run's own citation of
     Cais-Ellenberg-Zureick-Brown (§1.4 above).

### RESEARCH_SA17 (cotes 126-133: representability, descent, Barsotti-Tate and crystals, λ-operations)

Return: `research_returns/RESEARCH_SA17_checkpoint_12_20261119T2037Z_unzipped` (finishing run, cp12, INCOMPLETE; 271 rows).

1. **Useful.** Part A closes the cote 131 criterion (§1.7), and Part B gives a full-faithfulness counterexample that p-adic
   Hodge theorists would want. Part C is open-ended classification.
2. **What it proved.**
   - A:main-counterexample and A:pro7-representability.
   - A:L1-general: openness of the modularity locus.
   - A:L2-counterexample: our Lead L2 refuted.
   - A4: the cote 128 Théorème holds in every rank; Lemma 1 is false for every p.
   - B:crystal-counterexamples, B:finite-PD, B:PD-not-QSyn.
   - C:BO_affine_lambda: split WG(BO_m) is special iff m <= 2 or the base is a Q-algebra.
   - C:regular-coherent-criterion: for regular coherent rings, "polynomial" iff char 0 and K_0 = Z; for number rings,
     class number one.
   - **Check status.** Intakes of 19, 20 and 22 Nov by a512cf71/ac8bd2a2 (Claude Opus 5.5 at effort max); every id has
     an event, 13 at statement level. This pile adds a targeted check of the non-representability step.
3. **New since the last intake:** no new return.
4. **Open.** C.1 for singular rings of mixed characteristic; C.3 for arbitrary coefficient bases.
5. **Relations.**
   - Murre, Séminaire Bourbaki 294; de Jong-Olander; Berthelot-Breen-Messing; Lau; Anschütz-Le Bras.
   - Grothendieck's λ-rings and K-theory: C is his λ-question for Grothendieck-Witt rings.
6. **Candidates.**
   - Hexagon: B.3 (one gate: literature); the cote 131 theorem (two gates).
   - A possible Stacks erratum: the run says Example 60.22.1 omits the term de·uv at p = 2. Unverified; open Stacks
     first.
   - Edition notes for 131/14, 128 and 133/29, 36.
7. **Problems.** Our own finishing prompt (B.3(ii)) asked the run to exclude positive examples; the run rightly declined.

### RESEARCH_SA20 (cotes 119-125, 152-161: Esquisse dossiers; collars, analysers and integer-valued polynomials, vanishing cycles, Weyl groups, finite geometry)

Return: `research_returns/RESEARCH_SA20_final_20261120T0404Z_unzipped` (final, INCOMPLETE after its stopping rule; 267 rows).

1. **Useful,** mainly through Part B (§1.1). Part A gives exact verdicts on the Additif conjectures from classical
   inputs.
2. **What it proved.**
   - A.101-A.112 (II c) true; I b), I c), II b) false; five of eleven functors are equivalences).
   - A.701/A.703 (the foliation).
   - A.205 (a coarsest intrinsic PL partition).
   - B.016-B.082:
     - the projectivity of Int for one-branch finite-conductor domains;
     - the two-branch obstruction;
     - the tensor criterion classified (B.054 for Noetherian domains, B.082 for every inclusion).
   - C.004: Milnor's vanishing by Gysin/Wang in an open book.
   - D.002, D.005, D.021, D.025: the cote 123 Coxeter package.
   - E.003, E.006: finite-geometry readings.
   - **Check status.** Intakes of 20 and 22 Nov (round 3) by acf08879 and aaece8bf (Claude Opus 5.5 at effort max and
     high). A.104 and A.111 are independently re-proved; 10 rows remain statement-only. This pile adds B.022 and B.021
     and verifies Elliott's locator.
3. **New since the last intake:** no new return. **New information:** the 2026 literature (Ma; Jiang et al.) and the
   verified Elliott locator.
4. **Open.**
   - A.159-A.160: PL ≃ definable concordance over every o-minimal real closed field. The crux is the forward parameter
     bounds over a non-Archimedean model.
   - Real TOP concordances in base dimensions 3 and 4.
   - The maximal locus with target dimension >= 3.
5. **Relations.**
   - Elliott 2011 (arXiv 1109.3921); Ma 2026 (arXiv 2604.05922); Jiang et al. 2026 (arXiv 2605.25259); Cahen-Chabert;
     Hatcher-Wagoner; King; Cameron 2015 §6 (the triality, E.009).
   - Frameworks: integer-valued polynomials are binomial rings / λ-rings (Elliott's plethories), in Grothendieck's
     λ-ring line.
6. **Candidates.**
   - Hexagon note on B.022-B.024. Gates: a literature search since 2011, and a second route.
   - Inform Elliott once that is done.
7. **Problems.**
   - None found in what I read.
   - A.132 (π_2 P_TOP(S^3) = Z/2) is checked only in part.

### RESEARCH_SA21 (cote 156, *Vers une géométrie des formes*, 1986: supports, axiom systems, maquettes)

Return: `research_returns/RESEARCH_SA21_final_20261119T1242Z_unzipped/RESEARCH_SA21` (final; 92 rows: 53 proved, 31
refuted, 6 known, 2 proved under stated hypotheses, none open).

1. **Marginal for mathematics, useful for the archive.** The order-theoretic results are complete and correct as far as
   checked, but they are small. Their value is that cote 156's axiom systems now have exact verdicts, page by page.
2. **What it proved.**
   - **A-part:**
     - A03: Dacey's criterion, specialized;
     - A04: an exact Booleanity test for arbitrary orthosets;
     - A06/A26/A27: the classifications of §1.12;
     - A14a: the atom criterion;
     - A16: the two-neighbourhood condition for the Théorème of 156-7/94;
     - A07: the crown, 8 strata, 20 supports, not orthomodular, yet Sumner's condition holds;
     - A11: his ten-element ortholattice of 156-9/113 is not orthomodular;
     - A28: Jenča's corollary.
   - **B-part:**
     - B-prime-representation: bounded-join primality exactly repairs deployment;
     - B-M3: the equality-irreducible readings of 156-4 and 156-8 fail;
     - B-Sigma-gate and B-Sigma-counter;
     - B-C4-false;
     - BM-event-iff: contrées = locally distributive = binary-conflict event structures;
     - the o-minimal cell model.
   - **C-part:**
     - C08: Björner's CW-poset criterion with orientations;
     - C06: the torus counterexample to our L4;
     - C09: simplicial face posets;
     - C12: McCord for arbitrary Alexandrov posets, which is known.
   - **Check status before this pile.** The 19 Nov intake (a6d42bf6, Claude Opus 5.5 at effort max) did the following:
     - read A03, A04, A06, A07 and the infinite Boolean proof;
     - computed the M(L) classifications for posets with up to 5 elements;
     - decided the five ink points on the scans (156-6 (1.20) has the prime condition, so his deployment theorem holds
       there);
     - opened Jenča, Sumner and Nielsen-Plotkin-Winskel.
   - **This pile adds:**
     - computations for A27, A06 and A14a over all 96,428 labelled posets on 7 points and every smaller poset (0
       mismatches);
     - a re-proof of A14a;
     - the crown;
     - a targeted check of A28;
     - the decisive step of B-Sigma-counter.
3. **New since the last intake:** no new return; the checks above.
4. **Open.** The run reports none. Unread proofs remain: the axiom-atlas implications, the o-minimal model, C08-C12, and
   the At 1-11 verification of the Σ-countermodel (`parts/axioms/finite_axioms.py`, not rerun).
5. **Relations.**
   - Jenča 2023; Paseka-Vetterlein; Sumner 1974; Nielsen-Plotkin-Winskel 1981; Björner 1984; McCord 1966; Coste
     (o-minimal triangulation, unopened).
   - Frameworks: none of schemes, motives or weights. This is Grothendieck's late combinatorial geometry of forms.
6. **Candidates.**
   - A correction to report: A28 to Jenča, after checking that the Order 2023 version still has the statement.
   - No Hexagon note, and no research prompt; the three ink changes go to the next second pass of cote 156.
7. **Problems.** None found. The Coste and Björner originals are still unopened.

### RESEARCH_SA22 and RESEARCH_SA22_run2 (cotes 66-68: Teichmüller towers, capping, the 1980s letters; anabelian sheets)

Returns:
- run 1: `research_returns/RESEARCH_SA22_final_20261119T1905Z_unzipped` (159 rows);
- run 2: `research_returns/RESEARCH_SA22_run2_final_20261119T2149Z_unzipped` (202 rows).

Both are final and INCOMPLETE.

1. **Useful.**
   - The capping refutation with its exact image (§1.5), and the single-cap rigidity.
   - The orange-slice limit is the best positive statement about the letter.
2. **What they proved.**
   - The A1 refutation (0 < |q| < 16); A:alltypes.
   - A2-explicit-limits: the Jenkins-Strebel cells, Q_0 radius 4/(3√3).
   - A:single-cap-all-lengths.
   - The cap radii are the gradient of a strictly convex potential.
   - Run 1's toric non-injectivity and non-descent.
   - The 67/091 counterexample: R = Z[x,y,z]/(x^2+yz-1), which refutes our own correction.
   - Subject 24, question 2: classical in char 0 (Kleiman 1994).
   - Subject 21: yes for affine X (Gabber 1994); run 2's Nagata-type counterexample for qcqs X.
   - B:local-Hurewicz: against SGA 2 XIII §6 Conj. A, in the run's reading.
   - B:nonlinear-Artin: Rond 2005, made explicit.
   - Condition K false (C_4).
   - **Check status.** af3526fc (Claude Opus 5.5 at effort max), 20 and 22 Nov. Every id has an event. Many rows are
     background (55 and 67) or statement-only (40 and 67). This pile adds a targeted check of A:04 and of
     A:04-exact-image (run 2).
3. **New since the last intake:** no new return.
4. **Open.**
   - U:henselian-comparison (run 2).
   - The anabelian rows A6 (model and specialization) are at statement level.
   - A1-toric-nondescent (the phase rule).
5. **Relations.**
   - Koebe, Lavrentiev, Strebel, Mondello (grafting), Wolpert, Earle-Marden, Gabber 1994, Hoshi-Mochizuki, Kleiman 1994.
   - Frameworks: the anabelian rows sit in Grothendieck-Teichmüller and mixed Tate motives over Z (the GT hexagon). See
     the 20 Nov intake's bridges §5.0-5.2.
6. **Candidates.**
   - Hexagon: "(0,4) refutation and exact image" (one gate: literature).
   - Next prompt: an independent check of run 1's jets and toric non-descent.
   - B:local-Hurewicz needs SGA 2 XIII opened before anything is said about Conjecture A.
7. **Problems.** None in the statements checked. Run 2's C:Goldman-branches is unchecked.

### RESEARCH_SA23 (cotes 1-2, 21-26, 161: EGA drafts and letters, trace and determinant, Cohen lifts, natural bundles, categories)

Return: `research_returns/RESEARCH_SA23_final_20261120T0511Z_unzipped` (final, INCOMPLETE; 120 rows).

1. **Useful** for the archive and for our EGA editions (§1.6, §1.11). The rest is known mathematics placed against his
   pages.
2. **What it proved.**
   - geo-H: the trace formula, determinants, and the 1956 reconstruction.
   - A-04 to A-19: discrete formal smoothness and Cohen lifting; A-16 in the nonlocal noetherian adic case.
   - B: Cohen factorization; transfinite triangular presentations (B2-2).
   - C: Koszul versus quasi-regular.
   - D: the EGA errata.
   - geo-E-relative: the exponent of cote 23/006 must be (r+1)(d-1)^r.
   - F: natural bundles.
   - cat:I, J, K, L: the cat:J8 S_3 obstruction; geo-Ke-unpolarized.
   - **Check status.** acadc29d (Claude Opus 5.5 at effort max), 20 and 22 Nov: every id has an event, 0 gaps, 12
     refutations confirmed. This pile adds the D-6 re-proof and the geo-H-continuity check.
3. **New since the last intake:** no new return.
4. **Open.** Documentary only: the date of the cote 1 sheets.
5. **Relations.**
   - Lidskii 1959; Weyl; Hochs-Kaad-Schemaitat 2018; EGA 0_IV, III, IV and their Err_IV; Hochster 1973; Fontaine.
   - Later prompt: `SENT/33_TRACE_DET_cote_1_...`.
6. **Candidates.**
   - Hexagon: "Corrections to EGA" (gates: printed pages, script certificate); the trace-formula note (gate: printed
     sources).
   - Corrections into our EGA editions.
7. **Problems.**
   - The run's reading of the Err_IV 12 sign (D-7) has not been checked against the print.
   - The other EGA items need the printed pages.

## 3. What this pile did (the check events)

| Run | Statement | Type | Outcome |
|---|---|---|---|
| SA14_SA19 | J1-Th5 | computation (sympy) | confirmed; literal statement only (excess intersection) |
| SA14_SA19 | D4-gap | independent re-proof | holds |
| SA15 | thm:odd-plane-char2-obstruction | independent re-proof; computation | holds; the explicit fibre agrees in every entry; the obstruction is known (CEZB 2013) |
| SA17 | A:main-counterexample | targeted proof check (non-representability step) | confirmed as far as read |
| SA20 | B.022, B.021 | targeted proof check | confirmed; Elliott locator verified |
| SA21 | A27, A06, A14a, A07 | computation (n <= 7) | 0 mismatches |
| SA21 | A14a | independent re-proof | holds |
| SA21 | A28, B-Sigma-counter | targeted proof check | confirmed (decisive step) |
| SA22_run2 | A:04, A:04-exact-image | targeted proof check | confirmed |
| SA23 | SA23-D-6 | independent re-proof (depth sensitivity) | holds |
| SA23 | geo-H-continuity | targeted proof check | confirmed |

No statement of any run was refuted by this pile.

## 4. Not read, and why

- The runs' other proofs were not reread. The earlier intakes did that, and I took their verdicts from their files.
- Not opened: Katz 1981, Chai, Partsch, Mukai 2013, Zheng 2017, de Jong-Olander, SGA 2 XIII, the EGA print, the 1951
  CR and 1955 memoir, Jenča's journal version, Björner 1984 and Coste. These are the gates named above.
- The literature lookups (Lauritzen-Rao, Elliott 2011, Ma 2026, Jiang et al. 2026, a Dieudonné-theory search) were web
  lookups made today. They are leads for the gates, not complete searches.
