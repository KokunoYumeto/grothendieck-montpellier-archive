from review_root import review
from pathlib import Path
import json

k='ps_134-2_034'
review(k,changes=[
    (r'\mspage{\hand{11}}',r'\margin{11}','The handwritten 11 is at the upper-left margin; the centered typed folio is 10.'),
    (r'\xout{\unsure{thatxhad}}',r'\xout{that had}','That had is legible beneath the x cancellation; the x between the words is a cancelling impression over their space.'),
    (r'\unsure{rather|father}','father','The visible first letter is a typed f. The diplomatic form retains father; the corrected forms use rather only through a separately recorded one-off-slip variant.'),
    (r'\deleted{\unsure{namd}}',r'\deleted{namd}','The cancelled final letter is a typed d, below the clear handwritten replacement name.'),
    (r'\unsure{$\underline{C}$}',r'$\underline{C}$','The retouched letter has the open right side of C and a clear underline.'),
    (r'\xout{\unsure{wordx"stack"}}',r'\xout{word "stack"}','The cancelled phrase word followed by quoted stack is readable; the x between the words belongs to the cancellation.'),
    (r'\xout{\unsure{in n=2 groupoid}}',r'\xout{or a 2-groupoid\unsure{,}}','The beginning is or a, followed by 2-groupoid, not in n=2. A final cancelling x obscures whether a comma was present.'),
    (r'\xout{\unsure{a n=2-category}}',r'\xout{or a 2-category}','The cancelled wording reads or a 2-category; the draft misread the initial words and inserted an equals sign.'),
    (r'\xout{\illegible{2}}',r'\xout{in order to}','The three cancelled words in order to are legible under the x strokes.'),
    (r'\mspage{\hand{34}}',r'\margin{34}','The pencilled 34 is the archive number at bottom left, not the current manuscript folio.')
],doubts={'unsure':[
    (r'\over{\unsure{12}}{13}','doubt retained','The older section number is heavily scribbled over; 12 remains plausible but not secure.'),
    (r'\xout{that had}','doubt resolved','The words are readable beneath the cancelling x impressions.'),
    ('father','doubt resolved','The source clearly has f as its first letter.'),
    (r'\deleted{namd}','doubt resolved','The old final letter is d.'),
    (r'$\underline{C}$','doubt resolved','The underlined retouched letter is C.'),
    (r'\xout{word "stack"}','doubt resolved','Both word and the quoted stack are legible.'),
    (r'\xout{or a 2-groupoid\unsure{,}}','doubt narrowed','The words and hyphen are readable; only possible punctuation under the final x remains doubtful.'),
    (r'\xout{or a 2-category}','doubt resolved','The cancelled phrase reads or a 2-category.')
],'illegible':[
    (r'\deleted{\illegible{1}}','illegible retained','The dense pen cancellation before n-C-stacks does not yield a secure character or word.'),
    (r'\xout{in order to}','illegible resolved','The undertext reads in order to, despite the original two-word illegibility count.')
]},notes=[
    'The live section number is handwritten 13, above an older heavily cancelled number that remains uncertain as 12.',
    'The centered folio 10 is typed. The upper-left 11 is marginal handwriting, and the bottom-left 34 is the archive number.',
    'Structure and category have overlapping typewriter impressions but their live words are legible. No additional cancelled word can be separated from those impressions.',
    'Recovered that had, word "stack", or a 2-groupoid, or a 2-category, and in order to. Only a possible terminal comma in the groupoid phrase remains obscured.',
    'The first letter in father than is a typewriter f; the correct contextual word rather is used only as a recorded one-off slip variant, not as the diplomatic reading.',
    'The second underlined C has a clear open right side and remains C despite its retouching.',
    'The short isolated strokes near suited, French, Mme, Of course and One do not supply securely readable additional letters or words. They are noted without being expanded into text.',
    'The cancelled mark before n-C-stacks remains illegible.'
],summary='Both halves and nine enlarged details inspected. Corrected the marginal numbering; recovered five cancelled phrases, namd and the retouched C; resolved the literal father. Preserved the illegible pen cancellation and possible punctuation under a final x. Section 13 continues onto the next page.',differences={
    442:('n-Gr-stacks','the typescript reads as our transcription','The source has plural stacks; the witness formula is singular.'),
    450:('father','our transcription corrected','The image settles a typed f. The corrected forms apply the explicit slip father to rather in rather than; the same word rather is clearly present on the checked preceding site 32, while the diplomatic text keeps father.')
})

p=Path(__file__).resolve().parents[1]/'records/MASTER_VARIANTS_134_2.json'
v=json.loads(p.read_text()) if p.exists() else []
v=[x for x in v if x.get('source_id')!='DIFF:450']
v.append(dict(key=k,before='father than',after='rather than',kind='slip corrected',reason='One-off wrong first letter in the comparison rather than; rather is attested on checked site 32. Diplomatic father remains unchanged.',source_id='DIFF:450'))
p.write_text(json.dumps(v,ensure_ascii=False,indent=2)+'\n')
