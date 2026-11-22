**The attached files.** Besides this file there is one ZIP, `SA02_Quadratic_covers_cotes_77_83_84_night.zip`. Unpack it once: it holds every file named below. Each ZIP named below is already unpacked inside, as a folder of the same name without `.zip` (for example `RESEARCH_SA02_broad.zip` is the folder `RESEARCH_SA02_broad/`), so there is nothing more to unpack; every other file is at the top level under its own name.

# RESEARCH_SA02: Grothendieck's theory of quadratic covers over an arbitrary base, their contracted product and his generalized Arf-Stiefel-Whitney invariants (cotes 84, 77 and 83)

**To be settled:** the theory of quadratic covers over an arbitrary base that he builds in cote 84 (late 1984 or after) on the ground of cotes 77 and 83: its classification of quadratic covers where 2 is regular, in characteristic 2 and in general; the contracted product and the rank-4 Azumaya algebras it produces; his χ-trivialized extensions and their signs; and the "invariants d'Arf-Stiefel-Whitney généralisés" he announces on 84/43. A.1 is the main question.

Cotes 90 and 91/2-18, also in this topic, are worked through in their own prompts (the working-through objects H01J, H01K and H01L); they are not part of this one.

For GPT-6 Astra (OpenAI), ChatGPT Pro mode. File prefix for the deliverables: `RESEARCH_SA02`.

**Who drafted it.** Claude Opus 5.5 at effort max (Anthropic), agent a6d42bf6fe2b0d8a8, on 19 Nov 2026. It leads topic SA02 in sweep 3 (wave 1) and swept the topic in sweep 1. The user's decision of 19 Nov 2026 was relayed by the main session (Claude Opus 5.5 at effort max).

## What is attached

- **`RESEARCH_SA02_study.zip`: our study.**
  - `study/STUDY.md` (it lists what was not read in full), `study/HUNCHES.md`, `study/RESEARCH_PACKAGES.md`, and the tables `CHECK_EVENTS.tsv`, `CORRECTIONS.tsv`, `DEPENDS.tsv` and `DELIVERABLES.tsv`.
  - `study/readings/`: cote 84 in full (reader R4) and cotes 90 and 91/2-18 (reader R3), each Claude Opus 5.5 at effort max.
  - `study/SA04_cote77/`: the reading of cotes 76-79 by R4 for topic SA04, whose cote-77 part ("Extensions quadratiques", 77/21-86) is the ground of A.2, with its check events and corrections.
  - `study/SA01_cote83/`: the reading of cote 83 (and 93/92-134) by R1 for topic SA01, with its tables: the rank-4 Azumaya algebras and the ∗-product.
  - `study/stage_A_dossier_SA02_part2/`: the stage-A topic dossier of cotes 84, 90 and 91/2-18, made by GPT-6 Astra (ChatGPT Pro mode) on 19 Nov 2026 (`SA02_dossier.md`, `SA02_directions.md`); its claim ids refer to its own tables, which are not attached.
  - `study/sweep2_WHAT_IS_WHERE.md`: the map of the items SA02-1 to SA02-n.
  - All of this was written by Claude Opus 5.5 at effort max (Anthropic) on 18-19 Nov 2026, except the stage-A dossier. It was checked as recorded in the CHECK_EVENTS tables and nowhere else.
- **`RESEARCH_SA02_transcriptions.zip`: the AI transcriptions (LaTeX) of his pages, with their notes.**
  - `transcriptions/Pro/`: by GPT-6 Astra (ChatGPT Pro mode), each with its notes and doubt table: 84/97-145, 84/146-193 and 83/178-222.
  - `transcriptions/Codex/K84`, `K77`, `K83`: the Work returns of batch K, by GPT-6.2 Astra at reasoning effort max for most folders and GPT-6 Astra at reasoning effort max for the others (`transcriptions/Codex/AUDIT_K_RETURNS_20261118.tsv` gives the model of each folder). K84-01 to -07 are the only witness of 84/2-111.
  - `\scanpage{N}` marks scan N of the cote's PDF. Where a step of yours depends on a doubtful reading, say so.
- **`RESEARCH_SA02_broad.zip`:** the sweep-3 studies of SA04 (regular polytopes over rings, cotes 69-102) and SA01 (cotes 71-83), and the sweep-2 map of SA03 (deformations and crystals).
- Fetch the literature yourself. It is listed under "Sources" below.

## Where this comes from

His pages are in the Grothendieck archive of the University of Montpellier. They were transcribed by AI (above) and studied in our horizontal sweeps by Claude Opus 5.5 at effort max.

- **Cote 77 (1977-78), "Extensions quadratiques" (77/21-86).** Quadratic covers Ω = Spec B with B locally free of rank 2; the affine envelope; D = b² − 4c and Δ(N_{Ω/S}) = −D; Σⁿ and relative divisors; algebras ↔ (L, D) when 2 is invertible; Artin-Schreier in characteristic 2; and a mixed-characteristic theorem, quadratic covers ↔ (L, D, b₀) with a condition mod 4 (Th. 77/57, 77/59).
- **Cote 83 (1982-86).** 2×2 matrices over a ring; rank-4 Azumaya algebras M(b, c, b', c', t) and their criterion (83/075-128); twists and the ∗-product of quadratic algebras (83/129-181).
- **Cote 84 (late 1984 or after; its later pages are on the backs of an October 1984 typescript of Récoltes et Semailles), under the title "invariants d'Arf-Stiefel-Whitney généralisés" (84/43).** Binary forms and their quadratic algebra ("l'invariant d'Arf", 84/9-42); quadratic covers through (L, P₁, Q) (84/44-62); the contracted product (84/63-66, 87-106, 172-192); χ-trivialized extensions (84/66-87, 124-170); three quadratic algebras (84/4, 111-122); a graded monoid with parities (84/2, 54-56).

**Other work.** Michel Hua's project (github.com/Commutator-IO/grothendieck-project) has modernised readings of some of these cotes. You may consult them; credit any point taken from them to "Michel Hua's project", and quote phrases, not passages.

## Results this prompt builds on (status on 19 Nov 2026)

Each result carries the id of its check event or correction in the attached tables. Check each one where you use it (Rules of proof, 7).

- **R1 (SA02-R84-07, -08, -10, -11, -17; SA02-K84-04, -05, -07).** Q(z + T) = z² − δ with z = 2x − T, and the class T₀² ≡ δ mod 4 is well defined; the explicit A = {(b, r): b₀ = r₀T₀} with N(b, r) = (b² − r²δ)/4 is integral. The contracted product: b = b₁b₂, c = b₂²c₁ + b₁²c₂ − 4c₁c₂ and u = 2u₁u₂ + b₂u₁ + b₁u₂, with Q(u) = b₂²Q₁(u₁) + b₁²Q₂(u₂) + 4(Q₁Q₂ − c₁Q₂ − c₂Q₁) exactly (sympy). The Theorem of 84/90 holds for all points (re-proved). Over Z the fixed lattice of σ₁ ⊗ σ₂ in A₁ ⊗ A₂ is {a + pu₁ + qu₂ + ru₁u₂: 2p = rb₂, 2q = rb₁}, which gives the Proposition and Corollary of 84/86-87.
- **R2 (SA02-R84-09, -12, -13, -15, -16; SA02-K84-11, -12, -13).** For χ-trivialized torsors, π(x) = χx − Tψ(x), and (L, P, T), (E, ψ, T with ψ(T) = χ) and χ-retractions are equivalent. Of the two sign conventions of 84/130-140, the plus convention b'ᵢ = bᵢ + χUᵢ gives b'₁ ⊗ b'₂ = b₁ ⊗ b₂ + χU and U'' = U + U' exactly; the minus convention leaves −2χ(U₁U'₂ + U'₁U₂). The "signe étrange" (U₁ ∗ U₂)(x₁ ∗ x₂) = −χ U₁(x₁) ⊗ U₂(x₂) of 84/134-136 is consistent: his map Φ: E → Hom^!(E, L) is −id on L. "2 − χ = 1" on 84/140 is no condition.
- **R3 (SA02-R84-19, -20; SA02-K84-08, -09).** His margin of 84/27, that torsors under the norm-one group U_A are the same for fppf and étale, holds when A is étale and fails in general: over k = F₂(t), A = k[e]/(e²) and Q = tN, the torsor Q(x) = 1 is trivial fppf-locally but not étale-locally (a claim of the stage-A dossier, rechecked). The Corollary of 84/36 needs the hypothesis his proof uses: the automorphism is not the identity near any point of X₀.
- **R4 (SA02-R84-01 to -05).** His graded monoid of 84/2 (even triples (L, δ, T₀), odd pairs (L, δ), β(L, δ) = (L, 4δ, 0)) is associative: associativity reduces to two identities, which hold. The seven quadratic subalgebras of A₁ ⊗ A₂ ⊗ A₃ are the fixed rings of the seven index-2 subgroups of F₂³. The "Théorème récapitulatif" of 84/24-27 is the correspondence between primitive binary forms with values in a line bundle and pairs (quadratic algebra, invertible module) of Kneser and Wood.
- **R5 (SA04-R77-01 to -10; SA04-K77-02, -04, -05).** Cote 77: the calculus of quadratic covers was re-derived (tr = bu, N = cu², b' = b + 2τ, c' = c + τb + τ², the invariance of D); the uniqueness argument of the mixed case (4 regular) and the existence argument (the lifts of b₀ form a torsor under 2L) hold; on 77/74 condition b) should read γ(b₀) ≡ Δ mod 4, as in his Th. 77/59 c); his normalization on 77/101 (μ = 2, not 1/2) and the identity on 77/117 (two signs) are wrong.
- **R6 (SA01-R83-04, -05, and the cote 83 reading).** On H ⊗ H', u ∗ v = bv + b'u − 2uv has eigenvalues t, t' with t + t' = bb' and tt' = b²c' + b'²c − 4cc'; they are the roots of Q(T) = T² − bb'T + (b²c' + b'²c − 4cc'), the two values of Tr(uv) for commuting u and v. M(b, c, b', c', t) is Azumaya exactly when Q(t) is a unit: R1 proved it through the trace discriminant −Q(t)², filling his unfinished "Suffisance" (83/100). The ∗-product gives the composition c = b₂²c₁ + b₁²c₂ − 4c₁c₂ with δ(q₁ ⊗ q₂) = δ(q₁)δ(q₂), which is the contracted product of R1.

## Leads (inferences by Claude, Anthropic; to be checked in full)

- **L1 (A.1).** Cote 84 is a characteristic-free theory of quadratic covers and of their monoid under the contracted product, aimed at Arf and Stiefel-Whitney invariants of quadratic forms over bases where 2 is not invertible ("Arf(E) ... plus fin que c₁(E) (si 2 non inv. sur X)", 84/2). His graded parity monoid and the χ-trivialized extensions should give an invariant of a form of rank n as an element of the graded monoid, finer than the discriminant when 2 is not invertible. Modern counterparts to compare: Voight's monoid of quadratic rings (its product is his Construction 3.14), Loos's graded discriminant algebras, Wood (2011), Dallaporta (2025).
- **L2 (A.2).** The mixed-characteristic classification by (L, D, b₀) describes the stack of quadratic algebras [A²/(G_a ⋊ G_m)] through the discriminant; it is not stated in this form in Knus, Loos, Voight or Wood.
- **L3 (A.3).** The ∗-product of cote 83 and the contracted product of cote 84 are one composition law, Voight's monoid product, and they agree with Bhargava's composition restricted to the diagonal case; the discriminant Q of a pair of quadratic subalgebras, whose roots are the commuting values of Tr(uv), is the same object.
- **L4 (A.4).** The "signe étrange" of 84/134-136 and the sign of the odd-odd product of 84/2 are one phenomenon, a Koszul sign of the odd part. Loos's odd-odd formula has minus four times the product where Grothendieck has plus four (a point of the stage-A dossier); the sign comes from the anti-identification −id: L → Hom(M, L).

## What the outcome must be

**The rule that governs everything below: push.** The work is to settle the questions, not to describe them. Give most of the time to the hardest item, the main question first. Partial results (cases proved, reductions, computations, the smallest undecided instance) are steps you write down and then build on; they never finish an item. When an approach stalls, take the next one: a different method; a reduction to a theorem you find, open and check; a larger or smarter search for a counterexample; a stronger statement that implies the item; a weaker one that it implies, which you then push up. Do not deliver while an item is undecided and an untried approach remains. A gap in a proof is an undecided step: mark it and attack it; never paper over it, and never present a proof with a gap as a proof.

**Progress check at three hours** (the user's rule of 13 November 2026, amended on 17 November 2026). After about three hours of work, and every hour after that, review the work against a dated ledger (`PROGRESS_LEDGER.md`, in every checkpoint): every open row with its status, and for each main question its current gate (the strongest proved reduction). Movement means only an open row changing status, or a main question proved to reduce to a strictly smaller gate. Restating the same gate, side results that leave every gate as it was, and packaging are not movement. After two consecutive reviews without movement, stop that work, write the final package with every item's state, and deliver it; this check takes precedence over the sentence above about untried approaches.

What counts as done, per item of the Parts and per Lead: (a) a theorem with a complete proof; or (b) a refutation
with a complete counterexample (given completely, every hypothesis verified, and checked by a program when it is
finite) together with the strongest true statement proved in its place. Nothing else finishes an item. Partly settled
is not an outcome. The cases proved, the computations run, the obstruction as an exact statement and the smallest
undecided instance are the state of an item you are still working on: record them as you go, then attack the
obstruction, starting from that instance. "Known" counts only with the derivation of the statement used here from the
cited theorem, after opening the source. An item that begins with "Determine" is done when the object asked for is
given explicitly, with a proof that it is the whole answer.

Not acceptable: a survey; "open, see [reference]"; a plan, an outline or a sample; a statement for every dimension
proved in low dimension without saying so; a step that replaces a claim by a convenient special case without naming
it; a reading of the manuscript taken on trust where the mathematics depends on it (the transcriptions are AI-made
and carry doubt marks: where a step depends on a doubtful reading, say so and prove the statement for each reading).

**When the work is finished.** Only when every item, every lead and every lettered task is proved (a) or refuted (b). Keep working until then: do not stop because the remaining items are hard, because a partial result looks presentable, or because much has already been done. If the session itself ends first (the environment stops you, not your choice), the first line of `RESEARCH_SA02_report.md` reads INCOMPLETE, and its table marks every undecided line with the state reached, every approach tried with where it failed, and the next step you would take. Never present such a return as complete or as following an allowed alternative: there is none. A statement may be labelled Open only in a return marked INCOMPLETE, with the cases proved, the computations run, the obstruction, the smallest undecided instance, and every approach tried with where it failed.

## Parts

**A. Quadratic covers over an arbitrary base (cotes 77, 83, 84). The main question is A.1.**
- **A.1 (main).** His "invariants d'Arf-Stiefel-Whitney généralisés" (84/43, 84/2). Settle L1: determine, for a quadratic form E of rank n over a scheme X on which 2 need not be invertible, the invariant Arf(E) that his graded parity monoid and his χ-trivialized extensions are built to carry, prove that it is additive for orthogonal sums through the contracted product, and prove or refute his claim that it is strictly finer than c₁(E) (and than the discriminant) when 2 is not invertible on X. Relate it to Loos's graded discriminant algebra and to Voight's monoid, with locators.
- **A.2.** The classification of quadratic covers, in his three settings:
  - (a) where 2 is a non-zero-divisor: covers ↔ (L, D, b₀) = (L, δ, T₀) with T₀² ≡ δ mod 4 (77/53-64, 77/74-86; 84/44-56): full faithfulness, the essential image (b₀² = D on S₀ = V(2) and D₁ = γ(b₀) on S₁ = V(4), Th. 77/59), and his criterion that Δ = b² − 4c if and only if the étale algebra A_{2Δ}[√Δ] extends over A_Δ (Th. 77/57);
  - (b) in characteristic 2: covers by (L, P₁, T, α) as torsors under G_T = ker(u ↦ u² + Tu) (84/57-58);
  - (c) in general: covers by (L, P₁, Q) (84/59-62).
  Prove each in full or refute it with the corrected statement, and settle L2, with locators (Knus, Loos, Voight, Wood, Dallaporta).
- **A.3.** The contracted product over every base: the integral formula (R1), the kernel Ann(2, b₁, b₂)·U of A → A₁ ⊗ A₂, the fixed-ring criterion 2O + b₁O + b₂O = O (checked over Z), and the Theorem of 84/90. Then the rank-4 Azumaya algebras of cote 83: prove over every base that M(b, c, b', c', t) is Azumaya if and only if Q(t) is a unit (R6), and settle L3.
- **A.4.** The χ-trivialized extensions (84/66-87, 124-170): give one coherent sign convention for the monoidal structure (R2: the plus convention and the sign of the dual), prove its coherence constraints, and settle L4.
- **A.5.** Three quadratic algebras (84/4, 111-122): state precisely and prove or refute his statements on the rank-4 subalgebras of A₁ ⊗ A₂ ⊗ A₃ and on quasi-biquadratic systems, in the étale case and over any base, with the corrected lemma of 84/120 (SA02-K84-10).

## Sources (fetch them; cite them with exact locators; prefer the arXiv LaTeX source)

- M.-A. Knus, *Quadratic and Hermitian forms over rings* (Springer, 1991), ch. I-III.
- O. Loos, "Discriminant algebras of finite rank algebras and quadratic trace modules", Math. Z. 257 (2007); his work on graded discriminant algebras (1997).
- J. Voight, "Discriminants and the monoid of quadratic rings", Pacific J. Math. (2016).
- M. M. Wood, "Gauss composition over an arbitrary base", Adv. Math. 226 (2011).
- M. Kneser, "Composition of binary quadratic forms", J. Number Theory 15 (1982).
- M. Bhargava, "Higher composition laws I", Ann. of Math. 159 (2004).
- Dallaporta (2025), on quadratic algebras where 2 is regular (locator to be found).

## Rules of proof (they bind every statement you deliver)

1. State the actual claim with all its data (the axioms assumed, the class of structures, finiteness and dimension
   hypotheses). Do not replace it by a convenient special case. If you prove a special case, name it as one and keep
   the general statement on your list.
2. Type every map and relation you introduce: source, target, the category or ordered set in which it lives, and each
   extra property you use. Compositions must type-check.
3. Every reduction ("we may assume", "replace by", "refine to") comes with its comparison map and a proof that the
   exact property needed transfers in the direction needed.
4. "Up to" names the ambiguity. Keep apart: equality; isomorphism of algebras against isomorphism of algebras with their involution; equivalence of categories or of fibred categories (stacks); torsors in the fppf and the étale topology; a monoid structure up to isomorphism against an equality of classes.
5. Check the edge cases in scope: characteristic 2; 2 a zero-divisor or nilpotent; non-reduced, non-noetherian and non-connected bases; non-étale and degenerate quadratic algebras (b and c in the maximal ideal); rank 1 and 2; trivial and non-trivial line bundles L; the cases chi = 1, chi = 2 and chi nilpotent.
6. A counterexample is given completely and, when finite, checked by a program whose code and output you attach. One
   verified counterexample refutes the statement: say "false". An invalid proof alone shows a gap, not falsity; keep
   the two apart.
7. No authority. Grothendieck's pages, the transcriptions, our study, the readers' reports, their check events and
   corrections, and the Leads (inferences by Claude, Anthropic) are all to be checked where used; the Leads in full.
   If one is wrong, say so plainly and show where.
8. What is not yet settled stays on the page as an exact statement, with what you tried and the step that fails, and
   you go on attacking it; it never finishes an item. Never write it up as proved, and never drop it.
9. Known results are cited with exact locators (author, work, theorem or section number), not proved again, except
   for a short proof of a form the source does not state. Every new statement of this run is proved in full in the
   paper. Before calling anything new, search the literature and say what you searched. Never
   invent a reference; mark each entry of the bibliography opened or not opened. Prefer the LaTeX source of a paper
   (the arXiv e-print) where one exists.

## What to deliver

One ZIP containing:
- `RESEARCH_SA02_paper.tex` and its PDF (LuaLaTeX, compiles cleanly): the mathematics in the order of the Parts, every
  statement numbered and labelled Proved / Proved under stated hypotheses (with whether they hold where the statement
  is used) / Refuted (with the counterexample and the corrected statement) / Known (with citation), each new statement
  with its complete proof; checked and unchecked statements in separate parts; English, first person plural. Where a
  statement is Grothendieck's, give the cote and scan of his page.
- `RESEARCH_SA02_results.csv`: one row per numbered statement:
  `id, statement, status, where_proved, depends_on, manuscript_pages, notes`.
- `RESEARCH_SA02_references.bib`: each entry marked opened / not opened.
- `RESEARCH_SA02_report.md`: the outcome table first (one line per item of the Parts and per Lead: proved or refuted, with the
  statement number); then what you read, what you computed (every program with its scope, counts and run time), and
  every correction to the study, the readings, the transcriptions and the Leads, with the attached file and line.
- `PROGRESS_LEDGER.md`: the dated ledger of the progress reviews.
- `CHECK_EVENTS.tsv` (below) and `code/`: every program you ran, with its output.

The work is AI-produced by GPT-6 Astra (OpenAI, ChatGPT Pro mode); credit it so, attribute nothing to any person, and
claim no priority: where a result is known, cite it; where you did not find it, say what you searched.

This task is long by design. Work through all parts completely; do not stop at an outline, a sample or a plan, and do
not ask whether to continue. Take the time the work needs. Write the files from the start and extend them as you go,
so that an interruption loses little.

**Check events.** For every statement, record its check events in `CHECK_EVENTS.tsv`, one row per event: statement id, date, who (model, effort, run), type (targeted proof check / independent re-proof / computation or formal certificate / used and rechecked in this run / carried as background without fault found / refuted, with the refined statement's id), outcome. This covers the statements of this run and every earlier statement you check, use or refute here (the attached study's statements carry ids such as SA02-R84-11; keep them). Give each event the type of what actually happened, neither more nor less. `CHECK_EVENTS.tsv` goes into every checkpoint and into the final ZIP.

**If the execution environment fails.** A failed or unavailable environment does not end the task. Retry at intervals for as long as this session lasts, without writing recovery text into the chat. When the environment is back, restore your work from your newest checkpoint and the earlier checkpoints its file list names, redo what you had done after that checkpoint, and continue to the end. Do not write files out in this chat instead: the work reaches us only through checkpoint ZIPs and the final ZIP.

**Typesetting check.** Every PDF you deliver is published as it is. Before you deliver one, read its build log: no overfull box may stick out by more than 2pt, whether a diagram, a display or a line of text. Fix each one in the source (scale or split a wide diagram, break a wide display, let a line break) and compile again. Then render pages to images and look at them: every page that had an overflow, and a sample spread over the document. Give the counts before and after in the report.

**Checkpoints.** Save a checkpoint ZIP to the user's Library, or wherever files survive the loss of the execution environment, once every 45 minutes of work, each under a new name, `RESEARCH_SA02_checkpoint_<NN>.zip` with `NN` counting up; never overwrite, rename or delete an earlier checkpoint, and put no earlier checkpoint ZIP inside a checkpoint. Save checkpoints once every 45 minutes and at no other time: none after a page, part, section, cote, folder, chapter or reader. If the workspace comes back empty, restore it from the newest checkpoint and from this conversation before you continue. The final ZIP holds everything the checkpoints held. A checkpoint is one ZIP holding every deliverable written so far and everything that documents the work (records, notes, logs, scripts, the report so far), so that a new session can continue from it and the files attached to this prompt. Leave the attached files themselves out of it, the scans and sources you were given: we have them. It is never a JSON file, a recovery file, a summary, or an export of the newest pages only. Each checkpoint zip holds the current deliverables and documentation; earlier checkpoints are not copied into it. The checkpoints are what keeps the work if this session dies: work that is in no checkpoint is lost. Keep every checkpoint ZIP, and the final ZIP, under 500 MB.
