# SA25 — Autour de *Pursuing Stacks*, part 1

## Scope, evidence and outcome

This dossier consolidates the 374 entries of the supplied `NOTES_INDEX.tsv` for **Montpellier cote 105, package MPL_105**. It is a study of the supplied diplomatic transcription and its research notes, dated **19 November 2026**. It is not a new transcription from images. All 48 retained scan fragments, every indexed note entry, and the supplied doubts were read. The section readers also read the complete transcription to check statements of absence; the coordinating reader independently read the complete text and reconciled their findings. The reading logs preserve that work.

The material has two principal mathematical sequences. The first develops lifting classes, interval generators, recognition of a model structure with a prescribed class of weak equivalences, and a transfinite factorization construction. The second uses a category covered by two opens, replaces it by a category over a three-object fork, calculates a coherent cohomology square, and seeks strengthened excision and cube axioms. The connecting issue is how much information is supplied by weak equivalences alone, and what additional lifting, size, coefficient or exactness hypotheses are needed.

The consolidation confirms a substantial core of formal arguments. It also separates several stronger proposals from those arguments. The unrestricted interval-only recognition recipe fails even in **Set**; arbitrary directed colimits of maps in a left lifting class need not remain in that class; an arbitrary coefficient on a replacement category cannot be transported merely because its comparison map is a weak equivalence; and the strengthened reverse excision/cube principles fail for ordinary weak homotopy equivalences. These negative checks do not invalidate the corresponding conditional theorems. In particular, continuous ordinal lifting closure remains valid, correctly transported coefficients give the intended cohomology square, and the questioned third cube implication is valid in a coherent stable setting. Full proofs and the limited roles of the finite certificates are recorded separately.

The three evidence layers are kept apart throughout:

1. **Manuscript evidence:** the supplied transcription, including deletions, insertions, uncertain readings, changes of formulation and explicit withdrawals.
2. **Literature evidence:** opened works, with exact theorem or paragraph locators, hypotheses, and bibliographic verification. A source that gives a related theorem is not treated as settling a stronger or undefined statement.
3. **This run's work:** modern reconstructions, proof checks, counterexamples, consolidation decisions and suggested future tasks. These are labelled as such. No claim of novelty is made for a counterexample merely because its exact prior publication was not located.

### What is, and is not, covered by the archive inventory

`TOPIC.md` lists fifteen cotes: 103–109 and 111–118. The specific part-1 instruction limits entry consolidation to cote 105. `SA25_folder_coverage.tsv` accounts for every listed folder, with its supplied catalogue metadata and transcription counts. Only 105 has a transcription in this attachment. The other fourteen are marked as other-part material; their claims have not been invented or silently incorporated. In particular, the separate questions about cotes 115 and117–118 remain cross-folder leads.

The catalogue assigns 52 pages to cote 105; the supplied transcription contains 48 scan markers labelled 2–53, with 9,24,29 and 42 absent. These are different counts. Neither the number 52 nor the span 2–53 is a count of retained mathematical pages. There is no second-pass folder, Codex transcription, or scan image in this part. The Pro transcription and doubts are therefore the operative witnesses, as the instructions permit. Absence of a second pass is not treated as a missing research stage.

All `line` and `lines` fields mean **one-based physical lines of the supplied 1,895-line `MPL_105_transcription.tex`**, not lines of ink or reconstructed manuscript lineation. Scan labels are those in its `\scanpage` markers. Original page numbers and lower foliation are described separately. Source hashes are in `source_manifest.json`; the attached source files themselves are not duplicated in this ZIP.

## The manuscript in its own order

### 1. The preliminary lifting tests and the cancelled path sheet

The first mathematical leaf, scan 2, proposes lifting criteria for asphericity and for proper, smooth and perfect behaviour. Its sphere-like family, the cone directions, and some immersion qualifiers are insufficiently determined by the transcription. The claims map consequently splits the assertions instead of converting them into one modern theorem. CL-SA25-001–005 record exactly what can be read and which comparisons are conditional. Modern finite categorical lifting tests exist, but matching a broad topic is not enough to identify the displayed generators.

Scan3 is a wholly cancelled discussion of an endpoint map `Ch(C)→C×C`. It distinguishes categorical fibrations and opfibrations, cohomological properness and smoothness, and an intended intrinsic `W∞`-fibration property. The path objects and their morphisms are not defined on the retained sheet. It would therefore be unsound to replace them with the path convention of an unrelated theorem. CL-SA25-006–010 preserve both the deletion and the different questions. The explicitly defined constructions in the checked *Dérivateurs* V, Maltsiniotis and Shoikhet sources are useful comparisons, with different conventions and hypotheses; they are not a recovered definition of this `Ch(C)`.

This distinction matters for the many later project comparisons in the notes. An undefined path symbol on one cancelled page does not establish full-path enrichment, a hammock comparison, an endpoint-fibre theorem, or equality of an intrinsic fibration class with a model-category RLP class. The relevant entries remain traceable through SA25-23 and the separate comparison items.

### 2. Two lifting pairs and the class they generate

Scans5–7 introduce nested lifting data, with `(TC,F)` and `(C,TF)` mutually orthogonal and `TC⊂C`. The generated candidate weak-equivalence class is

\[
\widetilde W=\{p i\mid i\in TC,\ p\in TF\}.
\]

The identities `C∩W̃=TC` and `F∩W̃=TF` follow from the arrow-retract argument (CL-SA25-013). They do not require first proving two-out-of-three for `W̃`. Conversely, their truth does not make `W̃` a weak-equivalence class or supply the two factorizations. The notes' various uses of “saturated” must therefore be kept apart: closure under lifting orthogonals, two-out-of-three, split-retraction conditions, closure under arbitrary arrow retracts, and detection by localization are different assertions.

Scans7–14 then calculate tensor/internal-Hom lifting relations. The useful modern language is the pushout product and its corner-Hom adjoint, but the reconstruction retains the source's actual classes. Ordinary product stability is weaker than the mixed pushout-product condition. CL-SA25-014–019 give the individual statements, including the canonical identity

\[
i'\mathbin{\square}h(i_0,I,\epsilon)
\cong h(i'\mathbin{\square}i_0,I,\epsilon).
\]

For monomorphisms in a topos, both sides are the same subobject union in the threefold product. The formal proof uses its universal property. The finite Boolean/set calculation is an illustration and an error check, not a proof for every topos. The extension from the generator identity to the full left lifting class is written out in the proof record.

### 3. Interval generators, prescribed weak equivalences and recognition

The horns have the form

\[
(A\times I)\cup(B\times\{\epsilon\})\longrightarrow B\times I,
\qquad A\hookrightarrow B.
\]

The interval is required to be universally weakly equivalent to the terminal object, in the relevant sense. Scans14–18 admit factorization temporarily and try to prove `W̃⊂W`. The Lawvere object is used to control `TF`; pushouts, transfinite cell attachment and retracts control `TC`. These are separate steps. The source's five closure conditions on `W` do not themselves manufacture a cellular factorization for an arbitrary proper class of intervals.

There is also a smaller logical gap worth preserving. The split-deformation-retraction argument for `TF⊂W` is secure. The sentence that *every* Lawvere-homotopy equivalence lies in `W`, under only the initial weak saturation assumptions, requires more than simply noting that both inverse composites are homotopic to identities. CL-SA25-024 records the proved refinement with cyclic or strong saturation. The checked *Pursuing Stacks* §§48,54 explicitly distinguish the stronger saturation used for that conclusion. No unproved strictification has been inserted into this page.

Scan20 isolates the reverse inclusion. With the admitted weak factorization systems and `W̃⊂W`, the following are equivalent: `W⊂W̃`, `F∩W⊂TF`, and `C∩W⊂TC` (CL-SA25-029). The apparently weaker RLP condition in line 674 can be repaired by the standing factorization and a retract argument (CL-SA25-030). Its wording is therefore not evidence, by itself, of a transcription error.

The main negative check is more decisive. In **Set**, take prescribed `W` to be all maps and allow every pointed interval. A horn has empty source only when its target is empty. Consequently `∅→1` has the right lifting property against every horn, yet does not lift on the left against itself. Thus it is in `C∩W` and not in `TC`. In fact, with ordinary choice,

\[
F=\{\text{surjections}\}\cup\{\text{maps with empty domain}\},
\]

and `TC` consists of injections with nonempty domain, together with the identity of the empty set. Both factorization requirements hold. The resulting `W̃` is precisely the class of maps preserving emptiness, strictly smaller than the prescribed maximal `W`. CL-SA25-021 and `work/a/proof_checks.md` check every hypothesis. The independent review is in `work/root_proof_checks.md`.

This resolves the unrestricted recipe negatively without contradicting accessible-localizer model existence. Suitable extra anodyne seeds or completeness conditions matter. In this example adding `∅→1` supplies the missing seed. The checked modern existence results are located in Cisinski2002 Theorem 3.9, Cisinski2006 Theorem 1.4.3, and the related test-category/diagram results listed in CL-SA25-032–033. They are not the assertion that any interval-only family recovers an arbitrary prescribed `W`.

### 4. Quillen pairs, saturation and properness

Scans22–32 return to the abstract recognition problem. “Quillen pair” here means a factorizing mutually lifting pair, hence a weak factorization system; it does not mean an adjunction between two model categories. The retract criterion and recognition proof are mathematically sound with their stated assumptions (CL-SA25-102,110). The category must additionally have the finite limits and colimits, or bicompleteness, required by the chosen convention for a model category.

The cancelled scan 27 asks whether weak cyclic composites force their factors to be weak. The distinction is real. In the one-object category with endomorphism monoid `(N,+)`, take `W` to be the even integers. Isomorphisms belong to `W`; two-out-of-three holds; arrow retracts are trivial, so retract closure holds; and the special split condition holds. Nevertheless `1+1=2` is weak in both cyclic orders while neither factor is. The full unbounded argument, not just a finite parity table, is in `work/b/proofs.md`. Strong saturation gives a correct repair.

By contrast, Quillen's closed model-category saturation theorem is already explicitly cited by the author. The checked historical locators are I§5 Propositions 1–2, with finite-limit/colimit hypotheses retained. The manuscript's uncertainty about a statement from bare arrow data without those constructions is a separate problem, MP-SA25-37. The recorded search establishes qualified results; it does not establish that the completely bare formulation is either solved or an open problem of current mathematics.

Properness is another additional condition, emphasized by the source rather than derived from RLP notation. A chosen fibration class need not automatically make weak equivalences survive pullback. The exact accessible-topos criterion checked in Cisinski2002 Theorem 4.8 is recorded with its generator, base-map and fibrant-target quantifiers. The earlier context's intrinsic “fine” classes or general cohomological labels do not supply those hypotheses. See CL-SA25-111 and the merged properness problem.

### 5. All-squares attachment and the limit-stage boundary

Scans34–40 construct the first stage by attaching one cell for **each commutative lifting square**, not merely one for each generator. The author corrects the initial cardinal bound on the same page. The correct stagewise estimate is

\[
\sum_{g:A_g\to B_g}|\operatorname{Hom}(A_g,X)|
|\operatorname{Hom}(B_g,Y)|,
\]

with the displayed product-supremum estimate as an upper bound. It must not be reused unchanged after `X` grows. The finite count in the bundle demonstrates the multiplicity issue; the cardinal reasoning is checked separately in CL-SA25-112.

Under a set of generators, the required colimits, and domain smallness, the construction gives the expected factorization. A sufficiently long ordinal permits a generating source map into its colimit to factor through a stage; the required cell is attached at the next stage. Only smallness of the source is needed for this argument. The source's common source-and-target accessibility assumption is sufficient but stronger. In the finitely presentable case an `ω`-sequence suffices. Ordinary functoriality follows by sending every lifting square along a map of arrows and using chosen colimits (CL-SA25-113–115). It is not, by itself, an algebraic weak factorization system or an all-shapes rectification theorem.

Two qualifications must remain visible. First, a containing cellular class must include zero-length composites/identities; this is automatic for a lifting class but is a convention to state for an arbitrary intermediate `Φ`. Second, the unfinished Zorn argument on scan 38 is stronger than the valid ordinal lemma on40.

For the latter, work in abelian groups and let `Φ` be the maps with LLP against all surjections: split monomorphisms with free cokernel. The finite-rank pure subgroups of `P=∏Z` form a directed poset with binary joins. Each is a finite-rank direct summand; every transition lies in `Φ`; their colimit is `P`; but `0→P` is not in `Φ` because `P` is not free. The proof verifies finite generation, purity, retractions, directedness and the colimit. It uses the nonfreeness theorem checked in Schroer2007; it is not a conclusion from a bounded computer search. CL-SA25-204 is therefore separated from the valid continuous ordinal closure CL-SA25-201.

Finally, the author explicitly wants to remove the small-generating-family premise. The checked class-sized small-object theorem of Chorny gives a conditional extension with uniform smallness and solution-map requirements. It does not justify removing every size condition. The problem index preserves this difference.

### 6. Two opens, a fork and a coherent cohomology square

The French sequence begins with a cancelled comparison involving an incompletely specified `q`, followed by the heading about `W7`, `W(7bis)` and `W=W_D`. The cancelled square's two-out-of-three step can be checked, but the missing barred construction cannot be recovered from it (CL-SA25-228).

Two sieve subcategories `U,V` covering `X` give a functor to the fork `Ψ=(0→a,0→b)` inside `[1]²`. The strict side fibres are the differences of the opens, whereas the comma fibres are `U` and `V`. This is why the later warning that the strict fibres are disjoint matters. A Grothendieck construction on the comma fibres produces `barX→Ψ`, with fibres `U∩V,U,V`, a comparison `α:X→barX`, and a forgetful retraction `p`. The explicit adjunction `α⊣p` verifies the absolute nerve homotopy equivalence (CL-SA25-205–207).

In the manuscript's presheaf variance, right Kan extension along the opfibration is computed on the strict fibres of this replacement. A further right Kan extension to the square shape supplies a **coherent cartesian square**. Its missing value is total cohomology. This is a statement about an object of the diagram category `D([1]²)`, not just four objects and arrows in `D(e)`.

The coefficient enlargement must be read carefully. Take `X=e`, both opens equal to `e`, and hence `barX=Ψ`, with `α` selecting0. For the coherent presheaf diagram `2→1←2`, the total limit has 4 elements while restriction to0 has 1. Thus `α∈W∞` does not imply cohomology invariance for every coefficient on `barX`. A coefficient already on `X` can instead be transported as `p*η`, which gives the required comparison. This exact distinction is CL-SA25-209; the bar over `X` and the coefficient clause remain scan-reading questions.

The collapse `ρ` on scan 51 has a similar distinction. The isomorphism-leg lemma is correct by the pointwise Kan calculation. The unconditional claim that its right image is computed on strict fibres is not: the recorded finite example gives 4 versus 2. The doubtful word “proper” must be checked on the ink. These are separate claims, CL-SA25-217–218, so a defect in the stated justification does not erase the valid lemma.

### 7. Strengthened excision, the Hot withdrawal and the cube question

Cartesianity gives one direction of the opposite-edge isomorphism test. Cocartesianness gives the other. The provisional `Der6` and its dual ask for this additional exactness; scan 50 then considers requiring every coherent square to be cartesian exactly when it is cocartesian, and scan 51 asks for the same condition in every shift `D_I`.

The modern stable refinement has precise hypotheses. A pointed derivator with the square property is stable, and its shifts retain stability. The source does not state pointedness. Even constant coefficients in spaces give counterexamples to the unrestricted provisional forms: the finite graph `K_{2,2}` appears as a homotopy pushout with nonzero first homology. The proofs check the coefficient and (op)fibration requirements, rather than appealing only to the general slogan that spaces are unstable.

Scan52 explicitly withdraws the universal Hot-square claim and its component criterion with “Complètement faux.” Both clauses are separately checked in CL-SA25-219–220. The marginal suggestion that a bicartesian square ending in a point requires one adjacent object to be contractible is also too strong. This run uses a finite presentation complex

\[
K=\langle a,b\mid a^3b^{-5},\ b^5(ab)^{-2}\rangle
\]

whose cellular boundary matrix has determinant −1, but whose fundamental group has a nontrivial permutation quotient. Thus `K` is acyclic and noncontractible. Its join with itself is contractible. The product square with corners `K×K,K,K,*` is therefore bicartesian while neither adjacent object is contractible. The code certifies the integer matrix and permutation relations; the topological conclusions are proved separately using the stated CW hypotheses.

The third cube implication deserves a positive conclusion. For a coherent morphism of bicartesian squares in a stable setting, the Mayer–Vietoris triangle has middle term `X_a⊕X_b`. If the maps at the initial and terminal corners are isomorphisms, the block-diagonal middle map is an isomorphism, hence each side map is. This checks CL-SA25-222 under explicit stable and coherence hypotheses. It is not a formal consequence of the word “bicartesian” in every homotopy theory.

The final `W7bis/W8bis` and smooth/proper variants are **proposed extra axioms on `W`**. They are not all claimed as established facts about every localizer. For `W∞`, take a small category with nerve of the homotopy type of the acyclic noncontractible `K`, and form its double cone. The two branches and total are weakly contractible but the central category is not. This disproves the reverse edge implication and the corresponding cube implication, including the smooth fibred version whose hypotheses are explicitly checked. A coefficient theory sending the construction to coherent bicartesian squares supplies a sufficient stable refinement; no classification of all such `W` is asserted.

## What the earlier notes got right and what required correction

The strongest earlier observations survive: the interval-generator recognition gap is real; factorization and properness are different tasks; the source repeatedly distinguishes coherent diagrams from their skeletal images; coefficient scope changes; the reverse excision implication is unfinished; and the unstable Hot paragraph is expressly withdrawn. The notes also correctly say that many external project results have no form on these pages.

The main correction to an external citation is **MPL_105#114**. Cisinski2006 Corollary 4.2.22 concerns filtered-colimit closure of fundamental localizers. It is not the accessibility/model-existence equivalence attributed to it. The relevant model-existence locator is Theorem 1.4.3, with its precise accessibility hypothesis. This is a citation correction, not a change to Grothendieck's ink.

Further corrections prevent the same pattern at a conceptual level. A general existence theorem does not identify a particular proposed generator family. Failure of reverse excision for `W∞` does not prove that every localizer satisfying it is exactly a spectral-homology localizer. A path construction from another work does not define the cancelled `Ch(C)`. An exceptional duality hope does not construct six operations, dualizing weights, a correspondence enhancement, or an ambidexterity classification. The project comparisons retain their exact source IDs and reported statuses in their own table; those statuses are never treated as checks performed here.

There is no basis in this attachment for dating the autograph mathematics to 1983. The printed support contains 1982 dates, which date the support's printing. The catalogue says undated. The English pages, French page numbers, lower foliation, catalogue count and printer page numbers are distinct systems. The FORTRAN/GUTS listing and member-count tables are reused support, not evidence of a mathematical finite-category search by the author.

## Literature, links and historical limits

The literature audit used the named discovery channels: arXiv, MathOverflow, Numdam, author bibliographies and edited original works, EGA/SGA, and attempts to access zbMATH Open. The latter returned 403 for the tested records; Numdam supplied bibliographic identifiers, but no unseen zbMATH review is described as read. The EGAIV metadata page opened, while its large PDF did not; no exact EGA homotopical theorem is manufactured from that search. Searches for the reused prose page did not establish its source in *Récoltes et Semailles* or elsewhere.

Each claim has a recorded fate search and references. For F-class fragments, the result is often a precise statement of what remains unidentifiable. For C-class proposals, the result distinguishes a settled conditional version from an unproved, false, or undefined stronger version. A negative search is bounded evidence, never proof that no literature exists. The problem index likewise separates uncertainty in this source from a claim of current mathematical openness.

The checked author-work links are especially useful. SGA4 I§§9.1–9.3 explains the historical accessibility language. *Pursuing Stacks* supplies the Lawvere-interval discussion, the stronger saturation distinction, integration/coherent-diagram passages, and the distinction between ordinary homological Kan extension and a hoped-for exceptional duality. *Dérivateurs* XIII, XV and XIX give exact counterparts to the lifting and factorization constructions. XII§5 repeats the strengthened square/cube axioms and conditional total-category statements. Its manuscript-p78 Theorem 2 also asserts the full cube axiom for `W∞` with a verification still to be written; the same double-cone example checks that assertion negatively, using its two closed cone subcategories or the opposite category to obtain two opens. This is recorded as a checked source comparison, not as an additional cote 105 claim.

Dates of writing, circulation, publication and electronic edition are not conflated. *Pursuing Stacks* is 1983 work, not a 2021 discovery because its arXiv transcription appeared then. The editors date *Dérivateurs* to October 1990–the first half of 1991; individual electronic chapter editions have later dates. Quillen's book is 1967; the erroneous 1965 title-page date in the consulted modernized retyping is not used as a circulation date. Where a first-circulation date was not established, the bibliography and claim record say so. The undated cote 105 handwriting does not license a claim that any matching author passage is chronologically later than it.

`SA25_links.tsv` contains the full link register; `SA25_project_links.tsv` isolates project leads. Confirmed public-work matches have both endpoints checked. The private registers named in the notes were not supplied and exact-title retrieval found no matches; their target contents remain unverified. Public original-work counterparts were checked independently where possible. A link to a private companion's editorial claim is not marked verified merely because an original chapter has a related passage. No cross-folder mathematical comparison is certified from a catalogue title alone.

## How to use the dossier

Start with `SA25_entries.tsv` to trace any of the 374 stable entry IDs to its consolidated item. `SA25_items.json` preserves the individual evidence of merged comparisons, including the original components when a cross-reader merge would otherwise hide differences. An item check of “agrees” means that the note accurately describes the supplied text or its absence; it does **not** certify a theorem reported from an unavailable project.

Use `SA25_claims.json` for mathematical statements and their changing status, and `SA25_problems.json` for the author's open steps with contemporary qualified formulations. `SA25_readings.tsv` is an unresolved ink agenda: alternatives are not corrections. `CHECK_EVENTS.tsv` distinguishes text alignment, targeted proof checks, independent proofs, computations, background use and refutations. The proof files explain the mathematical work; finite computation outputs state what they do and do not certify.

The ranked tasks in `SA25_directions.md` cite the items, claims and problems from which they arise. They specify a first concrete step and a realistic one-run stopping point. They are not developed further in this dossier. The immediate editorial priorities are the undefined tests/path convention, the coefficient bar and quantifier, the doubtful properness word, and the final fork/index readings. The most productive mathematical follow-ups concern precise generator data and stable coefficient detection, rather than re-proving already established model-category machinery.

## Counts and completion audit

<!-- COUNTS_START -->
The final register contains **374 entries, 252 consolidated items, 82 claim records, 30 merged problems, 64 unresolved reading alarms and 8 ranked directions**. Every indexed entry has a read verdict; every claim and problem has a recorded search trail.

| Coverage | Count |
|---|---:|
| Supplied packages consolidated | 1 |
| Cotes accounted for in the topic inventory | 15 |
| Cotes whose mathematical text is supplied in this part | 1 |
| Retained scan fragments read | 48 |
| Physical lines in the transcription | 1,895 |
| Source entries | 374 |
| Consolidated items | 252 |
| Explicit cross-reader item merges | 45 |

### Entry verdicts

| Verdict | Entries |
|---|---:|
| kept | 245 |
| merged | 122 |
| corrected | 7 |
| withdrawn | 0 |
| rests on a misreading | 0 |

“Withdrawn in the same text” is a source-status category, represented among the items and claims. A note accurately recording that withdrawal is kept or merged; it need not itself receive a withdrawn-note verdict. No ink misreading is declared proved without images.

### Item kinds and text checks

| Item kind | Items |
|---|---:|
| conjecture | 5 |
| idea of the earlier run | 102 |
| other | 85 |
| reading question | 9 |
| self-flagged step | 21 |
| title, date or page count | 13 |
| unproved claim | 7 |
| unpursued implication | 9 |
| withdrawn in the same text | 1 |

| Text comparison | Items |
|---|---:|
| agrees | 245 |
| overstates | 7 |
| understates | 0 |
| misreads | 0 |
| not on the page | 0 |

### Claims by literature class and manuscript status

| Literature class | Meaning | Records |
|---|---|---:|
| A | Matched in his own demonstrably later published work | 0 |
| B | Established development by others | 17 |
| C | Qualified or partial development; unrestricted version distinguished | 21 |
| D | Not developed within the defined search scope | 0 |
| E | Standard antecedent / already established in the relevant historical framework | 31 |
| F | Exact source claim not identifiable | 13 |

No A-class assignment is inferred merely from a matching *Dérivateurs* passage: the cote 105 handwriting is undated and the exact mathematical hypotheses may differ. No D-class assignment is made merely because a search found no exact match. B/E dates describe the precise checked antecedent or exposition, not an unsupported priority claim.

| Principal status on the pages | Records |
|---|---:|
| stated without proof | 34 |
| open on the pages | 20 |
| proof sketched | 17 |
| proved there | 8 |
| corrected by himself later | 3 |

These principal categories summarize the occurrence records; the full `status_on_pages` fields retain cancellations, later continuations and mixed subclaims. They are distinct from this run’s mathematical evaluation. Fourteen claim records point to ten explicit refinement records, including the convention-dependent identity issue. Refutations of proposed axioms are scoped to the unrestricted spaces or `W∞` interpretations; they do not declare every theory satisfying an extra axiom inconsistent.

### Problems, readings, links and verification

| Register | Count |
|---|---:|
| Merged problems | 30 |
| Reading alarms, all unresolved on ink | 64 |
| Ranked follow-up tasks | 8 |
| Checked public-work passage links | 17 |
| Checked internal cote 105 passage links | 4 |
| Cross-part folder leads with unavailable mathematical target | 3 |
| Segregated project/provenance lead rows | 382 |
| All link rows | 406 |
| Bibliographic keys | 39 |
| Opened bibliographic sources/URLs | 37 |
| Explicitly unopened historical leads | 2 |
| Check-event rows | 553 |
| Distinct searched claims and merged problems | 112 |

The endpoint limitation is substantive: only the 17 public-work links and 4 internal passage links have both mathematical endpoints checked. The 3 other-part folder leads and the external project targets remain labelled unverified where their text is unavailable. The source endpoints and available target metadata were checked; no missing scan, companion, or register was reconstructed.

CL-SA25-117 is a transcription-only fragment with no indexed note isolating it; its empty item-link array is explicit, with exact scan/line evidence. No note relationship is invented.

The structural validation checks exact entry coverage, source hashes, item membership, required fields, identifiers, bibliography keys, search-action references and check-event coverage. Its success is not a mathematical proof; those checks are separately documented in the proof records and event registry.
<!-- COUNTS_END -->
