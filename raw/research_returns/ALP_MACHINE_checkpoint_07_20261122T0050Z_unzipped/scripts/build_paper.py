#!/usr/bin/env python3
"""Integrate the complete proof sources into a standalone LaTeX paper.

This is a faithful mathematical-source assembly, not a proof checker.
Individual whole-proof events remain in CHECK_EVENTS.tsv.
"""
from pathlib import Path
from datetime import datetime,timezone
import subprocess,json,hashlib,re

root=Path(__file__).resolve().parents[1]
checked=[
 'research/endpoint_cost_and_isotypy.md',
 'agents/lift_accounting.md',
 'agents/hodge_lattice_and_cm_basis.md',
 'agents/directional_budget_cancellation.md',
 'research/jacobian_period_theta.md',
 'research/all_theta_characteristic_bounds.md',
 'agents/finite_theta_null_normalization.md',
 'agents/trace_one_leading_jet.md',
 'research/trace_one_theta_scalar.md',
 'agents/definite_oscillator_cm_bridge.md',
 'agents/jacobian_reduced_theta.md',
 'agents/definite_oscillator.md',
 'agents/kummer_extension.md',
 'agents/kummer_cubic_host.md',
 'agents/definite_oscillator_moved_family.md',
 'agents/definite_oscillator_ramified_phase.md',
 'agents/actual_torus_first_lift.md',
 'research/split_place_class_representatives.md',
 'agents/jacobian_hessian_pcurvature.md',
 'agents/jacobian_source_gauge_match.md',
 'agents/permitted_orbit_first_image.md',
 'agents/definite_oscillator_unramified_host.md',
 'agents/definite_oscillator_positive_pairing.md',
 'research/compact_determinant_twist_accounting.md',
 'agents/definite_oscillator_real_second_edge.md',
 'agents/fixed_conductor_type_repair.md',
 'agents/jacobian_differential_lattice_obstruction.md',
 'agents/jacobian_sharp_small_prime_directions.md',
 'research/first_lift_unramified_host.md',
 'research/permitted_family_unramified_host.md',
 'agents/second_definite_lift_nonvanishing.md',
 'agents/definite_oscillator_selected_partitions.md',
 'agents/definite_oscillator_source_operator_match.md',
 'agents/kummer_relative_height_period.md',
 'agents/definite_oscillator_chart_phase.md',
 'research/selected_schur_metric.md',
 'agents/selected_schur_permitted_jets.md',
 'research/selected_even_first_lift.md',
 'agents/fixed_section_sharp_first_images.md',
 'agents/definite_oscillator_doubling_dictionary.md',
 'agents/selected_even_chain_nonvanishing.md',
 'agents/single_finite_heisenberg_chain.md',
 'research/selected_analytic_source_predicates.md',
 'agents/definite_oscillator_raw_xi.md',
 'agents/selected_jet_connection_normal_form.md',
 'agents/selected_schur_sharp_content.md',
 'agents/selected_adjacent_gap_content.md',
 'agents/spherical_tests_and_29_only_chain.md',
 'agents/definite_oscillator_auxiliary_multijets.md',
 'agents/hyp3_selected_costs.md',
 'research/selected_tower_cuspidality_stability.md',
 'agents/selected_schur_exact_slope.md',
 'agents/definite_oscillator_terminal_xi.md',
 'agents/unramified_eta_type_obstruction.md',
 'agents/prescribed_column_local_type_obstruction.md',
 'agents/degree_seven_eta_repair.md',
 'agents/degree_seven_principal_host.md',
 'agents/degree_four_principal_host_repair.md',
 'agents/literal_g_character_compatibility.md',
 'agents/definite_oscillator_terminal_fourier_gram.md',
 'agents/definite_oscillator_steinberg_first_input.md',
 'research/selected_real_descent.md',
 'research/last_two_free_data_seesaws.md',
 'agents/ramified_column_type_chain.md',
 'agents/raw_first_g_steinberg_bridge.md',
 'agents/enlarged_host_ranks_characters_alpha.md',
 'agents/definite_oscillator_degree_seven_first_input.md',
 'research/explicit_t_primes_and_central_class_input.md',
 'agents/raw_terminal_g_theta_quotient.md',
 'agents/definite_oscillator_first_tq_raw.md',
 'agents/selected_cm_frobenius_sharp_content.md',
 'agents/composed_raw_sharp_g_chain.md',
 'agents/torsion_gauge_selected_auxiliary_content.md',
 'research/selected_fixed_prime_size_intervals.md',
 'agents/raw_coupled_q_fourier.md',
 'agents/definite_oscillator_raw_first_nonvanishing.md',
]
pending=[]
documentation=['agents/cmdata_theta_constructor_audit.md']
if (root/'GROTHENDIECK_DICTIONARY.md').exists():documentation.append('GROTHENDIECK_DICTIONARY.md')
preface=r'''---
title: 'ALP_MACHINE: Mixed CM theta sections, lift costs, and arithmetic comparison gates'
author: 'GPT-6 Astra Pro research team'
date: '21 November 2026 — active research version'
documentclass: article
fontsize: 10pt
geometry: margin=22mm
mainfont: DejaVu Serif
sansfont: DejaVu Sans
monofont: DejaVu Sans Mono
mathfont: Latin Modern Math
colorlinks: true
linkcolor: blue
urlcolor: blue
header-includes:
  - '\usepackage{amsmath,amssymb,amsthm}'
  - '\usepackage{fvextra}'
  - '\usepackage{newunicodechar}'
  - '\providecommand{\bigboxtimes}{\mathop{\boxtimes}\displaylimits}'
  - '\newunicodechar{𝓞}{\ensuremath{\mathcal O}}'
  - '\newunicodechar{ℓ}{\ensuremath{\ell}}'
  - '\newunicodechar{∎}{\ensuremath{\blacksquare}}'
  - '\newunicodechar{⋯}{\ensuremath{\cdots}}'
  - '\newunicodechar{⋊}{\ensuremath{\rtimes}}'
  - '\newunicodechar{𝔣}{\ensuremath{\mathfrak f}}'
  - '\newunicodechar{𝜎}{\ensuremath{\sigma}}'
  - '\newunicodechar{ℒ}{\ensuremath{\mathcal L}}'
  - '\newunicodechar{〈}{\ensuremath{\langle}}'
  - '\newunicodechar{〉}{\ensuremath{\rangle}}'
  - '\DefineVerbatimEnvironment{verbatim}{Verbatim}{breaklines,breakanywhere,fontsize=\small}'
  - '\setlength{\emergencystretch}{3em}'
  - '\setcounter{tocdepth}{2}'
---

# Status and conventions

The requested shorter actual mixed-type lift chain, universal negative
lift-cost theorem, arithmetic MainX pairing value, and Kummer Hecke RH
theorem have not been established. This is the integrated active paper,
containing the full proofs written so far. Checked findings and work
awaiting whole-proof review are separated below. The dated register gives
the exact status of each original question and each completed subproblem.

Alpöge's theorem and archive are accepted as stipulated. No Lean build
or independent validity audit of that theorem is claimed. Settled prior
findings retain the supplied intake statuses. A literature theorem is an
input, not a newly proved finding. All new proofs have stable identifiers;
the event log records who read a complete proof and distinguishes those
readings from numerical diagnostics and exact computations.

The notation `M` in the source arithmetic Level is distinct from the
number of iterated lifts when both occur in a discussion. The actual
Level requires an odd integer. Three theta germs must also be kept
distinct: the value-one even-characteristic germ F1 on the D135 line,
its normalized Mumford translate Sigma_tr on the trace-one line, and
the trace-one germ sigma_q with quadratic term u1*u3-u2^2. AM-R-006
computes the scalar between the latter two. Later findings refine the
limitations recorded in earlier contributions; none silently replaces
a selected automorphic image by an unrestricted formal function.

ALP-LIFT-01 and AM-R-001 are two independently written versions of the
same elementary changed-family accounting identity. They are retained
with their check histories but count as one finding in novelty summaries.

\tableofcontents
\clearpage
\part{Checked findings and their full proofs}

'''
chunks=[preface]
manifest=[]
for part,files in [('checked',checked),('pending',pending),('documentation',documentation)]:
 if part=='pending':chunks.append('\n\\clearpage\n\\part{Proofs awaiting completed whole-proof review}\n\n'+('The following contributions are retained as work in progress at this build. Their status is not upgraded by inclusion.\n' if files else 'No completed proof awaiting whole-proof review is included in this build. The original questions that remain open are recorded in QUESTIONS.tsv and the status section; they are not declared proved by this empty part.\n'))
 if part=='documentation':chunks.append('\n\\clearpage\n\\part{Source audit and geometric dictionary}\n')
 for f in files:
  p=root/f
  if not p.exists():continue
  data=p.read_text()
  # Formatting only: these source prose formulas had bare TeX accents.
  replacements={
   r'Tr(ξ ζ^j \overline{ζ^k})':r'\(\operatorname{Tr}(\xi\zeta^j\overline{\zeta^k})\)',
   r'G=P Y \bar P^T':r'\(G=P Y\bar P^T\)',
   r'G=P Y\bar P^T is':r'\(G=P Y\bar P^T\) is',
   r'πκ Y^−1(z−\bar z)':r'\(\pi\kappa Y^{-1}(z-\bar z)\)',
   r'−πκ Y^−1\bar z':r'\(-\pi\kappa Y^{-1}\bar z\)',
   r'exp(−πκ\bar z^TY^−1z)':r'\(\exp(-\pi\kappa\bar z^TY^{-1}z)\)',
   r'κ(z)=(z/\bar z)²':r'\(\kappa(z)=(z/\bar z)^2\)',
   r'x/\bar x=det g':r'\(x/\bar x=\det g\)',
   r'⟨z,a⟩=Re(z\bar a)':r'\(\langle z,a\rangle=\operatorname{Re}(z\bar a)\)',
   r'χ(\bar{\mathfrak a})=\overline{\chi(\mathfrak a)}':r'\(\chi(\bar{\mathfrak a})=\overline{\chi(\mathfrak a)}\)',
   r'a↦\bar a':r'\(a\mapsto\bar a\)',
   r'm^{-1}Λ*\setminus\{0\}':r'\(m^{-1}\Lambda^*\setminus\{0\}\)',
   r'v_\mathfrak p':r'v_{\mathfrak p}',
   r'(\bar α)':r'\(\bar\alpha\)',
   r'\text{output at 1}\hline':r'\text{output at 1}\\\hline',
  }
  for old,new in replacements.items():data=data.replace(old,new)
  # Multiple alignment pairs need aligned, not the two-column split environment.
  # This is a layout-only transformation of the displayed equations.
  def compatible_alignment(match):
   body=match.group(1)
   if any(line.count('&')>1 for line in body.splitlines()):
    return r'\begin{aligned}'+body+r'\end{aligned}'
   return match.group(0)
  data=re.sub(r'\\begin\{split\}(.*?)\\end\{split\}',compatible_alignment,data,flags=re.S)
  chunks.append('\n\\clearpage\n\n'+data+'\n')
  manifest.append({'path':f,'part':part,'sha256':hashlib.sha256(p.read_bytes()).hexdigest()})
source=root/'research/integrated_paper_source.md'
source.write_text(''.join(chunks))
cmd=['pandoc',str(source),'-f','markdown+tex_math_single_backslash+raw_tex+autolink_bare_uris-superscript-subscript',
     '-t','latex','--standalone','--top-level-division=section',
     '--no-highlight','--lua-filter='+str(root/'scripts/paper_format.lua'),'--wrap=none','-o',str(root/'ALP_MACHINE.tex')]
subprocess.run(cmd,check=True)
(root/'research/paper_build.json').write_text(json.dumps({'built_utc':datetime.now(timezone.utc).isoformat(),'command':cmd,'sources':manifest,'scope':'Source assembly only; no mathematical or typesetting validation implied.'},indent=2)+'\n')
print(json.dumps({'tex_bytes':(root/'ALP_MACHINE.tex').stat().st_size,'source_files':len(manifest)}))
