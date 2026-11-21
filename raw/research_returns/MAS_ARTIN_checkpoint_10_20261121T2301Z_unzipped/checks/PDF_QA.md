# Integrated PDF build and layout check

Checked on 21 November 2026 by GPT-6 Astra Pro, MAS_ARTIN `/root/pf26_audit`.

`python3 checks/build_pdf.py` builds the integrated report using the installed
pdfTeX and LaTeX sources, without a network download. It initializes the missing
format and scalable-font maps in a temporary directory. Three compilation passes
resolve the contents and cross-references. The exact PDF hash, size, page count,
and automated checks are recorded in `pdf_build_report.json`.

The baseline checked build, before subsequently added research modules, has
56 pages. Its hash is
`c246094bcc9a8256c53b00848219f9aac4a53ed8eb270bd7736907a0ecde4b67`.
The generated report records the latest build if it is subsequently refreshed.
The baseline final TeX log has no errors, warnings,
undefined controls, or overfull boxes. PyMuPDF found no text blocks outside their
page bounds. Every page was inspected in contact sheets; the opening pages and
the corrected character and S5 display layouts were also rendered at a larger
scale and inspected. The contents originally spilled a single entry onto a third
page; reducing the contents font to `small` and its paragraph spacing removed that
spill. The final opening occupies two pages before the reading guide.

## Changes made during compilation

The explicitly authorized content correction was the master status paragraph's
reference from MA-S5-017 to **MA-S5-006**. No mathematical assertion was changed.

The remaining edits were TeX syntax or layout only:

- Load `mathrsfs`, which supplies the already-used `\mathscr` command.
- Change two character-module displays from `split` to `aligned` because they
  contain multiple alignment pairs.
- Put the three completion definitions in (MA-CH.6) on separate aligned rows.
- Put the initial S5 definitions in `gathered`, with a line break before the
  displayed hypothesis.
- Typeset the long source-note path with `\path`, allowing line breaks.
- Compact the contents as described above.

The generated `.aux`, `.log`, `.out`, and `.toc` files are build products, not
source requirements. An earlier manual `pdftex.map` is likewise unnecessary:
the reproducible script supplies its own temporary map. The rendering images are
temporary QA files outside the deliverable directory. No source PDF, source
extract, or source-page image was added to this report package.

These checks concern rendering and reproducibility. They do not replace the
mathematical proof-reading events recorded in the research registers.

## Checkpoint 02 integrated refresh

Root rebuilt the expanded 95-page paper on 21 November 2026. The final three-pass log has no warnings or overfull boxes, and automated page-bound checks pass. Root visually inspected a contact sheet of pages 43, 55, 72, 79, 80, 81 and 94, covering the new character calculation, Rankin order bounds, Fourier rigidity and updated status. Those pages have no visible clipping or overlap. This is a targeted layout inspection, not a claim that every newly added page has yet received a large-scale visual review. The complete mathematical proof readings are recorded separately.

## Checkpoint 03 integrated refresh

The integrated paper now has 145 pages. Root reviewed a contact sheet of pages 25, 70, 73, 74, 83, 130 and 144; no clipping or overlap was visible. The PF26/source agent independently inspected all pages 18–27 and 52–82 in five contact sheets, covering the new source/local-limit, all-weight, regularized commutator and partial-return sections. Equation tags, proof blocks and wrapping pass. Three initially overfull displays/paragraphs were reformatted; the final build report is authoritative for warnings and page bounds. These are visual checks, not substitutes for the separately recorded complete proof readings.
