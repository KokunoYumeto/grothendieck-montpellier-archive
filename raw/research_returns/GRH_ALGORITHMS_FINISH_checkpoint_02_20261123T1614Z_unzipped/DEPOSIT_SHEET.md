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
the logarithm of the characteristic, and the part of the relevant
cyclotomic value prime to twice the degree. Granting Alp\"oge's theorem
on Dirichlet GRH, we also give a construction polynomial in the
logarithm of the characteristic for each fixed prime degree and fixed
valuation. The first bound is uniform in its displayed numerical
parameters; the second has an exponent depending on its fixed
parameters. These results settle two classes of inputs in Lenstra's
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

Page numbers below refer to the current compiling draft, not a completed release review. They will be regenerated against the final PDF.

| Box | Requirement | Place and evidence |
|---|---|---|
| 1 | Title names the results and the ideas carried out | Title page: small numerical cyclotomic cofactors and fixed valuation; Bach, von zur Gathen, Lenstra and Pila. |
| 2 | Abstract begins with prior work, then results, inputs, significance and checking | Abstract, p. 1; A is granted; the two 2026 preprint inputs and Tang's Lemma 8.1 revision are explicit. |
| 3 | Full theorems, inputs, and explanations in words | Section 1, p. 1 (`sec:main-statements`); prose follows each main theorem/corollary. |
| 4 | Why this matters | Section 1, paragraph “Why this matters”; deterministic presentation of a finite field and the exact unsolved uniform range. |
| 5 | Exact division of credit | Section 1: BGL Theorems 1–3, printed pp. 6–7 and proofs pp. 16–24; Pila Theorem D, printed p. 746; precise additional construction inputs are identified. |
| 6 | Context, classical and recent | Section 1 classical table and named Tang/OpenAI/CT transfers; source versions and statement-level locators throughout; Boyer's thesis is compared by its fixed precomputation and certification scope, Chapter III, pp. 50 and 81. |
| 7 | Scope and open range together | Theorems 1.1, p. 2 (`cor:two-primary-cyclotomic-cofactor`) and 1.2, p. 3 (`thm:fixed-wild-cm`); fixed parameters versus absolute exponent, A versus CT, exceptional inputs and final questions section. |
| 8 | A section headed Proof overview before proofs | Section 2, p. 10 (`sec:proof-overview`); cofactor projection, CM/theta/Pila descent, classification and pure-field identity, presented-field interfaces, and conductor-budget averages. |

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

The current draft has a fresh source-only three-pass pdfLaTeX build, 151 pages, no final warnings, no undefined references, and no overfull box. This is compilation evidence only. The first expert image reading has completed pages 1–114 and their changed-page amendments; the final range is in progress. Corrected pages 127 and 143 still require their expert amendment, followed by the complete second reading. Fresh same-model statement-only reports are available for P006, P008, P009 (source transfer), P128 and P131. The separate complete CM/theta and étale/cofactor composition audits passed at their stated fixed-parameter scope. A distinct statement-only CM reconstruction closed in a separately sealed second phase at 15:44:21 UTC and passed complete root comparison; the pure-field and Teichmüller statement-only reports sealed with PASS at 15:27:13 UTC, with root comparison complete; the independent eighteen-row classification and fixed-strip transfers also passed with the recorded sampling-law and input-promise qualifications; all four average statement-only reconstructions sealed and passed root comparison at their stated strict constants and uniformity.

The owner assigns the permanent WB number and permanent record page on filing, as requested. The predeposit folder is therefore `work/unfiled/v1/`; no registry number, public repository commit, deposited version or human review is invented. Final byte hashes belong in its version manifest. The paper's permanent-record macro presently points to the specified registry root for replacement at filing.
