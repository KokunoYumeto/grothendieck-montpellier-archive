import sys, os
# usage: apply.py first_pass.tex out.tex edits.txt
# edits.txt: blocks of the form
# @@ [count]
# old text (one or more lines)
# ==
# new text
# @@end
src, out, ed = sys.argv[1], sys.argv[2], sys.argv[3]
t = open(src, encoding='utf-8').read()
blocks = open(ed, encoding='utf-8').read().split('@@end')
n = 0
for b in blocks:
    if '@@' not in b:
        continue
    head, body = b.split('@@', 1)[1].split('\n', 1)
    cnt = int(head.strip()) if head.strip() else 1
    old, new = body.split('\n==\n', 1)
    if new.endswith('\n'):
        new = new[:-1]
    c = t.count(old)
    if c != cnt:
        print('COUNT MISMATCH', c, 'expected', cnt, 'for:', repr(old[:80]))
        sys.exit(1)
    t = t.replace(old, new)
    n += 1
os.makedirs(os.path.dirname(out), exist_ok=True)
if os.path.exists(out):
    print('REFUSING: output exists', out)
    sys.exit(1)
open(out, 'w', encoding='utf-8', newline='\n').write(t)
print(n, 'edits applied ->', out)
