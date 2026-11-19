INCOMPLETE

# RESEARCH_SA05 research report

This is the current checkpoint of an ongoing proof audit. It is not a completed answer to the uploaded research programme.

## Outcome table

| Item | State | Numbered statements | Exact scope or remaining gate |
|---|---|---|---|
| A.1(a) | Proved under stated hypotheses; literal monoid reading corrected | 1.1 (`A:band`); 1.4 (`A:P`) | Full Tate over all finite extensions and products; abelian part now unconditional via cited CM theorem |
| A.1(b) | Proved | 1.1 (`A:band`) | H0 is a compact protorus, not a finite-dimensional torus |
| A.1(c) | Proved under stated hypotheses | 1.5 (`A:endomorphisms`); 1.4 (`A:P`) | End means Frobenius-compatible crystalline endomorphisms |
| A.2(a) | Proved | 1.11 (`A:class`) | Standard Artin–Tate-compatible prime-to-p realization |
| A.2(b) | Proved with corrected distinction | 1.6 (`A:crystalline`); 1.7 (`A:eta`) | Fp fibre functor is neutral; geometric isocrystal gerbe is not |
| A.2(c) | Proved with repaired arguments | 1.8 (`A:real`) | Fp supersingular-curve shortcut repaired using Fp² or a Honda surface |
| A.2(d) | Proved | 1.11 (`A:class`); 1.8 (`A:real`) | Both μ2 components have invariant1/2, including p2 |
| A.3(a) | Proved unconditionally for this band | 1.9 (`A:compacthasse`); 1.10 (`A:hasse`) | Explicitly kills lim1 H1; no generic protorus claim |
| A.3(b) | Proved | 1.11 (`A:class`) | Brauer reciprocity |
| A.3(c) | Bare and unframed coherent claims proved; framed stronger claim refuted | 1.16 (`A:enrichment`); 1.17 (`A:unframed-adelic`) | Prescribed adelic Artin restrictions are essential; arbitrary incoherent families are not included |
| A.3(d) | Proved | 1.11 (`A:class`) | Compact local functional +v_p and quaternion factor, conventions explicit |
| A.4 | Strict H/G equivalence refuted; P pushout comparison proved | 1.13 (`A:comparison`); 1.14 (`A:dictionary`) | Component groups distinguish the bands |
| A.5 | Proved in corrected form | 1.15 (`A:unconditional`); 1.18 (`A:lefschetz`); 1.20 (`A:kisin`) | Independent signed Kisin and Honda–Tate checks completed |
| B.1 | Incomplete; literal continuity refuted and abelian-type comparison proved | 2.3 (`prop:B-continuity`); 2.4 (`thm:B-abelian-type`); 2.5 (`prop:B-phantom-gate`) | Under strong Tate and semisimplicity, universal comparison still requires vanishing of numerically trivial Chow phantom summands; no general vanishing proof is asserted. |
| B.2 | All Tate degrees proved; general prescribed realization remains conjectural | 2.6 (`thm:B-full-tate`); 2.8 (`cor:B-Hf-all-degrees`); 2.33 (`prop:B-general-rational-gate`) | Full étale groups retain Leopoldt/Schneider defects. Finite-condition Tate groups are unconditional; higher common Q-form identifications use chosen splittings. General M requires c0/c1 f-admissibility. |
| B.3 | Arithmetic claims refuted; finite-field equivalences proved; universal finiteness undecided | 2.9 (`thm:B-Sha-corank`); 2.10 (`ex:B-X011`); 2.17 (`thm:B-finite-chain-all-bases`); 2.14 (`prop:B-relative-curve`) | Kummer equivalence chain now covers every finite-type finite-field base, including singular and nonseparated bases. The manuscript relative-curve statement uses a regular base. Universal Tate/BSD finiteness remains open. |
| B.4 | Proved as an effective presentation and generator construction | 2.20 (`thm:B-SpecZ-Q`); 2.22 (`prop:B-integral-structure`); 2.24 (`thm:B-effective-odd-torsion`); 2.25 (`thm:B-primitive-generator`) | Every group and generator is specified by a proved terminating arithmetic/cycle procedure; arbitrary large searches are not represented as executed. |
| B.5 | Finite and Artin–Tate cases proved; general rational realization remains conjectural | 2.29 (`thm:B-finite-duality`); 2.30 (`prop:B-finite-duality-nonsep`); 2.31 (`thm:B-rational-duality`); 2.32 (`cor:B-Artin-Tate-duality`); 2.33 (`prop:B-general-rational-gate`) | Finite duality includes compact support by finite open-cover descent for nonseparated bases, real Tate modifications and characteristic-p motivic coefficients. General pure-M rational comparison requires the stated f-admissibility gate. |
| C.1(a) | General cohomological determination proved | 3.3 (`c:matrix-presentation`); 1 (`c:contraction-matrix`); 5 (`c:dimension-pair`) | Finite contraction matrices determine every relation and rank from the full cup-product tensor; closed rank formulae are supplied in the stated curve and surface cases. |
| C.1(b) | Proved | 3.2 (`c:graph-rule`) | Full graph product rule with excess Euler factors; finite checks attached. |
| C.1(c) | Incomplete; exact finite criterion proved in pure-even complex scope | 3.11 (`c:finite-even-criterion`); 3.9 (`c:curve-chow-criterion`); 3.10 (`c:surface-chow-criterion`); 3.14 (`c:k3-transcendental-gate`); 3.16 (`c:fermat-counterexample`) | Classification over arbitrary algebraically closed fields and in mixed parity remains open. For X/C with pure-even cohomology, the all-powers property has a finite tensor criterion, whose Chow vanishing is not automatically decidable. General K3 still requires wedge^(23-rho)t2(X)=0. |
| C.2 | Proved in corrected definition | 3.18 (`c:bivariant-equivalence`); 3.19 (`c:r7-audit`) | Product-square exchange and Frobenius algebra reconstruction use bivariant adjoint pairs; the effective internal-Hom error is corrected. |
| C.3 | Proved/refuted by distinguishing meanings | 3.20 (`c:lie-centre`); 3.21 (`c:serre-centre`); 3.22 (`c:finite-field-lie`) | The arithmetic invariant centre, full geometric centre and analytic Lie algebra are different objects. |
| C.4 | Proposed bound refuted; corrected bounds proved; general sharp lower endpoint unresolved | 3.24 (`c:level-counterexample`); 7 (`c:weight-level-polygon`); 3.29 (`c:broader-coefficients`); 3.32 (`c:lic-endpoint`); 3.33 (`c:abelian-invariant-weights`) | Inherited delta-dimension is required. The sharp mixed-characteristic lower endpoint is equivalent to the stated local-invariant-cycle surjectivity; abelian-type coefficient motives satisfy the endpoint. |
| C.5 | Refuted generally; positive conditions proved | 3.34 (`c:vz-positive`); 3.35 (`c:explicit-bad-reduction`) | Explicit p=2 abelian-surface example over W(k)[[u,v]]/(2-uv), with nonflat finite subgroup closure; the positive Vasiu–Zink hypotheses are retained. |
| C.6 | All abelian-type motives proved; general task incomplete | 3.39 (`c:ell-independence-abelian`); 3.41 (`c:chow-unramified-purity-reduction`); 3.43 (`c:ell-independence-gate`) | Weak Mumford–Tate lift and common finite-inertia traces prove the abelian-type case. Homogeneous Chow projectors satisfy the result under the stated Frobenius-purity hypothesis. A general proof or exact named-conjecture equivalence has not been found. |
| D.1 | Literal bridges refuted; corrected determinations proved | 4.1 (`prop:d-integral-serre`); 4.3 (`prop:d-special-fibre-false`); 4.4 (`prop:d-cm-gerbe-reduction`); 4.5 (`lem:d-power-cm-lift`); 4.6 (`cor:d-all-weil`) | Schematic closure and a rational gerbe morphism replace the false special-fibre point claim. CM lifting is for A0^m over the exact residue field Fq, not a Frobenius power or residue-field extension. |
| D.2(a) | Abelian type proved; general exact Hodge-class equivalence supplied | 4.7 (`thm:d-toric-classification`) | The exact additional CM comparison-class condition is retained in the general category, as permitted in the prompt. |
| D.2(b) | Refuted with an S4 Artin counterexample; category determined | 4.8 (`prop:d-metabelian-false`) | A quotient of the Taniyama group need not be metabelian; the closed second-derived quotient gives the requested subcategory. |
| D.2(c) | Proved | 4.9 (`prop:d-hodge-comparison`) | Aut(C) acts through Taniyama torsors and conjugation of CM types. |
| D.3 | Computed; uniqueness claim corrected | 4.10 (`thm:d-serre-finite-kernel`); 4.11 (`ex:d-non-betti`) | Finite-place-trivial Serre torsors give even-parity real Brauer vectors; the Betti functor is unique precisely in the stated rank-one case. |
| D.4 | Proved | 4.12 (`thm:d-reflex-image`); 4.13 (`cor:d-compact-image`) | The saturated character lattice and CM-type matrix determine the dimension and Mumford–Tate image. |
| E.1 | Current statement index reconciled; programme remains incomplete | `RESEARCH_SA05_results.csv` | Every numbered statement is indexed with its scoped status; unresolved original item rows remain explicit. |
| E.2 | Source records consolidated; final audit ongoing | `LITERATURE_CHECK.tsv`; `RESEARCH_SA05_references.bib` | Opening status, exact source locators and failed retrievals are retained; duplicate works are merged without dropping locator notes. |
| Lead A1 | Refuted literally; corrected P comparison proved | 1.13 (`A:comparison`) | H and G have different component groups from P |
| Lead A2 | Corrected and proved | 1.6 (`A:crystalline`) | The Z/Zhat obstruction is Frobenius continuity, not absence of Qp fibre functor over Fp |
| Lead B1 | Incomplete as universally stated | 2.1 (`prop:B-e`); 2.3 (`prop:B-continuity`); 2.5 (`prop:B-phantom-gate`); 2.33 (`prop:B-general-rational-gate`) | Restriction on the arithmetic class is proved; continuity at the geometric limit is refuted. Universal motivic comparison and general arithmetic realization retain their stated gates. |
| Lead B2 | Proved with the stated archimedean completion | 2.20 (`thm:B-SpecZ-Q`); 2.31 (`thm:B-rational-duality`) | The degree-three fundamental class, dual rank pattern and completed zeta-order interpretation are proved; the optional uniform Vandiver pattern is not asserted. |
| Lead C1 | Modified-diagonal identification proved; all-powers general K3 scope incomplete | 3.4 (`c:modified-diagonal`); 6 (`c:k3-determinant`); 3.14 (`c:k3-transcendental-gate`) | For K3, the narrow point-and-diagonal determinant first occurs on46factors; the smaller transcendental test uses divisor correspondences and does not lie in that narrow ring. |
| Lead C3 | Corrected and proved/refuted by scope | 3.20 (`c:lie-centre`); 3.21 (`c:serre-centre`) | The full geometric centre is larger than its arithmetic invariant part. |
| Lead C5 | Proved identification and explicit counterexample | 3.34 (`c:vz-positive`); 3.35 (`c:explicit-bad-reduction`) | The extension problem and a fully specified bad base with its nonflat subgroup are verified. |
| Lead D1 | Literal special-fibre bridge refuted; rational replacement proved | 4.3 (`prop:d-special-fibre-false`); 4.4 (`prop:d-cm-gerbe-reduction`); 4.6 (`cor:d-all-weil`) | Tate Frobenius refutes the special-fibre point interpretation; the rational band morphism and exact-residue CM lifting supply the replacement. |
| Lead D2 | Metabelian slogan refuted; exact category clarified | 4.7 (`thm:d-toric-classification`); 4.8 (`prop:d-metabelian-false`) | The S4 quotient and exact CM comparison-class equivalence are explicit. |
| Lead D3 | Corrected and computed | 4.10 (`thm:d-serre-finite-kernel`); 4.11 (`ex:d-non-betti`) | Finite-place-trivial Serre torsors, the norm torus in R3 and the real fibre-functor ambiguity are carefully distinguished. |

## Conventions, sources, and attribution

AI-produced by GPT-6 Astra (OpenAI, ChatGPT Pro mode). No priority is claimed and no result is attributed to a human researcher as the author of this audit. The supplied GPT-6 Astra and GPT-6.2 Astra transcriptions, together with the Claude Opus 5.5 readings, are the principal manuscript witnesses. Michel Hua's project is a separate supplied witness; no mathematical remark from it is used without explicit credit. No original manuscript scans were supplied, so this package makes no independent palaeographic certification. French quotations retain their manuscript page references; mathematical corrections are identified as corrections.

The individual part notes and bibliographies record primary sources opened and exact theorem locators. The bibliography marks opening status. The prompt's bibliographic description of Milne's 2003 *Gerbes and abelian motives* as a Math. Ann. article was not substantiated; the verified arXiv preprint is cited. Current literature was checked through 19 November2026, including the October2026 author preprint on CM Hodge classes; its preprint status is retained.

## Computations and their limits

- `code/check_lefschetz_counterexample.py` computes the degree-eight polynomial, exact irreducibility over Q, and both F5 point counts. Its JSON records every finite input. The passage to the Lefschetz and Weil bands is proved in the paper, not inferred solely from the computation.
- `code/check_enriched_gerbe.py` checks the four quadratic-residue obstructions at5,7,13. Its JSON includes measured runtime.
- Part B includes certified PARI/GP computations of X0(11) and the rank-two curve389, without BSD assumptions; the command, version, rank bounds, generators, discriminant and torsion outputs are retained.
- Part C includes graph-product and tautological-dimension checks, the F5 elliptic level counterexample, and exact integer-polynomial verification of the explicit bad-reduction subgroup embeddings. The scripts and outputs state their scopes.
- Part D includes CM-type and reflex-rank enumeration and finite-field checks of the CM twist examples. These are finite certificates for the examples, not proofs of the global lifting theorem.
- Primary-source retrieval scripts record URLs, SHA256 digests, success/failure, and measured times. Full downloaded primary PDFs and extracted copyrighted source text are not republished in this ZIP.

## Corrections and rejected proof steps

Part A's note lists its corrections in detail: the Weil monoid must be group-completed; Artin-only rigidification has bandG0, notH; the crystalline Qp fibre functor overFp is genuine; the geometric isocrystal gerbe is different; gerbe and endomorphism Brauer classes have opposite signs under the declared cocycle convention; the protorus Hasse proof requires control of lim1; the full, connected, and Tate-rigidified bands cannot be identified; and a bare gerbe class does not choose framed local neutralizations. An early four-candidate omission in the framing example was replaced by the explicit p2 example.

Part B corrects missing Beilinson hypotheses, ordinary versus compactified Weil-etale groups, integral2-torsion omitted by R5, f versus g conditions at inverted primes aboveell, and the abstract-rank subtraction in the arithmetic corank formula. Part C distinguishes a disproved bound from an unproved proof, records the degree convention in the modified diagonal, and retains the all-powers K3 gate. Part D corrects the reading of closure (schematic, not profinite), the special-fibre Frobenius bridge, the missing CM twisting unit, and the metabelian slogan. The part ledgers give exact manuscript pages and replacement statement labels.

## Typesetting and build verification

The paper is built with LuaLaTeX and BibTeX in this environment, with an author-year bibliography. The first complete build had two overfull boxes above2pt:3.06645pt and13.71478pt. Those source paragraphs were corrected before checkpoint01. The dated verification entries below give each later build and rendered-page inspection. Initial unavailable TeX format and font dependencies were reconstructed locally; the reproducible build script and dependency retrieval records are included.

## Open work and attempted approaches

The progress ledger records every current main gate. We have not declared an item complete merely because it was reduced to a named conjecture unless the prompt explicitly accepts that exact equivalence. All-powers K3 Chow relations remain undecided. The integral SpecZ groups and generators now have a proved effective determination by terminating arithmetic and cycle searches. For K3, the three-factor Beauville–Voisin relation does not remove the degree23 antisymmetrizer gate; the current2026 special-family theorem does not cover general K3 surfaces. For integral SpecZ, rational Borel ranks do not compute all finite K-theory groups; the current partial-regularity result does not settle Vandiver. For independence ofell, the proved abelian-type case changes the generator and controls finite descent; the general-motive question remains undecided.

No substantive file is silently dropped. Earlier drafts remain superseded by the current section files; the mathematical changes and reasons are recorded above and in the part notes. Build intermediates, downloaded third-party dependencies, raw sources, and rendered QA pages are reproducible working files and are excluded from the deliverable ZIP.

### Checkpoint 01 historical audit update (03:35 UTC)

The independent reader accepted the relative-class counterexample and identified a missing Honda–Tate dimension check in the Lefschetz example; that check has been added. The Kisin character-sign dictionary is still under audit and is explicitly marked provisional in the paper. A.5 therefore remains incomplete at this checkpoint.

### Checkpoint 01 PDF verification

The final checkpoint build has56pages and zero overfull boxes (down from two above2pt). Pages1,7,14,24,27,35,40,49,56 were rendered and inspected; formulas, text, margins, and pagination were legible. The repaired R3 paragraph was additionally rendered at its new page location. The checkpoint remains a research draft, not a completed theorem package.

## Changes after checkpoint 01

The Kisin sign comparison is now proved: his source gerbe uses the negative arithmetic fundamental class and his slope cocharacter is also negative. Inverting the source band identifies the conventions; the target Weil-number band is unchanged. The Honda–Tate local-index calculation in the explicit Lefschetz example has been independently checked.

For A.3(c), the paper now proves the unframed coherent adelic classification separately from the framed counterexample. Matching the prescribed Artin restrictions lifts the difference torsors to the connected band P. Milne's global-to-adelic H1 isomorphism supplies the global equivalence; its lift to H preserves the global Artin–Tate rigidification. There is no claim that arbitrary independent local choices satisfy the necessary adelic condition.

The odd-primary terms in the integral number-ring calculation now have a terminating finite arithmetic presentation. The proof includes a finite prime bound, an explicit discriminant and defining-polynomial bound, compact-support cocycle matrices, their Pontryagin duals, and a proved stopping criterion. The 2-primary groups and their generators are explicit. The primitive free-generator construction is separately audited; no conjectural uniform vanishing pattern is inserted into the table. The small finite-group program checks eight cyclic/S3 presentations in exact arithmetic; it does not run the enormous number-field enumeration. Its measured runtime is in `code/check_finite_cocycle_presentation_output.json`.

For C.6, all rational motives of abelian type are now covered, including arbitrary initial bad reduction and residue characteristic2. The proof changes the abelian generator using Noot's weak Mumford–Tate lift, proves potential good reduction, then returns to the original field by induction. Inertia acts through one finite quotient on the new ambient object. Its graphs are Lefschetz classes, so the October2026 rationality theorem gives common rational traces on every Hodge projector. Finite-order trace equal to dimension forces the identity. The argument does not assert full Weil–Deligne compatibility. The general-motive question remains incomplete.

The sharp level bounds in C.4 are proved with the inherited dimension function, including the margin's relative-dimension hypothesis. The strengthened bound stated in the prompt is false. The sharp mixed-characteristic weight endpoint for degree0 and nonconstant positive-weight coefficients remains an exact local-invariant-cycle gate. The general K3 all-powers Chow relation remains unproved. A withdrawn October2026 preprint on products of K3 surfaces is not used.

The canonical results index is now generated from every numbered statement in the TeX sources, including included subsections, with balanced-brace status parsing and compiled theorem numbers. The individual per-item ledgers are retained alongside it. This replaces the earlier mixed item/statement index; no mathematical assertion is dropped.

### Checkpoint 02 verification (04:20 UTC)

The current PDF has81pages,92numbered statement records and209check events. The LuaLaTeX build has zero overfull boxes and no undefined citations or references. Pages1,11,21,31,41,51,61,71,81 were rendered and visually inspected; text, formulae and margins are legible. The final bookmark-only correction leaves the visible layout unchanged. The original first build had two boxes above2pt; checkpoint01 and checkpoint02 both have zero. Unchanged outputs are referenced to checkpoint01 in the new manifest; all current deliverables, sections, notes and programs are included. The programme remains INCOMPLETE because unresolved item rows remain active.

## Changes after checkpoint02

The finite-field Kummer equivalence chain now covers arbitrary finite-type bases. Its extension uses a finite smooth alteration cover only to control and split the section module; it does not assume injectivity of the full first cohomology pullback. The regular-base relative Brauer/Jacobian proof already covers the manuscript's stated hypotheses. The separate universal finiteness question remains unresolved.

All finite-condition Tate degrees and their common Q-forms are now specified. The source audit removed a proposed canonical degree-two identification: Fontaine's original exact sequences provide compatible vector-space descriptions only after choices of splittings. Rational Artin–Tate duality is included, while the general pure-motive realization gate is kept explicit. The source actually opened for the local/global finite-complex formalism is Fontaine's1992 Bourbaki text; the later full Fontaine–Perrin-Riou chapter remains marked not obtained.

For the rational cohomology algebra of a smooth projective complex variety with no odd cohomology, invariant theory gives an effective finite list of tensor relations whose Chow vanishing is equivalent to all point-and-diagonal cohomological relations holding in every power. Effectiveness here constructs the list; it does not decide whether a given cycle is rationally equivalent to zero. General mixed parity remains unresolved. The general K3 obstruction has been reduced to the transcendental motive, and the distinction between its divisor-defined projector and the narrower point-and-diagonal ring is explicit.

The bibliography now uses one citation key for each verified duplicate work while preserving all theorem and page locators from the individual audits. The root literature ledger includes the original per-part retrieval evidence, source scope checks and unsuccessful retrievals. The report's outcome table resolves labels to compiled statement numbers. These editorial corrections do not count as mathematical progress under the user's stopping rule.

New reproducible programs in this interval include follow-up primary-source retrieval with byte counts, hashes and timings; rendering selected pages of Fontaine's1992 source (pages11,12,13,18, with pages12–13 visually inspected); duplicate-reference canonicalization; source-ledger consolidation; and item-table reconciliation. Their output files state their scope and measured runtime. The downloaded copyrighted sources and rendered inspection images remain excluded from the checkpoint ZIP.

### Checkpoint 03 verification

The verified PDF has98pages and110numbered statement records. The final LuaLaTeX log has zero overfull boxes and no undefined citations or references. In this expansion an unbreakable program path produced one35.33685pt overflow; a breakable path fixed it. The three source syntax errors encountered during integration were repaired before this final build. Pages1,13,23,25,31,32,37,41,42,43,45,46,50,53,54,55,56,57,58,59,60,62,74,77,86,98 were rendered and visually inspected, including the repaired passage and the new proof sections. Text, formulae and margins are legible.

The source bibliography contains103canonical entries, each with explicit opening status, and the consolidated literature ledger contains125work records. Every numbered statement has a matching check-event label. There are353event records, including88explicit cross-reference records that link preserved checks to numbered statements; those links are not new independent checks. The item table resolves all statement labels to their compiled numbers. This verifies the checkpoint contents and does not declare the research programme complete.
