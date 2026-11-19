# Rebuild one topic's sweep-3 tables in the right order (agent a6d42bf6, horizontal sweep 3, 19 Nov 2026):
#   1. write_tables.py from cfg_<topic>.py (this agent's own rows)
#   2. merge_readings.py (the readers' rows and INTEGRATION blocks)
#   3. add_translation_targets.py (translate_to, why)
# usage: python -I -B rebuild.py SA10|SA11|SA21 [...]
import os, subprocess, sys
sys.stdout.reconfigure(encoding='utf-8')
T = os.path.dirname(os.path.abspath(__file__)); S = os.path.dirname(T)
for topic in sys.argv[1:]:
    d = os.path.join(S, topic)
    for args in (['write_tables.py', os.path.join(T, 'cfg_%s.py' % topic), d], ['merge_readings.py', d], ['add_translation_targets.py', d]):
        r = subprocess.run([sys.executable, '-I', '-B', os.path.join(T, args[0])] + args[1:], capture_output=True, text=True, encoding='utf-8')
        out = [l for l in r.stdout.splitlines() if not l.startswith('merged ')]
        print(topic, args[0], '|', '; '.join(out), r.stderr.strip()[-300:])
        if r.returncode: sys.exit(r.returncode)
