# Appends full-intake check events read from stdin to a CHECK_EVENTS table.
# Input lines: id <TAB-or-||> type-code <||> outcome <||> where ; type codes TP, IR, CO, BG, UR (used and rechecked), RF.
# Usage: python -I -B append_events.py <table.tsv> <run label>  (lines on stdin, fields separated by ' || ')
# Claude Opus 5.5 at effort max, agent a34c04448e8299803, 22 Nov 2026.
import sys
sys.stdout.reconfigure(encoding='utf-8'); sys.stdin.reconfigure(encoding='utf-8')
T, run = sys.argv[1], sys.argv[2]
W = 'Claude Opus 5.5 at effort max, agent a34c04448e8299803, full intake (21-22 Nov 2026) of ' + run + ' (GPT-6 Astra, ChatGPT Pro mode)'
TY = {'TP': 'targeted proof check', 'IR': 'independent re-proof', 'CO': 'computation or formal certificate',
      'BG': 'carried as background without fault found', 'UR': 'used and rechecked in this run',
      'RF': "refuted, with the refined statement's id"}
n = 0
with open(T, 'a', encoding='utf-8', newline='') as f:
    for line in sys.stdin:
        line = line.strip()
        if not line or line.startswith('#'):
            continue
        sid, typ, out, where = [x.strip() for x in line.split(' || ')]
        f.write('\t'.join([sid, '2026-11-22', W, TY[typ], out.replace('\t', ' '), where]) + '\n')
        n += 1
print('appended', n)
