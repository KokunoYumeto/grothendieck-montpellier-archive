"""Record the scheduled second substantive review, after15:04UTC only."""
from pathlib import Path
from datetime import datetime,timezone
import json,time

ROOT=Path(__file__).resolve().parents[1]
START=time.perf_counter()
now=datetime.now(timezone.utc)
assert now>=datetime(2026,11,19,15,4,tzinfo=timezone.utc)
previous=json.loads((ROOT/'notes/progress_review_state.json').read_text())
assert previous['review_number']==1, 'Do not duplicate or overwrite a review'
live=json.loads((ROOT/'notes/live_source_requirements.json').read_text())
assert set(live['remaining'])=={'Pfluger1960','Lieberman1968','Gabber1994','Fujiwara1995'}
(ROOT/'notes/progress_review_01_snapshot.json').write_text(json.dumps(previous,indent=2)+'\n')
state=dict(review_number=2,review_time=now.strftime('%Y-%m-%d %H:%M:%S UTC'),
 review_time_client=now.astimezone(__import__('zoneinfo').ZoneInfo('Europe/Berlin')).strftime('%Y-%m-%d %H:%M:%S Europe/Berlin'),
 movement=True,no_movement_streak=0,
 summary='Four original-source rows closed since review1: Alling-Greenleaf1971, Birman1974, Lehto-Virtanen1973, and RaynaudLNM119. Each closure has an actual relevant-original reading and a checked mathematical comparison or deduction. Four specific original readings remain open. Independent adversarial proof reviews and exposition/packaging are recorded but do not count as movement.',
 next_review='2026-11-19 16:04 UTC (17:04 Europe/Berlin)',
 open_requirements=['Pfluger1960 original pp401-412','Lieberman1968 original relevant mathematical statement','Gabber1994 original affine-henselian statement and its exact hypotheses','Fujiwara1995 original Corollary6.6.4 or an equally explicit original statement of that comparison'])
(ROOT/'notes/progress_review_state.json').write_text(json.dumps(state,indent=2)+'\n')
(ROOT/'notes/progress_review_02_snapshot.json').write_text(json.dumps(state,indent=2)+'\n')
live['next_review_utc']='2026-11-19T16:04:00+00:00'
live['updated_utc']=now.isoformat()
(ROOT/'notes/live_source_requirements.json').write_text(json.dumps(live,indent=2)+'\n')
entry=f'''

## Substantive progress review2 — {state['review_time']} / {state['review_time_client']}

This is the scheduled hourly comparison with review1. **Movement: yes. Consecutive reviews without movement:0.** Four previously open original-source rows changed status, from8 to4. We count neither additional checks of the same mathematical gates, broader source searches with unchanged results, corrected exposition, compilation nor checkpointing as movement.

### Status changes which count

| Open row at review1 | New state and exact evidence |
|---|---|
| Alling–Greenleaf1971 | Closed. Original §1.9 pp60–66, especially Proposition1.9.6 and Theorem1.9.8; all five lattice rows and topology/cohomology comparison checked directly. |
| Birman1974 | Closed. Original §4.1 pp148–161, especially pp151–152; the all-marked-points closed-surface sequence is distinguished from puncture/boundary variants. |
| Lehto–Virtanen1973 | Closed. Original ChapterII §§6–8 pp81–100, especially §7.5 pp92–95; the sewing theorem, transition directions and normalization are checked. |
| RaynaudLNM119 | Closed. Original pp14–15 and37–38 supply exact propertyW and LemmaIII1.1. The complete matrix/base-change deduction is thm:B3-raynaud-flatness and its subject17 application is thm:B3-picard. The full book is not claimed read; its unused purity statements are not assumed. |

### Current gates of the main mathematical questions

| Item | Current strongest proved formulation and boundary |
|---|---|
| A.1 / L2, main | Unrestricted global isomorphisms are refuted in(0,4) and every positive-complexity stable type. Exact graphwise support range, tangent map and orbifold fundamental-group comparison are proved; the(0,3)exception and(1,1)range are explicit. Arbitrary-cut and external-only interpretations have separate counterexamples. All requested local plumbing comparisons are checked. No mathematical gate changed in this hour. |
| A.2 / L3 / L4 | Fixed-compactification radii determine the cap system; the full logarithmic image and all relative-growth limits are proved in every stable genus. Cusp decorations and the exact collar equation/sign-changing example are complete. The moving-seam clarification strengthens exposition, not the established gate. |
| A.3 / L5 | Corrected seam existence/uniqueness, graph vertices, Jordan arcs and both ambiguous073 readings are proved. Lehto–Virtanen original now checked; Pfluger original remains a separate required source row. |
| A.4 | The orange-slice model is refuted and its asymptotic replacement proved. The enlarged mixed-cusp space and intrinsic nonnegative-length action are specified with their properties. |
| A.5 / L7 | Corrected characteristic-not2 theorem, characteristic5 exception, characteristic3 inertia, characteristic2 boundary and stack/coarse distinction are proved with finite certificates. |
| A.6 / L6 | Framed-logarithmic curve reconstruction, inertia corrections and presentations are proved in their explicit scopes. Characteristic-zero marked model systems use the stated Isom-anabelian input; specialization is explicitly equal-characteristic-zero. Same-cover-data special-scheme reconstruction is refuted. Birman original now checked. |
| A.7 / L9 | Real classification, arithmetic module/PID corrections, topology and H1 are proved. Alling–Greenleaf original comparison is now complete. |
| B.1 / L1 | Characteristic-zero equality and exact method domain are proved. Positive-characteristic abelian fourfold deduction uses the opened Broe2026 preprint plus Kahn and Ancona with explicit trust boundary; numerical positivity alone is not substituted for homological positivity. Fermat/correspondence/blowup members and generic-quintic counterexample are proved. Lieberman original remains a separate named-source row. |
| B.2 | Algebraically trivial divisor with nonzero square and the Albanese-kernel answer have complete constructions and opened-source derivations. |
| B.3 | All28 subjects plus9 Pour mémoire headings have the required strongest precise proved formulations. Raynaud thesis now contributes an original-based universal base-change refinement. Gabber1994 and Fujiwara1995 original deductions remain the two prescribed subject21 source rows. |
| C.1 | The filtered exp/log equivalence, exact differential criterion, locally nilpotent intertwining and functor criteria are proved, including non-noetherian and infinite-module cases. |
| C.2 / L8 | Literal-axiom classification, ConditionK counterexample/replacement, non-forced extension and asymmetry are proved. The optional nonempty-family refinement follows by zero indicators and does not add a fullness hypothesis or change the result. |

### Every remaining open requirement

| Open row | Exact remaining gate | Routes checked and next concrete approach |
|---|---|---|
| Pfluger1960 / A.3 | Read a relevant complete mathematical statement from the original pp401–412 and derive its precise welding use. Independent and Lehto–Virtanen proofs are already supplied. | Publisher and historical galley require subscription;182 public journal catalogue records and166 advertised OCR files inspected with explicit poor-OCR limits. Three undated covers are now visually resolved as1926/1929/1930 and the1958 item asvolume22. The original Tamil Digital Library search form is a distinct live route beyond the IA mirror and is being queried. |
| Lieberman1968 / B.1(b) | Open the original relevant Lefschetz/numerical-homological theorem with exact hypotheses, then compare it to the opened Kleiman deduction. | Publisher/repository/collection routes recorded. New official MIT TIMDEX metadata identifies the1966 dissertation but advertises no digital file; genealogy's1967 conflict is preserved. Public introductory OCR is corrupted and supplies no adequate theorem. Continue distinct public offprint/thesis routes if a new advertised link appears; do not call a catalogue record theorem access. |
| Gabber1994 / B.3#21 | Read the original affine-henselian statement and its complete hypotheses, then derive the form used here. | Publisher subscription, public repositories, IHES directory, journal holdings and1981-preprint provenance checked. A genuinely advertised original first-page/preview route is being re-examined for a complete relevant statement; title or abstract alone cannot close the row. The opened modern proof remains separate. |
| Fujiwara1995 / B.3#21 | Read original Corollary6.6.4 or an equally explicit original statement of that comparison, then check its noetherian scope. | Current and archived article routes, RIMS/author catalogues and1998 author exposition recorded. The advertised original first-page route was newly checked: archive404, exact capture list empty, live challenge HTML; stopped without a bypass. The1998 proof outline is not represented as the1995 original. Continue only a distinct legitimate public-copy route. |

The report remains **INCOMPLETE**. No new mathematical gap was found by this hour's independent A1/A2, B1(b), and C2 audits; their bounded verification scope is explicit. The next substantive review is16:04UTC /17:04Europe/Berlin. If no open row changes status or main gate strictly shrinks by then, the consecutive no-movement count becomes1. The user-directed stop requires two consecutive such reviews.
'''
with (ROOT/'PROGRESS_LEDGER.md').open('a') as f:f.write(entry)
out=dict(**state,seconds=time.perf_counter()-START)
(ROOT/'code/root_record_review02_output.json').write_text(json.dumps(out,indent=2)+'\n')
print(json.dumps(out,indent=2))
