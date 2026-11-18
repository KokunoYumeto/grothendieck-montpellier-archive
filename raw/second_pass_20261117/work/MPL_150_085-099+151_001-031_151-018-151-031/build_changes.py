"""Build the changes file: the hand-written table (changes_table_draft.md, in this
work folder) followed by an exact list of the doubt marks left in the corrected
files. Writes second_pass/out/MPL_150_085-099+151_001-031/..._changes.md once."""
import os
import re

BASE = "C:/Users/user/Documents/grothendieck_archive_transcription_20261110/"
WORK = os.path.dirname(os.path.abspath(__file__))
OUT = BASE + "second_pass/out/MPL_150_085-099+151_001-031/"
P = "MPL_150_085-099+151_001-031_151_scan"
SCANS = [18, 19, 20, 21, 22, 23, 24, 25, 27, 28, 29, 30, 31]
TAG = "\\unsure{"


def marks(line):
    """Yield the balanced contents of every \\unsure{...} in a line."""
    i = 0
    while True:
        j = line.find(TAG, i)
        if j < 0:
            return
        k = j + len(TAG)
        depth = 1
        while k < len(line) and depth:
            if line[k] == "{" and line[k - 1] != "\\":
                depth += 1
            elif line[k] == "}" and line[k - 1] != "\\":
                depth -= 1
            k += 1
        yield line[j + len(TAG):k - 1]
        i = j + len(TAG)


def main():
    rows = []
    tot = {"zx": 0, "sg": 0, "other": 0}
    per = []
    for s in SCANS:
        zx = sg = 0
        others = []
        with open(OUT + P + "%03d.tex" % s, encoding="utf-8") as f:
            for n, line in enumerate(f, 1):
                for m in marks(line):
                    if m.startswith("\\zeta") or m.startswith("\\xi"):
                        zx += 1
                    elif m.startswith("\\mathfrak S"):
                        sg += 1
                    else:
                        others.append("l.%d `%s`" % (n, m.replace("`", "'")))
        tot["zx"] += zx
        tot["sg"] += sg
        tot["other"] += len(others)
        per.append((s, zx, sg, others))
    lines = []
    lines.append("## Places still unresolved\n")
    lines.append("Every doubt mark left in the corrected files: %d in all (the first pass had 228 on these scans). "
                 "%d are the argument letter `\\unsure{\\zeta|\\xi}` (scans 021-025) and %d the group letter "
                 "`\\unsure{\\mathfrak S_n|\\mathcal G_n}` (scans 020, 022, 023, 025), both kept with their two "
                 "readings; %d are other places, listed below with the line of the corrected file (scan 023: three "
                 "comment lines follow line 4, so its later lines are three higher than in the first pass).\n"
                 % (tot["zx"] + tot["sg"] + tot["other"], tot["zx"], tot["sg"], tot["other"]))
    lines.append("Count before and after consulting Michel Hua's transcription: 192 after my own reading of the ink, "
                 "192 after Hua. His text settled 5 places (the four overwritten letters u, v on scan 018 and the "
                 "blotted p of \"induite par p\" on scan 023, which I would otherwise have marked) and opened 5 "
                 "(scan 028 simple|souple, 029 espace-topos|espace ou topos, 030 types|topos and pi|Pi_i, 031 "
                 "d'un choix|des choix), where his reading differs and the ink does not decide; in 6 further marks "
                 "his reading was added as an alternative (019 X(I|J), X(I'|J') and the struck vertex, 020 "
                 "q_3|p_{13} and pointations, 031 vaudrait).\n")
    lines.append("| Scan | Argument letter zeta/xi | Group letter | Other doubt marks (line: reading) |")
    lines.append("|---|---:|---:|---|")
    for s, zx, sg, others in per:
        lines.append("| %03d | %d | %d | %s |" % (s, zx, sg, "; ".join(others).replace("|", "\\|") or "none"))
    lines.append("")
    with open(os.path.join(WORK, "changes_table_draft.md"), encoding="utf-8") as f:
        head = f.read()
    name = OUT + "MPL_150_085-099+151_001-031_151-018-151-031_changes.md"
    with open(name, "w", encoding="utf-8", newline="\n") as f:
        f.write(head.rstrip("\n") + "\n\n" + "\n".join(lines))
    print(name, tot)


if __name__ == "__main__":
    main()
