"""Compare crop-only readings with their first and current transcription at the same place."""
from pathlib import Path
from difflib import SequenceMatcher
import csv, json, re

ROOT = Path(__file__).resolve().parent

def brace_end(s, k):
    depth = 1
    for j in range(k + 1, len(s)):
        if s[j] in '{}' and (j == 0 or s[j-1] != '\\'):
            depth += 1 if s[j] == '{' else -1
            if depth == 0:
                return j
    raise ValueError('unbalanced argument: ' + s[k:k+75])

def primary(s):
    pat = re.compile(r'\\(unsure|deleted|inserted|uline|uuline|margin|text)\s*(\{|\\[A-Za-z]+|[A-Za-z])')
    while m := pat.search(s):
        if m[2] == '{':
            end = brace_end(s, m.end()-1)
            body = s[m.end():end]
        else:
            end = m.end()-1
            body = m[2]
        if m[1] == 'unsure':
            body = body.split('|', 1)[0]
        s = s[:m.start()] + body + s[end+1:]
    return s

def canonical(s):
    s = primary(s)
    for old, new in [(r'\ast','*'),(r'\geq',r'\ge'),(r'\leq',r'\le'),
                     (r'\longmapsto',r'\mapsto'),(r'\varnothing',r'\emptyset'),
                     (r'\ne'+'q',r'\ne'),(r'\widehat',r'\hat'),(r'\overline',r'\bar'),
                     (r'\operatorname',''),(r'\mathrm',''),(r'\left',''),(r'\right',''),
                     (r'\quad',''),(r'\,',''),(r'\!',''),(r'\ ','')]:
        s = s.replace(old,new)
    s = re.sub(r'(?<!\\)[{}$&\s~]+','',s)
    return re.sub(r'\s+','',s)

def remap(blocks, a, b):
    def boundary(p, is_end):
        for tag, i,j,k,l in blocks:
            if tag == 'insert':
                continue
            if i <= p < j or (is_end and i < p <= j):
                if tag == 'equal':
                    return k + p-i
                if p == i: return k
                if p == j: return l
                return l if is_end else k
        return blocks[-1][4]
    return boundary(a,False),boundary(b,True)

def md(s):
    return str(s).replace('|',r'\|').replace('\n',' ')

def tex(value):
    return chr(96) + md(value) + chr(96)


def main():
    refs = json.loads((ROOT/'K68-03_collation.json').read_text())
    with (ROOT/'K68-03_blind.tsv').open() as f:
        blind = {(int(r['scan']),r['place']):r['what_the_crop_shows'] for r in csv.DictReader(f,delimiter='\t')}
    diffs, rows, later = [],0,[]
    after_witness = {
        (36, 'new quotient of algebra'): 'The witness check also admitted a double-struck A for the overlapped characters after J.',
        (40, 'third, retouched identity'): 'The witness check admitted fu as a second reading of the old left product.',
        (42, 'unusual phrase after tensor module'): 'At the witness check the crossed t and its single trailing stroke settled the word as et.',
    }
    for page, ref in refs.items():
        n = int(page)
        live = canonical((ROOT/'pages'/f'K68-03_68_scan{n:03}.tex').read_text())
        blocks = SequenceMatcher(None,ref['reference'],live,autojunk=False).get_opcodes()
        for rec in ref['checks']:
            p,a,b,first,settlement=rec
            raw = blind[n,p]
            old = ref['reference'][a:b]
            assert old == canonical(first), (n,p,first)
            i,j = remap(blocks,a,b)
            cur = live[i:j]
            rows += 1
            if canonical(raw) != old:
                if (n, p) in after_witness:
                    settlement += " " + after_witness[n, p]
                diffs.append((n,p,first,raw,settlement,cur))
            elif cur != old:
                later.append((n,p,first,cur))
    result = ['# Blind collation','',f'{rows} independently entered readings. {len(diffs)} differ from the first transcription. Each difference below includes the first-pass reading, the crop-only reading, the decision and the current comparison key.','',
              'The comparison removes layout, spacing and editorial wrappers and uses the first candidate of a doubt. It equates common TeX spellings of the same sign. Deletions remain in the comparison. The compact key removes spaces between TeX control words and adjoining letters. The companion JSON records the first-pass comparison stream and the character interval of each entry. The script maps that interval to the current page by sequence alignment.','',
              '| Scan | Place | First pass | Blind | Settlement on the image | Current comparison key |','|---|---|---|---|---|---|']
    for n,place,first,raw,settlement,current in diffs:
        columns = [str(n),md(place),tex(first),tex(raw),md(settlement),tex(current)]
        result.append('| ' + ' | '.join(columns) + ' |')
    result += ['','## Other changes at compared places','',
               'These first agreed with the blind reading. Subsequent editing or a witness decision can change the current comparison string.','',
               '| Scan | Place | First pass | Current |','|---|---|---|---|']
    result += ['| '+' | '.join(md(x) for x in row)+' |' for row in later] or ['| — | None | | |']
    (ROOT/'K68-03_blind_compare.md').write_text('\n'.join(result)+'\n')
    print(f'{rows} readings; {len(diffs)} differences; {len(later)} other current differences')
if __name__ == '__main__':
    main()
