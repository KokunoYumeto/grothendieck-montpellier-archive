"""Fold sweep-3 reader files into a topic folder: python -I -B integrate_readings.py SAnn
Appends the rows of readings/*_CHECK_EVENTS.tsv and *_CORRECTIONS.tsv (merged files only, not *_part*) to the topic's
CHECK_EVENTS.tsv and CORRECTIONS.tsv (columns matched by header name, duplicates skipped), and rewrites the readers
section of STUDY.md from readers_notes.py. Idempotent; rerun it after sweep3_tsv.py, which rewrites the TSVs."""
import sys, os, glob, importlib.util
sys.stdout.reconfigure(encoding="utf-8")
T = sys.argv[1]
BASE = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "..", "sweep3", T)
spec = importlib.util.spec_from_file_location("rn", os.path.join(os.path.dirname(os.path.abspath(__file__)), "readers_notes.py"))
rn = importlib.util.module_from_spec(spec); spec.loader.exec_module(rn)

def read_tsv(p):
    with open(p, encoding="utf-8") as f:
        lines = [l.rstrip("\n") for l in f if l.strip()]
    return lines[0].split("\t"), [l.split("\t") for l in lines[1:]]

def fold(kind):
    tgt = os.path.join(BASE, kind + ".tsv")
    th, trows = read_tsv(tgt)
    have = {"\t".join(r) for r in trows}
    added = 0
    for src in sorted(glob.glob(os.path.join(BASE, "readings", "*_" + kind + ".tsv"))):
        if "_part" in os.path.basename(src):
            continue
        sh, srows = read_tsv(src)
        idx = {h.strip().lower(): i for i, h in enumerate(sh)}
        if "who" in idx and "by" not in idx: idx["by"] = idx["who"]
        for r in srows:
            row = [r[idx[h.strip().lower()]] if h.strip().lower() in idx and idx[h.strip().lower()] < len(r) else "" for h in th]
            line = "\t".join(row)
            if line not in have:
                have.add(line); trows.append(row); added += 1
    with open(tgt, "w", encoding="utf-8", newline="\n") as f:
        f.write("\t".join(th) + "\n" + "".join("\t".join(r) + "\n" for r in trows))
    return added, len(trows)

out = []
for kind in ("CHECK_EVENTS", "CORRECTIONS"):
    if os.path.exists(os.path.join(BASE, kind + ".tsv")):
        out.append("%s +%d (now %d)" % ((kind,) + fold(kind)))
notes = rn.NOTES.get(T, [])
if notes:
    st = os.path.join(BASE, "STUDY.md")
    txt = open(st, encoding="utf-8").read()
    a, b = "<!-- readers:start -->", "<!-- readers:end -->"
    sec = a + "\n## Sweep 3 readers (files in readings/; rows folded into CHECK_EVENTS.tsv and CORRECTIONS.tsv)\n\n" + \
        "".join("- **readings/%s**: %s\n" % (f, s) for f, s in notes) + b
    txt = (txt[:txt.index(a)] + sec + txt[txt.index(b) + len(b):]) if a in txt else (txt.rstrip("\n") + "\n\n" + sec + "\n")
    open(st, "w", encoding="utf-8", newline="\n").write(txt)
    out.append("STUDY readers section: %d entries" % len(notes))
print(T, "; ".join(out))
