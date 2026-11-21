#!/usr/bin/env python3
"""Assemble the current complete manuscript and normalized audit registers."""
from pathlib import Path
from datetime import datetime, timezone
import csv
import json
import re
import subprocess

BASE = Path(__file__).resolve().parent.parent
WORK = BASE / 'work'
OUT = BASE / 'deliverables'
OUT.mkdir(exist_ok=True)


def read_rows(path):
    with path.open(newline='') as handle:
        return list(csv.DictReader(handle, delimiter='\t'))


def write_rows(path, names, rows):
    with path.open('w', newline='') as handle:
        writer = csv.DictWriter(handle, names, delimiter='\t', lineterminator='\n')
        writer.writeheader(); writer.writerows(rows)


def main():
    now = datetime.now(timezone.utc).isoformat()
    date = now[:10]
    preamble = r'''\documentclass[11pt,a4paper]{article}
\usepackage[margin=25mm]{geometry}
\usepackage{fontspec}
\setmainfont{DejaVu Serif}
\setsansfont{DejaVu Sans}
\setmonofont[Scale=0.84]{DejaVu Sans Mono}
\usepackage{amsmath,amssymb,amsthm,mathtools,bm}
\providecommand{\llbracket}{\mathopen{[\![}}
\providecommand{\rrbracket}{\mathclose{]\!]}}
\usepackage{booktabs,longtable,array,enumitem,xcolor,graphicx}
\usepackage{microtype}
\usepackage[unicode,breaklinks=true,colorlinks=true,linkcolor=blue!45!black,urlcolor=blue!45!black]{hyperref}
\usepackage{xurl}
\providecommand{\tightlist}{\setlength{\itemsep}{0pt}\setlength{\parskip}{0pt}}
\newtheorem{proposition}{Proposition}
\newtheorem{lemma}{Lemma}
\newtheorem{theorem}{Theorem}
\newtheorem{corollary}{Corollary}
\theoremstyle{definition}\newtheorem{definition}{Definition}
\DeclareMathOperator{\im}{im}
\DeclareMathOperator{\rank}{rank}
\DeclareMathOperator{\tr}{tr}
\DeclareMathOperator{\End}{End}
\DeclareMathOperator{\Hom}{Hom}
\DeclareMathOperator{\GL}{GL}
\DeclareMathOperator{\SL}{SL}
\DeclareMathOperator{\Sym}{Sym}
\DeclareMathOperator{\Spec}{Spec}
\DeclareMathOperator{\Proj}{Proj}
\DeclareMathOperator{\diag}{diag}
\makeatletter
\renewcommand*\l@subsection{\@dottedtocline{2}{1.5em}{2.8em}}
\renewcommand*\@pnumwidth{2.5em}
\renewcommand*\@tocrmarg{3.5em}
\makeatother
\setcounter{tocdepth}{2}
\setlength{\emergencystretch}{3em}
\setlength{\parskip}{0.3em}
\title{CUE, GCT, and Isolation\\Exact bridges, restricted multiplicity formulas,\\and the remaining derandomization gates}
\author{Research run CUE\_GCT\_20261121\_R1\\GPT-6 Astra Pro; model-assisted proof review and exact computation}
\date{21 November 2026\\Working manuscript; live status in the accompanying ledger}
\begin{document}
\maketitle
\begin{abstract}
We derive exact character, Haar-integral, covariance-rank, and quotient formulas linking finite CUE moments to the multiplicities used in geometric complexity theory. Explicit restrictions and determinantal representations locate low-row exclusion ranges. A reduced determinantal-quartic divisor gives an exact shifted-plethysm difference. Algebraic permanent-image dimensions and invariant quotients produce explicit rectangular multiplicity gaps in a range of genuine padding, with a separate rectangular exclusion threshold. Graph isolation is transferred in its valid independent-variable setting and then tested against monomial descent, coefficient cancellation, joint compression, and specialization. A checked rank-profile construction yields polynomial hitting sets for width three in an unknown order and an explicit arithmetic point with trace-coordinate span recovery. Purity gives additional sparse and trace-space constructions; uniformly conditioned energy reconstruction has explicit size barriers. The stated RH and Dirichlet GRH inputs are accepted as requested, and every further analytic dependency is separately identified. General polynomial ROABP hitting sets and the asymptotic determinant-versus-padded-permanent problem remain unresolved. The separate Grothendieck part transports every finding to its precise scheme, representation-ring, filtration, or sheaf framework.
\end{abstract}
\tableofcontents\clearpage
\part{Inputs, conventions, and scope}
'''
    parts = [preamble, (WORK/'root/intro.tex').read_text(), '\n\\part{Checked findings and checked conditional reductions}\n']
    for rel in ['rectangular/findings.tex', 'root/findings.tex', 'isolation/findings.tex', 'purity/findings.tex', 'purity/zero_status.tex']:
        parts += [f'\n% BEGIN SOURCE work/{rel}\n', (WORK/rel).read_text(), f'\n% END SOURCE work/{rel}\n']
    parts += ['\n\\part{The Grothendieck restatement}\n', (WORK/'root/grothendieck.tex').read_text(),
              '\n\\part{Unchecked targets and unresolved gates}\n', (WORK/'root/open_gates.tex').read_text(),
              '\n\\appendix\n\\part{References, exact locators, and audit scope}\n']
    for name in ['rectangular', 'isolation', 'purity', 'root']:
        source = WORK / name / 'sources.md'
        if source.exists():
            # Keep internal retrieval ids in work/source registers, while the
            # manuscript references present scholarly locators and source URLs.
            md = source.read_text()
            md = re.sub(r'(?ms)^## Web retrieval references retained for root citation verification\n.*?(?=^## |\Z)', '', md)
            md = re.sub(r'(?i)Web refs?(?: inspected here)?:[^.\n]*\.', '', md)
            lines = []
            for line in md.splitlines():
                if re.search(r'turn\d+(?:view|search|fetch|academia)\d+', line):
                    if line.lstrip().startswith('- ') and 'https://' not in line and not any(x in line for x in ['Additional I-', 'Host metadata']):
                        continue
                    line = re.sub(r'(?i)Primary PDF refs?:[^.\n]*\.', '', line)
                    line = re.sub(r'; web reference.*$', '.', line)
                    line = re.sub(r'`?turn\d+(?:view|search|fetch|academia)\d+`?', '', line)
                    line = re.sub(r'\(\s*[,; ]*\)', '', line)
                    line = re.sub(r'\(\s*[,;]+\s*', '(', line)
                lines.append(line)
            md = '\n'.join(lines)
            text = subprocess.run(['pandoc', '-f', 'gfm', '-t', 'latex'], input=md, check=True,
                                  capture_output=True, text=True).stdout
            parts.append(text)
    parts.append('\n\\end{document}\n')
    manuscript = ''.join(parts)
    # Code names and paths need break opportunities in the PDF. This changes
    # presentation only, preserving the underlying characters and source files.
    def breakable_code(match):
        raw = match.group(1)
        for escaped, literal in [(r'\_', '_'), (r'\%', '%'), (r'\#', '#'), (r'\&', '&')]:
            raw = raw.replace(escaped, literal)
        if '\\' in raw or '{' in raw or '}' in raw:
            return match.group(0)
        return r'\nolinkurl{' + raw + '}'
    manuscript = re.sub(r'\\texttt\{([^{}]*)\}', breakable_code, manuscript)
    manuscript = manuscript.replace('ℓ', r'\ensuremath{\ell}')
    (OUT/'CUE_GCT.tex').write_text(manuscript)

    questions = []
    for name in ['rectangular', 'isolation', 'purity', 'root']:
        path = WORK/name/'questions.tsv'
        if not path.exists(): continue
        for row in read_rows(path):
            identifier = row.get('id') or row.get('statement_id')
            source = row.get('source_locator') or row.get('source_and_locator') or row.get('source') or row.get('evidence') or row.get('question_group') or ''
            state = row.get('state') or row.get('status') or ''
            answer = row.get('finding_or_gate') or row.get('answer') or row.get('finding_ids') or row.get('current_gate') or ''
            remaining = row.get('remaining_gate', '')
            questions.append({'id': identifier, 'source_and_locator': source, 'question': row.get('question', ''),
                              'state': state, 'finding_or_current_gate': answer + (' Remaining: '+remaining if remaining else '')})
    write_rows(OUT/'QUESTIONS.tsv', ['id','source_and_locator','question','state','finding_or_current_gate'], questions)

    events = []; seen = set()
    for path in sorted(WORK.rglob('*.tsv')):
        if 'check_events' not in path.name and not path.name.endswith('_events.tsv'): continue
        for row in read_rows(path):
            if not row.get('statement_id'): continue
            who = row.get('who') or row.get('who_model_effort_run') or ''
            raw_type = row.get('type', '')
            lower_type = raw_type.lower()
            if raw_type in ['targeted proof check', 'independent re-proof', 'computation or formal certificate',
                            'used and rechecked in this run', 'carried as background without fault found'] or lower_type.startswith('refuted'):
                event_type = raw_type
            elif any(term in lower_type for term in ['computation', 'computer check', 'symbolic example', 'certificate metadata']):
                event_type = 'computation or formal certificate'
            elif 'independent specialized derivation' in lower_type:
                event_type = 'independent re-proof'
            elif any(term in lower_type for term in ['source', 'locator', 'dependency', 'input-scope', 'provenance']):
                event_type = 'used and rechecked in this run'
            else:
                event_type = 'targeted proof check'
            record = {'statement_id': row['statement_id'], 'date': row.get('date',''), 'who_model_effort_run': who,
                      'type': event_type, 'recorded_method': raw_type, 'outcome': row.get('outcome',''), 'event_source': str(path.relative_to(BASE))}
            key = tuple(record.values())[:-1]
            if key not in seen: events.append(record); seen.add(key)
    write_rows(OUT/'CHECK_EVENTS.tsv', ['statement_id','date','who_model_effort_run','type','recorded_method','outcome','event_source'], events)
    (OUT/'BUILD_STATUS.json').write_text(json.dumps({'assembled_utc': now, 'question_rows': len(questions),
                         'check_events': len(events), 'status': 'working; unrestricted main questions unresolved'}, indent=2)+'\n')
    print(json.dumps({'assembled_utc':now,'question_rows':len(questions),'check_events':len(events),'tex':str(OUT/'CUE_GCT.tex')}))


if __name__ == '__main__': main()
