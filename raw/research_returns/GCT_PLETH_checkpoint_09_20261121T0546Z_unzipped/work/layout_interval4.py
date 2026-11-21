from pathlib import Path
import re
# Break numeric table data at ordinary spaces, preserving every number.
p=Path('work/root/five_point_q_module_report.md');s=p.read_text()
s=re.sub(r'\\\(([0-9]+(?:,[0-9]+){10,})\\\)',lambda m:', '.join(m[1].split(',')),s)
p.write_text(s)
# Independent tuple tokens allow line breaks in narrow table cells.
for fn in ['work/root/five_point_symmetric_quotient_report.md','work/rectangular/rectangular_end_lower_bound.md']:
 p=Path(fn);s=p.read_text()
 s=re.sub(r'\\\((\([0-9,]+\)(?:,\([0-9,]+\)){2,})\\\)',lambda m:'\\('+m[1].replace('),(',')\\), \\((')+'\\)',s)
 p.write_text(s)
# File identifiers are code, including in this proof-review paragraph.
p=Path('work/archive/OUTER4_FREE_MODULE_REVIEW.md');s=p.read_text()
s=re.sub(r'\\\((`[^\n]*?`)\\\)',r'\1',s)
p.write_text(s)
# Split long displays without changing any terms or tags.
p=Path('work/root/prime_semigroup_report.md');s=p.read_text()
s=s.replace(r'\mathcal B_a=\{b\ge a: b\text{ is even and either }b-1\text{ or }b+1\text{ is an odd prime}\},'+ '\n'+r'\qquad',r'\begin{gathered}'+'\n'+r'\mathcal B_a=\{b\ge a: b\text{ even},\ b-1\text{ or }b+1\text{ an odd prime}\},\\')
s=s.replace(r'\text{ finitely many }n_b\ne0\right\}.'+'\n'+r'\tag{P.1}',r'\text{ finitely many }n_b\ne0\right\}.'+'\n'+r'\end{gathered}'+'\n'+r'\tag{P.1}')
p.write_text(s)
p=Path('work/theta/outer5/q_plus_report.md');s=p.read_text()
s=s.replace(r'R=\operatorname{Sym}(U)=\mathbf Q[A,B,C,D,E_0],'+ '\n'+r'\quad T=(A,B,C,D,E_0)^t,'+'\n'+r'\quad F=AD(E_0-B-C)-BC(E_0-A-D).',r'\begin{gathered}'+'\n'+r'R=\operatorname{Sym}(U)=\mathbf Q[A,B,C,D,E_0],\quad T=(A,B,C,D,E_0)^t,\\'+'\n'+r'F=AD(E_0-B-C)-BC(E_0-A-D).'+ '\n'+r'\end{gathered}')
s=s.replace(r'\boxed{'+'\n0\\longrightarrow\n'+r'\bigl(\epsilon E\otimes R(-2)\bigr)\oplus',r'\boxed{\begin{gathered}'+'\n0\\longrightarrow\n'+r'\bigl(\epsilon E\otimes R(-2)\bigr)\oplus')
s=s.replace(r'(\epsilon E\otimes U)\otimes R(-1)'+'\n'+r'\longrightarrow'+'\n'+r'(\operatorname{End}E/\mathbf1)\otimes R'+'\n'+r'\longrightarrow\mathcal N\longrightarrow0.}',r'(\epsilon E\otimes U)\otimes R(-1)\\'+'\n'+r'\longrightarrow(\operatorname{End}E/\mathbf1)\otimes R'+'\n'+r'\longrightarrow\mathcal N\longrightarrow0.\end{gathered}}')
s=s.replace(r'(L(0),L(1),L(2),L(3))&=(-1,1,-1,0)\quad\text{periodically modulo }4,',r'(L(0),L(1),L(2),L(3))&=(-1,1,-1,0)\quad(\bmod4),')
s=s.replace(r'(M(0),\ldots,M(4))&=(0,0,-1,1,0)\quad\text{periodically modulo }5.',r'(M(0),\ldots,M(4))&=(0,0,-1,1,0)\quad(\bmod5).')
p.write_text(s)
p=Path('work/rectangular/boundary_truncation_model.md');s=p.read_text()
s=s.replace(r' \boxed{'+'\n'+r' H_b^{-1}',r' \boxed{\begin{gathered}'+'\n'+r' H_b^{-1}')
s=s.replace(' \\ker Q_{L,b}\\ \\cap\\'+'\n'+r' \{\text{polynomials satisfying (R017.2)–(R017.4) and slot symmetry}\}.'+'\n }',r' \ker Q_{L,b}\ \cap\\'+'\n'+r' \{\text{polynomials satisfying (R017.2)–(R017.4) and slot symmetry}\}.'+'\n'+r' \end{gathered}}')
p.write_text(s)
p=Path('work/rectangular/canonical_below_square_families.md');s=p.read_text()
s=s.replace(r'D=\eta S,\quad y_i/\eta=-Y_J\ (i\in I),\quad'+'\n'+r'y_j/\eta=X_I\ (j\in J),\quad'+'\n'+r'\mathcal S=\eta^{n+1}(-1)^{s+1}S^2ZR X_I^{t-1}Y_J^{s-1},'+'\n'+r'\quad\eta\in\{1,-1\}.',r'\begin{gathered}'+'\n'+r'D=\eta S,\quad y_i/\eta=-Y_J\ (i\in I),\quad y_j/\eta=X_I\ (j\in J),\\'+'\n'+r'\mathcal S=\eta^{n+1}(-1)^{s+1}S^2ZR X_I^{t-1}Y_J^{s-1},\quad\eta\in\{1,-1\}.'+'\n'+r'\end{gathered}')
p.write_text(s)
# Long common-polarization definitions: separate target and action.
for fn in ['work/rectangular/polarization_boundary_report.md','work/rectangular/polarization_r4_boundary_and_geometry.md','work/rectangular/three_boundary_kernels.md']:
 p=Path(fn);s=p.read_text()
 blocks=[]
 def display(m):
  z=m[1]
  if ('f\\longmapsto' in z or 'T_{L,b}(f)=' in z) and '\\longrightarrow' in z and '\\begin{' not in z:
   z=z.replace('\\qquad','\\\\').replace('\\quad\n f\\longmapsto','\\\\\n f\\longmapsto')
   z='\n\\begin{gathered}\n'+z.strip()+'\n\\end{gathered}\n'
  return '\\['+z+'\\]'
 s=re.sub(r'\\\[([\s\S]*?)\\\]',display,s)
 p.write_text(s)
