"""Correct generated formatter escaping before executing its first integration."""
from pathlib import Path
import datetime,json,difflib
w=Path(__file__).resolve().parents[1];p=w/'code/consolidate.py'
old=p.read_text();(w/'outputs/checkpoint37_build_attempt01/consolidate_generated_escape_prior.py').write_text(old)
marker='# CP37: two source-neutral display wraps; canonical mathematical files stay frozen.'
head=old.split(marker)[0]
pairs=[('A_monodromy.tex',r''' V=\{O\}\times E,\qquad H=E\times\{O\},\qquad
 \Gamma=\{(a,b):a+b=O\},\qquad
 L_m=\mathcal O_A(mV+H+\Gamma)\quad(m\ge1).''',r'''\begin{gathered}
 V=\{O\}\times E,\qquad H=E\times\{O\},\qquad\Gamma=\{(a,b):a+b=O\},\\
 L_m=\mathcal O_A(mV+H+\Gamma)\quad(m\ge1).
\end{gathered}'''),('B.tex',r''' Y_0=X^A,\qquad
 Y_1=[p]_{X^b}(Y_0),\qquad
 Y_2=[p]_{X^b}(Y_1),\qquad
 P(X)=\Phi_{X^b}(Y_2),\quad \Phi_u(T)=[p]_u(T)/T .''',r'''\begin{gathered}
 Y_0=X^A,\qquad Y_1=[p]_{X^b}(Y_0),\qquad Y_2=[p]_{X^b}(Y_1),\\
 P(X)=\Phi_{X^b}(Y_2),\qquad \Phi_u(T)=[p]_u(T)/T .
\end{gathered}''')]
text=head+marker+'\n'
for name,before,after in pairs:
 assert (w/'sections'/name).read_text().count(before)==1
 text+=f'q=s/{name!r}; t=q.read_text()\nold={before!r}\nnew={after!r}\nassert t.count(old)==1, "CP37 expected display not found"\nq.write_text(t.replace(old,new))\n'
p.write_text(text)
(w/'outputs/checkpoint37_build_attempt01/formatter_escape_correction.diff').write_text(''.join(difflib.unified_diff(old.splitlines(True),text.splitlines(True))))
print(json.dumps({'actual_utc':datetime.datetime.now(datetime.timezone.utc).isoformat(),'status':'Generated Python literal escaping corrected before execution; no mathematical or compilation failure','canonical_files_changed':False}))
