"""Compare the independent crop readings with the TeX at the start of collation.
Run from any directory. Reading history reverses later edits in memory only.
"""
import csv
import re
from pathlib import Path

BASE = Path(__file__).resolve().parent
PREFIX = 'K64-09'
def table(name):
    with (BASE / f'{PREFIX}_{name}.tsv').open(newline='') as f:
        return list(csv.reader(f, delimiter='\t'))[1:]

def closed(s, start):
    depth = 1
    for j in range(start, len(s)):
        if s[j] in '{}' and (j == 0 or s[j-1] != '\\'):
            depth += (1 if s[j] == '{' else -1)
        if not depth:
            return j
    raise ValueError('open reading')

def plain(s):
    # The blind entries record visible strokes. Confidence and layout macros are editorial.
    while (m := re.search(r'\\(unsure|deleted|inserted|uline|uuline|mathrel|mathbin|operatorname|mathrm|text)\{',s)):
        j = closed(s,m.end())
        inside = s[m.end():j]
        if m[1] == 'unsure':
            inside = inside.split('|')[0]
        s = s[:m.start()] + inside + s[j+1:]
    for a,b in ((r'\smallsetminus',r'\setminus'),(r'\longrightarrow',r'\to'),(r'\rightarrow',r'\to'),
                (r'\longmapsto',r'\mapsto'),(r'\ne ',r'\neq '),(r'\le ',r'\leq '),(r'\ge ',r'\geq '),
                (r'\quad',''),(r'\qquad',''),(r'\,',''),(r'\;',''),(r'\!',''),(r'\ ',''),
                (r'\left',''),(r'\right',''),(r'\bigl',''),(r'\bigr',''),(r'\big',''),(r'\{','⦃'),(r'\}','⦄')):
        s = s.replace(a,b)
    return ''.join(s.split()).translate(str.maketrans('','','{}$&'))

def label_line(s):
    m = re.search(r'\\mspage\{(.*?)\}',s)
    labels = [m[1] or m[2] for m in re.finditer(r'\\tag\*\{(.*?)\}(?=\s*(?:\\\]|$))|^\s*(\(35\))(?=\\,)',s,re.M)]
    visible = []
    for label in labels:
        while (old := re.search(r'\\deleted\{',label)):
            j = closed(label,old.end())
            label = label[:old.start()]+label[j+1:]
        visible.append(label)
    labels = [x.replace(r'^{1}','¹').replace('^1','¹').replace('^','').replace('{','').replace('}','') for x in visible]
    number = re.search(r'archive sheet number:\s*(\d+)',s)
    return '{}; {}; {}'.format(m[1] if m else '—',' '.join(labels),number[1])

def run():
    cases = {(n,k):(p,d) for n,k,p,d in table('collation')}
    equivalences = {(n,k):a for n,k,a in table('alignment')} if (BASE/f'{PREFIX}_alignment.tsv').exists() else {}
    events = table('reading_history') if (BASE/f'{PREFIX}_reading_history.tsv').exists() else []
    pages = {f.stem[-3:]:f.read_text() for f in (BASE/'pages').glob('*.tex')}
    for n,offset,old,new in reversed(events):
        i=int(offset)
        if pages[n][i:i+len(new)] != new: raise ValueError(('edit history',n,offset))
        pages[n]=pages[n][:i]+old+pages[n][i+len(new):]
    issues=[]; count=0; missing=[]
    for n,k,b in table('blind'):
        count+=1; page=pages[n]
        first,decision=cases.get((n,k),(b,''))
        evidence=equivalences.get((n,k),first)
        if k=='folio and display labels':
            if plain(evidence)!=plain(label_line(page)):missing.append((n,k,label_line(page),evidence))
        else:
            for piece in evidence.split(' ⟐ '):
                if plain(piece) not in plain(page):missing.append((n,k,piece))
        if (n,k) in cases:issues.append((n,k,b,first,decision))
    def md(s):return s.replace('|',r'\|').replace('\n',' ')
    lines=['# Comparison of blind readings','',f'{count} independent entries. {len(issues)} differences at corresponding places. Equivalent TeX spacing, typesetting of operators, and editorial markup are excluded. The reading history reconstructs the first pass from the delivered pages. Alignment entries identify the corresponding TeX when a blind entry spans different lines or uses another typographic representation.','','| Scan | Place | Blind reading | First pass | Decision on the ink |','|---|---|---|---|---|']
    for number, place, blind, first, decision in issues:
        if place == 'old article' and number == '109':
            blind += ' (read as cancelled)'
            first += ' (read as live)'
        columns = [number,md(place),chr(96)+md(blind)+chr(96),chr(96)+md(first)+chr(96),md(decision)]
        lines.append('| '+' | '.join(columns)+' |')
    lines.extend(['', 'This table gives the audit decision at each disagreement. The final witness table in K64-09_doubts.md records subsequent changes at places that were still marked. Eight cancellations on scan 115 also have individual entries in the supplemental audit. Those entries were recorded after the witness check and are outside the independent count.'])
    if missing:
        lines+=['','## Unmatched text anchors','']+[repr(x) for x in missing]
    (BASE/f'{PREFIX}_blind_compare.md').write_text('\n'.join(lines)+'\n')
    print(f'{count} entries, {len(issues)} differences, {len(missing)} unmatched anchors')
    for x in missing: print(x)
    return not missing

if __name__=='__main__':
    raise SystemExit(0 if run() else 1)
