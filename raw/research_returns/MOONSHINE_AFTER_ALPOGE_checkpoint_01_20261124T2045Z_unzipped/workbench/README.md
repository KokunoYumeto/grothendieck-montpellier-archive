# Moonshine after Alpöge's theorem

This workbench contains two self-contained paper projects, exact arithmetic
certificates, and an audit trail. The main moonshine paper proves the
Dirichlet-shadow reductions and off-line-zero results, supplies lattice and
eta-form calculations, and separates class-number bounds from central values.
The companion note proves reductions and obstructions for the positive-
infinity-type Hecke problem. It does not prove its Riemann hypothesis.

## Reading and compiling

The main project is work/moonshine/v1/paper/main.tex and the PDF beside it.
The companion is work/cm_hecke/v1/paper/cm_hecke_windows.tex and its PDF.
The check folders contain only original programs, certificates and research
records. No attached archive or downloaded paper is included.

On a complete TeX installation run pdflatex main, bibtex main, pdflatex main,
pdflatex main in the main paper directory. The companion has its bibliography
inline and needs two runs of pdflatex cm_hecke_windows.
Python checks state their commands and dependencies in their docstrings or
component READMEs. Some reconstruction programs use the original attachment
as a separately provided input. Final Gram matrices and enumeration
certificates are included for replay without that attachment.

## Deposit status

The requested target is format 1 of mathematics-workbenches. The owner
assigns permanent WB numbers and paper pages when filing; no official
number has been invented. The current directory names and PENDING statement
identifiers are pre-deposit handles. At filing they must be replaced with
permanent tags, the registry URL must be replaced by each paper's page,
and the deposited commit and manifest hash recorded.
This working draft has not been deposited or passed a repository push gate.
There is no DEPOSITED.md.

All model checks are same-model checks by separate GPT-6 Astra instances
(ChatGPT Pro mode); the effort setting is not separately exposed.
Published Lean verification reports are cited as reports, not represented
as a local kernel rebuild. No human has checked these papers.
