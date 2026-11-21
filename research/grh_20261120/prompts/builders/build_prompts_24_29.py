"""Build Pro research prompts 24-29 (20 Nov 2026, main session, Claude Opus 5.5 at effort max), at the user's word:
"You need to make a few research prompts for Pro. Spread them out. Don't make it a huge 10-hour one. Like, parallelize
it." Prompt 23 (one large prompt) is split into 24-28 by topic; 29 is the DELTA_ON_GT successor (Fable's suggestion 1).
Each send folder gets PROMPT.md plus its attachments; pack_one_zip.py then makes PROMPT.md + one flat ZIP.
usage: python -I -B build_prompts_24_29.py"""
import pathlib, shutil, sys
sys.stdout.reconfigure(encoding="utf-8")
D = pathlib.Path(r"C:\Users\user\Documents")
Q = D / "TO_SEND/PRO/1_Archive_research_by_topic"
S = D / "TO_SEND/PRO/_staging_20261120"
F23, DL = S / "from_23", S / "dl"
DELTA = D / "longue_marche_pro_pilot_20261104/answers/DELTA_ON_GT_checkpoint_05_20261116T0650Z_unzipped/DELTA_ON_GT"
LM7 = D / "longue_marche_pro_pilot_20261104/answers/LM7_PUSH_checkpoint_09_20261113T2242Z_unzipped/LM7_PUSH"
AR = D / "reports_20261120/alpoge_rh"
MAS = D / "Papors/Chatnotes/Zeta-Function-Foundation/literature/masullo_grh_20261120/Masullo_the-music-of-the-primes.pdf"

ALPOGE = """## The results cited

**Alpöge.** On 20 November 2026 Levent Alpöge (a number theorist: Bhargava's student; Harvard Society of Fellows)
posted a four-page note and a complete Lean formalization of a proof of the Riemann hypothesis and of GRH for Dirichlet
L-functions, found with Claude. `ALPOGE_Main.lean` proves Mathlib's `RiemannHypothesis` and the Dirichlet statements
(defined in `ALPOGE_Statements.lean`); a text scan of all 175,187 source files (`ALPOGE_LEAN_SCAN.tsv`) finds no sorry,
axiom or native_decide. It has not been refereed, and that is not our concern here: its theorems are cited as theorems,
L. Alpöge, *Remark*, https://alpo.ge/remark.pdf (attached as `ALPOGE_remark.pdf`), with its Lean archive. The steps of
the note used below (numbered as in its pages 1-4): step 2, p-adic divisibility of derivatives of CM theta values at
inert primes; steps 3 and 5, the count qN = M^k + R on the path quadric and the "sign-only proof of Weil and Deligne"
(a definite sign from middle cohomology, square-root cancellation by iterated Parseval, opposite signs forbidding
cancellation of inverse roots); steps 4 and 7, positivity by determinants and Gan-Gross-Prasad periods (values 0 or 1
for interlacing weights); step 8, iterated theta lifts between totally definite unitary groups, each winning one order
of multiplicity; step 13, the Bost slope inequality; step 17, the groups H^1(o_E[1/l], Q_l/Z_l(-e)) and a weakening of
Vandiver's conjecture.
"""
MASULLO = """**Masullo.** A. M. Masullo, *The Music of the Primes* (940 pages, a draft posted 20 November 2026 and announced by
R. Vakil), proposes a proof of GRH for the Hecke L-functions of every number field (its §1.2), by adelic θ-functions,
idelic zeta functions and a trace formula on "orbital Schauder bases". It is neither refereed nor formalized: cite its
statements as the draft's claims, by chapter and statement number (`MASULLO_STATEMENTS_INDEX.md` lists all 336 numbered
statements with their PDF pages), and mark every finding that depends on it as conditional on it.
"""


LANG_PARAGRAPH = """## The language of the results

Whatever the outcome for P versus NP, the mathematics of this prompt has to transfer to our programme on Grothendieck's
work. So every finding is also stated, with its proof or the exact dictionary that carries the proof across, in the
language of algebraic geometry and of Grothendieck's own frameworks: schemes and group schemes over Z (SGA 3), λ-rings,
K_0 and the γ-filtration (SGA 6), representation rings as K_0 of categories of representations, Schur functors as
operations on locally free sheaves, orbit closures as schemes over Z with their Hilbert and Quot schemes (FGA), ℓ-adic
sheaves, weights and purity (SGA 4, SGA 5, Weil II), motives where they apply. For each finding, say where it lives in
Grothendieck's texts: the archive by cote and scan, the SGA, EGA or FGA by exact locator. A finding proved in
combinatorial, representation-theoretic or complexity language is stated again in this language in the paper, in a
part of its own, with the dictionary.

"""


def how_to_work(main_q, short):
    lang = LANG_PARAGRAPH if short != "DELTA23" else ""
    return lang + f"""## How to work

The rule that governs everything below: push. Work on the main question first: {main_q} Give it most of the time.
When one approach stalls, take the next one. Deliver nothing while an item is undecided and an untried approach
remains. A gap in a proof is an undecided step: attack it, never paper over it.

**Progress check at three hours**. After about three hours of work, and every hour after that, review the work against
a dated ledger (`LEDGER.md`): every open row with its status, and for each main question its current gate (the strongest
proved reduction). Movement means only an open row changing status, or a main question proved to reduce to a strictly
smaller gate. Restating the same gate, side results that leave every gate as it was, and packaging are not movement.
After two consecutive reviews without movement, stop that work, write the final package with every item's state, and
deliver it; this check takes precedence over the rule about untried approaches.

For every statement, record its check events in `CHECK_EVENTS.tsv`: statement id, date, who (model, effort, run), type
(targeted proof check / independent re-proof / computation or formal certificate / used and rechecked in this run /
carried as background without fault found / refuted, with the refined statement's id), outcome. Give each event the type
of what actually happened, neither more nor less. Cited statements you use get their events too.

Every proof is checked before the package is final, by a reading of the whole proof, and the check is recorded with
who, how, model, effort and date. A proof that fails its check is reported with its gap.

**Checkpoints.** Save a checkpoint ZIP to the user's Library, or wherever files survive the loss of the execution
environment, once every 45 minutes of work, each under a new name, `{short}_checkpoint_<NN>.zip` with `NN` counting up.
Never overwrite, rename or delete an earlier checkpoint, and put no earlier checkpoint ZIP inside a checkpoint. Save
checkpoints once every 45 minutes and at no other time. A checkpoint is one ZIP holding every deliverable written so far
and everything that documents the work, so that a new session can continue from it and the attached files. It is never
a JSON file, a recovery file, a summary, or an export of the newest part only. Each checkpoint zip holds the current
deliverables and documentation; earlier checkpoints are not copied into it.

**If the execution environment fails**, that does not end the task. Retry at intervals for as long as this session
lasts. When it is back, restore your work from the newest checkpoint, redo what you had done after that checkpoint, and
continue to the end. Do not write files out in this chat instead: the work reaches us only through checkpoint ZIPs and
the final ZIP.

## What to deliver

One final ZIP, `{short}_final.zip`, holding:
1. **The paper**, `{short}.tex`, in LaTeX:
   - every finding with its proof (a finding is a new result of this work), each under its id;
   - checked and unchecked findings in separate parts;
   - every cited result with an exact locator (Alpöge's by step and Lean file; Masullo's by statement number; the
     literature by work and statement number; Grothendieck's archive by cote and scan; our runs by run and statement id).
2. **`QUESTIONS.tsv`**, one row for each question treated: id, the source and locator, the question, its state (proved,
   with the finding ids; refuted, with the counterexample; or, if the session ends, its current gate).
3. **`LEDGER.md`** and **`CHECK_EVENTS.tsv`**.
4. **`IMPLICATIONS.md`**: what the findings change, for P versus NP through geometric complexity theory and for
   Grothendieck's texts (cote and scan).

A known result is cited with an exact locator and is not proved again, except for a short proof of a form its source
does not state. Every new result is proved in full. An item is finished only when it is proved or refuted. A return may
be marked INCOMPLETE only when the session itself ends. It then gives the state reached, every approach tried with where
it failed, and the next step.
"""


SIX = ("This prompt is one of six run in parallel on 20 November 2026. The others treat: Mulmuley's nonstandard Riemann "
       "hypothesis (24), plethysm through Grothendieck's λ-rings (25), Kronecker coefficients through his λ-operations on "
       "G-sets (26), Grothendieck's inequality and tensor norms (27), GRH and the ETH result in complexity (28), and the "
       "invariant Δ on the Grothendieck-Teichmüller group (29). Keep to this prompt's questions; the others are asked "
       "there.\n")

P = {}

P["24_GCT_NONSTANDARD_RH_and_purity_by_positivity"] = ("GCT_NSRH", f"""# GCT_NSRH: Mulmuley's nonstandard Riemann hypothesis, against purity by positivity

{SIX}
{ALPOGE}
## The question, and why it is the one

Geometric complexity theory (Mulmuley-Sohoni) aims at P ≠ NP through representation-theoretic obstructions on orbit
closures. Its "flip" (GCT VI, attached) rests on positivity hypotheses for the Kronecker and plethysm coefficients. GCT IV
(Blasiak-Mulmuley-Sohoni) and GCT VII define nonstandard quantum groups for the Kronecker and the plethysm problems; GCT
VIII studies canonical bases for them and conjectures their positivity. Mulmuley expects that positivity to follow from
a suitable nonstandard extension of the Riemann hypothesis over finite fields, as Kazhdan-Lusztig positivity follows from
Deligne's Weil II through the purity of intersection cohomology. Alpöge's step 5 proves purity, for the sums it treats,
by a definite sign alone: a "sign-only proof of Weil and Deligne". A sign-only proof may not need the geometry that the
nonstandard quantum groups lack. That is the question.

## The task

1. **The statement needed.** Locate where GCT IV, VI, VII and VIII state, or point to, the nonstandard Riemann hypothesis
   and the deduction from it to positivity. State both exactly: the objects, the weights, what purity would say, and
   every step of the deduction, with each gap named.
2. **The template.** Write the dictionary from Kazhdan-Lusztig positivity (Schubert varieties, intersection cohomology,
   Weil II, the decomposition theorem) to the nonstandard quantum groups: for each geometric ingredient, what replaces
   it, and where nothing does.
3. **The sign-only mechanism.** Formulate Alpöge's step 5 abstractly (exponential sums in a family; a definite sign in
   the middle degree; square-root cancellation; no cancellation of inverse roots), with the hypotheses it really uses.
   Decide whether it applies to the objects of item 2, and prove what it gives: the nonstandard Riemann hypothesis, or a
   precisely stated part of it, or a refutation of the route.
4. **Positivity reached.** From what item 3 proves, derive the positivity statements for canonical bases and for the
   Kronecker and plethysm coefficients in the cases geometric complexity theory needs (the rectangular cases of
   Ikenmeyer-Panova; the multiplicity obstructions left by Bürgisser-Ikenmeyer-Panova's theorem that occurrence
   obstructions do not suffice).
5. **The theta-lift positivity** of steps 4, 7 and 8 (determinants, interlacing periods, multiplicity won lift by lift):
   decide what it gives for the same positivity statements.

## The attached files

- `LIT_Mulmuley_GCT_IV_nonstandard_quantum_group_Kronecker/` (arXiv cs/0703110), `LIT_Mulmuley_GCT_VII_nonstandard_quantum_group_plethysm/`
  (arXiv 0709.0749), `LIT_Mulmuley_GCT_VIII_canonical_bases_nonstandard_quantum_groups/` (arXiv 0709.0751),
  `LIT_Mulmuley_GCT_VI_flip_via_positivity/`, `LIT_Landsberg_GCT_introduction_for_geometers/`,
  `LIT_Burgisser_Ikenmeyer_Panova_no_occurrence_obstructions/`, `LIT_Ikenmeyer_Panova_rectangular_Kronecker_plethysm/`:
  LaTeX sources.
- `ALPOGE_remark.pdf`, `ALPOGE_Main.lean`, `ALPOGE_Statements.lean`, `ALPOGE_LEAN_SCAN.tsv`.
- `FABLE_PROGRAM_SUGGESTIONS_20261120.md` and its expansion `..._EXPLAINED.md`: suggestions from our Claude Fable 5.2 (effort
  max) agent on Alpöge's method; suggestions 3, 4 and 8 bear here. Unchecked: use them as leads, never as results.

{how_to_work("whether the sign-only mechanism of Alpöge's step 5 proves Mulmuley's nonstandard Riemann hypothesis, or which exactly stated part of it.", "GCT_NSRH")}""",
    ["LIT_Mulmuley_GCT_VI_flip_via_positivity", "LIT_Landsberg_GCT_introduction_for_geometers",
     "LIT_Burgisser_Ikenmeyer_Panova_no_occurrence_obstructions", "LIT_Ikenmeyer_Panova_rectangular_Kronecker_plethysm",
     "ALPOGE_remark.pdf", "ALPOGE_Main.lean", "ALPOGE_Statements.lean", "ALPOGE_LEAN_SCAN.tsv"],
    {"LIT_Mulmuley_GCT_IV_nonstandard_quantum_group_Kronecker": DL / "cs_0703110/src",
     "LIT_Mulmuley_GCT_VII_nonstandard_quantum_group_plethysm": DL / "0709.0749/src",
     "LIT_Mulmuley_GCT_VIII_canonical_bases_nonstandard_quantum_groups": DL / "0709.0751/src",
     "FABLE_PROGRAM_SUGGESTIONS_20261120.md": AR / "bridges/FABLE_PROGRAM_SUGGESTIONS_20261120.md",
     "FABLE_PROGRAM_SUGGESTIONS_20261120_EXPLAINED.md": AR / "bridges/FABLE_PROGRAM_SUGGESTIONS_20261120_EXPLAINED.md"})

ARCH = ["ARCHIVE_133_scan006.tex", "ARCHIVE_133_scan008.tex", "ARCHIVE_133_scan009.tex", "ARCHIVE_133_scan019.tex",
        "ARCHIVE_133_scan028.tex", "ARCHIVE_16_scan038.tex", "ARCHIVE_4_scan007.tex", "ARCHIVE_2_scan017.tex",
        "ARCHIVE_12_scan041.tex", "ARCHIVE_43_scan037.tex", "ARCHIVE_79_scan051.tex", "ARCHIVE_89_scan018.tex",
        "ARCHIVE_119_scan217.tex", "SA17_STUDY_cote133_lambda.md"]

P["25_GCT_PLETHYSM_through_Grothendiecks_lambda_rings"] = ("GCT_PLETH", f"""# GCT_PLETH: plethysm coefficients through Grothendieck's λ-rings and the theta correspondence

{SIX}
{ALPOGE}
## The question

Plethysm is composition in Λ, the free λ-ring on one generator: the composition of Schur functors. Its coefficients are
the multiplicities geometric complexity theory needs in the coordinate rings of orbits and orbit closures: Foulkes-Howe
(Sym^m Sym^n against Sym^n Sym^m), the Hadamard-Howe map, the Chow variety and the orbit closure of x_1⋯x_n.
Grothendieck created λ-rings (1957, for Riemann-Roch; SGA 6), and his pages attached (cote 133 and others, transcribed,
with the study of cote 133 from our sweep) work with plethysm and λ-operations. Alpöge's proof wins multiplicity by
chains of theta lifts and counts interlacing (Gan-Gross-Prasad periods, values 0 or 1); a chain of compact dual pairs
counts Gelfand-Tsetlin patterns. The question: do these give positive formulas, or the nonvanishing geometric
complexity theory needs, for the plethysm coefficients?

## The task

1. **His pages as mathematics.** Read every attached archive page; state each λ-ring or plethystic statement on it,
   with cote and scan, and prove or refute it. Say what each gives for plethysm coefficients.
2. **Plethysm in a theta correspondence.** Express plethysm coefficients, or the Foulkes-Howe and Hadamard-Howe
   multiplicities, as multiplicities in a theta correspondence or a branching along a chain of compact dual pairs (Howe
   duality), and derive positive formulas (counts of lattice points in polytopes) wherever this works. Where it does not,
   prove what blocks it.
3. **Foulkes-Howe and Hadamard-Howe.** Decide what the formulas of item 2 give for injectivity or surjectivity of the
   Hadamard-Howe map in the ranges open today, with exact statements.
4. **The rectangular cases** of Ikenmeyer-Panova: positivity and nonvanishing statements that follow, proved.

## The attached files

- `LIT_Ikenmeyer_Panova_rectangular_Kronecker_plethysm/`, `LIT_Burgisser_Ikenmeyer_Panova_no_occurrence_obstructions/`,
  `LIT_Borger_lambda_rings_field_with_one_element/`, `LIT_Landsberg_GCT_introduction_for_geometers/`,
  `LIT_Mulmuley_GCT_VII_nonstandard_quantum_group_plethysm/`: LaTeX sources.
- `ARCHIVE_<cote>_scan<NNN>.tex`: Grothendieck's pages (our transcription of the scans), and `SA17_STUDY_cote133_lambda.md`.
- `ALPOGE_remark.pdf`; `FABLE_PROGRAM_SUGGESTIONS_20261120.md` and `..._EXPLAINED.md` (suggestion 8 bears here; leads only).

{how_to_work("positive formulas, or the nonvanishing geometric complexity theory needs, for the plethysm coefficients, through Grothendieck's λ-ring pages and the theta correspondence.", "GCT_PLETH")}""",
    ["LIT_Ikenmeyer_Panova_rectangular_Kronecker_plethysm", "LIT_Burgisser_Ikenmeyer_Panova_no_occurrence_obstructions",
     "LIT_Borger_lambda_rings_field_with_one_element", "LIT_Landsberg_GCT_introduction_for_geometers", "ALPOGE_remark.pdf"] + ARCH,
    {"LIT_Mulmuley_GCT_VII_nonstandard_quantum_group_plethysm": DL / "0709.0749/src",
     "FABLE_PROGRAM_SUGGESTIONS_20261120.md": AR / "bridges/FABLE_PROGRAM_SUGGESTIONS_20261120.md",
     "FABLE_PROGRAM_SUGGESTIONS_20261120_EXPLAINED.md": AR / "bridges/FABLE_PROGRAM_SUGGESTIONS_20261120_EXPLAINED.md"})

P["26_GCT_KRONECKER_through_lambda_operations_on_G-sets"] = ("GCT_KRON", f"""# GCT_KRON: Kronecker coefficients through Grothendieck's λ-operations on G-sets

{SIX}
{ALPOGE}
## The question

The Kronecker coefficients are the multiplicities of the inner tensor product of representations of the symmetric
groups. Grothendieck worked with λ-structures on Burnside rings and representation rings (cote 133, attached with the
study of it from our sweep). On the other side stand saturation and positivity: Littlewood-Richardson saturation
(Knutson-Tao), the model of the flip (GCT VI); its failure for Kronecker coefficients in general; the K-theoretic
positivity of Grothendieck polynomials (Lascoux-Schützenberger; Brion's alternating positivity); and GCT IV's
nonstandard quantum group for the Kronecker problem. The question: what do Grothendieck's λ-operations on G-sets give
for the positivity and saturation of Kronecker coefficients in the cases geometric complexity theory needs?

## The task

1. **His pages as mathematics.** State every statement on λ-operations, Burnside rings and representation rings in
   the attached pages, with cote and scan; prove or refute each.
2. **Kronecker coefficients from Burnside λ-structures.** Derive positive formulas, or nonvanishing criteria, for
   Kronecker coefficients in families (two-row and hook shapes, rectangles, the shapes of Ikenmeyer-Panova), and prove
   them.
3. **Saturation.** State exactly where saturation fails for Kronecker coefficients, and decide whether K-theoretic
   positivity (Grothendieck polynomials) or the λ-structures of item 2 give a saturation-type statement in the range
   geometric complexity theory needs.
4. **Obstructions.** Decide what items 2 and 3 give for multiplicity obstructions (Bürgisser-Ikenmeyer-Panova).

## The attached files

- `LIT_Mulmuley_GCT_IV_nonstandard_quantum_group_Kronecker/`, `LIT_Mulmuley_GCT_VI_flip_via_positivity/`,
  `LIT_Ikenmeyer_Panova_rectangular_Kronecker_plethysm/`, `LIT_Burgisser_Ikenmeyer_Panova_no_occurrence_obstructions/`,
  `LIT_Borger_lambda_rings_field_with_one_element/`: LaTeX sources.
- `ARCHIVE_133_scan<NNN>.tex` and the other archive pages, and `SA17_STUDY_cote133_lambda.md`; `ALPOGE_remark.pdf`.

{how_to_work("what Grothendieck's λ-operations on G-sets give for the positivity and saturation of Kronecker coefficients where geometric complexity theory needs them.", "GCT_KRON")}""",
    ["LIT_Mulmuley_GCT_VI_flip_via_positivity", "LIT_Ikenmeyer_Panova_rectangular_Kronecker_plethysm",
     "LIT_Burgisser_Ikenmeyer_Panova_no_occurrence_obstructions", "LIT_Borger_lambda_rings_field_with_one_element",
     "ALPOGE_remark.pdf"] + ARCH,
    {"LIT_Mulmuley_GCT_IV_nonstandard_quantum_group_Kronecker": DL / "cs_0703110/src"})

P["27_GCT_GROTHENDIECK_INEQUALITY_and_tensor_norms"] = ("GCT_GINEQ", f"""# GCT_GINEQ: Grothendieck's inequality and the projective tensor norm, against tensor rank

{SIX}
## The question

Grothendieck's *Résumé de la théorie métrique des produits tensoriels topologiques* (1953) contains his inequality and
the projective and injective tensor norms. In complexity they meet: semidefinite approximation (Alon-Naor's cut norm);
the Grothendieck constant as the approximation threshold under the Unique Games Conjecture (Raghavendra-Steurer);
quantum XOR games (Tsirelson); the projective tensor norm as the nuclear norm, NP-hard to compute for tensors of order
three (Friedland-Lim); and, in geometric complexity theory, tensor rank and border rank (matrix multiplication; the
permanent against the determinant). The question: what do Grothendieck's inequality and his tensor norms give for rank
and border-rank lower bounds on the tensors geometric complexity theory studies?

## The task

1. **Norms against rank.** Prove lower bounds for rank and border rank of the matrix multiplication
   tensor and of the determinant and permanent tensors, from nuclear and injective norms and their duality; state how
   they compare with the flattening and Koszul-flattening bounds and the barriers known for them.
2. **Grothendieck's inequality as a certificate.** Decide whether semidefinite relaxations with Grothendieck's
   inequality give certifiable lower bounds of these kinds, and prove what they give.
3. **The constant.** State what is known of the Grothendieck constant against the Unique Games threshold, and what
   items 1-2 add.

## The attached files

- `LIT_Pisier_Grothendiecks_theorem_past_and_present/` (arXiv 1101.4195), `LIT_Friedland_Lim_nuclear_norm_of_tensors/`
  (arXiv 1410.6072), `LIT_Landsberg_GCT_introduction_for_geometers/`,
  `LIT_Burgisser_Ikenmeyer_Panova_no_occurrence_obstructions/`: LaTeX sources.

{how_to_work("rank and border-rank lower bounds for the tensors of geometric complexity theory from Grothendieck's inequality and his tensor norms.", "GCT_GINEQ")}""",
    ["LIT_Landsberg_GCT_introduction_for_geometers", "LIT_Burgisser_Ikenmeyer_Panova_no_occurrence_obstructions"],
    {"LIT_Pisier_Grothendiecks_theorem_past_and_present": DL / "1101.4195/src",
     "LIT_Friedland_Lim_nuclear_norm_of_tensors": DL / "1410.6072/src"})

P["28_GRH_and_ETH_in_complexity_Koiran_GCT_V"] = ("CX_GRH", f"""# CX_GRH: what the GRH results and the ETH result make unconditional in complexity

{SIX}
{ALPOGE}
{MASULLO}
**ETH.** OpenAI, *The Exponential Time Hypothesis is False* (OpenAI Math Release preprint, 25 October 2026; LaTeX
source in `LIT_OpenAI_ETH_is_False/`, with its citation in that folder's README): a deterministic algorithm counts the
solutions of a k-CNF formula with n variables and m clauses in time (n+m)^(O_k(1)) 2^(n/(log n)^(1/2+o(1))), in
polynomial space, formalized in Lean. It is cited as a theorem.

## The task

1. **Which GRH, exactly.** For each of the following, find the exact hypothesis it uses (GRH for Dirichlet
   L-functions, for Dedekind zeta functions of which fields, for Hecke or Artin L-functions), and state what is now
   unconditional through Alpöge and what through Masullo's draft (conditional on it):
   - Koiran (1996): Hilbert's Nullstellensatz is in AM, hence in the second level of the polynomial hierarchy;
   - GCT V (attached): an h.s.o.p. for a variety given by its equations in PH, and Noether normalization for explicit
     varieties in EXPH (through Koiran);
   - Miller's primality test with Bach's bound (our run found Dirichlet GRH enough);
   - the deterministic algorithms for factoring polynomials over finite fields and for finding primitive roots and
     non-residues, and the class-group algorithms, that assume GRH.
   For each, prove the unconditional statement in full, citing the conditional proof by locator.
2. **ETH false: what follows.** Work out exactly what the result changes for: the ETH- and SETH-based lower bounds of
   fine-grained and parameterized complexity; circuit lower bounds through faster satisfiability algorithms (the
   algorithmic method); Valiant's classes VP and VNP and the permanent; and geometric complexity theory.

## The attached files

- `LIT_Mulmuley_GCT_V_Noether_normalization/`, `LIT_OpenAI_ETH_is_False/`: LaTeX sources.
- `MASULLO_the-music-of-the-primes.pdf` (no source posted) and `MASULLO_STATEMENTS_INDEX.md`.
- `ALPOGE_remark.pdf`, `ALPOGE_Main.lean`, `ALPOGE_Statements.lean`; `BRIDGES_QUESTIONS.tsv` and `BRIDGES_LEDGER.md`
  (our run of 20 Nov: Q07 Koiran, Q08 Miller-Bach).

{how_to_work("the exact GRH each complexity result uses, and the unconditional statements that follow from Alpöge and, conditionally, from Masullo.", "CX_GRH")}""",
    ["LIT_Mulmuley_GCT_V_Noether_normalization", "LIT_OpenAI_ETH_is_False", "ALPOGE_remark.pdf", "ALPOGE_Main.lean",
     "ALPOGE_Statements.lean"],
    {"MASULLO_the-music-of-the-primes.pdf": MAS,
     "MASULLO_STATEMENTS_INDEX.md": D / "reports_20261120/masullo_statements/STATEMENTS_INDEX.md",
     "BRIDGES_QUESTIONS.tsv": AR / "bridges/QUESTIONS.tsv", "BRIDGES_LEDGER.md": AR / "bridges/LEDGER.md"})

P["29_DELTA_2-3_reciprocity_of_frames_on_GT"] = ("DELTA23", f"""# DELTA23: the invariant Δ on the Grothendieck-Teichmüller group as a 2-3 reciprocity of frames

{SIX}
{ALPOGE}
## Where our runs stand

- **LM7_PUSH** (GPT-6 Astra, Pro mode; results and sections attached). The objects are these:
  - the modular group B = C_2 ∐ C_3 = ⟨s, r | s^2 = r^3 = 1⟩, with s at the harmonic point j = 1728 (CM by Z[i]) and r
    at the equianharmonic point j = 0 (CM by Z[ω]);
  - GT̂_0, the "gentle group": the part of GT̂ cut out by the relations at these two points, without the pentagon;
  - the frames of F ∈ GT̂_0: the conjugators β_F, A_F with F(s) = β_F s β_F^{-1} and F(r) = A_F r A_F^{-1}.

  E.65 proves that the CM parity is a continuous character of the full gentle group. E.58 constructs, by relative
  pronilpotent lifting, an element in the extra CM coset. E.3 (open) asks whether the full GT̂ reaches that coset.
- **DELTA_ON_GT** (GPT-6 Astra, Pro mode, checkpoint 05; attached). Its proved and open rows are these:
  - A.6 (proved): the frame sign u ∈ {{1, 5, 7, 11}} ⊂ (Z/12)^× is the CRT encoding of two parities, u ≡ (−1)^(a_3)
    mod 3 and u ≡ (−1)^(a_2) mod 4, with Δ = a_2 + a_3 mod 2.
  - A.5 (proved): the plain product formula, Weil reciprocity for the Kummer class of 1 − 1728/j with residues (1, 1, 0)
    at (0, 1728, ∞), does not by itself compare the two CM frames. Identifying (−1)^Δ with an independently defined
    local datum is an additional comparison.
  - Open: A.84 (the main quadratic decision on the full profinite pentagon group), A.24 (the missing passage from these
    fields to order-five frame characters), A.86 (the level-six Atkin-Lehner comparison) and B.40 (all relative
    quadratic characters of the gentle group).
- **Our Fable agent** (Claude Fable 5.2 at effort max; suggestion 1 of the attached file, unchecked) proposes the
  missing comparison:
  - Δ = χ_12(u), with χ_12 = χ_{{−4}} χ_{{−3}} the character of Q(√3), the real subfield of Q(i, ω);
  - a_2 and a_3 as local symbols at 2 and at 3 (Hilbert or Kubota) of the pair of frames;
  - Δ = 0 on Galois as a reciprocity law, and A.84 as the question whether the pentagon forces that product formula.
    Elements with unequal bits pass each local test and fail the product formula.

  It also points to:
  - the metaplectic reciprocity in Alpöge's steps 3 and 5: Gauss sums of order #μ_K on the #μ_K-fold cover, and "the
    reciprocity law of y(c·c′) against y(c)·y(c′)";
  - the quaternion algebra (−1, −3), ramified at 3 and ∞, the endomorphism algebra of the supersingular curve in
    characteristic 3, where j = 0 and j = 1728 coincide;
  - the quotients Ẑ[ω] ⋊ C_6 and Ẑ[i] ⋊ C_4 of the tripod group, the (2,3,6) and (2,4,4) triangle groups.

## The task

1. **The comparison.** Prove or refute: a_2 and a_3 are local symbols at 2 and at 3 of the pair of frames, for a
   definition you state, so that (−1)^Δ is their product. Evaluate on the element of E.58.
2. **The main question, A.84.** Decide whether the hexagon and pentagon relations force a_2 = a_3 on GT̂, that is,
   whether Δ = 0 on the full profinite Grothendieck-Teichmüller group (E.3 of LM7_PUSH).
3. **Order five, A.24.** The pentagon lives on M_{{0,5}}: give the passage from the fields of item 1 to order-five frame
   characters, and decide what it says about Δ.
4. **Level six, A.86.** Make the level-six Atkin-Lehner comparison well defined and decide it; relate it to the
   quaternion algebra of discriminant 6 (the Hilbert symbol (2, 3) is −1 exactly at 2 and 3) if it bears.
5. **B.40.** Determine all relative quadratic characters of the gentle group.

## The attached files

- `DELTA_ON_GT/`: the checkpoint-05 return:
  - the report and the results CSV;
  - `sections/*.tex`, which hold every statement with its proof;
  - `agent_five/five_point_results.tex`;
  - `agent_lifting/`.
- `LM7_PUSH/`: the results CSV and the sections of E.1-E.65 (`E_agent.tex`, `E_relative_cm_lift_agent.tex`,
  `E_cm_character_agent.tex`).
- `ALPOGE_remark.pdf`.
- `FABLE_PROGRAM_SUGGESTIONS_20261120.md` and `..._EXPLAINED.md` (suggestion 1). These are leads, not results.

{how_to_work("whether Δ = 0 on the full profinite Grothendieck-Teichmüller group (A.84), through the 2-3 comparison of frames.", "DELTA23")}""",
    ["ALPOGE_remark.pdf"],
    {"DELTA_ON_GT/DELTA_ON_GT_report.md": DELTA / "DELTA_ON_GT_report.md",
     "DELTA_ON_GT/DELTA_ON_GT_results.csv": DELTA / "DELTA_ON_GT_results.csv",
     "DELTA_ON_GT/sections": DELTA / "sections",
     "DELTA_ON_GT/agent_five/five_point_results.tex": DELTA / "agent_five/five_point_results.tex",
     "DELTA_ON_GT/agent_lifting": DELTA / "agent_lifting",
     "LM7_PUSH/LM7_PUSH_results.csv": LM7 / "LM7_PUSH_results.csv",
     "LM7_PUSH/E_agent.tex": LM7 / "sections/E_agent.tex",
     "LM7_PUSH/E_relative_cm_lift_agent.tex": LM7 / "sections/E_relative_cm_lift_agent.tex",
     "LM7_PUSH/E_cm_character_agent.tex": LM7 / "sections/E_cm_character_agent.tex",
     "FABLE_PROGRAM_SUGGESTIONS_20261120.md": AR / "bridges/FABLE_PROGRAM_SUGGESTIONS_20261120.md",
     "FABLE_PROGRAM_SUGGESTIONS_20261120_EXPLAINED.md": AR / "bridges/FABLE_PROGRAM_SUGGESTIONS_20261120_EXPLAINED.md"})


def put(src, dst):
    dst.parent.mkdir(parents=True, exist_ok=True)
    if src.is_dir():
        shutil.copytree(src, dst, dirs_exist_ok=True)
    else:
        shutil.copy2(src, dst)


for name, (short, text, from23, extra) in P.items():
    out = Q / name
    if out.exists():
        print("EXISTS, skipped:", out); continue
    out.mkdir(parents=True)
    (out / "PROMPT.md").write_text(text, encoding="utf-8")
    for n in from23:
        put(F23 / n, out / n)
    for n, src in extra.items():
        if not src.exists():
            print("MISSING", src); continue
        put(src, out / n)
    # pack_one_zip.py takes files and ZIPs only (each ZIP becomes a folder of its name inside the one ZIP), so every
    # attached folder goes in as <folder>.zip
    import zipfile
    for sub in sorted(p for p in out.iterdir() if p.is_dir()):
        with zipfile.ZipFile(out / (sub.name + ".zip"), "w", zipfile.ZIP_DEFLATED) as z:
            for f in sorted(sub.rglob("*")):
                if f.is_file():
                    z.write(f, f.relative_to(sub).as_posix())
        shutil.rmtree(sub)
    print("built", name)
