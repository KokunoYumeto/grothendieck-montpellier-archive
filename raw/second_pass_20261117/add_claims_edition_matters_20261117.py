"""17 Nov 2026 (~04:2x UTC): the 115 edition matters of the claims pass (field_experts/CLAIMS_FROM_NOTES_20261117.md, the
follow-ups reader a9ebc3d6, Claude Opus 5.5 at effort max) go to the same per-package files as the first pass's
(second_pass/edition_matters_20261117/<PKG>.md): appended as a section to an existing file, or a new file with the same
header. Then the block prompts of packages that had no file are rebuilt (make_second_pass.py), so that they name it.
usage: python -I -B add_claims_edition_matters_20261117.py"""
import pathlib
import re
import subprocess
import sys

sys.stdout.reconfigure(encoding="utf-8")
SP = pathlib.Path(__file__).resolve().parent
T = SP.parent
SRC = T.parent / "field_experts" / "CLAIMS_FROM_NOTES_20261117.md"
OUT = SP / "edition_matters_20261117"
HEAD = """# Edition matters for the second pass: {pkg}

From the research notes of this package's first pass (GPT-6 Astra, ChatGPT Pro mode), sorted by the follow-ups reader
(Claude Opus 5.5 at effort max, 17 Nov 2026). Each item names its scans.

- A reading question, a convention or an error of the page: check it on the scan, then confirm or correct the
  transcription, and record it in the changes table with its number.
- A proof obligation, a companion cross-reference or a dating lead: carry it into the checked notes with its number,
  kept or corrected against the corrected text.
- Findings of Michel Hua's project named here are his project's results; credit them to his project.
"""
SEC = """
## From the claims pass (Grothendieck's unproved claims; 17 Nov 2026)

Source: `field_experts/CLAIMS_FROM_NOTES_20261117.md`, where "#n" is the entry's number in the claims map. References
given there for known results come from the reader's memory: check them before citing. {n} items:

"""
s = SRC.read_text(encoding="utf-8")
i = s.index("## Edition matters for the second pass, by package")
j = s.find("\n## ", i + 10)
parts = re.split(r"\n### (\S+)\n", s[i: j if j > 0 else len(s)])
new_files, appended, total = [], 0, 0
for k in range(1, len(parts) - 1, 2):
    pkg, body = parts[k], parts[k + 1]
    items = [l for l in body.splitlines() if l.startswith("- #")]
    if not items:
        continue
    f = OUT / f"{pkg}.md"
    text = f.read_text(encoding="utf-8") if f.exists() else HEAD.format(pkg=pkg)
    if "## From the claims pass" in text:
        text = text[: text.index("\n## From the claims pass")] + "\n"
    if not f.exists():
        new_files.append(pkg)
    text = text.rstrip("\n") + "\n" + SEC.format(n=len(items)) + "\n".join(items) + "\n"
    f.write_text(text, encoding="utf-8", newline="\n")
    appended += 1
    total += len(items)
print("packages:", appended, "items:", total, "new files:", new_files)
for pkg in new_files:  # their prompts were built before the file existed: rebuild them (images exist, so this is fast)
    if not (T / "returns" / f"{pkg}_unzipped").is_dir():
        print("  no return folder for", pkg)
        continue
    if (SP / "out" / pkg).is_dir() and any((SP / "out" / pkg).iterdir()):
        print("  second pass already done, prompts kept as run:", pkg)  # never overwrite the prompts a pass ran on
        continue
    p = subprocess.run([sys.executable, "-I", "-B", str(SP / "make_second_pass.py"), pkg], capture_output=True, text=True,
                       encoding="utf-8", errors="replace", cwd=str(SP))
    print("  rebuilt", pkg, "exit", p.returncode, (p.stdout + p.stderr).strip().replace("\n", " | ")[:200])
