# Build notes

code/build_paper.py assembles the requested LaTeX from complete proof fragments and root reports. code/sync_records.py merges actual event records and updates questions. The first complete local pdfTeX output had59pages; compilation succeeded on2026-11-21 before checkpoint02. Run twice after rebuilding. Optional PDF not yet visually checked.

Normal filename lookup is broken. The working format is work/pdflatex.fmt. Successful command:

```
env TEXINPUTS=.:/usr/share/texlive/texmf-dist/tex//:/usr/share/texmf/tex// TFMFONTS=/usr/share/texlive/texmf-dist/fonts/tfm//:/usr/share/texmf/fonts/tfm// VFFONTS=/usr/share/texlive/texmf-dist/fonts/vf//:/usr/share/texmf/fonts/vf// TEXFONTMAPS=/usr/share/texlive/texmf-dist/fonts/map//:/usr/share/texmf/fonts/map// T1FONTS=/usr/share/texlive/texmf-dist/fonts/type1//:/usr/share/texmf/fonts/type1// ENCFONTS=/usr/share/texlive/texmf-dist/fonts/enc//:/usr/share/texmf/fonts/enc// pdflatex -fmt=/workspace/scratch/fd8d5745a052/work/pdflatex.fmt -interaction=nonstopmode -halt-on-error -output-directory=work /workspace/scratch/fd8d5745a052/DEG_L/DEG_L.tex
```

Preamble loads lm, cm, symbols, euler and rsfs maps. A fresh environment can use its normal LaTeX format. Tectonic bundle download failedHTTP403, but local pdfTeX works. Compilation is not a mathematical proof check; whole-proof readings are separately recorded.

Checkpoint03 build at03:01UTC: assembled paper compiled successfully to93pages,918210bytes before the final source-locator refresh. S21 is included; T6.16 remains a separate candidate file. All required TSVs parse through code/sync_records.py, including normalized imported local-newvector events.

Checkpoint04 pre-review build at03:42UTC compiled successfully to131pages and1110733bytes. T6.1–T6.18, B22a, B23, B24 and S25 are included. All91question rows and300actual mathematical check events parse. Generic heading labels are being namespaced; a remaining2.41pt overfull inline-code box is cosmetic. This is artifact validation, not mathematical proof verification.

At03:46UTC the updated manuscript compiled successfully to131pages,1113602bytes, with no undefined/multiply-defined labels or overfull boxes. The sole remaining amsmath advisory concerns legacy TeX fraction syntax. S26/S27 were author-and-root whole-proof checked, and the S27 injection now has a direct long-exact-sequence proof.

## 2026-11-21 04:31:23 UTC — expanded checkpoint05 proof validation

The current integrated LaTeX compiled successfully to a 165-page scratch QA PDF (1,306,357 bytes). The initial pass failed at an S33 proof paragraph heading inside the amsthm environment; the owner replaced the four headings with ordinary bold paragraphs, without mathematical edits, and the next compile succeeded. No overfull boxes or duplicate labels were reported; cross-reference rerun and the retained legacy amsmath over-command warning remained on this pass. A final pass will follow T22 promotion.
