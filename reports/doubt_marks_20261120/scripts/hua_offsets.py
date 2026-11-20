"""Pages where Hua's page (his page n = our scan n + 1) does not match our text: is another offset right? (20 Nov 2026,
main session, Claude Opus 5.5 at effort max). For every page of the text of record whose Hua page aligns with a ratio
under 0.25, Hua's pages at offsets -3..+3 around the usual one are tried; the best with a ratio of at least 0.40 is
recorded. python -I -B hua_offsets.py -> ../data/hua_offsets.tsv; prints the offsets found, by cote."""
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
_hua = {}


def hua_pages(cote):
    if cote not in _hua:
        pages = {}
        d = HUA / cote
        for f in sorted(d.glob("batch-*.tex")) if d.is_dir() else []:
            parts = re.split(r"\\page\{(\d+)\}", f.read_text(encoding="utf-8", errors="replace"))
            for i in range(1, len(parts) - 1, 2):
                pages[int(parts[i])] = pages.get(int(parts[i]), "") + parts[i + 1]
        _hua[cote] = pages
    return _hua[cote]


inv = [r for r in csv.DictReader(open(HERE.parent / "data/inventory_pages.tsv", encoding="utf-8"), delimiter="\t") if r["hua"] == "mismatch"]
man = {(r["cote"], int(r["scan"])): r for r in csv.DictReader(open(T / "text_of_record/MANIFEST.tsv", encoding="utf-8"), delimiter="\t")}
out = []
for r in inv:
    k = (r["cote"], int(r["scan"]))
    f = T / "text_of_record/pages" / k[0] / f"{k[0]}_scan{k[1]:03d}.tex"
    if not f.is_file():
        f = T / man[k]["base_file"]
    ct, _ = TA.tokenize(f.read_text(encoding="utf-8", errors="replace"))
    hp = hua_pages(k[0])
    best = (0.0, None)
    for dlt in (-3, -2, -1, 1, 2, 3):
        h = hp.get(k[1] - 1 + dlt)
        if not h:
            continue
        ht, _ = TA.tokenize(h, TA.HUAS)
        _, _, ratio = TA.align(ct, ht)
        if ratio > best[0]:
            best = (ratio, dlt)
    out.append(dict(cote=k[0], scan=k[1], ratio_at_usual=r["hua_ratio"], best_offset=best[1] if best[0] >= 0.4 else "",
                    best_ratio=round(best[0], 3)))
with open(HERE.parent / "data/hua_offsets.tsv", "w", encoding="utf-8", newline="") as fh:
    w = csv.DictWriter(fh, list(out[0].keys()), delimiter="\t")
    w.writeheader()
    w.writerows(out)
by = collections.defaultdict(collections.Counter)
for o in out:
    by[o["cote"]][o["best_offset"] if o["best_offset"] != "" else "none"] += 1
found = sum(1 for o in out if o["best_offset"] != "")
print(len(out), "mismatched pages;", found, "match at another offset")
for c, v in sorted(by.items(), key=lambda kv: -sum(kv[1].values()))[:30]:
    print(" ", c, dict(v))
