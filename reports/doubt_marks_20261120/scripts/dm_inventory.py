"""Every doubt mark in the text of record, with its type, where it sits, and what Hua's text has at the same place
(20 Nov 2026, main session, Claude Opus 5.5 at effort max; part of the doubt-mark report the user asked for on 19 Nov
2026, 23:04 UTC). The text of record is the best reading of each page (text_of_record/MANIFEST.tsv; La Longue Marche is
not in it: its edition is its text). Hua's page is matched by position, word by word, not by a word anywhere on the
page: this replaces the page-wide match of STATE/doubts_vs_hua.py.

python -I -B dm_inventory.py -> ../data/inventory_marks.tsv, ../data/inventory_pages.tsv"""
import collections
import csv
import pathlib
import re
import sys

sys.stdout.reconfigure(encoding="utf-8")
HERE = pathlib.Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
import texalign as TA  # noqa: E402

D = pathlib.Path("<project root>")
T = D / "grothendieck_archive_transcription_20261110"
HUA = D / "ai_math_sources_20261114/hua_michel/commutator_grothendieck-project/transcripts"
OUT = HERE.parent / "data"
state = {(r["cote"], int(r["scan"])): r["state"] for r in csv.DictReader(open(D / "STATE/PAGE_STATE.tsv", encoding="utf-8"), delimiter="\t")}
# the doubt-mark prompts (DMnn): the pages each one covers (the newest prompt wins), and which runs have come back
import zipfile  # noqa: E402
dm_piece = {}
for _d in sorted((T / "doubt_marks_pro_20261119").glob("DM[0-9][0-9]_*")):
    _zp = _d / f"{_d.name}_texts.zip"
    if not _zp.is_file():
        continue
    for n in zipfile.ZipFile(_zp).namelist():
        m = re.search(r"pages/(\d+(?:-\d+)?)_scan(\d{3})\.tex$", n)
        if m:
            dm_piece[(m.group(1), int(m.group(2)))] = _d.name.split("_")[0]
dm_back = {p.name.split("_")[0] for p in (T / "second_pass_returns").glob("DM[0-9][0-9]_*_unzipped")}


def checked_of(base, base_file, in_deleted):
    """20 Nov 2026 (the user: a doubt mark can mean not yet checked, or checked and still doubtful). A mark on a page whose
    text of record is a Pro second pass or a doubt-mark run has been looked at against the scan and left doubtful; DM01
    took every mark of its pages, the later DM prompts the live-text marks only. The 13 Nov Claude pages count as not
    second-passed (the user's decision of 20 Nov), so their marks count as not yet checked."""
    if base == "Pro second pass":
        return "yes", "Pro second pass"
    if base.startswith("doubt marks settled"):
        run = re.search(r"(DM\d\d)_", base_file)
        if (run and run.group(1) == "DM01") or not in_deleted:
            return "yes", "doubt-mark run"
        return "no", "struck-out text the doubt-mark run left out"
    if base == "Claude second pass":
        return "no", "Claude pass of 13 Nov only"
    return "no", "first reading only"


_hua = {}


def hua_page(cote, scan):
    if cote not in _hua:
        pages = {}
        d = HUA / cote
        for f in sorted(d.glob("batch-*.tex")) if d.is_dir() else []:
            parts = re.split(r"\\page\{(\d+)\}", f.read_text(encoding="utf-8", errors="replace"))
            for i in range(1, len(parts) - 1, 2):
                pages[int(parts[i])] = pages.get(int(parts[i]), "") + parts[i + 1]
        _hua[cote] = pages
    return _hua[cote].get(scan - 1)


HMAP = {"first reading confirmed": "Hua = C's first reading", "first reading confirmed (neighbours changed)": "Hua = C's first reading",
        "another listed alternative chosen": "Hua = C's other alternative",
        "another listed alternative chosen (neighbours changed)": "Hua = C's other alternative",
        "still doubtful, same reading": "Hua also uncertain here", "still doubtful, reading changed": "Hua also uncertain here",
        "still illegible": "Hua also uncertain here", "narrowed to a doubtful reading": "Hua also uncertain here",
        "nothing there": "Hua has nothing here", "not aligned (large rewrite here)": "Hua not aligned here",
        "read": "Hua has a reading", "same up to accents, case or punctuation": "Hua = C up to accents/case",
        "a reading not among the alternatives": "Hua has a third reading"}
rows, prows = [], []
man = list(csv.DictReader(open(T / "text_of_record/MANIFEST.tsv", encoding="utf-8"), delimiter="\t"))
for i, r in enumerate(man):
    k = (r["cote"], int(r["scan"]))
    f = T / "text_of_record/pages" / r["cote"] / f"{r['cote']}_scan{k[1]:03d}.tex"
    if not f.is_file():
        f = T / r["base_file"]
    t = f.read_text(encoding="utf-8", errors="replace")
    ct, cm = TA.tokenize(t, TA.OURS)
    zw = TA.zone_words(t, TA.OURS)
    st = state.get(k, "?")
    dmc = dm_piece.get(k)
    if r["base"].startswith("doubt marks settled"):
        _run = re.search(r"(DM\d\d)_", r["base_file"])
        st = f"doubt marks settled by {_run.group(1) if _run else 'a DM run'} (no full second pass)"
    elif dmc and st.startswith("nothing prepared"):
        st = f"{st}; doubt marks in {dmc} ({'the run ended before this page' if dmc in dm_back else 'built, nothing back yet'})"
    h = hua_page(*k)
    if h:
        ht, hm = TA.tokenize(h, TA.HUAS)
        hmap, _, hr = TA.align(ct, ht)
    else:
        ht = hm = hmap = None
        hr = None
    for m in cm:
        if not h:
            hc, hread = "no Hua text for the page", ""
        elif hr < 0.25:
            hc, hread = "Hua's page does not match (ratio < 0.25)", ""
        else:
            o, hread, _ = TA.classify(m, ct, ht, hmap, hm)
            hc = HMAP.get(o, o)
        chk, chk_by = checked_of(r["base"], r["base_file"], m["flags"]["deleted"])
        zone = "diagram" if m["flags"]["diagram"] else "math" if m["flags"]["math"] else "prose"
        rows.append(dict(cote=k[0], scan=k[1], base=r["base"], state=st, kind=m["kind"], nalts=len(m["raw_alts"]) if m["raw_alts"] else 0,
                         words=len(m["alts"][0]) if m["alts"] else 0, in_deleted=int(m["flags"]["deleted"]), in_margin=int(m["flags"]["margin"]),
                         in_inserted=int(m["flags"]["inserted"]), in_math=int(m["flags"]["math"]), in_diagram=int(m["flags"]["diagram"]),
                         zone=zone, checked=chk, checked_by=chk_by,
                         hua=hc, hua_reading=hread[:150], mark=m["text"].replace("\t", " ").replace("\n", " ")[:200]))
    zcols = {}
    for zn in ("prose", "math", "diagram"):
        for sk, sl in ((False, "live"), (True, "struck")):
            w_, l_ = zw.get((zn, sk), [0, 0])
            zcols[f"w_{zn}_{sl}"] = w_
            zcols[f"l_{zn}_{sl}"] = l_
    prows.append(dict(cote=k[0], scan=k[1], base=r["base"], state=st, words=len(ct), marks=len(cm),
                      hua=("none" if not h else "usable" if hr >= 0.25 else "mismatch"), hua_ratio=round(hr, 3) if hr is not None else "", **zcols))
    if i % 2000 == 0:
        print(i, "pages", len(rows), "marks", flush=True)


def tsv(path, rs):
    with open(path, "w", encoding="utf-8", newline="") as fh:
        w = csv.DictWriter(fh, list(rs[0].keys()), delimiter="\t")
        w.writeheader()
        w.writerows(rs)


tsv(OUT / "inventory_marks.tsv", rows)
tsv(OUT / "inventory_pages.tsv", prows)
c = collections.Counter((x["base"], x["kind"]) for x in rows)
print(len(prows), "pages,", len(rows), "marks")
for k, v in sorted(c.items()):
    print(" ", k, v)
print(collections.Counter(x["hua"] for x in rows).most_common())
print(collections.Counter((x["checked"], x["checked_by"]) for x in rows).most_common())
