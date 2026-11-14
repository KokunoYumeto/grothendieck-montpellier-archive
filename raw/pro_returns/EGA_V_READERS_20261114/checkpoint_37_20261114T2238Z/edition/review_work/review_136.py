import sys
sys.path.insert(0,'edition/scripts')
from audit_late_helpers import complete
from audit_record import source_path
k='ega25_25_136';s=source_path(k).read_text()
old='\n'.join(s.splitlines()[18:26])
new=r'''% NOTE: The following fragment is written upside down on the scan. It was checked after a 180-degree rotation; the diplomatic layout preserves that orientation.
\diagram{\rotatebox{180}{\begin{minipage}{0.9\linewidth}
\hand{\deleted{Donner une signification \unsure{alg.} intrinsèque}}
\par\hfill\hand{$\searrow$}\hfill\mbox{}
\par\hand{\deleted{$H^{\unsure{n}}(X$}}
\begin{center}
\begin{tikzcd}[row sep=1.2em,column sep=1em]
\hand{H^n(X)}\arrow[d,no head] & \hand{\simeq\sum_{p+q=n}H^{\unsure{q|p}}(X,\Omega^p)}\arrow[d,no head,shift left=2ex]\arrow[d,no head,shift right=2ex] \\
\hand{\text{poids }n} & \hand{\text{poids }p+q} \\
 & \hand{\text{filtration }\uuline{p}}
\end{tikzcd}
\end{center}
\end{minipage}}}'''
r=[(r'\hand{§20 \quad \unsure{Compléments} \unsure{appl.} \unsure{rationnelles} et \unsure{morphismes} \unsure{birationnels} et}\n\hand{\unsure{éclatements} :}',r'','unused')]
r=[('\\hand{§20 \\quad \\unsure{Compléments} \\unsure{appl.} \\unsure{rationnelles} et \\unsure{morphismes} \\unsure{birationnels} et}\n\\hand{\\unsure{éclatements} :}',r'''\hand{§20 \quad Compléments \unsure{appl.} rationnelles et}
\hand{morphismes birationnels et}
\hand{éclatements :}''','The three handwritten lines are readable in their visible order; the compressed abbreviation appl. stays doubtful.'),(r'\unsure{Brauer}','Brauer','The handwritten name Brauer is legible.'),(r'\unsure{Sections} \unsure{hyperplanes}',r'Sect. hyperplanes','The first word is abbreviated Sect., with a visible dot; the expanded Sections was unsupported.'),(old,new,'Rotation of the lower scan settles poids n, poids p+q, filtration p and the superscript n. The descriptive English macro is removed and the visible connecting strokes are drawn as a diagram. The crossed heading is now read where legible; alg. and the overwritten exponent retain doubt.')]
d={5:'The handwritten upper folio reads 39.',7:'The line reads Compléments appl. rationnelles et; the abbreviation remains compressed and doubtful.',8:'Éclatements is legible; morphismes birationnels et belongs to the preceding handwritten baseline.',10:'The handwritten list reads Diviseurs de Cartier, Weil, Picard,.',11:'The next line reads Syst. lin., Brauer-Severi.',13:'The double marginal stroke and handwritten Grassmanniennes are visible; the compressed spelling remains doubtful.',15:'The title is abbreviated Sect. hyperplanes, not the expanded Sections.',17:'The last upright entry reads §24 Ext. Inf.',20:'After rotation the label reads filtration p, with p doubly underlined; it is not a letter F.',21:'After rotation the two labels read poids p+q and poids n.',22:'The English parenthetic description has no counterpart as text on the scan; the actual connecting strokes are drawn in the replacement diagram.',23:'The summation condition reads p+q=n below the summation sign.',24:'The leading n is a superscript; the cohomology exponent is overwritten and stays q|p uncertain. The crossed H expression is separately retained.',25:'In the upright reading orientation the isolated arrow points diagonally down and right.',26:'The cancelled heading reads Donner une signification alg. intrinsèque, with the short abbreviation still doubtful.',28:'The archive number 136 is handwritten.'}
n=['The full page is handwritten; all upright lines and the rotated lower fragment were read.','The two page numbers read39 and136.','The abbreviation after Compléments stays uncertain; the surrounding words are legible.','Rotation settles poids n, poids p+q, filtration p and the superscript n; the overwritten cohomology exponent remains doubtful.','The crossed H expression is retained in the upright reading orientation, including its uncertain exponent.','The crossed heading is substantially legible after rotation; the arrow points down-right in that orientation.','The double marginal bar beside §22 is present.','All long handwriting was read in both orientations.']
x=complete(k,r,d,n);print(k,len(x['decisions']))
