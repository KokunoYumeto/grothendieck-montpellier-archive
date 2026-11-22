"""Merge branch check records while preserving reviewer and locator provenance.

The central ledger is not a count of independent reviews: two branches may
record the same communicated review in different words. This script removes
identical rows, repairs date/locator normalization of previously imported
records, and keeps each branch's actual event type and outcome.
"""
from pathlib import Path
import csv
import re

ROOT = Path(__file__).resolve().parents[1]
FIELDS = ['statement_id', 'date_utc', 'who', 'model', 'effort', 'run',
          'type', 'outcome', 'locator']


def locator(raw, branch):
    result = []
    for item in raw.split(';'):
        item = item.strip()
        candidate = item
        suffix = ''
        match = re.match(r'([^\s]+\.(?:tex|md|tsv|py|json(?:\.gz)?|pdf))(.*)$', item)
        if match:
            candidate, suffix = match.groups()
        for base in (ROOT, branch):
            path = (base / candidate).resolve()
            if path.exists() and path.is_relative_to(ROOT):
                item = str(path.relative_to(ROOT)) + suffix
                break
        result.append(item)
    return ';'.join(result)


def key(row):
    return tuple(row[x] for x in FIELDS if x not in ('date_utc', 'locator'))


def main():
    target = ROOT / 'CHECK_EVENTS.tsv'
    with target.open() as f:
        rows = list(csv.DictReader(f, delimiter='\t'))
    canonical = []
    for name in ('kronecker', 'plethysm'):
        branch = ROOT / 'branches' / name
        with (branch / 'CHECK_EVENTS.tsv').open() as f:
            for source in csv.DictReader(f, delimiter='\t'):
                row = {field: source.get(field, '') for field in FIELDS}
                row['date_utc'] = source.get('date_utc') or source.get('date', '')
                row['locator'] = locator(source['locator'], branch)
                canonical.append(row)
    branch = ROOT / 'branches/nonstandard'
    with (branch / 'CHECK_EVENTS.tsv').open() as f:
        for source in csv.DictReader(f, delimiter='\t'):
            typ = source['Event_type']
            who = '/root/nonstandard'
            if 'root' in typ.lower():
                who = '/root'
            elif 'plethysm' in typ.lower():
                who = '/root/plethysm_proof'
            row = dict(zip(FIELDS, (
                source['Finding_ID'], source['Date_UTC'], who,
                'GPT-6 Astra Pro', 'not exposed', 'GCT_POS', typ,
                f"Imported branch record {source['Event_ID']}: {source['Outcome']}; {source['Scope_and_limit']}",
                locator(source['Evidence'], branch))))
            canonical.append(row)
    replacements = {key(row): row for row in canonical}
    repaired = 0
    for i, row in enumerate(rows):
        replacement = replacements.get(key(row))
        if replacement is not None and row != replacement:
            rows[i] = replacement
            repaired += 1
    existing = {tuple(row[field] for field in FIELDS) for row in rows}
    added = 0
    for row in canonical:
        value = tuple(row[field] for field in FIELDS)
        if value not in existing:
            rows.append(row)
            existing.add(value)
            added += 1
    unique = []
    seen = set()
    for row in rows:
        assert all(row.get(field) is not None for field in FIELDS)
        assert row['date_utc'], row
        value = tuple(row[field] for field in FIELDS)
        if value not in seen:
            unique.append(row)
            seen.add(value)
    with target.open('w', newline='') as f:
        writer = csv.DictWriter(f, fieldnames=FIELDS, delimiter='\t', lineterminator='\n')
        writer.writeheader()
        writer.writerows(unique)
    print({'rows': len(unique), 'added': added, 'date_or_locator_repairs': repaired,
           'identical_duplicates_removed': len(rows)-len(unique)})


if __name__ == '__main__':
    main()
