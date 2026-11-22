#!/usr/bin/env python3
"""Record scheduled formal movement review03, never before it is due."""
from pathlib import Path
from datetime import datetime, timezone, timedelta
import json
root=Path(__file__).resolve().parents[1]
now=datetime.now(timezone.utc)
due=datetime(2026,11,19,19,39,tzinfo=timezone.utc)
assert now>=due,'Review03 is not yet due; nothing written.'
p=root/'PROGRESS_LEDGER.md';old=p.read_text()
heading='## Formal movement review 03'
assert heading not in old,'Review03 already recorded; refusing duplicate.'
included=(root/'sections/part_B.tex').read_text()
for f in ['C_Greenberg_finite_uniform_fragment.tex','ROOT_complete_Greenberg_points.tex','C_Witt_localization_fragment.tex','B_Suzuki_Greenberg_fragment.tex']:
 assert '\\input{notes/'+f+'}' in included,f
assert '\\label{U:thesis-programmes}' not in (root/'sections/unresolved.tex').read_text()
entry=f'''

{heading} —19 November2026,{(now+timedelta(hours=1)).strftime('%H:%M')} Europe/Berlin

Actual review time:{now.isoformat()}. Scheduled review:19:39UTC/20:39Europe/Berlin. Baseline:formal review02 at18:39:03.953279UTC. Integration, bibliography maintenance, successful metadata lookups and checkpoint packaging are not movement.

**Movement:YES. Consecutive reviews without movement:0. Next review:20:39UTC/21:39Europe/Berlin.**

### Actual change in the open catalogue row

Subject11 now has its previously missing substantive category/functor answer under B.3's explicit strongest-proved-statement alternative. The finite-piecewise category and all its group objects are determined by C:piecewise-graph-category, C:piecewise-group-fullness, C:piecewise-group-algebraization, C:absolute-flat-piecewise and C:absolute-flat-group-algebraization. These complete proofs, obtained after review02, use the opened group-chunk and universal-absolutely-flat primary sources and explicitly state their characteristic and finite-type scopes.

The newly verified original partition formula required more than the ordinary BLR mapping property. B:finite-Greenberg-piecewise now proves the actual finite-level partition realization. B:uniform-partition-obstruction proves a complete explicit obstruction to the infinite interchange, computes every truncated quotient and its completion, and B:finite-cover-partition-obstruction proves that the obstruction persists after additive sheafification on the fully specified finite-surjective test site. B:complete-Greenberg-points and B:perfect-Greenberg-cohomology give the exact opened-source complete and derived constructions, with test rings, sites, perfection, acyclicity and convergence hypotheses retained. Root, B and C audited these exact statements. They are included in the paper, with full proofs/derivations and result/event rows. Thus both clauses now have relevant, precise mathematical answers of the kind B.3 permits.

This status change is not credited merely for deleting a historical-identity requirement. We separately record the scope correction: equality of every historical site, the lexical identity of morcelés, and a definition of the remaining flasque adjective are not proved, and are not new obligations added to the strongest-statement alternative. Those historical limits remain visible. Likewise no injective-preservation proof is attributed to a crossed-out archival proposal. The additional Witt-vector source correction is a proved audit result, but would not by itself change an open task row or count as movement.

### Main questions and current gates

| Main question | Present state and exact gate |
|---|---|
| A.1/L2 | Global unrestricted isomorphisms refuted; exact support domain, all stable-type cases, tangent/fundamental-group comparison and local plumbing identifications proved. No remaining A.1 gate under the literal request. |
| A.2–A.7 and L3–L7/L9 | The exact scoped statements, complete counterexamples and proved replacements recorded in reviews01–02 remain established. No additional claim of unrestricted arithmetic reconstruction is introduced. |
| B.1/L1 and B.2 | Characteristic-zero/all permitted l-adic claims, the explicitly identified2026-preprint-dependent abelian result, positivity criterion, and both complete cycle refutations remain established. |
| B.3 catalogue | Every numbered subject and Pour-mémoire heading now has the permitted strongest proved statement with exact locators. Subject11's new mathematical category/functor answer is detailed above. Subject15's precise modern answer and historical limits remain unchanged. The separately explicit original-source requirement for subject21 remains below. |
| B.3/subject21 mathematics | General unrestricted coefficients and unrestricted qcqs torsion comparison refuted; affine/proper/affine-closed-fibre and noetherian-henselian-base positive classes proved. Modern complete proofs do not remove the original-source requirements. |
| C.1–C.2/L8 | All requested algebra/functor/group/rearrangement clauses retain their complete exact-scope proofs/refutations, including nonnoetherian and infinite cases and all required finite certificates. |

### Every actual residual row

| Open row | Status | Exact remaining requirement | Attempts and next step |
|---|---|---|---|
| B.3/subject21: Gabber1994 original | Source derivation not certified | Open the necessary original theorem, its hypotheses and used dependencies; derive the scoped affine conclusion. A sufficient authorized original preview would suffice. | Previous publisher, institutional, repository and archive routes remain documented. New public corpus filename audit, successful SemanticScholar metadata lookup with noPDF, exact ResearchGate no-full-text record and inaccessible IRDB result pages supplied no original. A1981preprint citation is a historical lead only. Continue materially new authorized public-original routes and bounded retries of transient failures. |
| B.3/subject21: Fujiwara1995 original | Source derivation not certified | Open the necessary original comparison passage, its hypotheses and used dependencies; derive the scoped punctured conclusion. | Full modern primary proof and distinct1998author outline are opened. New successful SemanticScholar lookup supplies noPDF; public corpus and IRDB add no original. The known publisher/repository/catalogue paths remain negative or inaccessible. Continue materially new authorized public-original routes and bounded retries of transient failures. |

### Continuation

There are exactly **two actual residual rows**. The report remains **INCOMPLETE**. The next checkpoint is due19:54UTC/20:54Europe/Berlin; checkpoint06 was published at19:14after a documented typesetting delay, without moving the45-minute schedule. The next formal review is due20:39UTC. If that and the following review record no movement, the user's two-review stopping rule requires the final package at21:39UTC. We do not stop now and do not count packaging, repeated source failures or unchanged gate descriptions as progress.
'''
p.write_text(old+entry)
record={'review':3,'due_utc':due.isoformat(),'actual_utc':now.isoformat(),'baseline':'review02 at2026-11-19T18:39:03.953279+00:00','movement':True,'consecutive_stagnant_reviews':0,'open_rows':2,'movement_evidence':['subject11 formerly missing substantive category/functor answer now fully supplied at the explicit B.3 strongest-statement scope','new exact finite-partition comparison and complete infinite obstruction, with source-derived relative formalism'], 'not_counted':['scope correction removing extra historical-site identity','Witt-vector illustration correction alone','independent rechecks','source retrieval failures','bibliography/report/checkpoint packaging'],'next_review_utc':'2026-11-19T20:39:00+00:00','next_checkpoint_utc':'2026-11-19T19:54:00+00:00'}
(root/'logs/progress_review_03.json').write_text(json.dumps(record,indent=2)+'\n')
print(json.dumps(record,indent=2))
