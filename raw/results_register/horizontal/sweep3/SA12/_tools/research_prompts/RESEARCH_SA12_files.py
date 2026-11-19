# Files attached to RESEARCH_SA12 besides the topic study (the builder adds the study and broad ZIPs).
# SA12 lead a65dbdc241d1a129a (Claude Opus 5.5 at effort max), 19 Nov 2026. Text and LaTeX only, no scans.
import glob, os
D = 'C:/Users/user/Documents'
T = D + '/grothendieck_archive_transcription_20261110'
R = T + '/codex_web_20261113/returns'
tx = []
for pkg in ('MPL_29_049-094', 'MPL_29_095-140', 'MPL_29_141-187', 'MPL_31_002-051', 'MPL_33_002-049', 'MPL_33_050-097'):
    for suf in ('_transcription.tex', '_notes.md', '_doubts.md'):
        hits = [p for p in glob.glob(T + '/returns/' + pkg + '_unzipped/**/' + pkg + suf, recursive=True)
                if '_checkpoint_' not in p.replace('\\', '/')]
        hits.sort(key=len)
        if hits:
            tx.append(('transcriptions/Pro_' + pkg + '/' + pkg + suf, hits[0]))
CODEX = ['A29-01'] + ['C29-0%d' % i for i in range(1, 8)] + ['K29-%02d' % i for i in range(1, 12)] + \
        ['K31-0%d' % i for i in range(1, 4)] + ['B37-0%d' % i for i in range(1, 6)] + ['C32-01', 'H35-01', 'H37-01']
for f in CODEX:
    for suf in ('_transcription.tex', '_notes.md', '_doubts.md', '_mathnotes.md'):
        p = R + '/' + f + '/out/' + f + suf
        if os.path.exists(p):
            tx.append(('transcriptions/Codex_' + f + '/' + f + suf, p))
S2 = D + '/results_register/horizontal/sweep2'
study_extra = [('study/sweep2/' + n, S2 + '/SA12/' + n) for n in ('OBJECTS.tsv', 'FLAGS.tsv', 'TOPIC_NOTES.md')]
study_extra.append(('study/sweep2/SA12_scan_readings.md', S2 + '/REPORTS/SA12_scan_readings.md'))
ZIPS = {'transcriptions': tx, 'study': study_extra}
