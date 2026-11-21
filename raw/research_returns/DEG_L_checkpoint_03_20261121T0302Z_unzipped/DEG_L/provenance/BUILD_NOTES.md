# Build notes

code/build_paper.py assembles the requested LaTeX from complete proof fragments and root reports. code/sync_records.py merges actual event records and updates questions. The first complete local pdfTeX output had59pages; compilation succeeded on2026-11-21 before checkpoint02. Run twice after rebuilding. Optional PDF not yet visually checked.

Normal filename lookup is broken. The working format is work/pdflatex.fmt. Successful command:

```
env TEXINPUTS=.:/usr/share/texlive/texmf-dist/tex//:/usr/share/texmf/tex// TFMFONTS=/usr/share/texlive/texmf-dist/fonts/tfm//:/usr/share/texmf/fonts/tfm// VFFONTS=/usr/share/texlive/texmf-dist/fonts/vf//:/usr/share/texmf/fonts/vf// TEXFONTMAPS=/usr/share/texlive/texmf-dist/fonts/map//:/usr/share/texmf/fonts/map// T1FONTS=/usr/share/texlive/texmf-dist/fonts/type1//:/usr/share/texmf/fonts/type1// ENCFONTS=/usr/share/texlive/texmf-dist/fonts/enc//:/usr/share/texmf/fonts/enc// pdflatex -fmt=/workspace/scratch/fd8d5745a052/work/pdflatex.fmt -interaction=nonstopmode -halt-on-error -output-directory=work /workspace/scratch/fd8d5745a052/DEG_L/DEG_L.tex
```

Preamble loads lm, cm, symbols, euler and rsfs maps. A fresh environment can use its normal LaTeX format. Tectonic bundle download failedHTTP403, but local pdfTeX works. Compilation is not a mathematical proof check; whole-proof readings are separately recorded.

Checkpoint03 build at03:01UTC: assembled paper compiled successfully to93pages,918210bytes before the final source-locator refresh. S21 is included; T6.16 remains a separate candidate file. All required TSVs parse through code/sync_records.py, including normalized imported local-newvector events.
