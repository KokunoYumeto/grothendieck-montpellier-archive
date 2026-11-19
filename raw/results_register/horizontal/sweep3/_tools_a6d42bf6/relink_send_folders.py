# Replaces the contents of the two send folders by hard links to the build files, for pack_one_zip.py.
# Claude Opus 5.5 at effort max, agent a6d42bf6fe2b0d8a8, 19 Nov 2026. Usage: python -I -B relink_send_folders.py
import os
D = 'C:/Users/user/Documents/'
T = D + 'TO_SEND/PRO/1_Archive_research_by_topic/'
PAIRS = {'RESEARCH_SA11': T + '10_SA11_Stratified_spaces_cote_154_night',
         'RESEARCH_SA20': T + '12_SA20_Esquisse_cotes_121-125_155_night'}
for name, send in PAIRS.items():
    B = D + 'pro_prompt_builds/' + name + '/'
    old = sorted(os.listdir(send))
    assert set(old) <= {'PROMPT.md'} | {f for f in old if f.endswith('.zip')}, old   # only PROMPT.md and the packed ZIP
    for f in old:
        os.remove(os.path.join(send, f))
    files = [f for f in sorted(os.listdir(B)) if f == 'PROMPT.md' or f.endswith('.zip') or f == 'SA10_RESULTS_20261119.md']
    for f in files:
        os.link(B + f, os.path.join(send, f))
    print(name, 'removed', old, '; linked', files)
