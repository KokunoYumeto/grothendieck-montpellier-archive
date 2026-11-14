from review_root import review
from pathlib import Path
import json
k='ps_134-2_037'
margin_cue=r'\margin{\diagram{\begin{tikzpicture}\draw (0,0)--(.30,0)--(.43,.28)--(.76,.28);\draw (.33,0)--(.46,.28);\end{tikzpicture}}}'
inline_cue=r'\hand{\tikz[baseline=-.4ex]{\draw (0,0)--(.30,0)--(.43,.28)--(.76,.28);\draw (.33,0)--(.46,.28);}}'
review(k,changes=[
(r'\mspage{23}',r'\mspage{\hand{23}}','The centered folio is penned.'),
(r'\unsure{,|.} Thanks',r', Thanks','The mark has a descending comma tail and is not a full stop.'),
(r'retyping\inserted{that letter}',r'retyping \inserted{that letter}','The inserted two-word phrase is separated from the preceding word.'),
(r'the\inserted{new} intuition',r'the \inserted[typed]{new} intuition','New is typed interlinear text, with a pen insertion curve, and is a separate word.'),
(r'\margin{//}',margin_cue,'The margin has a stepped double-stroke paragraph cue, not two slash characters.'),
(r'types.\hand{//} The third letter,\inserted{written in}',r'types.'+inline_cue+r' The third letter, \inserted{written} \inserted[typed]{in}','The inline stepped cue repeats the marginal paragraph instruction. Written is handwritten, while in is typed beside it above the line.'),
(r'\xout{\illegible{1}}\inserted[typed]{working}',r'\xout{\unsure{dealing}}\inserted[typed]{working}','The cancelled word appears to read dealing, but overlapping x impressions prevent certainty. The typed replacement working is clear.'),
(r'or\inserted{of} a scheme\inserted{say}',r'or \inserted{of} a scheme \inserted{say}','The inserted of and say are whole words, with visible word boundaries at their anchors.'),
(r'to\inserted{all} equisingular',r'to \inserted{all} equisingular','All is a separate inserted word after to.')
],doubts={'unsure':[
(r'\xout{\unsure{1|I}}','doubt retained','The overworked first character has a tall stem with cancelling impressions; 1 and I cannot be securely distinguished.'),
(',','doubt resolved','The punctuation has a clear comma tail.'),
(r'\deleted{\unsure{as it}}','doubt retained','The old phrase under which is heavily inked; as it remains plausible but not fully recoverable.'),
(r'\unsure{\over{.}{,}}','doubt retained','The dense mark after n-stacks does not securely separate the underlying period and proposed comma correction.'),
(r'\over{\unsure{t}}{tc}','doubt retained','The pen tc is legible, but the underlying typed letter remains obscured.'),
(r'\unsure{\hand{,}}','doubt retained','The small mark after fine remains uncertain as comma and in provenance; no extra letters of finite are present.')
],'illegible':[
(r'\deleted{\illegible{1}}','illegible retained','The long dense cancellation after the rewritten contribution clause yields no secure undertext.'),
(r'\xout{\unsure{dealing}}','illegible narrowed','The visible skeleton suggests dealing, but the cancellation prevents a certain reading.')
]},notes=[
'The initial cancelled character remains uncertain between 1 and I; it is not silently omitted.',
'The older phrase beneath handwritten which remains uncertain as as it.',
'The penned tc is clear; the old typed letter beneath it remains doubtful. The literal resulting spelling sketchyly is retained.',
'The punctuation after n-stacks is heavily retraced and its period-to-comma history remains uncertain.',
'The word is fine, not finite. The following small mark remains doubtful as a comma and in provenance.',
'The cancelled word beneath typed working can be tentatively read dealing; a doubt replaces the illegibility marker.',
'The lower-left handwritten 37 is the archive number and remains marginal.'
],summary='Both scan halves and eight enlarged details inspected. Resolved the comma before Thanks, corrected typed new and the typed in after handwritten written, restored whole-word insertion spacing, and drew the repeated stepped paragraph cue. Preserved unresolved cancelled undertext and punctuation. The source says 1975, fine homotopy type, and inverse system, not the witness readings 1945, finite, and inverted.',differences={
493:('APPENDIX to Chapter I : three letters to Larry Breen','the typescript reads as our transcription','The complete typed heading explicitly includes to Chapter I.'),
494:(r'\xout{\unsure{1|I}}','the typescript reads as our transcription','The cancelled initial character is present but remains uncertain; the witness omits it.'),
500:(r'\hand{/}','the typescript reads as our transcription','The tall pen slash before Also is visible and retained.'),
501:('made in 1975','the typescript reads as our transcription','The typed year clearly has 7; the witness 1945 is not supported.'),
502:('handwriting), Thanks','our transcription corrected','The punctuation is a comma, whereas the witness uses a full stop.'),
506:(r'\inserted{that letter}','the typescript reads as our transcription','The handwritten demonstrative is that, not the witness the.'),
508:(r'(in the notes (\hand{22}) to (\hand{31}))','the typescript reads as our transcription','Both handwritten note numbers are present; the witness drops their range.'),
509:(r'\inserted{adding subtitles (with numbers App. 1 to App. 18), and correcting some}','the typescript reads as our transcription','Both App. prefixes occur in the handwritten insertion and are omitted from the witness.'),
514:(r'\inserted[typed]{new}','our transcription corrected','New is typed above the line.'),
515:(inline_cue,'our transcription corrected','The source has a stepped paragraph cue, repeated in the margin; it is drawn diplomatically and applied as a paragraph boundary in the corrected forms.'),
516:(r'\inserted{written} \inserted[typed]{in}','our transcription corrected','Written is penned and in is typed; both are separate words.'),
521:(r'in print\hand{,} \deleted{and going back to the end of the fif-ties.}','the typescript reads as our transcription','The source retains the handwritten comma and cancelled continuation; the witness supplies a sentence-ending full stop.'),
522:(r'\xout{\unsure{dealing}}\inserted[typed]{working}','our transcription corrected','The old word is tentatively recoverable as dealing; it remains doubtful and cancelled.'),
524:(r'fine\unsure{\hand{,}} homotopy type','the typescript reads as our transcription','The source word is fine, not finite; only the following small mark remains uncertain.'),
526:(r'\deleted{ordered set}\inserted{inverse system}','the typescript reads as our transcription','The handwritten replacement clearly says inverse system, not inverted system.')
})
p=Path(__file__).resolve().parents[1]/'records/MASTER_VARIANTS_134_2.json';v=json.loads(p.read_text())
v=[x for x in v if x.get('source_id') not in ['DIFF:515','PARAGRAPH:037:margin','SPACE:038:1','SPACE:038:2']]
v.extend([
dict(key=k,before=margin_cue,after='',kind='author paragraph cue',reason='The marginal stepped cue repeats the inline paragraph instruction applied before The third letter; its drawing remains in the diplomatic form.',source_id='PARAGRAPH:037:margin'),
dict(key=k,before=inline_cue+' The third letter',after='\n\nThe third letter',kind='author paragraph break',reason='The repeated stepped pen cue instructs a new paragraph at this boundary.',source_id='DIFF:515')])

k='ps_134-2_038'
review(k,changes=[
(r'\hfill Villecun 5.2.1975',r'\hfill Villecun 5.2.1975\margin{--}','The short right-edge dash at the level of the date and salutation is visible and was omitted from the initial transcription.'),
('au clair, chaque',r"au clair, ch\'aque",'There is a definite acute accent above the a in chaque. The source accented spelling is retained rather than normalized.'),
],doubts={'unsure':[
(r'\unsure{rèfoulé|refoulé}','doubt retained','A dark upright accent-like mark is present above the first e, but its shape and relation to the original typed letter remain insufficiently clear to settle rèfoulé versus refoulé.')
],'illegible':[]},notes=[
'The centered 23 bis is handwritten and the lower-left 38 is separate archive foliation.',
'The page is a pasted slip, with faint earlier text showing through. Only the visible current surface text is transcribed; no hidden continuation is supplied.',
'Both left marginal dashes are present. The additional right-edge dash level with the heading is now restored.',
'The first e in refoulé has a dark accent-like mark; the original doubt remains because its shape and provenance are not secure.',
'The acute accent above the a of chaque is clear and is now represented, without correcting the accented spelling.',
'One continuous pen stroke separates reputées from sérieuses and que from le monde on consecutive lines. Both intersections remain marked diplomatically; explicit variants apply their spacing function in the corrected forms.',
'The live words qu\'on, venant and entendu remain legible through overtyping. Demi has widened spacing but no extra word or different letter; the witness d\'en is not supported.',
'The line break places pour at the end and -raient at the beginning of the next line. The source hyphen position is retained.'
],summary='Both scan halves and enlarged details of the accent marks inspected. Retained the pasted-sheet distinction, restored the right marginal dash and the visible acute accent in cháque, and preserved the unresolved first-e accent in refoulé. The continuous pen spacing cue has two explicitly recorded corrected-form applications. Appendix section 1 continues.',differences={
529:('(App.1)','the typescript reads as our transcription','The current source has only the numbered call App.1, without the descriptive witness heading.'),
531:('à demi','the typescript reads as our transcription','The first word has a grave à, not circumflex â.'),
532:(r'\unsure{rèfoulé|refoulé}','the typescript reads as our transcription','The first-e mark remains uncertain; the witness unaccented reading does not settle the image.'),
533:('dans telle ou telle circonstance','the typescript reads as our transcription','The words ou telle are present and absent from the witness.'),
535:("pu s'en tirer",'the typescript reads as our transcription','The letter is s, not the witness d.'),
538:(r'reputées\hand{|}"sérieuses"','the typescript reads as our transcription','The pen spacing cue crosses this boundary, and sérieuses has only one s before the final e; the witness changes that spelling.'),
539:('sérieuses','the typescript reads as our transcription','The visible word has the ordinary single-s ending, not sérieusses.'),
541:('développées','the typescript reads as our transcription','The first e carries its typed acute accent; the witness omits it.'),
542:('le monde','the typescript reads as our transcription','The n is visibly present; the witness mode omits it.'),
545:('(ou équivalence...)','the typescript reads as our transcription','The ellipsis is part of the typed text and is absent from the witness.')
})
v.extend([
dict(key=k,before=r'reputées\hand{|}"sérieuses"',after='reputées "sérieuses"',kind='author spacing cue',reason='The continuous pen stroke marks a missing space at this line boundary; apply the space while preserving its graphic in the diplomatic form.',source_id='SPACE:038:1'),
dict(key=k,before=r'que\hand{|}le monde',after='que le monde',kind='author spacing cue',reason='The same continuous pen stroke intersects the next line between que and le; apply the indicated word space.',source_id='SPACE:038:2')])
p.write_text(json.dumps(v,ensure_ascii=False,indent=2)+'\n')
