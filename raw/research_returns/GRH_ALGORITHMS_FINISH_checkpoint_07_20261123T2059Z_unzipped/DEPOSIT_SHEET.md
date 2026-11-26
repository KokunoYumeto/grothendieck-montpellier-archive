# Deposit sheet — predeposit, not filed

**Title:** Unconditional finite-field constructions with small cyclotomic cofactors and fixed-valuation constructions under Dirichlet GRH, after Bach, von zur Gathen, Lenstra, and Pila.

**Author line:** Empty in the manuscript, for completion by the owner at filing.

**Subject:** Computational algebra and analytic number theory; deterministic finite-field construction; exact analytic inputs; complex multiplication and finite étale algorithms.

**Keywords:** Dirichlet GRH; finite fields; irreducible polynomials; cyclotomic cofactor; Teichmüller unit; complex multiplication; theta functions; Frobenius; deterministic factorization; effective Chebotarev; character averages.

## Exact manuscript abstract

```latex
Bach, von zur Gathen and Lenstra constructed nonresidues from smooth
cyclotomic values, and Pila used Frobenius polynomials of abelian
varieties to find roots of unity of fixed prime order. Starting from
these methods, we give an unconditional deterministic construction of
a finite field of prime degree, with bit cost polynomial in the degree,
the logarithm of the characteristic, a chosen prime cutoff, and an
unremoved cyclotomic cofactor. Each prime up to the cutoff may be
removed with its full multiplicity when it is not one modulo the
degree, without roots of unity as inputs. Granting Alp\"oge's theorem
on Dirichlet GRH enlarges the removable prime set: in degree three,
for example, only primes congruent to one modulo nine are excluded.
It also gives a construction polynomial in the logarithm of the
characteristic for each fixed prime degree and fixed valuation. The unconditional bound
has an absolute exponent; the CM bounds have exponents depending on
their fixed parameters. These results settle two classes of inputs in Lenstra's
construction problem, while the uniform problem with growing valuation
and cofactor remains open by these methods. We identify the pure-field
zeta hypothesis in the classical auxiliary-prime route, classify
classical consequences by their exact analytic inputs, and prove short
auxiliary and cubic searches outside explicit exceptional sets of
input primes. Tang's distinct polynomial-time interfaces rest on two
2026 preprints: OpenAI's prime-field theorem and Cureton and Thorner's
uniform Dedekind zero-free strip, Hexagon~2610.00200v2, whose Lemma~8.1
required the revision posted by Tang. The mathematics and text were
produced by GPT-6 Astra in ChatGPT Pro mode; statement-only re-proofs
used the same model, targeted proof checks were made by Claude Opus~5.5
at effort high, and no human has checked this paper.
```

## The eight opening requirements

Page numbers in the opening map remain those of Section1 and the proof overview. The current190-page PDF has SHA256 `9cc33a603ce72cc0a4dc5b50b5416534b24375f1d674720d442b4b230ede93f4` and source SHA256 `a9d56ce00281385b06a2018296df904929b7ac6d6b6238a2dca9cb858637680d`. Its fresh three-pass build completed 2026-11-23T19:57:02.801020+00:00, with zero final warnings/undefined references and maximum overfull box1.95055pt. The new changed-page expert and newcomer readings are pending. The previous181-page PDFef192414d9c0 was fully read twice, with exact coverage in checks/finishing/page_coverage_ef192414d9c0_both_passes.json. Rendering is never counted as reading.

| Box | Requirement | Place and evidence |
|---|---|---|
| 1 | Title names the results and the ideas carried out | Title page: small numerical cyclotomic cofactors and fixed valuation; Bach, von zur Gathen, Lenstra and Pila. |
| 2 | Abstract begins with prior work, then results, inputs, significance and checking | Abstract, p. 1; A is granted; the two 2026 preprint inputs and Tang's Lemma 8.1 revision are explicit. |
| 3 | Full theorems, inputs, and explanations in words | Section 1, pp. 1–12 (`sec:main-statements`); Theorems 1.1–1.3 on pp. 2–4, with explanatory prose after each main statement. |
| 4 | Why this matters | Section 1, p. 11, paragraph “Why this matters”; deterministic presentation of a finite field and the exact unsolved uniform range. |
| 5 | Exact division of credit | Section 1: BGL Theorems 1–3, printed pp. 6–7 and proofs pp. 16–24; Pila Theorem D, printed p. 746; precise additional construction inputs are identified. |
| 6 | Context, classical and recent | Section 1 classical table and named Tang/OpenAI/CT transfers; source versions and statement-level locators throughout; Boyer's thesis is compared by its fixed precomputation and certification scope, Chapter III, pp. 50 and 81. |
| 7 | Scope and open range together | Theorems 1.1, p. 2 (`thm:threshold-cyclotomic-cofactor`) 1.2, p. 3 (`thm:bounded-congruence-cofactor`), and 1.3, p. 4 (`thm:fixed-wild-cm`); fixed parameters versus absolute exponent, A versus CT, exceptional inputs and final questions section. |
| 8 | A section headed Proof overview before proofs | Section 2, p. 12 (`sec:proof-overview`); cofactor projection, CM/theta/Pila descent, classification and pure-field identity, presented-field interfaces, and conductor-budget averages. |

## Authors whose work carries the arguments

| Authors | Exact contribution carried here | What the manuscript adds or makes explicit |
|---|---|---|
| Bach, von zur Gathen, Lenstra (2001) | Smooth-cyclotomic algorithms, separating elements, rational-function count and odd-prime commutator; Thms. 1–3, Prop. 5.2, §§5.7–5.11. | The cofactor projection with no omitted roots-of-unity inputs, complete finite-étale computation and normalized descent; the smoothness estimate itself is credited to its source. |
| Pila (1990) | Frobenius characteristic polynomials in fixed dimension and fixed-prime-order roots of unity; Thms. A and D. | Explicit varying CM models and prescribed wild layers at fixed degree and valuation. |
| Mumford (1966, 1967) | Theta moduli, multiplication and addition formulas, universal quadratic equations. | A fixed-size arithmetic interface and complete addition atlas used in the composition. |
| Lenstra (1991) | Normal bases and cyclotomic/Teichmüller descent, Thms. 3.1, 5.1, 5.2. | Full formal-algebra input/output reductions and their parameter accounting. |
| Colmez, Wei, Pazuki; von Känel and Kret; Kannan, Lenstra and Lovász | CM height bounds and effective algebraic recognition. | Bounds for the explicit family, with the coarse unconditional alternative and exact hypothesis accounting. |
| Alpöge (2026) | A, RH for rational Dirichlet L-functions including zeta, expressly granted for this paper. | Applications within the stated scope; no claim to check that theorem's full proof. |
| OpenAI (2026), Cureton and Thorner (2026), Tang (2026) | Prime-field algebraic theorem, asserted uniform Dedekind zero-free strip, and both finite-field interfaces. | Detailed transfer, exact query bounds and analytic provenance; no certification of the whole preprints. |
| Cilleruelo (2011); Montgomery, as presented by Montgomery and Vaughan (2007) | Quadratic-value product and character-product mechanisms. | Private conductor primes and the displayed auxiliary/cubic average specializations. |

No correspondence or notification has been sent to any author. The table identifies attribution, not an inferred endorsement.

## Exact closing method note

```latex
The mathematics and text were produced by GPT-6 Astra in ChatGPT Pro mode.
Separate statement-only re-proofs used the same model; the configured
effort was not independently exposed. Claude Opus~5.5 at effort high
made targeted proof checks of the fixed-degree average theorem and
its character lemmas, of the logarithmic cubic search and its
quadratic-value and independence lemmas, and of the root-extraction
lemma behind the cofactor theorem, with the recorded finite
computations. The dates, scope, and outcomes of those checks and the
program reruns on 23 November 2026 are given in the workbench.
These checks are not formal certificates of the whole paper.
No human has checked this paper.
Our text is dedicated to the public domain under
\href{https://creativecommons.org/publicdomain/zero/1.0/}{CC0~1.0}.
The accompanying programs and records are in the
\href{\workbenchurl}{zeta and $L$-functions workbench}; the permanent
record address is \url{\recordurl}.
```

## Verification and filing state

The completed Parts2/3 version had source SHA256 `9c48048c92f3268f4d7d4704ad6e7d4b1c04f95dea0bf8243272f2fcbebf911e` and PDF SHA256 `f568cba4230b717d6899d568226341202b21b2f4b07630b15f72f287788e5444`. Its fresh source-only three-pass pdfLaTeX build had151 pages, no final warnings, no undefined references, and no overfull box. Every page of that exact version had an actual expert and newcomer image reading, including separately sequenced amendments of all changed images. The complete page association is `checks/finishing/page_coverage_f568cba4230b_both_passes.json`; the phase record is `checks/finishing/parts_2_3_completion.md`.

All 142 original permanent IDs have current proof-check events. The requested same-model statement-only reconstructions, full finite-etale/cofactor and CM/theta audits, main-theorem comparisons, and all fourteen finite reruns passed at their stated scopes. The original partial CM reconstruction remains preserved; its separately sealed second phase closes the missing step. Later local corrections are explicit errata rather than rewrites of earlier sealed no-fault reports. No human or formal verification is claimed.

Parts2/3 are completed for that exact earlier manuscript. The current190-page Part4 source/PDF pair is identified above. P143 is an average refinement; P144–P149 give certified smaller cofactor gates and the quantitative CM interface. P150–P164 contain the finite/genus-two, cyclic-descent, local-residue, fixed-menu and restricted ideal/reflex findings with full proofs and typed checks. P160–P161 have separate statement-only reconstructions; P162–P164 are recorded at their targeted check scope. None of these latter side results guarantees a new original-input class. Every changed image of the current build still requires expert then newcomer reading before final release. There are164 permanent statements,575 cumulative check events and200 source-scope rows. Review03 at19:45:00 found no main-gate movement, consecutive count1; review04 is due20:44:36. The uniform construction and A-only auxiliary-prime questions remain open.
