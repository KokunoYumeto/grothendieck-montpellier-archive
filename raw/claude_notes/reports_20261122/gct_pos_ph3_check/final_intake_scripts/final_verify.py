"""Verification of what the final intake claims; reads files, runs no code of the return, writes nothing."""
import collections, hashlib, json, pathlib, re
from fractions import Fraction as Fr
from itertools import combinations

D = pathlib.Path('<local>/Documents')
F = D / 'grothendieck_archive_transcription_20261110/research_returns/GCT_POS_final_20261122T0219Z_unzipped'
C = pathlib.Path(__file__).parent

print('== K-022 exactly, in Z[x]/(x^(M/2)+1)')
for m in (2, 4, 8, 16):
    a, M = (1, m, 2*m-1, 2*m+1, 4*m-1), 4*m
    S = sum(a)
    N = collections.Counter({0: 1})
    for x in a:
        N[S-x] -= 1; N[S+x] += 1
    N[2*S] -= 1
    out = []
    for o in range(3):
        r = [0]*(M//2)
        for d, c in N.items():
            for q in range(o):
                c *= d-q
            e = (d-o) % M
            r[e % (M//2)] += -c if e >= M//2 else c
        out.append(not any(r))
    print(M, 'N, N1, N2 vanish:', out, '| vanishing denominator weights:', sum((a[i]+a[j]) % M == 0 for i, j in combinations(range(5), 2)))

print('== PNEW-016 exactly')
n = 79004
print(n < 2**17, Fr(2+17) <= Fr(n, 96), Fr(n**4, 96) > 5*n**3+2, (Fr(1, 5)-Fr(343, 1728))*2000 >= 3)

print('== four checked files: SHA-256')
for l in (D/'reports_20261122/gct_pos_ph3_check/FILES_READ.sha256').read_text(encoding='utf-8').splitlines():
    h, name = re.match(r'([0-9a-f]{64})\s+\*?(.+)', l).groups()
    hit = [p for p in F.rglob(pathlib.PurePosixPath(name.replace('\\', '/')).name) if hashlib.sha256(p.read_bytes()).hexdigest() == h]
    print(bool(hit), name)

print('== N diff, counts by status')
print(dict(collections.Counter(l.split('\t')[0] for l in (C/'n_branch_diff.tsv').read_text(encoding='utf-8').splitlines())))

print('== names of the two proofs, ALPOGE_GCT run id removed')
pat = re.compile(r'alp(?:ö|o|\\"o|\\"\{o\})ge|masullo|riemann hypothesis|\bGRH\b|remark\.pdf|music of the primes', re.I)
count = collections.Counter()
for p in F.rglob('*'):
    if p.is_file() and p.suffix.lower() in ('.tex', '.md', '.tsv', '.txt', '.py', '.json', '.bib', '.csv'):
        for k, l in enumerate(p.read_text(encoding='utf-8', errors='replace').splitlines(), 1):
            m = pat.search(re.sub(r'ALPOGE\\?_(GCT|PF\d+)', '', l))
            if m:
                count['hits'] += 1
                print(p.relative_to(F).as_posix(), k, '|', l[max(0, m.start()-120):m.start()+280])
        count['files'] += 1
print(dict(count))

print('== events on the hypothesis and parameter')
for l in (F/'CHECK_EVENTS.tsv').read_text(encoding='utf-8').splitlines():
    if l.startswith('GCTVI-parameter'):
        print(l)
print('== FINAL_STATUS 91-98')
print('\n'.join((F/'FINAL_STATUS.md').read_text(encoding='utf-8').splitlines()[90:]))

print('== did the mirror hold anything the notes file lacks?')
T = '<local>/.claude/projects/C--Users-user-Documents/e0d20ada-e036-40ad-83b1-31e9a63b69bc/subagents/agent-a0805369bae2ebddc.jsonl'
mir = '20261121_intake_GCT_PLETH_ALPOGE_GCT_NOTES.md'
notes = (D/'agent_notes/a0805369bae2ebddc_NOTES.md').read_text(encoding='utf-8')
for line in open(T, encoding='utf-8'):
    if mir not in line:
        continue
    r = json.loads(line)
    c = (r.get('message') or {}).get('content')
    if not isinstance(c, list):
        continue
    for b in c:
        if not isinstance(b, dict) or b.get('type') != 'tool_use':
            continue
        i = b['input']
        if b['name'] in ('Write', 'Edit') and mir in i.get('file_path', ''):
            body = i.get('content') or i.get('new_string') or ''
            miss = [x for x in body.splitlines() if x.strip() and x not in notes]
            print(r.get('timestamp'), b['name'], 'lines', len(body.splitlines()), 'absent from notes', len(miss), miss[:2])
        elif b['name'] == 'Bash' and mir in i.get('command', ''):
            print(r.get('timestamp'), 'Bash', [x[:170] for x in i['command'].splitlines() if mir in x][:3])
