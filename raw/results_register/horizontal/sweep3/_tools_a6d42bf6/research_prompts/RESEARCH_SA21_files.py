# Files attached to RESEARCH_SA21 besides the topic study (build_research_prompt.py adds the study ZIP itself).
import glob, os
D = 'C:/Users/user/Documents'
R = D + '/grothendieck_archive_transcription_20261110/codex_web_20261113/returns'
I = D + '/results_register/horizontal/inputs/SA21/pro'
tx = []
for p in sorted(glob.glob(I + '/MPL_156-1+156-2_*')):
    tx.append(('transcriptions/156-1+156-2_Pro/' + os.path.basename(p), p))
for d in sorted(glob.glob(R + '/J156-*')) + sorted(glob.glob(R + '/H156-01')):
    f = os.path.basename(d)
    for suf in ('_transcription.tex', '_doubts.md'):
        p = d + '/out/' + f + suf
        if os.path.exists(p): tx.append(('transcriptions/156_Codex_web/' + f + suf, p))
L = 'F:/user/Documents/arxiv_latex/library/idempotent_tropical_F1_semirings/math/0211133__Orthomodular Lattices and Quantales'
lit = [('literature/math0211133_Roman_Orthomodular_lattices_and_quantales/' + os.path.basename(p), p) for p in sorted(glob.glob(L + '/*'))]
ZIPS = {'transcriptions': tx, 'literature': lit}
