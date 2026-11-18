"""Second pass of the archive transcriptions (Claude Opus 5.5 at effort max; user, 12-13 Nov 2026): cut a returned
package into blocks of about 19 scans, extract each block's images from the package's scans zip, and write one prompt
file per block. usage: python -I -B make_second_pass.py PKG [BLOCK]   (PKG as in returns/<PKG>_unzipped)
Paths in the prompts use forward slashes; BS is the backslash of LaTeX macro names."""
import math, pathlib, sys, zipfile
sys.stdout.reconfigure(encoding="utf-8")
BS = chr(92)
T = pathlib.Path("C:/Users/user/Documents/grothendieck_archive_transcription_20261110")
SP = T / "second_pass"
pkg = sys.argv[1]; block = int(sys.argv[2]) if len(sys.argv) > 2 else 19
ret = T / "returns" / f"{pkg}_unzipped"
if not (ret / "pages").is_dir() and (ret / pkg / "pages").is_dir():  # 17 Nov 2026: some returns unpacked one level deeper
    ret = ret / pkg
RET = ret.relative_to(T).as_posix()
MAN = T / "packages_work" / pkg / "MANIFEST.json"
TOOLS = pathlib.Path("C:/Users/user/Documents/grothendieck_archive_tools_20261110")


def manifest_pdfs():
    """cote -> source PDF, in the package's order (both manifest formats: the multi-cote 'files' list, or one cote)."""
    import json
    if not MAN.exists():
        return {}
    man = json.loads(MAN.read_text(encoding="utf-8"))
    if "files" in man:
        return {str(f["cote"]): pathlib.Path(f["source_pdf"]) for f in man["files"]}
    return {str(man["cote"]): pathlib.Path(man["source_pdf"])}


PDFS = manifest_pdfs()


def cote_scan(p):
    """(cote, scan number) of a page file: <PKG>_<cote>_scanNNN.tex, or <PKG>_scanNNN.tex for a one-cote package."""
    key = p.stem[len(pkg) + 1:]
    if "_scan" in key:
        c, n = key.rsplit("_scan", 1)
        return c, int(n)
    return (next(iter(PDFS)) if len(PDFS) == 1 else ""), int(key[len("scan"):])


def page_order(p):
    c, n = cote_scan(p)
    order = list(PDFS)
    return (order.index(c) if c in order else len(order), c, n)


def render_missing(chunk, img):
    """The builder's images again, from the source PDF (see the docstring of the patch of 17 Nov 2026)."""
    import tempfile
    from PIL import ImageFilter, ImageOps
    sys.path.insert(0, str(TOOLS))
    from build_package import page_image
    with tempfile.TemporaryDirectory() as tmp:
        for p in chunk:
            if all((img / f"{p.stem}{suf}.jpg").exists() for suf in ("", "_a", "_b")):
                continue
            c, n = cote_scan(p)
            ctmp = pathlib.Path(tmp) / f"c_{c}_{n}"
            ctmp.mkdir()
            im = page_image(PDFS[c], n, ctmp)
            if im is None:
                print("  no image in the PDF for", p.name)
                continue
            im = ImageOps.autocontrast(im, cutoff=1).filter(ImageFilter.UnsharpMask(radius=2, percent=120, threshold=3))
            w, h = im.size
            if w > h:
                p1, p2 = im.crop((0, 0, w // 2 + 60, h)), im.crop((w // 2 - 60, 0, w, h))
            else:
                p1, p2 = im.crop((0, 0, w, h // 2 + 80)), im.crop((0, h // 2 - 80, w, h))
            im.save(img / f"{p.stem}.jpg", quality=88)
            p1.save(img / f"{p.stem}_a.jpg", quality=88)
            p2.save(img / f"{p.stem}_b.jpg", quality=88)


pages = sorted((ret / "pages").glob(f"{pkg}_*scan*.tex"), key=page_order)  # 17 Nov 2026: also <PKG>_<cote>_scanNNN.tex (multi-cote packages)
assert pages, ret
done = [d for d in (T / "packages_done").iterdir() if d.is_dir() and d.name.endswith(pkg)]
assert len(done) == 1, done
zp = done[0] / f"{pkg}_scans.zip"
em = SP / "edition_matters_20261117" / f"{pkg}.md"  # 17 Nov 2026: edition matters from the first pass's notes
em_line = ("\n- Edition matters found in the first pass's notes (the follow-ups reader, 17 Nov 2026): "
           f"`second_pass/edition_matters_20261117/{pkg}.md`. Check those that fall on the scans of this block "
           "(method, step 5).") if em.exists() else ""
cb = T / "returns" / f"{pkg}_chatB_unzipped"  # 17 Nov 2026: a second Pro run of the same package, if any
if not (cb / "pages").is_dir() and (cb / pkg / "pages").is_dir():
    cb = cb / pkg
cb_line = ("\n- A second Pro run of the same package (chat B), as a further witness: "
           f"`{cb.relative_to(T).as_posix()}/pages/`, with the same file names. Where the two runs differ, the image "
           "decides; a difference that neither the image nor the context settles goes in the unresolved places.") \
    if (cb / "pages").is_dir() else ""
emb = SP / "edition_matters_20261117" / f"{pkg}_chatB.md"  # 17 Nov 2026: the chat B run's own edition matters
if cb_line and emb.exists():
    cb_line += (f" Its notes' edition matters: `second_pass/edition_matters_20261117/{pkg}_chatB.md`; check them as "
                "those of step 5.")
em_step = ("\n5. Check each edition matter of that file that falls on these scans against the image. A reading, a "
           "convention or an error of the page is confirmed or corrected in the transcription and recorded in the "
           "changes table with its number (@n or #n). A proof obligation, a cross-reference or a dating lead goes into the "
           "checked notes with its number, kept or corrected against the corrected text.") if em.exists() else ""
n = math.ceil(len(pages) / block); size = math.ceil(len(pages) / n)
for b in range(n):
    chunk = pages[b * size:(b + 1) * size]
    if not chunk:
        continue
    keys = [p.stem[len(pkg) + 1:].replace("_scan", "-").replace("scan", "") for p in chunk]  # "001" or "105-002"
    tag = f"{pkg}_{keys[0]}-{keys[-1]}"
    img = SP / "img" / pkg; img.mkdir(parents=True, exist_ok=True)
    if zp.exists():
        with zipfile.ZipFile(zp) as z:
            names = set(z.namelist())
            for p in chunk:  # 17 Nov 2026: each image is named as its page file
                for suf in ("", "_a", "_b"):
                    name = f"{p.stem}{suf}.jpg"
                    if name in names and not (img / name).exists():
                        (img / name).write_bytes(z.read(name))
    else:  # 17 Nov 2026: the scans zips of the packages of 11-12 Nov are gone: render from the source PDFs
        render_missing(chunk, img)
    (SP / "out" / pkg).mkdir(parents=True, exist_ok=True)
    files = "\n".join(f"  - {RET}/pages/{p.name}" for p in chunk)
    prompt = f"""# Second pass: check a first-pass transcription of a Grothendieck manuscript against the scans

You check and correct a diplomatic LaTeX transcription of manuscript pages from the Grothendieck archive at
Montpellier, made blind from the scans by GPT-6 Astra (ChatGPT Pro mode). Nobody has edited these pages before: your
pass is the first check they get. The sample checks of such first passes found about 0.5 to 2 errors per 100 words:
fluent misreadings that put a plausible mathematical word where the ink says something else, dropped conditions and
symbols, wrong indices and signs, missed deletions and insertions. Only some of them carry a doubt mark.

Block: {tag}, {len(chunk)} scans. All paths are under `C:/Users/user/Documents/grothendieck_archive_transcription_20261110`.

Inputs:
- The first pass, one file per scan:
{files}
- Its notes, doubts and inventory: `{RET}/{pkg}_notes.md`, `{pkg}_doubts.md`, `{pkg}_inventory.csv`.
- The prompt it ran on (its macros and conventions): `{done[0].relative_to(T).as_posix()}/PROMPT.md`.{em_line}{cb_line}
- The images: `second_pass/img/{pkg}/`, each named as its page file, with `.jpg` (the whole page) and `_a.jpg`, `_b.jpg`
  (the two halves).
  Read both halves of every scan. Where a word or symbol is hard, crop and enlarge it (PIL), and rotate margin notes;
  put crops in `second_pass/work/{tag}/`.

Method:
1. Go through the block scan by scan, line by line, with the image halves. Compare every word, abbreviation, symbol,
   index, sign, inequality, arrow, parenthesis, underline, deletion, insertion and margin note.
2. Settle every doubt mark of the first pass where the ink allows; where it does not, keep `{BS}unsure{{...}}` with
   the alternatives.
3. Look for what the first pass missed: words, conditions, symbols, margin notes, whole lines.
4. Correct the transcription where the image settles it. Keep the first pass's diplomatic conventions and macros,
   Grothendieck's spelling, accents, abbreviations and numbering. Never expand, modernise or complete. Do not guess.{em_step}

Work economically: read each scan's two halves once and settle what you can from them; make an enlarged crop only
where the first pass and your reading still disagree, or where a symbol decides the mathematics. Aim at no more than
about 120 tool calls for the block. Write each output file once, at the end.

Write, under `second_pass/out/{pkg}/`:
- the corrected file of every scan of the block, with the same name as the first-pass file;
- `{tag}_changes.md`: one table row per change: scan, place, first-pass reading, corrected reading, evidence (what
  the image shows), confidence (high, medium, low); then the places still unresolved;
- `{tag}_notes_checked.md`: the first pass's notes on these scans (Grothendieck's claims, conjectures, questions,
  implications not pursued), each checked against the corrected text: keep, correct or drop it, with a reason; add
  your own notes of the same kinds, labelled as yours, with the scan number.

Final message, short: the counts (scans, changes by confidence, unresolved places) and the consequential corrections
(those that change the mathematics), one per line. Nothing else.
"""
    pf = SP / "prompts" / f"PROMPT_{tag}.md"
    pf.write_text(prompt, encoding="utf-8")
    print(pf.name, len(chunk), "scans")
