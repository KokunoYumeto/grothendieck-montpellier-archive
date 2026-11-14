from review_root import review, macro_occurrences, TEXT

def ds(key,name,reasons,resolved=None):
    s=(TEXT/'transcription/ps_pages'/(key+'.tex')).read_text();o=macro_occurrences(s,name);resolved=resolved or {}
    assert len(o)==len(reasons),(key,name,len(o),len(reasons))
    return [(resolved.get(i,x['source']),'doubt resolved' if i in resolved else 'doubt retained',reason) for i,(x,reason) in enumerate(zip(o,reasons),1)]

k='ps_134-2_014'
review(k,changes=[
    (r'\inserted{program for a}',r'\inserted[typed]{program for a}','The interlinear phrase is typed in the same monospaced face; the placement curve is handwritten.'),
    (r'\unsure{at a time}',r'at a time','The three handwritten words are legible in the enlarged upper-half crop.'),
    (r'\unsure{for}',r'for','The replacement reads for; the extended initial f and the following or are clear in enlargement.'),
    (r'\hand{\S} 1.',r'\hand{\S 1.}','The section sign and the 1 with its full stop are handwritten together.')
],doubts={'unsure':ds(k,'unsure',[
    'The dark dash-like title mark remains blotted and its layer cannot be settled.',
    'The lower-case letter under the handwritten capital A is obscured.',
    'The scratched symbol above Dear has no secure reading; the proposed hash remains doubtful.',
    'The name is heavily hatched; Daniel remains a proposed reading of the cancelled name.',
    'The beginning of homotopical has both overtyping and pen strokes; the full reading and the exact underlying layers remain doubtful.',
    'The blackened opening mark before Some remains uncertain.',
    'At a time is legible in the added line.',
    'The typed cancellation before even leaves only a probable there.',
    'The cancelled mark after nowadays remains difficult to separate from the note call.',
    'The cancelled In is heavily blackened; the handwritten replacement is independently legible.',
    'The corrected word is clearly for.',
    'The short typed cancellation before I use remains only probably in.',
    'The long cancelled phrase before prevents remains partly obscured by the overtyped x characters.',
    'The cancelled word before corresponding remains partly hidden; theory stays marked.',
    'The mark after spaces is too dark to distinguish a footnote call from other cancelled strokes.',
    'The final cancelled letters are partly cut by the right edge; th remains uncertain.'
],{7:'at a time',11:'for'}),'illegible':ds(k,'illegible',[
    'The x-overtyped text after an cannot be recovered.',
    'The x-overtyped word after prevents remains unreadable.'
])},notes=[
    'The title mark is a dark blot and remains uncertain.',
    'The capital A is handwritten; the underlying typed character remains uncertain.',
    'The short scratched mark above Dear remains doubtful.',
    'The initial part of homotopical is overworked by typing and pen; its doubt is retained.',
    'The black mark before Some remains unresolved.',
    'The added phrase reads then, at a time when followed by the existing terminal marks; at a time is resolved.',
    'The hand-drawn cancellation crosses the full passage through Spinger’s Lecture Notes; the arXiv witness prints this cancelled continuation as live text.',
    'The final typed word looks is visible despite its overtyped vowel; no change is made.',
    'The words after an and prevents remain illegible; the small cancellation after the opening parenthesis remains a doubtful in.',
    'The handwritten call (2) and ! In are visible, but the overwritten original marks remain doubtful.',
    'The corrected word is legible as for; the doubt on the replacement is removed.',
    'The spaces call and final overtyped th remain doubtful. The inserted than is legible.',
    'The lower-left 14 is pencil and retained as a marginal folio.'
],summary='Both halves and enlarged overtyping crops reviewed against the complete opening arXiv passage. Restored typed provenance of program for a, the handwritten section number, and two clear hand readings. Retained cancellations and unresolved dense overtyping. The witness prints a cancelled autobiographical continuation and rewrites or for schemes as as for schemes.',differences={
2:('A letter to ....','the typescript reads as our transcription','The four dots and this separate typed subtitle are visible; the witness omits them.'),
3:(r'\hand{(}followed by an \over{\unsure{a}}{A}ppendix: Three letters to Larry Breen\hand{)}','the typescript reads as our transcription','The appendix subtitle is present on the upper sheet; the witness omits it.'),
5:(r'\margin{1)}','the typescript reads as our transcription','The handwritten 1) appears at the left edge of the pasted strip.'),
6:(r'Dear \deleted{\unsure{Daniel},} ---','the typescript reads as our transcription','The addressee is crossed through with dense diagonal pen strokes; arXiv prints Daniel without applying the cancellation.'),
7:('---','the typescript reads as our transcription','Three short strokes follow the cancelled salutation; the witness omits them.'),
8:('','the arXiv text adds','The source begins with a handwritten section number and Last year; it has no descriptive title The importance of innocence.'),
13:(r'of a \inserted[typed]{program for a} kind','our transcription corrected','The phrase is a typed interlinear insertion with a hand-drawn connector, rather than handwritten words.'),
15:(r'before\hand{,} \inserted{then, at a time when\dots?}','our transcription corrected','The added at a time is legible. The witness joins the added phrase to the cancelled continuation, whereas the source abbreviates the new wording with terminal marks.'),
16:(r'\deleted{at a time when you had just written up your nice ideas on axiomatic homotopical algebra, published since in Spinger\textquotesingle s Lecture Notes.}','the typescript reads as our transcription','The scan carries a continuous handwritten deletion through this entire continuation. The witness prints it as live text and corrects Spinger.'),
27:(r'\inserted{(or for schemes)}','the typescript reads as our transcription','The initial handwritten connective is or, with a rounded o and r; the witness substitutes as.'),
33:(r'spaces\hand{\unsure{(4)}}\hand{,}','the typescript reads as our transcription','The source has a dark handwritten mark before the comma. Its reading as (4) remains doubtful; it is absent from the witness.'),
35:(r'\margin{\unsure{\#}}','the typescript reads as our transcription','The scratched mark above Dear exists on the scan but remains unresolved; the witness has no counterpart.')
})

k='ps_134-2_015'
review(k,changes=[
    (r'\hand{any program of homological, homotopical or topological algebra}',r'\hand{any program of homological, homotopical or topological algebra.}','The handwritten continuation ends with a visible full stop.'),
    (r'\unsure{who\xout{m}|whom}',r'\unsure{who\deleted{m}|whom}','The dense mark over the proposed final m is a hand-drawn cancellation, unlike the separate x-overtyped word following moreover; the underlying letter remains doubtful.'),
    (r'\unsure{ggod|good}',r'ggod','Enlargement clearly shows two g characters followed by o and d. The diplomatic typo is retained.'),
    (r'\unsure{,}',r',','The curved stroke at the right edge after matters is a handwritten comma.'),
    (r'\unsure{$^{(5)}$|$^{(4)}$}',r'$^{(5)}$','The enlarged note call has a visible 5 within parentheses.'),
    (r'\unsure{.}',r'.','The full stop after the closing parenthesis of natural integer is visible.'),
    (r'\mspage{15}',r'\mspage{\hand{15}}','The lower-left folio is pencil handwriting.')
],doubts={'unsure':ds(k,'unsure',[
    'The short mark at the left of the partially covered handwritten heading remains uncertain.',
    'The underlying final letter after who remains obscured; the cancellation is made by hand rather than typed x characters.',
    'The enlarged scan reads ggod, with two descenders in the initial gg.',
    'The hand stroke after matters is a comma.',
    'The call after Bangor group is (5), not (4).',
    'The full stop is clear.',
    'The initial letters of obvious are overtyped; their underlying sequence and exact correction remain uncertain.',
    'The final handwritten word is compatible with work but its middle letters remain too compressed to exclude the alternative confidently.'
],{3:'ggod',4:',',5:r'$^{(5)}$',6:'.'}),'illegible':ds(k,'illegible',[
    'The word after moreover is overtyped with x characters and cannot be read.',
    'The word before natural is x-overtyped and remains unreadable.'
])},notes=[
    'The upper text is reversed show-through and is excluded. The pasted strip obscures any underlying text; the two hand lines, including their terminal period, are retained.',
    'The possible m after who is cancelled by pen. The separate word before may is x-overtyped; may itself is readable despite overtyping.',
    'The inserted o makes too; the following typed word is definitely ggod.',
    'The first note call reads (3), and the enlarged call after Bangor group reads (5).',
    'The right-edge mark after matters is a handwritten comma.',
    'The final hand word remains doubtful between the recorded alternatives despite enlargement.',
    'The overtyped beginning of obvious remains uncertain; no clean spelling is substituted.'
],summary='Both halves and enlarged crops reviewed against arXiv ps1. Restored the first full stop, pen-cancellation provenance and pencil folio; resolved ggod, the comma, call (5) and a full stop. The source includes the n-equivalence and realization sentence missing from arXiv. Six doubt marks remain.',differences={
36:(r'\hand{any program of homological, homotopical or topological algebra.}','our transcription corrected','The omitted terminal period is visible on the strip; arXiv includes it.'),
37:('','the arXiv text adds','The handwritten source section begins 2. The motivation; the descriptive title is not on the scan.'),
39:(r'\margin{\unsure{=}}','the typescript reads as our transcription','A dark mark remains partly hidden under the pasted strip at the left; the witness omits it.'),
40:(r'to\inserted{o} ggod','our transcription corrected','The inserted o and typed ggod are clear. The witness silently supplies the standard good.'),
42:('it had seemed','the typescript reads as our transcription','The typed auxiliary is had; arXiv substitutes has.'),
48:(r'any n-groupoid is n-equivalent to a \hand{$\Pi$}$_n$(X). Moreover, when the notion of n-groupoid (or more generally of an n-categroy) is relativized','the typescript reads as our transcription','Both halves show the full realization/n-equivalence assertion and the start of the next sentence. The corresponding arXiv lines omit this clause and join the remaining pieces.')
})
