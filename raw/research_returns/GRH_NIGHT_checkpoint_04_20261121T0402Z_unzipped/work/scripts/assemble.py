#!/usr/bin/env python3
"""Assemble the living GRH_NIGHT deliverables, without making a checkpoint ZIP.

Run from the task workspace: python work/scripts/assemble.py
Pass --final only for the closing package; this labels remaining gates explicitly.
"""
from pathlib import Path
from datetime import datetime, timezone
from zoneinfo import ZoneInfo
import argparse, csv, json, re, shutil, hashlib

parser = argparse.ArgumentParser()
parser.add_argument('--final', action='store_true')
args = parser.parse_args()
ROOT = Path(__file__).resolve().parents[2]
WORK = ROOT / 'work'
OUT = ROOT / 'deliverable'
OUT.mkdir(exist_ok=True)
DOMAINS = ['number_theory', 'geometry_programme', 'complexity', 'root']
now = datetime.now(timezone.utc)
berlin = now.astimezone(ZoneInfo('Europe/Berlin'))
metadata = json.loads((WORK / 'RUN_METADATA.json').read_text())
started = datetime.fromisoformat(metadata['started_utc'].replace('Z', '+00:00'))
elapsed = (now - started).total_seconds() / 3600
status = 'INCOMPLETE: remaining research gates are recorded' if args.final else 'IN PROGRESS'

def read_json(path, fallback):
    return json.loads(path.read_text()) if path.exists() else fallback

def read_tsv(path):
    if not path.exists(): return []
    with path.open(newline='') as f:
        return list(csv.DictReader(f, delimiter='\t'))

def clean(x):
    if x is None: return ''
    if isinstance(x, (dict, list)): x = json.dumps(x, ensure_ascii=False)
    return re.sub(r'[\t\r\n]+', ' ', str(x)).strip()

def write_tsv(path, rows, fields):
    with path.open('w', newline='') as f:
        w = csv.DictWriter(f, fieldnames=fields, delimiter='\t', extrasaction='ignore')
        w.writeheader()
        for row in rows: w.writerow({k: clean(row.get(k, '')) for k in fields})

fields = ['id', 'statement', 'input', 'status', 'where_the_proof_is', 'where_it_lives']
rows, questions, events, sources, counts = [], [], [], [], {}
for domain in DOMAINS:
    d = WORK / domain
    rr = read_json(d / 'rows.json', [])
    if isinstance(rr, dict): rr = rr.get('rows', [])
    counts[domain] = len(rr)
    for row in rr:
        missing = set(fields) - set(row)
        if missing: raise ValueError((domain, row.get('id'), missing))
    rows.extend(rr)
    for q in read_tsv(d / 'questions.tsv'):
        q['_domain'] = domain
        questions.append(q)
    events.extend(read_tsv(d / 'events.tsv'))
    ss = read_json(d / 'sources.json', [])
    if isinstance(ss, dict):
        ss = [dict(value, id=key) if isinstance(value, dict) else {'id':key, 'title':value}
              for key, value in ss.items()]
    for s in ss:
        s['_domain'] = domain
        s['locator'] = s.get('locator') or s.get('locators') or ''
        s['inspection'] = s.get('inspection') or s.get('verification_scope') or ''
        s['web_refs'] = s.get('web_refs') or s.get('retrieval_refs') or []
        sources.append(s)

ids = [r['id'] for r in rows]
if len(ids) != len(set(ids)): raise ValueError('Duplicate consequence IDs')
events.extend(read_tsv(WORK / 'checks' / 'root_peer_reviews.tsv'))
events.extend(read_tsv(WORK / 'checks' / 'source_events.tsv'))
events.sort(key=lambda r: (r.get('date', ''), r.get('statement_id', '')))
write_tsv(OUT / 'CONSEQUENCES.tsv', rows, fields)
write_tsv(OUT / 'QUESTIONS.tsv', questions,
          ['id', 'source_and_locator', 'question', 'state'])
write_tsv(OUT / 'CHECK_EVENTS.tsv', events,
          ['statement_id', 'date', 'who', 'model', 'effort', 'run', 'type', 'outcome'])
write_tsv(OUT / 'BIBLIOGRAPHY.tsv', sources,
          ['_domain', 'id', 'title', 'locator', 'url', 'inspection', 'web_refs'])

def esc(s):
    m = {'\\':r'\textbackslash{}','&':r'\&','%':r'\%','$':r'\$',
         '#':r'\#','_':r'\_','{':r'\{','}':r'\}','~':r'\textasciitilde{}',
         '^':r'\textasciicircum{}'}
    math_chars = {'ζ':r'\zeta','ℓ':r'\ell','λ':r'\lambda','π':r'\pi',
                  'μ':r'\mu','η':r'\eta','θ':r'\theta','β':r'\beta',
                  'α':r'\alpha','γ':r'\gamma','Δ':r'\Delta','Σ':r'\Sigma',
                  'ψ':r'\psi','χ':r'\chi','φ':r'\varphi','ε':r'\epsilon',
                  'ρ':r'\rho','δ':r'\delta','↦':r'\mapsto',
                  '′':r'{}^{\prime}',
                  '≤':r'\le','≥':r'\ge','≠':r'\ne','∈':r'\in',
                  '∤':r'\nmid','⊂':r'\subset','⊆':r'\subseteq','∞':r'\infty',
                  '√':r'\surd','⊗':r'\otimes','±':r'\pm','−':'-'}
    m.update({c:r'\ensuremath{'+v+'}' for c,v in math_chars.items()})
    m.update({'.':r'.\allowbreak{}','/':r'/\allowbreak{}',
              '_':r'\_\allowbreak{}','–':r'–\allowbreak{}',':':r':\allowbreak{}'})
    return ''.join(m.get(c,c) for c in clean(s))

preamble = r'''\documentclass[11pt,a4paper]{article}
\usepackage[margin=25mm]{geometry}
\usepackage{fontspec}
\setmainfont[BoldFont=lmroman10-bold.otf,ItalicFont=lmroman10-italic.otf,
 BoldItalicFont=lmroman10-bolditalic.otf]{lmroman10-regular.otf}
\setsansfont{lmsans10-regular.otf}
\setmonofont[Scale=0.87]{lmmono10-regular.otf}
\usepackage{amsmath,amssymb,amsthm,mathtools,mathrsfs}
\usepackage{booktabs,longtable,array,enumitem,microtype}
\usepackage{xcolor}
\definecolor{inkblue}{HTML}{173B52}
\usepackage[colorlinks=true,linkcolor=inkblue,urlcolor=inkblue]{hyperref}
\usepackage{xurl}
\usepackage{bookmark}
\usepackage{fancyhdr}
\pagestyle{fancy}\fancyhf{}
\fancyhead[L]{\small GRH\_NIGHT: consequences and proof gates}
\fancyfoot[C]{\thepage}
\setlength{\headheight}{14pt}
\setlength{\emergencystretch}{3em}
\setlist{nosep}
\newtheorem{proposition}{Proposition}
\newcommand{\A}{A_D}
\newcommand{\M}{M_H}
\title{\textbf{GRH\_NIGHT}\\Consequences, methods, and the Grothendieck programme}
\author{GPT-6 Astra Pro research run\\Model effort setting not exposed}
'''
tex = [preamble, '\\date{'+esc(berlin.strftime('%d %B %Y, %H:%M %Z'))+'}\n',
       '\\begin{document}\n\\maketitle\n',
       '\\begin{abstract}\n',
       esc(f'This finite catalogue records {len(rows)} consequences, refinements, counterexamples and explicit gates. '),
       r'The input $A_D$ is the Alp\"oge RH/Dirichlet-GRH theorem designated in the task. '
       r'The input $M_H$ is Masullo\textquotesingle s claimed universal unitary-Hecke GRH and is always conditional. '
       r'Classical proofs are located rather than reproduced; new formulations receive complete proofs. '
       r'``Proved here'' means established in this run, not a claim of publication novelty. '
       r'The source formalization was not rebuilt. The full 940-page draft was not certified. '
       r'Explicit source errors are distinguished from the conditional endpoint assumption. ',
       esc(status)+'.\n\\end{abstract}\n\\tableofcontents\n\\newpage\n',
       r'''\section*{How to read the evidence}
\addcontentsline{toc}{section}{How to read the evidence}
The six-column \texttt{CONSEQUENCES.tsv} is the authoritative statement and
dependency catalogue. \texttt{QUESTIONS.tsv} records the state of every
question treated. \texttt{CHECK\_EVENTS.tsv} records actual check events,
including who performed them and whether a proof was read, independently
derived, checked by a finite computation, or carried from the supplied
record. A citation verified at the statement level is not a claim that the
whole classical proof was rechecked. All new proof texts in the final
checked part have a complete-reading event; computational examples are
not substituted for a general proof.

All critical-line assertions concern the stated nontrivial divisor, with
Tate shifts, trivial zeros, poles and omitted Euler factors handled as
specified. A signed Brauer factorization gives zero/pole locations; it
does not supply the nonnegative divisor orders required by Artin
holomorphy. The notation $A$, $A_D$ refers to the same adopted theorem,
and $M$, $M_H$ to the same conditional draft claim.

The original prompt asks for an open-ended exhaustive investigation.
This is a finite research record. Unresolved conjectures and unavailable
proofs are displayed as such rather than given invented resolutions.
Archive locators distinguish PDF page, repository footer and manuscript
numbering where they differ. The old papers absent from the supplied ZIP
are cited through their attached return records, without a claim of fresh
whole-proof verification.

\part{Checked findings and located consequences}
''']
for domain in DOMAINS:
    p = WORK / domain / 'section.tex'
    if p.exists(): tex.extend(['\n% BEGIN '+domain+'\n', p.read_text(), '\n% END '+domain+'\n'])

tex.append(r'''\part{Unchecked claims and unresolved gates}
The complete proofs above establish only their stated implications.
The rows below are retained as research gates or as carried claims whose
complete source proofs were unavailable. They are not additional theorems.
The manuscript faults MT-M01 and MT-M02 have proved counterexamples;
the associated repairs do not certify every downstream operator or trace.
''')
gates=[]
for q in questions:
    text = (q.get('state','')+' '+q.get('question','')).lower()
    if any(w in text for w in ['open','gate','unresolved','unchecked','not treated','incomplete']): gates.append(q)
for q in gates:
    tex.extend(['\n\\paragraph{'+esc(q.get('id',''))+'} ',esc(q.get('question','')), '\n\n',
                '\\textbf{State:} '+esc(q.get('state','')), '\n\n',
                '\\textbf{Source:} '+esc(q.get('source_and_locator',''))+'.\n'])
tex.append(r'''\section*{Statement index}
\addcontentsline{toc}{section}{Statement index}
The complete statement, exact input, proof location and work placement for
every ID below is recorded in \texttt{CONSEQUENCES.tsv}. This index keeps
the paper navigable without duplicating the entire machine-readable table.
''')
for domain in DOMAINS:
    dr=read_json(WORK/domain/'rows.json',[])
    if isinstance(dr,dict): dr=dr.get('rows',[])
    tex.append('\\paragraph{'+esc(domain.replace('_',' '))+'} '+', '.join(esc(r['id']) for r in dr)+'.\n')
tex.append(r'''\section*{Source registry and exact locators}
\addcontentsline{toc}{section}{Source registry and exact locators}
The inspection descriptions below record their actual scope. A located
classical theorem is not labelled as a fresh whole-proof audit unless
its event explicitly records that reading.
''')
for s in sources:
    tex.extend(['\n\\paragraph{'+esc(s.get('id',''))+'} ',esc(s.get('title','')),'.\n\n',
                '\\textbf{Locator:} '+esc(s.get('locator','')),'.\n\n',
                '\\textbf{Inspection:} '+esc(s.get('inspection','')), '\n\n'])
    if s.get('url'): tex.append(r'\url{'+str(s['url'])+'}.\n')
tex.append('\n\\end{document}\n')
paper = ''.join(tex)
paper = re.sub(r'\\texttt\{([^{}]*)\}',
               lambda m: r'\path{' + m.group(1).replace(r'\_', '_') + '}', paper)
(OUT/'GRH_NIGHT.tex').write_text(paper)

ledger=[f'# GRH_NIGHT ledger\n\nStatus: **{status}**.\n\n',
        f'Run began {started.isoformat()}. Snapshot {now.isoformat()} '
        f'({berlin.strftime("%d %B %Y %H:%M %Z")}); elapsed {elapsed:.2f} hours.\n\n',
        f'Catalogue: {len(rows)} rows; questions: {len(questions)}; check events: {len(events)}.\n\n',
        '## Inputs and check discipline\n\n',
        'A_D is used as the user-designated cited theorem. M_H remains a conditional claim. '
        'Missing imported Lean dependencies were not kernel-checked. '
        'A proof-check event states exactly the work performed; reading a source statement is not a full-proof audit.\n\n',
        '## Progress reviews and checkpoints\n\n',
        'The first movement review is due at three hours, and then hourly. '
        'No review is reported before it occurs. Checkpoint ZIPs are made only at 45-minute work intervals, '
        'never include earlier checkpoint ZIPs, and are never overwritten.\n\n']
if elapsed<3: ledger.append('The first three-hour review is not yet due at this snapshot.\n\n')
history=WORK/'root'/'ledger_history.md'
if history.exists(): ledger.extend([history.read_text(),'\n\n'])
ledger.append('## Current question states\n\n| ID | State and strongest gate | Source |\n|---|---|---|\n')
for q in questions:
    ledger.append('| '+ ' | '.join(clean(q.get(k,'')).replace('|','\\|') for k in ['id','state','source_and_locator'])+' |\n')
ledger.append('\n## Domain research notes\n\n')
for domain in DOMAINS:
    notes=WORK/domain/'notes.md'
    if notes.exists(): ledger.extend(['\n### '+domain.replace('_',' ')+'\n\n',notes.read_text(),'\n'])
(OUT/'LEDGER.md').write_text(''.join(ledger))

imp=WORK/'root'/'implications.md'
if imp.exists(): (OUT/'IMPLICATIONS.md').write_text(imp.read_text())
else: (OUT/'IMPLICATIONS.md').write_text('# Implications\n\nThe detailed implications are organized by domain in GRH_NIGHT.tex. This narrative is in progress.\n')

readme=f'''# GRH_NIGHT

**Status: {status}.**

Start with `CONSEQUENCES.tsv` for the full catalogue and `GRH_NIGHT.pdf` (when present)
or `GRH_NIGHT.tex` for the paper. `IMPLICATIONS.md` explains programme changes.
`QUESTIONS.tsv`, `LEDGER.md`, and `CHECK_EVENTS.tsv` preserve the research state.
`BIBLIOGRAPHY.tsv` records precise literature locators and the actual source inspection.

There are {len(rows)} catalogue rows, {len(questions)} question rows, and {len(events)} check events.
The paper distinguishes cited A_D from conditional M_H and from independent classical inputs.
The working papers and computation certificates are retained under `work/` and `checks/`.

No externally retrieved full copyrighted literature is redistributed. Its URLs and locators are retained.
The original supplied archive remains the source for attached background files; `INPUTS.tsv` records its contents and hashes.
'''
(OUT/'README.md').write_text(readme)
(OUT/'RESUME.md').write_text(f'''# Resume this research

Snapshot: {now.isoformat()}.
Read the attached original prompt, README.md, LEDGER.md, and CONSEQUENCES.tsv first.
Use the original user-supplied source archive, checking INPUTS.tsv hashes. In a fresh environment,
unpack that archive once into `sources/`; do not repeatedly unpack it over edited material.
The domain drafts in `work/` are the source for the paper and registers.
Run `python work/scripts/assemble.py` from the extracted package to rebuild the root deliverables.
The script writes `deliverable/`; compile its GRH_NIGHT.tex with XeLaTeX twice.

Preserve all earlier checkpoint ZIPs. Continue its numbering from the saved checkpoint register.
Do not create extra checkpoint ZIPs between the specified 45-minute intervals.
At the three-hour and subsequent hourly reviews count only a status change or a strictly smaller main gate as movement.
Every next research step must retain exact hypotheses, primary theorem/page locators, and truthful check events.

The main unresolved gates are individually listed in QUESTIONS.tsv. In particular, do not present full GUE,
general Artin holomorphy, non-CM GL2 GRH, integral K-theory vanishing, or general derandomization
as consequences already proved in this package.
''')
write_tsv(OUT/'INPUTS.tsv', metadata['files'], ['name','bytes','sha256'])
(OUT/'RUN_METADATA.json').write_text(json.dumps(dict(metadata,snapshot_utc=now.isoformat(),status=status,counts=counts),indent=2)+'\n')
print(json.dumps({'output':str(OUT),'rows':len(rows),'questions':len(questions),'events':len(events),
                  'counts':counts,'elapsed_hours':round(elapsed,3),'status':status},indent=2))
