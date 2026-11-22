"""Retain the actual overflow evidence, repair layout/path only, and rebuild."""
from pathlib import Path
import datetime,json,subprocess,sys
import fitz
w=Path(__file__).resolve().parents[1]
evidence=w/'outputs/checkpoint17_overflow_evidence'
assert not evidence.exists();evidence.mkdir()
doc=fitz.open(w/'RESEARCH_SA15_paper.pdf')
pages=[]
for i,page in enumerate(doc):
    if '(B-RD49.2)' in page.get_text():
        page.get_pixmap(matrix=fitz.Matrix(1.3,1.3)).save(evidence/f'page_{i+1:03d}.png')
        pages.append(i+1)
assert pages
p=w/'agents/reduction_descent/B_tame_minimal_height_two.tex'
before=p.read_text()
old=''' [p](T)=pT+c_pT^p+\\sum_{j>p}c_jT^j,\\qquad
 c_p=(1-p^{p-1})u,\\qquad
 c_j\\in(p,u)R\\ (p<j<p^2),\\qquad c_{p^2}\\in R^\\times.
                                                        \\tag{B-RD49.2}'''
new=''' \\begin{gathered}
 [p](T)=pT+c_pT^p+\\sum_{j>p}c_jT^j,\\qquad
 c_p=(1-p^{p-1})u,\\\\
 c_j\\in(p,u)R\\ (p<j<p^2),\\qquad c_{p^2}\\in R^\\times.
 \\end{gathered}
                                                        \\tag{B-RD49.2}'''
assert before.count(old)==1
after=before.replace(old,new)
after=after.replace('\\begin{remark}[Scope and exact arithmetic check]',
                    '\\begin{remark}[Scope and exact arithmetic check]\n\\label{rem:B-RD49-scope}')
assert after.count('\\label{rem:B-RD49-scope}')==1
after=after.replace('\\path{code/verify_tame_height_two_gate.py}',
                    '\\path{code/reduction_descent/verify_tame_height_two_gate.py}')
(w/'outputs/checkpoint17_before_layout_repair_B49.tex').write_text(before)
p.write_text(after)
record={'actual_utc':datetime.datetime.now(datetime.timezone.utc).isoformat(),
        'problem_pages_rendered':pages,'initial_over_2pt':1,
        'initial_new_overflow_points':7.63602,
        'changes':['Split B49.2 into two gathered lines without changing its formula.',
                   'Corrected new scope program path to its literal code/ export.',
                   'Assigned the newly introduced scope remark a stable explicit label.']}
(w/'outputs/checkpoint17_layout_repair.json').write_text(json.dumps(record,indent=2)+'\n')
print(json.dumps(record,indent=2),flush=True)
for name in ['consolidate.py','number_statements.py','build_paper.py',
             'merge_registers.py','update_current17.py']:
    subprocess.run([sys.executable,str(w/'code'/name)],check=True,cwd=w)
