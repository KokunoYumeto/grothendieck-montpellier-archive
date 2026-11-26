# Writes ABSTRACT_v2.txt (the metadata abstract, plain text with TeX mathematics) from h17_note_v2.tex.
import io

s = io.open("h17_note_v2.tex", encoding="utf-8").read()
a = s[s.index(r"\begin{abstract}") + len(r"\begin{abstract}"):s.index(r"\end{abstract}")]
a = a.replace(r"\noindent", "")
a = a.replace(r"\GT", r"\widehat{\mathrm{GT}}")
a = a.replace("\\\"u", "ü")
a = " ".join(a.split())
io.open("ABSTRACT_v2.txt", "w", encoding="utf-8", newline="\n").write(a + "\n")
print(len(a.split()), "words;", "noindent" in a, "backslash-quote left:", '\\"' in a)
