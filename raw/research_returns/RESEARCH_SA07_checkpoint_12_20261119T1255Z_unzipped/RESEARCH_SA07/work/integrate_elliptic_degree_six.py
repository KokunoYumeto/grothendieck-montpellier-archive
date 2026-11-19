"""Append root-approved F.3.20 after independent exact certificate pass."""
from pathlib import Path
root=Path('/workspace/scratch/f6dbb6638732')
path=root/'output/RESEARCH_SA07/sections/F_audit.tex'
paper=path.read_text()
assert '\\begin{result}{F.3.19}' in paper and '\\begin{result}{F.3.20}' not in paper
src=(root/'work/LM6_A22_Nakamura_degree_six.tex').read_text().split('\\paragraph{Theorem.}',1)[1]
statement,proof=src.split('\\paragraph{1. The exact primary input.}',1)
proof='\\paragraph{1. The exact primary input.}\n'+proof
proof=proof.replace('p.117, identify this quotient and its action:',r'p.117, identify this quotient and its action\cite[pp.115--117]{AuditNakamura1996}:')
proof=proof.replace('standing prime in Section2,p.101 is any rational prime.',r'standing prime in Section2,p.101 is any rational prime\cite[p.101]{AuditNakamura1996}.')
proof=proof.replace('endomorphism theorem, original \\S5,S\\"atze3--4,p.360, give',r'endomorphism theorem, original \S5,S\"atze3--4,p.360, give\cite{GenFaltings1983}')
proof=proof.replace('Nakamura1995,(4.3)--(4.4),p.214, to lift',r'Nakamura1995,(4.3)--(4.4),p.214, to lift\cite{AuditNakamura1995}')
proof=proof.replace('Nakamura1994,Theorem2.1.1,p.94, now applies',r'Nakamura1994,Theorem2.1.1,p.94, now applies\cite{AuditNakamura1994}')
certificate=r'''\paragraph{Finite certificate.}
The independent exact program \texttt{check\_elliptic\_degree\_six.py} constructs the Lyndon brackets from associative words, checks that both displayed derivations preserve $[x,y]$, computes the full middle-space dimension, and obtains both displayed matrices with determinant $-8$. Its arithmetic input is the cited original theorem; the closed-image argument above supplies the actual Galois element. Root independently ran the certificate and checked the source and proof.

'''
proof=proof.replace('\\paragraph{Scope.}',certificate+'\\paragraph{Scope.}')
block=(r'\begin{result}{F.3.20}{Degree-six recognition for every once-punctured elliptic curve}{Proved; all number fields and all primes}'+'\n'+statement.strip()+'\n'+r'\end{result}'+'\n'+r'\begin{proof}'+'\n'+proof.strip()+'\n'+r'\end{proof}'+'\n\n')
marker='\\paragraph{Unresolved obligations retained.}'
assert paper.count(marker)==1
paper=paper.replace(marker,block+marker)
path.write_text(paper)
print('Appended F.3.20 to live section; result count',paper.count('\\begin{result}'))
