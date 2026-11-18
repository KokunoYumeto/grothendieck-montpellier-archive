"""After build_k_rounds78.py --build and the Chrome split (18 Nov 2026, Claude Opus 5.5 at effort high).

The main session, 18 Nov 01:3x UTC (the user: account 4's Pro prompts go to the transcription tonight): no Pro package
is moved out of packages/ or packages_chrome/, and no Work folder from the eight packages in packages_chrome/ is sent.
So this script moves no package. The round-7 folders (all 20 queued packages) and K109-01 (from .s_P181, cote 109)
are held in drag_next_held_round7_20261118/, unsplit, for the main session to decide. Only rounds 7a and 8 (pages in no
queue) go to Work:
- their ASSIGNMENTS.tsv rows are added;
- drag_split_next/ROUNDS.tsv gets round 7a right after the header (sent first) and round 8 at the end.
usage: python -I -B tools/finish_k_rounds78.py"""
import csv
import json
import pathlib
import shutil

CW = pathlib.Path(__file__).resolve().parent.parent
P = json.loads((CW / "K_ROUNDS78_PLAN_20261118.json").read_text(encoding="utf-8"))
HOLD = CW / "drag_next_held_round7_20261118"
HELD = [f for f in P["folders"] if f["round"] == 7 or f["packages"]]   # every folder cut from a queued Pro package
SEND = [f for f in P["folders"] if f not in HELD]

# 1. hold the folders cut from Pro packages
HOLD.mkdir(exist_ok=True)
for f in HELD:
    src = CW / "drag_next" / f["id"]
    if src.is_dir():
        shutil.move(str(src), str(HOLD / f["id"]))
print("held:", len(HELD), "to send:", [f["id"] for f in SEND])

# 2. ASSIGNMENTS rows of the folders that go to Work
have = {r["folder"] for r in csv.DictReader(open(CW / "ASSIGNMENTS.tsv", encoding="utf-8"), delimiter="\t")}
rows = []
for f in SEND:
    if f["id"] in have:
        continue
    what = {"7a": "batch K round 7a (gaps of cotes 70-97 % transcribed)", 8: "batch K round 8 (pages in no queue)"}[
        f["round"]]
    rows.append("\t".join([f["id"], f["cote"], ",".join(map(str, f["scans"])), str(len(f["scans"])),
                           "none: pages in no queue",
                           what + ", 18 Nov 2026 (template PROMPT_TEMPLATE_HANDWRITING_K2.md, for GPT-6.2 Astra at "
                           "reasoning effort max, ChatGPT Work)"]) + "\n")
with open(CW / "ASSIGNMENTS.tsv", "a", encoding="utf-8", newline="\n") as fh:
    fh.writelines(rows)
print("ASSIGNMENTS rows added:", len(rows))

# 3. ROUNDS.tsv
R = CW / "drag_split_next" / "ROUNDS.tsv"
lines = R.read_text(encoding="utf-8").splitlines(keepends=True)
done = {l.split("\t")[0] for l in lines[1:]}


def row(f):
    d = CW / "drag_split_next" / f["id"]
    return f"{f['id']}\t{f['round']}\t{f['cote']}\t{len(f['scans'])}\t{len(list(d.glob('*_scans_part*.zip')))}\n"


top = [row(f) for f in SEND if f["round"] == "7a" and f["id"] not in done]
end = [row(f) for f in SEND if f["round"] == 8 and f["id"] not in done]
R.write_text("".join(lines[:1] + top + lines[1:] + end), encoding="utf-8", newline="\n")
print("ROUNDS.tsv: round 7a rows at the top", len(top), "; round 8 rows at the end", len(end))
