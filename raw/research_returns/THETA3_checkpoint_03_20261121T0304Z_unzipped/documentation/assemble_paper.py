"""Flatten checked proof parts into the requested standalone LaTeX file."""
from pathlib import Path
import re

root=Path(__file__).resolve().parent.parent
w=root/'work'; p=w/'paper_parts'
def read(name): return (w/name).read_text()
front=(p/'front.tex').read_text()
front=front.replace(r'\texttt{7cbf7a0c32fca1badf05931879a37c3f8a2b03b4}.',r'\begin{center}\small\texttt{7cbf7a0c32fca1badf05931879a37c3f8a2b03b4}.\end{center}')
abstract=r'''We compare the CM Hodge construction with the theta and period mechanisms in Alp\"oge's archive, retaining the Hermitian spaces, splitting characters, coefficient types, measures and integral structures. Exact zero-orbit and restriction-seesaw identities give finite quantitative certificates and a positive finite-frame formula for the ball pairing. A direct construction on an $n$-ball realizes balanced $2n$-factor CM tensors by codimension-$n$ cycles; Liu's componentwise theorem supplies their precise CM sources in all ranks. A finite-dimensional kernel argument realizes the wedge as a genuine single theta lift; its true adjoint supplies a common double-lift and last-step Bessel identity. The completed Taylor tensor agrees with the matched canonical harmonic jet. For non-CM sources, finite \'etale covers of one arithmetic ball surface provide infinitely many pairwise nonisogenous elliptic Albanese factors, explicit new $j$-invariants, a simple genus-two Jacobian with endomorphism ring $\Z$, and positive integral periods. An algebraic Weil projector and a curve-product calculation isolate the remaining exceptional-Hodge-class problem. The integral part separates derived signs, horizontal cycles, intrinsic sharp height-two derivative bounds and actual reduced theta frames. Checked implications and cited inputs are distinguished from the unresolved instantiation of the complete character-independent iterated functional. No Masullo claim is used, and no general non-CM Hodge-conjecture conclusion is asserted.'''
front=re.sub(r'(?s)(\\begin\{abstract\}\n).*?(\n\\end\{abstract\})',lambda m:m.group(1)+abstract+m.group(2),front)
A=read('paper_A.tex')
cut=A.index(r'\subsection{THETA3-A1:')
dictionary=A[:cut]
findings=A[cut:]
C=read('paper_C.tex')
local=C.index(r'\subsection{The precise unramified local normalization}')
noncm=C[:local].replace(r'\section{Non-CM sources and the integral-model comparison}',r'\section{Non-CM sources and algebraic extraction}')
integral=C[local:]
chunks=[front,r'\section{Oscillator and arithmetic source conventions}',dictionary,
 (p/'dictionary_032_arithmetic.tex').read_text(),
 r'\part{Checked findings and proved conditional implications}',
 r'\section{Common kernels, ball tensors and exact pairing recovery}',findings,
 read('paper_A6.tex'),read('paper_A7.tex'),read('paper_A8.tex'),read('paper_B.tex'),
 read('paper_B16.tex'),read('paper_B17.tex'),read('paper_B18.tex')]
if (w/'paper_B15.tex').exists(): chunks.append(read('paper_B15.tex'))
chunks += [(p/'Q.tex').read_text(),read('paper_Q10.tex'),read('paper_Q11.tex'),noncm,
 (p/'C12.tex').read_text(),(p/'C13_C14.tex').read_text(),read('paper_C15_C16.tex'),read('paper_C20.tex'),
 r'\section{Integral models, theta frames and specialization}',integral,(p/'C18.tex').read_text(),read('paper_C19.tex'),read('paper_C21.tex'),read('paper_C22.tex'),
 (p/'gates.tex').read_text(),(p/'source_crosswalk.tex').read_text(),r'\end{document}']
text='\n\n'.join(chunks)+'\n'
# Long source locators must be breakable; preserve ordinary mathematical texttt.
text=text.replace(r'\allowbreak{}','')
text=re.sub(r'\\texttt\{([^{}]*[/][^{}]*)\}',lambda m:r'\path{'+m.group(1).replace(r'\_','_')+'}',text)
text=re.sub(r'\\texttt\{([A-Za-z0-9_.\\-]{22,})\}',lambda m:r'\nolinkurl{'+m.group(1).replace(r'\_','_')+'}',text)
(root/'deliverables/THETA3.tex').write_text(text)
print('LaTeX bytes:',len(text.encode()),'lines:',len(text.splitlines()))
