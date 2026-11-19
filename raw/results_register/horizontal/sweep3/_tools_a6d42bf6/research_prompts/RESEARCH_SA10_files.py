# Files attached to RESEARCH_SA10 besides the topic study (build_research_prompt.py adds the study ZIP itself).
import glob, os
D = 'C:/Users/user/Documents'
SP = D + '/grothendieck_archive_transcription_20261110/second_pass/out'
I = D + '/results_register/horizontal/inputs/SA10/pro'
tx = []
for pk in ('MPL_150_001-043', 'MPL_150_044-084', 'MPL_150_085-099+151_001-031', 'MPL_151_032-075'):
    for p in sorted(glob.glob(SP + '/' + pk + '/*')):
        tx.append(('transcriptions/second_pass_17Nov/' + pk + '/' + os.path.basename(p), p))
    for suf in ('_notes.md', '_doubts.md'):
        p = I + '/' + pk + suf
        if os.path.exists(p): tx.append(('transcriptions/first_pass_Pro_notes/' + pk + suf, p))
ZIPS = {'transcriptions': tx}
