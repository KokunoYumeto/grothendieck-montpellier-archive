# RESEARCH_SA14_SA19: Grothendieck's Picard and Jacobians dossiers (cotes 57-60 and 43-44). Lefschetz for Pic in characteristic p (57:97-100), Seshadri's theorem and his Question 2 (57:103-111), the henselian questions of 1962, the structure of Pic_{X/S}, the local Lefschetz conjecture for π_1 (58:19), the canonical points of the torsors Pic^δ (cote 59), geometric class field theory in all degrees (43:80), the residual complex (43:50-69), and the programme of 1964 (cote 44)

To be settled: the main question (Part A) is Grothendieck's question on 57:97. For `X` smooth projective of dimension
`n ≥ 4` over an algebraically closed field `k` of characteristic `p > 0`, and `Y` a smooth hyperplane section, is
`Pic(X) → Pic(Y)` an isomorphism with no vanishing hypothesis on `H^i(Y, O_Y(−m))`? Is the kernel zero for `n ≥ 4`,
as he boxes it ("noyau nul")? Is there a smooth projective `X` with `O_X(1)` very ample and `H^1(X, O_X(−1)) ≠ 0`,
that is, a nonzero infinitesimal kernel in his corollary of 57:100? The same Picard and Jacobians dossiers carry
further questions, Parts B-J, one cluster of related questions.

For GPT-6 Astra (OpenAI), ChatGPT Pro mode. File prefix for the deliverables: `RESEARCH_SA14_SA19`.
Drafted on 19 Nov 2026 by Claude Opus 5.5 at effort max (Anthropic), agent a28ea31fa17dd65e1, at the word of the main
session (Claude Opus 5.5 at effort max), from the sweep-3 readings of these cotes. The readings were made the same day
by three readers, all Claude Opus 5.5 at effort max, read against the scans:
- aa478f9ff10218651 read cote 57;
- a262249a0710a599b read cotes 43, 44, 58, 59 and 60.

Related prompts: RESEARCH_SA06 (motifs II, cotes 14-15: algebraic and Albanese equivalence) and RESEARCH_SA16_SA18
(elliptic curves and abelian varieties). Their questions are not to be done here.

## What is attached

One file, `RESEARCH_SA14_SA19_background.zip` (1.5 MB; LaTeX and text only, no scans, no PDF). `MANIFEST.tsv` at its
root lists every file with its origin and SHA256.
- `sweep3_SA14/` and `sweep3_SA19/`: the sweep-3 study of each topic.
  - `STUDY.md`: what the pages contain, what is new, wrong and open.
  - `HUNCHES.md`: the Leads, with their grounds.
  - `RESEARCH_PACKAGES.md`: the questions as the readers framed them, with the strongest reduction known and the material.
  - `CHECK_EVENTS.tsv` and `CORRECTIONS.tsv`: every check and every correction of the readings, with the page.
  - `DEPENDS.tsv` and `DELIVERABLES.tsv`.
  - `readings/`: the item-by-item readings in page order: `c57.md`, `c58_c60.md`, `c43_c44.md`, with their TSVs. Every
    statement of this prompt that cites a page is worked through there.
- `sweep2_SA14_WHAT_IS_WHERE.md`, `sweep2_SA19_WHAT_IS_WHERE.md`: the item maps (item ids SA14-n, SA19-n).
- `sweep2_reports/cote57_scan144_a_verifier.md`: the reading of 57:144 decided on the scan image.
- `transcriptions/pro/<package>/`: the transcriptions by GPT-6 Astra (ChatGPT Pro mode), one `.tex` file per scan,
  `\scanpage{N}` = scan N, with the package's notes. Packages:
  - cote 57: MPL_57_089-132, 133-179, 226-270, 271-315;
  - cotes 58 and 60: MPL_58_020-067, MPL_60_002-035, 036-070;
  - cote 43: MPL_43_094-142;
  - cote 44: from MPL_16+47+54+44.
- `transcriptions/codex/<folder>/`: the transcriptions by Codex web / ChatGPT Work (GPT-6.2 Astra at Max), with their
  notes and math notes:
  - A57-01, A57-02, K57-01 to K57-10;
  - K58-01, K58-02, K59-01, K59-02;
  - K43-01 to K43-10, K44-01.
  - They are the only transcription of 57:2-88 and 180-225, 58:2-19, 59:2-28, and 43:1-93 and 143-208.
- `broad_layer/SA06_readings_c14_c15rest.md`: the sweep-3 reading of cote 14 (algebraic and Albanese equivalence,
  zero-cycles, the letter to Serre of 1965), which these questions touch.

His pages are diplomatic transcriptions: `\unsure{a|b}` marks a reading in doubt (the first is what the ink shows),
`\illegible` marks unreadable ink, and `\deleted{...}` and `\inserted{...}` keep his corrections. Quote his statements
from the transcription with the page as `cote:scan` (57:97 is cote 57, scan 97).

## Where this comes from

The pages are Alexandre Grothendieck's manuscripts in the Fonds Grothendieck at the Université de Montpellier:
- cote 57: the Picard dossier of 1961-1962, with the letters to Hironaka (Neuilly, 6 July 1962) and to Murre
  (18 July 1962);
- cote 58: Lefschetz-Grauert and the local Lefschetz theorems;
- cote 59: the determinant of cohomology on Picard torsors;
- cote 60: "Notes sur l'équation fonctionnelle";
- cote 43: duality for group schemes over local fields and curves, and geometric class field theory;
- cote 44: the "Programme de travail" in seven theorems and the letter to Serre of 12.8.1964.

The transcriptions are AI-produced: by GPT-6 Astra (ChatGPT Pro mode), and by Codex web / ChatGPT Work (GPT-6.2 Astra at
Max). The sweeps that located, linked and worked through the material are by Claude Opus 5.5 at effort max. In sweep 3
each page was read against the scans, the steps that carry each statement were re-derived (the check events), and the
open questions were stated with the strongest reduction on the page. No research run has yet worked on these cotes.

## Results this prompt builds on (status on 19 Nov 2026)

Each result was obtained or checked once, by a sweep-3 reader (Claude Opus 5.5 at effort max). The proof or computation is
in the reading named, and the check events are in `CHECK_EVENTS.tsv`. None has been checked independently. Check each one
where you use it.

- **R1 (57:111, his Question 2; c57 §1.6).** Refuted as stated.
  - Counterexample: X = Spec k[[t]][x,y,z,w]/(xy − z² − t²) over S = Spec k[[t]], with D = V(x, z − it). The fibres are
    normal, but D is not Cartier along a 3-fold node.
  - The refined form is proved: S regular and the fibres R_2.
  - The smooth case is Ramanujam-Samuel.
- **R2 (57:144; c57 §2.3).** His relation ξ_n = δ_n(η), marked "à vérifier", holds up to sign.
- **R3 (57:99-100; c57 §1.4).** The kernel K in his corollary on the generic hyperplane section has Lie algebra
  h·H^1(X, O_X(−1)), of dimension h^1(X, O_X(−1)). So K = 0 iff H^1(X, O_X(−1)) = 0.
- **R4 (57:97; c57 §1.3).** For n ≥ 4 the cokernel of Pic(X) → Pic(Y), and for n ≥ 3 the kernel, are finite p-groups
  of bounded exponent, built from the layers H^2(Y, O_Y(−m)) and H^1(Y, O_Y(−m)) for small m.
- **R5 (57:70; c57 §5.6).** Igusa's b_2 as written lacks a factor 2 (his slip).
- **R6 (57:286; c57 §4.3).** For X = (A × B)/Γ, with Γ finite acting on A and freely on B:
  Pic_X = Pic_Y × Pic_A^Γ and Pic^τ_X = Pic^τ_Y × A'^Γ. Igusa's own example gives Hodge difference 0.
- **R7 (60:53; c58_c60 §2.5(d)).** His open question "δ^♮(E)² = q^{χ^♮(E)} ??" has the answer yes. His correction
  terms μ_x vanish for every E, so E ↦ E^♮ commutes with duality.
- **R8 (58:2-19; c58_c60 §3).**
  - Lemme 2 and 3, the cutting Théorème and its converse, and the local Lefschetz theorem for π_1 of 58:19 are
    re-proved.
  - His "Conjecture" (finite generation of the local étale fundamental group) is reduced to normal A of dimension 2.
  - H^1(U_1, Z/p) is finite for every connected finite étale U_1 → U (Hartshorne-Speiser-Lyubeznik).
- **R9 (59:10-14; c58_c60 §4.3-4.4).** The boxed relation of 59 is re-proved. The torsor Pic^δ has a canonical point
  when at most one d_i is odd (Mumford's e_*^L), and (Pic^δ)^{⊗2} always has one.
- **R10 (43:117; c43_c44 §1.5).** On the scan: π_0(A) and π_0(B), the component groups of the Néron models of an abelian
  variety A over a local field and of its dual B, are dual with values in Q/Z. This is his pairing of SGA 7 IX, known
  there. The page places it in the duality programme of 1964-65.

## Leads

The Leads are the hunches in `sweep3_SA14/HUNCHES.md` (H1-H13) and `sweep3_SA19/HUNCHES.md` (H1-H6). They are
inferences by Claude, Anthropic, and every one is to be checked in full: proved, or refuted with the corrected statement.
The parts below use H1-H4, H7, H9, H11-H13 of SA14 and H3-H5 of SA19. Each of the others is settled where it bears on a
part, in the report's table:
- SA14 H6: Nér = Pic/Pic^τ exists as an algebraic space as soon as Pic^τ is flat (57:277, "Au concours").
- SA14 H8: his expectation (12) on 57:8, D → NS(X_o) injective.
- SA14 H10: Pic^0 is an abelian scheme for smooth projective X/S in characteristic 0 over an arbitrary base (57:64).
- SA19 H1 and H2: priority remarks, to be checked against SGA 7 VII-IX.
- SA19 H6: the planning question on the leaves.

## What the outcome must be

**The rule that governs everything below: push.** The work is to settle the questions, not to describe them. Give most of the time to the hardest item, the main question first. Partial results (cases proved, reductions, computations, the smallest undecided instance) are steps you write down and then build on; they never finish an item. When an approach stalls, take the next one: a different method; a reduction to a theorem you find, open and check; a larger or smarter search for a counterexample; a stronger statement that implies the item; a weaker one that it implies, which you then push up. Do not deliver while an item is undecided and an untried approach remains. A gap in a proof is an undecided step: mark it and attack it; never paper over it, and never present a proof with a gap as a proof.

**Progress check at three hours** (the user's rule of 13 November 2026, amended on 17 November 2026). After about three hours of work, and every hour after that, review the work against a dated ledger (`PROGRESS_LEDGER.md`, in every checkpoint): every open row with its status, and for each main question its current gate (the strongest proved reduction). Movement means only an open row changing status, or a main question proved to reduce to a strictly smaller gate. Restating the same gate, side results that leave every gate as it was, and packaging are not movement. After two consecutive reviews without movement, stop that work, write the final package with every item's state, and deliver it; this check takes precedence over the sentence above about untried approaches.

What counts as done, per item of the Parts and per Lead: (a) a theorem with a complete proof; or (b) a refutation with a
complete counterexample, with every hypothesis and the failure verified (the variety, scheme, ring, group or family
given completely, and checked by a program when finite or computable), and the strongest true statement proved in its
place. Nothing else finishes an item. Partly settled is not an outcome. The cases proved, the computations run, the
obstruction as an exact statement and the smallest undecided instance are the state of an item you are still working
on: record them as you go, then attack the obstruction, starting from that instance. "Known" counts only with the
derivation of the statement used here from the cited theorem, after opening the source. An item that begins with
"Determine" is done when the object asked for is given explicitly, with a proof that it is the whole answer.

For Part A in particular:
- A positive answer is proved for every smooth projective X of dimension n ≥ 4 and every smooth hyperplane section Y,
  in every characteristic p > 0, with no vanishing hypothesis.
- A negative answer is one explicit X, Y and p, with the class in the kernel or the cokernel computed and checked.
- Every statement names whether Y is a hyperplane section for a given embedding, an ample divisor, or a general member
  of a linear system.

Not acceptable:
- a survey, or "open, see [reference]";
- a plan, an outline or a sample;
- proving R1-R10 again in place of the items, except where a Part asks for it;
- a result of the readings used without the check above;
- a statement for every p, every n or every X proved for some, without saying so;
- a step that replaces a claim by a convenient special case without naming it;
- a reading of his pages changed to fit the mathematics without saying what the transcription reads and why you read it
  otherwise.

**When the work is finished.** Only when every item, every lead and every lettered task is proved (a) or refuted (b). Keep working until then: do not stop because the remaining items are hard, because a partial result looks presentable, or because much has already been done. If the session itself ends first (the environment stops you, not your choice), the first line of `RESEARCH_SA14_SA19_report.md` reads INCOMPLETE, and its table marks every undecided line with the state reached, every approach tried with where it failed, and the next step you would take. Never present such a return as complete or as following an allowed alternative: there is none. A statement may be labelled Open only in a return marked INCOMPLETE, with the cases proved, the computations run, the obstruction, the smallest undecided instance, and every approach tried with where it failed.

## Parts

**A. Lefschetz for Pic in characteristic p (57:97-102; SA14-3; R3, R4; Leads SA14 H1, H3, H4). The main question.**
1. Prove or refute that Pic(X) → Pic(Y) is an isomorphism for X smooth projective of dimension n ≥ 4 over k
   algebraically closed of characteristic p and Y a smooth hyperplane section, with no condition on H^i(Y, O_Y(−m)).
   This is his "Question" of 57:97.
2. Prove or refute his boxed "noyau nul si n ≥ 4": injectivity for every smooth hyperplane section. Determine the least n
   for which injectivity holds in every characteristic.
3. Prove or refute that there is a smooth projective X of dimension ≥ 2 over k, with O_X(1) very ample, such that
   H^1(X, O_X(−1)) ≠ 0. By R3 this is the same as a nonzero infinitesimal kernel in his corollary of 57:100. If such X
   exist, determine the least dimension in which they occur.
4. Determine the kernel and cokernel of Pic(X) → Pic(Y) in terms of the layers of R4, and prove that this is the whole
   answer.

**B. Seshadri's theorem and Question 2 (57:103-114; SA14-4, SA14-18; R1; Leads SA14 H2, H13).**
1. For f: X → S proper flat with geometrically integral S_2 fibres over a normal noetherian S, prove or refute that a
   Weil divisor on X with no vertical component and Cartier on the generic fibre is Cartier. This is "Seshadri without
   Pic", 57:110.
2. Determine the exact condition on the fibres, and on S, under which his Question 2 holds. R1 has R_2 fibres over
   regular S as sufficient and the 3-fold node as a counterexample. Settle whether R_2 is necessary.

**C. The henselian questions of 1962 (57:193-194, 227-231, 272; SA14-5, SA14-6; Leads SA14 H5, H12).** For A the
henselization of a local ring of finite type over a field of characteristic 0, and over excellent discrete valuation
rings, prove or refute each of the following:
1. X^/Y^ projective ⇒ X/Y projective.
2. Pic(X) = Pic(X^) when R^1 f_* O_X has finite length.
3. Pic(Y − y) = Pic(Y^ − y^) at isolated singularities.

In characteristic p, prove or refute that the local Néron-Severi groups of S, S~ and S^ agree modulo p-groups. The
pages prove the analytic case (his Th. 1.7, Th. 2.1, Cor. 2.4); start from it.

**D. Pathologies of Pic in characteristic p from quotients (A × B)/Γ (57:283-297; SA14-7, SA14-9; R6).**
1. Construct, or prove impossible within this family, triples (A, B, Γ) with Γ finite acting on an abelian scheme A and
   freely on B such that dim (t_{A'})^Γ − dim (t_A)_Γ is positive, or negative, or varies in a family. This is the
   asymmetry h^{01} − h^{10} of X = (A × B)/Γ.
2. Settle whether A'^Γ can fail to be flat. Prove or refute the consequences he lists:
   - Pic^τ not flat;
   - the Picard variety not compatible with specialization.

   He plans to study "la famille modulaire de la surface de Igusa" (57:311). Do it.

**E. The structure of Pic_{X/S} (57:21-32, 73-79, 277, 308-315; SA14-4, SA14-9; Leads SA14 H6, H7, H9, H11).**
1. For X normal and proper over a trait with a section, prove or refute that every L on the generic fibre algebraically
   equivalent to 0 extends to X with special fibre algebraically equivalent to 0, i.e. properness of Pic^0 without
   projectivity (57:314-315).
2. Prove or refute that Corr_S(X, Y) is separated for X, Y proper flat with f_* O = O universally (57:22, 32).
3. Prove or refute that his "Problem A", the flattening functor for proper X/S (57:73-79), is representable by a
   monomorphism of finite presentation.
4. Settle his remaining open questions on Pic_{X/S} on 57:308-315, one by one.

**F. The local Lefschetz conjecture for π_1 (58:2-19; SA14-3, SA14-6; R8).** Let A be a complete noetherian normal local
ring of dimension 2 with algebraically closed residue field, and U = Spec A − {m}. Prove or refute that π_1^ét(U) is
topologically finitely generated.
- With 58:19 and its "Conséquence", a proof gives his Conjecture: topological finite generation of π_1 of the punctured
  spectrum of every complete local ring with algebraically closed residue field.
- The open part is the non-abelian wild ramification along the exceptional curves of a resolution. Finite H^1 of every
  open subgroup does not by itself give finite generation.
- First establish the state of the question in the literature (Grothendieck-Murre, LNM 208; Carvajal-Rojas, Schwede and
  Tucker for strongly F-regular rings).

**G. The canonical points of the torsors Pic^δ (59:2-28; R9).**
1. For each polarization type D = (d_1 | ... | d_n), determine whether Pic^δ_{A/S} has a section over the moduli stack
   of abelian schemes with a polarization of type D over Z[1/2], compatible with base change.
2. Prove or refute that the trivializations his page constructs from the determinant of cohomology are these canonical
   sections. This is his "à vérifier".
3. Settle the sign question of the Albanese torsor (59:23-25) and the canonical class of principally polarized abelian
   schemes (59:26-28).

**H. Geometric class field theory in all degrees (43:24-35, 43:80; SA19-1, SA19-6; Lead SA19 H4).** Let k be
algebraically closed of characteristic p > 0, C a smooth curve over k with function field K, and J_{K/k} the pro-system
of generalized Jacobians. In Serre's category of commutative proalgebraic groups (or on the perfect étale site of k),
prove or refute that Ext^i(J_{K/k}, G) = 0 for every i ≥ 2 and every commutative algebraic group G over k. That would
make H^*(K, G) = Ext^*(J_{K/k}, G) in all degrees, as he boxes it on 43:80. Settle the case G = G_a first, where the
question lies.

**I. The endomorphism algebra of the residual complex (43:45-69; SA19-5; Lead SA19 H3).** Let A be a regular local ring
essentially of finite type over a field, and K^• its residual complex. Let 𝒜^* be his completed graded algebra on
𝒜^0 = ∏_x Ô_x and one element θ of degree 1, with θ² = 0 and π_{x'} θ π_x = 0 unless x' is an immediate specialization
of x, completed as on 43:65-66. Prove or refute that 𝒜^* → End^*_A(K^•) is an isomorphism of graded topological
algebras ("𝒜 libre pour ces propriétés"). Degree 0 and dimension 1 hold (c43_c44 §3.8-3.9). Settle dimension 2, degree
2, for A = k[[s, t]] first.

**J. The programme of 1964 (44:2-9; SA19-14 = SA18-14; Lead SA19 H5).**
1. Sort his seven theorems of 44:2-6 into proved (with the source), false (with a counterexample) and open (with the
   strongest reduction), and prove or refute each open one.
2. For a smooth projective threefold X over an algebraically closed field of characteristic p, with Ab^2(X) the
   algebraic representative of algebraically trivial codimension-2 cycles:
   - prove or refute that the intersection of cycles induces a canonical isomorphism Ab^2(X) → Ab^2(X)^∨ (his Th. 3
     with n = 3, i = 2);
   - prove or refute that, up to the sign of his Th. 5, this isomorphism is a polarization (Th. 4 with m = 2, and the
     positivity of D = r_*(p^*z·q^*z) in the letter to Serre of 12.8.1964).

**K. Statement of results.** Every result of Parts A-J and every settled Lead, numbered, with its status. For each
statement of his that you prove or refute, give his statement in French with the page, then the correct statement.

## Rules of proof (they bind every statement you deliver)

Known results (published papers, books, the standard literature) are cited with exact locators (paper, section, theorem number, page) and are not re-proved. The exception is a short proof of a form the source does not state. Every new result of yours is proved in full.

1. State the actual claim with all its data:
   - the field (perfect or not, its characteristic) and the base (noetherian, normal, regular, excellent, henselian or
     complete);
   - the dimension, and whether X is projective or only proper;
   - whether a divisor is Weil or Cartier;
   - whether Pic means the group, the functor, the étale sheaf or the scheme, and in which topology;
   - whether a statement holds up to isomorphism or up to a p-group.

   Do not replace the claim by a convenient special case. If you prove a special case, name it as one and keep the
   general statement on your list.
2. Type every map you introduce: source, target, the category in which it is a morphism, and each extra property you use
   (a morphism of group schemes, of algebraic spaces, of torsors, of proalgebraic groups; over which base). Compositions
   must type-check.
3. Every reduction ("we may assume", "after an étale extension", "pass to the henselization", "replace S by a trait")
   comes with a proof that the property needed transfers in the direction needed.
4. Conventions are named and kept:
   - Pic^0, Pic^τ and NS;
   - the dual abelian scheme and the sign of A ≅ A^∨∨;
   - Serre duality and its trace;
   - Cartier duality;
   - his indexing of the Leray and hypercohomology spectral sequences.
5. Check the edge cases in scope: p = 2 and p = 3; n = 3 against n ≥ 4; non-reduced, non-normal and non-excellent
   bases; disconnected fibres; supersingular, non-ordinary and ordinary abelian varieties.
6. A counterexample is given completely and, when finite or computable, checked by a program whose code and output you
   attach. One verified counterexample refutes the statement: say "false". An invalid proof alone shows a gap, not
   falsity; keep the two apart.
7. No authority. The transcriptions, the Pro notes, the Codex web notes, the readings, R1-R10 and the Leads (inferences
   by Claude, Anthropic) are all to be checked where used; the Leads in full. If one is wrong, say so plainly and show
   where.
8. What is not yet settled stays on the page as an exact statement, with what you tried and the step that fails, and you
   go on attacking it; it never finishes an item. Never write it up as proved, and never drop it.
9. Before calling anything new, search the literature and say what you searched. Cite exact theorem numbers. Never
   invent a reference; mark each entry of the bibliography opened or not opened. The literature to search first:
   - SGA 2 XI-XIII;
   - Hartshorne, Ample Subvarieties of Algebraic Varieties (LNM 156);
   - Bhatt and de Jong on Lefschetz for local Picard groups;
   - Raynaud (1978) and Lauritzen-Rao (1997) on Kodaira vanishing;
   - Kleiman, "The Picard scheme" (2005);
   - Raynaud, Publ. IHES 38 (1970);
   - Artin, Publ. IHES 36 (1969);
   - Grothendieck-Murre, LNM 208;
   - Serre, Groupes algébriques et corps de classes, and "Groupes proalgébriques";
   - Breen on the perfect site;
   - Yekutieli, Astérisque 208;
   - Mumford, "On the equations defining abelian varieties I";
   - Moret-Bailly, Astérisque 129;
   - Murre (LNM 1124), and Achter, Casalaina-Martin and Vial on algebraic representatives;
   - SGA 7 VII-IX.

   These locators are cited from memory and are unverified: open each before you rely on it.

**Check events.** For every statement, record its check events in `CHECK_EVENTS.tsv`, one row per event: statement id, date, who (model, effort, run), type (targeted proof check / independent re-proof / computation or formal certificate / used and rechecked in this run / carried as background without fault found / refuted, with the refined statement's id), outcome. This covers the statements of this run and every earlier statement you check, use or refute here. Give each event the type of what actually happened, neither more nor less. `CHECK_EVENTS.tsv` goes into every checkpoint and into the final ZIP.

## What to deliver

One ZIP containing:
- `RESEARCH_SA14_SA19_paper.tex` and its PDF (LuaLaTeX, compiles cleanly): the mathematics in the order of the Parts, every
  statement numbered and labelled Proved / Proved under stated hypotheses (with whether they hold where the statement is
  used) / Refuted (with the counterexample and the corrected statement) / Known (with citation), with complete proofs;
  English, first person plural; his statements quoted in French with the page.
- `RESEARCH_SA14_SA19_results.csv`: one row per numbered statement:
  `id, statement, status, where_proved, depends_on, manuscript_pages_settled, notes`.
- `RESEARCH_SA14_SA19_references.bib`: each entry marked opened / not opened.
- `RESEARCH_SA14_SA19_report.md`: the outcome table first (one line per item of the Parts and per Lead: proved or refuted, with
  the statement number); then what you read, what you computed (every computation with its scope, inputs, run time and
  output files), and every correction to R1-R10, to the Leads, to the readings and to the transcriptions, with the page.
- `CHECK_EVENTS.tsv` and `PROGRESS_LEDGER.md`.
- `code/`: every program you ran, with its output.

The work is AI-produced by GPT-6 Astra (OpenAI, ChatGPT Pro mode); credit it so, attribute nothing to any person, and
claim no priority: where a result is known, cite it; where you did not find it, say what you searched. Remarks taken from
Michel Hua's project are credited to it.

This task is long by design. Work through all parts completely; do not stop at an outline, a sample or a plan, and do not ask whether to continue. Take the time the work needs. Write the files from the start and extend them as you go, so that an interruption loses little.

**If the execution environment fails.** A failed or unavailable environment does not end the task. Retry at intervals
for as long as this session lasts, without writing recovery text into the chat. When the environment is back, restore
your work from your newest checkpoint and the earlier checkpoints its file list names, redo what you had done after
that checkpoint, and continue to the end. Do not write files out in this chat instead: the work reaches us only
through checkpoint ZIPs and the final ZIP.
**Typesetting check.** Every PDF you deliver is published as it is. Before you deliver one, read its build log: no overfull box may stick out by more than 2pt, whether a diagram, a display or a line of text. Fix each one in the source (scale or split a wide diagram, break a wide display, let a line break) and compile again. Then render pages to images and look at them: every page that had an overflow, and a sample spread over the document. Give the counts before and after in the report.

**Checkpoints.** Save a checkpoint ZIP to the Library once every 45 minutes of work, each under a new name, `RESEARCH_SA14_SA19_checkpoint_<NN>.zip` with `NN` counting up; never overwrite, rename or delete an earlier checkpoint. If the workspace comes back empty, restore it from your checkpoints (the newest first, then the earlier ones its file list names) and from this conversation before you continue. The final ZIP holds every deliverable in its current version and every file of yours that is in no checkpoint whose save you saw succeed; its file list names the checkpoint that holds each other file. A file or passage dropped from the work is listed in the report with the reason (superseded by which file, or wrong).
Save checkpoints once every 45 minutes and at no other time: none after a page, part, section, cote, folder, chapter or reader. A checkpoint is one ZIP holding every deliverable in its current version (paper, sections, results table, report, notes, scripts) and every other file of yours that is new or changed since your last checkpoint whose save you saw succeed, with a file list that names, for each file left out because it is unchanged, the checkpoint that holds it. Leave out the attached files themselves, the scans and sources you were given: we have them. Leave out earlier checkpoints, archives of earlier versions, and rendered page images (keep only an image that shows a problem the report discusses); we keep every checkpoint you save. It is never a JSON file, a recovery file, a summary, or an export of the newest pages only. Each checkpoint zip holds the current deliverables and documentation; earlier checkpoints are not copied into it. The checkpoints are what keeps the work if this session dies: work that is in no checkpoint is lost. Keep every checkpoint ZIP, and the final ZIP, under 500 MB. The Library refuses a file larger than 512 MiB (536,870,912 bytes), and a checkpoint it refuses is lost: one of our runs lost a checkpoint that way. If one would be larger, save it as several ZIPs of under 500 MB each, `RESEARCH_SA14_SA19_checkpoint_<NN>_part<k>.zip`, the file list in the first part.
