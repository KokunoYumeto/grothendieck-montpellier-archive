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
bounded. A further paired-constituent and dyadic-contraction argument
proves $p(f_n)>2^{cn}$ and $s(f_n)\ge2^{cn}$ for every fixed
$0<c<1/4$ eventually. Thus the literal narrow polynomial PH2 and
SH(a) index bounds also fail; an explicit threshold is given.
This does not refute the narrow SH(b) density assertion or
Kronecker-specific polynomial index bounds. A fixed product factor
separately refutes the broad subgroup density clause under finite
constant-additive input specifications.  A separate balanced tensor
construction refutes the canonical parameter clause for actual
triple-rectangular Kronecker coefficients; its numerical positive-form
clause remains open. Positive Hilbert data yield shifted polytope models; the
standard plethysm counterexample has an optimal two-dimensional model
and an actual normal multiplicity algebra with a positive multiplicative
basis and pure even Tate intersection cohomology. These results separate qualitative purity
from the additional grading, uniformity and quotient-rank information
needed for an obstruction. A named regularized theta construction
identifies the degree-$80$ cubic discriminant in the actual five-variable
plethysm algebra. Its exact input has a specified definite-unitary theta
factor and Hilbert-scheme cohomology models for all its coefficients.
Its known cusp product is the completed exterior Euler character of
these spaces, with an exact inverse at the character level.
Fixed finite definite-theta and ordinary lambda operations cannot
produce that full input; an explicit coefficient-growth bound quantifies
the necessary growth of varying data.
For the nonstandard cubic example, an explicit positive central word
realizes the quadratic operator inside the actual algebra. It admits
an explicit positive integral quadratic order, a bar-fixed source-word
lattice, and an additive cohomological model on Grothendieck groups.
An actual four-dimensional left ideal also has positive Laurent
matrices for both chosen rescaled generators and all positive words;
precise finite lambda and source-cone comparisons fail. The
ordinary graded semisimple adjoint dictionary is also excluded
by the actual spectrum at unit-circle parameters.  Completed tangle
complexes nevertheless realize the full concrete source algebra on a
rational Euler subspace, uniformly extending to actual tensor-image
algebras for $\mathfrak{sl}_2$.  Mixed homotopy relations and finite
pure canonical coefficients remain open. A separate
geometric comparison excludes the split quadratic numbers as
Frobenius eigenvalues but realizes them, at specified prime-power
fibers, as rationally normalized real-quadratic traces on ordinary
abelian surfaces. A further construction realizes them as exact
component Frobenius traces after an ordinary Tate twist on projected
cohomology of a Weil restriction. Actual specialized source generators
also act by quasi-endomorphisms, with a Rosati-positive central action.
Another
normalization proves that its positive action and Lefschetz trace and
norm do not characterize the source scale. An unconditional cubic average-polynomial estimate
and a signed global cone decomposition further delimit the remaining
index problem. Pairing constituents half a period apart cancels every
pole except a specified primitive dyadic wave. Near-multiplier
sparse-dyadic estimates and a far-multiplier count of small factors
prove uniform two-child contraction and domination by one conjugate
pair. This gives the stated strict-index refutation despite
polynomial eventual actual support.  Polynomial odd dilations even give
positive multiplicity at every positive stretch with the same
exponential strict-index failure. Explicit Hessian contractions give polynomial Fermat
nonvanishing and conductor bounds, sharpened by the supplied Dirichlet
theorem. A quantified compact-average argument also proves polynomial
eventual actual support for the entire cubic family. These are
actual-support statements, separate from the strict
constituent indices. We give checked deductions for all seven
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
             'positivity_cyclic_cover_range.tex','positivity_theta_input.tex',
             'positivity_exterior_volume.tex','positivity_density_scope.tex',
             'positivity_hessian_fermat.tex','positivity_fermat_conductor.tex',
             'positivity_definite_theta_factor.tex',
             'positivity_nonstandard_central_word.tex',
             'positivity_nonstandard_projector_lift.tex',
             'positivity_hilbert_theta_input.tex',
             'positivity_cubic_reynolds_support.tex',
             'positivity_cubic_fourfold_theta.tex',
             'positivity_paired_wave.tex',
             'positivity_dyadic_dominance.tex',
             'positivity_kronecker_bridge_audit.tex',
             'positivity_rectangular_adjoint.tex',
             'positivity_tensor_chain_point.tex',
             'positivity_higher_rank_projector_scope.tex',
             'positivity_positive_start_dilation.tex',
             'positivity_subgroup_density_padding.tex',
             'positivity_tensor_competing_component.tex',
             'positivity_tensor_second_local.tex',
             'positivity_nonstandard_weil_eigenvalue.tex',
             'positivity_logarithmic_density_padding.tex',
             'positivity_finite_theta_growth.tex',
             'positivity_nonstandard_honda_trace.tex',
             'positivity_nonstandard_correspondence.tex',
             'positivity_symmetric_restriction.tex',
             'positivity_nonstandard_tate_trace.tex']:
 parts.append((w/name).read_text())
parts.extend([needle+last,(w/'plethysm.tex').read_text(),
              (w/'positivity_actual_plethysm.tex').read_text(),
              (w/'bridges.tex').read_text(),(w/'complexity.tex').read_text(),
              (w/'open_gates.tex').read_text(),r'\clearpage\begin{thebibliography}{99}'])
for name in ['root_bib.tex','bridges_bib.tex','complexity_bib.tex']:
 parts.append((w/name).read_text())
parts.append(r'\end{thebibliography}\end{document}')
(out/'ALPOGE_GCT.tex').write_text('\n\n'.join(parts))
print({'paper_bytes':(out/'ALPOGE_GCT.tex').stat().st_size,'fragments':73})
