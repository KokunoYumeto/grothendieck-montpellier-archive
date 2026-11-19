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
| B.1 | Incomplete; literal continuity refuted and abelian-type comparison proved; remaining index set reduced | 2.3 (`prop:B-continuity`); 2.4 (`thm:B-abelian-type`); 2.5 (`prop:B-phantom-gate`); 2.6 (`prop:B-diagonal-Chow-gate`); 2.7 (`prop:B-rational-blowup-gate`); 2.8 (`prop:B-surface-supported-CH2`); 2.9 (`cor:B-uniruled-threefold`); 2.10 (`prop:B-limit-diagnostics`); 2.11 (`prop:B-fixed-open-ramification-obstruction`); 2.12 (`prop:B-Milnor-divisible-kernel`); 2.13 (`cor:B-Milnor-free-quotient`) | Under universal Tate and semisimplicity, comparison reduces to Chow-cycle injectivity in codimension m on varieties of dimension 2m−1, m≥2. The first case is codimension2 on threefolds; it is now proved for universal surface-supported zero-cycles, including geometrically uniruled threefolds. No Parshin or higher-codimension conclusion follows for an individual such variety. The rational blow-up test class retains arbitrary centres and is not counted as a further resolution. The new limit diagnostics refute two shortcuts involving continuous-cohomology colimits and completed Frobenius modules; they do not prove the required uniform ramification control. On the specified two-boundary open in P4, the comparison cokernel is exactly im(G) intersect ker(cl) on its threefold components. This fixed-open formula neither proves vanishing nor proves survival under further shrinking. The ordinary Milnor regulator has exactly the infinitely ell-divisible kernel in every degree; the residue criterion holds in positive degree. This uses the diagonal twist and does not remove the weight-zero part of the degree-three/twist-two residue gate. The separated ordinary Milnor quotient is countably free and has the same completion. A fully explicit free submodule of a sum of finite permutation lattices nevertheless acquires eigenvalue4 after3-adic completion, so freeness does not control the missing completed eigenclasses. The separated quotient is in fact canonical and common to every coefficient prime different from p: divisibility maps trivially into any of the proved free quotients. The same formal integral module can nevertheless have a completed eigenvalue at3 and none at any other prime, so the common quotient does not resolve the required comparison. |
| B.2 | Tate determination proved; corrected general conjecture formulated and its specializations proved | 2.14 (`thm:B-full-tate`); 2.16 (`cor:B-Hf-all-degrees`); 2.17 (`def:B-corrected-comparison-package`); 2.18 (`prop:B-comparison-specializations`); 2.19 (`prop:B-Scholbach-finite-support`) | Full étale groups retain their exact Leopoldt/Schneider defects; finite-condition Tate groups are unconditional. The requested general-M formulation explicitly adds finite-field and gluing clauses to Fontaine f-admissibility. Universal existence remains conjectural; Scholbach ordinary Hom fails the full odd-Weil requirement on a finite-support motive. |
| B.3 | Arithmetic and full-Brauer claims refuted; whole prime-to-p arbitrary-base equivalences proved; universal finiteness undecided | 2.20 (`thm:B-Sha-corank`); 2.22 (`ex:B-X011`); 2.29 (`thm:B-finite-chain-all-bases`); 2.34 (`thm:B-all-bases-surface-gate`); 2.35 (`prop:B-integral-torsor-lattice`); 2.40 (`thm:B-all-bases-Brauer-units`); 2.41 (`cor:B-all-bases-relative-Brauer`); 2.43 (`thm:B-Brauer-prime-uniform`); 2.44 (`cor:B-torsors-prime-uniform`); 2.46 (`thm:B-irregularity-zero-surface-gate`); 2.48 (`cor:B-canonical-surface-gate`); 2.49 (`thm:B-simply-connected-surface-gate`); 2.50 (`thm:B-Brauer-characteristic`) | The full-Brauer assertion has explicit infinite 2-torsion over A1/F2. The whole prime-to-p abelian-torsor finiteness and relative-curve Brauer finiteness assertions over every finite-type base are equivalent to divisor Tate for surfaces over all finite constants. Unit cups remove the singular/nonproper base obstruction. The fixed-field reduction now restricts the remaining Tate hypothesis to smooth projective geometrically integral surfaces with trivial geometric etale fundamental group, H1(O)=0 and very ample canonical bundle, retaining all previous numerical thresholds and slope conditions. A finite etale cover, the generic isogeny, a new Yuan model and ample cuts prove the reduction over the unchanged finite field. Free cyclic Fermat quotients prove that the intrinsic subclass is proper after finite constants. This restricted Tate conjecture remains unproved. |
| B.4 | Proved as an effective presentation and generator construction | 2.52 (`thm:B-SpecZ-Q`); 2.54 (`prop:B-integral-structure`); 2.56 (`thm:B-effective-odd-torsion`); 2.57 (`thm:B-primitive-generator`) | Every group and generator is specified by a proved terminating arithmetic/cycle procedure; arbitrary large searches are not represented as executed. |
| B.5 | Finite and Artin–Tate cases proved; general rational realization remains conjectural | 2.61 (`thm:B-finite-duality`); 2.62 (`prop:B-finite-duality-nonsep`); 2.63 (`thm:B-rational-duality`); 2.64 (`cor:B-Artin-Tate-duality`); 2.66 (`prop:B-general-rational-gate`); 2.65 (`prop:B-finite-field-coefficient-gate`) | Finite duality includes compact support by finite open-cover descent for nonseparated bases, real Tate modifications and characteristic-p motivic coefficients. General pure-M rational comparison requires the stated f-admissibility gate. For the specified rational Weil extension of all Chow-heart coefficients, perfect duality is equivalent to Beilinson plus Parshin and is already detected on P1 with constant coefficients. This stronger coefficient scope is distinguished from homogeneous pure summands; it does not resolve arithmetic f-admissibility. |
| C.1(a) | General cohomological determination proved | 3.3 (`c:matrix-presentation`); 2 (`c:contraction-matrix`); 6 (`c:dimension-pair`) | Finite contraction matrices determine every relation and rank from the full cup-product tensor; closed rank formulae are supplied in the stated curve and surface cases. |
| C.1(b) | Proved | 3.2 (`c:graph-rule`) | Full graph product rule with excess Euler factors; finite checks attached. |
| C.1(c) | Incomplete; finite all-power criterion proved without C+ for arbitrary Weil coefficients | 3.19 (`c:covariant-polynomial-lifting`); 3.20 (`c:finite-unconditional-criterion`); 3.21 (`c:finite-power-cutoff`); 3.23 (`c:uniform-arity-bound`); 3.24 (`c:uniform-arity-scope`); 3.9 (`c:curve-chow-criterion`); 3.10 (`c:surface-chow-criterion`); 3.27 (`c:k3-transcendental-gate`); 3.29 (`c:fermat-counterexample`) | The finite rational Chow criterion and a single finite-power test require no algebraic parity projector or rational form of the Weil cup algebra. A total computable arity bound depending only on dimension and super-Betti dimensions is proved for rational cohomology tables; exact coefficient presentations give the stated larger bound. Actual finite Chow vanishings remain undecided in general; K3 still requires wedge^(23-rho)t2(X)=0. |
| C.2 | Proved in corrected definition | 3.31 (`c:bivariant-equivalence`); 3.32 (`c:r7-audit`) | Product-square exchange and Frobenius algebra reconstruction use bivariant adjoint pairs; the effective internal-Hom error is corrected. |
| C.3 | Proved/refuted by distinguishing meanings | 3.33 (`c:lie-centre`); 3.34 (`c:serre-centre`); 3.35 (`c:finite-field-lie`) | The arithmetic invariant centre, full geometric centre and analytic Lie algebra are different objects. |
| C.4 | Proposed bound refuted; corrected bounds and low-weight sharp endpoint proved; higher endpoint unresolved | 3.37 (`c:level-counterexample`); 13 (`c:weight-level-polygon`); 3.42 (`c:broader-coefficients`); 3.45 (`c:improved-zero-weight`); 3.46 (`c:threefold-weight-gate`); 3.47 (`c:threefold-pairing-kernel`); 3.48 (`c:threefold-divisor-split`); 3.49 (`c:threefold-pairing-scope`); 3.57 (`c:lic-endpoint`); 3.58 (`c:abelian-invariant-weights`); 3.50 (`c:threefold-target-positivity`); 3.53 (`c:exterior-weight-criterion`); 3.54 (`c:universal-trait-weight-equivalence`); 3.55 (`c:single-endpoint-insufficient`); 3.56 (`c:trait-exterior-scope`); 3.51 (`c:threefold-simple-spectrum`); 3.52 (`c:threefold-simple-spectrum-scope`) | For R0 the upper weight is at most 0, 1, or 2j−2 for j=0, j=1, or j≥2, respectively. The expected endpoint holds for j≤2 and abelian-type coefficients. The first mixed-characteristic threefold case has an exact radical-quotient kernel and primitive restriction-image criterion. Its rational divisor-image part splits off; identifying the remainder with the transcendental restriction image additionally uses surface Tate. The residual pairing is unresolved. Positivity on the surface-square target together with homological=numerical equivalence on the mixed threefold-surface product is a proved sufficient package. Its unresolved product hypotheses do not prove the residual pairing. The universal middle-degree trait endpoint is equivalent to weight–monodromy; an individual j-fold has a finite exterior-power test with r<=j+1. Both universal assertions remain unresolved, and the arbitrary-morphism transfer is separately scoped. A globally squarefree primitive target Frobenius polynomial replaces the target Hodge-positivity hypothesis in a proved sufficient subcase, with mixed numerical=homological equivalence retained. No universal transfer supplies these conditions. The additional transfer attempt proves that constant-field extensions, smooth projective surface alterations and nonzero Artin-factor twists cannot remove a repeated primitive Frobenius root. This is a limitation of those transfers to the sufficient squarefree case, not a theorem excluding every possible geometric transfer. |
| C.5 | Refuted generally; positive conditions proved | 3.59 (`c:vz-positive`); 3.60 (`c:explicit-bad-reduction`) | Explicit p=2 abelian-surface example over W(k)[[u,v]]/(2-uv), with nonflat finite subgroup closure; the positive Vasiu–Zink hypotheses are retained. |
| C.6 | Abelian-type and stated geometric cases proved; motivated rank implication proved conditionally; general task incomplete | 3.64 (`c:ell-independence-abelian`); 3.66 (`c:chow-unramified-purity-reduction`); 3.68 (`c:surface-lowdegree-chow-unramified`); 3.69 (`c:hyperkahler-chow-unramified`); 3.70 (`c:chow-unramified-rank-reduction`); 3.72 (`c:motivated-unramified-rank-reduction`); 3.73 (`c:motivated-abelian-strata-unramified`); 3.74 (`c:motivated-rank-reduction-scope`); 3.77 (`c:ell-independence-gate`); 3.75 (`c:local-global-motive-approximation`); 3.76 (`c:bgv-pure-local-boundary`) | Common finite-inertia traces prove the abelian-type case, and the stated purity cases hold at the original place. The published finite-field correspondence-rank conjecture now implies independence of every monodromy rank and of the unramifiedness flag for all Andre motivated motives; the proof uses finite graph constraints on whole-product Lefschetz expressions and simultaneous conjugate semistable alterations. Actual rational Chow abelian-type presentations of every auxiliary stratum give an unconditional special criterion. The general assertion and an exact named-conjecture converse remain unresolved. Finite-prime local/global approximation proves equivalence of the universal number-field and p-adic pure-motive formulations. A finite-field cycle still lacks the pure local realization needed for the attempted converse; occurrence among semistable strata is insufficient. The inspected conductor formulas do not supply the missing ordinary inertia-invariant dimension: their additive derived-inertia scalar trace ignores the nilpotent rank even after a supplied homogeneous projector. |
| D.1 | Literal bridges refuted; corrected determinations proved | 4.1 (`prop:d-integral-serre`); 4.3 (`prop:d-special-fibre-false`); 4.4 (`prop:d-cm-gerbe-reduction`); 4.5 (`lem:d-power-cm-lift`); 4.6 (`cor:d-all-weil`) | Schematic closure and a rational gerbe morphism replace the false special-fibre point claim. CM lifting is for A0^m over the exact residue field Fq, not a Frobenius power or residue-field extension. |
| D.2(a) | Abelian type proved; general exact Hodge-class equivalence supplied | 4.7 (`thm:d-toric-classification`) | The exact additional CM comparison-class condition is retained in the general category, as permitted in the prompt. |
| D.2(b) | Refuted with an S4 Artin counterexample; category determined | 4.8 (`prop:d-metabelian-false`) | A quotient of the Taniyama group need not be metabelian; the closed second-derived quotient gives the requested subcategory. |
| D.2(c) | Proved | 4.9 (`prop:d-hodge-comparison`) | Aut(C) acts through Taniyama torsors and conjugation of CM types. |
| D.3 | Computed; uniqueness claim corrected | 4.10 (`thm:d-serre-finite-kernel`); 4.11 (`ex:d-non-betti`) | Finite-place-trivial Serre torsors give even-parity real Brauer vectors; the Betti functor is unique precisely in the stated rank-one case. |
| D.4 | Proved | 4.12 (`thm:d-reflex-image`); 4.13 (`cor:d-compact-image`) | The saturated character lattice and CM-type matrix determine the dimension and Mumford–Tate image. |
| E.1 | Current statement index reconciled; programme remains incomplete | `RESEARCH_SA05_results.csv` | Every numbered statement is indexed with its scoped status; unresolved original item rows remain explicit. |
| E.2 | Source records consolidated and audited within the stated retrieval limits | `LITERATURE_CHECK.tsv`; `RESEARCH_SA05_references.bib` | Every recorded source retains its actual opening status, exact local theorem/page scope and failed retrievals. Bibliography and check-event reconciliation passed. This is a completed record of the work performed, not a claim that uninspected source proofs or unresolved mathematics have been completed. |
| Lead A1 | Refuted literally; corrected P comparison proved | 1.13 (`A:comparison`) | H and G have different component groups from P |
| Lead A2 | Corrected and proved | 1.6 (`A:crystalline`) | The Z/Zhat obstruction is Frobenius continuity, not absence of Qp fibre functor over Fp |
| Lead B1 | Incomplete as universally stated | 2.1 (`prop:B-e`); 2.3 (`prop:B-continuity`); 2.6 (`prop:B-diagonal-Chow-gate`); 2.17 (`def:B-corrected-comparison-package`) | Restriction on the arithmetic class is proved; continuity at the geometric limit is refuted. Universal finite-field comparison has the odd-dimensional middle-plus-one cycle gate; the general arithmetic comparison is precisely formulated as a conjectural package. |
| Lead B2 | Proved with the stated archimedean completion | 2.52 (`thm:B-SpecZ-Q`); 2.63 (`thm:B-rational-duality`) | The degree-three fundamental class, dual rank pattern and completed zeta-order interpretation are proved; the optional uniform Vandiver pattern is not asserted. |
| Lead C1 | Modified-diagonal identification proved; all-powers general K3 scope incomplete | 3.4 (`c:modified-diagonal`); 12 (`c:k3-determinant`); 3.27 (`c:k3-transcendental-gate`) | For K3, the narrow point-and-diagonal determinant first occurs on46factors; the smaller transcendental test uses divisor correspondences and does not lie in that narrow ring. |
| Lead C3 | Corrected and proved/refuted by scope | 3.33 (`c:lie-centre`); 3.34 (`c:serre-centre`) | The full geometric centre is larger than its arithmetic invariant part. |
| Lead C5 | Proved identification and explicit counterexample | 3.59 (`c:vz-positive`); 3.60 (`c:explicit-bad-reduction`) | The extension problem and a fully specified bad base with its nonflat subgroup are verified. |
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

## Changes after checkpoint03

The full, unqualified relative Brauer assertion on12:79 is false. For S=A1 over F2 and E:y^2+y=x^3, the Frobenius kernel alpha2 gives F2[t]/F2[t^2] inside H1(S,E)[2]. The zero section splits the derived pushforward of Gm and injects these classes into Br(E times S)/Br(S). The proof gives actual two-torsion classes and does not use a prime-to-characteristic proper-base-change argument. The corresponding prime-to-p equivalences remain proved, while their universal finiteness remains open.

For C.4 the new R0 bound is max(0,2j−2), with the separate value1 at j=1. It proves the expected weight-j endpoint for j≤2. After normalization to middle degree, the first remaining trait case is H3 of a semistable projective threefold in mixed characteristic, where the requested endpoint is exactly equivalent to H3 weight-monodromy. The argument checks the extreme Rapoport-Zink maps through finite-strata and Picard polarizations and supplies the finite-residue trait selection needed for general stalks. The opened2026 source has an erroneous sign in a printed hard-Lefschetz twist; the paper states the correct sign and does not use that faulty formula.

For C.1 a projective-superrepresentation construction gives a finite necessary-and-sufficient list under C+(X), the existence of an algebraic cohomological parity projector. It uses neither an idempotent lift of parity in Chow nor a parity correspondence belonging to the narrow point-and-diagonal ring. The latter stronger requirement is independently disproved by the positive pair E times P1. The finite criterion does not settle arbitrary Chow vanishing or the general K3 finite-dimensionality question.

The characteristic-two Brauer and the Kahn-route normalization examples have explicit finite certificates with their code and measured runtime. The super criterion has exact small signed-tensor certificates checking rectangular identities and the difference between zero superdimension and positive parity trace; those finite tests supplement the general proofs and are not represented as proving them.

### Arbitrary Weil coefficient scope checked

The finite criterion extends to rational relations for any characteristic-zero Weil coefficient field by taking the rational kernel of the super-orbit pullback. This requires no rational form of the cup algebra. A finite presentation of its coefficient algebra suffices for effective elimination; an opaque coefficient field gives finite existence only. The criterion remains conditional on algebraic parity C+, except in the stated finite-field cases where the Katz–Messing Frobenius-projector argument supplies it. Relations after extending Chow coefficients to the Weil field are explicitly treated as a separate convention.


## Final mathematical additions before checkpoint04

B.1 now has a strictly smaller universal cycle gate, under the same universal Tate and semisimplicity hypotheses: only codimension m on varieties of dimension2m−1, m≥2, is required. The published Balkan–Schreieder upper-half reduction and an explicit split projective-space product prove the reduction. The first case is codimension2 on threefolds, equivalently the stated H4(F0 P4,Qell(3)) invariant vanishing under the fixed Tate assumptions. It is not claimed to imply all higher cases by itself.

B.3's intended regular separated-base prime-to-p relative-curve assertion is now equivalent to Tate divisors on smooth projective surfaces over the prime field, with finite constant extensions included. Equivalently its gate is H3(F0 P3_Fbarp,Qell(2))^GammaFp=0. The proof preserves the nonproper arithmetic cohomology term and shows it comes from the base; the pencil converse uses its extending section to kill the base Brauer ambiguity. Arbitrary singular/nonseparated-base equivalence chains remain separately recorded, without promoting this surface reduction to that larger scope.

B.2's requested general conjectural formulation and its specializations are now explicitly supplied. The formulation states the additional finite-field and gluing hypotheses instead of claiming that Bloch–Kato degree1 constructs them. The Tate determination and the two implications are proved. The conjectural global completion is not asserted to exist. B.5's requested general pure-motive duality proof remains open. The specified finite-support object gives a direct refutation of identifying Scholbach's ordinary Hom theory with the entire absolute Weil theory.

C.6 has a further proved case for homogeneous algebraic Chow summands of tensor constructions on hyper-Kähler varieties. The opened Ito–Zou purity theorem supplies the necessary ambient purity at the original local field. This does not settle the general-motive row and is not counted as closing that gate. The new K3 nilpotence and specialization attempts give no smaller proved general K3 gate; their precise failures remain recorded.

### Checkpoint 04 verification

The verified PDF has 117 pages and 126 numbered statement records. The final LuaLaTeX log has zero overfull boxes and no undefined citations or references. For checkpoint 04, both the first complete build of the expanded manuscript and the final build had zero overfull boxes; the final build also has no LaTeX or BibTeX warnings. Earlier integration repairs remain recorded in their own checkpoint entries. Pages 1, 16, 20, 21, 25, 26, 27, 28, 30, 37, 38, 39, 40, 41, 44, 59, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 74, 85, 86, 87, 88, 96, 97, 102, 117 were rendered and visually inspected, including the new proof sections. Text, formulae and margins are legible.

The source bibliography contains 123 canonical entries, each with explicit opening status, and the consolidated literature ledger contains 147 work records. Every numbered statement has a matching check-event label. There are 444 event records, including 106 explicit cross-reference records that link preserved checks to numbered statements; those links are not new independent checks. The item table resolves all statement labels to their compiled numbers. This verifies the checkpoint contents and does not declare the research programme complete.

## Late proof after the checkpoint typesetting freeze

After the PDF was frozen, the complete proof in part_b/b3_all_bases_surface_gate_audited_draft.md passed B, D and root audits. It extends the surface-Tate equivalence to abelian schemes over every finite-type base. The numbered PDF and outcome-table scope for this extension await integration in the next checkpoint; the full proof and root check event are already preserved here. The formal review counts this movement now. It does not settle the arbitrary-base relative-curve Brauer quotient or prove surface Tate.

## Scheduled progress review01

The first formal three-hour review was completed at05:50:13UTC. The dated ledger lists every mathematically open row, the smallest remaining gates, the unsuccessful approaches and the actual movements. The no-movement count is0; work continues. The complete item snapshot is `progress/review_01.json`. This is not an overall-completion declaration.


## Changes after checkpoint04

The general finite C.1 criterion now has no C+ hypothesis. The proof first uses the point augmentation and the higher modified diagonal to reduce to finitely many scalar forms. Its finite orbit-ideal relations lift inside fixed-degree covariant polynomial representations, whose Schur superalgebra is semisimple in characteristic zero. A rectangular Young relation makes every representation-theoretic equality valid in Chow. The resulting finite-power cut-off has the same exact coefficient-input qualification as the construction. This does not decide rational equivalence or prove the general K3 determinant cycle vanishes. The earlier C+ criterion remains a correct, superseded sufficient method; it has not been silently deleted.

The finite-field B.3 surface gate now controls localized integral torsor groups on every base, including their non-torsion part, and full localized H2(Gm) on proper singular bases. The latter uses only the degree-two injection from etale to v-cohomology after perfection, not an unproved all-degree comparison. Jaffe's opened Theorem10.11 gives the Picard localization; Proposition10.8 is an opened statement whose source refers its proof elsewhere. The relative Picard degree obstruction is removed, while the nonproper base-image issue is being attacked separately.

The additional C.6 case covers homogeneous algebraic Chow summands built from surfaces and supplied low-degree homogeneous summands. The hard-Lefschetz retraction is used as a Galois map, with no claim that its inverse is algebraic. The B.1 blow-up construction gives explicit split maps into rational test varieties but preserves the original phantom obstruction, so it is not counted as progress toward vanishing.

Checkpoint04's save was observed to succeed; its complete current deliverables and the first formal review are preserved in that immutable archive. Its PDF has 117 pages, no overfull boxes, no unresolved citations or references, and no LaTeX/BibTeX warnings. The verification record identifies the 35 pages actually inspected. Subsequent changes in this section belong to checkpoint05.


## Arbitrary-base Brauer saturation removed

The separate singular, nonproper base-image gate in B.3 is now removed. Under divisor Tate for all smooth projective surfaces over finite extensions of F_p, arithmetic character cups with global units generate Br′(S)[ell-infinity] up to a finite group for every finite-type F_p-scheme S, with ell≠p. More precisely, full H2_et(S,Gm) tensor Z_(ell), modulo the divisible unit-cup image, is finitely generated. The proof uses a finite-type h-cover by smooth quasi-projective alteration opens, the degree-two perfection/v-descent injection, a finite valuation-matrix bound on the cup kernel, and a uniform finite-error unit equalizer. It neither assumes full H2 is torsion nor discards the arithmetic contribution on an open base.

For any morphism identifying global units, the relative ell-primary Brauer cokernel is consequently finite. This includes every smooth proper curve family with geometrically connected fibres over every finite-type base, including singular, nonreduced and nonseparated ones. The converse follows from the earlier pencil family. Thus both universal questions in B.3 for each fixed prime ell≠p now have exactly the surface-Tate gate, equivalently the already proved single H3(F0 P3_Fbarp,Qell(2)) invariant gate. The conjecture itself remains unresolved. The literal unrestricted full-Brauer assertion remains refuted by the explicit characteristic-two family.

This is a substantive removal of the remaining base-image obstruction after formal review01. The intermediate proper-base theorem and integral torsor-lattice theorem remain valid and are retained as separately scoped results. The root, B and D checks are recorded individually; the source record distinguishes statements opened from complete proofs read. No novelty or priority is claimed.


## Computable uniform cutoff in its exact coefficient scope

The unconditional finite criterion now has a total computable arity bound depending only on dimension and the even and odd Betti dimensions whenever the graded cohomology algebra has a rational table. The argument gives its own recursive Groebner bound by a finite controlled Dickson tree, then converts the schematic super-orbit ideal to an ordinary elimination problem using a square-zero module encoding. Rational Betti cohomology is within this scope. For a presented coefficient algebra, an explicit larger bound also depends on the number and relation degrees of named coordinates of every scalar form. Those coefficient variables must be eliminated to obtain rational relations. Arbitrary unspecified Weil coefficients retain finite existence, without the asserted uniform bound.

The complete proof passed the owner, root and D written checks. The exact code verifies small controlled trees and one super-elimination mechanism only; no enormous geometric bound and no Chow vanishing was computed. This strengthens the finite criterion but is not counted as a separate resolution of the remaining general Chow gate. The programme remains incomplete.


## Checkpoint05 integration repairs

The first complete build of the expanded manuscript had one 7.03163pt display overflow and one unresolved citation key. Splitting the proper-base statement over two display lines repaired the overflow. Adding the already-opened Colliot–Thelene–Skorobogatov source fragment to bibliography consolidation resolved the citation. The final build has neither defect and has no LaTeX or BibTeX warnings. The 33-page visual sample includes every newly added proof section; the repaired display and the dense finite-criterion, elimination-bound and low-degree-purity pages were additionally inspected at full rendered size.

### Checkpoint 05 verification

The verified PDF has 136 pages and 144 numbered statement records. The final LuaLaTeX log has zero overfull boxes and no undefined citations or references. Any earlier integration repairs are recorded separately in this report. Pages 1, 18, 20, 21, 35, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 52, 68, 80, 81, 82, 83, 84, 85, 86, 87, 88, 102, 112, 113, 114, 119, 136 were rendered and visually inspected, including the new proof sections. Text, formulae and margins are legible.

The source bibliography contains 148 canonical entries, each with explicit opening status, and the consolidated literature ledger contains 176 work records. Every numbered statement has a matching check-event label. There are 568 event records, including 131 explicit cross-reference records that link preserved checks to numbered statements; those links are not new independent checks. The item table resolves all statement labels to their compiled numbers. This verifies the checkpoint contents and does not declare the research programme complete.

## Whole prime-to-p extension preserved as a proof note

During the checkpoint05 main-file freeze, a complete extension of the arithmetic-unit proof was independently checked. Under divisor Tate for surfaces at one fixed prime different from p, it proves one finite unit-cup cokernel across all primes different from p, first on smooth quasi-projective schemes and then on every finite-type base by the same Z[1/p] descent. Its complete proofs are preserved in the Part B and Part D pending-integration notes. The numbered theorem in this checkpoint remains the earlier fixed-prime theorem; the stronger checked proof is not omitted merely because typesetting is pending.

The smooth-source proof uses the Hochschild–Serre filtration, finite H1 of the geometric Picard group, and arithmetic units generating H2 of geometric units. An integral Gysin map descends to Brauer torsion through Kummer lifts and the generic injection, and carries unit cups to norm cups. The global argument uses one fixed annihilator and divisibility of the cup image to bound quotient torsion by a finite-coefficient cohomology group. It does not infer a prime-uniform finite group from separate primary finiteness. The exact primary-source scopes are recorded in the owner ledgers. This strengthens the conclusion but does not reduce the remaining surface-Tate gate further.


## Whole prime-to-p results and the irregularity-zero gate

The complete prime-uniform proofs are now integrated in `sections/b3_prime_uniform.tex`. Under the surface-Tate condition, the prime-to-characteristic Brauer quotient by arithmetic unit cups is one finite group on every finite-type base. Relative Brauer finiteness follows for every morphism identifying units. For every abelian scheme A/S, the entire prime-to-p subgroup of H1(S,A) is finite and H1(S,A)[1/p] is finitely generated over Z[1/p]. The zero-section splitting of the derived Picard complex gives an actual injection into Brauer classes and controls its finite 2-primary kernel; it does not assume that torsion in a quotient lifts to torsion. B, D and root each read the complete written proof.

Yuan’s published fixed-finite-field reduction is also integrated, with a full proof account and exact source locators. The remaining surface-Tate condition can be restricted to smooth projective geometrically integral surfaces satisfying H1(Y,O_Y)=0. Its prime independence is proved using the intersection pairing and the Frobenius polynomial. This is a smaller intrinsic test class and qualifies as a main-gate reduction. It does not prove the restricted conjecture. The all-prime strengthening itself retains the same Tate gate and is not separately counted as progress for the stopping rule.

Checkpoint05 was saved at its scheduled 06:35 UTC boundary with 248 included files, 72 unchanged references, and 2,348,090 ZIP bytes. Its 136-page PDF had 144 numbered statements, 568 check events (including 131 explicit cross-references, not independent checks), 148 canonical bibliography entries, and 176 literature records. Its SHA256 is ca29760d4d7867302b9e5607d9f08954f030db1468f873ab60b623d7ee420d0f. The final build had zero overfull boxes, undefined references or citations, or LaTeX/BibTeX warnings. The 33 inspected page renders were pixel-identical after the final bibliography consolidation. The prime-uniform proof notes were included there; these complete integrated statements and the new irregularity-zero proof will be included in the next scheduled checkpoint.

## Scheduled progress review02

The second formal review was completed at 06:50:14 UTC. Three qualifying changes since review01 are documented: removal of C+ from the finite cycle criterion, removal of the arbitrary-base Brauer obstruction, and restriction of the surface-Tate test class to H1(O)=0 with very ample canonical bundle, together with all numerical cut refinements. The no-movement count is 0. All eight mathematically open rows remain explicit in `progress/review_02.json`; work continues. The prime-uniform upgrade and additional special cases are not separately counted as smaller conjectural gates.


## Post-review02 proofs and unsuccessful extensions

The paired arithmetic counterexample has a full independent exact PARI rerun in `code/check_paired_corank_root.py` and `part_b/output/paired_corank_root.txt`. Two products over the identical base have dimension2, Mordell–Weil rank2 and zero entire 2-primary Sha, yet arithmetic H1 coranks1 and0. Every two-Selmer basis cover has a displayed rational point and its covering map satisfies the exact curve identity. The local closure ranks are proved by formal groups. The initially overstrict wrapper flagged the harmless stack-size announcement; that run and the precisely corrected diagnostic are recorded. This does not change the remaining finite-field surface-Tate gate.

The threefold monodromy block now has an exact radical-quotient description and a primitive surface-pairing criterion. The rational primitive divisor restriction image splits unconditionally by its rational Hodge-index form. Under the separate surface-Tate hypothesis, only the transcendental restriction image remains. The full written proofs passed owner, D and root checks. Root also independently read Ito Claim4.6 and the relevant Saito proof. The universal pairing nondegeneracy remains unresolved, and the new representation is not automatically classified as qualifying progress.

The first B1 Chow gate has a complete surface-support criterion and an uniruled-threefold consequence. The hypothesis concerns zero-cycles after arbitrary field extension. The proof transposes a generic-point diagonal decomposition and factors through finite-field surface zero-cycles and divisors, where the numerical kernels vanish rationally. This establishes ordinary Chow equality in the stated class, without a Parshin or full-motive conclusion. Whether this affects the stopping-rule gate is left to the next scheduled review; an additional solved class is not automatically counted.

A new attempted B3 refinement is under active source and proof audit: remove the finite prime-to-characteristic geometric fundamental group of Yuan's abelian-fibration model by its universal finite étale cover, preserve the ample Hodge bundle through the generic isogeny, reconstruct the regular model, and use ample Lefschetz sections to obtain a geometrically simply connected surface. It is not declared proved in this entry. Its complete notes and subsequent audit state govern any later theorem.

The general C6 conductor route did not close the gap. Root opened Kato–Takeshi Saito2004 only at the introduction, pp5–7: its alternating conductor and Swan formulas do not supply the individual tame inertia codimension for an arbitrary motivic summand. Root rechecked Takeshi Saito2003 Theorem0.1 and Corollaries0.2/0.4, and the local-invariant-cycle obstruction in Esnault–Wittenberg2016 section3.1, p494. No high-dimensional mixed-characteristic purity theorem was inferred. A separate conditional correspondence-rank approach is being investigated; no exact converse or arbitrary nonalgebraic projector assertion is recorded as proved.

Root read all mathematical sections1–4 of the live25-page van Hoften–Sempliner2026 CM-Hodge preprint. Its theorem is retained as the explicitly identified current external input for abelian-type results. This is a reading of the complete argument, not an independent verification of every external theta and representation-theoretic theorem it invokes. It remains separate from the two withdrawn October2026 K3 preprints. No general geometric-positivity conclusion is imported from it.


### Checkpoint06 pending proof and layout record

The full simply-connected surface reduction is preserved in `part_b/b3_simply_connected_pending.md`, with an independent primary-source audit in `part_c/b3_simply_connected_independent_audit.md`. Root has now read and passed the entire written argument, including the fixed-field cover and the reconstructed regular model. Its numbered integration follows the checkpoint freeze. The restricted Tate conjecture is not claimed. The conditional C6 correspondence-rank proof is separately preserved in `part_d/c6_rank_conjecture_reduction.tex`; its precise sufficient-only boundary is retained, and no general converse is inferred.

The first expanded checkpoint06 build had two overfull boxes, measuring4.87817pt and12.19835pt, and one citation using the pre-canonical de Jong key. The sentence, display and key were repaired. Eight missing citation spaces were subsequently inserted. The final verification entry below reports the actual clean build and rendered-page inspection, not merely successful compilation.

### Checkpoint 06 verification

The verified PDF has 152 pages and 157 numbered statement records. The final LuaLaTeX log has zero overfull boxes and no undefined citations or references. Any earlier integration repairs are recorded separately in this report. Pages 1, 19, 20, 21, 22, 23, 32, 33, 39, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 76, 92, 93, 94, 95, 96, 97, 98, 114, 115, 116, 117, 118, 120, 124, 125, 126, 133, 140, 141, 142, 151, 152 were rendered and visually inspected, including the new proof sections. Text, formulae and margins are legible.

The source bibliography contains 171 canonical entries, each with explicit opening status, and the consolidated literature ledger contains 195 work records. Every numbered statement has a matching check-event label. There are 683 event records, including 160 explicit cross-reference records that link preserved checks to numbered statements; those links are not new independent checks. The item table resolves all statement labels to their compiled numbers. This verifies the checkpoint contents and does not declare the research programme complete.


## Checkpoint06 saved; subsequent source audits

Checkpoint06 was observed to save successfully at the scheduled 07:20 UTC boundary. It contains 290 files and references 88 unchanged files in preceding checkpoints. The ZIP is 2,644,498 bytes. Its clean 152-page PDF has 157 numbered statements; 45 rendered pages were actually viewed. The verification records 683 events, including 160 cross-reference records rather than new independent checks, and 171 canonical bibliography entries with 195 literature records. The simply-connected reduction and the conditional C6 rank proof were preserved as complete standalone notes before numbered integration.

After that save, root directly read the complete written C6 rank proof and the primary proofs in Takeshi Saito (2003), section2.4, author pp33–36, together with Corollary1.2.6, Corollary2.2.4 and Lemma3.7, and van Dobben de Bruyn (2020), Theorem5.1 and Corollary5.2, pp17–18. The argument passes in its stated conditional scope. Algebraic homological projectors suffice; no Chow-idempotent lift is needed. The converse and arbitrary nonalgebraic projectors remain unresolved. The precise reads, failed initial URL and repaired primary URL are recorded in the JSON audit.

The full B3 simply-connected reduction has now passed complete written audits by B, root, C and D. The next scheduled formal review remains07:50 UTC, and no new movement is pre-counted. The next checkpoint is due08:05 UTC.


## Conditional motivated-projector reduction: root audit

At 2026-11-19T07:49:39+00:00, root completed the written proof audit of the finite-field rank implication for Andre motivated motives. The full derivations are preserved in the two root notes, and the numbered proof is in part_d/c6_motivated_rank_reduction.tex. The graph constraints invert Hard-Lefschetz maps only on alteration-projector images, use whole-product operators, and retain the original inertia action through conjugate models. Exact matrix checks support, but do not replace, the general proofs. The source-normalization issue in Andre p11 is recorded in the operator note; the proof uses the directly verified Hodge normalization. The result is conditional on the published finite-field correspondence-rank conjecture. It proves neither that conjecture nor a converse, and it is not counted as closure or a strictly smaller universal gate.

## Scheduled progress review03

The third formal review took place at07:50:01UTC. It counts one strict intrinsic reduction: the surface-Tate gate now requires only geometrically simply connected surfaces, with the previous coherent and canonical conditions retained. The complete proof and the strictness construction are recorded under `thm:B-simply-connected-surface-gate`. The no-movement count remains0. The eight universal mathematical rows remain open, and the conditional monodromy work is not counted as a named equivalence or as a general solution.


## Checkpoint07 integration repairs

The first expanded build had zero overfull boxes but two missing bibliography keys, SGA1 and SGA2, because the separate already-read source bibliography was not included in the consolidation list. The input list was repaired. A second build had zero overfull boxes and no undefined citations, but two BibTeX author/editor-field warnings; the corrected-edition credits were moved to the bibliography notes after checking both primary prefaces. The final build and visual audit are recorded separately below. No source was invented or treated as unread to repair a citation.


## Final checkpoint07 scope and typing check

The final source check expanded the Hard-Lefschetz inverse composition into its fully twisted arrows. It also replaced one inherited phrase in the earlier algebraic-projector proof: the transferred correspondence is algebraic and acts idempotently on cohomology; it is not asserted idempotent in Chow. The theorem and its proof use only the former property. The change repairs wording left over from the original Chow-only version and does not change the proved scope.

### Checkpoint 07 verification

The verified PDF has 161 pages and 163 numbered statement records. The final LuaLaTeX log has zero overfull boxes and no undefined citations or references. Any earlier integration repairs are recorded separately in this report. Pages 1, 21, 22, 23, 32, 33, 41, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 81, 92, 93, 94, 101, 114, 115, 116, 117, 118, 121, 129, 130, 131, 132, 133, 134, 135, 136, 141, 161 were rendered and visually inspected, including the new proof sections. Text, formulae and margins are legible.

The source bibliography contains 177 canonical entries, each with explicit opening status, and the consolidated literature ledger contains 206 work records. Every numbered statement has a matching check-event label. There are 732 event records, including 165 explicit cross-reference records that link preserved checks to numbered statements; those links are not new independent checks. The item table resolves all statement labels to their compiled numbers. This verifies the checkpoint contents and does not declare the research programme complete.


## Checkpoint07 saved; fourth review interval begins

The seventh checkpoint was packaged at the scheduled 08:05 UTC boundary and its successful save was observed. It has 312 included files and 110 references to unchanged files in earlier checkpoints; its size is 2,829,456 bytes. The 161-page PDF has 163 numbered statements, 732 check-event records (165 are cross-reference records, not new independent checks), 177 canonical bibliography entries and 206 literature records. Forty rendered pages were actually viewed after the final wording correction. The final LuaLaTeX and BibTeX logs have no warnings or overfull boxes.

The third formal review at07:50:01 UTC counted only the simply-connected B3 surface reduction as qualifying movement. The conditional motivated C6 implication and the standalone C4 sufficient positivity theorem do not count as closure or an exact converse. All eight universal mathematical rows remain unresolved. The next review and checkpoint are both due08:50 UTC; the consecutive no-movement count remains zero until that review is actually performed.


## Fourth review interval: independently checked refinements

Root read the complete new target-only positivity proof and the exact primary standard-conjecture arguments in Morihiko Saito2003 sections4.1–4.3, pp14–16, and Jannsen1992 Theorem1 with Lemmas1–2, pp448–449. The proof uses a finite-dimensional rational numerical corner and the Lefschetz-modified pairing. It does not infer rationality from a Q_l-linear projector or assume the ordinary intersection form is positive on all H2.

Root also read the complete finite-prime local/global approximation proof and Kisin's original Theorem5.1 and Proposition5.2 with their local proofs. A dense number subfield and an etale chart yield an algebraic nearby point with exactly the original p-adic completion; the projected local system itself is held fixed. This removes a globalization obligation from the analytic converse route, but leaves pure local realization unresolved. The full BGV square-zero encoding and the relevant internal compactness, equivalence and weight-heart proofs were read separately. No arbitrary analytic object is declared pure.

The fresh arithmetic source check opened Flach–Krause–Morin2026. Their local Tate determinant theorem and global syntomic comparison retain the global motivic finite-generation assumptions in Conjecture7.1.1 and Proposition7.1.2. The main B5 prescribed realization gate is therefore unchanged. The current Awada–Bolognesi–Laterveer–Pedrini paper has specified high-rank and four-dimensional families; its density theorem does not reverse specialization and does not settle the general K3 exterior projector. Exact primary locators, actual read scope, failed initial retrieval and successful downloads are recorded. None of these source checks is counted as mathematical movement.


## Further proof and source audits before checkpoint08

The integrated B1 proposition gives complete counterexamples to two limit arguments. The first exhibits an invariant infinite-support continuous Kummer class outside the colimit over fixed opens; the second constructs a non-root-of-unity Frobenius eigenvalue after completion. These are method obstructions, not counterexamples to B1 itself. The fixed-orbit direct-sum permutation calculation is separately preserved.

The B5 coefficient note proves the exact Beilinson--Parshin dependency for the specified rational Weil extension of every Chow-heart object, with the point's degree-one pairing and the P1 degree-three pairing. It expressly does not infer the same necessity from homogeneous pure coefficients without actual Chow--Kunneth decompositions. Root checked the complete written argument and the exact Kahn primary-source passages listed in the audit output. The universal arithmetic realization gate remains open.

The complete blowup diagnostic shows why occurrence among semistable strata is insufficient for the C6 converse: the added terms cancel, and the direct pullback of a prescribed cycle still vanishes in the relevant restriction cokernel after transverse cuts. A new primitive construction is not ruled out. Root also read Kato--Nakayama--Usui2025 Theorem2.3 with its full local proof and section4. Its stated logarithmic Tate and semisimplicity assumptions give a sufficient weight--monodromy route, not a pure-local realization of arbitrary cycles. Exact version, pages and read limits are in the bibliography and check ledger.

No qualifying formal-review movement is claimed for these additions. Earlier estimated root message times for the B1/B5 audits are superseded by the actual clock-based records.


### Checkpoint08 first-build typesetting repairs

The first expanded build had two overfull horizontal boxes, of 108.63458pt and 5.84212pt. The B1 program paths were put on separate breakable lines, and the C4 pair of correspondence spaces was moved to a display. These changes alter no mathematical claim. Final counts and inspection are recorded in the checkpoint08 verification entry after the corrected build.

### Checkpoint 08 verification

The verified PDF has 169 pages and 168 numbered statement records. The final LuaLaTeX log has zero overfull boxes and no undefined citations or references. Any earlier integration repairs are recorded separately in this report. Pages 1, 3, 15, 22, 24, 25, 26, 39, 43, 61, 64, 65, 78, 79, 80, 81, 85, 91, 102, 106, 119, 120, 121, 122, 123, 124, 125, 126, 127, 136, 137, 138, 139, 140, 141, 142, 143, 144, 148, 150, 159, 166, 169 were rendered and visually inspected, including the new proof sections. Text, formulae and margins are legible.

The source bibliography contains 199 canonical entries, each with explicit opening status, and the consolidated literature ledger contains 224 work records. Every numbered statement has a matching check-event label. There are 804 event records, including 178 explicit cross-reference records that link preserved checks to numbered statements; those links are not new independent checks. The item table resolves all statement labels to their compiled numbers. This verifies the checkpoint contents and does not declare the research programme complete.

### Standalone diagnostics retained at checkpoint08

The fixed two-boundary B1 note identifies a precise cokernel in terms of a rational Gysin relation on the threefold components. It does not assert survival under further shrinking. The pure-local encoding note proves the limited hyperbolic-rank and smooth-parameter obstructions, with the weight--monodromy condition explicitly retained. Root and independent readers checked these written arguments; the exact source-read scopes are separate.

A further source check found a literal Tate-twist issue in the archived BGV v2 purity definition: its algebraic-integrality clause is incompatible with the negative-weight Tate object. The exact normalization, elementary counterexample and rational-arithmetic certificate are retained in the standalone note. The compact-monodromy equivalence used here does not depend on the affected purity clause. This is not a refutation of that equivalence or of an uninspected later version. No open universal row changes status.

## Scheduled progress review04

The fourth formal review took place at 08:50:14 UTC. It records no qualifying movement and a no-movement count of 1. All eight universal mathematical rows remain open. The complete B1 limit diagnostics, B5 coefficient-duality criterion, C4 sufficient positivity package and C6 transfer theorem are retained in their precise scopes, but none closes an original open row or proves a strictly smaller remaining universal gate. Work continues to the next scheduled review at 09:50 UTC.


## Checkpoint08 saved; fifth formal-review interval begins

Checkpoint08 was packaged immediately after the scheduled review at 08:50:14 UTC and its successful save was observed. The ZIP has 351 included files, 125 unchanged-file references and a size of 3,019,806 bytes. Its verified PDF has 169 pages and 168 numbered statement records; all 43 rendered sample pages were actually viewed. Both corrected build logs are clean of warnings and overfull boxes. The two initial overflows and their source repairs remain documented separately. The final records contain 804 check events, including 178 explicit cross-reference records, 199 canonical bibliography entries and 224 literature records.

Formal review04 found no qualifying movement after review03. The consecutive no-movement count is one; all eight universal mathematical rows remain unresolved. The next checkpoint is due 09:35 UTC and the next formal review 09:50 UTC. If that next review also has no qualifying movement, the prescribed stopping rule requires the final INCOMPLETE package. The ongoing exterior-power weight--monodromy argument is not pre-counted as a smaller gate.

The uncited Colliot--Thelene--Kahn lead briefly acquired duplicate bibliography keys in simultaneous edits. The owned duplicate was removed before the final consolidation and before packaging; the annotated canonical entry is BColliotTheleneKahnFiniteFields. No proof passage or primary-source read record was dropped.


## After checkpoint08: finite exterior tests and remaining method obstructions

The complete exterior-power criterion now proves that the universal middle-degree trait endpoint is equivalent to weight–monodromy. For an individual j-fold, the tests use ordinary exterior powers of orders at most j+1, realized as Galois direct summands on actual powers. Semistable alterations are made over separate extension fields for each power; no ramified base change is assumed to preserve a regular model. Root and both independent readers checked the written proof. This equivalent universal gate is not counted as a strictly smaller gate under the review rule.

The integrated fixed-open B1 comparison identifies its cokernel with a rational Chow Gysin obstruction on explicit threefold boundary components. The further moving-support and completion attempts still do not give uniform control under shrinking. Their exact failures are retained in the part notes; no rational Chow kernel is killed by a torsion or completion theorem alone.

The new conductor-source audit includes the October2026 Kisin result and the twisted Beraldo–Pippi formula. A supplied homogeneous projector does remove alternating degrees, but the specific additive trace over the inertia-cochain algebra still records the dimension of that summand, not the kernel dimension of monodromy. The full categorical object is not declared information-free. This is a proved limitation of the attempted scalar argument, not a refutation of C6.

The Zhang source audit independently checks the local invariant-cycle equivalence. It also supplies an explicit regular semistable elliptic model disproving the unconditional perfect-pairing wording for H_psi on p9 of the inspected arXivv3. A separate local subscript error in the invariant-cycle proof is corrected. The valid supported quotient-kernel duality is retained. These bounded source corrections do not refute weight–monodromy or the checked invariant-cycle theorem, and do not change an open universal row.

Formal review04 remains a no-movement review with consecutive count1. The next formal review is scheduled for09:50UTC (10:50Europe/Berlin); another review without qualifying movement invokes the user's stopping rule. Checkpoint09 remains scheduled for09:35UTC (10:35Europe/Berlin), with no intervening ZIP.


### Further checked results before checkpoint09

The ordinary Milnor regulator kernel is now proved to be the infinitely ell-divisible subgroup in every degree over an algebraic closure of a finite field. In positive degree, infinitely divisible residues on a smooth projective model force infinite divisibility of the original ordinary element. The proof uses degree induction, the exact ordinary refined-unramified weight interval, finite Frobenius orbits and torsion-freeness. It does not identify an ordinary colimit with its completion and does not exclude the weight-zero interval in the actual degree-three/twist-two B1 residue problem.

For C4, a second sufficient pairing criterion replaces the surface-square positivity hypothesis with squarefreeness of the entire primitive target Frobenius polynomial over the fixed field of definition. Mixed numerical-equals-homological equivalence remains assumed. Two algebraic cohomological image/kernel constructions obtain the actual primitive intersection; the resulting finite étale endomorphism algebra has adjoint-fixed idempotents. The condition is not claimed to hold after an arbitrary extension or for every degeneration.

Both complete arguments have owner and independent written-proof checks. Root also reopened the precise primary inputs for the Milnor argument. Neither result closes an original open row or proves a strictly smaller universal gate, so neither resets the formal no-movement count.


### Separated Milnor quotient and the remaining saturation issue

The all-degree ordinary regulator lemma further proves that the quotient by infinitely ell-divisible elements is a free abelian group of at most countable rank. The kernel is ell-divisible, and quotienting induces a canonical equivariant isomorphism on completions. The proof includes alteration transfer for arbitrary function fields and finite-support residue induction.

This does not supply the missing spectral control. An explicit exact sequence with quotient Z[1/3]/Z gives a free Frobenius-stable subgroup of a countable sum of finite permutation lattices whose3-adic completion contains a nonzero four-eigenvector. Its compatible elements, exact orders and Tor transitions are proved, and a finite congruence program is supplied as a supplementary check. This formal example blocks an inference from freeness or from an unsaturated permutation-submodule embedding; it is not identified with a geometric Milnor group. The B1 universal gate and formal no-movement count are unchanged.

### Checkpoint 09 verification

The verified PDF has 180 pages and 177 numbered statement records. The final LuaLaTeX log has zero overfull boxes and no undefined citations or references. Any earlier integration repairs are recorded separately in this report. Pages 1, 8, 16, 20, 23, 24, 25, 26, 27, 28, 29, 30, 37, 46, 47, 66, 67, 68, 83, 84, 90, 100, 110, 113, 120, 127, 128, 129, 130, 131, 132, 133, 134, 135, 136, 145, 153, 158, 160, 165, 176, 177, 178, 179, 180 were rendered and visually inspected, including the new proof sections. Text, formulae and margins are legible.

The source bibliography contains 212 canonical entries, each with explicit opening status, and the consolidated literature ledger contains 236 work records. Every numbered statement has a matching check-event label. There are 903 event records, including 195 explicit cross-reference records that link preserved checks to numbered statements; those links are not new independent checks. The item table resolves all statement labels to their compiled numbers. This verifies the checkpoint contents and does not declare the research programme complete.

### Checkpoint 09 build repair and visual check

The first checkpoint-09 build stopped during the second LuaLaTeX pass because
two newly added bibliography annotations contained unescaped underscores in
program paths (the Taylor–Yoshida and Vial entries). The retained initial
failure is `code/checkpoint09_initial_build_failure.txt`. We wrapped those
literal paths in `\path{...}`, reran BibTeX and then the full build. The
repair and its output are retained in `code/fix_checkpoint09_bibliography.py`,
its JSON output, and `code/checkpoint09_bibtex_repair_output.txt`. This was a
typesetting repair and did not change a mathematical statement. Duplicate
terminal periods in the new B.1 and C.4 status strings were also removed.

The initial failed build had zero overfull boxes; the final complete build
has zero overfull boxes and zero LaTeX/BibTeX warnings. All 45 pages listed in
`code/checkpoint_09_verification_output.json` were actually inspected in the
five rendered page panels, including the new B.1 and C.4 proofs and the final
bibliography pages. No clipping, overlapping text, or unreadable layout was
found. The final PDF has 180 pages. This layout check does not certify a new
mathematical result and does not count as movement at a formal review.


## Checkpoint09 saved at its scheduled boundary

Checkpoint09 was packaged at 09:35:00 UTC (10:35 Europe/Berlin), and its
successful save was observed immediately afterward. It contains 389 files
and references 146 unchanged supplementary files in earlier successful
checkpoints. Its size is 3,260,946 bytes. The current PDF has 180 pages and
177 numbered statements; the consolidated records have 903 check events,
including 195 explicit cross-reference records, 212 canonical bibliography
entries and 236 literature records. All 45 rendered sample pages were
actually inspected. The initial bibliography-path build failure and its
repair are recorded above; the final build has zero warnings and zero
overfull boxes.

The fifth formal review remains due at 09:50 UTC (10:50 Europe/Berlin).
The no-movement counter remains one. The new ordinary Milnor and trait
weight–monodromy results have not been counted as a closure or a strictly
smaller universal gate. This save is not a final research outcome.


### Post-checkpoint09 refinements and failed transfers

The separated ordinary Milnor quotient has now been proved independent of
the coefficient prime different from the characteristic. The proof is short:
the ell-divisible kernel maps to zero in every other separated free abelian
quotient, and symmetry identifies the kernels. Root read the complete revised
corollary and the all-prime formal counterexample in the actual written files
at 09:37 UTC; C independently checked them. The formal permutation-submodule
example has an extra four-eigenline after3-adic completion and none after
completion at any other prime. This is not a geometric counterexample.

The source all-model residue audit was independently read by root, including
its code and saved output, at09:32UTC. The family t=s^m has iterated residue m
and gives infinitely many nonzero coordinates in the literal all-model target.
The source-version boundary is retained: only the opened author/arXiv text is
diagnosed, not the uninspected published file. A fixed chosen residue tree
avoids that construction issue; the ordinary regulator proof uses only fixed
finite-support maps. Root did not rerun the finite certificate. C's subsequent
actual timed rerun is separately recorded.

Root also proved the bounded C.4 spectral-transfer obstruction retained in
`root_post09_spectral_transfer_attempt.md`; C checked the entire written
argument. Surface alteration gives divisibility of the primitive Frobenius
characteristic polynomial by cancelling one ample Tate factor from split
degree-two pullback. Constant-field extension and Artin-factor twist retain
old multiplicities as well. These operations therefore do not establish the
new sufficient squarefree hypothesis when it initially fails. This is not
an impossibility result for arbitrary geometric constructions.

The additional conductor/microlocal primary reads are recorded with their
exact limited scopes in Part D's post09 note and canonical source ledger.
Root read that complete note, but did not reopen those three primary papers.
The geometric conductor's actual closed stalk, a generic inertia-invariant
space, and cross-prime support compatibility remain distinct. The BGV local
construction supplies a Clemens–Schmid complex whose required exactness
remains conditional on weight–monodromy. None of these refinements closes an
original open row or supplies a strictly smaller universal gate.


### Actual geometric illustration of Milnor completion

The final standalone note `part_d/post09/milnor_elliptic_completion.md`
uses K=Fbar2(E), E:y²+y=x³, to exhibit a nonzero T3E subspace in the
actual3-adic completion of K1^M(K). The principal-divisor sequence and
compatible division of the explicit point(0,0) prove the inclusion and
nonvanishing. The tangent line gives arithmetic Frobenius phi²=[−2],
so geometric Frobenius satisfies F²=−1/2. These completed eigenvalues
are not roots of unity. The example illustrates completion in geometry;
it does not assert a prime-dependent failure for a geometric motive.

The complete proof was read independently by B and root. The program
`part_d/post09/code/check_elliptic_tangent.py` executed eight exact
characteristic-two polynomial checks at09:41:42UTC in0.059081959seconds,
with output `part_d/post09/output/elliptic_tangent_certificate.json`.
That output identifies by hash the existing Part B projective-smoothness
and F2-point certificate. Root read both programs and both saved outputs
at09:43–09:44UTC without rerunning them. The infinite completion proof is
not inferred from the finite certificate. This additional example does
not change any original open row or the review movement count.

## Final stopping decision

Formal review05 took place at 09:50:00 UTC (10:50Europe/Berlin). It found no qualifying movement since review04. These are two consecutive formal reviews without an open-row closure or a strictly smaller proved universal gate, so the user's stopping rule now requires this work to stop. The final status is **INCOMPLETE**. All44 item rows and all8 mathematically open rows remain explicitly recorded, with the strongest proved reductions, exact limitations and prospective next attempts.

The final package preserves the complete current deliverables and every new or changed work file since the last successful checkpoint. Its file list identifies earlier successful checkpoints holding unchanged supplementary outputs. No earlier ZIP is embedded. The supplied original archive, raw third-party sources and ordinary render images are excluded as required.


## Final verification of the INCOMPLETE deliverables

After the stopping review, the final paper was rebuilt from the retained
LuaLaTeX/BibTeX sources. It has 180 pages and
177 numbered statements. The final build has zero
overfull boxes and zero LaTeX/BibTeX warnings. The checkpoint-09 initial
bibliography-path failure and its repair remain recorded above; no failed
build is represented as a successful final build. The final pages
1, 8, 16, 20, 23, 24, 25, 26, 27, 28, 29, 30, 37, 46, 47, 66, 67, 68, 83, 84, 90, 100, 110, 113, 120, 127, 128, 129, 130, 131, 132, 133, 134, 135, 136, 145, 153, 158, 160, 165, 176, 177, 178, 179, 180 were rendered and actually viewed.
The first page explicitly states INCOMPLETE. No clipping, overlapping
formulae or margin defects were found in the inspected sample.

The final statement-to-event index resolves every numbered label. It has
935 check-event records, including
199 explicit cross-reference records;
cross-references link existing checks and are not additional independent
proof checks. The bibliography has 216 canonical
entries with opening annotations, and the literature ledger has
240 work records. The outcome table resolves all
44 item rows to compiled statement numbers or the named index files.
The eight mathematical rows identified by the stopping review remain
unresolved in their stated universal scopes.

The last source-reconciliation repair changed the Saito publication-list
annotation from an access statement to the explicit word Opened, preserving
its metadata-only scope. No mathematical assertion changed. An optional
sentence in the elliptic-completion note extending the illustration to every
odd coefficient prime was removed: the retained prime-three case has a fully
explicit torsion point and already proves the required distinction. That
omission is a scope choice, not a claim that the broader standard statement
is false. No other post-checkpoint09 proof passage was discarded.

The final file list records hashes and identifies the successful checkpoint
holding each unchanged supplementary file omitted from this ZIP. Current
deliverables, notes and programs are included. New or changed computation
outputs are included; earlier raw third-party sources, supplied attachments,
ordinary rendered page images and earlier ZIPs are excluded as requested.
All retained results are AI-produced research records; no priority or
completed solution of the unresolved questions is claimed.
