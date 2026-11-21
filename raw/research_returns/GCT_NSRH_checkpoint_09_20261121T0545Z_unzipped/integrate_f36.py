from pathlib import Path
root=Path(__file__).resolve().parent
p=root/'GCT_NSRH.tex'
s=p.read_text()
f=(root/'finding_F36.tex').read_text()
body, tail=f.split('\\paragraph{The Grothendieck dictionary and the exact remaining comparison.}',1)
dictionary, scope=tail.split('Thus the failed claim',1)
body += '\nThus the failed claim'+scope
if '\\label{f:coherentfrobenius}' not in s:
 s=s.replace('\\subsection{Testing the smooth proper noncommutative Weil framework}',body+'\n\\subsection{Testing the smooth proper noncommutative Weil framework}',1)
 d=r'''
\paragraph{\fid{F36}: coherent Frobenius, normalization and descent.}
'''+dictionary+r'''
The affine module/sheaf language is EGA~I, \S9.5; the action and
equivariant-module language is SGA~3, I, 4.7.2--3, with the audited
cote~90, scan~17, as its archival anchor. The derived calculations
are the explicit resolutions in the proof, not an invocation of
flat base change at the singular point. No archival identification
of coherent absolute Frobenius with a nonstandard Weil realization
is asserted.
'''
 s=s.replace('\\section{Archival audit and the Fable leads}',d+'\n\\section{Archival audit and the Fable leads}',1)
 s=s.replace('The actual collision algebra also fails the smoothness hypothesis', 'The actual tensor lattice admits unit coherent Frobenius over the parameter base and on its normalization, while descent through the singular center has an explicit torsion defect. The actual collision algebra also fails the smoothness hypothesis',1)
 s=s.replace('F35 closes the scalar stack-realization question', 'F36 constructs action-compatible coherent Frobenius models and computes their descent defect. F35 closes the scalar stack-realization question',1)
 s=s.replace('F01--F32, F34--F35, F37--F39','F01--F32, F34--F39')
p.write_text(s)
print('Integrated full F36 proof, normalization repair and separate dictionary.')
