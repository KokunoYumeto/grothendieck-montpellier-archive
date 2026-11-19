# Import the second-pass verdicts on MPL_16+47+54+44 (R/S/F/D items) as check events, one per entry.
import csv, re, sys
sys.stdout.reconfigure(encoding="utf-8", errors="replace")
from pathlib import Path
H = Path(r"C:/Users/user/Documents/results_register/horizontal")
WHO = "Claude Opus 5.5 at effort max, second pass (in the input second_pass folder)"
HOW = "note checked against the corrected transcription and the scans (second pass)"


def events(topic="SA18"):
    idx = list(csv.DictReader(open(H / "inputs" / topic / "NOTES_INDEX.tsv", encoding="utf-8"), delimiter="\t"))
    lab = {}
    for r in idx:
        if r["entry_id"].startswith("MPL_16+47+54+44#"):
            m = re.match(r"([RSFD]\d+)[ .]", r["heading"])
            if m and m.group(1) not in lab:
                lab[m.group(1)] = r["entry_id"]
    out, seen = [], set()
    d = H / "inputs" / topic / "second_pass" / "MPL_16+47+54+44"
    for f in sorted(d.glob("*_notes_checked.md")):
        for i, line in enumerate(f.read_text(encoding="utf-8").splitlines(), 1):
            m = re.match(r"\|\s*([RSFD]\d+)\b[^|]*\|\s*([^|]*)\|\s*(keep|correct|drop)[^|]*\|\s*([^|]*)\|", line)
            if not m:
                m2 = re.match(r"- \*\*([RSFD]\d+)\*\*\s*(\([^)]*\))?:\s*(keep|correct|drop)[.,;]?\s*(.*)", line)
                if not m2:
                    continue
                L, verdict, reason = m2.group(1), m2.group(3), m2.group(4)
            else:
                L, verdict, reason = m.group(1), m.group(3), m.group(4)
            if L not in lab or (L, f.name) in seen:
                continue
            seen.add((L, f.name))
            res = {"keep": "agrees: keep", "correct": "corrected", "drop": "dropped"}[verdict]
            reason = " ".join(reason.split()[:30])
            out.append([lab[L], "2026-11-17", WHO, HOW, f"{res} ({L}). {reason}".strip(),
                        f"{topic}/second_pass/MPL_16+47+54+44/{f.name}:{i}"])
    return out


if __name__ == "__main__":
    ev = events()
    print(len(ev), len({e[0] for e in ev}))
    for e in ev[:3]:
        print(e)
