"""Build batch K of the Codex-web folders (17 Nov 2026, Claude Opus 5.5 at effort high, the agent that built batches H
and J), per BRIEF_BATCH_K_20261117.md: the tail of the queued Pro transcription packages goes to GPT-6 Astra in Codex
web at reasoning effort max, on an account whose Codex capacity (about 120x) expires on 21 Nov 2026.

- Packages: every queued package in ../../packages/ except the sixteen promoted ones (names starting .01_ to .16_) and
  the next twenty by name (P051 onwards), which stay on Pro.
- Scans: those in each package's scans zip, minus every scan another route has done or is doing (packages_done/ scans
  zips, returns/*_unzipped page files, packages_work/CODEX_COVERED_SCANS.tsv, ASSIGNMENTS.tsv, the API page files of
  api_typescripts_20261112/, the packages kept on Pro), minus blank scans (ink below 0.0003, the builder's own test).
- Folders: per cote, the scans in order, cut into folders of about 15; cotes in the order of their first package.
  Same images, template (PROMPT_TEMPLATE_HANDWRITING.md, no draft) and folder form as batches H and J
  (build_handwriting.build()). Material sentences from K_MATERIAL below.
Reads the archive PDFs and the package zips only; writes only under codex_web_20261113/. Skips folders that exist.

usage: python -I -B build_handwriting_k.py --plan            (writes K_PLAN_20261117.json and .tsv, builds nothing)
       python -I -B build_handwriting_k.py --build [R ...]   (builds the folders of rounds R, default all, then writes
                                                             their PROMPT.md)
       python -I -B build_handwriting_k.py --prompts [R ...] (rewrites PROMPT.md and PREAMBLE.tex of built folders from
                                                             the current template; the zips are not touched)
"""
import csv
import json
import math
import pathlib
import re
import sys
import tempfile
import zipfile

sys.stdout.reconfigure(encoding="utf-8")
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent))
import build_codex_web as B  # noqa: E402
import build_handwriting as H  # noqa: E402

CW = H.HERE.parent
T = CW.parent
PKG = T / "packages"
RATE = 0.030          # x of a weekly allowance a page (batches H and J)
CAP = 120.0           # x available until 21 Nov 2026
SIZE = 16             # scans a folder at most: double the H/J size, about two hours (the user, 17 Nov)
ROUND = 33            # a new round starts at a cote boundary once a round holds this many folders
INKS = H.HERE / "K_INKS_20261117.json"
PLAN_JSON = CW / "K_PLAN_20261117.json"
PLAN_TSV = CW / "K_PLAN_20261117.tsv"
SCAN_RE = re.compile(r"_(\d+(?:-\d+)?)_scan(\d{3})(?:_[a-z0-9]+)?\.(?:jpg|tex)$")


def queue():
    names = sorted(p.name for p in PKG.iterdir() if p.is_dir())
    promoted = [n for n in names if n.startswith(".")]
    rest = [n for n in names if not n.startswith(".")]
    return promoted, rest[:20], rest[20:]


def zip_scans(folder):
    out = set()
    for z in folder.glob("*_scans.zip"):
        for n in zipfile.ZipFile(z).namelist():
            m = SCAN_RE.search(n)
            if m:
                out.add((m.group(1), int(m.group(2))))
    return out


def taken_by_others(kept):
    taken = {}

    def add(keys, why):
        for k in keys:
            taken.setdefault(k, why)
    for d in sorted((T / "packages_done").iterdir()):
        if d.is_dir():
            add(zip_scans(d), "Pro sent " + d.name)
    for d in sorted((T / "returns").glob("*_unzipped")):
        for f in (d / "pages").glob("*.tex") if (d / "pages").is_dir() else []:
            m = SCAN_RE.search(f.name)
            if m:
                add([(m.group(1), int(m.group(2)))], "Pro return " + d.name)
    for r in csv.DictReader(open(T / "packages_work/CODEX_COVERED_SCANS.tsv", encoding="utf-8"), delimiter="\t"):
        add([(r["cote"], int(r["scan"]))], "Codex web " + r["folder"])
    for r in csv.DictReader(open(CW / "ASSIGNMENTS.tsv", encoding="utf-8"), delimiter="\t"):
        add([(r["cote"], int(n)) for n in re.findall(r"\d+", r["scans"])], "Codex web " + r["folder"])
    for d in (T / "api_typescripts_20261112").iterdir():
        for f in (d / "pages").glob("*.tex") if (d / "pages").is_dir() else []:
            m = re.match(r"^[a-z0-9]+_(.+)_(\d{3})\.tex$", f.name)
            if m:
                add([(m.group(1), int(m.group(2)) + 1)], "API " + d.name)
    for n in kept:
        d = n if isinstance(n, pathlib.Path) else PKG / n
        add(zip_scans(d), "kept on Pro " + d.name)
    for base in ("packages_held_for_codex_web", "packages_covered_by_codex_web"):
        for d in (T / base).iterdir() if (T / base).is_dir() else []:
            if d.is_dir():
                add(zip_scans(d), base + " " + d.name)
    return taken


def inks(cote, scans, cache):
    have = cache.setdefault(cote, {})
    need = [n for n in scans if str(n) not in have]
    if need:
        r = B.row(cote)
        pdf = B.ARCH / r["folder"] / r["file"]
        with tempfile.TemporaryDirectory() as tmp:
            for n in need:
                im = B.page_image(pdf, n, tmp)
                have[str(n)] = -1.0 if im is None else round(B.ink(im), 4)
        INKS.write_text(json.dumps(cache, indent=0), encoding="utf-8")
    return {n: have[str(n)] for n in scans}


def chunks(xs, size=SIZE):
    k = max(1, math.ceil(len(xs) / size))
    q, r = divmod(len(xs), k)
    res, i = [], 0
    for j in range(k):
        m = q + (1 if j < r else 0)
        res.append(xs[i:i + m])
        i += m
    return res


def plan():
    promoted, kept20, k_pkgs = queue()
    taken = taken_by_others(promoted + kept20)
    cache = json.loads(INKS.read_text(encoding="utf-8")) if INKS.exists() else {}
    per_pkg, overlap, blanks = {}, [], {}
    for p in k_pkgs:
        sc = sorted(zip_scans(PKG / p))
        free = []
        for k in sc:
            if k in taken:
                overlap.append((p, k[0], k[1], taken[k]))
            else:
                free.append(k)
                taken[k] = "batch K " + p
        per_pkg[p] = free
    cotes, first = {}, {}
    for i, p in enumerate(k_pkgs):
        for c, n in per_pkg[p]:
            cotes.setdefault(c, []).append(n)
            first.setdefault(c, (i, p))
    folders = []
    for c in sorted(cotes, key=lambda c: first[c][0]):
        scans = sorted(cotes[c])
        ink = inks(c, scans, cache)
        live = [n for n in scans if ink[n] >= 0.0003]
        blanks[c] = [n for n in scans if ink[n] < 0.0003]
        for j, part in enumerate(chunks(live), 1):
            folders.append(dict(id=f"K{c}-{j:02d}", cote=c, scans=part, package=first[c][1],
                                packages=sorted({p for p in k_pkgs if any((c, n) in set(per_pkg[p]) for n in part)})))
    rnd, n_in, cur = 1, 0, None
    for f in folders:
        if f["cote"] != cur and n_in >= ROUND:
            rnd, n_in = rnd + 1, 0
        cur = f["cote"]
        f["round"] = rnd
        n_in += 1
    return dict(promoted=promoted, kept_on_pro=kept20, k_packages=k_pkgs, folders=folders, blanks=blanks,
                overlap=overlap, pages=sum(len(f["scans"]) for f in folders))


T_K = H.HERE / "PROMPT_TEMPLATE_HANDWRITING_K.md"   # G1-G3 of METHOD_AUDIT_AND_PLAN_20261117.md (round 1, controls)
T_K2 = H.HERE / "PROMPT_TEMPLATE_HANDWRITING_K2.md"  # rounds 2-7: K plus Hua's transcription as a witness after the freeze
HUA_T = pathlib.Path.home() / "Documents/ai_math_sources_20261114/hua_michel/commutator_grothendieck-project/transcripts"
SMALL = T / "packages_work/SMALL_FOR_EXPIRING_ACCOUNT_20261117.txt"
EXCLUDED_EXTRA = ["P177_153_MPL_93_092-134"]  # the user runs this Pro prompt unchanged on Codex as a test (.AUDIT2_)
MOVED = T / "packages_moved_to_codex_20261117"


def hua_files(x):
    """Hua's batch files (and their drawing files) whose pages overlap the folder's scans (their page = scan - 1)."""
    d = HUA_T / x["cote"]
    if not d.is_dir():
        return []
    want = {n - 1 for n in x["scans"]}
    out = []
    for f in sorted(d.glob("batch-*.fr.tex")):
        m = re.search(r"\\pages\{(\d+)\}\{(\d+)\}", f.read_text(encoding="utf-8"))
        if m and any(int(m.group(1)) <= p <= int(m.group(2)) for p in want):
            out.append(f)
            num = re.search(r"batch-(\d+)", f.name).group(1)
            out += sorted((d / "drawings").glob(f"{num}-*.tex")) if (d / "drawings").is_dir() else []
    return out


NEXT = CW / "drag_next"  # rounds 2-7 wait here until the pilot's verdict (the main session, 17 Nov ~17:5x UTC)


def build_next(fid, cote, scans, material):
    """build_handwriting.build(), but into drag_next/, so that a later round cannot be sent from drag/ by mistake.
    Same images, zip, manifest and checks; PROMPT.md is written afterwards by make_prompt()."""
    import hashlib
    from PIL import ImageFilter, ImageOps
    out = NEXT / fid
    if out.exists() or (CW / "drag" / fid).exists() or (CW / "done" / fid).exists():
        print("exists, skipped:", fid)
        return None
    r = B.row(cote)
    pdf = B.ARCH / r["folder"] / r["file"]
    files, man, ink = [], [], {}
    with tempfile.TemporaryDirectory() as tmp:
        for n in scans:
            im = B.page_image(pdf, n, tmp)
            if im is None or B.ink(im) < 0.0003:
                raise SystemExit(f"{fid}: cote {cote} scan {n} is blank or has no image")
            ink[n] = round(B.ink(im), 4)
            im = ImageOps.autocontrast(im.convert("L"), cutoff=1).filter(
                ImageFilter.UnsharpMask(radius=2, percent=120, threshold=3))
            stem = f"{fid}_{cote}_scan{n:03d}"
            for part, sub in [("whole", im)] + [(f"s{i}", t) for i, t in enumerate(B.thirds(im), 1)]:
                name = stem + ("" if part == "whole" else "_" + part) + ".jpg"
                data = B.jpg(sub)
                files.append((name, data))
                man.append((name, len(data), hashlib.sha256(data).hexdigest(), cote, n, part, sub.size[0], sub.size[1]))
    out.mkdir(parents=True)
    mtsv = "file\tbytes\tsha256\tcote\tscan\tpart\twidth\theight\n" + "".join("\t".join(map(str, m)) + "\n" for m in man)
    z = out / f"{fid}_scans.zip"
    with zipfile.ZipFile(z, "w", zipfile.ZIP_STORED) as zf:
        zf.writestr("MANIFEST.tsv", mtsv)
        for name, data in files:
            zf.writestr(name, data)
    (out / "PREAMBLE.tex").write_bytes(B.PREAMBLE.read_bytes())
    with zipfile.ZipFile(z) as zz:
        assert zz.testzip() is None and len(zz.namelist()) == 1 + 4 * len(scans)
    rec = dict(id=fid, cote=cote, scans=scans, kind="hand", draft=None, ink=ink,
               pdf=str(pdf).replace(pathlib.Path.home().name, "user"), url=r["url"], title=r["title"], date=r["date"],
               zip_mb=round(z.stat().st_size / 1e6, 1), zip_sha256=hashlib.sha256(z.read_bytes()).hexdigest())
    print(json.dumps(rec, ensure_ascii=False), flush=True)
    return rec


def add_hua(x, rec):
    """Append Hua's files of the folder to its scans zip (rounds 2-7 only); update the build record."""
    files = hua_files(x)
    if not files:
        return rec
    z = folder_of(x["id"]) / f"{x['id']}_scans.zip"
    with zipfile.ZipFile(z, "a", zipfile.ZIP_DEFLATED) as zf:
        if any(n.startswith("hua/") for n in zf.namelist()):
            return rec
        for f in files:
            zf.write(f, "hua/transcripts/" + f.relative_to(HUA_T).as_posix())
        zf.write(HUA_T / "preamble/grothendieck.sty", "hua/preamble/grothendieck.sty")
    with zipfile.ZipFile(z) as zf:
        assert zf.testzip() is None
    import hashlib
    rec.update(hua=[f.relative_to(HUA_T).as_posix() for f in files], zip_mb=round(z.stat().st_size / 1e6, 1),
               zip_sha256=hashlib.sha256(z.read_bytes()).hexdigest())
    return rec


def plan2():
    """Rounds 2-7 again, without the packages that left batch K on 17 Nov ~17:4x UTC (the 21 small ones for the
    expiring account's Pro, and P177); round 1 and the controls stay as built."""
    old = json.loads(PLAN_JSON.read_text(encoding="utf-8"))
    r1 = [f for f in old["folders"] if f["round"] == 1]
    excl = {re.sub(r"^\.(?:\d+)?s_", "", l.strip()) for l in SMALL.read_text(encoding="utf-8").splitlines() if l.strip()}
    excl |= set(EXCLUDED_EXTRA)
    k_pkgs = [p for p in old["k_packages"] if p not in excl]
    pro = [d for d in PKG.iterdir() if d.is_dir() and d.name.startswith(".")]
    pro += [PKG / n for n in old["kept_on_pro"] if (PKG / n).is_dir()]
    taken = taken_by_others(pro)
    for f in r1:
        for n in f["scans"]:
            taken[(f["cote"], n)] = "batch K round 1 " + f["id"]
    cache = json.loads(INKS.read_text(encoding="utf-8")) if INKS.exists() else {}
    per_pkg, overlap = {}, []
    for p in k_pkgs:
        d = PKG / p if (PKG / p).is_dir() else MOVED / p
        free = []
        for k in sorted(zip_scans(d)):
            if k in taken:
                if not taken[k].startswith("batch K round 1"):
                    overlap.append((p, k[0], k[1], taken[k]))
            else:
                free.append(k)
                taken[k] = "batch K " + p
        per_pkg[p] = free
    cotes, first = {}, {}
    for i, p in enumerate(k_pkgs):
        for c, n in per_pkg[p]:
            cotes.setdefault(c, []).append(n)
            first.setdefault(c, (i, p))
    folders, blanks = [], {}
    for c in sorted(cotes, key=lambda c: first[c][0]):
        scans = sorted(cotes[c])
        ink = inks(c, scans, cache)
        live = [n for n in scans if ink[n] >= 0.0003]
        blanks[c] = [n for n in scans if ink[n] < 0.0003]
        for j, part in enumerate(chunks(live), 1):
            folders.append(dict(id=f"K{c}-{j:02d}", cote=c, scans=part, package=first[c][1],
                                packages=sorted({p for p in k_pkgs if any((c, n) in set(per_pkg[p]) for n in part)})))
    rnd, n_in, cur = 2, 0, None
    for f in folders:
        if f["cote"] != cur and n_in >= ROUND:
            rnd, n_in = rnd + 1, 0
        cur = f["cote"]
        f["round"] = rnd
        n_in += 1
    if rnd > 2 and sum(f["round"] == rnd for f in folders) < 10:  # a short last round joins the one before
        for f in folders:
            if f["round"] == rnd:
                f["round"] = rnd - 1
    return dict(old, k_packages=k_pkgs, excluded_20261117=sorted(excl & set(old["k_packages"])),
                folders=r1 + folders, blanks=blanks, overlap=overlap,
                pages=sum(len(f["scans"]) for f in r1 + folders))
# Control folders (METHOD_AUDIT_AND_PLAN_20261117.md section 3): pages that already have a Pro first pass and a Claude
# second pass of 17 Nov 2026, so that the corrected text is ground truth. Their returns are filed apart
# (returns_control/), never over the first passes.
CONTROLS = [dict(id="CTRL-148", cote="148", scans=list(range(44, 59)), round=1, package="control", packages=[]),
            dict(id="CTRL-145", cote="145", scans=list(range(20, 35)), round=1, package="control", packages=[])]


def neighbours(x, folders):
    same = [f for f in folders if f["cote"] == x["cote"]]
    if len(same) < 2:
        return ""
    i = next(k for k, f in enumerate(same) if f["id"] == x["id"])

    def span(fs):
        ids = fs[0]["id"] if len(fs) == 1 else f"{fs[0]['id']} to {fs[-1]['id']}"
        return f"{ids} (scans {B.ranges([n for f in fs for n in f['scans']])})"
    parts = []
    if i:
        parts.append(span(same[:i]) + " before this one")
    if i < len(same) - 1:
        parts.append(span(same[i + 1:]) + " after it")
    return (f" The other scans of cote {x['cote']} in this batch are transcribed in separate tasks that run in parallel: "
            + " and ".join(parts) + ". The notation tables of all these tasks are reconciled afterwards, so every entry "
            "of yours names the scan and the line where you saw the glyph.")


def make_prompt(x, folders=()):
    """PROMPT.md of a folder from the K template and material sentence; rerunnable over built folders."""
    import k_material  # noqa: E402
    r = B.row(x["cote"])
    if x.get("round", 1) == 1:
        t = T_K.read_text(encoding="utf-8")
    else:  # the Hua witness blocks stay only where his files cover the folder's scans
        has = bool(hua_files(x))
        t = re.sub(r"<!--HUA-->(.*?)<!--/HUA-->", (lambda m: m.group(1)) if has else "",
                   T_K2.read_text(encoding="utf-8"), flags=re.S)
    reps = {"{ID}": x["id"], "{COTE}": x["cote"], "{TITLE}": r["title"], "{DATE}": r["date"],
            "{COUNT}": str(len(x["scans"])), "{SCANS}": B.ranges(x["scans"]), "{MATERIAL}": k_material.sentence(x),
            "{NEIGHBOURS}": neighbours(x, folders)}
    reps.update(H.draft_text(None))
    for k, v in reps.items():
        t = t.replace(k, v)
    left = re.findall(r"\{(?:ID|COTE|TITLE|DATE|COUNT|SCANS|MATERIAL|DRAFT|DRAFT_RULES|DRAFT_DOUBTS|NEIGHBOURS)\}", t)
    if left:
        raise SystemExit(f"placeholders left: {left}")
    return t


def folder_of(fid):
    for base in ("drag", "drag_next", "done"):
        d = CW / base / fid
        if d.is_dir():
            return d
    return None


if __name__ == "__main__":
    if "--plan" in sys.argv or "--plan2" in sys.argv:
        if "--plan2" in sys.argv:
            bak = CW / "K_PLAN_20261117_before_exclusions.json"
            if not bak.exists():
                bak.write_bytes(PLAN_JSON.read_bytes())
            P = plan2()
        else:
            if PLAN_JSON.exists() and "--force" not in sys.argv:
                raise SystemExit("K_PLAN exists and round 1 is built from it: use --plan2 (or --force)")
            P = plan()
        PLAN_JSON.write_text(json.dumps(P, indent=1, ensure_ascii=False), encoding="utf-8")
        with open(PLAN_TSV, "w", encoding="utf-8", newline="\n") as f:
            f.write("folder\tcote\tscans\tcount\tfirst_package\tpackages\n")
            for x in P["folders"]:
                f.write(f"{x['id']}\t{x['cote']}\t{B.ranges(x['scans'])}\t{len(x['scans'])}\t{x['package']}\t"
                        f"{' '.join(x['packages'])}\n")
        print("K packages:", len(P["k_packages"]), "folders:", len(P["folders"]), "pages:", P["pages"],
              "x:", round(P["pages"] * RATE, 1), "overlap scans:", len(P["overlap"]),
              "blanks:", sum(len(v) for v in P["blanks"].values()))
        sys.exit()
    P = json.loads(PLAN_JSON.read_text(encoding="utf-8"))
    rounds = {int(a) for a in sys.argv[2:] if a.isdigit()}
    sel = [x for x in CONTROLS + P["folders"] if not rounds or x["round"] in rounds]
    if sys.argv[1:2] == ["--build"]:
        import k_material  # noqa: E402
        recs = []
        for x in sel:
            try:
                if x["round"] >= 2:
                    r = build_next(x["id"], x["cote"], x["scans"], k_material.sentence(x))
                else:
                    r = H.build(x["id"], x["cote"], x["scans"], k_material.sentence(x), H.HAND, None)
            except SystemExit as e:
                print("FOLDER FAILED:", x["id"], e)
                continue
            if r:
                r["round"] = x["round"]
                if x["round"] >= 2:
                    r = add_hua(x, r)
                recs.append(r)
        with open(H.HERE / "BUILD_LOG.jsonl", "a", encoding="utf-8") as f:
            for r in recs:
                f.write(json.dumps(r, ensure_ascii=False) + "\n")
    if sys.argv[1:2] in (["--build"], ["--prompts"]):
        # PROMPT.md (and PREAMBLE.tex) of every selected built folder, from the current template; the zips stay
        n = 0
        for x in sel:
            d = folder_of(x["id"])
            if d is None:
                continue
            (d / "PROMPT.md").write_text(make_prompt(x, P["folders"]), encoding="utf-8")
            (d / "PREAMBLE.tex").write_bytes(B.PREAMBLE.read_bytes())
            n += 1
        print("PROMPT.md written:", n)