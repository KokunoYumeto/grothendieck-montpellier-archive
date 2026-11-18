"""Background for the Les Dérivateurs Pro packages (18 Nov 2026). The user, ~20:0x UTC: "Do the transcription prompts
have all the new notes and stuff as well as background?" They had the transcription rules and the second-pass cautions
of 17 Nov, but no background. Written by the main session, Claude Opus 5.5 at effort max.

For every package in pro_derivateurs_20261118/PACKAGES.tsv this writes <pkg>_background.zip:
- RESULTS_STATE.md: our results that bear on Les Dérivateurs (subjects derivators and homotopy), with the broad layer
  every archive package gets (programme map, headline results, orientation), built by
  ../tools_20261113/build_results_state.py (its build()). Hua's readings are left out: these are blind first readings.
- same_file_157/<id>/: for every cote-157 folder already returned (round D, ChatGPT Work), its notation table and
  doubts, its notes and its mathematical notes, so that the notation stays one across the whole file.
- README.md: what is in the zip.
and adds one paragraph about it to the package's PROMPT.md (once), then lints every PROMPT.md.

usage: python -I -B tools/add_dp_background.py
"""
import csv
import pathlib
import re
import subprocess
import sys
import zipfile

sys.stdout.reconfigure(encoding="utf-8")
CW = pathlib.Path(__file__).resolve().parent.parent
TR = CW.parent
OUT = CW / "pro_derivateurs_20261118"
RET = CW / "returns"
LINT = pathlib.Path.home() / "Documents/claude_tools/push_rule_pro_prompts.py"
sys.path.insert(0, str(TR / "tools_20261113"))
import build_results_state as B  # noqa: E402

B.KEY_SUBJECTS["dp157"] = ["derivators", "homotopy"]
B.hua_section = lambda pkg: ""  # blind first reading: no other transcription of these pages

MARK = "**Background (attached `"


def paragraph(pkg, n_folders):
    return (
        f"{MARK}{pkg}_background.zip`).** It holds two things. `RESULTS_STATE.md` gives our results so far that bear on "
        "Les Dérivateurs, with a map of the whole programme: every run, its main results and its open questions. Read it "
        "after a task's transcription is frozen and before you write that task's mathematical notes, and use it as its "
        "first section says. `same_file_157/` holds, for each of the "
        f"{n_folders} folders of cote 157 already transcribed (by GPT-6.2 Astra at reasoning effort max in ChatGPT Work), "
        "its notation table and doubts (`<id>_doubts.md`), its notes and its mathematical notes. Before your first page, "
        "read the notation tables of the folders just before yours and of the other parts of cote 157. Keep their "
        "notation where the ink on your pages agrees, and record every disagreement in your own notation table. Cite "
        "those folders' notes by their id where your pages continue, repeat or correct them. None of this is a source "
        "of readings: every reading comes from the ink of your pages, as the task files say.\n\n"
    )


def main():
    rows = list(csv.DictReader(open(OUT / "PACKAGES.tsv", encoding="utf-8"), delimiter="\t"))
    same = []
    for d in sorted(RET.glob("K157-*")):
        o = d / "out"
        files = [o / f"{d.name}_{k}.md" for k in ("doubts", "notes", "mathnotes")]
        files = [f for f in files if f.is_file()]
        if files:
            same.append((d.name, files))
    print("returned cote-157 folders with notes:", len(same))
    data = B.load_data()
    bad = []
    for r in rows:
        pkg, cote = r["package"], r["cote"]
        d = OUT / pkg
        ids = r["tasks"].split()
        nums = [int(i.rsplit("-", 1)[1]) for i in ids]
        plan = dict(num=pkg, name=pkg, folder=pkg, group="Les Dérivateurs, cote 157, round D remainder (Pro)",
                    context="dp157", questions="dp157", segments=[[cote, min(nums), max(nums)]])
        text, counts = B.build(plan, data)
        readme = (f"# {pkg}: background\n\nBuilt 18 Nov 2026 by `codex_web_20261113/tools/add_dp_background.py` "
                  "(the main session, Claude Opus 5.5 at effort max).\n\n"
                  "- `RESULTS_STATE.md`: our results that bear on Les Dérivateurs, with the programme map "
                  f"({len(text.encode('utf-8')):,} bytes).\n"
                  f"- `same_file_157/<id>/`: notation table and doubts, notes and mathematical notes of the {len(same)} "
                  "cote-157 folders already returned: " + ", ".join(i for i, _ in same) + ".\n")
        z = d / f"{pkg}_background.zip"
        tmp = z.with_suffix(".tmp")
        with zipfile.ZipFile(tmp, "w", zipfile.ZIP_DEFLATED) as zf:
            zf.writestr("README.md", readme)
            zf.writestr("RESULTS_STATE.md", text)
            for i, files in same:
                for f in files:
                    zf.write(f, f"same_file_157/{i}/{f.name}")
        with zipfile.ZipFile(tmp) as zf:
            assert zf.testzip() is None
        tmp.replace(z)
        p = d / "PROMPT.md"
        t = p.read_text(encoding="utf-8")
        if MARK not in t:
            anchor = "**Checkpoints that survive a disconnection.**"
            assert t.count(anchor) == 1, pkg
            t = t.replace(anchor, paragraph(pkg, len(same)) + anchor)
            p.write_text(t, encoding="utf-8")
        lint = subprocess.run([sys.executable, "-I", "-B", str(LINT), "--lint", str(p)], capture_output=True, text=True)
        ok = lint.returncode == 0
        if not ok:
            bad.append(pkg)
            print("LINT FAILED", pkg, lint.stdout[-600:])
        nfiles = len([x for x in d.iterdir() if x.is_file()])
        print(pkg, "background", f"{z.stat().st_size / 1e6:.2f} MB", "files", nfiles, "lint ok" if ok else "LINT FAILED",
              counts)
    print("done; lint failed:", bad)


if __name__ == "__main__":
    main()
