# Step 1: chronology and geometric-count routes

Run **TRACE_DET_20261121**, 21 November 2026. Agent `/root/step1_history_route`; model GPT-6 Astra Pro (inherited developer label); effort setting not exposed. This is source analysis of the stipulated theorem's implementation, not a Lean build, axiom audit, or reassessment of the theorem.

## Result

The exact historical mapping of Remark §2 step1, p.3, “10/6/26: Stepanov determinant,” remains **unresolved**. This pass tried two routes not exhausted by the earlier Wronskian/theta/monomial/Hasse-minor/Moore inventory:

1. recover chronology from the archive or its public mirror history;
2. identify a concrete determinant in finite-field point counts or geometric multiplicity constructions.

The chronology route gives a definite negative result about the available *metadata*: it contains no 6 October development history. The geometric routes locate actual finite-field Fourier counting and local Hasse-jet divisibility, but neither supplies the historical declaration dictionary. These observations do not establish absence of an unnamed Stepanov mechanism, and they are not counted as a reduction of the remaining historical gate.

## 1. Archive chronology cannot distinguish the candidates

The entire tar archive `work/source_extra/lean.tar.gz` was traversed with Python's `tarfile` reader, examining every regular-file header without extracting it again. The resulting inventory is `step1_archive_metadata.json`.

- There are 175190 regular files: 175187 Lean files and three build/configuration files.
- Every regular-file `mtime` is exactly zero, corresponding to `1970-01-01T00:00:00+00:00`.
- Every regular-file owner and group name is empty; user and group IDs are both zero.
- The only non-Lean files are `lean/lake-manifest.json` (3221 bytes), `lean/lakefile.toml` (1619 bytes), and `lean/lean-toolchain` (25 bytes).

Thus no timestamp or accompanying narrative file in this archive can select the construction made on 6 October. This conclusion concerns the inspected tar headers, not the author's original working directory or an unavailable private history.

The public GitHub mirror was also read at `https://github.com/CocoSgt/riemann-hypothesis-lean`, README sections “Getting the code” and “For agents: suggested procedure.” Its only narrative pointer for the mathematical chronology is back to `remark.pdf`. The current repository page reports two commits. The web service could not fetch the commits page (`DisabledError`); a direct read of the public GitHub API then succeeded:

`https://api.github.com/repos/CocoSgt/riemann-hypothesis-lean/commits?per_page=100`

The complete two-entry response was reduced to source-provenance fields in `step1_mirror_commit_metadata.json`:

| Commit | UTC author and committer date | Role stated in the commit message |
|---|---|---|
| `0fb9869c6e6d7b54b67de803af0e0be29d37fc22` | 2026-11-20 14:59:12 | Initial mirror import; no parent commit |
| `7cbf7a0c32fca1badf05931879a37c3f8a2b03b4` | 2026-11-20 15:13:33 | README guide; parent is the initial import |

This public history records mirroring and documentation, not October development. The mirror's own assertion that it copied the original files is recorded as its assertion; this pass did not authenticate it independently against the author's fourteen original parts.

A bounded literal-date search over all Lean source for `2026.?10.?0?6`, `0?6.?10.?2026`, `10/6/26`, `6 october`, `october 6`, and `stepanov` returned no lines. Its result is `step1_date_hits.txt`. Date/name absence is only search evidence and supplies no semantic impossibility theorem.

## 2. A genuine finite-field point count, with its actual determinant role

All Lean locators here are relative to the retrieved mirror's `lean/src/`.

`CompanionTheory/SpectralGeometry/LocalGlobalProofs/AdelicAnalysis/FiniteFieldQuadraticFormPointCount.lean:13–14` defines

\[
Q_B(x)=\tfrac12 x^tBx
\]

for a finite field k and a finite index set. Its `gauss_mul_conj` at42–45 assumes characteristic different from2, B symmetric, det(B) nonzero, a nontrivial additive character ψ, and t nonzero; it asserts

\[
\left|\sum_x\psi(tQ_B(x))\right|^2=|k|^{|\iota|}.
\]

The proof uses determinant nonvanishing at lines53–56 only to infer that Bx=0 forces x=0. Character orthogonality then kills nonzero shifts. `count_mul_card` at84–86 gives the exact finite orthogonality count

\[
|k|\,\#\{x:Q_B(x)=s\}
=\sum_{t\in k}\psi(-ts)\sum_x\psi(tQ_B(x)).
\]

For |ι|=2M and M≥1, `card_quadric_even` at108–112 bounds the deviation from |k|^(2M−1) by |k|^M. The exported wrapper is

`CompanionTheory/SpectralGeometry/LocalGlobalProofs/AdelicAnalysis/FiniteFieldQuadraticFormPointCountStatement.lean:8–9`,

`GlobalTheory.T.finite_field_quadratic_form_point_count`.

This is a concrete finite-field Fourier calculation in the source, with an actual finite matrix B. The determinant is the nondegeneracy test for a quadratic form over k; it is not a displayed Fredholm determinant in a Xi spectral parameter. Its occurrence strengthens the broad finite-field counting analogy, but the inspected statements do not call it the step1 determinant or provide the October chronology. The full Lean proof was not replayed; the displayed definitions, assumptions, orthogonality identity and determinant-use site were checked as source content.

## 3. A geometric multiplicity mechanism, but in a Picard-divisibility argument

`Development/AbelianVarietyTheory/Proofs/DivisorProofs/HasseJetVanishingMemPowStatement.lean:7–8` exports

`GlobalTheory.T.exists_maximal_mem_pow_of_hasse_vanishing`.

It assumes an algebraically closed field k, a finite-type Dedekind k-algebra A, N≥2, and k-linear functionals Δ_l:A→k with Δ_0(1)=1, truncated Hasse Leibniz rules, and an element π with Δ_1(π)=1. It concludes that there is a maximal ideal Q, characterized by Δ_0, such that

\[
\Delta_l(f)=0\quad(0\le l<N)\quad\Longrightarrow\quad f\in Q^N.
\]

The proof body is `HasseJetVanishingMemPow.lean:7–135`. This is genuine conversion from derivative vanishing to multiplicity along a closed point. A search of the exact declaration names found one substantive application in

`Development/AbelianVarietyTheory/Proofs/DivisorProofs/PicDivisibleDedekindFiniteTypeAlgClosed.lean:320–333`.

The surrounding construction is `formal_deformation` at61–64 and `specialise_generic_solution_hasse` beginning273. The endpoint `pic_divisible` at498–499 asserts divisibility of `CommRing.Pic B` by an integer invertible in k for a finite-type Dedekind algebra over algebraically closed k. Thus this source route concerns a geometric deformation and Picard-divisibility mechanism. The presence of vanishing conditions alone does not identify an auxiliary determinant for finite-field rational-point bounds or for the timeline's step1. Its exact-name use list is retained in `step1_hasse_jet_uses.txt`.

This pass read the signatures and the application neighborhood, not all of the long Picard-divisibility proof; no independent proof certification is claimed.

## 4. Other candidate distinctions checked

- `Development/EtaleCohomology/WeilConjectures/FermatCount.lean:170–172` defines a proposition bounding the Fermat count by a squared-error estimate. Lines143–154 define a curve-family weight-propagation proposition. These are explicit proposition definitions at those locators; neither is a displayed auxiliary determinant or historical identification. This is not a claim that no proofs of related propositions occur elsewhere.
- `GroundTheory/HeightsAndTheta/Heights/OrbitLimits/StatementsCurveCountLower.lean:9–16`, `StatementsNefCountUpperCurve.lean:13–21`, and `../HilbertSamuel/StatementsCurveSmallCountLower.lean:11–18` concern small-section counts and arithmetic heights. Their word “count” does not itself make them finite-field point-count arguments.
- `Formalism/LocalToGlobal/CharacterGerms/CartesianBoundOnCurves.lean:48–54` proves integrality of a finite determinant from integrality of its entries. The surrounding `Cart` formal-series module statements are not, from that formula alone, a historical Stepanov matrix.
- `Development/AbelianVarietyTheory/Proofs/InertiaEigenvalues/IndexSpanMatrixEqValDet.lean:105–137` bounds the root multiplicity at1 of a finite polynomial-matrix determinant by its degree rn. This is an actual determinant-and-multiplicity argument, but the inspected local-polynomial/lattice context does not supply the missing chronology or a Xi identity.

## Search scope, limits, and next step

The retained candidate files are `step1_deeper_candidates.txt`, `step1_deeper_text_hits.txt`, `step1_pointcount_paths.txt`, `step1_pointcount_text.txt`, and `step1_targeted_count_paths.txt`. A broad path search was noisy because directory names themselves contained “WeilBound” or “PointCounts”; it was followed by a basename-only filter (94 files) and concrete statement reads. Candidate counts are not semantic coverage or proof-audit claims.

The next needed datum is still the **specific determinant, auxiliary section, or declaration together with the specialization the author meant on 6 October**. An author-supplied mathematical account or a historical working source could provide that. Neither file timestamps nor the mirror's two import/documentation commits can provide it. The current report's finite-polynomial obstruction and positive trace-norm-limit criterion continue to apply to any proposed bridge once its actual definition is supplied.

Whole-note check: after composition, every assertion above was reread against the displayed source signatures, metadata and recorded queries. No new mathematical theorem is asserted with an unchecked proof. The surviving exact-history gate is explicitly unchanged.
