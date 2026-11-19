import sys, csv
sys.path.insert(0, r"C:\Users\user\Documents\results_register\sweep2_global\tools")
import core
n = int(sys.argv[1]) if sys.argv[1].isdigit() else 700
tags = sys.argv[2:] if sys.argv[1].isdigit() else sys.argv[1:]
for t in tags:
    r = core.BYTAG.get(t)
    if not r:
        print("== MISSING", t); continue
    print(f"== {t} [{r['status_raw'][:40]}] where: {r['where_proved'][:90]} | dep: {r['depends_on'][:220]}")
    print("   ", r["statement"][:n])
    if r["notes"]: print("    notes:", r["notes"][:250])
