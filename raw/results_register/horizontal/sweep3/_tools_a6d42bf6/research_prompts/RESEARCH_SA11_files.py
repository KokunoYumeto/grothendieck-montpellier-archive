# Files attached to RESEARCH_SA11 besides the topic study (build_research_prompt.py adds the study ZIP itself).
import glob, os
D = 'C:/Users/user/Documents'
I = D + '/results_register/horizontal/inputs'
tx = []
for pk in ('MPL_154_001-045', 'MPL_81_038-055+154_046-076', 'MPL_154_077-126', 'MPL_154_127-176'):
    for suf in ('_transcription.tex', '_notes.md', '_doubts.md'):
        p = I + '/SA11/pro/' + pk + suf
        if os.path.exists(p): tx.append(('transcriptions/154_Pro/' + pk + suf, p))
for p in sorted(glob.glob(I + '/SA11/codex/K154-0*')):
    tx.append(('transcriptions/154_Codex/' + os.path.basename(p), p))
for pk in ():  # cote 121 is asked in RESEARCH_SA20
    for base in (I + '/SA20/pro/', I + '/SA11/pro/'):
        for suf in ('_transcription.tex', '_notes.md', '_doubts.md'):
            p = base + pk + suf
            if os.path.exists(p): tx.append(('transcriptions/121_Pro/' + pk + suf, p))
R20 = D + '/results_register/horizontal/sweep3/SA20/readings'
other = [] and [('study/readings_SA20/' + os.path.basename(p), p) for p in sorted(glob.glob(R20 + '/121_049-073_153_155*') + glob.glob(R20 + '/121_001-048*') + glob.glob(R20 + '/152_120*')) if os.path.isfile(p)]
ZIPS = {'transcriptions': tx, 'study': other}
