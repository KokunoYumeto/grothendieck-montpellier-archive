from review_root import review
k='ps_134-2_057'
review(k,changes=[
(r'\margin{(26)}',r'\margin{\hand{(26)}}','The duplicate note call in the left margin is handwritten.'),
(r'\margin{\unsure{x}(27)}',r'\margin{\hand{$\times$(27)}}','A light pencil cross intersects the opening parenthesis of the handwritten marginal call; it is not an uncertain text letter.'),
(r'(Gr)).\over{\unsure{(*)}}{(27)}The',r'(Gr))\over{\unsure{(*)}}{(27)}. The','The typed period follows the overwritten note call, rather than preceding it; restore its position and the visible separation before The.'),
(r'\margin{57}',r'\margin{\hand{57}}','The lower-left archive number is in pencil.')
],doubts={'unsure':[
(r'\hand{$\times$(27)}','doubt resolved','The two light crossing strokes are a pencil cross at the margin call.'),
(r'\unsure{(*)}','doubt retained','The central old mark is heavily covered by the handwritten 27; an original asterisk remains plausible but not fully recoverable.'),
(r'\unsure{;}','doubt retained','The dark mark over the typed comma is too dense to distinguish a replacement semicolon securely from cancellation strokes.')
],'illegible':[]},notes=[
'The leading 1 of the typed 12 is overwritten by a handwritten 4, giving the live folio 42; the surrounding hyphens are retained.',
'The new note number 27 covers an old parenthesized mark; the possible asterisk remains uncertain. The sentence period is after the call.',
'The marginal mark is a pencil cross cutting the opening parenthesis of (27), now resolved as a graphic.',
'The black mark over the comma remains unresolved; its interpretation as a semicolon is not promoted to certainty.',
'The underline beneath not necessarily commutative is drawn by hand and stops with the phrase.'
],summary='Both halves and enlarged note call, marginal cross and punctuation inspected. Resolved the pencil cross, marked both margin calls as handwriting, and moved the sentence period to its actual position after call27. The old asterisk and black punctuation remain uncertain. The source plural categories, singular structure, explicit multiplication dots and missing close-parenthesis in axiom(b) remain as typed.',differences={
901:('(1-cat) - this will be','the typescript reads as our transcription','The source has a hyphen after the category name, not the witness period.'),
902:(r'X.X^{-1}\simeq1','the typescript reads as our transcription','The multiplication dot after the first X is explicitly typed.'),
903:('strict Gr-categories, by a kind of','the typescript reads as our transcription','The source has the plural categories, not the witness singular.'),
904:('formulation of the structure','the typescript reads as our transcription','The singular structure is clearly typed.'),
906:(r'(Gr))\over{\unsure{(*)}}{(27)}. The structure','our transcription corrected','The note call precedes the sentence period. Its obscured older mark remains doubtful.'),
907:(r'd(\theta(x_0).x_1)','the typescript reads as our transcription','The typed dot between the action and x_1 is present.'),
908:(r'\theta(d(x_1)=\mathrm{int}(x_1)','the typescript reads as our transcription','Only one closing parenthesis appears before the equals sign; the source does not have the witness d() sequence.'),
909:(r'L_0\over{,}{\unsure{;}}','the typescript reads as our transcription','The dark handwritten mark and underlying comma are present; the witness omits them. Their precise relation remains doubtful.')
})
k='ps_134-2_058'
spacer=r'\tikz[baseline=(x.base)]{\node[draw,circle,inner sep=1pt] (x) {espacer};\draw[->] (1,.1)--(.7,.1)--(.7,.7);\draw[->] (1,-.1)--(.7,-.1)--(.7,-.7);}'
loop=r'\tikz[baseline=-.4ex,x=.5em,y=.5em]{\draw (1,1) .. controls (0,1) and (-.1,.8) .. (0,.3) .. controls (.2,0) and (.8,.2) .. (1,0);}'
review(k,changes=[
(r'\mspage{-13 -}',r'\mspage{-\over{1}{4}3 -}','The leading typed 1 has a clear handwritten 4 over it, producing the live folio 43.'),
(r'\margin{espacer}',r'\margin{\hand{'+spacer+r'}}','The handwritten spacing instruction is circled and accompanied by opposed bent arrows; restore these graphics rather than print the label as plain typing.'),
('* * *',r'\hand{* * *}','The three uneven asterisks are drawn in pen; their strokes differ from the regular typed mathematical asterisks below.'),
(r'\inserted{(App.10)} Your',r'\margin{\hand{(App.10)}} \hand{'+loop+r'}Your','The appendix label is handwritten in the margin, with a separate curved placement mark around the opening Your; it is not an insertion into the sentence.'),
(r'\overset{\hand{$\mathbb{L}$}}{\otimes}',r'\overset{\mathbb{L}}{\otimes}','The double-stroked L is typed, with regular serifs and aligned strokes; it is not handwriting.'),
(r'\hand{$\mathbb{R}$}Hom',r'$\mathbb{R}$Hom','The double-stroked R is also typed; both bars and its bowl have the same regular impression as the mathematical type.'),
(r'\mspage{\hand{58}}',r'\margin{\hand{58}}','The lower-left 58 is a pencil archive foliation.')
],doubts={'unsure':[(r'\unsure{Ens}','doubt retained','The old word is densely hatched out; the replacement Sets does not independently establish its obscured letters.')],'illegible':[]},notes=[
'The handwritten 4 over the leading typed 1 is clear, so the live folio is 43 rather than uncorrected 13.',
'The old word inside the replaced parenthesized expression remains unreadable enough that Ens stays tentative.',
'The y is written over the i of identities; the following es that underly a is struck, and between is the new interlinear word. The original underly spelling is preserved.',
'The circled espacer, opposed bent arrows, marginal App.10 label and separate placement curve are restored graphically.',
'The three separator stars are handwritten and irregularly positioned, unlike the typed asterisks in the operation symbols.',
'The double-stroked R and L are typed with regular serifs; the original handwritten provenance labels are removed.',
'The lower-left 58 is pencil archive numbering.'
],summary='Both scan halves and enlarged cancelled word, identity correction, double-stroked letters and separator stars inspected. Restored the corrected folio43, the handwriting and geometry of the spacing marks and marginal section call, and the pen stars. Reclassified double-stroked L/R as typed. Ens remains uncertain under cancellation. The live text says some exist, and the handwritten replacements however formal, or equivalently and pointed connected remain intact.',differences={
917:('no descriptive heading','the typescript reads as our transcription','The scan has a marginal appendix number and separator stars, not the witness descriptive title.'),
918:(r'\margin{\hand{(App.10)}}','our transcription corrected','The handwritten section call is in the margin rather than inserted into the sentence.'),
921:('some exist at present','the typescript reads as our transcription','The source verb has no final s; the witness exists is unsupported.'),
923:(r'\overset{\mathbb L}{\otimes} and \mathbb R Hom','our transcription corrected','The double-stroked operation letters are typed, not handwritten.')
})
