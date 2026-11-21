"""Merge actual per-agent events without upgrading the type of a check."""
from pathlib import Path
import csv

ROOT = Path(__file__).resolve().parents[2]
OUT = ROOT / 'deliverables/CHECK_EVENTS.tsv'
HEADER = ['statement_id','date_utc','who_model_effort_run','type','outcome','locator_or_method']
TYPE_MAP = {
    'targeted whole-proof check':'targeted proof check',
    'targeted conceptual check':'targeted proof check',
    'targeted independent proof check':'targeted proof check',
    'independent proof check':'targeted proof check',
    'independent whole-proof check':'targeted proof check',
    'targeted consistency check':'targeted proof check',
    'targeted whole-proof and implementation check':'targeted proof check',
    'executed exact symbolic check':'computation or formal certificate',
    'independent review reported':'carried as background without fault found',
}
ALLOWED = {
    'targeted proof check','independent re-proof','computation or formal certificate',
    'used and rechecked in this run','carried as background without fault found',
    "refuted, with the refined statement's id",
}
sources = [OUT, *sorted(ROOT.glob('work/*/CHECK_EVENTS*.tsv'))]
events = {}
for path in sources:
    with path.open(newline='') as f:
        for item in csv.DictReader(f, delimiter='\t'):
            old_type = item['type']
            event_type = TYPE_MAP.get(old_type, old_type)
            if event_type not in ALLOWED:
                raise ValueError((str(path), event_type))
            outcome = item['outcome']
            if old_type != event_type:
                outcome = '[' + old_type + '] ' + outcome
            row = {
                'statement_id':item['statement_id'],
                'date_utc':item['date_utc'],
                'who_model_effort_run':item.get('who_model_effort_run') or item.get('who',''),
                'type':event_type,
                'outcome':outcome,
                'locator_or_method':item.get('locator_or_method') or str(path.relative_to(ROOT)),
            }
            key = tuple(row[x] for x in HEADER[:5])
            events.setdefault(key, row)
rows = sorted(events.values(),key=lambda x:(x['date_utc'],x['statement_id'],x['who_model_effort_run']))
with OUT.open('w',newline='') as f:
    writer = csv.DictWriter(f, HEADER,delimiter='\t',lineterminator='\n')
    writer.writeheader();writer.writerows(rows)
print(f'Merged {len(rows)} recorded check events from {len(sources)} logs.')
