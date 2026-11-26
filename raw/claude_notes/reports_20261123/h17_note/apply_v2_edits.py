# Remaining v2 edits of h17_note.tex (second reader ae4ae3dc; workbench address). Usage: python -I -B apply_v2_edits.py
import io
p = "h17_note.tex"
s = io.open(p, encoding="utf-8").read()
R = [
 (r"\newcommand{\workbenchurl}{https://github.com/KokunoYumeto/grothendieck-longue-marche}",
  r"\newcommand{\recordurl}{https://github.com/KokunoYumeto/mathematics-workbenches}"),
 ("The outputs of the runs and the check records are to be public at\n\n"
  r"{\raggedright\smallskip\noindent\url{\workbenchurl}.\par}",
  "The outputs of the runs and the check records are public at the permanent page of this note, given at deposit,\nin\n\n"
  r"{\raggedright\smallskip\noindent\url{\recordurl}.\par}"),
 ("several proofs, and in part by Claude Opus 5.5 at effort max. No human has checked it.",
  "several proofs, and by Claude Opus 5.5 at effort max as second reader. No human has checked it."),
 ("identity of Step 5 (22 November). No fault was found in the statements.",
  "identity of Step 5 (22 November). As second reader of this text (23 November) it followed every step of Sections\n"
  "4 and 8 and of the proofs rewritten by the editor, re-derived the matrix and braid identities, opened\n"
  r"\cite{HMM} at the source, and found no mathematical error; its corrections of citation and precision are" "\n"
  "incorporated. No fault was found in the statements."),
 ("these places, which nobody else has checked:", "these places, which the second reader checked:"),
 ("Of\n" r"\cite{HMM}, \cite{BBR}, \cite{DG} and \cite{Co} only the abstracts were read; \cite{BBR} also in its first section. The" "\n"
  "other references are cited from memory or with the locators of the runs.",
  r"\cite{HMM} was" "\n" r"opened by the second reader (Corollary C and Corollary 2.8). Of \cite{BBR}, \cite{DG} and \cite{Co} only the" "\n"
  r"abstracts were read; \cite{BBR} also in its first section. The bibliographic data of \cite{As} and \cite{FR} were" "\n"
  r"confirmed; \cite{A} was not opened, and what is taken from it is proved in (F). The other references are cited" "\n"
  "from memory or with the locators of the runs."),
 (r"\emph{Mat. Sb.} 8" "\n" "(1940), 265--276.", r"\emph{Mat. Sb.} 8(50)" "\n" "(1940), 265--276."),
 (r"subgroups of configuration space groups, \emph{Kodai Math. J.} 45 (2022), 295--348.",
  r"subgroups of configuration space groups, \emph{Kodai Math. J.} 45 (2022), 295--348. Corollary C of the" "\n"
  "introduction is Corollary 2.8 of the body."),
 (r"algebraic curves, \emph{J. Pure Appl. Algebra} 159 (2001), 123--147.",
  r"algebraic curves, \emph{J. Pure Appl. Algebra} 159 (2001), no.~2, 123--147."),
]
for a, b in R:
    n = s.count(a)
    if n != 1:
        raise SystemExit("count %d for: %r" % (n, a[:70]))
    s = s.replace(a, b)
io.open(p, "w", encoding="utf-8", newline="\n").write(s)
print("applied", len(R))
