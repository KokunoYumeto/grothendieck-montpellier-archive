"""Execute the third scheduled review; preserve previous reviews immutably."""
from pathlib import Path
from datetime import datetime, timezone
from copy import deepcopy
import csv
import json
import time

root=Path(__file__).resolve().parents[1]
start=time.perf_counter()
due=datetime(2026,11,19,7,50,tzinfo=timezone.utc)
now=datetime.now(timezone.utc).replace(microsecond=0)
if now<due:
    raise SystemExit('Review03 is due at07:50UTC; it cannot be executed prematurely.')
target=root/'progress/review_03.json'
if target.exists():
    raise SystemExit('Review03 already exists and will not be overwritten.')
previous=json.loads((root/'progress/review_02.json').read_text())
with (root/'ITEM_STATUS.tsv').open(newline='') as handle:
    items=list(csv.DictReader(handle,delimiter='\t'))
by_item={r['item']:r for r in items}
rows=deepcopy(previous['open_mathematical_rows'])
for item in rows:
    rows[item]['recorded_status']=by_item[item]['status']
rows['B.1']['attempts_and_limits']=(
    'The new universal-CH0 surface-support criterion proves rational=numerical in codimension2, '
    'and hence all ordinary Chow degrees for geometrically uniruled threefolds over finite fields. '
    'This is a broad proved class, but it does not reduce the universal Chow-phantom gate. '
    'The earlier rational blow-up encoding still retains arbitrary centres. No universal vanishing is proved.')
rows['B.3']['current_gate']=(
    'Divisor Tate for smooth projective geometrically integral surfaces with trivial geometric '
    'etale fundamental group, H1(Y,O_Y)=0 and very ample canonical bundle, over every finite '
    'constant extension of F_p. The reduction already holds over each unchanged fixed finite field. '
    'The same previously counted numerical thresholds and slope-near-one conditions can be imposed. '
    'This is equivalent to the universal whole-prime-to-p Brauer and abelian-torsor assertions.')
rows['B.3']['attempts_and_limits']=(
    'The finite abelian prime-to-p fundamental group of Yuan\'s model is killed by a fixed-field '
    'finite etale cover defined by the zero-section arithmetic splitting. Its generic isogeny '
    'preserves the ample dual Hodge bundle. Reapplying Yuan4.5 to the identical generic abelian '
    'variety recovers coherent H1=0; birational purity and ample Lefschetz cuts preserve simple '
    'connectedness. The full written proof passed B, root, C and D; the final typeset source '
    'also passed root. Free cyclic quotients of Fermat surfaces, followed by the old cut, '
    'show that the new intrinsic class is proper in every characteristic after finite constants. '
    'The restricted Tate conjecture itself remains unresolved.')
rows['C.4']['attempts_and_limits']=(
    'The new exact formula identifies the first missing kernel as rad(b|R)/K0, and Saito\'s '
    'primitive criterion identifies the remaining geometric pairing. The rational primitive '
    'divisor image splits off by Hodge index. Under a separate all-surface Tate hypothesis, '
    'the remaining image lies in the transcendental summands. No nondegeneracy of that image '
    'is proved. This exact reformulation and conditional split are not counted as a strictly '
    'smaller universal gate. Positivity cannot be transported from an abstract abelian-motive '
    'isomorphism without identifying the geometric form.')
rows['C.6']['attempts_and_limits']=(
    'A complete conditional proof now derives monodromy-rank and unramified-flag independence '
    'for homogeneous algebraic homological projectors from the published finite-field '
    'homological-equivalence/rank-independence conjecture. No Chow-idempotent lift is needed. '
    'The complete motivated-projector extension passed owner, root and independent C audits, using finite graph-rank constraints, '
    'whole-product Lefschetz operators and conjugate semistable alterations. The operator lemmas '
    'have complete proofs and exact checks; all auxiliary abelian strata also give a special unconditional criterion. No unconditional general assertion or converse to '
    'the named finite-field conjecture has been established, so these sufficient implications '
    'are not counted as a new smaller universal gate.')
movement=[
    'B.3: the universal surface-Tate test class is now restricted further to geometrically '
    'simply connected surfaces, while retaining H1(O)=0, very ample canonical bundle and '
    'all previously bundled numerical conditions. The fixed-field reduction and properness '
    'of the intrinsic subclass are fully proved in thm:B-simply-connected-surface-gate. '
    'This removes a geometric obstruction beyond the review02 gate; it does not prove Tate.'
]
excluded=[
    'The paired arithmetic-corank example is a complete explicit refutation of rank-only determination, but leaves the universal finite-field Tate gate unchanged.',
    'The B1 surface-support and uniruled-threefold results are solved classes, not a closure or smaller proved universal Chow gate.',
    'The C4 exact pairing kernel and rational divisor split clarify the same remaining obstruction; neither proves the residual nondegeneracy.',
    'The C6 finite-field rank implication and the motivated-operator work are sufficient conditional results, not an exact named equivalence or an unconditional general solution.',
    'Inherited numerical cut refinements, exact finite operator checks, source corrections, further audits, integration, typesetting and checkpoint packaging are not separate movement.'
]
proof=root/'sections/b3_simply_connected_surface_gate.tex'
assert proof.exists() and '\\label{thm:B-simply-connected-surface-gate}' in proof.read_text()
record=dict(review=3,scheduled_at=due.isoformat(),reviewed_at=now.isoformat(),
    movement=True,consecutive_reviews_without_movement=0,comparison_review=2,
    movement_evidence=movement,not_counted_as_movement=excluded,all_item_rows=items,
    open_mathematical_rows=rows,
    main_A_status=previous['main_A_status'],main_D_status=previous['main_D_status'],
    B2_scope_note=previous['B2_scope_note'],
    editorial_rows={k:by_item[k] for k in ['E.1','E.2']},
    next_formal_review='2026-11-19T08:50:00+00:00',
    next_checkpoint='2026-11-19T08:05:00+00:00',stop_rule=previous['stop_rule'])
target.write_text(json.dumps(record,indent=2,ensure_ascii=False)+'\n')
lines=[f'\n## Formal hourly review03 — {now:%Y-%m-%d %H:%M:%S} UTC\n',
    'One qualifying strict main-gate reduction occurred after review02. Consecutive formal reviews without movement: **0**. The programme remains **INCOMPLETE**. The next review is due08:50UTC and the next checkpoint08:05UTC.\n',
    'All44 item rows are snapshotted in `progress/review_03.json`. Every mathematically open row follows.\n',
    '| Open row | Current gate / smallest instance | Attempts and exact limit |',
    '|---|---|---|']
for item,r in rows.items():
    lines.append('| '+item+' | '+r['current_gate'].replace('|','\\|')+' | '+r['attempts_and_limits'].replace('|','\\|')+' |')
lines+=['\nMovement counted:\n']+['- '+x for x in movement]
lines+=['\nWork excluded from the movement count:\n']+['- '+x for x in excluded]
lines+=['\nNo original universal open row is declared solved. Work continues under the stopping rule.\n']
p=root/'PROGRESS_LEDGER.md'; p.write_text(p.read_text()+'\n'.join(lines))
p=root/'RESEARCH_SA05_report.md';p.write_text(p.read_text()+
    f'\n## Scheduled progress review03\n\nThe third formal review took place at{now:%H:%M:%S}UTC. '
    'It counts one strict intrinsic reduction: the surface-Tate gate now requires only geometrically '
    'simply connected surfaces, with the previous coherent and canonical conditions retained. '
    'The complete proof and the strictness construction are recorded under '
    '`thm:B-simply-connected-surface-gate`. The no-movement count remains0. '
    'The eight universal mathematical rows remain open, and the conditional monodromy work '
    'is not counted as a named equivalence or as a general solution.\n')
result=dict(review=3,reviewed_at=now.isoformat(),all_items=len(items),
    open_mathematical_rows=len(rows),movement=True,consecutive_without_movement=0,
    seconds=round(time.perf_counter()-start,6))
(root/'code/third_progress_review_output.json').write_text(json.dumps(result,indent=2)+'\n')
print(json.dumps(result,indent=2))
