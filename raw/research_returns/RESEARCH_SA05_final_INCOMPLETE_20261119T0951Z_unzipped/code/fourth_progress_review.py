"""Execute review04 at its scheduled time and preserve earlier snapshots."""
from pathlib import Path
from datetime import datetime, timezone
from copy import deepcopy
import csv
import json
import time

root=Path(__file__).resolve().parents[1]
start=time.perf_counter()
due=datetime(2026,11,19,8,50,tzinfo=timezone.utc)
now=datetime.now(timezone.utc).replace(microsecond=0)
if now<due:
    raise SystemExit('Review04 is not due until 08:50 UTC.')
target=root/'progress/review_04.json'
if target.exists():
    raise SystemExit('Review04 already exists and will not be overwritten.')
previous=json.loads((root/'progress/review_03.json').read_text())
with (root/'ITEM_STATUS.tsv').open(newline='') as handle:
    items=list(csv.DictReader(handle,delimiter='\t'))
by={r['item']:r for r in items}
rows=deepcopy(previous['open_mathematical_rows'])
for item in rows:
    rows[item]['recorded_status']=by[item]['status']
rows['B.1']['attempts_and_limits']=(
    'The surface-support and uniruled-threefold classes remain proved. Two new complete '
    'limit counterexamples show that continuous cohomology of the function field need not '
    'come from any fixed open, even rationally and on Frobenius invariants, and that a '
    'locally finite integral Frobenius module can acquire a non-root-of-unity eigenvalue '
    'after completion. Fixed finite-orbit direct sums are distinguished. These refute '
    'proposed shortcuts, not the universal cycle assertion; uniform ramification and the '
    'unramified residue kernel remain uncontrolled.')
rows['B.5']['attempts_and_limits']=(
    'The new finite-field coefficient-duality proposition proves an exact equivalence '
    'between perfect rational Weil pairings for every Chow-heart coefficient and '
    'Beilinson plus Parshin, already tested on P1 with constant coefficients. Its full '
    'proof includes the degree-one sign and the degree-three cross pairing. This is '
    'an additional necessary dependency for the stronger coefficient scope, not a '
    'solution for homogeneous pure coefficients or arithmetic f-admissibility. The '
    'March2026 prismatic/logarithm paper retains its global finite-generation hypotheses.')
rows['C.1(c)']['attempts_and_limits']=(
    'The finite all-power criterion without C+ and the explicit finite arity bounds '
    'remain proved; the actual Chow vanishings are not established. The formal '
    'Beauville–Voisin countermodel and the two withdrawn K3 preprints remain recorded. '
    'The current Awada–Bolognesi–Laterveer–Pedrini paper proves specified high-rank and '
    'family results; density does not reverse Chow specialization. No general '
    'transcendental exterior-projector vanishing follows.')
rows['C.4']['attempts_and_limits']=(
    'The target-only positivity proposition proves a sufficient package: standard '
    'positivity for the surface-square target and homological=numerical equivalence '
    'for the mixed threefold-surface product imply primitive-image nondegeneracy. '
    'The algebraic-Lefschetz-inverse alternative still needs a mixed surface product. '
    'Tate spanning over Q_l does not provide the rational correspondence image '
    'required for positivity. Rational Frobenius polynomials and semisimplicity '
    'do not repair that missing descent. These unproved product hypotheses leave '
    'the same residual pairing and sharp-endpoint gate open.')
rows['C.6']['attempts_and_limits']=(
    'The complete finite-field rank-conjecture implication for motivated motives '
    'remains a sufficient conditional theorem. The new finite-prime approximation '
    'proposition proves equivalence of universal number-field and p-adic pure-motive '
    'unramifiedness formulations, using Kisin local constancy and algebraic nearby '
    'points with the original completion. It removes a globalization obligation '
    'from an attempted converse, but not the missing pure local realization of '
    'an arbitrary cycle. The BGV square-zero encoding yields a compact analytic '
    'object only. The fully checked semistable blowup/cut construction cancels '
    'the prescribed cohomology. Consani represents monodromy of an existing '
    'degeneration; logarithmic Tate gives further conjectural sufficient routes. '
    'None supplies the requested exact named-conjecture converse.')
rows['Lead B1']['attempts_and_limits']=(
    'The finite-field extension-degree formula, continuity refutation and the new '
    'limit diagnostics are proved. They leave the same universal Chow gate and '
    'the independently stated arithmetic comparison package unresolved.')
rows['Lead C1']['attempts_and_limits']=(
    'The modified-diagonal identification and stated low-power results remain proved. '
    'The actual general-K3 determinant is unchanged by the current-family literature '
    'check or the already recorded formal countermodel.')
excluded=[
    'B1 limit counterexamples disprove methods; they do not close B1 or reduce its universal cycle gate.',
    'B5 all-Chow-heart duality is an exact dependency under a stronger coefficient scope, not a solution to the general prescribed rational realization.',
    'C4 target positivity gives additional sufficient unproved product assumptions, not nondegeneracy of the remaining geometric image.',
    'C6 local/global approximation is a transfer theorem for equivalent universal formulations. The pure-local cycle encoding and named-conjecture converse remain missing.',
    'Semistable blowup cancellation, current-source scope checks, individual classes, audits, integration and packaging are not qualifying movement.'
]
movement=[]
count=previous['consecutive_reviews_without_movement']+1
assert len(items)==44 and len(rows)==8
record=dict(review=4,scheduled_at=due.isoformat(),reviewed_at=now.isoformat(),
    movement=False,consecutive_reviews_without_movement=count,comparison_review=3,
    movement_evidence=movement,not_counted_as_movement=excluded,all_item_rows=items,
    open_mathematical_rows=rows,main_A_status=previous['main_A_status'],
    main_D_status=previous['main_D_status'],B2_scope_note=previous['B2_scope_note'],
    editorial_rows={k:by[k] for k in ['E.1','E.2']},
    next_formal_review='2026-11-19T09:50:00+00:00',
    next_checkpoint='2026-11-19T09:35:00+00:00',stop_rule=previous['stop_rule'])
target.write_text(json.dumps(record,indent=2,ensure_ascii=False)+'\n')
lines=[f'\n## Formal hourly review04 — {now:%Y-%m-%d %H:%M:%S} UTC\n',
    f'No qualifying mathematical movement occurred after review03. Consecutive formal reviews without movement: **{count}**. The programme remains **INCOMPLETE**. The next review is due 09:50 UTC; the next checkpoint after the present one is due 09:35 UTC.\n',
    'All 44 item rows are snapshotted in `progress/review_04.json`. Every mathematically open row follows.\n',
    '| Open row | Current gate / smallest instance | Attempts and exact limit |',
    '|---|---|---|']
for item,r in rows.items():
    lines.append('| '+item+' | '+r['current_gate'].replace('|','\\|')+' | '+r['attempts_and_limits'].replace('|','\\|')+' |')
lines+=['\nWork excluded from the movement count:\n']+['- '+x for x in excluded]
lines+=['\nThe stopping threshold has not been reached. Work continues until the next formal review, unless a qualifying result changes the ledger.\n']
path=root/'PROGRESS_LEDGER.md';path.write_text(path.read_text()+'\n'.join(lines))
path=root/'RESEARCH_SA05_report.md';path.write_text(path.read_text()+
    f'\n## Scheduled progress review04\n\nThe fourth formal review took place at {now:%H:%M:%S} UTC. '
    f'It records no qualifying movement and a no-movement count of {count}. '
    'All eight universal mathematical rows remain open. The complete B1 limit diagnostics, '
    'B5 coefficient-duality criterion, C4 sufficient positivity package and C6 transfer '
    'theorem are retained in their precise scopes, but none closes an original open row '
    'or proves a strictly smaller remaining universal gate. Work continues to the next '
    'scheduled review at 09:50 UTC.\n')
out=dict(review=4,reviewed_at=now.isoformat(),all_items=len(items),
         open_mathematical_rows=len(rows),movement=False,
         consecutive_without_movement=count,seconds=round(time.perf_counter()-start,6))
(root/'code/fourth_progress_review_output.json').write_text(json.dumps(out,indent=2)+'\n')
print(json.dumps(out,indent=2))
