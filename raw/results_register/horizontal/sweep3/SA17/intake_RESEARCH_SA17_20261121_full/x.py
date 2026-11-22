"""For a section file: print each pending id's statement and the first N lines of its proof (reading aid).
usage: python -I -B x.py <section file name> <N> [width]"""
import pathlib
import sys

B = chr(92)
ENDS = tuple(B + "end{" + w + "}" for w in ("theorem", "proposition", "lemma", "corollary", "remark", "definition"))
root = pathlib.Path("../../../../../grothendieck_archive_transcription_20261110/research_returns/"
                    "RESEARCH_SA17_checkpoint_12_20261119T2037Z_unzipped/RESEARCH_SA17")
f, N = sys.argv[1], int(sys.argv[2])
W = int(sys.argv[3]) if len(sys.argv) > 3 else 260
done = {l.split("\t")[0] for l in open("../INTAKE_RESEARCH_SA17_20261121_full_CHECK_EVENTS.tsv",
                                       encoding="utf-8").read().splitlines()[1:]}
ids = [l.split("\t")[2] for l in open("plan.tsv", encoding="utf-8").read().splitlines() if l.split("\t")[0] == f]
L = (root / f).read_text(encoding="utf-8").splitlines()
for i in ids:
    if i in done:
        continue
    tag = B + "label{" + i + "}"
    k = next(n for n, s in enumerate(L) if tag in s)
    print("=====", i, "line", k + 1)
    j = k
    while j < len(L) and not L[j].strip().startswith(ENDS):
        print(L[j][:W])
        j += 1
    p = j
    while p < len(L) and (B + "begin{proof") not in L[p] and (B + "label{") not in L[p]:
        p += 1
    if p < len(L) and (B + "begin{proof") in L[p]:
        e = p
        while e < len(L) and (B + "end{proof}") not in L[e]:
            e += 1
        print("--- proof", e - p, "lines")
        for s in L[p + 1:min(e, p + 1 + N)]:
            print(s[:W])
