# GCT_PLETH dated work ledger

Run: GCT_PLETH_20261121_run01. User-facing date: 21 November 2026, Europe/Berlin.
Start: 20 November 2026, 23:01:08.313727 UTC (21 November, 00:01:08 Berlin).
Models: GPT-6 Astra Pro, root and three delegated agents. Reasoning effort is not exposed.

## Current main questions

| Row | State | Strongest proved reduction / next operation |
|---|---|---|
| Archive, exact operations | substantially proved/refuted, precise context gates active | All13 original target leaves inspected;123 assertion rows:80proved,25refuted,18 exact gates. A001–A023 give the defined operations, integral tensor equality, DVR classification and explicit local-ring counterexample. |
| Positive lattice counts | proved with terminating preprocessing | G009 for symmetric plethysm, G010 for all Schur plethysm, G011 for actual canonical-map image. Every step uses explicit generators and finite algorithms. |
| Efficient positive formulas | open, smaller gates | T037 completes every outer-degree-four coefficient with≤108 fixed polytopes. G015 gives the exact all-rank flag ideal. G020 evaluates all symmetric quotient powers for c≥2k. G021 evaluates every two-row quotient there with122 active polytopes and155 support exceptions; exact multiplication/complement maps cover both outside λ-regions. The strict central region c<2k remains the direct outer-five gate; general preprocessing bounds remain open. |
| Canonical-map ranges | specified blocks proved; full family open | Current checked full bound b>=(a-1)^2 (Sra III Thm1.3). R021 gives every even-rank boundary determinant preimage; R023 removes its exact prolongation and restricts the remaining critical first factor to rowsν1≥r²+1,ν2≥r(r−1). R024 gives recursive component ranges from actual degree-five and square bases. R025–R026 remove explicit multiplicity-one components throughout r²−r+1≤b≤r²−1 using cofactor and apolar evaluations; full varying annihilator remains open. |
| Rectangular nonvanishing | proved in exact stated families | Determinant parity, row extensions, prime-width image blocks, Latin-square scalar and valuations; hook comparison counterexample; repeated-odd-part stable families. |
| Grothendieck dictionary | written, checking continues | Every finding is mapped through frame torsors, exact K0, group-scheme comodules, invariant schemes/modules, and where applicable Artin motives; precise SGA/EGA/FGA locators. |
| Alpoge period transfer | explicit-morphism input gate | Need the actual representation/period comparison carrying the finite normalizer or grid idempotents. Four-page note read; named Lean files absent. |

## Movement already achieved in this run

1. Balanced-weight invariant formula proved; the unprojected GT equality refuted by the actual determinant sign.
2. Width-five and width-six positive formulas reduced to fixed, fully certified exterior-cube tables and explicit LR polytopes.
3. Width-seven end-node orbit extension condition evaluated exactly, including a pole counterexample and explicit stable positive families.
4. A general finite invariant-ring presentation gives positive polytopes for every coefficient, and a finite coherent-module presentation gives them for every canonical-map image rank.
5. The outer-degree-three projected flag algebra is presented by six generators and two monic equations, yielding four fixed polytopes.
6. Prime-modular determinant contractions produce actual canonical-map preimages below the general quadratic bound.
7. Integral tensor-power equality on 133/028 proved in exact equivariant K0 using the integral Cauchy filtration; this closes the earlier rational-to-integral gate.
8. Two finite symmetric common-polarization cases certified; the actual r=4,L=4,b=15 case is still computing and has no claimed outcome.

## Approaches tried and their exact outcome

Ordinary GT counting retains the finite projector; determinant parity disproves dropping it. A permutation-basis route fails on the explicit sign-twisted standard A5 restriction. Homogeneous Ehrhart dilation fails on the cited period-six ray. G2 open-orbit invariants require the computed discriminant valuation. Purity has an explicit two-point Artin example with different invariant ranks. Symmetric common-polarization determinant kernels cover odd r; their symmetric projection vanishes for even r, leaving the stated even-r calculation. Reynolds, Hilbert-basis and module elimination do terminate and prove the general positive counts, with large unbounded preprocessing.

## Timing and checkpoint protocol

First checkpoint due at 20 November 2026, 23:46:08 UTC (00:46:08 Berlin). Subsequent checkpoints are due at 45-minute intervals from the start. No earlier checkpoint is overwritten or placed inside another checkpoint. The first checkpoint is prepared from the current deliverables and all work documentation; its exact save receipt is retained separately after saving.

The first progress review is due at 21 November 2026, 02:01:08 UTC (03:01:08 Berlin), then hourly. No such review has yet been due. Only an open-row state change or a strictly smaller main gate counts as movement. No stagnation review has been fabricated.

## Check conventions

Whole-proof readings, separate-agent reviews, exact computations and source-background uses have distinct event types in CHECK_EVENTS.tsv. No proof assistant was run. Every missing file and source-context gate remains explicit. Checkpoint status is continuing work, not a final completion claim.

## Checkpoint 02 update — 21 November, 01:31 Europe/Berlin

The first checkpoint was saved at 00:46:27 Europe/Berlin. The second is due at 01:31:08. The research remains active; no formal stagnation review is due yet.

Since checkpoint 01, the outer-degree-four direct formula has advanced through every proper face, both outside chambers, and the central equal-opposite-gap family. T-035 proves an exact four-point vanishing model for the entire remaining region. Evaluation of its unequal-gap ideal powers is the next main operation. Independent cycle-index/Murnaghan–Nakayama calculations checked 1,370 chamber coefficients and 420 coefficients in the new central family; the full proofs were also read independently.

For the canonical map, G-013 constructs actual prime-adjacent semigroup preimages; 198 exact semigroup certificates cover ranks 2–100. G-014 gives explicit lifts of all target components with tail size at most coordinate degree. R-015 certifies the complete rank-six quintic common-polarization source, including 65,481 matrix entries and 893 selected determinants. R-016 classifies three finite boundary kernels. R-017–R-018 replace the remaining general kernel by exact block truncation and eliminate every component with second row at most b−L, for all outer Schur functors.

The original archive scans have now been inspected for all thirteen target leaves. The assertion register contains 80 proved rows, 25 refuted rows and 18 precise gates. The exact lattice ring is proved over every characteristic-zero DVR; an explicit characteristic-zero local ring with K0 equal to Z refutes the unrestricted generator claim. The hyperbolic class formula is proved for all schemes with 2 invertible through an actual injective splitting construction.

Earlier 'still computing' notes above are historical. The current finite boundary outcomes are those in R-012, R-015 and R-016, with all complete certificates included. No general boundary-kernel classification is asserted.

## Research status before checkpoint03 — 2026-11-21T02:13:24.741642+01:00

T037 has closed the complete outer-degree-four direct-formula gate. G015–G016 have replaced the general extension question by an explicit projective-frame ideal-power problem. The five-point quadratic algebra and ordinary-power cohomology are proved with all local hypotheses checked (T038,A028–A029). G017 now has an explicit matrix factorization, full section-module identification and positive invariant-parameter basis. G019 extends this to all symmetric quotient powers and all point orders, with a fixed positive formula and complete support; independent exact arithmetic has reproduced all403200 constants. G018,T040,T041 evaluate additional exterior, shifted and hook bundles.

R019–R024 provide actual map movement: the full first-row common-polarization band, every even-rank boundary determinant, exact rectangular prolongation removal, recursive second-row surjectivity and positive image multiplicities. The next boundary vectors remain under whole-proof checks and are not declared a general solution.

This is an ongoing status update, not the scheduled three-hour review. The first formal review remains due at03:01:08Europe/Berlin. No stagnant-review count has been started.

Checkpoint03 is scheduled for21November2026,01:16:08UTC (02:16:08Berlin). The snapshot includes the current full proof record, source inventory, exact certificates and continuing gates. Its save receipt is recorded after upload; no earlier checkpoint is altered.

## Research update during fourth work interval — 2026-11-21T02:43:38.201360+01:00

G020 and G021 strictly shrink the outer-five direct-formula gate from arbitrary rank-three quotient twists to the central region c<2k, after the exact complement transport. All two-row quotient Schur functors in c≥2k now have a fixed positive formula and complete support. The positive-difference proof for G021 uses34 exact coefficientwise domination inequalities, independently reconstructed from a complementary-rectangle Schur determinant. Its155 vanishing quadruples were computed over all90,720,000 initial multiplicities. Independent actual plethysm checks cover882 cases.

R025 and R026 give exact nonzero canonical components throughout the degrees immediately below the square bound. Root read their entire proofs, including every boundary parameter, actual annihilator morphism, cofactor sign and the endpoint apolar scalar. Both pass. Their finite coefficient computations are separately logged as computations.

This update precedes the scheduled first review. The first formal review remains due at03:01:08Europe/Berlin; no stagnation count has been started.

## Formal progress review 01 — 2026-11-21T03:01:25.219857+01:00

Scheduled three-hour review. Movement: **YES**. Consecutive reviews without movement: **0**. Continue the research. Next formal review:21November2026,03:01:08UTC (04:01:08Europe/Berlin).

The complete outer-four direct-formula row changed to proved (T037). The outer-five main gate strictly shrank to the central inequalities after G021, and G023 now evaluates every central staircase shape with seven active positive polytopes and exact support. G022 proves all-rank staircase nonvanishing with an explicit uniform bound. The actual-map gate strictly shrank by the first-row band, rectangular prolongation, recursive component ranges and the explicit multiplicity-one components R025–R026. These are proved reductions and row changes, independent of packaging.

The remaining main gates are: polynomial description-size preprocessing for varying rank; the outer-five central flag-ideal correction away from the evaluated staircase and other completed families; the remaining actual common-polarization annihilator after the exact component removals; and the width-seven boundary valuation filtration. The archive and named-source input gates are retained verbatim below.

Every currently open question row at this review:

| Row | State | Exact current gate |
|---|---|---|
| M-001 | source audit and exact morphisms checked; open ranges retained | M-001 |
| M-002 | source audit and exact morphisms checked; open ranges retained | M-002 |
| A-Q009 | gate | A-014; OriginalPDFpp3-7 recover the crystalline, torsion and stable-part definitions. Section8.3 and Theorem8.5 expressly admit the crystalline Lefschetz/freeness input; the proposed geometric exactness is the remaining gate.; Original Montpellier PDFp7/sitep6 visually inspected with neighboring PDFpp2-9; see PRIMARY_SCAN_FOLLOWUP.md |
| A-Q012 | gate | ; Deleted passage is not promoted to a theorem; source also has n-1 versus n+1 and polarization-symbol uncertainty.; Original Montpellier PDFp7/sitep6 visually inspected with neighboring PDFpp2-9; see PRIMARY_SCAN_FOLLOWUP.md |
| A-Q013 | gate | ; Definitions recovered. Original PDFp4 section8.3 expressly admits the crystalline analogue of integral Lefschetz and torsion-freeness; this is the exact remaining geometric input.; Original Montpellier PDFp7/sitep6 visually inspected with neighboring PDFpp2-9; see PRIMARY_SCAN_FOLLOWUP.md |
| A-Q014 | gate | A-014; Stable part and finite-field iterate convention recovered from originalPDFpp5-7. A014 proves the linear-algebra unit-root count; application to E(Y) retains the freeness assumption in source8.3.; Original Montpellier PDFp7/sitep6 visually inspected with neighboring PDFpp2-9; see PRIMARY_SCAN_FOLLOWUP.md |
| A-Q015 | gate | ; The source explicitly invokes algebraicity of Lambda; no unconditional proof of that input is supplied.; Original Montpellier PDFp7/sitep6 visually inspected with neighboring PDFpp2-9; see PRIMARY_SCAN_FOLLOWUP.md |
| A-Q016 | gate | A-014; The q-power iterate and inverse Galois-Frobenius convention are recovered on originalPDFpp5-7. A014 proves reduction of unit roots for a finite free Frobenius lattice; applying it to E(Y) retains the source8.3 freeness gate.; Original Montpellier PDFp7/sitep6 visually inspected with neighboring PDFpp2-9; see PRIMARY_SCAN_FOLLOWUP.md |
| A-Q017 | gate | ; It is the alternating-dimension expression of the proposed exact sequence; exactness and the changed middle term remain the precise unresolved input.; Original Montpellier PDFp7/sitep6 visually inspected with neighboring PDFpp2-9; see PRIMARY_SCAN_FOLLOWUP.md |
| A-Q018 | gate | ; Requires the injection ker v to the indicated p-torsion stable part in (8.5.1).; Original Montpellier PDFp7/sitep6 visually inspected with neighboring PDFpp2-9; see PRIMARY_SCAN_FOLLOWUP.md |
| A-Q019 | gate | ; OriginalPDFpp31-40 recover the weight filtration, effective motive category, simple labels and xi=[Q_X(-1)]. The projected category and effectivity/duality morphism remain unconstructed here; the overwritten coefficient symbol is not silently resolved.; Original Montpellier PDFpp31-43 visually inspected, including targetp41/site40 and260dpi detail; see PRIMARY_SCAN_FOLLOWUP.md |
| A-Q020 | gate | ; Tate object and primitive label sets recovered. Double duality gives the formal involution calculation; its preservation of the specified effective primitive motivic class set requires the preceding motivic duality input.; Original Montpellier PDFpp31-43 visually inspected, including targetp41/site40 and260dpi detail; see PRIMARY_SCAN_FOLLOWUP.md |
| A-Q021 | gate | ; Originalp41 explicitly says this will follow from the projected theory. Need an actual motivic self-duality isomorphism for every primitive simple class, compatible with the Tate twist and chosen equivalence on correspondences.; Original Montpellier PDFpp31-43 visually inspected, including targetp41/site40 and260dpi detail; see PRIMARY_SCAN_FOLLOWUP.md |
| A-Q022 | gate | ; Precisely the consequence of the announced triviality of twisted duality on primitive simple classes; the requisite motivic self-duality map remains the gate, after definitions were recovered.; Original Montpellier PDFpp31-43 visually inspected, including targetp41/site40 and260dpi detail; see PRIMARY_SCAN_FOLLOWUP.md |
| A-Q024 | gate | A-016; Original definitions recovered; the supplied literal L_X^j P^j display has an inconsistent superscript relative to those definitions. A016 proves the exact typed identification on the corrected shared pieces L_X^j P^i; no silent source correction.; Original Montpellier PDFp38/site37 and definingPDFpp33,34,36 visually checked; top/bottom target crops at240dpi. |
| A-Q030 | gate | A-016; The first equality Lambda_Y r=r Lambda_X(1-Q_Xtop) is proved in A016. The second literal equality places p_X next to id_Y and is ill-typed in the original image; A016 proves the explicitly repaired equality with p_Y.; Original Montpellier PDFp38/site37 and definingPDFpp33,34,36 visually checked; top/bottom target crops at240dpi. |
| A-Q047 | gate | A-017; Original target asks this reconstruction question; neighboring pages give the model from a rank-two module, but no inverse construction recovering that model and the full family from one unlabeled triangulation.; Original Montpellier PDFpp46-51 visually inspected; targetp51/site50; rank-two module, torsor, wedge and125-prime recovered. |
| A-Q056 | gate | ; Document and context recovered: the1972 Esquisse thematique historical topology paragraph, continuing beyond the leaf. It specifies no additional mathematical theorem to verify, so no coefficient conclusion is inferred.; Original Montpellier PDFpp215-217 visually inspected; p215 title identifies1972 Esquisse thematique, targetp217/site216 is typed reportp3. |
| A-Q080 | gate | A-006; A-010; The page does not specify ring multiplication and lambda operations on that target; SGA6 universal Chern-ring formulation is identified, but no unmentioned target structure is asserted.; Original Montpellier PDFp9 / sitep8 visually inspected; see PRIMARY_SCAN_FOLLOWUP.md; p6/p8 details260dpi, p19 detail300dpi. |
| A-Q122 | gate | A-007; A-020; A-021; A-023; Positive cases now include all characteristic-zero fields and DVRs, with the actual rationalization map proved. F_p gives the modular failure and A023 gives a characteristic-zero local failure. No complete necessary-and-sufficient classification of coefficient rings has been obtained.; Original Montpellier PDFp29/sitep28 visually inspected; study text read independently. |
| Q-ARCH-CONTEXT | precise mathematical and target-definition gates | Original contexts are recovered. Remaining inputs include crystalline Lefschetz/freeness, the stated motivic self-duality map, and reconstruction from one unlabeled triangulation; see assertion-level archive rows. |
| Q-EFFICIENT | open | G-009--G-011 give terminating positive formulas; no polynomial input-size bound for Hilbert bases, Reynolds lists, or elimination. |
| Q-OUTER5 | open with strictly smaller central gate | G-021 proves all two-row quotient functors for c≥2k, with122 active positive terms and155 exact support exceptions. Its exact multiplication and complement pairings cover λ2+λ3≤2n or λ3+λ4≥2n. Remaining direct region: λ2+λ3>2n>λ3+λ4; evaluate its actual H1 correction and finite-group covariants. |
| Q-MAP | open with reduced component and finite boundary gates | G-011 counts ranks effectively; G-013 gives prime-adjacent semigroup preimages; G-014 lifts every tail of size at most the coordinate degree; R-011--R-015 certify specified common-polarization boundaries. R-019--R-023 remove the full first-row boundary band and the rectangular prolongation; R-024 gives recursive second-row ranges from actual degree-five and square bases. The remaining critical annihilator injects into N_r tensor Sym^(r²-1), where N_r has first row at least r²+1 and second row at least r(r-1). |
| Q-W7 | open | T-018 evaluates the end-node sector; G-010 gives a general finite count; evaluate the remaining boundary valuation filtration. |
| Q-ALPOGE | input and explicit-morphism gate | No such comparison map is specified in the four-page note; T-001--T-003 construct the exact compact realization used here. |
| Q-MASULLO | input gate | No Masullo source or statement identifier in the 25 supplied files. |

Checkpoint04 is prepared at the scheduled45-minute boundary. It contains the current complete deliverables, full work documentation and attached sources; earlier checkpoint ZIPs are excluded. Research continues.
