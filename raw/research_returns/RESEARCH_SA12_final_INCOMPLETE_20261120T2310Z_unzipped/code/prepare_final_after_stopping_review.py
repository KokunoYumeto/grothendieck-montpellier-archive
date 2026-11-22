"""Stage final scope only after the actual two-review stopping condition."""
from pathlib import Path
from datetime import datetime, timezone
import csv
import hashlib
import json
import re

root = Path(__file__).resolve().parents[1]
reviews = [(int(m.group(1)), p) for p in (root / 'code/output').glob('formal_review*.json')
           if (m := re.fullmatch(r'formal_review(\d+)\.json', p.name))]
number, path = max(reviews)
review = json.loads(path.read_text())
prior = json.loads((root / f'code/output/formal_review{number - 1}.json').read_text())
assert review['stopping_condition_met'] and review['consecutive_no_movement_reviews'] >= 2
assert prior['consecutive_no_movement_reviews'] >= 1
assert not review['movement'] and not prior['movement']
assert not review['requested_status_changes'] and not review['strict_main_gate_reductions']
stopped = json.loads((root / 'code/output/research_stopped.json').read_text())
assert stopped['formal_review_number'] == number and stopped['all_research_agents_stopped'] is True
qa = json.loads((root / 'qa/pdf_verified.json').read_text())
assert hashlib.sha256((root / 'build/RESEARCH_SA12_paper.pdf').read_bytes()).hexdigest() == qa['sha256']
freeze = json.loads((root / 'code/output/checkpoint30_source_freeze.json').read_text())
for rel, digest in freeze['files'].items():
    assert hashlib.sha256((root / rel).read_bytes()).hexdigest() == digest, rel
with (root / 'RESEARCH_SA12_results.csv').open() as f:
    rows = list(csv.DictReader(f))
with (root / 'CHECK_EVENTS.tsv').open() as f:
    events = list(csv.DictReader(f, delimiter='\t'))
table = (root / 'RESEARCH_SA12_report.md').read_text().split('## Outcome table\n', 1)[1].split('\n## ', 1)[0]
requested = [s for s in table.splitlines() if s.startswith('| ') and not s.startswith('| Item |')]
assert len(requested) == 57
open_items = [s.split('|')[1].strip() for s in requested if 'Incomplete' in s.split('|')[2]]
assert open_items == ['D.1', 'D.2(ii)', 'L8'], open_items
now = datetime.now(timezone.utc).isoformat()
scope = '\n'.join([
    'INCOMPLETE', '', '# Final research scope and stopping record', '',
    f'Research stopped after formal review{number}, scheduled for {review["scheduled_utc"]} and recorded at {review["actual_utc"]}. '
    f'Reviews{number - 1} and{number} both had no requested-outcome status change and no strictly smaller strongest main gate. '
    'The required two-consecutive-review stopping condition was therefore met. No request to continue is being made.', '',
    '## Deliverable and status', '',
    f'The final manuscript has {qa["pages"]} pages, {len(rows)} statement rows, {len(events)} recorded check events and57 requested outcome rows. '
    'The exact distinctions between proved, refuted, known, qualified and incomplete outcomes remain in RESEARCH_SA12_report.md and RESEARCH_SA12_results.csv. '
    'Only general D.1, general D.2(ii), and residual dependent L8 remain requested open outcomes. '
    'The many restricted generation and representation-count theorems do not imply these general conclusions.', '',
    '## Strongest remaining gates', '',
    *[f'{i}. {gate}' for i, gate in enumerate(review['remaining_strongest_gates'], 1)], '',
    '## Last audited additions and explicit correction', '',
    'The final integrated auxiliary packet constructs a generating root-stack anchor of rank equal to the geometric period, '
    'proves exceptional infinitesimal Picard rigidity and class openness for already effective unit families, and realizes '
    'unbounded geometric Brauer periods through explicit nilpotent Heisenberg images on one fixed elliptic-cone puncture. '
    'These results do not supply the missing uniform quantitative object atlas or a counting counterexample.', '',
    'A substantive error in the earlier A-chain finite-jet wording was corrected: a preassigned coordinate w can vanish on an endpoint branch. '
    'The theorem now defines intrinsic maximal-ideal jets and proves an adapted standard coordinate choice in every characteristic. '
    'All four exact correction audits pass. The numerical bounds and actual Artinian companion remain valid. '
    'The complete original source, counterexample, exact five-block correction, audited candidate, status delta and all historical audits are retained. '
    'Eight correction events were added for two existing labels; this was not counted as main movement.', '',
    'Subsequent conditional generation, semisimple-head, exact generator-count, root-bridge, canonical-overorder, toric-chain and weighted SNC-refinement investigations remain separate unpromoted research notes. '
    'Their hypotheses and missing global/pole compatibility are explicit. Neither computational certificates nor these diagnostics '
    'replace a proof of a requested open outcome.', '',
    '## Verification and provenance', '',
    f'Final LuaLaTeX build: {qa["build"]}. PDF SHA-256: {qa["sha256"]}. '
    f'Warnings, undefined references/citations and missing characters: zero. Maximum overflow: {qa["maximum_overfull_after_pt"]}pt. '
    'The final corrected PDF was actually inspected through five contact sheets covering39 selected pages and14 enlarged full-page views. '
    'Every new proof, the corrected chain block and its Artinian companion, updated contents/scope, and the relevant bibliography entries were covered. '
    'All earlier images and exact source/QA records remain available.', '',
    f'The latest scheduled archive was checkpoint{review["latest_created_and_verified_checkpoint"]}; '
    f'the latest confirmed saved scheduled archive was checkpoint{review["latest_confirmed_persistently_saved_checkpoint"]}. '
    'The final ZIP is a separate immutable archive after stopping. Supplied original inputs and previous ZIP archives are excluded. '
    'Earlier missed-slot and unknown-save records remain explicit; no late checkpoint or unverified save is represented as completed.', '',
    f'Final scope staged at {now}. The exact stopping assessment is {path.relative_to(root)}.', ''
])
out = root / 'FINAL_SCOPE.md'
assert not out.exists()
out.write_text(scope)
with (root / 'PROGRESS_LEDGER.md').open('a') as f:
    f.write('\n\n## Final stopping scope\n\nINCOMPLETE. ' + now + '. Research stopped under the two-consecutive-review rule. '
            'Only final packaging, verification and delivery remain. General D.1, general D.2(ii) and dependent residual L8 are open.\n')
record = dict(utc=now, stopping_review=number, requested_outcome_rows=57, requested_open=open_items,
              statement_rows=len(rows), check_events=len(events), pdf=qa,
              scope_sha256=hashlib.sha256(out.read_bytes()).hexdigest(), archive_created=False)
(root / 'code/output/final_preparation.json').write_text(json.dumps(record, indent=2) + '\n')
print(json.dumps({k: v for k, v in record.items() if k != 'pdf'}))
