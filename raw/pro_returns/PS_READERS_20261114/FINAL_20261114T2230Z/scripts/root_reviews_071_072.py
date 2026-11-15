from review_root import review
from pathlib import Path
import json
k='ps_134-2_071'
move=r'\begin{tikzpicture}[baseline=(a.base)]\node[anchor=base west,draw=blue,ellipse,inner sep=1pt] (a) {topological intuition};\node[anchor=base west,inner sep=0pt,xshift=3pt] (b) at (a.base east) {extraordinarily simple};\draw[blue,->] (a.north east) .. controls +(1,.35) and +(0,.35) .. (b.north east);\end{tikzpicture}'
review(k,changes=[
(r'\deleted{topological intuition} extraordinarily simple\inserted{topological intuition}',move,'The typed phrase is circled and moved by a long pen curve; it is not crossed out. Preserve the typed order and the actual transposition graphic diplomatically, with an explicit master variant applying the move.'),
(r'\margin{$\longmapsto$}',r'\margin{\hand{$\longmapsto$}}','The mapsto reminder in the left margin is handwritten.'),
(r'''\arrow[r, "j", "\text{inclusion}"']''',r'''\arrow[r, "j", "\text{inclusion}"', color=blue]''','The horizontal diagram arrow is drawn by hand; j is above and inclusion below.'),
(r'''\arrow[d, "\text{fibration}"', "p"]''',r'''\arrow[d, "\text{fibration}"', "p", color=blue]''','The vertical diagram arrow is pen; fibration stands to its left and p to its right.'),
(r'\mspage{\hand{71}}',r'\margin{\hand{71}}','The lower-left71 is pencil archive foliation, not the centered typescript folio.')
],doubts={'unsure':[],'illegible':[]},notes=[
'The leading5 of56 is pen; no separately readable old digit is supplied.',
'The acute over the e of étale has the regular shape and placement of the typed accented letter; no separate handwritten accent is established.',
'The phrase topological intuition is enclosed by a pen oval, with a line pointing after extraordinarily simple. The diplomatic form now preserves this arrangement; a single explicit transposition variant applies the move.',
'The flagged subscripts1 are handwritten and the plain typewritten instances stay plain. The pen0 at the conic-bundle expression is also visible.',
'The heavy live opening bracket after1 is unambiguous; no independently legible older closing bracket is restored beneath it.',
'The lower-left71 is pencil archive foliation.'
],summary='Both halves and enlarged interval bracket and diagram relation signs inspected. Reconstructed the circled transposition rather than inventing a cancellation, marked the pen diagram arrows and marginal mapsto, and relocated archive71 to the margin. The diagram relations visibly have a tilde over two bars, so con g rather than simeq is retained. The source tilde-X and the labels j/inclusion and p/fibration are confirmed. Mathematical boundary-convention problems are reserved for the guide.',differences={
1140:('I think that this','the typescript reads as our transcription','The word that is fully typed.'),
1144:('extraordinarily simple','the typescript reads as our transcription','The typed adverb ends in ily; the witness shortens it to extraordinary.'),
1148:('equi-singularity is that there exists','the typescript reads as our transcription','The verb is is visible and omitted from the witness.'),
1151:(r'\margin{\hand{$\longmapsto$}}','our transcription corrected','The margin arrow is pen and is absent from the witness.'),
1153:(r'\widetilde{X}_1=X_{\hand{1}}\backslash\overset{\circ}{T}','the typescript reads as our transcription','The letter under the tilde is X, not the witness T.'),
1155:('j above the horizontal arrow; inclusion below','the typescript reads as our transcription','The source positions are clear in the diagram.'),
1156:('p right of the downward arrow; fibration left','the typescript reads as our transcription','The source positions are clear in the diagram.'),
1157:(r'\cong in both diagram relations','the typescript reads as our transcription','Enlargement clearly shows a tilde above two horizontal bars in both positions, distinct from the witness simeq.')
})
p=Path(__file__).resolve().parents[1]/'records/MASTER_VARIANTS_134_2.json';v=json.loads(p.read_text());v=[x for x in v if x.get('source_id')!='MOVE:071:1'];v.append(dict(key=k,before=move,after='extraordinarily simple topological intuition',kind='authorial transposition',reason='The pen oval and long arrow move the typed phrase topological intuition after extraordinarily simple; the diplomatic form preserves the earlier order and the visible graphic.',source_id='MOVE:071:1'));p.write_text(json.dumps(v,ensure_ascii=False,indent=2)+'\n')
k='ps_134-2_072'
spacing=r'\hand{\tikz[baseline=(x.base)]{\node[draw,ellipse,inner sep=2pt] (x) {espacer};\draw[->] (1,.1)--(.7,.1)--(.7,1.1);\draw[->] (1,-.1) .. controls (.25,-.1) and (.8,-.7) .. (.7,-1.1);\draw (-.15,-.05)--(1.7,-.05);}}'
label=r'\hand{\tikz[baseline=(x.base)]{\node (x) {(App \unsure{17})};\draw (.5,.3)--(.5,.5);\draw (.5,.3) .. controls (-1,.6) and (-1,-.65) .. (.5,-.3)--(.5,-.5);\draw (1.65,.4)--(.95,.4) .. controls (.7,.4) and (.7,-.2) .. (.95,-.2)--(1.65,-.2);}}'
review(k,changes=[
(r'\mspage{- \unsure{57} -}',r'\mspage{- \hand{5}7 -}','The folio57 is clear, with the5 retraced in pen and7 typed.'),
(r'F_0 \ , \ \widetilde{F}_1 \ ,',r'F_0 \ , \ \widetilde{F}_{\hand{1}} \ ,','The first F-tilde subscript in the opening display is a flagged pen1; the later1 in the morphism target is typed.'),
(r'(respectively $X_1$)',r'(respectively $X_{\hand{1}}$)','This subscript1 has the large slanting head and continuous pen stem.'),
(r'$X_0$ , $X_1$ smooth',r'$X_0$ , $X_{\hand{1}}$ smooth','The1 in the smoothness parenthesis is handwritten.'),
(r'''\overset{\circ}{T} \ar[r,"j'"]\ar[d,swap,"p'"] & X_1''',r'''\overset{\circ}{T} \ar[r,"j'",color=blue]\ar[d,swap,"p'",color=blue] & X_{\hand{1}}''','The first diagram has pen arrows and a flagged pen1; its j-prime and p-prime labels are typed.'),
(r'''\overset{\circ}{T} \ar[r]\ar[d,swap,"p''"] & X_1''',r'''\overset{\circ}{T} \ar[r,color=blue]\ar[d,swap,"p''",color=blue] & X_1''','The second diagram arrows are pen, but its X subscript is a plain typewritten1 and remains plain.'),
(r'\inserted{compact} of finite',r'\inserted{compact} o\over{\unsure{r|f}}{f} finite','The f is visibly handwritten with a tall stem and descending hook; the underlying typed r/f cannot be distinguished securely.'),
(r'\margin{\unsure{à part} (circled), with a hand-drawn line under the paragraph above and arrows pointing up and down in the left margin}',r'\margin{'+spacing+'}','Two independent readings identify the circled word as espacer, with joined es, tall p, small a and final cer. Replace the descriptive prose with the actual word, enclosure, rule and opposed arrows.'),
(r'\inserted{(App \unsure{17})}',r'\margin{'+label+'}','The handwritten appendix label is placed in the margin with brackets, not inserted as running prose; its retraced number remains doubtful.'),
(r'\margin{72}',r'\margin{\hand{72}}','The lower-left72 is pencil archive foliation.')
],doubts={'unsure':[
(r'\hand{5}7','doubt resolved','The pen5 and typed7 are legible.'),
(r'\unsure{then}','doubt retained','The cancellation is dense across the middle and final letters; then remains tentative.'),
('espacer','doubt resolved','Enlargement and an independent visual check agree on espacer; there is no separate accented a or crossed final t.'),
(r'\unsure{17}','doubt retained','The label number is retraced; its first digit is not independently secure.')
],'illegible':[]},notes=[
'The folio is57, with pen5 and typed7.',
'Only the flagged handwritten1s are marked: the first F-tilde in the opening display, X1 in the respective and smoothness clauses, and X1 in the first diagram. The remaining F-tilde subscripts and the second diagram’s1 are regular type.',
'The live f of of is pen, with its old r/f layer now marked doubtful. The cancelled then remains doubtful.',
'The circled word is espacer, independently confirmed. Its enclosure, rule and opposed arrows are reconstructed; the appendix17 label stays doubtful and marginal.',
'The lower-left72 is pencil archive foliation.'
],summary='Both halves and enlarged margin instruction, cancelled word, of repair and contrasting subscripts inspected. Resolved folio57 and espacer, distinguished four pen1s from the typed1s, marked all four diagram arrows, and restored the handwritten f over a doubtful old letter. The section label is marginal with its pen brackets, not an insertion into the sentence. The two original remaining doubts and the newly recovered old r/f doubt stay marked.',differences={
1167:('marginal handwritten(App17) label with placing brackets','our transcription corrected','The source has a margin label and spacing graphics, not the witness descriptive section title or an inline insertion.'),
1168:('the consideration of sheaves','the typescript reads as our transcription','The source types of in full.'),
1170:('circled espacer, rule and opposed pen arrows','our transcription corrected','Both visual readings identify espacer. The witness omits the entire marginal instruction and its graphics.')
})
p=Path(__file__).resolve().parents[1]/'guide_sections/134_2_appendix.tex';s=p.read_text()
if '\\subsection*{Appendix 16:' not in s:
 s+=r'''
\subsection*{Appendix 16: Constructible data, gluing, and tubular neighborhoods}
Cote 134-2, sites 69--72 (folios 54--57), responds to the loss of structure lamented in Appendix 15 by retaining sheaves, complexes, or higher stacks constructible for a fixed stratification P. The initial quasi-compact and quasi-separated hypothesis is materially changed to quasi-coherent by the witness. Grothendieck distinguishes ordinary constructibility under operations from the stronger stability for one fixed stratification, proposing sufficiently fine equi-singular stratifications for the latter. He then analyzes two strata, a closed part $X_0$ and its open complement $X_1$, by gluing locally constant sheaves with a map $F_0\to\phi(F_1)$. The literal formula at site70 contains an extra superscript star on the second inclusion symbol, in addition to its subscript star; the required gluing functor is $i_0^*i_{1*}$, and the later formula $p_*j^*$ confirms its variance. The witness introduces a further error by raising that lower star onto the index1. The intended étale tubular neighborhood is motivated on site71 by a conic neighborhood over $X_0$, with boundary fibration p and an inclusion j into the cut-open complementary piece; it yields $\phi\simeq p_*j^*$ and, by adjunction, a gluing map $p^*F_0\to j^*\widetilde F_1$. Two geometric conventions need clarification in the literal text: the conic bundle is called a bundle over X rather than over $X_0$, and the definition $\widetilde X_1=X_1\setminus(T\setminus X_0)$ removes the boundary if the earlier closed-cone convention for T is used, although the diagram requires that boundary to lie in $\widetilde X_1$. Deleting the appropriate interior or choosing compatible open and closed neighborhoods repairs the construction conceptually; no such repair is inserted into the readers. Site72 offers the less symmetric but more canonical diagram using the punctured neighborhood and then T itself, distinguishing an actual inclusion from a map regarded homotopically as a fibration. The qualification about compact finite-dimensional smooth fibers is part of this geometric proposal, not a property of every replacement by an arbitrary fibration. Note28 later comments on the étale-neighborhood construction. The witness also substitutes tilde-T for the visible tilde-X and changes two diagram relation signs; the scans show a tilde above two bars. The circled transposition of topological intuition is now represented faithfully, and the new section's circled spacing note reads espacer, not the initial tentative à part. Appendix 17 generalizes this gluing diagram to indexed homotopy types over many strata.
'''
 p.write_text(s)
