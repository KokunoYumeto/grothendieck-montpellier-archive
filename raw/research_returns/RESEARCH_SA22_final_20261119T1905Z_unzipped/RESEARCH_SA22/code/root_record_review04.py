"""Record the fourth substantive review only once its scheduled time is reached."""
from pathlib import Path
from datetime import datetime, timezone
from zoneinfo import ZoneInfo
import json, time

R=Path(__file__).resolve().parents[1]
began=time.perf_counter()
now=datetime.now(timezone.utc)
due=datetime(2026,11,19,17,4,tzinfo=timezone.utc)
assert now>=due,'Do not record an hourly review before its scheduled time.'
target=R/'code/root_record_review04_output.json'
assert not target.exists()
previous=json.loads((R/'notes/progress_review_state.json').read_text())
assert previous['review_number']==3
live=json.loads((R/'notes/live_source_requirements.json').read_text())
gaps=json.loads((R/'notes/live_mathematical_scope_gaps.json').read_text())
assert live['remaining']==['Pfluger1960','Lieberman1968','Fujiwara1995']
assert all(x['status'].startswith('closed:') for x in gaps)
required={'A1-raw-toric-isotopy-descent','A6-mixed-characteristic-specialization'}
assert required<={x['id'] for x in gaps if x.get('closed_utc','')>'2026-11-19T16:09:28'}
state=dict(review_number=4,review_time=now.strftime('%Y-%m-%d %H:%M:%S UTC'),
 review_time_client=now.astimezone(ZoneInfo('Europe/Berlin')).strftime('%Y-%m-%d %H:%M:%S Europe/Berlin'),
 scheduled_time='2026-11-19 17:04 UTC',movement=True,no_movement_streak=0,
 summary='The two mathematical requirements open at review3 changed status: raw toric fixed-surface isotopy descent was refuted with the exact four-point analytic construction, and mixed-characteristic specialization was resolved by the precise existing-model tame comparison plus counterexamples to stronger readings. The nonsplit-node character and relative-Frobenius preservation issues exposed in that work were also resolved. Three required original-source readings remain open. Intrinsic-category clarification, proof rereads, the C.1(d) wording/test clarification, source searches with unchanged outcomes, typesetting and packaging do not count as movement.',
 next_review='2026-11-19 18:04 UTC (19:04 Europe/Berlin)',
 open_requirements=['Pfluger1960 original pp401-412','Lieberman1968 original relevant mathematical statement','Fujiwara1995 original Corollary6.6.4 or explicit original comparison'],
 documentation_limitation='Some historical utility/failure runtimes were not recorded. Their exact known/unknown scope remains in the program inventory and notes; later runtimes are not substituted for the original durations.',
 counted_existing_row_changes=sorted(required))
for name in ['notes/progress_review_state.json','notes/progress_review_04_snapshot.json']:
    (R/name).write_text(json.dumps(state,indent=2)+'\n')
live.update(updated_utc=now.isoformat(),next_review_utc='2026-11-19T18:04:00+00:00')
(R/'notes/live_source_requirements.json').write_text(json.dumps(live,indent=2)+'\n')
entry=f'''

## Substantive progress review4 — {state['review_time']} / {state['review_time_client']}

**Movement: yes. Consecutive reviews without movement:0.** The two explicit mathematical rows open at review3 changed status after that review. We count those closures, not the quantity of subsequent proof notes or pages. The next review is18:04UTC /19:04Europe/Berlin.

### Actual changes since review3

| Existing open row | Status now and complete proof |
|---|---|
| A1-raw-toric-isotopy-descent | Refuted. Lemmas1.16–1.17 compute the one-cap third jet and the normalized four-point plumbing coefficient. Theorem1.18 specifies exact radii and an exact deterministic phase and proves that the unequal toric seam and its own geodesic in the same X have different raw tensor outputs. The integer selecting the phase is proved to exist, not numerically evaluated. |
| A6-mixed-characteristic-specialization | Resolved by Theorem6.16 for actual finite Kummer-etale covers of an existing proper log-regular model and its strict special log fibre. Proper valuative comparison proves model independence without a common regular refinement. Proposition6.18 supplies an explicit wild constant cover over Q2 refuting the unrestricted-cover strengthening. |

During that same scope work, Proposition6.19 gave the exact cyclotomic-times-branch-sign node-inertia character and an explicit rational nonsplit nodal cubic; Proposition6.17 gave the relative-Frobenius pair over F16 with verified characteristic-zero lifts, refuting unchanged strict reconstruction under reduction. Their finite certificates contain21 and20 assertions respectively, with actual recorded runtimes. These are not merely restatements of the equal-characteristic-zero result.

Proposition6.20's intrinsic all-DVR category is a useful clarification of the already closed tame scope. It is **not counted as another movement**. Neither are the independent zero-face/inactive-component audit, the exact-phase audit, the B.2 reread, the C.1(d) scalar/nonunital precision fixes and universal-algebra explanation, the status-label audit, new negative public-catalogue searches, or PDF/report work.

### Main-question gates and retained scope

| Item | Strongest current proved formulation / boundary |
|---|---|
| A.1 / L2 | Unrestricted global isomorphisms and raw cut-isotopy descent are refuted. The geodesic convention has the exact support image and tangent isomorphism; actual unequal toric seams have the same shadow/tensor image and signed-edge R^E fibers. Full external shapes retain their explicit matching condition. The orbifold fundamental-group statements and low-complexity cases are proved. |
| A.2 / L3 / L4 | Fixed-compactification radius injectivity, full support image and relative-growth limits are proved with the explicit connected-component conventions. Cusp decorations and the exact collar equation/counterexample are proved. |
| A.3 / L5 | Corrected existence/uniqueness, vertex compatibility, Jordan arcs and both073 readings are proved. The separate prescribed Pfluger original reading remains open. |
| A.4 | Literal orange model is refuted; the correct asymptotic replacement and enlarged mixed-cusp space with intrinsic length action are proved. |
| A.5 / L7 | Characteristic-not2 theorem, corrected proposition, characteristic5 counterexample, characteristic3 inertia and stack/coarse distinctions are proved. |
| A.6 / L6 | Framed reconstruction, precise model systems, existing-model tame specialization, intrinsic tame-category clarification and mapping-class presentations are supplied in their written scopes. Wild covers, nonsplit-node automatic cyclotomy, chosen-fibre uniqueness and unchanged strict reconstruction under reduction have explicit counterexamples. General mixed-characteristic regular-model existence is not asserted. |
| A.7 / L9 | Real classification, arithmetic corrections, topology and H1 are proved and compared with the original Alling–Greenleaf passages. |
| B.1 / L1 | Characteristic-zero equality; all-ell abelian-fourfold deduction with its explicit opened2026-preprint dependency; exact domain of the positivity argument and geometric members; and first-question quintic counterexample are supplied. Lieberman original reading remains open. |
| B.2 | Generic divisor-square nontorsion and the exact Albanese-kernel replacement are proved through opened Mumford/Bloch inputs and the full parameter-space argument. |
| B.3 | All28 subjects plus9 Pour mémoire headings retain their individually scoped strongest proved formulations. Gabber original main theorem is directly checked; Fujiwara original remains open. No blanket settlement of motives or arbitrary positive-characteristic resolution is claimed. |
| C.1 | Filtered exp/log, exact differential criterion, locally nilpotent intertwining and arbitrary module-functor criteria are proved. The clarified universal tests are explicit ring/linear-lifting conditions, with no quasi-coherence assumption. |
| C.2 / L8 | Literal017 group classification, ConditionK counterexample and exact replacement, non-forced extension and symmetry characterization are proved. Extra021/022 assumptions are not silently added. |

### Every remaining substantive open row

| Required original | Exact smallest gate | Latest distinct approaches and outcome | Next action if a real route appears |
|---|---|---|---|
| Pfluger1960 | Actual original relevant theorem in pp401–412, with its hypotheses, remains unread. | Publisher restriction; public journal metadata/OCR and actual covers; ETH finding aid; TDL1959 volume; UPenn/Hathi/Mathdoc/IIT catalogue routes. No relevant original text. Failures and OCR limits are not absence evidence. | Follow an actually advertised public original/offprint or authorized copy; do not replace it with a later citation. |
| Lieberman1968 | Actual original mathematical statement and hypotheses remain unread. | JSTOR/private-issue limitations, MIT thesis metadata, IHES2-hit records, ProjectMUSE coverage from1996, and Ranicki public collections. No original passage obtained. | A distinct advertised original/theorem preview would suffice; a full-paper requirement has not been imposed. |
| Fujiwara1995 | Original Cor6.6.4 or equally explicit original comparison remains unread. | Publisher/archive limits;1992-preprint bibliographies; Tokyo/RIMS/IAS/MPIM catalogues; OpenAIRE; later1998 author exposition; new IHES2/0 search resolves both hits as Lafforgue2000/2002. No target original theorem. | Follow a distinct actual1992/1995 original link if found; modern proofs and the1998 exposition remain separately identified. |

### Documentation limitation retained separately

Some early failed prototypes and source/admin utilities did not record elapsed time. The inventory preserves the actual output and marks those historical values unknown; a timed rerun is never represented as the original duration. The exact cases are already listed in the timing audits. No additional mathematics or unverifiable guessed duration can repair a measurement that was not recorded. This limitation is not hidden by the three substantive-source-row count.

The report remains **INCOMPLETE**. The current mathematical-scope registry has no additional open row, but this does not discharge the named-original obligations or the historical reporting limitation. The user's two-consecutive-no-movement rule has not yet been met.
'''
with (R/'PROGRESS_LEDGER.md').open('a') as f:f.write(entry)
out=dict(**state,seconds=time.perf_counter()-began)
target.write_text(json.dumps(out,indent=2)+'\n')
print(json.dumps(out,indent=2))
