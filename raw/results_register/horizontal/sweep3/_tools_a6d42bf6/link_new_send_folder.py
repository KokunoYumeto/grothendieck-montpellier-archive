# Link a built research prompt into a new send folder and pack it (agent a6d42bf6, wave 1, 19 Nov 2026).
# usage: python -I -B link_new_send_folder.py RESEARCH_SA04 18_SA04_<short>_night
# The send folder must not exist yet. Hard links to the build's PROMPT.md and ZIPs, then pack_one_zip.py, then the lint.
import os, subprocess, sys
D = 'C:/Users/user/Documents/'
name, folder = sys.argv[1], sys.argv[2]
B = D + 'pro_prompt_builds/' + name + '/'
S = D + 'TO_SEND/PRO/1_Archive_research_by_topic/' + folder
assert not os.path.exists(S), 'exists: ' + S
os.makedirs(S)
files = [f for f in sorted(os.listdir(B)) if f == 'PROMPT.md' or f.endswith('.zip')]
for f in files:
    os.link(B + f, os.path.join(S, f))
print('linked', files)
r = subprocess.run([sys.executable, '-I', '-B', D + 'claude_tools/prompts/pack_one_zip.py', S], capture_output=True, text=True)
print(r.stdout[-1500:], r.stderr[-800:])
r = subprocess.run([sys.executable, '-I', '-B', D + 'claude_tools/push_rule_pro_prompts.py', '--lint-math', S + '/PROMPT.md'], capture_output=True, text=True)
print('lint-math (packed):', (r.stdout.strip().splitlines() or ['?'])[-1], r.stderr[-300:])
for f in sorted(os.listdir(S)):
    print(f, os.path.getsize(os.path.join(S, f)))
