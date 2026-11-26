"""The two small object prompts of the conference (proposals 15 and 16), from the archive builder's output.

Conference convener ae84c4aa (Claude Fable 5.2 at effort max), 25 Nov 2026, for the main session 329fb1e6.

The builder (grothendieck_archive_transcription_20261110/working_through_20261118/build_object_prompts.py) wrote
objects/OBJ_H0A2-1 and objects/OBJ_H037. This script copies each to a staging folder, adds the folder of what our
runs proved toward the main question, puts the main question into PROMPT.md, adds the two paragraphs the finished
object prompts carry (LaTeX sources; no copies of sources), packs everything into one flat ZIP with
claude_tools/prompts/pack_one_zip.py, adds our LaTeX editions with claude_tools/latex_sources.py, and lints.
The builder's own folders are not changed.

usage: python -I -B build_small_prompts.py refs      cross-references of the section files that point outside them
       python -I -B build_small_prompts.py stage     build both staging folders, pack, lint, verify
"""
import io
import pathlib
import re
import shutil
import subprocess
import sys
import zipfile

sys.stdout.reconfigure(encoding="utf-8")
DOCS = pathlib.Path("<local>/Documents")
HERE = pathlib.Path(__file__).resolve().parent
WT = DOCS / "grothendieck_archive_transcription_20261110/working_through_20261118"
RR = DOCS / "grothendieck_archive_transcription_20261110/research_returns"
TOOLS = DOCS / "claude_tools"
STAGE = pathlib.Path("<local>/AppData/Local/Temp/claude/f2c80a22394db22f/"
                     "329fb1e6-0570-47be-9060-a2a454bf3e15/scratchpad/small_prompts/stage")
SA14 = RR / "RESEARCH_SA14_SA19_checkpoint_08_20261120T2005Z_unzipped"
SA15 = RR / "RESEARCH_SA15_checkpoint_37_20261120T0635Z_unzipped"
PAG2 = RR / "POLISH_ALGEBRAIC_GEOMETRY_checkpoint_35_20261124T0416Z_unzipped/workbench/papers/paper_02"
PC4 = (RR / "POLISH_CRISTAUX_checkpoint_34_20261124T2141Z_unzipped/POLISH_CRISTAUX_checkpoint_34/workbench/papers"
       / "paper4")
P90A = DOCS / "reports_20261124/INTAKE_PILE_20261124/v2/2611.00936_v3"
BS = chr(92)


def filtered(path, keep, header=True):
    """the header line and the lines of a table for which keep(line) holds, as bytes"""
    lines = path.read_text(encoding="utf-8", errors="replace").splitlines(keepends=True)
    out = lines[:1] if header else []
    out += [x for x in lines[1 if header else 0:] if keep(x)]
    return "".join(out).encode("utf-8"), len(out) - (1 if header else 0)


def question_files(key):
    """(arcname, bytes) of the question folder"""
    f = []
    if key == "OBJ_H0A2-1":
        for n in ("RESEARCH_SA14_SA19_paper.tex", "RESEARCH_SA14_SA19_references.bib", "RESEARCH_SA14_SA19_results.csv",
                  "CHECK_EVENTS.tsv"):
            f.append(("SA14/" + n, (SA14 / n).read_bytes()))
        for n in ("A.tex", "K.tex"):
            f.append(("SA14/sections/" + n, (SA14 / "sections" / n).read_bytes()))
        part_a = re.compile(r"^(A\d|A_|attempt_A\d|audit_A\d|Raynaud_exclusion|additional_leads|notes\.md$|audits_08)")
        for agent in ("bce", "dgj", "fhi", "root"):
            for p in sorted((SA14 / "work" / agent).iterdir()):
                if p.is_file() and part_a.match(p.name) and p.suffix.lower() in (".tex", ".md"):
                    f.append(("SA14/work/%s/%s" % (agent, p.name), p.read_bytes()))
        for p in sorted(PAG2.iterdir()):
            if p.suffix.lower() in (".tex", ".tsv", ".md") and p.is_file():
                f.append(("POLISH_AG_paper_02/" + p.name, p.read_bytes()))
        for n in ("p90a_note_v3.tex", "METADATA_ABSTRACT.txt", "CHANGE_NOTE.txt"):
            f.append(("P90a_note_v3/" + n, (P90A / n).read_bytes()))
    else:
        for n in ("RESEARCH_SA15_paper.tex", "RESEARCH_SA15_references.bib"):
            f.append(("SA15/" + n, (SA15 / n).read_bytes()))
        for n in ("C.tex", "F.tex"):
            f.append(("SA15/sections/" + n, (SA15 / "sections" / n).read_bytes()))
        import csv
        with open(SA15 / "RESEARCH_SA15_results.csv", encoding="utf-8", errors="replace", newline="") as fh:
            rows = list(csv.reader(fh))
        sel = [rows[0]] + [r for r in rows[1:] if r and ":C-" in r[0]]
        buf = io.StringIO()
        csv.writer(buf, lineterminator="\n").writerows(sel)
        b, k = buf.getvalue().encode("utf-8"), len(sel) - 1
        assert k == 18, k
        f.append(("SA15/RESEARCH_SA15_results_part_C.csv", b))
        b2, k2 = filtered(SA15 / "CHECK_EVENTS.tsv", lambda x: x.split("\t")[0].startswith("C-"))
        f.append(("SA15/CHECK_EVENTS_part_C.tsv", b2))
        print("   SA15 extracts: results rows", k, "check-event rows", k2)
        for p in sorted(PC4.iterdir()):
            if p.suffix.lower() in (".tex", ".tsv", ".md") and p.is_file():
                f.append(("POLISH_CRISTAUX_paper4/" + p.name, p.read_bytes()))
    f.append(("README.md", (HERE / (SPECS[key]["q"] + "_question_README.md")).read_bytes()))
    return f


SPECS = {
    "OBJ_H0A2-1": dict(q="Q03b", packs=["SGA2_EN", "SGA1_EN", "SGA6_FR", "FGA_FR", "EGA_FR"],
                       folder="Q03b_OBJ_H0A2-1_cote57_Picard_points"),
    "OBJ_H037": dict(q="Q11", packs=["SGA2_EN", "SGA1_EN", "SGA7_FR", "FGA_FR", "EGA_FR"],
                     folder="Q11_OBJ_H037_cote100_finite_normalization"),
}


def once(text, old, new, what):
    assert text.count(old) == 1, (what, text.count(old))
    return text.replace(old, new)


def patch_prompt(key, text):
    q = SPECS[key]["q"]
    section = (HERE / (q + "_question_section.md")).read_text(encoding="utf-8")
    bullet = (HERE / (q + "_question_bullet.md")).read_text(encoding="utf-8")
    # 1. the main question, before the attachments
    text = once(text, "\n## The attachments\n", "\n" + section + "## The attachments\n", "attachments heading")
    # 2. the question folder among the attachments, before the results
    res = "- `%s_results.zip`: the statements of our own research runs that cite these folders." % key
    text = once(text, res, bullet.rstrip("\n") + "\n" + res, "results bullet")
    # 3. the paragraphs on LaTeX sources and on copies of sources, before "How to work" (as in the finished prompts)
    sys.path.insert(0, str(TOOLS))
    import latex_sources  # noqa: E402
    packs = ", ".join("`latex_sources/%s/`" % p for p in SPECS[key]["packs"])
    latex = latex_sources.PARAGRAPH + " Here it holds " + packs + "."
    nocopy = (TOOLS / "prompts/no_source_copies.md").read_text(encoding="utf-8").strip("\n")
    text = once(text, "\n## How to work\n", "\n" + latex + "\n\n" + nocopy + "\n\n## How to work\n", "how to work")
    # 4. the main question is fixed by this prompt
    rx = re.compile(r"\*\*The main question\*\* is the object's\s+central statement: the claim or question of his "
                    r"that the other items serve, or, where none stands out, the statement\s+the most other items "
                    r"depend on\. Name it at the top of the ledger\.")
    assert len(rx.findall(text)) == 1, "main-question sentence"
    text = rx.sub("**The main question** of this run is fixed: it is the\none stated in the section \"The main question "
                  "of this run\" above, with the rows named there. Name it at the top of\nthe ledger, with its gate.",
                  text)
    return text


def patch_readme(key, text):
    first = ("Upload every file of this folder except this README in a new ChatGPT chat with GPT-6 Astra in Pro mode, "
             "`PROMPT.md` as a file, no text typed.")
    text = once(text, first, "The send folder holds `PROMPT.md` and one ZIP, `%s_O.zip`; this README is inside the ZIP. "
                "Upload both in a new ChatGPT chat with GPT-6 Astra in Pro mode, `PROMPT.md` as a file, no text typed."
                % key, "readme first line")
    a, b = text.index("## Files\n"), text.index("## Context")
    files = ("## Files\n\nInside `%s_O.zip`, each as a folder: `%s_context/`, `%s_entries/`, `%s_pages/`, `%s_question/`, "
             "`%s_results/`, `%s_scans/`, and `latex_sources/` (our LaTeX editions: %s).\n\n"
             % (key, key, key, key, key, key, key, ", ".join(SPECS[key]["packs"])))
    text = text[:a] + files + text[b:]
    a, b = text.index("## Results (opened last by the run)"), text.index("## Provenance")
    results = ("## Results\n\n- `%s_results/`: 0 statements; the register it is built from dates from 18 Nov 2026, before "
               "our runs on these pages returned.\n- `%s_question/`: what our runs proved toward the main question of "
               "this prompt (its README says which run, model and date); open from the start.\n\n" % (key, key))
    text = text[:a] + results + text[b:]
    m = re.search(r" Lint \(--lint-math\): [A-Z]+\.", text)
    assert m, "readme lint line"
    text = text.replace(m.group(0), "")
    text = text.rstrip("\n") + ("\n- **Amended** 2026-11-25 by the conference convener (Claude Fable 5.2 at effort max), "
                                "for the conference's proposal %s: the main question of the run and the folder "
                                "`%s_question/` added; the paragraphs on LaTeX sources and on copies of sources added; "
                                "packed into one ZIP by `claude_tools/prompts/pack_one_zip.py`; our LaTeX editions added "
                                "by `claude_tools/latex_sources.py`.\n" % ("15" if key == "OBJ_H0A2-1" else "16", key))
    return text


def refs():
    for root, main in ((SA14, "A.tex"), (SA15, "C.tex")):
        secs = {p.name: p.read_text(encoding="utf-8", errors="replace") for p in (root / "sections").glob("*.tex")}
        t = secs[main]
        labs = set(re.findall(re.escape(BS + "label{") + r"([^}]*)\}", t))
        used = set(re.findall(re.escape(BS) + r"(?:eq|auto|c|C)?ref\{([^}]*)\}", t))
        miss = sorted(used - labs)
        print(root.name[:32], main, "labels", len(labs), "refs", len(used), "outside", len(miss))
        for m in miss:
            where = [n for n, s in secs.items() if (BS + "label{" + m + "}") in s]
            print("    ", m, "->", where)
        cites = set()
        for c in re.findall(re.escape(BS) + r"cite(?:\[[^\]]*\])*\{([^}]*)\}", t):
            cites |= {x.strip() for x in c.split(",")}
        print("     cite keys:", len(cites))


def stage():
    if STAGE.exists():
        shutil.rmtree(STAGE)
    for key, spec in SPECS.items():
        src, dst = WT / "objects" / key, STAGE / (key + "_O")
        dst.mkdir(parents=True)
        for p in src.iterdir():
            if p.is_file():
                shutil.copy2(p, dst / p.name)
        print("==", key)
        qf = question_files(key)
        with zipfile.ZipFile(dst / (key + "_question.zip"), "w", zipfile.ZIP_DEFLATED) as z:
            for arc, data in qf:
                z.writestr(zipfile.ZipInfo(arc, date_time=(2026, 11, 25, 0, 0, 0)), data, zipfile.ZIP_DEFLATED)
        print("   question folder:", len(qf), "files,", sum(len(d) for _, d in qf), "bytes")
        pm = dst / "PROMPT.md"
        pm.write_text(patch_prompt(key, pm.read_text(encoding="utf-8")), encoding="utf-8", newline="\n")
        rm = dst / "README.md"
        rm.write_text(patch_readme(key, rm.read_text(encoding="utf-8")), encoding="utf-8", newline="\n")
        r = subprocess.run([sys.executable, "-I", "-B", str(TOOLS / "prompts/pack_one_zip.py"), str(dst)],
                           capture_output=True, text=True, encoding="utf-8")
        print("   pack:", (r.stdout + r.stderr).strip())
        assert r.returncode == 0
        one = dst / (key + "_O.zip")
        r = subprocess.run([sys.executable, "-I", "-B", str(TOOLS / "latex_sources.py"), "add", str(one)] + spec["packs"],
                           capture_output=True, text=True, encoding="utf-8")
        print("   latex:", (r.stdout + r.stderr).strip())
        assert r.returncode == 0
        verify(key, dst)


def verify(key, dst):
    names = sorted(p.name for p in dst.iterdir())
    assert names == sorted(["PROMPT.md", key + "_O.zip"]), names
    text = (dst / "PROMPT.md").read_text(encoding="utf-8")
    with zipfile.ZipFile(dst / (key + "_O.zip")) as z:
        assert z.testzip() is None
        members = [i.filename for i in z.infolist() if not i.is_dir()]
        assert not [n for n in members if n.lower().endswith(".zip")], "a ZIP inside the ZIP"
        tops = {}
        for i in z.infolist():
            if not i.is_dir():
                t = i.filename.split("/")[0]
                tops[t] = tops.get(t, 0) + 1
        # every folder and file the prompt names must be there
        named = set(re.findall(r"`(%s_[a-z]+)\.zip`" % re.escape(key), text))
        for n in sorted(named):
            assert n in tops, ("folder named in the prompt but not in the ZIP", n)
        for n in re.findall(r"`(%s_question/|latex_sources/[A-Z0-9_]+/)`" % re.escape(key), text):
            assert any(m.startswith(n) for m in members), ("named but absent", n)
        q = key + "_question/"
        for n in re.findall(r"`((?:SA14|SA15|P90a_note_v3|POLISH_AG_paper_02|POLISH_CRISTAUX_paper4)/)`", text):
            assert any(m.startswith(q + n) for m in members), ("question subfolder absent", n)
        for n in re.findall(r"`(sections/[A-Z]\.tex|[A-Za-z0-9_]+\.(?:csv|tsv|tex))`", text):
            if n in ("PROOFS.tex",) or n.split(".")[0] in ("STATEMENTS", "NOTES_VERDICTS", "READINGS", "LINKS",
                                                             "CONSEQUENCES", "CHECK_EVENTS", "ENTRIES", "OBJECT",
                                                             "CHECKS", "page_map", "OBJECTS_NEARBY", "CORRECTIONS",
                                                             "DEPENDS", "PREAMBLE"):
                continue
            assert any(m.endswith("/" + n) for m in members), ("file named in the prompt but not in the ZIP", n)
        print("   ZIP:", (dst / (key + "_O.zip")).stat().st_size, "bytes,", len(members), "files; top level:",
              ", ".join("%s (%d)" % kv for kv in sorted(tops.items())))
    for mode in ("--lint", "--lint-math"):
        r = subprocess.run([sys.executable, "-I", "-B", str(TOOLS / "push_rule_pro_prompts.py"), mode,
                            str(dst / "PROMPT.md")], capture_output=True, text=True, encoding="utf-8")
        print("   %s: %s" % (mode, " | ".join((r.stdout + r.stderr).strip().splitlines())))
    print("   PROMPT.md:", len(text), "characters,", len(text.split()), "words")


if __name__ == "__main__":
    if sys.argv[1:] == ["refs"]:
        refs()
    elif sys.argv[1:] == ["stage"]:
        stage()
    else:
        sys.exit(__doc__)
