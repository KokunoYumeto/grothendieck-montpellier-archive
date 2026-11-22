# Read-only audit of Refuted-row polarity

19 November2026. Reviewer: GPT-6 Astra Pro, OpenAI, ChatGPT Pro mode; agent `part_c_algebra`.

**Scope:** all159current aggregate CSVrows were inventoried; all28rows with status `Refuted` were compared with their active TeXcaptions and contributor CSVrows. No TeX, CSV, aggregate, proof or certificate was edited or rerun. This is reporting clarity, with no mathematical/status movement.

## Aggregate-level cause and sufficient repair

`code/assemble_records.py:89` unconditionally replaces contributor `statement` text with the active theorem body. Those bodies correctly assert the proved counterexample or corrected result, while `Refuted` classifies the original claim addressed by the result. Thus positive contributor rephrasings alone will not fix the aggregate.

A uniform prefix is sufficient;28handwritten positive-claim mappings are unnecessary:

> Proved refutation and corrected scope (active caption: …): [existing body]

Standard notes sentence:

> Refuted classifies the original manuscript claim addressed here; the statement field records its proved refutation and any corrected scope.

Use **active caption**, rather than claiming every caption literally states the positive original claim. For example, the A7-domain-counterexample and B1c captions describe the proved negative conclusion. This does not require a mathematical or TeXstatus change.

## Standalone contributor rows with genuine polarity ambiguity

These rows state a true negative/counterexample proposition while their standalone status says `Refuted`. The following positive-claim alternatives remove that ambiguity if contributor CSVs are intended to remain self-contained. They are optional once the schema's status semantics are explicitly documented. The known A1-toric-nondescent case is included for completeness; the other19IDs are the additional cases. File row numbers below include the CSVheader.

| ID | Owner CSV and row | Suggested positive claim classified as Refuted |
|---|---|---|
| A1-nontoric-cut | `checks/part_a1_cut_results.csv:2` | Arbitrary analytic cuts canonically yield pointed-cap antiisomorphisms. |
| A1-bordered-landing | `checks/part_a1_bordered_results.csv:2` | Canonical cutting and capping always lands in the bordered target with external-only admissibility. |
| A1-toric-noninjective | `checks/part_a567_results.csv:38` | Toric compatibility of the paired caps suffices for injectivity of canonical surgery. |
| A1-toric-nondescent | `checks/part_a567_results.csv:42` | Raw canonical toric surgery is invariant under replacement by an isotopic toric cut in the same labelled surface. |
| A1-cut-not-algebraic | `checks/part_a1_algebraicity_results.csv:2` | The natural complex geodesic-cut component for the four-labelled punctured sphere is the analytification of a smooth connected finite-type algebraic curve. |
| A5-six-points | `checks/part_a567_results.csv:3` | The six-point reconstruction and S4stabilizer assertion holds in every characteristic different from2, without a characteristic5exception. |
| A6-ordinary-counterexample | `checks/part_a567_results.csv:7` | The ordinary arithmetic étale fundamental group of a stable marked curve determines its chosen nonzero normal tensor. |
| A6-procyclic | `checks/part_a567_results.csv:12` | Invariant cyclotomic procyclic subgroup conjugacy classes are in bijection with the nodes and marked points. |
| A6-three-classes | `checks/part_a567_results.csv:14` | The literal NB exhausts the injective homomorphism conjugacy classes by three classes, or two when n=0. |
| A6-special-fibre-counterexample | `checks/part_b_a6_counterexample_results.csv:2` | The Kummer-étale cover category over the generic Galois group, or the same framed tangential extension, reconstructs a chosen special-fibre scheme. |
| A6-frobenius-counterexample | `checks/part_c_a6_scope_results.csv:5` | The strict characteristic-zero Isom-anabelian definition is preserved unchanged by arithmetic specialization. |
| A6-wild-counterexample | `checks/part_c_a6_scope_results.csv:3` | All finite étale covers may replace the boundary-tame subcategory in mixed-characteristic logarithmic specialization. |
| A7-domain-counterexample | `checks/part_a567_results.csv:26` | Over a2-torsion-free connected ring, every involution distinct from±1on a rank-two projective module has invertible eigenspaces. |
| A7-ratio-j | `checks/part_a567_results.csv:29` | The numerical guesses of67/097–098are correct: the quadratic-form hexagonal ratio is√3and j=c log(a)for the proposed nonzero constant. |
| thm:B1c / B.1c | `checks/part_b_results.csv:9` | Numerically trivial curve cycles on smooth connected projective threefolds are τ-trivial. |
| thm:B2-square / B.2.square and B.3.25 | `checks/part_b_results.csv:11,48` | An algebraically trivial divisor has rationally trivial square, and every Albanese-trivial zero-cycle is rationally trivial. |
| C-other-autos | `checks/part_c_results.csv:5` | Every differential automorphism is the exponential of a nilpotent derivation. |
| C-functor-counter | `checks/part_c_results.csv:8` | Both exponential maps of68/044are bijective for every K-module functor. |
| C-K-counter | `checks/part_c_results.csv:12` | The chain axioms a)–d)of68/017imply ConditionKfor the convolution-stable family they span. |
| C-packed-asymmetry | `checks/part_c_results.csv:17` | The tassé relation is symmetric. |

These are20aggregate IDs and21contributor rows, because B.2.square and B.3.25share the same active theorem. The positive alternatives retain the standing hypotheses of their respective sections; they are labels of claims being refuted, not new assertions added to the paper. Counterexample details should remain in the proved body/notes.

## Descriptive or explicitly mixed rows not needing this rewrite

Four remaining contributor-backed aggregate rows already make their mixed roles clear: A6-node-character (`checks/part_c_a6_scope_results.csv:4`, status explicitly adds “corrected statement proved”); thm:B3-pprimary/B.3.3(`checks/part_b_results.csv:26`, known lower bound plus refuted equality); thm:B3-specialization/B.3.16(row34, known specialization plus refuted unrestricted invariance); and thm:B3-sga2/B.PM.sga2(row57, explicit counterexample plus known replacement). These are normal corrected-result/counterexample descriptions, not additional mathematical polarity failures. The mixed B.3.24alias(row47) likewise covers several conclusions and is not a separate aggregate Refuted-row mismatch.

The other four aggregate rows—A1-global-refutation, A2-independence, A4-orange-extremal and A4-orange-jets—have no matching contributor CSVrow. Their active captions identify the questioned global isomorphism, independence or orange-slice model; their proved negative bodies are correctly handled by the uniform aggregate prefix. No separate owner-CSVchange is suggested for them.

This accounts for all28Refuted aggregate rows:20IDs with standalone contributor wording worth clarifying,4explicitly mixed/descriptive IDs, and4root-generated IDs. The audit found no reversed mathematical conclusion and recommends no status change.
