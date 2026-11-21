"""Masullo's GRH draft (940 pages, pdfTeX, no source posted): the mathematics only, keyed to the PDF text layer (21 Nov
2026, main session, Claude Opus 5.5 at effort max). The user, 20 Nov 22:39 UTC: "Only the math, yes. Text layer has the
pro statements. Would only get page plus text layer and return only the math as LaTeX key to the text layer line";
22:44 UTC: "you can do the API thing. Just make sure to use batch"; 21 Nov ~01:5x UTC: "we also need to have a version of
the other GRH proof because they both show different things that might be relevant."
Per page: the numbered text layer plus the page as two overlapping 200-dpi halves (the pilot of 20 Nov), to
Claude Opus 5.5 at effort high over the Message Batches API. Requests are split into files under 200 MB (the API's
batch limit is 256 MB).
usage: python -E -B build_math_batch.py pilot|all|<p1,p2,...>   (PyMuPDF needs -E here, not -I)"""
import base64, io, json, pathlib, sys
import fitz  # PyMuPDF
from PIL import Image

HERE = pathlib.Path(__file__).resolve().parent
PDF = HERE.parents[1] / "Papors/Chatnotes/Zeta-Function-Foundation/literature/masullo_grh_20261120/Masullo_the-music-of-the-primes.pdf"
arg = sys.argv[1] if len(sys.argv) > 1 else "pilot"
doc = fitz.open(PDF)
PAGES = ([12, 16, 28, 300, 517] if arg == "pilot" else list(range(1, doc.page_count + 1)) if arg == "all"
         else [int(x) for x in arg.split(",")])
OUT = HERE / ("pilot" if arg == "pilot" else "full" if arg == "all" else "custom")
OUT.mkdir(parents=True, exist_ok=True)

SYSTEM = """You extract the mathematics of one page of a typeset mathematics paper (made with LaTeX and pdfTeX).

You get the page as two overlapping images (top half, bottom half) and its PDF text layer with numbered lines. The text layer carries the prose correctly but mangles the mathematics: symbols are lost, sub- and superscripts flattened, fractions and displays broken into pieces.

Return the mathematics of the page, and only the mathematics, as LaTeX keyed to the text-layer lines:
- For every text-layer line that contains mathematics in running text, one entry `L<n>: ` followed by all formulas of that line in order, each in $...$, separated by ` ; `.
- For every displayed formula, one entry `D<n>: ` followed by the display in LaTeX (an equation or align environment body), where n is the text-layer line the display starts on; put a printed equation number in \\tag{...}.
- For every theorem-type heading with a formula in it, an `L<n>:` entry as above.
- Match the printed notation exactly: letters, fonts (\\mathcal, \\mathfrak, \\mathbb, \\mathrm, bold), accents, sub- and superscripts, brackets.
- If a symbol cannot be read with certainty, write your best reading inside \\unsure{...}.
- Do not transcribe prose, do not correct, complete or comment. Lines without mathematics get no entry.

Answer between a line BEGIN-MATH and a line END-MATH, one entry per line."""


def halves(page):
    pix = page.get_pixmap(dpi=200)
    img = Image.frombytes("RGB", (pix.width, pix.height), pix.samples)
    h = img.height
    out = []
    for im in (img.crop((0, 0, img.width, int(h * 0.55))), img.crop((0, int(h * 0.45), img.width, h))):
        buf = io.BytesIO()
        im.save(buf, format="JPEG", quality=90)
        out.append(buf.getvalue())
    return out


files, cur, size = [], [], 0
for p in PAGES:
    page = doc[p - 1]
    lines = page.get_text().splitlines()
    numbered = "\n".join(f"{i}\t{t}" for i, t in enumerate(lines, 1))
    (OUT / "textlayer").mkdir(exist_ok=True)
    (OUT / "textlayer" / f"p{p:03d}.txt").write_text(numbered, encoding="utf-8")
    content = [{"type": "text", "text": f"Page {p} of {doc.page_count}. Image 1 is the top half, image 2 the bottom half."}]
    for data in halves(page):
        content.append({"type": "image", "source": {"type": "base64", "media_type": "image/jpeg",
                                                    "data": base64.b64encode(data).decode("ascii")}})
    content.append({"type": "text", "text": "The page's text layer, numbered:\n\n" + numbered +
                    "\n\nReturn the mathematics of this page as instructed."})
    req = {"custom_id": f"math-p{p:03d}",
           "params": {"model": "claude-opus-5-5", "max_tokens": 16000, "thinking": {"type": "adaptive"},
                      "output_config": {"effort": "high"}, "system": SYSTEM,
                      "messages": [{"role": "user", "content": content}]}}
    line = json.dumps(req) + "\n"
    if size + len(line) > 200_000_000 and cur:
        files.append(cur); cur, size = [], 0
    cur.append(line); size += len(line)
if cur:
    files.append(cur)
for i, chunk in enumerate(files, 1):
    (OUT / f"requests_{i:02d}.jsonl").write_text("".join(chunk), encoding="utf-8")
    print(f"requests_{i:02d}.jsonl: {len(chunk)} pages, {sum(len(x) for x in chunk) / 1e6:.0f} MB")
print("pages:", len(PAGES), "->", OUT)
