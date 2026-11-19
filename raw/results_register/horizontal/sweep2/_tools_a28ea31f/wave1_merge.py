"""Wave-1 merge: build a topic's HUNCHES.md, RESEARCH_PACKAGES.md, DEPENDS.tsv and DELIVERABLES.tsv from the readers'
files in sweep3/SAnn/readings/<stretch>.md, and create the CHECK_EVENTS/CORRECTIONS headers that
integrate_readings.py folds into. Usage: python -I -B wave1_merge.py SAnn stretch [stretch ...]"""
import sys, os, re
sys.stdout.reconfigure(encoding="utf-8")
T, stretches = sys.argv[1], sys.argv[2:]
BASE = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "..", "sweep3", T)
RD = os.path.join(BASE, "readings")
WHO = "Claude Opus 5.5 at effort max, a28ea31fa17dd65e1, sweep 3 wave 1 (merge)"


def sections(md):
    """[(heading, body)] for the top-level '## ' sections."""
    out, cur, buf = [], None, []
    for line in md.splitlines():
        if line.startswith("## "):
            if cur is not None:
                out.append((cur, "\n".join(buf).strip("\n")))
            cur, buf = line[3:].strip(), []
        elif cur is not None:
            buf.append(line)
    if cur is not None:
        out.append((cur, "\n".join(buf).strip("\n")))
    return out


def pick(secs, *keys):
    for h, b in secs:
        hl = h.lower()
        if any(k in hl for k in keys):
            return h, b
    return None, ""


hun, pkg, dep_rows, del_rows = [], [], [], []
for s in stretches:
    p = os.path.join(RD, s + ".md")
    md = open(p, encoding="utf-8").read()
    secs = sections(md)
    h, b = pick(secs, "hunch")
    if b:
        hun.append("## From readings/%s.md (%s)\n\n%s\n" % (s, h, b))
    h, b = pick(secs, "research package")
    if b:
        pkg.append("## From readings/%s.md (%s)\n\n%s\n" % (s, h, b))
    h, b = pick(secs, "dependenc")
    if b:
        items = re.split(r"\n(?=- )", "\n" + b)
        for it in items:
            it = " ".join(it.split())
            if not it.startswith("- "):
                continue
            ids = re.findall(r"SA\d\d-\d+", it)
            if not ids:
                continue
            rel = "used by" if re.search(r"\bused by\b|\bis used\b", it[:200]) else "uses"
            dep_rows.append((ids[0], rel, ", ".join(dict.fromkeys(ids[1:])), it[2:].replace("\t", " "), s))
    h, b = pick(secs, "deliverable")
    if b:
        for line in b.splitlines():
            if line.startswith("|") and not re.match(r"^\|\s*-", line) and not re.search(r"\|\s*(Scans?|Scan range)\s*\|", line):
                cells = [c.strip() for c in line.strip().strip("|").split("|")]
                if len(cells) >= 4:
                    del_rows.append((s, cells[0], cells[1], cells[2], " | ".join(cells[3:])))

hdr = "# %s: %s (sweep 3, wave 1)\n\nMerged by %s from the readers' files in readings/. Each section is the reader's text, unchanged.\n\n"
open(os.path.join(BASE, "HUNCHES.md"), "w", encoding="utf-8", newline="\n").write(hdr % (T, "hunches", WHO) + "\n".join(hun))
open(os.path.join(BASE, "RESEARCH_PACKAGES.md"), "w", encoding="utf-8", newline="\n").write(hdr % (T, "research packages (concepts)", WHO) + "\n".join(pkg))
with open(os.path.join(BASE, "DEPENDS.tsv"), "w", encoding="utf-8", newline="\n") as f:
    f.write("item\trelation\tother_items\ttext\tsource\n")
    for r in dep_rows:
        f.write("\t".join(r) + "\n")
with open(os.path.join(BASE, "DELIVERABLES.tsv"), "w", encoding="utf-8", newline="\n") as f:
    f.write("stretch\tscans\tpasses\topen_readings\tready_for_edition\n")
    for r in del_rows:
        f.write("\t".join(x.replace("\t", " ") for x in r) + "\n")
for name, head in (("CHECK_EVENTS.tsv", "id\tdate_utc\twho\thow\tresult\twhere\n"),
                   ("CORRECTIONS.tsv", "where\twhat\tcorrection\treason\tby\n")):
    p = os.path.join(BASE, name)
    if not os.path.exists(p):
        open(p, "w", encoding="utf-8", newline="\n").write(head)
print(T, "hunch sections", len(hun), "package sections", len(pkg), "depends", len(dep_rows), "deliverables", len(del_rows))
