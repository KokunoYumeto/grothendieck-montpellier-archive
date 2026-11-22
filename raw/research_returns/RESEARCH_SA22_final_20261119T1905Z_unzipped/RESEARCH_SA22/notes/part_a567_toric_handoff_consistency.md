# Final handoff wording audit: A1 raw toric isotopy counterexample

Date: 2026-11-19, approximately18:11–18:14UTC. Agent: part_a567.
Scope: consistency of the current statement, proof wording, outcome-table generator and locators. No proof, numerical calculation, phase search, source retrieval or mathematical program was repeated.

## Main outcome

The three requested distinctions are consistent in the active theorem and report generator. No mathematical or definition-scope mismatch was found. One minor CSV status-polarity ambiguity is reported separately below; no requested file was edited.

The active fragment is sections/part_a567_toric_descent.tex, included by sections/part_a1.tex:170. It is therefore part of the current paper, not merely an unused draft.

| Statement ID | Current compiled number | Statement start page | Source locator |
|---|---|---:|---|
|A1-pant-third-jet|Lemma1.16|15|part_a567_toric_descent.tex:13–64|
|A1-four-point-plumbing-jet|Lemma1.17|16|part_a567_toric_descent.tex:65–168|
|A1-toric-nondescent|Theorem1.18|17|part_a567_toric_descent.tex:170–276|

These mappings agree with logs/RESEARCH_SA22_paper.aux:48–50, the current aggregate CSV's A1-toric-nondescent row, and the generated report's A.1 outcome row. The generator reads those actual auxiliary labels at code/root_reconcile_report.py:11–18 and resolves them in the outcome table at67–68.

## Requested wording checks

**Unevaluated analytic phase.** The fragment's opening lines9–11 call this an exact analytic counterexample and expressly distinguish its deterministic analytic rule from an evaluated numerical angle. Lines243–252 define N as the least positive n for which Delta(exp(i/n)) is nonzero, prove existence by the identity theorem, and explicitly assert no numerical value of N. The same qualification appears in the owned results row, live mathematical-scope record, and generator paragraph at code/root_reconcile_report.py:72. No finite enumeration, numerical welding certificate, or evaluated phase is claimed in these checked statements. The exact coefficient identity is not described as a numerical approximation (fragment:160–162).

**Two cuts in the same marked surface.** The theorem statement at172–177 names one four-labelled X and two isotopic cuts C,C_geo within it. The proof's unequal X and balanced X_G at255–264 are auxiliary comparison surfaces. The actual same-surface pair is then explicitly C and X's own geodesic C_geo at266–275. The generator's A.1 row at41 and explanatory paragraph at72 both say that the unequal seam and its own geodesic have different tensors in the same X. They do not substitute C on X and a curve on the distinct X_G as the counterexample pair. The fixed four external labels are retained; choosing a topological marking of that single X does not introduce a second surface.

**Separate geodesic convention.** Fragment:178–179 explicitly identifies replacing a representative by its geodesic before surgery as the different well-defined convention. The generator repeats that distinction at41 and72. The A.1 definition text at sections/part_a1.tex:10–16 separately identifies equal-length geodesic representatives and broader unequal-length toric compatibility. The older radius-pair noninjectivity example remains labelled as distinct actual cut objects in generator:42; it is not silently promoted into the same-X isotopy counterexample.

The exact manuscript-interpretation correction is still attached to inputs/RESEARCH_SA22_transcriptions/transcriptions/MPL_67_053-101_transcription.tex:939–963 (67/079–080). Those lines discuss possibly nongeodesic circles, their unique geodesics and the tentative reciprocal-rescaling heuristic, including the manuscript's own expressed doubt. The current correction row and labels map to that passage consistently.

## Minor metadata polarity ambiguity, reported without edits

checks/part_a567_results.csv:42 gives the statement in negative form, namely that raw canonical toric surgery is **not invariant**, while its status cell says **Refuted**. The current aggregate RESEARCH_SA22_results.csv:20 similarly places the proved counterexample statement next to Refuted.

The active theorem caption is unambiguous: **Refuted: raw toric surgery is invariant under isotopy in a fixed surface**. The outcome-table generator also attaches Refuted to the positive invariance/descent claim. Thus the CSV cell is understandable as the status of the manuscript claim, but a reader treating the status as applying literally to the adjacent negated statement could read it backwards. This is a metadata wording ambiguity, not a changed mathematical conclusion or an error in the phase or same-X argument.

The parent was alerted. A consistent resolution, if desired, is to clarify that the CSV status applies to the original positive claim, or to make that positive claim the row's status-bearing text while retaining the proved counterexample in its notes. No TeX, generator, CSV, aggregate or mathematical status was changed by this audit. It does not count as progress movement.

