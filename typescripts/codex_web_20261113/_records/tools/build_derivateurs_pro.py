"""Les Derivateurs, the folders of round D that the Work credits could not carry (18 Nov 2026), as Pro packages of
about 48 pages (three folders) for GPT-6 Astra (ChatGPT Pro mode); 30-page pairs until 18 Nov ~19:5x UTC. Written by the main session, Claude Opus 5.5 at effort max.

The user, 18 Nov 2026 ~16:2x UTC: "Or just transcription, where de Vateurs isn't yet done ... Then we just need to
finish it anyway. I mean, that's the easiest one. Just like 30-page transcription packages, which would take an hour."
The Work sender's credit guard stopped round D at 72 of 136 sent (17:26 UTC); the 64 unsent folders are in
TODO_SENDER_20261118.md.

Each package is two consecutive unsent folders of one cote. It carries the two Work task files unchanged except for
the model line, so the readings follow the same template K2 as the rest of round D, and each task still delivers its
own <ID>_out.zip: tools/file_returns.py files them like any round-D return. The package adds hourly checkpoints.

usage: python -I -B tools/build_derivateurs_pro.py            (builds every package into pro_derivateurs_20261118/)
"""
import csv
import json
import pathlib
import shutil
import subprocess
import sys

sys.stdout.reconfigure(encoding="utf-8")
CW = pathlib.Path(__file__).resolve().parent.parent
PLAN = CW / "K_DERIVATEURS_PLAN_20261118.json"
SPLIT = CW / "drag_split_next"
OUT = CW / "pro_derivateurs_20261118"
LINT = pathlib.Path.home() / "Documents/claude_tools/push_rule_pro_prompts.py"
WORK_WHO = "GPT-6.2 Astra at reasoning effort max (ChatGPT Work), run {id}"
PRO_WHO = "GPT-6 Astra (ChatGPT Pro mode), run {id}, package {pkg}"


GROUP = 3


def groups(xs, size=GROUP):
    """Consecutive folders of one cote in groups of `size`; a remainder of one folder joins the last group, a remainder
    of two is a package of its own. The user, 18 Nov 2026 ~19:5x UTC, for accounts 1-3: not 30 prompts but 15 to 20."""
    out = [xs[i:i + size] for i in range(0, len(xs), size)]
    if len(out) > 1 and len(out[-1]) == 1:
        last = out.pop()
        out[-1] = out[-1] + last
    return out


def sent_ids():
    ids = set()
    for r in csv.reader(open(CW / "SENT_K_20261117.tsv", encoding="utf-8"), delimiter="\t"):
        if r:
            ids.add(r[0].strip())
    return ids


def ranges(scans):
    out, start, prev = [], scans[0], scans[0]
    for n in scans[1:]:
        if n != prev + 1:
            out.append((start, prev))
            start = n
        prev = n
    out.append((start, prev))
    return ", ".join(f"{a}" if a == b else f"{a}-{b}" for a, b in out)


def wrapper(pkg, cote, tasks):
    n = sum(len(t["scans"]) for t in tasks)
    first, rest = tasks[0], tasks[1:]
    order = "; then ".join(f"`TASK_{t['id']}.md` ({len(t['scans'])} scans: {ranges(t['scans'])})" for t in tasks)
    zips = ", ".join(f"`{t['id']}_out.zip`" for t in tasks)
    return f"""**This file is the task: carry it out in full, now. The other attached files are its materials.**

# Pro package {pkg}: Les Dérivateurs, Alexander Grothendieck's manuscript, cote {cote}, {n} scan pages in {len(tasks)} tasks

This package holds {len(tasks)} transcription task{'s' if len(tasks) > 1 else ''} of the same manuscript file, `{cote}.pdf` of
the Montpellier archive: his handwritten notes for *Les Dérivateurs*. The tasks were written for another environment;
they come to you because its credits ran out, and they are unchanged except for the model line. Carry out every task
completely, in this order: {order}.

**Each task file governs its own pages.** Follow it exactly: its rules, its reading of the handwriting, its method
(transcription page by page, the second reading of every page, the assembly and balance check, the freeze, the
mathematical notes after the freeze) and its deliverables. Where a task file names its own scan zips, `PREAMBLE.tex`
or its own `out/` folder, it means the files of that task in this package. Finish the first task, with its
`{first['id']}_out.zip` offered as a download, before you begin the next: the tasks are sequential pages of one file,
so the notation table of the first task is where the second one starts from, and every entry is checked again on the
new pages as the task file says.

**One stream.** Read every page yourself, in order, in one stream: no parallel workers or sub-agents (the task files
say why).

**Checkpoints that survive a disconnection.** Once every hour of work, save a checkpoint ZIP of everything so far
(the `out/` folder of every task as it stands, each under its task's id: `{first['id']}/out/`, ...) to the user's
Library, or wherever files survive the loss of the execution environment, named `{pkg}_checkpoint_NN.zip`, with NN
counting up from 01; never overwrite an earlier checkpoint. Save the final out zips there too. Save checkpoints once
an hour and at no other time: none after a page, part, section, cote, folder, chapter or reader. A checkpoint is one
ZIP holding every deliverable written so far and everything that documents the work (page files, inventories,
progress logs, doubts, audits, notes), so that a new session can continue from it and the files attached to this
prompt. Leave the attached files themselves out of it, the scans you were given: we have them. It is never a JSON
file, a recovery file, a summary, or an export of the newest pages only. Each checkpoint zip holds the current
deliverables and documentation; earlier checkpoints are not copied into it. The checkpoints are what keeps the work if
this session dies: work that is in no checkpoint is lost. A checkpoint is a safety copy, not a delivery: after it, go
on with the work.

**Check events.** For every statement the mathematical notes of a task check, use or refute (a claim of his or a
remark of yours, by its place in the notes), record its check events in that task's `out/CHECK_EVENTS.tsv`, one row
per event: statement id, date, who (model, effort, run), type (targeted proof check / independent re-proof /
computation or formal certificate / used and rechecked in this run / carried as background without fault found /
refuted, with the refined statement's id), outcome. In the who column write `GPT-6 Astra (ChatGPT Pro mode), run <task
id>, package {pkg}` (the task files already say this). Give each event the type of what actually happened, neither
more nor less: reading a statement while transcribing it is not a check of it. Write "none" under the header if there
is no such event.

**Delivery.** The work is done when every task has its own out zip ({zips}), each exactly as its task file
describes, offered as downloads. Your final message gives, for each task, what its task file asks the final message to
give.
"""


def main():
    P = json.loads(PLAN.read_text(encoding="utf-8"))
    sent = sent_ids()
    unsent = [x for x in P["folders"] if x["id"] not in sent]
    by_cote = {}
    for x in unsent:
        by_cote.setdefault(x["cote"], []).append(x)
    OUT.mkdir(exist_ok=True)
    rows, bad = [], []
    for cote, xs in by_cote.items():
        for tasks in groups(xs):
            nums = [t["id"].rsplit("-", 1)[1] for t in tasks]
            pkg = f"DP{cote}_{nums[0]}-{nums[-1]}"
            d = OUT / pkg
            if d.exists():
                shutil.rmtree(d)
            d.mkdir()
            pre = None
            for t in tasks:
                src = SPLIT / t["id"]
                text = (src / "PROMPT.md").read_text(encoding="utf-8")
                old, new = WORK_WHO.format(id=t["id"]), PRO_WHO.format(id=t["id"], pkg=pkg)
                if text.count(old) != 1:
                    raise SystemExit(f"{t['id']}: model line found {text.count(old)} times")
                (d / f"TASK_{t['id']}.md").write_text(text.replace(old, new), encoding="utf-8")
                for z in sorted(src.glob(f"{t['id']}_scans_part*.zip")):
                    shutil.copy2(z, d / z.name)
                p = (src / "PREAMBLE.tex").read_bytes()
                if pre is not None and p != pre:
                    raise SystemExit(f"{pkg}: the PREAMBLE.tex files differ")
                pre = p
            (d / "PREAMBLE.tex").write_bytes(pre)
            (d / "PROMPT.md").write_text(wrapper(pkg, cote, tasks), encoding="utf-8")
            lint = subprocess.run([sys.executable, "-I", "-B", str(LINT), "--lint", str(d / "PROMPT.md")],
                                  capture_output=True, text=True)
            ok = lint.returncode == 0
            if not ok:
                bad.append(pkg)
                print("LINT FAILED", pkg, lint.stdout[-500:])
            files = sorted(p.name for p in d.iterdir())
            mb = sum(p.stat().st_size for p in d.iterdir()) / 1e6
            rows.append([pkg, cote, " ".join(t["id"] for t in tasks), sum(len(t["scans"]) for t in tasks),
                         len(files), f"{mb:.1f}", "lint ok" if ok else "LINT FAILED"])
            print(pkg, rows[-1][3], "pages,", len(files), "files,", f"{mb:.1f} MB,", rows[-1][-1])
    with open(OUT / "PACKAGES.tsv", "w", encoding="utf-8", newline="") as f:
        w = csv.writer(f, delimiter="\t", lineterminator="\n")
        w.writerow(["package", "cote", "tasks", "pages", "files", "MB", "lint"])
        w.writerows(rows)
    print("packages:", len(rows), "pages:", sum(r[3] for r in rows), "lint failed:", bad)


if __name__ == "__main__":
    main()
