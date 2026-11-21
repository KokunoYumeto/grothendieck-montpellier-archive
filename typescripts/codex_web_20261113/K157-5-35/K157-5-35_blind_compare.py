"""Collate the independent crop entries against the saved first and final readings.
Run with Python 3 from any directory. All inputs live next to this script."""
from pathlib import Path
import csv, hashlib, html, json, re
from collections import Counter, defaultdict

ROOT = Path(__file__).resolve().parent
K = 'K157-5-35'
def records(suffix):
    with (ROOT / (K + suffix)).open(encoding='utf-8', newline='') as f:
        return list(csv.DictReader(f, delimiter='\t'))

def project(s, include_old):
    """Select the first doubtful candidate. Keep or omit deleted matter as requested."""
    pattern = re.compile(r'\\(unsure|illegible|deleted|inserted|margin|mspage)\{')
    pieces = []
    while (m := pattern.search(s)):
        pieces.append(s[:m.start()])
        i, depth = m.end(), 1
        while depth and i < len(s):
            if s[i] in '{}' and s[i-1] != '\\':
                depth += 1 if s[i]=='{' else -1
            i += 1
        group = s[m.end():i-1]
        if m[1]=='unsure':
            group = group.split('|',1)[0]
        if m[1]=='illegible':
            group = '¤'
        if m[1]!='deleted' or include_old:
            pieces.append(project(group,include_old))
        s=s[i:]
    return ''.join(pieces)+s

def normalize(s):
    s=s.replace(r'\{','⦃').replace(r'\}','⦄').replace('’',"'")
    s=s.replace(chr(96)*2,'').replace("''",'')
    s=re.sub(r'\\(?:mathrm|operatorname|mathrel|mathbin|uline|uuline|underline|text|overset|underset|underbrace|overline|substack|mathord)\b','',s)
    s=s.replace(r'\longrightarrow','→')
    s=re.sub(r'\\to\b','→',s)
    s=s.replace(r'\longmapsto','↦')
    s=re.sub(r'\\mapsto\b','↦',s)
    return re.sub(r'\\(?:quad|qquad|,|!|;)|\s+|[\x24{}]','',s)

def matches(s, reading):
    views=[normalize(project(s,yes)) for yes in (False,True)]
    return all(any(normalize(bit.strip()) in v for v in views)
               for bit in reading.split(' ; '))

def cell(s):
    return '<code>'+html.escape(s).replace('|','&#124;')+'</code>'

def main():
    spans=defaultdict(list)
    for r in records('_first_reading_spans.tsv'):
        spans[int(r['scan'])].append(r)
    judgments={(int(r['scan']),r['place']):r for r in records('_blind_decisions.tsv')}
    loci={(int(r['scan']),r['place']):r for r in records('_blind_loci.tsv')}
    blind=records('_blind.tsv'); stats=Counter(); groups=defaultdict(list); usage=set()
    for n in range(543,558):
        final=next((ROOT/'pages').glob(f'*scan{n}.tex')).read_text()
        lines=final.splitlines(keepends=True)
        for e in reversed(spans[n]):
            a,b=int(e['final_begin_line_0']),int(e['final_end_line_0_exclusive'])
            lines[a:b]=json.loads(e['first_reading_lines_json'])
        first=''.join(lines)
        if spans[n]:
            assert hashlib.sha256(first.encode()).hexdigest()==spans[n][0]['first_page_sha256']
        for r in (r for r in blind if int(r['scan'])==n):
            p,b=r['place'],r['what_the_crop_shows']
            loc=loci[(n,p)]
            fa,fb,la,lb=(int(loc[key]) for key in ('first_start','first_end','final_start','final_end'))
            orig=''.join(first.splitlines(keepends=True)[fa-1:fb])
            current=''.join(final.splitlines(keepends=True)[la-1:lb])
            old=matches(orig,b);new=matches(current,b)
            scope=f'{fa}–{fb} / {la}–{lb}'
            j=judgments.get((n,p))
            if j:
                usage.add((n,p));status=j['classification'];after=j['final_locus'];reason=j['settlement']
            elif old and new:
                status='Concordant';after=b;reason='The recorded characters occur in the corresponding source block of both readings.'
            else:
                raise SystemExit(f'Unsettled comparison: {n} / {p} / {b} (first={old}, final={new})')
            stats[status]+=1
            groups[n].append('| '+' | '.join([p,cell(b),scope,('yes' if old else 'no')+' / '+('yes' if new else 'no'),cell(after),status+'. '+reason])+' |')
    assert usage==set(judgments), 'Unused manual decision'
    report=['# Blind collation · scans 543–557','',
      f'{len(blind)} hard-place entries. The source-line columns locate the corresponding passage in the reconstructed first page file and in the final page file. The literal comparison is restricted to those named blocks, ignoring TeX spacing, grouping and upright type styles. A search includes a view with canceled text and a view without it. Script alphabets, primes, accents, case and subscripts remain distinct. The two searches do not adjudicate the reading. The place and settlement identify the mark that was checked by eye.',
      '', 'The blind column reproduces the original field. Semicolon-separated extracts can describe nonadjacent marks. Square brackets and ellipses in those fields are the reader’s brief indications of cancellation or unquoted surroundings. They are not manuscript punctuation.', '',
      ' | '.join(f'{key}: {value}' for key,value in sorted(stats.items())), '']
    for n,rows in groups.items():
        report+= [f'## Scan {n}', '', '| Place | Blind entry | Source lines, first / final | Literal in first / final | Adopted locus | Settlement |','|---|---|---|---|---|---|',*rows,'']
    (ROOT/(K+'_blind_compare.md')).write_text('\n'.join(report),encoding='utf-8')
    print(len(blind),dict(stats))
if __name__=='__main__':
    main()
