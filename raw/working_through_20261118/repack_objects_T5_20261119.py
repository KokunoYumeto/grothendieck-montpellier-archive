"""Repack the 112 object send folders after T5 (19 Nov 2026): the progress check when the run judges it useful.

The user, 13:05 UTC: "Yes, the objects prompt can check whenever ... they feel like." For each object prompt among
002-200 of batch_20261119 (001 is sent; the range pilot 033 keeps the three-hour rule and is not touched): the packed
PROMPT.md and ZIP of the verdict rebuild go to TO_SEND/_SUPERSEDED/F_working_through_objects_before_T5_20261119/<folder>/,
the new build is hard-linked in and packed by claude_tools/prompts/pack_one_zip.py, and every packed PROMPT.md is
linted with --lint-math. The supersessions are recorded in TO_SEND/_NOT_READY/MOVED.tsv, as in the previous round.

usage: python -I -B repack_objects_T5_20261119.py [--dry]
Claude Opus 5.5 at effort max (agent a11a6de3), 19 Nov 2026.
"""
import csv
import os
import pathlib
import subprocess
import sys

sys.stdout.reconfigure(encoding="utf-8")
DRY = "--dry" in sys.argv
HERE = pathlib.Path(__file__).resolve().parent
BATCH = HERE / "batch_20261119"
TS = pathlib.Path("C:/Users/user/Documents/TO_SEND")
F = TS / "PRO/F_Archive_working_through_200"
SUP = TS / "_SUPERSEDED/F_working_through_objects_before_T5_20261119"
PACK = pathlib.Path("C:/Users/user/Documents/claude_tools/prompts/pack_one_zip.py")
LINT = pathlib.Path("C:/Users/user/Documents/claude_tools/push_rule_pro_prompts.py")
WHO = "Claude Opus 5.5 at effort max (agent a11a6de3), 19 Nov 2026"
HEAD = "**Progress check when the run judges it useful**"


def rel(p):
    return str(p.relative_to(TS)).replace("\\", "/")


def main():
    order = list(csv.DictReader(open(BATCH / "ORDER.tsv", encoding="utf-8", newline=""), delimiter="\t"))
    objs = [r for r in order if r["variant"] == "O" and int(r["n"]) >= 2]
    bad = [r["folder"] for r in objs if r["lint"] != "pass"]
    no_t5 = [r["folder"] for r in objs if HEAD not in (BATCH / r["folder"] / "PROMPT.md").read_text(encoding="utf-8")]
    if len(objs) != 112 or bad or no_t5:
        raise SystemExit(f"not as expected: {len(objs)} objects, lint failures {bad}, without the T5 heading {no_t5[:5]}")
    send = {d.name: d for d in F.glob("17_working_through_wave*/batch_*/*") if d.is_dir()}
    sent = {d.name for d in (TS / "_SENT/PRO").rglob("*") if d.is_dir()}
    moves, packs = [], []
    for r in objs:
        name = r["folder"]
        if name in sent:
            raise SystemExit(f"{name} is in _SENT: not touched")
        d = send.get(name)
        if d is None:
            raise SystemExit(f"{name}: no send folder")
        if DRY:
            print("would repack", rel(d))
            continue
        sup = SUP / name
        sup.mkdir(parents=True, exist_ok=True)
        for f in sorted(d.iterdir()):
            os.replace(f, sup / f.name)
        moves.append(dict(state="superseded", path=rel(d) + "/" + ",".join(sorted(p.name for p in sup.iterdir())),
                          evidence=f"the packed files of the verdict rebuild, before T5 (the progress check when the run "
                                   f"judges it useful; the user, 13:05 UTC); moved to {rel(sup)}; the rebuilt prompt is "
                                   f"packed in {rel(d)} ({WHO})"))
        for f in sorted((BATCH / name).iterdir()):
            os.link(f, d / f.name)
        packs.append(d)
    if DRY:
        return
    with open(TS / "_NOT_READY/MOVED.tsv", "a", encoding="utf-8", newline="") as fh:
        csv.DictWriter(fh, fieldnames=["state", "path", "evidence"], delimiter="\t", lineterminator="\n").writerows(moves)
    for i in range(0, len(packs), 20):
        subprocess.run([sys.executable, "-I", "-B", str(PACK)] + [str(p) for p in packs[i:i + 20]], check=True)
    fails, sizes = [], []
    for p in packs:
        res = subprocess.run([sys.executable, "-I", "-B", str(LINT), "--lint-math", str(p / "PROMPT.md")],
                             capture_output=True, text=True, encoding="utf-8")
        if "failing lint: 0" not in res.stdout or HEAD not in (p / "PROMPT.md").read_text(encoding="utf-8"):
            fails.append((p.name, res.stdout[-300:]))
        files = sorted(p.iterdir())
        sizes.append((sum(f.stat().st_size for f in files if f.suffix == ".zip") / 1e6, p.name, len(files)))
    sizes.sort(reverse=True)
    print(f"packed {len(packs)}; lint failures {len(fails)} {fails[:3]}")
    print(f"over 100 MB: {sum(1 for s in sizes if s[0] > 100)}; largest: {sizes[0][1]} {sizes[0][0]:.1f} MB; "
          f"total {sum(s[0] for s in sizes):.0f} MB; files per folder {sorted({s[2] for s in sizes})}")
    print(f"supersessions recorded: {len(moves)}")


if __name__ == "__main__":
    main()
