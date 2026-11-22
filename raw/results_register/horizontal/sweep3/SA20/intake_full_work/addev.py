"""Append check events: python -I -B addev.py rows.py (ROWS = [(id, type, outcome), ...])."""
import sys, runpy
T = r"C:\Users\user\Documents\results_register\horizontal\sweep3\SA20\INTAKE_RESEARCH_SA20_20261121_full_CHECK_EVENTS.tsv"
WHO = "Claude Opus 5.5 at effort max, agent acf08879a01b97ed4, full intake of RESEARCH_SA20 (GPT-6 Astra, ChatGPT Pro mode, final 20 Nov 04:04 UTC)"
rows = runpy.run_path(sys.argv[1])["ROWS"]
with open(T, "a", encoding="utf-8") as f:
    for (i, t, o) in rows:
        f.write("\t".join(x.replace("\t", " ").replace("\n", " ") for x in (i, "2026-11-22", WHO, t, o)) + "\n")
print("appended", len(rows))
