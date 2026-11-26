"""Compare independently recorded readings with their locations in the page files."""
import csv
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parent

def simplify(s):
    """Ignore TeX grouping and spacing; preserve letters, accents, alphabets and indices."""
    mark = re.compile(r'\\(unsure|inserted|deleted|uline|uuline|text|mathrm|operatorname)\{')
    while m := mark.search(s):
        depth, end = 1, m.end()
        while depth and end < len(s):
            if s[end] in '{}' and s[end-1] != '\\':
                depth += 1 if s[end] == '{' else -1
            end += 1
        val = s[m.end():end-1]
        if m[1] == 'unsure':
            val = val.split('|', 1)[0]
        s = s[:m.start()] + val + s[end:]
    s = s.replace('½','1/2').replace('’',"'").replace('−','-')
    s = re.sub(r'\\(?:qquad|quad|displaystyle|raggedright|,|!|;| )', '', s)
    return re.sub(r'[\s{}$]', '', s)

def tsv(name):
    with (ROOT/name).open(encoding='utf8',newline='') as f:
        return list(csv.DictReader(f, delimiter='\t'))

def focus(s, where):
    if not where: return s
    kind, index=where.split(':')
    if kind=='line': return (s.splitlines()+['']*int(index))[int(index)-1]
    matches=list(re.finditer(r'\\'+kind+r'\{',s))
    if int(index)>len(matches): return ''
    start=matches[int(index)-1].end()
    depth=1
    for end in range(start,len(s)):
        if s[end] in '{}' and s[end-1] != '\\':
            depth+=1 if s[end]=='{' else -1
            if not depth: return s[start:end]
    return ''

def hits(leaf, first_line, last_line, reading, where=''):
    lines = leaf.splitlines()
    return simplify(reading) in simplify(focus('\n'.join(lines[first_line-1:last_line]),where))

def table_row(cells):
    return '| ' + ' | '.join(c.replace('|', '\\|').replace('\n', ' ') for c in cells) + ' |'

def main():
    blind = {(r['scan'],r['place']):r['what the crop shows'] for r in tsv('K64-03_blind.tsv')}
    rows = tsv('K64-03_blind_alignment.tsv')
    lines = ['# Blind readings compared with the page files','',
             'The first comparison uses the transcription as it stood when the blind readings were written. '
             'The last column is recalculated from the numbered lines of the delivered page. '
             'Spacing, grouping and presentational wrappers are ignored. Repeated signs on the same line were also checked visually.','']
    differences = [r for r in rows if r['first comparison'] == 'differs']
    lines += [f'## The {len(differences)} differences and their decisions', '',
              f'{len(rows)} hard places were read from the crops before the second pass reopened the page files. '
              'This first table includes differences of lettering, pen state, arrow length, alignment and caption placement. '
              'The last column gives the corresponding entry in the witness table when the same place remained marked at the freeze.', '',
              '| Scan | Place | Blind reading | Decision on the crop | Subsequent witness decision |', '|---|---|---|---|---|']
    for r in differences:
        lines.append(table_row([r['scan'], r['place'], blind[r['scan'], r['place']], r['decision'],
                                r.get('subsequent witness decision') or '—']))
    lines += ['', '## Comparison by scan', '']
    for scan in dict.fromkeys(r['scan'] for r in rows):
        selected = [r for r in rows if r['scan']==scan]
        page = (ROOT/'pages'/('K64-03_64_scan%03d.tex'%int(scan))).read_text(encoding='utf8')
        lines += [f'### Scan {scan}','','| Place | Blind reading | First comparison | Decision on the crop | Blind reading found in final lines |','|---|---|---|---|---|']
        for r in selected:
            key=(scan,r['place'])
            v=blind[key]
            found=hits(page,int(r['from']),int(r['to']),v,r['scope'])
            cells=[r['place'],v,r['first comparison'],r['decision'],('yes' if found else 'no')+f" ({r['from']}–{r['to']})"]
            lines.append(table_row(cells))
        lines.append('')
    if len(rows) != len(blind): raise ValueError('Incomplete alignment')
    (ROOT/'K64-03_blind_compare.md').write_text('\n'.join(lines)+'\n',encoding='utf8')

if __name__ == '__main__':
    main()
