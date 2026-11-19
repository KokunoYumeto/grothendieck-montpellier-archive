"""Merge the SA13 sweep-3 readings into sweep3/SA13/ (agent a84c887cf408574ed, Claude Opus 5.5 at effort max, 19 Nov 2026).
Writes CHECK_EVENTS.tsv, CORRECTIONS.tsv and DELIVERABLES.tsv."""
import csv, glob, os, re
DOC = r'C:\Users\user\Documents'
S3 = os.path.join(DOC, r'results_register\horizontal\sweep3\SA13')
RD = os.path.join(S3, 'readings')
STRETCHES = ['c34', 'c33_c36_c39', 'c32_c35_c37_c40', 'c27_c28_c41_c42']


def rows(path):
    with open(path, encoding='utf-8', newline='') as f:
        return list(csv.reader(f, delimiter='\t'))


def merge(suffix, header):
    out = [header + ['stretch']]
    for s in STRETCHES:
        p = os.path.join(RD, f'{s}_{suffix}.tsv')
        if not os.path.exists(p):
            continue
        r = rows(p)
        for row in r[1:]:
            if not any(x.strip() for x in row):
                continue
            row = (row + [''] * len(header))[:len(header)]
            out.append(row + [s])
    with open(os.path.join(S3, f'{suffix}.tsv'), 'w', encoding='utf-8', newline='') as f:
        csv.writer(f, delimiter='\t', lineterminator='\n').writerows(out)
    return len(out) - 1


n_ev = merge('CHECK_EVENTS', ['id', 'date_utc', 'who', 'how', 'result', 'where'])
n_co = merge('CORRECTIONS', ['where', 'what', 'correction', 'reason', 'who'])

# DELIVERABLES
RET = os.path.join(DOC, r'grothendieck_archive_transcription_20261110\returns')
CW = os.path.join(DOC, r'grothendieck_archive_transcription_20261110\codex_web_20261113\returns')
deliv = [['topic', 'package_or_folder', 'cote', 'scans', 'pages', 'words', 'open_readings', 'passes', 'read_in_sweep3', 'edition_and_translation', 'note']]


def unsure_count(text):
    return len(re.findall(r'\\unsure\{', text))


PRO = [('MPL_33_098-146', {'33': 'c33_c36_c39'}), ('MPL_33_147-181+34_002-017', {'33': 'c33_c36_c39', '34': 'c34'}),
       ('MPL_36_002-052', {'36': 'c33_c36_c39'}), ('MPL_36_053-085+39', {'36': 'c33_c36_c39', '39': 'c33_c36_c39'})]
EDN = {'33': 'ready as a transcription edition after the corrections of c33_c36_c39 (33/172 (i) is a sheaf Ext)',
       '34': 'ready after the 34:155 fix and the K34-13 second witness (c34 §16)',
       '36': 'ready for 3-8 and 28-85 once the pencil replies on 36/6-8 are printed as marginal text (c33_c36_c39)',
       '39': 'ready (c33_c36_c39)'}
for pkg, cotes in PRO:
    files = sorted(glob.glob(os.path.join(RET, pkg + '_unzipped', 'pages', '*.tex')))
    by = {}
    for fp in files:
        m = re.search(r'_(\d+)_scan(\d+)\.tex$', fp)
        if m:
            by.setdefault(m.group(1), []).append((int(m.group(2)), fp))
    for c, lst in sorted(by.items()):
        lst.sort()
        txt = ''.join(open(fp, encoding='utf-8').read() for _, fp in lst)
        scans = [n for n, _ in lst]
        deliv.append(['SA13', pkg, c, f'{min(scans)}-{max(scans)}', str(len(scans)), str(len(txt.split())), str(unsure_count(txt)),
                      'Pro transcription with notes and doubts (GPT-6 Astra, ChatGPT Pro mode); Michel Hua modern reading exists',
                      f'read in full ({cotes[c]})', EDN[c], ''])
CODEX = {'A36-01': ('36', 'c33_c36_c39', 'needs a second pass on the scans before an edition (single Codex-web witness)'),
         'A36-02': ('36', 'c33_c36_c39', 'needs a second pass on the scans before an edition (single Codex-web witness)')}
for i in range(1, 13):
    CODEX['K34-%02d' % i] = ('34', 'c34', 'second witness wanted on the doubtful places (single Codex-web witness)')
for f in ['K27-01', 'K27-02', 'K27-03', 'K28-01', 'K41-01', 'K42-01']:
    CODEX[f] = (f[1:3], 'c27_c28_c41_c42', 'ready after the open readings of c27_c28_c41_c42 and a second witness')
for f in ['K32-01', 'K32-02', 'K32-03', 'K35-01', 'K37-01', 'K37-02', 'K37-03', 'K40-01', 'K40-02']:
    note = {'32': 'cote 32: 8 typescript scans untranscribed; hands to correct (37-48 Deligne, margins Grothendieck)',
            '35': 'plan drawn in TikZ; an edition needs the arrow list as text', '37': 'about 50 typescript scans untranscribed',
            '40': 'ready'}[f[1:3]]
    CODEX[f] = (f[1:3], 'c32_c35_c37_c40', note)
for f, (c, s, ed) in sorted(CODEX.items(), key=lambda kv: (int(kv[1][0]), kv[0])):
    p = os.path.join(CW, f, 'out', f + '_transcription.tex')
    t = open(p, encoding='utf-8').read()
    sc = [int(x) for x in re.findall(r'\\scanpage\{(\d+)\}', t)]
    deliv.append(['SA13', f, c, f'{min(sc)}-{max(sc)}', str(len(sc)), str(len(t.split())), str(unsure_count(t)),
                  'Codex-web transcription (GPT Codex web at reasoning effort max) with Codex notes, doubts and Work math notes; Michel Hua modern reading exists',
                  f'read in full ({s})', ed, 'second run K34-02_2 on 34-49' if f == 'K34-02' else ''])
with open(os.path.join(S3, 'DELIVERABLES.tsv'), 'w', encoding='utf-8', newline='') as fo:
    csv.writer(fo, delimiter='\t', lineterminator='\n').writerows(deliv)
print('check events', n_ev, 'corrections', n_co, 'deliverable rows', len(deliv) - 1,
      'pages', sum(int(r[4]) for r in deliv[1:]), 'open readings', sum(int(r[6]) for r in deliv[1:]))
