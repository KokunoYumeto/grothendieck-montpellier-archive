"""Repair generated root locators from actual Codex physical scan sections.

Usage: python SA05/work/root/repair_codex_locators.py items|tables|all

Only root items.json's `lines`, readings.tsv's `line`, and links.tsv's
`from`/`to` are changed. Source files, Pro/B12 locators, reading judgments,
author scripts, claims and consolidated top-level files are never edited.
Whole Codex scan sections deliberately replace unreliable narrow offsets.
"""
from __future__ import annotations

import argparse
import copy
import csv
import hashlib
import io
import json
from pathlib import Path
import re

HERE = Path(__file__).resolve().parent
WORKSPACE = next(p for p in HERE.parents if (p/'sources/texts/codex').is_dir())
SOURCES = WORKSPACE/'sources/texts/codex'
OUT = HERE/'outputs'
TAG = 'Codex physical scan sections:'
TAG_RE = re.compile(r'\s*;?\s*\[' + re.escape(TAG) + r'[^\]]*\]')
# These are locator fields, not mathematical prose. The old references occur
# as semicolon-delimited suffixes, or as K12-05(143–164) in one link endpoint.
OLD_REF_RE = re.compile(
    r'(?:\s+and\s+)?(?:Codex\s+)?K12-\d{2}(?:_transcription\.tex)?'
    r'(?:\s*\([^)]*\)|[^;)]*)'
)
SCAN_EXPR = re.compile(r'(\d{1,3})(?:\s*[–—-]\s*(\d{1,3}))?')
ENDPOINT_SCAN = re.compile(
    r'(?<!\d)12\s*/\s*'
    r'(\d{1,3}(?:\s*[–—-]\s*\d{1,3})?'
    r'(?:\s*,\s*\d{1,3}(?:\s*[–—-]\s*\d{1,3})?)*)'
)
PROTECTED_LOCATOR = re.compile(
    r'((?:Pro\s*(?:(?:early|middle|late)(?:\s*notes)?)?|B12-\d{2}))'
    r'\s*\(?(\d+(?:\s*[–—,\-]\s*\d+)*)'
)


def physical_lines(path: Path):
    text = path.read_text(encoding='utf-8')
    lines = text.split('\n')
    if lines and lines[-1] == '':
        lines.pop()
    return lines


def sections(path: Path):
    lines = physical_lines(path)
    markers = []
    for no, line in enumerate(lines, 1):
        m = re.match(r'^\s*\\scanpage\{(\d+)\}', line)
        if m:
            markers.append((int(m.group(1)), no))
    result = []
    for i, (scan, first) in enumerate(markers):
        last = markers[i+1][1]-1 if i+1 < len(markers) else len(lines)
        result.append(dict(alias=path.name.split('_')[0],
                           path=str(path.relative_to(WORKSPACE)),
                           scan=scan, start_line=first, end_line=last))
    return result


def scan_numbers(expr):
    out = set()
    for m in SCAN_EXPR.finditer(expr):
        first, last = int(m.group(1)), int(m.group(2) or m.group(1))
        if last < first:
            raise ValueError(f'Reversed scan range: {expr}')
        out.update(range(first, last+1))
    return sorted(out)


def endpoint_numbers(text):
    out = set()
    for m in ENDPOINT_SCAN.finditer(text):
        out.update(scan_numbers(m.group(1)))
    return sorted(out)


def remove_old_refs(text):
    text = TAG_RE.sub('', text)
    text = OLD_REF_RE.sub('', text)
    # Remove separators left by deleting a Codex-only clause. The content
    # of every remaining Pro/B12 clause is unchanged.
    text = re.sub(r';\s*(?=\))', '', text)
    text = re.sub(r';\s*;', ';', text)
    text = re.sub(r'\s+\)', ')', text)
    return text.strip().rstrip(';').rstrip()


def format_block(scans, index):
    available, missing = [], []
    for scan in sorted(set(scans)):
        if scan not in index:
            missing.append(scan)
        else:
            available.extend(index[scan])
    parts = [f"{s['alias']} scan{s['scan']:03d} physical lines"
             f"{s['start_line']}–{s['end_line']}" for s in available]
    if missing:
        parts.append('no K12-series section for scan(s) '
                     + ','.join(f'{s:03d}' for s in missing)
                     + '; any B12 locator is retained separately')
    return '['+TAG+' '+' | '.join(parts)+']', available, missing


def repair(text, scans, index):
    if not scans:
        if re.search(r'K12-\d{2}', text):
            raise ValueError('K12 locator without a declared physical scan: '+text)
        return text, [], []
    retained = remove_old_refs(text)
    block, available, missing = format_block(scans, index)
    after = retained+('; ' if retained else '')+block
    # Idempotence is a required property for the generator pipeline.
    assert remove_old_refs(after) == retained
    # Parentheses around the surrounding endpoint can become adjacent when
    # a Codex clause is removed; the protected alias and line numbers cannot.
    assert PROTECTED_LOCATOR.findall(text) == PROTECTED_LOCATOR.findall(after)
    return after, available, missing


def dump(path, obj):
    path.parent.mkdir(parents=True, exist_ok=True)
    tmp = path.with_suffix(path.suffix+'.tmp')
    tmp.write_text(json.dumps(obj, ensure_ascii=False, indent=2)+'\n', encoding='utf-8')
    tmp.replace(path)


def dump_tsv(path, rows, fields):
    buff = io.StringIO()
    writer = csv.DictWriter(buff, fieldnames=fields, delimiter='\t', lineterminator='\n')
    writer.writeheader()
    writer.writerows(rows)
    tmp = path.with_suffix(path.suffix+'.tmp')
    tmp.write_text(buff.getvalue(), encoding='utf-8')
    tmp.replace(path)


def load_tsv(path):
    with path.open(encoding='utf-8', newline='') as f:
        reader = csv.DictReader(f, delimiter='\t')
        return reader.fieldnames, list(reader)


def audit(mode, rows, summary):
    packet = dict(mode=mode, scope='generated root locator fields only',
                  line_numbering='1-based physical file lines; section includes scan marker through line before next marker',
                  summary=summary, records=rows)
    initial = OUT/f'codex_locator_initial_{mode}.json'
    if not initial.exists():
        dump(initial, packet)
    dump(OUT/f'codex_locator_audit_{mode}.json', packet)
    flat = [dict(record=r['record'], field=r['field'],
                 scans=','.join(f'{s:03d}' for s in r['scans']),
                 before=r['before'], after=r['after'],
                 missing_k12=','.join(f'{s:03d}' for s in r['missing_k12']),
                 changed=r['before'] != r['after']) for r in rows]
    dump_tsv(OUT/f'codex_locator_audit_{mode}.tsv', flat,
             ['record','field','scans','before','after','missing_k12','changed'])
    text = json.dumps(summary, ensure_ascii=False, indent=2)+'\n'
    (OUT/f'repair_codex_locators_{mode}_run.txt').write_text(text, encoding='utf-8')
    print(text, end='')


def repair_items(index):
    path = HERE/'items.json'
    data = json.loads(path.read_text(encoding='utf-8'))
    rows = []
    inspected = []
    for item in data:
        m = re.fullmatch(r'SA05-(\d+)', item['id'])
        if not m or not 1 <= int(m.group(1)) <= 100:
            continue
        inspected.append(int(m.group(1)))
        original = copy.deepcopy(item)
        before = item['lines']
        if not isinstance(before, str):
            raise TypeError(f"Expected root string locator in {item['id']}")
        after, available, missing = repair(before, item['scans'], index)
        item['lines'] = after
        assert {k:v for k,v in item.items() if k != 'lines'} == {
            k:v for k,v in original.items() if k != 'lines'}
        rows.append(dict(record=item['id'], field='lines', scans=item['scans'],
                         before=before, after=after, sections=available, missing_k12=missing))
    assert sorted(inspected) == list(range(1,101)), 'Not all root items1–100 were available'
    dump(path, data)
    summary = dict(mode='items', inspected_items=len(rows),
                   changed=sum(r['before'] != r['after'] for r in rows),
                   records_with_absent_k12=[dict(record=r['record'], scans=r['missing_k12'])
                                            for r in rows if r['missing_k12']],
                   nonlocator_fields_unchanged=True)
    audit('items', rows, summary)


def repair_tables(index):
    rows = []
    rpath = HERE/'readings.tsv'
    rfields, readings = load_tsv(rpath)
    for no, row in enumerate(readings, 1):
        original = dict(row)
        if str(row['cote']) != '12':
            continue
        scans = scan_numbers(row['scan'])
        after, available, missing = repair(row['line'], scans, index)
        row['line'] = after
        assert {k:v for k,v in row.items() if k != 'line'} == {
            k:v for k,v in original.items() if k != 'line'}
        rows.append(dict(record=f'readings row{no}', field='line', scans=scans,
                         before=original['line'], after=after, sections=available, missing_k12=missing))
    dump_tsv(rpath, readings, rfields)
    lpath = HERE/'links.tsv'
    lfields, links = load_tsv(lpath)
    inspected_endpoints = 0
    for no, row in enumerate(links, 1):
        original = dict(row)
        for field in ['from','to']:
            inspected_endpoints += 1
            scans = endpoint_numbers(row[field])
            if not scans:
                if re.search(r'K12-\d{2}', row[field]):
                    raise ValueError(f'Unresolved Codex endpoint links row{no} {field}')
                continue
            after, available, missing = repair(row[field], scans, index)
            row[field] = after
            rows.append(dict(record=f'links row{no}', field=field, scans=scans,
                             before=original[field], after=after, sections=available, missing_k12=missing))
        assert {k:v for k,v in row.items() if k not in ('from','to')} == {
            k:v for k,v in original.items() if k not in ('from','to')}
    dump_tsv(lpath, links, lfields)
    summary = dict(mode='tables', inspected_reading_rows=len(readings),
                   inspected_link_endpoints=inspected_endpoints,
                   mapped_fields=len(rows), changed=sum(r['before'] != r['after'] for r in rows),
                   fields_with_absent_k12=[dict(record=r['record'],field=r['field'],scans=r['missing_k12'])
                                          for r in rows if r['missing_k12']],
                   all_reading_disagreements_and_nonlocator_fields_unchanged=True)
    audit('tables', rows, summary)


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('mode', choices=['items','tables','all'], nargs='?', default='all')
    args = parser.parse_args()
    OUT.mkdir(parents=True, exist_ok=True)
    aliases, index = {}, {}
    for path in sorted(SOURCES.glob('K12-*_transcription.tex')):
        found = sections(path)
        alias = path.name.split('_')[0]
        aliases[alias] = dict(path=str(path.relative_to(WORKSPACE)),
                              physical_lines=len(physical_lines(path)),
                              sha256=hashlib.sha256(path.read_bytes()).hexdigest(),
                              scan_sections=found)
        for s in found:
            index.setdefault(s['scan'], []).append(s)
    assert len(aliases) == 9
    assert index[51][0]['alias'] == 'K12-04' and index[51][0]['start_line'] == 2
    assert index[71][0]['alias'] == 'K12-05' and index[71][0]['start_line'] == 94
    for alias, path in {
        'Pro early':'sources/texts/pro/MPL_12_002-050_transcription.tex',
        'Pro middle':'sources/texts/pro/MPL_12_051-098_transcription.tex',
        'Pro late':'sources/texts/pro/MPL_12_099-149_transcription.tex',
        'Pro early notes':'sources/notes/pro/MPL_12_002-050_notes.md',
        'Pro middle notes':'sources/notes/pro/MPL_12_051-098_notes.md',
        'Pro late notes':'sources/notes/pro/MPL_12_099-149_notes.md',
    }.items():
        aliases[alias] = dict(path=path, locator_policy='Preserved; not repaired by this script')
    for path in sorted(SOURCES.glob('B12-*_transcription.tex')):
        aliases[path.name.split('_')[0]] = dict(
            path=str(path.relative_to(WORKSPACE)), physical_lines=len(physical_lines(path)),
            scan_sections=sections(path), locator_policy='Preserved; different archival labels may be intentional')
    dump(HERE/'source_guide_aliases.json', dict(
        line_numbering='Physical 1-based file lines, not scan numbering, printed pagination, or content-relative offsets.',
        section_policy='Each range starts at its actual scanpage marker and ends immediately before the next scanpage marker, or at EOF.',
        warning='Missing in the K12 series does not mean absent from B12; B12 locators and documentary disagreements are preserved.',
        aliases=aliases, scan_to_k12_sections={f'{k:03d}':v for k,v in sorted(index.items())}))
    if args.mode in ('items','all'):
        repair_items(index)
    if args.mode in ('tables','all'):
        repair_tables(index)


if __name__ == '__main__':
    main()
