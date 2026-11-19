# Re-link one send folder to its build and repack (agent a6d42bf6, wave 1, 19 Nov 2026).
# usage: python -I -B relink_one.py RESEARCH_SA04 18_SA04_<short>_night
# Refuses if the folder is marked sent (__SENT) or holds anything but PROMPT.md and ZIPs; then removes those two kinds
# of files (hard links and the packed ZIP), links the build's PROMPT.md and ZIPs, packs, and lints the packed PROMPT.md.
import os, subprocess, sys
D = 'C:/Users/user/Documents/'
name, folder = sys.argv[1], sys.argv[2]
assert '__SENT' not in folder
B = D + 'pro_prompt_builds/' + name + '/'
S = D + 'TO_SEND/PRO/1_Archive_research_by_topic/' + folder
old = sorted(os.listdir(S))
assert all(f == 'PROMPT.md' or f.endswith('.zip') for f in old), old
sent = open(D + 'TO_SEND/PRO/SENT_PRO.tsv', encoding='utf-8').read()
assert folder not in sent, 'listed in SENT_PRO.tsv'
for f in old: os.remove(os.path.join(S, f))
files = [f for f in sorted(os.listdir(B)) if f == 'PROMPT.md' or f.endswith('.zip')]
for f in files: os.link(B + f, os.path.join(S, f))
print('removed', old, '; linked', files)
r = subprocess.run([sys.executable, '-I', '-B', D + 'claude_tools/prompts/pack_one_zip.py', S], capture_output=True, text=True)
print(r.stdout[-600:], r.stderr[-600:])
r = subprocess.run([sys.executable, '-I', '-B', D + 'claude_tools/push_rule_pro_prompts.py', '--lint-math', S + '/PROMPT.md'], capture_output=True, text=True)
print('lint-math (packed):', (r.stdout.strip().splitlines() or ['?'])[-1], r.stderr[-300:])
for f in sorted(os.listdir(S)): print(f, os.path.getsize(os.path.join(S, f)))
