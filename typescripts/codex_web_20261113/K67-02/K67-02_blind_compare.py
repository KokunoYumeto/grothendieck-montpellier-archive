"""Compare the blind entries with first-pass text and recover their final TeX excerpts."""
from collections import defaultdict
import csv
from html import escape
from pathlib import Path

BASE = Path(__file__).resolve().parent


def rows(name):
    with (BASE / name).open(newline='') as source:
        return list(csv.DictReader(source, delimiter='\t'))


def code(fragment):
    return '<code>' + escape(fragment).replace('|', '&#124;').replace('\n', ' ') + '</code>'


def final_excerpt(before, after, changes, snippet):
    # Each disputed collation anchor is unique on the frozen page.
    assert before.count(snippet) == 1, snippet
    start = before.index(snippet)
    end = start + len(snippet)
    shift_before = shift_inside = 0
    for row in changes:
        pos = int(row['frozen_offset'])
        last = pos + len(row['frozen_tex'])
        delta = len(row['final_tex']) - len(row['frozen_tex'])
        if last <= start:
            shift_before += delta
        elif pos < end:
            assert start <= pos and last <= end, (snippet, row['id'])
            shift_inside += delta
    return after[start + shift_before:end + shift_before + shift_inside]


def main():
    blind = {(r['scan'], r['place']): r['what_the_crop_shows'] for r in rows('K67-02_blind.tsv')}
    collation = rows('K67-02_collation.tsv')
    assert set(blind) == {(r['scan'], r['place']) for r in collation}
    changes = defaultdict(list)
    if (BASE / 'K67-02_witness.tsv').exists():
        for row in rows('K67-02_witness.tsv'):
            changes[row['scan']].append(row)
    page_texts = {}
    for scan in sorted({r['scan'] for r in collation}):
        final = (BASE / 'pages' / f'K67-02_67_scan{scan}.tex').read_text()
        frozen = final
        for row in reversed(changes[scan]):
            at = int(row['final_offset'])
            end = at + len(row['final_tex'])
            assert frozen[at:end] == row['final_tex'], row['id']
            frozen = frozen[:at] + row['frozen_tex'] + frozen[end:]
        page_texts[scan] = frozen, final

    disagreements = []
    for row in collation:
        if row['first_pass_tex'] == row['blind_in_same_tex_notation']:
            continue
        scan, place = row['scan'], row['place']
        frozen, final = page_texts[scan]
        excerpt = final_excerpt(frozen, final, changes[scan], row['settled_tex'])
        disagreements.append('| ' + ' | '.join([
            scan, place, code(row['first_pass_tex']), code(blind[scan, place]),
            row['settlement'].replace('|', '&#124;'), code(excerpt)
        ]) + ' |')

    report = ['# Blind comparison', '',
              f'{len(collation)} places compared. {len(disagreements)} disagreements with the first-pass pages.',
              '', '| Scan | Place | First page file | Independent blind reading | Decision on the crop at audit | Final page excerpt after the witness check |',
              '| --- | --- | --- | --- | --- | --- |', *disagreements, '',
              f'The collation TSV preserves the exact first-pass and audited text at all {len(collation)} places. The witness TSV records later decisions at individual doubt marks.']
    (BASE / 'K67-02_blind_compare.md').write_text('\n'.join(report) + '\n')
    print(f'{len(collation)} loci compared. {len(disagreements)} blind disagreements located in the final pages.')


if __name__ == '__main__':
    main()

