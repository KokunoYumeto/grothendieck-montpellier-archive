# Independent prompt-to-manuscript coverage audit

Audit date: 2026-11-19, approximately 12:59–13:06 UTC. Researcher: GPT-6 Astra (OpenAI, ChatGPT Pro mode), `part_c_algebra` independent review. This is a coverage and proof-scope audit of the **active** master and its included fragments, not a new proof of every result. The earlier detailed independent audits of C, A2 radii, A1 range, A3/A4, collars, B2 and B3 supply the deeper checks named below. No priority is claimed.

Inputs read: the full attached `upload/PROMPT(20261119-110314).md`; active `RESEARCH_SA22_paper.tex`; the current included A1–A7, B and C fragments; current source bibliographies; current report and progress ledger. The master includes `part_a567.tex`, which includes A5/A6/A7, and A1/A2 include their subsidiary comparison/range/collar fragments. `sections/unsettled.tex` is presently absent, so the master uses its generic live-status fallback. The report's B3 row is stale: the active B manuscript contains all 28 subjects and nine Pour mémoire blocks.

## Finding

No new unresolved mathematical proof step was found in this audit. This statement is limited to the actual proofs and explicitly stated interpretations in the manuscript. It does **not** upgrade unexamined original literature or claim that every broader interpretation of an undeveloped research programme has been proved. The remaining named-original-source requirements are materially broader than the three already prominent gates. Root has explicitly accepted that the prompt's `Sources (fetch them)` is a source-delivery obligation, even when an independent proof supplies the mathematics.

One small edge-case omission was sent to the A567 owner: A5 should explicitly state what degenerates in characteristic 2, which Rule 5 requires checking, even though both main theorems exclude it. In characteristic 2 the displayed six-set collapses to `{0,1,infinity}` and the displayed four transformations become only two. This is an omitted explanatory edge case, not a counterexample to the stated characteristic-not-2 theorem. The owner is handling its addition/certificate. A harmless typesetting error `^{,d}` in the two Kra polydisc expressions was sent to root; it should be `^d`.

Update13:14UTC: A567 has added and proved the characteristic2 degeneration, including the faithfulF4translation action with common fixedpointinfinity, and supplied its exact finite certificate. Independently read the new paragraph; this edge-case omission is closed. Knudsen–Mumford1976 original is now opened, with exact source-scope and printed-sign correction in `notes/part_c_required_originals.md`; Gabriel remains unopened. The source table below is retained as the dated audit snapshot rather than silently rewritten as if those later opens had already occurred.

## Compact coverage matrix

“Math complete” below means complete under the interpretation and hypotheses explicitly identified in that row; the final column preserves material limits. Named-source gates are listed separately.

| Prompt task | Active proof / counterexample | Mathematical coverage and qualification |
|---|---|---|
| A1(a), main `(0,4)` | A1-global-refutation; A1-graph-range | False for unrestricted tensors: `q=17` violates cap product bound 16. Corrected geodesic-cut range is exactly `0<abs(q)<16`. |
| A1(b), every stable type | A1-dimensions; A1-graph-range; A1-bordered-shadow-range; A1-bordered-shape-image | Graphwise positive Hessian, exact open convex logarithmic image, real tangent and fundamental-group isomorphisms; automorphisms and phases retained. Every positive-complexity type has a proper-image counterexample. |
| A1 definition choices | A1-nontoric-cut; A1-bordered-landing; A1-retained-discs; A1-cut-not-algebraic | Arbitrary embedded cuts need not induce toric seams. Literal external-only admissibility can fail to land. Joint caps or radius reconstruction repair it. Natural `(0,4)` cut-cover complex curve is not finite-type algebraic; this does not infer nonholomorphicity merely from real analyticity. |
| A1(c) | A1-first-order; A1-welding-plumbing; A1-kra-comparison; A1-wolpert-comparison; A1-hinich-counterexample; A1-Earle-Sipe-comparison | Coordinate-level comparison and local Hubbard–Koch universal charts are proved from opened sources. The alleged unrestricted global inverse is refuted. **Original Earle–Marden theorem-text requirement remains.** Earle–Sipe is not substituted under their name. |
| A2(a) | A2-schwarzian; A2-independence | False: cap second jet changes from `1/2` to `5/4` at fixed own boundary length. |
| A2(b) | A2b-regularity; A2b-energy; A2b-recession; A2b-image | Exact all-genus injectivity/image for a fixed pointed compactification: gradient of strictly convex potential; inequalities against every nonnegative Strebel weight; arbitrary active ends with fixed cusps. No numerical Hessian experiment is a premise. |
| A2(c) | A2-strebel-deficit; A2-cap-limit; A2-explicit-limits | All relative growth directions on fixed pointed compactification, including zero weights; active caps converge to weighted Strebel domains, inactive caps collapse. Koebe is the one-dominant-end limit, not every simultaneous growth limit. |
| A2(d) | A2-cusp-norm; A4-grafting | Canonical tangent norms; unrestricted Penner decorations interpreted in cusp covers; length-parametrized positive bundle and mixed zero strata. Embedded horocycles are not assumed at arbitrary decoration size. |
| A2(e) | A2-collar; A2-collar-general; A2-collar-shape; A2-collar-explicit | Exact nonlinear metric relation for arbitrary smooth collars, signed curvature and first variation; monotonicity for nonnegative outward curvature; blanket pointwise monotonicity refuted by completely explicit analytic collar. Independent full bound/sign audit in `part_a2_collar_secondary_audit.md`. |
| A3 | A3-boundary-chart (root addition), A3-welding, A3-rectifiable, A3-graph, A3-slit, A3-L5 | Correct QS sufficient existence, removable uniqueness, continuous-function Morera, common-exponent vertex chart, Jordan-arc/prime-end cutting, both 073 normalization readings. Bankwise QS alone is not asserted to imply tip compatibility. |
| A4 orange model | A4-orange-extremal; A4-orange-jets; A2-explicit-limits | Literal finite-length orange model false; exact annulus/extremal-length counterexample, second-jet dependence, equal-weight asymptotic orange domains. |
| A4 enlarged space/action | A4-grafting; A4-action | Marked bordered/cusped spaces, all-zero stratum, coordinatewise nonnegative action, fixed sets and deformation retraction; units free on positive strata only. |
| A5 theorem089 | A5-normalizer; A5-groupoid | Full groupoid equivalence in every algebraically closed characteristic not 2, including 3 and 5; torsor inverse and arrows checked. |
| A5 proposition086 | A5-six-points; A5-faces | Corrected characteristic not 2,5; complete characteristic-5 120-element stabilizer/five-Klein counterexample and finite certificate. Antipodal pairing restores uniqueness. |
| A5 moduli/L7 | A5-moduli | Quotient stack and coarse affine line distinguished; family descent and characteristic-3 invariants/inertia handled. Char2 explicit degeneration addition requested above. |
| A6(a):049(a) | A6-ordinary-counterexample; A6-graphic; A6-normal-kummer; A6-anabelian | Full reconstruction for **framed logarithmic** groups over finitely generated characteristic-zero fields; ordinary groups refuted. Component anabelian theorem, twist kernel and injective Kummer map are separate checked inputs. |
| A6(a):049(b),NB048 | A6-procyclic; A6-cyclotomic-detection; A6-three-classes | Bare invariant procyclic criterion and literal three classes refuted; maximal geometric inertia recovered from full action/finite covers. Smooth cyclotomic criterion has its explicit extra hypotheses. |
| A6(a):049(c) | A6-blowup; A6-SNC-existence; A6-log-specialization; A6-canonical-compactification | Exact sheet asks for a definition and specialization (`MPL_67_002-052_transcription.tex:1081`). A chosen SNC tangential-log definition exists in arbitrary dimension, with proved specialization. Reconstruction under ample log canonical hypothesis is conditional. No universal recovery of every compactification or universal ample smooth compactification is claimed. |
| A6(b) | A6-matrix-presentations; A6-four-punctures; A6-binary-S3; A6-projective-line; A6-birman; A6-presentation-types | Pure/distinguished-point/full groups separated; both superscript readings; explicit SL2/GL2 and binary quotient; Birman exceptions; pants/Lego action-groupoid interpretation; closed-surface involution theorem only in its stated scope. Arithmetic tower compatibility is not inferred from geometric simple connectivity. |
| A7 | A7-gluing-modules; A7-domain-counterexample; A7-PID-count; A7-real-classification; A7-ratio-j; A7-real-topology | Complete real classification, exact nonsplit count, topology and H1, all R5 corrections; stronger counterexample shows connected domain is insufficient for arbitrary eigensheaf invertibility. Independent lattice proof does not depend on unopened Alling–Greenleaf. |
| B1(a) | thm:B1a-betti; lem:B-basechange-num; thm:B1a-etale | Characteristic-zero theorem for all fields, with spreading/base-change directions and algebraic Lefschetz components. |
| B1(b) | prop:B1b-criterion; prop:B1b-gap; thm:B1b-abelian; prop:B1b-scope | Ancona alone supplies numerical positivity/infinitely many primes, not the all-prime inference requested from memory. Opened Broe2026 theorem closes all-prime result. General class is explicit positivity/decomposition criterion plus specialization and generically finite domination families, not an exhaustive classification of geometric fourfold types. |
| B1(c) | thm:B1c | Both doubtful tau/algebraic glyph readings refuted by completely specified generic quintic with skew lines; smoothness finite certificate and source incidence argument. |
| B2 first question | lem:B2-mumford; thm:B2-square | Explicit algebraically trivial divisor on E×E with nontrivial square, Mumford family-form contradiction and countable constructible rational-equivalence loci; all n handled. |
| B2 second question | prop:B2-kernel; thm:B2-square | Albanese-kernel question separately refuted; exact positive kernel/spanning description. All Bloch facts used are in opened official excerpt pp.3–11; no unseen full-book result assumed. |
| B3 all28 | all thm:B3-* in active part_b.tex | Every numbered subject appears, often in more than one block to cover abelian-p-primary/D-module/Artinian/coherent branches. Detailed independent audit in `part_b3_secondary_audit.md`; two degree/sign errors were found and corrected before this coverage pass. |
| B3 subject21 | thm:B3-21; thm:B3-fujiwara | Full modern proofs and deductions available; exact universal henselian quantifier and original noetherian completion scope distinguished. **Required direct derivation from opened Gabber/Fujiwara originals remains a source gate.** |
| B3 Pour mémoire | nine blocks at end of part_b.tex | Resolution/alterations, purity, regular base change, local duality/biduality, finiteness, affine dimension, Grauert, rigid geometry, SGA1962 questions all present with strongest stated scopes. No universal resolution or integral Chow pullback is asserted. |
| C1(a) | C-exp-log; C-filtered | Nilpotent ideal, all commutative Q-algebras, no Noetherian/finiteness assumptions; identity on associated graded is the correct hypothesis. |
| C1(b) | C-differential; C-other-autos | Exact automorphism order/diagonal-ideal test and conormal unipotence criterion; square-zero arbitrary GL and nonuniform locally nilpotent examples. “Differential operator” is not silently substituted for “differential algebra automorphism.” |
| C1(c) | C-intertwine | Pointwise finite exp/log for locally nilpotent u,v; no false claim that the induced Hom commutator is uniformly nilpotent. |
| C1(d) | C-functor-criterion; C-functor-counter; C-qcoh | Exact arbitrary-functor images/kernels, formal and ordinary cases distinguished; quasi-coherent classification, finite-generation sufficiency but not necessity. |
| C2(a) | C-K-counter; C-chain-true; C-K-replacement | False even for C4 full-cardinality chain system; all axioms and all finite products enumerated. Pairwise pretasse, not ConditionK for triples, is the universal implication. Spanning cone and union of individual cones distinguished. |
| C2(b) | C-literal-class; C-extension | Complete classification for the literal no-fullness axioms, finite and infinite discrete groups; sparse/vacuous possibilities stated. Two inequivalent exact C2 extensions verified. No strengthened unstated fullness problem claimed solved. |
| C2(c) | C-symmetry | Universal pretasse symmetry iff abelian, all discrete groups; explicit noncommuting witness and finite S3 tasse certificate. |

## Leads, all preserved

| Lead | Outcome and pointer |
|---|---|
| L1 | Proved: B1(a), classical. |
| L2 | Refuted: unrestricted global maps; repaired maps and local comparisons above. |
| L3 | Proved with correct decoration-bundle interpretation, not arbitrary embedded discs. |
| L4 | Corrected: relative growth direction matters; exact support region is not a box; cap dependence proved. |
| L5 | Proved for geodesic/toric or smooth-diffeomorphism seams; arbitrary smooth homeomorphism may fail QS, and arbitrary embedded cuts have separate A1 obstruction. |
| L6 | Precise framed-log reconstruction proved from opened later sources. Historical source-chain fetch obligations for Nakamura/Ihara–Nakamura still remain. |
| L7 | Stack/coarse statement corrected and proved, with base descent and small-characteristic qualifications. |
| L8 | Refuted by complete C4 counterexample; cyclic and Z literal existence follows from full group classification. |
| L9 | Full real lattice classification and all corrections proved independently; preview of Alling1981 supports terminology but not unseen formulas. |

## Named-source requirement, independent from mathematical validity

This inventory is a snapshot, not a claim that later retrieval work cannot change it. Entries marked “not found in current bib” were checked across all `sources/*.bib`; it does not claim no source exists elsewhere on the web.

| Requested work/category | Actual status at audit | Required follow-up / mathematical role |
|---|---|---|
| Earle–Marden plumbing original | Not opened | Explicit A1(c) direct-source comparison remains. Separate Earle–Sipe opened and honestly identified. |
| Gabber1994; Fujiwara1995 | Originals not opened | Explicit B3 subject21 direct-source derivations remain; modern Stacks/HHW/Bhatt–Mathew proofs are complete substitutes only for mathematical truth. |
| Lieberman1968 | Not opened | Kleiman1968/1994 opened original expositions supply abelian Lefschetz theorem; literal fetch still unfulfilled. Independent short retrieval failed as logged below. |
| Nakamura1990; Ihara–Nakamura1997 | Mathematical originals not opened | Later Mochizuki/Hoshi sources supply the actual reconstruction proofs; source-chain historical requirements remain. |
| Alling–Greenleaf1971 | Metadata only | Independent A7 proof complete; requested book not fetched mathematically. Alling1981 preview is not the 1971 book. |
| Gabriel1932 | Not opened | C2 arguments are independently proved, HLP original opened. Root assigned fresh retrieval of Gabriel. |
| Knudsen–Mumford1976 | No current original entry | Root assigned retrieval. R13's determinant claim is background unless used; it is not an omitted lettered C task. A fetched source should identify axioms precisely without pretending a new determinant theorem was required/proved here. |
| Bers boundary papers | Ahlfors–Bers1960 opened; no boundary-paper entry identified | Root checking exact requested category. Parameter-dependence proof already cites the opened paper. |
| Lehto–Virtanen; Pfluger1960 | No current original entries | Root retrieval. BA/Bishop and direct seam proofs supply present math. |
| Koebe; Lavrentiev | No original entries identified | Quarter theorem independently proved; weighted-disc extremal arguments use opened Jenkins–Strebel/Dubinin literature. Root retrieval. |
| Birman book | No original entry identified | Farb–Margalit original authored book gives exact Birman theorem used; requested Birman source still distinct. |
| SGA4 | Opened Expose XVI in authorized reedition | Exact used comparison locators supplied. |
| SGA4½,5,6 | No original current entries | B agent now retrieving lawful original scans. Toën2012 URL ending `sga6.pdf` is a different work. |
| Raynaud thesis1970 | Picard1970 article opened; exact thesis title being resolved | Do not identify the article, LNM119 thesis and LNM169 henselian-rings book without title-page evidence. |
| Kleiman1968 and1994 | Both full original texts opened | 1994 newly retrieved by B, active bib reflects this. |
| Ancona; Mumford; Bloch | Required mathematical passages opened | Bloch fullbook not opened, but all used steps explicitly available in official excerpt. |
| EGAIV16; HLPchX | Original texts opened and inspected | No source gate for C1 differential operators or classical rearrangement background. |

## Other prompt obligations

Update13:50UTC: the new A6-model-system and A6-model-specialization theorems have been integrated and independently checked by A567, B and root. They give a canonical marked cofiltered SNC model system and model-independent tangential specialization over one fixed trait. The Fermat cubic fourfold proof and correspondence/smooth-blowup closure results are integrated before B1(c), with a completed independent B audit. The exact conditional domain of the componentwise-definiteness method is accepted as the literal B1(b) scope; an unrequested exhaustive geometric isomorphism classification is not added as a blocker. Gabriel1932 is now opened in full from the public volume33 scan, with precise symmetry/parity scope in notes/part_c_gabriel_original.md. These updates supersede the corresponding earlier snapshot rows without pretending they were known at the original audit time.

The focused literature search for existing published studies is recorded in `notes/root_literature_search.md`, with both search engines, Michel Hua's project, and the historical letter transcription distinguished. The quarter bound, orange argument and marking correction retain their prior credit. No absence/priority claim is made.

The active report must eventually replace its stale B3 “in progress” mathematics row with the completed scoped theorem inventory while retaining original-source gates. The root is separately responsible for final result/event reconciliation, report correction/program tables, source-status merging, clean LuaLaTeX build and PDF rendering, and scheduled checkpoints. This audit did not rerun optional finite checks or alter those root-owned files.
