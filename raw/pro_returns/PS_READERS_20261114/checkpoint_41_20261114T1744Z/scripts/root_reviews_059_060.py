from review_root import review
from pathlib import Path
import json
k='ps_134-2_059'
review(k,changes=[
(r'\mspage{-\hand{\unsure{1}}4 -}',r'\mspage{-\over{\unsure{1}}{4}4 -}','The live first digit is a clear handwritten 4; its covered older typed digit remains uncertain.'),
(r'characteristic\hand{\unsure{s}}',r'characteristic\hand{s}','The added s is a separate legible pen letter before the new parenthesis.'),
(r'truncat\over{\unsure{ion}}{ion}',r'truncat\over{\unsure{i}}{e}\deleted{on}','The live pen letter is e over the old i cell, and a separate dark stroke cancels the following on. Two visual readings confirm this; the older i remains doubtful.'),
(r'\over{\unsure{s}}{\unsure{z}}',r'\over{\unsure{s}}{z}','The pen replacement has the two bars and diagonal of z; the buried older letter remains uncertain.'),
(r'\deleted{\unsure{these|thesis}}',r'\deleted{thesis}','The six letters thesis are recoverable beneath the separate oblique hatching, including the dotted i and final s.'),
(r'\mspage{\hand{59}}',r'\margin{\hand{59}}','The lower-left 59 is pencil archive foliation.')
],doubts={'unsure':[
(r'\over{\unsure{1}}{4}','doubt narrowed','The live 4 is clear; the underlying original digit is substantially covered.'),
(r'\hand{s}','doubt resolved','The s is independent of the following parenthesis and legible.'),
(r'\over{\unsure{i}}{e}\deleted{on}','doubt narrowed','The replacement e and cancellation of on are visible; only the older i cell remains doubtful.'),
(r'\unsure{s}','doubt retained','The original letter beneath the pen z is not independently recoverable.'),
('z','doubt resolved','The live replacement is a pen z.'),
('thesis','doubt resolved','The six old letters can be read between the hatching strokes.')
],'illegible':[(r'\illegible{1}','illegibility retained','The old punctuation after Z/nZ is concealed by a dense zigzag cancellation; the new comma is clear.')]},notes=[
'The live folio is 44, with its first 4 handwritten over a doubtful older digit; the initial transcription mistook the pen shape for 1.',
'The pen s after characteristic is a separate readable letter, not part of the following parenthesis.',
'The old dash after perhaps is cancelled, and a new handwritten dash begins the following line; both are retained.',
'The live z is now resolved; the lower s-like layer remains doubtful.',
'The scan shows e over i followed by cancellation of on, giving truncate after the inserted need to. The old i is the only remaining uncertainty in this correction.',
'The cancelled word reads thesis, with a clear dotted i and final s visible through the oblique pen hatching.',
'The lower-left archive number 59 is in pencil.',
'The small caret over f is typed and is retained as a literal hat; it is not silently dropped as a stray mark.'
],summary='Both halves and enlarged folio, plural s, truncate correction, dualizing overprint, cancelled thesis and punctuation inspected. Resolved the live 4, s, e, z and thesis while retaining the buried older digit/letters and unreadable punctuation. The source has no article before characteristic0, no period in the REMARKS heading, an explicit hat over f, and the quoted chains phrase. Its live truncate reading is restored from the actual pen correction.',differences={
930:('in characteristic 0','the typescript reads as our transcription','There is no the before characteristic.'),
939:(r'\uline{REMARKS}','the typescript reads as our transcription','The heading is underlined without a following period.'),
940:(r'no \inserted{need to} truncat\over{\unsure{i}}{e}\deleted{on}','our transcription corrected','The e and cancellation of on are visible; the earlier transcription’s ion replacement was incorrect.'),
942:('to the fact','the typescript reads as our transcription','The source plainly types the, not the witness he.'),
945:(r"coefficients in $\Lambda$ ''.", 'the typescript reads as our transcription','The closing quotation marks are present, as is the final period; the witness omits the quotation marks.'),
948:(r'I fear!)\hand{.}','the typescript reads as our transcription','A handwritten period follows the parenthesis and is absent from the witness.')
})
k='ps_134-2_060'
spacing1=r'\tikz[baseline=(x.base)]{\node (x) {espacer};\draw (.7,.1)--(.7,.65)--(1,.65);\draw (.7,-.1)--(.7,-.65);}'
spacing2=r'\tikz[baseline=(x.base)]{\node (x) {espacer};\draw[->] (1,.1)--(.7,.1)--(.7,.7);\draw[->] (1,-.1)--(.7,-.1)--(.7,-.7);}'
review(k,changes=[
(r'\mspage{- 45 -}',r'\mspage{- \hand{4}5 -}','The leading 4 is handwritten; the 5 and flanking hyphens are typed.'),
(r'\margin{espacer} properties',r'\margin{\hand{'+spacing1+r'}} properties','The first espacer and opposed bracket strokes are handwritten; preserve the layout instruction graphically.'),
(r'\deleted{enhaut local properties}',r'\deleted{\textit{enhaut} local properties}','Enhaut is typed in italic, while the following words are upright; the cancellation crosses the full phrase.'),
(r'\Lambda_s',r'\Lambda_{\unsure{s|S}}','The small subscript has an s/S form whose capitalization cannot be securely separated at this image resolution. Retain that ambiguity rather than adopt either transcription solely from context.'),
(r"\margin{$*$ $*$ $*$ (three hand stars below the line, under ``that'', ``H'' and ``='')}",r'\margin{\hand{$*\quad *\quad *$}}','The three stars are actual pen marks; remove the descriptive editorial prose and retain the graphic at its line.'),
(r'\margin{espacer} But',r'\margin{\hand{'+spacing2+r'}} But','The second handwritten espacer has opposed bent arrows bracketing the separation before the new part.'),
(r'\margin{$*$ $*$ $*$ (three hand stars above the line)}',r'\margin{\hand{$*\quad *\quad *$}}','Replace the editorial description by the three visible pen stars at their source anchor.'),
(r'\margin{60}',r'\margin{\hand{60}}','The lower-left archive number is in pencil.')
],doubts={'unsure':[(r'\unsure{App.11|App.II}','doubt retained','The old pen section label is thickly retraced and crossed; the final two tall strokes do not securely distinguish digits from capital I letters.')],'illegible':[]},notes=[
'The strike crosses all of enhaut local properties, and enhaut is typed italic. The inserted parenthesized phrase replaces this old parenthesized unit in the corrected forms.',
'The three pen stars under the formula and the three above the new part are restored as marks without printing descriptive prose as source text.',
'The new s after residue is handwritten. The cancellation visibly covers fiel, but the terminal ds remains outside it; this literal partial cancellation is retained, unlike the witness cleaned word.',
'The old App.11/App.II label remains doubtful beneath the pen strokes; its cancellation is clear.',
'Both espacer labels are handwritten and legible, with bracket/arrow geometry now represented.',
'The lower-left 60 is pencil archive foliation.',
'The leading 4 of the folio45 is handwritten, while the remaining characters are typed.'
],summary='Both scan halves and enlarged coefficient subscript, partial fields cancellation, old parenthesized phrase and cancelled section label inspected. Marked the handwritten folio and spacing graphics, restored the italic old enhaut, removed editorial descriptions of stars, and added a doubt to the small s/S coefficient subscript. The pen cancellation of fiel leaves ds live; this is preserved rather than silently completed. The paired f_! and f^! are distinct, and Rosenlicht, flat of relative and residual field are as typed.',differences={
950:(r"\inserted{(properties ``local upstairs'')} (\deleted{\textit{enhaut} local properties})",'our transcription corrected','The old enhaut is italic and the complete phrase is crossed out. An explicit master replacement removes the empty old delimiters when applying the superseding parenthesized insertion.'),
952:(r'\Lambda_{\unsure{s|S}}','our transcription corrected','The small case distinction is not sufficiently secure in the scan; the source now retains the capitalization doubt.'),
954:('flat of relative','the typescript reads as our transcription','The source has of, not the witness or.'),
956:('another ...) with no period','the typescript reads as our transcription','There is no additional period after the closing parenthesis.'),
957:(r'(f_!,f^!)','the typescript reads as our transcription','The first exclamation mark is below f and the second is above it; the witness conflates them.'),
958:('Rosenlicht','the typescript reads as our transcription','The final t is typed and clearly visible.'),
961:('residual field','the typescript reads as our transcription','The source says residual, not residue.'),
963:(r'residue\hand{s}\deleted{fiel}ds','the typescript reads as our transcription','The final ds is visibly outside the cancellation; the witness silently completes the cleanup.'),
964:('succeeded in mobilizing','the typescript reads as our transcription','The pen word mobilizing has z, which the witness changes to s.'),
967:('no descriptive heading','the typescript reads as our transcription','The scan has a cancelled appendix number and the new lettered part(C), not the witness supplied heading.'),
971:('handwritten espacer with bracket/arrow geometry','our transcription corrected','The source spacing instructions are handwritten and are retained graphically; the witness substitutes a generic stars break.')
})
p=Path(__file__).resolve().parents[1]/'records/MASTER_VARIANTS_134_2.json';v=json.loads(p.read_text());v=[x for x in v if x.get('source_id')!='REPLACE:060:1'];v.append(dict(key=k,before=r"\inserted{(properties ``local upstairs'')} (\deleted{\textit{enhaut} local properties})",after=r"\hand{(properties ``local upstairs'')}",kind='author replacement',reason='The new parenthesized phrase replaces the old parenthesized expression as a unit; applying the cancellation does not leave an empty pair of old parentheses in the running text.',source_id='REPLACE:060:1'));p.write_text(json.dumps(v,ensure_ascii=False,indent=2)+'\n')
