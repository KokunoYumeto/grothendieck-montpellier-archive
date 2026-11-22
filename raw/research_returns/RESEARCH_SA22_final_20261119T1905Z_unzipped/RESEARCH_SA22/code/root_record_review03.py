"""Record the third hourly substantive review and newly exposed scope gates."""
from pathlib import Path
from datetime import datetime, timezone
from zoneinfo import ZoneInfo
import json, time

R=Path(__file__).resolve().parents[1]
start=time.perf_counter();now=datetime.now(timezone.utc)
assert now>=datetime(2026,11,19,16,4,tzinfo=timezone.utc)
target=R/'code/root_record_review03_output.json'
assert not target.exists()
previous=json.loads((R/'notes/progress_review_state.json').read_text())
assert previous['review_number']==2
live=json.loads((R/'notes/live_source_requirements.json').read_text())
assert set(live['remaining'])=={'Pfluger1960','Lieberman1968','Fujiwara1995'}
gaps=json.loads((R/'notes/live_mathematical_scope_gaps.json').read_text())
assert gaps[0]['status'].startswith('closed:')
new=[dict(id='A1-raw-toric-isotopy-descent',opened_utc=now.isoformat(),status='open: under independent attack',
 claim='Raw cutting/capping on an actual toric seam is independent of its representative in a fixed-surface isotopy class.',
 issue='The fixed-target R^E fibers do not prove that their cuts are isotopic in one fixed underlying conformal surface, nor that raw tensor/normalization data descend to that quotient.',
 gate='Prove descent, or give an explicit isotopic toric pair in the same fixed X with different raw outputs; geodesic replacement already defines a separate canonical functor.',
 affects=['A.1 definition choices','67/079-080 heuristic']),
 dict(id='A6-mixed-characteristic-specialization',opened_utc=now.isoformat(),status='open: source-based replacement being derived',
 claim='The response to 049(c) covers specialization beyond equal characteristic zero.',
 issue='The existing theorem restricts to R=k[[t]], char(k)=0. The original question does not impose that restriction.',
 gate='Derive tame specialization for an existing proper log-regular model from Hoshi Cor3.9/PropA.10; explicitly test all-finite-etale strengthening; state model-existence boundaries without assuming general mixed-characteristic resolution.',
 affects=['A.6(a)','67/049(c)'])]
gaps.extend(new)
(R/'notes/live_mathematical_scope_gaps.json').write_text(json.dumps(gaps,indent=2)+'\n')
state=dict(review_number=3,review_time=now.strftime('%Y-%m-%d %H:%M:%S UTC'),
 review_time_client=now.astimezone(ZoneInfo('Europe/Berlin')).strftime('%Y-%m-%d %H:%M:%S Europe/Berlin'),
 scheduled_time='2026-11-19 16:04 UTC',movement=True,no_movement_streak=0,
 summary='Gabber1994 original-source row closed by actual reading of pp325-326 and exact deduction; the unequal-length toric definition branch was opened and resolved by Theorem1.13/Proposition1.14/Corollary1.15. Three original-source rows remain. A fresh scope audit exposed two additional open mathematical requirements: raw toric descent under fixed-surface isotopy, and specialization beyond equal characteristic zero. They are recorded explicitly, not hidden by the previous broad completion language. Rechecking and packaging do not count as movement.',
 next_review='2026-11-19 17:04 UTC (18:04 Europe/Berlin)',
 open_requirements=['Pfluger1960 original pp401-412','Lieberman1968 original relevant mathematical statement','Fujiwara1995 original Corollary6.6.4 or explicit original comparison','A1 raw-toric fixed-surface isotopy descent','A6 mixed-characteristic specialization scope'])
for name in ['notes/progress_review_state.json','notes/progress_review_03_snapshot.json']:
 (R/name).write_text(json.dumps(state,indent=2)+'\n')
live.update(updated_utc=now.isoformat(),next_review_utc='2026-11-19T17:04:00+00:00')
(R/'notes/live_source_requirements.json').write_text(json.dumps(live,indent=2)+'\n')
entry=f'''

## Substantive progress review3 — {state['review_time']} / {state['review_time_client']}

Scheduled for16:04UTC; recorded after the integrated proof/QA review and immediate new-scope triage. **Movement: yes. Consecutive reviews without movement:0.** The Gabber original row changed from open to closed after review2. The genuinely omitted independent-length toric branch was separately opened and resolved. No new finite rerun, literature search with unchanged result, typesetting or packaging is counted as movement.

### Status changes and current gates

| Item | Strongest current proved formulation and exact remaining boundary |
|---|---|
| A.1 / L2, main | Unrestricted isomorphisms remain refuted. Equal-length geodesic surgery has its exact support image, tangent isomorphism and orbifold fundamental-group comparison. Actual toric seams with independent paired lengths have that same image and global R^E fibers, with the explicit q=1 noninjectivity example. **New open branch:** raw surgery on toric representatives modulo isotopy in one fixed X has not been shown to descend. Geodesic replacement is already a well-defined separate convention. The fixed-target fiber theorem cannot substitute for the missing fixed-X comparison. |
| A.2 / L3 / L4 | Fixed-compactification radii, their complete support image and relative-growth limits, cusp decorations and the collar equation/counterexample are proved in the stated all-genus scope. Renewed proof review found no new gap and is not movement. |
| A.3 / L5 | Corrected welding, removable-seam uniqueness, vertices, Jordan arcs and both073 readings are proved. Pfluger1960 remains a prescribed original-source row. |
| A.4 | Orange-slice refutation and asymptotic replacement; enlarged mixed-cusp space and intrinsic length action are proved. |
| A.5 / L7 | Characteristic-not2 theorem, characteristic5 counterexample, characteristic3 inertia, characteristic2 boundary and stack/coarse distinction remain proved. |
| A.6 / L6 | Framed logarithmic reconstruction, characteristic-zero marked-model systems and mapping-class presentations are proved in their explicit scopes. **New open scope:** 049(c) is not restricted to equal characteristic zero. A proper log-regular mixed-characteristic tame-cover replacement is being derived from Hoshi; all-cover strengthening and model-existence assumptions are being separated. |
| A.7 / L9 | Real classification, arithmetic corrections, topology and H1 remain proved with original Alling–Greenleaf comparison. |
| B.1 / L1 | Characteristic-zero equality; explicit homological-positivity method domain; all-ell abelian-fourfold deduction using the opened Broe2026 preprint; Fermat and correspondence/blowup members; and generic-quintic counterexample are proved with their stated dependencies. Lieberman1968 remains a named-original source row. |
| B.2 | The divisor-square counterexample and Albanese-kernel answer remain proved with opened-source derivations. |
| B.3 | The28 subjects and9 Pour mémoire headings have individually scoped strongest proved statements, not blanket settlements of all historical problems. Gabber original pp325–326 now directly supply the arbitrary henselian-pair theorem and hypotheses. Fujiwara original remains open. |
| C.1 | Filtered exp/log, exact differential criterion, locally nilpotent intertwining and functor criteria remain proved, including the stated non-noetherian/infinite-module scope. |
| C.2 / L8 | Literal-axiom group classification, ConditionK refutation and exact replacement, non-forced extension and asymmetry remain proved. The renewed audit does not silently add021 cardinality completeness or022 translation saturation to017. |

### Every open requirement at this review

| Row | Current gate | Next concrete work |
|---|---|---|
| Pfluger1960 | Original relevant complete theorem in pp401–412 still unread. Lehto–Virtanen and independent welding proof already checked. | Only distinct public original-copy/catalogue routes; distinguish missing results, poor OCR, HTTP failure and restricted access. |
| Lieberman1968 | Relevant original mathematical theorem and exact hypotheses still unread. Kleiman deduction checked. | Distinct public author/offprint/thesis routes if advertised; metadata or corrupted introductory OCR is insufficient. |
| Fujiwara1995 | Original Cor6.6.4 or equally explicit original comparison still unread. Modern full theorem and later1998 author exposition checked separately. | Distinct public preprint/original-copy route; the MPIM9-item search adds no target and Fatcat503 is an unavailable route, not an absence result. |
| A1-raw-toric-isotopy-descent | Descent of raw surgery under isotopy of actual compatible seams in fixed X is unproved; neither well-definedness nor its failure is being asserted. | Compare fixed-X local deformations with fixed-(Y,q) imbalance fibers; seek a complete explicit counterexample or descent theorem. |
| A6-mixed-characteristic-specialization | Existing response is equal-characteristic-zero only, narrower than049(c). | Give the precise Hoshi tame-cover deduction for an existing proper log-regular model, test the unrestricted-cover claim, and retain exact model-existence limitations. |

The report remains **INCOMPLETE**. Two newly identified scope issues supersede any earlier summary that listed only the three source readings as outstanding. The next review remains17:04UTC /18:04Europe/Berlin. The user-directed stop requires two consecutive reviews without a row changing status or a main gate strictly shrinking.
'''
with (R/'PROGRESS_LEDGER.md').open('a') as f:f.write(entry)
out=dict(**state,seconds=time.perf_counter()-start)
target.write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out,indent=2))
