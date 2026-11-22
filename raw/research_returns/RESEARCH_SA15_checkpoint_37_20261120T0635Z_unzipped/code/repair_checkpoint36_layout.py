"""Preserve CP36 attempt1 and apply source-neutral display/date formatting fixes."""
from pathlib import Path
import datetime,difflib,hashlib,json,shutil
w=Path(__file__).resolve().parents[1]
folder=w/'notes/CP36_layout_repair';assert not folder.exists();folder.mkdir()
conso=w/'code/consolidate.py';bib=w/'agents/obstructions_crystals/D_E_references.bib'
originals={p:p.read_text() for p in [conso,bib]}
for p in originals:shutil.copy2(p,folder/(p.name+'.before'))
for suffix in ['aux','bbl','blg','pdf']:
 p=w/('RESEARCH_SA15_paper.'+suffix)
 if p.exists():shutil.copy2(p,folder/p.name)
b=originals[bib];needle='  author = {Kleiman, Steven L.},\n  title = {The Picard Scheme},'
assert b.count(needle)==1
bib.write_text(b.replace(needle,'  author = {Kleiman, Steven L.},\n  year = {n.d.},\n  title = {The Picard Scheme},'))
replacements=[
 (r''' E_h=L(P),\qquad S=R_oE_h,\qquad T=R_oL(P^+),
 \qquad [E_h:L]=25,\quad[S:L]=125,\quad[T:L]=3125,''',r'''\begin{gathered}
 E_h=L(P),\qquad S=R_oE_h,\qquad T=R_oL(P^+),\\
 [E_h:L]=25,\quad[S:L]=125,\quad[T:L]=3125,
\end{gathered}'''),
 (r''' v_T(gP_i^+-P_i^+)=D_{1,i}\quad(0\ne g\in H_T),\qquad
 v_T(gP_i^+-P_i^+)=D_{0,i}\quad(g\notin H_T),\qquad
 v_T(5)=1500000.''',r''' v_T(gP_i^+-P_i^+)=D_{1,i}\quad(0\ne g\in H_T),\\
 v_T(gP_i^+-P_i^+)=D_{0,i}\quad(g\notin H_T),\\
 v_T(5)=1500000.'''),
 (r''' c_1=N(p-1)=\text{last upper break of }F_2/L,\qquad
 c_2=(q^2-1)(p-1),\qquad
 \text{last upper break of }F_3/F_2\le p^{r_1-2}c_2.''',r''' c_1=N(p-1)=\text{last upper break of }F_2/L,\\
 c_2=(q^2-1)(p-1),\\
 \text{last upper break of }F_3/F_2\le p^{r_1-2}c_2.''')]
block='\n# CP36: source-neutral display wrapping; exact canonical formulas are unchanged.\n'
block+="q=s/'B.tex'; t=q.read_text()\n"
for old,new in replacements:
 block+='old='+repr(old)+'\nnew='+repr(new)+'\n'
 block+="assert t.count(old)==1, 'CP36 expected display not found'\nt=t.replace(old,new)\n"
block+='q.write_text(t)\n'
needle="print('Integrated four sections and',len(seen),'bibliography records')"
assert originals[conso].count(needle)==1
conso.write_text(originals[conso].replace(needle,block+'\n'+needle))
for p,old in originals.items():
 (folder/(p.name+'.diff')).write_text(''.join(difflib.unified_diff(old.splitlines(True),p.read_text().splitlines(True),fromfile='before',tofile='after')))
# The failed auxiliary file forces numerical citations before the new BibTeX run.
# Its exact bytes have been preserved above and in build attempt1.
(w/'RESEARCH_SA15_paper.aux').unlink()
r={'actual_utc':datetime.datetime.now(datetime.timezone.utc).isoformat(),
 'failed_attempt':'outputs/checkpoint36_build_attempt01',
 'failure':'The undated Kleiman bibliography entry had an empty year, which makes this author-year natbib style emit NAT@force@numbers and fail. Use explicit n.d., not an invented publication year.',
 'display_fixes':['B-RD96.1 fields and degrees split into two lines','B-RD96.2 two displacement cases and v_T(5) split into three lines','B-RD98.10 the two point conductors and terminal bound split into three lines'],
 'failed_log_overflows_gt2pt':[28.93817,28.92967,80.85048],
 'canonical_mathematics_unchanged':True,
 'preserved':'Full failed actual log/input snapshot plus additional aux,bbl,blg and available PDF retained. Source and bibliography priors/diffs retained. Clearing the generated aux permits a clean author-year rebuild.'}
(folder/'record.json').write_text(json.dumps(r,indent=2)+'\n')
print(json.dumps(r,indent=2))
