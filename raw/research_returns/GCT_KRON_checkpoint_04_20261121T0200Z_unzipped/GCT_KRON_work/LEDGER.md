# GCT_KRON dated research ledger

Run: GCT_KRON_20261120. Started 2026-11-20 23:00:17 UTC (2026-11-21 00:00:17 Europe/Berlin). Model: GPT-6 Astra Pro; reasoning-effort setting is not exposed.

## Governing rules

Deliver new findings only with full proofs and honest check events. Known results are cited at exact locators. Source transcriptions are distinguished from original scans. Checkpoints are due every 45 minutes, each a new complete ZIP excluding previous ZIPs. First progress review after three hours; subsequent reviews hourly. Two consecutive reviews without main-gate movement require stopping.

## Initial main gates

| Question | State | Strongest proved reduction / remaining gate | Owner |
|---|---|---|---|
| Q1. Audit supplied archive statements | In progress | Subset-power and opposite-symmetric-power definitions must be distinguished; all statements need inventory and correction | archive_audit |
| Q2. Positive formulas/nonvanishing in target families | In progress | Linearization reduces to representation operations; need exact positive family formulas and their GCT ranges | positive_formulas + root |
| Q3. Saturation and K-theoretic positivity | In progress | Ordinary saturation, corrected GCT VI saturation index, and support of actual plethysm candidates must be separated | saturation_obstructions |
| Q4. Multiplicity obstructions | In progress | Need exact comparison theorem between permanent-side multiplicities and determinant coordinate ring; positivity alone gives no comparison | saturation_obstructions + root |
| Q5. Grothendieck dictionary and exact locators | In progress | Verify K0/Schur/finite-group-scheme/invariant-scheme translations and locate precise primary references | all |

## Reviews

The first timed review is recorded below and in TIMED_REVIEW_01.md.

## Substantive gate changes, 2026-11-20T23:29:31.693119+00:00

These are working updates, not the three-hour timed review.

- Q1: the scan019 subset identity is refuted by the free C2-set; canonical opposite-symmetric operations are virtual and non-special (V4 witness). The literal split quadratic WG question also has a modular-representation counterexample; audit inventory is being completed.
- Q2: exact positive series/criteria established for three two-row outputs and three hooks, plus rectangle/two-row and rectangle/hook families. A binary-table incidence-kernel formula is proved. Independent exact character checks pass.
- Q3: all ordinary-saturation holes classified in the 2x2x4 family using GCT IV Proposition18.6; factor2 suffices there. Long-row rectangular holes occur at every height. In the stable-tail range, every stretch t>=2 is positive. Ordinary saturation remains distinct from GCT VI's revised saturation index.
- Q4 first reduction: no actual multiplicity obstruction has <=3 rows (binary forms elementary; ternary forms via Beauville). Nontrivial hooks have zero ambient multiplicity.
- Q4 strict further reduction M006-M008: all r-variable projections of the padded permanent lie in the determinant closure when n>=S(m,r), where p=floor((r-1)/2), q=ceil((r-1)/2), and S=binom(m+p,p)+binom(m+q,q)-1. The universal determinant is proved by cycle covers of two trees. Projection containment compares all multiplicities with <=r rows. Thus the actual gate is at least10rows when n>3m^4, and at least52rows when n>=m^25; the same lower bounds apply to degree d. Independent full proof checks are being recorded.
- Q4 method boundary: for n=m^c, the universal containment approach cannot handle every fixed r>=2c+2 asymptotically, by the dimension of padded forms versus the determinant-pencil image. This limits the current approach, not permanent-specific improvements.

## Current main-question gates

| Main question | Checked conclusion / remaining gate |
|---|---|
| Q1 archive statements | Exhaustive76-row inventory completed; all supplied mathematical assertions treated under stated interpretations; original scan images and the named but undefined operators remain availability limits. |
| Q2 family formulas | Requested small-shape families have positive formulas. No general cancellation-free rectangular formula is proved beyond the stated families and cited Ikenmeyer-Panova ranges. |
| Q3 saturation | Generic saturation inference refuted; exact restricted classifications and stable-tail all-t>=2 theorem proved. Full rectangular support classification outside these ranges remains open in this run. |
| Q4 actual multiplicity | For n>=m^25 remaining actual candidates require m>=190, at least52rows, n<P_d(dm) and n<P_d(lambda2), the staircase lambda_(2j)>=28-j for1<=j<=26, lambda3>=557 OR lambda52>=3, lambda3>=27 OR lambda2>=478126780, q>=2, padding constraints, and failure of F018 and the jet criteria M013/M016/M017. At lambda2=27, M017 forces at least478126755 rows with rows2 through that index equal27. Still must compare q with actual closure K. The known d>n/m bound is reserved for the stronger q>g test. |

## Substantive gate changes, 2026-11-20T23:44:51.478632+00:00

These are working updates, not a timed progress review.

- Q1: exhaustive76-row inventory completed. A001–A016 fully written and independently read by root, with hypotheses and missing-source gates preserved. Both canonical and subset Burnside structures fail specialness; exact Zp lattice induction ring proved polynomial, arbitrary local-ring claim refuted.
- Q4: M009 replaces the uniform row gate by the finer necessary condition n<T_m(lambda), using highest-weight weight boxes and bounded tries. Two agents independently read the full proof, including S<m boundary.
- Q4: known Grenet upper bound excludes all rows when n>=2^m−1; therefore m>=19 in IP range and m>=190 in BIP range are necessary for any remaining actual obstruction.
- Q4: F010 identifies the exact remaining data as evaluation-tensor ranks. Ambient lambda structure and positive occurrence do not determine those ranks.
- Convention correction: both supplied IP/BIP papers use INTERNAL X11 padding. All stated source thresholds and lengthm² bounds are attached to that convention. Explicit determinant constructions also permit external padding, with source theorems kept distinct.
- Q4 next checked derivation in progress: internal padded-permanent Hessian determinant is nonzero at all-ones for n>=m+2, giving an explicit positive-q thin-tail family; Cauchy yields ambient multiplicityone and determinant Hessian yields Kone. Full written integration pending.

## Checkpoint01, 2026-11-20T23:45:34.416221+00:00

First45-minute checkpoint due23:45:17UTC. Includes all current deliverables, proof fragments, computation certificates, inventories, source/check notes, and the supplied extracted source corpus. This is not the three-hour progress review. The first XeLaTeX compile could not start because its format is absent; compilation repair remains pending.

## Substantive gate changes, 2026-11-21T00:06:45.512970+00:00

These are working updates, not a timed progress review.

- Q4 M-010: verified the complete primary proof of the 2026 quadratic Foulkes–Howe stabilization theorem; diagonal Chow containment gives K=a for d(d-1)<=n. No historical priority or formal verification claim.
- Q4 F-014/O-012: flag-minor divisibility stabilizes every highest-weight copy at inner degree lambda2. The degree-split determinant and invertible padding pullback give K=a when n>=B(lambda2,rows). Uniform consequences: lambda2>=6 in IP range and lambda2>=26 in BIP range are necessary, including d much larger than rows.
- Q4 A-020: a type-sensitive differential proof gives K=a when n>=lambda2+binom(d,2). Root and an independent worker read the complete proof and passed it. Adaptive refinement in progress.
- Q4 O-011/F-011–F-013: Hessian family has explicit q=K=a=1 in the stated rank range; near-rectangle zero and scalar families and an ambient multiplicity-four family are proved. O-012 determines all four determinant-side copies when its bound holds.
- Q1/Q3 A-017–A-019: exact K0 product issue resolved, all fixed-height Kronecker families have explicit raising-kernel models, and the precise normal multiplicity-free support hypothesis gives only relative lattice saturation. All three complete proofs were read.
- Rendering: local XeLaTeX format repaired; working PDF now compiles. Visual layout review is underway and is not mathematical gate movement.

## Substantive gate changes, 2026-11-21T00:23:16.048191+00:00

These are working updates, not a timed review.

- Q4 A021: adaptive differential orders prove K=a for n>=B_d(lambda2)=lambda2+sum(j=2..d-1)min(j,lambda2). In particular every actual obstruction must have (d-1)lambda2>n. With the padding constraint, every actual obstruction must also have md+binom(d,2)-1>n. Root and obstructions worker read the complete proof.
- Q4 F015/F016: restricting the stabilized coefficient family first to coordinate caps, then to the much smaller nested tail-sum region, preserves every ambient copy. Full K=a follows from either restricted graph count. All full proofs independently read.
- Q4 M011: direct use of nested support on degree-m projections works even when lambda2>n. The exact row-cut size proves q<=K; in particular remaining IP candidates need lambda6>=3, and remaining BIP candidates need lambda27>=13. More generally n>=m^c,c>=6 requires lambda_(c+2)>=floor(c/2)+1. Two independent complete proof reviews PASS.
- Q4 M012: an explicit binary permanent with its (1,1) entry equal to the padding form contains every padded binary degree-m form. All-copy stabilization gives exact q=K=a=4 at two-row tail6, and multiplication in the integral permanent coordinate ring gives q>=4 for higher-row tail(b,2,...,2). This strengthens the test examples beyond a positive ambient coefficient. Two independent complete proof reviews PASS.
- Rendering:82-page working PDF compiled and all pages reviewed in contact sheets; selected proof and inventory pages checked at full size. This verification is not counted as mathematical gate movement.

## Substantive gate change, 2026-11-21T00:25:25.008932+00:00

Working update, not a timed review: A022 sharpens the degree gate to n<N_d(dm), with N defined by an explicit checked recurrence and a two-candidate exact maximum. It also sharpens the shape-specific gate to n<N_d(lambda2). The complete proof has been independently read by root. The weaker md+binom(d,2)-1>n remains a readable consequence, not the strongest recorded gate.

## Substantive gate change, 2026-11-21T00:30:13.986000+00:00

Working update, not a timed review: F017 mixed early-variable/later-degree trees prove a full staircase of actual-multiplicity exclusions. In BIP range require lambda_(54-2s)>=s+1 for1<=s<=25 (lambda4>=26 through lambda52>=2); in IP range require lambda_(12-2s)>=s+1 for1<=s<=5. Root read the complete written proof and checked cycle signs, two-copy suffix paths, all-copy ideal inclusion and exact constants.

## Checkpoint02, 2026-11-21T00:30:23.444902+00:00

Scheduled45-minute checkpoint, due2026-11-21T00:30:17+00:00. This is not a timed progress review. Includes the current complete work, source corpus, proof fragments, checks, computations, ledgers and working paper. Earlier checkpoint ZIPs are excluded.

## Substantive gate changes, 2026-11-21T00:57:54.964720+00:00

Working update, not a timed review.

- A023 groups whole derivative powers on their actual source. The new necessary degree gate is n<P_d(dm), with P_d(dm)<=min((d-1)^2,floor(d(d+m-1)/2)); shape by shape require n<P_d(lambda2). Complete root and peer proof checks passed.
- M013 proves dominance of determinant coefficient jets through even order b using an acyclic bridge graph with a unit Jacobian minor. Every ambient copy survives in the stated size range. At n>=m^c,c>=6, require lambda2>=c+2; BIP now has the full staircase lambda_(2j)>=28-j for1<=j<=26. All three independent complete proof reads passed; the integral pullback refinement is separately scoped.
- F018 packages arbitrary nested support into a finite two-order-ideal cover. It gives actual q<=K at base degree m, full K=a at base degree lambda2, and full q=K=a if the distinguished-entry permanent construction fits size m.
- O018 adds the joint BIP gate lambda3>=139 OR lambda52>=3. Its explicit four-copy example passes all single-row staircase conditions and has lambda2>n; full nested support still proves4<=q<=K, while every single-cut universal family is too large by dimension.
- O016/O017/O019 prove distinct method boundaries for exact universal padded forms, border-valid single-cut containment, and full jet dominance. None is promoted to an actual multiplicity obstruction.
- F019/A024 identify a complete known rectangle-square rule and its explicit normal polynomial HW algebra. A monomial positive basis coexists with ordinary saturation holes because its weight lattice has index4 in the even-size ambient lattice. This resolves a concrete positivity/saturation bridge, without claiming a general rectangular rule.

## Substantive gate change, 2026-11-21T00:59:32.497739+00:00

Working update, not a timed review: A025 replaces O018's139 constant by420 using an asymmetric two-tree support cover. Remaining BIP candidates require lambda3>=420 OR lambda52>=3. The exact 49/50 margin at m190 and monotonic extension were fully read by root. Total-degree pruning is being tested as a further improvement; it is not yet counted as proved. F020 also completes the positive two-hook/one-two-row family with checked k0/1 overlap cases.

## Checked developments, 2026-11-21T01:13:49.004722+00:00

Working update, not a timed review.

- A025's explicit corollary is now lambda3>=557 OR lambda52>=3. The171-case exact certificate and monotone infinite tail are checked. These constant evaluations are corollaries of the already strongest F018 κ criterion; they are not separately counted as fresh main-gate movement once that criterion is the baseline.
- A026 resolves the equal height-three rectangle family by the known SL3³ invariant ring: g(h³,h³,h³) counts2a+3b+4c=h, with a checked closed form. It supplies an actual normal polynomial Kronecker algebra with primitive scalar support lattice and a hole at1. Its multiplicity2 at h4 identifies the failure of the multiplicity-free extension.
- O020 strengthens full ambient determinant equality for lambda3<=2 to n>=r−1, arbitrary second row and outer degree. The quadratic incidence isomorphism and all added vertices were fully checked. This is stronger multiplicity information in shapes already excluded as BIP actual obstructions.
- F021 proves full internally padded permanent multiplicity by dominant coefficient jets and exhibits actual multiplicity>=2 beyond every exact two-tree support cover. No general q-versus-K conclusion outside its hypotheses is claimed.
- M014 proves the complete staircase at every integral c>=6. M015 uses a cyclic shared-star pencil to get order-five jet dominance at n>=r², hence lambda2>=6 already at n>=m4. Both complete proofs passed independent readers; exact direct minors verify M015's small full pencils.

## Checkpoint 03, 2026-11-21T01:17:36.942981+00:00

Scheduled 45-minute checkpoint, due 2026-11-21T01:15:17+00:00. This is not a timed progress review. Includes the current complete work, source corpus, proof fragments, checks, computations, ledgers and working paper. Earlier checkpoint ZIPs are excluded.

## Checked developments, 2026-11-21T01:32:13.972776+00:00

Working update, not a timed review: A027 transports the positive height-three formula and a separate unit family through fully proved rectangular complement duality, giving growing-height families. Multiplicative compatibility is not claimed. O021 determines actual q=K=a4 at m9,n10,d6,lambda(44,8,2,2,2,2), beyond every exact support-cover threshold. F022 gives every odd jet order from shared cores, in particular lambda2>=4 at n>=m2 andlambda2>=6 at n>=m4. Root read all proofs and O020's precise integral incidence cokernel. M016 coupled-core even jets is written and under independent review; it is not yet counted as a checked main-gate reduction.

Checkpoint03 timing: scheduled01:15:17UTC, actual archive01:17:36.942981UTC; the working PDF delimiter error was repaired before that snapshot. The durable save succeeded. No additional checkpoint was created.

## Substantive gate changes, 2026-11-21T01:48:26.014925+00:00

These are working updates, not a timed review.

- Q4 M016, checked by root with independent reviews pending: shared core components coupled through a matrix of root bridges give an integral right inverse for even-jet differentials. Together with F022 and the Hessian case, n>=m^c for every integer c>=1 forces lambda2>=c+2.
- Q4 M017, checked by root with independent reviews pending: attaching prefix trees to every inward jet vertex gives a coupled all-copy equality. In BIP range, lambda2<=26+t requires lambda_k>=27 whenever 1+binom(k-2+t,t)<=478126755. In particular lambda3>=27 or lambda2>=478126780; at lambda2=27, at least478126755 rows are necessary. This adds a restriction to the previous jet/support gates; the strict actual-positive example is being independently written and checked.
- Q2 A027: castling transports the complete height-three count to explicit rectangular families with all heights unbounded, and a separate growing-height family has multiplicity exactly one. The equality is an invariant-space duality, not a claim that multiplication or all GCT rectangle squares are preserved.
- Q4 O021: positive permanent transverse jets give full q=K=a for lambda3<=2 in the stated permanent-size range, including an exact four-copy shape outside every earlier exact support-cover criterion.

## Substantive gate changes, 2026-11-21T01:56:40.452120+00:00

- Q4 M018 extends jets by arbitrary finite monomial order ideals and gives a finite all-copy criterion beyond M017 prefix simplices. Its BIP corollary is lambda2>=1000001 OR lambda3>=29 OR lambda4>=27. O023 has q>=4 but no M017 parameter choice, no exact F018 cover, and no entire one-cut family reaches it; M018 gives K=a. This witnesses a strict new gate, not only a new evaluation of the previous criterion.
- Q4 A028 computes an unbounded orbit/closure gap: even h>=4 gives closureK=ambient1 while symmetric and ordinary Kronecker multiplicities both equal # {2a+3b+4c=h}. It supplies no permanent obstruction because q<=a=K. Full root and archive proof readings passed.
- Q4 F023 improves the even-order full-permanent jet bound, with exact full-matrix determinant/permanent Jacobian ranks35 and70 in the two small cases checked. The strict support-cover example now works at permanent size32768.

## Timed review 01, 2026-11-21T02:00:17.030081+00:00

Movement: yes; consecutive reviews without movement: zero. The initial open questions have changed status and the actual multiplicity gate has strictly shrunk. The complete current main gates and every open question row are snapshotted in TIMED_REVIEW_01.md and TIMED_REVIEWS.json. Packaging and successive evaluations of an existing criterion are not counted. Continue; the next review is due 2026-11-21T03:00:17Z.

## Checkpoint 04, 2026-11-21T02:00:24.494769+00:00

Scheduled 45-minute checkpoint, due 2026-11-21T02:00:17+00:00. This is not a timed progress review. Includes the current complete work, source corpus, proof fragments, checks, computations, ledgers and working paper. Earlier checkpoint ZIPs are excluded.
