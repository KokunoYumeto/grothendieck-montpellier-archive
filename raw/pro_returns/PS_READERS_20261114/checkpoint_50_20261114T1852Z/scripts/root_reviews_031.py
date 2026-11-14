from review_root import review
from pathlib import Path
import json

k='ps_134-2_031'
review(k,changes=[
    (r"\mspage{9'}",r'\mspage{\hand{17}}','The centered pen folio is 17, not 9-prime.'),
    (r'ope\xout{\unsure{rat}}ion',r'ope\over[typed]{\illegible{1}}{rat}ion','The r, a and t occupy their normal typewriter cells and remain live beneath overlapping machine impressions. A second reader independently confirmed that there is no extra rat sequence to delete. The earlier layer cannot be recovered.'),
    (r'\unsure{wiewed|viewed}','wiewed','The first letter is a typed w. The diplomatic reading is wiewed; a separately recorded one-off slip variant uses viewed in the corrected forms.'),
    (r"""K \ar[r] & K' \ar[r, shift left, "{f',g'}"] \ar[r, shift right] & F_i""",r"""K \ar[r, blue] & K' \ar[r, shift left, blue, "{f',g'}"] \ar[r, shift right, blue] & F_i""",'All three arrows in the factorization diagram are drawn by hand; the objects and labels remain typed.'),
    (r'\xout{\illegible{1}} starting',r'\xout{using \unsure{rather}} starting','The cancelled using is recoverable, including its g descender. Rather is plausible but remains partly obscured by the x strokes; an independent reading agrees with that distinction.'),
    (r'\inserted{with}',r'\inserted[typed]{with}','With is typed above the line and accompanied by a pen insertion curve.'),
    (r'\inserted{I Believe}',r'\inserted[typed]{I believe}','The interlinear words are typed, and believe has a lowercase b.'),
    (r'\inserted{two}',r'\inserted[typed]{two}','Two is also typed above the line.'),
    (r'\margin{* even not in the \unsure{grou-poid} context}',r'\margin{\unsure{* even not in the grou-poid context}}','The word is readable across its written line division as grou-poid. The broad pencil hatching leaves the status of the note uncertain, so doubt is moved to the note level.'),
    (r'equivalent\hand{*}.\inserted{(15)}',r'equivalent\hand{\unsure{*}}\inserted{(15)}.','The visible call (15) precedes the period. The heavy terminus of its curved entry stroke does not securely establish a separate asterisk, so that possible mark is retained as doubtful.'),
    (r'\deleted{remain\unsure{s}}',r'\deleted{remains}','The old terminal s is visible before the right-edge clipping, beneath its cancellation.'),
    (r'condition\unsure{\hand{s}}','conditions','The final s has the same typewriter impression as the word, although its right edge is clipped; it is not a distinct pen addition.')
],doubts={'unsure':[
    (r'\over[typed]{\illegible{1}}{rat}','doubt narrowed','The live letters rat are clear. Only the underlying typed overprint remains unreadable; treating rat as cancelled would remove necessary live letters.'),
    ('wiewed','doubt resolved','The printed first character is w.'),
    (r'\deleted{cas\unsure{e}}','doubt retained','The old final letter or letters are crossed at the clipped right edge; the new handwritten cases is clear.'),
    (r'\margin{\unsure{* even not in the grou-poid context}}','doubt resolved','The marginal word is legible; a distinct note-status doubt retains the uncertainty caused by pencil hatching.'),
    (r'\deleted{remains}','doubt resolved','The old s can be distinguished beneath the pen cancellation.'),
    ('conditions','doubt resolved','The s is typed and continuous with the word at the page edge.')
],'illegible':[
    (r'\xout{using \unsure{rather}}','illegible partly resolved','Using is legible; rather remains doubtful beneath the x cancellation.')
]},notes=[
    'The centered folio is handwritten 17. Its slanted second digit was misread as a prime in the initial draft.',
    'The y in many and the operation words have overlapping typewriter impressions. The two extra x cancellations in operations remain. In single operation, rat is live overprinting, with an unreadable earlier layer, not three deleted letters.',
    'The cancelled phrase before starting reads using followed by a doubtful rather; no fully certain expansion is claimed.',
    'The margin reads even not in the grou-poid context, with the word divided across its written lines. Its pencil hatching remains uncertain in status.',
    'The call (15) is clear before the full stop. A separate asterisk cannot be distinguished securely from the heavy insertion-curve terminus and remains doubtful.',
    'The final s in conditions is typed, with its right edge clipped.',
    'The clipping at transiti, with, the cancelled remains, and conditions is retained. Letters are supplied as certain only where their surviving strokes settle them.'
],summary='Both halves and enlarged details inspected. Corrected the folio to 17 and the first operation to live typed overprinting, independently checked. Resolved wiewed, the old remains and typed conditions; recovered part of the cancellation using rather. Corrected the typed provenance of with, I believe and two, preserved marginal-note status uncertainty and checked all formula differences.',differences={
    359:('wiewed','our transcription corrected','The scan settles wiewed. The corrected forms use viewed as a one-off wrong-letter slip: the same word is clearly typed viewed on the already checked preceding site 29, and the original page drafts contain no second wiewed occurrence. The change is an explicit master variant.'),
    360:(r'$U_1=u$','the typescript reads as our transcription','The first U is visibly a capital, unlike the lower-case u that follows it; the witness silently lowers it.'),
    364:(r"another object $K'$", 'the typescript reads as our transcription','Object is singular in the source; the witness adds an s.'),
    369:(r'\margin{$\otimes$}','the typescript reads as our transcription','The separate pen tensor sign in the left margin is present and omitted from the witness.'),
    370:(r'\uline{either}','the typescript reads as our transcription','Either has a visible underline.'),
    371:(r'\uline{or}\inserted[typed]{with}','our transcription corrected','The underline of or is present, while with is typed interlinear text rather than handwriting.'),
    374:(r'are\hand{"}equivalent\hand{"},','the typescript reads as our transcription','The source adds quotation marks and retains the comma; the witness replaces the punctuation.'),
    375:(r'\inserted[typed]{I believe}','our transcription corrected','The source insertion is typed and believe begins with lowercase b; the witness supplies surrounding commas.'),
    376:(r'\inserted[typed]{two}','our transcription corrected','The word is a typed interlinear addition.'),
    378:(r'\margin{\unsure{* even not in the grou-poid context}}','our transcription corrected','The source note is much shorter than the witness footnote and does not mention Gr-categories. Its wording is readable, but the hatching status and possible body asterisk remain uncertain.'),
    379:(r'\uline{finite}','the typescript reads as our transcription','Finite is visibly underlined.'),
    382:(r'\margin{31}','the typescript reads as our transcription','The archive number 31 is present in the lower-left margin.')
})

p=Path(__file__).resolve().parents[1]/'records/MASTER_VARIANTS_134_2.json'
v=json.loads(p.read_text()) if p.exists() else []
v=[x for x in v if x.get('source_id')!='DIFF:359']
v.append(dict(key=k,before='wiewed',after='viewed',kind='slip corrected',reason='One-off wrong initial letter: the same word is clearly typed viewed on site 29; the diplomatic reader preserves wiewed.',source_id='DIFF:359'))
p.write_text(json.dumps(v,ensure_ascii=False,indent=2)+'\n')
