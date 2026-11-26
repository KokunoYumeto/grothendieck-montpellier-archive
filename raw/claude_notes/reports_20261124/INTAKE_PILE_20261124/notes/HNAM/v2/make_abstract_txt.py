# Writes ABSTRACT.txt (the metadata abstract) from the abstract of the version-2 TeX source.
import io, pathlib
HERE = pathlib.Path(__file__).resolve().parent
t = io.open(HERE / "nullstellensatz_am_half_plane.tex", encoding="utf-8").read()
a = t.split(r"\begin{abstract}")[1].split(r"\end{abstract}")[0].strip()
for old, new in [
    (r"$\AM\cap\cl{coAM}$", r"AM $\cap$ coAM"),
    (r"$\AM$", "AM"),
    (r"$\cl{FP}^{\Sigtwo}$", r"$\mathrm{FP}^{\Sigma_2^{\mathrm P}}$"),
    ("--", "-"),
    ("~", " "),
]:
    a = a.replace(old, new)
io.open(HERE / "ABSTRACT.txt", "w", encoding="utf-8", newline="\n").write(a + "\n")
print(len(a))
print(a)
