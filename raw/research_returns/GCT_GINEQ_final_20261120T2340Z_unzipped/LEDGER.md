# GCT_GINEQ — dated research ledger

Run: GCT_GINEQ-2026-11-20-R1. Start: 2026-11-20 23:00 UTC, which is 2026-11-21 00:00 Europe/Berlin. The user's 20 November run label is retained. Root and the three delegated agents used GPT-6 Astra Pro. The effort setting was not exposed; no effort label is inferred.

This ledger records actual movement in the mathematical questions. Packaging and additional prose are not counted as mathematical progress. Agent working IDs are mapped to the final F-IDs in ID_MAP.tsv.

## Current main gates

| Main question | Strongest proved answer or reduction | State |
|---|---|---|
| Norms against rank and border rank | Direct full-tensor ratios fail even up to every fixed constant; support-exponent conversions work but are dominated by mode ranks. For any specified linear flattening, nuclear/operator certificates recover exactly its rank bound under invertible output preconditioning. Uniform norms on the whole image give the stronger F-13/F-14 bounds. | Decided at the stated scope |
| Stronger determinant/permanent image bounds | The exact minimum CP border rank on a residual image equals the same-family smaller tensor's CP border rank. Thus the gate is reduced to a smaller instance, with the precise recurrence in F-23. | Proved exact reduction |
| Grothendieck SDP certificates | Primal/dual inequalities have explicit correct directions. The direct unscaled Hilbert route is trivial; natural target matrices have gap one. A dimension-sensitive K_G(s) gap plus a separate sign-norm upper bound gives a valid rank test. | Decided at the stated scope |
| Constant and Unique Games | The cited threshold is K_G for the real sign problem, with UGC hardness and arbitrarily close algorithms. The deductions here neither determine the constant nor alter that threshold. Recent numerical endpoints are source-checked background. | Answered with explicit provenance |
| Grothendieck frameworks | Integral secant and orbit-image models, Koszul bundles, Hilbert/Grassmann incidence, coordinate restrictions, lambda/K_0/gamma and étale limitations are proved or supplied by exact dictionaries. | Proved at the stated scope |
| Archival source | Published-work catalogue CSG17 and exact original scan leaves are verified; EGA/SGA/FGA anchors are supplied. A separate unpublished manuscript cote has not been established. | Bibliographic field explicitly unverified |

## Progress and corrections

Times below are UTC; add one hour for Europe/Berlin. Minute ranges describe working phases, not invented precise event timestamps. Exact check timestamps are in CHECK_EVENTS.tsv.

### 23:00–23:06 — stress tests and the first valid conversion

The supplied archive was extracted once. Its four LaTeX works were read and divided among the root and three agents. The first route tested the matrix inequalities involving nuclear, Frobenius, and injective norms.

- M_2 has all three norm ratios equal to 8 but a seven-term decomposition. Grouped tensor powers give 8^k versus rank at most 7^k. This refutes every fixed constant repair without assuming arbitrary norm multiplicativity.
- The W degeneration shows why coefficients cannot be kept bounded in an unrestricted border-rank argument. The rational parameter 1/100 yields an exact rank-two counterexample.
- Orthogonal expansion on intrinsic mode supports gives the valid exponent 1/(d-1). Its limitation is exact: the resulting bound cannot exceed a mode rank.

Movement: the naive norm-to-rank conjecture changed from candidate to refuted; a correct replacement was proved.

### 23:06–23:16 — exact target norms, flattenings, and SDP direction

The root and tensor agent independently checked the symmetric polynomial coefficient normalization, all block singular spectra, and finite sign-average nuclear decompositions. Matrix nuclear/operator certificates and their saturation under preconditioning were proved. The Koszul atom cost was kept explicit.

The SDP agent checked the primal/dual directions and found a precise gap-sensitive rank test. A rational CHSH Gram solution and a Boolean SOS identity provide a nontrivial finite certificate. The natural target flattenings were shown to have Grothendieck gap one.

Two source errors in the supplied Friedland–Lim v3 were isolated by counterexamples and repaired in F-08. The mistaken use of an operator norm in equation (57)'s denominator, and the matrix inequality immediately before (60), are not used. Raghavendra–Steurer's displayed algorithm loss factor was checked against the actual proof and stated in the correct reciprocal direction.

Movement: each certificate route acquired a proved scope, an exact limitation, and working examples.

### 23:16–23:24 — a stronger route through the whole image

An initial conclusion limited to scalar norm ratios and one matrix map was deliberately not treated as a barrier for all norm-assisted methods. The next route combined a uniform injective-norm estimate on the entire flattening image with border substitution.

One proof detail needed repair: the approximating image itself need not have a basis of decomposition atoms. The proof now uses the span of all target atoms, selects a basis there, and chooses fixed independent source columns to obtain q-planes converging to the desired image. That corrected limiting argument was independently rederived by the tensor, SDP, and geometry agents.

The projector constant was computed over the full complex image, with conjugate factors retained. This gave n^2+n-1 for matrix multiplication, an alternating contraction improvement for row determinants, and explicit squarefree/minor image bounds for the other families.

Movement: a main lower-bound gate became strictly stronger than plain flattening.

### 23:24–23:34 — exact smaller-image reduction

The geometry agent proposed a quadratic residual-rank refinement. Two other agents independently checked it. The root then simplified and generalized it: a coordinate restriction isolates any nonzero coefficient of a residual minor or permanent and recovers a smaller member of the same tensor family.

This proves equality of the residual minimum with the smaller CP border rank, not merely an estimate. The recurrence in F-23 follows. Quadratic residual matrices have rank four, so both degree-four polynomial tensors receive the lower bound 39. Verified cubic CP seeds 17 and 16 give determinant size five at least 116 and permanent size five at least 115.

The more elaborate isotropic-line proof of the quadratic special case is retained only as a checked working alternative; the final paper uses the shorter coordinate restriction proof. No priority or new-record claim is made.

Movement: the generic residual-image gate was reduced exactly to a smaller same-family instance.

### Final proof and production review

Every F-01–F-23 proof was read in full by an assigned checker against the actual paper, in addition to cross-checks of the earlier notes. The final audit found a missing positivity hypothesis for the bounded-weight parameter B; B>0 and delta>=0 were added. The UGC consequence explicitly includes P!=NP when phrased as nonexistence of a polynomial algorithm.

The TeX runtime initially lacked format and font-map caches. The paper was compiled using installed local TeX sources and explicit existing font maps; no mathematical content was changed to accommodate the build. Layout and final package checks are recorded as production checks, not proof formalization.

## Routes that failed, and what replaces them

| Attempt | Failure or exact limitation | Refined result |
|---|---|---|
| Matrix ratios directly lower-bound CP rank | M_2 and the W family refute it. | F-01, F-05, F-06 |
| Divide by a fixed K_G power | Tensor powers make the ratio unbounded. | F-05 |
| Read nuclear norm as term count | It counts weighted normalized atoms; border decompositions may diverge. | F-07 |
| Use the unscaled sign SDP as a Hilbert spectral certificate | S(flat T) is at least HS(T); the resulting conversion is trivial. | F-09, F-10 |
| Use the same SDP upper bound for the sign optimum in the rank-sensitive test | L<=S<=U prevents the required strict violation. | F-11 needs a separate sign upper certificate |
| Choose pure basis vectors in the approximating flattening image | Such an image need not be spanned by pure vectors. | F-13 uses the full span of decomposition atoms |
| Use a real residual minimum for complex border rank | The real span of I and a planar rotation has complex rank-one members. | F-13/F-14 quantify over the complex image |
| Identify the limiting plane with the actual span of a Hilbert limit | Evaluation rank can drop. | F-17 retains both the scheme and the plane |
| Infer map rank from source/target K_0, lambda, gamma data | Zero and identity have identical such classes. | F-20 |
| Infer tensor rank from constant stalks, purity, or abstract point motives | Zero and pure rational points have identical specified data. | F-21 |
| Transfer factorial-normalized symmetric tensors integrally | Division by n! fails in small characteristic. | F-22 uses Hasse derivatives/divided powers |

## Residual scope, with next steps

There is no unchecked lemma inside the proved findings. The following are deliberately not asserted as solved open problems:

1. A generic efficient algorithm for the residual projector injective norm. A further result would need an explicit relaxation and a proved uniform approximation or avoidance guarantee.
2. Exact CP border ranks of the smaller family members appearing in F-23. The recurrence is proved; any sharper independently certified seed can be inserted. For row/permanent tensors one must not insert a merely Waring-border lower bound.
3. A separation of P from NP, an improved matrix-multiplication exponent lower bound, or superpolynomial determinantal complexity. Additional reductions to those computational models are necessary.
4. An unpublished-manuscript cote beyond the verified published Résumé archive and facsimile. The source audit records the actual searches and the limit of what was found.

## Required timing gates

The checkpoint schedule begins at 23:45 UTC and repeats every 45 minutes only while work remains active. Earlier checkpoints are never overwritten or nested. A final run ending before that first due time requires no checkpoint. The first three-hour stagnation review is due at 02:00 UTC on 21 November, then hourly. It has not been reached during the recorded mathematical work; no fictional three-hour review or two unchanged gates is claimed.

Final production review completed 2026-11-20 23:40:37 UTC. The mathematical scope is decided as recorded above; the separate unpublished-manuscript cote remains unlocated. The run ended before the first 45-minute checkpoint and before the three-hour review gate; no early checkpoint was created.
