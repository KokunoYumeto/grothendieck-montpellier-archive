"""17 Nov 2026 (~02:5x UTC): the 495 edition matters that the follow-ups reader (Claude Opus 5.5 at effort max) found in
the research notes of the returned Pro packages go to the Claude second pass of those packages: one file per package,
second_pass/edition_matters_20261117/<PKG>.md, and make_second_pass.py names the file in each block's prompt (inputs)
with a method step for it. Source: field_experts/FOLLOWUPS_FROM_NOTES_20261117.md, section "Edition matters for the
second pass, by package". usage: python -I -B split_edition_matters_20261117.py"""
import pathlib
import re
import sys

sys.stdout.reconfigure(encoding="utf-8")
T = pathlib.Path("C:/Users/user/Documents/grothendieck_archive_transcription_20261110")
SP = T / "second_pass"
SRC = T.parent / "field_experts" / "FOLLOWUPS_FROM_NOTES_20261117.md"
OUT = SP / "edition_matters_20261117"
OUT.mkdir(exist_ok=True)

s = SRC.read_text(encoding="utf-8")
i = s.index("## Edition matters for the second pass, by package")
j = s.find("\n## ", i + 10)
sec = s[i: j if j > 0 else len(s)]
parts = re.split(r"\n### (\S+)\n", sec)
returns = {d.name[:-len("_unzipped")] for d in (T / "returns").iterdir() if d.is_dir() and d.name.endswith("_unzipped")}
HEAD = """# Edition matters for the second pass: {pkg}

From the research notes of this package's first pass (GPT-6 Astra, ChatGPT Pro mode), sorted by the follow-ups reader
(Claude Opus 5.5 at effort max, 17 Nov 2026). Source: `field_experts/FOLLOWUPS_FROM_NOTES_20261117.md`, where "@n" is
the entry's number. Each item names its scans.

- A reading question, a convention or an error of the page: check it on the scan, then confirm or correct the
  transcription, and record it in the changes table with its @number.
- A proof obligation, a companion cross-reference or a dating lead: carry it into the checked notes with its @number,
  kept or corrected against the corrected text.
- Findings of Michel Hua's project named here are his project's results; credit them to his project.

{n} items:

"""
total, missing = 0, []
for k in range(1, len(parts) - 1, 2):
    pkg, body = parts[k], parts[k + 1]
    items = [l for l in body.splitlines() if l.startswith("- @")]
    if not items:
        continue
    (OUT / f"{pkg}.md").write_text(HEAD.format(pkg=pkg, n=len(items)) + "\n".join(items) + "\n", encoding="utf-8")
    total += len(items)
    if pkg not in returns:
        missing.append(pkg)
print("files:", len(list(OUT.glob("*.md"))), "items:", total)
print("no returns/<PKG>_unzipped for:", missing or "none")

# make_second_pass.py: name the file in the inputs and add a method step, only where the file exists.
M = SP / "make_second_pass.py"
m = M.read_text(encoding="utf-8")
if "edition_matters_20261117" not in m:
    a1 = 'zp = done[0] / f"{pkg}_scans.zip"\n'
    assert m.count(a1) == 1
    m = m.replace(a1, a1 + '''em = SP / "edition_matters_20261117" / f"{pkg}.md"  # 17 Nov 2026: edition matters from the first pass's notes
em_line = ("\\n- Edition matters found in the first pass's notes (the follow-ups reader, 17 Nov 2026): "
           f"`second_pass/edition_matters_20261117/{pkg}.md`. Check those that fall on the scans of this block "
           "(method, step 5).") if em.exists() else ""
em_step = ("\\n5. Check each edition matter of that file that falls on these scans against the image. A reading, a "
           "convention or an error of the page is confirmed or corrected in the transcription and recorded in the "
           "changes table with its @number. A proof obligation, a cross-reference or a dating lead goes into the "
           "checked notes with its @number, kept or corrected against the corrected text.") if em.exists() else ""
''')
    a2 = "- The prompt it ran on (its macros and conventions): `{done[0].relative_to(T).as_posix()}/PROMPT.md`."
    assert m.count(a2) == 1
    m = m.replace(a2, a2 + "{em_line}")
    a3 = "   Grothendieck's spelling, accents, abbreviations and numbering. Never expand, modernise or complete. Do not guess."
    assert m.count(a3) == 1
    m = m.replace(a3, a3 + "{em_step}")
    M.write_text(m, encoding="utf-8", newline="\n")
    print("make_second_pass.py patched")
