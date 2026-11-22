# Files attached to RESEARCH_SA04 besides the topic study (build_research_prompt.py adds the study ZIP itself).
import glob, os
D = 'C:/Users/user/Documents'
H = D + '/results_register/horizontal'
I = H + '/inputs'
CW = D + '/grothendieck_archive_transcription_20261110/codex_web_20261113/returns'
WT = D + '/grothendieck_archive_transcription_20261110/working_through_20261118'
tx = []
# the Pro transcriptions (GPT-6 Astra, ChatGPT Pro mode) with their notes and doubt tables
for pk in ('MPL_93_047-091',):   # 93/55-66 (Part C); cotes 98, 100 and 161-5 are asked in other prompts
    for suf in ('_transcription.tex', '_notes.md', '_doubts.md'):
        p = I + '/SA04/pro/' + pk + suf
        if os.path.exists(p): tx.append(('transcriptions/Pro/' + pk + suf, p))
for suf in ('_transcription.tex', '_notes.md', '_doubts.md'):   # cote 72, read for SA04 against K72
    p = I + '/SA01/pro/MPL_72_035-081' + suf
    if os.path.exists(p): tx.append(('transcriptions/Pro/MPL_72_035-081' + suf, p))
tx.append(('transcriptions/Codex/AUDIT_K_RETURNS_20261118.tsv', CW + '/../AUDIT_K_RETURNS_20261118.tsv'))
# the Codex-web transcriptions (GPT-6 Astra at reasoning effort max, Codex web), with their notes
cotes = ['69', '70', '72', '73', '74', '76', '77', '78', '79', '80', '82', '85', '86', '87', '88', '89',
         '93', '101', '161-6']
for c in ('J71', 'J75', 'J81', 'K83'):   # SA01's cotes folded into this prompt (19 Nov 2026)
    for d in sorted(glob.glob(CW + '/' + c + '-[0-9]*')):
        k = os.path.basename(d)
        for suf in ('_transcription.tex', '_mathnotes.md', '_notes.md'):
            p = d + '/out/' + k + suf
            if os.path.exists(p): tx.append(('transcriptions/Codex/' + c + '/' + k + suf, p))   # 94, 97, 98, 100, 102 and 161-5 are asked in other prompts
for c in cotes:
    for d in sorted(glob.glob(CW + '/K' + c + '-[0-9]*')):
        k = os.path.basename(d)
        for suf in ('_transcription.tex', '_mathnotes.md', '_notes.md'):
            p = d + '/out/' + k + suf
            if os.path.exists(p): tx.append(('transcriptions/Codex/K' + c + '/' + k + suf, p))
# the verdict on the working-through pilot of cote 94/2-13 (OBJ_H035)
st = []   # the H035 verdict (cote 94) belongs to the working-through prompts
SA = D + '/grothendieck_archive_transcription_20261110/stage_a_20261118_sent/returns/SA04_v2_final_20261119T0323Z_unzipped/'
for fn in ('SA04_dossier.md', 'SA04_directions.md', 'READ_ME.md'):   # the stage-A dossier of cotes 93, 98, 100, 161-5
    st.append(('study/stage_A_dossier_SA04_v2/' + fn, SA + fn))
S1 = H + '/sweep3/SA01/'
for fn in sorted(os.listdir(S1)):
    if fn.endswith(('.md', '.tsv')) and not fn.startswith('_'):
        st.append(('study/SA01/' + fn, S1 + fn))
for fn in sorted(os.listdir(S1 + 'readings')):
    if fn.startswith(('cote72', 'cotes71_75', 'cote81')):
        st.append(('study/SA01/readings/' + fn, S1 + 'readings/' + fn))
ZIPS = {'transcriptions': tx, 'study': st}
# the broad layer: the neighbouring topics (polyhedra and quadratic algebras SA01-SA03; crystals SA15; forms SA21;
# the EGA V-VI programme SA23; pseudolines SA11)
BROAD = []
for t in ('SA01', 'SA02', 'SA03'):
    for fn in ('WHAT_IS_WHERE.md', 'TOPIC_NOTES.md'):
        BROAD.append((f'broad/{t}_sweep2/{fn}', H + f'/sweep2/{t}/{fn}'))
for t in ('SA15', 'SA21', 'SA23', 'SA11'):
    for fn in ('STUDY.md', 'HUNCHES.md'):
        BROAD.append((f'broad/{t}/{fn}', H + f'/sweep3/{t}/{fn}'))
for fn in ('C_22_23_26_161-5.md', 'A2_161-4_161-6_162.md'):   # SA23's own readings of 161-5 and 161-6
    BROAD.append(('broad/SA23/readings/' + fn, H + '/sweep3/SA23/readings/' + fn))
EQUIV = ('equality; isomorphism; equivalence of categories or of fibred categories; a scheme against the functor it '
         'represents; isogeny against isomorphism; homotopy equivalence; an isomorphism of graphs or maps against an '
         'isomorphism of their flag systems')
EDGES = ('characteristic 2 and 3 and the primes dividing the discriminants; non-reduced, non-noetherian, non-normal '
         'and non-excellent bases; depth and etale depth exactly 1 and 2; rank one; the degenerate realizations '
         '(alpha = +-2, beta = -2); the small cases n <= 4; infinite families and non-compact spaces')
EXAMPLE_ID = 'SA04-R93-11'
ROLE = 'the lead of SA04 in sweep 3, wave 1, and its deep-sweep agent in sweep 1'
