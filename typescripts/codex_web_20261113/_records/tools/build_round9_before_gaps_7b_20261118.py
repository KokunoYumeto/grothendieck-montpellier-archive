"""Batch K round 9 for GPT-6.2 Astra at reasoning effort max (ChatGPT Work), 18 Nov 2026. Written by the main
session, Claude Opus 5.5 at effort max.

PLAN_WORKING_THROUGH_PRO_20261118.md section 0a: reading the ink belongs to Work; pages Pro transcribed get a second
reading from Work, so that each page has two witnesses; the second readings run in the order of the mathematical
pass. Round 7 gives that reading to the pages of the 20 Pro packages queued tonight. Round 9 gives it to the pages Pro
transcribed before tonight: the Pro packages of the topic dossiers (stage_a_20261118/STAGE_A_PACKAGES.tsv), in the
order of the mathematical pass (section 5): the pilot's cote 22 first (MPL_22+23_002-016), then topic by topic in the
dossiers' order (the topics the vertical work never touched first, then Pursuing Stacks, then the Longue Marche, then
the Derivateurs), and within a topic the packages in the order listed there.

Per package: the (cote, scan) pairs its name stands for, minus every scan that already has a Work or Codex reading
(ASSIGNMENTS.tsv, packages_work/CODEX_COVERED_SCANS.tsv, the K plans), an API page file or a round-9 folder, minus
blank scans and the IMAG logo sheet (the tests of rounds 7-8); cut per cote into folders of at most 16 scans; ids
continue each cote's K numbering. Each folder is a blind reading on template K2 (Hua's text as a witness after the
freeze, where he has the pages); Pro's reading is not shown.

usage: python -I -B tools/build_round9.py --plan [MAX]   (plans new folders package by package, stopping at the first
                                                         package boundary past MAX new folders; appends to
                                                         K_ROUND9_PLAN_20261118.json)
       python -I -B tools/build_round9.py --build N      (builds the next N planned folders into drag_next/, writes
                                                         PROMPT.md, splits them for Chrome into drag_split_next/,
                                                         appends ROUNDS.tsv and ASSIGNMENTS.tsv rows, lints them)
"""
import csv
import json
import pathlib
import re
import subprocess
import sys
import tempfile

HERE = pathlib.Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
import build_k_rounds78 as R  # noqa: E402

K, B, CW, T = R.K, R.B, R.CW, R.T
PLAN9 = CW / "K_ROUND9_PLAN_20261118.json"
SA = T / "stage_a_20261118" / "STAGE_A_PACKAGES.tsv"
PILOT = "MPL_22+23_002-016"
LINT = pathlib.Path.home() / "Documents/claude_tools/push_rule_pro_prompts.py"
WHAT = ("batch K round 9, 18 Nov 2026: Work second reading of pages Pro transcribed before tonight "
        "(PLAN_WORKING_THROUGH_PRO 0a: two witnesses a page), blind (Pro's reading not shown); template "
        "PROMPT_TEMPLATE_HANDWRITING_K2.md, for GPT-6.2 Astra Max")


def package_order():
    names = [PILOT]
    for r in csv.DictReader(open(SA, encoding="utf-8"), delimiter="\t"):
        for n in r["packages"].split():
            if n not in names:
                names.append(n)
    return names


def have_reading(P9):
    got = {}
    for r in csv.DictReader(open(T / "packages_work/CODEX_COVERED_SCANS.tsv", encoding="utf-8"), delimiter="\t"):
        got.setdefault((r["cote"], int(r["scan"])), "Codex web " + r["folder"])
    for r in csv.DictReader(open(CW / "ASSIGNMENTS.tsv", encoding="utf-8"), delimiter="\t"):
        for n in re.findall(r"\d+", r["scans"]):
            got.setdefault((r["cote"], int(n)), "Work " + r["folder"])
    for d in (T / "api_typescripts_20261112").iterdir():
        for f in (d / "pages").glob("*.tex") if (d / "pages").is_dir() else []:
            m = re.match(r"^[a-z0-9]+_(.+)_(\d{3})\.tex$", f.name)
            if m:
                got.setdefault((m.group(1), int(m.group(2)) + 1), "API " + d.name)
    plans = json.loads(K.PLAN_JSON.read_text(encoding="utf-8"))["folders"]
    plans += json.loads(R.PLAN78.read_text(encoding="utf-8"))["folders"]
    for f in plans + P9["folders"]:
        for n in f["scans"]:
            got.setdefault((f["cote"], n), "K " + f["id"])
    return got


def load():
    if PLAN9.exists():
        return json.loads(PLAN9.read_text(encoding="utf-8"))
    return dict(order=[], done_packages=[], already_read={}, folders=[], blank={}, logo={}, missing_image={},
                unparsed=[])


def plan(maxnew):
    P9 = load()
    P78 = json.loads(R.PLAN78.read_text(encoding="utf-8"))
    pages = P78["pages_per_cote"]
    got = have_reading(P9)
    cache = json.loads(R.CACHE.read_text(encoding="utf-8")) if R.CACHE.exists() else {}
    with tempfile.TemporaryDirectory() as tmp:
        ref = R.thumb(B.page_image(R.pdf_of(R.LOGO_REF[0]), R.LOGO_REF[1], tmp))
    ids = R.existing_ids() | {f["id"] for f in P9["folders"]}
    P9["order"] = package_order()
    new = 0
    for name in P9["order"]:
        if name in P9["done_packages"]:
            continue
        if maxnew and new >= maxnew:
            break
        keys, bad = R.name_ranges(name, pages)
        if bad:
            P9["unparsed"].append([name, bad])
        free, nread = {}, 0
        for k in sorted(keys, key=lambda k: (k[0], k[1])):
            if k in got:
                nread += 1
                continue
            free.setdefault(k[0], []).append(k[1])
        P9["already_read"][name] = nread
        cotes = list(dict.fromkeys(m.group(1) for m in re.finditer(r"(?:MPL_|\+)(\d+(?:-\d{1,2})?)", name)))
        for cote in sorted(free, key=lambda c: cotes.index(c) if c in cotes else len(cotes)):
            scans = sorted(free[cote])
            info = R.scan_info(cote, scans, cache, ref)
            live = []
            for n in scans:
                ink, dist = info[n]
                if ink < 0:
                    P9["missing_image"].setdefault(cote, []).append(n)
                elif ink < 0.0003:
                    P9["blank"].setdefault(cote, []).append(n)
                elif dist < 12:
                    P9["logo"].setdefault(cote, []).append(n)
                else:
                    live.append(n)
            j = R.next_index(cote, ids)
            for part in (K.chunks(live) if live else []):
                fid = f"K{cote}-{j:02d}"
                ids.add(fid)
                P9["folders"].append(dict(id=fid, cote=cote, scans=part, round=9, package=name, packages=[name]))
                for n in part:
                    got[(cote, n)] = "K " + fid
                new += 1
                j += 1
        P9["done_packages"].append(name)
        PLAN9.write_text(json.dumps(P9, indent=1, ensure_ascii=False), encoding="utf-8")
    left = [n for n in P9["order"] if n not in P9["done_packages"]]
    print(f"new folders: {new}; planned in all: {len(P9['folders'])} folders, "
          f"{sum(len(f['scans']) for f in P9['folders'])} pages; packages planned {len(P9['done_packages'])}, "
          f"left {len(left)}; unparsed: {P9['unparsed']}")


def built(fid):
    return any((CW / b / fid).is_dir() for b in ("drag", "drag_next", "done", "drag_split_next"))


def build(n):
    import k_material  # noqa: E402
    P9 = load()
    allk = (json.loads(K.PLAN_JSON.read_text(encoding="utf-8"))["folders"]
            + json.loads(R.PLAN78.read_text(encoding="utf-8"))["folders"] + P9["folders"])
    todo = [x for x in P9["folders"] if not built(x["id"])][:n]
    recs, failed = [], []
    for x in todo:
        try:
            mat = k_material.sentence(x)
        except KeyError:
            mat = None
        try:
            r = K.build_next(x["id"], x["cote"], x["scans"], mat or "")
        except SystemExit as e:
            failed.append((x["id"], str(e)))
            print("FOLDER FAILED:", x["id"], e, flush=True)
            continue
        if r:
            r["round"] = 9
            recs.append(K.add_hua(x, r))
            (CW / "drag_next" / x["id"] / "PROMPT.md").write_bytes(K.make_prompt(x, allk).encode("utf-8"))
    with open(HERE / "BUILD_LOG.jsonl", "a", encoding="utf-8") as f:
        for r in recs:
            f.write(json.dumps(r, ensure_ascii=False) + "\n")
    ids = [r["id"] for r in recs]
    if not ids:
        print("nothing built; failed:", failed)
        return
    s = subprocess.run([sys.executable, "-I", "-B", str(HERE / "split_for_chrome.py"), "--dst", "drag_split_next",
                        "drag_next"] + ids, capture_output=True, text=True, cwd=str(CW))
    print(s.stdout[-1200:], s.stderr[-600:])
    rounds = CW / "drag_split_next" / "ROUNDS.tsv"
    have = {row[0] for row in csv.reader(open(rounds, encoding="utf-8"), delimiter="\t")}
    assign = CW / "ASSIGNMENTS.tsv"
    have_a = {row[0] for row in csv.reader(open(assign, encoding="utf-8"), delimiter="\t")}
    byid = {x["id"]: x for x in todo}
    bad = []
    with open(rounds, "a", encoding="utf-8", newline="") as fr, open(assign, "a", encoding="utf-8", newline="") as fa:
        wr, wa = csv.writer(fr, delimiter="\t", lineterminator="\n"), csv.writer(fa, delimiter="\t", lineterminator="\n")
        for fid in ids:
            x = byid[fid]
            parts = len(list((CW / "drag_split_next" / fid).glob(f"{fid}_scans_part*.zip")))
            if parts == 0:
                print("NOT SPLIT:", fid)
                bad.append(fid)
                continue
            lint = subprocess.run([sys.executable, "-I", "-B", str(LINT), "--lint-codex",
                                   str(CW / "drag_split_next" / fid / "PROMPT.md")], capture_output=True, text=True)
            if lint.returncode != 0:
                print("LINT FAILED:", fid, lint.stdout[-400:], lint.stderr[-200:])
                bad.append(fid)
                continue
            if fid not in have:
                wr.writerow([fid, "9", x["cote"], len(x["scans"]), parts])
            if fid not in have_a:
                wa.writerow([fid, x["cote"], ",".join(str(s) for s in x["scans"]), len(x["scans"]), x["package"], WHAT])
    print("built and queued:", len(ids) - len(bad), "of", len(todo), "| held back:", bad, "| failed:", failed)
    print("queued:", " ".join(f for f in ids if f not in bad))


if __name__ == "__main__":
    if "--plan" in sys.argv:
        i = sys.argv.index("--plan")
        plan(int(sys.argv[i + 1]) if len(sys.argv) > i + 1 and sys.argv[i + 1].isdigit() else 0)
    elif "--build" in sys.argv:
        build(int(sys.argv[sys.argv.index("--build") + 1]))
