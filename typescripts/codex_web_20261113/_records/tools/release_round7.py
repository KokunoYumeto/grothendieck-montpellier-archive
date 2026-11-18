"""Release batch K round 7 to Work (18 Nov 2026, the main session, Claude Opus 5.5 at effort max).

Rounds 2-6, 7a and 8 were all sent by 07:59 UTC; the account-4 credits last to about 11:45 UTC. Round 7 (the 54 Work
folders cut from the 20 queued Pro transcription packages, held in drag_next_held_round7_20261118/) goes to Work as
the second witness of those pages (PLAN_WORKING_THROUGH_PRO section 0a: every Pro-transcribed page gets a Work
reading). The Pro packages stay in the Pro queue; nothing is moved out of packages_chrome/.

Order: the folders of the packages Pro reaches last go first (reverse of the Pro order), then those Pro has done.
Per folder: split for Chrome into drag_split_next/<ID>/ (tools/split_for_chrome.py), add a ROUNDS.tsv row (round 7),
add an ASSIGNMENTS.tsv row, and move the original from the hold folder to drag_next/ (where the filer looks).
usage: python -I -B tools/release_round7.py"""
import csv, json, pathlib, re, shutil, subprocess, sys

CW = pathlib.Path(__file__).resolve().parent.parent
HOLD = CW / "drag_next_held_round7_20261118"
P = json.loads((CW / "K_ROUNDS78_PLAN_20261118.json").read_text(encoding="utf-8"))
folders = {f["id"]: f for f in P["folders"] if f["round"] == 7 or f.get("packages")}
PRO_ORDER = ["P073", "P075", "P076", "P056", "P052", "P072", "P097", "P121", "P135", "P158", "P160", "P161", "P179",
             "P181", "P069", "P067", "P064", "P071", "P074", "P055"]
DONE_OR_RUNNING = {"P073", "P075", "P076", "P056", "P052"}


def pnum(pkg):
    m = re.search(r"(P\d{3})", pkg or "")
    return m.group(1) if m else ""


def key(f):
    p = pnum(f.get("package") or (f.get("packages") or [""])[0])
    if p in DONE_OR_RUNNING:
        return (1, PRO_ORDER.index(p), f["id"])
    rank = PRO_ORDER.index(p) if p in PRO_ORDER else len(PRO_ORDER)
    return (0, -rank, f["id"])


order = [f for f in sorted(folders.values(), key=key) if (HOLD / f["id"]).is_dir()]
ids = [f["id"] for f in order]
r = subprocess.run([sys.executable, "-I", "-B", str(CW / "tools" / "split_for_chrome.py"), "--dst", "drag_split_next",
                    "drag_next_held_round7_20261118"] + ids, capture_output=True, text=True, cwd=str(CW))
print(r.stdout[-1500:], r.stderr[-800:])
rounds = CW / "drag_split_next" / "ROUNDS.tsv"
have = {row[0] for row in csv.reader(open(rounds, encoding="utf-8"), delimiter="\t")}
assign = CW / "ASSIGNMENTS.tsv"
have_a = {row[0] for row in csv.reader(open(assign, encoding="utf-8"), delimiter="\t")}
with open(rounds, "a", encoding="utf-8", newline="") as fr, open(assign, "a", encoding="utf-8", newline="") as fa:
    wr, wa = csv.writer(fr, delimiter="\t", lineterminator="\n"), csv.writer(fa, delimiter="\t", lineterminator="\n")
    for f in order:
        ID = f["id"]
        parts = len(list((CW / "drag_split_next" / ID).glob(f"{ID}_scans_part*.zip")))
        if parts == 0:
            print("NOT SPLIT:", ID); continue
        if ID not in have:
            wr.writerow([ID, "7", f["cote"], len(f["scans"]), parts])
        if ID not in have_a:
            wa.writerow([ID, f["cote"], ",".join(str(s) for s in f["scans"]), len(f["scans"]),
                         f.get("package") or "", "batch K round 7, 18 Nov 2026: Work reading of a Pro package's pages "
                         "(second witness; the package is also sent or queued to Pro on account 4); template "
                         "PROMPT_TEMPLATE_HANDWRITING_K2.md, for GPT-6.2 Astra Max"])
        dst = CW / "drag_next" / ID
        if not dst.exists():
            shutil.move(str(HOLD / ID), str(dst))
print("released", len(order), "folders in this order:", " ".join(ids))
