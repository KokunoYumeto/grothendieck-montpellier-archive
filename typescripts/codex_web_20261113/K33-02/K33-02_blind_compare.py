from pathlib import Path
import csv, json, re, sys

ROOT = Path(__file__).resolve().parent
REFERENCE = json.loads((ROOT / 'K33-02_blind_reference.json').read_text())
DATA, FIRST = REFERENCE['alignments'], REFERENCE['first']

def normal(s):
    s=s.replace('“', "``").replace('”', "''").replace('~',' ')
    # Ignore typesetting choices, keep diplomatic distinctions: i/j, dash/arrow, marks above and below, and letter order.
    s=s.replace('\\ ',' ').replace('\\,',' ').replace('$','')
    wrappers=r'\\(?:mathrm|uline|uuline|inserted|deleted|handwritten|text|underline)\{([^{}]*)\}'
    for _ in range(8):
        old=s
        s=re.sub(r'\\unsure\{((?:[^{}]|\{[^{}]*\})*)\}',lambda m:m[1].split('|')[0],s)
        s=re.sub(wrappers,r'\1',s)
        s=re.sub(r'([_^])\{([A-Za-z0-9*!])\}',r'\1\2',s)
        s=s.replace('{}','')
        if s==old:break
    return re.sub(r'\s+','',s)

def contains(source,target):
    return normal(target) in normal(source)

def diagrams(source,place):
    ds=re.findall(r'\\diagram\{(.*?)\\end\{tikzcd\}\}',source,re.S)
    if place.startswith('weight row '):
        row=ds[1 if place.endswith('B') else 2]
        labels=re.findall(r'label=above:\{\$(\d+)\$\}',row)
        return ' '.join(labels[:3])+ ' | '+' '.join(labels[3:])
    if place=='fork':
        row=next(l for l in ds[3].splitlines() if 'D_\\ell' in l)
        cols=row.split(r'\&')
        forks=[i for i,c in enumerate(cols) if '\\arrow[ur,dash]' in c and '\\arrow[dr,dash]' in c]
        return 'two limbs to the right of sixth point' if forks==[6] else repr(forks)
    if place=='E6 branch':
        row=next(l for l in ds[4].splitlines() if 'E_6' in l)
        return 'down from third of five' if row.count(r'\vert')==5 and r'\arrow[d,dash]' in row.split(r'\&')[3] else row
    raise KeyError(place)

PLACES = {
    18: {"good": "Insertion about préschémas", "lineend": "End of the same marginal addition", "suff": "Words before cas", "cancel": "Cancellation before the reduction", "arrows": "First arrow label in the factorisation", "ex": "Parenthetical example", "derived": "Indices of the derived image"},
    20: {"fact": "Abbreviation before Notation", "item2": "Cancellation in item (ii)", "trace": "Trace map", "map1": "First covariance formula", "map2": "Second covariance formula"},
    22: {"ring": "Cancelled equation for the ring", "cross": "Cancelled units and et", "gamma": "Underform before G on U", "gammaold": "Cancelled Γ expression", "dail": "Cancellation before ailleurs", "unit": "Γ expression for units on X", "quot": "Cancelled quotient numerator", "seq": "Support-sequence diagram", "iso": "Isomorphism following the diagram", "beta": "Name of the local class", "kummer": "Kummer sequence"},
    24: {"class": "Cancellation before the local class", "base": "Base-change abbreviation", "form": "Word before the equations of Y", "cup": "First factor of the cup product"},
    26: {"base": "Admissible base change", "product": "Points in the product formula", "under": "Two groups before the list of cases", "cases": "Connector beside X in the regular case"},
    28: {"coef": "Cancelled coefficient in the first display", "class": "Cancelled noun before canonique", "family": "Marginal note on the support family", "nb": "Marginal N.B.", "oldline": "Cancelled announcement in Example 1", "choix": "End of the point-independence sentence", "return": "Underwords before nous ramenant"},
    31: {"title": "Punctuation after the E₇ heading"},
    32: {"condition": "End of the condition on ambiguity", "var": "Inserted qualifier before variable", "last": "Underword below hom."},
}


def cell(value):
    value = value.replace('|', r'\|').replace('\n', ' ')
    longest = max((len(run) for run in re.findall(r'\x60+', value)), default=0)
    delimiter = chr(96) * (longest + 1)
    return f"{delimiter} {value} {delimiter}"


def compare():
    rows=list(csv.DictReader((ROOT/'K33-02_blind.tsv').open(),delimiter='\t'))
    md=['# Blind comparison','',
        'Of the 192 records, 184 were entered directly as crop readings. Eight more index distinct readings in the dated pre-opening word and accent lists printed in the audit. The reference is the saved first-pass text. The audit describes how the two readings were settled. The last column checks the aligned passage against the distributed page, which can also contain a later, separately recorded witness decision. Listed diagram descriptions are extracted from node and edge data. Typographic spacing, math delimiters and editorial wrappers are ignored for literal comparison. A cancelled letter is included when comparing the visible ink.','',
        '| Scan | Place | Blind reading | First-pass reading | Decision on the ink | Final passage located |','|---|---|---|---|---|---|']
    total=0; missing=[]
    for r in sorted(rows, key=lambda record: int(record['scan'])):
        n=int(r['scan']); k=r['place']; raw=r['what the crop shows']
        t=(ROOT/'pages'/f'K33-02_33_scan{n:03}.tex').read_text()
        d=DATA[str(n)].get(k)
        if n==21 and k in ('weight row B','weight row C','fork','E6 branch'):
            before=diagrams(FIRST[str(n)],k);after=diagrams(t,k);matches=before==raw; found=(after==raw)
        else:
            before=d['before'] if d else raw
            after=d['after'] if d else raw
            matches=contains(FIRST[str(n)],raw) if not d else not d['difference']
            found=contains(t,after)
            if d and not contains(FIRST[str(n)],before):missing.append(f'{n} {k}: first-pass locus')
        if not found:missing.append(f'{n} {k}: final locus')
        if not matches:
            total+=1
            decision=d['decision'] if d else 'Unaligned reading; verify against the crop.'
            place = PLACES.get(n, {}).get(k, k)
            md.append(f'| {n:03} | {place} | {cell(raw)} | {cell(before)} | {decision} | {"yes" if found else "no"} |')
    summary = f'{len(rows)} blind records. {total} differences in reading or editorial state. {len(missing)} missing reference or final passages.'
    md.extend(['', summary])
    if missing:
        md.extend([''] + ['- ' + s for s in missing])
    witness_table = ROOT / 'K33-02_witness.tsv'
    if witness_table.exists():
        with witness_table.open(encoding='utf-8', newline='') as stream:
            decisions = [r for r in csv.DictReader(stream, delimiter='\t') if r['result'] != 'unchanged']
        md.extend(['', '## Subsequent witness decisions', '',
                   'Six open readings were settled and seven gained an alternative. Where a decision below affects an entry above, the reading below is the one in the delivered source. Line numbers refer to the individual TeX file.', '',
                   '| Scan | TeX line | Locus | Final reading | Result | Evidence in the image |',
                   '|---|---:|---|---|---|---|'])
        for r in decisions:
            md.append(f"| {int(r['scan']):03} | {r['tex_line']} | {r['locus']} | {cell(r['final'])} | {r['result']} | {r['ink']} |")
    (ROOT/'K33-02_blind_compare.md').write_text('\n'.join(md)+'\n', encoding='utf-8')
    print(summary if not missing else '\n'.join(missing))
    return missing
if __name__=='__main__':
    sys.exit(bool(compare()))
