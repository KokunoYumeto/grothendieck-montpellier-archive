# Rebuilds the RESEARCH_SA09 send folder from hard links to the build files and packs it with pack_one_zip.py; keeps the
# Space paragraph (space_flat.py, key P008) that the old packed PROMPT.md carried.
# Claude Opus 5.5 at effort max, agent a34c04448e8299803, 19 Nov 2026, on the model of a6d42bf6's relink_send_folders.py.
# Usage: python -I -B relink_sa09_send_folder.py
import os, pathlib, subprocess, sys
sys.stdout.reconfigure(encoding='utf-8')
D = 'C:/Users/user/Documents/'
B = D + 'pro_prompt_builds/RESEARCH_SA09/'
SEND = pathlib.Path(D + 'TO_SEND/PRO/1_Archive_research_by_topic/09_SA09_de_Rham_cotes_137-138_night')
MARK = '**The same files in this Space.**'
old = sorted(os.listdir(SEND))
assert set(old) <= {'PROMPT.md'} | {f for f in old if f.endswith('.zip')}, old      # only PROMPT.md and the packed ZIP
space = [p for p in (SEND / 'PROMPT.md').read_text(encoding='utf-8').split('\n\n') if p.startswith(MARK)]
assert len(space) <= 1
for f in old:
    os.remove(SEND / f)
files = ['PROMPT.md', 'RESEARCH_SA09_study.zip', 'RESEARCH_SA09_transcriptions.zip', 'SA08_final_paper_tex.zip',
         'SA08_RESULTS_20261119.md']
for f in files:
    os.link(B + f, SEND / f)
print('removed', old, '; linked', files)
r = subprocess.run([sys.executable, '-I', '-B', D + 'claude_tools/prompts/pack_one_zip.py', str(SEND)],
                   capture_output=True, text=True, encoding='utf-8')
print(r.stdout.strip(), r.stderr.strip())
assert r.returncode == 0
pm = SEND / 'PROMPT.md'
assert os.stat(pm).st_nlink == 1                     # the packed PROMPT.md is its own file, not the build's
if space:
    t = pm.read_text(encoding='utf-8')
    head, rest = t.split('\n\n', 1)
    assert head.startswith('**The attached files.**') and MARK not in t
    pm.write_text(head + '\n\n' + space[0] + '\n\n' + rest, encoding='utf-8')
    print('Space paragraph kept')
print(sorted(os.listdir(SEND)))
