# Prompt updates (main session, Claude Opus 5.5 at effort max)

The user, 16 Nov 2026: note the prompt updates I think are required; implement them myself when I am sure, or wait for a
Fable check; either way is fine. Every implemented change: backup of the PROMPT.md first, the push-rule lint after, and
a line here.

## Implemented

- **16 Nov ~00:4x UTC, LM 05_DELTA_ON_GT, item 2(b).**
  - Added: by Euler's pentagonal theorem eta = theta_{6,1}(tau, 0) - theta_{6,5}(tau, 0) =
    sum over n >= 1 of chi_12(n) q^{n^2/24}. So eta spans the chi_12-eigenline of the frame operators {1, 5, 7, 11}, and
    chi_12 is the character of {1, 5, 7, 11}/±1.
  - Prove or refute: on the multiplier-one subgroup, Delta = (1 - chi_12(a))/2, i.e. Delta = 1 exactly when the frame
    acts on eta by -1. Relate this to eta's multiplier system (Rademacher's Dedekind sums; Atiyah, Math. Ann. 278, 1987),
    and say whether the multiplier gives Delta a formula on all of GT-hat_0.
  - Why I am sure: the identity is classical. The Delta statement is put as prove-or-refute and only restates Lead 3(a)
    in a computable form.
  - Backup: longue_marche_pro_pilot_20261104/pro_prompts_draft_20261111_work/DELTA_ON_GT/
    PROMPT_before_eta_line_20261116.md.
  - `--lint-math` passes.

- **16 Nov ~01:2x UTC, LM 05_DELTA_ON_GT, item 2(b): consult lead C4.**
  - Replaced "say whether that multiplier gives Delta a formula on all of GT-hat_0" with prove-or-refute of aec1e030's
    lead: no function of the frame's class in the abelianization of the metaplectic group equals Delta (the E.58 frame
    lies in F'F^3, trivial in B^ab = Z/6, and has Delta = 1); Delta is the permutation part of the action of the
    central frame on eta in the Weil representation of index 6, and the phase part is the eta multiplier (chi_-4 on
    the centre separates 5 from 7).
  - Backup: .../DELTA_ON_GT/PROMPT_before_consult_lead_C4_20261116.md. `--lint-math` passes.

## Candidates (waiting for a Fable check or for reading)

- **aec1e030's C1-C3, for LM8_PUSH's successor (Part A) when it is written.**
  - C1: Goldstein's cusp etas of Gamma_0(4); kappa = Dedekind-sum differences; the order-4 character; A.6 as the
    Aut(E, O)-orbit of a tangential section. C1 could also go into the background of 02_SECTIONS_OVER_Q.
  - C2: Banerjee-Merel check of A.4's cusp divisor groups.
  - C3: the general A.3, i.e. Astra A1.
  - Text in research_maps_20261114/DEDEKIND_LM8_CONSULT/CONSULT_AEC1E030_20261116.md, section "Items for GPT-6
    Astra".

- **LM 02_SECTIONS_OVER_Q, background.**
  - lambda = theta_2^4/theta_3^4 = 16 eta(tau/2)^8 eta(2tau)^16/eta(tau)^24, and 1 - lambda likewise; Jacobi's identity
    is the unit equation.
  - A_s and B_s are Kummer classes of modular units on Y(2), with their archimedean side in the Kronecker limit formula
    at the three cusps.
  - Attach Banerjee-Merel for the cusp-divisor question.
  - Waits for F2.
- **LM 06_ANABELIAN_SUCCESSOR or a new item.** The general A.3 (Astra A1), with Banerjee-Merel and Zarhin as background.
  Waits for F1, and 06's scope still has to be checked.
- **LM 05_DELTA_ON_GT, item 2(c).** The elliptic Kashiwara-Vergne paper (dessins proceedings, p. 233) as a source for
  the genus-zero to genus-one step. I have to read it first.

## 16 Nov ~01:0x UTC
- LM 02_SECTIONS_OVER_Q was sent tonight without aec1e030's C1 (the candidate above): C1 moves to its successor.
- LM 05_DELTA_ON_GT was not sent tonight: R4 (CONSULT_AEC1E030_RAMANUJAN_20261116.md) and the chi_12 reading of NOTES
  §24 can go into item 2 before it is sent. Not implemented yet.

## 16 Nov ~03:3x UTC
- LM 05_DELTA_ON_GT was sent by the user after 01:40 UTC (first checkpoint filed 03:4x UTC). It went out with the eta
  line and consult lead C4, without R4 and without the chi_12 reading. Both are moot: the run's first checkpoint
  (A.2-L1) refutes the literal central-frame reading item 2(a) asked about, and R4 as worded fails anyway (a central
  element acts by a scalar on the irreducible rank-2 local system of E4^{1/4}). NOTES §30 (a). As-sent copy:
  longue_marche_pro_pilot_20261104/pro_prompts_draft_20261111_work/DELTA_ON_GT/PROMPT_as_sent_20261116.md (+ sha256);
  the folder moved to ALREADY_RAN.
- aec1e030's R1-R3 are now FOR_ASTRA A3 (R2, for the next S6 prompt) and A4 (R1 with the open half of R3: HMOZ proved
  the signature-2 and 3 identities, so only signatures 4 and 6 and the E4/E6/Chowla-Selberg expressions remain). R4 is
  moot (above). None is placed in a prompt yet: no unsent prompt fits them.

## 19 Nov ~11:45 UTC (Claude Opus 5.5 at effort max, agent a6d42bf6fe2b0d8a8, from the intake of RESEARCH_SA10)
- Why: RESEARCH_SA10 (stratified spaces, cotes 150-151; GPT-6 Astra, ChatGPT Pro mode, final 05:40 UTC) was taken in
  (results_register/horizontal/sweep3/SA10/INTAKE_RESEARCH_SA10_20261119.md). New results go as background into every
  unsent prompt they bear on.
- RESEARCH_SA11 (cote 154): backup PROMPT_before_SA10_results_20261119.md; added the attachment bullet, the files
  SA10_RESULTS_20261119.md (10 statements with status and checks) and SA10_final_paper_tex.zip (the paper's LaTeX and
  results register), and the section "Results of RESEARCH_SA10 that this prompt builds on" before the Leads. It settles
  and changes no item; it gives A4.1-A4.3 (embedding of the discs in the glued surface), A1.2, A1.5, B2.1-B2.2 (homotopy
  type from covers, not topos colimits) and C3.01, C3.04 (surface is a local criterion) as tools for A.1-A.2.
- RESEARCH_SA20 (built by ae4ae3dc): the same backup, files (31 statements plus the intake's INT-SA10-K10) and section;
  ae4ae3dc's items unchanged. Settled for A.6: the sheaf recollement of 039 (B1.1, A3.2; the derived six functors
  remain), the smooth Thom-Mather reconstruction as the known resolution theorem C2.05 (cite; what remains is matching
  041-047 to it, n strata in his form, PL and TOP), the groupoid data of 043 in general (B3.1-B3.2, B4.1-B4.3; dimension
  2 remains). Restated: pair pieces do not glue (A1.3, INT-SA10-K10; use A1.2's tubes with actual overlaps); control
  data need pi-control, the whole collar germ and regular source bundles (C2.01-C2.04); collars and manifoldness are
  hypotheses (C1.01, C3.01, C3.04, C4.04, C5.03-C5.05, C5.08); closed diagrams need cartesian meets (A4.1-A4.4, for A.3(c)
  and A.4); order-defined lower unions under restriction (A2.2, A3.1, for A.5). Open: A.1-A.5, A.7.
- Both: --lint-math and paper_completeness_lint pass on the build and on the packed PROMPT.md. Send folders
  TO_SEND/PRO/1_Archive_research_by_topic/10_SA11_Stratified_spaces_cote_154_night and
  12_SA20_Esquisse_cotes_121-125_155_night rebuilt from hard links to the builds and packed by pack_one_zip.py (one ZIP
  each, the SA10 files at its top level). Scripts: results_register/horizontal/sweep3/_tools_a6d42bf6/
  add_sa10_results_to_prompts.py, relink_send_folders.py.

## 19 Nov ~11:55 UTC (Claude Opus 5.5 at effort max, agent a34c04448e8299803, from the intake of RESEARCH_SA08)
- Why: RESEARCH_SA08 (divided-power de Rham complex, cote 136; GPT-6 Astra, ChatGPT Pro mode, final 10:27 UTC, INCOMPLETE
  under the two-review rule) was taken in (results_register/horizontal/sweep3/SA08/INTAKE_RESEARCH_SA08_20261119.md). New
  results go as background into every unsent prompt they bear on; the coordinator asked to carry SA08's open C.3 into
  SA09 if it fits its cluster, and to add the check of D-031 if SA09's material bears on it.
- RESEARCH_SA09 (cotes 137-138): backup PROMPT_before_SA08_results_20261119.md; added the files SA08_RESULTS_20261119.md
  (69 statements by group, with status, proof locator, the run's check events counted by type, and the intake's checks)
  and SA08_final_paper_tex.zip (the SA08 paper with sections/, bib, results register, corrections, check events, report,
  ledger, notes/, code/, the computation logs under 300 KB without fetched sources, and the intake; MANIFEST.tsv with
  SHA-256), the attachment bullet, a header line, and the section "Results of RESEARCH_SA08 that this prompt builds on"
  before the Leads. Settled outright: none. Restated: A.3 (cote 136's PD cochains already recover RΓ(X,Z) with product,
  the E-infinity algebra and the nilpotent finite-type homotopy type, D006, D006E, A-018/D006M; R5 transports them to
  τ≤n C•, so A.3 becomes whether that transport carries R4's cup product and the Γ-operations); no filtered numerical
  lift (A-026, intake-checked both parts; A-015, A-017, A-025, D-026); literal against graded cochains (A-002 to A-004).
  Tools: D007-D012 and the γ^p(γ^q) slip of 136/334 (D-C15) for A.1; C02-C05 for A.4. Part B untouched.
- New items: A.5 = SA08's C.3 (his uniqueness conjecture for admissible generalized de Rham theories over Z), with what
  SA08 settled (C06-C10, C16-C17), the gate (C30, C32, C34), every approach tried with where it failed, cote 137's
  universal objects as the new tools, and the SA08 files to restore from; A.6 = an independent check of D-031 (the
  refutation of Caradot-Lin, arXiv 2511.22614v4, Prop. 3.10) against the paper's LaTeX source, with exact locators, its
  reach (Thm 3.15 included) and the corrected statement. Sources: Caradot-Lin added. Rules 5 and 7 extended (Z and rings
  with infinitely many noninvertible primes; the SA08 results are checked where used).
- --lint-math and paper_completeness_lint pass on the build and on the packed PROMPT.md. Send folder
  TO_SEND/PRO/1_Archive_research_by_topic/09_SA09_de_Rham_cotes_137-138_night rebuilt from hard links to the build and
  packed by pack_one_zip.py (one ZIP, 542 members; SA08_RESULTS_20261119.md at its top level). The Space paragraph (P008)
  of the old packed PROMPT.md is kept; the Space copies do not hold the two new files, so space_flat.py needs a rerun if
  the Space is used for this prompt. Scripts: results_register/horizontal/sweep3/_tools_a34c0444/
  add_sa08_results_to_sa09.py, relink_sa09_send_folder.py.


## POLISH_TOPOLOGY_PERIODS: items for the prompt after 91b (intake a9e9559d, Claude Opus 5.5 at effort high, 23 Nov 2026)

Prompt 91b (sent; continues from checkpoint 13) carries the S20 literature into Paper 2. It does not carry these items from the cp12 and cp13 intakes; they belong in the finishing prompt that follows 91b's final return (running threads are unreachable after one to two hours):
1. Every paper gets a section headed "Proof overview" (HOW.md box 8); none of the seven has one.
2. CHECK_EVENTS types: Paper 2 carries six events whose types are not among the seven of the rubric (build and visual checks); move them to a QA log. Normalize the model field to "GPT-6 Astra (ChatGPT Pro mode)".
3. Paper 5's abstract names "Claude Opus 5.5" without its effort: write "at effort max".
4. Paper 4: compare the single-cap theorem with infinite grafting and meromorphic projective structures (Gupta 2014; Gupta-Mj; Dumas) at exact locators.
5. Paper 7: obtain the Order 40 (2023) page of Jenca's Corollary 4.5; route the V-poset counterexample to CORRECTIONS_FOR_AUTHORS.md only if the published corollary keeps the unbounded wording.
6. Paper 2: obtain King 1985 (Topology Appl. 20, 149-160) for the A.205 comparison; the collar rows now use base-fixed cone parametrizations, and the paper should say in Section 1 that the literal base-setwise reading of II c) is false (the space is Homeo(Y) up to homotopy).
7. The Elliott note in CORRECTIONS_FOR_AUTHORS.md resolves a conjecture; title it so.
8. Split Paper 3: a short paper on the strong transcendence counterexample and the dimension table (Thm 1.1, Cor 1.2), apart from the elliptic and arithmetic material.
