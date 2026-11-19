"""Print a Codex-web transcription compactly, page by page, for study (agent a84c887cf408574ed,
Claude Opus 5.5 at effort max, SA13 lead, sweep 3, 19 Nov 2026).

python -I -B readcodex.py <folder> [first_scan] [last_scan] [keepdel] [--macros]

<folder> is a Codex-web return folder such as K34-01, A36-02 or K27-01; the file read is
grothendieck_archive_transcription_20261110/codex_web_20261113/returns/<folder>/out/<folder>_transcription.tex.
Cleaning is readtex.clean from sweep2/_tools_a28ea31f (\\deleted dropped unless keepdel, \\unsure{a|b} -> a(?),
figures dropped, margins inline), plus the Codex macros \\handwritten, \\uuline, \\typed, \\cotefile unwrapped.
--macros prints the macro counts of the file instead.
"""
import re, sys, glob, collections, importlib.util
from pathlib import Path
sys.stdout.reconfigure(encoding="utf-8", errors="replace")
DOC = Path(r"C:/Users/user/Documents")
CW = DOC / "grothendieck_archive_transcription_20261110" / "codex_web_20261113" / "returns"
spec = importlib.util.spec_from_file_location("readtex", str(DOC / "results_register/horizontal/sweep2/_tools_a28ea31f/readtex.py"))
rt = importlib.util.module_from_spec(spec)
spec.loader.exec_module(rt)


def main():
    folder = sys.argv[1]
    nums = [int(x) for x in sys.argv[2:4] if x.isdigit()]
    a, b = (nums + [0, 10 ** 6])[:2] if len(nums) == 2 else (0, 10 ** 6)
    keep = "keepdel" in sys.argv
    p = CW / folder / "out" / f"{folder}_transcription.tex"
    if not p.exists():
        alt = sorted(glob.glob(str(CW / folder / "out" / "*_transcription.tex")))
        p = Path(alt[0])
    t = p.read_text(encoding="utf-8")
    if "--macros" in sys.argv:
        print(collections.Counter(re.findall(r"\\([a-zA-Z]+)\{", t)).most_common(40))
        return
    cote = (re.search(r"\\cotefile\{(\d+)\}", t) or re.search(r"K(\d+)|A(\d+)", folder))
    cote = cote.group(1) if cote and cote.group(1) else re.sub(r"\D", "", folder.split("-")[0])
    parts = re.split(r"\\scanpage\{(\d+)\}", t)
    for i in range(1, len(parts), 2):
        n = int(parts[i])
        if not a <= n <= b:
            continue
        s = parts[i + 1]
        for name in ("handwritten", "uuline", "typed", "cotefile", "textit", "emph"):
            s = rt.strip_cmd(s, name, (lambda x: "") if name == "cotefile" else (lambda x: x))
        c = rt.clean(s, keep)
        if "--nodiag" in sys.argv:
            c = re.sub(r"\\begin\{tikzcd\}.*?\\end\{tikzcd\}", "[diagram]", c, flags=re.S)
        print(f"=== {cote}:{n}")
        print(c)


if __name__ == "__main__":
    main()
