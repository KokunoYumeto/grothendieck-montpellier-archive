from pathlib import Path
import re, json, csv

ROOT = Path('/workspace/scratch/f6dbb6638732')
FILES = {
    'I': ROOT/'background/transcriptions/MPL_15_195-228+18_002-017/MPL_15_195-228+18_002-017_notes.md',
    'II': ROOT/'background/transcriptions/MPL_18_018-062/MPL_18_018-062_notes.md',
}

def selected(pkg, ident):
    m = re.fullmatch(r'([A-Z]+)(\d+)(b?)', ident)
    if not m:
        return False
    prefix, digits, suffix = m.groups()
    n = int(digits)
    if pkg == 'I':
        return (prefix == 'P' and 1 <= n <= 33) or (prefix == 'M' and 1 <= n <= 11) or (prefix == 'B' and 1 <= n <= 5) or (prefix == 'X' and 1 <= n <= 3)
    return (prefix == 'C' and 1 <= n <= 8) or (prefix == 'RH' and 3 <= n <= 20) or (prefix == 'P' and 1 <= n <= 26) or (prefix == 'MB' and 1 <= n <= 16) or (prefix == 'SF' and (10 <= n <= 19 or n in (21,22) or 24 <= n <= 36))

entries = []
for pkg, file in FILES.items():
    text = file.read_text()
    heads = list(re.finditer(r'^### ([A-Z]+\d+b?) — (.*)$', text, re.M))
    for i, m in enumerate(heads):
        ident, title = m.groups()
        if not selected(pkg, ident):
            continue
        stop = heads[i+1].start() if i+1 < len(heads) else len(text)
        body = text[m.end():stop].strip()
        body = re.split(r'^## ', body, flags=re.M)[0].strip()
        witness = re.search(r'\*\*Witness:\*\*\s*(.*?)(?:\n|\. \*\*)', body)
        kind = re.search(r'\*\*Kind:\*\*\s*(.*?)(?:\n|\. \*\*)', body)
        entries.append(dict(note_id=f'{pkg}.{ident}', package=pkg, source_id=ident,
            title=title, witness=witness.group(1).strip() if witness else '',
            note_kind=kind.group(1).strip() if kind else '',
            source_file=str(file.relative_to(ROOT)),
            source_line=text[:m.start()].count('\n')+1, body=body))

text = FILES['I'].read_text()
start = text.index('### Cote 18\n', text.index('## Standing question I:'))
stop = text.index('## Standing question II:', start)
for line in text[start:stop].splitlines():
    if not line.startswith('| 18/'):
        continue
    cells = [c.strip() for c in line.strip('|').split('|')]
    # No literal pipes occur in the cote-18 table cells.
    assert len(cells) == 4, cells
    n = 1 + sum(e['package']=='I-Standing' for e in entries)
    entries.append(dict(note_id=f'I.ST{n:02d}', package='I-Standing', source_id=f'ST{n:02d}',
        title=cells[1], witness=cells[0], note_kind='author-marked standing step',
        source_file=str(FILES['I'].relative_to(ROOT)),
        source_line=text[:text.index(line,start)].count('\n')+1,
        body=cells[2]+' Linked observations: '+cells[3]))

expected = {'I':52, 'II':94, 'I-Standing':8}
for pkg, n in expected.items():
    assert sum(e['package']==pkg for e in entries) == n, (pkg,n)

out = ROOT/'work/audit_notes_source.json'
out.write_text(json.dumps(entries, indent=2, ensure_ascii=False)+'\n')
fields = ['note_id','package','source_id','title','witness','note_kind','source_file','source_line']
with (ROOT/'work/audit_notes_entries.csv').open('w',newline='') as f:
    w=csv.DictWriter(f,fieldnames=fields);w.writeheader()
    w.writerows({k:e[k] for k in fields} for e in entries)
print('Extracted',len(entries),'entries:',expected)
