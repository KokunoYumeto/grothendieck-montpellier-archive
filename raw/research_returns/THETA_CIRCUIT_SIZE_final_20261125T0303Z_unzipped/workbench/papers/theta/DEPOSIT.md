# Deposit sheet

Title: Exact gate counts for theta graphs and cycles with pendant leaves, after jiaxun530 and fengqiaoqu

Authors: deliberately blank for the editor.

Subject: Boolean circuit complexity and graph edge functions.

MSC suggestions: 68Q17; 05C38.

Keywords: Boolean circuit; theta graph; vertex cover; charged negation;
fan-in two; branching wire; even cycle; pendant leaf.

## Abstract

In the PEqualNP circuit programme, fengqiaoqu proved that a theta graph
without a four-cycle has monotone circuit size equal to its number of edges
plus its vertex-cover number minus one; jiaxun530 used first branching wires
to prove an all-gate lower bound for a particular theta. We show that the
same exact size holds when arbitrary internal NOT gates are allowed and
charged. In particular, the edge function of two seven-cycles sharing an
edge requires eighteen gates. The main lemma states that a graph of minimum
degree at least two without a four-cycle requires at least its number of
vertices plus its cover number minus one binary gates, even in the presence
of negations. We re-prove the positive theta theorem in the form needed for its
equality case, making the argument self-contained for every theta.
We also determine the exact charged-gate size of an even cycle with two
pendant leaves, including fourteen gates for the eight-cycle with leaves
at vertices zero and three. Three nonadjacent leaves on an odd cycle,
separated by odd distances, give another exact formula and seventeen gates
for the nine-cycle with roots zero, three and six.
The mathematics and text were produced by GPT-6 Astra Pro and checked by
separate instances of that model and finite computations; no human has
checked them.

## Eight opening requirements

| Requirement | Location |
|---|---|
| The theorem and credited programme in title | Title; Section1 opening |
| Source work, result, scope, production in abstract | Abstract |
| Complete main statements in words and symbols | Theorems1.1,1.2,1.4,1.5; Corollary1.3 |
| Why the result matters | Section1 paragraphs after Figure1 |
| Exact division of credit | Abstract; Section1 credit paragraph; references |
| Context and neighbouring work | Section1 credit paragraph; references |
| Scope and remaining open cases | Section1; final section |
| Prose proof overview | Section2, Proof overview |

## Credit

- jiaxun530: first-branch DAG ingredients in the prior ten-input theta proof,
  public contribution3848,24November2026.
- fengqiaoqu: monotone theta theorem, singleton-carrier and consumption
  method, public contribution761,23November2026.
- Ikenmeyer, Komarath, Lenzen, Lysikov, Mokhov, Sreenivasaiah: hazard
  derivative background; not used as an all-gate lower bound.
- Jukna: historical single-level-conjecture counterexamples, contextual.
- The original graph reductions and witness are credited in CROSSWALK.tsv.
- OpenAI: First Proof report, methodological context only.

## Method, rights and status

Produced by GPT-6 Astra Pro in ChatGPT Pro mode. Same-model independent
re-proofs, targeted audits, finite computations, and the limited formal
certificate are distinguished in CHECK_EVENTS.tsv. The numerical inherited
reasoning effort was not exposed. No human check. Original text and code:
CC0 1.0 Universal.

The primary mathematical question and requested follow-on are settled in the
paper. The complete literal PEqualNP lower bound is not yet a kernel-checked
certificate; only the ordered-group cover step is compiled. The conditional
project theorem source is labelled as such. No public publication, repository
push, assigned WB number, or deposit commit has been made.

The editor assigns the permanent WB number and version directory under
work/WB-nnnn/vX. Until then the THETA-nnn tags are stable local tags, and
recordurl points to the registry as requested. The complete per-version
manifest accompanies each return; its digest is also stored in the ZIP
comment. An actual repository commit and publication imprint must be added
at deposit, without inventing an existing commit or circularly hashing a PDF
containing its own final-file manifest.

## Production provenance outside the paper

The inherited numerical reasoning setting was not exposed. The frozen source
inventory records file assembly by Claude Opus5.5 at effort max; this is
provenance of those files, not authorship or an independent check of the new
theorems. All proof-check workers in this run used the same GPT-6 Astra Pro
model. The chronology distinguishes fresh re-proofs, prior-source exposure,
and later targeted reading of the manuscript.
