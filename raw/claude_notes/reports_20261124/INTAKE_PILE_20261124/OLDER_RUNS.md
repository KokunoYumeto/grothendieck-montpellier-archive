# OLDER_RUNS: older results that never became a Hexagon note (intake pile, 24-25 Nov 2026)

Written 24 Nov 2026 by agent a24b3bc642b5dfddf (Claude Opus 5.5 at effort high), launched by the main session 329fb1e6
(Claude Opus 5.5 at effort max). The user, 24 Nov ~22:5x UTC: [the user's words, omitted] Briefs followed: `BRIEF.md` and `TOPICALITY_BRIEF.md` in this folder. Rows: `OLDER_RUNS.tsv`. Notes:
`<local>/Documents/agent_notes/a24b3bc642b5dfddf_NOTES.md`. Nothing in any run folder was changed; no git.

**Scope.** (1) The Hexagon board of record (`field_experts/hexagon/HEXAGON_BOARD.tsv`; `HEXAGON_CANDIDATES.md` is its
history): every candidate not posted, with its stage, and which of them no pile cluster covers. (2) Research results
older than the pile's runs: the Dérivateurs runs of 10-17 Nov (TOTAL_ASPHERICITY, CATHOT, POLES, GALOIS, STRATA, PATHS,
TOTEX2 = TOTAL_EXACT_2, TOTEX, PRETOT, INDLOCAL, DER_FOLLOWUP, FINMON), the early Longue Marche runs (LM1 and its rerun,
LM3, LM3b, LM8_LIE_APPROXIMATIONS, EXIT_ONE_TYPE), RESEARCH_SA11, the archive sweeps 1-2 (Claude's horizontal sweeps,
`results_register/horizontal/sweep1`, `sweep2`), and the October ChatGPT Pro answers to Claude's open questions (Q01-Q41,
F01-F14), which the register lists as "older candidates". Left out: posted notes, the S6 series, Codex's runs,
SAT_WITNESS*, SAT_KRONECKER*, prompt 74.

**Models.** Every run below is GPT-6 Astra (ChatGPT Pro mode); the October answers (22-25 Oct) predate 24 Oct and so ran
at reasoning effort ultra by the standing default. Checkers are named with their effort as their records give it.

**Topicality searches made (for all items).** (a) The whole Hexagon catalogue through its API, 1,530 works from
2609.00001 (1 Sep) to 2611.00999 (24 Nov), titles and abstracts, dump and grep script in my scratchpad
(`older_runs/hex_all.json`, `hg.py`): no work on Singer / L²-Betti numbers / aspherical, on filtered, exact or totally
aspherical categories, Isbell, Oberst, Adámek, localizers or derivators, Bowditch, convergence groups or dendrites,
Voiculescu or clock-and-shift, bondage numbers, Kan-Thurston, or tangential / cuspidal sections other than our own.
(b) The OpenAI repository `openai/math` (752 preprint folders listed through `gh api`, `history.md` read): no
generalization of the Singer preprint and nothing on the categorical items. (c) Web searches (standard and extended) per
item, named in each entry. The arXiv API returned HTTP 429 (rate limit) all evening, so arXiv was reached through web
search and abstract pages only.

---

## A. Worth a paper now, ranked

### 1. Degree-one Singer vanishing in every dimension n ≥ 3 (Q02, October answer)

**What.** Statement E of `pro_batch_20261022_open_questions/answers/Q02-solution.tex` (l. 60-70): for a finite
connected aspherical integral Poincaré complex Q of formal dimension n ≥ 3, any orientation character,
b₁⁽²⁾(Q̃) = b₍ₙ₋₁₎⁽²⁾(Q̃) = 0 (also b₀ = bₙ = 0, b_p = 0 for p > n); hence for every closed aspherical topological
n-manifold. Behind it, the group criterion (Thm `thm:group`, l. 86-91): a finitely presented torsion-free one-ended group
with H²(Γ; F₂Γ) = 0 and no splitting over a finite or two-ended subgroup has b₁⁽²⁾ = 0; corollary for finitely presented
integral PD(n) groups, n ≥ 3. The proof is OpenAI's finite-energy-boundary argument from *The Singer conjecture in
dimension four* (25 Sep 2026), reproduced and audited, with its Section 2 replaced by reductions R1-R5 valid in formal
dimension n. The only dimension inputs are n − 1 > 0, n − 2 > 0 and n − 1 ≥ 2 (mod-2 duality gives
H¹(Γ;F₂Γ) = H²(Γ;F₂Γ) = 0 and H¹(Γ;F₂[Γ/ℤ]) = H_{n−1}(ℤ;F₂) = 0).

**Why it matters.** Singer's conjecture is a standard open problem (Davis-Okun Conj. 0.3; Kirstein-Kremer-Lück 2025
Conj. 4.1). Degree one is the first case; n = 3 was known only through geometrization (Lott-Lück 1995), n = 4 is OpenAI's
September result, and n ≥ 5 was open: Di Cerbo-Hunter-Thrasher, arXiv:2601.08804 (Jan 2026), study "a potential
counterexample to the Singer conjecture in degree one" (abstract page opened). The PD(n)-group form is the statement
group theorists want, and the n = 3 case becomes geometrization-free.

**Checks.** One referee report, Claude Opus 5.5 at effort max (Message Batches API), 23 Oct 2026:
`F:\user\Documents\claude_open_courses_20260926\plan\pro_checks_20261023\Q02-check.md` (not reopened here; verdict: proved
with fixable gaps; "the dimension-independence claim itself is sound"; open: Bowditch Lemma 1.4 and the Treelike
citations only paraphrased; Section 9 spot-checked). Earlier, Claude read OpenAI's four-dimensional manuscript twice
(hub LOGBOOK 11-12 Oct; every Bowditch statement compared). **New here (this agent):** targeted proof checks of the
whole replacement Section 2 (Lemmas `found:model`, `found:reduction`, `found:duality`, `found:ends`, `found:trees`):
no gap; and the referee's main open citation closed: Bowditch, *Connectedness properties of limit sets*, Lemma 1.4,
opened in the author PDF (`Free or receipted/free/authors/bowditch/bhb-connected.pdf`, p. 6), says exactly (B) of
l. 711-721; *Treelike structures* Theorem 5.23 and Lemma 6.5 (`bhb-treelike.pdf`) say what l. 727-729 use. Events:
`INTAKE_Q02_20261124_CHECK_EVENTS.tsv`. Not checked by anyone since October: Sections 3-10 as reproduced (≈ 150 KB,
OpenAI's argument), and the Treelike citations of Section 6 (Thm 3.19, Lemmas 3.28, 3.34, 4.2-4.4, 6.8-6.11, Thm 6.1).

**Topicality: STILL NEW.** Searches: Hexagon catalogue (above); `openai/math` preprint list and history (only the
four-dimensional preprint); web search, extended, "first L2-Betti number vanishes aspherical manifolds all dimensions
Singer conjecture degree one 2026" and "'Singer conjecture in dimension four' OpenAI generalization all dimensions";
standard, "'PD(n) group' 'first L^2-Betti number' vanishes n ≥ 3" (found Fisher-Italiano-Kielak arXiv:2506.14666 on RFRS
PD groups and fibring, which assumes RFRS; Avramidi-Okun-Schreve on branched covers; neither gives degree one in
general); DCHT 2601.08804 treats degree one as open. The public prior observation is the Reddit remark of
u/Apprehensive_Sand951 (r/math, 10 Oct 2026), conditional, no proof: it must be credited, with OpenAI for the method.

**Worth a paper now: yes.** A theorem the L²-invariants community wants, with a complete written proof in hand. Gates:
an independent read of Sections 3-10 (or a line-by-line comparison with OpenAI's preprint, which we have read twice);
the Section 6 Treelike locators (the PDF is local); the write-up crediting OpenAI and the Reddit observation. No Hexagon
entry. Not on the board: it should be added.

### 2. Filtered ⊊ exact ⊊ total ⊊ quasi-filtered: a total category whose abelian colimits are not exact (TOTEX2 with TOTAL_ASPHERICITY, PRETOT, DER_FOLLOWUP)

**What.** TOTEX2 A.1/A.3 (`derivateurs_companion_20261109/pro_prompts_max_20261112_work/TOTAL_EXACT_2/checkpoints/TOTEX2_checkpoint_03_20261113T1144Z_unzipped/TOTEX2/sections/main_question.tex`,
labels `A:main`, `A:coefficients`): the category C_δ of ordered 3-uniform hypergraphs ([n], E) with
δ(U) = 2|U| − 3e(U) > 0 for all non-empty U, arrows the increasing induced embeddings with δ_Y(U) > δ_Y(fX) for
fX ⊊ U, is small, connected and **total** (colimits over it of simplicial sets are homotopy colimits; equivalently every
component of every category of elements is weakly contractible, TOTASPH C.5), yet the three vertex inclusions
v₁, v₂, v₃: V → W into the one-edge object have no affine equalizer over any non-zero ring: colim over C_δ is not exact
over ℚ nor over any F_p (D_R injective, coker of projective dimension one, T₁ = R). D.1 (`statements_sources.tex`,
`D:known-diagram`): among non-empty connected small categories, filtered ⊊ exact ⊊ total ⊊ quasi-filtered, witnessed by
Δ_inj (Isbell-Mitchell 1973), C_δ, and a repaired Adámek-Koubek-Reiterman category K*. D.2: Grothendieck's implication
"totalement W∞-asphérique ⇒ filtrante" (Les Dérivateurs II ms. 36ter) is false, and filtered ⇔ total and sifted (also
PRETOT F.3). With them: TOTASPH C.5 (the characterization of totality), C.13 (total ⇔ filtered when there is a weakly
terminal object, so Grothendieck's guess holds where he tested it), and DER_FOLLOWUP Part A (the finer tower is strict at
every level: A_n(F₂) ∈ 𝒬_n ∖ 𝒬_{n+1}, A.4: B A_r(Λ) ≃ K(Λ, r); A.13 for Δ_inj/K).

**Why it matters.** Exactness of colimits over a shape (Oberst; Isbell-Mitchell, *Exact colimits*, 1973) and
"colimit = homotopy colimit" are two classical weakenings of filteredness; C_δ separates them, which nobody had done, and
the four-term chain places Grothendieck's question at II ms. 36ter exactly. It is a clean statement for category
theorists and homotopy theorists, and the base on which the pile's FREX results (DERIVATEURS.md items 1, 2, 6) stand.

**Checks.** TOTEX2: intake by a5ead5c6 (Claude Fable 5.2 at effort high), `pro_intake_20261113/INTAKE_TOTEX2.md`,
13 Nov: 89 statements consistent, 47 proofs followed or recomputed, A.1 in full; referee reading of the main proofs by
afbbdefd (Claude Fable 5.2 at effort max), `DERIVATEURS_EXPERT/REVIEW_MAIN_PROOFS_TOTEX2.md`, 13 Nov: A.21, A.24,
A.30-A.34, C.25-C.28 correct, cited theorems checked at their sources (Evans-Hubička-Nešetřil 2019 Thm 2.6, Goerss-Jardine
IV.5.6, AKR 1981 pp. 375-387); D.1 stands. TOTASPH: every one of 107 items checked by a0a83137 (Claude Fable 5.2 at
effort max), 12 Nov (104 correct, 2 open, 0 wrong). PRETOT: review by abe075dc (Claude Opus 5.5 at effort max), 13 Nov.
DER_FOLLOWUP Part A followed in full by afbbdefd (Claude Fable 5.2 at effort max), 17 Nov
(`INTAKE_DER_FOLLOWUP_FINMON_20261117.md` §1). **New here:** an independent computation from the statement of A.1 only
(`OLDER_RUNS_checks/totex2_affine_equalizer_check.py`, `.out`): all 31,176 objects of C_δ with 3-7 points (31,178 with
the one- and two-point objects, the count the FRAISSE_EXACT drafter found independently on 13 Nov); none has an affine
equalizer of v₁, v₂, v₃ over ℚ, F₂, F₃, F₅. Evidence on small targets, not a proof. Event:
`INTAKE_TOTEX2_20261124_CHECK_EVENTS.tsv`.

**Topicality: STILL NEW** for the separation total ⇏ exact and the strict four-term chain; the inclusion
filtered ⊊ exact is Isbell-Mitchell 1973 Thm 3, and the characterization C.5 may be folklore in the homotopy-colimit
literature. Searches: Hexagon catalogue; web, extended, "category colimits of simplicial sets are homotopy colimits not
filtered 'exact colimits' Isbell Mitchell quasi-filtered Adámek totally aspherical" (found only Rosický, *On homotopy
varieties*, math/0509655, where "totally aspherical" is the other notion, of Grothendieck's test-category theory via the
diagonal: D homotopy sifted ⇔ D^op totally aspherical, so the paper must keep the two notions apart); web, "arXiv 2026
totalement asphérique / totally aspherical ... exact colimits abelian groups" (Hubert 2602.09674, Chirvasitu 2604.20554:
different questions). A specialist's look at the homotopy-colimit literature (Dwyer-Kan, Chorny, Raptis) for C.5 is
advised before claiming it.

**Worth a paper now: yes**, one paper "Exact colimits, total asphericity and filteredness" taking TOTEX2 A.1-A.3, D.1,
D.2, TOTASPH C.5, C.13, PRETOT F.3, DER_FOLLOWUP Part A, and the pile's FREX A.9-A.11, C.10-C.13 (their checks are in
DERIVATEURS.md). The proofs are in TeX in the runs; the companion repository grothendieck-derivateurs already carries the
material in another form. No Hexagon entry; not on the board.

### 3. Rational points in characteristic p separated by the prime-to-p fundamental group (H07; AN_GRH)

On the board at stage W; its run AN_GRH is in no pile cluster. Note written and read (`reports_20261123/h07_note/h07_note_v3.pdf`,
9 pp., by a2fedc2a, Claude Fable 5.2 at effort max; Steps 1-2 re-proved by a28ea31f, Claude Opus 5.5 at effort max;
Steps 3-6 line by line, Claude Opus 5.5 at effort max, 23 Nov). **Topicality: STILL NEW** as the board records; my
Hexagon catalogue search (1 Sep-24 Nov: "Saïdi", "Tamagawa", "prime-to-p fundamental", "separat* points", "cuspidal
section", "anabelian") finds nothing near it (the only "anabelian" hit, hexagon:2611.00419, is on bounded presentations in
Frobenioid theory). **Worth a paper now: yes** (it removes Saïdi-Tamagawa's exceptional set for rational points). Gates
as the board has them: Stix LNM 2054 ch. 7, Mochizuki's journal reference, the user's look.

---

## B. Not a paper now (checked, partly known, archive material, or still thin)

**H16, Grothendieck's tangential-section question (cote 149, scans 83-85; K17 cp08, `K17.tex` l. 13643-14090).**
Re-intake done here (events in `INTAKE_K17_20261124_CHECK_EVENTS.tsv`): F149-GENERIC (a section class over S is
geometric iff its generic pullback is; Hartogs plus all-exponent Kummer ramification), F149-UNMARKED-CURVE (an
automorphism of the full curve diagram over G_m multiplying π₁(S_Q̄) by u ∈ Ẑ^×, u₂ = 3, moves the section of tb off the
geometric set) followed in full; F149-BARE-EXTENSION re-proved; F149-MARKED-RECOGNITION followed with Mochizuki 1999
Theorems A, B carried. No gap. **Topicality: PARTLY.** Over a field the bare-extension statement is the packet structure
of cuspidal sections (Stix, *On cuspidal sections of algebraic fundamental groups*, 2012, which the run itself cites:
the geometric tangential classes are κ(K^×) inside H¹(G_K, Ẑ(1))); the relative statements over S and the marked
recognition are short consequences of Hartogs and of Mochizuki/Pop. Useful for the archive companion of cote 149, not a
paper on its own. The board's gate "intake read of the proof" is now met; the literature gate is answered as above.

**H06a (K17: what Alpöge's step 17 proves, log|K_4k(ℤ)| ≤ C(2k)^7).** Moving on the board; its successor line (KTOWER,
H18) is in the AG_POLISH cluster, and LITERATURE_20261124 records K_{4k}(ℤ) = 0 to degree 120 by Mok-Zheng
(hexagon:2611.00998) and to 104 by Pintar (2611.00829), both from Alpöge's step 17. **OVERTAKEN in its main use**; the
unevaluated-constant bound has no standalone interest now. No paper.

**The Dérivateurs answers to Grothendieck (POLES, GALOIS, STRATA, PATHS, CATHOT, BISITE's first round; 10-11 Nov).** 658
statements, no statement labelled Proved, Known or Refuted found false in seven reviews (Claude Fable 5.2, the earlier
ones at the session's default effort with none set at launch, the max-effort ones a0a83137 and afceadd4; summary in
`pro_reviews_20261110/7_BISITE/COMBINED_REVIEW.md`). The best of them: POLES F3-1 (every fibration condition of XVI §4
holds only for W∞ and Fl(Cat); the reverse cofibration axiom is the cofibre criterion, least solution W_ℤ; XII Théorème 2
and XVI Théorème 5.4 false as stated); F3-2 (Loc (7 F) ⇔ right properness ⇔ the localization is a nullification);
GALOIS B.3 (W_D^lc is a fundamental localizer for every derivator), B.10-B.12 (cardinal-controlled Kan-Thurston; small
ind-objects of Cat hot see only 1-types); the expert's own `RESULT_REVERSIBLE_NOT_STABLE.md` (a reversible localizer
not of the form R(L)), continued in REVLOC G.6-G.7 (pile). **Topicality: PARTLY / KNOWN in substance** for F3-2 (accessible
left-exact localizations versus nullifications: Cisinski, Astérisque 308, ch. 6, which the review itself cites, and the
modalities literature, Rijke-Shulman-Spitters); the rest are answers to questions in an unpublished manuscript, which the
companion already carries. **No separate paper**; candidates for the companion, and for one survey-type note "Grothendieck's
localizer axioms, settled" if the user wants one. The TOTASPH and PRETOT items that matter are in A.2.

**INDLOCAL (final 14 Nov), FINMON (cp20), the rest of DER_FOLLOWUP.** INDLOCAL: Kan-Thurston with no small quotients,
the representable types of Cat hot are 1-types for strict n-categories too (E.5-E.6), and a trivial cofibration between
countable posets with no strict retraction (D.19, resting on D.17); A.19 rests on an unrefereed 2026 OpenAI preprint.
Intake by a5ead5c6 (Claude Fable 5.2 at effort high), 14 Nov, mostly statement level. FINMON: 695 rows, statement level
only, C2-CP2 unresolved between 17 and 22 arrows. DER_FOLLOWUP Parts D, G (PRETOT F.10 answered no; W̃, W♯ refute XV
9.11-9.13 under Loc (1)-(3)) followed by afbbdefd (Claude Fable 5.2 at effort max). **Marginal; no paper now.** INDLOCAL
D.19 would need a full read of D.17 first.

**LM1 (rerun 12 Nov), LM3, LM3b (11-12 Nov).** Reviews by a9f76900, a4e7fde3, aac97df3 (all Claude Opus 5.5 at effort
max): 0 wrong. New mathematics is about Grothendieck's §§49-52 (LM1 N1: effective automorphisms of SL(2,ℤ)^ preserve the
congruence kernel; N5: a real error in the restricted quotient of §49.VI; N11: the positive-power theorem for linear group
schemes over every ring); LM3 §4.1 (his isomorphism (6) of scan 396 holds for every type, without the congruence
subgroup property). Many rows are Known. **Marginal: archive companion material, no paper.**

**LM8_LIE_APPROXIMATIONS (cp16, 13 Nov).** 167 rows; intake by a5ead5c6 (Claude Fable 5.2 at effort high), 32 proofs
read. Its results (pro-ℓ GT₀ ⊋ GT; F.15, F.21; A.22's invisible involution) are continued and superseded by LM8_PUSH,
which the LONGUE_MARCHE_A cluster ranks first (its item 1). **Covered there; no separate item.**

**EXIT_ONE_TYPE (13 Nov).** 63 statements, review by Claude Fable 5.2 at effort max (`pro_reviews_archive_20261112/EXIT_ONE_TYPE_REVIEW_FABLE/REVIEW.md`):
61 correct, 0 wrong; the review proved **Theorem R** itself: two good smooth projective normal-crossings completions of a
smooth complex threefold are joined by blow-ups and blow-downs along closures of strata (via toroidal weak
factorization). Theorem R has no second reader and rests on Svaldi 2019 and Kato's criterion, unopened. **UNSETTLED;
marginal** (it answers a question inside our own prompt); no paper now.

**RESEARCH_SA11 (cote 154, cp01).** Intake a6d42bf6 (Claude Opus 5.5 at effort max): χ(𝒳₂) = 1 − n − 4Σ k c_{2k+1}.
Superseded by POLISH_TOPOLOGY_PERIODS Paper 5 (board P91c, AG_POLISH cluster). **Covered there.**

**The October answers (Q-series), other than Q02.** Register: `recent_results_20261114/REVIEW_REGISTER_PRO_RESULTS_20261114.md`.
- **Q21** (exact distances of Voiculescu's clock and shift matrices from commuting unitary, normal and arbitrary pairs:
  sum 2cos(π/2n), 1, 1; maximum 2sin(π/4 − π/4n), cos(π/2n), cos(π/2n), all attained). One referee, Claude Opus 5.5 at
  effort max, 24 Oct: proved as stated. **PARTLY**: the answer itself says the sharp unitary lower bound is in Loring 2014;
  web search ("Voiculescu unitaries clock shift distance to commuting normal matrices exact value Loring Exel 2026") found
  only bounds (Dor-On-Hall-Kachkovskiy arXiv:2510.03674) and no exact normal or arbitrary values. A short note is
  possible after a second check (the closed forms can be tested numerically cheaply); low priority.
- **Q22** (Bowditch's Theorem 6.1 with infinite torsion, by a single cut-point orbit). One referee, Opus max, 24 Oct:
  proved as stated. **PARTLY**: Dasgupta-Hruska, arXiv:2204.02463, prove the relative version with finite-or-parabolic
  edge stabilizers and every global cut point parabolic with no torsion restriction (the answer says so). Not needed for
  Q02 (torsion-free). No paper now.
- **Q11** (the truncated octahedral graph has bondage number 5). **KNOWN BEFORE**: Srivastava's preprint (2 Sep 2026)
  and Yavari's cubic counterexample (10 Aug 2026), as the answer itself records. No paper.
- **Q03** (Pm|prec,p_j=1|C_max polynomial for every fixed m): dropped by the register (Jansen, arXiv:2611.09392, proves
  it with better bounds). **OVERTAKEN.**
- **Q12-Q16, Q23-Q24, Q27-Q28, Q34/F06, Q29/F02, Q40, Q41** (points in Illusie's *Complexe cotangent*, SGA 3, classical
  criteria by new routes): one referee each (Opus max), mostly proved as stated; several are already lessons. Useful
  to the courses, **not papers now**; Q40/Q41 would need a novelty search first. F07-F14 were never refereed.

**Archive sweeps 1-2 (Claude, 17-18 Nov).** Thirty reports in `results_register/horizontal/sweep2/REPORTS/` (index in
`WHAT_IS_WHERE.md`). Mathematical findings among them are corrections to his pages, each checked by its author (Claude
Opus 5.5 at effort max): his Proposition on 67/086 fails in characteristic 5 (five Klein groups share the octahedral set
P¹(F₅); `char5_67_086.md`, program `octa.py`); √3 for 3 on 67/098; XII Théorème 2 refuted (it gathers POLES G.2, B.7,
B.8); his "Contre-exemples pour la totale asphéricité" (157-3, scans 342-356) read against TOTASPH. **Archive notes, no
paper.**

---

## C. The board: every candidate not posted, by stage (generated from HEXAGON_BOARD.tsv, 24 Nov 13:35 UTC build)

Posted, left out: H01, H06b, H09, H17, H22, S20, H29, P90a, H29b, ZH3. Of the 99 others, only three come from runs no
pile cluster covers: **H07** (AN_GRH; entry A.3 above), **H16** and **H06a** (K17; part B). The rest are the cluster
readers' and the topicality agents' (H10 belongs to S6 and is left out).

The table below is the board as built; its "Gates left" column is the board's, not updated here except where part A or
B says so.

**W ready for the write-up (11)**

| Id | Line | Result | Gates left (board) | Source | In a pile cluster? |
|---|---|---|---|---|---|
| H02 | GCT | GCT VI's index hypotheses PH2, SH(a) and PH3 all fail for plethysm (P-F57, P-F19, P-F31), with the Theorem 1.6.1(d) erratum | literature search (Kahle-Michałek first; Hexagon); proof checks of PNEW-002 to 004 and the exterior identity if those a… | ALPOGE_GCT final; GCT_PLETH; GCT_POS final | yes (GCT_PLETH, GCT_POS) |
| H02b | GCT | Numerical PH3 (GCT VI, Hypothesis 3.3.4) fails for Kronecker coefficients: every positive form for g((s^n),(s^n),(s^n)) has a denominator weight of a… | literature search (Hexagon included); the self-contained text (P-F23, P-F27, P-F30 with proofs); the claim stops at the… | GCT_POS final | yes (GCT_POS) |
| H07 | anabelian | Rational points of curves in characteristic p are separated by the prime-to-p fundamental group, on a question of Grothendieck (cote 149, ms. pp. 17-… | Stix LNM 2054 ch. 7 (library; bears on what is known and credit, not on the proof); Mochizuki's journal reference and t… | AN_GRH final; reports_20261123/h07_note/ | **no** |
| H13 | GCT | Occurrence obstructions for per_n against det_n with no padding (A-030, A-034) | reframe per the pequalnp check (LMR + swarm L-gct-070/074 cited; 'best refereed' bound wording); literature search (Bür… | GCT_KRON final | yes (GCT_KRON) |
| H15 | CM points | Galois orbits of CM points in A_g: /Gal x/ >= c_g D_x^{1/(4g)}, explicit constants, all centre orders and products (A.ORBIT); effective Andre-Oort it… | the write-up with Jaswal's Prop 3.3 stated beside ours (needs a pass: effective André-Oort is Jaswal + Cureton-Thorner,… | NIGHT_AFTER_ALPOGE cp11 (Part A); ZETA_NEXT final | yes (NIGHT_AFTER_ALPOGE, ZETA_NEXT) |
| S12a | archive (cote 31) | The persistent A.2 counterexample to Grothendieck's margin question | literature (Hasse 1925, Schilling 1950); the locator: '31/085' is a PDF page, the archive sheet is 84; a 'Proof overvie… | RESEARCH_SA12 final | yes (RESEARCH_SA12) |
| S17a | crystalline | A counterexample to full faithfulness of crystalline Dieudonné theory (B:crystal-counterexamples) | literature search; the finished text | RESEARCH_SA17 cp12 | yes (RESEARCH_SA17) |
| S17b | archive (cote 133) | WG(BO_m) is a special lambda-ring exactly when m <= 2 or k contains Q | literature search with exact locators; the finished text | RESEARCH_SA17 cp12 | yes (RESEARCH_SA17) |
| S22a | archive (cote 67) | Grothendieck's (0,4) capping map is not onto; its image is 0 < /q/ < 16 (Koebe) | literature search; the finished text | RESEARCH_SA22 and run 2 | yes (RESEARCH_SA22) |
| S12d | characteristic two (cote 29) | An explicit characteristic-two wild genus-two example showing the formal-linearity hypothesis cannot be dropped (RESEARCH_SA12 rows 433-435); also D:… | the write-up (core: the run's D_wild_genus2_curve.tex, with a Proof overview); a Hexagon search for the topic; every pa… | RESEARCH_SA12 final | yes (RESEARCH_SA12) |
| S06b | abelian varieties | Jacobian summands of abelian varieties of dimension <= 3: s_J divides gcd(2, delta) for surfaces and gcd(6, delta) for threefolds (C.4i, j, m, n, p, … | literature search including Hexagon; every page read | RESEARCH_SA06 final | yes (RESEARCH_SA06) |

**G1 one gate (15)**

| Id | Line | Result | Gates left (board) | Source | In a pile cluster? |
|---|---|---|---|---|---|
| H03 | complexity | The border rank of det_4 and of per_4 is at least 43 over C, and at least 42 over every field | the 25 border-apolarity cases checked independently; the finished text | BR_PENCIL final | yes (BR_PENCIL) |
| H04 | archive (cote 44) | Grothendieck's cote 44 Th. 5 fails as displayed; corrected by one term per singular fibre | scan-004 image check; the finished text | HODGE_SIGN; SIGN_NEXT final; JAC1964 | yes (HODGE_SIGN, JAC1964) |
| H14 | GCT | Four-row multiplicity obstructions under padding; the gaps exist exactly when n^2 <= 2m^2 - m + 1 (m >= 17) | reframe per the pequalnp check (LMR + swarm L-gct-070/074 cited; 'best refereed' bound wording); literature search (Dör… | CUE_GCT final | yes (CUE_GCT) |
| GPK18 | GCT (Kronecker, polytopes) | The largest vertex-denominator (determinant) order of the n-fold Kronecker tensors is 2^(n-1+floor((n-2)/7)), not 2^(n-1), with smooth density-one fi… | compare with Kravtsov's work on vertex denominators of axial three-index assignment polytopes (may contain the order gr… | GCT_POS cp03 | yes (GCT_POS) |
| S14a | archive (1964) | Counterexamples to Grothendieck's 1964 programme: his Th. 5 fails in codimension 2 (J5), with J2a, J2b and J6C | coordinate with H11 (JAC1964) | RESEARCH_SA14_SA19 cp08 | yes (RESEARCH_SA14_SA19) |
| S14b | various | G1 (literature gate); A3 (certificate rerun); F11: every metabelian quotient of the local pi_1 is finitely generated | literature; F11 also test 2 (the Krishna-Majumder preprint) | RESEARCH_SA14_SA19 cp08 | yes (RESEARCH_SA14_SA19) |
| S15 | archive (8.3) | Grothendieck's admitted integral crystalline weak Lefschetz (8.3) fails in degree one on products of the OC chain, and holds for degree d >= p^2 - p … | a forward literature search (is the crystalline torsion failure folklore?); test 2: rational crystalline weak Lefschetz… | RESEARCH_SA15 cp37; POLISH_CRISTAUX cp12 (Paper 1) | yes (POLISH_CRISTAUX, RESEARCH_SA15) |
| S23b | archive (cote 1) | The Hilbert trace formula proved in Grothendieck's hand | open the printed sources | RESEARCH_SA23 final | yes (RESEARCH_SA23) |
| S07b | Hodge (computability) | A non-computable non-geometric Hodge pair whose period is built from the halting set (C.1.5) | literature search | RESEARCH_SA07 cp12 | yes (RESEARCH_SA07) |
| S15b | archive (cote 4, 8.6) | Cote 4's question 8.6 for plane curves in characteristic 2: the monodromy on the theta characteristics is reducible for every odd degree d >= 5 (full… | literature search including Hexagon (characteristic-2 theta-characteristic monodromy of plane curves) | RESEARCH_SA15 cp37 | yes (RESEARCH_SA15) |
| S07c | Longue Marche (LM6 A.22) | The open CM common-kernel case of LM6 A.22: for E0: y^2 = x^3 - x minus its origin, no nontrivial closed procyclic subgroup of the common kernel of a… | literature: the published characterization (Nakamura 1994 Thm 2.1.1) needs the normalizer to act through the cyclotomic… | RESEARCH_SA07 cp12 | yes (RESEARCH_SA07) |
| S15e | Cristaux | A reduced counterexample to Grothendieck's extension assertion, after Ferrand-Raynaud and Olberding (C-RD4, C-RD11; Paper 4 of POLISH_CRISTAUX) | a 'Proof overview' section; the run's final | POLISH_CRISTAUX cp12 (Paper 4) | yes (POLISH_CRISTAUX) |
| P91a | transcendence | A counterexample and a dimension formula for Grothendieck's strong transcendence conjecture (18:11): the dimension table (Thm 1.1) and the counterexa… | cut out as a short standalone paper; literature | POLISH_TOPOLOGY_PERIODS cp12 (Paper 3) | yes (POLISH_TOPOLOGY_PERIODS) |
| H25b | Hodge (HODGE_FINISH) | Integral Gaussian Hermitian lattices of determinant class [-3]: every pairing-integral Z[i]-lattice of signature (3,3), class [-3], embeds isometrica… | literature search (Hermitian lattice classification over Z[i]: Jacobowitz, Kirschmer); otherwise part of Paper A | field_experts/intake_20261121/intakes/HODGE_FINISH/INTAKE_HODGE_FINIS… | yes (HODGE_FINISH) |
| ZH4 | zeta zeros (ZETA_HEAT) | The complete local multiplicity partition for heat-flow Newton determinants: ord_(t=0) det[S_(u+v)(t)]_(u,v<k) = sum_(j<=k) b_j, recovering every mul… | our proof check | field_experts/intake_20261121/intakes/ZETA_HEAT/INTAKE_ZETA_HEAT_2026… | yes (ZETA_HEAT) |

**G2 two or more gates (34)**

| Id | Line | Result | Gates left (board) | Source | In a pile cluster? |
|---|---|---|---|---|---|
| H16 | archive (cote 149) | Grothendieck's tangential-section question (scan 85): yes with the marking of scans 83-84, no without it | intake read of the proof; literature | K17 final | **no** |
| H18 | K-theory | K_4k(Z) = 0 for k <= 20 (K_12 to K_80 new), given Alpöge's archive theorems | #print axioms on a compiled build (OneCharU_s chain incl. Keep.levelKA_alt with hH.toClassicalTheorems); the KMSW backg… | K17 final; KTOWER cp09; NIGHT_AFTER_ALPOGE cp11 (Part C) | yes (KTOWER, NIGHT_AFTER_ALPOGE) |
| H20 | GCT | A complete positive formula for every outer-degree-five plethysm coefficient (G-036 with T-037) | proof checks; literature | GCT_PLETH final | yes (GCT_PLETH) |
| H21 | GCT | Polynomial-size formulas for stable hooks with varying outer degree (G-037 to G-039), and G-040's, polynomial for each fixed b (its literal construct… | proof checks; literature | GCT_PLETH; GCT_POS | yes (GCT_PLETH, GCT_POS) |
| S06 | archive (1965 letter) | The 1965 letter's conjectures modulo algebraic equivalence: exactly when they hold over C; the Jacobian-summand bounds | literature; a re-proof of the C.4 bounds | RESEARCH_SA06 final | yes (RESEARCH_SA06) |
| S22b | SGA 2 | The cone over Sigma RP^2 refutes SGA 2 XIII §6 Conjecture A (local Hurewicz) | check the quotation against SGA 2's text; literature | RESEARCH_SA22 run 2 | yes (RESEARCH_SA22) |
| S23a | EGA | EGA corrections: 0_IV 19.3.12 restored (wrong proof, true statement; confirmed); the III 4.3.6 and IV 20.1.3 counterexamples are already published (E… | scope the package to what is not published; a 'Proof overview' section | RESEARCH_SA23 final | yes (RESEARCH_SA23) |
| S22c | schemes | A non-separated, non-noetherian pair where degree-zero comparison holds but H^1 comparison with Z/n fails | check C:Goldman-branches; an independent re-proof; literature | RESEARCH_SA22 run 2 | yes (RESEARCH_SA22) |
| S15c | archive (cote 4, 8.6) / abelian surfaces | Abelian surfaces at p = 2: the monodromy group in degree one is GL_8(F_2) on the supersingular product E x E for all odd degrees (thm:ss-all-odd-full… | the Coble identification lemma (unchecked); thm:ss-all-odd-Hasse at full depth; literature search including Hexagon | RESEARCH_SA15 cp37 | yes (RESEARCH_SA15) |
| S15d | archive (cote 4, 8.5.8) | The unit-root rank of the vanishing cohomology is positive once the degree is large (thm:all-X-explicit-positive-rank: the missing 'n° 7' of 8.5.8); … | literature search (generic ordinarity, Illusie 1990, Ekedahl) including Hexagon; an independent re-proof | RESEARCH_SA15 cp37 | yes (RESEARCH_SA15) |
| S12c | archive (cote 29) | D:boundary-neighborhood settles the one-point case of D.2(ii) (a finite set of points is not covered in general); the B.2 stabilization chain for Pic… | an independent re-proof; literature; for B.2 a re-proof of B.2u | RESEARCH_SA12 final | yes (RESEARCH_SA12) |
| H25 | Hodge | The Hodge conjecture for abelian varieties is equivalent to a Poincare-pairing bound on the multiplier (bounded cycle degrees on reductions of CM poi… | the finishing prompt 70c's fixes (Voisin state of the field, title and abstract, Proof overview, why it matters, Markma… | HODGE_BOUNDED_CYCLES final (prompt 70) | yes (HODGE_BOUNDED_CYCLES) |
| P90b | AG | The Igusa surface in the ordinary case: Pic^tau flat for every Artinian deformation (contradicts claims of Chai, Chai-Oort and Partsch) | an independent re-proof; read Chai's note directly | POLISH_ALGEBRAIC_GEOMETRY cp12 (corrections) | yes (POLISH_ALGEBRAIC_GEOMETRY) |
| P91b | conformal | One cap determines all lengths: the single-cap theorem of Grothendieck's conformal surgery (Paper 4, Thm 1.1) | comparison with the infinite-grafting literature (Gupta, Gupta-Mj, Dumas); the run's separate re-proof recorded as a ch… | POLISH_TOPOLOGY_PERIODS cp12 (Paper 4) | yes (POLISH_TOPOLOGY_PERIODS) |
| P91c | topology | The genus of Grothendieck's relative-position surface (cote 154), with the 23 and 47 crosscap counts | a read of the local topology proof; an independent recount of c_3 | POLISH_TOPOLOGY_PERIODS cp12 (Paper 5) | yes (POLISH_TOPOLOGY_PERIODS) |
| H30b | Alpoge (ALP_MACHINE) | Abelian coefficient fields cannot carry normalized ideal generators: K imaginary quadratic with mu(K) = {+-1}, F/K finite abelian, J O_F = (xi) with … | literature search for Theorem A (may be known); read LIFT107-109; written as a section of the chain-length note (H30) | field_experts/intake_20261121/intakes/ALP_MACHINE/INTAKE_ALP_MACHINE_… | yes (ALP_MACHINE) |
| H25c | Hodge (HODGE_FINISH) | Obstructions to cycle constructions and criteria for Mumford's exceptional classes (Paper B, 88 pp.): if one specified quadratic Lie block is algebra… | open Bolognesi-Laterveer before the half-twist remark is posted; a check of the overview; page view | field_experts/intake_20261121/intakes/HODGE_FINISH/INTAKE_HODGE_FINIS… | yes (HODGE_FINISH) |
| P91d | conformal (POLISH_TOPOLOGY_PERIODS) | Removing a collar from a hyperbolic surface with geodesic boundary: the conformal factor solves Delta u = e^{2u} - 1, d_n u = k_g; constant-width cut… | targeted check of the positivity and sign-change proofs; literature (grafting, Fenchel-Nielsen deformations); a short n… | field_experts/intake_20261121/intakes/POLISH_TOPOLOGY_PERIODS/INTAKE_… | yes (POLISH_TOPOLOGY_PERIODS) |
| P90f | AG (POLISH_ALGEBRAIC_GEOMETRY) | Adjoint and tangent-line bigness for surfaces in characteristic p (Paper 2, the very-ample section: curve-genus lemma; numerical obstruction through … | literature search | field_experts/intake_20261121/intakes/POLISH_ALGEBRAIC_GEOMETRY/INTAK… | yes (POLISH_ALGEBRAIC_GEOMETRY) |
| P90g | AG (POLISH_ALGEBRAIC_GEOMETRY) | Over every base, a projective bundle over an abelian torsor is a scheme only if the torsor is | the proof read | field_experts/intake_20261121/intakes/POLISH_ALGEBRAIC_GEOMETRY/INTAK… | yes (POLISH_ALGEBRAIC_GEOMETRY) |
| P90h | AG (POLISH_ALGEBRAIC_GEOMETRY) | On a normal surface, an algebraically trivial p-torsion line bundle trivial on a curve Y with Y^2 > 0 never reaches conductor equality (Thm positive-… | the run's isolated reconstruction (stability); literature: Esnault 2006 (partial connections for p-torsion line bundles… | field_experts/intake_20261121/intakes/POLISH_ALGEBRAIC_GEOMETRY/INTAK… | yes (POLISH_ALGEBRAIC_GEOMETRY) |
| P91f | algebra (POLISH_TOPOLOGY_PERIODS) | A non-Noetherian inclusion R in S with every polynomial tensor map an isomorphism (a unique plethory) but Omega(R,S) and S not flat: flatness is not … | literature (Elliott's plethory papers, Borger-Wieland, Stacks 06RH); an independent re-proof of the colon identity; a s… | field_experts/intake_20261121/intakes/POLISH_TOPOLOGY_PERIODS/INTAKE_… | yes (POLISH_TOPOLOGY_PERIODS) |
| P91g | topology (POLISH_TOPOLOGY_PERIODS) | The three-sphere: pi_2 P_TOP(S^3) = Z/2 while pi_2 P_PL(S^3) = 0, a concrete PL/TOP concordance discrepancy | a Claude targeted read; literature (Hatcher's Smale conjecture, Kirby-Siebenmann) | field_experts/intake_20261121/intakes/POLISH_TOPOLOGY_PERIODS/INTAKE_… | yes (POLISH_TOPOLOGY_PERIODS) |
| P91h | topology (POLISH_TOPOLOGY_PERIODS) | pi_0 P_PL(M) = E(M) for compact PL M of dimension >= 6, without a smoothing (a PL form of Hatcher-Wagoner-Igusa) | a Claude read; comparison with Burghelea-Lashof-Rothenberg and Pedersen (may be known) | field_experts/intake_20261121/intakes/POLISH_TOPOLOGY_PERIODS/INTAKE_… | yes (POLISH_TOPOLOGY_PERIODS) |
| A133a | archive (cote 133; NIGHT_GROTHENDIECK_Q… | Grothendieck's question on cote 133, scan 29, answered no and classified in the curvilinear case: characteristic 0 is necessary; locality and K_0 = Z… | Cor. 27.3 and Thm 13.1/19.1 read in full; the external inputs (Burke-Walker, Blumberg-Gepner-Tabuada) at their locators… | field_experts/intake_20261121/intakes/NIGHT_GROTHENDIECK_QUESTIONS/IN… | yes (NIGHT_GROTHENDIECK_QUESTIONS) |
| AM112 | Alpoge's interface (ALP_MACHINE) | K imaginary quadratic with mu(K) = {+-1}, G in Cl(K) odd of order g: a field in which every J in G has a generator xi with /sigma xi/^2 = NJ for all … | literature search; LIFT112 A/C and LIFT113 proof reads | field_experts/intake_20261121/intakes/ALP_MACHINE/INTAKE_ALP_MACHINE_… | yes (ALP_MACHINE) |
| S15n | Cristaux (abelian surfaces, characteris… | Eventual defect two for every mixed pair of abelian surfaces in characteristic two, without the finite-field-model and index-zero hypotheses; a Picar… | a proof check; the run's open quantitative items | field_experts/intake_20261121/intakes/POLISH_CRISTAUX/INTAKE_POLISH_C… | yes (POLISH_CRISTAUX) |
| P91k | real algebraic geometry (POLISH_TOPOLOG… | Coarsest embedded smooth partitions exist for every semialgebraic set but depend on the embedding (the compact cusp) | literature (Whitney stratification, smooth-locus results) | field_experts/intake_20261121/intakes/POLISH_TOPOLOGY_PERIODS/INTAKE_… | yes (POLISH_TOPOLOGY_PERIODS) |
| ZH5 | zeta zeros (ZETA_HEAT) | An all-window lower rate for the Weil form: a_1(L), a_2(L) >= exp{-C mu^(1/d_MT) log mu (1 + log log mu)}, mu = e^(2L), d_MT = 0.83625...; improves t… | a proof check; the credit split with Mori; open Voss | field_experts/intake_20261121/intakes/ZETA_HEAT/INTAKE_ZETA_HEAT_2026… | yes (ZETA_HEAT) |
| ZH6 | zeta zeros (ZETA_HEAT) | Collision laws for the CUE heat flow: the first collision is Weibull-3/2; early collisions are Poisson with intensity (3/2) sqrt(v); the adjacent lab… | a whole-proof check | field_experts/intake_20261121/intakes/ZETA_HEAT/INTAKE_ZETA_HEAT_2026… | yes (ZETA_HEAT) |
| S93a | complexity (fleet) | Exact count /E/ + tau - 1 for edge functions of bipartite C4-free graphs among circuits whose formal monomials have at most one distinct variable of … | 647 read live by fork 2 (672ae3a0, Claude Opus 5.5 at effort max, 24 Nov 11:50 UTC): still a conjecture, 0 attempts, no… | field_experts/intake_20261121/intakes/SPLIT_ZERO_AFTER_FGJM/INTAKE_SP… | yes (SPLIT_ZERO_AFTER_FGJM) |
| S93c | foundation (with H22) | Semimodules over every inverse semiring are module diagrams for (Q, F); K_0(R_0) is free on connected labelled posets (93 paper 1) | H22 v3's two false sentences: FIXED in v4 (24 Nov); literature on Clifford semimodules; a second reader for the other c… | field_experts/intake_20261121/intakes/SPLIT_ZERO_AFTER_FGJM/INTAKE_SP… | yes (SPLIT_ZERO_AFTER_FGJM) |
| S93d | GCT | The rank-four order of the nonstandard Hecke algebra is free after inverting M exactly when 6 divides M; generic rank 114 (93 paper 5) | an independent check; comparison with GCT IV 11.8 | field_experts/intake_20261121/intakes/SPLIT_ZERO_AFTER_FGJM/INTAKE_SP… | yes (SPLIT_ZERO_AFTER_FGJM) |
| S93e | operator algebras | K_1 of the semilocal one-zero C*-algebras: nonsplit boundary sequence exactly for two or more primes; every finite torsion order with four odd primes… | a reader of paper 3 | field_experts/intake_20261121/intakes/SPLIT_ZERO_AFTER_FGJM/INTAKE_SP… | yes (SPLIT_ZERO_AFTER_FGJM) |

**M moving (16)**

| Id | Line | Result | Gates left (board) | Source | In a pile cluster? |
|---|---|---|---|---|---|
| H06a | K-theory | What Alpöge's step 17 proves: log/K_4k(Z)/ <= C(2k)^7 | Soulé comparison; the exponent-7 chain; a re-proof at l = 2 | K17 | **no** |
| H12 | Hodge | Bounded division for Weil classes (HD-U) for every imaginary quadratic K and every n, with explicit constants; the ghost-class dichotomy | literature search; the finished text; HODGE_DIVISION still running | GHOSTS final; HODGE_DIVISION cp10-cp16 | yes (HODGE_DIVISION) |
| H19 | Hodge | Bounded division for split Q(omega) Weil eightfolds from published inputs | full read of D-G34-04 to 06; the run's final; literature | HODGE_DIVISION | yes (HODGE_DIVISION) |
| NEG | complexity and zeros | The parity of #SAT is a Hasse-Witt scalar (computing it is ⊕P-hard); one sparse smooth cubic whose class encodes #SAT; the CUE first heat collision i… | proof checks; literature; the run continues | NEG_NIGHT cp04 | yes (NEG_NIGHT) |
| S15h | Cristaux | Sharp ramification thresholds of Barsotti-Tate groups for every e prime to p, with central p^2 rigidity (Paper 2 of POLISH_CRISTAUX); final of 23 Nov… | the merge of the two threads (the 92 final and 92b, cp18 or its final); a full-chain check by a different model | field_experts/intake_20261121/intakes/POLISH_CRISTAUX/INTAKE_POLISH_C… | yes (POLISH_CRISTAUX) |
| AC219 | Selmer (cubic Kummer, ALP_CONNES) | Strict 7-adic Selmer groups of a cubic Kummer twist family over Q(sqrt-3), L = K(cbrt 269): S_7(K, (E/O)(chi^j xi_7^a c_7^-e)) = O/7^{s(e)}, s(e) >= … | replay the class-group certificate Cl(L) = C_7^2 in a second system; check steps 6-8; literature (Iwasawa-theoretic lif… | field_experts/intake_20261121/intakes/ALP_CONNES/INTAKE_ALP_CONNES_20… | yes (ALP_CONNES) |
| ZH1 | zeta zeros (ZETA_HEAT) | Under Alpoge's theorem, simplicity of the zeta zeros is equivalent to an exact growth rate of the finite positivity tests (Toeplitz minors / Jensen p… | check of the local Hermite/orbital part; comparison with Shi (2026) and Griffin-Ono-Rolen-Zagier; the run's final; the … | field_experts/intake_20261121/intakes/ZETA_HEAT/INTAKE_ZETA_HEAT_2026… | yes (ZETA_HEAT) |
| S15i | Cristaux (cote 8:49) | Grothendieck's two Lubin-Tate lattices agree exactly when e <= p; the extremal exponents are max(0, e-p) and the tangent images always agree (POLISH_… | a different-model re-proof; literature (Kisin-Ren, Pham, Lau); the merge of the two threads (the 92 final and 92b, cp18… | field_experts/intake_20261121/intakes/POLISH_CRISTAUX/INTAKE_POLISH_C… | yes (POLISH_CRISTAUX) |
| S15j | Cristaux (cote 8:81) | The least rank of a local system with a non-split co-Lie complex is 4, 3, 2 for p = 2, 3, >= 5, realized on surfaces (the Z/p^2-lifting obstruction; … | full check of thm:surface; literature (Bergh-Rydh, ABM); the merge of the two threads (the 92 final and 92b, cp18 or it… | field_experts/intake_20261121/intakes/POLISH_CRISTAUX/INTAKE_POLISH_C… | yes (POLISH_CRISTAUX) |
| S15k | Cristaux (inertia characters) | The complete next wild band for the special inertia character: nu_min = v + 2 on the whole band 2 <= k <= p^2, p not dividing k, every v >= 0 (v + 1 … | the merge (92c); a full check of the midpoint exclusions and of the three carried inputs by a model other than GPT-6 As… | field_experts/intake_20261121/intakes/POLISH_CRISTAUX/INTAKE_POLISH_C… | yes (POLISH_CRISTAUX) |
| S15l | Cristaux (hypersurface sections) | Full mod-2 monodromy groups GL_8(F_2) and GL_80(F_2) for hyperplane and cubic sections of the supersingular cubic square (POLISH_CRISTAUX Papers 20, … | proofs read and certificates rerun independently; the merge of the two threads (the 92 final and 92b, cp18 or its final) | field_experts/intake_20261121/intakes/POLISH_CRISTAUX/INTAKE_POLISH_C… | yes (POLISH_CRISTAUX) |
| P90e | AG (POLISH_ALGEBRAIC_GEOMETRY) | Picard kernels on surfaces in characteristic p: X smooth projective surface, Y a smooth very ample curve, L nontrivial of order p trivial on Y => 2g(… | a018e2d2's read of the three lemmas; a literature pass; the run's final | field_experts/intake_20261121/intakes/POLISH_ALGEBRAIC_GEOMETRY/INTAK… | yes (POLISH_ALGEBRAIC_GEOMETRY) |
| S15m | Cristaux (Grothendieck's weak-formal H^… | Grothendieck's weak-formal H^1: rigid rationally with no lift needed, torsion-free integrally (it injects into the rational theory), with infinite to… | the merge (92c); a check of the torsor and site proofs by a different model | field_experts/intake_20261121/intakes/POLISH_CRISTAUX/INTAKE_POLISH_C… | yes (POLISH_CRISTAUX) |
| A133b | archive (cote 133; NIGHT_GROTHENDIECK_Q… | Regularity criterion for lattice generation: for A finite free local over any mixed-characteristic DVR with edim(A/pA) <= 1, the map Phi_A (the trivi… | Cor. 27.3 and Thm 13.1/19.1 read in full; the external inputs (Burke-Walker, Blumberg-Gepner-Tabuada) at their locators… | field_experts/intake_20261121/intakes/NIGHT_GROTHENDIECK_QUESTIONS/IN… | yes (NIGHT_GROTHENDIECK_QUESTIONS) |
| P91j | topology (POLISH_TOPOLOGY_PERIODS) | A surjective Casson-Sullivan homomorphism for oriented 3-manifolds with finite pi_1; vanishing on T^3; the concordance component group of RP^3 | a Claude targeted read; comparison with Galvin 2026 and OPR 2026 at locators; a short note | field_experts/intake_20261121/intakes/POLISH_TOPOLOGY_PERIODS/INTAKE_… | yes (POLISH_TOPOLOGY_PERIODS) |
| S15o | Cristaux (abelian surfaces, characteris… | Reduced Hasse divisors and natural GL_8 blocks in every cubic-theta degree: all-degree structure for Frobenius on the sections /3d Theta/ of ordinary… | the merge (92c); the proofs checked by a different model; the full eventual image (open) | field_experts/intake_20261121/intakes/POLISH_CRISTAUX/INTAKE_POLISH_C… | yes (POLISH_CRISTAUX) |

**N note to an author (13)**

| Id | Line | Result | Gates left (board) | Source | In a pile cluster? |
|---|---|---|---|---|---|
| H10 | S6 | Biró's Conjecture 1 contradicts Louvel's first moment of Salié sums | only if Biró wants a citable note | S6_05 A.5.7 | S6 (left out) |
| H23 | GCT (erratum) | GCT VIII: Conj. 3.2 as printed has no minimum (N-012); the Positivity conjecture's unimodality clause fails at r = 3; the printed b2 has the wrong si… | independent re-run of P-F-E3-01; literature; a draft note to Mulmuley first, on the user's word | E4_RANK_FOUR; GCT_POS N-012 | yes (GCT_POS) |
| S07 | transcendence (erratum) | A counterexample to Bhowmik-Pathak 2024, Thm 1.11: at tau = i, E6 vanishes and the transcendence degree drops to 2 | check the Acta Arithmetica version (it may be corrected); a draft note to the authors first, on the user's word | RESEARCH_SA07 cp12 | yes (RESEARCH_SA07) |
| S15g | Cristaux | Erratum: Grammatica, arXiv:2507.08568v2, Remark 4.6, p. 29: the last conclusion (H^i_et(X,Z_p) = H^i_cris(X/W(k))^{F=1} for X proper over a perfect f… | the user's word on the drafted email | POLISH_CRISTAUX cp12 (corrections) | yes (POLISH_CRISTAUX) |
| P90c | AG | Errata to published work: Stacks Tags 07BV (x_r for x_d, twice) and 0BTP (an fppf lemma for an fpqc step); Popescu 2022 p. 510 claims (a) and (c) fal… | the user's word on the drafts; Liedtke after a look at his printed table | POLISH_ALGEBRAIC_GEOMETRY cp12 (corrections) | yes (POLISH_ALGEBRAIC_GEOMETRY) |
| P90i | AG (erratum) | Zheng, arXiv:1509.04993 (v1), Cor. 4.4 fails in characteristic 5: a minimal surface of general type with ample L = O(S+F), (5^2-1)L - K ample, and H^… | the run's final; the e-mail (draft folded into the planned P90a notice), on the user's word | reports_20261123/p90a_note/EMAIL_DRAFT_Zheng_20261123.md | yes (POLISH_ALGEBRAIC_GEOMETRY, via the P90a note) |
| P90j | AG (erratum) | Mukai, RIMS-1736: in the proof of Prop. 3.2, L should be L^-1 throughout; in Case 3(d), b_2 = 2, not 6, for hyperelliptic and quasi-hyperelliptic sur… | the e-mail (draft folded into the P90a notice), on the user's word | reports_20261123/p90a_note/EMAIL_DRAFT_Mukai_20261123.md | yes (POLISH_ALGEBRAIC_GEOMETRY, via the P90a note) |
| P90k | AG (erratum) | Esnault, math/0608203v1, Section 2: Lemma 2.2's first map is injective only when omega_L has zero annihilator; Prop. 2.5's residue map is ill-defined… | the e-mail (new draft), on the user's word | reports_20261123/p90a_note/EMAIL_DRAFT_Esnault_20261123.md | yes (POLISH_ALGEBRAIC_GEOMETRY, via the P90a note) |
| P91i | topology (erratum) | Boyle-Chen, Rev. Mat. Iberoam. 2024, Thm A.6: the displayed generator (r,theta,y) -> (r,theta+pi y,y) does not fix the top end, and the group has ord… | the e-mail (draft in EMAIL_DRAFTS_POLISH_TOPOLOGY_PERIODS.md), on the user's word; not a post | field_experts/intake_20261121/intakes/POLISH_TOPOLOGY_PERIODS/EMAIL_D… | yes (POLISH_TOPOLOGY_PERIODS) |
| A15c | archive (cote 15) / CM | Over a CM centre, the central model exponents of isogeny descent are the multiples of a.t.s with s in {1, 2} (central models: those over F_(p^n) with… | the e-mail (draft intakes/NIGHT_GROTHENDIECK_QUESTIONS/EMAIL_DRAFT_Thakur_20261123.md, pending the run final), on the u… | field_experts/intake_20261121/intakes/NIGHT_GROTHENDIECK_QUESTIONS/IN… | yes (NIGHT_GROTHENDIECK_QUESTIONS) |
| P91l | topology (erratum) | Galvin, Compositio Math. 162 (2026) 2496-2544: Lemma 4.9 (p. 2526) states the Steenrod-square vanishing the wrong way round; Prop. 2.23 (p. 2508) nee… | open pp. 2508 and 2526; the e-mail (Draft 4), on the user's word | field_experts/intake_20261121/intakes/POLISH_TOPOLOGY_PERIODS/EMAIL_D… | yes (POLISH_TOPOLOGY_PERIODS) |
| P91m | topology (erratum) | Orson-Powell-Randal-Williams, Smoothing topological pseudo-isotopies of 4-manifolds (accepted, J. reine angew. Math., 31 Oct 2026): Remark 8.2 (p. 25… | open Definition 5.8; the e-mail (Draft 5), on the user's word | field_experts/intake_20261121/intakes/POLISH_TOPOLOGY_PERIODS/EMAIL_D… | yes (POLISH_TOPOLOGY_PERIODS) |
| S93b | GCT | GCT VIII (arXiv:0709.0751v2), rank-three section, 'Positivity': the unimodality assertion fails in both sign readings, on a constant printed in the p… | E-MAIL SENT to K. D. Mulmuley 24 Nov 11:54 UTC (reports_20261124/EMAILS_SENT_20261124.md, no. 6); the draft's 'Section … | field_experts/intake_20261121/intakes/SPLIT_ZERO_AFTER_FGJM/INTAKE_SP… | yes (SPLIT_ZERO_AFTER_FGJM) |

**H held (2)**

| Id | Line | Result | Gates left (board) | Source | In a pile cluster? |
|---|---|---|---|---|---|
| H11 | archive (cote 44) | Grothendieck's 1964 Th. 4 for abelian varieties in every characteristic | test 2: it rests on OpenAI 032 and Milne's report (unrefereed) | JAC1964 final | yes (JAC1964) |
| H05 | GRH (Masullo) | RH for every CM motive, under Masullo's claim | Masullo's proof refereed | ZETA_TWO CM01 | yes (ZETA_TWO) |

**X not a post (8)**

| Id | Line | Result | Gates left (board) | Source | In a pile cluster? |
|---|---|---|---|---|---|
| GPK08 | GCT (Kronecker) | Triple-rectangular Kronecker series have the plethysm-type dyadic pole at n = 4 and n = 5: simple poles at the primitive 8th roots of unity (residue … | absorbed in H02b: the poles at n = 4, 5 are its small-rank theorem (prompt 56, A2) | GCT_POS cp03 | yes (GCT_POS) |
| S05 | archive (cote 12) | The explicit global class of Grothendieck's F_p gerbe | the gerbe results are Milne's (the polish run withdrew its Paper 6; the intake agrees); withdraw the novelty claim | RESEARCH_SA05 | yes (RESEARCH_SA05) |
| S12b | characteristic p | R^1 f_* O_X = 0 in characteristic p without resolution (L6c) | known: Ishii-Yoshida Cor. 1.4 and Li-Wang Cor. 4.6 (the polish paper cites them as such); withdraw the novelty claim wh… | RESEARCH_SA12 final | yes (RESEARCH_SA12) |
| H08 | archive (cote 123) | Grothendieck's 1969 prediction to Kostant fails in sp4 | known: Richardson 1987, Lemma 5.1 | ALPOGE_BRIDGES | yes (ALPOGE_BRIDGES) |
| H27 | Connes | Connes's trace formula over Q (explicit cutoff) is equivalent to GRH for Dirichlet L-functions (T51); finite prime-built approximants of Xi/Xi(0) wit… | a written comparison with Connes 1999 section VIII and Connes-Consani-Marcolli; a check of the analytic inputs T25-T43;… | ALP_CONNES cp41 (prompt 55) | yes (ALP_CONNES) |
| H30 | Alpoge | The chain length forced by the size hypotheses of Alpoge's proof (the chain-length theorem); f is the degree of the totally real subfield, the CM fie… | NOT USEFUL as a post (the user, 23 Nov ~13:1x: 'It contributes very little'): parts 2-3 are two-line consequences of fi… | NIGHT_AFTER_ALPOGE cp11 (Part B); SEED_ALP_MACHINE | yes (ALP_MACHINE, NIGHT_AFTER_ALPOGE) |
| S15f | Cristaux | Grothendieck's Frobenius-stable Lefschetz formula (8.5.1) for every smooth ample divisor, and the unit-root count (Paper 3 of POLISH_CRISTAUX) | known in substance (Ogus 1975, Lemma 4.8, Thm 4.9, Cor 4.11; Katz-Messing): an exposition, not a post | POLISH_CRISTAUX cp12 (Paper 3) | yes (POLISH_CRISTAUX) |
| ZH2 | zeta zeros (ZETA_HEAT) | A trace certificate for simplicity of the zeta zeros below a given height: E(T) <= (T^2/2) D_N (prop:trace-height) | a proof check; the run's final | field_experts/intake_20261121/intakes/ZETA_HEAT/INTAKE_ZETA_HEAT_2026… | yes (ZETA_HEAT) |

Posted (left out): H01, H06b, H09, H17, H22, S20, H29, P90a, H29b, ZH3

---

## D. Files of this pass

- `OLDER_RUNS.tsv`: one row per candidate of parts A and B (run, item, statement, proof locator, checks, usefulness,
  topicality verdict with evidence, worth a paper now, Hexagon status).
- `INTAKE_Q02_20261124_CHECK_EVENTS.tsv`, `INTAKE_K17_20261124_CHECK_EVENTS.tsv`, `INTAKE_TOTEX2_20261124_CHECK_EVENTS.tsv`:
  the checks made here.
- `OLDER_RUNS_checks/`: `totex2_affine_equalizer_check.py` and `.out` (the C_δ computation); `board_section.md` (part C,
  generated).

**For the board (the main session's to enter):** add Q02 (stage G1/G2: the Sections 3-10 read and the Treelike locators)
and the TOTEX2 hierarchy paper (stage W once the FREX parts are scoped); mark H16's proof-read gate met and its
literature gate answered PARTLY (archive note); mark H06a overtaken in its main use by Mok-Zheng and Pintar.
