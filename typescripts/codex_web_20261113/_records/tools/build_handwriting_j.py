"""Build batch J of the Codex-web handwriting folders (14 Nov 2026, Claude Opus 5.5, the agent that built batch H),
after the spot check SPOT_CHECK_H_20261114.md found batch H (GPT-6 Astra in Codex web at effort max) at least as good
as the Pro packages on the B and B-C hands. Batch J holds every B-C cote of HANDWRITING_INVENTORY_20261114.tsv that is
neither sent to Pro (packages_work/RECUT_20261113/SENT_PACKAGES.txt) nor in a Codex-web folder, plus one C-hand pilot
(HC1-01: the eight pages of cote 1 already checked on the Pro return, for a head-to-head comparison).

Same images, template (PROMPT_TEMPLATE_HANDWRITING.md, no draft) and folder form as batch H: it calls
build_handwriting.build(). Blank scans (ink below 0.0003, the builder's own test) are left out and listed.
Reads the archive PDFs only; writes only under codex_web_20261113/. Skips folders that exist.

usage: python -I -B build_handwriting_j.py            (builds)
       python -I -B build_handwriting_j.py --plan     (prints the folders, builds nothing)
"""
import json
import math
import sys
import tempfile
import pathlib

sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent))
import build_codex_web as B  # noqa: E402
import build_handwriting as H  # noqa: E402

M156 = ("They are his handwritten notes of June-July 1986 (the chapter named in the title above), in French, in his "
        "spaced late hand, in which many letters are reduced to strokes, with formulas, diagrams and drawings; the "
        "pages follow on from one another, and the chapter goes on in other tasks before and after these scans.")
CORPUS = [
    # cote, scans, material ; send order = list order
    ("156-7", list(range(10, 115)), M156 + " Scans 2-9 of this chapter were transcribed in an earlier task."),
    ("156-3", list(range(2, 42)), M156),
    ("156-4", list(range(2, 90)), M156),
    ("156-5", list(range(2, 50)), M156),
    ("156-6", list(range(2, 95)), M156),
    ("156-8", list(range(2, 128)), M156),
    ("156-9", list(range(2, 141)), M156),
    ("13", list(range(2, 14)) + list(range(21, 53)),
     "They are his handwritten notes on the subject of the title above (motivic Galois groups, Hodge structures), in "
     "English or French, in his spaced hand, with formulas and struck passages. Scans 14-20 of this cote (a letter "
     "to D. Mumford and notes) are another task."),
    ("53", list(range(2, 35)),
     "They are his handwritten notes on algebraic groups, with a letter (1973) as the title says, in a spaced hand, "
     "with formulas."),
    ("71", list(range(2, 49)),
     "They are his handwritten notes on the Jordan theorem (1976 and undated), in French, with formulas and drawings."),
    ("75", list(range(2, 34)),
     "They are his handwritten notes for the course C4 (DEA), in French, with a letter (1978) and typed pages among "
     "them, as the title says; with formulas and drawings."),
    ("81", list(range(2, 56)),
     "They are his handwritten notes on immersions of the disc and of the circle, in French, with many drawings."),
]
PILOT = ("HC1-01", "1", [4, 12, 15, 24, 27, 35, 39, 49],
         "They are pages of his handwritten working notes on functional analysis, in French, in his dense working "
         "hand, with crossings-out, insertions, margin notes and formulas. The pages are not consecutive: each is "
         "transcribed on its own.")


def inks(cote, scans):
    r = B.row(cote)
    pdf = B.ARCH / r["folder"] / r["file"]
    out = {}
    with tempfile.TemporaryDirectory() as tmp:
        for n in scans:
            im = B.page_image(pdf, n, tmp)
            out[n] = -1.0 if im is None else round(B.ink(im), 4)
    return out


def chunks(xs, size=8):
    k = math.ceil(len(xs) / size)
    q, r = divmod(len(xs), k)
    res, i = [], 0
    for j in range(k):
        m = q + (1 if j < r else 0)
        res.append(xs[i:i + m])
        i += m
    return res


def plan():
    folders, blanks = [], {}
    cache = H.HERE / "J_INKS_20261114.json"
    known = json.loads(cache.read_text(encoding="utf-8")) if cache.exists() else {}
    for cote, scans, mat in CORPUS:
        if cote not in known:
            known[cote] = {str(k): v for k, v in inks(cote, scans).items()}
            cache.write_text(json.dumps(known, indent=0), encoding="utf-8")
        ink = {int(k): v for k, v in known[cote].items()}
        live = [n for n in scans if ink.get(n, -1) >= 0.0003]
        blanks[cote] = [n for n in scans if n not in live]
        for i, part in enumerate(chunks(live), 1):
            fid = f"J{cote}-{i:02d}"
            folders.append((fid, cote, part, mat + (" Blank scans of this range are left out." if blanks[cote] else "")))
    return folders, blanks


if __name__ == "__main__":
    folders, blanks = plan()
    folders.append(PILOT)
    if "--plan" in sys.argv:
        for f in folders:
            print(f[0], f[1], B.ranges(f[2]), len(f[2]))
        print("blanks:", json.dumps(blanks))
        print("pages:", sum(len(f[2]) for f in folders), "folders:", len(folders))
        sys.exit()
    recs = []
    for fid, cote, scans, mat in folders:
        try:
            x = H.build(fid, cote, scans, mat, H.HAND, None)
        except SystemExit as e:
            print("FOLDER FAILED:", fid, e)
            continue
        if x:
            recs.append(x)
    with open(H.HERE / "BUILD_LOG.jsonl", "a", encoding="utf-8") as f:
        for x in recs:
            f.write(json.dumps(x, ensure_ascii=False) + "\n")
    print("blanks:", json.dumps(blanks))
