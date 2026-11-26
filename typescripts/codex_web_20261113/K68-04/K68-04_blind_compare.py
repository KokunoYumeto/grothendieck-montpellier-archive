"""Compare blind readings with the recorded first pass. An optional argument supplies those pages directly."""
from pathlib import Path
import csv, hashlib, re, sys
from functools import lru_cache

root = Path(__file__).resolve().parent
def rows(name):
    with (root / ('K68-04_' + name + '.tsv')).open() as f:
        return list(csv.reader(f, delimiter='\t'))[1:]

def primary(s):
    # Retain the first candidate while respecting nested arguments.
    pattern = re.compile(r'\\unsure\{')
    while match := pattern.search(s):
        start = match.end()
        depth = 1
        divide = None
        for j in range(start, len(s)):
            if s[j] in '{}' and (j == 0 or s[j - 1] != '\\'):
                depth += 1 if s[j] == '{' else -1
            if depth == 1 and s[j] == '|' and divide is None:
                divide = j
            if depth == 0:
                break
        else:
            raise ValueError('Unclosed candidate in ' + s)
        s = s[:match.start()] + s[start:(j if divide is None else divide)] + s[j + 1:]
    return s

def norm(s):
    s = primary(s)
    s = re.sub(r'\\(?:deleted|inserted|handwritten|margin|uline|uuline|mathrm|text|operatorname|textsuperscript|underbrace|boxed|left|right)(?![A-Za-z])', '', s)
    s = s.replace(r'\longrightarrow', r'\to').replace(r'\rightarrow', r'\to')
    s = s.replace(r'\longmapsto', r'\mapsto').replace(r'\leq', r'\le').replace(r'\geq', r'\ge')
    s = s.replace(r'\,', '').replace(r'\ ', '').replace(r'\quad','').replace(r'\qquad','')
    s = s.replace(r'\neq',r'\ne')
    return re.sub(r'[\s{}$]', '', s)

def cell(s):
    return s.replace('|', r'\|').replace('\n', ' ')

def page(folder,n):
    return (folder / f'K68-04_68_scan{int(n):03}.tex').read_text()

@lru_cache(maxsize=None)
def stages(n):
    """Invert recorded span edits and zero-context line hunks, checking both stages."""
    current = page(root/'pages', n)
    changes = rows('witness_changes') if (root/'K68-04_witness_changes.tsv').is_file() else []
    for scan, _, _, start, old, new, _ in reversed(changes):
        if int(scan) == int(n):
            i = int(start)
            if current[i:i+len(new)] != new:
                raise ValueError(f'{n}: witness edit does not match the final page')
            current = current[:i] + old + current[i+len(new):]
    log = (root/'progress.log').read_text().split('transcription frozen', 1)[0]
    digest = hashlib.sha256(current.encode()).hexdigest()
    if f'{digest}  pages/K68-04_68_scan{int(n):03}.tex' not in log:
        raise ValueError(f'{n}: the reconstructed freeze has the wrong SHA-256')
    audit = (root/'K68-04_audit.md').read_text().split('## Exact changes during the image audit\n', 1)[1]
    block = audit.split(f'### {n}\n', 1)[1].split('\n### ', 1)[0]
    lines = current.splitlines(keepends=True)
    hunks = []
    for line in block.splitlines(keepends=True):
        match = re.match(r'@@ -\d+(?:,\d+)? \+(\d+)(?:,(\d+))? @@', line)
        if match:
            pos, count = int(match[1]), int(match[2] or 1)
            hunks.append((pos if count == 0 else pos-1, [], []))
        elif hunks and line.startswith(('-', '+')):
            hunks[-1][1 if line[0]=='-' else 2].append(line[1:])
    for pos, before, after in reversed(hunks):
        if lines[pos:pos+len(after)] != after:
            raise ValueError(f'{n}: audit line change does not match the freeze')
        lines[pos:pos+len(after)] = before
    return ''.join(lines), current


blind = rows('blind')
decisions = {(n,k):(old,new,why) for n,k,old,new,why in rows('blind_resolutions')}
first = Path(sys.argv[1]) if len(sys.argv)>1 else None
draft = '--draft' in sys.argv
if draft and first and first.name=='--draft':
    first = None
missing = []
report = []
for n,k,value in blind:
    reconstructed, current = stages(n)
    document = page(first, n) if first else reconstructed
    if first and document != reconstructed:
        raise ValueError(f'{n}: supplied first pass differs from the reconstructed first pass')
    reading = norm(value)
    if (n,k) in decisions:
        before, after, reason = decisions[n,k]
        if norm(before) not in norm(document):
            missing.append((n,k,'historical excerpt',before))
        if norm(after) not in norm(current):
            missing.append((n,k,'settled excerpt',after))
        if norm(value) != norm(before):
            report.append((n,k,value,before,after,reason))
    elif reading not in norm(document):
        missing.append((n,k,'unmapped blind reading',value))
if missing:
    for x in missing: print(*x,sep='\t')
    if not draft: sys.exit(1)
if not draft:
    out = ['# Blind comparison','',
        f'{len(blind)} entries. {len(report)} differ from the first-pass reading after removing spacing and editorial wrappers, taking the first alternative, and identifying LaTeX commands for the same arrow. Cases with a different extent or cancellation boundary are explained in the audit and the resolution ledger. The comparison reconstructs the pre-witness freeze from the final page, verifies its recorded digest, then reverses the audit line changes to recover the first pass. The optional originals produce the same result.','',
        '| Scan | Crop and place | Blind | First pass | Settled on the crop | Decision |',
        '|---|---|---|---|---|---|']
    for row in report:
        out.append('| '+' | '.join((chr(96)+cell(x)+chr(96)) if i in (2,3,4) else cell(x) for i,x in enumerate(row))+' |')
    (root/'K68-04_blind_compare.md').write_text('\n'.join(out)+'\n')
    print(f'{len(blind)} entries compared, {len(report)} differences.')

