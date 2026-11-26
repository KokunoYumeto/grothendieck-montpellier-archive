# Deposit sheet — B

Status: research in progress; not deposited. Author line intentionally blank. The owner assigns the permanent registry number, public page and commit.

## Title

Monotone circuits for the edge functions of C4-free graphs

## Current abstract

The following is the editable LaTeX abstract of the accompanying source; its mathematics and scope match the PDF built from it.

```latex
Jukna's work on quadratic Boolean functions shows why circuit computation cannot in general be reduced without cost to a single product level. The public P versus NP programme asks whether the edge function of every graph of girth at least five requires exactly the number of edges plus the vertex-cover number minus one binary monotone gates. Starting from the established theorem for at most three missing quadratic witnesses, we prove that four missing induced edges require at least four deleted products, exclude both the optimal six-deletion and optimal seven-deletion cases, and prove the full lower bound whenever four missing witnesses increase the vertex-cover number by four. A full-graph safety argument handles the remaining quadratic circuit with excess one. At cover gain three, we prove the full bound for an optimal quadratic frame when the missing graph is a three-edge path and a disjoint edge and the ambient graph has girth at least five; we also exclude five deletions for a missing triangle and disjoint edge in a four-cycle-free graph. With only one deleted addition, we prove an exponential lower bound on the deletion count in terms of the cover gain. We also give a size-preserving normalization for a specified shared two-level bilinear class. Complete propositional certificates support the finite obstructions. We prove the earlier bounded-weight barrier and one-point constructions in full, and correct the negation budget in the fast convolution construction using Beals, Nishino and Tanaka. The unrestricted conjecture, the remaining four-witness cases and general syntactic bidegree two remain open. The mathematics and text were produced by GPT-6 Astra Pro; separate re-proofs by the same model and exact certificate checks are recorded, and no human has checked the paper.
```

## Subject and keywords

Computational complexity; monotone circuits; graph edge functions; vertex cover; quadratic witnesses; bounded negation.

## Method and checking note

Mathematics and text: GPT-6 Astra (ChatGPT Pro mode; runtime label GPT-6 Astra Pro). Separate workers used the same model and inherited reasoning settings; no unexposed effort level is invented. CHECK_EVENTS.tsv distinguishes statement-only reproof, targeted proof check, exact computation/certificate, and source verification. No human has checked the papers. No Lean proof of these new statements is claimed. Original text and programs are dedicated under CC0 1.0. Intended workbench: https://github.com/KokunoYumeto/arithmetic-geometry-complexity-workbench . Permanent record placeholder: https://github.com/KokunoYumeto/mathematics-workbenches .

## Eight opening requirements

| Requirement | Location in this paper |
|---|---|
| 1. Field-recognizable title and credit | Title block; the programme/source is identified immediately in the abstract and Section1 |
| 2. Source, result, scope and production/check note | Abstract, first through last sentences |
| 3. Full main statements and meaning | Section1 named main theorems and the paragraphs immediately following them |
| 4. Why the question matters | Section1 opening question and consequences; A gives the explicit border transfer, B the size conjecture, C the height-stratum/counting distinction |
| 5. Exact division of credit | Section1 source/context subsection; exact theorem/page locators in references and proof citations |
| 6. Earlier and neighboring work | Section1 source comparisons and cited context; no source proof is assumed beyond its explicitly cited statement |
| 7. Scope and remaining obstruction | Section1 after the main theorems, and the closing What remains open section |
| 8. Proof overview | Section2, explicitly headed Proof overview, before the main proof sections |

## Authors whose work carries the arguments

Jukna (support criterion, quadratic Boolean context, open problem); Jerrum and Snir (lowest homogeneous components); Beals, Nishino, and Tanaka (negation simulation); Amano and Maruoka (tradeoff context); the public P versus NP programme and the cited companion circuit manuscripts (quadratic extraction, at-most-three witnesses and one-sided theorem); Claude Fable reports for the weight and light-input ideas, proved here at their stated scope.

The source list records exact locations used, not an assertion that the authors have seen or endorsed this text. Final visual inspection and complete final-version rereading are recorded separately when completed.
