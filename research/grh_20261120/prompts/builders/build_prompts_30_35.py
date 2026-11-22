"""Build Pro research prompts 30-35 (20-21 Nov 2026, main session, Claude Opus 5.5 at effort max), at the user's word,
21 Nov ~23:2x UTC: "we also want to make prompts that push all the other insights about how the GRH proofs push through
the AG program, which is probably technically a priority". With 22:23 UTC: "Spread them out. Don't make it a huge 10-hour
one. Like, parallelize it." Prompt 22 (one large prompt) is split into 30-35 by topic (its Δ item is prompt 29).
Sources of the questions: our Fable agent's ranked suggestions (reports_20261120/alpoge_rh/bridges/FABLE_PROGRAM_
SUGGESTIONS_20261120.md), the bridges run (QUESTIONS.tsv, LEDGER.md), the intakes of 20 Nov.
Reuses the shared blocks of build_prompts_24_29.py (ALPOGE, MASULLO, how_to_work), with the language paragraph and the
IMPLICATIONS item for the AG programme instead of P vs NP. Then packs (pack_one_zip.py), lints, and updates ORDER.md.
usage: python -I -B build_prompts_30_35.py"""
import pathlib, re, shutil, subprocess, sys, zipfile
sys.stdout.reconfigure(encoding="utf-8")
HERE = pathlib.Path(__file__).resolve().parent
exec((HERE / "build_prompts_24_29.py").read_text(encoding="utf-8").split("SIX = (")[0])
F22 = S / "from_22"
TR = D / "grothendieck_archive_transcription_20261110/text_of_record/pages"
SORTED = D / "field_experts/intake_20261120/SORTED"
SR3 = D / "results_register/horizontal/sweep3"
MIDX = D / "reports_20261120/masullo_statements/STATEMENTS_INDEX.md"
Z22 = Q / "22_ALPOGE_RH_bridges_into_the_programme/ALPOGE_RH_bridges_into_the_programme.zip"
if not F22.exists():
    with zipfile.ZipFile(Z22) as z:
        z.extractall(F22)


def arch(cote, scans):
    return {f"ARCHIVE_{cote}_scan{n:03d}.tex": TR / str(cote) / f"{cote}_scan{n:03d}.tex" for n in scans}


def arch_all(cote):
    return {f"ARCHIVE_{f.name}": f for f in sorted((TR / str(cote)).glob("*.tex"))}


AG_LANG = """## The language of the results

State every finding in the language of algebraic geometry and of Grothendieck's frameworks: schemes over Z, ℓ-adic
sheaves, weights and purity (SGA 4, SGA 5, Weil I and II), crystals and divided powers, λ-rings, motives where they apply.
For each finding, say where it lives in Grothendieck's texts: the archive by cote and scan, the SGA, EGA or FGA by exact
locator.

"""
IMPL = ("4. **`IMPLICATIONS.md`**: what the findings change in our programme: Grothendieck's texts by cote and scan, the\n"
        "   open rows of our runs by run and statement id, and the conditional statements of the literature that become\n"
        "   theorems (unconditional by Alpöge, or conditional on Masullo only)." + "\n5. **TRANSCRIPTION_NOTES.tsv**: every place where the mathematics shows that our text of record misreads\n   Grothendieck's page (a formula, an index, a sign, a twist, a word), one row each: cote, scan, line, our reading,\n   the reading the mathematics requires, the reason, and how sure you are. Our transcription of his archive is the\n   project's base layer; these rows go to its second pass against the scans.")


def hw(main_q, short):
    t = how_to_work(main_q, short).replace(LANG_PARAGRAPH, AG_LANG)
    t, n = re.subn(r"4\. \*\*`IMPLICATIONS\.md`\*\*:.*?\(cote and scan\)\.", lambda m: IMPL, t, flags=re.S)
    assert n == 1 and AG_LANG in t, "template changed"
    return t


PAR = ("This prompt is one of six run in parallel on 21 November 2026 on what the two proofs of 20 November (Alpöge's, "
       "cited as a theorem; Masullo's, a draft) make true in Grothendieck's programme. The others treat: the anabelian "
       "and Galois line (30), step 17 and the K-groups of Z (31), the sign-only proof as the Hodge-index route (32), the "
       "trace formula of cote 1 (33), divided powers and the multiplicity of step 2 (34), and the zeta functions of "
       "schemes and motives (35). A second set (24-29) treats P versus NP through geometric complexity theory and the "
       "invariant Δ on the Grothendieck-Teichmüller group. Keep to this prompt's questions; the others are asked there.\n")
AL4 = ["ALPOGE_remark.pdf", "ALPOGE_Main.lean", "ALPOGE_Statements.lean", "ALPOGE_LEAN_SCAN.tsv"]
FAB = {"FABLE_PROGRAM_SUGGESTIONS_20261120.md": AR / "bridges/FABLE_PROGRAM_SUGGESTIONS_20261120.md",
       "FABLE_PROGRAM_SUGGESTIONS_20261120_EXPLAINED.md": AR / "bridges/FABLE_PROGRAM_SUGGESTIONS_20261120_EXPLAINED.md"}
MASF = {"MASULLO_the-music-of-the-primes.pdf": MAS, "MASULLO_STATEMENTS_INDEX.md": MIDX}
BRQ = {"BRIDGES_QUESTIONS.tsv": AR / "bridges/QUESTIONS.tsv", "BRIDGES_LEDGER.md": AR / "bridges/LEDGER.md"}
FLAGS = {"BRIDGE_FLAGS.tsv": D / "field_experts/intake_20261120/BRIDGE_FLAGS.tsv"}
HUNCH = {"WARGAME_MATH_HUNCHES_20261112.md": D / "grothendieck_archive_montpellier/WARGAME_MATH_HUNCHES_20261112.md"}
LMAP = {"ALPOGE_LEAN_MAP_20261120.md": AR / "ALPOGE_LEAN_MAP_20261120.md"}
FABLE_WHO = "Our Fable agent (Claude Fable 5.2 at effort max; the attached suggestions file, unchecked: leads, not results)"

P = {}

P["30_GRH_ANABELIAN_Hooley_Chebotarev_and_cote_149"] = ("AN_GRH", f"""# AN_GRH: the two GRH proofs through the anabelian and Galois line of Grothendieck's programme

{PAR}
{ALPOGE}
{MASULLO}
## Where our files stand

- Alpöge's theorems give GRH for Dirichlet L-functions, hence RH for the Dedekind zeta functions of abelian fields
  (our bridges run, F2). Most analytic inputs of the anabelian line need more:
  - Hooley (J. reine angew. Math. 225, 1967) proved Artin's primitive root conjecture, with its density, assuming GRH
    for the Dedekind zeta functions of the Kummer fields Q(ζ_n, a^(1/n)). These fields are not abelian over Q, so
    Alpöge's theorems do not reach them. Masullo's claim does: the trivial character of his Hecke L-functions gives the
    Dedekind zeta function of every number field.
  - The effective Chebotarev theorem (Lagarias-Odlyzko 1977; Serre, Publ. Math. IHÉS 54, 1981) bounds the least prime
    with a given Frobenius class in a Galois extension L/Q by a power of log d_L, assuming GRH for ζ_L: Masullo again.
  - Bach (Math. Comp. 55, 1990): under GRH for Dirichlet L-functions, (Z/N)^× is generated by the primes below 2 log² N.
    This one follows from Alpöge's theorems.
- {FABLE_WHO}, suggestion 7, points to two uses:
  - the Bach bound as a certificate for the cyclotomic coordinate of every finite level of GT̂_0 used in our shadow
    computations;
  - route 2 for A1 (cote 149, scans 35-36; "Artin's conjecture on average" in our intake), which needs GRH for Kummer
    fields.
- Our anabelian, GT and Longue Marche runs (GPT-6 Astra, ChatGPT Pro mode) are attached as row lists, every row with its
  statement. `BRIDGE_FLAGS.tsv` flags, for all our runs, the rows that name GRH, Chebotarev, Artin's conjecture, the Weil
  bounds or purity.

## The task

1. **A1 by route 2.** State A1 exactly as cote 149 (scans 33-38) and our runs state it, and prove it from Masullo's GRH
   through Hooley's method. Then decide what Alpöge's theorems alone give for it.
2. **Every row that waits on GRH or an effective Chebotarev bound.** Go through the attached row lists and
   `BRIDGE_FLAGS.tsv`. For each row whose statement or proof uses GRH, an effective Chebotarev bound, Artin's conjecture
   or a least-prime bound: name the exact L-functions it needs, and decide it as unconditional by Alpöge, conditional on
   Masullo only, or beyond both (naming the missing statement).
3. **The finite levels of GT̂_0.** Write the certificate the Bach bound gives for the cyclotomic coordinate of each
   finite level our computations used, with the explicit bound, and check it on those levels.
4. **Galois images.** Where our rows use Serre's open-image theorem, the Faltings-Serre method or the separation of
   Galois representations by Frobenius traces, give the effective forms that Masullo's claim makes conditional theorems,
   with their constants.

## The attached files

- `ARCHIVE_149_scan033.tex` to `ARCHIVE_149_scan038.tex`: Grothendieck's text of record, cote 149.
- `INTAKE_ANABELIAN_149_FINAL_20261114.md`; the row lists `SORTED_ANABELIAN_A1.md`, `SORTED_ANABELIAN_A1_SUCCESSOR.md`,
  `SORTED_ANABELIAN_SUCCESSOR.md`, `SORTED_GT_TOWER_CHECK.md`, `SORTED_LM7_PUSH.md`, `SORTED_LM8_PUSH.md`;
  `BRIDGE_FLAGS.tsv`.
- `MASULLO_the-music-of-the-primes.pdf` and `MASULLO_STATEMENTS_INDEX.md`; `ALPOGE_remark.pdf`, `ALPOGE_Main.lean`,
  `ALPOGE_Statements.lean`, `ALPOGE_LEAN_SCAN.tsv`; `BRIDGES_QUESTIONS.tsv` and `BRIDGES_LEDGER.md` (our run of 20 Nov).
- `FABLE_PROGRAM_SUGGESTIONS_20261120.md` and `..._EXPLAINED.md`.

{hw("A1, Grothendieck's question of cote 149, proved from Masullo's GRH through Hooley's method, and what Alpöge's theorems alone give for it.", "AN_GRH")}""",
    AL4,
    {**arch(149, range(33, 39)), **MASF, **BRQ, **FLAGS, **FAB,
     "INTAKE_ANABELIAN_149_FINAL_20261114.md": D / "pro_intake_20261114/INTAKE_ANABELIAN_149_FINAL_20261114.md",
     **{f"SORTED_{r}.md": SORTED / f"{r}.md" for r in ["ANABELIAN_A1", "ANABELIAN_A1_SUCCESSOR", "ANABELIAN_SUCCESSOR",
                                                        "GT_TOWER_CHECK", "LM7_PUSH", "LM8_PUSH"]}})

P["31_STEP17_K-groups_of_Z_Soule_and_pro-l_kernels"] = ("K17", f"""# K17: step 17 of Alpöge's note, the K-groups of Z, Soulé's characters and the pro-ℓ kernels of the tripod

{PAR}
{ALPOGE}
## Where our files stand

- **Alpöge's step 17** (page 4 and footnote 6): for the classes in H^1(o_E[1/ℓ], Q_ℓ/Z_ℓ(−e)) that twisting cannot
  kill, the note proves "a significant weakening of Vandiver". He believes the vanishing of a number of K-groups of Z
  follows ("I had Lichtenbaum"). Our map of the Lean archive found no file named for Vandiver, so the exact statement is
  taken from the note.
- **The literature, cited from memory; verify each locator before use:**
  - Kurihara (1992): Vandiver's conjecture at ℓ is equivalent to the vanishing of K_{{4k}}(Z) ⊗ Z_ℓ for all k.
  - Soulé: his characters κ_m (m odd, m ≥ 3) are nonzero, and their images are governed by the ℓ-parts of the
    K-groups of Z.
  - Sharifi: for regular ℓ, the kernel field of G_Q → Out π_1^(ℓ)(P^1 − {{0, 1, ∞}}) is the maximal pro-ℓ extension of
    Q(μ_ℓ) unramified outside ℓ.
  - Deligne-Goncharov (LaTeX attached) and Brown: mixed Tate motives over Z.
- **Our runs:**
  - LM6 A.44-A.45: the kernel question, open at ℓ = 2 and at the irregular primes (its intake is attached);
  - bridge B3 of the war game: grt_1 and mixed Tate motives over Z (the war-game file is attached);
  - SA06's E.4 rows, which tabulate groups H^1(o_E[1/ℓ], ...);
  - cote 149, scans 79-85: Grothendieck's H^1(S, T) and Kummer sequences, with T = Ẑ(1).
- {FABLE_WHO}, suggestion 5, proposes that if the K_{{4k}}(Z) of footnote 6 vanish, then two things hold beyond the
  regular primes: the generators σ_{{2k+1}} of the Galois image in the pro-ℓ group of the tripod exist integrally, and
  the kernel field is the maximal pro-ℓ extension of Q(μ_ℓ) unramified outside ℓ.

## The task

1. **Step 17.** State it exactly: the fields E, the twists e, the primes ℓ and the classes. Prove it from the note's
   argument and the theorems it cites.
2. **The K-groups of Z.** Decide which K_{{4k}}(Z) ⊗ Z_ℓ vanish as a consequence, for which k and ℓ, and state the
   relation to Vandiver's conjecture at ℓ exactly.
3. **LM6 A.44-A.45.** Decide them at the irregular primes and at ℓ = 2 with what items 1 and 2 give.
4. **B3, integrally.** For the ℓ that item 2 covers, decide whether the generators σ_{{2k+1}} of the image in the
   pro-ℓ group of the tripod exist integrally. Give the consequences for grt_1 and for the Deligne-Ihara statement over
   Z_ℓ.
5. **Cote 149, scans 79-85.** Read Grothendieck's H^1(S, T) and Kummer sequences against items 1-4: what his text asks,
   and what is now proved.

## The attached files

- `ARCHIVE_149_scan079.tex` to `ARCHIVE_149_scan085.tex`.
- `INTAKE_LM6_FINAL_20261114.md`; `INTAKE_RESEARCH_SA06_20261120.md` (the E.4 rows); `PROGRAM_WARGAME_ROUND2_20261112.md`
  (bridge B3, S9).
- `LIT_Deligne_Goncharov_mixed_Tate_motives/`: LaTeX source.
- `ALPOGE_remark.pdf`, `ALPOGE_Main.lean`, `ALPOGE_Statements.lean`, `ALPOGE_LEAN_SCAN.tsv`, `ALPOGE_LEAN_MAP_20261120.md`
  (our map of the Lean archive); `BRIDGES_QUESTIONS.tsv` (Q06).
- `FABLE_PROGRAM_SUGGESTIONS_20261120.md` and `..._EXPLAINED.md`.

{hw("the exact statement of step 17 and what it proves about the K-groups of Z and Vandiver's conjecture, then LM6 A.44-A.45 at the irregular primes and at ℓ = 2.", "K17")}""",
    AL4 + ["INTAKE_RESEARCH_SA06_20261120.md", "LIT_Deligne_Goncharov_mixed_Tate_motives"],
    {**arch(149, range(79, 86)), **LMAP, **FAB, "BRIDGES_QUESTIONS.tsv": AR / "bridges/QUESTIONS.tsv",
     "INTAKE_LM6_FINAL_20261114.md": D / "pro_intake_20261114/INTAKE_LM6_FINAL_20261114.md",
     "PROGRAM_WARGAME_ROUND2_20261112.md": D / "grothendieck_archive_montpellier/PROGRAM_WARGAME_ROUND2_20261112.md"})

P["32_HODGE_SIGN_sign-only_purity_as_the_Hodge_index_route_cotes_16_44"] = ("HODGE_SIGN", f"""# HODGE_SIGN: the sign-only proof of Weil and Deligne as the Hodge-index route of cote 16, and its arithmetic form on cote 44

{PAR}
{ALPOGE}
## Where our files stand

- **Alpöge's step 5.** Bertini gives a definite sign from middle cohomology, "one off from the one on M^k". Iterating
  Parseval gives square-root cancellation, and "opposite signs mean no cancellation of inverse roots". He calls this a
  "sign-only proof of Weil and Deligne".
- **Grothendieck's cote 16** (Book II, the ring of correspondences):
  - the universal Lefschetz ring Φ (scans 14-18);
  - the hyperplane induction and the intersection form on the evanescent part of a hyperplane section (scans 34-40);
  - Weil from his conjectures C and A, and semisimplicity from C with I(X × X) (scans 49-50).
- **SA06's intake** (Claude Opus 5.5 at effort max, attached). The split sixfold quadric of E.3u has primitive middle
  motive Q(−3), with L-function ζ(s − 3). Its class ζ, with ζ² = −2, carries the definite sign of step 5. If the
  sign-only proof holds, it carries out the plan of Grothendieck's letter (absolute values "justiciable de B") without
  the Hodge standard conjecture.
- {FABLE_WHO}, suggestions 4 and 6, proposes:
  - The sign of step 5 is the Hodge-index sign on the evanescent part. On powers of the hexagonal CM curve every
    algebraic class is a Lefschetz class, and there the Hodge standard conjecture holds (Milne).
  - With the Bost slope inequality (step 13), the positivity on arithmetic models is an arithmetic Hodge-index
    statement (Gillet-Soulé, Künnemann) that reaches cote 44: Th. 4, and Th. 5 with its "variante locale" (hunch H9).
  - The SL_2 of the lift chain is the Lefschetz sl_2 of cote 16. The divisibilities of steps 9, 10 and 15 are then
    indices of the integral order generated by L and Λ, computed by hunch H8 (integral hard Lefschetz with divided
    powers; Wilson's diagonal form).
- **Our bridges run:**
  - Q03, cote 34 scan 64 (Remarque 1.17, struck): the openness of [π_0, H] "semblerait devoir résulter de l'hyp. de
    Riemann-Weil en dim. quelconque". It is open.
  - Q05, the standard conjectures: open.

## The task

1. **The abstract sign-only theorem.** State step 5 as a theorem on families of exponential sums, or of ℓ-adic sheaves,
   with exactly the hypotheses it uses, and prove it from the note's argument.
2. **Cote 16.** Decide whether the sign of item 1 is the sign of the intersection form on the evanescent part (scans
   34-40). Decide accordingly whether the sign-only argument proves Weil's theorem by Grothendieck's own route of scans
   49-50 without the Hodge standard conjecture. Give the cases where it does: powers of CM curves, quadrics, abelian
   varieties.
3. **The letter's plan.** For the split sixfold quadric and for the varieties of SA06's C.1 rows, prove or refute that
   the sign-only argument gives the absolute values asked for.
4. **Cote 44.** With the Bost slope inequality, state and prove the arithmetic Hodge-index statement the argument gives,
   and say which cases of Th. 4 and Th. 5 it settles.
5. **Cote 34, scan 64 (Q03).** Read 1.1 on scans 53-63 first, then derive from Deligne's purity (Weil I) the openness he
   asks for.
6. **The Lefschetz sl_2.** Decide whether the Arthur SL_2 of the lift chain is the Lefschetz sl_2 of the universal ring Φ
   (scans 14-18). For small m, compute the divisibility of step 10 against Wilson's diagonal form.

## The attached files

- `ARCHIVE_16_scan014.tex` to `ARCHIVE_16_scan018.tex`, `ARCHIVE_16_scan034.tex` to `ARCHIVE_16_scan040.tex`,
  `ARCHIVE_16_scan049.tex`, `ARCHIVE_16_scan050.tex`; the pages of cote 44; `ARCHIVE_34_scan053.tex` to
  `ARCHIVE_34_scan064.tex` and `ARCHIVE_34_scan074.tex`.
- `INTAKE_RESEARCH_SA06_20261120.md`; `WARGAME_MATH_HUNCHES_20261112.md` (H8, H9).
- `ALPOGE_remark.pdf`, `ALPOGE_Main.lean`, `ALPOGE_Statements.lean`, `ALPOGE_LEAN_SCAN.tsv`. `ALPOGE_LEAN_MAP_20261120.md`
  names the libraries `PositivityTheory` and `Formalism/HermitianCurvature`.
- `BRIDGES_QUESTIONS.tsv` and `BRIDGES_LEDGER.md`; `FABLE_PROGRAM_SUGGESTIONS_20261120.md` and `..._EXPLAINED.md`.

{hw("whether the sign of Alpöge's step 5 is the Hodge-index sign on the evanescent part of cote 16, so that the sign-only argument proves Weil's theorem by Grothendieck's own route without the Hodge standard conjecture, and in which cases.", "HODGE_SIGN")}""",
    AL4 + ["INTAKE_RESEARCH_SA06_20261120.md"],
    {**arch(16, list(range(14, 19)) + list(range(34, 41)) + [49, 50]), **arch_all(44),
     **arch(34, list(range(53, 65)) + [74]), **HUNCH, **LMAP, **BRQ, **FAB})

P["33_TRACE_DET_cote_1_trace_formula_and_the_determinants"] = ("TRACE_DET", f"""# TRACE_DET: Grothendieck's Hilbert-space trace formula (cote 1) against the determinants of the two proofs

{PAR}
{ALPOGE}
{MASULLO}
## Where our files stand

- **Cote 1**, sheets 79-80 and 111-112 (SA23 intake, Claude Opus 5.5 at effort max, attached), hold Grothendieck's
  proof of the trace formula for trace-class operators. He announced it in 1951 and 1955 and dropped it in the 1956
  Erratum as "essentially contained in Weyl". The intake applies it to the zeta function:
  - Ξ(√w)/Ξ(0) = det(1 − wB) with B trace class, unconditionally;
  - RH is equivalent to B ≥ 0, so with Alpöge's theorem B ≥ 0 now holds;
  - no trace-class operator has Ξ itself as its determinant, because its zeros are too dense.
- **Alpöge's determinants.**
  - Steps 1, 4 and 7: a Stepanov determinant; W(1_S) ≥ 0 "via a determinant"; determinants containing Gan-Gross-Prasad
    periods.
  - Steps 3 and 5: the count qN = M^k + R by iterated Parseval.
- {FABLE_WHO}, suggestion 3: it proves a toy count and proposes the link.
  - **The toy.** For t ≥ 0 on Z/q, q·N_k = M^k + R_k with |R_k| ≤ (q − 1)·q^((k−1)/2)·‖t‖_2²·‖t‖_∞^(k−2). The terms
    with h ≠ 0 are moments ⟨t, K_h D_t K_h ⋯ D_t K_h t⟩ of "multiply by t, then Fourier transform".
  - **The proposal.** B is that operator and the sums are its moments. "Opposite signs, no cancellation" is then
    Landau's lemma for Σ N_k w^k, the positivity Deligne uses on even tensor powers.
- **Masullo's draft:** a trace formula on "orbital Schauder bases" for the idelic zeta functions (§§1.2-1.4), and a
  section on the programmes of Connes and Deninger (§1.5).
- **Connes-Consani:** Weil positivity at the archimedean place (LaTeX attached).

## The task

1. **The toy.** Prove the agent's bound or refute it with the corrected statement.
2. **B.** Write Grothendieck's operator B of cote 1 for Ξ concretely: its Hilbert space and kernel. Decide whether
   Alpöge's determinants (steps 1, 4, 7) are Fredholm determinants det(1 − wB) or their finite analogues, and whether
   his sign gives B ≥ 0 directly.
3. **Masullo's trace formula.** State his main trace formula from the draft, by statement number. Compare it with cote
   1's trace formula and with Weil's explicit formula, and say what the positivity statement is in each.
4. **The RH programmes.** For each of the following, state what it now asserts as a theorem given Alpöge's RH, and what
   part remains its own open question (for instance the existence of Deninger's cohomology): Weil's positivity
   criterion, Li's criterion, Beurling-Nyman, de Branges, Connes's trace formula and Deninger's programme.
5. **Finite fields.** Write the analogue of cote 1's statement for the zeta function of a curve over F_q, where B is
   Frobenius on H^1 up to scaling, and check the dictionary on it.

## The attached files

- `ARCHIVE_1_scan078.tex` to `ARCHIVE_1_scan082.tex` and `ARCHIVE_1_scan110.tex` to `ARCHIVE_1_scan113.tex`.
- `INTAKE_RESEARCH_SA23_20261120.md`.
- `LIT_Connes_Consani_Weil_positivity_archimedean/`: LaTeX source.
- `MASULLO_the-music-of-the-primes.pdf` and `MASULLO_STATEMENTS_INDEX.md`.
- `ALPOGE_remark.pdf`, `ALPOGE_Main.lean`, `ALPOGE_Statements.lean`, `ALPOGE_LEAN_SCAN.tsv`, `ALPOGE_LEAN_MAP_20261120.md`.
- `FABLE_PROGRAM_SUGGESTIONS_20261120.md` and `..._EXPLAINED.md`.

{hw("whether Alpöge's determinants are Grothendieck's Fredholm determinant det(1 − wB) of cote 1, so that his sign is the positivity B ≥ 0, and how Masullo's trace formula compares.", "TRACE_DET")}""",
    AL4 + ["INTAKE_RESEARCH_SA23_20261120.md", "LIT_Connes_Consani_Weil_positivity_archimedean"],
    {**arch(1, list(range(78, 83)) + list(range(110, 114))), **MASF, **LMAP, **FAB})

P["34_DP_MULT_divided_powers_and_the_multiplicity_of_step_2"] = ("DP_MULT", f"""# DP_MULT: the multiplicity of step 2 as a divided-power structure, and Grothendieck's crystals

{PAR}
{ALPOGE}
## Where our files stand

- **Alpöge's step 2** (9 Oct). On a CM curve the invariant derivation D satisfies D^p ≡ 0 for p inert in K, and
  D^a θ(0)/Ω^a is divisible by p^(a/p + a/p³ + ... − O(log a)). Page 1 names the obstacle that multiplicity meets over Z:
  "differentiating whole numbers".
- {FABLE_WHO}, suggestion 2, gives a proof that has not been checked.
  - **The bound.** For a one-dimensional formal group F of height h over W(k):
    v_p(D^a f(0)) ≥ v_p(a!) − a/(p^h − 1) − O(log a).
  - For h = 2 the gain is a·p/(p² − 1) = a/p + a/p³ + ..., the note's exponent. For h = 1 there is none, which is why
    p must be inert.
  - **The proposed use.** CM abelian varieties whose reduction has a formal summand of large height win multiplicity
    faster, with a gain of 1/(p − 1) − 1/(p^h − 1) per derivative.
- **Grothendieck:**
  - cote 54, scans 5-7: the extension S_A as an extension of p-Lie algebras; his boxed "t_A^∨ est muni de la puiss.
    p-ième nulle"; "comparer ... avec ce que donne la dualité de Cartier";
  - the crystals (cote 4; the letter to Tate);
  - divided powers in cote 16 (scan 14) and cote 47 (scan 9), and hunch H8.
  The agent also cites Katz, "Divisibilities, congruences, and Cartier duality" (1981), from memory: this exponent for
  Hurwitz numbers.
- **Suggestion 9** of the same file: Borger's λ-rings and F_1, binomial rings, and Grothendieck's 1976 notes (cotes 133,
  153, 136-137).

## The task

1. **The bound.** Prove it, or refute it with the corrected statement, for every height h, with the exact error term.
2. **Step 2.** Decide whether the note's divisibility is exactly the case h = 2 of item 1 (supersingular reduction, the
   Hasse invariant D^p ≡ 0), and if not, what else it uses.
3. **Higher height.** State and prove the multiplicity gain for CM abelian varieties whose reduction has a formal summand
   of height h. Decide whether a chain of such lifts gives the multiplicity of step 8 with fewer lifts: the shorter
   proof the note expects.
4. **Grothendieck's text.** Read cote 54, scans 5-7, and cote 4 against items 1-3: his p-Lie algebras with zero p-th
   power and Cartier duality. Say what he asks and what is now proved.
5. **Suggestion 9.** Decide whether Frobenius lifts that are the identity (binomial structures) give the homotopy side
   of "differentiating whole numbers". Give a precise statement with its proof.

## The attached files

- The pages of cotes 54, 47 and 4; `ARCHIVE_16_scan014.tex` to `ARCHIVE_16_scan018.tex`.
- `WARGAME_MATH_HUNCHES_20261112.md` (H8).
- `LIT_Borger_lambda_rings_field_with_one_element/`: LaTeX source.
- `ALPOGE_remark.pdf`, `ALPOGE_Main.lean`, `ALPOGE_Statements.lean`, `ALPOGE_LEAN_SCAN.tsv`, `ALPOGE_LEAN_MAP_20261120.md`.
- `FABLE_PROGRAM_SUGGESTIONS_20261120.md` and `..._EXPLAINED.md`.

{hw("the divided-power bound for formal groups of height h, whether it is exactly the multiplicity mechanism of Alpöge's step 2, and then the higher-height gain.", "DP_MULT")}""",
    AL4 + ["LIT_Borger_lambda_rings_field_with_one_element"],
    {**arch_all(54), **arch_all(47), **arch_all(4), **arch(16, range(14, 19)), **HUNCH, **LMAP, **FAB})

P["35_ZETA_TWO_RH_for_schemes_and_motives_from_the_two_proofs"] = ("ZETA_TWO", f"""# ZETA_TWO: RH for the zeta functions of schemes over Z and of motives over Q, from the two proofs, and the conditional theorems of our files

{PAR}
{ALPOGE}
{MASULLO}
## Where our files stand

- **Our bridges run** (Claude Opus 5.5 at effort max; its questions, ledger, implications and paper are attached):
  - F1: if the point counts of a scheme X of finite type over Z are combinations of χ(p)^r p^(ri) (abelian Artin-Tate
    type), then ζ_X is the matching product of the L(s − i, χ). Its non-integer zeros and poles lie on Re s = i + 1/2,
    by Alpöge.
  - F2: the same for the Dedekind zeta functions of abelian fields.
  - Q01 (RH for ζ_X in general, after Serre 1965) and Q02 (RH for the L-functions of pure motives over Q, after Deligne
    1979) are open. Their gate is GRH for non-abelian Artin L-functions together with RH in positive weight.
- **Masullo's claim** covers the Hecke L-functions of every number field. By Brauer's induction theorem every Artin
  L-function is a quotient of products of Hecke L-functions with integer exponents. His claim would therefore put every
  zero and every pole of every Artin L-function inside the critical strip on the critical line. It would not give
  Artin's holomorphy conjecture.
- **The intakes of 20 Nov** (Claude Opus 5.5 at effort max, attached) record statements that wait on GRH or on the
  absence of a Siegel zero:
  - SA06 A.8a: Littlewood bounds for supersingular counts;
  - SA07: Faltings heights of CM elliptic curves, and Colmez's formula for CM by Q(ζ_5);
  - SA20 A5.011: K̃_0(Z[C_23]) through Cl(Q(ζ_23)) and L(0, χ);
  - REVLOC I.5 and I.8b: Littlewood bounds on L(1, χ) and cyclotomic units.
- **The two proofs:**
  - Alpöge's: Stepanov determinants, theta lifts and positivity; Lean-formalized;
  - Masullo's: adelic θ-functions, idelic zeta functions and a trace formula; unrefereed.
  The user's view: if both hold, they attack the programme from two directions at once.

## The task

1. **Q01 and Q02.** State and prove the class of schemes over Z, and the class of motives over Q, for which RH follows:
   - from Alpöge's theorems alone (F1, F2);
   - conditionally on Masullo's claim (every Artin-Tate point count; Artin motives and their twists).
   State exactly the gate for the rest: motives of positive weight, starting with elliptic curves and modular forms.
2. **Our conditional statements.** Take each statement listed above, and each row of the attached intakes and
   `BRIDGE_FLAGS.tsv` that assumes GRH or the absence of a Siegel zero. Decide each as unconditional by Alpöge,
   conditional on Masullo only, or beyond both. Give the effective constants that become theorems: class numbers,
   heights and least non-residues.
3. **The two routes.** Compare the methods at the level of statements: which intermediate statements each proves
   (Alpöge's by step and Lean file, Masullo's by statement number). Say which of them are new theorems our programme can
   use independently of RH: positivity of periods, divisibility of theta derivatives, trace formulas.
4. **Special values.** Separate what RH and GRH say (zeros) from what the special-value statements of our runs use
   (K-groups, regulators, Bernoulli numbers), with Deligne-Goncharov where it bears.

## The attached files

- `BRIDGES_QUESTIONS.tsv`, `BRIDGES_LEDGER.md`, `BRIDGES_IMPLICATIONS.md`, `BRIDGES_20261120.tex`; `BRIDGE_FLAGS.tsv`.
- `INTAKE_RESEARCH_SA06_20261120.md`, `INTAKE_RESEARCH_SA07_20261120.md`, `INTAKE_RESEARCH_SA20_20261120.md`,
  `INTAKE_REVLOC_20261120.md`.
- `MASULLO_the-music-of-the-primes.pdf` and `MASULLO_STATEMENTS_INDEX.md`.
- `ALPOGE_remark.pdf`, `ALPOGE_Main.lean`, `ALPOGE_Statements.lean`, `ALPOGE_LEAN_SCAN.tsv`, `ALPOGE_LEAN_MAP_20261120.md`.
- `LIT_Deligne_Goncharov_mixed_Tate_motives/`: LaTeX source.

{hw("the exact classes of schemes over Z and of motives over Q for which RH follows from Alpöge's theorems and, conditionally, from Masullo's claim, and the gate for the rest.", "ZETA_TWO")}""",
    AL4 + ["INTAKE_RESEARCH_SA06_20261120.md", "INTAKE_RESEARCH_SA07_20261120.md", "INTAKE_RESEARCH_SA20_20261120.md",
           "INTAKE_REVLOC_20261120.md", "LIT_Deligne_Goncharov_mixed_Tate_motives"],
    {**MASF, **BRQ, **FLAGS, **LMAP, "BRIDGES_IMPLICATIONS.md": AR / "bridges/IMPLICATIONS.md",
     "BRIDGES_20261120.tex": AR / "bridges/BRIDGES_20261120.tex"})


def put(src, dst):
    dst.parent.mkdir(parents=True, exist_ok=True)
    if src.is_dir():
        shutil.copytree(src, dst, dirs_exist_ok=True)
    else:
        shutil.copy2(src, dst)


built = []
for name, (short, text, from22, extra) in P.items():
    out = Q / name
    if out.exists():
        print("EXISTS, skipped:", out); continue
    out.mkdir(parents=True)
    (out / "PROMPT.md").write_text(text, encoding="utf-8")
    for n in from22:
        src = F22 / n
        if not src.exists():
            print("MISSING (from 22)", n); continue
        put(src, out / n)
    for n, src in extra.items():
        if not src.exists():
            print("MISSING", src); continue
        put(src, out / n)
    for sub in sorted(p for p in out.iterdir() if p.is_dir()):
        with zipfile.ZipFile(out / (sub.name + ".zip"), "w", zipfile.ZIP_DEFLATED) as z:
            for f in sorted(sub.rglob("*")):
                if f.is_file():
                    z.write(f, f.relative_to(sub).as_posix())
        shutil.rmtree(sub)
    built.append(out)
    print("built", name, sum(1 for _ in out.iterdir()), "files")

PY = sys.executable
for out in built:
    r = subprocess.run([PY, "-I", "-B", str(D / "claude_tools/prompts/pack_one_zip.py"), str(out)], capture_output=True, text=True,
                       encoding="utf-8", errors="replace")
    print("pack", out.name, (r.stdout.strip().splitlines() or ["?"])[-1], r.stderr.strip()[-300:])
for out in built:
    pm = out / "PROMPT.md"
    a = subprocess.run([PY, "-I", "-B", str(D / "claude_tools/push_rule_pro_prompts.py"), "--lint-math", str(pm)], capture_output=True,
                       text=True, encoding="utf-8", errors="replace")
    b = subprocess.run([PY, "-I", "-B", str(D / "claude_tools/paper_completeness_lint.py"), str(pm)], capture_output=True, text=True,
                       encoding="utf-8", errors="replace")
    print(f"lint {out.name}: math -> {(a.stdout.strip().splitlines() or ['?'])[-1]} | paper -> {(b.stdout.strip().splitlines() or ['?'])[-1]}")
    if "failing lint: 0" not in a.stdout or "failing: 0" not in b.stdout:
        print(a.stdout[-1500:], b.stdout[-1500:])
    zs = list(out.glob("*.zip"))
    print("   ", ", ".join(f"{z.name} {z.stat().st_size / 1e6:.1f} MB" for z in zs))
