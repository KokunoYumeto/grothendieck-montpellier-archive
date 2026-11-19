"""Append F.3.22 after root, generation and elliptic independent audits."""
from pathlib import Path

root = Path('/workspace/scratch/f6dbb6638732')
path = root / 'output/RESEARCH_SA07/sections/F_audit.tex'
paper = path.read_text()
assert r'\begin{result}{F.3.21}' in paper and r'\begin{result}{F.3.22}' not in paper
source = (root / 'work/LM6_A22_X5_all_primes.tex').read_text().split(r'\paragraph{Theorem.}', 1)[1]
statement, proof = source.split(r'\paragraph{1. Reduction to the four split CM lines.}', 1)
proof = r'\paragraph{1. Reduction to the four split CM lines.}'+'\n'+proof
proof = proof.replace('By Faltings, the endomorphism algebra',
                      'By Faltings\\cite[\\S5, S\\"atze~3--4, p.~360]{GenFaltings1983}, the endomorphism algebra')
proof = proof.replace('Tate~1967, \\S4.1, Theorem~3 and Corollary~2, identifies',
                      'Tate~1967, \\S4.1, Theorem~3 and Corollary~2, identifies\\cite{Tate1967}')
proof = proof.replace('Lemma~4.5, p.~116, and (4.7.1)--(4.7.2), p.~117, supply',
                      'Lemma~4.5, p.~116, and (4.7.1)--(4.7.2), p.~117, supply\\cite{AuditNakamura1996}')
proof = proof.replace('proves $Q_0(m)=Q_1(m)$ for every $m$.',
                      'proves $Q_0(m)=Q_1(m)$ for every $m$\\cite{AuditTakao2010RIMS1709}.')
proof = proof.replace('Nakamura~1994, Theorem~2.1.1, p.~94, then puts $A$ in',
                      'Nakamura~1994, Theorem~2.1.1, p.~94, then puts $A$ in\\cite{AuditNakamura1994}')
block = (r'\begin{result}{F.3.22}{All-prime recognition on the genus-two CM target}{Proved; actual simultaneous normalizer constraints}'
         +'\n'+statement.strip()+'\n'+r'\end{result}'+'\n'+r'\begin{proof}'+'\n'
         +'We impose the four conjugacy constraints on one actual arithmetic image and compute its entire relevant leading-term space.\n\n'
         +proof.strip()+'\n'+r'\end{proof}'+'\n\n')
marker = r'\paragraph{Unresolved obligations retained.}'
assert paper.count(marker) == 1
paper = paper.replace(marker, block+marker)
old = ('The split primes\n$\\ell\\equiv1\\pmod5$ and the full profinite A.22 requirement are\n'
       'not settled by this theorem.')
new = ('F.3.22 below supplies the remaining split primes\n$\\ell\\equiv1\\pmod5$ for this same curve. The full profinite\n'
       'A.22 requirement remains unresolved.')
assert old in paper
paper = paper.replace(old, new, 1)
old = ('It specifies exactly the\nprime range in which that possibility has been excluded.')
new = ('It specifies exactly the\nprime range treated by the boundary argument alone. F.3.22\n'
       'below excludes degree one at the remaining split primes\nthrough simultaneous arithmetic conjugacy constraints.')
assert old in paper
paper = paper.replace(old, new, 1)
path.write_text(paper)
print('Integrated F.3.22 and F.3.21 forward scope; numbered results:', paper.count(r'\begin{result}'))
