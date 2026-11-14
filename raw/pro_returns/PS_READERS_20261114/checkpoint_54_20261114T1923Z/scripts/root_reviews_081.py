from review_root import review
from pathlib import Path
import json

its=r"it\hand{'}\tikz[baseline=(s.base),x=1pt,y=1pt]{\node[anchor=base,inner sep=0pt] (s) at (0,0) {s};\draw[blue,line width=.3pt] (-1,-2)--(0,-3) (1,-4)--(3,-1);}"
connector=r'\margin{\hand{\tikz[x=1cm,y=1cm]{\draw[->] (.8,-.35) .. controls (-.35,.4) and (-.35,1.4) .. (.4,1.4)--(2.4,1.4);\draw (0,-.1)--(2.6,-.1);}}}'
review('ps_134-2_081',changes=[
(r'\xout{\unsure{s}}',r'\xout{s}','The two curves of the old final s are visible beneath the hash-like overstrike.'),
(r'\xout{\unsure{to be}}',r'\xout{to be}','The letters and the intervening word space are clear beneath the typewriter x strikes.'),
(r"it\unsure{\deleted{'}}s",its,'The upper mark is an added pen apostrophe, with no cancellation crossing it. An independent visual check agrees. Preserve also the two separate lower pen strokes below s without assigning them a lexical meaning.'),
(r'\deleted{\unsure{.(*)}}',r'.\deleted{\unsure{(*)}}'+connector,'The sentence period is visible before the blackened note marker and is live. Restore the long curved connector and the separate horizontal rule linking the lower handwritten continuation to this location.'),
(r'\deleted{(*)} At least',r'\deleted{\unsure{(*)}} At least','The blackened lower reference marker does not securely reveal every character of the proposed(*); retain that reading as doubtful.'),
(r'\deleted{\unsure{the}} $H^i(X)$',r'\deleted{the} $H^i(X)$','The tall t, looped h and low e can be distinguished beneath the diagonal pen cancellation.'),
(r"\inserted[typed]{``problem'' is",r"\inserted[typed]{``prob\over[typed]{a}{l}em'' is",'The typed insertion itself has an l superposed on a smaller a impression; restore both layers rather than silently printing only the final problem.'),
(r'\margin{81}',r'\margin{\hand{81}}','The lower-left81 is pencil archive foliation; the centered65 retains its regular typewritten provenance.')
],doubts={'unsure':[
('s','doubt resolved','The old final s is legible beneath its overstrike.'),
('to be','doubt resolved','The source has the two complete old words to be, cancelled by x overstrikes.'),
(r'\unsure{te}','doubt retained','The last part is both overprinted and clipped at the right edge; the suggested te cannot be fully verified.'),
(r"\hand{'}",'doubt resolved','The apostrophe is an independent pen addition. Neither the upper mark nor the lower strokes show a cancellation of it; the live spelling is literally it\'s.'),
(r'.\deleted{\unsure{(*)}}','doubt partly resolved','The preceding period is live and distinct; the blackened reference marker remains uncertain.'),
('the','doubt resolved','The three handwritten letters can be separated from the diagonal cancellation.'),
(r'\unsure{commutative}','doubt retained','The x-overstrikes obscure parts of the inner letter sequence; the full old word remains tentative despite its plausible reading.')
],'illegible':[
(r'\illegible{1}','illegibility retained','The long crossed handwritten false start above At least cannot be read securely; its strokes do not establish a particular phrase.'),
(r'\illegible{1}','illegibility retained','The tiny blackened handwritten word after developped has no securely separable letter sequence.')
]},notes=[
'The old final s of modules and the old to be are resolved. The overtyped te after associa remains doubtful at the cropped edge.',
'An independent reading confirms that the apostrophe is added by pen, not deleted. Its two lower companion strokes are drawn separately; the corrected and reading forms therefore retain the author’s it\'s.',
'The period after contemplating is live. Both cancelled reference markers remain doubtful; the crossed false start is illegible. The cancelled the before H^i(X) is resolved, and the connector and rule of the long handwritten continuation are restored.',
'The cancelled typed word commutative remains tentative. In the live typed replacement, problem contains an earlier a overtyped by l, now explicitly represented.',
'The lower-left81 is pencil archive foliation. Independent comparison of the centered64 and65 supports regular typewriting, and65 remains plain.'
],summary='Both halves and enlarged typewriter deletions, apostrophe, reference markers, handwritten false start, cancelled the and typed problem repair inspected. The entire long handwritten continuation is retained with its connector and rule. Corrected the false apostrophe deletion to a pen addition, restored the live period, resolved s/to be/the, and retained all genuinely unreadable layers. The degreewise finite-dimensional qualification and final finite-type question remain literal.',differences={
1303:('Note26 naming the Dold-Kan theorem, with pen in before accurate','the typescript reads as our transcription','The entire note is present on the source page; the comparison excerpt contains no corresponding passage.'),
1304:('As was pointed out','the typescript reads as our transcription','Only the first letter A is capital; the following s is lowercase.'),
1306:('non commuative','the arXiv text corrects','The source omits the t of commutative, an isolated typing slip supported by the complete spelling in the surrounding notes. The corrected forms record the supplied t without adding the witness hyphen.'),
1309:('stratified topoi).','the typescript reads as our transcription','The typed terminal period is clearly present.'),
1310:('Complete note29 on the derivator associated to(Hot)','the typescript reads as our transcription','The source contains the whole note, including its section69 reference; it is absent from the selected witness excerpt.'),
1311:('Complete note30 referring to Esquisse and Réflexions Mathématiques1','the typescript reads as our transcription','The source contains this note and its hand quotation marks and underlines; it is absent from the selected excerpt.'),
1316:('At least','the typescript reads as our transcription','The handwritten word contains a distinct e before a: least, not last.'),
1318:('Compare with note24.','the typescript reads as our transcription','The reference and final period are visible at the end of note32 and absent from the witness passage.')
})

project=Path(__file__).resolve().parents[1];p=project/'records/MASTER_VARIANTS_134_2.json';a=json.loads(p.read_text());a=[x for x in a if x['source_id']!='DIFF:1306']
a.append(dict(key='ps_134-2_081',before='non commuative',after='non commutative',kind='slip corrected',reason='The isolated missing t is a typing slip: non commutative is fully spelled in the immediately preceding notes and in the same mathematical usage. The source space is retained, without the witness hyphen.',source_id='DIFF:1306'));p.write_text(json.dumps(a,ensure_ascii=False,indent=2)+'\n')
p=project/'guide_sections/134_2_appendix.tex';s=p.read_text()
if '\\subsection*{Notes 25--32:' not in s:
 s+=r'''
\subsection*{Notes 25--32: Coherence, homotopy invariants, and later references}
Cote 134-2, sites80--81 (folios64--65), finishes the retrospective notes. Note25 broadens uniqueness to account for the choice of a coherator, recalling section13. Note26 corrects the theorem's name to Dold--Kan; note27 connects the earlier structure with Whitehead's crossed modules and with a then forthcoming generalization by Conduché. Note28 records Cox's work on algebraic tubular neighborhoods while explicitly withholding judgment on whether it supplies the precise stratified dévissage machinery proposed in Appendix16. Notes29--30 connect the diagram construction with a derivator and point to tame topology in the Esquisse. Note31 reports a negative answer to the reconstruction question in Appendix18 using simply connected rational homotopy types: the rational cohomology ring alone does not determine such a type. The argument's asserted identification of that ring with all the contemplated data must be distinguished from a statement about any richer, fully specified enhancement of the derived structure; the note does not provide such an enhancement or a comparison theorem. A handwritten addition qualifies the assertion by finite-dimensionality of each cohomology group and asks whether a counterexample remains for a homotopy type of finite type, without defining that latter condition here. The addition begins At least, not the witness At last. Its long connector, cancelled false start, and reference-marker layers are retained. The apostrophe in it's is an authorial pen addition, not a deletion, so the witness's its fails to preserve his final spelling. Note32 substitutes the derivator formulation for an earlier description of the non-commutative problem and recalls note24. These qualifications provide the author's later perspective on the letters and should accompany their claims about reconstruction, uniqueness and homological algebra.
'''
 p.write_text(s)
