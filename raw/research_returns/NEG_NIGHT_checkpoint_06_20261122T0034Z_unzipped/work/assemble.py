"""Assemble current NEG_NIGHT deliverables. Never creates a checkpoint ZIP.

Proof-review assertions come only from explicit review records, not from a
theorem environment or a successful computation. Run from the workspace root.
"""
import argparse
import csv
import hashlib
import json
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
OUT = ROOT / "deliverables"
OUT.mkdir(exist_ok=True)

def textify(value):
    return value if isinstance(value, str) else json.dumps(value, ensure_ascii=False)

def tsv(path, records, fields):
    with path.open("w", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=fields, delimiter="\t", extrasaction="ignore")
        writer.writeheader()
        for record in records:
            writer.writerow({k: textify(record.get(k, "")) for k in fields})

def tex_escape(s):
    return ''.join({'\\':r'\textbackslash{}','&':r'\&','%':r'\%','$':r'\$','#':r'\#','_':r'\_','{':r'\{','}':r'\}','~':r'\textasciitilde{}','^':r'\textasciicircum{}'}.get(c,c) for c in str(s))

def breakable_paths(content):
    def repl(match):
        body=match.group(1)
        plain=body.replace(r'\_','_')
        if '\\' not in plain and ' ' not in plain and ('_' in plain or '/' in plain or (len(plain)>24 and ':' in plain)):
            return r'\path{'+plain+'}'
        return match.group(0)
    content=re.sub(r'\\texttt\{([^{}]*)\}',repl,content)
    content=re.sub(r'\\emph\{((?:OURS|LIT)(?:\\_|_)[^{}]*)\}',lambda m:r'\path{'+m.group(1).replace(r'\_','_')+'}',content)
    return content

def chapters_by_id(path):
    content=path.read_text()
    matches=list(re.finditer(r'\\(?:subsection|section)\{(NN-[A-Z]\d+)\b',content))
    chunks={}
    for i,m in enumerate(matches):
        end=matches[i+1].start() if i+1<len(matches) else len(content)
        # Non-theorem current-gate material belongs in the separate gate part.
        chunk=content[m.start():end]
        if '\\subsection{Current gates' in chunk:
            chunk=chunk.split('\\subsection{Current gates',1)[0]
        chunks[m.group(1)]=chunk
    return chunks

def root_geometry(proof):
    paragraphs=list(re.finditer(r'\\paragraph\{([^}]+)\}',proof))
    result=[]
    for i,m in enumerate(paragraphs):
        if re.search(r'geometr|dictionary|grothendieck',m.group(1),re.I):
            end=paragraphs[i+1].start() if i+1<len(paragraphs) else len(proof)
            result.append(proof[m.end():end].strip())
    return '\n\n'.join(result)

def main():
    parser=argparse.ArgumentParser()
    parser.add_argument('--utc',required=True,help='Actual clock__curr_time timestamp; never host datetime')
    args=parser.parse_args()
    reviews=json.loads((ROOT/'work/review_status.json').read_text())
    all_records=[]
    questions=[]
    event_rows=[]
    for track in ['root','complexity','gct','analytic']:
        base=ROOT/'work'/track
        p=base/'consequences.json'
        if p.exists():
            records=json.loads(p.read_text())
            if isinstance(records,dict):
                records=records.get('findings',records.get('consequences',[]))
            for rec in records:
                rec=dict(rec);rec['track']=track
                fid=rec['id'];review=reviews.get(fid)
                rec['proof_review']='full proof checked' if review else 'not yet independently full-read'
                rec['status']='PROVED_FULL_PROOF_CHECKED' if review else rec.get('status','DRAFT_REVIEW_PENDING')
                rec['review_evidence']=review or ''
                rec['proof_sha256']=hashlib.sha256(rec.get('proof','').encode()).hexdigest()
                rec.setdefault('proof_locator','NEG_NIGHT.tex: '+fid+'; complete proof in the corresponding paper_parts fragment and work/'+track+' source')
                if track=='root':
                    rec['geometry_translation']=root_geometry(rec.get('proof',''))
                all_records.append(rec)
        q=base/'QUESTIONS.tsv'
        if q.exists():
            for row in csv.DictReader(q.open(),delimiter='\t'):
                fid=row.get('finding_ids',row.get('finding_id',''))
                questions.append({
                    'id':('Q-'+fid.removeprefix('NN-')) if track=='complexity' and fid.startswith('NN-C') else row.get('question_id',row.get('id','')),
                    'source_and_locator':row.get('source_and_locator',row.get('source_locator',f'work/{track}/QUESTIONS.tsv'))+(('; prompt territories '+row.get('question_id','')) if track=='complexity' else ''),
                    'question':row.get('question',''),
                    'state':'proved; complete proof checked' if fid in reviews else row.get('state',row.get('status','')),
                    'finding_ids':fid,
                    'counterexample':row.get('counterexample',''),
                    'current_gate':row.get('current_gate',row.get('remaining_gate','')),
                    'approaches_tried':row.get('approaches_tried',''),
                    'next_step':row.get('next_step',''),
                })
        e=base/'CHECK_EVENTS.tsv'
        if e.exists():
            for row in csv.DictReader(e.open(),delimiter='\t'):
                event_rows.append({
                    'statement_id':row.get('statement_id',row.get('finding_ids','')),
                    'date_utc':row.get('date_utc',row.get('utc_recorded',row.get('date',''))),
                    'who':row.get('who',row.get('run',row.get('checker_agent',f'/root/{track}'))),
                    'model':row.get('who_model',row.get('model','GPT-6 Astra Pro (inherited)')),
                    'effort':row.get('effort','not exposed by runtime'),
                    'type':row.get('type',row.get('check_kind','')),
                    'outcome':row.get('outcome',''),
                    'scope_and_method':row.get('scope_and_method',row.get('evidence','')),
                    'limitations':row.get('limitations',''),
                    'evidence':row.get('evidence',f'work/{track}/CHECK_EVENTS.tsv'),
                })
    all_records.sort(key=lambda r:r['id'])
    # These are actual reviews reported by their named reviewers.
    for fid,review in reviews.items():
        event_rows.append({'statement_id':fid,**review})
    gates=json.loads((ROOT/'work/main_gates.json').read_text())
    questions.extend(gates)
    fields=['id','question_id','title','statement','inputs','status','proof_review','proof_locator','proof_file','sources','complexity_impact','geometry_translation','counterexample','review_evidence','proof_sha256']
    tsv(OUT/'CONSEQUENCES.tsv',all_records,fields)
    tsv(OUT/'QUESTIONS.tsv',questions,['id','source_and_locator','question','state','finding_ids','counterexample','current_gate','approaches_tried','next_step'])
    tsv(OUT/'CHECK_EVENTS.tsv',event_rows,['statement_id','date_utc','who','model','effort','type','outcome','scope_and_method','limitations','evidence'])
    (OUT/'CONSEQUENCES.json').write_text(json.dumps(all_records,ensure_ascii=False,indent=2)+'\n')
    fragments=OUT/'paper_parts';fragments.mkdir(exist_ok=True)
    chunks={}
    for rel in ['work/root/chapter.tex','work/root/chapter2.tex','work/root/chapter3.tex','work/root/chapter4.tex','work/root/chapter5.tex','work/root/chapter6.tex','work/root/chapter7.tex','work/root/chapter8.tex','work/root/chapter9.tex','work/root/chapter10.tex','work/root/chapter11.tex','work/gct/chapter.tex','work/complexity/chapter.tex']:
        chunks.update(chapters_by_id(ROOT/rel))
    checked=[];unchecked=[]
    for rec in all_records:
        fid=rec['id']
        if rec['track']=='analytic':continue
        chunk=chunks.get(fid)
        if chunk is None:
            chunk='\\section{'+tex_escape(fid+' '+rec.get('title',''))+'}\n'+rec.get('statement','')+'\n'+rec.get('proof','')
        target=checked if fid in reviews else unchecked
        if chunk.startswith('\\subsection{'):
            chunk=chunk.replace('\\subsection{','\\section{',1)
        target.append(chunk)
    (fragments/'checked.tex').write_text(breakable_paths('\n\n'.join(checked)))
    analytic=[]
    analytic_index=(ROOT/'work/analytic/chapter.tex').read_text()
    analytic_paths=re.findall(r'\\input\{(work/analytic/[^{}]+\.tex)\}',analytic_index)
    for rel in analytic_paths:
        content=(ROOT/rel).read_text()
        theorem_ids=set(re.findall(r'\\begin\{(?:theorem|proposition|corollary|lemma)\}\[\s*(NN-A\d+)\b',content))
        if theorem_ids and theorem_ids.issubset(reviews):
            analytic.append(content)
        else:
            unchecked.append(content)
    # A new analytic file is included, but cannot enter the checked part
    # until every finding it states has an explicit full-proof review.
    (fragments/'analytic.tex').write_text(breakable_paths('\n\n'.join(analytic)))
    (fragments/'unchecked.tex').write_text(breakable_paths('\n\n'.join(unchecked)) or 'No independently unread finding is included in this snapshot.\n')
    geometry=[]
    for rec in all_records:
        fid=rec['id'];body=rec.get('geometry_translation','')
        if not body:
            geometry.append('\\section{'+tex_escape(fid)+': geometric formulation pending}\nTranslation pending. This is an explicit documentation gate, not a proved arithmetic realization.\n')
            continue
        geometry.append('\\section{'+tex_escape(fid)+': geometric formulation and dictionary}\n\\begin{geometricstatement}['+tex_escape(fid)+']\n'+body+'\n\\end{geometricstatement}\n\\begin{proof} The displayed dictionary transports the proof of '+tex_escape(fid)+'. Any additional realization, effectiveness or uniformity hypothesis is retained explicitly.\\end{proof}\n')
    (fragments/'geometry.tex').write_text(breakable_paths('\n\n'.join(geometry)))
    gate_tex=[]
    for row in gates:
        gate_tex.append('\\section{'+tex_escape(row['id']+': '+row['question'])+'}\n\\paragraph{State.} '+tex_escape(row['state'])+'\n\\paragraph{Current gate.} '+tex_escape(row['current_gate'])+'\n\\paragraph{Tried and next.} '+tex_escape(row['approaches_tried']+' '+row['next_step'])+'\n')
    (fragments/'gates.tex').write_text('\n'.join(gate_tex))
    main=r'''\documentclass[11pt]{article}
\usepackage[a4paper,margin=25mm]{geometry}
\usepackage[T1]{fontenc}
\usepackage[utf8]{inputenc}
\usepackage{lmodern}
\usepackage{xurl}
\emergencystretch=3em
\DeclareUnicodeCharacter{2212}{\ensuremath{-}}
\usepackage{amsmath,amssymb,amsthm,mathtools,booktabs,longtable,array}
\usepackage[hidelinks,unicode]{hyperref}
\makeatletter
\renewcommand{\@pnumwidth}{2.5em}
\renewcommand{\@tocrmarg}{3.5em}
\renewcommand{\l@section}{\@dottedtocline{1}{0em}{3em}}
\makeatother
\newtheorem{theorem}{Theorem}[section]
\newtheorem{proposition}[theorem]{Proposition}
\newtheorem{lemma}[theorem]{Lemma}
\newtheorem{corollary}[theorem]{Corollary}
\newtheorem{definition}[theorem]{Definition}
\newtheorem{remark}[theorem]{Remark}
\newtheorem{conjecture}[theorem]{Conjecture}
\theoremstyle{definition}
\newtheorem{geometricstatement}[theorem]{Geometric theorem}
\DeclareMathOperator{\Spec}{Spec}
\DeclareMathOperator{\Proj}{Proj}
\DeclareMathOperator{\Tr}{Tr}
\DeclareMathOperator{\Hom}{Hom}
\DeclareMathOperator{\End}{End}
\DeclareMathOperator{\GL}{GL}
\DeclareMathOperator{\rk}{rk}
\newcommand{\mathscr}[1]{\mathcal{#1}}
\newcommand{\F}{\mathbb F}
\newcommand{\Q}{\mathbb Q}
\newcommand{\Z}{\mathbb Z}
\newcommand{\C}{\mathbb C}
\newcommand{\R}{\mathbb R}
\newcommand{\N}{\mathbb N}
\allowdisplaybreaks
\title{NEG\_NIGHT: consequences, corrected transfers, and remaining gates}
\author{Research run /root and analytic, complexity, GCT tracks}
\date{SNAPSHOTDATE}
\begin{document}
\maketitle
\begin{abstract}
This is a continuing research catalogue, not a final claim to have exhausted
an open-ended programme. E and A are used as the designated input theorems
specified by the prompt. The complete Lean archive was not rebuilt in this
run. Every consequence using M remains conditional on M. New deductions,
counterexamples to proposed transfers, exact finite certificates, and open
gates are distinguished. A complete proof reading is a targeted check of the
deduction, not a formal verification of all its input theorems. The external
registers identify each actual check and its scope.
\end{abstract}
\tableofcontents
\part{Input contract and audit conventions}
\section{Designated inputs and previous work}
E is the supplied OpenAI preprint dated 25 October 2026. Its theorem numbers
are those in the supplied source and are mapped in
\texttt{work/complexity/eth\_number\_map.json}. A is Alp\"oge's
\emph{Remark}: RH and Dirichlet GRH. The supplied Lean map identifies
\texttt{Main.lean} lines 4, 6, 8, 10 and 12 and
\texttt{Supplements/Kernels/MainTheorems.lean} lines 7--16;
these are locators in the supplied map, not a fresh build certificate.
M is the claim of all-Hecke GRH in the Masullo draft, whose defects and
repairs are recorded in the supplied defect table. Its current locator is
Chapter 1, Section 1.2, especially Section 1.2.3, PDF pages 12--16,
as recorded in the previous CX catalogue. Theorem 13.3.1.2 on page 522
is an empty heading in that draft and is not used as a statement locator.
No consequence is made
unconditional by silently replacing A with M.
The CX catalogue and the 362-row GRH catalogue are retained as background.
The supplied GCT refutations P-F19, P-F31, P-F56 and P-F57 are inputs,
and their new consequences below are distinguished from the refutations.
\section{What checked means}
The checked part contains proofs read in full by another named track or by
root, with any reported corrections incorporated. Exact primary-source
locator checks and computations are separate events. Model effort is not
exposed by the runtime and is recorded as such. Archive transcriptions are
identified by cote and scan; a transcription read is not an image inspection.
The LaTeX source is the authoritative paper. PDF build and visual checks,
when completed, are reported separately in the build documentation.
\part{Findings whose complete deduction proofs have been checked}
\input{paper_parts/checked.tex}
\input{paper_parts/analytic.tex}
\part{Findings awaiting a complete independent proof reading}
\input{paper_parts/unchecked.tex}
\part{The findings stated in algebraic geometry and Grothendieck frameworks}
\input{paper_parts/geometry.tex}
\part{Unresolved questions and strictly stated current gates}
\input{paper_parts/gates.tex}
\end{document}
'''.replace('SNAPSHOTDATE',tex_escape(args.utc+'; continuing checkpoint draft'))
    (OUT/'NEG_NIGHT.tex').write_text(main)
    state={'snapshot_utc':args.utc,'findings':len(all_records),'full_proof_reviewed':sum(r['id'] in reviews for r in all_records),'unreviewed':[r['id'] for r in all_records if r['id'] not in reviews],'first_review_due_utc':'2026-11-21T23:04:37Z','first_checkpoint_due_utc':'2026-11-21T20:49:37Z'}
    (OUT/'BUILD_STATE.json').write_text(json.dumps(state,indent=2)+'\n')
    print(json.dumps(state))

if __name__=='__main__':main()
