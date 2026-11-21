"""Compare independent visual readings with their localized first and final page excerpts.
Run from any directory with Python 3. Sources and coordinates are relative to this file.
Whitespace and alternative TeX spellings of the same glyph are normalised. Uncertainty
uses the first candidate. The full literal excerpts are preserved in blind_locations.tsv.
"""
import csv, re
from pathlib import Path
D = Path(__file__).resolve().parent
K = 'K157-5-34'
def rows(s):
    with (D/(K+s)).open(encoding='utf-8', newline='') as f:
        return list(csv.DictReader(f, delimiter='\t'))
def first(s):
    pattern=re.compile(r'\\unsure\{')
    while (hit:=pattern.search(s)):
        p=hit.end()
        depth=1
        while p<len(s) and depth:
            if s[p] in '{}' and s[p-1]!='\\':
                depth += 1 if s[p]=='{' else -1
            p+=1
        if depth: raise ValueError('unclosed doubt')
        s=s[:hit.start()]+s[hit.end():p-1].split('|',1)[0]+s[p:]
    return s
def canon(s):
    s=first(s)
    for a,b in [('∀',r'\forall'),('∃',r'\exists'),('°',r'^\circ'),('’',"'"),(r'\textquotedblleft','“'),(r'\textquotedblright','”')]:
        s=s.replace(a,b)
    s=re.sub(r'\\(?:bigl|bigr|Bigl|Bigr|left|right|limits)(?![a-zA-Z])','',s)
    for a,b in [(r'\operatorname',r'\mathrm'),(r'\longrightarrow',r'\to'),(r'\rightarrow',r'\to'),(r'\longmapsto',r'\mapsto'),(r'\longleftarrow',r'\leftarrow'),(r'\geq',r'\ge'),(r'\leq',r'\le'),(r'\mid','|'),(r'\bar ',r'\overline ')]:
        s=s.replace(a,b)
    # Remove only neutral wrappers. The text or symbols inside a cancellation are retained.
    wrapper=re.compile(r'\\(?:deleted|inserted|margin|uline|mathrm|text|mathop|mathrel|mathord)\{')
    while (m:=wrapper.search(s)):
        end=m.end();depth=1
        while end<len(s) and depth:
            if s[end] in '{}' and s[end-1]!='\\':depth+=(s[end]=='{')-(s[end]=='}')
            end+=1
        if depth:break  # a located excerpt may cut through a wrapper
        s=s[:m.start()]+s[m.end():end-1]+s[end:]
    s=s.replace(r'\[','').replace(r'\]','').replace('$','')
    s=re.sub(r'\\(?:qquad|quad|,|;|!| )','',s)
    s=re.sub(r'\\(begin|end)\{aligned\}','',s)
    s=s.replace('\\\\','').replace('&','')
    # Equivalent grouping around a single character or control sequence.
    for _ in range(3):
        s=re.sub(r'\{(\\[A-Za-z]+|[A-Za-z0-9?=<>])\}',r'\1',s)
    return ''.join(s.split()).replace('{}','')
def esc(s):return '<code>'+s.replace('&','&amp;').replace('<','&lt;').replace('>','&gt;').replace('|','&#124;').replace('\n',' ')+'</code>'
def main():
    independent = rows('_blind.tsv')
    blind = {(r['scan'], r['place']): r['what_the_crop_shows'] for r in independent}
    if len(independent) != len(blind):
        raise ValueError('Duplicate place in the blind register')
    pages = {n: (D/'pages'/f'{K}_157-5_scan{n}.tex').read_text(encoding='utf-8')
             for n in {r['scan'] for r in independent}}
    per_page = {}
    decisions, editorial = [], []
    seen = set()
    for row in rows('_blind_locations.tsv'):
        scan, place = row['scan'], row['place']
        key = scan, place
        if key in seen:
            raise ValueError(f'Duplicate reference to {key}')
        seen.add(key)
        page = pages[scan]
        start, end = int(row['start']), int(row['end'])
        if not 0 <= start <= end <= len(page) or (
            page[max(0, start-24):start] != row['left'] or page[end:end+24] != row['right']
        ):
            raise ValueError(f'Page moved at {key}')
        recorded, before, after = blind[key], row['first_pass'], page[start:end]
        reading = canon(recorded)
        differs_before, differs_after = canon(before) != reading, canon(after) != reading
        different = differs_before or differs_after
        counts = per_page.setdefault(scan, [0, 0, 0, 0])
        for index, increment in enumerate([1, differs_before, differs_after, different]):
            counts[index] += increment
        if not different and recorded == before == after:
            continue
        line = '| ' + ' | '.join([scan, place, esc(before), esc(recorded), esc(after),
                                  row['settlement'].replace('|', '&#124;')]) + ' |'
        (decisions if different else editorial).append(line)
    if seen != set(blind):
        raise ValueError('The blind and location registers cover different places')
    total, first_count, final_count, distinct = map(sum, zip(*per_page.values()))
    identical = total - distinct - len(editorial)
    lines = [
        '# Independent reading compared with page files', '',
        f'Of {total} locations, {first_count} differed from the first pass and {final_count} '
        f'from the final primary reading. These comparisons identify {distinct} distinct places. '
        f'At {len(editorial)} further places the wording or signs agree and the literal encodings '
        f'differ. The remaining {identical} entries agree character for character across all three readings.',
        '', '## Page index', '',
        'The table counts differences of wording, punctuation, indices, scope and diagram description. '
        'A doubtful reading is compared using its first candidate. The full alternatives and '
        'diplomatic marks appear in the two tables below. The blind register preserves the independent '
        'entries. The location register supplies exact first-pass excerpts and offsets in the final pages.',
        '', '| Scan | Locations compared | Different from first pass | Different from audited excerpt | Distinct locations with a primary difference |',
        '|---|---:|---:|---:|---:|'
    ]
    lines.extend('| ' + n + ' | ' + ' | '.join(map(str, counts)) + ' |'
                 for n, counts in per_page.items())
    header = ['| Scan | Place | First transcription | Blind | Audited | Resolution |',
              '|---|---|---|---|---|---|']
    lines.extend(['', '## Location-by-location decisions', '',
                  'Each row differs from the first transcription, the audited transcription, or both. '
                  'A decision may retain several candidates where the ink permits more than one.', ''])
    lines.extend(header + decisions)
    lines.extend(['', '## Matching primary readings with differences in markup or TeX spelling', '',
                  'These entries include differences in underlining, insertion or doubt marking, '
                  'mathematical typesetting, delimiters and spacing. The separate audit also records '
                  'the locations with identical literal readings.', ''])
    lines.extend(header + editorial)
    (D/(K+'_blind_compare.md')).write_text('\n'.join(lines)+'\n', encoding='utf-8')
    print(total, first_count, final_count, distinct, len(editorial), identical)
if __name__=='__main__':main()
