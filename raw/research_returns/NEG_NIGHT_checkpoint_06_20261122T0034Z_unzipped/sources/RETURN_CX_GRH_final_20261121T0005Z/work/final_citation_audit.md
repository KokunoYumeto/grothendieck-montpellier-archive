# Final citation and check-event coverage audit

**Auditor:** `/root/number_algorithms`; GPT-6 Astra Pro; inherited reasoning effort not exposed; run `CX_GRH-20261121`. This is a coverage audit of already recorded work. No new primary-source reading or proof validation is claimed here.

## Snapshot and result

- Audited the actual citations in `deliverables/CX_GRH.tex` together with the final `work/eth_factoring_composition.tex` (CX-N15), and compared them against `deliverables/CHECK_EVENTS.tsv` and all component `work/*check_events.tsv` ledgers. Historical draft/wrapper files are not treated as final deliverables.
- Final-source SHA-256: `5e59adf332b4211475f320efd942fcfb1b03dc791d03d2865e12ce3af0feb8fb`.
- N15 SHA-256: `5d433a8c0319e8a06c591f10d0ba52740e6bbb8564fd0646f078a1ef06cef247`.
- Consolidated-ledger SHA-256: `6f30c013f6d3fed11b83a37320b74f835095cf212eee0b03431518e3fd0b085b`.
- Cited bibliography keys: **51**. Undefined keys: **0**. Duplicate bibliography keys: **0**.
- The final refreshed consolidated snapshot contains **196 events**. Every component event is represented by the same statement ID and outcome; **0 component events remain to merge**. The four events that arrived during the original audit are retained below as an integration record.
- The initial audit identified two clear dedicated-source-event omissions: **Miller1976** and **Bürgisser2004 Theorem5.7**. Four exact background-status rows, including clearer Rónyai1992 and Gao-introduction mappings, are supplied in `work/final_citation_additions.tsv` and reproduced below. **All four are now consolidated.** They deliberately do not manufacture source-proof checks.
- **No claim that M gives general deterministic polynomial-time finite-field factorization was found.** The general bound remains quasipolynomial in the polynomial degree; fixed-degree and special-field qualifications are retained.

## Coverage map for every cited key

“Covered” means an honest event exists with the indicated scope, not that the underlying entire paper was independently proved. Source-abstract/background statuses are retained. All listed component events are consolidated in the refreshed snapshot.

| Bibliography key | Consolidated event IDs | Scope of the recorded check |
|---|---|---|
| `Alpoge2026` | SRC-A-D | Stipulated theorem; interface/Remark inspection only, no kernel replay. |
| `Archive2` | SRC-ARCHIVE2-5 | Historical scan inspection. |
| `Archive28` | SRC-ARCHIVE28-3 | Historical scan inspection. |
| `Archive34` | SRC-ARCHIVE34-64-74 | Historical scan inspection; crossed-out and finite-field scope retained. |
| `Archive98` | SRC-ARCHIVE98-11-12-44 | Historical scan inspection. |
| `BIMS17` | BIMS17-C1.3; SRC-BIMS17-T1.2-C1.3-T6.7; CX-N05-N06-BIMS-BGL-AL-chain | Exact theorem/model/scope checks; general theorem not independently reproved. |
| `Burgisser04` | GCT5-T2.8-T2.10-T3.4 indirectly; K-BURGISSER04-T5.7-INDIRECT | Dedicated background event now records the indirect use through GCT V; no fresh primary-source check is claimed. |
| `Burgisser2024` | E-S08; E08-S-Burgisser-7.4 | Definitions and named theorem statements located; model distinctions checked. |
| `CXBachShallit89` | SRC-BACHSHALLIT89-L13; CX-N11-BachShallit89-L13-T3 | Primary premise inspected; corrupted radical formulas explicitly excluded. |
| `CXNAKS04` | N-AKS04-T4.1-T5.1 | Background theorem statements verified, not complete AKS reproof. |
| `CXNAdlemanLenstra86` | N-AL86-P3; N15-S-AL86-BGL-Lenstra | Theorem1, AlgorithmA, Proposition3 and Lemma6 checked. |
| `CXNBDF08` | N-BDF08-T1.1-T2.1 | Relevant full proof and precise Hecke family read. |
| `CXNBGL01` | N-BGL01-T1-T2-T3; N-BGL01-T2-FULL-INTERFACE; N15-S-AL86-BGL-Lenstra | Inputs and bounds checked; N15 full interface/algorithm-flow events are consolidated. |
| `CXNBach90` | N-BACH90-T2-T3; N-BACH90-T4; SRC-BACH90-ROOT | Original paper recovered; relevant proofs/formulas checked. |
| `CXNBachSorenson96` | N-BACHSORENSON96-T5.1; BS96-T5.1 | Exact analytic convention and explicit bound checked; no analytic reproof. |
| `CXNBiasseErukulangara` | N-BIASSEERUKULANGARA-C1; CX-N12 | Main statement, algorithm/certification and conditional runtime audited. |
| `CXNBuchmannShoup96` | N-BUCHMANNSHOUP96; CX-N06 | Relevant algorithm and exact zeta/ray-class inputs inspected. |
| `CXNEvdokimov89` | N-EVD89-TI.3 | Original pp105–110 read with OCR defects disclosed; N15 now avoids this oracle. |
| `CXNEvdokimov94` | N-EVD94-MAIN; CX-N09 | Explicit primary-abstract-only status; complete original proof not retrieved. N15 supplies another composition. |
| `CXNGao01` | N-GAO01-L2.6; N09-S-Gao-2.6; N14-S-Gao-2.6; N-GAO01-INTRO-BACKGROUND | Root algorithm proofs checked; dedicated background row separately records introductory background/1988 attribution. |
| `CXNIKRS08` | N-IKRS08-L4.2-P4.6; N14-S-IKRS-4.2-4.6; N-IKRS08-MAIN | Relevant lemmas/proposition fully read; Main Theorem/input statement checked as established input, not full §5 reproof. |
| `CXNJMV09` | N-JMV09-T1.1-C1.3 | Exact Hecke-family theorem and relevant proof checked. |
| `CXNLenstra91` | N-LENSTRA91-T1.2; N-LENSTRA91-EXPLICIT-SUBFIELDS; N15-S-AL86-BGL-Lenstra | Isomorphism theorem/model checked; explicit-data/subfield proof read for N15. |
| `CXNLenstra92` | N-LENSTRA92-EQ5.7; CX-N08 | S-unit exact sequence and certification proof checked. |
| `CXNMiller76` | N-MILLER76-HISTORICAL | Dedicated background event records historical attribution, with N01 actually proved using separately checked Bach/Schoof. |
| `CXNRonyai92` | CX-N10 already qualifies it; N-RONYAI92-ABSTRACT | Only primary-abstract parameter claim used; original proof/theorem number not retrieved. |
| `CXNSchoof08` | N-SCHOOF08-T2.2 | Entire relevant theorem proof and quadratic-character scope read. |
| `CXNShoup92` | N-SHOUP92-T3-P9; N-SHOUP92-T2-P13 | Both distinct source proofs and families checked. |
| `EGA2` | SRC-EGAII6 | Finite-morphism/base-change locators inspected. |
| `FGA221` | SRC-FGA221 | Original theorem statements and hypotheses inspected. |
| `FS18` | FS18-T7.1 | Statement/parameters/output checked, no independent robust hitting-set proof. |
| `GCT5` | GCT5-T2.8-T2.10-T3.4; GCT5-T4.1-T5.5; GCT5-T4.10-T5.11a-T5.12; GCT5-D5.1-D5.6-D5.7; E-S09 | Relevant complete displayed proofs and encoding conditions read. |
| `GSS19` | GSS19-T1.5-T1.6 | Statements and immediate reduction inspected. |
| `JMV2013` | E-S06 | Theorem1 locality/parameter statement verified; no full reproof. |
| `K96` | K96-DIMACS-T2; K96-T4-T7-L3-T8-T9-C1 | Relevant theorem/proof and arithmetic reductions checked. |
| `K96TR` | K96-DIMACS-T2; K96-T4-T7-L3-T8-T9-C1 | DIMACS source used for complete displayed proof and protocol. |
| `K97Err` | K96-ERRATUM | Both pages read and correction visually checked. |
| `LO77` | LO77-T1.1; LO77-C1.2-FINAL-S9 | Exact zeta premise and scope checked; analytic theorem accepted as input. |
| `Macdonald1995` | SRC-MACDONALD-I3.4 | Formula/conventions inspected in scan. |
| `Masullo2026` | SRC-M-GRH | Conditional draft premise; selected convention/claim locators inspected, full proposed proof unaudited. |
| `MilneCFT` | SRC-MILNE0.4-0.5 | Hilbert/ray class reciprocity statements inspected. |
| `OpenAIETH` | E-S01; E-S02; E-S03; E-S04 | Stipulated main theorem; relevant consequence proofs and scope inspected. |
| `SGA1` | SRC-SGA1-V4-V7 | Equivalence/scheme-application statements read; no full Galois-category reconstruction. |
| `SGA3` | SRC-SGA3-I-VIII | Action/comodule/diagonalizable-group passages inspected. |
| `SGA4` | SRC-SGA4-IX3 | Kummer/Picard statements inspected. |
| `SGA5` | SRC-SGA5-XV3 | Determinant/Euler-product and finite-field scope read. |
| `SGA6` | SRC-SGA6-V-VI | Lambda/gamma and K-group structures inspected; source machinery not fully reproved. |
| `Valiant1979` | E-S07 | Permanent-completeness statement and characteristic condition located. |
| `Washington1997` | SRC-WASHINGTON4.3 | Primitive-character zeta factorization statement inspected. |
| `WeilII` | SRC-WEILII | Weight definitions and named finite-field bounds inspected. |
| `Williams2013` | E-S05-1.1; E-S05-2.1; E-S05-6.1; later CX-E03 refinement | Exact speedup and hierarchy premises; relevant ETH proof sketch checked. |

## Events integrated during the audit

These actual component events were outstanding in the 181-event intermediate snapshot and are all present in the final 196-event refreshed snapshot. Their check scopes are preserved here. Author/self-review and independent-review events for N15 and N14 remain distinct.

| Component ledger | Event ID | Scope |
|---|---|---|
| `eth_check_events.tsv` | `N15-final-integration` | Read IMPLICATIONS, revised paper_scope U02/U03, updated N15 PartII dictionary, latest assembly inclusion, and per-ID E01-E08 geometric dictionary/source linkage. Suggested exact IMPLICATIONS replacements recorded in final_n15_integration_review.md. Revised scope and geometry pass; no generic tests performed. |
| `eth_check_events.tsv` | `E08-S-Burgisser-7.4` | Directly read author PDF Section7.4 eq7.6 printedp38 and eq7.9 printedp39 (turn318824175view0); inserted this exact locator in E08 as authorized. No proof change. eth_geometry.tex SHA-256 72e73b127dad2189370fc2516c261a7fe4459d75768fc10000e4a995ee8b1f46. |
| `koiran_check_events.tsv` | `CX-N15-complete-composition` | PASS at SHA256 5d433a8c0319e8a06c591f10d0ba52740e6bbb8564fd0646f078a1ef06cef247; every new proof step read end to end, full N11/N14 support read, BGL2 and IKRS Main/L4.2/P4.6 statements rechecked in primary sources. Exact E_nu family covers every AL86 call; no mathematical gap found. Cited literature not independently reproved. |
| `koiran_check_events.tsv` | `BGL01-T3-single-prime-shortcut` | Read full section5 displayed algorithm pp20-24. Paragraph afterT5.1 expressly requires roots for all primes dividing Phi_k(p), largest entering time even for smallest target. Steps5.9-5.10 use those inputs. Does not supply a uniform single-r shortcut; no general H_A impossibility inferred. |

## Exact additional rows now consolidated

These source-coverage records have **background** status and have now been added to the final ledger. They describe this audit and the existing dependency record rather than asserting unperformed primary-proof reading. The separate TSV file uses the exact final-ledger column schema; do not append it again.

```tsv
statement_id	date	who_model_effort_run	type	outcome	method_and_locator
N-MILLER76-HISTORICAL	2026-11-21 Europe/Berlin	/root/number_algorithms; GPT-6 Astra Pro; inherited effort not exposed; CX_GRH-20261121	carried as background without fault found	Citation-coverage audit only. Final N01 gives Miller1976 Theorem2 and Appendix as historical attribution. Their locators are recorded in the existing working notes; this audit did not reopen the original paper or newly check its proof. The actual cutoff and transfer rely on separately checked Bach1990 and Schoof2008 events.	CXNMiller76; Theorem2 p301; Appendix pp315–316; https://www.cs.cmu.edu/~glmiller/Publications/Papers/Mi76.pdf
K-BURGISSER04-T5.7-INDIRECT	2026-11-21 Europe/Berlin	/root/number_algorithms; GPT-6 Astra Pro; inherited effort not exposed; CX_GRH-20261121	carried as background without fault found	Theorem5.7 is used indirectly exactly as invoked in the checked proof of GCT V Theorem2.8. No independent reading or proof validation of the Burgisser2004 primary article is claimed by this citation-coverage audit. The direct source-proof event is GCT5-T2.8-T2.10-T3.4.	Burgisser04; Theorem5.7, as cited in GCT V Theorem2.8; final CX-K06
N-RONYAI92-ABSTRACT	2026-11-21 Europe/Berlin	/root/number_algorithms; GPT-6 Astra Pro; inherited effort not exposed; CX_GRH-20261121	carried as background without fault found	The final N10 passage uses only the qualified primary-abstract parameter statement recorded in the existing research notes. Its full original proof and exact theorem number were not retrieved. This audit matched the citation to the already explicit CX-N10 limitation; it makes no fresh primary-source proof-reading claim.	CXNRonyai92; primary abstract; SIAM J Discrete Math5(3)(1992)345–365; DOI10.1137/0405026
N-GAO01-INTRO-BACKGROUND	2026-11-21 Europe/Berlin	/root/number_algorithms; GPT-6 Astra Pro; inherited effort not exposed; CX_GRH-20261121	carried as background without fault found	The final N09/N10 introductory background uses Gao author pp1–2 for pre-existing randomized polynomial-time factoring, the prime-field reduction, and the Ronyai1988 nontrivial-factor parameter statement. This audit maps those background uses separately from the independently checked Gao Lemma2.6 root algorithm; no fresh primary-proof reading is claimed.	CXNGao01; author introduction pp1–2; source-root proof events N-GAO01-L2.6 and N14-S-Gao-2.6
```

## Factoring-complexity wording audit

1. The abstract explicitly preserves the degree dependence of finite-field factoring.
2. CX-N09 states `(d^{log d} log q)^{O(1)}`, calls the degree dependence quasipolynomial, and explicitly denies a general polynomial bound in `d, log q`. The statement about already existing randomized polynomial-time factorization is clearly randomized.
3. CX-N10 retains BGL smoothness/auxiliary-input parameters and the splitting-field parameter in Rónyai background. Its polynomial Fermat/Mersenne result is explicitly a special-field unconditional corollary.
4. CX-N14 gives polynomial time only with a supplied nonidentity automorphism and the stated divisibility/valuation or additional-coefficient-unit conditions. It is not presented as a complete general polynomial-time factoring algorithm.
5. CX-N15 constructs the coefficient unit in polynomial additional time, but the IKRS call remains `d^{O(log d)}(log q)^{O(1)}`. Its recursion accounting preserves the same quasipolynomial final bound. It explicitly disclaims a polynomial bound for varying degree.
6. The current `work/paper_scope.tex` CX-U03 expressly includes both N09 and N15 and says that no general deterministic polynomial-time factoring claim is made. Ensure this latest scope fragment is included in the final assembly.

## Nonblocking bibliography observations

- The earlier snapshot had three uncited Huang entries; the final refreshed bibliography has **0 uncited entries**. The retrieval record still correctly states that the Huang originals were not recovered.
- Lenstra1991 is not a gap: Theorem(1.2), p330, already has `N-LENSTRA91-T1.2`; the newly used explicit-data definition p329 and Frobenius-subfield construction p332 have the consolidated `N-LENSTRA91-EXPLICIT-SUBFIELDS` and `N15-S-AL86-BGL-Lenstra` events.
- AL86/BGL/IKRS are not untracked N15 assumptions: the corresponding exact theorem/input-interface events already exist. The main IKRS recursion remains an established source theorem rather than a claimed independent full §5 reproof.
- No shared final file was edited by this audit.
