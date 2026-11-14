from review_root import review
from pathlib import Path
import json

review('ps_134-2_080',changes=[
(r'wh\over{a}{\unsure{i}}ch',r'\over[typed]{wh\unsure{e|a}}{whi}ch','The live first three letters have superposed typewriter impressions, with a clear serifed i and dot; the former third letter remains uncertain between e and a.'),
(r'\uline{Picard category}\xout{xx}',r'\uline{Picard} \uline{categor\over{i}{y}}\xout{es}','The source had categories: a pen y replaces its i, and the final e,s are cancelled by typewriter x strokes. The two underlines are separate.'),
(r'\xout{\unsure{is a category is}}',r'\xout{are categorie\unsure{s}}','The old line visibly begins are and continues categorie; its last letter is obscured by the final x. The original guessed phrase is a category is does not match the scan.'),
(r'\margin{$\otimes$,}',r'\margin{\hand{$\otimes$,}}','The duplicate tensor mark and following comma in the left margin are pen.'),
(r'\deleted{\unsure{s}}',r'\deleted{s}','The lower loop and upper turn of the final s of stacks are visible beneath its localized cancellation.'),
(r'general\deleted{\unsure{ly}}',r'\over{g}{g}eneral\deleted{ly}','The ending ly is legible below the diagonal cancellation; a larger pen g is written over and below the original typed g.'),
(r'\unsure{developped|developed}',r'developped','The typed word has two consecutive p impressions, both plainly visible.'),
(r'\over{$=2$}{\unsure{$\leq 3$}}',r'\over{$=2$}{$\leq 3$}','The pen less-than-or-equal sign and3 are clear over the old typed=2.'),
(r"\inserted{(the ``Mac-Lane resolution'')}",r"\inserted{the ``Mac-Lane resolution''}",'The apparent enclosing parentheses are the ends of a continuous insertion curve, not literal punctuation.'),
(r'cal \inserted{left} resolution',r'cal \inserted[typed]{left} resolution','The interlinear left has typewriter serifs and regular spacing; only its locating curve is pen.'),
(r'\unsure{69}',r'69','Both handwritten digits are clear in the enlarged reference.'),
(r'\margin{80}',r'\margin{\hand{80}}','The lower-left80 is pencil archive foliation, whose orientation does not alter the numeral order.')
],doubts={'unsure':[
('i','doubt resolved','The live typewritten i has a distinct dot and serifed stem; uncertainty now belongs only to its older underlying letter.'),
(r'are categorie\unsure{s}','doubt partly resolved','Most of the older typewritten phrase is legible; only its final letter remains uncertain under an x.'),
('s','doubt resolved','The final s is recognizable under its cancellation.'),
('ly','doubt resolved','The tall l and descending y remain visible beneath the pen strikes.'),
('developped','doubt resolved','The scan distinctly prints two p letters.'),
(r'$\leq 3$','doubt resolved','The two-stroke comparison sign and upper/lower lobes of3 are clear.'),
(r'\unsure{sp}','doubt retained','The small struck word remains too blackened to confirm its first letter securely.'),
(r'\unsure{,}','doubt retained','The dark small mark after adequately merges with nearby pen strokes; the proposed cancelled comma remains tentative.'),
('69','doubt resolved','The open lower loop of6 and the separate9 are legible.')
],'illegible':[(r'\illegible{1}','illegibility retained','The old character after operation is overprinted and traversed by the insertion curve; its upright and bowl do not give a secure reading.')]},notes=[
'The old cancelled line begins are categorie, with only its last letter still doubtful. The typed replacement literally stops at groupoi; an explicit master variant supplies its one-off missing d, supported by groupoid later in this same paragraph.',
'The old character after operation remains illegible; the inserted tensor symbol and its marginal duplicate are clear.',
'The final s of stacks is recoverable beneath the localized cancellation.',
'The cancelled ly of generally is legible, and the displaced pen g is now preserved as an overwrite of typed g.',
'The supplied right edge ends at rathe. No unseen r is invented in the checked source or the readers.',
'The source correction is n less than or equal to3 over typed n=2; it is not the witness equality n=3.',
'The cancelled comma after adequately remains doubtful because its ink merges with adjacent strokes.',
'The handwritten section reference is69, now resolved.',
'The archive numeral is80, lightly written at lower left; it is marked as handwriting. Independent comparison of folios64 and65 confirms matching regular typewriter impressions, so the centered64 remains plain.'
],summary='Both halves and enlarged opening overprints, category plural repair, cancelled old phrase, stack/general endings, developped, n<=3, citation69 and insertion curves inspected. Corrected the recovered plural-to-singular layers, resolved six original doubts, retained the old ambiguous letters and punctuation, distinguished typed left from pen, and removed false parentheses around the Mac-Lane insertion. The clipped rathe remains literal.',differences={
1279:('refer to his book','the typescript reads as our transcription','The typed word is singular book.'),
1282:('is a groupoi','the arXiv text corrects','The interlinear typing literally lacks its final d. The corrected forms apply a recorded isolated-slip correction, supported by groupoid later in this paragraph.'),
1289:('I am assuming','the typescript reads as our transcription','The source has both s letters in assuming.'),
1290:(r'(for $n$\over{$=2$}{$\leq 3$} at any rate)','our transcription corrected','The scan resolves the handwritten inequality less than or equal to3; the witness prints equality3.'),
1293:('in such a way','the typescript reads as our transcription','There is a single typed article a, whereas the witness doubles it.')
})

project=Path(__file__).resolve().parents[1];p=project/'records/MASTER_VARIANTS_134_2.json';a=json.loads(p.read_text());a=[x for x in a if x['source_id']!='DIFF:1282']
a.append(dict(key='ps_134-2_080',before=r'\inserted[typed]{is a groupoi}',after='is a groupoid',kind='typed insertion with slip corrected',reason='The typed insertion is applied and its isolated missing final d supplied: groupoid appears fully spelled later in this same paragraph, referring to the same object.',source_id='DIFF:1282'));p.write_text(json.dumps(a,ensure_ascii=False,indent=2)+'\n')
p=project/'guide_sections/134_2_appendix.tex';s=p.read_text()
if '\\subsection*{Notes 22--24:' not in s:
 s+=r'''
\subsection*{Notes 22--24: Picard stacks, resolutions, and derived structure}
Cote 134-2, site80 (folio64), supplies the background for the Breen letters. Note22 explains lien or tie and Picard categories and stacks, referring to Giraud and to Deligne's account in SGA4, XVIII,1.4. The source visibly changes plural categories to singular category and its verb phrase to the typed is a groupoi; the missing final d is an isolated slip confirmed by groupoid later in the paragraph. The stated range of the presumed higher-stack formalism is changed from n=2 to $n\leq3$, not to the witness's n=3. The proposed connection with truncated complexes requires the strict commutativity condition that the symmetry on $L\otimes L$ be the identity; the note assumes without further explanation that the appropriate condition extends to higher Picard stacks. That assumption should not be read as a supplied higher-categorical proof. Note23 recalls the Mac-Lane resolution by sums of free abelian sheaves on finite products of M, relating Ext invariants to the cohomology of the slice topos. The word left is a typed interlinear insertion; the enclosing curves around the resolution's name are placement marks rather than parentheses. Note24 makes the search for an adequate version of Verdier's triangulated-category formalism part of the projected later work and adds a handwritten pointer to section69 and derivators. The spelling developped is clearly typed and remains unchanged; the cut-off rathe at the scan edge is not completed from the witness.
'''
 p.write_text(s)
