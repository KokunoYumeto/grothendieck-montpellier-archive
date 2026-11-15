from review_root import review
from pathlib import Path

label=r'\hand{\tikz[baseline=(x.base)]{\node (x) {(App.18)};\draw (1.6,.4)--(.9,.4) .. controls (.6,.4) and (.6,-.2) .. (.9,-.2)--(1.6,-.2);}}'
review('ps_134-2_075',changes=[
(r'\mspage{\unsure{-\over{\illegible{1}}{6}0-}}',r'\mspage{-\over{\illegible{1}}{6}0-}','The live6 and typed0 with both hyphens are clear. Only the blackened underlying digit remains illegible.'),
(r'\margin{(App.18)}',r'\margin{'+label+'}','The appendix label is handwritten with a continuous placing bracket enclosing the start of From.'),
(r'\over{S}{(s}ay',r'\hand{(}\over{S}{s}ay','The opening parenthesis is a separate pen stroke before the overwritten S; it is not itself written over that letter.'),
(r'\margin{75}',r'\margin{\hand{75}}','The lower-left75 is pencil archive foliation.')
],doubts={'unsure':[(r'-\over{\illegible{1}}{6}0-','doubt partly resolved','The live folio60 is legible; its separately marked underlying first digit remains illegible.')],'illegible':[
(r'\illegible{1}','illegibility retained','The blackened lower impression beneath the pen6 does not yield a secure earlier digit.'),
(r'\illegible{1}','illegibility retained','The crossed handwritten word after their is obscured by a repeated scribble; isolated ascenders do not settle the word.')
]},notes=[
'The live folio is60. The overwritten first digit remains illegible, so only the redundant outer uncertainty is removed.',
'The scribbled handwritten word after their remains illegible and cancelled; neither a context-driven completion nor a guessed word is substituted.',
'The lower-left75 is pencil archive foliation.',
'The three underlined spans are present as drawn rules beneath the typed words, with the same endpoints represented in the checked source.'
],summary='Both halves and enlarged folio, cancelled handwritten word, appendix label and Say correction inspected. Resolved the live folio60 while retaining its illegible old digit and the illegible cancelled word. Restored the appendix label’s pen bracket and separated its opening parenthesis from the lower-case s overwritten on typed S. The finiteness statement and the distinction of ordinary types from prime-to-characteristic profinite completions remain literal.',differences={
1204:('how to begin on such a programme','the typescript reads as our transcription','The article a is fully typed before programme and omitted by the witness.'),
1212:('No descriptive section title; handwritten(App.18) in the left margin','the arXiv text adds','The scan has only the short numbered marginal label and its placing bracket, not the witness descriptive heading.'),
1213:(r'\margin{'+label+'}','our transcription corrected','The handwritten numbered label and its bracket are visible; the witness omits the marginal instruction.')
})

review('ps_134-2_076',changes=[
(r'\mspage{- \unsure{61} -}',r'\mspage{- \hand{6}1 -}','The live folio61 is legible; the6 is retraced in pen and the1 is typed.'),
(r"\unsure{do'nt|don't}",r"do'nt",'The apostrophe is visibly between o and n; preserve the author’s handwritten do\'nt.'),
(r'\margin{(31)}',r'\margin{\hand{(31)}}','The marginal duplicate call31 and its parentheses are handwritten.'),
(r'\infty$-groupoid',r'\over{\unsure{oo}}{\infty}$-groupoid','The infinity mark has a larger handwritten loop over smaller round impressions; the possible underlying oo remains explicitly doubtful.'),
(r"``fibr\deleted{ations}\inserted{es}''",r"``fibr\over{at}{es}\hand{''}\deleted{ions''}",'The pen e and s replace the first two letters of the old ending, and a new pen closing quote follows them. The later ions and original closing quote are crossed out.'),
(r"``cofibr\deleted{ations}\inserted{es}''",r"``cofibr\over{at}{es}\hand{''}\deleted{ions''}",'The same correction is repeated: pen es overwrites at, new pen quotes close the shortened word, and the remaining ions with the old quotes are cancelled.'),
(r'\mspage{76}',r'\margin{\hand{76}}','The lower-left76 is pencil archive foliation, not a second typescript folio.')
],doubts={'unsure':[
(r'\hand{6}1','doubt resolved','The live6 and1 are clear after enlargement.'),
(r'\unsure{?}','doubt retained','The first punctuation mark is densely blackened; the tentative question mark cannot be independently confirmed.'),
(r"do'nt",'doubt resolved','The apostrophe is distinctly above the space after o, before n.'),
(r'\unsure{\over{;}{:}}','doubt retained','The lower comma-like tail remains visible beneath retouching. The proposed semicolon-to-colon change is not fully settled.')
],'illegible':[]},notes=[
'The folio61 is clear, with a pen6 and typed1; no separately legible old digit is supplied.',
'The cancelled first punctuation mark remains tentatively a question mark; the following live typed question mark and pen closing parenthesis are clear.',
'The infinity sign is handwritten over round impressions, possibly oo. The old reading is now explicitly doubtful rather than silently discarded.',
'The punctuation after fundamentally remains doubtful: a comma-like lower tail is visible under the heavier dot.',
'The endings are corrected by es over at, handwritten closing quotes immediately after them, and cancellation of the remaining ions and original quotes. This arrangement is now preserved in both words.',
'The lower-left76 is pencil archive foliation and has been moved from mspage to margin.'
],summary='Both halves and enlarged folio, cancelled punctuation, apostrophe position, infinity sign, retouched colon and word endings inspected. Resolved61 and do\'nt; preserved the two original unresolved punctuation readings and added a doubt for the possible old oo below the handwritten infinity. Restored the actual overwrite-and-cancellation arrangement of fibres and cofibres, and correctly classified archive76. The source’s categorical dimension claims are left untouched.',differences={
1227:('Handwritten call31 in the line and duplicated in the left margin','the typescript reads as our transcription','This source page contains the call only; the witness imports the later note body at this position.'),
1237:('more simply','the typescript reads as our transcription','The typed final y is clearly present; the witness changes the adverb to simple.'),
1241:('Handwritten call32 at the end of the paragraph','the typescript reads as our transcription','The source carries only the call here. Its note body is on the later notes pages, whereas the witness imports it here.')
})

p=Path(__file__).resolve().parents[1]/'guide_sections/134_2_appendix.tex';s=p.read_text()
if '\\subsection*{Appendix 17:' not in s:
 s+=r'''
\subsection*{Appendix 17: Stratified diagrams and the fine homotopy type}
Cote 134-2, sites 72--75 (folios 57--60), generalizes the two-stratum construction to a geometric description of constructible sheaves and higher stacks by diagrams of homotopy types. Site73 insists on taking the homotopy category of the category of diagrams, rather than merely forming diagrams in a homotopy category; note29 supplies the later categorical perspective. For tame compact spaces with equi-singular strata, the proposed diagram consists of manifolds with boundary, fibrations with compact fibers, and inclusions of boundary pieces, from which the space should be reconstructed by gluing. The witness's singular space and its singular inclusion of the boundary fail to preserve the visible plural data. Site74 extends the proposal to a morphism and to the six operations, then proposes a corresponding construction for excellent schemes through étale tubular neighborhoods. Its displayed list mixes $Rf_*,Rf_!$ with $Lg^*,g^!$, although $g$ is subsequently introduced as the restriction to locally closed unions of strata; the variance of the four operations must be read with a consistent choice of the ambient or restricted map. The baseline hyphens in $P_X$- and $P_Y$-constructible are not superscripts on the indices, as the witness makes them. The handwritten word replacing some natural is literally mutal, not natural. Refinement of the stratification leads to a fine homotopy type, intended to retain the whole system of constructible data rather than the ordinary homotopy type alone. The assertion at site75 that passage to an inductive limit gives all of them requires the preceding constructibility restriction: refinement through finite suitable stratifications does not make every arbitrary sheaf locally constant on strata. The proposed strongest finiteness theorem says that the constituent ordinary types, or more cautiously their prime-to-characteristic profinite completions, should come from finite polyhedra or compact manifolds with boundary. This is a programmatic proposal here, with the characteristic-zero route contrasted explicitly with the difficulty of varieties resisting even birational lifting in positive characteristic. Appendix18 turns from these geometric diagrams to the algebraic structures that could recover them; the later notes revisit both the diagram category and the gluing construction. The call after gluing is handwritten30, not the initial transcription's50.
'''
 p.write_text(s)
