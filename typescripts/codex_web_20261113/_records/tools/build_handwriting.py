"""Build the handwriting Codex-web folders (series H) of 14 Nov 2026 (Claude Opus 5.5, effort high), from the runs of
HANDWRITING_CANDIDATES_20261114.md, approved by the user ("180 pages of a codex, yeah, build that"). Same form as the
13 Nov folders (build_codex_web.py: flat folder with PROMPT.md, PREAMBLE.tex and <ID>_scans.zip; same images), with
the handwriting prompt PROMPT_TEMPLATE_HANDWRITING.md. The typed pages of cote 63 use the typed template
PROMPT_TEMPLATE_CODEX_WEB.md. A folder may carry a draft by others (DRAFT_*.tex/.pdf), named with its source in the
prompt. Reads the archive PDFs and the drafts only; writes only under codex_web_20261113/. Skips folders that exist.

usage: python -I -B build_handwriting.py
"""
import hashlib
import json
import pathlib
import re
import sys
import tempfile
import zipfile

sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent))
import build_codex_web as B  # noqa: E402  (page_image, ink, jpg, thirds, ranges, row, ARCH, BASE)
from PIL import ImageFilter, ImageOps  # noqa: E402

HERE = pathlib.Path(__file__).resolve().parent
T_HAND = HERE / "PROMPT_TEMPLATE_HANDWRITING.md"
T_TYPED = HERE / "PROMPT_TEMPLATE_CODEX_WEB.md"
DRAFTS = HERE / "drafts_20261114"

# Draft of the letters to L. Breen (cote 134-2): the appendix of chapter I of Pursuing Stacks as edited by M. Carmona
# with U. Buchholtz, arXiv:2111.01000, file ps1.tex, from the line "\chapter*{Appendix: Three letters to Larry Breen}"
# to the end of the file. Extracted by make_drafts() below from the local arXiv source.
PS_SRC = pathlib.Path.home() / "Documents" / "Free or receipted" / "free" / "arxiv-tex" / "2111.01000" / "ps1.tex"
PS_DRAFT = DRAFTS / "DRAFT_PS_Breen_letters.tex"
PS_SOURCE = ("the appendix \"Three letters to Larry Breen\" of chapter I of Pursuing Stacks, in the edition of "
             "M. Carmona with U. Buchholtz, arXiv:2111.01000 (LaTeX source, file ps1.tex). By its own introduction, "
             "Grothendieck's appendix of 1983 gives the letters of 5.2.1975 (its beginning skipped) and 17.2.1975 in "
             "French, the second from a typed copy made by L. Breen, and the letter of 17-19.7.1975 only in R. Brown's "
             "English translation; the editors added section headings and comments. So it is at most a partial "
             "check for the French letters of these scans, and for the July letter it is a translation, not a draft "
             "of the French text: use it there only to check formulas and the order of the passages")


def make_drafts():
    DRAFTS.mkdir(exist_ok=True)
    if PS_SRC.exists() and not PS_DRAFT.exists():
        lines = PS_SRC.read_text(encoding="utf-8").splitlines()
        i = next(k for k, s in enumerate(lines) if s.startswith("\\chapter*{Appendix: Three letters to Larry Breen}"))
        head = ["% DRAFT, not a transcription of these scans. Source: arXiv:2111.01000 (Grothendieck, Pursuing Stacks,",
                "% ed. M. Carmona with U. Buchholtz), file ps1.tex, from its line " + str(i + 1) + " to the end of the file.",
                "% Copied unchanged for checking only (14 Nov 2026). Its macros are the edition's; it is not meant to compile.", ""]
        PS_DRAFT.write_text("\n".join(head + lines[i:]) + "\n", encoding="utf-8")


HAND = "hand"
TYPED = "typed"
M109 = ("They are lists of corrections and comments, handwritten in English, on the typescript of Pursuing Stacks, "
        "in the archive file \"Tables [Corrections et préparation à l'édition]\" (with R. Brown's corrections, "
        "1983-84): page and line references with the words to change, in a small regular hand, with some lines "
        "struck through.")
M63H = ("They are a handwritten formulaire on elliptic curves, in English, in a careful hand (J. Tate's, by the "
        "archive's description of the file; record the hand in the inventory as you see it), dense in formulas, with "
        "a contents page (scan 3) and a table (scan 10); brown ink on yellowed paper.")
M63T = ("They are typed pages (typescripts of the formulaire on elliptic curves, in French or English), with formulas "
        "and symbols filled in by hand and some handwritten corrections.")
M156 = ("They are his handwritten notes of June 1986, \"Analysis situs (troisième mouture)\", in French, in his spaced "
        "late hand, in which many letters are reduced to strokes; the pages follow on from one another.")
M13 = ("They are his handwritten letter in English to D. Mumford, dated Algiers, Nov. 1, 1965 (scans 14-15, a "
       "half-sheet each, signed on scan 15), followed by handwritten notes in English on the same subject (Hodge "
       "structures, the Tate conjecture), scans 16-20, with struck passages.")
M97 = ("They are a handwritten letter of J.-P. Serre in French on Collège de France paper, dated Paris, 4 Nov. 66, in "
       "red ink (scan 2); a handwritten list of names (scan 3); a short handwritten note on Institut des Hautes Études "
       "Scientifiques paper (scan 4); and typed pages with many handwritten corrections, insertions and formulas "
       "(scans 8, 10, 14, 19).")
M37 = ("They are handwritten sheets about the re-edition of SGA and EGA: lists of SGA exposés with notes, in French "
       "(scans 52, 53, 77; 53 and 77 on Institut des Hautes Études Scientifiques paper), a handwritten letter in "
       "English on Harvard University letterhead, signed (scans 54-55), and a handwritten letter in French on graph "
       "paper (scans 75-76).")
M103 = ("They are the correspondence on the thesis of Hoàng Xuân Sính (1974): typed pages (a summary of the thesis "
        "and typed letters) and his handwritten letters in French, in a large spaced hand.")
M104 = ("They are copies of his handwritten notes in French on stacks (\"Champs (stacks) 1\"), in a spaced hand, with "
        "formulas and diagrams.")
M26 = ("They are his handwritten plans, notations and lists of open problems for EGA VI, in French: numbered lists and "
       "short lines, some struck through; scans 4 and 6 are typed.")
M48 = "They are his handwritten plan of EGA VII, in French: a numbered plan with short lines and insertions."
M35 = ("They are the plan of SGA 7: a typed list with handwritten additions (scan 2) and his handwritten lists of "
       "exposés and names (scans 3-5), in French.")
M66 = ("They are his handwritten list of problems (\"Problèmes\", 1964), in French: numbered items, with insertions "
       "and struck words.")
M1621 = ("They are his handwritten list of names and of papers lent (\"Papiers prêtés\"), in French: a list with many "
         "struck lines and additions.")
M1626 = "They are isolated handwritten sheets in pencil, faint, with short formulas (L-functions, class field theory)."
M1341 = ("They are a folder cover (scan 2) and his handwritten letter in French beginning \"Cher Deligne\", in a "
         "spaced hand, with formulas.")
M1342 = ("They are copies of his handwritten letters in French to L. Breen of 1975 (the first on scan 146 begins "
         "\"Cher Larry\"), in a spaced but small hand, on a faint copy, with formulas and diagrams; the pages follow on "
         "from one another.")

PS = (PS_DRAFT, PS_SOURCE)
FOLDERS = [
    # run 1
    ("H109-01", "109", [9, 10, 11, 13, 14, 15, 17, 18, 19], M109 + " Scans 10-11 are a handwritten text in English, "
     "and scans 13-15 are typed (\"Comments on Pursuing Stacks\").", HAND, None),
    ("H109-02", "109", list(range(21, 30)), M109, HAND, None),
    ("H109-03", "109", list(range(30, 39)), M109, HAND, None),
    # run 2
    ("H63-01", "63", list(range(3, 9)), M63H, HAND, None),
    ("H63-02", "63", list(range(9, 15)), M63H, HAND, None),
    ("H63-03", "63", list(range(16, 25)), M63T, TYPED, None),
    ("H63-04", "63", list(range(25, 35)), M63T, TYPED, None),
    ("H63-05", "63", list(range(41, 49)), M63T, TYPED, None),
    ("H63-06", "63", list(range(49, 56)), M63T, TYPED, None),
    ("H63-07", "63", list(range(57, 65)), M63T, TYPED, None),
    ("H63-08", "63", [78, 80, 81, 83, 84, 85], M63T + " Scans 83-85 are a bibliography.", TYPED, None),
    ("H63-09", "63", list(range(87, 95)), M63T, TYPED, None),
    # run 3 (pilot)
    ("H156-01", "156-7", list(range(2, 10)), M156, HAND, None),
    # runs 4-6
    ("H13-01", "13", list(range(14, 21)), M13, HAND, None),
    ("H97-01", "97", [2, 3, 4, 8, 10, 14, 19], M97, HAND, None),
    ("H37-01", "37", [52, 53, 54, 55, 75, 76, 77], M37, HAND, None),
    # run 7
    ("H103-01", "103", [2, 3, 4, 5, 6, 7, 9, 10], M103 + " Scan 8, a blank sheet, is left out.", HAND, None),
    ("H103-02", "103", list(range(11, 19)), M103, HAND, None),
    ("H104-01", "104", list(range(2, 10)), M104, HAND, None),
    ("H104-02", "104", list(range(10, 18)), M104, HAND, None),
    # run 8
    ("H26-01", "26", list(range(2, 12)), M26, HAND, None),
    ("H48-01", "48", list(range(2, 7)), M48, HAND, None),
    ("H35-01", "35", list(range(2, 6)), M35, HAND, None),
    ("H66-01", "66", list(range(2, 6)), M66, HAND, None),
    ("H162-01", "162-1", list(range(2, 11)), M1621, HAND, None),
    ("H162-02", "162-6", list(range(2, 7)), M1626, HAND, None),
    # run 9
    ("H134-01", "134-1", [2, 4, 5, 6, 7], M1341 + " Scan 3, a blank sheet, is left out.", HAND, None),
    ("H134-02", "134-2", list(range(146, 154)), M1342, HAND, PS),
    ("H134-03", "134-2", list(range(154, 162)), M1342, HAND, PS),
    ("H134-04", "134-2", list(range(162, 170)), M1342, HAND, PS),
    ("H134-05", "134-2", list(range(170, 178)), M1342, HAND, PS),
    ("H134-06", "134-2", list(range(178, 186)), M1342, HAND, PS),
]


def draft_text(draft):
    if not draft:
        return {"{DRAFT}": "", "{DRAFT_RULES}": "There is no draft for these pages: transcribe them from the images "
                "alone.", "{DRAFT_DOUBTS}": ""}
    path, src = draft
    n = path.name
    return {
        "{DRAFT}": f"\nThe folder also holds `{n}`, a transcription by others of part of this material: {src}. Use it "
                   "only as the section \"The attached draft\" says.\n",
        "{DRAFT_RULES}": (
            f"`{n}` is a check, not a source, and it is not the page: it may modernize spelling, add headings, correct "
            "slips, leave passages out, or be a translation. Use it in this one way. First transcribe each page from "
            "the images, completely, as if there were no draft. Only then compare your page with the draft, passage "
            "by passage. At every difference, read the ink again on the crop and write what the ink shows; if the "
            "ink does not decide, write `\\unsure{ink reading|draft reading}`, with the reading the ink favours "
            "first. Never write a word from the draft that you have not seen on the page; never take the draft's "
            "headings, notes, corrections or translation into the text; never use it to fill an illegible place. "
            "Passages the draft does not cover are transcribed from the images alone."),
        "{DRAFT_DOUBTS}": "then a table of the differences from the draft (scan, line approximately, your reading, the "
                          "draft's reading, what the ink shows, and your verdict); ",
    }


def build(fid, cote, scans, material, kind, draft):
    out = B.BASE / "drag" / fid
    if (B.BASE / "done" / fid).exists() or out.exists():
        print("exists, skipped:", fid)
        return None
    if draft and not draft[0].exists():
        raise SystemExit(f"{fid}: draft missing: {draft[0]}")
    r = B.row(cote)
    pdf = B.ARCH / r["folder"] / r["file"]
    files, man, inks = [], [], {}
    with tempfile.TemporaryDirectory() as tmp:
        for n in scans:
            im = B.page_image(pdf, n, tmp)
            if im is None or B.ink(im) < 0.0003:
                raise SystemExit(f"{fid}: cote {cote} scan {n} is blank or has no image")
            inks[n] = round(B.ink(im), 4)
            im = ImageOps.autocontrast(im.convert("L"), cutoff=1).filter(
                ImageFilter.UnsharpMask(radius=2, percent=120, threshold=3))
            stem = f"{fid}_{cote}_scan{n:03d}"
            for part, sub in [("whole", im)] + [(f"s{i}", t) for i, t in enumerate(B.thirds(im), 1)]:
                name = stem + ("" if part == "whole" else "_" + part) + ".jpg"
                data = B.jpg(sub)
                files.append((name, data))
                man.append((name, len(data), hashlib.sha256(data).hexdigest(), cote, n, part, sub.size[0], sub.size[1]))
    t = (T_HAND if kind == HAND else T_TYPED).read_text(encoding="utf-8")
    reps = {"{ID}": fid, "{COTE}": cote, "{TITLE}": r["title"], "{DATE}": r["date"], "{COUNT}": str(len(scans)),
            "{SCANS}": B.ranges(scans), "{MATERIAL}": material}
    if kind == HAND:
        reps.update(draft_text(draft))
    for k, v in reps.items():
        t = t.replace(k, v)
    left = re.findall(r"\{(?:ID|COTE|TITLE|DATE|COUNT|SCANS|MATERIAL|DRAFT|DRAFT_RULES|DRAFT_DOUBTS)\}", t)
    if left:
        raise SystemExit(f"placeholders left: {left}")
    out.mkdir(parents=True)
    mtsv = "file\tbytes\tsha256\tcote\tscan\tpart\twidth\theight\n" + "".join("\t".join(map(str, m)) + "\n" for m in man)
    with zipfile.ZipFile(out / f"{fid}_scans.zip", "w", zipfile.ZIP_STORED) as z:
        z.writestr("MANIFEST.tsv", mtsv)
        for name, data in files:
            z.writestr(name, data)
    (out / "PROMPT.md").write_text(t, encoding="utf-8")
    (out / "PREAMBLE.tex").write_bytes(B.PREAMBLE.read_bytes())
    if draft:
        (out / draft[0].name).write_bytes(draft[0].read_bytes())
    z = out / f"{fid}_scans.zip"
    with zipfile.ZipFile(z) as zz:
        assert zz.testzip() is None and len(zz.namelist()) == 1 + 4 * len(scans)
    rec = dict(id=fid, cote=cote, scans=scans, kind=kind, draft=draft[0].name if draft else None, ink=inks,
               pdf=str(pdf).replace(pathlib.Path.home().name, "user"), url=r["url"], title=r["title"], date=r["date"],
               zip_mb=round(z.stat().st_size / 1e6, 1), zip_sha256=hashlib.sha256(z.read_bytes()).hexdigest())
    print(json.dumps(rec, ensure_ascii=False))
    return rec


if __name__ == "__main__":
    make_drafts()
    recs = []
    for f in FOLDERS:
        try:
            x = build(*f)
        except SystemExit as e:
            print("FOLDER FAILED:", f[0], e)
            continue
        if x:
            recs.append(x)
    with open(HERE / "BUILD_LOG.jsonl", "a", encoding="utf-8") as f:
        for x in recs:
            f.write(json.dumps(x, ensure_ascii=False) + "\n")
