"""Doubt marks through the second passes (20 Nov 2026, main session, Claude Opus 5.5 at effort max).

The user, 19 Nov 2026 23:04 UTC: "I need an actual report on all the doubt marks, all their types, all the ways that
we've suggested fixing them, and all their effectiveness, HTML, and it needs to be complete and rigorous"; "Base it on
intakes from the more recent pro runs, including partials."

For every page a second pass has finished, this lines up three texts word by word: the first reading as the pass
received it (witness C), the pass's final text (F), and Hua's text of the same page (H). For each doubt mark of C it
records what F has at that place, and what H has there. The passes covered:
- the Pro second passes in second_pass_returns/ (newest return of each run; partial returns count, with only the pages
  their progress.log says are done);
- the doubt-mark run DM01 (cote 1);
- the Claude block second pass of 13 Nov (second_pass/out/; its C is the Pro first reading of the block).

python -I -B dm_followup.py  ->  ../data/marks.tsv, ../data/pages.tsv, ../data/runs.json, ../data/dm01_check.tsv
"""
import collections
import csv
import datetime
import json
import pathlib
import re
import statistics
import sys
import zipfile

sys.stdout.reconfigure(encoding="utf-8")
HERE = pathlib.Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
import texalign as TA  # noqa: E402

D = pathlib.Path("<project root>")
T = D / "grothendieck_archive_transcription_20261110"
SPR = T / "second_pass_returns"
SPB = T / "second_pass_pro_20261114"
DMB = T / "doubt_marks_pro_20261119"
HUA = D / "ai_math_sources_20261114/hua_michel/commutator_grothendieck-project/transcripts"
OUT = HERE.parent / "data"
OUT.mkdir(exist_ok=True)
PAGEF = re.compile(r"(?:^|[_/])(\d+(?:-\d+)?)_scan(\d{3})\.tex$")
DONE = re.compile(r"scan[ _]?(\d{3})\b[^\n]*?\b(done|amended|committed|finali[sz]ed)\b", re.I)
STAMP = re.compile(r"(\d{4}-\d\d-\d\d)[ T](\d\d:\d\d:\d\d)")

# The design of each run, from its prompt as sent (checked by the phrases printed below).
DESIGN = {
    "SP02": "Pro, one reader, large piece (sent 14-17 Nov)", "SP04": "Pro, one reader, large piece (sent 14-17 Nov)",
    "SP12": "Pro, one reader, large piece (sent 14-17 Nov)", "SP14": "Pro, one reader, large piece (sent 14-17 Nov)",
    "SP31": "Pro, one reader, piece of 16-24 pages (sent 19 Nov)", "SP32": "Pro, one reader, piece of 16-24 pages (sent 19 Nov)",
    "SP33": "Pro, one reader, piece of 16-24 pages (sent 19 Nov)",
    "SP34": "Pro, three readers + main reader (sent 19 Nov ~20:2x UTC)",
    "SP35": "Pro, three readers + reading workflow of 21:07 UTC",
    "SP36": "Pro, three fresh readers per page, deep zoom, reading workflow (from 21:10 UTC)",
    "SP37": "Pro, three fresh readers per page, deep zoom, reading workflow (from 21:10 UTC)",
    "SP38": "Pro, three fresh readers per page, deep zoom, reading workflow (from 21:10 UTC)",
    "SP57": "Pro, three fresh readers per page, deep zoom, reading workflow (from 21:10 UTC)",
    "DM01": "Pro, doubt marks only, its own workflow (sent 19 Nov ~22:0x UTC)",
    "CLAUDE13": "Claude Opus 5.5 at effort max, block second pass (13 Nov)",
}
PHRASES = {"three readers": r"three (independent |fresh )?(sub-?agents|readers)", "fresh per page": r"fresh",
           "deep zoom": r"thousand pixels|2,?000.{0,20}3,?000|deep", "one tight crop": r"one tight crop",
           "hash/freeze": r"hash|frozen|freeze", "witness S": r"witness S", "doubt marks only": r"doubt marks? only|every listed mark"}


def hua_pages_from_batches(texts):
    """{page n: text} from Hua's batch files (\\page{n} markers)."""
    pages = {}
    for t in texts:
        parts = re.split(r"\\page\{(\d+)\}", t)
        for i in range(1, len(parts) - 1, 2):
            pages[int(parts[i])] = pages.get(int(parts[i]), "") + parts[i + 1]
    return pages


_hua_cache = {}


def hua_checkout_page(cote, scan):
    if cote not in _hua_cache:
        d = HUA / cote
        _hua_cache[cote] = hua_pages_from_batches(
            [f.read_text(encoding="utf-8", errors="replace") for f in sorted(d.glob("batch-*.tex"))]) if d.is_dir() else {}
    return _hua_cache[cote].get(scan - 1)


def progress(d):
    pl = d / "progress.log"
    if not pl.is_file():
        return None, {}
    txt = pl.read_text(encoding="utf-8", errors="replace")
    st = STAMP.search(txt)
    start = datetime.datetime.strptime(st.group(1) + " " + st.group(2), "%Y-%m-%d %H:%M:%S") if st else None
    done = {}
    for line in txt.splitlines():
        m = DONE.search(line)
        s = STAMP.search(line)
        if m and s:
            done.setdefault(int(m.group(1)), datetime.datetime.strptime(s.group(1) + " " + s.group(2), "%Y-%m-%d %H:%M:%S"))
    return start, done


def crop_records(d):
    """Every crop a return logged, as dicts (scan, box_w, box_h, scale, out_w, src). Sources, in order: JSON and JSONL
    logs (bbox/box/box_ltrb ... with scale, or an output width from which the scale follows), TSV crop manifests, and,
    for a return that logged none, the crop images themselves (output width only; the scale is then unknown)."""
    BOX = ("bbox", "box", "box_ltrb", "crop", "region", "rect", "source_box", "crop_box", "source_bbox", "xyxy", "bounds",
           "coords", "bbox_px", "crop_px")
    SCALE = ("scale", "zoom", "factor", "magnification", "upscale", "enlarge", "resize_factor", "scale_factor")
    OUTW = ("width", "out_width", "output_width", "target_width")
    OUTS = ("target_size", "output_size", "out_size")
    recs, seen = [], set()

    def scan_in(v):
        if isinstance(v, str):
            m = re.search(r"scan[_-]?(\d{3})|(?:^|[/\\])(\d{3})_|crops?(\d{3})", v)
            if m:
                return int(next(g for g in m.groups() if g))
        return None

    def scan_of(obj, fname):
        for k in ("scan", "page", "scan_page"):
            v = obj.get(k)
            if isinstance(v, int):
                return v
            if isinstance(v, str) and re.fullmatch(r"\D*(\d{1,3})\D*", v):
                return int(re.search(r"\d{1,3}", v).group())
        for k in ("file", "path", "output", "out", "crop_file", "image", "target", "destination", "source", "crop_path"):
            sc = scan_in(obj.get(k))
            if sc is not None:
                return sc
        return scan_in(fname)

    def box_of(v):
        if isinstance(v, str):
            nums = re.findall(r"-?\d+(?:\.\d+)?", v)
            v = [float(x) for x in nums] if len(nums) == 4 else None
        if isinstance(v, dict):
            for kk in (("x0", "y0", "x1", "y1"), ("left", "top", "right", "bottom"), ("x", "y", "w", "h")):
                if all(k in v for k in kk):
                    a = [float(v[k]) for k in kk]
                    return (a[2], a[3]) if kk[2] == "w" else (a[2] - a[0], a[3] - a[1])
            return None
        if isinstance(v, (list, tuple)) and len(v) == 4 and all(isinstance(x, (int, float)) for x in v):
            w, h = v[2] - v[0], v[3] - v[1]
            return (w, h) if w > 0 and h > 0 else None
        return None

    def add(scan, w, h, sc, out_w, src, ident):
        key = (scan, round(w) if w else None, round(h) if h else None, sc, ident)
        if key in seen:
            return
        seen.add(key)
        if sc is None and out_w and w:
            sc = out_w / w
        if out_w is None and sc and w:
            out_w = w * sc
        recs.append(dict(scan=scan, box_w=w, box_h=h, scale=sc, out_w=out_w, src=src))

    def walk(obj, fname):
        if isinstance(obj, dict):
            b = next((box_of(obj[k]) for k in BOX if k in obj and box_of(obj[k])), None)
            if b:
                sc = next((float(obj[k]) for k in SCALE if isinstance(obj.get(k), (int, float)) and not isinstance(obj.get(k), bool)), None)
                ow = next((float(obj[k]) for k in OUTW if isinstance(obj.get(k), (int, float)) and not isinstance(obj.get(k), bool)), None)
                if ow is None:
                    ow = next((float(obj[k][0]) for k in OUTS if isinstance(obj.get(k), (list, tuple)) and obj[k]), None)
                ident = str(obj.get("file") or obj.get("path") or obj.get("output") or obj.get("target") or obj.get("destination") or "")
                add(scan_of(obj, fname), b[0], b[1], sc, ow, "log", ident)
            for v in obj.values():
                walk(v, fname)
        elif isinstance(obj, list):
            for v in obj:
                walk(v, fname)

    for f in d.rglob("*"):
        suf = f.suffix.lower()
        if suf not in (".json", ".jsonl", ".tsv") or f.stat().st_size > 8e6:
            continue
        txt = f.read_text(encoding="utf-8", errors="replace")
        if suf == ".tsv":
            if "crop" not in f.name.lower():
                continue
            for line in txt.splitlines():
                cells = line.split("\t")
                bi = next((i for i, c in enumerate(cells) if re.fullmatch(r"\s*\d+(\.\d+)?\s*,\s*\d+(\.\d+)?\s*,\s*\d+(\.\d+)?\s*,\s*\d+(\.\d+)?\s*", c)), None)
                if bi is None:
                    continue
                b = box_of(cells[bi])
                sc = None
                if bi + 1 < len(cells) and re.fullmatch(r"\s*\d+(\.\d+)?\s*", cells[bi + 1]):
                    sc = float(cells[bi + 1])
                scan = next((scan_in(c) for c in cells if scan_in(c) is not None), None)
                if b:
                    add(scan, b[0], b[1], sc, None, "manifest", cells[0])
            continue
        objs = []
        if suf == ".jsonl":
            for line in txt.splitlines():
                try:
                    objs.append(json.loads(line))
                except Exception:
                    pass
        else:
            try:
                objs.append(json.loads(txt))
            except Exception:
                pass
        for o in objs:
            walk(o, f.name)
    if not recs:  # no log: the crop images themselves
        try:
            from PIL import Image
        except Exception:
            Image = None
        for f in d.rglob("*"):
            if f.suffix.lower() not in (".png", ".jpg", ".jpeg") or re.search(r"(_a|_b|_full|_page|page_?view)\.(png|jpe?g)$", f.name, re.I):
                continue
            if re.search(r"_scan\d{3}\.(png|jpe?g)$", f.name):  # a whole scan
                continue
            ow = None
            if Image is not None:
                try:
                    with Image.open(f) as im:
                        ow = im.size[0]
                except Exception:
                    pass
            add(scan_in(str(f.relative_to(d))), None, None, None, ow, "image", str(f.relative_to(d)))
    return recs


def run_inputs(name):
    """-> (C pages {(cote, scan): text}, H pages {(cote, scan): text or None}, prompt text)."""
    C, H, prompt = {}, {}, ""
    if name.startswith("DM"):
        b = DMB / name
        z = zipfile.ZipFile(b / f"{name}_texts.zip")
        for n in z.namelist():
            m = PAGEF.search(n)
            if n.startswith("pages/") and m:
                C[(m.group(1), int(m.group(2)))] = z.read(n).decode("utf-8", "replace")
            if n.startswith("hua/") and m:
                H[(m.group(1), int(m.group(2)))] = z.read(n).decode("utf-8", "replace")
        prompt = (b / "PROMPT.md").read_text(encoding="utf-8", errors="replace")
        return C, H, prompt
    b = SPB / name if (SPB / name).is_dir() else SPB / "ALREADY_RAN" / name
    for p in ("PROMPT_as_sent_20261117.md", "PROMPT.md"):
        if (b / p).is_file():
            prompt = (b / p).read_text(encoding="utf-8", errors="replace")
            break
    z = zipfile.ZipFile(b / f"{name}_witnesses.zip")
    names = z.namelist()
    for n in names:
        m = PAGEF.search(n)
        if n.startswith("codex/") and "/pages/" in n and m:
            C[(m.group(1), int(m.group(2)))] = z.read(n).decode("utf-8", "replace")
    batches = {}
    if "page_map.tsv" in names:
        rows = list(csv.DictReader(z.read("page_map.tsv").decode("utf-8", "replace").splitlines(), delimiter="\t"))
        for r in rows:
            k = (r["cote"], int(r["our_scan"]))
            if r.get("hua_has", "text") != "text" or not r.get("hua_file") or r["hua_file"] not in names:
                H[k] = None
                continue
            if r["hua_file"] not in batches:
                batches[r["hua_file"]] = hua_pages_from_batches([z.read(r["hua_file"]).decode("utf-8", "replace")])
            H[k] = batches[r["hua_file"]].get(int(r["their_page"]))
    else:
        for k in C:
            H[k] = hua_checkout_page(*k)
    return C, H, prompt


def analyse_page(run, design, key, ctext, ftext, htext, rows, prow):
    ct, cm = TA.tokenize(ctext, TA.OURS)
    ft, fm = TA.tokenize(ftext, TA.OURS)
    amap, ops, ratio = TA.align(ct, ft)
    if htext:
        ht, hm = TA.tokenize(htext, TA.HUAS)
        hmap, hops, hratio = TA.align(ct, ht)
    else:
        ht, hm, hmap, hratio = None, None, None, None
    hua_usable = bool(htext) and hratio is not None and hratio >= 0.25
    for i, m in enumerate(cm):
        out, reading, det = TA.classify(m, ct, ft, amap, fm)
        if not htext:
            hcls, hread = "no Hua text for the page", ""
        elif not hua_usable:
            hcls, hread = "Hua's page does not match (ratio < 0.25)", ""
        else:
            hc, hread, hdet = TA.classify(m, ct, ht, hmap, hm)
            hcls = {"first reading confirmed": "Hua = C's first reading",
                    "first reading confirmed (neighbours changed)": "Hua = C's first reading",
                    "another listed alternative chosen": "Hua = C's other alternative",
                    "another listed alternative chosen (neighbours changed)": "Hua = C's other alternative",
                    "still doubtful, same reading": "Hua also uncertain here", "still doubtful, reading changed": "Hua also uncertain here",
                    "still illegible": "Hua also uncertain here", "narrowed to a doubtful reading": "Hua also uncertain here",
                    "nothing there": "Hua has nothing here", "not aligned (large rewrite here)": "Hua not aligned here",
                    "read": "Hua has a reading", "same up to accents, case or punctuation": "Hua = C up to accents/case",
                    "a reading not among the alternatives": "Hua has a third reading"}.get(hc, hc)
        f_eq_h = ""
        if hua_usable and reading and hread:
            f_eq_h = "yes" if reading == hread else ("loose" if [TA.loose(x) for x in reading.split()] == [TA.loose(x) for x in hread.split()] else "no")
        rows.append(dict(run=run, design=design, cote=key[0], scan=key[1], idx=i, kind=m["kind"], nalts=len(m["alts"]) if m["kind"] != "illegible" else 0,
                         words=len(m["alts"][0]) if m["alts"] else 0, in_deleted=int(m["flags"]["deleted"]), in_margin=int(m["flags"]["margin"]),
                         in_math=int(m["flags"]["math"]), in_diagram=int(m["flags"].get("diagram", False)), nested=m["nested"], outcome=out, final_reading=reading, hua=hcls, hua_reading=hread[:200],
                         final_eq_hua=f_eq_h, lost_in=m.get("lost_in", ""), mark=m["text"].replace("\t", " ").replace("\n", " ")[:200]))
    ct2, _ = TA.tokenize(ctext, TA.OURS, drop_env=True)  # reading changes, drawings left out
    ft2, fm2 = TA.tokenize(ftext, TA.OURS, drop_env=True)
    _, ops2, _ = TA.align(ct2, ft2)
    blocks, words, trivial = TA.unmarked_changes(ct2, ft2, ops2)
    nm = TA.new_marks(ct2, ft2, fm2, ops2)
    prow.update(run=run, design=design, cote=key[0], scan=key[1], c_words=len(ct), f_words=len(ft), ratio=round(ratio, 3),
                c_marks=len(cm), c_choice=sum(m["kind"] == "choice" for m in cm), c_single=sum(m["kind"] == "single" for m in cm),
                c_illegible=sum(m["kind"] == "illegible" for m in cm), f_marks=len(fm), f_new_marks=len(nm),
                unmarked_blocks=blocks, unmarked_words=words, unmarked_trivial=trivial,
                c_deleted=len(re.findall(r"\\deleted\{", ctext)), f_deleted=len(re.findall(r"\\deleted\{", ftext)),
                hua=("none" if not htext else "usable" if hua_usable else "mismatch"), hua_ratio=round(hratio, 3) if hratio is not None else "")


def main():
    rows, pages, runs = [], [], {}
    # ---- Pro second passes and DM runs
    for d in sorted(SPR.iterdir()):
        m = re.match(r"(.+?)_(checkpoint_\d+|final(?:_INCOMPLETE)?)_(\d{8}T\d{4}Z)_unzipped$", d.name)
        if not m or not d.is_dir():
            continue
        name, kind, stamp = m.groups()
        code = name.split("_")[0]
        design = DESIGN.get(code, "Pro, other")
        C, H, prompt = run_inputs(name)
        start, done = progress(d)
        finals = {}
        for f in (d / "pages").glob("*.tex") if (d / "pages").is_dir() else []:
            mm = PAGEF.search(f.name)
            if mm:
                finals[(mm.group(1), int(mm.group(2)))] = f
        cotes = {k[0] for k in C}
        done_keys = [k for k in finals if k[1] in done] if done else []
        if not done and kind.startswith("final"):
            done_keys = list(finals)
        missing_c = [k for k in done_keys if k not in C]
        feats = {p: bool(re.search(rx, prompt, re.I)) for p, rx in PHRASES.items()}
        crops = crop_records(d)
        by_scan = collections.defaultdict(list)
        for c in crops:
            by_scan[c["scan"]].append(c)
        for k in sorted(done_keys):
            if k not in C:
                continue
            prow = {}
            analyse_page(code, design, k, C[k], finals[k].read_text(encoding="utf-8", errors="replace"), H.get(k), rows, prow)
            pc = by_scan.get(k[1], [])
            sc = [c["scale"] for c in pc if c["scale"]]
            bw = [c["box_w"] for c in pc if c["box_w"]]
            ow = [c["out_w"] for c in pc if c["out_w"]]
            prow.update(crops=len(pc), crop_src=",".join(sorted({c["src"] for c in pc})),
                        crop_scale_med=round(statistics.median(sc), 2) if sc else "", crop_scale_max=round(max(sc), 2) if sc else "",
                        crops_ge4=sum(x >= 4 for x in sc) if sc else "", crop_box_w_med=round(statistics.median(bw)) if bw else "",
                        crop_out_w_med=round(statistics.median(ow)) if ow else "")
            pages.append(prow)
        times = sorted(done[k[1]] for k in done_keys if k[1] in done)
        hours = (times[-1] - start).total_seconds() / 3600 if times and start else None
        per_scan = collections.Counter(c["scan"] for c in crops)
        scales = [c["scale"] for c in crops if c["scale"]]
        widths = [c["box_w"] for c in crops if c["box_w"]]
        runs[code] = dict(folder=d.name, name=name, kind=kind, stamp=stamp, design=design, features=feats,
                          pages_in_return=len(finals), pages_done=len(done_keys), pages_analysed=sum(1 for k in done_keys if k in C),
                          pages_missing_c=len(missing_c), cotes=sorted(cotes), start=str(start) if start else None,
                          last_done=str(times[-1]) if times else None, hours=round(hours, 2) if hours else None,
                          pages_per_hour=round(len(times) / hours, 1) if hours else None,
                          crops_logged=len(crops), crops_with_scan=sum(1 for c in crops if c["scan"] is not None), crop_sources=sorted({c["src"] for c in crops}),
                          crops_per_done_page=round(sum(per_scan[k[1]] for k in done_keys) / len(done_keys), 1) if done_keys else None,
                          crop_box_w_median=round(statistics.median(widths)) if widths else None,
                          crop_scale_median=statistics.median(scales) if scales else None,
                          crop_scale_share_ge4=round(sum(s >= 4 for s in scales) / len(scales), 3) if scales else None,
                          crop_out_w_median=round(statistics.median([c["out_w"] for c in crops if c["out_w"]])) if any(c["out_w"] for c in crops) else None)
        print(f"{code:6s} {kind:14s} done {len(done_keys):4d} (in pages/ {len(finals):4d}; C missing {len(missing_c)}) "
              f"crops {len(crops):5d} scale~{runs[code]['crop_scale_median']} feats {[p for p, v in feats.items() if v]}")
    # ---- the Claude block second pass of 13 Nov
    cl_pages = 0
    for bd in sorted((T / "second_pass" / "out").iterdir()):
        if not bd.is_dir():
            continue
        src = T / "returns" / f"{bd.name}_unzipped" / "pages"
        for f in sorted(bd.glob("*.tex")):
            mm = PAGEF.search(f.name)
            if not mm:
                continue
            k = (mm.group(1), int(mm.group(2)))
            if re.fullmatch(r"\d{3}-\d{3}", k[0]):  # a scan range, not a cote: the file name carries no cote
                bc = re.match(r"MPL_(\d+(?:-\d+)?)_", bd.name)
                k = (bc.group(1) if bc else k[0], k[1])
            cands = [src / f"{bd.name}_{k[0]}_scan{k[1]:03d}.tex", src / f"{bd.name}_scan{k[1]:03d}.tex"]
            c = next((p for p in cands if p.is_file()), None)
            if c is None:
                continue
            prow = {}
            analyse_page("CLAUDE13", DESIGN["CLAUDE13"], k, c.read_text(encoding="utf-8", errors="replace"),
                         f.read_text(encoding="utf-8", errors="replace"), hua_checkout_page(*k), rows, prow)
            pages.append(prow)
            cl_pages += 1
    runs["CLAUDE13"] = dict(design=DESIGN["CLAUDE13"], pages_analysed=cl_pages)
    print("CLAUDE13 pages analysed", cl_pages)
    # ---- write
    def tsv(path, rs):
        if not rs:
            return
        keys = list(rs[0].keys())
        with open(path, "w", encoding="utf-8", newline="") as fh:
            w = csv.DictWriter(fh, keys, delimiter="\t", extrasaction="ignore")
            w.writeheader()
            w.writerows(rs)
    tsv(OUT / "marks.tsv", rows)
    tsv(OUT / "pages.tsv", pages)
    (OUT / "runs.json").write_text(json.dumps(runs, indent=1, default=str), encoding="utf-8")
    # ---- DM01: our classification against its own decisions.tsv (a check of the aligner)
    dmd = next((d for d in SPR.glob("DM01_*_unzipped")), None)
    if dmd:
        dec = list(csv.DictReader(open(dmd / "decisions.tsv", encoding="utf-8"), delimiter="\t"))
        by_scan = collections.defaultdict(list)
        for r in dec:
            by_scan[int(r["scan"])].append(r)
        ours = collections.defaultdict(list)
        for r in rows:
            if r["run"] == "DM01":
                ours[r["scan"]].append(r)
        chk = []
        for s in sorted(by_scan):
            a, b = by_scan[s], ours.get(s, [])
            for i, r in enumerate(a):
                o = b[i] if i < len(b) else None
                chk.append(dict(scan=s, id=r["id"], dm_decision=r["decision"], dm_reading=r["reading"][:80],
                                our_outcome=o["outcome"] if o else "(no mark at this index)", our_reading=o["final_reading"][:80] if o else "",
                                count_dm=len(a), count_ours=len(b)))
        tsv(OUT / "dm01_check.tsv", chk)
        cm = collections.Counter((c["dm_decision"], c["our_outcome"]) for c in chk)
        print("DM01 check:", sum(len(v) for v in by_scan.values()), "decisions;", sum(len(v) for v in ours.values()), "marks found by us")
        for k, v in cm.most_common():
            print("  ", v, k)
    print("marks", len(rows), "pages", len(pages))


if __name__ == "__main__":
    main()
