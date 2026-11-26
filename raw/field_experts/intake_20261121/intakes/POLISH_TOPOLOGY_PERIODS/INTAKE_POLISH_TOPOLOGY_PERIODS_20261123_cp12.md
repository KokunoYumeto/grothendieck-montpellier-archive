# Intake: POLISH_TOPOLOGY_PERIODS, checkpoint 12 (23 Nov 2026)

This intake was done by Claude Opus 5.5 at effort high, launched by the main session (Claude Opus 5.5 at effort max). The run it reads is prompt 91 POLISH_TOPOLOGY_PERIODS, carried out by GPT-6 Astra (ChatGPT Pro mode); the runtime did not expose its numerical effort. The run is **still going**: checkpoint 12 was saved at 10:04 UTC, at formal review 07.

## 0. What I read and the scope

**Read in full:**
- PROMPT.md as sent (`TO_SEND/PRO/1_Archive_research_by_topic/SENT/91_POLISH_TOPOLOGY_PERIODS/PROMPT.md`).
- From the return: README.md, LEDGER.md (01:03 to 10:04 UTC), CORRECTIONS_FOR_AUTHORS.md and REGISTER_STATISTICS.tsv.
- The Paper 7 and Elliott/Bhowmik/King/Jenča entries of LITERATURE.md.

**CHECK_EVENTS.tsv:** I tallied the 420 events by paper and type and read every event whose outcome is not "no fault".

**INHERITED_CHECK_EVENTS.tsv:** I read only the header and the first row. It has 4,557 rows and is kept separate by the run as evidence from earlier runs.

**REGISTER.tsv** was used only to locate the main theorems, as the brief asks.

**The papers.** All seven are in `workbench/<repo>/work/PAPER-0N/v1/` (main.tex and main.pdf). Their TeX comes to about 1.3 MB, which cannot be read whole within this budget. For each paper I read the abstract and the main statements of Section 1. Proofs read in full:

| Paper | Proofs read in full |
|---|---|
| 1 | Theorem 1.1, the covering claim; the whole section "Two counterexamples to incidence-piece gluing" (Theorem 1.2) |
| 2 | Theorem 12.1 (patching lemma), Theorem 12.2 (finite-conductor theorem), Corollary 15.5 |
| 3 | §2.3 (the joint torsor), Lemma 3.1, Proposition 3.2, Corollary 3.3. I reproved Corollary 1.2 independently, by a direct elliptic computation |
| 4 | Theorem 1.1, single cap (its whole proof section and eq. (connection)); Theorem 1.5, the eigenspace counterexample |
| 5 | The Euler-characteristic algebra of Theorem 1.1, plus a hand case |

Everything else in the papers I read at the level of the statement or not at all; §1 says which.

**Primary sources I fetched myself:**
- Bhowmik-Pathak, arXiv:2408.00271v1. Its SHA-256 equals the run's record (58604953…). I read Theorem 1.11 (p. 3) and the proof in §3.5 (pp. 17-18).
- The arXiv pages of Elliott 1109.3921 (v1 only, no journal reference), of Jenča 2206.08113 (v1 only, Order 40 (2023)) and of Ma 2604.05922.
- The full text of Jiang-Li-Sun-Wang-Xiao-Yu 2605.25259v2 (the Rethlas paper), searched for these rings.
- A web search for a Bhowmik-Pathak erratum. It found none; arXiv v1 says "to appear in Acta Arithmetica".

All my checks are in `INTAKE_POLISH_TOPOLOGY_PERIODS_20261123_cp12_CHECK_EVENTS.tsv`.

## 1. Each paper's main theorems: the checks they received

The run's state, from LEDGER review 07 at 10:04 UTC:
- 344 of 1,028 register rows are accepted in a corrected exact scope; 684 are open, each with its gate.
- There are 420 current check events.
- Every hourly review so far records mathematical movement, with zero consecutive reviews without it.
- Page counts: Paper 1, 56; Paper 2, 85; Paper 3, 84; Paper 4, 33; Paper 5, 41; Paper 6, 31; Paper 7, 45.

### Paper 1. "Gluing Grothendieck's tubes by their intersections" (56 pp.)

| Statement | My check |
|---|---|
| Thm 1.1, open-tube descent | **Targeted proof check, confirmed.** The open sets W_i = N_i \ R_i cover X: for x, the set I_x is finite and downward directed, so it has a least element i_0, and x is not in R_{i_0}. The rest is Stacks 00AL/00AN, cited as such. The content is a careful application of ordinary descent. |
| Thm 1.2, the incidence pieces are insufficient (chains {0} ⊂ R ⊂ C and {0} ⊂ R^2 ⊂ R^4) | **Targeted proof check, confirmed.** The punctured disk V_02 ∩ V_12 is not a piece of the diagram. Compatibility along V_02* → V_12* fixes the isomorphism on the upper-half-plane stalk, so a global sheaf would have to send the ray-to-u map to both 0 and 1. The successor-pair variant is also correct. This is the paper's real answer to cote 151. |
| Thm 1.3, stable-graph meets | Statement only. |
| Thm 1.4, truncation level of exodromy | Statement only. Known in substance: the second equivalence is formal, since S_{≤n} is an (n+1)-category, and the first is exodromy (Lurie HA A.9.3; Haine). |
| Thms 1.5-1.7, Cor 1.8 and Thm 1.9: shape, exit comparison, holink pushout, proper Hurewicz fibrations with singular fibres | Statements only. Not read in full. |

The run's own record for Paper 1:
- 73 of 74 rows are accepted.
- Nine main statements have separate-worker frozen re-proofs. These are re-proofs by the same model.
- The all-band C4 proof was closed at 08:48 UTC.
- B6.3 (a glyph in the manuscript) is open.

### Paper 2. "Grothendieck's collars, cones, and polynomial operations" (85 pp.)

| Statement | My check |
|---|---|
| Thm 12.1, the infinite-rank patching lemma | **Targeted proof check, confirmed.** I verified the Whitehead identity by block multiplication. Column-finite elementary lifts are automorphisms. |
| Thm 12.2, Int(R) projective for every finite-conductor subring of a DVR with finite residue field | **Targeted proof check, confirmed, every step**: R is local and Noetherian; the greedy Newton basis of Int(R,V); the digit map δ = (X^Q - X)/π, with v(δx - δy) = v(x - y) - 1; the indicator H^{Q^m}; B/JB ≅ F(R,D); A/JB ≅ colim R_0^{E_N}, which is free; the Milnor square R = V ×_D R_0. **Strengthening, my addition:** Int(R) is countably generated and projective over a local ring, hence **free** (Kaplansky). |
| Cor 15.5 at F_2[[t^2,t^3]] and F_2 + tF_4[[t]] | **Confirmed.** See §2. |
| Thm 12.3, branch criterion (tensor maps are isomorphisms iff the normalization is local) | Statement only. The run's record: targeted check of the whole necessity chain (P02-RG-T001); independent re-proof of sufficiency and all arities only (P02-RG-I001). |
| Thms 1.1-1.6, collars and cones: fibrewise contractibility; parametrized collars contractible; Col(X,B) ≃ BP(B); the torus concordance group; strict cones; the eleven arrows | Statements only. The component group of the torus is an application of Hatcher-Wagoner and Igusa, credited as such. **Still moving:** at review 07 the run's fresh collar comparison found that the live rigidification definition lacks the "identity on the base" condition. The theorem is held until a correction is staged. The rows A101-A112 and the universal-Tor main row B082 are held for a clean whole-main reconstruction. |
| A.160, PL = definable concordance over every o-minimal real closed field | The run accepts it, after separate frozen A158 and A157/A160 proofs and a chain audit (P02-TROOT-CHAIN). Not read by me. |
| A.205, intrinsic partition versus King | The intrinsic partition is accepted; King 1985 itself was never obtained, so the comparison gate is open. |

### Paper 3. "A counterexample and a dimension formula for Grothendieck's strong transcendence conjecture" (84 pp.)

| Statement | My check |
|---|---|
| Thm 1.1, the joint-torsor dimension table | **Targeted proof check, confirmed.** I read §2.3, Lemma 3.1, Proposition 3.2 and Corollary 3.3 in full, and rederived the stabilizers B_J = J ∩ (B × B^-), S_γ and S_K and the six dimensions g, u, u+v, g+v, b+v, u. 0 ≤ v ≤ u holds because n - n_B is the positive-μ-weight part of Lie N_2. The upper bounds are unconditional because the comparison point lies on André's motivated torsor. The equalities hold under genericity of that point. The "five false predictions when v < u" are strict inequalities of upper bounds; for K/k(α), the uniform fibre dimension supplied by normality of N_2 is what is used. |
| Cor 1.2, h^1 of y^2 = x^3 - x + 1 | **Independent re-proof, confirmed**, by my own computation before reading the paper's proof. j = -6912/23, so the curve is non-CM, and (g,b,u,v) = (4,3,1,0). The real Frobenius gives conj(F) = F_∞(F), so K = k(α) and Q(ψ) = Q(φ). Explicitly, γ has columns (ω_1, ω_2) and λ·(conj ω_1, conj ω_2); the conjugates are rational combinations of ω_1 and ω_2 through F_∞. So trdeg k(γ) ≤ 3 < 4 and trdeg Q(ψ) ≤ 1 < 2. The five predictions are false unconditionally. |
| Thm 1.3 (1)-(5): the ordinary curve at 5, the Cartier restricted-Lie formula, the nongeometric (3,0)+(0,3) Hodge structure, the integral Betti functors, Z[√-5] | Statements only. The paper itself labels (1), (2) and (5) as applications of Howe, Ogus/Cartier and Milne. |

The run's own record:
- The whole joint-torsor theorem has a clean-context statement-only re-proof, frozen before target access (review 04).
- The five ancillary main families were reconstructed separately (10:02 UTC).
- 128 rows are accepted; about 58 are still open.

### Paper 4. "Canonical caps, plumbing and algebraic questions in Grothendieck's conformal surgery" (33 pp.)

| Statement | My check |
|---|---|
| Thm 1.1, a positive cap determines all lengths, cusps included | **Targeted proof check, confirmed.** Both developing maps are w^{ia_i} on the common cap, so dF_2/F_2 = r·dF_1/F_1 on the universal cover. Faithful free holonomy of rank at least 2 preserves no pair {0, ∞}, so F_1 has a simple zero or pole at an ordinary point, and r = ±1. Then F_2 = cF_1^{±1}, and the double-pole coefficients (1 + λ^2)/2 agree at every mark. A short and clean proof. |
| Thm 1.5, rank one does not imply a line bundle; R = Z[x,y,z]/(x^2+yz-1) | **Targeted proof check, confirmed.** P = ker(σ-1) ≅ coker(σ-1). At m = (2, x-1, y, z), σ - 1 ≡ 0, so P/mP = F_2^2 and P is not invertible. The repaired hypotheses are proved: a Dedekind base, or 2 invertible and Spec R connected. |
| Thms 1.2-1.4, radius map, limits and jets; Thms 1.6-1.7, comparisons and algebraic counterexamples | Statements only. |

The run's record:
- The radius theorem has a complete separate re-proof (review 05).
- The full 352-row inventory was finished at 10:02 UTC, without blanket acceptance.
- The nodal-q test and the abelian-fourfold input remain conditional, and are stated as hypotheses.

### Paper 5. "The genus of Grothendieck's relative-position surface" (41 pp.)

| Statement | My check |
|---|---|
| Thm 1.1, X_2 ≅ #^{n+1+4Σk c_{2k+1}} RP^2 | **Targeted check of the counting, confirmed.** χ = F(1) - F'(1) - b. With F(-1) = 1 - n and F'(-1) = b this gives χ = 1 - n - 4Σ k c_{2k+1}. Hand case, three generic lines: F = 4 + 6t, b = 6, χ = -2. I did **not** read the local surface topology (closed cells embed, vertex links are 4-cycles). The run has a fresh separate statement-only proof of it, with full comparison. |
| Thm 1.2, 23 and 47 crosscaps | The arithmetic is checked. c_3 = 4 and c_3 = 10 were not recomputed by me; the run has a fresh enumeration and a 15-case sign test. |
| Thms 1.3-1.4, identities and the extension-complex comparison | Statements only. Sturmfels-Ziegler 1993 is credited. |

Open in the run: C.06 (identity with Grothendieck's unspecified gluing) and a fresh generator of endpoint pairings.

### Paper 6. "Grothendieck's tensor divided-power categories and cellwise dessins after Mulase and Penkava" (31 pp.)

Not read in full: main statements only. Thm 1.5 (2) is the standard criterion "perfect = pseudo-coherent + bounded Tor amplitude at closed points". The dessin theorem rests on Mulase-Penkava's classification, which the run now credits in the title. The run accepts all 43 rows, with re-proofs by the same model. What remains is reconciliation and the program citation.

### Paper 7. "Grothendieck's interval supports and oriented maquettes, after Jenča and Björner" (45 pp.)

Not read in full: main statements only. The run records one refutation with refinement: SA21 extension uniqueness. Open gates: the contre/atelier bridge, primitive carriers, incidence/infinite admission, the published page of Jenča's Corollary 4.5, and final main-proof completeness.

### What is settled and what is still moving at checkpoint 12

**Settled** (accepted by the run and stable since several reviews):
- Paper 1 Thms 1.1-1.2 and most of Paper 1.
- The Paper 3 main table and its counterexample.
- Paper 2 Thm 12.2 and the all-field comparison A.160.
- The Paper 4 single cap and radius map.
- The Paper 5 counting, genus and examples.
- Paper 6 (43/43).
- Paper 7: the finite interval theorem, event domains and oriented maquettes.

**Moving:**
- Paper 2: the collar main theorem (definition fix pending), B082, the King comparison, the text of the TOP-PL interface.
- Paper 3: about 58 open rows.
- Paper 4: the cap/algebra independence, the 310 unmapped rows.
- Paper 5: C.06 and the pairing generator.
- Paper 7: the remaining partial or absent rows.

## 2. Corrections to published work

**(a) Bhowmik-Pathak, Theorem 1.11: CONFIRMED.**
- Source: arXiv:2408.00271v1 (1 Aug 2024), p. 3; proof §3.5, pp. 17-18.
- Counterexample: τ = i, f = E_4, g = j, F_0 = 1 + E_2E_6/E_4^2 = 2 - 1008q + …. E_6(i) = 0, so F_0(i) = 1, and the field has trdeg ≤ 2 < 3.
- Failed step: §3.5 proves only that the chosen values are algebraic over Q̄(E_2, E_4, E_6)(τ). The equality of transcendence degrees needs E_2(τ) back, which requires some f_r(τ) ≠ 0 with r ≥ 1.
- Repair: add k ≠ 0 and the condition that some f_r(τ) ≠ 0 with r ≥ 1. I checked the proof, including the generic-point argument for values of modular functions.
- Already known? v1 is the accepted version ("to appear", and it thanks the referee). The published text (Acta Arith. 218 (2025), 1-23) was not seen. No erratum was found (search of 23 Nov).
- Verdict: **report**. Draft 1 is in EMAIL_DRAFTS_POLISH_TOPOLOGY_PERIODS.md. It asks the authors to compare with the published wording.

**(b) Elliott, the conjectured nonflat Int(D): CONFIRMED.** This is not an error in a proof: it answers a conjecture he recorded as open.
- Source: arXiv:1109.3921v1, p. 2. There is only v1 and no journal reference.
- Result: by Theorem 12.2 both rings have Int(D) projective, and in fact free.
- Already known? Not in Ma 2604.05922 (a two-branch nonflat example answering CFFG Problem 19), nor in the Rethlas paper 2605.25259. The Cahen-Chabert book, the text of CFFG Problem 19 and Elliott's later papers have not been opened.
- Verdict: **report, after that literature gate.** Draft 2 is in EMAIL_DRAFTS.

**(c) Jenča, Corollary 4.5 of "Orthogonality spaces associated with posets": NOT READY.**
- The run derived an unbounded V-poset counterexample against the preprint's unrestricted singleton-closure wording (arXiv:2206.08113v1, p. 8; v1 is the only version).
- The publisher's abstract of Order 40 (2023) says "bounded". The published page of Corollary 4.5 has not been seen, and the run has not routed this item to CORRECTIONS_FOR_AUTHORS.md.
- No draft. Gate: the Order page. If the published corollary already says "bounded", there is nothing to report.

The third item in CORRECTIONS_FOR_AUTHORS.md (`paper07_event_domain_prefetch_correction.md`) is internal to the run and goes to no author.

## 3. Corrections to our own work

Paths are those inside the prompt's ZIP (`ours/…`). No edits were made.

1. **RESEARCH_SA07, B.4.1** (`ours/RESEARCH_SA07/RESEARCH_SA07/sections/B.tex`). The equalizer of two comparison sections was claimed normal. That is true only under both global centralizations and compatibility; an unconstrained equalizer can fail to be normal.
   - Edit: add those hypotheses to B.4.1 and mark the original clause as refuted (CROSSWALK row 74; P03-C31/C32/C34/C35).
2. **RESEARCH_SA22, the corollary of 67/091 as first read.** The eigenspaces of an involution on R^2 are not line bundles in general (Paper 4, Thm 1.5).
   - Edit: replace the hypothesis "connected, no 2-torsion" by "Dedekind base, or 2 invertible and Spec R connected", and cite the counterexample R = Z[x,y,z]/(x^2+yz-1), σ = (x y; z -x).
3. **RESEARCH_SA21, SA21-B-extension-unique** is refuted (P07-ROOT-EXT-REFUTE).
   - Edit: replace it by SA21-B-extension-Zorn (existence) and SA21-B-deployment-unique, and note that uniqueness of the deployment diagram does not give uniqueness of the realization.
4. **RESEARCH_SA21 credit.** The general Boolean-neighbourhood theorem for orthosets is Jenča, Order 43 (2026), art. 11, Thm 3.2, p. 5. It is not ours.
   - Edit: wherever SA21 presents it as new.
5. **Credits in Paper 6 and RESEARCH_SA09.**
   - The walking-complex equivalence for targets with kernels is in Hua's Hexagon compilation 2611.00125v2, pp. 165-166.
   - The dessin classification's combinatorial core is Mulase-Penkava (1998).
   - Edit: SA09's B3.1 and A2.2 should credit them, as the paper now does.
6. **Page locators in our citations.** In cotes 18, 119, 137, 151, 154 and 156-9 the archive footer numbers and the PDF page numbers differ by one.
   - Edit: every earlier SA07, SA09, SA10, SA11, SA20 and SA21 citation of those cotes should give both numbers, as the new papers do.
   - Bühler's cancellation is Proposition 7.5 in the 2008 version, not the number our earlier records give.
7. **Paper 5, line 40 of main.tex (abstract)**, in the run's own text: "Earlier material was checked by Claude Opus 5.5" names no effort.
   - Edit: "by Claude Opus 5.5 at effort max", as line 1085 already says.

## 4. What is new against the literature (main theorems)

- **Paper 3.** The refutation of Grothendieck's strong-transcendence prediction (cote 18, sheet 11) and the joint-torsor table. The prediction is unpublished, so its refutation is new as such.
  - The mechanism (real Frobenius makes the conjugate filtration rational) is elementary and close to Brown-Dupont's single-valued comparison, which the run credits.
  - The table is a Tannakian stabilizer computation; I know of no published equivalent. The run's search covers André, Ayoub, Huber-Müller-Stach, Kontsevich-Zagier and Bost-Charles.
- **Paper 2.**
  - Projectivity (freeness) of Int(R) for finite-conductor one-branch rings appears new and answers Elliott's recorded conjecture, subject to the literature gate in §2(b).
  - The branch criterion appears new and is topical alongside Ma 2026.
  - The torus concordance obstruction is known input (Hatcher-Wagoner, Igusa); its use against cote 119 is new.
  - King 1985 is still not compared.
- **Paper 4.** The single-cap theorem appears new.
  - Gate: compare with the literature on infinite grafting and meromorphic projective structures (Gupta 2014; Gupta-Mj, Adv. Math.; Dumas). I do not see it in the run's literature record.
  - The radius map credits Strebel/Liu and Fırat.
- **Paper 5.** The genus formula appears new. Sturmfels-Ziegler (the extension space is a 2-sphere) is the known input, and the run's search of the oriented-matroid literature found no match.
- **Paper 1.**
  - Thm 1.1 and Thm 1.4 are known in substance (Stacks; exodromy).
  - Thm 1.2 (an explicit linear counterexample to gluing by the prescribed incidence pieces) is new as an answer to cote 151, but elementary.
  - The other main theorems were not compared by me.
- **Papers 6 and 7.** Refinements of known cores (Mulase-Penkava, Hua's compilation, Jenča, Björner), which the run credits exactly.

## 5. Hexagon readiness

The five tests: complete / self-contained / stable / checked / of interest now. HOW.md box 8 is now a section headed "Proof overview": **no paper of this run has such a heading** (grep over all seven main.tex files). Every candidate below needs it in its write-up.

| Candidate | 1 | 2 | 3 | 4 | 5 | Gate left |
|---|---|---|---|---|---|---|
| **H-a. Int(R) is free for every finite-conductor subring of a DVR with finite residue field; Elliott's two conjectured nonflat rings are free** (Paper 2, Thm 12.1-12.2 and Cor 15.5; also SA20 in the HEXAGON_CANDIDATES back catalogue) | pass | pass: elementary inputs, plus Milnor patching and Kaplansky | pass: accepted, and nothing running will change it | pass: the run's targeted check and frozen reconstruction (P02-RG-I001), plus my full targeted check | **strong**: Ma 2026 and the Rethlas paper put Problem 19 in view now | **One gate: the literature search** (Cahen-Chabert book, CFFG Problem 19 text, Elliott's later work). Then a 4-6 page standalone note with the HOW boxes and a "Proof overview". The branch criterion could join only after an independent check of necessity. **Flag to the user.** |
| **H-b. A counterexample to Grothendieck's strong transcendence conjecture, and the joint-torsor dimension table** (Paper 3, Thm 1.1 and Cor 1.2) | pass | pass: André's motivated category, cited | pass for these two statements; other Paper 3 rows are still moving, but they do not touch them | pass: the run's frozen statement-only re-proof, my targeted check, and my independent elliptic computation | good: the archive audience; Grothendieck's own question "alors ?" | Extract a short paper (the 84-page paper is far beyond the main theorem). Add the "Proof overview" section. Quote the manuscript at cote 18, PDF p. 11. |
| **H-c. One canonical cap determines every boundary length** (Paper 4, Thm 1.1) | pass | pass: elementary Schwarzian and holonomy arguments | pass | partial: my targeted check, and the run's "independent residue proof" (ledger 01:45); its re-proof event should be confirmed in CHECK_EVENTS | moderate | Literature comparison with infinite grafting (Gupta; Gupta-Mj; Dumas); a standalone write-up. |
| H-d. The genus of the relative-position surface (Paper 5) | the local topology is not read by me | pass (Sturmfels-Ziegler) | pass, except C.06 (identity with the source surface) | the run: fresh separate local proof and certificates; mine: counting only | moderate | A Claude targeted read of the local-topology proof; c_3 recomputed by an independent program. |
| H-e. The Bhowmik-Pathak correction | — | — | — | — | — | Not a post: it goes to the authors (§2). |

## 6. What a successor or finishing prompt needs

1. **Box 8.** Every paper needs a section headed "Proof overview". None has one; the prompt as sent did not require the heading.
2. **CHECK_EVENTS taxonomy.**
   - Paper 2 carries six events with types outside the six allowed ones, for example "fresh build, final three passes and all affected-page visual verification". They should be re-typed, or moved to a QA log, since a build or visual check is not a check event on a statement.
   - The model field is written in about a dozen variants; normalize it to "GPT-6 Astra (ChatGPT Pro mode)".
3. **Paper 2.**
   - Repair the rigidification definition ("identity on the base"), then finish the held collar main theorems (A101-A112) and B082.
   - Obtain King 1985 (Topology Appl. 20, 149-160) and finish the A.205 comparison.
4. **Paper 7.**
   - Obtain the Order 40 (2023) page of Jenča's Corollary 4.5. If the unrestricted wording survives there, route the V-poset counterexample to CORRECTIONS_FOR_AUTHORS.md with its proof. If the page says "bounded", record that and drop the item.
5. **Paper 3.** Finish the roughly 58 open rows. The finishing prompt should allow the main paper to be split: a short paper on the conjecture (Thm 1.1, Cor 1.2), and the elliptic and arithmetic material separately.
6. **Paper 4.**
   - Literature on infinite grafting and the meromorphic projective-structure monodromy (Gupta-Mj) for the single-cap theorem.
   - Record its separate re-proof as a check event.
7. **Effort naming in the papers' notes on method.** Paper 5's abstract says "Claude Opus 5.5" without effort. The run writes "effort not exposed by runtime" for itself; the notes on method should say that.
8. **Corrections file.** The Elliott note is a resolution of a conjecture, not a correction of an error, and should be titled so.

Since every hourly review so far records movement, no finishing prompt is needed while the run is alive. These items go into the prompt that follows its final return, according to the standing rule: running threads are unreachable after one to two hours.
