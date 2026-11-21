# TRACE_DET — final reading guide

Run: **TRACE_DET_20261121**, 20–21 November 2026. Reviewer/model: **GPT-6 Astra Pro**; effort setting not exposed by the runtime.

**Final-return status: INCOMPLETE on five explicitly identified evidence or correspondence questions.** The 81-page paper contains the completed checked findings in Part I and the unresolved identifications in Part II. The outstanding rows are **Q-STEP1, Q-STEP4, Q-STEP7, Q-DIRECT-BRIDGE and Q-TRANSCRIPTION**. Their precise gates and next steps are below.

The task's convention is retained: **Alpöge's RH and Dirichlet GRH statements are cited theorems**. No Lean build, complete formal-proof audit or independent authentication of the public source mirror is claimed. Every use of **Masullo's deep draft statements is conditional** on the particular statement and hypotheses cited.

## Main files

| File | Contents |
|---|---|
| `TRACE_DET.tex` | Self-contained paper, full proofs, finding IDs, exact source locators, conditional scopes and a separate part for unresolved identifications. |
| `TRACE_DET.pdf` | Compiled 81-page reading copy of the same paper. |
| `QUESTIONS.tsv` | 79 question rows with proved/refuted states or exact remaining gates. |
| `CHECK_EVENTS.tsv` | Actual dated source readings, whole-proof checks and computations, with model, disclosed effort information, run, event type and originating event stream. |
| `LEDGER.md` | Dated progress, attempts, smaller gates, checkpoint receipts and final status. Older entries are history; the closing entry supersedes their provisional gates. |
| `IMPLICATIONS.md` | Consequences for cote 1, SA23/Fable, the cited literature and the six RH programmes. |
| `TRANSCRIPTION_NOTES.tsv` | 16 mathematical repairs or qualifications, exact cote/scan/line references and confidence limits pending manuscript images. |
| `EVIDENCE_INDEX.md` | Grouped map to the research notes, source provenance, proof checks and visual verification in `work/`. |
| `REQUEST.md` | The supplied task, retained verbatim for audit context. |
| `RELEASE_STATE.json`, `MANIFEST.sha256` | Release metadata and SHA256 checksums for every other archive entry. |

## Main mathematical outcome

**The determinant exists concretely, and an actual source-model realization is proved.** B-01 constructs the trace-class operator on the zero-pair Hilbert space and as a continuous sine-series kernel:

\[
G(w)=\frac{\Xi(\sqrt w)}{\Xi(0)}=\det(I-wB),\qquad
B\ge0\ \Longleftrightarrow\ \mathrm{RH}.
\]

DET-15 constructs infinitely many orthogonal rank-one Bessel convolution projectors on one fixed Hilbert space, retaining all source hypotheses. Every complex summable weighting has an explicit measurable kernel, exact trace-norm approximants and the product determinant. The reciprocal-square zero weights give B plus zero without RH, and are positive under the stipulated theorem.

**The arithmetic scalar reconstruction is closed under RH.** DET-16 starts from the prime-sum cosine kernel, recovers its frequencies and integer multiplicities by Fourier averages, and reconstructs the full ordinary determinant. The multiplicity restoration matters: the scalar cyclic space alone has one dimension per distinct atom. These recovered weights can be placed on the actual DET-15 source projectors. The positive-type condition used in this reconstruction is itself RH-equivalent; this does not independently identify the historical finite determinant sign with positivity of B.

**The weighted-character endpoint has an ordinary determinant.** DET-18 clears the source's rational weights by the explicit integer multiplier M=2(3o+1), treats the central branch and all zero multiplicities, and proves the exact Mellin/resolvent formula including gamma and polar corrections. It proves the necessary and sufficient divisor integrality criterion for omitting that multiplier. For the resulting transformed operator, the exact GRH condition is 0<=C<=4I.

**Several proposed identifications are refuted in their stated scopes.** The literal Fourier operator has incompatible eigenvalue signs; path moments need a rank-one insertion; a fixed polynomial determinant cannot equal G; the actual signed Gram sign does not make its Gram matrix positive. Prime-weighted projectors give the arithmetic trace -zeta'/zeta, but their determinant at exponent 2 has the wrong zero count (DET-17). The natural Lorentz boost in the source cannot be the arithmetic pure-point flow (DET-19). These are specific obstructions, not a universal nonexistence theorem for every possible correspondence.

## Masullo and the other requested questions

MAS-SRC-01–03 identify the exact draft statements and their limits, especially Theorems 10.3.2.1, 12.5.1.1 and 13.3.1.1. MAS-10 constructs an ordinary Xi determinant on the actual quotient, conditional on the full spectral-annihilator theorem. MAS-11 extends the construction to fixed unitary Hecke characters with central blocks removed and functional-equation partners paired. These analytic determinant proofs do not require GRH or the draft's separate nuclearity assertion. MAS-09/12 show that the resulting inverse-square operator in the stated quotient metric is not boundedly similar to a selfadjoint operator. The draft dependence is retained in all these conclusions.

TOY-01 proves the estimate for k>=2 over finite fields and corrects the composite cyclic-ring constant; explicit counterexamples refute the unqualified composite and k=1 versions. The paper also gives the requested six-programme comparison, a finite-field curve dictionary and checked archive repairs. The abstract analytic trace theorem, cohomological Lefschetz formula, weight/purity statement and positive-Hilbert-space assertion are kept distinct, with exact Grothendieck/SGA/Deligne locators where they apply.

## Remaining gates and next steps

| Question | Strongest result reached | Exact next step |
|---|---|---|
| Historical step 1 | Five actual determinant families were read structurally, beyond keyword searches. | Identify the intended declaration, its parameters and multiplicity-producing specialization. |
| Historical step 4 | The two-indicator Weil calculation and scalar Landau consequence are proved; actual finite signed determinants are understood. | Specify W, S, linear/quadratic convention, determinant and normalization, then prove the equality in that specialization. |
| Historical step 7 | Actual finite Gram/Capelli/exterior-period identities and a positive rank-one period map are identified; an interlacing selector is proved separately. | Match the full historical determinant and its non-interlacing parameters to exact declarations. |
| Direct finite-sign bridge | The common source Hilbert space, trace-norm approximants, arithmetic scalar reconstruction and weighted endpoint determinant exist. | Prove that the source's finite sign supplies the exact scalar/kernel identity, or a stronger operator correspondence, independently of invoking RH-equivalent positivity. |
| Transcription attribution | The required mathematical corrections are proved. | Compare each listed place with the original manuscript images to distinguish transcription error, authorial slip and implicit convention. |

A particularly small sufficient target for the direct-sign question is a specified actual determinant whose positive normalization equals

\[
W_{\rm std}(q_0+q_{-\log X})=2k(0)+2k(\log X)
\]

for all sufficiently large X. Its nonnegativity gives the proved global lower bound and hence RH by STEP6-03. A positive Gram-matrix identification is a stronger sufficient target. The actual weighted-character power-window endpoint must retain its own coefficients, corrections and quantifiers. No missing historical definition is filled by resemblance alone.

The integrality question for an **uncleared** weighted determinant is a refinement with an exact proved criterion, not a remaining trace-class existence gap. Deninger's specified arithmetic cohomology and the truth of Masullo's complete draft are not constructed or certified by this audit; their programme/source status is stated explicitly.

## Approaches tried and where they led

| Route | Result or precise limitation |
|---|---|
| Note, supplied map, entry files and mirror history | The timeline lacks the matrices and is qualified as provisional paraphrase; mirror timestamps/history do not recover the October chronology. |
| Exact names and independent structural searches | Five step-1 determinant families, several step-4 functional/matrix families and the period neighborhood were read. None uniquely determines the historical declaration. Search absence is not a mathematical absence proof. |
| Literal finite Fourier identification | Refuted by the q=3 spectrum. |
| Open-path moments as traces | Refuted; repaired by a rank-one determinant variation (DET-08). |
| A fixed finite polynomial as the Xi determinant | Refuted by infinitely many zeros; limiting families were then investigated. |
| Actual Gram, Capelli and exterior-period source definitions | Exact finite identities proved/reported with hypotheses; signed determinant positivity does not imply positive matrix inertia. |
| Endpoint dependency and Mellin/Laplace analysis | Scalar bound/window/pole mechanism identified; exact resolvent, Weil and weighted-character determinant representations established. |
| Raw signed scalar as a positive kernel or trace coefficient | Refuted by finite matrices; determinant-line and Lorentz-projection interpretations proved (DET-12). |
| Inverse-power Berezin transform | Positive kernel and trace-class frames proved; no arithmetic Xi measure was identified for this particular construction (DET-13). |
| Period frames with a common finite target | Positive frames and exact trace summability proved; degree/cutoff restrictions apply to that finite-target realization (DET-14). |
| Fixed infinite Bessel convolution model | Common Hilbert-space construction and exact finite approximants closed; source instantiation checked (DET-15). |
| Prime-sum scalar kernel and GNS reconstruction | Frequencies and full integer multiplicities recovered under RH; direct historical sign attribution remains (DET-16). |
| Positive von Mangoldt projector weights | Exact arithmetic trace obtained; exponent-2 determinant refuted as Xi by zero counts (DET-17). |
| Rational character weights | Ordinary determinant constructed after integer multiplication; exact criterion for the unmultiplied version proved (DET-18). |
| Source's natural boost as arithmetic flow | Refuted on the actual representation and closed Bessel image; other specified flows are not excluded (DET-19). |
| Masullo compact-test/heat/Green routes | A single smooth compact test fails; the Green construction closes the actual quotient trace-class bridge, with Hecke extension and metric obstruction (MAS-07–12). |

The notes in `work/`, indexed by `EVIDENCE_INDEX.md`, preserve calculations, attempted alternatives, failures, hypotheses and source locations. The closing ledger gives the final states without erasing earlier dated progress.

## Checks, provenance and reproduction

Every new claimed proof has a recorded whole-proof reading before delivery. Event labels describe what actually occurred. Cited theorems have source-reading events, not invented complete proof checks. The prompt's category `computation or formal certificate` includes rows whose outcomes explicitly describe numerical/symbolic computations, byte comparisons or release checks. No event claims a Lean build.

A shared intermediate event filename was overwritten early in the run. The original checks were restored in distinct determinant and Masullo streams, and the restoration was recorded. The merger excludes the ambiguous duplicate and retains both restored streams.

All 81 PDF pages were visually checked in seven contact sheets, with additional full-size inspections. See `work/pdf_qa_build23.md` and the rendered pages. The final build has no missing citation, unresolved reference or overfull box. One benign underfull paragraph involving a long source identifier was reviewed and retained.

Run `pdflatex TRACE_DET.tex` twice in a standard LaTeX installation with the packages named in the preamble. The main file has no external input dependency. Proof fragments and assembly/event-merge scripts are included for continuation; the assembled TeX is the reading and compilation authority. From the archive root, run `sha256sum -c MANIFEST.sha256` to check the supplied file hashes.

The input ZIP was extracted once. Its 20 supplied files are identified in `work/input_manifest.tsv`. The public Lean mirror archive was 239,275,554 bytes, SHA256 `9631b4f020199e580ba86178cb56c6e9b09f690c2369a80dc4334aa93f49c7fc`; the supplied Main/Statements files and nine separately fetched files match the corresponding mirror files byte for byte. This does not authenticate the author's multipart archive. Retrieval URLs and further hashes are retained in the manifests.

The final ZIP includes deliverables, research notes, proof fragments, search evidence, computation results, dated event streams and final PDF renders. It excludes reproducible full external source caches, LaTeX runtime files and earlier checkpoint ZIPs. The original attachments remain the input set for a continuation.

## Timing and return status

The recorded start was 20 November 2026, 23:51 UTC (21 November, 00:51 CET). Three scheduled 45-minute checkpoints were saved under distinct names at 00:36, 01:21 and 02:06 UTC. Their receipts are in the ledger; none was overwritten or nested.

The first three-hour movement review would be due at 02:51 UTC / 03:51 CET. The final return is being closed before that boundary. No such review, no hourly review and no two-consecutive-no-movement stopping trigger is claimed. INCOMPLETE describes the unresolved correspondence and image-attribution questions at this session's final return; it does not reclassify a checked theorem as unproved or claim the unnamed historical correspondence impossible.
