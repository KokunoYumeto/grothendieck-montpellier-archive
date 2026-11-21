"""Flatten the current checked sections into one standalone KTOWER.tex."""
from pathlib import Path
import hashlib,json,re
BASE=Path(__file__).resolve().parent
preamble=r'''\documentclass[11pt,a4paper]{article}
\usepackage[T1]{fontenc}
\usepackage[utf8]{inputenc}
\usepackage{lmodern}
\usepackage[margin=25mm]{geometry}
\usepackage{amsmath,amssymb,amsthm,mathtools,mathrsfs}
\usepackage{booktabs,longtable,array,enumitem}
\usepackage{microtype}
\usepackage{xurl}
\usepackage[colorlinks=true,linkcolor=blue,urlcolor=blue,citecolor=blue]{hyperref}
\setlength{\emergencystretch}{3em}
\setlength{\parskip}{3pt}
\setcounter{tocdepth}{2}
\newtheorem{theorem}{Theorem}[section]
\newtheorem{proposition}[theorem]{Proposition}
\newtheorem{lemma}[theorem]{Lemma}
\newtheorem{corollary}[theorem]{Corollary}
\theoremstyle{definition}
\newtheorem{definition}[theorem]{Definition}
\newtheorem{remark}[theorem]{Remark}
\newtheorem{example}[theorem]{Example}
\renewcommand{\paragraph}[1]{\par\smallskip\noindent\textbf{#1}\quad\ignorespaces}
\newcommand{\Gal}{\operatorname{Gal}}
\newcommand{\Spec}{\operatorname{Spec}}
\title{KTOWER\\The Galois action on the tower,\\the $K$-groups of $\mathbf Z$, and cote 149}
\author{Research continuation of K17, AN\_GRH, and GRH\_NIGHT\\GPT-6 Astra Pro; effort setting not exposed}
\date{21 November 2026 --- active research snapshot}
\begin{document}
\maketitle
\begin{abstract}
This report separates exact new results, carried theorems, and unresolved
arithmetic gates. It gives uniform compact-unitary and classical finite
models, independent trace and source audits, a stronger explicit bound
for higher $K$-groups, and newly completed finite vanishing certificates.
It also records counterexamples to finite-field section surjectivity
and unrestricted higher-dimensional prime-to-characteristic point
separation, and audits the marked tangential statements at cote149.
The all-weight vanishing target and the remaining Ihara and geometric
cover questions are not asserted solved.
\end{abstract}
\tableofcontents
\clearpage
'''
checked=[
'sections/00_introduction.tex',
'evidence/lean_chain/onechar_section.tex',
'evidence/unitary_audit/unitary_results.tex',
'evidence/gl2_uniform_section.tex',
'evidence/unitary_audit/coverage_results.tex',
'evidence/unitary_audit/endoscopic_results.tex',
'evidence/unitary_audit/endoscopic_converse.tex',
'evidence/unitary_audit/symmetric_square_results.tex',
'evidence/unitary_audit/dual_hecke_results.tex',
'evidence/unitary_audit/quartic_refinement.tex',
'evidence/higher4/higher4_section.tex',
'evidence/higher4/native_full_rows_section.tex',
'evidence/higher4/exact_cyclic_charpoly_section.tex',
'evidence/higher4/exact_sum_first_replay_section.tex',
'sections/component_extension.tex',
'evidence/higher4/next_vanishing_section.tex',
'evidence/higher4/later_vanishing_section.tex',
'evidence/higher4/last_vanishing_section.tex',
'evidence/main_gate/residual_global_gate.tex',
'evidence/main_gate/residual_trace_avoidance.tex',
'evidence/main_gate/two_field_eisenstein_obstruction.tex',
'evidence/main_gate/two_field_global_obstruction.tex',
'evidence/main_gate/two_field_infinite_family.tex',
'evidence/main_gate/stable_residual_propagation.tex',
'evidence/main_gate/ordinary_symmetric_square_admissibility.tex',
'evidence/main_gate/level_variation_scope.tex',
'evidence/unitary_audit/host_sign_results.tex',
'evidence/unitary_audit/projector_results.tex',
'evidence/unitary_audit/projector_selmer_equivalence.tex',
'evidence/unitary_audit/projector_flatness_audit.tex',
'evidence/unitary_audit/hecke_normal_results.tex',
'evidence/main_gate/field_variation_nonvanishing.tex',
'evidence/main_gate/explicit_two_unit_family.tex',
'evidence/main_gate/odd_discriminant_two_unit_family.tex',
'evidence/main_gate/bernoulli_prefix_formula.tex',
'evidence/main_gate/third_unit_character_obstruction.tex',
'evidence/main_gate/auxiliary_unit_selmer_bridge.tex',
'evidence/unitary_audit/reducible_comparison/reducible_comparison_results.tex',
'evidence/unitary_audit/reducible_comparison/ordinary_rank2_exclusion.tex',
'evidence/unitary_audit/reducible_comparison/polarized_extension_graph.tex',
'evidence/unitary_audit/reducible_comparison/local_mixed_paths.tex',
'evidence/soule_comparison.tex',
'evidence/main_gate/soule_stabilizer_correction.tex',
'evidence/lean_chain/c7_section.tex',
]
geometry=[
'evidence/geometry_tower/finite_field_sections.tex',
'evidence/geometry_tower/polycurve_counterexample.tex',
'evidence/geometry_tower/artin_tower_counterexample.tex',
'evidence/geometry_tower/product_separation.tex',
'evidence/geometry_tower/f149_review.tex',
'evidence/geometry_tower/f149_normalizer_comparison.tex',
'evidence/geometry_tower/route2_gate.tex',
'evidence/geometry_tower/rm_frobenius_avoidance.tex',
]
open_parts=['sections/open_gates.tex','evidence/main_gate/ordinary_eisenstein_ideal_attempt.tex','evidence/main_gate/recent_arithmetic_route_audits.tex','evidence/geometry_tower/ihara_gate.tex']
chunks=[preamble,r'\part{Checked findings and exact source comparisons}']
manifest=[]
def add(name):
 data=(BASE/name).read_bytes();text=data.decode()
 text=re.sub(r'\\texttt\{([^{}]*)\}',lambda m:(r'\path{'+m.group(1).replace(r'\_', '_')+'}') if (len(m.group(1))>30 or any(token in m.group(1) for token in ('/',r'\_','.tex','.lean'))) else m.group(0),text)
 chunks.append('\n% BEGIN '+name+'\n'+text+'\n% END '+name+'\n')
 manifest.append({'path':name,'sha256':hashlib.sha256(data).hexdigest()})
for name in checked:add(name)
chunks.append(r'\section{Cote 149 and the geometric questions}')
for name in geometry:add(name)
add('sections/framework.tex')
chunks.append(r'\part{Unresolved questions and unproved proposals}')
for name in open_parts:add(name)
chunks.append(r'\end{document}')
(BASE/'KTOWER.tex').write_text('\n'.join(chunks))
(BASE/'PAPER_ASSEMBLY.json').write_text(json.dumps({'standalone':True,'sections':manifest},indent=2)+'\n')
print('Assembled',len(manifest),'sections into standalone KTOWER.tex')
