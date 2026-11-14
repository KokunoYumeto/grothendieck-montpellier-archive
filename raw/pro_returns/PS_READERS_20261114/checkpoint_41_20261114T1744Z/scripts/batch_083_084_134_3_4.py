import sys
sys.path.insert(0,'PS_READERS_WORK/scripts')
from review_134_3_4 import save_review,TEXT
key='ps_134-3_083';src=(TEXT/'transcription/ps_pages'/f'{key}.tex').read_text();edits=[]
for line in src.splitlines():
 if line.startswith('%'):continue
 new=line.replace(r'A\^{}',r'A\hand{\ensuremath{^{\wedge}}}').replace(r'A \^{}',r'A\hand{\ensuremath{^{\wedge}}}').replace(r'^\wedge',r'^{\hand{\wedge}}').replace(r'\to',r'\hand{\to}')
 if new!=line:edits.append([line,new,'All presheaf carets and the inline localization arrow are penned; use explicit raised symbols instead of empty accents.'])
edits += [
 [r'\unsure{ze}','ze','The crossed final z and e remain readable at the right edge before the next-line zer.'],
 [r"\xout{\unsure{'ll}}",r"\deleted{\xout{'ll}}",'The old apostrophe and two l letters are readable beneath typewriter strikes reinforced by a pen stroke.'],
 [r'sense\inserted',r'sense \inserted','The inserted phrase consists of separate words and requires a boundary after sense.'],
 [r'sure\inserted[typed]',r'sure \inserted[typed]','For instance is a separate interlinear phrase and needs its leading word boundary.'],
 [r'\unsure{dwell}',r'\unsure{dwell on}','The surviving d-w-e-l-l and later rounded o support dwell on, but the heavily crossed ending remains uncertain.'],
 [r'conditions on the small',r'conditions \over[typed]{o}{o}\over[typed]{n}{n} the small','The on has repeated, slightly displaced type impressions.'],
 [r'category\inserted[typed]',r'category \inserted[typed]','The inserted cross-reference is separated from the preceding word in the scan.'],
 [r'\xrightarrow{\deleted{\illegible{1}}}',r'\hand{\xrightarrow{\deleted{\illegible{1}}}}','The display arrow is hand drawn; its crossed superscript mark remains unreadable.'],
 [r'\hand{/}is',r'\hand{/} is','The pen slash separates the formula from the word is; retain a word boundary.'],
 [r'\hand{\ensuremath{^{\wedge}}}is',r'\hand{\ensuremath{^{\wedge}}} is','The word is is separated from the presheaf expression.'],
 [r'\hand{/}commutes',r'\hand{/} commutes','The slash is a word-separation mark before commutes.'],
 [r'aspheric\inserted{[Section 35]}',r'aspheric \inserted{[Section 35]}','The bracketed handwritten reference is a separate inserted phrase.'],
 [r'namely\unsure{.}','namely','The apparent dot is an ochre paper blemish, unlike the black writing; no source punctuation is present there.'],
 [r'(apart\inserted{from}',r'(apart \inserted{from}','The hand insertion from is a separate word.']
]
# Two slash/is sites share the same spelling: combine their otherwise identical
# spacing repair in one page-wide line operation before applying it.
multi=edits.index(next(e for e in edits if e[0]==r'\hand{/}is'))
edits.pop(multi)
for oldline in src.splitlines():
 if r'\hand{/}is' in oldline:
  line=oldline.replace(r'A\^{}',r'A\hand{\ensuremath{^{\wedge}}}').replace(r'^\wedge',r'^{\hand{\wedge}}')
  edits.append([line,line.replace(r'\hand{/}is',r'\hand{/} is'),'Both pen slash marks function as word separators; keep the following is separated.'])
save_review({'key':key,'edits':edits,'diffs':{
 2954:[r'A^{\hand{\wedge}} \hand{\xrightarrow{\deleted{\illegible{1}}}} (\mathrm{Hot}) = W^{-1}(\mathrm{Cat})','The parentheses around Hot and Cat, hand arrow and two crossed hand marks are visible. Neither cancelled mark is securely readable.'],
 2955:[r'\inserted{[Section 35]}','The square-bracketed hand reference reads Section 35 and is live.'],
 2956:[r'(apart \inserted{from} having','From is a clear live hand insertion after apart.']
 },'unsure':[
 ['ze','The two old letters remain distinguishable under their x row.'],
 [r"\deleted{\xout{'ll}}",'The apostrophe and ll are legible; machine cancellation is reinforced by pen.'],
 [r'\unsure{inde}','The four-cell crossed fragment does not preserve enough of its final two letters to settle inde.'],
 [r'\unsure{dwell on}','Dwell and the later o are visible; the complete crossed phrase remains qualified.'],
 [r'\unsure{en}','The last two cells of even are overprinted and cannot be separated securely.'],
 ['','The orange-brown speck is paper staining rather than black punctuation.']
 ],'illegible':[[r'\illegible{1}','The broad hatching over the first hand symbol prevents a secure reading.'],[r'\illegible{1}','The small crossed arrow label has no recoverable complete letter sequence.']],
 'notes':[
 'The cancelled line-end ze is readable; the following line begins zer.',
 'The old apostrophe and ll are legible; both the x strikes and a reinforcing pen stroke cross them.',
 'The en of even remains overprinted and doubtful. The speck after namely is visibly ochre, so it is not transcribed as punctuation.',
 'Both crossed display marks remain unreadable. Their presence and the handwritten arrow are preserved.',
 'The three slash marks are deliberate pen word separators. Their following words now have explicit spaces.'
 ],'evidence':'Both original halves and nine enlarged details inspected. The local/global distinction is stated with penned presheaf carets and three pen separation slashes. The cancelled line-end ze and the old apostrophe-ll are recoverable. Inde and the expanded proposed dwell on remain doubtful, as does the overprinted ending of even. The dot after namely is orange-brown staining and has been removed from the transcription. The strict-test display contains a hand arrow and two genuinely cancelled but unreadable hand marks. The insertion Section 35 is bracketed and capitalized. Typed for instance and the inserted reference to a)(iii) retain their placement and proper word spacing.'})

key='ps_134-3_084';src=(TEXT/'transcription/ps_pages'/f'{key}.tex').read_text();edits=[]
for line in src.splitlines():
 if line.startswith('%'):continue
 new=line.replace(r'A\^{}',r'A\hand{\ensuremath{^{\wedge}}}').replace(r'A\hat{}',r'A^{\hand{\wedge}}').replace(r'\hand{$\to$}',r'\hand{\ensuremath{\to}}')
 if new!=line:edits.append([line,new,'The carets and arrows are pen additions. Replace empty accents and nested dollar math by explicit raised symbols and ensuremath.'])
edits += [
 [r'\mspage{84} \margin{[besides $A\neq\emptyset$],}',r'\mspage{84}','The top-right besides note is the same single insertion already placed after conditions; remove the duplicated margin transcription.'],
 [r'conditions\inserted{[besides $A\neq\emptyset$],}',r'conditions \inserted{[besides $A\neq\emptyset$]}','The pen note ends with a square bracket, not a comma. Its long lower curve places it before the existing typed colon.'],
 [r'\inserted{in A\hand{\ensuremath{^{\wedge}}}} \deleted{of}',r'\inserted[typed]{in A\hand{\ensuremath{^{\wedge}}}} of','In A is typed interlinearly and its caret is penned. The gentle curve through of belongs to placement of this insertion; it does not cancel of.'],
 [r'\hand{\v{}}Cech',r'\ensuremath{\overset{\hand{\vee}}{\mathrm{C}}}ech','The hand supplies the v-shaped hacek over a typed C. Keep C plain and represent the actual separate mark.'],
 [r'\xout{\unsure{s}}',r'\deleted{\unsure{s}}','The dark cancellation after object is a cluster of pen strokes, not typewriter x impressions; the covered letter remains doubtful.'],
 [r'\xout{\unsure{In}}',r'\deleted{\unsure{In}}','The following fragment is cancelled with pen. Its proposed In remains uncertain under the ink.'],
 [r'need to \xout{\illegible{1}}',r'need to \xout{assume}','The right-edge cancelled word reads assume, followed by the new admit on the next line.'],
 [r"it\xout{'}s",r"it\over[typed]{'}{s}",'The apostrophe and s share a type cell: s is typed over the earlier apostrophe rather than following a separately crossed cell.'],
 [r'\hand{$^{(35)}$.}',r'\hand{$^{(36)}$.}','The handwritten call reads 36, ending in a closed-loop 6, not 5.'],
 [r'for F,G in A\hand{\ensuremath{^{\wedge}}}\xout{x}',r'for F,G in A\hand{\ensuremath{^{\wedge}}}\xout{\unsure{n}}','The cancelled following cell retains an n-like shoulder under its x strike; keep the lower letter doubtful.'],
 [r'elements\xout{\unsure{:}}','elements','No independent colon follows elements. The visible ink belongs to the final s, without a separately cancelled punctuation cell.'],
 [r'\xout{\illegible{2}}\inserted[typed]{they are}',r'\xout{\unsure{that is in}} \inserted[typed]{they are}','The earlier crossed phrase retains that and is-like forms, with a possible final in. Preserve the recovery as doubtful and separate the typed replacement phrase.'],
 [r'which also \xout{\illegible{1}}',r'which also \xout{mean}','The clipped cancelled word reads mean before the next line restarts means.'],
 [r'\hand{\unsure{/}}indeed',r'\hand{/} indeed','The thin sloping pen stroke between the caret and i is a word separator, continuing below the line.'],
 [r'\unsure{\over{T}{t}}',r'\over{T}{t}','The small pen t over the typed capital T is clear; the upper typed bar remains behind it.']
]
save_review({'key':key,'edits':edits,'diffs':{
 2958:[r'\inserted{[besides $A\neq\emptyset$]}','Only one such insertion is on the sheet. It has square brackets and no following comma; the typed colon remains.','correct transcription'],
 2959:[r'\inserted[typed]{in A\hand{\ensuremath{^{\wedge}}}}','The words in A are typed; the caret and placement curve are pen.','correct provenance'],
 2960:['of any two elements','Of remains live. The single gently curved stroke through it is the insertion line leading to in A-hat.','reject false deletion'],
 2961:[r'\inserted{Of course (ii)$\Longrightarrow$(iii).}','The hand insertion uses an implication arrow and no comma after Of course.'],
 2968:[r'\hand{$^{(36)}$.}','The call is 36 and supplies no footnote text on this sheet.','correct call number'],
 2971:['what amounts to the same','The typed verb ends with s.'],
 2975:[r'three notions\hand{,} of a','The added pen comma is visible after notions.'],
 2976:['notions however seem','There are no commas bracketing however.'],
 2977:[r'right\over{.}{,} \over{T}{t}he notion','The pen changes the period to a comma and the capital T to a lowercase t.','settle pen correction']
 },'unsure':[
 [r'\unsure{s}','The covered final letter after object remains uncertain; the cancellation is pen.'],
 [r'\unsure{In}','The two-letter fragment is too blackened to settle its original reading.'],
 ['','There is no separately cancelled colon after elements.'],
 ['/','The long thin stroke is a word separator, visible above and below the type line.'],
 [r'\over{T}{t}','The final lowercase t and remaining typed T bar are both visible.']
 ],'illegible':[
 ['assume','The letters of assume survive the right-edge x strikes.'],
 [r'\unsure{that is in}','Several old letter groups can be recovered, but the complete phrase remains uncertain under the x row.'],
 ['mean','The cancelled mean is legible at the right edge, with the next line starting means again.']
 ],'notes':[
 'Of is not deleted: the curved line passes through it as part of the insertion mark for the typed in A and penned caret.',
 'The cancellations read A-hat admit and T2) and T3). The original colon remains. The top besides insertion has no comma and was duplicated in the original transcription; that duplicate has been removed.',
 'The s is typed over an apostrophe in the same cell of its.',
 'The slash before indeed is a thin pen separator. At right, the period-to-comma and capital-T-to-small-t corrections are clear.',
 'Assume and mean are recovered. The earlier phrase under they are is partly readable but remains doubtful.'
 ],'evidence':'Both original halves and twelve enlarged details inspected. The besides-nonemptiness note occurs only once, has square brackets and no comma, and is placed before the live typed colon. In A is typewritten with a pen caret; its curved placement stroke does not delete of. The cohomological name has a separate pen hacek over typed C. The footnote call is 36. The old assume and mean are legible under x strikes; the phrase below they are remains only partly recoverable. The s in its overprints an apostrophe in one cell. No extra colon occurs after elements. The long slash before indeed is a separator, and the last T-to-t correction is secure. The two dark cancellations after object are pen, with their original letters still doubtful.'})
