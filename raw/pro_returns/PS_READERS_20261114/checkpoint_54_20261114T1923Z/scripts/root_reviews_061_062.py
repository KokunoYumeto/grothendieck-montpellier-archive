from review_root import review
from pathlib import Path
k='ps_134-2_061'
step=r'\tikz{\draw (0,0)--(.55,0)--(.55,.42)--(1.65,.42);\draw (.62,0)--(.62,.37);}'
curve=r'\tikz{\draw (0,0) .. controls (-.10,.45) and (1.6,.25) .. (2.15,.45) .. controls (2.65,.55) and (2.65,.80) .. (2.30,.80);}'
formula=r'\tikz[baseline=(x.base)]{\node (x) {formule sur une ligne};\draw (0,-.35)--(.8,-.35)--(.8,-.1)--(1.15,-.1);}'
edge=r'\tikz{\draw (0,0)--(.55,0)--(.55,.55)--(1.8,.55);\draw (.62,0)--(.62,.50);}'
circled=r'\tikz[baseline=(x.base)]{\node[draw,ellipse,inner sep=2pt] (x) {laisser espace};}'
review(k,changes=[
(r'\mspage{-46 -}',r'\mspage{-\hand{4}6 -}','The 4 is a handwritten angular digit; the 6 and hyphens are typed.'),
(r'\hand{\unsure{)|,}}',r'\hand{)}','Enlargement shows a full closing arc, not a comma.'),
(r'\margin{$\llcorner$}',r'\margin{\hand{'+step+r'}}','The N.B. opening is marked by a double upright step and horizontal strokes, not a lone corner glyph.'),
('by an appropriate proalgebraic group.','by an appropriate proalgebraic group.'+r'\margin{\hand{'+curve+r'}}','A long curved closing stroke below the N.B. paragraph was missing from the transcription.'),
(r'\margin{formule sur une ligne}',r'\margin{\hand{'+formula+r'}}','Preserve the handwritten instruction and its stepped connecting stroke.'),
(r'G)$ but for which coefficients\hand{\unsure{$G$?}}',r'G)$\margin{\hand{'+edge+r'}} but for which coefficients\hand{$G$?}','The added G and question mark are clear in enlargement. The formula also has a double step at its right edge, now retained at that anchor.'),
(r'$_{\unsure{i}X/k}$',r'$_{iX/k}$','The subscript i is a clearly typed dotted letter, outside the handwritten parenthesis enclosing J.'),
('* *\n*',r'\hand{$*\quad *$}'+ '\n\n'+r'\hand{$\qquad *$}','The three irregular stars are handwritten, not typed asterisks.'),
(r'\margin{laisser espace}',r'\margin{\hand{'+circled+r'}}','The spacing instruction is circled in pen; preserve the enclosure.'),
(r'\margin{61}',r'\margin{\hand{61}}','The lower-right 61 is pencil archive foliation.')
],doubts={'unsure':[
(')','doubt resolved','The enlarged mark is a closing parenthesis with a continuous full arc.'),
(r'\hand{$G$?}','doubt resolved','The capital G and following question mark are readable on enlargement.'),
('i','doubt resolved','A dotted typed i is visible below and outside the handwritten closing parenthesis.')
],'illegible':[
(r'\illegible{1}','illegibility retained','Dense pen hatching conceals the word after and; no continuous letter sequence can be securely recovered.'),
(r'\illegible{1}','illegibility retained','The faint small scribble above f.p.p.f. does not yield a reliable word.')
]},notes=[
'The leading 4 of the folio46 is handwritten; 6 and the flanking hyphens are typed.',
'The enlarged mark after Alb has a complete closing arc and is now read as a parenthesis.',
'The added G and question mark are clear; no older punctuation is securely recoverable beneath their dark junction.',
'The i is typed and legible. Both enclosing parentheses around J are handwritten; the typed iX/k remains outside them.',
'The struck handwritten word between and and in the sense of a is still unreadable beneath thick hatching.',
'The gray scribble above f.p.p.f. remains unreadable.',
'The lower-right 61 is in pencil and is retained as archive foliation.'
],summary='Both halves and enlarged Alb punctuation and G? inspected. Resolved the closing parenthesis, G? and typed subscript i; two illegibilities remain. Restored the pen folio, double-step N.B. bracket, closing curve, formula framing strokes, handwritten stars and circled spacing instruction. The source literally says homeomorphism, different point and (J)_{iX/k}; no mathematical repair is imposed.',differences={
973:(r'\hand{)}','our transcription corrected','The scan shows a closing parenthesis where the witness prints a comma.'),
977:(r'\deleted{localised}\inserted{localizations}','the typescript reads as our transcription','The pen replacement has z and a final plural s; the witness changes both.'),
978:(r'Spec $\underline{O}_{X,\ x}$','the typescript reads as our transcription','The O is the baseline argument of Spec and has its own X,x subscript, not a subscript of Spec.'),
979:(r'$\underline{H}_0$ $(J_*)$','the typescript reads as our transcription','The index is the digit0, consistent with the later same-page H_0; the witness capital O is not printed.'),
980:(r'\hand{comm.}','the typescript reads as our transcription','The handwritten abbreviation comm. is not expanded in this edition.'),
981:(r'$\underline{H}_0$','the typescript reads as our transcription','The scan has a digit0, not capital O.'),
983:('double-step opening bracket and long curved closing stroke','our transcription corrected','Both pen graphics enclosing the N.B. paragraph are now represented, rather than a single corner glyph.'),
985:(r'\mathbb{E}xt^i','the typescript reads as our transcription','The doubled vertical stroke of the typed E is visible in both occurrences.'),
986:(r'\hand{$G$?}','our transcription corrected','The handwritten G and question mark are readable; the witness omits G.'),
988:(r'\hand{(}$J$\hand{)}$_{iX/k}$','our transcription corrected','The i is typed, legible and outside the pen parenthesis. The witness relocates it inside.'),
995:(r'\margin{\illegible{1}}','the typescript reads as our transcription','The faint interlinear scribble above f.p.p.f. remains unreadable and is absent from the witness.'),
998:('circled handwritten laisser espace','our transcription corrected','The wording is readable and its pen enclosure is restored; the witness omits it.')
})
k='ps_134-2_062'
app=r'\tikz[baseline=(x.base)]{\node (x) {(App.12)};\draw (.5,.3)--(.5,.65);\draw (.5,.3) .. controls (-1,.6) and (-1,-.65) .. (.5,-.3)--(.5,-.65);\draw (1.65,.45)--(.95,.45) .. controls (.7,.45) and (.7,-.2) .. (.95,-.2)--(1.65,-.2);}'
review(k,changes=[
(r'\mspage{-47 -}',r'\mspage{-\hand{4}7 -}','The 4 is handwritten; the 7 and hyphens are typed.'),
(r'\margin{(App.12)}',r'\margin{\hand{'+app+r'}}','The handwritten appendix label has surrounding placement curves and bracket strokes, now retained graphically.'),
(r'\mathbb{Z}/n\mathbb{Z}\deleted{)}.',r'\mathbb{Z}/n\mathbb{Z}\deleted{\unsure{)}}.','The old glyph is blackened; a closing parenthesis is plausible but not securely readable independently of its replacement.'),
(r'\margin{a/ \quad $p^n\mathbb{Z}$}',r'\margin{\hand{a/ \quad $p^n\mathbb{Z}$}}','The coefficient reminder in the left margin is written in pale pencil.'),
(r'\margin{62}',r'\margin{\hand{62}}','The lower-left 62 is pencil archive foliation.')
],doubts={'unsure':[
(r'\unsure{X|K}','doubt retained','The old capital is partly covered by the beginning of with; its intersecting strokes do not securely distinguish X from K.'),
(r'\unsure{same}','doubt retained','The initial letters have overlapping dark and faint strokes. The final me is clear, but the complete word remains uncertain.'),
(r'\unsure{n}','doubt retained','The old coefficient is crossed by the new p and its superscript; the remaining arch does not independently settle n.')
],'illegible':[(r'\illegible{1}','illegibility retained','The typed letter beneath the handwritten p has a loop and stem, but their overlap does not settle the original character.')]},notes=[
'The lower-left archive number62 is in pencil.',
'The initial4 of47 is handwritten, while7 and the hyphens are typed.',
'The word same remains doubtful because its first two letters are overwritten. The pale marginal a/ p^nZ is a separate pencil reminder, retained without attributing a specific hand.',
'The covered coefficient under p remains illegible, and the cancelled capital before with X remains X/K. Both live corrections are clear.',
'The old glyph before the period is blackened. It is now marked as a doubtful closing parenthesis; the new closing parenthesis after the period is clear pen.'
],summary='Both halves and enlarged first-verification and H1 lines inspected. Marked the pen folio, appendix placement graphic and pencil coefficient reminder, and added a doubt to the covered old closing parenthesis. Retained the three original doubts and one illegibility. The literal mu_m tensor exponent lacks d, the source says of relative dimension and perfect dualities, and RHom uses lowercase hom in the display.',differences={
1000:('of relative dimension','the typescript reads as our transcription','The typed word is of, not the witness or.'),
1003:('perfect dualities','the typescript reads as our transcription','The source has the plural dualities, with its final ies clearly typed.'),
1004:(r'\mathbb{R}\mathrm{hom}(F,\mu_n^{\otimes d})','the typescript reads as our transcription','The display has lowercase hom and a doubled-stroke capital R.'),
1005:(r'\mathbb{Z}/n\mathbb{Z}\deleted{\unsure{)}}.\hand{)}','our transcription corrected','The covered old parenthesis is now marked doubtful; the live period and following pen parenthesis are clear.'),
1006:('prime to the characteristic','the typescript reads as our transcription','The source types the in full.'),
1010:('proalgebraic groups','the typescript reads as our transcription','The complete typed word is proalgebraic, unlike the witness poalgebric.'),
1013:(r'\margin{\hand{a/ \quad $p^n\mathbb{Z}$}}','our transcription corrected','The pale pencil reminder is readable and now explicitly marked as handwriting.'),
1014:('mod radical isogeny','the typescript reads as our transcription','The italic word is the abbreviation mod; it is not expanded to modulo.'),
1015:('handwritten (App.12) with curved placement brackets','our transcription corrected','The source has a margin label and placement strokes beside(D), not the witness supplied section heading.')
})
p=Path(__file__).resolve().parents[1]/'guide_sections/134_2_appendix.tex'
s=p.read_text()
if '\\subsection*{Appendix 11:' not in s:
 s+='''\n\\subsection*{Appendix 11: A homological generalized Jacobian (part C)}
Cote 134-2, sites 60--61 (folios 45--46), recalls a complex $J_{*X/k}$ whose degree-zero part contains the generalized Jacobian and whose proposed universal role is expressed by $H^i(X,G_X)\\simeq\\mathbb E xt^i(J_{*X/k},G)$. The residual-complex construction and local generalized Jacobians are meant to produce a homology object representing cohomology with commutative algebraic-group coefficients, continuing part B's class-field-theoretic motivation and preparing part D's continuous duality. The author explicitly revises the old Zariski-topology construction toward étale and finally f.p.p.f. cohomology, and changes the anticipated range from dimension $n$ to $2n$, allowing zero-dimensional components beyond $n$; these are a research programme and recollections, not an established representability theorem. The base-change claim is deliberately only derived. At site61 the literal ``homeomorphism'' $X\\to\\underline H_0$ cannot be read as an asserted topological equivalence establishing the universal algebraic mapping property: its intended morphism and topology require specification. Neither that word nor the heuristic bounds are repaired in the readers. The witness materially changes the notation by making the argument of Spec a subscript, printing capital O for the homology index0, moving the typed i inside the handwritten parentheses around J, dropping the added coefficient G before the question mark, and replacing the plural pen word ``localizations'' by a singular spelling. The edition preserves the visible formulas, the abbreviation ``comm.'', and the original punctuation, including a closing parenthesis after Alb; the two unrecovered pen traces remain marked.\n'''
 p.write_text(s)
