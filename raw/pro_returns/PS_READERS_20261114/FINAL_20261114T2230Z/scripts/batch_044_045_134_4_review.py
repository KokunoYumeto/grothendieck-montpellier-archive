import sys
sys.path.insert(0,'PS_READERS_WORK/scripts')
from review_134_3_4 import save_review
key='ps_134-4_044'
brace=r"\margin{\uline{$I$}\diagram{\begin{tikzpicture}[baseline=0ex,x=1em,y=1ex]\draw[color=blue,line width=.5pt] (.7,3.2)--(.6,2.2)..controls (.1,2.2) and (.1,1)..(.15,.35)..controls (.15,0) and (0,0)..(0,0)..controls (.15,0) and (.15,-.2)..(.15,-.5)..controls (.1,-1.7) and (.2,-2.2)..(.6,-2.2)--(.7,-3.2);\end{tikzpicture}}}"
edits=[
 [r'\xout{partxof}',r'\xout{part of}','The cancelled part of is legible; the intermediate x is a strike impression over the word space.'],
 [r'\xout{\unsure{xtxthexpoint}}',r'\xout{at the point}','The old at the point is readable under the regular machine strikes.'],
 [r'\margin{\unsure{$\mathbb{I}$} (with a brace along these lines)}',brace,'The margin has a handwritten underlined I beside a tall brace. Reconstruct the graphic and remove the transcriptional description from manuscript content.'],
 [r'W-aspheric \xout{xxxx}',r'W-aspheric \xout{over}','The four cancelled cells read over in the enlarged panel.'],
 ['discussion p. 181 and following}', 'discussion p. 181 and following.}','The rotated margin ends following with a clear point.'],
 [r'\inserted{moreover}',r'\inserted[typed]{moreover}','Moreover is regular interlinear type, placed by a pen curve.'],
 [r'\xout{\unsure{for}}',r'\xout{for}','The letters for remain clear below their x impressions.'],
 [r'\xout{\unsure{s}}',r'\unsure{s}','The terminal s is densely blackened. Neither an independent cancellation nor a secure order of overprint layers is established; retain the live candidate with doubt.'],
 [r'\unsure{Clearly}',r'C\unsure{\over[typed]{ll}{le}}arly','Two tall l-like typed stems overlap rounded e-like impressions. Preserve a doubtful typed layer, without silently choosing Cllarly or clean Clearly.'],
 [r'\inserted{strictly}',r'\inserted[typed]{strictly}','Strictly has regular typewriter cells above a placing curve.'],
 [r'\hand{$\subset$}',r'\hand{\ensuremath{\subset}}','The display inclusion is handwritten; remove its nested math delimiters.'],
 [r'\inserted{mathematical}',r'\inserted[typed]{mathematical}','Mathematical is typed above the line, rather than penned.'],
 [r'\deleted{the} \inserted{natural}',r'the \inserted[typed]{natural}','The typed natural is placed after the by a continuous curve. Of the remains live; the curve is not an independent strike.'],
 [r'W_{\hand{h}} \hand{$\subset$} W',r'W_{\hand{h}} \hand{\ensuremath{\subset}} W','The subscript h and inclusion are handwritten. Preserve W_h, and repair nested math only.'],
 [r'\xout{\unsure{weak}}',r'\xout{weak}','Weak is readable in the cancelled interlinear typed phrase.'],
 [r'\xout{\unsure{takexforxWxxxx(M,W)xxthexmodelizerxofxallxKanxcom-}}',r'\xout{take for W \illegible{1}(M,W) the modelizer of all Kan com-}','Most of this machine-cancelled line resolves, while the run between W and (M,W) remains unreadable.'],
 [r'\xout{\unsure{plexesxandxweakxequivalencesxcorrespondingxto}}',r'\xout{plexes and weak equivalences corresponding to}','The complete second cancelled line is legible beneath the x row.'],
 [r'\xout{xxxxxx} imply',r'\xout{\illegible{1}} imply','The old run before imply remains obscured; replace literal cancellation x placeholders with an explicit lacuna.'],
 [r'in\xout{x} terms',r'in\xout{\unsure{t}} terms','The cancelled extra cell after in has a tall stem and crossbar consistent with t, but the x overlaps it heavily.'],
 [r'are\xout{x} compatib',r'are\xout{\illegible{1}} compatib','The isolated cancelled cell after are is not recoverable; an x strike is not a reading of the lower layer.']
]
# The display and inline inclusion edits must remain individually unique.
edits[10][0]=r'\[ W_{(h_W)} \hand{$\subset$} W \]'
edits[10][1]=r'\[ W_{(h_W)} \hand{\ensuremath{\subset}} W \]'
save_review({'key':key,'edits':edits,'diffs':{
 3951:[r'homotopy interval\unsure{s}','The blackened terminal s has possible crossed impressions, but cancellation is not secure; preserve its doubt without deleting it.'],
 3958:[r'W_{(h_W)} subset W','Both typed parentheses round the subscript h_W are visible, and the inclusion is penned.'],
 3960:['loc. cit.','The typewriter c and following it are clear; the witness sit is not the source.'],
 3963:['of the natural order relation','Natural is typed above the line. Its placing curve passes below of the without cancelling those words; the original deletion premise is rejected.','correct transcription'],
 3965:[r'W_h subset W','The source has a single handwritten subscript h, not h_W.'],
 3966:['homotopy structures definable','The final s of structures is clearly typed.']
 },'unsure':[
 ['at the point','The cancelled old phrase resolves through the regular x row.'],
 [r'\uline{$I$} with adjacent reconstructed brace','The margin symbol is a handwritten I with a separate underline; the tall brace is also clear.'],
 [r'\unsure{dist}','The old pen word before discussion is heavily retraced and struck; dist remains only a candidate.'],
 ['for','All three lower letters are recoverable under the strike.'],
 [r'\unsure{s}','The s remains the visible candidate, but dense overprinting does not securely establish deletion or layer order.'],
 [r'C\unsure{\over[typed]{ll}{le}}arly','The two tall stems and superposed rounded impressions make the middle typed layers uncertain.'],
 ['weak','The raised cancelled word has recognizable w-e-a-k letter bodies.'],
 [r'take for W \illegible{1}(M,W) the modelizer of all Kan com-','The long line resolves except for the dense short run after W.'],
 ['plexes and weak equivalences corresponding to','The second struck line is fully recoverable from its lower letters.']
 ],'notes':[
 'The final s is blackened with possible x-like diagonals, but a secure cancellation cannot be separated from overprinting. Its doubt is retained, also supported by an independent reading.',
 'Clearly has two tall l-like stems overlapping rounded e-like typed forms. The layered reading remains doubtful, also supported independently.',
 'Of the remains live. The continuous hooked curve places the typed natural after the; no separate cancellation crosses either word.',
 'At the point and for resolve. The long cancelled example resolves except for the short old run after W; its second line is legible throughout.',
 'The display has the typed parentheses in W_(h_W), with a penned inclusion. The later expression has a single penned h subscript and another penned inclusion.',
 'The rotated dated margin is legible apart from the cancelled dist candidate. It qualifies W-aspheric as universally in W and refers to p. 181 and following.',
 'The lower-left folio 44 is handwritten.'
 ],'evidence':'Both original halves and seven detail panels, plus the correctly rotated margin, inspected. The margin symbol is underlined I beside a brace, reconstructed without editorial prose. Part of, at the point, over and for resolve beneath x strikes. Moreover, strictly, mathematical and natural are typed interlinearly; is, definitely, many, i.e. is and itself are penned. The curve under natural leaves of the live. Terminal s in homotopy intervals and the ll/le typed layers in Clearly remain doubtful, with independent agreement. The display retains parentheses around h_W, and the later subscript is plain handwritten h. The long old Kan-complex example resolves except for a short run after W; the old run before imply remains illegible. The dated 11.4 margin explicitly qualifies W-aspheric and ends with the p. 181 reference and a point. Nested math in the two penned inclusions is repaired.'})

key='ps_134-4_045'
edits=[
 [r'\inserted[typed]{and such that $W_h\hand{\subset}W$,} \inserted{Clearly,}',r'\inserted[typed]{and such that $W_h\hand{\subset}W$,}','Clearly has its own placing curve leading to the next sentence, not to satisfies. Remove it from the incorrect position.'],
 [r'satisfies $h\hand{\leq}h_W$ . \over{F}{f}or',r'satisfies $h\hand{\leq}h_W$ . \inserted{Clearly,} \over{F}{f}or','The pen curve inserts Clearly immediately before for such an h. Its descending end is a placing hook, not a separate opening parenthesis.'],
 [r'any weak homotopy interval \underline{I}',r'any we\over[typed]{\illegible{1}}{a}k homotopy interval \underline{I}','The a of weak is typed over a lower cell with a descender; the lower letter cannot be securely distinguished.'],
 [r'means that \xout{xxx} any',r'means that \xout{\illegible{1}} any','The short old run is obscured by machine strikes and the overlying pen descender.'],
 [r"it's endpoint\xout{x} \xout{xxx} sections",r"it's endpoint\xout{\unsure{s}} \xout{\illegible{1}} sections",'The extra endpoint cell suggests s under x but remains doubtful; the following cancelled run is unreadable.'],
 [r'\deleted{a}\inserted{some}',r'\deleted{a} \inserted{some}','The separate replacement word some has a word space before it.'],
 [r'intervals\hand{*}in M',r'intervals\hand{*} in M','The footnote marker is followed by a real word space before in.'],
 [r'\deleted{\xout{xxxxxxx}}is',r'\deleted{\xout{\illegible{1}}} is','The old run under h_W is densely crossed by both machine and pen; retain a lacuna and separate the following is.'],
 [r'structures \xout{xx} h',r'structures \xout{\illegible{1}} h','The two cancelled cells before h do not give a secure old word.'],
 [r'\xout{xxmpatible}',r'\xout{\unsure{co}mpatible}','The visible mpatible resolves, while the first two cells remain heavily crossed; co is only tentative.'],
 [r'\hand{\unsure{,}}',r'\hand{,}','The enlarged terminal mark has a broad head and a distinct descending comma tail.'],
 [r'\xout{xxxwhich}',r'\xout{to which}','The old t, o, space and which are all recoverable through the regular machine row.'],
 [r'\xout{xxsuring}',r'\xout{\unsure{en}suring}','The old suring is readable; the initial en-like cells remain too crossed to settle against insuring.'],
 ['It would thus',r'\over[typed]{it}{It} would thus','The initial It has displaced regular type impressions, with capital I over lowercase i and a repeated t.'],
 [r'in \hand{all} cases',r'in \over{all}{all} cases','All is retraced in pen over the visible typed all, rather than wholly added.'],
 ['Of course,  in case',r'Of course,  \unsure{\over[typed]{in}{in}} case','The in has dense overlapping letter forms; the live word is clear, but the typing-layer interpretation remains doubtful.'],
 [r'\over{x}{w}e',r'\over{\unsure{x}}{w}e','The live w is pen-written; the old cell is largely hidden and cannot securely be settled as x.']
]
save_review({'key':key,'edits':edits,'diffs':{
 3968:['whenever M has a zero object','Both has and singular object are plainly typed.'],
 3970:['isomorphisms ...).','The source ends with the ellipsis, closing parenthesis and a separate point.'],
 3975:[r'Sigma_(h_W)','Both parentheses around the typed h_W subscript are present.'],
 3982:['handwritten comma after strongly saturated','The enlarged pen mark has a definite descending comma tail; retain it.'],
 3985:['the triples','The definite article the is clearly typed before triples.']
 },'unsure':[['handwritten comma','The enlarged mark shows a broad pen head and descending comma tail.']],
 'illegible':[[r'\illegible{1}','The old run following the W-shaped initial is hidden by dense pen scribble and machine strikes.']],
 'notes':[
 'Clearly belongs before for such an h after the preceding full stop. The curved pen line gives its placement, and its left end is not independent punctuation.',
 'All is clearly penned over the typed all; both layers are now represented.',
 'The old W-prefixed cancelled word remains unreadable through the dense combined strikes.',
 'The final mark is a comma with a recognizable tail, now resolved.',
 'The left-margin cross at the On the other hand paragraph is clearly drawn in pencil and retained.'
 ],'evidence':'Both original halves, five first detail panels, separate revision/conditions/comma/all panels and a five-panel extra sheet inspected. The line about a zero object reads has and singular object, and its ellipsis closes with a parenthesis and point. Clearly is placed before the next for sentence; no extra textual parenthesis is present. The a of weak is typed over an unreadable descender cell. The inserted finite-product qualification and crossed conversely are preserved. The endpoint extra s, several old short runs, co of compatible, en of the old ensuring/insuring and the lower cell under final w remain uncertain. The display subscript retains its parentheses. The comma after strongly saturated resolves by its descending tail. To which resolves under machine cancellation. It shows typed overprinting, all is pen-retraced over typing, and in retains a doubtful typed-layer interpretation. Prefix W- remains joined to aspheric; whole-word some and the star marker receive appropriate spaces. The literal projective-complexes example is preserved for qualification in the guide.'})
