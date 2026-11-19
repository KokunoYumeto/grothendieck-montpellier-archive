"""Append root-approved F.3.21 without changing prior live section formatting."""
from pathlib import Path
import re

root = Path('/workspace/scratch/f6dbb6638732')
path = root / 'output/RESEARCH_SA07/sections/F_audit.tex'
paper = path.read_text()
assert r'\begin{result}{F.3.20}' in paper
assert r'\begin{result}{F.3.21}' not in paper
source = (root / 'work/LM6_A22_X5_nonsplit.tex').read_text()
source = source.split(r'\paragraph{Theorem.}', 1)[1]
statement, proof = source.split(r'\paragraph{1. The exact absence of a rational line at these primes.}', 1)
proof = r'\paragraph{1. The exact absence of a rational line at these primes.}' + '\n' + proof
proof = proof.replace(
    'endomorphism theorem, original\n\\S5,S\\"atze3--4,p.360, identify',
    'endomorphism theorem, original\n\\S5, S\\"atze~3--4, p.~360, identify\\cite{GenFaltings1983}')
proof = proof.replace(
    'Nakamura1994,Theorem2.1.1,p.94, for the full class of finite',
    'Nakamura~1994, Theorem~2.1.1, p.~94, for the full class of finite\\cite{AuditNakamura1994}')
proof = proof.replace('genus-two model', 'genus-two model')
proof = proof.replace('Steps', 'Steps')
for word in ['degree', 'rank', 'Step', 'divides', 'was']:
    proof = re.sub(r'\b' + word + r'(?=\d)', word + '~', proof)
proof = proof.replace('Step2', 'Step~2').replace('Step1', 'Step~1').replace('Step3', 'Step~3')
proof = proof.replace('etale', "\\'etale")
block = (
    r'\begin{result}{F.3.21}{Actual genus-two normalizer recognition at nonsplit primes}{Proved; exact finite-cover and cyclotomic maps}'
    + '\n' + statement.strip() + '\n' + r'\end{result}' + '\n'
    + r'\begin{proof}' + '\n'
    + 'We use the actual detecting cover to identify the normalizer character before applying cusp recognition.\n\n'
    + proof.strip() + '\n' + r'\end{proof}' + '\n\n'
)
marker = r'\paragraph{Unresolved obligations retained.}'
assert paper.count(marker) == 1
path.write_text(paper.replace(marker, block + marker))
print('Appended F.3.21 to the live section; numbered result count:', (paper + block).count(r'\begin{result}'))
