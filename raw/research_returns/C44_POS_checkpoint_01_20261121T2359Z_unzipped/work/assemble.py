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
axis (without a cycle-lifting assertion), explicit positive axis
subspaces, special-cover generic-stratum calculations, exact integral
arithmetic obstructions, a characteristic-$p$ detector/division theorem,
and geometric extensions of the primitive incidence polarization.
The proposed supersingular Fermat test case already satisfies the
required Hodge standard conjecture; its corrected restriction and
weighted Gysin conditions are verified explicitly.
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
 'work/axis/root_explicit_axes.tex',
 'work/covers/contribution.tex',
 'work/arithmetic/contribution.tex',
 'work/scan_w/contribution.tex',
]
boundary_checked=(ROOT/'work/checks/boundary_strata_passed.txt').exists()
if boundary_checked: checked.insert(3,'work/covers/boundary_strata.tex')
parts=[preamble]
for name in checked:
    parts += ['\n% BEGIN '+name+'\n',(ROOT/name).read_text(),'\n% END '+name+'\n']
parts.append('\n\\part{Unchecked candidates and unresolved work}\n')
if not boundary_checked:
    parts.append('The following two cover candidates are awaiting an independent whole-proof reading. They are not included among checked findings at this checkpoint.\n')
    parts.append((ROOT/'work/covers/boundary_strata.tex').read_text())
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

header=['statement_id','date','who','model','effort','run','type','outcome','details']
events=[]
for name in ['work/checks/root_events.tsv','work/axis/CHECK_EVENTS.tsv','work/scan_w/check_events.tsv','work/arithmetic/CHECK_EVENTS.tsv','work/arithmetic/check_events.tsv']:
    p=ROOT/name
    if not p.exists(): continue
    with p.open(newline='') as f:
        for row in csv.DictReader(f,delimiter='\t'):
            who=row.get('who',row.get('who_model_effort_run',''))
            events.append({
                'statement_id':row.get('statement_id',''),
                'date':row.get('date',''),
                'who':who,
                'model':row.get('model','GPT-6 Astra Pro'),
                'effort':row.get('effort','not exposed'),
                'run':row.get('run','C44_POS'),
                'type':row.get('type',''),
                'outcome':row.get('outcome',''),
                'details':row.get('details',row.get('locator','')),
            })
with (OUT/'CHECK_EVENTS.tsv').open('w',newline='') as f:
    w=csv.DictWriter(f,fieldnames=header,delimiter='\t');w.writeheader();w.writerows(events)

manifest=[]
for name in checked+['work/covers/boundary_strata.tex','work/consolidated_th5.tex']:
    p=ROOT/name
    manifest.append({'path':name,'sha256':hashlib.sha256(p.read_bytes()).hexdigest()})
(ROOT/'work/assembly_manifest.json').write_text(json.dumps({'assembled_at':stamp.isoformat(),'parts':manifest,'events':len(events),'boundary_checked':boundary_checked},indent=2)+'\n')
print(json.dumps({'paper_bytes':(OUT/'C44_POS.tex').stat().st_size,'events':len(events),'boundary_checked':boundary_checked,'assembled_at':stamp.isoformat()}))
