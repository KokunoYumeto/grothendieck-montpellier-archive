"""Retain actual first-build evidence and wrap two overwide displays only."""
from pathlib import Path
import shutil,json,datetime,difflib
w=Path(__file__).resolve().parents[1]
folder=w/'outputs/checkpoint37_build_attempt01'
shutil.copy2(w/'RESEARCH_SA15_paper.pdf',folder/'RESEARCH_SA15_paper.pdf')
(w/'outputs/qa37').rename(folder/'qa37_unreviewed')
(w/'outputs/visual_qa37_pending.json').rename(folder/'visual_qa37_unreviewed.json')
p=w/'code/consolidate.py';old=p.read_text()
(folder/'consolidate_before_layout_repair.py').write_text(old)
addition=r'''
# CP37: two source-neutral display wraps; canonical mathematical files stay frozen.
q=s/'A_monodromy.tex'; t=q.read_text()
old=' V=\\{O\\}\\times E,\\qquad H=E\\times\\{O\\},\\qquad\n \\Gamma=\\{(a,b):a+b=O\\},\\qquad\n L_m=\\mathcal O_A(mV+H+\\Gamma)\\quad(m\\ge1).'
new='\\begin{gathered}\n V=\\{O\\}\\times E,\\qquad H=E\\times\\{O\\},\\qquad\\Gamma=\\{(a,b):a+b=O\\},\\\\\n L_m=\\mathcal O_A(mV+H+\\Gamma)\\quad(m\\ge1).\n\\end{gathered}'
assert t.count(old)==1, 'CP37 EDC1 expected display not found'
q.write_text(t.replace(old,new))
q=s/'B.tex'; t=q.read_text()
old=' Y_0=X^A,\\qquad\n Y_1=[p]_{X^b}(Y_0),\\qquad\n Y_2=[p]_{X^b}(Y_1),\\qquad\n P(X)=\\Phi_{X^b}(Y_2),\\quad \\Phi_u(T)=[p]_u(T)/T .'
new='\\begin{gathered}\n Y_0=X^A,\\qquad Y_1=[p]_{X^b}(Y_0),\\qquad Y_2=[p]_{X^b}(Y_1),\\\\\n P(X)=\\Phi_{X^b}(Y_2),\\qquad \\Phi_u(T)=[p]_u(T)/T .\n\\end{gathered}'
assert t.count(old)==1, 'CP37 B100.4 expected display not found'
q.write_text(t.replace(old,new))
'''
# Raw controller text above uses double escapes for the Python literals written out.
addition=addition.replace('\\\\','\\')
new=old+addition;p.write_text(new)
(folder/'layout_repair.diff').write_text(''.join(difflib.unified_diff(old.splitlines(True),new.splitlines(True),fromfile='first-build consolidation',tofile='display-wrapped consolidation')))
record={'actual_utc':datetime.datetime.now(datetime.timezone.utc).isoformat(),'status':'LAYOUT REPAIR ONLY','first_build_over_2pt':[24.44771,7.08499],'canonical_files_unchanged':True,'retained_first_pdf_and_unreviewed_renders':str(folder.relative_to(w)),'scope':'Two line breaks with gathered wrappers; no mathematics altered and no prior image inspection claimed.'}
(w/'outputs/checkpoint37_layout_repair.json').write_text(json.dumps(record,indent=2)+'\n')
with (w/'notes/checkpoint37_changes.md').open('a') as f:
 f.write('\n## First-build layout correction\n\nThe first actual build completed in87.888seconds and produced810pages. Its log found two displays wider than the target by24.44771pt and7.08499pt. Their lines were split in the consolidation formatter; all canonical mathematical files stayed unchanged. The first PDF, every actual build input/log and the unreviewed first render set are retained. No inspection of those obsolete images is claimed. Two smaller paragraph overflows,0.41342pt and1.56165pt, are below the2pt threshold and are included in the final page review.\n')
print(json.dumps(record,indent=2))
