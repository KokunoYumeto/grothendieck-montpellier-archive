"""Split a Codex-web drag folder's scans zip into parts under 9 MB (Claude in Chrome uploads at most 10 MB a call),
keeping each scan's four images together and MANIFEST.tsv and every non-scan file (such as hua/) in part 1; copy
PREAMBLE.tex; add one paragraph to PROMPT.md naming the parts; and write <ID>_PROMPT.zip holding that PROMPT.md, for
when the .md fails to load in Chrome (K34-01, 17 Nov 2026).
usage: python -I -B tools/split_for_chrome.py [--dst <dir>] <src_dir> <ID>...
       python -I -B tools/split_for_chrome.py --prompt-only [--dst <dir>] <src_dir> <ID>...
         (an existing split folder: rewrite PROMPT.md from <src_dir>/<ID>/PROMPT.md and its PROMPT.zip; zips kept)"""
import sys, zipfile, pathlib, shutil
from collections import OrderedDict
base = pathlib.Path(__file__).resolve().parent.parent
args = sys.argv[1:]
prompt_only = "--prompt-only" in args
args = [a for a in args if a != "--prompt-only"]
dst_root = base / "drag_split"
if args[:1] == ["--dst"]:
    dst_root = base / args[1]
    args = args[2:]
src_dir = base / args[0]
LIM = 8_950_000  # packing limit; zip headers bring a part to just under 9 MB


def note(ID, k):
    return (f"**The scans come in {k} zips** (`{ID}_scans_part1.zip` to `{ID}_scans_part{k}.zip`, each under 10 MB): "
            f"unpack all of them into the same working folder; together they are `{ID}_scans.zip`, and `MANIFEST.tsv` "
            f"(in part 1) lists every file of all parts. Wherever this task says `{ID}_scans.zip`, it means these {k} "
            f"zips together. An attached file may carry a suffix such as `(2)` in its name (for example "
            f"`PREAMBLE(2).tex`): it is the file of the same name without the suffix. This task file is also attached "
            f"as `{ID}_PROMPT.zip`, which holds the same `PROMPT.md`, in case the .md file fails to load.\n\n")


def write_prompt(src, dst, ID, k):
    t = (src / "PROMPT.md").read_text(encoding="utf-8")
    i = t.index("## Absolute rules")
    out = t[:i] + note(ID, k) + t[i:]
    (dst / "PROMPT.md").write_bytes(out.encode("utf-8"))
    with zipfile.ZipFile(dst / f"{ID}_PROMPT.zip", "w", zipfile.ZIP_DEFLATED) as z:
        z.writestr("PROMPT.md", out.encode("utf-8"))
    with zipfile.ZipFile(dst / f"{ID}_PROMPT.zip") as z:
        assert z.testzip() is None and z.read("PROMPT.md") == (dst / "PROMPT.md").read_bytes()


for ID in args[1:]:
    src = src_dir / ID
    dst = dst_root / ID
    if prompt_only:
        k = len(list(dst.glob(f"{ID}_scans_part*.zip")))
        assert k and all((dst / f"{ID}_scans_part{j}.zip").exists() for j in range(1, k + 1)), ID
        write_prompt(src, dst, ID, k)
        print(ID, "prompt rewritten,", k, "parts")
        continue
    if dst.exists():
        print("exists", ID)
        continue
    dst.mkdir(parents=True)
    z = zipfile.ZipFile(src / f"{ID}_scans.zip")
    names = z.namelist()
    man = [n for n in names if n.endswith("MANIFEST.tsv")]
    extra = [n for n in names if n not in man and "_scan" not in n.split("/")[-1]]
    groups = OrderedDict()
    for n in names:
        if n in man or n in extra:
            continue
        groups.setdefault(n.split("_scan")[1][:3], []).append(n)
    parts, cur = [], list(extra)
    size = sum(z.getinfo(n).file_size for n in extra + man)
    for k, ns in groups.items():
        s = sum(z.getinfo(n).file_size for n in ns)
        if cur and size + s > LIM:
            parts.append(cur)
            cur, size = [], 0
        cur += ns
        size += s
    if cur:
        parts.append(cur)
    for i, ns in enumerate(parts, 1):
        p = dst / f"{ID}_scans_part{i}.zip"
        with zipfile.ZipFile(p, "w", zipfile.ZIP_STORED) as out:
            if i == 1:
                for m in man:
                    out.writestr(m, z.read(m))
            for n in ns:
                out.writestr(n, z.read(n))
        with zipfile.ZipFile(p) as zz:
            assert zz.testzip() is None
        assert p.stat().st_size < 9_000_000, (ID, i, p.stat().st_size)
    got = sum(len(zipfile.ZipFile(dst / f"{ID}_scans_part{i}.zip").namelist()) for i in range(1, len(parts) + 1))
    assert got == len(names), (ID, got, len(names))
    shutil.copy2(src / "PREAMBLE.tex", dst / "PREAMBLE.tex")
    write_prompt(src, dst, ID, len(parts))
    print(ID, len(parts), "parts", [round((dst / f"{ID}_scans_part{j}.zip").stat().st_size / 1e6, 1)
                                    for j in range(1, len(parts) + 1)])
