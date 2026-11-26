# The rest of the pile: everything started or promised and not finished (24 Nov 2026)

Written 24 Nov 2026 ~21:2x UTC by agent a88af1f4fbcac932c (Claude Opus 5.5 at effort high) for the main session 329fb1e6
(Claude Opus 5.5 at effort max), for the intake pile of 24-25 Nov. Read-only inventory: nothing was changed anywhere.

**Sources read:** RUNBOOK_20261110.md from its end back to 20 Nov (lines 6374-6881 in full, 5505-6373 in full, 4900-5504
by search); task_notes/README.md and its active notes (the open lines of each); task_notes/PLAN_POST_COMPACTION_20261123b.md
whole; field_experts/hexagon/HEXAGON_BOARD.tsv (the board of record; HEXAGON_CANDIDATES.md is its history);
field_experts/INTAKE_LEDGER.md sections 0-2 (built 24 Nov 21:07 UTC). Statuses were checked on disk where cheap (TO_SEND
folders, research_returns, intake folders, e-mail files, the cost ledger, agent transcripts). "l.NNNN" = a line of
RUNBOOK_20261110.md.

**Left out, as briefed:** the transcription second passes (SP/SR/RA/IM pieces, witness P, Work readings) and the S6 series
(sessions 5c7e951b and aacf1302). Pointers only, in section 7. The research runs themselves are the ten cluster readers';
section 1.4 lists only the newest returns that no intake has read, for them to check against their coverage.

**One caution on the ledger.** INTAKE_LEDGER.md section 1 marks almost every 20-24 Nov research run "not taken in". That
status is document-based and indicative only (the ledger says so; l.6336-6340): those runs do have intakes in
`field_experts/intake_20261121/intakes/<RUN>/`. What is genuinely unread is in 1.1-1.4 below.

---

## 1. Intakes not done, or sent with no report back

**1.1 Wave 2: the Longue Marche / anabelian intakes, held since 20 Nov.** Queued 20 Nov ~20:0x UTC and held for the
weekly meter (l.5136), then "only on the user's go" (l.5342); never launched. Agents picked then: SECTION_GHOSTS +
FERMAT_SUCCESSOR a28ea31f; ANABELIAN_A1_SUCCESSOR + ANABELIAN_A1 + ANABELIAN_SUCCESSOR aff445fc; LM4_SUCCESSOR aacef3f0;
LM7_PUSH aad0e932; LM8_PUSH a4688aef; GT_TOWER_CHECK a45b5a3f; LM4_FINITE_GROUP_ACTIONS a0c4bb37; LM1 rerun a9f76900
(their models and efforts are in field_experts/REGISTRY.md; the RUNBOOK line does not give them). The ledger (sections 1b
and 2b) confirms these runs are thinly read, with the rows no intake names: LM4_SUCCESSOR ~317 of 401, LM8_PUSH ~304 of 304,
LM4_FINITE_GROUP_ACTIONS ~251 of 272, SECTION_GHOSTS ~228 of 228, ANABELIAN_A1_SUCCESSOR ~210 of 210, LM7_PUSH ~187 of 218,
ANABELIAN_SUCCESSOR ~156 of 157, GT_TOWER_CHECK ~149 of 180, FERMAT_SUCCESSOR ~144 of 144, ANABELIAN_A1 ~114 of 121,
LM1 rerun ~80 of 84; and for Les Dérivateurs REVLOC ~117 of 152, DER_LOCALIZERS ~81 of 100, RESIDUE ~64 of 85.
*Holder:* the user's go; then the main session. *Next:* choose the route (resume the named agents, or Pro intake prompts in
the ledger's 2b order), rebuild the ledger first (INTAKE_LEDGER_README.md).

**1.2 Wave C of the 22 Nov full intake.** Planned 22 Nov ~00:0x UTC (l.5739) and still "NOT YET" at 22 Nov ~01:0x (l.5764):
the Longue Marche registers (~2,400 statements), Les Dérivateurs (~440), and RESEARCH_SA10 + SA21 (agent a6d42bf6). The
ledger now shows SA10 0 of 74 and SA21 1 of 92 statements checked by an intake. Overlaps 1.1. *Holder:* main session.
*Next:* fold into the 1.1 decision.

**1.3 Statement-level backlog of the sweep-3 runs.** Ledger section 0: 6,461 of 10,156 statements of the newest registers
have no intake check event. The largest: RESEARCH_SA15 955, SA12 438, SA17 221, SA06 215, SA20 210, SA22_run2 202, SA07 185,
SA05 177. Two partial jobs of 22 Nov had no closing record: SA15 statement rows (a1cf7c6b) and SA12 rows 433-435 literature
(a3c8d7de) (l.5764). *Holder:* nobody assigned. *Next:* decide whether statement-level coverage is still wanted (it was the
user's "I also want the full intake", 22 Nov, l.5739).

**1.4 Newest research returns with no intake yet** (all filed 24 Nov; for the cluster readers to check against their runs):
- BEYOND_DIRICHLET cp10 (20:10Z; the run of prompt 69, sent 24 Nov ~13:4x): no intake folder exists for this run at all.
- POLISH_CRISTAUX, the 92c merge run, cp32 (20:09Z; carries cp25/26). Thread B's cp22 was taken in (a512cf71); the merge run
  was not.
- COUNTING_VARIETIES cp01 (20:15Z), first return of prompt 63. Ownership to settle first: l.6766 records "94_THETA_CIRCUIT_SIZE
  is Codex's (with 63, 78)", yet the main session filed it (l.6876) and the ledger lists it as ours.
- SPLIT_ZERO_AFTER_FGJM, the new run of 93 (started 24 Nov 13:40 UTC), cp08 (19:40Z). The old run's cp08 (03:28Z) was taken
  in by a2fedc2a (Claude Fable 5.2 at effort max).
- MOONSHINE_AFTER_ALPOGE cp01 (20:45Z), first return of 97.

**1.5 NIGHT_GROTHENDIECK_QUESTIONS cp13, Parts B and C: quick checks with no file.** Asked 24 Nov ~10:5x UTC (l.6816) of
a9e9559d (Part B) and aaf69461 (Part C), both Claude Opus 5.5 at effort high. aaf69461 answered only in its transcript (Part C
not started by cp13; no file written). a9e9559d left no Part B record (its later turns were the e-mails). Part A (a0805369)
is done. *Next:* note both in intakes/NIGHT_GROTHENDIECK_QUESTIONS/; Part B is likely also unstarted (the run works A, B, C
in order, l.6805).

**1.6 98_VPVNP_HINGE: the reply is unread.** Sent 24 Nov (folder in SENT, 19:58 UTC); the run answered in about two minutes
(the user); nobody has read the reply (l.6879-6880). The replacement 99_VPVNP_WIRE_GEOMETRY (written by the main session with
the papers builder) is in SENT (21:01 UTC); no return yet. *Holder:* the user (the reply is in ChatGPT) / main session.
*Next:* get the reply and read it before judging 98.

**1.7 The GCT write-up prompts 56 and 56c were rejected.** Both are in SENT; ORDER.md (line 89): "56 and 56c are rejected;
their returns stay out of every filer and post." No return was filed. So H02, H02b, H13 and H23 have no write-up route, and
the board still says "prompt 56 GCT_WRITEUP ready, not sent (22 Nov)" for them (stale). *Holder:* main session; the user for
the route. *Next:* decide how those four get written.

## 2. Reports received but not acted on (oldest first)

**2.1 GCT_POS final intake, 22 Nov 08:57 (l.5841).** "N-017..N-024 and the changed N files for a8d75352" (Claude Opus 5.5 at
effort high): no later record. Also: the GCT VI subtitle is wrong in prompt 52 and in the runs (l.5845: arXiv v4's title is
"the flip via saturated and positive integer programming ..."); prompt 52 is sent, so the fix belongs in our records.

**2.2 Dated corrections of flagged faults, 22 Nov 14:0x, NEXT 4 (l.5868).** GCT_OBS intake section 1.4 and the event types of
NN-A001, NN-A017, NN-G012: no later record of the corrections.

**2.3 Masullo traces in our public pages (22 Nov 21:31 and ~21:35, l.6200-6202, l.6222).** research/grh_20261120/README.md
(lines ~11, 42, 45: "need Masullo", "Under Masullo, RH holds for every CM motive"), the TRACE_DET part-2 intake (MAS-10) and
H05 rest on Masullo's draft. Proposed: mark them as resting on GRH for Hecke L-functions as a hypothesis. Waits for the user's
yes (a push); no later record. Related, from the GRH_ALGORITHMS cp04 intake (l.6367-6368): a workbench note's section-5
heading calls GRH_NIGHT constructions "repairs" of his draft: reword before publishing. The board still lists H05 as
"held"; under the user's Masullo rule it is void (l.6217-6218).

**2.4 ALP_MACHINE: 49b never taken up; the finishing prompt is unbuilt.** 49b was sent 22 Nov 23:5x (l.6341); the run never
took it up (cp36 l.6442, cp48 l.6596, cp59 l.6804). The cp67 intake (abcaba9b, Claude Opus 5.5 at effort high; l.6818): no
main question moved; "49's finishing prompt should note" the AM112 transport result (R110, LIFT117-120). PLAN l.120 lists the
finishing prompt (LIFT110-120 note + AM112). *Holder:* main session.

**2.5 The POLISH runs: finishing prompts for 90 and 91.** The intakes of 23 Nov (l.6646-6648, 6804, 6805) found that no paper
of 90-92 has its "Proof overview" section, plus locator faults "for their finishing prompts": 31/085 is a PDF page (sheet 84);
SA06 "14:38" merges two items; E4 is cote 57 sheet 314; footer vs PDF page off by one in cotes 18, 119, 137, 151, 154, 156-9.
POLISH_TOPOLOGY_PERIODS Paper 2 (169 -> 250 pp.) should be split in three (l.6805, l.6819). 92's corrections went into 92c
(checked); finishing prompts for 90 (newest cp35) and 91 (newest cp26) are not built. Experts: a018e2d2 (AG) and a9e9559d
(TP), both Claude Opus 5.5 at effort high.

**2.6 H18 after Pintar (23 Nov 12:43-12:49, l.6659-6660).** The user: [the user's words, omitted]. Planned: our
single-place certificates for k = 21..26 would remove Pintar's simultaneous-trace hypothesis (a computation or a prompt, not
yet planned). Also still open: the `#print axioms` check on a compiled build of the OneCharU_s chain (l.5625; board H18).

**2.7 NIGHT_GROTHENDIECK_QUESTIONS: Part B as its own prompt.** Proposed by a9e9559d (l.6805; PLAN l.82): the user's call.

**2.8 NIGHT_AFTER_ALPOGE: 75's successor.** K-groups: the order-5 annihilator, the U(3) endoscopic formula, Ishii, H15 on
Hodge-type subvarieties, Ihara at p = 37 (l.6775; PLAN l.41). Waits for the run's final (newest cp13, 23 Nov 11:54Z; no final
filed).

**2.9 Prompt 93: its successor, and the lambda-ring / Artin successor.** From the cp08 intake (l.6838; PLAN l.119): when the
93 run ends, its intake section 5 + fork 2's remarks (a)-(c) + cite 720 + aim at 608/612. PLAN l.131-135 (24 Nov ~13:5x): a
successor on counts with coefficients in a lambda-ring (cote 133), c -> Z_c giving Artin L-functions, after 93's final and the
68/69 returns. Note that 93 is running again (a new run from 13:40 UTC, 1.4).

**2.10 The English translation's loose ends (23 Nov, l.6757 and l.6781).** The run that propagated 135 pages by diff
(a3d0153a, Claude Opus 5.5 at effort high; GPT-6.1 Sol at reasoning effort max, Flex, $1.78) has no compute-cost ledger row
(checked: LEDGER.jsonl has none); 20 new second-passed pages wait for translation; the user's ask to consolidate the English
"into something readable where possible" has no later record. Nothing pushed.

**2.11 GitHub push of the new mathematics of filed returns.** The user, 23 Nov 16:48 (l.6745): after unpacking, push the
non-copyrighted new mathematics of everything that came in. The last such push was 23 Nov ~18:3x (l.6747). Everything filed
since is "no push": among others ALP_MACHINE cp67, POLISH_AG cp35, POLISH_TP cp26, POLISH_CRISTAUX thread-B cp22 and merge
cp32, NGQ cp13, ZETA_HEAT final, GRH_ALGORITHMS_FINISH cp07, BEYOND_DIRICHLET cp10, SPLIT_ZERO cp08 (both runs), MOONSHINE
cp01. Mind the PUSH_NOTE.md of 93 and 97 (folders that quote the user). *Holder:* main session.

**2.12 Hua's review, the codicology rows into the readers (24 Nov 13:52-15:5x, l.6850-6860; PLAN l.141).** Reader builds
should consume codicology/HUA_REVIEW_CONFIRMED_20261124.tsv (101 corrections) and GENETIC_FINDINGS_20261124.tsv (8 rows):
not done. Of Hua's 130 findings, 8 remain "not decidable". (Archive readers, not second passes.)

## 3. Hexagon candidates not yet decided

The board of record is field_experts/hexagon/HEXAGON_BOARD.tsv (109 rows; STATUS.md built 24 Nov 12:35 UTC): P 10, W 11,
G1 15, G2 34, M 16, N 13, H 2, X 8. Since that build: P90a v2 published 16:29, S20 v2 15:40, H22 (2611.00993) 17:15,
ZH3 (2611.00996) 17:20 UTC (l.6861, l.6865); the publication of 2611.00987v1 (67c, H29/H29b) is not recorded.

**Stale entries on the board** (to correct at the next rebuild):
- H02, H02b, H13, H23: "prompt 56 ready, not sent": 56 and 56c were sent and rejected (1.7).
- The N rows P90i (Zheng), P90j (Mukai), P90k (Esnault), P91i (Boyle-Chen), P91l (Galvin), P91m (Orson-Powell-Randal-Williams),
  A15c (Thakur), S93b (Mulmuley): the e-mails went out on 24 Nov (section 5 has the state).
- H05: void under the Masullo rule, still "H".

**Follow-ups on posted notes:**
- H01: v2 with F50, SN-14, AM-S1-S3 (a phase replaces the sign only if it commutes with Frobenius), once the additions are
  checked.
- H06b: three small fix-ups for the posted text (NIGHT_AFTER_ALPOGE intake, 23 Nov evening, ad855737).
- Author notices, with no draft written yet: H09 (Katz, Bannai-Kobayashi, Boxall, Berger), H17 (Nakamura, Schneps, Lochak),
  H06b (Sharifi; Wake, Wang-Erickson; Fukaya, Kato; Ishii), H22 (the FGJM and CFMM authors), ZH3 (Alpöge and Furman; PLAN
  l.116), and with the H07 post, Saïdi and Tamagawa. Under the user's e-mail rule of 24 Nov (send when confident, with the
  note on why we write; l.6832).
- H07 v3 (9 pp.) and H15 (8 pp.) wait for the user's word: not 100 % (H07: Stix LNM 2054 ch. 7 unread; H15: modest gain over
  Gaudron-Rémond Thm 1.9(5), effective André-Oort is Jaswal's) (l.6695, l.6706).
- S17a: a second re-proof, then show the user; the Stacks p = 2 correction after posting.

**The open candidates, by stage** (generated from HEXAGON_BOARD.tsv; cells cut to fit; the full rows are in the TSV):

#### W: ready for the write-up (11)

| Id | Line | Result | Gates left | Next (board) |
|---|---|---|---|---|
| H02 | GCT | GCT VI's index hypotheses PH2, SH(a) and PH3 all fail for plethysm (P-F57, P-F19, P-F31), with the Theorem 1.6.1(d) erratum | literature search (Kahle-Michałek first; Hexagon); proof checks of PNEW-002 to 004 and the exterior identity if those additions go in; the finished t… | prompt 56 GCT_WRITEUP ready, not sent (22 Nov) |
| H02b | GCT | Numerical PH3 (GCT VI, Hypothesis 3.3.4) fails for Kronecker coefficients: every positive form for g((s^n),(s^n),(s^n)) has a den… | literature search (Hexagon included); the self-contained text (P-F23, P-F27, P-F30 with proofs); the claim stops at the existence clause | prompt 56 GCT_WRITEUP ready, not sent (22 Nov) |
| H07 | anabelian | Rational points of curves in characteristic p are separated by the prime-to-p fundamental group, on a question of Grothendieck (c… | Stix LNM 2054 ch. 7 (library; bears on what is known and credit, not on the proof); Mochizuki's journal reference and the SGA 1 / Weil I locators; th… | show the user reports_20261123/h07_note/h07_note_v3.pdf (9 pp.) |
| H13 | GCT | Occurrence obstructions for per_n against det_n with no padding (A-030, A-034) | reframe per the pequalnp check (LMR + swarm L-gct-070/074 cited; 'best refereed' bound wording); literature search (Bürgisser-Ikenmeyer-Panova; Ikenm… | prompt 56 GCT_WRITEUP ready, not sent (22 Nov) |
| H15 | CM points | Galois orbits of CM points in A_g: /Gal x/ >= c_g D_x^{1/(4g)}, explicit constants, all centre orders and products (A.ORBIT); eff… | the write-up with Jaswal's Prop 3.3 stated beside ours (needs a pass: effective André-Oort is Jaswal + Cureton-Thorner, cited); literature pass incl.… | main session reads the note; then show the user reports_20261123/h15_note/h15_note.pdf / 23 Nov evening (ad855737): unchanged by NIGHT_AFTE… |
| S12a | archive (cote 31) | The persistent A.2 counterexample to Grothendieck's margin question | literature (Hasse 1925, Schilling 1950); the locator: '31/085' is a PDF page, the archive sheet is 84; a 'Proof overview' section | the run's final, then the finishing prompt of 90 |
| S17a | crystalline | A counterexample to full faithfulness of crystalline Dieudonné theory (B:crystal-counterexamples) | literature search; the finished text | second re-proof from the statements; main session reads the note; show the user; Stacks p = 2 correction after posting |
| S17b | archive (cote 133) | WG(BO_m) is a special lambda-ring exactly when m <= 2 or k contains Q | literature search with exact locators; the finished text | literature, then text |
| S22a | archive (cote 67) | Grothendieck's (0,4) capping map is not onto; its image is 0 < /q/ < 16 (Koebe) | literature search; the finished text | literature, then text |
| S12d | characteristic two (cote 29) | An explicit characteristic-two wild genus-two example showing the formal-linearity hypothesis cannot be dropped (RESEARCH_SA12 ro… | the write-up (core: the run's D_wild_genus2_curve.tex, with a Proof overview); a Hexagon search for the topic; every page read | write the short note |
| S06b | abelian varieties | Jacobian summands of abelian varieties of dimension <= 3: s_J divides gcd(2, delta) for surfaces and gcd(6, delta) for threefolds… | literature search including Hexagon; every page read | literature, then write-up |

#### G1: one gate left (15)

| Id | Line | Result | Gates left | Next (board) |
|---|---|---|---|---|
| H03 | complexity | The border rank of det_4 and of per_4 is at least 43 over C, and at least 42 over every field | the 25 border-apolarity cases checked independently; the finished text | independent check of the 25 cases |
| H04 | archive (cote 44) | Grothendieck's cote 44 Th. 5 fails as displayed; corrected by one term per singular fibre | scan-004 image check; the finished text | scan check; then the archive companion paper |
| H14 | GCT | Four-row multiplicity obstructions under padding; the gaps exist exactly when n^2 <= 2m^2 - m + 1 (m >= 17) | reframe per the pequalnp check (LMR + swarm L-gct-070/074 cited; 'best refereed' bound wording); literature search (Dörfler-Ikenmeyer-Panova); proof… | checks, then literature |
| GPK18 | GCT (Kronecker, polytopes) | The largest vertex-denominator (determinant) order of the n-fold Kronecker tensors is 2^(n-1+floor((n-2)/7)), not 2^(n-1), with s… | compare with Kravtsov's work on vertex denominators of axial three-index assignment polytopes (may contain the order growth) | literature |
| S14a | archive (1964) | Counterexamples to Grothendieck's 1964 programme: his Th. 5 fails in codimension 2 (J5), with J2a, J2b and J6C | coordinate with H11 (JAC1964) | the archive companion paper with H04 and H11 |
| S14b | various | G1 (literature gate); A3 (certificate rerun); F11: every metabelian quotient of the local pi_1 is finitely generated | literature; F11 also test 2 (the Krishna-Majumder preprint) | literature |
| S15 | archive (8.3) | Grothendieck's admitted integral crystalline weak Lefschetz (8.3) fails in degree one on products of the OC chain, and holds for… | a forward literature search (is the crystalline torsion failure folklore?); test 2: rational crystalline weak Lefschetz is cited from an arXiv prepri… | the run's final, then the finishing prompt of 92 |
| S23b | archive (cote 1) | The Hilbert trace formula proved in Grothendieck's hand | open the printed sources | sources, then an archive note |
| S07b | Hodge (computability) | A non-computable non-geometric Hodge pair whose period is built from the halting set (C.1.5) | literature search | literature |
| S15b | archive (cote 4, 8.6) | Cote 4's question 8.6 for plane curves in characteristic 2: the monodromy on the theta characteristics is reducible for every odd… | literature search including Hexagon (characteristic-2 theta-characteristic monodromy of plane curves) | literature search |
| S07c | Longue Marche (LM6 A.22) | The open CM common-kernel case of LM6 A.22: for E0: y^2 = x^3 - x minus its origin, no nontrivial closed procyclic subgroup of th… | literature: the published characterization (Nakamura 1994 Thm 2.1.1) needs the normalizer to act through the cyclotomic character; F.3.20/F.3.29/F.3.… | literature search on the open-normalizer form; repair F.3.33 |
| S15e | Cristaux | A reduced counterexample to Grothendieck's extension assertion, after Ferrand-Raynaud and Olberding (C-RD4, C-RD11; Paper 4 of PO… | a 'Proof overview' section; the run's final | the run's final, then the finishing prompt of 92 |
| P91a | transcendence | A counterexample and a dimension formula for Grothendieck's strong transcendence conjecture (18:11): the dimension table (Thm 1.1… | cut out as a short standalone paper; literature | the run's final |
| H25b | Hodge (HODGE_FINISH) | Integral Gaussian Hermitian lattices of determinant class [-3]: every pairing-integral Z[i]-lattice of signature (3,3), class [-3… | literature search (Hermitian lattice classification over Z[i]: Jacobowitz, Kirschmer); otherwise part of Paper A | with H25 |
| ZH4 | zeta zeros (ZETA_HEAT) | The complete local multiplicity partition for heat-flow Newton determinants: ord_(t=0) det[S_(u+v)(t)]_(u,v<k) = sum_(j<=k) b_j,… | our proof check | - |

#### N: note to an author (send state in section 5 is newer than the board) (13)

| Id | Line | Result | Gates left | Next (board) |
|---|---|---|---|---|
| H10 | S6 | Biró's Conjecture 1 contradicts Louvel's first moment of Salié sums | only if Biró wants a citable note | on offer to Biró |
| H23 | GCT (erratum) | GCT VIII: Conj. 3.2 as printed has no minimum (N-012); the Positivity conjecture's unimodality clause fails at r = 3; the printed… | independent re-run of P-F-E3-01; literature; a draft note to Mulmuley first, on the user's word | prompt 56 GCT_WRITEUP ready, not sent (22 Nov) |
| S07 | transcendence (erratum) | A counterexample to Bhowmik-Pathak 2024, Thm 1.11: at tau = i, E6 vanishes and the transcendence degree drops to 2 | check the Acta Arithmetica version (it may be corrected); a draft note to the authors first, on the user's word | email Draft (field_experts/intake_20261121/intakes/POLISH_TOPOLOGY_PERIODS/EMAIL_DRAFTS_POLISH_TOPOLOGY_PERIODS.md) on the user's word, aft… |
| S15g | Cristaux | Erratum: Grammatica, arXiv:2507.08568v2, Remark 4.6, p. 29: the last conclusion (H^i_et(X,Z_p) = H^i_cris(X/W(k))^{F=1} for X pro… | the user's word on the drafted email | send Draft 1 of field_experts/intake_20261121/intakes/POLISH_CRISTAUX/EMAIL_DRAFTS_POLISH_CRISTAUX.md on the user's yes |
| P90c | AG | Errata to published work: Stacks Tags 07BV (x_r for x_d, twice) and 0BTP (an fppf lemma for an fpqc step); Popescu 2022 p. 510 cl… | the user's word on the drafts; Liedtke after a look at his printed table | eight drafts in field_experts/intake_20261121/intakes/POLISH_ALGEBRAIC_GEOMETRY/EMAIL_DRAFTS_POLISH_ALGEBRAIC_GEOMETRY.md |
| P90i | AG (erratum) | Zheng, arXiv:1509.04993 (v1), Cor. 4.4 fails in characteristic 5: a minimal surface of general type with ample L = O(S+F), (5^2-1… | the run's final; the e-mail (draft folded into the planned P90a notice), on the user's word | the user's word on the e-mail |
| P90j | AG (erratum) | Mukai, RIMS-1736: in the proof of Prop. 3.2, L should be L^-1 throughout; in Case 3(d), b_2 = 2, not 6, for hyperelliptic and qua… | the e-mail (draft folded into the P90a notice), on the user's word | the user's word on the e-mail |
| P90k | AG (erratum) | Esnault, math/0608203v1, Section 2: Lemma 2.2's first map is injective only when omega_L has zero annihilator; Prop. 2.5's residu… | the e-mail (new draft), on the user's word | the user's word on the e-mail |
| P91i | topology (erratum) | Boyle-Chen, Rev. Mat. Iberoam. 2024, Thm A.6: the displayed generator (r,theta,y) -> (r,theta+pi y,y) does not fix the top end, a… | the e-mail (draft in EMAIL_DRAFTS_POLISH_TOPOLOGY_PERIODS.md), on the user's word; not a post | the user's word on the e-mail |
| A15c | archive (cote 15) / CM | Over a CM centre, the central model exponents of isogeny descent are the multiples of a.t.s with s in {1, 2} (central models: tho… | the e-mail (draft intakes/NIGHT_GROTHENDIECK_QUESTIONS/EMAIL_DRAFT_Thakur_20261123.md, pending the run final), on the user word; literature (Brooks e… | the user word on the e-mail |
| P91l | topology (erratum) | Galvin, Compositio Math. 162 (2026) 2496-2544: Lemma 4.9 (p. 2526) states the Steenrod-square vanishing the wrong way round; Prop… | open pp. 2508 and 2526; the e-mail (Draft 4), on the user's word | the user's word on the e-mail |
| P91m | topology (erratum) | Orson-Powell-Randal-Williams, Smoothing topological pseudo-isotopies of 4-manifolds (accepted, J. reine angew. Math., 31 Oct 2026… | open Definition 5.8; the e-mail (Draft 5), on the user's word | the user's word on the e-mail |
| S93b | GCT | GCT VIII (arXiv:0709.0751v2), rank-three section, 'Positivity': the unimodality assertion fails in both sign readings, on a const… | E-MAIL SENT to K. D. Mulmuley 24 Nov 11:54 UTC (reports_20261124/EMAILS_SENT_20261124.md, no. 6); the draft's 'Section 3' corrected to Section 2 | wait for a reply; then a short Hexagon note if wanted (stage N: erratum) |

#### H: held (2)

| Id | Line | Result | Gates left | Next (board) |
|---|---|---|---|---|
| H11 | archive (cote 44) | Grothendieck's 1964 Th. 4 for abelian varieties in every characteristic | test 2: it rests on OpenAI 032 and Milne's report (unrefereed) | hold |
| H05 | GRH (Masullo) | RH for every CM motive, under Masullo's claim | Masullo's proof refereed | hold |

#### M: moving (a run of ours still extends it) (16)

| Id | Line | Result | Gates left | Next (board) |
|---|---|---|---|---|
| H06a | K-theory | What Alpöge's step 17 proves: log/K_4k(Z)/ <= C(2k)^7 | Soulé comparison; the exponent-7 chain; a re-proof at l = 2 | wait for the KTOWER final |
| H12 | Hodge | Bounded division for Weil classes (HD-U) for every imaginary quadratic K and every n, with explicit constants; the ghost-class di… | literature search; the finished text; HODGE_DIVISION still running | post when the run ends, scoped to HD-U and the dichotomy |
| H19 | Hodge | Bounded division for split Q(omega) Weil eightfolds from published inputs | full read of D-G34-04 to 06; the run's final; literature | wait for the HODGE_DIVISION final |
| NEG | complexity and zeros | The parity of #SAT is a Hasse-Witt scalar (computing it is ⊕P-hard); one sparse smooth cubic whose class encodes #SAT; the CUE fi… | proof checks; literature; the run continues | wait for the NEG_NIGHT final |
| S15h | Cristaux | Sharp ramification thresholds of Barsotti-Tate groups for every e prime to p, with central p^2 rigidity (Paper 2 of POLISH_CRISTA… | the merge of the two threads (the 92 final and 92b, cp18 or its final); a full-chain check by a different model | the merge prompt 92c (rebuilt 24 Nov ~11:5x UTC with thread B cp22; waiting to be sent) |
| AC219 | Selmer (cubic Kummer, ALP_CONNES) | Strict 7-adic Selmer groups of a cubic Kummer twist family over Q(sqrt-3), L = K(cbrt 269): S_7(K, (E/O)(chi^j xi_7^a c_7^-e)) =… | replay the class-group certificate Cl(L) = C_7^2 in a second system; check steps 6-8; literature (Iwasawa-theoretic lifting at split primes) | the run's next checkpoints |
| ZH1 | zeta zeros (ZETA_HEAT) | Under Alpoge's theorem, simplicity of the zeta zeros is equivalent to an exact growth rate of the finite positivity tests (Toepli… | check of the local Hermite/orbital part; comparison with Shi (2026) and Griffin-Ono-Rolen-Zagier; the run's final; the upper radius bound r_m <= pi s… | merge into ZH3's note |
| S15i | Cristaux (cote 8:49) | Grothendieck's two Lubin-Tate lattices agree exactly when e <= p; the extremal exponents are max(0, e-p) and the tangent images a… | a different-model re-proof; literature (Kisin-Ren, Pham, Lau); the merge of the two threads (the 92 final and 92b, cp18 or its final) | the merge prompt 92c (rebuilt 24 Nov ~11:5x UTC with thread B cp22; waiting to be sent) |
| S15j | Cristaux (cote 8:81) | The least rank of a local system with a non-split co-Lie complex is 4, 3, 2 for p = 2, 3, >= 5, realized on surfaces (the Z/p^2-l… | full check of thm:surface; literature (Bergh-Rydh, ABM); the merge of the two threads (the 92 final and 92b, cp18 or its final) | the merge prompt 92c (rebuilt 24 Nov ~11:5x UTC with thread B cp22; waiting to be sent) |
| S15k | Cristaux (inertia characters) | The complete next wild band for the special inertia character: nu_min = v + 2 on the whole band 2 <= k <= p^2, p not dividing k,… | the merge (92c); a full check of the midpoint exclusions and of the three carried inputs by a model other than GPT-6 Astra; literature (Hattori, Bond… | the merge prompt 92c (rebuilt 24 Nov ~11:5x UTC with thread B cp22; waiting to be sent) |
| S15l | Cristaux (hypersurface sections) | Full mod-2 monodromy groups GL_8(F_2) and GL_80(F_2) for hyperplane and cubic sections of the supersingular cubic square (POLISH_… | proofs read and certificates rerun independently; the merge of the two threads (the 92 final and 92b, cp18 or its final) | the merge prompt 92c (rebuilt 24 Nov ~11:5x UTC with thread B cp22; waiting to be sent) |
| P90e | AG (POLISH_ALGEBRAIC_GEOMETRY) | Picard kernels on surfaces in characteristic p: X smooth projective surface, Y a smooth very ample curve, L nontrivial of order p… | a018e2d2's read of the three lemmas; a literature pass; the run's final | the run's final |
| S15m | Cristaux (Grothendieck's weak-formal H^… | Grothendieck's weak-formal H^1: rigid rationally with no lift needed, torsion-free integrally (it injects into the rational theor… | the merge (92c); a check of the torsor and site proofs by a different model | the merge prompt 92c (rebuilt 24 Nov ~11:5x UTC with thread B cp22; waiting to be sent) |
| A133b | archive (cote 133; NIGHT_GROTHENDIECK_Q… | Regularity criterion for lattice generation: for A finite free local over any mixed-characteristic DVR with edim(A/pA) <= 1, the… | Cor. 27.3 and Thm 13.1/19.1 read in full; the external inputs (Burke-Walker, Blumberg-Gepner-Tabuada) at their locators; non-curvilinear singular rin… | the run's final |
| P91j | topology (POLISH_TOPOLOGY_PERIODS) | A surjective Casson-Sullivan homomorphism for oriented 3-manifolds with finite pi_1; vanishing on T^3; the concordance component… | a Claude targeted read; comparison with Galvin 2026 and OPR 2026 at locators; a short note | the run's final |
| S15o | Cristaux (abelian surfaces, characteris… | Reduced Hasse divisors and natural GL_8 blocks in every cubic-theta degree: all-degree structure for Frobenius on the sections /3… | the merge (92c); the proofs checked by a different model; the full eventual image (open) | the merge prompt 92c (rebuilt 24 Nov ~11:5x UTC with thread B cp22; waiting to be sent) |

#### G2: two or more gates left (34)

| Id | Line | Result | Gates left | Next (board) |
|---|---|---|---|---|
| H16 | archive (cote 149) | Grothendieck's tangential-section question (scan 85): yes with the marking of scans 83-84, no without it | intake read of the proof; literature | proof read |
| H18 | K-theory | K_4k(Z) = 0 for k <= 20 (K_12 to K_80 new), given Alpöge's archive theorems | #print axioms on a compiled build (OneCharU_s chain incl. Keep.levelKA_alt with hH.toClassicalTheorems); the KMSW background (Mok, Chaudouard-Laumon,… | cite Pintar and build on it (the user, 23 Nov ~12:45): our single-place certificates for k = 21..26 would remove his simultaneous-trace hyp… |
| H20 | GCT | A complete positive formula for every outer-degree-five plethysm coefficient (G-036 with T-037) | proof checks; literature | checks |
| H21 | GCT | Polynomial-size formulas for stable hooks with varying outer degree (G-037 to G-039), and G-040's, polynomial for each fixed b (i… | proof checks; literature | checks |
| S06 | archive (1965 letter) | The 1965 letter's conjectures modulo algebraic equivalence: exactly when they hold over C; the Jacobian-summand bounds | literature; a re-proof of the C.4 bounds | checks |
| S22b | SGA 2 | The cone over Sigma RP^2 refutes SGA 2 XIII §6 Conjecture A (local Hurewicz) | check the quotation against SGA 2's text; literature | SGA 2 check, then literature |
| S23a | EGA | EGA corrections: 0_IV 19.3.12 restored (wrong proof, true statement; confirmed); the III 4.3.6 and IV 20.1.3 counterexamples are… | scope the package to what is not published; a 'Proof overview' section | the run's final |
| S22c | schemes | A non-separated, non-noetherian pair where degree-zero comparison holds but H^1 comparison with Z/n fails | check C:Goldman-branches; an independent re-proof; literature | checks |
| S15c | archive (cote 4, 8.6) / abelian surfaces | Abelian surfaces at p = 2: the monodromy group in degree one is GL_8(F_2) on the supersingular product E x E for all odd degrees… | the Coble identification lemma (unchecked); thm:ss-all-odd-Hasse at full depth; literature search including Hexagon | check the Coble lemma, then literature |
| S15d | archive (cote 4, 8.5.8) | The unit-root rank of the vanishing cohomology is positive once the degree is large (thm:all-X-explicit-positive-rank: the missin… | literature search (generic ordinarity, Illusie 1990, Ekedahl) including Hexagon; an independent re-proof | literature |
| S12c | archive (cote 29) | D:boundary-neighborhood settles the one-point case of D.2(ii) (a finite set of points is not covered in general); the B.2 stabili… | an independent re-proof; literature; for B.2 a re-proof of B.2u | checks |
| H25 | Hodge | The Hodge conjecture for abelian varieties is equivalent to a Poincare-pairing bound on the multiplier (bounded cycle degrees on… | the finishing prompt 70c's fixes (Voisin state of the field, title and abstract, Proof overview, why it matters, Markman quoted exactly, split the 12… | build 70c / 23 Nov evening: HODGE_FINISH final in (aaf69461): Paper A (66 pp.) = this row's paper, fixes 1-7 made, 8 partial (Schoen 2007 t… |
| P90b | AG | The Igusa surface in the ordinary case: Pic^tau flat for every Artinian deformation (contradicts claims of Chai, Chai-Oort and Pa… | an independent re-proof; read Chai's note directly | then the drafted emails to Chai-Oort and Partsch (on hold) |
| P91b | conformal | One cap determines all lengths: the single-cap theorem of Grothendieck's conformal surgery (Paper 4, Thm 1.1) | comparison with the infinite-grafting literature (Gupta, Gupta-Mj, Dumas); the run's separate re-proof recorded as a check event | the comparison |
| P91c | topology | The genus of Grothendieck's relative-position surface (cote 154), with the 23 and 47 crosscap counts | a read of the local topology proof; an independent recount of c_3 | the run's final |
| H30b | Alpoge (ALP_MACHINE) | Abelian coefficient fields cannot carry normalized ideal generators: K imaginary quadratic with mu(K) = {+-1}, F/K finite abelian… | literature search for Theorem A (may be known); read LIFT107-109; written as a section of the chain-length note (H30) | with H30 |
| H25c | Hodge (HODGE_FINISH) | Obstructions to cycle constructions and criteria for Mumford's exceptional classes (Paper B, 88 pp.): if one specified quadratic… | open Bolognesi-Laterveer before the half-twist remark is posted; a check of the overview; page view | after H25 |
| P91d | conformal (POLISH_TOPOLOGY_PERIODS) | Removing a collar from a hyperbolic surface with geodesic boundary: the conformal factor solves Delta u = e^{2u} - 1, d_n u = k_g… | targeted check of the positivity and sign-change proofs; literature (grafting, Fenchel-Nielsen deformations); a short note | - |
| P90f | AG (POLISH_ALGEBRAIC_GEOMETRY) | Adjoint and tangent-line bigness for surfaces in characteristic p (Paper 2, the very-ample section: curve-genus lemma; numerical… | literature search | - |
| P90g | AG (POLISH_ALGEBRAIC_GEOMETRY) | Over every base, a projective bundle over an abelian torsor is a scheme only if the torsor is | the proof read | - |
| P90h | AG (POLISH_ALGEBRAIC_GEOMETRY) | On a normal surface, an algebraically trivial p-torsion line bundle trivial on a curve Y with Y^2 > 0 never reaches conductor equ… | the run's isolated reconstruction (stability); literature: Esnault 2006 (partial connections for p-torsion line bundles), Langer 2011, with Hexagon | after the run's final |
| P91f | algebra (POLISH_TOPOLOGY_PERIODS) | A non-Noetherian inclusion R in S with every polynomial tensor map an isomorphism (a unique plethory) but Omega(R,S) and S not fl… | literature (Elliott's plethory papers, Borger-Wieland, Stacks 06RH); an independent re-proof of the colon identity; a short note | - |
| P91g | topology (POLISH_TOPOLOGY_PERIODS) | The three-sphere: pi_2 P_TOP(S^3) = Z/2 while pi_2 P_PL(S^3) = 0, a concrete PL/TOP concordance discrepancy | a Claude targeted read; literature (Hatcher's Smale conjecture, Kirby-Siebenmann) | - |
| P91h | topology (POLISH_TOPOLOGY_PERIODS) | pi_0 P_PL(M) = E(M) for compact PL M of dimension >= 6, without a smoothing (a PL form of Hatcher-Wagoner-Igusa) | a Claude read; comparison with Burghelea-Lashof-Rothenberg and Pedersen (may be known) | - |
| A133a | archive (cote 133; NIGHT_GROTHENDIECK_Q… | Grothendieck's question on cote 133, scan 29, answered no and classified in the curvilinear case: characteristic 0 is necessary;… | Cor. 27.3 and Thm 13.1/19.1 read in full; the external inputs (Burke-Walker, Blumberg-Gepner-Tabuada) at their locators; non-curvilinear singular rin… | the run's final; post with A133b as the lead result |
| AM112 | Alpoge's interface (ALP_MACHINE) | K imaginary quadratic with mu(K) = {+-1}, G in Cl(K) odd of order g: a field in which every J in G has a generator xi with /sigma… | literature search; LIFT112 A/C and LIFT113 proof reads | - |
| S15n | Cristaux (abelian surfaces, characteris… | Eventual defect two for every mixed pair of abelian surfaces in characteristic two, without the finite-field-model and index-zero… | a proof check; the run's open quantitative items | - |
| P91k | real algebraic geometry (POLISH_TOPOLOG… | Coarsest embedded smooth partitions exist for every semialgebraic set but depend on the embedding (the compact cusp) | literature (Whitney stratification, smooth-locus results) | - |
| ZH5 | zeta zeros (ZETA_HEAT) | An all-window lower rate for the Weil form: a_1(L), a_2(L) >= exp{-C mu^(1/d_MT) log mu (1 + log log mu)}, mu = e^(2L), d_MT = 0.… | a proof check; the credit split with Mori; open Voss | - |
| ZH6 | zeta zeros (ZETA_HEAT) | Collision laws for the CUE heat flow: the first collision is Weibull-3/2; early collisions are Poisson with intensity (3/2) sqrt(… | a whole-proof check | - |
| S93a | complexity (fleet) | Exact count /E/ + tau - 1 for edge functions of bipartite C4-free graphs among circuits whose formal monomials have at most one d… | 647 read live by fork 2 (672ae3a0, Claude Opus 5.5 at effort max, 24 Nov 11:50 UTC): still a conjecture, 0 attempts, nothing depends on it; free side… | mirror entry PUSHED by fork 2: github.com/KokunoYumeto/pequalnp-mirror commit d1464a4, extension/entries/X-meta-005.md (our 23 Nov proof as… |
| S93c | foundation (with H22) | Semimodules over every inverse semiring are module diagrams for (Q, F); K_0(R_0) is free on connected labelled posets (93 paper 1) | H22 v3's two false sentences: FIXED in v4 (24 Nov); literature on Clifford semimodules; a second reader for the other classifications | decide: H22 v4 or a second note |
| S93d | GCT | The rank-four order of the nonstandard Hecke algebra is free after inverting M exactly when 6 divides M; generic rank 114 (93 pap… | an independent check; comparison with GCT IV 11.8 | wait for the run's final |
| S93e | operator algebras | K_1 of the semilocal one-zero C*-algebras: nonsplit boundary sequence exactly for two or more primes; every finite torsion order… | a reader of paper 3 | wait for the run's final |

## 4. Prompts

**4.1 Built and waiting for the user to send** (TO_SEND/PRO/1_Archive_research_by_topic/, checked on disk 24 Nov ~21:1x
UTC; both lints passed at the last build of each):
- 95_GT_AFTER_H17 (built 23 Nov 18:48 UTC).
- 70d_HODGE_EFFECTIVE (built 23 Nov 18:48, rebuilt 22:38 with two NGQ Part C edits).
- 96_FLEET_HARD_LINKS (built 23 Nov 22:43, rebuilt 23:08 with the lambency-6 pass, updated 24 Nov 12:36 with 93 cp08; ZIP
  581656cd...).
- 68_CONNES_AFTER_RH (rebuilt 24 Nov 10:57 with the ZETA_HEAT final; ZIP 7097a500...). Codex revised 68 earlier (l.6211,
  l.6449): tell Codex what changed.
- Not ours: 78_SIGNED_COUNTS_AND_WINDING (the user sent it 23 Nov 01:1x, l.6443; its folder was left in place) and
  94_THETA_CIRCUIT_SIZE (Codex's).

**4.2 Sent, no return yet:** 99_VPVNP_WIRE_GEOMETRY (SENT 21:01 UTC 24 Nov); 98_VPVNP_HINGE answered, reply unread (1.6).

**4.3 To build, each waiting for an intake's result or a run's final:**
- ALP_MACHINE finishing prompt (2.4).
- 75's successor, after the NIGHT_AFTER_ALPOGE final (2.8).
- Finishing prompts for 90 and 91, after their runs' finals (2.5); 92's, after the 92c merge returns.
- 93's successor, and the lambda-ring / Artin successor (2.9).
- A write-up route for the GCT notes H02, H02b, H13, H23 in place of the rejected 56/56c (1.7).
- NGQ Part B as its own prompt, if the user wants it (2.7).
- H18: the k = 21..26 certificate computation or prompt (2.6).
- Carry into any DEG_L / HODGE_DIVISION successor: prompt 46b (sent) states DEG_L S-30 to S-41 too broadly (l.6770).
- Not to build: the Masullo-defect prompts (demoted by the user, 22 Nov ~00:4x, l.5740).

## 5. Corrections to report to a source (oldest first)

- **E1, Mulmuley, GCT VI (arXiv:0704.0229v4) Thm 1.6.1(d)** and the index hypotheses: NOTE_E1 drafted 21 Nov 01:06 (l.5544);
  held: Kahle-Michałek (arXiv:1507.07131v3) already answer part of it; needs the PH3 => PH2 qualifier and their credit
  (l.5554). Belongs with the GCT write-up (1.7). The GCT VIII note went out 24 Nov 11:54 (S93b; H23 with it): wait for his
  reply.
- **E2, Friedland-Lim (arXiv:1410.6072v3), two displays:** NOTE_E2 drafted 21 Nov, not sent (reports_20261120/errata/).
- **DEKM (arXiv:1910.11598v1), Thm 4.5 enumeration (K17 cp05):** held, the published version and data are paywalled (l.5626).
- **01b, Bhowmik-Pathak:** our own suggested repair needs k != 0; drafted 22 Nov ~04:00 with proof (l.5807); a second mail to
  the same authors: asks the user (still open at l.6220).
- **Addresses missing:** Partsch (06 bounced; P90b's Chai-Oort/Partsch drafts on hold for an independent re-proof),
  Knudsen (11), Grigoriev and Pitassi (07's co-authors, not reached).
- **Held in the 22 Nov outreach register, each needing a targeted check first** (grant_evidence/OUTREACH_REGISTER_20261122.md):
  Yamaguchi (LM6 A.46), Kent (EXIT_TOWER D.11-D.12), Wilkes (E.82/E.83; the paper not identified), Boggi and Funar (E.14,
  D.20, D.26, E.48), Porowski (LM8_PUSH A.20; the paper not identified), Schreieder (likely drop).
- **Morishita (T15/T17 against arXiv:2508.15971 Th. 2.2.8(2)) and Suzuki (S50: is it known?):** drafts in
  reports_20261123/h27_note/RECORDS.md, not sent (l.6670). The Suzuki e-mail of 24 Nov 18:47 was about ZH3, not S50.
- **Alpöge, the size floors (a fact about his formal hypotheses):** optional one-line note, not drafted (l.6250).
- **The 23 Nov intake drafts** (field_experts/intake_20261121/EMAIL_DRAFTS_INDEX_20261123.md), none sent: Grammatica
  (arXiv:2507.08568v2 Rem. 4.6: ready), the Stacks project (Tags 07BV, 0BTP: ready), Popescu 2022 p. 510 (ready), Bhatt
  (Constr. 4.7 typo: optional), Rains-Sam (Rem. 5.8 typo: optional), Liedtke (one look at his printed table first),
  Cotner-Zavyalov (Ex. 3.4.6(ii)), Milne (Abelian Varieties Rem. 8.5; Gerbes p. 23), Achter-Casalaina-Martin (sec. 1.7.2) (the
  last three: confirm at the source), Chai-Oort and Partsch (on hold, as above). The user's rule of 24 Nov ~11:2x lets the
  ready ones go when confident.
- **Stacks 60.22.1, the p = 2 formula** (from the S17a note): after S17a is posted.
- **Zheng (P90i):** both published addresses bounced (18:35, 18:42); his Stony Brook page has a contact form only; the user
  was asked (l.6865).
- Closed, for the record: Esnault (sent, reply answered 19:12), Thakur (replied 12:00; nothing more), Elliott (has died; nothing
  more is sent), Boyle-Chen, Galvin, Orson-Powell-Randal-Williams, Mukai, Kweon (resent to SNU), Suzuki (ZH3), Mulmuley (GCT VIII)
  all sent 24 Nov (reports_20261124/EMAILS_SENT_20261124.md).

## 6. Decisions left to the user

- Send 68, 70d, 95, 96 (4.1).
- The route for the unread Longue Marche, anabelian and Dérivateurs registers (1.1-1.2), and whether statement-level coverage
  of the sweep-3 runs is wanted (1.3).
- 01b to Bhowmik-Pathak; Zheng's contact form (section 5).
- H07 v3 and H15: post or not (section 3).
- NGQ Part B as its own prompt (2.7).
- The Masullo lines on our public GRH page (2.3).
- pequalnp: the Reddit comment (pequalnp_work/fleet_mirror/RED_TEAM_FINAL_DRAFTS.md); filing L-meta-647 with the fleet
  (l.6839).
- The Reddit drafts of 21 Nov, not posted: reports_20261120/reddit_double_grh/DOUBLE_GRH_REDDIT_DRAFT.md and
  DELIGNE_SIGN_ONLY_REDDIT_DRAFT.md.
- shwarm.org: splitting "explain one AI proof" into up to three branches (l.6615).
- GitHub, other authors' works and licences (task_notes/other_authors_works_removal_20261122.md; reports_20261122/
  public_push_check/FORCE_PUSH_PLAN_20261122.md): the older pushes' documents, the text extractions and prompt packs, group C,
  the history-rewrite plan (on private copies, nothing pushed); the Lean licence notices (l.6136, l.6183); K17's data files
  (l.6050, l.6135).
- The disk agent's questions (af351bc8, Claude Opus 5.5 at effort max, holding; PLAN l.82): 24 superseded checkpoints
  (7.57 GB), eight dead junctions, F:\RW (24.5 GB), the Drive duplicates (694 GB), ocr_env (5 GB), F:\dowloads (~100 GB not on
  Drive), the empty F:\disk_pack_20261115; hibernation needs an elevated `powercfg /h off` (l.6828).
- supersede_carry.py deletes older versions of changed files: asked 22 Nov (l.5838-5840); used for retiring checkpoints since
  23 Nov evening; no answer recorded.
- Fable a157422a (Claude Fable 5.2 at effort max): its own V35 task of 13 Nov is unfinished; continuing needs the user's word
  (l.5663).
- The data bank of Grothendieck's foibles: publication only on the user's word (20 Nov, l.5012).
- Unread Proton replies: brilliant.design and Richard Zach (PLAN l.121).
- Remind the user: the split-zero follow-up note (memory claude-agenda; PLAN l.127).
- COUNTING_VARIETIES (prompt 63): Codex's or ours (1.4).

## 7. Held by other sessions (pointers only)

- **Second passes** (main session's second-pass track): run A of Les Dérivateurs (RA01-RA40, built; pilot read; the user
  sends), IMW01 Work pilot (batch_17), batch_16 Work resend (47 folders), the 110 waiting SP/SR prompts, witness P.
- **S6** (sessions 5c7e951b and aacf1302): continuation 10 running from cp70 (cp71 filed 20:27 UTC); the Paper II reading's
  corrections of others' work, P19 (HKP Cor. 1.3 / AC26, draft to Alpöge unsent) and P21 (Fujimoto 1988 Thm 2.8, blocked by a
  CAPTCHA) (l.6863); the GitHub purge request and Engel's follow-up (S6 repository; the user's yes); Papers III-IV deposits.
