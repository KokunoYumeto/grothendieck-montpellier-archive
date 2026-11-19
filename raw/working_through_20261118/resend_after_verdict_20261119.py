"""Rebuild the send folders after the OBJ_H035 verdict (19 Nov 2026), and set the range prompts aside.

1. For each object prompt among 002-200 of batch_20261119 (001_OBJ_H035_O is sent and is not touched): the old packed
   PROMPT.md and ZIP of its send folder in TO_SEND/PRO/F_Archive_working_through_200/ go to
   TO_SEND/_SUPERSEDED/F_working_through_objects_before_verdict_20261119/<folder>/; the new build is hard-linked in and
   packed by claude_tools/prompts/pack_one_zip.py.
2. The range pilot (033_WT_94_002-013_B, rebuilt) gets a new send folder PRO/F_Archive_working_through_200/
   00_range_pilot_first/<folder>/, first in order; its old send folder goes to _SUPERSEDED as well.
3. The other 86 range prompts (templates A and B, whose pilots of 18 Nov stopped early and were never judged) move to
   TO_SEND/_NOT_READY/F_working_through_ranges_awaiting_pilot/<folder>/; every move is recorded in
   TO_SEND/_NOT_READY/MOVED.tsv (state, path, evidence), and PRO/PROMPTS.tsv is updated.
4. Every packed PROMPT.md is linted with --lint-math; the ZIP sizes are reported.

usage: python -I -B resend_after_verdict_20261119.py [--dry]
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
SUP = TS / "_SUPERSEDED/F_working_through_objects_before_verdict_20261119"
NR = TS / "_NOT_READY/F_working_through_ranges_awaiting_pilot"
PILOT = "033_WT_94_002-013_B"
PILOT_DIR = F / "00_range_pilot_first" / PILOT
PACK = pathlib.Path("C:/Users/user/Documents/claude_tools/prompts/pack_one_zip.py")
LINT = pathlib.Path("C:/Users/user/Documents/claude_tools/push_rule_pro_prompts.py")
WHO = "Claude Opus 5.5 at effort max (agent a11a6de3), 19 Nov 2026"


def rel(p):
    return str(p.relative_to(TS)).replace("\\", "/")


def main():
    order = list(csv.DictReader(open(BATCH / "ORDER.tsv", encoding="utf-8", newline=""), delimiter="\t"))
    send = {}
    for d in F.glob("17_working_through_wave*/batch_*/*"):
        if d.is_dir():
            send[d.name] = d
    sent = {d.name for d in (TS / "_SENT/PRO/F_Archive_working_through_200").rglob("*") if d.is_dir()} \
        if (TS / "_SENT/PRO/F_Archive_working_through_200").exists() else set()
    objs = [r for r in order if r["variant"] == "O" and int(r["n"]) >= 2]
    ranges = [r for r in order if r["variant"] in ("A", "B")]
    bad = [r["folder"] for r in objs if r["lint"] != "pass"]
    if bad or len(objs) != 112 or len(ranges) != 87:
        raise SystemExit(f"ORDER.tsv not as expected: {len(objs)} objects, {len(ranges)} ranges, lint failures {bad}")
    moves, packs = [], []
    # 1-2: the rebuilt prompts
    for r in objs + [x for x in ranges if x["folder"] == PILOT]:
        name = r["folder"]
        if name in sent:
            raise SystemExit(f"{name} is in _SENT: not touched")
        old = send.get(name)
        if old is None:
            raise SystemExit(f"{name}: no send folder")
        target = PILOT_DIR if name == PILOT else old
        sup = SUP / name
        if DRY:
            print("would repack", rel(target), "from", rel(old))
            continue
        sup.mkdir(parents=True, exist_ok=True)
        for f in sorted(old.iterdir()):
            os.replace(f, sup / f.name)
        moves.append(dict(state="superseded", path=rel(old) + "/" + ",".join(sorted(p.name for p in sup.iterdir())),
                          evidence=f"the packed files before the OBJ_H035 verdict was applied; moved to {rel(sup)}; "
                                   f"the rebuilt prompt is packed in {rel(target)} ({WHO})"))
        if target != old:
            old.rmdir()
            target.mkdir(parents=True, exist_ok=True)
            moves.append(dict(state="moved", path=rel(old),
                              evidence=f"to {rel(target)}: the range pilot, first in order, rebuilt without the time "
                                       f"figure in its README (T6); the range template's pilots of 18 Nov stopped early "
                                       f"and were never judged (main session, Claude Opus 5.5 at effort max, 19 Nov "
                                       f"2026; chosen by {WHO}: the same pages as OBJ_H035, cote 94 scans 2-13)"))
        for f in sorted((BATCH / name).iterdir()):
            os.link(f, target / f.name)
        packs.append(target)
    # 3: the other range prompts
    for r in ranges:
        name = r["folder"]
        if name == PILOT:
            continue
        old = send.get(name)
        if old is None:
            raise SystemExit(f"{name}: no send folder")
        dst = NR / name
        if DRY:
            print("would move", rel(old), "->", rel(dst))
            continue
        NR.mkdir(parents=True, exist_ok=True)
        os.replace(old, dst)
        moves.append(dict(state="moved", path=rel(old),
                          evidence=f"to {rel(dst)}: a range prompt (template {r['variant']}); the range template's "
                                   f"pilots, the six WT packages of 18 Nov, stopped early and were never judged, so the "
                                   f"range prompts wait for the range pilot {PILOT} (main session, Claude Opus 5.5 at "
                                   f"effort max, 19 Nov 2026; moved by {WHO})"))
    if DRY:
        return
    for d in sorted(F.glob("17_working_through_wave*/batch_*"), reverse=True):
        if d.is_dir() and not any(d.iterdir()):
            d.rmdir()
    for d in sorted(F.glob("17_working_through_wave*")):
        if d.is_dir() and not any(d.iterdir()):
            d.rmdir()
    mv = TS / "_NOT_READY/MOVED.tsv"
    new = not mv.exists()
    with open(mv, "a", encoding="utf-8", newline="") as fh:
        w = csv.DictWriter(fh, fieldnames=["state", "path", "evidence"], delimiter="\t", lineterminator="\n")
        if new:
            w.writeheader()
        w.writerows(moves)
    # pack and lint
    for i in range(0, len(packs), 20):
        subprocess.run([sys.executable, "-I", "-B", str(PACK)] + [str(p) for p in packs[i:i + 20]], check=True)
    fails, sizes = [], []
    for p in packs:
        res = subprocess.run([sys.executable, "-I", "-B", str(LINT), "--lint-math", str(p / "PROMPT.md")],
                             capture_output=True, text=True, encoding="utf-8")
        if "failing lint: 0" not in res.stdout:
            fails.append((p.name, res.stdout[-300:]))
        files = sorted(p.iterdir())
        zs = [f for f in files if f.suffix == ".zip"]
        sizes.append((sum(f.stat().st_size for f in zs) / 1e6, p.name, len(files), [f.name for f in files]))
    # PROMPTS.tsv
    pt = TS / "PRO/PROMPTS.tsv"
    rows = list(csv.DictReader(open(pt, encoding="utf-8", newline=""), delimiter="\t"))
    keep = []
    for r in rows:
        full = TS / "PRO" / r["prompt"]
        if full.exists():
            keep.append(r)
    have = {r["prompt"] for r in keep}
    pil = str(PILOT_DIR.relative_to(TS / "PRO")).replace("\\", "/")
    if pil not in have:
        keep.insert(next((i for i, r in enumerate(keep) if r["prompt"].startswith("F_Archive_working_through_200/")),
                         len(keep)), dict(prompt=pil, files=str(len(list(PILOT_DIR.iterdir()))), state="ready"))
    for r in keep:
        full = TS / "PRO" / r["prompt"]
        if r["prompt"].startswith("F_Archive_working_through_200/"):
            r["files"] = str(len(list(full.iterdir())))
    with open(pt, "w", encoding="utf-8", newline="") as fh:
        w = csv.DictWriter(fh, fieldnames=list(rows[0].keys()), delimiter="\t", lineterminator="\n")
        w.writeheader()
        w.writerows(keep)
    sizes.sort(reverse=True)
    over = [s for s in sizes if s[0] > 100]
    print(f"packed {len(packs)}; lint failures {len(fails)} {fails[:3]}")
    print(f"over 100 MB: {len(over)}; largest: {sizes[0][1]} {sizes[0][0]:.1f} MB; total {sum(s[0] for s in sizes):.0f} MB")
    print("top 8:", [(n, round(m, 1)) for m, n, _, _ in sizes[:8]])
    print("files per folder:", sorted({k for _, _, k, _ in sizes}))
    print(f"moves recorded: {len(moves)}; PROMPTS.tsv rows {len(rows)} -> {len(keep)}")
    print("not-ready folders:", len(list(NR.iterdir())))


if __name__ == "__main__":
    main()
