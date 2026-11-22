"""Local line-breaking corrections for the fifth checkpoint PDF."""
from pathlib import Path
root=Path(__file__).resolve().parents[1]
changes=[]
replacements=[
 ('Cai--Lee--Ma--Schwede--Tucker, Theorem~D on pp.~5--6 and','Cai, Lee, Ma, Schwede, and Tucker, Theorem~D on pp.~5--6 and'),
 ('for a constant $C_1$ fixed by $X,J,m_0$. In combination with\n(F5.3), this bounds $\\dim_{\\mathbf F_p}H^0(D,R^1\\Psi M)$ by $C_1r$.',
  'for a constant $C_1$ fixed by $X,J,m_0$. Combining this with\n(F5.3) gives\n\\[\n \\dim_{\\mathbf F_p}H^0(D,R^1\\Psi M)\\leq C_1r.\n\\]'),
 ('Let $k$ be algebraically closed of arbitrary characteristic, let\n$j:Y\\hookrightarrow X$ be a smooth hyperplane section of a smooth',
  'Let $k$ be algebraically closed, of any characteristic. Let\n$j:Y\\hookrightarrow X$ be a smooth hyperplane section of a smooth'),
 ('then its induced rational homomorphism\n$P^a_{\\rm inc}(U)\\to P^b_{\\rm inc}(V)$ is zero.\nHere rational homomorphism means an element of',
  'then the induced rational homomorphism\n\\[\n P^a_{\\rm inc}(U)\\longrightarrow P^b_{\\rm inc}(V)\n\\]\nis zero. Here a rational homomorphism is an element of'),
 ('\\subsection{Codimension-two pencils: the trace image and a stable-range consequence}',
  '\\subsection{Codimension-two pencils and the trace image}')
]
files=['work/fhi/F.tex','work/fhi/F_tame_abelian_bound.tex',
 'work/dgj/section_J.tex','work/dgj/section_J_lefschetz.tex','work/dgj/attempt_J6_lefschetz.tex',
 'work/dgj/section_J_pencil.tex','work/dgj/attempt_J6_pencil.tex']
for name in files:
 p=root/name;s=p.read_text();count=0
 for old,new in replacements:
  count+=s.count(old);s=s.replace(old,new)
 if count:p.write_text(s);changes.append((name,count))
print(changes)
