"""Place the two staged small prompts in TO_SEND/PRO/1_Archive_research_by_topic and add their lines to ORDER.md.

Conference convener ae84c4aa (Claude Fable 5.2 at effort max), 25 Nov 2026. Run build_small_prompts.py stage first.
Refuses an existing target folder. ORDER.md is backed up to TO_SEND/PRO/_backups_20261125/ before it is edited.
Nothing is sent.

usage: python -I -B place_small_prompts.py
"""
import hashlib
import pathlib
import shutil
import subprocess
import sys

sys.stdout.reconfigure(encoding="utf-8")
DOCS = pathlib.Path("<local>/Documents")
STAGE = pathlib.Path("<local>/AppData/Local/Temp/claude/f2c80a22394db22f/"
                     "329fb1e6-0570-47be-9060-a2a454bf3e15/scratchpad/small_prompts/stage")
QUEUE = DOCS / "TO_SEND/PRO/1_Archive_research_by_topic"
BACKUPS = DOCS / "TO_SEND/PRO/_backups_20261125"
LINT = DOCS / "claude_tools/push_rule_pro_prompts.py"
PLACES = [
    ("OBJ_H0A2-1", "Q03b_OBJ_H0A2-1_cote57_Picard_points"),
    ("OBJ_H037", "Q11_OBJ_H037_cote100_finite_normalization"),
]
LINE_3B = (
    "   3b. `Q03b_OBJ_H0A2-1_cote57_Picard_points` (NEW 25 Nov 2026; conference proposal 15; an object prompt for H0A2 "
    "part 1, from the archive builder, amended by the convener): main question = his box « noyau nul si n ≥ 4 » on "
    "57:97: is Pic(X) → Pic(Y) injective for every smooth hyperplane section of a smooth projective X of dimension "
    "n ≥ 4 in characteristic p, with no cohomological condition (SA14 A1/A2, undecided in our runs; Kweon's Question "
    "7.7 is the neighbouring question in the literature). Carries SA14 Part A with its work files, the P90a note v3 "
    "and POLISH_AG paper 2, all in LaTeX. PROMPT.md + `OBJ_H0A2-1_O.zip` (%s MB); `--lint` and `--lint-math` pass; "
    "not sent.")
LINE_11 = (
    "11. `Q11_OBJ_H037_cote100_finite_normalization` (NEW 25 Nov 2026; conference proposal 16; an object prompt for "
    "H037, cote 100, from the archive builder, amended by the convener): main question = part 2) of his theorem on "
    "100:3 for a reduced base whose normalization is finite (the condition of his box on 100:7): is the functor from "
    "abelian schemes over S to triples (A_U, M, φ) an equivalence there. By our runs the normal case holds (SA15 "
    "C-RD6), and a base that is not reduced and a reduced base whose normalization is not finite fail (C-RD5, "
    "C-RD11); this case is what is left. Carries SA15 Part C and POLISH_CRISTAUX paper 4 in LaTeX. PROMPT.md + "
    "`OBJ_H037_O.zip` (%s MB); `--lint` and `--lint-math` pass; not sent.")
OLD_SENTENCE = ("The convener is building two small prompts (cotes 57 and 100); they will slot in after Q03 and at the "
                "end.")
NEW_SENTENCE = ("The convener's two small prompts (cotes 57 and 100) are built and placed, not sent: "
                "`Q03b_OBJ_H0A2-1_cote57_Picard_points` after Q03 and `Q11_OBJ_H037_cote100_finite_normalization` at "
                "the end (25 Nov 2026).")


def sha(p):
    h = hashlib.sha256()
    with open(p, "rb") as f:
        for chunk in iter(lambda: f.read(1 << 20), b""):
            h.update(chunk)
    return h.hexdigest()


def main():
    sizes = {}
    for key, name in PLACES:
        src, dst = STAGE / (key + "_O"), QUEUE / name
        assert sorted(p.name for p in src.iterdir()) == sorted(["PROMPT.md", key + "_O.zip"]), src
        assert not dst.exists(), "target exists: %s" % dst
        dst.mkdir()
        for n in ("PROMPT.md", key + "_O.zip"):
            shutil.copy2(src / n, dst / n)
            assert sha(src / n) == sha(dst / n), n
        assert sorted(p.name for p in dst.iterdir()) == sorted(["PROMPT.md", key + "_O.zip"])
        sizes[key] = (dst / (key + "_O.zip")).stat().st_size
        print(name)
        for n in ("PROMPT.md", key + "_O.zip"):
            print("   %s  %d bytes  sha256 %s" % (n, (dst / n).stat().st_size, sha(dst / n)))
        for mode in ("--lint", "--lint-math"):
            r = subprocess.run([sys.executable, "-I", "-B", str(LINT), mode, str(dst / "PROMPT.md")],
                               capture_output=True, text=True, encoding="utf-8")
            out = " | ".join((r.stdout + r.stderr).strip().splitlines())
            print("   %s: %s" % (mode, out))
            assert "failing lint: 0" in out, out
    order = QUEUE / "ORDER.md"
    bak = BACKUPS / "ORDER_research_before_small_prompts_20261125.md"
    assert not bak.exists(), bak
    shutil.copy2(order, bak)
    raw = order.read_bytes()
    crlf = b"\r\n" in raw
    text = raw.decode("utf-8").replace("\r\n", "\n")
    assert text.count(OLD_SENTENCE) == 1, "sentence on the convener's prompts"
    text = text.replace(OLD_SENTENCE, NEW_SENTENCE)
    lines = text.split("\n")
    i3 = [i for i, x in enumerate(lines) if x.startswith("3. `Q03_INTAKE_A_ANABELIAN_SECTIONS`")]
    i10 = [i for i, x in enumerate(lines) if x.startswith("10. `Q10_24_SA20_Autour_dEsquisse_dun_programme`")]
    assert len(i3) == 1 and len(i10) == 1 and i3[0] < i10[0], (i3, i10)
    mb = lambda k: "%.0f" % (sizes[k] / 1e6)
    lines.insert(i10[0] + 1, LINE_11 % mb("OBJ_H037"))
    lines[i3[0] + 1:i3[0] + 1] = ["", LINE_3B % mb("OBJ_H0A2-1"), ""]
    text = "\n".join(lines)
    order.write_bytes((text.replace("\n", "\r\n") if crlf else text).encode("utf-8"))
    print("ORDER.md updated; backup:", bak)


if __name__ == "__main__":
    main()
