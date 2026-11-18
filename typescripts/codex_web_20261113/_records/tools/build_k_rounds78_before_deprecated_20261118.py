"""Batch K rounds 7 and 8 for GPT-6.2 Astra at reasoning effort max (ChatGPT Work), 18 Nov 2026.

The main session (Claude Opus 5.5 at effort max), 18 Nov 00:5x UTC, quoting the user: "dump everything over Astra
6.2 ... grind everything out over 6.2 ASAP". Written by Claude Opus 5.5 at effort high.

- Round 7: the 20 Pro packages still queued in packages/ (the eight .s_ ones and P052-P076); .04_P085 is skipped (a
  locked leftover of a package already sent and filed).
- Round 8: every scan of the archive in no route: not in packages_done/, returns/, CODEX_COVERED_SCANS.tsv,
  ASSIGNMENTS.tsv, the API pages, packages/, packages_chrome(_sent)/, packages_held_for_codex_web/,
  packages_covered_by_codex_web/ or packages_moved_to_codex_20261117/, and not round 7. Blank scans (ink < 0.0003)
  and the IMAG logo sheet that opens most PDFs (scan 1) are left out.
Folders of at most 16 scans per cote (chunks() of build_handwriting_k), template K2 (Hua witness step, G1 notes, the
CTRL-145 lines), built into drag_next/ like rounds 2-6; ids continue each cote's K numbering.

usage: python -I -B tools/build_k_rounds78.py --plan     (writes K_ROUNDS78_PLAN_20261118.json, builds nothing)
       python -I -B tools/build_k_rounds78.py --build    (builds the planned folders, PROMPT.md included)
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
import build_handwriting_k as K  # noqa: E402
from PIL import Image  # noqa: E402

B, H, CW, T = K.B, K.H, K.CW, K.T
PLAN78 = CW / "K_ROUNDS78_PLAN_20261118.json"
CACHE = HERE / "K_ROUNDS78_SCANS_20261118.json"   # ink and logo distance per (cote, scan)
ROUND7 = ["P097", "P121", "P135", "P158", "P160", "P161", "P179", "P181",
          "P052", "P055", "P056", "P064", "P067", "P069", "P071", "P072", "P073", "P074", "P075", "P076"]
SKIP = [".04_P085_89_MPL_15_034-086"]
LOGO_REF = ("57", 1)   # scan 1 of cote 57: the IMAG logo sheet (checked by eye, 18 Nov)


def pdf_of(cote):
    r = B.row(cote)
    return B.ARCH / r["folder"] / r["file"]


def n_pages(cote):
    out = subprocess.run(["pdfinfo", str(pdf_of(cote))], capture_output=True, text=True, check=True).stdout
    return int(re.search(r"Pages:\s+(\d+)", out).group(1))


def thumb(im):
    return list(im.convert("L").resize((64, 38)).getdata())


def scan_info(cote, scans, cache, ref):
    """{scan: (ink, logo distance)}; images extracted once and cached."""
    have = cache.setdefault(cote, {})
    need = [n for n in scans if str(n) not in have]
    if need:
        with tempfile.TemporaryDirectory() as tmp:
            for n in need:
                im = B.page_image(pdf_of(cote), n, tmp)
                if im is None:
                    have[str(n)] = [-1.0, 999.0]
                    continue
                t = thumb(im)
                dist = sum(abs(a - b) for a, b in zip(t, ref)) / len(t) if ref else 999.0
                have[str(n)] = [round(B.ink(im), 4), round(dist, 1)]
        CACHE.write_text(json.dumps(cache, indent=0), encoding="utf-8")
    return {n: tuple(have[str(n)]) for n in scans}


def existing_ids():
    ids = set()
    for r in csv.DictReader(open(CW / "ASSIGNMENTS.tsv", encoding="utf-8"), delimiter="\t"):
        ids.add(r["folder"])
    for base in ("drag", "drag_next", "done", "drag_split", "drag_split_next"):
        d = CW / base
        if d.is_dir():
            ids |= {p.name for p in d.iterdir() if p.is_dir()}
    return ids


def next_index(cote, ids):
    nums = [int(m.group(1)) for i in ids for m in [re.fullmatch(rf"K{re.escape(cote)}-(\d+)", i)] if m]
    return max(nums, default=0) + 1


NAME_DIRS = ["packages_done", "returns", "packages", "packages_chrome", "packages_chrome_sent",
             "packages_held_for_codex_web", "packages_covered_by_codex_web", "packages_moved_to_codex_20261117",
             "second_pass/out", "second_pass_returns", "second_pass_pro_20261114"]
# Cotes 90-97 % and 70-90 % transcribed whose gaps go first, as round 7a (the main session, 18 Nov 01:2x UTC)
GAP_COTES = ["2", "6", "8", "11", "56", "68", "75", "81", "103", "105", "116", "121", "122", "131", "133", "134-8",
             "144", "146", "161-5", "13", "15", "35", "39", "71", "109", "119", "134-1", "134-2", "136", "162-5"]


def name_ranges(name, pages):
    """the (cote, scan) pairs a package name stands for: MPL_<cote>[_<NNN>-<NNN>](+...); a bare cote is all its pages.
    Early Pro returns name their pages by package (MPL_147_003-047_scan003.tex), so the name is the record."""
    m = re.search(r"MPL_(.+?)(?:_checkpoint_\d+)?(?:_unzipped|_check)?$", name)
    if not m:
        return set(), None
    out, bad = set(), []
    for part in m.group(1).split("+"):
        p = re.fullmatch(r"(\d+(?:-\d{1,2})?)(?:_(\d{3})-(\d{3}))?(?:r|_continue|_chat[A-Z])?", part)
        if not p or p.group(1) not in pages:
            bad.append(part)
            continue
        a, b = (int(p.group(2)), int(p.group(3))) if p.group(2) else (1, pages[p.group(1)])
        out |= {(p.group(1), s) for s in range(a, b + 1)}
    return out, (bad or None)


def plan():
    pkgs = {}
    for d in sorted(K.PKG.iterdir()):
        if not d.is_dir() or d.name in SKIP:
            continue
        key = re.sub(r"^\.[^_]*_", "", d.name)[:4]
        if key in ROUND7:
            pkgs[key] = d
    missing = [k for k in ROUND7 if k not in pkgs]
    if missing:
        raise SystemExit(f"round 7 packages not in packages/: {missing}")
    order = [pkgs[k] for k in ROUND7]
    names7 = {re.sub(r"^\.[^_]*_", "", d.name) for d in order}
    # everything already routed; the round-7 packages themselves (and their Chrome copies) are left out of it
    others = [d for d in K.PKG.iterdir() if d.is_dir() and d not in order]
    taken = K.taken_by_others(others)
    for base in ("packages_chrome", "packages_chrome_sent", "packages_moved_to_codex_20261117"):
        for d in (T / base).iterdir() if (T / base).is_dir() else []:
            if d.is_dir() and re.sub(r"^\.[^_]*_", "", d.name) not in names7:
                for k in K.zip_scans(d):
                    taken.setdefault(k, base + " " + d.name)
    man = json.loads((B.ARCH / "MANIFEST.json").read_text(encoding="utf-8"))
    pages = {r["cote"]: n_pages(r["cote"]) for r in man}
    unparsed = []
    for base in NAME_DIRS:
        for d in (T / base).iterdir() if (T / base).is_dir() else []:
            if not d.is_dir() or re.sub(r"^\.[^_]*_", "", d.name) in names7:
                continue
            keys, bad = name_ranges(d.name, pages)
            if bad:
                unparsed.append([base, d.name, bad])
            for k in keys:
                taken.setdefault(k, "by name " + base + "/" + d.name)
    # The recut plan of 12-13 Nov (BLANKS_20261112.json) is not a route: a scan it lists that no route above holds
    # is in no package anywhere, so it belongs to round 8.
    cache = json.loads(CACHE.read_text(encoding="utf-8")) if CACHE.exists() else {}
    with tempfile.TemporaryDirectory() as tmp:
        ref = thumb(B.page_image(pdf_of(LOGO_REF[0]), LOGO_REF[1], tmp))
    ids = existing_ids()
    out = dict(round7_packages=[d.name for d in order], skipped_packages=SKIP, overlap7=[], folders=[],
               blank={}, logo={}, missing_image={}, unparsed_names=unparsed)

    def cut(cote, scans, rnd, package, packages):
        info = scan_info(cote, scans, cache, ref)
        live, bl, lg, mi = [], [], [], []
        for n in scans:
            ink, dist = info[n]
            if ink < 0:
                mi.append(n)
            elif ink < 0.0003:
                bl.append(n)
            elif dist < 12:
                lg.append(n)
            else:
                live.append(n)
        for key, v in (("blank", bl), ("logo", lg), ("missing_image", mi)):
            if v:
                out[key].setdefault(cote, []).extend(v)
        j = next_index(cote, ids)
        for part in (K.chunks(live) if live else []):
            fid = f"K{cote}-{j:02d}"
            ids.add(fid)
            out["folders"].append(dict(id=fid, cote=cote, scans=part, round=rnd, package=package, packages=packages))
            j += 1

    # round 7, package by package; a cote spread over several packages is cut per package
    for d in order:
        free = {}
        for k in sorted(K.zip_scans(d)):
            if k in taken:
                out["overlap7"].append([d.name, k[0], k[1], taken[k]])
            else:
                free.setdefault(k[0], []).append(k[1])
                taken[k] = "round 7 " + d.name
        for cote, scans in free.items():
            cut(cote, sorted(scans), 7, d.name, [d.name])
    # round 8: every scan of every cote that is in no route
    out["pages_per_cote"] = pages
    for r in man:
        c = r["cote"]
        if c.startswith(("140-", "157-")):  # La Longue Marche and Les Dérivateurs: finished texts (PROJECT_RECORD)
            continue
        free = [s for s in range(1, pages[c] + 1) if (c, s) not in taken]
        if free:
            cut(c, free, 8, "none (pages in no queue)", [])
    # gaps of cotes already 70-97 % transcribed go first, as round 7a
    for f in out["folders"]:
        if f["cote"] in GAP_COTES:
            f["round"] = "7a"
    out["folders"].sort(key=lambda f: {"7a": 0, 7: 1, 8: 2}[f["round"]])
    out["pages"] = {str(rnd): sum(len(f["scans"]) for f in out["folders"] if f["round"] == rnd) for rnd in ("7a", 7, 8)}
    return out


def build():
    import k_material  # noqa: E402
    P = json.loads(PLAN78.read_text(encoding="utf-8"))
    allk = json.loads(K.PLAN_JSON.read_text(encoding="utf-8"))["folders"] + P["folders"]
    recs, failed = [], []
    for x in P["folders"]:
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
            r["round"] = x["round"]
            r = K.add_hua(x, r)
            recs.append(r)
    with open(H.HERE / "BUILD_LOG.jsonl", "a", encoding="utf-8") as f:
        for r in recs:
            f.write(json.dumps(r, ensure_ascii=False) + "\n")
    n = 0
    for x in P["folders"]:
        d = CW / "drag_next" / x["id"]
        if d.is_dir():
            (d / "PROMPT.md").write_bytes(K.make_prompt(x, allk).encode("utf-8"))
            n += 1
    print("built:", len(recs), "PROMPT.md written:", n, "failed:", failed)


if __name__ == "__main__":
    if "--plan" in sys.argv:
        P = plan()
        PLAN78.write_text(json.dumps(P, indent=1, ensure_ascii=False), encoding="utf-8")
        for rnd in ("7a", 7, 8):
            fs = [f for f in P["folders"] if f["round"] == rnd]
            print(f"round {rnd}: {len(fs)} folders, {P['pages'][str(rnd)]} pages, cotes",
                  " ".join(dict.fromkeys(f["cote"] for f in fs)))
        print("overlap in round 7:", len(P["overlap7"]), "blank:", sum(map(len, P["blank"].values())),
              "logo:", sum(map(len, P["logo"].values())), "no image:", P["missing_image"],
              "unparsed names:", P["unparsed_names"])
    elif "--build" in sys.argv:
        build()
