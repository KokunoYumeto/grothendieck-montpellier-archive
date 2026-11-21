"""Merge the 940 batch results with the PDF text layer into one readable file (21 Nov 2026, main session, Claude Opus 5.5
at effort max): MASULLO_MATH_VERSION_20261121.md. For each page: its text-layer lines (the prose, correct), and under each
line that carries mathematics the LaTeX of that line from the batch (Claude Opus 5.5 at effort high, Message Batches
API); displayed formulas as display blocks after the line they start on. Also prints token totals.
usage: python -I -B merge_math_version.py"""
import json, pathlib, re, sys
sys.stdout.reconfigure(encoding="utf-8")
HERE = pathlib.Path(__file__).resolve().parent
F = HERE / "full"
res = {}
tin = tout = 0
for f in sorted(F.glob("results_*.jsonl")):
    for line in open(f, encoding="utf-8"):
        r = json.loads(line)
        p = int(r["custom_id"].split("-p")[1])
        res[p] = r
        u = r.get("usage") or {}
        tin += (u.get("input_tokens") or 0) + (u.get("cache_creation_input_tokens") or 0)
        tout += u.get("output_tokens") or 0
ENT = re.compile(r"^([LD])(\d+):\s?(.*)$")
out = ["# Masullo, *The Music of the Primes*: the mathematics keyed to the text layer", "",
       "A. M. Masullo's 940-page draft (posted 20 Nov 2026, announced by R. Vakil; unrefereed), made readable on 21 Nov "
       "2026. The prose of each page is the PDF's text layer, which is correct for words but mangles formulas. The "
       "formulas are re-read from the page images by Claude Opus 5.5 at effort high (Message Batches API), keyed to "
       "the text-layer line they sit on:", "",
       "- `↳` gives the formulas of the line above, in order;",
       "- `$$ ... $$` gives a display that starts at that line.", "",
       "This is a reading aid, not a transcription of record. A formula marked `\\unsure{}` was not read with "
       "certainty; check the PDF page before quoting.", ""]
missing = []
for p in range(1, 941):
    tl = F / "textlayer" / f"p{p:03d}.txt"
    lines = [l.split("\t", 1)[1] if "\t" in l else l for l in tl.read_text(encoding="utf-8").splitlines()] if tl.exists() else []
    r = res.get(p)
    inline, disp = {}, {}
    if r and r.get("type") == "succeeded":
        body = r.get("text") or ""
        m = re.search(r"BEGIN-MATH\s*\n(.*?)\n\s*END-MATH", body, re.S)
        for e in (m.group(1) if m else body).splitlines():
            mm = ENT.match(e.strip())
            if mm:
                (inline if mm.group(1) == "L" else disp).setdefault(int(mm.group(2)), []).append(mm.group(3).strip())
    else:
        missing.append(p)
    out.append(f"## Page {p}")
    out.append("")
    for i, t in enumerate(lines, 1):
        out.append(t)
        for x in inline.get(i, []):
            out.append(f"  ↳ {x}")
        for x in disp.get(i, []):
            out.append("")
            out.append("$$" + x + "$$")
            out.append("")
    out.append("")
(HERE / "MASULLO_MATH_VERSION_20261121.md").write_text("\n".join(out), encoding="utf-8")
print(f"pages {len(res)}; missing or failed {missing}; tokens in {tin:,} out {tout:,}")
print("written", (HERE / "MASULLO_MATH_VERSION_20261121.md").stat().st_size, "bytes")
