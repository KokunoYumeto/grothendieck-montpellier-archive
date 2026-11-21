# Isolated standalone TeX compilation check

Date: 2026-11-21. Checker: GPT-6 Astra Pro; effort not exposed.

## Environment recovery

The packages were present under `/usr/share/texlive/texmf-dist` and `/usr/share/texmf`, but Kpathsea's default `!!` paths required filename databases whose `ls-R` links were dangling. A process-local override

```
TEXMF={/usr/share/texlive/texmf-dist,/usr/share/texmf,/etc/texmf}
```

enables normal filesystem lookup. An isolated XeLaTeX format was generated from the installed `xelatex.ini`; format generation fell back to the installed English hyphenation patterns because `language.dat` was absent. No package fetch, privileged action or system-tree modification was needed. The earlier LuaLaTeX missing-format result was confirmed from the parent's retained log. The parent reported a Tectonic bundle HTTP403; that identical failed network request was not repeated.

## Reproducible workflow

The exact reusable implementation is `final/reproduce/compile_standalone_tex.py`. From the final package directory:

```
python reproduce/compile_standalone_tex.py --source AN_GRH.tex --build-dir /tmp/an_grh_build
```

The script copies the source to the build directory, generates a local format when needed, compiles with `-no-shell-escape`, reruns until references/tables stabilize, records source/PDF/format hashes and compiler arguments, and writes all logs. It never edits the input source. Existing formats can be reused via `--format-dir`.

## Findings so far

The first snapshot compiled to35pages in3passes but exposed two real layout defects. Rendered page3 confirmed that the Lean declaration list was clipped at the paper edge; page6 confirmed the long T(C) display entered the right margin. Root corrected the canonical proof sources.

The corrected snapshot, SHA256 `ac3308412cdbb6612bab547242179c06935197fef6e8892ef9efa8920f89a367`, compiles to35pages in3passes with no overfull boxes, unresolved references or rerun requests. Underfull spacing notices and the legacy `\over` warning remain. Those are not compilation errors. Exact commands, timings and hashes are in `layout_corrected/BUILD_MANIFEST.json`.

Static checks of the initial snapshot found balanced braces/environments, no undefined or duplicate citation keys or labels, no external input dependencies, and no unknown commands. Actual compilation is the stronger command-resolution check. Compilation and PDF review are not formal verification or mathematical proof checking.

A final refresh is required if the root changes the source after this snapshot; the report and PDF must be associated with the source hash actually compiled.

## Visual QA of the corrected snapshot

All35pages were rendered and inspected through four contact sheets. Pages3 and6 were checked at full-page scale to verify the corrected declaration list and T(C) display; dense tables on pages23,25,28 were also checked at full-page scale. No clipping, overlaps, missing glyphs or broken table boundaries were observed. The PDF was copied to `final/AN_GRH.pdf` only after confirming that the current source still matched the compiled hash. This remains subject to final refresh after any additional mathematical sections are assembled.
