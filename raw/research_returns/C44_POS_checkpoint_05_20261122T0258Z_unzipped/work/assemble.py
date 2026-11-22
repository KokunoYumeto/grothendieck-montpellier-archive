from pathlib import Path
import csv
import datetime
import hashlib
import json

ROOT=Path(__file__).resolve().parents[1]
OUT=ROOT/'deliverables'
OUT.mkdir(exist_ok=True)
stamp=datetime.datetime.now(datetime.timezone.utc).astimezone(datetime.timezone(datetime.timedelta(hours=1)))

preamble=r'''\documentclass[11pt]{article}
\usepackage[T1]{fontenc}
\usepackage[utf8]{inputenc}
\usepackage{lmodern,amsmath,amssymb,amsthm,mathrsfs,mathtools,booktabs,longtable,array}
\usepackage[margin=1in]{geometry}
\usepackage[colorlinks=true,urlcolor=blue,linkcolor=blue]{hyperref}
\newtheorem{theorem}{Theorem}[section]
\newtheorem{proposition}[theorem]{Proposition}
\newtheorem{lemma}[theorem]{Lemma}
\newtheorem{corollary}[theorem]{Corollary}
\theoremstyle{remark}\newtheorem{remark}[theorem]{Remark}
\DeclareMathOperator{\CH}{CH}
\DeclareMathOperator{\Alg}{Alg}
\DeclareMathOperator{\Pic}{Pic}
\DeclareMathOperator{\Alb}{Alb}
\DeclareMathOperator{\NS}{NS}
\DeclareMathOperator{\End}{End}
\DeclareMathOperator{\Hom}{Hom}
\DeclareMathOperator{\Nm}{Nm}
\newcommand{\Q}{\mathbf Q}\newcommand{\Z}{\mathbf Z}\newcommand{\F}{\mathbf F}
\newcommand{\tun}[1]{#1}
\setlength{\emergencystretch}{2em}
\title{C44\_POS: primitive signs, special axes, and the 1964 programme}
\author{Research continuation of JAC1964 and SIGN\_NEXT}
\date{22 November 2026}
\begin{document}
\maketitle
\begin{abstract}
Working research manuscript. The general fixed-axis sign and the Fermat
Abel--Jacobi injection remain unresolved. New checked results include
an exact axis primitive decomposition, lifts of every embedded smooth
axis (without a cycle-lifting assertion), and an unconditional sign
theorem whenever at most one potential Tate direction remains after
a known positive algebraic span. An extending orthogonal-block criterion
now also proves the sign on actual closed affine-$S_3$ families with
three residual potential Tate directions, including families with a
known positive span of rank six. The unsplit higher-rank gate remains
open. Other
checked findings include closed supersingular axes with their entire
positive kernels controlled, intrinsically nonliftable surface centres
whose primitive nonliftability is still open, lifts of every finite
curve cover as a map, special-cover sign tests, exact integral
arithmetic obstructions, a characteristic-$p$ detector/division theorem,
and geometric extensions of the primitive incidence polarization.
The algebraically trivial Fermat obstruction is reduced to specified
nonzero universal cycles from excess Picard quotients; several entire
classes of singular ample image surfaces are eliminated in rational
Chow. Full Abel--Jacobi injectivity remains open.
The proposed supersingular Fermat test case already satisfies the
required Hodge standard conjecture; its corrected restriction and
weighted Gysin conditions are verified explicitly. A separate
nonsupersingular degree-seven Fermat calculation supplies explicit
new special cycles, all-prime Tate and positivity for the fourfold,
and numerical and 13-adic positivity for its square.
Every use of 032 or Milne's 2026 report remains conditional on those
unrefereed preprints. The separate Milne 2022 transfer assertion is
exposed wherever used. Whole-proof reading events and finite
computations are distinguished in \texttt{CHECK\_EVENTS.tsv}.
\end{abstract}
\tableofcontents
\part{Checked findings and explicitly conditional deductions}
\section{Normalization, scope, and inherited results}
The starting isometry is JAC1964 H9-T7, equation (H9.18):
\[
 A_X\oplus A_B\simeq\CH^m(Y)_{\mathrm{hom},\Q}/\mathcal H_0,
 \qquad Q((z,w),(z',w'))=(-1)^m\int_Xzz'+(-1)^{m-1}\int_Bww'.
\]
Here $A_B=\ker\kappa_*$ on the algebraic middle classes of the axis,
and $h_BA_B=0$. This is an inherited statement, not a new result of
this run. The ambient sign is conditional on 032 Corollary 8.4 and
Milne's report. Weak semidefiniteness and strict positive definiteness
are distinguished throughout; no numerical/homological equivalence
on an arbitrary axis is silently assumed.

Geometric generic parameter points are taken over algebraic closures
of function fields. They are not closed points over
$\overline{\mathbf F}_p$. A monodromy vanishing assertion at the
former does not settle a sign at every latter point.

Every finding retains its stable C44 identifier. A displayed
proposition that assumes an additional unproved input is a checked
conditional implication, not a proof of that input. Prior statements
retain their JAC1964 or SIGN\_NEXT identifiers and are not claimed
as findings of this continuation. The governing source is the attached
\texttt{PROMPT(20261121-231316).md}.
'''

checked=[
 'work/axis/axis_contribution.tex',
 'work/axis/axis_correspondence_obstruction.tex',
 'work/axis/axis_forced_tate_root.tex',
 'work/axis/root_explicit_axes.tex',
 'work/axis/axis_boundary_relation.tex',
 'work/axis/axis_asymptotic_centres.tex',
 'work/axis/axis_product_curves.tex',
 'work/axis/axis_product_grid.tex',
 'work/axis/axis_grid_strict.tex',
 'work/axis/axis_supersingular_nonliftable.tex',
 'work/axis/axis_product_ci_matching.tex',
 'work/axis/relative_form_transfer.tex',
 'work/covers/contribution.tex',
 'work/covers/boundary_strata.tex',
 'work/covers/as_conductor_strata.tex',
 'work/arithmetic/contribution.tex',
 'work/arithmetic/fermat_relative_transfer.tex',
 'work/arithmetic/fermat7_frobenius.tex',
 'work/scan_w/contribution.tex',
 'work/scan_w/relative_th4.tex',
 'work/scan_w/sharp_cycle_bound.tex',
]
if (ROOT/'work/checks/axis_frobenius_selection_passed.txt').exists():
    checked.insert(checked.index('work/covers/contribution.tex'),
                   'work/axis/axis_frobenius_selection.tex')
if (ROOT/'work/checks/closed_rank_one_axis_passed.txt').exists():
    checked.insert(checked.index('work/covers/contribution.tex'),
                   'work/scan_w/closed_rank_one_axis.tex')
if (ROOT/'work/checks/closed_odd_rank_axes_passed.txt').exists():
    checked.insert(checked.index('work/covers/contribution.tex'),
                   'work/scan_w/closed_odd_rank_axes.tex')
if (ROOT/'work/checks/nonliftable_surface_centres_passed.txt').exists():
    checked.insert(checked.index('work/covers/contribution.tex'),
                   'work/axis/nonliftable_surface_centres.tex')
if (ROOT/'work/checks/axis_one_tate_direction_passed.txt').exists():
    checked.insert(checked.index('work/covers/contribution.tex'),
                   'work/scan_w/axis_one_tate_direction.tex')
if (ROOT/'work/checks/fermat_excess_picard_passed.txt').exists():
    checked.insert(checked.index('work/arithmetic/fermat_relative_transfer.tex'),
                   'work/arithmetic/fermat_excess_picard.tex')
for marker, file, before in [
    ('constrained_moment_monodromy_passed', 'work/axis/constrained_moment_monodromy.tex', 'work/covers/contribution.tex'),
    ('axis_realization_kernel_passed', 'work/axis/axis_realization_kernel.tex', 'work/covers/contribution.tex'),
    ('equivariant_axis_blocks_passed', 'work/scan_w/equivariant_axis_blocks.tex', 'work/covers/contribution.tex'),
    ('affine_s3_axis_geometry_passed', 'work/scan_w/affine_s3_axis_geometry.tex', 'work/covers/contribution.tex'),
    ('s3_multiplicity_monodromy_passed', 'work/axis/s3_multiplicity_monodromy.tex', 'work/covers/contribution.tex'),
    ('axis_realization_blocks_passed', 'work/axis/axis_realization_blocks.tex', 'work/covers/contribution.tex'),
    ('axis_primitive_semiregularity_passed', 'work/axis/axis_primitive_semiregularity.tex', 'work/covers/contribution.tex'),
    ('higher_dimensional_s3_axes_passed', 'work/scan_w/higher_dimensional_s3_axes.tex', 'work/covers/contribution.tex'),
    ('totally_real_axis_blocks_passed', 'work/scan_w/totally_real_axis_blocks.tex', 'work/covers/contribution.tex'),
    ('fermat_cartier_families_passed', 'work/arithmetic/fermat_cartier_families.tex', 'work/arithmetic/fermat_relative_transfer.tex'),
    ('low_rank_tate_obstructions_passed', 'work/scan_w/low_rank_tate_obstructions.tex', 'work/covers/contribution.tex'),
    ('fermat_albanese_surfaces_passed', 'work/arithmetic/fermat_albanese_surfaces.tex', 'work/arithmetic/fermat_relative_transfer.tex'),
    ('separable_cover_lifts_passed', 'work/covers/separable_cover_lifts.tex', 'work/arithmetic/contribution.tex'),
    ('fermat_product_surfaces_passed', 'work/arithmetic/fermat_product_surfaces.tex', 'work/arithmetic/fermat_relative_transfer.tex'),
    ('odd_tate_selection_axes_passed', 'work/scan_w/odd_tate_selection_axes.tex', 'work/covers/contribution.tex'),
    ('axis_ring_obstruction_passed', 'work/axis/axis_ring_obstruction.tex', 'work/covers/contribution.tex'),
    ('fermat_residual_motive_passed', 'work/arithmetic/fermat_residual_motive.tex', 'work/arithmetic/fermat_relative_transfer.tex'),
]:
    if (ROOT/('work/checks/'+marker+'.txt')).exists():
        checked.insert(checked.index(before), file)
boundary_checked=(ROOT/'work/checks/boundary_strata_passed.txt').exists()
if not boundary_checked: checked.remove('work/covers/boundary_strata.tex')
th5_checked=(ROOT/'work/checks/consolidated_th5_passed.txt').exists()
if th5_checked: checked.append('work/consolidated_th5.tex')
parts=[preamble]
for name in checked:
    parts += ['\n% BEGIN '+name+'\n',(ROOT/name).read_text(),'\n% END '+name+'\n']
parts.append('\n\\part{Unchecked candidates and unresolved work}\n')
if (ROOT/'work/scan_w/totally_real_axis_blocks.tex').exists() and not (ROOT/'work/checks/totally_real_axis_blocks_passed.txt').exists():
    parts.append('\nThe following coefficient-field criterion is awaiting completion of its whole-proof checks. It is not promoted to a checked finding at this checkpoint.\n')
    parts.append((ROOT/'work/scan_w/totally_real_axis_blocks.tex').read_text())
if not (ROOT/'work/checks/axis_frobenius_selection_passed.txt').exists():
    parts.append('The following closed-point selection criterion awaits its independent whole-proof review.\n')
    parts.append((ROOT/'work/axis/axis_frobenius_selection.tex').read_text())
if not boundary_checked:
    parts.append('The following two cover candidates are awaiting an independent whole-proof reading. They are not included among checked findings at this checkpoint.\n')
    parts.append((ROOT/'work/covers/boundary_strata.tex').read_text())
if not th5_checked:
    parts.append('\n\\section{Consolidation under final review}\n')
    parts.append((ROOT/'work/consolidated_th5.tex').read_text())
parts.append(r'''
\section{Unresolved goals}
The fixed-axis sign is not proved for every special axis, and no
wrong-sign algebraic class is constructed. The universal lifting
question for classes remains open. The special-cover sign remains
open at arbitrary closed points with new algebraic trace-kernel
classes. Fermat Abel--Jacobi injectivity remains open, with the
exact gates specified above. Full Th.~4 for arbitrary new special
incidence directions is not proved. The proposed supersingular
Fermat family does not meet the requested initially-unknown-$I$
status. The ledger and question register give the current precise
state of every treated row.
\end{document}
''')
(OUT/'C44_POS.tex').write_text(''.join(parts))

def normalized_type(original):
    allowed={'targeted proof check','independent re-proof','computation or formal certificate',
             'used and rechecked in this run','carried as background without fault found',
             "refuted, with the refined statement's id"}
    if original in allowed: return original
    if original == 'outage recovery and persistence': return None
    if any(word in original for word in ['arithmetic','computation','certificate']):
        return 'computation or formal certificate'
    if 'source' in original: return 'used and rechecked in this run'
    if any(word in original for word in ['proof','scope']): return 'targeted proof check'
    return original

header=['statement_id','date','who','model','effort','run','type','outcome','details']
events=[]
for name in ['work/checks/root_events.tsv','work/axis/CHECK_EVENTS.tsv','work/scan_w/check_events.tsv','work/arithmetic/CHECK_EVENTS.tsv','work/arithmetic/check_events.tsv']:
    p=ROOT/name
    if not p.exists(): continue
    with p.open(newline='') as f:
        for row in csv.DictReader(f,delimiter='\t'):
            who=row.get('who',row.get('who_model_effort_run',''))
            original_type=row.get('type','')
            kind=normalized_type(original_type)
            if kind is None: continue # Operational recovery is preserved in the raw work register and ledger.
            detail=row.get('details',row.get('locator',''))
            if kind != original_type:
                detail='Original recorded event type: '+original_type+'. '+detail
            events.append({
                'statement_id':row.get('statement_id',''),
                'date':row.get('date',''),
                'who':who,
                'model':row.get('model','GPT-6 Astra Pro'),
                'effort':row.get('effort','not exposed'),
                'run':row.get('run','C44_POS'),
                'type':kind,
                'outcome':row.get('outcome',''),
                'details':detail,
            })
with (OUT/'CHECK_EVENTS.tsv').open('w',newline='') as f:
    w=csv.DictWriter(f,fieldnames=header,delimiter='\t');w.writeheader();w.writerows(events)

manifest=[]
for name in checked+['work/covers/boundary_strata.tex','work/consolidated_th5.tex']:
    p=ROOT/name
    manifest.append({'path':name,'sha256':hashlib.sha256(p.read_bytes()).hexdigest()})
(ROOT/'work/assembly_manifest.json').write_text(json.dumps({'assembled_at':stamp.isoformat(),'parts':manifest,'events':len(events),'boundary_checked':boundary_checked},indent=2)+'\n')
print(json.dumps({'paper_bytes':(OUT/'C44_POS.tex').stat().st_size,'events':len(events),'boundary_checked':boundary_checked,'assembled_at':stamp.isoformat()}))
