from pathlib import Path
base=Path(__file__).resolve().parent.parent
w=base/'work'; out=base/'deliverable'; out.mkdir(exist_ok=True)
preamble=r'''\documentclass[11pt,a4paper]{article}
\ifdefined\pdfmapfile
\pdfmapfile{+cm.map}
\pdfmapfile{+cmextra.map}
\pdfmapfile{+symbols.map}
\pdfmapfile{+euler.map}
\pdfmapfile{+lm.map}
\pdfmapfile{+rsfs.map}
\fi
\usepackage{lmodern}
\usepackage[margin=25mm]{geometry}
\usepackage{amsmath,amssymb,amsthm,mathtools,mathrsfs}
\usepackage{booktabs,tabularx,longtable,array}
\usepackage[hyphens]{url}
\usepackage[colorlinks=true,linkcolor=blue!45!black,citecolor=blue!45!black,urlcolor=blue!45!black]{hyperref}
\usepackage{xcolor}
\usepackage{enumitem}
\setlist{itemsep=3pt,topsep=5pt}
\setlength{\emergencystretch}{3em}
\setlength{\parskip}{4pt}
\setlength{\parindent}{0pt}
\renewcommand{\arraystretch}{1.17}
\newtheorem{proposition}{Proposition}[section]
\newtheorem{corollary}[proposition]{Corollary}
\newtheorem{theorem}[proposition]{Theorem}
\newtheorem{lemma}[proposition]{Lemma}
\hypersetup{pdftitle={Purity, positive Hilbert series, and the GCT flip},pdfauthor={Research analysis},pdfsubject={Checked deductions, exact source scopes, and open gates}}
\title{Purity, positive Hilbert series, and the GCT flip\\[5pt]\large Checked deductions and remaining gates}
\author{}
\date{21 November 2026}
\begin{document}
\maketitle
\begin{abstract}
We examine what the supplied RH/Dirichlet-GRH and subexponential counting
theorems, and their proposed positivity methods, yield for geometric
complexity theory. For ordinary cubic plethysm, a complete classification
of extremal two-power stabilizer supports makes the chain curve the unique
nonzero fixed component of the invariant quotient. Its Hilbert series
has actual simple poles at roots of unity of order $2^{n-1}$,
although the conjectured size
parameter is $O(n^6)$. Thus both the numerical positive-form clause and
the stronger canonical clause of GCT VI PH3 are false. An explicit
polynomial bound for the coefficient
positivity index of a positive rational Hilbert series proves the revised
GCT implication PH3 $\Rightarrow$ PH2. Fixed-rank torus embeddings refute
the printed rank-only bounds in the broader subgroup-restriction problem.
Fixed inner dimension nevertheless gives a finite uniform bound; its
optimal canonical envelope is therefore finite but not polynomially
bounded. The pole theorem does not settle PH2 or saturation; an
exterior-power reduction gives a separate square-root lower bound for
their indices on an infinite cubic family. Positive Hilbert data yield shifted polytope models; the
standard plethysm counterexample has an optimal two-dimensional model
and an actual normal multiplicity algebra with a positive multiplicative
basis and pure even Tate intersection cohomology. These results separate qualitative purity
from the additional grading, uniformity and quotient-rank information
needed for an obstruction. A named regularized theta construction
identifies the degree-$80$ cubic discriminant in the actual five-variable
plethysm algebra. For the nonstandard cubic example, exact trace and norm
models and a positive operator expose the necessary normalization and
quadratic descent data. An unconditional cubic average-polynomial estimate
and a signed global cone decomposition further delimit the remaining
index problem. We give checked deductions for all seven
requested Grothendieck bridges, distinguish Dirichlet from number-field
GRH in complexity applications, and track the precise consequences and
limitations of the supplied ETH theorem. No resolution of $\mathsf P$
versus $\mathsf{NP}$ or the usual $\mathsf{VP}$ versus $\mathsf{VNP}$
problem is claimed; unresolved targets are listed separately.
\end{abstract}
{\small\setlength{\parskip}{0pt}\tableofcontents}
\clearpage
'''
front=(w/'frontmatter.tex').read_text()
pos=(w/'positivity.tex').read_text()
needle=r'\subsection{Disposition of the main request}'
first,last=pos.split(needle,1)
parts=[preamble,front,r'\clearpage\part{Checked findings and cited background}',first]
for name in ['positivity_bounds.tex','positivity_modular.tex','positivity_ph3.tex',
             'positivity_reconstruction.tex','positivity_torus.tex',
             'positivity_fixedembedding.tex','positivity_fixed_plethysm.tex',
             'positivity_dimension_bound.tex','positivity_cubic_counterexample.tex',
             'positivity_universal_denominator.tex','positivity_period_collapse.tex',
             'positivity_gorenstein_collapse.tex','positivity_noncancellation.tex',
             'positivity_chain_smoothness.tex','positivity_binary_holes.tex',
             'positivity_finite_lift.tex','positivity_graph_support.tex',
             'positivity_chain_residue.tex','positivity_squarefree_support.tex',
             'positivity_full_cubic_support.tex','positivity_actual_cubic_pole.tex',
             'positivity_exterior_duality.tex','positivity_large_period_zero_indices.tex',
             'positivity_fourier_index_gate.tex','positivity_quaternary_indices.tex',
             'positivity_nonstandard_descent.tex','positivity_automorphic_cubic.tex',
             'positivity_bounded_entry_average.tex','positivity_nonstandard_trace_norm.tex',
             'positivity_klein_phase.tex','positivity_theta_discriminant.tex',
             'positivity_cubic_average_upper.tex','positivity_binary12_hsop.tex',
             'positivity_klein_global_contribution.tex',
             'positivity_cyclic_cover_range.tex','positivity_theta_input.tex']:
 parts.append((w/name).read_text())
parts.extend([needle+last,(w/'plethysm.tex').read_text(),
              (w/'positivity_actual_plethysm.tex').read_text(),
              (w/'bridges.tex').read_text(),(w/'complexity.tex').read_text(),
              (w/'open_gates.tex').read_text(),r'\clearpage\begin{thebibliography}{99}'])
for name in ['root_bib.tex','bridges_bib.tex','complexity_bib.tex']:
 parts.append((w/name).read_text())
parts.append(r'\end{thebibliography}\end{document}')
(out/'ALPOGE_GCT.tex').write_text('\n\n'.join(parts))
print({'paper_bytes':(out/'ALPOGE_GCT.tex').stat().st_size,'fragments':46})
