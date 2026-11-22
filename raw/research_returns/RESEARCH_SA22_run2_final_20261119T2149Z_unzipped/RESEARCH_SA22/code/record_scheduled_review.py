#!/usr/bin/env python3
"""Record a root-assessed scheduled review, without inferring mathematical movement.

The evidence note must be written after the actual substantive assessment.
This script enforces timing and preserves earlier reviews. It cannot decide
whether a theorem is proved or whether a source has actually been read.
"""
from pathlib import Path
from datetime import datetime, timezone, timedelta
import argparse
import hashlib
import json

parser = argparse.ArgumentParser()
parser.add_argument('--number', type=int, required=True)
parser.add_argument('--movement', choices=['yes', 'no'], required=True)
parser.add_argument('--open-rows', type=int, required=True)
parser.add_argument('--evidence', required=True)
parser.add_argument('--movement-evidence', action='append', default=[])
args = parser.parse_args()
root = Path(__file__).resolve().parents[1]
now = datetime.now(timezone.utc)
assert args.number >= 4, 'Earlier reviews already have their own preserved records.'
due = datetime(2026, 11, 19, 17, 39, tzinfo=timezone.utc) + timedelta(hours=args.number - 1)
assert now >= due, 'Review is not yet due; nothing written.'
target = root / f'logs/progress_review_{args.number:02d}.json'
assert not target.exists(), 'Review already recorded; refusing overwrite.'
previous_path = root / f'logs/progress_review_{args.number - 1:02d}.json'
previous = json.loads(previous_path.read_text())
evidence = (root / args.evidence).resolve()
assert evidence.is_relative_to(root)
assert evidence.exists() and evidence.stat().st_size > 100
movement = args.movement == 'yes'
assert not movement or args.movement_evidence, 'A YES review requires exact status-change evidence.'
assert movement or not args.movement_evidence, 'A NO review cannot claim movement evidence.'
stagnant = 0 if movement else previous['consecutive_stagnant_reviews'] + 1
stop = stagnant >= 2
ledger_path = root / 'PROGRESS_LEDGER.md'
ledger = ledger_path.read_text()
heading = f'## Formal movement review {args.number:02d}'
assert heading not in ledger, 'Review ledger heading already exists.'
record = {
    'review': args.number,
    'due_utc': due.isoformat(),
    'actual_utc': now.isoformat(),
    'baseline_review': args.number - 1,
    'baseline_actual_utc': previous['actual_utc'],
    'movement': movement,
    'consecutive_stagnant_reviews': stagnant,
    'open_rows': args.open_rows,
    'movement_evidence': args.movement_evidence,
    'assessment_note': str(evidence.relative_to(root)),
    'assessment_sha256': hashlib.sha256(evidence.read_bytes()).hexdigest(),
    'not_counted': [
        'new source readings that leave all open task gates unchanged',
        'independent verification without a status change',
        'scope wording and historical access-status corrections',
        'source-search failures, metadata and catalogue coverage',
        'program provenance, typesetting, register and package maintenance',
    ],
    'stop_required': stop,
    'next_review_utc': None if stop else (due + timedelta(hours=1)).isoformat(),
}
decision = 'YES' if movement else 'NO'
continuation = (
    'The user\'s rule now requires stopping the research phase: two consecutive '
    'scheduled reviews recorded no movement. We prepare the final INCOMPLETE '
    'package, retaining every unresolved obligation and all prior checkpoints. '
    'Necessary final typesetting, verification and persistent delivery are '
    'administrative completion of that instruction, not further research.'
    if stop else
    f'The work continues. The next formal review is due '
    f'{(due + timedelta(hours=1)).strftime("%H:%M")} UTC / '
    f'{(due + timedelta(hours=2)).strftime("%H:%M")} Europe/Berlin. '
    'No early final package is authorized by this review.'
)
entry = (
    f'\n\n{heading} — 19 November 2026, '
    f'{(now + timedelta(hours=1)).strftime("%H:%M")} Europe/Berlin\n\n'
    f'Actual review: {now.isoformat()}. Scheduled review: {due.isoformat()}. '
    f'Baseline: review {args.number - 1:02d} at {previous["actual_utc"]}.\n\n'
    f'**Movement: {decision}. Consecutive reviews without movement: {stagnant}. '
    f'Actual residual rows: {args.open_rows}.**\n\n'
    f'The dated assessment below is preserved independently at '
    f'`{evidence.relative_to(root)}`. Its SHA-256 is recorded in '
    f'`logs/progress_review_{args.number:02d}.json`.\n\n'
    + evidence.read_text().strip() + '\n\n### Review decision\n\n'
    + continuation + '\n'
)
ledger_path.write_text(ledger + entry)
target.write_text(json.dumps(record, indent=2) + '\n')
print(json.dumps(record, indent=2))
