"""Static checks only. Run with Python 3 from any directory."""
from pathlib import Path
import re, hashlib

root = Path(__file__).resolve().parent
key = 'K45-03'
scans = [*range(33, 43), 45, 46, 47]
allowed = set("""
alpha arrow bar begin beta bullet cap cdot circ cotefile cup deleted delta Delta
diagram draw ell end figure frac Gamma hfill illegible in infty inserted lambda
langle ldots left longrightarrow Longleftrightarrow Longrightarrow lrcorner margin
mathbb mathbin mathcal mathfrak mathrel mathrm mathscr mspage mu ne node notin
operatorname otimes overset phantom phi Phi Pi psi qquad quad rangle rho right
Rightarrow rtimes S scanpage sim simeq subset supset text textquotedblleft
textquotedblright textsuperscript tfrac to uline underline unsure uuline
varepsilon varphi widehat xi xrightarrow""".split())
envs = {'aligned','array','tikzcd','tikzpicture','gathered','matrix','cases'}
def check(page):
    raw = page.read_text()
    source = re.sub(r'(?<!\\)%[^\n]*', '', raw)
    depth, math, environments = 0, [], []
    for m in re.finditer(r'\\(?:begin|end)\{([A-Za-z*]+)\}|\\([A-Za-z]+)|\\(.)|[{}$]', source):
        t = m[0]
        line = source.count('\n', 0, m.start())+1
        def require(ok, reason):
            if not ok: raise ValueError(f'{page.name}, line {line}: {reason}')
        if m[1]:
            env=m[1]; require(env in envs, f'unknown environment {env}')
            if t.startswith(r'\begin'): environments.append(env)
            else: require(environments and environments.pop()==env, 'environment mismatch')
        elif m[2]: require(m[2] in allowed, f'unknown command {t}')
        elif t=='{': depth+=1
        elif t=='}': depth-=1; require(depth>=0,'early closing brace')
        elif t in (r'\(',r'\['): require(not math,'nested math delimiters'); math.append(t)
        elif t in (r'\)',r'\]'): require(math and math.pop()=={r'\)':r'\(',r'\]':r'\['}[t],'math delimiter mismatch')
        elif t=='$':
            if math==['$']: math.pop()
            else: require(not math,'nested dollar'); math.append(t)
    if depth or math or environments: raise ValueError((page.name,depth,math,environments))
    for m in re.finditer(r'\\begin\{tikzcd\}\[([^\]]*)\](.*?)\\end\{tikzcd\}',source,re.S):
        if r'ampersand replacement=\&' not in m[1] or re.search(r'(?<!\\)&',m[2]):
            raise ValueError((page.name,'tikzcd cell separator'))
    return raw
def check_witness(files):
    import csv
    ledger = root / f'{key}_witness_edits.tsv'
    if not ledger.exists():
        return
    log=(root/'progress.log').read_text()
    freeze=log.split('transcription frozen ',1)[0]
    recorded=dict((path,digest) for digest,path in re.findall(r'^([0-9a-f]{64}) (.+\.tex)$',freeze,re.M))
    with ledger.open(newline='') as f:
        edits=list(csv.DictReader(f,delimiter='\t'))
    chunks=[]
    for n,p in zip(scans,files):
        s=p.read_text()
        rows=[r for r in edits if int(r['scan'])==n]
        for row in reversed(rows):
            i=int(row['final_character_offset'])
            current,old=row['final_span'],row['frozen_span']
            assert s[i:i+len(current)]==current,(n,i)
            assert old.startswith((r'\unsure{',r'\illegible{')) and old.endswith('}')
            s=s[:i]+old+s[i+len(current):]
        data=s.encode('utf-8'); chunks.append(data)
        assert hashlib.sha256(data).hexdigest()==recorded[str(p.relative_to(root))],p
    assert hashlib.sha256(b''.join(chunks)).hexdigest()==recorded[f'{key}_transcription.tex']
    print(f'{len(edits)} witness edits reverse to all 14 frozen hashes.')
    if 'witness check done ' in log:
        second=log.split('transcription frozen ',1)[1].split('witness check done ',1)[0]
        expected=dict((path,digest) for digest,path in re.findall(r'^([0-9a-f]{64}) (.+\.tex)$',second,re.M))
        for p in files+[root/f'{key}_transcription.tex']:
            assert hashlib.sha256(p.read_bytes()).hexdigest()==expected[str(p.relative_to(root))],p
        print('All 14 files match the recorded post-witness hashes.')


def check_inventory(files):
    import csv
    from collections import Counter, defaultdict
    inventory = root / f'{key}_inventory.csv'
    with inventory.open(encoding='utf-8', newline='') as f:
        reader = csv.DictReader(f)
        assert reader.fieldnames == ['cote','scan','sheet_kind','hand','element','kind','position','first_words_or_objects','transcribed']
        rows = list(reader)
    by_scan = defaultdict(list)
    for row in rows:
        assert row['cote'] == '45' and row['transcribed'] == 'yes', row
        assert row['sheet_kind'] in {'text','letter','reused_typed','cancelled_draft','cover'}, row
        assert row['hand'] in {'typed','Grothendieck','other hand','unknown'}, row
        assert row['position'] and row['first_words_or_objects'], row
        by_scan[int(row['scan'])].append(row)
    assert list(by_scan) == scans
    mark_totals = Counter()
    tag_by_kind = {'deletion':r'\deleted{','insertion':r'\inserted{','margin note':r'\margin{',
                   'diagram':r'\diagram{','drawing':r'\figure{','handwritten':r'\handwritten{','display':r'\['}
    for n, page in zip(scans,files):
        page_rows = by_scan[n]
        assert [int(row['element']) for row in page_rows] == list(range(1,len(page_rows)+1)), n
        text = re.sub(r'(?<!\\)%[^\n]*','',page.read_text())
        kinds = Counter(row['kind'] for row in page_rows)
        for kind, tag in tag_by_kind.items():
            assert kinds[kind] == text.count(tag), (n,kind)
        for tag in ('unsure','illegible','deleted'):
            mark_totals[tag] += text.count('\\'+tag+'{')
    print(f'{len(rows)} inventory elements marked yes. Display and editorial-element counts match all 13 pages.')
    print('Final marks: ' + ', '.join(f'{n} {tag}' for tag,n in mark_totals.items()) + '.')



def main():
    files=[root/'pages'/f'{key}_45_scan{n:03}.tex' for n in scans]
    assert sorted(files)==sorted((root/'pages').glob('*.tex'))
    for n,p in zip(scans,files):
        t=check(p);assert re.findall(r'\\scanpage\{(\d+)\}',t)==[str(n)]
    aggregate=root/f'{key}_transcription.tex'
    assert aggregate.read_bytes()==b''.join(p.read_bytes() for p in files)
    s=check(aggregate);assert s.count(r'\cotefile{45}')==1 and s.startswith(r'\cotefile{45}')
    wrapper=(root/f'{key}_standalone.tex').read_text().split()
    assert wrapper==[r'\input{PREAMBLE.tex}',r'\begin{document}',r'\input{K45-03_transcription}',r'\end{document}']
    print('13 page fragments and aggregate passed brace, math, environment and command checks.')
    print('Page order, cotefile, TikZ separators, wrapper and byte-for-byte assembly verified.')
    check_witness(files)
    check_inventory(files)
    for p in files+[aggregate]:
        print(hashlib.sha256(p.read_bytes()).hexdigest(),p.relative_to(root))
if __name__=='__main__':
    main()

