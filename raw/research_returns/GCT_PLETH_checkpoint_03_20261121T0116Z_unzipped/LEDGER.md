# GCT_PLETH dated work ledger

Run: GCT_PLETH_20261121_run01. User-facing date: 21 November 2026, Europe/Berlin.
Start: 20 November 2026, 23:01:08.313727 UTC (21 November, 00:01:08 Berlin).
Models: GPT-6 Astra Pro, root and three delegated agents. Reasoning effort is not exposed.

## Current main questions

| Row | State | Strongest proved reduction / next operation |
|---|---|---|
| Archive, exact operations | substantially proved/refuted, precise context gates active | All13 original target leaves inspected;123 assertion rows:80proved,25refuted,18 exact gates. A001–A023 give the defined operations, integral tensor equality, DVR classification and explicit local-ring counterexample. |
| Positive lattice counts | proved with terminating preprocessing | G009 for symmetric plethysm, G010 for all Schur plethysm, G011 for actual canonical-map image. Every step uses explicit generators and finite algorithms. |
| Efficient positive formulas | open, smaller gates | T037 completes every outer-degree-four coefficient with≤108 fixed polytopes. G015 gives the exact all-rank flag ideal. G019 evaluates all Sym^a Q on the five-point quadratic ray, with≤16 active positive tags and complete44-exception support; G017,G018,T039–T041 cover related bundles. Arbitrary rank-three Schur twists and other first-line degrees remain the direct gate; general preprocessing bounds remain open. |
| Canonical-map ranges | specified blocks proved; full family open | Current checked full bound b>=(a-1)^2 (Sra III Thm1.3). R021 gives every even-rank boundary determinant preimage; R023 removes its exact prolongation and restricts the remaining critical first factor to rowsν1≥r²+1,ν2≥r(r−1). R024 gives recursive component ranges from actual degree-five and square bases. Further explicit boundary vectors are being checked. |
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
