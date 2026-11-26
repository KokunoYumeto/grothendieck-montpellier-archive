"""Compare the recorded blind readings with the first pass and the delivered page files."""
import csv
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parent
SYMBOLS = dict(zip(
    'lambda nu rho varphi varepsilon eta delta gamma mu chi Delta leq geq ne in '
    'infty ast otimes sum prod det check bar bigwedge mathbb mathcal mathfrak '
    'mathscr ell prime rightarrow longrightarrow leftrightarrow leftarrow '
    'Rightarrow Longrightarrow simeq cdots ldots S lVert rVert'.split(),
    'λ ν ρ φ ε η δ γ μ χ Δ ≤ ≥ ≠ ∈ ∞ * ⊗ Σ Π det ˇ ¯ ⋀ ℬ 𝒞 𝔉 𝒮 ℓ ′ → → ↔ ← ⇒ ⇒ ≃ … … § ‖ ‖'.split()))
STRIP = set('mathrel operatorname text uline uuline handwritten inserted deleted margin '
            'left right bigl bigr Bigl Bigr qquad quad boxed centerline texttt'.split())

def normal(text, live=False):
    text = text.replace(r'\{','⦃').replace(r'\}','⦄').replace(r'\|','‖')
    text = text.replace(r'\,',' ')
    text = arguments(text, 'unsure', lambda x: x.split('|')[0])
    if live:
        # Remove complete cancellations before comparing the surviving formula.
        text = arguments(text, 'deleted', lambda _: '')
    text = arguments(text, 'unsure', lambda x: x.split('|')[0])
    text = re.sub(r'\\(?:underset)\{[^{}]*\}\{([^{}]+)\}',r'\1',text)
    text = re.sub(r'\\([A-Za-z]+)',lambda m: '' if m[1] in STRIP else SYMBOLS.get(m[1],m[1]),text)
    text = text.replace("''",'′′').replace("'",'′')
    return re.sub(r'[\s$&{}\\]','',text)

def arguments(text, name, replacement):
    key='\\'+name+'{'
    while key in text:
        start=text.rindex(key); pos=start+len(key); end=pos; depth=1
        while end<len(text) and depth:
            depth += int(text[end]=='{')-int(text[end]=='}'); end+=1
        if depth: break
        text=text[:start]+' '+replacement(text[pos:end-1])+' '+text[end:]
    return text

def matches(text, query):
    for view in (normal(text),normal(text,live=True)):
        pos=0
        for piece in query.split('||'):
            token=normal(piece)
            at=view.find(token,pos)
            if at<0: break
            pos=at+len(token)
        else: return True
    return False

def md(s):
    return s.replace('|',r'\|').replace(chr(96),'′').replace('\n',' ')

def read_table(name):
    with (ROOT / name).open(encoding='utf-8', newline='') as stream:
        return list(csv.DictReader(stream, delimiter='\t'))


def page_excerpt(lines, span):
    first, _, last = span.partition('-')
    return ' '.join(lines[int(first) - 1:int(last or first)])


def audit_words(scan, audit):
    marker = f'\n## Scan {scan}\n'
    section = audit.split(marker, 1)[1].split('\n## ', 1)[0]
    return section.split('**Words and accents read before opening the page file.** ', 1)[1].split('\n\n', 1)[0]


def main():
    rows = read_table('K60-01_blind.tsv')
    blind = {(r['scan'], r['place']): r['what the crop shows'] for r in rows}
    if len(blind) != len(rows):
        raise ValueError('Duplicate scan and place in the blind register')
    loci = read_table('K60-01_blind_loci.tsv')
    audit = (ROOT / 'K60-01_audit.md').read_text(encoding='utf-8')
    seen, pages = set(), {}
    differences, later, unresolved = [], [], []
    direct_count = projection_count = audit_count = 0

    for locus in loci:
        scan, place = locus['scan'], locus['place']
        key = scan, place
        if key in seen:
            raise ValueError(f'Duplicate locator {key}')
        seen.add(key)
        original = locus['blind wording']
        if key in blind:
            reading = blind[key]
            if reading == locus['search form']:
                direct_count += 1
            else:
                projection_count += 1
        else:
            excerpt = locus['blind audit excerpt']
            if not excerpt or excerpt not in audit_words(scan, audit):
                raise ValueError(f'Missing independent audit reading for {key}')
            reading = original
            audit_count += 1

        # The special forms expand slash fractions, compare sequences of signs,
        # or isolate the signs named in a descriptive reading. Use them only
        # when their recorded input matches the independently written wording.
        query = locus['search form'] if reading == original else reading
        if scan not in pages:
            filename = ROOT / 'pages' / f'K60-01_60_scan{int(scan):03}.tex'
            pages[scan] = filename.read_text(encoding='utf-8').splitlines()
        current = page_excerpt(pages[scan], locus['line'])
        old = locus['first-pass line']
        pending = (scan, place, reading, old, current)
        evidence = locus['delivered evidence']
        if evidence and not all(piece in current for piece in evidence.split('||')):
            unresolved.append(pending)
            continue

        # Underlining, hand, strike layers and direction sometimes have the
        # same letters in either reading. In those cases use the documented
        # adjudication, anchored to both the blind wording and delivered TeX.
        if locus['post-freeze decision']:
            if reading != original or not matches(old, query):
                unresolved.append(pending)
            else:
                later.append((scan, place, reading, locus['post-freeze decision']))
        elif locus['differing first reading']:
            if reading != original or not evidence:
                unresolved.append(pending)
            else:
                differences.append((scan, place, reading, locus['differing first reading'], locus['crop decision']))
        elif not matches(old, query) or not matches(current, query):
            unresolved.append(pending)

    if set(blind) - seen:
        raise ValueError(f'Blind places without a locator: {sorted(set(blind) - seen)}')

    output = [
        '# Comparison of the blind readings', '',
        f'{len(blind)} entries in the blind register. {direct_count} supply their own search text. '
        f'The other {projection_count} use documented equivalents, for example the component signs of a cancelled array '
        'or a slash quotient expressed as a TeX fraction. '
        f'{audit_count} further readings come from the words and accents recorded in the audit before the page file was opened. '
        'Line addresses refer to the individual TeX fragments. Differences in handwriting, cancellation or positioning '
        'use the crop decision and check for its exact evidence in the delivered line.',
        '', '## Differences and their decisions', '',
        '| Scan | Place | Blind reading | First pass | Decision on the crop |',
        '|---|---|---|---|---|'
    ]
    for row in sorted(differences, key=lambda item: int(item[0])):
        output.append('| ' + ' | '.join(map(md, row)) + ' |')
    if later:
        output += ['', '## Differences introduced by the witness pass', '',
                   '| Scan | Place | Blind and first-pass reading | Delivered decision |', '|---|---|---|---|']
        output += ['| ' + ' | '.join(map(md, row)) + ' |' for row in later]
    if unresolved:
        output += ['', '## Other line comparisons to inspect', '',
                   '| Scan | Place | Blind reading | First-pass line | Delivered line |', '|---|---|---|---|---|']
        output += ['| ' + ' | '.join(map(md, row)) + ' |' for row in unresolved]
    output += ['', f'{len(differences)} differences in the two independent readings and '
               f'{len(later)} later witness-pass difference. {len(unresolved)} further line comparisons require inspection.', '']
    (ROOT / 'K60-01_blind_compare.md').write_text('\n'.join(output), encoding='utf-8')
    if unresolved:
        raise SystemExit('Blind comparisons need inspection: ' + ', '.join(f'{row[0]} {row[1]}' for row in unresolved))


if __name__ == '__main__':
    main()
