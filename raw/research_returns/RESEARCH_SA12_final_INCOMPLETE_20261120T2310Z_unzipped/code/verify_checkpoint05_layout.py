"""Record completed human-model visual inspection of checkpoint 05 renderings."""
from pathlib import Path
from datetime import datetime, timezone
import csv
import hashlib
import json
import re

root = Path(__file__).resolve().parents[1]
render = json.loads((root / 'qa/checkpoint05_render.json').read_text())
pdf = root / 'build/RESEARCH_SA12_paper.pdf'
log = (root / 'build/RESEARCH_SA12_paper.log').read_text()
assert render['pdf_pages'] == 107
assert len(render['rendered_pages']) == 65
assert not re.search(r'Overfull|Warning|undefined|Missing character', log)
for number in range(1, 9):
    assert (root / f'qa/checkpoint05_contact_{number}.png').is_file()
old = root / 'qa/pdf_verified_checkpoint04.json'
if not old.exists():
    old.write_text((root / 'qa/pdf_verified.json').read_text())
now = datetime.now(timezone.utc)
record = {
    'utc': now.isoformat(), 'build': 'build_pass34',
    'pages': 107, 'sha256': hashlib.sha256(pdf.read_bytes()).hexdigest(),
    'overfull_before': 0, 'overfull_after': 0, 'warnings_after': 0,
    'undefined_citations_after': 0, 'undefined_references_after': 0,
    'missing_characters_after': 0,
    'rendered_and_inspected_pages': render['rendered_pages'],
    'visual_outcome': (
        'Root actually viewed all eight contact sheets, one per tool return, '
        'covering 65 pages of the final 107-page build. The sample includes '
        'all new arithmetic and all-model surface arguments, the R1 vanishing '
        'and threefold Picard counterexamples, smallness and group obstruction '
        'proofs, unresolved gates, and bibliography. No clipped, overlapping '
        'or out-of-margin text was observed. The final log has zero warnings, '
        'overfull boxes, unresolved citations/references or missing characters. '
        'The earlier truncated multi-image call was not counted as inspection.'
    )
}
(root / 'qa/pdf_verified.json').write_text(json.dumps(record, indent=2) + '\n')
events = root / 'parts/A/CHECK_EVENTS_A.tsv'
with events.open('a', newline='') as f:
    csv.writer(f, delimiter='\t').writerow([
        'A:strict-normalization-rigidity', now.strftime('%Y-%m-%d %H:%M UTC'),
        'GPT-6 Astra; inherited reasoning effort; /root',
        'used and rechecked in this run',
        'Opened EGA IV1 Chapitre 0 Proposition23.2.7 and Remarque23.2.8(iii), '
        'printed pp218–220. The global normalization-as-Krull-ring assertion '
        'is a remark, not a separately numbered theorem. Confirmed its '
        'nonfinite, possibly nonnoetherian normalization scope; the paper '
        'also cites the full Mori–Nagata proof in Huneke–Swanson Th4.10.5.'
    ])
ledger = root / 'PROGRESS_LEDGER.md'
ledger.write_text(ledger.read_text() + '\n\n## Scheduled checkpoint05: preparation completed '
    + now.strftime('%Y-%m-%d %H:%M UTC') + '\n\n'
    'The 107-page integrated paper has zero overfull boxes before and after '
    'the final revision, and no warnings, missing characters, or unresolved '
    'citations/references. All eight contact sheets, covering65 spread pages '
    'including every newly added proof section, were actually viewed. The '
    'current PDF hash is recorded and enforced by the checkpoint writer. '
    'The report remains INCOMPLETE; the A.2 and D.1/D.2(ii) requests and the '
    'additional weak B.2 upper-cone formulation remain active. The archive '
    'is due03:55 UTC, independently of formal review02 at04:10 UTC.\n')
print(json.dumps(record, indent=2))
