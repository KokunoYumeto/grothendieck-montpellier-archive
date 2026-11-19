"""Append approved F.3.18--19 to the current live section; no old assembly used."""
from pathlib import Path
root=Path('/workspace/scratch/f6dbb6638732')
path=root/'output/RESEARCH_SA07/sections/F_audit.tex'
paper=path.read_text()
assert '\\begin{result}{F.3.18}' not in paper
rank=(root/'work/LM6_A22_rank_one_CM_quotient.tex').read_text()
rank=rank.split('\\paragraph{Statement.}',1)[1]
statement,proof=rank.split('\\paragraph{Proof with the projector rank retained.}',1)
proof=proof.split('\\paragraph{Source status.}',1)[0]
rank_result=(r'\begin{result}{F.3.18}{A rank-one Jacobian character gives an actual CM quotient}{Proved; exact quotient and Prym maps supplied}'+'\n'+statement.strip()+'\n'+r'\end{result}'+'\n'+r'\begin{proof}'+'\n'+proof.strip()+'\n'+r'\end{proof}'+'\n')
surface=(root/'work/LM6_A22_CM_surface_Prym.tex').read_text().split('\n',1)[1]
surface_statement=r'''For $U=E_0\setminus\{O\}$ with $E_0:y^2=x^3-x$, there is a degree-$800$ finite etale cover over $L=\mathbf Q(i,\zeta_5)$ whose smooth compactification is the genus-$171$ Fermat curve $C_{20}$. Its proper Prym contains an abelian surface isogenous to the absolutely simple CM Jacobian of $Y^2=1-X^5$. The inclusion is injective on integral Tate modules at every prime, including $2$ and $5$. The same open cover has the explicit map to the once-punctured genus-two curve described below. No procyclic lift with open arithmetic normalizer is asserted.'''
surface_result=(r'\begin{result}{F.3.19}{An absolutely simple CM surface in a finite-cover Prym}{Proved; the actual geometric maps are explicit}'+'\n'+surface_statement+'\n'+r'\end{result}'+'\n'+r'\begin{proof}'+'\n'+surface.strip()+'\n'+r'\end{proof}'+'\n')
marker='\\paragraph{Unresolved obligations retained.}'
assert paper.count(marker)==1
paper=paper.replace(marker,rank_result+'\n'+surface_result+'\n'+marker)
path.write_text(paper)
print('Appended F.3.18--19 to live section; result count',paper.count('\\begin{result}'))
