# BR_PENCIL dated research ledger

Run: BR_PENCIL-20261121-R1. Model: GPT-6 Astra Pro.
Reasoning-effort setting: inherited; no separate numeric setting exposed.
Start: 2026-11-21 02:59 UTC / 03:59 Europe/Berlin.

## Operating rules

The attached prompt controls scope and stopping. Main question receives priority.
Checkpoints are due every 45 minutes after start, first at 03:44 UTC, and
are immutable full ZIPs without earlier checkpoints inside. Progress reviews
are due after about three hours (05:59 UTC), then hourly. Two consecutive
reviews without a changed question status or a strictly smaller gate stop
that work. No checkpoint is created outside the scheduled cadence.

## Initial state, 2026-11-21 03:09 UTC

| Question | State / strongest current gate |
|---|---|
| Multi-dimensional substitution | General image argument being re-proved with a proper Grassmannian incidence. |
| Four-family pencil minimum, n=4,b=2,j=2 | Promising reduction to coordinate pairs by a torus degeneration; support lower bound 6 for polynomial families, 3 for row families; matching star degenerations under independent check. |
| Larger residual dimension | Root enumerating coordinate configurations and Koszul ranks, starting j=3,4. |
| DPS residual image outside four families | Explicit C^2⊗C^3 subspace with conjectured alpha=3/4 and exact PPT dual witness under proof check. |
| Arbitrary algebraically closed fields | Integral orbit-sum/divided-power tensor model isolated; characteristic-zero normalized tensors must not be reduced modulo n!. |
| GL-orbit alpha | Candidate refutation: supremum always 1 for the full product GL action, maximum iff a product vector is present. |
| Literature and Grothendieck dictionary | Primary-source verification ongoing; no priority claim. |

The attachment was unpacked once into source/. All source files are unchanged.
The exact prompt and source archive identify the predecessor and intakes.


## Research state, 2026-11-21 03:38 UTC

The requested n=4,b=2,j=2 computation is proved: the row minima are 3
and polynomial minima are 6, giving bounds 7 and 40. Continuing the
polynomial calculation proves exact minima 8,9,11,12 for j=3,4,5,6,
respectively, and therefore **both polynomial border ranks are at least42**.
All these statements hold over every algebraically closed field for the
integral coefficient-tensor model. Complete proofs have been read and the
standalone exact certificate suite passes.

| Question | State / strongest current gate |
|---|---|
| General multidimensional substitution | R-01 proved by closed flag incidence and proper projection; known three-factor principle attributed to Landsberg–Michałek Prop2.3. |
| General four-family Grassmannian minimum | P-01 proves exact finite coordinate reduction. P-02 reduces every j=2 seed to an adjacent pair. Numerical values outside evaluated ranges remain open. |
| n=4,b=2,j=2 | P-03–P-05 proved: row3, polynomial6, all fields. |
| Polynomial b=2,j=3,4,5,6 | R-02–R-07 proved:8,9,11,12 for every n>=4. The exceptional permanent5-plane is settled by unit-minor unique-extension obstruction R-04. |
| A bound above39 | PROVED:42 for both integral polynomial tensors; usual CP and symmetric border ranks over C also satisfy it. |
| Seven-dimensional improvement to43 | Checked interval13<=mu7<=14. A-factor Koszul search covers7,972 permutation orbits. Support-factor Koszul further removes3 permanent orbits /2 determinant Borel ideals. Four other determinant Borel ideals have new finite prolongation certificates under final independent review. Several rank13 cases remain; no43claim. |
| Larger residual order | Row permanent adjacent cubic seed has a six-point all-field upper curve and unit-minor lower6, under final integration. Row determinant cubic seed has lower7 away fromchar2; exact value remains under study. |
| DPS outside four families | S-01 proved:alpha3/4, rational PPT primal/dual certificate, zero error at all higher levels. S-02 generic error proved. Generic efficient Q-30 remains a separate open problem. |
| All algebraically closed fields | FL-01–FL-05 proved. Ordinary polynomial powers in characteristic p<=n have a different, infinite-rank answer; no normalization by n! used. |
| GL-orbit alpha | Proposed maximum refuted; O-01 supremum1 with precise attainment criterion. O-02 gives actual Plucker norm/minimal-vector condition. |
| Literature and dictionary | Primary audit completed for listed sources, with exact locators and scan provenance. No exhaustive historical-priority claim; no unpublished-manuscript cote established. |

### Approaches already tried and their outcome

- Ordinary support and first-factor Koszul maps solve the two-plane case and
  most j=3,4,5 cases. All finite coverage is exhaustively checked, not sampled.
- The exceptional permanent5-plane has direct Koszul lower bound10. Alternate
  factor wedges and restricted first-factor Koszul maps did not raise it.
  The degree210/120 limiting-span obstruction instead gives11, with a unique
  possible10-plane that fails the other prolongation test.
- A direct permanent6-plane prolongation investigation was superseded by the
  proved monotonicity mu_j-j>=mu_i-i; its exact minimum is12.
- Borel compression applies to determinant residuals, not generally to the
  characteristic-zero permanent. The 25determinant seven-ideals include cases
  with Koszul bounds12 and13. Eliminating the former alone is insufficient
  for a uniform14; this distinction was checked and a premature progress
  inference was explicitly corrected before any theorem was entered.
- Support-factor Koszul maps were evaluated in exact torus weight blocks.
  They improve three permanent and two determinant seven-cases, but the other
  candidates still need a different argument.
- For the two support9 permanent seven-planes, secondary substitution on all
  coordinate retained dimensions2–8 did not establish14. Full-weight-space
  prolongation saturation reduces the possible extension supports but leaves
  thousands of cases. These are failed sufficiency tests, not impossibility
  theorems about the methods.
- A rank13 upper degeneration for a permanent seven-plane has not been found.
  Boolean finite differences give the proved upper14. Degree111 compatibility
  and more precise extension-line tests remain possible next approaches.

No three-hour progress review has yet fallen due. Packaging is not counted
as mathematical movement. The two consecutive no-movement review rule has
not been triggered.


### Update, 2026-11-21 03:43 UTC

P-09 and P-12 have passed whole-proof reads and independent exact
verifiers. They exclude eight named determinant seven-planes in
characteristic zero. The determinant global43 gate still includes
two eleven-variable types and one nine-variable type (with transposes).
P-10/P-11 are now proved and checked: the row permanent adjacent
cubic pencil has exact border rank6 in every characteristic, and
rowP4 has exact border rank8 in every characteristic. RowD4 likewise
has border rank8 in characteristic2. In other characteristics the
adjacent determinant cubic pencil remains between7 and9. An exhaustive
projection search on the cited12-term D4 formula drops at most3terms;
that particular upper-bound route therefore stops at9.


### Update, 2026-11-21 03:43:40 UTC

The last determinant support-9 seven-plane has a successful exhaustive
prolongation computation: 42,274 multiplicity arrangement states and
32 two-line state pairs leave no candidate. This is still awaiting its
complete independent certificate and whole-proof audit. The proposed
uniform bound43 is therefore a verification gate, not an asserted theorem.
The new determinant eleven-variable cases are also being packaged as P-14.


## Research state, 2026-11-21 04:10 UTC

This is a mathematical update, not the scheduled three-hour review.
Both polynomial size-four tensors now have checked characteristic-zero
CP and symmetric border-rank lower bound **43**. R-08 and R-10 prove the
exact seventh minimum14; R-09/R-10 propagate the exact eighth and ninth
minima15 and16. All constituent prolongation proofs have received complete
reads and exact independent certificate checks. The all-field bound42 is
retained separately; no unsupported positive-characteristic upgrade is made.

The determinant cover contains25 Borel ideals and2997 modular minor
certificates. The permanent cover independently checks all8347680
seven-subsets;1543608 low-support subsets form1517 disjoint orbits with
6041 modular minors and11 explicitly named prolongation dependencies.
The last permanent orbit is excluded by a closed degree22 prolongation
condition with eight candidate spaces and24 final unit minors (P-19).

P-11 is now exact: the row determinant cubic adjacent pencil has border
rank8 outside characteristic2, and6 in characteristic2. The permanent
value is6 in every characteristic. An integral eight-term upper curve
and a proper three-Grassmannian incidence with eight rank58 product
certificates establish the determinant value. The earlier interval7..9
is superseded, not retained as the current gate.

P-18 gives polynomial cubic intervals: permanent21..24 in all fields;
determinant21..30 outside characteristic3, with21..24 also in
characteristic2. It proves explicit30/24-term integral upper curves and
905 exact weight-block minors for each lower bound. Exact values remain
open. The permanent upper bound caps this particular substitution at38.

### Current main gates

- Size-four bound44 through j10: propagation gives mu10>=17. Determinant
  reduces to59 Borel ideals, six already certified at18 by Koszul maps.
  Borel-stable extension enumeration has found further exclusions, but
  the complete P-17 proof/certificate is still being assembled. Unresolved
  projective weight kernels are retained explicitly. No global44 claim.
- Uniform n>=4 seventh minimum: all supports at least14 are immediate.
  A support outside4x4 with at most13 entries has at most6 rows and6 columns.
  Exact bipartite-graph enumeration found34 support graph types before
  seven-subset and Koszul testing. A trivial-action kernel in the induced
  automorphism action was detected by an assertion and corrected by
  deduplicating the action; no failed run is treated as a certificate.
- Larger residual order: row cubic seeds are finished; polynomial cubic
  exact values and general b numerical formulas remain undecided.
- The requested DPS, all-field F-23, and orbit-maximum questions are
  finished in the precise scopes of S-01/S-02, FL-01--FL-05 and O-01/O-02.
- The literature and Grothendieck dictionary remain scoped primary-source
  audits, with no exhaustive priority claim and no invented manuscript cote.

Checkpoint01 was saved at03:44:34UTC with its SHA256 and persistence
receipt in work/checkpoint_receipts.json. Its immutable original remains
untouched. Checkpoint02 is due04:29:26UTC. The first progress review remains
scheduled for05:59:26UTC; no no-movement review has yet occurred.


## Research state, 2026-11-21 04:24 UTC

R-11 is proved and independently checked: both polynomial seventh,
eighth and ninth minima are14,15,16 for every n>=4 in characteristic
zero. Outside4x4, the exhaustive cover has34 support graphs,1027
seven-subset orbits and18501 support-exact subsets;4996 nonzero modular
minors certify the additional cases. This closes Q-18 and strengthens
the uniform consequence to binom(n,2)^2+7 in characteristic zero.

P-20 proves the entire row permanent quadratic range mu_j=j+1 for
1<=j<=binom(n,2), over every algebraically closed field. Its graph
finite-difference construction gives an explicit polynomial permanent
ten-plane upper18. Thus the permanent ten-plane gate is now17 versus18.

P-18's determinant cubic upper is sharpened from30 to27 in every
characteristic. A63x63 Jacobian minor equals-16, proving dominance of
the nine-labelled-square parameterization in odd characteristic;
three-term simultaneous tangent curves transfer it to27. Characteristic2
uses the permanent24 upper. The cubic two-plane route is therefore
capped at41 determinant and38 permanent and cannot improve43. This
closes the improvement-route question Q-19 even though the exact
cubic pencil numerical values remain Q-16.

P-17 excludes18 additional determinant ten-plane Borel ideals. Its
self-contained checker passes22120 exact rational weight-kernel checks
and685 modular rank exclusions. The complete proof and checker were
read by root, pencil and fields. An independent audit corrected the
preliminary19 count to18: two of the ten representatives are
self-transpose. All rank calculations were unchanged. Together with
six earlier Koszul cases, the checked uniform44 gate is now35 Borel
ideals. Smaller extension-space reductions are being pursued; no
unresolved projective family is sampled away.

The non-coordinate A9 compression probe on all28 unresolved transpose
representatives gave no18 certificate (largest ranks1178 and1177,
needed1191 at pure cost70). This is a finite unsuccessful probe, not a
maximum-rank theorem. The next determinant approach is substitution
in a used-variable factor and exact treatment of the remaining
Borel parameter families. The permanent approach tests hereditary
seven-subset bounds and potential17-term constructions beyond the
existing18-term finite-difference curve.

The full packaged certificate suite is running after integration.
The PDF has been rebuilt and wide certificate tables corrected;
final current-layout checking remains in progress. No three-hour
review is due yet, and packaging is not counted as mathematical movement.


### Verification update, 2026-11-21 04:27 UTC

All22 integrated packaged checker jobs passed, including a separate
final-location P-17 replay. The current67-page PDF compiles without
overfull boxes or undefined references; all67 rendered pages were
visually inspected in four contact sheets.

P-21 independently closes one early support13 projective-line branch.
Pencil read the entire actual proof and standalone checker and replayed
all31 minors; fields also checked it, and root read the complete proof.
The main paper integration follows the scheduled checkpoint; all source,
certificate and check events are already included under work/. This
does not by itself close any of the35 remaining ten-plane ideals.
