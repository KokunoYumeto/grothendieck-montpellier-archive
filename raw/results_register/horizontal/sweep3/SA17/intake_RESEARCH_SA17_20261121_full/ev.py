"""Append check events to the full-intake TSV of RESEARCH_SA17 (Claude Opus 5.5 at effort max, agent
ac8bd2a26d00b4f37). Reads lines 'id|code|outcome' from stdin. Codes: T targeted proof check; R independent re-proof;
K computation or formal certificate; U used and rechecked in this run; C carried as background without fault found;
X refuted, with the refined statement's id; S statement read only, not checked.
usage: python -I -B ev.py <CHECK_EVENTS.tsv>"""
import datetime
import pathlib
import sys

TYPES = {"T": "targeted proof check", "R": "independent re-proof", "K": "computation or formal certificate",
         "U": "used and rechecked in this run", "C": "carried as background without fault found",
         "X": "refuted, with the refined statement's id", "S": "statement read only; not checked"}
WHO = "Claude Opus 5.5 at effort max (agent ac8bd2a26d00b4f37, full intake of RESEARCH_SA17 cp12)"
tsv = pathlib.Path(sys.argv[1])
new = not tsv.exists()
ids = set(open("ids_221.txt", encoding="utf-8").read().split())
date = datetime.datetime.now(datetime.timezone.utc).strftime("%Y-%m-%d")
n = 0
with open(tsv, "a", encoding="utf-8", newline="\n") as f:
    if new:
        f.write("statement_id\tdate\twho\ttype\toutcome\n")
    for line in sys.stdin:
        line = line.strip()
        if not line:
            continue
        sid, code, out = (p.strip() for p in line.split("|", 2))
        if sid not in ids:
            print("WARNING not in the 221 list:", sid)
        f.write(f"{sid}\t{date}\t{WHO}\t{TYPES[code]}\t{out}\n")
        n += 1
done = {l.split("\t")[0] for l in open(tsv, encoding="utf-8").read().splitlines()[1:]}
print("appended", n, "| ids with an event:", len(done & ids), "of", len(ids))
