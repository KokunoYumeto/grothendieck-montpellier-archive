"""Content comparison of retired checkpoints with the surviving returns.

The retired folders are gone.  What survives of their content is (a) the verbatim output of my own read commands,
kept in this agent's transcript, and (b) one preserved manifest (handled separately).  For each range that a command
printed, the same range of the surviving file is compared as a string with the stored output.  Nothing is inferred
about lines that were not printed.  Read-only; own code; imports the standard library only.
"""
import json, pathlib, re, sys

T = pathlib.Path(sys.argv[1])
R = pathlib.Path(sys.argv[2])
calls, results = [], {}
for line in T.open(encoding='utf-8'):
    try:
        rec = json.loads(line)
    except ValueError:
        continue
    content = (rec.get('message') or {}).get('content')
    if not isinstance(content, list):
        continue
    for c in content:
        if not isinstance(c, dict):
            continue
        if c.get('type') == 'tool_use' and c.get('name') == 'Bash':
            calls.append((c['id'], c['input'].get('command', '')))
        elif c.get('type') == 'tool_result':
            body = c.get('content')
            if isinstance(body, list):
                body = ''.join(x.get('text', '') for x in body if isinstance(x, dict))
            results[c['tool_use_id']] = (body or '').replace('\r\n', '\n')


def outputs(*needles):
    return [results.get(i, '') for i, cmd in calls if all(n in cmd for n in needles)]


def lines(p):
    return p.read_bytes().decode('utf-8').replace('\r\n', '\n').rstrip('\n').split('\n')


def cut(ls, w):
    return [l.encode('utf-8')[:w].decode('utf-8', 'ignore') for l in ls] if w else ls


def test(label, path, a, b, w, *needles):
    ls = lines(path)
    b = len(ls) if b is None else min(b, len(ls))
    want = '\n'.join(x.rstrip() for x in cut(ls[a - 1:b], w)).strip()
    got = ['\n'.join(x.rstrip() for x in o.split('\n')) for o in outputs(*needles)]
    ok = any(want in o for o in got)
    scope = 'WHOLE FILE' if a == 1 and b == len(ls) and not w else 'lines %d-%d of %d%s' % (a, b, len(ls), ' (first %d bytes of each)' % w if w else '')
    print('%-9s %-44s %s' % ('SAME' if ok else ('DIFFERS' if got else 'NOOUTPUT'), label, scope))
    if not ok and got:
        miss = [a + i for i, l in enumerate(cut(ls[a - 1:b], w)) if l.strip() and not any(l.rstrip() in o for o in got)]
        print('          lines absent from the stored output:', len(miss), miss[:12])


F = R / 'GCT_POS_final_20261122T0219Z_unzipped'
C = 'GCT_POS_checkpoint_03'
K, RT, P = F / 'branches/kronecker', F / 'branches/root', F / 'branches/plethysm'
print('## GCT_POS checkpoint 03 -> final')
test('K-001..K-004', K / 'KRONECKER_FINDINGS.tex', 1, 200, 0, C, 'sed -n 1,200p KRONECKER_FINDINGS.tex')
test('K-004..K-008', K / 'KRONECKER_FINDINGS.tex', 200, 520, 0, C, 'sed -n 200,520p KRONECKER_FINDINGS.tex')
test('K-009', RT / 'lift_bound.tex', 1, 140, 0, C, 'sed -n 1,140p lift_bound.tex')
test('R-NEW-003', RT / 'h4_finite_rational.tex', 1, 90, 0, C, 'h4_finite_rational.tex | head -90')
test('R-NEW-003 k4 values', F / 'certificates/k4_small_values.json', 1, None, 0, C, 'k4_small_values.json')
test('K-014', K / 'N5_POLE.tex', 1, 60, 400, C, 'sed -n 1,60p kronecker/N5_POLE.tex')
test('K-010 table', K / 'N5_SPECTRA_TABLE.tex', 1, 25, 300, C, 'sed -n 1,25p N5_SPECTRA_TABLE.tex')
test('K-018', K / 'AMPLIFYING_GADGET.tex', 1, 70, 300, C, 'sed -n 1,70p kronecker/AMPLIFYING_GADGET.tex')
for lab, name in (('K-020', 'AMPLIFIER_FULL_STABILIZERS'), ('K-019', 'N9_FULL_STABILIZER'), ('K-016', 'EVEN_DIMENSION_STABILIZER'),
                  ('K-012', 'ANTIPODAL_STABILIZER'), ('K-013', 'ONE_PAIR_STABILIZER'), ('K-017', 'ALL_N_ROUTE_AUDIT')):
    p = K / (name + '.tex')
    ls = lines(p)
    n = next(i + 1 for i, l in enumerate(ls) if 'begin{theorem}' in l or 'begin{proposition}' in l)
    test(lab + ' statement', p, n, n + 16, 200, C, 'AMPLIFIER_FULL_STABILIZERS.tex kronecker/N9_FULL_STABILIZER.tex')
test('K-015 title', K / 'LIE_EXTENSION.tex', 1, 1, 200, C, 'AMPLIFIER_FULL_STABILIZERS.tex kronecker/N9_FULL_STABILIZER.tex')
test('R-NEW-002', RT / 'canonical_rank_laws.tex', 1, 60, 260, C, 'sed -n 1,60p root/canonical_rank_laws.tex')
test('R-NEW-001 head', F / 'certificates/outer_six_n_le_3.tsv', 1, 5, 0, C, 'head -5 outer_six_n_le_3.tsv')
test('PNEW-001..005 opening', P / 'quantitative_refinement.tex', 1, 40, 0, C, 'sed -n 1,40p quantitative_refinement.tex')
test('PNEW-005', P / 'quantitative_refinement.tex', 329, 420, 0, C, 'sed -n 329,420p quantitative_refinement.tex')
for lab, name in (('PNEW-009', 'fixed_rank_density'), ('PNEW-008', 'density_converse'), ('PNEW-010', 'uniform_positive_gate'),
                  ('PNEW-012', 'outer_six_scalar_positive'), ('PNEW-006', 'exterior_witnesses')):
    p = P / (name + '.tex')
    ls = lines(p)
    n = next(i + 1 for i, l in enumerate(ls) if 'begin{theorem}' in l or 'begin{proposition}' in l)
    test(lab + ' statement', p, n, n + 22, 220, C, 'for f in fixed_rank_density.tex')
test('plethysm LEDGER', P / 'LEDGER.md', 1, None, 900, C, 'cat plethysm/LEDGER.md')
test('SOURCE_AUDIT', F / 'SOURCE_AUDIT.md', 1, 60, 300, C, 'sed -n 1,60p SOURCE_AUDIT.md')
test('root LEDGER, its first 81 lines', F / 'LEDGER.md', 1, 81, 1500, C, 'cat LEDGER.md | cut -c1-1500')

print('## QUESTIONS rows, checkpoint 03 -> final (first four columns)')
old = {}
for o in outputs(C, 'cut -f1-4 QUESTIONS.tsv'):
    for l in o.split('\n'):
        c = l.split('\t')
        if len(c) == 4 and re.match(r'^Q\d', c[0]):
            old[c[0]] = c[3]
new = {}
for l in lines(F / 'QUESTIONS.tsv')[1:]:
    c = l.split('\t')
    new[c[0]] = c[3] if len(c) > 3 else ''
for k in list(new) + [k for k in old if k not in new]:
    a, b = old.get(k), new.get(k)
    print(('same   ' if a == b else 'ADDED  ' if a is None else 'GONE   ' if b is None else 'CHANGED'), k, '' if a == b else '| %s -> %s' % (a, b))

A9 = R / 'ALPOGE_GCT_checkpoint_09_20261121T0547Z_unzipped/work'
print('## ALPOGE_GCT -> checkpoint 09')
for lab, name, cp in (('P-F31', 'positivity_actual_cubic_pole', '05'), ('P-F23', 'positivity_noncancellation', '05'),
                      ('P-F30', 'positivity_full_cubic_support', '05'), ('P-F19', 'positivity_cubic_counterexample', '03'),
                      ('P-F14/15', 'positivity_torus', '03')):
    if (A9 / (name + '.tex')).exists():
        test('%s (stored output of cp%s)' % (lab, cp), A9 / (name + '.tex'), 1, None, 0, 'ALPOGE_GCT_checkpoint_' + cp, 'cat ' + name + '.tex')
    else:
        print('ABSENT', lab)
