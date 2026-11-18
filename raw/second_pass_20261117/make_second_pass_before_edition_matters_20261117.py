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
pages = sorted((ret / "pages").glob(f"{pkg}_scan*.tex"))
assert pages, ret
done = [d for d in (T / "packages_done").iterdir() if d.is_dir() and d.name.endswith(pkg)]
assert len(done) == 1, done
zp = done[0] / f"{pkg}_scans.zip"
n = math.ceil(len(pages) / block); size = math.ceil(len(pages) / n)
for b in range(n):
    chunk = pages[b * size:(b + 1) * size]
    if not chunk:
        continue
    keys = [p.stem.split("_scan")[-1] for p in chunk]
    tag = f"{pkg}_{keys[0]}-{keys[-1]}"
    img = SP / "img" / pkg; img.mkdir(parents=True, exist_ok=True)
    with zipfile.ZipFile(zp) as z:
        names = set(z.namelist())
        for k in keys:
            for suf in ("", "_a", "_b"):
                name = f"{pkg}_scan{k}{suf}.jpg"
                if name in names and not (img / name).exists():
                    (img / name).write_bytes(z.read(name))
    (SP / "out" / pkg).mkdir(parents=True, exist_ok=True)
    files = "\n".join(f"  - returns/{pkg}_unzipped/pages/{p.name}" for p in chunk)
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
- Its notes, doubts and inventory: `returns/{pkg}_unzipped/{pkg}_notes.md`, `{pkg}_doubts.md`, `{pkg}_inventory.csv`.
- The prompt it ran on (its macros and conventions): `{done[0].relative_to(T).as_posix()}/PROMPT.md`.
- The images: `second_pass/img/{pkg}/{pkg}_scanNNN.jpg` (the whole page) and `_a.jpg`, `_b.jpg` (two halves).
  Read both halves of every scan. Where a word or symbol is hard, crop and enlarge it (PIL), and rotate margin notes;
  put crops in `second_pass/work/{tag}/`.

Method:
1. Go through the block scan by scan, line by line, with the image halves. Compare every word, abbreviation, symbol,
   index, sign, inequality, arrow, parenthesis, underline, deletion, insertion and margin note.
2. Settle every doubt mark of the first pass where the ink allows; where it does not, keep `{BS}unsure{{...}}` with
   the alternatives.
3. Look for what the first pass missed: words, conditions, symbols, margin notes, whole lines.
4. Correct the transcription where the image settles it. Keep the first pass's diplomatic conventions and macros,
   Grothendieck's spelling, accents, abbreviations and numbering. Never expand, modernise or complete. Do not guess.

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
