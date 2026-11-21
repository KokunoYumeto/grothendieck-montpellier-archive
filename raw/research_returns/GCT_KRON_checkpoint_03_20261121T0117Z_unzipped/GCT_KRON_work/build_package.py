#!/usr/bin/env python3
"""Assemble the self-contained working paper and consolidate honest ledgers."""
from pathlib import Path
import csv, json, hashlib, datetime, re

ROOT = Path(__file__).resolve().parent
def read(path): return (ROOT/path).read_text(encoding='utf-8')
def expand_inputs(text):
    return re.sub(r'\\input\{([^}]+)\}',lambda m: expand_inputs(read(m.group(1))),text)
def ids(text): return re.sub(r'\bA-?(\d{3})\b',r'A-\1',text)
def tex(s):
    return ''.join({'\\':r'\textbackslash{}','&':r'\&','%':r'\%','$':r'\$','#':r'\#','_':r'\_', '{':r'\{','}':r'\}','~':r'\textasciitilde{}','^':r'\textasciicircum{}'}.get(c,c) for c in s)

fragments = [
 ('Archive audit and the exact Burnside-to-representation passage', [
  'agents/archive/ARCHIVE_FINDINGS.tex','proofs/root_findings.tex']),
 ('Positive formulas and restricted saturation',[
  'agents/formulas/formulas.tex','agents/formulas/hooks_two_row.tex',
  'agents/archive/rectangle_square_known.tex',
  'agents/archive/POSITIVE_HW_ALGEBRA.tex','agents/archive/HEIGHT_THREE_RECTANGLES.tex',
  'agents/obstructions/obstructions_findings.tex']),
 ('Comparisons of actual orbit-closure multiplicities',[
  'proofs/projection_bound.tex','proofs/weight_box_bound.tex',
  'proofs/chow_degree_bound.tex','agents/archive/SHAPE_CHOW_BOUND.tex',
  'agents/archive/ADAPTIVE_CHOW_BOUND.tex',
  'agents/archive/OPTIMIZED_CHOW_BOUND.tex',
  'agents/archive/GROUPED_CHOW_BOUND.tex',
  'agents/formulas/further_gates.tex','agents/formulas/second_row_stabilization.tex',
  'agents/formulas/restricted_padding.tex','agents/formulas/nested_support.tex',
  'agents/formulas/mixed_tail_graph.tex',
  'agents/formulas/support_cover.tex',
  'agents/archive/JOINT_SUPPORT_COVER.tex',
  'proofs/nested_tail_bound.tex','proofs/binary_permanent_seed.tex',
  'proofs/jet_dominance.tex','proofs/general_staircase.tex',
  'proofs/cyclic_star_jets.tex','agents/formulas/permanent_jet_dominance.tex'])]

header = r'''\documentclass[11pt]{article}
\usepackage[a4paper,margin=26mm]{geometry}
\usepackage{fontspec}
\setmainfont{Latin Modern Roman}
\usepackage{amsmath,amssymb,amsthm,mathtools}
\usepackage{longtable,booktabs,array,enumitem,xurl}
\usepackage[hidelinks]{hyperref}
\usepackage{fancyhdr}
\pagestyle{fancy}\fancyhf{}\fancyhead[L]{GCT\_KRON: checked research record}\fancyhead[R]{\thepage}
\setlength{\headheight}{15pt}
\setlength{\emergencystretch}{3em}
\newtheorem{theorem}{Theorem}
\newtheorem{lemma}[theorem]{Lemma}
\newtheorem{proposition}[theorem]{Proposition}
\newtheorem{corollary}[theorem]{Corollary}
\title{Kronecker coefficients through Grothendieck's\linebreak
\(\lambda\)-operations on finite group sets}
\author{Research run GCT\_KRON\_20261120}
\date{Working paper, 21 November 2026 (Europe/Berlin)}
\begin{document}
\maketitle
\begin{abstract}
This working paper audits the supplied archive transcriptions, derives
exact formulas and restricted nonvanishing statements, and distinguishes
support positivity from comparison of actual orbit-closure multiplicities.
It corrects the subset interpretation of the Burnside operations and proves
explicit limits on several proposed positivity-to-saturation inferences.
Projection, coefficient-support and jet-dominance arguments compare every
multiplicity copy in explicit ranges. At \(n\geq m^{25}\), a remaining
actual obstruction requires at least fifty-two rows and satisfies
\(\lambda_{2j}\geq28-j\) for \(1\leq j\leq26\), as well as a
joint later-row restriction. A grouped differential refinement of the
known canonical Foulkes--Howe argument excludes every degree with
\(n\geq P_d(dm)\), where the explicit recurrence below has
\(P_d(dm)\leq\min\{(d-1)^2,\lfloor d(d+m-1)/2\rfloor\}\).
An explicit normal polynomial highest-weight algebra explains ordinary
saturation failure through its nonprimitive weight lattice. The general
higher-multiplicity comparison remains open in this run. This is a
checkpoint working paper, not a claim to have settled that comparison.
\end{abstract}

\section*{Conventions, source status, and checks}
The attached Ikenmeyer--Panova and B\"urgisser--Ikenmeyer--Panova papers
use the internal padding \(X_{11}^{n-m}\operatorname{perm}_m\).
We use that convention for \(Z_{n,m}\) and \(q^m_\lambda(d[n])\),
so their literal constants and the bound \(\ell(\lambda)\leq m^2\)
apply. The explicit determinant constructions also work with an external
padding variable, but the stated cited GCT constants are not silently
transferred between conventions. Coordinate functions carry the polynomial
\(\mathrm{GL}(V)\)-representations; forms themselves lie in
\(\operatorname{Sym}^n V^*\).

Finding identifiers label arguments and refinements established in this
run, including short dictionary versions of known results. They do not
assert historical priority. Known inputs are identified with exact work
and statement locators. The archive inputs are transcriptions, not supplied
images of manuscript pages. Conditional readings, deletions and missing
definitions are kept distinct. Full proof-reading events, source-use events
and finite computational checks are recorded separately in
\texttt{CHECK\_EVENTS.tsv}; finite experiments are not promoted to general
proofs. The model is GPT-6 Astra Pro; its reasoning-effort setting was not
exposed and is not invented. The run began at 2026-11-20 23:00:17 UTC.

The prompt stipulates Alp\"oge's RH and Dirichlet-GRH statements as
theorems. None of the arguments here uses them. The supplied four-page
\emph{Remark} was read; the named Lean files and the full scan of Lean
sources were not in the attached ZIP. No Lean verification is claimed.
No Masullo statement is used. The archive, formulas, schemes and
cohomological statements below do not depend on those analytic inputs.
\clearpage
\tableofcontents
\clearpage
'''

parts=[header]
if (ROOT/'proofs/result_overview.tex').exists():
    parts.append(read('proofs/result_overview.tex'))
for title, paths in fragments:
    parts.append('\n\\part{'+title+'}\n')
    for path in paths:
        if (ROOT/path).exists():
            text=expand_inputs(read(path))
            text=ids(text)
            parts.append('\n% BEGIN '+path+'\n'+text+'\n% END '+path+'\n')

parts.append(r'''
\part{Unresolved questions and limits of the current results}
\section{No unchecked theorem is used as a proved finding}
The remaining main problem is to compare the positive ranks in F-010
for permanent and determinant at shapes not excluded by M-008, M-009,
the permanent-size gate F-009, and the other explicit families above.
At \(n\geq m^{25}\), occurrence positivity alone does not decide that
rank comparison. This paper does not prove either a general multiplicity
obstruction or a general inequality \(q\leq K\). It does not prove a
general cancellation-free rule for rectangular Kronecker coefficients,
nor ordinary saturation beyond the stated restricted families.

The archive availability gates are also explicit: original manuscript
images were not supplied; the operators \(q_H^n\) are only named in the
secondary study; and a classification of all singular local coefficient
rings is not asserted. Proved corrections and counterexamples remain
valid under their stated interpretations.

There has not yet been a three-hour progress review. Checkpoint and final
status must follow the dated ledger, rather than an invented elapsed time.

\appendix
\section{Archive inventory}
Each row below is an assertion, definition, question, source-status issue,
or explicit scope exclusion from the supplied material. The full machine
readable version is \texttt{agents/archive/ARCHIVE\_INVENTORY.tsv}.
\small
\begin{longtable}{@{}>{\raggedright\arraybackslash}p{0.07\textwidth}>{\raggedright\arraybackslash}p{0.18\textwidth}>{\raggedright\arraybackslash}p{0.36\textwidth}>{\raggedright\arraybackslash}p{0.28\textwidth}@{}}
\toprule ID & Source and locator & Statement & State and resolution\\\midrule\endhead
''')
inv=ROOT/'agents/archive/ARCHIVE_INVENTORY.tsv'
if inv.exists():
    for row in csv.DictReader(inv.open(encoding='utf-8'),delimiter='\t'):
        cell=tex(ids(row['status']+'; '+row['resolution']+'. '+row['scope_or_uncertainty']))
        cell=cell.replace(r'A=Z\_(2)[epsilon]/(2epsilon,epsilon²)',r'\(A=\mathbb Z_{(2)}[\epsilon]/\allowbreak(2\epsilon,\epsilon^2)\)')
        parts.append(tex(row['id'])+' & '+tex(row['locator'])+' & '+tex(row['statement'])+' & '+cell+r' \\'+'\n')
parts.append(r'\bottomrule\end{longtable}\normalsize'+'\n')
parts.append(r'''
\section{Source catalog and reproducibility}
The complete exact-locator catalogs are
\path{agents/archive/SOURCE_LOCATORS.tsv},
\path{agents/formulas/SOURCE_NOTES.md}, and
\path{agents/obstructions/SOURCE_NOTES.md}. They record the supplied
LaTeX labels as well as printed statement numbers. The archive source
hash and run rules are in \texttt{RUN\_METADATA.json}. The attached
source archive was unpacked once.

The computation files use exact integers or rational arithmetic. The
character engine in \texttt{computations/independent\_characters.py}
uses Murnaghan--Nakayama independently of the family formulas, and
checks character orthogonality. The formulas worker's separate
certificates verify the generating identity as an exact integer
polynomial identity, the incidence maps, subset-sum support and the
determinant constructions. These supplement the full proofs and are
not substitutes for them. All files needed to reproduce these checks
are included; external literature is identified by exact locators
and primary URLs rather than copied as complete books.
\end{document}
''')
(ROOT/'GCT_KRON.tex').write_text(''.join(parts),encoding='utf-8')

qrows=[]
for path in sorted((ROOT/'agents').glob('*/QUESTIONS.tsv')):
    with path.open(encoding='utf-8',newline='') as h:
        for row in csv.DictReader(h,delimiter='\t'):
            qrows.append([row.get('id',''),row.get('source_and_locator',''),row.get('question',''),row.get('state',''),row.get('finding_ids_or_gate',row.get('finding_ids_or_current_gate',''))])
rootq=ROOT/'ROOT_QUESTIONS.tsv'
if rootq.exists():
    with rootq.open(encoding='utf-8',newline='') as h:
        qrows.extend(list(csv.reader(h,delimiter='\t'))[1:])
with (ROOT/'QUESTIONS.tsv').open('w',encoding='utf-8',newline='') as h:
    w=csv.writer(h,delimiter='\t');w.writerow(['id','source_and_locator','question','state','finding_ids_or_current_gate']);w.writerows([[ids(s) for s in r] for r in qrows])

events=[]
eventpaths=sorted((ROOT/'agents').glob('*/*CHECK_EVENTS.tsv'))
if (ROOT/'ROOT_CHECK_EVENTS.tsv').exists():eventpaths.append(ROOT/'ROOT_CHECK_EVENTS.tsv')
for path in eventpaths:
    with path.open(encoding='utf-8',newline='') as h:
        reader=csv.reader(h,delimiter='\t');next(reader,None)
        for row in reader:
            if len(row)==6: events.append(row)
            elif len(row)==5:
                events.append([row[0],row[1],row[2],row[3],'Method and outcome recorded together in original agent ledger',row[4]])
            elif len(row)==9:
                events.append([row[0],row[1],'; '.join([row[5],row[2],'effort '+row[3],row[4]]),row[6],row[8],row[7]])
            elif row: raise ValueError(f'Unexpected event columns in {path}: {row}')
with (ROOT/'CHECK_EVENTS.tsv').open('w',encoding='utf-8',newline='') as h:
    w=csv.writer(h,delimiter='\t');w.writerow(['statement_id','date_utc','who_model_effort_run','type','method','outcome']);w.writerows([[ids(s) for s in r] for r in events])

print(json.dumps({'paper_bytes':(ROOT/'GCT_KRON.tex').stat().st_size,'questions':len(qrows),'check_events':len(events),'built_utc':datetime.datetime.now(datetime.timezone.utc).isoformat()}))
