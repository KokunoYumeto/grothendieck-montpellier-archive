# B.1–B.4: proof report and integration notes

AI-produced by GPT-6 Astra (OpenAI, ChatGPT Pro mode), agent `/root/homotopy_levels`, 2026-11-19. Effort is not separately exposed. No priority is claimed.

## Outcome table

| Item | Outcome | Statements |
|---|---|---|
| B.1 | The unrestricted uniform pro-tube assertion is false. The exact necessary-and-sufficient pro-tube criterion is proved, and compact conical tube hypotheses are verified sufficient. | B1.1–B1.5 |
| B.2 | The ordinary-topos bicategorical principle is false. The correct infinity-topos shape theorem is known and derived explicitly; the actual A.1 cover diagrams satisfy higher descent stage by stage. Quinn's geometric hypothesis is separated from the formal theorem. | B2.1–B2.4 |
| B.3 | The exit-path equivalences hold under the stated paracompact, local singular-shape, conical and ACC hypotheses. Every truncation level is proved with a finite-stratum induction; groupoid stacks and the complete gerbe calculation follow. Unrestricted conical bases are refuted by the one-stratum Cantor example. | B3.1–B3.3 |
| B.4 | The prompt's inference from R5 is false: a full groupoid span of aspherical pieces suffices in the two-stratum case. The full flag assembly formula is proved, including the exact coherent groupoid reduction for aspherical pairwise incidence links. | B4.1–B4.3 |
| L2 | False as stated. A holink fibration omits Quinn tameness; arbitrary ordinary-topos bicategorical colimits do not preserve shape. Correct replacements are stated and proved/derived. | B2.1–B2.3 |
| L3 | Correct after the exact hypotheses and truncation convention are supplied. A link's fundamental group and the fundamental group of an exit mapping space are different levels of data. Gerbes are a subproblem of general constructible stacks. | B3.1–B3.3 |

## Deliverables

- `B_levels.tex`: 15 numbered statements, typed constructions, proofs, counterexamples, edge cases and exact citations.
- `RESULTS_B.csv`: one row per numbered statement.
- `CHECK_EVENTS_B.tsv`: 29 check events, including earlier study IDs SA10-C3-04 through SA10-C3-07 and SA10-8.
- `B_references.bib`: ten opened primary references, with exact theorem locators and version qualifications.
- `code_B/check_B_finite.py` and output: finite checks described below.
- `code_B/download_sources.py` and output: source retrieval record.
- `code_B/write_B_records.py` and output: reproducible generation of the metadata files.

## Primary manuscript readings

Read directly the second-pass transcriptions of 151/027–044 and 151/057–061 on 2026-11-19. The mathematical conclusions on 151/035–043 do not depend on the doubt marks about typography, the category's name, or punctuation. In particular (18)'s direction, the invariants map, the sphere diagram and the explicit retraction of the feared groupoid-span failure on 151/041 are unambiguous in the supplied text.

The manuscript itself initially calls the tube a topos limit on 151/028. The task requires the repaired pro-object interpretation. The counterexample in B1.3 concerns this required pro-interpretation with actual local-system germs and morphisms represented at one stage. It is not a claim that a collapsed ordinary topos limit retains the punctured-neighbourhood information.

## Corrections and qualifications, with attached locations

All paths below are relative to the unpacked `sources/` directory, except the prompt.

1. `RESEARCH_SA10_study/study/STUDY.md:117`: the unrestricted equivalence of ordinary tube systems with constructible sheaves needs B1.5's extension and uniform morphism conditions. B1.3 gives a compact metric counterexample with infinite stalks. The inertia formulation also requires the surjectivity and connecting-map qualifications in B1.4.
2. The same file, lines 112–115: independently confirmed by the homotopy exact sequence in B1.4. This rechecks SA10-C3-04.
3. The same file, lines 120–121: independently confirmed in B2.4 (SA10-C3-05 and SA10-C3-06). Its category C is used contravariantly as a presheaf index; our covariant exit category is its opposite. Thus 'final' there and 'initial' here are consistent, not a mathematical contradiction.
4. The same file, line 125: for the constant abelian band, extensions must be central. A gerbe and a group extension are equivalent descriptions after basepoint/neutralization choices, not canonically identical objects.
5. The same file, line 126: independently confirmed in B3.3, including why changing either neutralization does not identify distinct elements of A (SA10-C3-07).
6. The same file, line 127: the unqualified colimit assertion is false in the ordinary 2-category of topoi, by B2.2. B2.1 states the correct infinity-topos theorem.
7. The same file, line 132: F is a category of representations of the homotopy exit category, not the exit category itself. B3.1 gives the exact equivalence. Lines 133–134 become correct under the stated hypotheses and finite truncation conventions (SA10-8).
8. `upload/PROMPT(20261119-040801).md:143`: its last sentence is false. R5 does not show that the groupoid span (8)/(10) is insufficient when all pieces are K(pi,1). B4.1 reconstructs the sphere as the homotopy pushout `* <- BZ -> *`. In `RESEARCH_SA10_transcriptions/transcriptions/second_pass_17Nov/MPL_151_032-075/MPL_151_032-075_151_scan041.tex:3-11`, Grothendieck explicitly withdraws that fear and distinguishes the failure of F.
9. The prompt, line 84 (L2): Quinn's Definition 3.1 has both tameness and a holink source-fibration condition. Fibration alone is not his entire condition; the Hawaiian-earring common point witnesses that distinction. Also, the formal shape theorem applies to infinity-topos colimits, not all ordinary bicategorical colimits.
10. The prompt, lines 85–88 (L3): set-valued sheaves retain pi_0 of exit mapping spaces, while groupoid stacks retain their pi_1. The pi_1 of a whole incidence link can still enter the set-valued description through its maps to stratum fundamental groups. These two uses of 'pi_1 of links' should not be conflated.
11. `RESEARCH_SA10_transcriptions/transcriptions/second_pass_17Nov/MPL_151_032-075/MPL_151_032-075_151_scan032.tex:16,19`: the running text has the normal fibre `V*_{z,Z}`, while display (11) has `V*_{z,X}`. We have not claimed a paleographic correction without the scan. Mathematically the local normal-model reading is the one that types correctly. The two readings differ in positive stratum dimension: for a line in the plane the normal link is S0, whereas the ambient point link is S1. The proof uses the normal-model reading, and the ambient-point reading is false in this example.
12. A source locator correction discovered during this run: Woolf's corrected arXiv v3 introduction still refers to Theorem 4.6 for constructible sheaves, but the actual body statement is Theorem 4.3, PDF p.15. The bibliography records the body locator. Miller's arXiv v1 holink theorem is 4.9, which differs from journal numbering quoted by Woolf.

## Primary sources opened and used

The complete URLs and opened annotations are in `B_references.bib`.

- Lurie, *Higher Algebra*, 18 September 2017: Theorem A.9.3, Corollary A.9.4, Remark A.9.7, Proposition A.9.16; Theorem A.7.1; recollement A.8.4/A.8.11/A.8.14; the finite-rank induction on printed pp.1463–1465. PDF opened online. Both local PDF download attempts returned HTTP403, which is recorded; this does not affect the opened web source.
- Lurie, *Higher Topos Theory*: shape §7.1.6, especially Remark7.1.6.15 and Example7.1.6.9.
- Treumann, arXiv:0708.0659: PDF and LaTeX source opened; Definition3.1, Theorems7.13 and7.14, introductory examples.
- Quinn, *Homotopically stratified sets*: Definition2.1, Lemma2.4 and its corollary, Definition3.1, Proposition3.2. PDF downloaded and text extracted. His mapping-cylinder topology is not the ordinary quotient topology. The final B2.3 proof therefore derives the ordinary homotopy-pushout statement independently, from actual numerable open covers and the fixed-tame pro-neighborhood/holink comparisons proved explicitly in C4.02. Quinn's controlled strict relative theorem remains cited with its own convention.
- Barwick–Glasman–Haine, *Exodromy*, arXiv1807.03281v7: Definition2.1.8, Lemma2.7.3, Theorem2.7.4, Definition4.2.1, Example4.2.3.
- Hoyois, *Higher Galois theory*: Proposition5.1, with hypercompletion explicitly retained.
- Miller, *Popaths and Holinks*, arXiv0909.1201v1, Theorem4.9.
- Woolf, arXiv0811.2580v3, Lemma3.5 and Theorem4.3: opened as background verification of the holink and set-level classification; not substituted for the full infinity-exodromy theorem.
- Ayala–Francis–Tanaka, arXiv1409.0501v6, Lemmas6.1.4 and6.1.7 and Theorem6.1.9. The primary abstract pages verified arXiv identifiers and versions.

## Computations and actual scope

`check_B_finite.py` ran in 0.091153 seconds. It verified C2 group operations, all eight associativity triples, and both inverses. The normalized bar complex through degree4 has differentials 0,2,0,2, giving H1(BC2;Z)=Z/2. It also checked the tetrahedral sphere with four vertices, six edges and four faces: the second boundary matrix has rank3, its fundamental cycle is (-1,1,-1,1), and the cochain (1,0,0,0) pairs to -1. Thus the Hopf-bundle coherence class is not a coboundary. These checks certify the finite algebra used in B2.2 and B4.3; they do not purport to certify the general theorems.

`download_sources.py` ran in 11.378 seconds. It obtained and unpacked the Treumann LaTeX source and downloaded the Quinn PDF; the HA403 failures were logged.

`write_B_records.py` ran in 0.000767 seconds and produced 15 result rows and29 check-event rows. Its purpose is metadata generation, not proof checking.

## Literature search and priority

No priority is claimed for any argument. Exact primary theorem locators were searched and opened rather than relying on the attached reading. Further searches used the queries 'locally constant sheaves germ neighborhood closed subset infinite stalk extension Hawaiian earring recollement', 'shape bicategorical pushout topoi classifying topos suspension group', and 'stratified space aspherical links fundamental groupoids homotopy colimit coherence'. No primary source for the two exact counterexamples B1.3 and B2.2 was located in those searches; their complete direct proofs are supplied. Searches for 'infinity category collage mapping cylinder pushout left fibration correspondence' and 'infinity category collage lax colimit correspondence Grothendieck construction universal property' are part of the additional C.1 proof assistance, not a priority claim.

## Integration caution

Do not apply B2.1 directly to an ordinary 2-Pro(Topos) colimit from A.1. Apply it to the honest full open-cover descent diagram at each synchronized neighbourhood stage. Do not exchange an infinite homotopy colimit with a pro-limit. The ordinary-topos counterexample is exactly why the distinction matters.

B4.2 distinguishes two meanings of 'links': all pairwise incidence links versus only each stratum's entire normal link. The latter does not imply pairwise asphericity; the three-stratum closed4-ball is an explicit witness. The full spatial flag diagram still reconstructs X; it reduces to groupoids exactly under the stated one-type condition.

No PDF has been independently published by this agent. The root owns integration, LuaLaTeX compilation, rendering and final storage.

## Additional C.1 assistance

`C1_collage_B.tex` gives four explicit lemmas/theorems for the full coherent Exit comparison: directed collage, the crossing-arrow left fibration, coherent inward transport of retained outer faces, and recursive cone-collar induction. It has been sent to the C agent for independent review and integration. `CHECK_EVENTS_C1_B.tsv` records these checks. The hypotheses deliberately include recursive compatible conical collars and proper stratified locally trivial source bundles; mere fibrancy is not asserted to imply them.

We visually inspected the primary cote150 PDF page43, rendered at2200px as `literature_B/cote150_scan043.png`. The main text really reads `p=long.d-prime`, whereas the margin says `d` is the set of maxima of `d1,...,dp`. Thus the mismatch is in the supplied manuscript scan, not an invented correction to an AI reading. For an arbitrary selected subflag the corrected count is `p=|d|`. The projection-chain index is `p+1`, resolving the supplied `p+1|p-1` doubt; the boxed equation below visually reads29.

Added an opened primary research citation for the classical gerbe classification used in B3.3: Ashwin Deopurkar, *Torsors and gerbes*, arXiv2305.15412v1, Theorem2.7 and Remark3.1. This supplies the precise H²/banded-gerbe and neutral-gerbe/torsor identifications; the sphere gluing and gauge quotient are proved directly.


## Final independent C audits

- `C4_path_proof_B.tex` supplies the full C4.02 proof with all relative paths allowed when bands overlap. The explicit path-shortening equivalence and endpoint-preserving radial-replacement homotopy are continuous in families and coherent under shrinking. The strict-holink version is false when the bands coincide.
- `C4_collar_proof_B.tex` repairs C4.05: fixed rectangles are not cofinal (for instance a tube may impose r1 < r0²). Actual control tubes with radius functions on their stratum bases are cofinal by proper closed-subtube maps. Their intersections are triangular varying-radius regions, each homeomorphic to the open resolved face times a cube. One natural projection proves the pro-equivalence. The proof derives the triangular coordinates from the full horizontal/vertical collar axioms of C2.05.
- `C4_remaining_audit_B.tex` makes C4.03 exact sheaf descent: in the interval hull, L is open, so choose all L-stratum neighborhoods inside it; their union is exactly X_L. It also records the local flabby/direct-image argument and normal-crossings identity-normal-derivative and positive-scaling precision for C4.06.
- `CHECK_EVENTS_C4_B.tsv` contains six independent audit events, one for each C4.01–C4.06.
- `C1_incidence_audit_B.tex` checks C1.04 completion using full chain-isomorphism groupoids, not only object replacement. It proves atlas independence by local sections, split augmented Čech diagrams and open-cover exit excision, and specifies globally pulled-back orbifold collar data.
- Haine, arXiv1811.01119v6 (27 March2023), Definition1.1.4 and Theorem1.1.7, printedp8, were opened independently. Their complete-Segal proof identifies flag décollages with conservative infinity-categories; this corroborates the C1.B2 category model but does not replace the geometric comparison. Bibliographic key B56Haine2023 is supplied by the B5–6 agent.
