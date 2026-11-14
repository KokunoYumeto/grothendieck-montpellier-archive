#!/usr/bin/env python3
"""Exercise deferred notes and the actual three-line marginal-note boundary.

The temporary diagnostic PDF remains outside the edition. Its sanitized log and
measured outcome document the reusable renderer, not a source-page reading.
"""
import argparse,hashlib,json,pathlib,subprocess
import fitz
from bootstrap_tex import tex_env
from build_edition import make_document,get_metadata
from compile_readers import parse_log,sanitized

BODY=r'''
\noindent Circled annotation: \textcolor{HandInk}{\textcircled{17}}. Typed call with handwritten oval: \handcircle{(*).}\par\bigskip
\def\CurrentPageKey{probe-three}
\noindent Three-line note.\margin{first\\second\\third\tnote{PROBE-SHORT}{Short marginal translator note retained.}}
\par\vspace{60pt}
\def\CurrentPageKey{probe-four}
\noindent Four-line note.\margin{first\\second\\third\\fourth}
\par\bigskip
{\uline{Grouped translator marker\tnote{PROBE-TN}{Grouped translator note retained.} within underlining.}}
\par\bigskip
{\textit{Grouped copy marker\copytwo{PROBE-C2}{Grouped copy-two note retained.} within italics.}}
\par\bigskip
\def\CurrentPageKey{probe-four-with-note}
\noindent Four-line note with a nested marker.\margin{first\\second\\third\\fourth\tnote{PROBE-LONG}{Long marginal translator note occurs once.}}
\finishscan
\typeout{EDITION-APPARATUS-COUNT: \theappnote}
\end{document}
'''

def run(root):
    runtime=root.parent/'tex-runtime';scratch=root.parent/'build/rendering-probe';scratch.mkdir(parents=True,exist_ok=True)
    doc=make_document(root,'EN_corrected_translator_notes',{}, {},[], '')
    doc=doc.split(r'\begin{document}',1)[0]+r'\begin{document}'+BODY
    path=scratch/'rendering-probe.tex';path.write_text(doc);runs=[]
    env=tex_env(runtime);env['max_print_line']='10000'
    for n in range(3):
        process=subprocess.run(['lualatex','-interaction=nonstopmode','-halt-on-error','-file-line-error',path.name],cwd=scratch,env=env,capture_output=True,text=True);runs.append(process.returncode)
        if process.returncode:break
    log=(scratch/'rendering-probe.log').read_text(errors='replace');result=parse_log(log,doc);result.update(runs=runs,source_sha256=hashlib.sha256(doc.encode()).hexdigest())
    if not process.returncode:
        pdf=fitz.open(scratch/'rendering-probe.pdf');text='\n'.join(p.get_text() for p in pdf)
        phrases=['Short marginal translator note retained.','Grouped translator note retained.','Grouped copy-two note retained.','Long marginal translator note occurs once.']
        result['note_text_occurrences']={phrase:text.count(phrase) for phrase in phrases}
        result['expected_marginal_placements']=[{'key':'probe-three','placement':'margin','lines':3},{'key':'probe-four','placement':'block','lines':4},{'key':'probe-four-with-note','placement':'block','lines':4}]
        observed=[{k:r[k] for k in ['key','placement','lines']} for r in result['marginal_note_placements']]
        result['printed_block_labels']=text.count('Marginal note:')
        result['passed']=not result['errors'] and not result['missing_characters'] and observed==result['expected_marginal_placements'] and all(n==1 for n in result['note_text_occurrences'].values()) and result['executed_apparatus_entries']==4 and len(result['printed_apparatus_entries'])==4 and result['printed_block_labels']==2
        for i,page in enumerate(pdf):page.get_pixmap(matrix=fitz.Matrix(1.5,1.5)).save(scratch/f'page_{i+1:03d}.png')
    else:result['passed']=False
    current=root/'records/RENDERING_PROBE.json';history=root/'records/RENDERING_PROBE_HISTORY.jsonl'
    records=[json.loads(line) for line in history.read_text().splitlines()] if history.exists() else []
    for item in ([json.loads(current.read_text())] if current.exists() else [])+[result]:
        if not any(x.get('source_sha256')==item.get('source_sha256') for x in records):records.append(item)
    history.write_text(''.join(json.dumps(x,ensure_ascii=False)+'\n' for x in records))
    current.write_text(json.dumps(result,ensure_ascii=False,indent=2)+'\n')
    (root/'build_logs/RENDERING_PROBE.log').write_text(sanitized(log,root.resolve(),runtime.resolve()))
    return result

if __name__=='__main__':
    p=argparse.ArgumentParser();p.add_argument('--root',type=pathlib.Path,default=pathlib.Path(__file__).resolve().parents[1]);a=p.parse_args();result=run(a.root.resolve());print(json.dumps(result,ensure_ascii=False,indent=2));raise SystemExit(0 if result['passed'] else 1)
