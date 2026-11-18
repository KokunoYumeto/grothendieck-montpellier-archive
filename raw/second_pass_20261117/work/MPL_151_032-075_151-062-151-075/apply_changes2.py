"""Second set of edits on the corrected pages (after apply_changes.py): where the ink does not decide and
Michel Hua's transcription (batch-04) reads otherwise, his reading is added to the alternatives of the doubt mark."""
import os
import sys

DST = r"C:/Users/user/Documents/grothendieck_archive_transcription_20261110/second_pass/out/MPL_151_032-075"
NAME = "MPL_151_032-075_151_scan{}.tex"

CHANGES = {
    "064": [(r"\deleted{\unsure{p}} topos-pierres", r"\deleted{\unsure{p}} \unsure{topos|types}-pierres")],
    "065": [(r"ce diagramme \unsure{est en.|est env.} (19).", r"ce diagramme \unsure{est en.|est env.|est celui de} (19).")],
    "067": [(r"\deleted{$I$ fini}", r"\unsure{\deleted{$I$ fini}|$I$ fini}")],
    "068": [(r"\unsure{X_{n-1}^*|X_{m-1}^*}", r"\unsure{X_{n-1}^*|X_{m-1}^*|X_{n-2}^*}")],
    "069": [
        (r"\unsure{1\textsuperscript{ère}|1\textsuperscript{ière}}",
         r"\unsure{1\textsuperscript{ère}|1\textsuperscript{ière}|p\textsuperscript{re}}"),
        (r"$U_{ij}^*=U_{ij}\setminus X_i^*$", r"$\unsure{U_{ij}^*|V_{ij}^*}=\unsure{U_{ij}|V_{ij}}\setminus X_i^*$"),
    ],
}

for scan, changes in CHANGES.items():
    p = os.path.join(DST, NAME.format(scan))
    with open(p, encoding="utf-8", newline="") as f:
        text = f.read()
    for old, new in changes:
        n = text.count(old)
        if n != 1:
            sys.exit(f"scan {scan}: {n} occurrences of {old!r}")
        text = text.replace(old, new)
    with open(p, "w", encoding="utf-8", newline="") as f:
        f.write(text)
    print(scan, len(changes), "edits")
