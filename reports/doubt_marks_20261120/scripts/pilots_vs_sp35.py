"""The Claude pilots of 19 Nov against Pro's SP35 on the same pages (cote 156-7, scans 2-6), at witness C's doubt marks
(20 Nov 2026, main session, Claude Opus 5.5 at effort max). For each reader's page: what it did with each of C's
marks, and whether its reading there agrees with SP35's final text (Pro, three readers + the reading workflow of
21:07 UTC). Agreement is not accuracy: neither text has been checked against the scan at these places.
python -I -B pilots_vs_sp35.py -> ../data/pilots_vs_sp35.tsv"""
import collections
import csv
import pathlib
import sys

sys.stdout.reconfigure(encoding="utf-8")
HERE = pathlib.Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
import texalign as TA  # noqa: E402

T = pathlib.Path("<project root>/grothendieck_archive_transcription_20261110")
P = T / "second_pass_claude_pilot_20261119"
CW = P / "D_two_high_debate/in/witnesses/codex/H156-01/pages"
SP35 = next((T / "second_pass_returns").glob("SP35_*_unzipped")) / "pages"
READERS = {
    "A R1 (high)": P / "A_lead_three_readers/readers/R1/pages", "A R2 (high)": P / "A_lead_three_readers/readers/R2/pages",
    "A R3 (high)": P / "A_lead_three_readers/readers/R3/pages", "B (max)": P / "B_one_reader/out/pages",
    "C R1 (max)": P / "C_two_max_debate/readers/R1/pages", "C R2 (max)": P / "C_two_max_debate/readers/R2/pages",
    "D R1 (high)": P / "D_two_high_debate/readers/R1/pages", "D R2 (high)": P / "D_two_high_debate/readers/R2/pages",
    "E1a (high, 10 crops)": P / "E_capped_high/E1a/pages", "E1b (high, 10 crops)": P / "E_capped_high/E1b/pages",
}
RES = {"first reading confirmed", "first reading confirmed (neighbours changed)", "another listed alternative chosen",
       "another listed alternative chosen (neighbours changed)", "a reading not among the alternatives",
       "same up to accents, case or punctuation", "nothing there", "read"}
rows = []
for scan in range(2, 7):
    name = f"H156-01_156-7_scan{scan:03d}.tex"
    c = (CW / name).read_text(encoding="utf-8", errors="replace")
    ct, cm = TA.tokenize(c)
    st, sm = TA.tokenize((SP35 / name).read_text(encoding="utf-8", errors="replace"))
    smap, _, _ = TA.align(ct, st)
    sp = [TA.classify(m, ct, st, smap, sm) for m in cm]
    for who, d in READERS.items():
        f = d / name
        if not f.is_file():
            continue
        rt, rm = TA.tokenize(f.read_text(encoding="utf-8", errors="replace"))
        rmap, _, _ = TA.align(ct, rt)
        for i, m in enumerate(cm):
            o, rr, _ = TA.classify(m, ct, rt, rmap, rm)
            so, sr, _ = sp[i]
            rows.append(dict(scan=scan, reader=who, idx=i, kind=m["kind"], reader_outcome=o, sp35_outcome=so,
                             reader_resolved=int(o in RES), sp35_resolved=int(so in RES),
                             same_reading=int(rr == sr), reader_reading=rr[:120], sp35_reading=sr[:120], mark=m["text"][:120]))
with open(HERE.parent / "data/pilots_vs_sp35.tsv", "w", encoding="utf-8", newline="") as fh:
    w = csv.DictWriter(fh, list(rows[0].keys()), delimiter="\t")
    w.writeheader()
    w.writerows(rows)
agg = collections.defaultdict(collections.Counter)
for r in rows:
    a = agg[r["reader"]]
    a["marks"] += 1
    a["pages"] = len({x["scan"] for x in rows if x["reader"] == r["reader"]})
    a["reader resolved"] += r["reader_resolved"]
    a["SP35 resolved"] += r["sp35_resolved"]
    a["same reading as SP35"] += r["same_reading"]
    a["both resolved"] += r["reader_resolved"] and r["sp35_resolved"]
    a["both resolved, same"] += r["reader_resolved"] and r["sp35_resolved"] and r["same_reading"]
for who, a in agg.items():
    print(f"{who:22s} pages {a['pages']} marks {a['marks']:3d} | resolved: reader {a['reader resolved']:3d}, SP35 {a['SP35 resolved']:3d} | "
          f"same reading {a['same reading as SP35']:3d} | both resolved {a['both resolved']:3d}, of which same {a['both resolved, same']:3d}")
