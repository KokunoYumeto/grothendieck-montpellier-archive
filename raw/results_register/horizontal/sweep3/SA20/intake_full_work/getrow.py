"""Print the statement and proof of a RESEARCH_SA20 register id from the return (read-only).
Usage: python -I -B getrow.py ID [maxlines]
Claude Opus 5.5 at effort max, agent acf08879a01b97ed4, full intake, 22 Nov 2026."""
import sys, os, re
sys.stdout.reconfigure(encoding="utf-8")
ROOT = r"C:\Users\user\Documents\grothendieck_archive_transcription_20261110\research_returns\RESEARCH_SA20_final_20261120T0404Z_unzipped\RESEARCH_SA20"
rid = sys.argv[1]
mx = int(sys.argv[2]) if len(sys.argv) > 2 else 400
BEG = "\\begin{saresult}"
pat = BEG + "{" + rid + "}"
hits = []
for dp, dn, fn in os.walk(ROOT):
    parts = dp.split(os.sep)
    if "logs" in parts or "_from_earlier_checkpoints" in parts:
        continue
    for f in fn:
        if f.endswith(".tex"):
            p = os.path.join(dp, f)
            try:
                L = open(p, encoding="utf-8").read().split("\n")
            except Exception:
                continue
            for i, l in enumerate(L):
                if pat in l:
                    hits.append((p, i, L))
if not hits:
    print("NOT FOUND", rid)
    sys.exit()
p, i, L = hits[0]
print("##", rid, "at", os.path.relpath(p, ROOT) + ":" + str(i + 1), "(other hits: %d)" % (len(hits) - 1))
out = []
for j in range(i, min(len(L), i + mx)):
    l = L[j]
    if j > i and (BEG in l or l.startswith("\\subsection") or l.startswith("\\section")):
        break
    l = re.sub(r"(?<!\\)%.*$", "", l)
    if l.strip():
        out.append(l)
print("\n".join(out))
