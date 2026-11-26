# Progress ledger

Research started: 24 November 2026, approximately 20:59 Europe/Berlin
(19:59 UTC). Times below are actual observations, not simulated elapsed time.
First 45-minute checkpoint is due at approximately 21:44 Europe/Berlin.
The first formal progress review is due after about three hours of work;
subsequent reviews are hourly. Two consecutive reviews with no movement
trigger the stopping rule in the supplied prompt.

## Initial gates

| Item | Status | Strongest current gate |
|---|---|---|
| Q1a, complex field | Open | Construct a finite exact strict shortening, or prove none exists. |
| Q1a, field of two elements | Open | Same, with coefficients in the field itself. |
| Q1b, contracting or flat | Open | Audit the definitions and the alternative theorem; neither case selected. |
| Q1b, exclusivity | Open | Flatness does not immediately negate the stated rank-step inequality. |
| Q1c | Open | Determine the relation between shortening and flatness, then contraction. |
| Q2, three parties | Open | Identify which normalized wire exponents extend to all tensors. |
| Q2, four parties | Open | Exact cone; Euclidean square as a first test. |
| Q2, five parties | Open | Exact cone, including possible constraints beyond CAT(0). |
| Q2, cross-polytope and centre | Open | Saturated diameters and CAT(0) rigidity. |
| Q3 | Open | Formalize the class of hub arguments before claiming a universal ceiling. |

## Working entry: 24 November 2026, 21:07 Europe/Berlin

The following are under independent proof review. This entry is not the
three-hour stopping review.

- A multiplicity-profile construction yields a homogeneous selector
  inequality for every price. It removes the scale limitation in Fact 5.
- Using the all-tensor duality of the attached Anthropic manuscript,
  absence of shortening forces a price dominated by Euclidean distance
  which saturates the coordinate diameters. A CAT(0) rigidity lemma is
  being checked to finish the converse.
- A proposed field-descent argument uses a finite multiplication algebra
  and constant auxiliary wire cost after tensor powers.
- The four-thirds and five-fourths exponent calculations are being
  separated from claims of a universal method ceiling.
- A Fourier calculation shows that all Hilbert-valued maps on
  Mat_2(F_2) satisfy the strict rank-step bound with squared factor 3/2.
  Thus the prompt's claim that a Euclidean cube defeats the actual
  rank-step inequality is not justified.

## Review log

Scheduled reviews are appended below; earlier working entries remain historical.

## Working entry: 24 November 2026, 20:40 UTC (21:40 Europe/Berlin)

This is an interim ledger entry, not a scheduled stopping review.

| Main item | Status | Strictly reduced gate or decided subcase |
|---|---|---|
| Q1a, both fields | Open | Equivalent to failure of flatness; a finite complete-wire-graph obstruction is sufficient. Field extensions add no new shortening possibilities. |
| Q1b, choice | Open | CAT(0) necessity is insufficient, as sqrt(rank) embeds in a building cone. No-square would imply every price is a tree metric; explicit tree contraction is being checked. |
| Q1b, exclusivity / Q1c | Open | Q1c is exactly the exclusivity question once strict shortening iff not-flat is used. Hilbert geometry cannot refute contraction. |
| Q2, three parties | PROVED | Every pseudometric over both fields, indeed every field. |
| Q2, four/five parties | Open | All complex tree metrics are prices; square existence is equivalent to existence of any non-tree price. All-field tree inclusion is being independently checked. |
| Q2, cross-polytope plus centre | Open | Saturated dominated prices force a Euclidean ball by CAT(0) rigidity; no explicit normalized realization found. |
| Q3 | Open | Exact 4/3 balance in the stated complete-network inequalities and exact5/4 barrier in the specified two-hub model; unrestricted method remains unformalized. |

No formal no-movement review has been counted. First scheduled checkpoint remains20:44:50 UTC; first scheduled review remains approximately22:59:50 UTC.

## Checkpoint 01 preparation

The first scheduled checkpoint captures the active incomplete draft, exact programs and certificates, and all available check logs. Its scheduled time is20:44:50 UTC on24November2026. It is a research checkpoint, not a stopping review or a completion claim.


## Working entry: 24 November 2026, 21:25 UTC (22:25 Europe/Berlin)

This is an interim entry for checkpoint 02, not a scheduled stopping review.

| Main item | Status | Current strongest gate and movement |
|---|---|---|
| Q1a, C and F_2 | Open | For each fixed D, no shortening iff the Euclidean crosspolytope is a price iff all finite Euclidean D-configurations are prices (SH-15, PG-CROSSPOLY-GATE). This is a smaller finite gate than the earlier all-configuration formulation. |
| Q1b, choice | Open | No-square implies all prices are trees and explicit contraction at n=4,s=15/8 (PG-TREE-CONTRACTION). Square membership remains undecided. A CND graph-conversion route is being checked. |
| Q1b, exclusivity / Q1c | Open | Still exactly the possible coexistence of flatness and contraction; no decision. |
| Q2, three parties | PROVED | Every pseudometric over every field. |
| Q2, four parties | Open, reduced | Exactly two possible classes: all tree pseudometrics if the square is absent; all four-point CAT(0)-embeddable pseudometrics if it is present. Full proof PG-FOUR-CORE and PG-FOUR-CONDITIONAL. Only the square decision remains for this classification. |
| Q2, five parties | Open | All trees over every field; CAT(0) embeddability characterized externally by weighted quadruple inequalities. Planar-core-plus-pendants sufficiency is false already for an explicit square-plus-height-point configuration (PG-FIVE-CORE-FAIL). |
| Q2, crosspolytope and centre | Open, reduced | Its Euclidean metric is a price exactly when no shortening exists in that fixed dimension; the centre is not needed for this equivalence. Arbitrary pseudometric classification on these party counts remains open. |
| Q3 | Open in unrestricted scope | Exact fixed-power supremum4/3 for arbitrary two hubs, arbitrary antipodal unit directions, integer edge widths, and binary averaging selector accounting; h=O(B^(4/3)(log B)^(1/3)), with4/3 attained by the supplied conditional construction (EX-19). Fixed-size richer averaging seeds do not improve the power (EX-20). Actual spectral selectors and other layouts remain outside this barrier. |

New checked route results: two-cut rank is within a factor4 of complex sums-of-squares length; no planar shortening gives the exact finite lower bound in RT-SOS. The checked crossing identity gives chi_F(q)<=q^(sqrt2+o(1)) over every field (RT-SOS-UPPER). Repeated graph-image substitution cannot improve the maximum-cut asymptotic exponent for fixed wire graphs (RT-IMAGE). These do not select the open alternatives.

Checkpoint01 was saved at20:45:29 UTC,39seconds after its scheduled20:44:50 time. Checkpoint02 is scheduled21:29:50 UTC. First formal progress review remains22:59:50 UTC. No no-movement review has been counted.

## Working entry: 24 November 2026, 22:09 UTC

This is an interim entry for checkpoint03, not a scheduled stopping review.

| Main item | Status | Current strongest gate and movement |
|---|---|---|
| Q1a, C and F_2 | Open, reduced | Every strict shortening must have m>=5. SH-23--26 exclude all widths m<=4 in every dimension and arbitrary internal layouts. D6..9 at width4 have exact rational Farkas certificates, checked by an independent verifier; D>=10 follows from complement-even Fourier variance and Cantelli. Fixed-D crosspolytope equivalence remains in force. |
| Q1b, choice | Open, reduced sufficient gate | The one eight-party asymptotic cover H_4<=G_4 would force explicit contraction at n=3,s^2=3-2^-523336 (SH-22). No-square still gives n=4,s=15/8. A uniform Izeki--Nayatani invariant below1 on actual price realizations is another sufficient condition. None of these antecedents has been proved. |
| Q1b, exclusivity / Q1c | Open | Still exactly possible coexistence of flatness and contraction. Hilbert geometry satisfies strict contraction and cannot separate the alternatives. |
| Q2, three parties | PROVED | Every pseudometric over every field. |
| Q2, four parties | Open, single decision | Square membership decides between precisely the tree metrics and all CAT(0)-embeddable four-point metrics. No square decision yet. |
| Q2, five parties | Open | The tripod-times-line witness excludes every Euclidean-core-plus-pendants representation, in every Euclidean dimension. Over C, a capacity argument excludes K_(3,2)(q) border conversion to a triangle times an edge for all q>1, including every equal tensor power. This is a strengthened route obstruction, not an asymptotic price decision. |
| Q2, crosspolytope plus centre | Open | Its Euclidean metric is a price iff no shortening exists in the fixed dimension. No alternative selected. |
| Q3 | Open in unrestricted scope, reduced model gap | The exact4/3 fixed-power supremum now covers arbitrary radial lengths with all target segments through one common origin, arbitrary two hubs, integer widths, and the stated averaging selector debit. The upper bound is O(B^(4/3)log B). Actual spectral selector improvements and more general layouts remain outside this theorem. |

Checkpoint02 was created at21:29:50.033663 UTC and saved successfully.
Checkpoint03 remains scheduled for22:14:50 UTC. First formal review remains
22:59:50 UTC; no no-movement review has been counted. Width5 investigations
continue separately; unverified solver infeasibility is not counted as a proof.

Further checked before checkpoint03: SH-27 leaves only A=2 and 4<=D<=14 at width5, over every field. PG-CAP-HYPER extends the equal-size complex border obstruction to all K_(r,r-1)->K_r disjoint-union K_(r-1), r>=3. EX-24 improves the growing-seed coefficient to q^(1/6), retaining the4/3 supremum for subpolynomial seed size. These updates do not decide any remaining main alternative.


## Working entry: 24 November 2026, 22:55 UTC

This is preparation for checkpoint04, not the scheduled stopping review.
All widths m<=5 have now been excluded over every field, with the complete
273+439-certificate proof independently checked and written. The first
remaining planar rank relaxation at m6 is feasible (SH-30); this is a method
limit, not a shortening. The contraction test now has seven parties (SH-29),
and six-point square-root metrics are L1 (EX-25). The crossing-operator
functional needs a second power regularization; the exact finite Schur
block has been checked independently in all65536 tensor coordinates. The
new star-hub barrier (EX-26) retains4/3 for growing hub counts under its
stated selector debit. The first formal review remains due22:59:50 UTC.


## Formal review01: 2026-11-24T22:59:50.030844+00:00

Scheduled due time: 2026-11-24T22:59:50+00:00.

| Requested item | State | Strongest result and proof location |
|---|---|---|
| Q1a over C | Undecided | No strict shortening exists at any width m<=5, in any dimension or layout (SH-23--28). Strict shortening iff failure of flatness (SH-08). For fixed D, no shortening iff its Euclidean crosspolytope is a price (SH-15, PG-CROSSPOLY-GATE). |
| Q1a over F_2 | Undecided | The same all-width-m<=5 exclusion and fixed-D equivalences hold. Existence depends only on characteristic (EX-07); no shortening was found in the checked crossing-identity searches. |
| Q1b: contracting/flat over C | Undecided | No-square gives explicit n=4,s=15/8. A single seven-party asymptotic cover K_(4,3) to K_4 disjoint-union K_3 would give explicit n=3,s^2=3-2^-523336 (SH-29). A uniform Izeki--Nayatani invariant bound is another sufficient gate (PG-IN-GATE). |
| Q1b: contracting/flat over F_2 | Undecided | The same no-square and seven-party cover implications hold with explicit constants. General CAT(0) necessity alone is insufficient (PG-BUILDING). |
| Q1b: mutual exclusion | Undecided | Hilbert maps satisfy a strict rank-step inequality already at Mat_2(F_2), factor 3/2 (PG-HILB2). Thus Euclidean prices alone do not refute contraction. |
| Q1c over C | Undecided | Reduced exactly to mutual exclusion of flatness and contraction (SH-09). Strict shortening does imply contraction. |
| Q1c over F_2 | Undecided | Same reduction, with no characteristic change. |
| Q2: three parties over C | Proved | Every pseudometric, by nonnegative star-arm decomposition (PG-THREE). |
| Q2: three parties over F_2 | Proved | Same proof over every field (PG-THREE). |
| Q2: four parties over C | Undecided | Reduced to square membership: absent gives exactly tree pseudometrics; present gives exactly CAT(0)-embeddable four-point pseudometrics (PG-FOUR-CONDITIONAL). |
| Q2: four parties over F_2 | Undecided | The same exact conditional four-point classification holds over every field (PG-TREE-ALL, PG-FOUR-CONDITIONAL). |
| Q2: five parties over C | Undecided | All trees included; weighted quadruple inequalities are necessary. A CAT(0) metric in a tripod times a line has no Euclidean-core-plus-pendants representation in any dimension (PG-FIVE-NONL1). K_(r,r-1)(q) does not border-restrict to K_r(q) times K_(r-1)(q), for every r>=3 and q>1 over C (PG-CAP-HYPER); the asymptotic cover gate remains open. |
| Q2: five parties over F_2 | Undecided | All tree pseudometrics included over every field; same geometric necessary inequalities and failed Euclidean-core representation route. The complex capacity obstruction is not asserted in characteristic two. |
| Q2: Euclidean square, both fields | Undecided | Equivalent to existence of any non-tree price over the same field; it would imply every finite planar Euclidean metric is a price. |
| Q2: cross-polytope plus centre, both fields | Undecided | Euclidean metric is a price iff no strict shortening exists in that fixed D, iff all finite Euclidean D-configurations are prices (PG-CROSSPOLY-GATE). Full pseudometric class remains open. |
| Q3: exact supremum and matching limit | Undecided | Exact fixed-power supremum4/3 for arbitrary two hubs, integer weighted graphs, all wire segments through one common origin with arbitrary end radii, and the stated averaging selector debit (EX-23). Upper bound O(B^(4/3) log B); supplied complete-network construction attains4/3 conditionally. The same4/3 fixed-power ceiling holds for arbitrarily many star-connected hubs with unit antipodal endpoints and selector charge ak(log r)C (EX-26). Subpolynomial seed sizes cannot improve the power. Unrestricted selectors/layouts remain open. |


This is the first formal three-hour review, assessed against the initial gates.
Movement is present: Q2 on three parties changed from open to proved over both
fields; Q1c reduced exactly to exclusivity; the no-shortening decision reduced
to the finite crosspolytope gate in each dimension; all widths at most five
were excluded; the four-party classification reduced to square membership;
and the sufficient contraction test reduced from the eight-party even test
to one seven-party odd-hypermetric asymptotic cover. These are substantive
status or gate changes, not packaging or numerical search counts alone.

The central alternatives remain open over C and F2. Neither a strict
shortening nor all-dimensional flatness has been established. The seven-party
cover is a sufficient contraction gate whose antecedent is still unproved;
it is not an equivalence. The operator-mean gate r(C2)>2 is also unproved.
The width-six rank/Crofton feasible profile and its fractional-capacity
realization limit the current necessary-inequality method; they do not
construct a tensor decomposition or an integer-wire shortening.

Q3 remains open in unrestricted scope. Its proved4/3 ceiling covers the
specified common-origin two-hub model and the separate growing star-hub
model, both with stated selector accounting. General hub trees, arbitrary
target layouts, and better actual spectral selectors remain outside them.

Decision: continue the authorized research. Consecutive scheduled reviews
without movement:0. The next formal review is due2026-11-24T23:59:50Z.
The next checkpoint after04 is due2026-11-24T23:44:50Z.


## Working entry: 24 November2026,23:40 UTC

Checkpoint05 preparation only; the next formal review remains23:59:50 UTC. Since review01: RT-W6-PARAM leaves only (A=2,D=2..19) or(A=3,D=2..16); RT-W6-EULER forces an odd-degree internal vertex in both planar two-term networks. SH-33 permits seven-party cover exponent1/128 or a balanced growing-party exponent r^2/2048. PG-CYCLE-FINITE/AMPLIFICATION gives an exact finite certificate for planar shortening, and PG-CYCLE-SPECIALIZATION gives a bounded-width almost-all-primes equivalence. PG-CROSSING-EXPONENT-GAP reduces the asymptotic exponent to1 orsqrt2, without selecting a branch. EX-29 extends the common-origin4/3 ceiling to polynomially many fixed labelled hubs; EX-30 permits adaptive graphs and assignments for subpolynomially many hubs. All main undecided rows remain undecided; Q2 on three parties remains proved. No-movement counter remains0 pending the next scheduled assessment.

Before checkpoint05, PG-CYCLE-FINITE-LOWER further excludes dyadic cycle-certificate widths1,2,3 by u(Cq)>=q(3q-1)/(q+1); the first unexcluded dyadic certificate width is4. The99-page checkpoint paper compiles without warnings;16 new/revised pages were visually checked. This is a working addition, not a formal review.


## Formal review02: 2026-11-24T23:59:50.834386+00:00

Scheduled due time: 2026-11-24T23:59:50+00:00.

| Requested item | State | Strongest result and proof location |
|---|---|---|
| Q1a over C | Undecided | No strict shortening exists at any width m<=5, in any dimension or layout (SH-23--28). At width6 only(A=2,D=2..19) or(A=3,D=2..16) remain; both planar two-term networks must contain an odd-degree internal vertex (RT-W6-PARAM/EULER). Strict shortening iff failure of flatness (SH-08). For fixed D, no shortening iff its Euclidean crosspolytope is a price (SH-15, PG-CROSSPOLY-GATE). |
| Q1a over F_2 | Undecided | The same width<=5 exclusion, narrowed width6 parameters and fixed-D equivalences hold. Existence depends only on characteristic (EX-07); no shortening was found in the checked crossing-identity searches. |
| Q1b: contracting/flat over C | Undecided | No-square gives explicit n=4,s=15/8. A seven-party cover exponent at most1/128, or balanced K_(r,r) to two r-cliques with exponent at most r^2/2048 for some r divisible by4, would give explicit n=3,s^2=3-2^-523336 (SH-33). A uniform Izeki--Nayatani invariant bound is another sufficient gate (PG-IN-GATE). |
| Q1b: contracting/flat over F_2 | Undecided | The same no-square and positive-overhead cover implications hold with explicit constants (SH-33). General CAT(0) necessity alone is insufficient (PG-BUILDING). |
| Q1b: mutual exclusion | Undecided | Hilbert maps satisfy a strict rank-step inequality already at Mat_2(F_2), factor 3/2 (PG-HILB2). Thus Euclidean prices alone do not refute contraction. |
| Q1c over C | Undecided | Reduced exactly to mutual exclusion of flatness and contraction (SH-09). Strict shortening does imply contraction. |
| Q1c over F_2 | Undecided | Same reduction, with no characteristic change. |
| Q2: three parties over C | Proved | Every pseudometric, by nonnegative star-arm decomposition (PG-THREE). |
| Q2: three parties over F_2 | Proved | Same proof over every field (PG-THREE). |
| Q2: four parties over C | Undecided | Reduced to square membership: absent gives exactly tree pseudometrics; present gives exactly CAT(0)-embeddable four-point pseudometrics (PG-FOUR-CONDITIONAL). |
| Q2: four parties over F_2 | Undecided | The same exact conditional four-point classification holds over every field (PG-TREE-ALL, PG-FOUR-CONDITIONAL). |
| Q2: five parties over C | Undecided | All trees included; weighted quadruple inequalities are necessary. A CAT(0) metric in a tripod times a line has no Euclidean-core-plus-pendants representation in any dimension (PG-FIVE-NONL1). K_(r,r-1)(q) does not border-restrict to K_r(q) times K_(r-1)(q), for every r>=3 and q>1 over C (PG-CAP-HYPER); the asymptotic cover gate remains open. |
| Q2: five parties over F_2 | Undecided | All tree pseudometrics included over every field; same geometric necessary inequalities and failed Euclidean-core representation route. The complex capacity obstruction is not asserted in characteristic two. |
| Q2: Euclidean square, both fields | Undecided | Equivalent to any non-tree price and to planar flatness. The regularized cycle-cover value is exactly2 or2^sqrt2; square absence is equivalent to one finite dyadic cycle cover of cost below q^sqrt2 (PG-CYCLE-GAP/FINITE). The two-cut rank exponent is exactly1 orsqrt2; neither branch is selected. |
| Q2: cross-polytope plus centre, both fields | Undecided | Euclidean metric is a price iff no strict shortening exists in that fixed D, iff all finite Euclidean D-configurations are prices (PG-CROSSPOLY-GATE). Full pseudometric class remains open. |
| Q3: exact supremum and matching limit | Undecided | A4/3 fixed-power ceiling now covers arbitrary common-origin radii and polynomially many hubs with a fixed labelled connected graph and the prescribed averaging-selector debit (EX-29). It also covers subpolynomially many hubs with graph and assignment chosen after the partition (EX-30). If the claimed direct-case theorem is correct, its complete-network construction attains4/3. Non-common-origin segments, polynomially many adaptive hubs and improved actual spectral selectors remain open. |


No previously undecided main yes/no item was resolved in this hour.
Movement is nevertheless present under the user's stated gate criterion:

1. The width-six part of the Q1a search is now restricted to A=2 with
   D=2..19, or A=3 with D=2..16. In the planar two-term case both networks
   must contain an internal vertex of odd integer weighted degree.
   These proved exclusions strictly reduce the remaining search domain.
2. The square/planar-shortening decision now has an equivalent finite
   cycle-cover certificate with no geometric auxiliary vertices. The
   first four dyadic certificate widths are excluded; the first width
   not excluded is m=5. The two-cut rank exponent is reduced to the
   discrete alternatives1 and sqrt2. Neither alternative is selected.
3. The sufficient explicit-contraction cover gate now permits a positive
   exponent1/128 on seven parties, or r^2/2048 on balanced8t-party
   instances. A family with2^{o(r^2)} terms at binary wire dimension
   would suffice. This weakens the previously required zero overhead;
   it is a sufficient condition, not a claimed equivalence.
4. The Q3 common-origin4/3 ceiling now includes polynomially many hubs
   with a fixed labelled connected graph, and subpolynomially many
   hubs when the graph and group assignment can be chosen after the
   partition. Polynomially many adaptive hubs, non-common-origin
   target segments and improved actual spectral selector costs remain
   outside the proved barrier.

The new finite-identity verification, sparse-map obstruction, failed
numerical searches, paper compilation and checkpoint packaging are not
counted as movement. Q2 on three parties was already proved before the
first review and is not counted again. The no-square finite certificate
is still unconstructed; no strict shortening or all-dimensional flatness
has been established over either C or F2. The exact general four- and
five-party and crosspolytope price classifications remain undecided.
Q1c remains precisely the unresolved flat/contracting exclusivity issue.

Decision: continue the authorized research. Consecutive scheduled reviews
without movement:0. The next formal review is due2026-11-25T00:59:50Z.
The next checkpoint is06, due2026-11-25T00:29:50Z. No extra checkpoint
is created at this review.


## Working entry: 25 November2026,00:20 UTC

After review02, the cycle-certificate gate has narrowed again: PG-CYCLE-Q32 excludesq32 by an exact205-profile certificate independently reconstructed by the root verifier and a separately checked exceptional-profile proof. The first dyadic width not excluded is nowm6(q64). A feasible necessary capacity profile atq64 is not an actual cover. Normalized dense K33 searches found no identity; their finite numerical failures are not counted as movement. This entry is not a scheduled stopping review.

## Checkpoint06 preparation: 25 November2026,00:27 UTC

The manuscript now contains111 pages. Independent root proof checks passedSH34a/b, SH35, EX31--35, the rank-at-most-two residual lemma, its resource refinement and the allfield strict slice/CAR obstruction. Theq32 gate is excluded andq64 remains the first unexcluded dyadic cycle width; the corrected six-resource necessary profile has cost313 and smaller-rank sum65. The same-graph integer packing route is explicitly refuted and repaired for its counterexample. This is checkpoint preparation, not a scheduled stopping review; counter0 and nextreview00:59:50 remain unchanged.


## Formal review03: 2026-11-25T00:59:50.030482+00:00

Scheduled due time: 2026-11-25T00:59:50+00:00.

| Requested item | State | Strongest result and proof location |
|---|---|---|
| Q1a over C | Undecided | No strict shortening exists at any width m<=5, in any dimension or layout (SH-23--28). At width6 only(A=2,D=3..19) or(A=3,D=3..16) remain; every planar width6 case is excluded (SH-37--38). Planar two-term width7 is also excluded. Strict shortening iff failure of flatness (SH-08). For fixed D, no shortening iff its Euclidean crosspolytope is a price (SH-15, PG-CROSSPOLY-GATE). |
| Q1a over F_2 | Undecided | The same width<=5 exclusion, width6 restrictions to D>=3, planar two-term width7 exclusion and fixed-D equivalences hold (SH-38). Existence depends only on characteristic (EX-07); no shortening was found in the checked crossing-identity searches. |
| Q1b: contracting/flat over C | Undecided | No-square gives explicit n=4,s=15/8. A seven-party cover exponent at most1/128, or balanced K_(r,r) to two r-cliques with exponent at most r^2/2048 for some r divisible by4, would give explicit n=3,s^2=3-2^-523336 (SH-33). A uniform Izeki--Nayatani invariant bound is another sufficient gate (PG-IN-GATE). |
| Q1b: contracting/flat over F_2 | Undecided | The same no-square and positive-overhead cover implications hold with explicit constants (SH-33). General CAT(0) necessity alone is insufficient (PG-BUILDING). |
| Q1b: mutual exclusion | Undecided | Hilbert maps satisfy a strict rank-step inequality already at Mat_2(F_2), factor 3/2 (PG-HILB2). A model containing all flats and trees and having CAT(0) realizations also contracts uniformly (EX-32); it is not a class of actual prices. The geometric properties alone do not decide exclusivity. |
| Q1c over C | Undecided | Reduced exactly to mutual exclusion of flatness and contraction (SH-09). Strict shortening does imply contraction. |
| Q1c over F_2 | Undecided | Same reduction, with no characteristic change. |
| Q2: three parties over C | Proved | Every pseudometric, by nonnegative star-arm decomposition (PG-THREE). |
| Q2: three parties over F_2 | Proved | Same proof over every field (PG-THREE). |
| Q2: four parties over C | Undecided | Reduced to square membership: absent gives exactly tree pseudometrics; present gives exactly CAT(0)-embeddable four-point pseudometrics (PG-FOUR-CONDITIONAL). |
| Q2: four parties over F_2 | Undecided | The same exact conditional four-point classification holds over every field (PG-TREE-ALL, PG-FOUR-CONDITIONAL). |
| Q2: five parties over C | Undecided | All trees included; weighted quadruple inequalities are necessary. A CAT(0) metric in a tripod times a line has no Euclidean-core-plus-pendants representation in any dimension (PG-FIVE-NONL1). K_(r,r-1)(q) does not border-restrict to K_r(q) times K_(r-1)(q), for every r>=3 and q>1 over C (PG-CAP-HYPER); the asymptotic cover gate remains open. |
| Q2: five parties over F_2 | Undecided | All tree pseudometrics included over every field; same geometric necessary inequalities and failed Euclidean-core representation route. The complex capacity obstruction is not asserted in characteristic two. |
| Q2: Euclidean square, both fields | Undecided | Equivalent to any non-tree price and to planar flatness. The regularized cycle-cover value is exactly2 or2^sqrt2; square absence is equivalent to one finite dyadic cycle cover of cost below q^sqrt2 (PG-CYCLE-GAP/FINITE). The two-cut rank exponent is exactly1 orsqrt2; neither branch is selected. |
| Q2: cross-polytope plus centre, both fields | Undecided | Euclidean metric is a price iff no strict shortening exists in that fixed D, iff all finite Euclidean D-configurations are prices (PG-CROSSPOLY-GATE). Full pseudometric class remains open. |
| Q3: exact supremum and matching limit | Undecided | A4/3 fixed-power ceiling now covers arbitrary common-origin radii and polynomially many hubs with a fixed labelled connected graph and the prescribed averaging-selector debit (EX-29). It also covers subpolynomially many hubs with graph and assignment chosen after the partition (EX-30). If the claimed direct-case theorem is correct, its complete-network construction attains4/3. Non-common-origin segments, polynomially many adaptive hubs and improved actual spectral selectors remain open. |


Movement is present under the user's stated criterion, although no remaining main yes/no alternative has been selected.

1. Q1a has a strictly smaller search domain. Every planar strict shortening of width at most6 is excluded over every field, and every planar two-term shortening of width at most7 is excluded (SH-37--38). The remaining width6 parameters are A=2,D=3..19 or A=3,D=3..16. The integer-flow parity calibration gives a universal strict geometric gap, independent of numerical searches and of the unsuccessful reserved-tree route.
2. The equivalent finite cycle-cover gate for square absence now starts at dyadic width7(q128). Width5(q32) is excluded by an independently reconstructed205-profile certificate; width6(q64) by an independently reconstructed540-profile certificate with one rational dual. The latter gives u(C64)>=359>64^sqrt2. Both exclusions were established after review02. Necessary profiles atq128 remain only a relaxation, with no local maps or qualifying cover.

Q1b still has no proof of flatness or explicit contraction over C or F2. Its positive-overhead seven-party and growing-balanced-cover sufficient gates are unchanged. Mutual exclusion remains unproved; the geometric countermodel is not a class of actual prices. Q1c remains exactly the flat/contracting exclusivity issue under the checked reduction.

Q2 on three parties was already proved before review01 and is not counted again. The exact four-party classification still depends on square membership; five-party and full crosspolytope price classifications remain undecided. The q32/q64 exclusions narrow the square's finite-certificate gate but do not select its branch.

Q3 has no new movement in this hour. The4/3 barrier still covers polynomially many fixed labelled common-origin hubs and subpolynomially many adaptive hubs with the stated selector debit. Polynomially many adaptive hubs, non-common-origin target segments and improved actual spectral selector costs remain open.

The explicit characteristic-two one-copy border conversion, newly audited published/preprint rank certificates, tangent-space border obstructions, larger unsuccessful numerical searches, compilation and checkpoint packaging are not needed to justify this review's movement. In particular a fixed-size border obstruction is not promoted to an asymptotic-overhead obstruction.

Decision: continue the authorized research. Consecutive scheduled reviews without movement:0. Next formal review:2026-11-25T01:59:50Z. Next checkpoint07:2026-11-25T01:14:50Z. No checkpoint ZIP is created at this review.

### Checkpoint07 preparation (not a formal progress review)

At01:14:50 UTC on25 November2026 the scheduled checkpoint includes the128-page paper, explicit integer sign-border formula and its cost accounting, independent q64 and binary-Jacobian verifiers, and SH39--40. SH40 excludes the previously open m6,D3,A2 case over every field. The main width-six gate is nowA2,D4..19 orA3,D3..16. This will be assessed at formal review04 at01:59:50 UTC. The consecutive no-movement count remains0 from review03; no additional review is being conducted here.


## Checkpoint08 preparation: 2026-11-25T01:57:20.569136+00:00

All agent-owned proof files are frozen. The paper has138 pages with stable references and no overfull boxes;23 changed pages passed visual inspection. The independently checked Q1a gate is now A=2,D=8..19 or A=3,D=3..16 at width6. SH40--43 supply the post-review03 gate reduction. General causal linear coding and globally stabilizer GHZ-assisted constructions have additional limitations, with scope stated in the paper. Neither limitation resolves arbitrary covers. The formal review remains scheduled for01:59:50 UTC and is not advanced by this preparation entry.


## Formal review04: 2026-11-25T01:59:50.077227+00:00

Scheduled due time: 2026-11-25T01:59:50+00:00.

| Requested item | State | Strongest result and proof location |
|---|---|---|
| Q1a over C | Undecided | No strict shortening exists at any width m<=5, in any dimension or layout (SH-23--28). At width6 only(A=2,D=8..19) or(A=3,D=3..16) remain; every planar width6 case and two-term dimensions3 through7 are excluded (SH-37--43). Planar two-term width7 is also excluded. Strict shortening iff failure of flatness (SH-08). For fixed D, no shortening iff its Euclidean crosspolytope is a price (SH-15, PG-CROSSPOLY-GATE). |
| Q1a over F_2 | Undecided | The same width<=5 exclusion, width6 restrictions to D>=8 forA2 andD>=3 forA3, planar two-term width7 exclusion and fixed-D equivalences hold (SH-38). Existence depends only on characteristic (EX-07); no shortening was found in the checked crossing-identity searches. |
| Q1b: contracting/flat over C | Undecided | No-square gives explicit n=4,s=15/8. A seven-party cover exponent at most1/128, or balanced K_(r,r) to two r-cliques with exponent at most r^2/2048 for some r divisible by4, would give explicit n=3,s^2=3-2^-523336 (SH-33). A uniform Izeki--Nayatani invariant bound is another sufficient gate (PG-IN-GATE). |
| Q1b: contracting/flat over F_2 | Undecided | The same no-square and positive-overhead cover implications hold with explicit constants (SH-33). General CAT(0) necessity alone is insufficient (PG-BUILDING). |
| Q1b: mutual exclusion | Undecided | Hilbert maps satisfy a strict rank-step inequality already at Mat_2(F_2), factor 3/2 (PG-HILB2). A model containing all flats and trees and having CAT(0) realizations also contracts uniformly (EX-32); it is not a class of actual prices. The geometric properties alone do not decide exclusivity. |
| Q1c over C | Undecided | Reduced exactly to mutual exclusion of flatness and contraction (SH-09). Strict shortening does imply contraction. |
| Q1c over F_2 | Undecided | Same reduction, with no characteristic change. |
| Q2: three parties over C | Proved | Every pseudometric, by nonnegative star-arm decomposition (PG-THREE). |
| Q2: three parties over F_2 | Proved | Same proof over every field (PG-THREE). |
| Q2: four parties over C | Undecided | Reduced to square membership: absent gives exactly tree pseudometrics; present gives exactly CAT(0)-embeddable four-point pseudometrics (PG-FOUR-CONDITIONAL). |
| Q2: four parties over F_2 | Undecided | The same exact conditional four-point classification holds over every field (PG-TREE-ALL, PG-FOUR-CONDITIONAL). |
| Q2: five parties over C | Undecided | All trees included; weighted quadruple inequalities are necessary. A CAT(0) metric in a tripod times a line has no Euclidean-core-plus-pendants representation in any dimension (PG-FIVE-NONL1). K_(r,r-1)(q) does not border-restrict to K_r(q) times K_(r-1)(q), for every r>=3 and q>1 over C (PG-CAP-HYPER); the asymptotic cover gate remains open. |
| Q2: five parties over F_2 | Undecided | All tree pseudometrics included over every field; same geometric necessary inequalities and failed Euclidean-core representation route. The complex capacity obstruction is not asserted in characteristic two. |
| Q2: Euclidean square, both fields | Undecided | Equivalent to any non-tree price and to planar flatness. The regularized cycle-cover value is exactly2 or2^sqrt2; square absence is equivalent to one finite dyadic cycle cover of cost below q^sqrt2 (PG-CYCLE-GAP/FINITE). The two-cut rank exponent is exactly1 orsqrt2; neither branch is selected. |
| Q2: cross-polytope plus centre, both fields | Undecided | Euclidean metric is a price iff no strict shortening exists in that fixed D, iff all finite Euclidean D-configurations are prices (PG-CROSSPOLY-GATE). Full pseudometric class remains open. |
| Q3: exact supremum and matching limit | Undecided | A4/3 fixed-power ceiling now covers arbitrary common-origin radii and polynomially many hubs with a fixed labelled connected graph and the prescribed averaging-selector debit (EX-29). It also covers subpolynomially many hubs with graph and assignment chosen after the partition (EX-30). If the claimed direct-case theorem is correct, its complete-network construction attains4/3. Non-common-origin segments, polynomially many adaptive hubs and improved actual spectral selectors remain open. |


Movement is present under the user's stated criterion. The remaining width-six two-term shortening gate has become strictly smaller after review03: dimensions3 and4 are excluded by independently checked analytic proofs SH40 andSH41; dimensions5 and6 are excluded by complete rational-certificate families independently reconstructed from their mathematical row labels. The current residual range, including any further independently checked exclusions, is stated in the status table above. These are universal all-field exclusions for arbitrary layouts and local maps, not finite searches for examples.

The main alternatives remain undecided. Q1a still has no explicit strict shortening and no proof of universal absence. Q1b still has neither explicit contraction nor flatness over C or F2, and mutual exclusion is open. Its positive-overhead seven-party and growing-balanced-cover sufficient gates have not been met. Q1c remains the flatness/contraction exclusivity question under the checked reduction.

Q2 on three parties was proved earlier and is not counted again. The four-party classification still depends on Euclidean-square membership. The square's finite cycle-certificate gate still first permits width7(q128); the new border identities do not meet its cost threshold. Five-party and full crosspolytope classifications remain undecided.

Q3 has no counted movement at this review. The established4/3 barrier covers the previously stated fixed labelled common-origin and subpolynomial adaptive-hub models; the unrestricted supremum remains open.

The universal integral rank witness, causal-linear-code limitation, stabilizer-selector barrier, additional source audits, failed searches and packaging are recorded with their actual scope. They are not needed to justify movement and are not treated as a resolution of an asymptotic cover gate.

Decision: continue the authorized research. Consecutive scheduled reviews without movement:0. Next formal review:2026-11-25T02:59:50Z. Checkpoint08 is due at this same01:59:50 boundary; the next checkpoint after it is09 at02:44:50Z. This script records only the formal review; the schedule wrapper creates the one authorized checkpoint ZIP.


## Checkpoint09 preparation: 2026-11-25T02:40:50.311497+00:00

All agent-owned proof and certificate writers are frozen. The156-page paper has stable references and no overfull boxes;27new or changed pages passed visual inspection. The independently checked width-six gate is A2,D10..19 or A3,D4..16 after SH46/47. EX42 gives the4/3 fixed-power ceiling for arbitrary lengths and segment centres in the exactly-two-hub prescribed-binary-debit model; unrestrictedQ3 remainsopen. The finite crown identities and quotient-preserving one-term-per-matching obstruction, and the local-unitary weighted-rank counterexample, are recorded with full proofs and independent checks. PartialD10/D11 searches are preserved but establish no further exclusion. This is checkpoint preparation, not an early formal review; review05 remains due02:59:50 UTC.


## Formal review05: 2026-11-25T02:59:50.152069+00:00

Scheduled due time: 2026-11-25T02:59:50+00:00.

| Requested item | State | Strongest result and proof location |
|---|---|---|
| Q1a over C | Undecided | No strict shortening exists at any width m<=5, in any dimension or layout (SH-23--28). At width6 only(A=2,D=10..19) or(A=3,D=4..16) remain; every planar width6 case and two-term dimensions3 through9 and three-term dimension3 are excluded (SH-37--47). Planar two-term width7 is also excluded. Strict shortening iff failure of flatness (SH-08). For fixed D, no shortening iff its Euclidean crosspolytope is a price (SH-15, PG-CROSSPOLY-GATE). |
| Q1a over F_2 | Undecided | The same width<=5 exclusion, width6 restrictions to D>=10 forA2 andD>=4 forA3, planar two-term width7 exclusion and fixed-D equivalences hold (SH-38). Existence depends only on characteristic (EX-07); no shortening was found in the checked crossing-identity searches. |
| Q1b: contracting/flat over C | Undecided | No-square gives explicit n=4,s=15/8. A seven-party cover exponent at most1/128, or balanced K_(r,r) to two r-cliques with exponent at most r^2/2048 for some r divisible by4, would give explicit n=3,s^2=3-2^-523336 (SH-33). A uniform Izeki--Nayatani invariant bound is another sufficient gate (PG-IN-GATE). |
| Q1b: contracting/flat over F_2 | Undecided | The same no-square and positive-overhead cover implications hold with explicit constants (SH-33). General CAT(0) necessity alone is insufficient (PG-BUILDING). |
| Q1b: mutual exclusion | Undecided | Hilbert maps satisfy a strict rank-step inequality already at Mat_2(F_2), factor 3/2 (PG-HILB2). A model containing all flats and trees and having CAT(0) realizations also contracts uniformly (EX-32); it is not a class of actual prices. The geometric properties alone do not decide exclusivity. |
| Q1c over C | Undecided | Reduced exactly to mutual exclusion of flatness and contraction (SH-09). Strict shortening does imply contraction. |
| Q1c over F_2 | Undecided | Same reduction, with no characteristic change. |
| Q2: three parties over C | Proved | Every pseudometric, by nonnegative star-arm decomposition (PG-THREE). |
| Q2: three parties over F_2 | Proved | Same proof over every field (PG-THREE). |
| Q2: four parties over C | Undecided | Reduced to square membership: absent gives exactly tree pseudometrics; present gives exactly CAT(0)-embeddable four-point pseudometrics (PG-FOUR-CONDITIONAL). |
| Q2: four parties over F_2 | Undecided | The same exact conditional four-point classification holds over every field (PG-TREE-ALL, PG-FOUR-CONDITIONAL). |
| Q2: five parties over C | Undecided | All trees included; weighted quadruple inequalities are necessary. A CAT(0) metric in a tripod times a line has no Euclidean-core-plus-pendants representation in any dimension (PG-FIVE-NONL1). K_(r,r-1)(q) does not border-restrict to K_r(q) times K_(r-1)(q), for every r>=3 and q>1 over C (PG-CAP-HYPER); the asymptotic cover gate remains open. |
| Q2: five parties over F_2 | Undecided | All tree pseudometrics included over every field; same geometric necessary inequalities and failed Euclidean-core representation route. The complex capacity obstruction is not asserted in characteristic two. |
| Q2: Euclidean square, both fields | Undecided | Equivalent to any non-tree price and to planar flatness. The regularized cycle-cover value is exactly2 or2^sqrt2; square absence is equivalent to one finite dyadic cycle cover of cost below q^sqrt2 (PG-CYCLE-GAP/FINITE). The two-cut rank exponent is exactly1 orsqrt2; neither branch is selected. |
| Q2: cross-polytope plus centre, both fields | Undecided | Euclidean metric is a price iff no strict shortening exists in that fixed D, iff all finite Euclidean D-configurations are prices (PG-CROSSPOLY-GATE). Full pseudometric class remains open. |
| Q3: exact supremum and matching limit | Undecided | A4/3 fixed-power ceiling now covers arbitrary common-origin radii and polynomially many hubs with a fixed labelled connected graph and the prescribed averaging-selector debit (EX-29). It also covers subpolynomially many hubs with graph and assignment chosen after the partition (EX-30). If the claimed direct-case theorem is correct, its complete-network construction attains4/3. Arbitrary segment centres and arbitrary lengths with exactly two hubs obey the4/3 fixed-power ceiling, h=O_a(B^(4/3)logB), with the prescribed binary-certificate debit (EX-42). Growing many-hub cases outside the earlier models remain open. The actual-selector gate for the complete-network construction is now only Gamma_k, the least ordinary normalized Euclidean scale of its2k cross-polytope endpoints (EX-43); Gamma_k=O(k^beta) would conditionally give alpha=1+1/[2(1+beta)]. Only1<=Gamma_k<=sqrt(k) is proved under flatness. |


Movement is present under the user's stated criterion. Q1a has a strictly smaller width-six gate than at review04: the complete two-term dimension8 and9 families are excluded by independently reconstructed exact rational certificates (SH47), and the complete three-term dimension3 case is excluded by2970 covered integer-propagation branches plus a hand proof for the three surviving profiles (SH46). Neither exclusion assumes a bounded family of layouts or local maps; both hold over every field. At the time these audits finished, the residual width-six gate was A2,D10..19 or A3,D4..16. Any further independently checked reduction is shown in the status table; incomplete numerical families are not counted.

Q3 has a proved larger barrier domain: EX42 covers arbitrary segment centres and arbitrary positive lengths with exactly two hubs and the prescribed binary-certificate selector debit, giving h=O_a(B^(4/3)logB). The auxiliary-partition/two-stage-signing proof and constants have independent full checks. It does not settle growing/adaptive many-hub configurations or actual spectral-selector normalization. The unrestricted supremum remains undecided; its claimed4/3 attainment remains conditional on the supplied direct theorem being correct. EX43 further reduces the actual-selector question to the ordinary normalized Euclidean scale Gamma_k on the2k endpoints alone: midpoint extension preserves the original GHZ factor and a balanced-block rigid ball contains every required hub. This reduction has an independent full check. Only1<=Gamma_k<=sqrt(k) is proved under flatness.

The main alternatives remain undecided. No strict shortening or proof of universal absence has been found. Flatness, explicit contraction, their exclusivity, and therefore the remaining Q1c alternative are open over C and F2. The SH33 asymptotic cover threshold is still unmet. Q2 on three parties was already proved before review01 and is not counted again. The four-party classification still depends on square membership, whose finite cycle-cover gate first permits q128. Five-party and full crosspolytope price classes remain open.

Finite crown identities, the all-r quotient-preserving one-term-per-matching obstruction, the local-unitary counterexample to weighted stabilizer-rank monotonicity, bounded searches, source audits, and packaging are not counted as main-gate movement. Their scopes and limitations remain explicit.

Decision: continue the authorized research. Consecutive scheduled reviews without movement:0. Next formal review:2026-11-25T03:59:50Z. Next checkpoint10:2026-11-25T03:29:50Z. No checkpoint ZIP is created at this review.


## Checkpoint10 preparation: 2026-11-25T03:27:14.540972+00:00

All agent-owned writers are frozen. The173-page paper has stable references and no overfull boxes;27selected new/changed/title/bibliography pages passed visual inspection. OverC, the complex-square gate is narrowed to the prescribed finite rational Specht-operator systems of PG-OP-DETERMINISTIC, using the new full-multiplicity SOS duality; no system has been solved. The regularized operator endpoint agrees with the universal cycle branch, without selecting it. The width-six and Gamma_k quantitative gates are unchanged. EX44, SH49-52b, the signed/positive finite tests and all exact independent verifiers are preserved. This is checkpoint preparation, not a formal review; review06 remains due03:59:50 UTC.


### Checkpoint10 writer-inventory correction (2026-11-25T03:37:39.311989+00:00)

The proof manuscripts and newly launched calculations were frozen, but a legacy dimension-ten diagnostic batch remained active in a separate command process namespace. It was identified and stopped at03:35:59 UTC using its exact verified parent command. The checkpoint archive remains valid, and no dimension-ten exclusion was claimed; those calculations were explicitly partial. The preparation statement that all writers were frozen was too broad. Root now owns separate retry outputs and a shared-file pause mechanism. See outputs/checkpoint10_legacy_writer_correction.json and the exact stop acknowledgement.


### Additional writer correction and checked D10 completion (2026-11-25T03:48:51.567818+00:00)

The analogous legacy dimension11 batch was also stopped, at03:38:27 UTC, with its exact parent command recorded in outputs/sh_stop_legacy_D11_acknowledgement.json. No D11 exclusion is inferred from those partial outputs. The separate root D10 retry run finished at03:44:16 UTC; its full independent semantic/rational/coverage verifier then passed26radial and405two-minimum certificates plus1149pruned branches. This reduces the width-six gate to A2,D11..19 orA3,D4..16. It will be assessed at scheduled review06, not as an extra review.


## Formal review06: 2026-11-25T03:59:50.025092+00:00

Scheduled due time: 2026-11-25T03:59:50+00:00.

| Requested item | State | Strongest result and proof location |
|---|---|---|
| Q1a over C | Undecided | No strict shortening exists at any width m<=5, in any dimension or layout (SH-23--28). At width6 only(A=2,D=11..19) or(A=3,D=4..16) remain; every planar width6 case and two-term dimensions3 through10 and three-term dimension3 are excluded (SH-37--47,SH-53). Planar two-term width7 is also excluded. Strict shortening iff failure of flatness (SH-08). For fixed D, no shortening iff its Euclidean crosspolytope is a price (SH-15, PG-CROSSPOLY-GATE). |
| Q1a over F_2 | Undecided | The same width<=5 exclusion, width6 restrictions to D>=11 forA2 andD>=4 forA3, planar two-term width7 exclusion and fixed-D equivalences hold (SH-38). Existence depends only on characteristic (EX-07); no shortening was found in the checked crossing-identity searches. |
| Q1b: contracting/flat over C | Undecided | No-square gives explicit n=4,s=15/8. A seven-party cover exponent at most1/128, or balanced K_(r,r) to two r-cliques with exponent at most r^2/2048 for some r divisible by4, would give explicit n=3,s^2=3-2^-523336 (SH-33). A uniform Izeki--Nayatani invariant bound is another sufficient gate (PG-IN-GATE). |
| Q1b: contracting/flat over F_2 | Undecided | The same no-square and positive-overhead cover implications hold with explicit constants (SH-33). General CAT(0) necessity alone is insufficient (PG-BUILDING). |
| Q1b: mutual exclusion | Undecided | Hilbert maps satisfy a strict rank-step inequality already at Mat_2(F_2), factor 3/2 (PG-HILB2). A model containing all flats and trees and having CAT(0) realizations also contracts uniformly (EX-32); it is not a class of actual prices. The geometric properties alone do not decide exclusivity. |
| Q1c over C | Undecided | Reduced exactly to mutual exclusion of flatness and contraction (SH-09). Strict shortening does imply contraction. |
| Q1c over F_2 | Undecided | Same reduction, with no characteristic change. |
| Q2: three parties over C | Proved | Every pseudometric, by nonnegative star-arm decomposition (PG-THREE). |
| Q2: three parties over F_2 | Proved | Same proof over every field (PG-THREE). |
| Q2: four parties over C | Undecided | Reduced to square membership: absent gives exactly tree pseudometrics; present gives exactly CAT(0)-embeddable four-point pseudometrics (PG-FOUR-CONDITIONAL). |
| Q2: four parties over F_2 | Undecided | The same exact conditional four-point classification holds over every field (PG-TREE-ALL, PG-FOUR-CONDITIONAL). |
| Q2: five parties over C | Undecided | All trees included; weighted quadruple inequalities are necessary. A CAT(0) metric in a tripod times a line has no Euclidean-core-plus-pendants representation in any dimension (PG-FIVE-NONL1). K_(r,r-1)(q) does not border-restrict to K_r(q) times K_(r-1)(q), for every r>=3 and q>1 over C (PG-CAP-HYPER); the asymptotic cover gate remains open. |
| Q2: five parties over F_2 | Undecided | All tree pseudometrics included over every field; same geometric necessary inequalities and failed Euclidean-core representation route. The complex capacity obstruction is not asserted in characteristic two. |
| Q2: Euclidean square, both fields | Undecided | Equivalent to any non-tree price and to planar flatness. The regularized cycle-cover value is exactly2 or2^sqrt2; square absence is equivalent to one finite dyadic cycle cover of cost below q^sqrt2 (PG-CYCLE-GAP/FINITE). The two-cut rank exponent is exactly1 orsqrt2; neither branch is selected. Over C, PG-OP-DETERMINISTIC narrows square absence to failure of one explicitly prescribed finite rational Specht-operator linear system; every member passing is equivalent to square presence. The equivalent compressed and fixed-rectangle families have explicit slice-determinant solutions atq2,4,8,16,32,64 (PG-OP-SLICE-DETERMINANT); their first unresolved parameter isq128. No member of the original maximum-dimension family has been solved. |
| Q2: cross-polytope plus centre, both fields | Undecided | Euclidean metric is a price iff no strict shortening exists in that fixed D, iff all finite Euclidean D-configurations are prices (PG-CROSSPOLY-GATE). Full pseudometric class remains open. |
| Q3: exact supremum and matching limit | Undecided | A4/3 fixed-power ceiling now covers arbitrary common-origin radii and polynomially many hubs with a fixed labelled connected graph and the prescribed averaging-selector debit (EX-29). It also covers subpolynomially many hubs with graph and assignment chosen after the partition (EX-30). If the claimed direct-case theorem is correct, its complete-network construction attains4/3. Arbitrary segment centres and arbitrary lengths with exactly two hubs obey the4/3 fixed-power ceiling, h=O_a(B^(4/3)logB), with the prescribed binary-certificate debit (EX-42). Growing many-hub cases outside the earlier models remain open. The actual-selector gate for the complete-network construction is now only Gamma_k, the least ordinary normalized Euclidean scale of its2k cross-polytope endpoints (EX-43); Gamma_k=O(k^beta) would conditionally give alpha=1+1/[2(1+beta)]. Only1<=Gamma_k<=sqrt(k) is proved under flatness. For arbitrary endpoint geometry and polynomially many fixed labelled hubs, every equal labelled partition and common actual-selector debit ak(log2r)G have ceiling3/2, h=O(B^(3/2)logB) (EX-46); adaptive hub graphs/labels and unrestricted methods remain open. |


Movement is present under the user's exact criterion. Q1a has a strictly smaller gate than at review05: SH53 excludes every width-six two-term shortening in dimension10 over every field, including arbitrary layouts and local maps. A separate generator-free verifier reconstructed26 radial certificates and405 two-minimum rational contradictions, checked1149 integer-pruned branches, and verified complete coverage. The remaining width-six parameters are A2,D11..19 or A3,D4..16. Partial dimension11 data and numerical solver statuses are not counted.

Over C, the Euclidean-square question is reduced to a prescribed family of finite rational linear systems, with both a compressed symmetric-power formulation and a fixed rectangular local Schur formulation. Explicit slice-determinant vectors solve the compressed and rectangular systems atq2,4,8,16,32,64. The first unresolved dyadic parameter for these proved formulations isq128, subject only to any further independently checked update in the table above. The algebraic projection and exact entropy comparisons have independent checks. No instance of the original maximum-dimension Specht family is asserted solved. The regularized operator endpoint and the two-cut/SOS exponents still have two possible branches; no branch has been selected.

Q3 has an additional proved barrier for actual spectral selectors: EX46 allows arbitrary endpoint positions, positive integer widths and polynomially many fixed labelled hubs, with one common scale G and debit ak(log2r)G, and gives h=O(B^(3/2)logB). The weighted-median extension and all abstract hypotheses of the partition proof have independent checks. This yields a3/2 fixed-power ceiling when every equal labelled partition must work. Adaptive hub graphs or labels remain outside this model. The4/3 construction remains conditional on the claimed theorem being correct. Arbitrary growing many-hub methods and the unrestricted supremum remain undecided. EX44 reformulates Gamma_k using finite resource covers without improving its quantitative bound, and is not itself counted as movement.

Q1a, Q1b and Q1c remain undecided over C and F2. Neither a strict shortening nor universal absence is proved; flatness, explicit contraction and mutual exclusion remain open. Q2 on three parties was proved before review01 and is not counted again. The four-party conditional classification still depends on square membership; five-party and full crosspolytope price classes remain open. The finite cycle-cover gate still first permitsq128.

The new principal-angle necessary condition, finite signed/positive operator certificates, bounded numerical crown fits, invariant-projection lemma, source checks and packaging are recorded with their actual scope. They are not substitutes for an open-row decision and are not needed to justify this review's movement.

Decision: continue the authorized research. Consecutive scheduled reviews without movement:0. Next formal review:2026-11-25T04:59:50Z. Next checkpoint11:2026-11-25T04:14:50Z. No checkpoint ZIP is created at this review.


### Post-review06 checked moment reduction (2026-11-25T04:05:22.768566+00:00)

SH55 independently passes: all-field width-six two-termD>=17 and three-termD>=13 are excluded analytically using the joint geometric second moment and complement-even variance. The current Q1a gate is A2,D11..16 orA3,D4..12. New moment-row computation is a separate model and has not yet supplied another exclusion. EX47 independently extends the actual-selector3/2 ceiling to subpolynomially many adaptive hubs. Review07 remains scheduled04:59:50 UTC; the no-movement count remains0 from review06.


### Further checked reduction before checkpoint11 (2026-11-25T04:11:43.889942+00:00)

SH56 independently excludes two-term width-six dimensions11,12,13 by complete radial families44,48,52. SH55c independently excludes alltwo-termD>=15 analytically using the coupled deficit product bound. The only remaining two-term width-six dimension is14; three-term dimensions4..12remain. D14radialexceptions43,44,45are explicitlyunresolved. These post-review06changes willbeassessedatreview07; no extra reviewisconducted.


### Scheduled checkpoint11 preparation correction (2026-11-25T04:18:25.213984+00:00)

The scheduled checkpoint started at04:14:50.000301UTC. Before delivery, two root preparation errors were found: the final191-page PDF remained under build/ instead of its deliverable path, and20 previously completed root checks had been appended to the generated CHECK_EVENTS.tsv and were overwritten by aggregation. The PDF is now promoted and these pre-boundary check records are recovered into root_checks.tsv with their original session-recorded times; aggregate generation is rerun. The same scheduled checkpoint is repaired in place, with its original hash and reason recorded. No additional checkpoint is issued and no post-boundary mathematical finding is included. Visual QA covers34selected pages. The next review and checkpoint remain04:59:50UTC.


### Checked gate reductions after checkpoint11 (2026-11-25T04:26:08.530686+00:00)

SH55d excludes every width-six two-term shortening over every field and arbitrary layouts, by a joint edge-variance bound for the two deficit profiles together with the earlier low-dimensional certificates. SH57 excludes three terms in dimension12 by an integer quadratic majorant for the exponential rank contribution. SH58 excludes three terms in dimension4 by a complete exact propagation tree: the independent generator-free semantic verifier replays7013nodes and127524updates, checks all28roots and all branches, and finds no survivor. The remaining width-six gate is A=3,D=5..11. These are post-review06 gate changes for the scheduled review07; this entry is not an additional formal review. EX48 expands the proved binary-certificate barrier to arbitrary cut-feasible graph/GHZ seeds but does not bound actual Gamma_k.


### Width-six exclusion completed (2026-11-25T04:44:15.709317+00:00)

SH60 closes the last three-term dimensions5,6,7. A generator-free independent verifier reconstructed all39rational Farkas certificates, checked exact cancellation and right side−1, independently enumerated every foldedQ5vertex subset, recomputed ordinary-cube neighborhoods, and verified all case prunes and coverage. SH60b now proves no strict shortening at any widthm<=6 over every field, for every dimension, term count and arbitrary finite layouts. Width7 is the first unexcluded width; planar two-term width7 was already excluded. No global flat/contracting branch is selected. This strict main-gate reduction will be assessed at scheduledreview07, not an extra review.


## Formal review07: 2026-11-25T04:59:52.098380+00:00

Scheduled due time: 2026-11-25T04:59:50+00:00.

| Requested item | State | Strongest result and proof location |
|---|---|---|
| Q1a over C | Undecided | No strict shortening exists at any width m<=6, in any dimension, for any term count or arbitrary finite layouts (SH-60b, with SH-55d and SH-57--60). Width7 is the first unexcluded width; a planar shortening with exactly two terms requires width at least8 (SH-38). Strict shortening iff failure of flatness (SH-08). For fixed D, no shortening iff its Euclidean crosspolytope is a price (SH-15, PG-CROSSPOLY-GATE). |
| Q1a over F_2 | Undecided | The same universal width<=6 exclusion, planar two-term width7 exclusion, and fixed-D equivalences hold (SH-60b, SH-38). Width7 is the first unexcluded width. Existence depends only on characteristic (EX-07); no shortening was found in the checked crossing-identity searches. |
| Q1b: contracting/flat over C | Undecided | No-square gives explicit n=4,s=15/8. A seven-party cover exponent at most1/128, or balanced K_(r,r) to two r-cliques with exponent at most r^2/2048 for some r divisible by4, would give explicit n=3,s^2=3-2^-523336 (SH-33). A uniform Izeki--Nayatani invariant bound is another sufficient gate (PG-IN-GATE). |
| Q1b: contracting/flat over F_2 | Undecided | The same no-square and positive-overhead cover implications hold with explicit constants (SH-33). General CAT(0) necessity alone is insufficient (PG-BUILDING). |
| Q1b: mutual exclusion | Undecided | Hilbert maps satisfy a strict rank-step inequality already at Mat_2(F_2), factor 3/2 (PG-HILB2). A model containing all flats and trees and having CAT(0) realizations also contracts uniformly (EX-32); it is not a class of actual prices. The geometric properties alone do not decide exclusivity. |
| Q1c over C | Undecided | Reduced exactly to mutual exclusion of flatness and contraction (SH-09). Strict shortening does imply contraction. |
| Q1c over F_2 | Undecided | Same reduction, with no characteristic change. |
| Q2: three parties over C | Proved | Every pseudometric, by nonnegative star-arm decomposition (PG-THREE). |
| Q2: three parties over F_2 | Proved | Same proof over every field (PG-THREE). |
| Q2: four parties over C | Undecided | Reduced to square membership: absent gives exactly tree pseudometrics; present gives exactly CAT(0)-embeddable four-point pseudometrics (PG-FOUR-CONDITIONAL). |
| Q2: four parties over F_2 | Undecided | The same exact conditional four-point classification holds over every field (PG-TREE-ALL, PG-FOUR-CONDITIONAL). |
| Q2: five parties over C | Undecided | All trees included; weighted quadruple inequalities are necessary. A CAT(0) metric in a tripod times a line has no Euclidean-core-plus-pendants representation in any dimension (PG-FIVE-NONL1). K_(r,r-1)(q) does not border-restrict to K_r(q) times K_(r-1)(q), for every r>=3 and q>1 over C (PG-CAP-HYPER); the asymptotic cover gate remains open. |
| Q2: five parties over F_2 | Undecided | All tree pseudometrics included over every field; same geometric necessary inequalities and failed Euclidean-core representation route. The complex capacity obstruction is not asserted in characteristic two. |
| Q2: Euclidean square, both fields | Undecided | Equivalent to any non-tree price and to planar flatness. The regularized cycle-cover value is exactly2 or2^sqrt2; square absence is equivalent to one finite dyadic cycle cover of cost below q^sqrt2 (PG-CYCLE-GAP/FINITE). The two-cut rank exponent is exactly1 orsqrt2; neither branch is selected. Over C, PG-OP-DETERMINISTIC narrows square absence to failure of one explicitly prescribed finite rational Specht-operator linear system; every member passing is equivalent to square presence. The equivalent compressed and fixed-rectangle families have explicit slice-determinant solutions atq2,4,8,16,32,64 (PG-OP-SLICE-DETERMINANT); their first unresolved parameter isq128. No member of the original maximum-dimension family has been solved. |
| Q2: cross-polytope plus centre, both fields | Undecided | Euclidean metric is a price iff no strict shortening exists in that fixed D, iff all finite Euclidean D-configurations are prices (PG-CROSSPOLY-GATE). Full pseudometric class remains open. |
| Q3: exact supremum and matching limit | Undecided | A4/3 fixed-power ceiling now covers arbitrary common-origin radii and polynomially many hubs with a fixed labelled connected graph and the prescribed averaging-selector debit (EX-29). It also covers subpolynomially many hubs with graph and assignment chosen after the partition (EX-30). If the claimed direct-case theorem is correct, its complete-network construction attains4/3. Arbitrary segment centres and arbitrary lengths with exactly two hubs obey the4/3 fixed-power ceiling, h=O_a(B^(4/3)logB), with the prescribed binary-certificate debit (EX-42). Growing many-hub cases outside the earlier models remain open. The actual-selector gate for the complete-network construction is now only Gamma_k, the least ordinary normalized Euclidean scale of its2k cross-polytope endpoints (EX-43); Gamma_k=O(k^beta) would conditionally give alpha=1+1/[2(1+beta)]. Only1<=Gamma_k<=sqrt(k) is proved under flatness. For arbitrary endpoint geometry and polynomially many fixed labelled hubs, every equal labelled partition and common actual-selector debit ak(log2r)G have ceiling3/2, h=O(B^(3/2)logB) (EX-46); For subpolynomially many adaptive hubs, the same3/2 ceiling holds with arbitrary endpoint geometry (EX-47). Polynomially growing adaptive hubs and unrestricted methods remain open. |


Movement is present under the user's exact criterion. The Q1a gate has strictly decreased since review06: SH60b now excludes every strict shortening of widthm<=6 over every field, in every dimension, with any term count and arbitrary finite layouts. The first unexcluded width is7; its planar two-term case was already excluded. The new proof combines the joint-edge two-term theoremSH55d, the complete dimension-four tree with independent replay of7013nodes and127524updates, Harper neighborhood comparisons, and39independently verified exact tail-count certificates that close the final three-term dimensions5,6,7. No numerical optimizer status is counted as proof.

Neither flatness nor contraction nor their mutual exclusion is decided over either requested field. The Euclidean square still has two possible branches. The six explicit determinant instances and the new uniform multi-cut upper bound do not choose a branch. The latter rules out a particular characteristic-two identity-matrix PT-rank candidate in the cited growing-dimension regime, but does not yield a strict shortening or a new price.

The unrestricted Q3 supremum remains undecided. EX47 adds a3/2 ceiling for subpolynomially many adaptive hubs under the stated actual-selector debit. EX48 shows that arbitrary cut-feasible graph/GHZ seed certificates reduce to binary pointwise averages within a constant factor, extending the scope of the binary-certificate barrier; it does not lower-bound the actual spectral normalization Gamma_k. Those distinctions remain explicit. Every circuit consequence continues to carry the hypothesis that the claimed theorem is correct.

Only the strict Q1a gate reduction is needed to justify movement. Source checks, fresh equivalent formulations, failed numerical probes, and packaging are not counted. Decision: continue the authorized research. Consecutive scheduled reviews without movement:0. Next formal review:2026-11-25T05:59:50Z. Checkpoint12 is due at this same04:59:50 boundary; next checkpoint13 is due05:44:50UTC.
