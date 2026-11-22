#!/usr/bin/env python3
"""Assemble ARCH_ALG deliverables; does not upload or create timed ZIPs."""
from pathlib import Path
import csv, hashlib, json, shutil
from datetime import datetime
from zoneinfo import ZoneInfo

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / 'deliverable'
OUT.mkdir(exist_ok=True)
RESEARCH = OUT / 'research'
RESEARCH.mkdir(exist_ok=True)
for src in (ROOT/'work').rglob('*'):
    if not src.is_file() or any(p in {'tex_build','__pycache__','private_transfer'} for p in src.parts):
        continue
    if src.suffix not in {'.tex','.md','.tsv','.py','.json','.txt'}:
        continue
    if src.name in {'Richardson1987.txt','check.tex'}:
        continue
    dest = RESEARCH / src.relative_to(ROOT/'work')
    dest.parent.mkdir(parents=True, exist_ok=True)
    shutil.copy2(src,dest)

modules = [
    'cote136/homotopy.tex',
    'cote136/arithmetic_improvement.tex',
    'cote136/prime_degree_agent/free_disk_support.tex',
    'cote136/prime_degree_agent/free_cell_homotopy.tex',
    'cote136/counterexample_agent/linear_prime_tail.tex',
    'cote136/counterexample_agent/massey_transport.tex',
    'cote1348/arch134_checked.tex',
    'cote1348/arch134_raw.tex',
    'cote15/cote15_core.tex',
    'cote15/cote15_ordinary_target.tex',
    'cote15/cote15_honda_check.tex',
    'cote123/companion.tex',
]
intro = r'''\documentclass[11pt,a4paper]{article}
\usepackage{fontspec}
\setmainfont{Latin Modern Roman}
\usepackage[margin=25mm]{geometry}
\usepackage{amsmath,amssymb,amsthm,mathtools,mathrsfs,booktabs,longtable,array}
\usepackage[unicode,hidelinks]{hyperref}
\usepackage{microtype}
\setlength{\emergencystretch}{3em}
\setlength{\parskip}{0.25em}
\newcommand{\Acal}{\mathcal A}
\title{ARCH\_ALG\\The archive's algebra: cotes 136, 134--8, 15 and 123}
\author{Research continuation of ALPOGE\_BRIDGES checkpoint 09}
\date{22 November 2026 --- working checkpoint}
\begin{document}
\maketitle
\begin{abstract}
This continuation distinguishes new proved statements, inherited accepted
inputs, and the questions still under active investigation. Integral
connectedness of the category of admissible divided-power de Rham theories
is not claimed. New checked reductions give a precise simplicial-homotopy
interpretation of the quoted equalization conjecture, remove the sum of
prime-dependent bounds from finite arithmetic gluing, and bound the
vertical torsion of a common free horizontal source by a number depending
only on form degree. The full tensor and interval hypotheses in cote
134--8 do not force higher coproduct surjectivity; the explicit example
nevertheless has the predicted localization. The motive sections give
geometric Chow constructions, exact mixed Tate criteria, a published-only
ordinary target, and a complete Honda--Tate check. The letter companion
includes an independent verification of the type-A normal form and a
finite orbit count. No result conditional on an outside preprint is
presented as unconditional.
\end{abstract}
\tableofcontents
\clearpage
\section*{Reading and provenance conventions}
\addcontentsline{toc}{section}{Reading and provenance conventions}
The supplied prompt and intakes designate the ALPOGE\_BRIDGES checkpoint
09 statements as inputs. An inherited statement is cited by its exact
identifier rather than silently reproved or upgraded. The event register
records separately a whole new proof check, an independent re-proof, a
computation, a rechecked inherited use, and a background citation. All
readers in this run are GPT-6 Astra Pro; the reasoning-effort setting is
not exposed and is not guessed. The actual reader role and date accompany
each event. ``Checked'' refers to the stated mathematical scope, including
every displayed hypothesis; it does not remove a Tate-conjecture gate.

The required source sheets are cote 136, physical pp.~111, 113, 115,
117, 119, 121 (footers 110--120); cote 134--8, physical pp.~48--55
(footers 47--54); cote 15, physical pp.~94--106 (footers 93--105);
and cote 123, physical pp.~22--23 (footers 21--22). Exact scan names
occur in the sections and question register. No Masullo pages or text
copies are used. A and M are not needed for the new arguments.

\part{Checked findings and checked reductions}
'''
pieces=[intro]
for mod in modules:
    if (RESEARCH/mod).exists():
        pieces.append('\\input{research/'+mod+'}\n')
pieces.append(r'''
\clearpage
\part{Open gates and unproved construction routes}
\section{The integral question remains active}
\paragraph{ARCH-136-OPEN.}
The results in the first part do not prove connectedness of
$\mathcal A_{\mathbf Z}$, terminality of its all-arrow localization,
or the integral homotopy equalization property. The strongest new
constructive reduction is ARCH-136-DISK-SUPPORT: for any finite family
there is a strict common partial source with all required horizontal
tails, exact vertical degrees zero through three, and positive
degree-$d$ cohomology annihilated by
$L_d=\operatorname{lcm}(1,\ldots,\lfloor d/2\rfloor)$, uniformly in
weight and simplex. The missing step is a compatible completion to
vertical exactness in every fixed degree while preserving one eventual
weight cutoff in that degree and in each horizontal row. The inverse
refinement obstruction and the inherited higher-completion example
exclude specified repairs, not every possible common source.

The homotopy calculation reduces the integral quoted equalization
property exactly to vanishing of the fundamental group of every
component. Together with connectedness this is terminality. These
two integral assertions remain separate. Over the semilocal rings
specified in AQ-136-SEMILOCAL they both hold.

\paragraph{Other remaining gates.}
The bare general localization theorem in cote 134--8 is not disproved
by failure of higher coproduct compatibility: the checked counterexample
still localizes correctly. The raw ordinary-$G$ counit is established
in ARCH-134-04 with its explicit finite-dimensional noetherian and
scalar-compatible interval hypotheses; the unrestricted criterion
SM25.2 remains open here. For general cubic fourfolds and finite-height
K3 surfaces, the exact displayed mixed Tate maps remain the obstruction
to the requested fixed-target forward cycles. The explicit split-cubic
and Kummer constructions have no such missing cycle. For ordinary
varieties, the selected abelian target uses published inputs, but the
mixed correspondence is still required.

\paragraph{Research notes, not promoted theorems.}
All exploratory documents are retained under \texttt{research/}.
Their candidate arguments are not assertions of this checked part
unless assigned a proved identifier and a whole-proof event in
\texttt{CHECK\_EVENTS.tsv}. \texttt{LEDGER.md} records the current gates
and the timed movement reviews. No scheduled review is recorded before
it actually takes place.

\section{Sources and exact locators}
The literature locators and dependency tags are provided alongside
each mathematical use, with fuller retrieval records in
\nolinkurl{research/cote123/SOURCES.md},
\nolinkurl{research/cote1348/CITATIONS.tsv},
\texttt{research/cote15/cote15\_sources.md}, and
\texttt{research/cote136/SOURCES.md}. The input manifest identifies the
supplied archive and prompt by SHA-256. Downloaded third-party articles
are not redistributed; their primary URLs and inspected statement
locations are recorded so that the checks can be repeated.
\end{document}
''')
(OUT/'ARCH_ALG.tex').write_text(''.join(pieces),encoding='utf-8')

# Merge heterogeneous branch registers, preserving actual event wording.
events=[]
for p in sorted((ROOT/'work').rglob('CHECK_EVENTS.tsv')):
    with p.open(newline='',encoding='utf-8') as f:
        for row in csv.DictReader(f,delimiter='\t'):
            if not row: continue
            who=row.get('who',row.get('who_model_effort_run',''))
            date=row.get('date','')
            # These date-only first-session rows were recorded after23:14UTC,
            # hence on22November in the user's Europe/Berlin timezone.
            if date=='2026-11-21':date='2026-11-22'
            events.append([row.get('statement_id',''),date,who,row.get('type',''),row.get('outcome','')])
with (OUT/'CHECK_EVENTS.tsv').open('w',newline='',encoding='utf-8') as f:
    writer=csv.writer(f,delimiter='\t'); writer.writerow(['statement_id','date','who_model_effort_run','type','outcome']); writer.writerows(events)

questions=[]
for p in sorted((ROOT/'work').rglob('QUESTIONS.tsv')):
    with p.open(newline='',encoding='utf-8') as f:
        for row in csv.DictReader(f,delimiter='\t'):
            answer=row.get('current_gate_or_answer',row.get('finding_ids_or_current_gate',row.get('answer','')))
            findings=row.get('findings',row.get('finding_ids',''))
            questions.append([row.get('id',row.get('question_id','')),row.get('source_locator',row.get('source','')),row.get('question',''),row.get('state',row.get('status','')),findings,answer])
with (OUT/'QUESTIONS.tsv').open('w',newline='',encoding='utf-8') as f:
    writer=csv.writer(f,delimiter='\t');writer.writerow(['id','source_locator','question','state','finding_ids','current_gate_or_answer']);writer.writerows(questions)

manifest={'assembled_at':datetime.now(ZoneInfo('Europe/Berlin')).isoformat(),'supplied_inputs':[],'note':'The user-supplied ZIP was extracted once. Resume from this package together with those attachments. No prior checkpoint ZIP is nested here.'}
for p in sorted((ROOT/'upload').iterdir()):
    if p.is_file():
        manifest['supplied_inputs'].append({'name':p.name,'bytes':p.stat().st_size,'sha256':hashlib.sha256(p.read_bytes()).hexdigest()})
(OUT/'INPUT_MANIFEST.json').write_text(json.dumps(manifest,indent=2),encoding='utf-8')
print(json.dumps({'paper_modules':len(modules),'check_events':len(events),'questions':len(questions),'destination':str(OUT)}))
