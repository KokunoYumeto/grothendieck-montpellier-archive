import sys,json
sys.path.insert(0,'PS_READERS_WORK/scripts')
from review_134_3_4 import save_review,OUT,occurrences,TEXT
key='ps_134-3_027';s=(TEXT/'transcription/ps_pages'/f'{key}.tex').read_text();u=occurrences(s,'unsure')
edits=[]
def edit(a,b,r):edits.append([a,b,r])
edit(r'\mspage{27}',r'\mspage{\hand{27}}','The page number is penned, with a curved open 2 and a slant 7 rather than typewriter figures.')
edit(r'\margin{we will \unsure{rather say} ``test functors\'\', see below\dots}'.replace("\\'","'"),r'\margin{\unsure{we will rather say ``test functors\'\', see below\dots}}'.replace("\\'","'"),'Rotated upper-margin crop resolves rather say; broad gray hatching crosses the whole note, so cancellation status remains doubtful.')
edit(r'\[ B \longrightarrow M \ , \]',r'\[ B \hand{\longrightarrow} M \ , \]','The B and M are typed, while the connecting arrow is penned.')
edit(r'\[ M \rightarrow B^{\wedge} \ . \]',r'\[ M \hand{\rightarrow} B^{\hand{\wedge}} \ . \]','The arrow and hat are dark hand strokes over typed M and B.')
edit(r'\inserted{lemma}',r'\inserted[typed]{lemma}','Lemma is typed above the line with even typewriter letters; the insertion stroke is pen.')
edit(r'either $B \rightarrow M$ \inserted{or $M \rightarrow B^{\wedge}$}',r'either $B \hand{\rightarrow} M$ \inserted[typed]{or $M \hand{\rightarrow} B^{\hand{\wedge}}$}','The interlinear or M B is typed; both arrows and the hat are handwritten.')
edit(r'to $B^{\wedge}$  (using',r'to $B^{\hand{\wedge}}$  (using','The hat over the typed B is handwritten.')
edit(r'(*)  $M^{\sim} \rightarrow$ (Hot)',r'(*)  $M^{\hand{\sim}} \hand{\rightarrow}$ (Hot)','The tilde and arrow in the labelled line are pen; the parenthesized star is typed.')
edit(r'\[ M^{\sim} \xrightarrow{\hand{$\approx$}} B^{\wedge} \longrightarrow (Hot) \quad , \]',r'\[ M^{\hand{\sim}} \hand{\xrightarrow{\approx}} B^{\hand{\wedge}} \hand{\longrightarrow} (Hot) \quad , \]','Both arrows, the two-wave approximation sign, M tilde and B hat are hand strokes in the compositum.')
edit(r'\margin{a ``test category\'\', \unsure{as we will say}}'.replace("\\'","'"),r'\margin{\unsure{a ``test category\'\', as we will say}}'.replace("\\'","'"),'The rotated middle margin clearly gives as we will say; gray diagonal hatching leaves the note cancellation status uncertain.')
edit(r'any} functor $B \rightarrow M$',r'any} functor $B \hand{\rightarrow} M$','The arrow after the underlined any is hand drawn.')
edit(r'localization of $M^{\sim}$.',r'localization of $M^{\hand{\sim}}$.','The superscript tilde is handwritten.')
edit(r'$B \rightarrow M$,  $B\' \rightarrow M$'.replace("\\'","'"),r'$B \hand{\rightarrow} M$,  $B\' \hand{\rightarrow} M$'.replace("\\'","'"),'Both functor arrows in this pair are pen strokes.')
edit(r'``the same\'\' functor  $M \rightarrow$'.replace("\\'","'"),r'``the same\'\' functor  $M \hand{\rightarrow}$'.replace("\\'","'"),'The arrow in the same-functor line is handwritten.')
edit(r'\margin{\unsure{same question for Hot-equivalence of topologies on M}\dots}',r'\margin{\unsure{same question arises for Hot-equivalence of topologies on M\dots}}','The rotated margin shows arises before for Hot-equivalence; cancellation remains uncertain under gray hatching.')
edit(r'\inserted{certain}',r'\inserted[typed]{certain}','Certain is typed above full, with typewriter serifs and spacing.')
edit(r'\uline{canonical} functor  $M \rightarrow$',r'\uline{canonical} functor  $M \hand{\rightarrow}$','The arrow following M is handwritten.')
edit(r'\[ B \hookrightarrow \underline{B}',r'\[ B \hand{\hookrightarrow} \underline{B}','The hooked inclusion arrow is penned between typed letters.')
edit(r'\inserted{natural}',r'\inserted[typed]{natural}','Natural is typed above the struck n of an.')
edit(r'\inserted{(more or less)}',r'\inserted[typed]{(more or less)}','More or less has typewriter letters below the line; the enclosing placement brace is pen.')
conf=dict(key=key,edits=edits,diffs={
1887:['we will rather say “test functors”, see below…; cancellation uncertain','The rotated upper margin resolves rather say; preserve the note with uncertain cancellation rather than importing the witness footnote.'],
1888:[r'\inserted[typed]{lemma}','Typewriter serifs and spacing identify lemma as typed interlinear text.','correct provenance'],
1889:[r'\inserted[typed]{or $M \hand{\rightarrow} B^{\hand{\wedge}}$}','The letters are typed; the arrow and hat are added by hand.','correct provenance'],
1890:[r'\inserted{(cf. section 25)}','The small running-hand phrase is clear immediately above is nothing but; retain it despite witness omission.'],
1891:['a “test category”, as we will say; cancellation uncertain','The rotated crop confirms the wording while the broad pencil hatch may cancel or highlight the note.'],
1893:['same question arises for Hot-equivalence of topologies on M…; cancellation uncertain','The additional verb arises is visible on the second slanting line; note status remains uncertain.','correct transcription'],
1896:[r'\inserted[typed]{certain}','The inserted word is typewritten above full.','correct provenance'],
1897:[r'\inserted{(say)}','The small parenthesis and say are continuous pen strokes above B.'],
1898:['how define','No to appears between how and define in the typewritten line.'],
1900:[r'\deleted{\hand{$(^{25})$}} \hand{?} \hand{$(^{25})$}','The first parenthesized call is heavily scribbled over, followed by a separate question and replacement call.'],
1901:['reasonable','The typed word ends able, not ably.'],
1902:[r'a\deleted{n} \inserted[typed]{natural} equivalence','The n is struck and natural is typed above it.','correct provenance'],
1903:[r'in \inserted[typed]{(more or less)} any','The phrase is typed under the line with a pen placement brace.','correct provenance'],
1904:[r'\hand{\unsure{$(^{*})$}}','The edge crops the dark hooked or parenthesized mark; its full form cannot be securely recovered.'],
1905:[r'M^{\hand{\sim}} \hand{\xrightarrow{\approx}} B^{\hand{\wedge}}','The visible sign above the arrow consists of two waves; it is not replaced by the witness single-wave equivalence form.','correct provenance']},
unsure=[['rather say; entire note cancellation uncertain','Rotated crop resolves the letters but gray hatching traverses the note.'],[u[1][0],'The ending of topology is overtyped; the supplied uncertainty is retained.'],['as we will say; entire note cancellation uncertain','The middle rotated crop resolves the wording; cancellation remains doubtful.'],['same question arises for Hot-equivalence of topologies on M…; cancellation uncertain','Rotated crop resolves the missing verb arises and the rest of the note; gray shading affects its status.'],[u[4][0],'The final l is clipped and overwritten at the right paper edge.'],[u[5][0],'The edge mark includes a hook and dark superscript strokes, but the complete call is cut off.']],
illegible=[[r'\illegible{1}','The short dark mark at the start of the underlined line may connect the margin note, but no secure literal reading is available.']],
notes=['Both upper and middle notes read rather say and as we will say; the whole notes retain uncertainty about hatching/cancellation.','The lower note reads same question arises for Hot-equivalence of topologies on M; the adjacent dark mark remains unreadable.','The word topology is recognizable but its last overtyped character remains doubtful.','All M tildes, the approximation sign, B hats and associated arrows were checked and marked as handwritten where the strokes show it.','The right edge obscures the final l, quote, and following hooked mark; their supplied doubts remain.'],
evidence='Both complete halves opened and inspected. Upper half: typed eligible-functor prose, handwritten arrows and accents, typed interlinear lemma and or M B; the three rotated margin crops resolve rather say, as we will say, and the omitted arises in same question arises for Hot-equivalence of topologies on M. Broad gray hatching over all three notes leaves cancellation uncertain. Lower half: how define and reasonable read literally; certain, natural and (more or less) are typed insertions, (say) is penned, the inclusion arrow is hand drawn, the first call25 is scribbled out and replaced. The clipped universal ending and final edge call remain uncertain; the little mark by the underlined weak-equivalence question remains unread.')
(OUT/'review_notes'/f'{key}.json').write_text(json.dumps(conf,ensure_ascii=False,indent=2))
save_review(conf)
