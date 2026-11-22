# Files attached to RESEARCH_SA02 besides the topic study (build_research_prompt.py adds the study ZIP itself).
# The quadratic-algebra cluster: cote 84 (SA02), with cote 77 (SA04) and cote 83 (SA01). Agent a6d42bf6, 19 Nov 2026.
import glob, os
D = 'C:/Users/user/Documents'
H = D + '/results_register/horizontal'
I = H + '/inputs'
CW = D + '/grothendieck_archive_transcription_20261110/codex_web_20261113/returns'
SA = D + '/grothendieck_archive_transcription_20261110/stage_a_20261118_sent/returns/SA02_part2_final_20261119T1453Z_unzipped/'
tx = []
for pk, top in (('MPL_84_097-145', 'SA02'), ('MPL_84_146-193', 'SA02'), ('MPL_83_178-222', 'SA01')):
    for suf in ('_transcription.tex', '_notes.md', '_doubts.md'):
        p = I + '/' + top + '/pro/' + pk + suf
        if os.path.exists(p): tx.append(('transcriptions/Pro/' + pk + suf, p))
for c in ('K84', 'K77', 'K83'):
    for d in sorted(glob.glob(CW + '/' + c + '-[0-9]*')):
        k = os.path.basename(d)
        for suf in ('_transcription.tex', '_mathnotes.md', '_notes.md'):
            p = d + '/out/' + k + suf
            if os.path.exists(p): tx.append(('transcriptions/Codex/' + c + '/' + k + suf, p))
tx.append(('transcriptions/Codex/AUDIT_K_RETURNS_20261118.tsv', CW + '/../AUDIT_K_RETURNS_20261118.tsv'))
st = []
for fn in ('SA02_dossier.md', 'SA02_directions.md'):   # the stage-A dossier of cotes 84, 90, 91/2-18
    if os.path.exists(SA + fn): st.append(('study/stage_A_dossier_SA02_part2/' + fn, SA + fn))
R4 = H + '/sweep3/SA04/readings/'
for fn in ('cotes76-79.md', 'cotes76-79_CHECK_EVENTS.tsv', 'cotes76-79_CORRECTIONS.tsv'):   # cote 77 is read there
    st.append(('study/SA04_cote77/' + fn, R4 + fn))
R1 = H + '/sweep3/SA01/readings/'
for fn in sorted(os.listdir(R1)):   # cote 83 is read there
    if fn.startswith('cotes83_93-92-134'):
        st.append(('study/SA01_cote83/' + fn, R1 + fn))
ZIPS = {'transcriptions': tx, 'study': st}
BROAD = []
for t in ('SA04', 'SA01'):
    for fn in ('STUDY.md', 'HUNCHES.md', 'RESEARCH_PACKAGES.md'):
        BROAD.append((f'broad/{t}/{fn}', H + f'/sweep3/{t}/{fn}'))
for t in ('SA03',):
    BROAD.append((f'broad/{t}_sweep2/WHAT_IS_WHERE.md', H + f'/sweep2/{t}/WHAT_IS_WHERE.md'))
EQUIV = ('equality; isomorphism of algebras against isomorphism of algebras with their involution; equivalence of '
         'categories or of fibred categories (stacks); torsors in the fppf and the étale topology; a monoid structure '
         'up to isomorphism against an equality of classes')
EDGES = ('characteristic 2; 2 a zero-divisor or nilpotent; non-reduced, non-noetherian and non-connected bases; '
         'non-étale and degenerate quadratic algebras (b and c in the maximal ideal); rank 1 and 2; trivial and '
         'non-trivial line bundles L; the cases chi = 1, chi = 2 and chi nilpotent')
EXAMPLE_ID = 'SA02-R84-11'
ROLE = 'the lead of SA02 in sweep 3, wave 1, and its deep-sweep agent in sweep 1'
