"""Reconstruct the first reading by undoing the recorded edits; compare blind snippets
to both versions. Run beside the page files or invoke this script from any directory."""
from pathlib import Path
import csv,re,sys,difflib
from unicodedata import normalize
root=Path(__file__).resolve().parent
def tab(name):
    f=root/name
    if not f.exists():return []
    with f.open(newline='') as h:return list(csv.DictReader(h,delimiter='\t'))
def flat(s):
    return ' '.join(s.split())
def canon(s):
    s=re.sub(r'(?m)^% archive sheet number: (\d+)[^\n]*',r' \1 ',s)
    s=re.sub(r'(?m)^%[^\n]*','',s)
    s=re.sub(r'\\(?:cotefile|scanpage)\{\d+\}','',s)
    for a,b in [('geq','ge'),('leq','le'),('prod','prod'),('Pi','prod'),('longrightarrow','to'),('rightarrow','to'),('Longrightarrow','Rightarrow'),('varinjlim','lim'),('mathrm',''),('operatorname',''),('underline',''),('uline',''),('textcircled',''),('text',''),('qquad',''),('quad',''),('unsure',''),('illegible',''),('inserted',''),('deleted',''),('handwritten',''),('mspage',''),('margin',''),('mathord',''),('tag*','')]:
        s=re.sub(r'\\'+re.escape(a)+r'(?![A-Za-z])',lambda m:b,s)
    s=re.sub(r'\\(?:begin|end)\{(?:aligned|tikzcd)\}','',s)
    s=s.replace('\\&','').replace('~','').replace(r'\,','').replace(r'\;','').replace(r'\!','')
    return ''.join(c for c in normalize('NFC',s) if c not in '{}$\\' and not c.isspace())
def nearby(needle,hay):
    if not needle:return ''
    m=difflib.SequenceMatcher(None,needle,hay,autojunk=False).find_longest_match()
    i=max(0,m.b-m.a);return hay[i:i+len(needle)]
def esc(x):return chr(96)+flat(x).replace('|',r'\|')+chr(96)
def versions():
    revisions = tab('K31-04_revisions.tsv')
    result = {}
    for file in (root / 'pages').glob('*.tex'):
        n = int(file.stem[-3:])
        edits = [r for r in revisions if int(r['scan']) == n]
        final = file.read_text()
        first = final
        for row in reversed(edits):
            i = int(row['offset'])
            before, after = row['before'], row['after']
            if not first.startswith(after, i):
                raise ValueError(f'{n:03} at offset {i}: revision mismatch')
            first = first[:i] + before + first[i + len(after):]
        result[n] = first, final, edits
    return result

def final_interval(start, end, edits):
    # Replay the actual changed runs inside each before/after pair. Unchanged
    # surrounding text in a revision must not enlarge the selected interval.
    for edit in edits:
        offset = int(edit['offset'])
        matcher = difflib.SequenceMatcher(None, edit['before'], edit['after'], autojunk=False)
        for operation, a, b, c, d in reversed(matcher.get_opcodes()):
            if operation == 'equal':
                continue
            i, j = offset + a, offset + b
            new_length = d - c
            delta = new_length - (j - i)
            if j <= start:
                start, end = start + delta, end + delta
            elif i < end:
                start = min(start, i)
                end = max(i + new_length, end + delta)
    return start, end

def compare(only=None):
    pages = versions()
    loci = {}
    for row in tab('K31-04_blind_loci.tsv'):
        loci.setdefault((int(row['scan']), row['place']), []).append(row)
    results = []
    for reading in tab('K31-04_blind.tsv'):
        n, place = int(reading['scan']), reading['place']
        if only and n != only:
            continue
        original, final, edits = pages[n]
        key = canon(reading['what_the_crop_shows'])
        locus = loci.get((n, place))
        whole = False
        if locus:
            first_pieces, last_pieces = [], []
            for position in locus:
                start = int(position['first_pass_start'])
                end = int(position['first_pass_end'])
                final_start, final_end = final_interval(start, end, edits)
                first_pieces.append(canon(original[start:end]))
                last_pieces.append(canon(final[final_start:final_end]))
            first, last = ' … '.join(first_pieces), ' … '.join(last_pieces)
            whole = locus[0]['match'] == 'whole'
        else:
            first, last = canon(original), canon(final)
        first_ok = bool(key) and (key == first if whole else key in first)
        final_ok = bool(key) and (key == last if whole else key in last)
        shown = first if locus else nearby(key, first)
        outcome = 'exact sequence' if final_ok else 'different sequence'
        results.append((n, place, reading['what_the_crop_shows'], first_ok, shown, outcome))
    return results

def report():
    rows=compare()
    decisions={(int(x['scan']), x['place']):x['decision'] for x in tab('K31-04_blind_decisions.tsv')}
    intro = ('The blind TSV preserves the readings as written before the page files were reopened. '
             'Comparison preserves case, accents, numerals and punctuation, removes spacing and editorial wrappers, '
             'and equates common TeX spellings of the same sign. An excerpt may identify only part of a correction. '
             'For repeated strings, isolated symbols and every reported difference, the locus TSV fixes the first-pass '
             'character intervals and the script carries them through every recorded audit and witness edit. An ellipsis in the comparison column separates nonadjacent intervals. '
             'For other excerpts it searches the page. At an anchored place the fourth column is the normalized '
             'first-pass excerpt. Elsewhere it is an approximate nearest string and the decision identifies the '
             'reading on the ink. The last column distinguishes an actual textual revision from abbreviated '
             'blind notation, superposition, segmentation or layout.')
    out = ['# Blind collation', intro,
           '| Scan | Place | Blind reading | First-pass sequence | Normalized final page | Decision on the crop |',
           '|---:|---|---|---|---|---|']
    for n,place,v,match,near,r in rows:
        if not match:out.append('| '+str(n)+' | '+place+' | '+esc(v)+' | '+esc(near)+' | '+r+' | '+decisions.get((n,place),'see page audit').replace('|',r'\|')+' |')
    total = len(rows)
    matched = sum(x[3] for x in rows)
    out += ['', f'Compared {total} blind entries. {matched} matched the first-pass sequence under the stated rules. '
                f'{total-matched} have individual decisions above. The earlier case-folded, whole-page search had '
                'flagged 56 entries. The register below lists every literal audit revision, including other findings '
                'from the complete thirds.',
            '', '| Scan | Before | After | Decision on the ink |', '|---:|---|---|---|']
    for row in tab('K31-04_revisions.tsv'):
        if row['phase']=='audit':out.append('| '+row['scan']+' | '+esc(row['before'])+' | '+esc(row['after'])+' | '+row['ink_or_interpretation']+' |')
    (root/'K31-04_blind_compare.md').write_text('\n\n'.join(out[:2])+'\n\n'+'\n'.join(out[2:])+'\n')
if __name__=='__main__':
    if len(sys.argv)>1:
        for n,loc,v,ok,near,r in compare(int(sys.argv[1])):
            if not ok:print(loc,flat(v),'<>',near)
    else:report()
