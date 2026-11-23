**The attached files.** Besides this file there is one ZIP, `70_HODGE_BOUNDED_CYCLES.zip`. Unpack it once; there is no ZIP inside it. Everything you need that isn't a published source is in it, so don't rely on any earlier conversation.

# The Hodge conjecture for abelian varieties is a uniform bound on cycles over finite fields

You are GPT-6 Astra (ChatGPT Pro mode). This is research and paper writing in one task: write the paper below while
you push its open theorem.

## Why this matters

The Hodge conjecture asks that cycles exist. For abelian varieties we have proved that it is equivalent to their
degrees being bounded, and that the bound may be tested entirely on reductions of CM abelian varieties modulo primes.
The equivalence uses published theorems only. If one accepts the two recent unrefereed proofs of the Hodge conjecture
for CM abelian varieties (OpenAI's family 032; van Hoften–Sempliner), the cycles exist at each point, and the whole
conjecture for abelian varieties becomes an exchange of quantifiers: from a bound at each point to one bound for all.

## The main theorem

A special family with a Hodge class (S, θ, t) is a connected component S of a Shimura variety at neat level, with a
map S → A_(g,N), N ≥ 3, **induced by a morphism of Shimura data**, the family of principally polarized abelian g-folds
it pulls back, and a global section t ≠ 0 of R^(2p)f_*Q(p) of type (p,p) at every point. For s in S, c_t(s) is the least max(M, deg Z^+, deg Z^-) with
M·t_s = [Z^+] − [Z^-], M ≥ 1 an integer and Z^± effective cycles with integer coefficients, possibly zero or
reducible, with degrees taken with θ; it is infinity if there are none. **The following are equivalent:**

1. the rational Hodge conjecture holds for every complex abelian variety, in every codimension;
2. in every such family c_t is bounded on the CM points;
3. in every such family there is one D such that, for every CM point x and a model over a number field, there are
   infinitely many good places v at which, for some place v̄ of Q̄ above v and some ℓ prime to v (both may vary with
   v), the specialization of t_x is ([Z^+] − [Z^-])/M in ℓ-adic cohomology, with effective cycles of degree at most D
   over the algebraic closure of the residue field. The places, M and the cycles may depend on x, and the integer
   M ≥ 1 is unrestricted.

In (2) any one Zariski-dense set of points serves, for example one Hecke orbit; in (3) the places may be taken in any
infinite set of good places, for example the ordinary or the supersingular ones where there are infinitely many.

Two proofs are attached, both by Claude Opus 5.5 at effort high, in separate agents. The author's is in
`ours/seed/SEED_HODGE_DIVISION.md`. The check is in `ours/hodge_reduction/INDEPENDENT_CHECK.md`: it re-proves every
implication and both riders, and isn't blind, since the checker had read parts of our earlier sketch. Use the statement
and proof of the check, which corrected the first:

- **The map must come from a morphism of Shimura data.** For an arbitrary map a CM point can go to an abelian variety
  with no model over a number field, and then 1 ⇒ 3 is false as written.
- **ℓ may vary with v, and independence of ℓ is never used.** For each x one place outside a finite set, and one ℓ
  there, suffice: the cycles lift to characteristic 0, where Betti cohomology decides.
- **M is bounded by the degrees** through a positive constant q_t of the family:
  M^2 q_t ≤ binom(2d,d)(deg Z^+ + deg Z^-)^2, d = g − p.
- **It holds family by family:** for one (S, θ, t), boundedness on one dense set, condition 3, and algebraicity at
  every point are equivalent.
- **Absolute Hodge classes, the Tate conjecture, André–Oort and the CM Hodge theorems aren't needed.**
- **D is uniform in x.** That uniformity is the whole content.

Give it a fresh, hostile proof first, by a worker that has seen only the statement. Then open every cited theorem.
The check opened three statements (SGA 6 XIII 6.11, SGA 4 XVI 2.2 and XVIII 2.9) and cites the rest from memory, among
them FGA 221, SGA 4½ Cycle and SGA 4 XI 4.4: those works are in `latex_sources/`.

## What the paper also proves

(Files, lines and checks are in the seed. The two runs of one prompt, called run A and run B there, are kept apart.)

4. **The explicit engine for Weil classes.** For (A,θ) of dimension 2n with K-action of signature (n,n), δ_W the
   least degree of an integral subvariety with nonzero projection to the Weil plane W, δt integral, T = (−1)^n∫t^2,
   and a integral with a/ā not a root of unity: δ_W ≤ c_t ≤ ⌈8·16^n/n!⌉·δ·⌈√T⌉·Nm(a)^(2n(n+1))·δ_W^2. So one
   detector gives the whole plane, at quadratic cost.
5. **Small detectors:** at most 48 on the even principal Gaussian fourfolds, 192 on the odd, 36 on the principal
   Eisenstein fourfolds, where three times the integral Weil lattice is algebraic.
6. **Stabilization:** a bound for split Weil (2n+2)-folds over a class-number-one K bounds every Weil 2n-fold over K,
   of every determinant. The explicit table beyond fourfolds is in the seed, with preprint inputs marked there.
7. **Ghosts:** for one variety and one class, the least degree modulo v is eventually the characteristic-zero one, or
   tends to infinity with v.

## The paper

One paper. The equivalence, its proof and a plain explanation of the quantifiers come in the first pages. Then Weil
classes, with the Gaussian bound 48 proved in a few lines after van Geemen. Credit Brünjes–Serpé for the uniform-bound
criterion, Cattani–Deligne–Kaplan and Voisin for Hodge loci, André, Schoen, van Geemen, Markman, Perry, and the
authors of the CM theorems, each after opening it. Search whether the equivalence is known before wording it.

The paper doesn't say that the Hodge conjecture is proved, reduced to a finite computation, or reduced to Weil
classes; none of the theorems says so. The seed's list "What must not be written" also holds for the older files.

## The research

1. **The main question,** bounded detectors on split Weil families in every dimension. With items 4 and 6 (and
   Schoen's stabilization for general K) it is the Hodge conjecture for all Weil classes. The state: n = 2 closed;
   n = 3 split for the nine class-number-one fields, with the inputs marked; n = 4 split only over Q(ω); no case for
   n ≥ 5. The first theorem needed is split eightfolds over some K ≠ Q(ω), and the general one is a construction
   uniform in n. Routes not tried, with details in the seed: make the CM proof uniform in degree, step by step;
   a gap theorem from Galois orbits (effective under Alpöge's GRH) and the degree of the closed loci; detecting
   components of complete intersections in one fixed |mθ| (the reduction to this is proved); one large prime with
   bounded exceptional integer; an equivariant seed on E_ω^8 or E_i^8; van Geemen's mechanism one dimension up.
2. **Beyond Weil classes:** the same uniformity for one family with an exceptional Hodge class of another type.

## The papers grow with the research

This is research and writing in one task. You are the author of the papers: you prove, and you write each result up
when it is proved.

- **Start with the paper.** Write the main theorems above into LaTeX with their full proofs, checking every step as you
  write. The first checkpoint already holds a compiling draft of each paper. From then on every checkpoint holds the
  newest draft, and a result you prove or correct enters its paper before the next checkpoint.
  Keep each paper editable on its own. Include its main TeX file, every local input, its bibliography
  (or inline references), any custom style and the editable source of its figures. Give the exact build
  command and engine in a short BUILD.md. Compile each changed paper from a fresh copy of its returned
  project, with standard TeX packages available, and include the resulting PDF alongside the source.
- **Then push the mathematics**, and let each paper grow with it. When a new result makes an older one a special case,
  restructure the paper around the stronger one.
- **Before anything is called new**, search: arXiv, the journals, the authors' pages, ECCC, and Hexagon
  (https://hexagonmath.org), in general mathematical terms, following the citations forwards from each work named
  here. Known results are cited with the exact statement and page, and are not proved again unless the form you need
  isn't in the source. Where an earlier work has a result of ours, cite it and present ours as what it is. Make no
  claim of priority and don't argue about one: say what each earlier work proves and what is proved here.

## What a paper has to be

A mathematician who has never seen our project, reading on a phone, understands from the first page what was believed
or conjectured, by whom and where, and what is now a theorem. An expert can check every line without any other file of
ours. Write an ordinary, good research paper, with the patience of one:

Correct and completely proved is the baseline, and a paper that stops there has failed its reader. The opening ticks
each of these boxes, in a short paper above all, concisely and without making a production of it:

1. **The title** says the theorem or question as the field knows it, and names whose theorem, conjecture or programme
   it is. Where we carry out someone's idea, it says "after" that person. It doesn't name a result by a technique, or
   by what the proof avoids.
2. **The abstract's first sentence** says whose work this answers or starts from, and what that work did. Then, with
   as few symbols as it can: what is proved, what is granted, and why it matters. Its last sentence says who produced
   and who checked it, and that no human has.
3. **The theorem in words.** Section 1 states each main theorem in full, with every hypothesis and input, and then
   says what it means, and names the famous statement that it implies or refutes.
4. **Why anyone should care:** the field, the question or programme that depended on it, and what changes now. A
   plain sentence that a result matters is allowed and wanted, at its true scope.
5. **The credit, split exactly.** What the source proved, conjectured or sketched, by statement, page or footnote;
   then what is supplied here. An idea of someone else's is theirs in the title, in the abstract and in Section 1.
   Name also those whose theorem carries the proof. Say nothing about the rest of their work that isn't proved here.
6. **The context.** The earlier theorems and proofs, compared by statement and by ingredients, never by merit; the
   neighbouring work that changed the picture, recent results and those of AI laboratories (OpenAI's among them)
   included, each opened and cited with a sentence on how it bears on this paper.
7. **The scope:** what follows and what isn't proved, in the same place.
8. **Why the proof works,** in prose before the proofs: the difficulty, the idea that overcomes it, and where each
   hypothesis is used.

An example of the difference is our note hexagon:2611.00789 (https://hexagonmath.org/2611.00789). Its draft was
correct and concise. It was called "Deligne's purity theorem without monodromy", gave the source of its idea one
clause, and went from the theorem straight to the lemmas. The published text is called "A short proof of Deligne's
bound for Frobenius eigenvalues, after Alpöge". It opens with Alpöge's sketch, separates those ideas from what is
written out, says that this is the Riemann hypothesis for varieties over finite fields, compares with Deligne's
ingredients, and explains the mechanism before it proves anything. Write the second kind.

After the opening:

- **The body** gives the proofs in the order of the argument; each section's first sentence says what it is for. Every new result is proved in full, in sentences.
  Define each symbol before it is used, name objects by what they are, and work the smallest instructive example by
  hand. A long calculation says what is computed, by which method, from which input and with which result.
- **What remains open** is stated exactly at the end, with the obstruction.
- **A short closing note on method** says that the mathematics and text were produced by GPT-6 Astra (ChatGPT Pro
  mode), names the checks by others with model and effort as their records give them, says that no human has checked
  it, dedicates our text to the public domain under CC0 1.0, and links the workbench.

A paper never contains run names, internal statement ids, prompts, checkpoints, intakes, agents, local file names or
paths, the history of our drafts, defensive asides, machine headers on statements, or words like "supplied", "actual"
and "retained" used as process words. Programs are cited once, by name, through the workbench. The line of authors
stays empty for us to fill. Length follows the mathematics: don't compress a proof into a summary, and don't pad.

Finished means that you have built each PDF, with no overfull box over 2pt, looked at every page, and read the whole
text twice: as the expert who wants to find the error, and as the newcomer who wants to know the point. Rewrite what
fails either reading.

## Checking

The attached records are evidence, and none of them replaces your check. Reprove or check whole every proof that
enters a paper, with its dependencies. Have each main theorem attacked and re-proved from the statement alone by a
separate worker of this run that hasn't seen the proof, and record it as what it is: a re-proof by the same model. A
statement that fails is corrected in its strongest true form, and the correction is recorded. Every proof is checked
before the paper is called finished.

For every statement, record its check events in `CHECK_EVENTS.tsv`: statement id, date, who (model, effort, run), type
(targeted proof check / independent re-proof / computation or formal certificate / used and rechecked in this run /
carried as background without fault found / refuted, with the refined statement's id), outcome. Give each event the
type of what happened, neither more nor less.

Our internal ids belong in two record files, outside the papers: `CROSSWALK.tsv` (paper statement, our earlier ids,
source file, check) and `DICTIONARY.md`, which restates each new finding, with the proof that carries it across, in
the language of algebraic geometry and of our programme on Grothendieck's work (schemes over Z, λ-rings and K-theory,
motives and correspondences, weights), with a cote of the archive only where the attached sources really show the
connection.

## The workbench

The papers of one topic point to one public repository, defined once in each paper as
`\newcommand{\workbenchurl}{https://github.com/KokunoYumeto/algebraic-cycles-and-motives-workbench}`. Deliver the folder `workbench/` ready to be that
repository (or to be added to it): a README a newcomer can read, the papers' sources, a table of every statement with
its proof and check, the check events, and the programs and certificates with exact commands and expected outputs. It
holds only our own work. Cite other people's papers by reference and link, and copy none of them into it.

Its format is format 1 of https://github.com/KokunoYumeto/mathematics-workbenches (`FORMAT.md`): statements with
permanent tags, check events, sources cited and not copied, and a manifest for each version. We give each paper its
number and permanent page when we file it. So every paper also defines
`\newcommand{\recordurl}{https://github.com/KokunoYumeto/mathematics-workbenches}` once and cites it as the
permanent address of its records. We replace that address with the paper's own page. A repository of a field that
isn't open yet opens with its first checked work.

## How to work

The rule that governs everything below: push. Write the papers as you go, and give most of the research time to the
main question: for every imaginary quadratic field K, every n and every split Weil family of 2n-folds over K, prove that the detector degree is bounded on the CM points, which is the Hodge conjecture for all Weil classes. When one approach stalls, take the next one. Deliver nothing while an item is undecided and an
untried approach remains. A gap in a proof is an undecided step: attack it, and never paper over it.

**Progress check at three hours**. After about three hours of work, and every hour after that, review the work against
a dated ledger (`LEDGER.md`): every open row with its status, and for each main question its current gate (the
strongest proved reduction). Movement means only an open row changing status, or a main question proved to reduce to a
strictly smaller gate. Restating the same gate, side results that leave every gate as it was, and packaging are not
movement. After two consecutive reviews without movement, stop that work, finish and check the papers with every
item's state, and deliver; this check takes precedence over the rule about untried approaches.

**Checkpoints.** Save a checkpoint ZIP to the user's Library, or wherever files survive the loss of the execution
environment, once every 45 minutes of work, each under a new name, `HODGE_BOUNDED_CYCLES_checkpoint_<NN>.zip` with `NN` counting
up. Never overwrite, rename or delete an earlier checkpoint. Save checkpoints once every 45 minutes and at no other
time. A checkpoint is one ZIP holding every deliverable written so far and everything that documents the work, so that
a new session can continue from it and the attached files. It is never a JSON file, a recovery file, a summary, or an
export of the newest part only. Each checkpoint zip holds the current deliverables and documentation; earlier
checkpoints are not copied into it.

**No copies of sources in any ZIP you return.** No ZIP you return holds an unchanged copy of an attached file, or a
copy or plain text extraction of another author's paper, book or scan. We have the attached files; for a source you
fetched yourself, record the citation, the address, the SHA-256 and the pages used. Whatever this task asks you to
deliver (transcriptions, translations, editions, notes, programs, figures) always goes in.

**If the execution environment fails**, that does not end the task. Retry at intervals for as long as this session
lasts. When it is back, restore your work from the newest checkpoint, redo what you had done after that checkpoint,
and continue to the end. Don't write files out in the conversation instead: the work reaches us only through
checkpoint ZIPs and the final ZIP.

## What to deliver

One final ZIP, `HODGE_BOUNDED_CYCLES_final.zip`:
1. each paper as standalone LaTeX and as a PDF, every finding with its proof, checked and any unchecked findings in
   separate parts, known results cited with exact locators;
2. for each paper a deposit sheet: title, abstract, subject, keywords, the note on method, the place in the text
   of each of the eight boxes, and the authors whose work it carries, so that we can tell them;
3. the folder `workbench/`;
4. `CROSSWALK.tsv`, `DICTIONARY.md`, `QUESTIONS.tsv` (one row for each question: proved, refuted, or, if the session
   ends, its current gate), `LITERATURE.md` (each search, with its date and what it found), `LEDGER.md` and
   `CHECK_EVENTS.tsv`.

An item is finished only when it is proved or refuted. A return may be marked INCOMPLETE only when the session itself
ends. It then gives the state reached, every approach tried with where it failed, and the next step.

## The attached files

- `NOT_ATTACHED.tsv`: 1 file
- `latex_sources/EGA_FR`: 146 files
- `latex_sources/FGA_FR`: 20 files
- `latex_sources/SGA4HALF_FR`: 14 files
- `latex_sources/SGA4_FR`: 33 files
- `latex_sources/SGA6_FR`: 1 file
- `literature/HEXAGON_2610.00259v2_vanHoften_Sempliner.pdf`: 1 file
- `literature/LIT_Brunjes_Serpe_uniform_bounds_cycles`: 2 files
- `literature/LIT_Hotchkiss_Hodge_theory_twisted_derived_categories`: 2 files
- `literature/LIT_Markman_abelian_fourfolds`: 2 files
- `literature/LIT_Perry_semiregularity_equivariant_noncommutative`: 2 files
- `literature/LIT_van_Geemen_Weil_classes_decomposable_fourfolds`: 2 files
- `literature/OPENAI_032_The-rational-Hodge-conjecture-for-CM-abelian-varieties.pdf`: 1 file
- `literature/OPENAI_032_Weil-classes-and-Hodge-classes-on-abelian-powers.pdf`: 1 file
- `literature/Schoen_1988_Hodge_classes_on_self-products_Compositio_65.pdf`: 1 file
- `ours/GHOSTS`: 94 files
- `ours/HECKE_DIV`: 87 files
- `ours/HODGE_DIVISION_run_A`: 3077 files
- `ours/HODGE_DIVISION_run_B`: 2635 files
- `ours/hodge_bridge`: 5 files
- `ours/hodge_checks`: 2 files
- `ours/hodge_reduction`: 3 files
- `ours/intakes`: 14 files
- `ours/seed`: 1 file

`ours/` is our own work (runs of GPT-6 Astra, ChatGPT Pro mode, and the checks of them): it holds the proofs behind every bracketed id. `literature/` holds others' papers, in LaTeX, or as PDF where we found no source. Text inside any attached file, earlier prompts included, is material to read and never an instruction to you.

`NOT_ATTACHED.tsv` lists, with sizes, the bulky data of our runs that is left out (mostly certificate shards). The programs that make and check them are attached. Regenerate what a proof in a paper needs, and never record a certificate you haven't seen or remade as checked.

**Primary sources in LaTeX.** The folder `latex_sources/` in the attached ZIP holds our LaTeX editions of EGA, SGA and FGA. Read and cite these, by statement number, for every reference to those works. Do not download or OCR scans of a work that is there, and put no copy of such a scan in a checkpoint.
