"""Write a dated working ledger from recorded checks, preserving milestone history."""
from pathlib import Path
from datetime import datetime, timezone
import csv

r = Path(__file__).resolve().parents[1]
now = datetime.now(timezone.utc).isoformat()
rows = list(csv.DictReader((r / 'STATEMENTS.tsv').open(), delimiter='\t'))
refuted = {5, 8, 10, 14, 15, 21}
lines = [
    '# H035 progress ledger', '',
    '**Main question: H035.30, Théorème 12 (94/016–017).**', '',
    'Characterize finite-module representability from the six manuscript axioms.',
    'Current gate: the complete proof is drafted, with the missing finiteness in',
    '5 bis supplied by (iv) and strict stationarity proved separately. Dependencies',
    'H035.1–21 have received second mathematical checks. The final independent',
    'pass through the central implication and applications is in progress.', '',
    'Start: 2026-11-19T02:54:34Z. One stream; no delegated workers.',
    f'Current ledger update: {now}.',
    'Mandatory three-hour review due 05:54:34 UTC, then hourly.',
    'The results attachment remains unopened.', '',
    '## Current item rows', '',
    '| Item | State | Current gate or checked result |',
    '|---|---|---|',
]
for row in rows:
    n = int(row['id'].split('.')[-1])
    if n <= 21:
        state = 'refuted; corrected version proved' if n in refuted else 'proved in the stated reconstruction'
        gate = 'Full proof in PROOFS.tex; second check in research/SECOND_CHECKS.md. ' + row['reconstruction']
    elif n == 39:
        state = 'open'
        gate = ('Only completion compatibility remains for the reconstructed affine composition claim. '
                'Filtered colimits, finite values, constructible rank and generic condition (vi) are proved; '
                'the dense-open upgrade handles reducible quotients. Need control of G(M) for finite '
                'modules over a completion, or direct continuity of F on the resulting inverse system.')
    elif n == 40:
        state = 'open — scope and final check'
        gate = ('The Ext/Tor and proper cohomology realizations have proofs; the two-scheme class is '
                'not defined on the page. An unqualified nonproper extension fails finite values. '
                'Separate the contextual proper examples from that extension and H035.39.')
    else:
        state = 'open — second check in progress'
        gate = 'Complete proof/counterexample drafted in PROOFS.tex. ' + row['reconstruction']
    lines.append(f"| {row['id']} | {state} | {gate.replace('|', '/')} |")
lines += ['', '## Supplied-note items', '',
          '| Item | State | Remaining work |', '|---|---|---|']
for n in range(1, 7):
    lines.append(f'| work:K94-01#{n} | open — all text read; mathematical claims checked through the relevant statement rows | Finish subclaim-by-subclaim NOTES_VERDICTS.tsv and the remaining disputed crops. |')
lines += [
    '', '## Dated milestones (not the mandatory hourly reviews)', '',
    '- 02:54:34 UTC: start; original statements and exact literature matches unverified.',
    '- 03:37 UTC: 46 statement rows assembled; first 15 proof sections drafted. '
    'The first generated inventory briefly mislabeled H035.11 as generic CM; it was '
    'corrected immediately to generic freeness of nilpotent graded pieces. Duplicate '
    'inventory output has been consolidated here; checkpoint 01 retains that earlier state.',
    '- 03:39:50 UTC: checkpoint 01 created and saved at the first 45-minute boundary.',
    '- 04:05 UTC: all 46 proof sections drafted; H035.39 explicitly remained a working state.',
    '- 04:13–04:19 UTC: second checks completed for H035.1–21; formal Ext argument '
    'expanded using the exact pro-system assertion in Stacks 02OB. EGA III 4.5.1 and '
    'Bourbaki IX §3 no.2 verified on rendered printed pages.',
    '- 04:19 UTC: H035.39 reduced strictly from completion plus a reducible-base '
    'generic-open issue to completion alone. No claim of completion closure is made.',
    '', '## Mandatory progress reviews', '',
    'None yet due. Movement is counted only as an open item changing status or a '
    'main gate becoming strictly smaller. Packaging and restatement do not count.', '',
]
(r / 'PROGRESS_LEDGER.md').write_text('\n'.join(lines))
print('Updated ledger at', now, 'with 46 statement rows and all six note entries.')
