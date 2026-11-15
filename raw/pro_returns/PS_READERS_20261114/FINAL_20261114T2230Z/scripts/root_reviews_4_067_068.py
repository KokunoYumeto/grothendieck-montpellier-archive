from review_root import review
from pathlib import Path
import json

transposition=r'\tikz[baseline=(words.base)]{\node[inner sep=0pt] (words) {using constantly};\draw[blue!65!black] (-1.32,.05) .. controls (-1.45,-.40) and (-.45,-.40) .. (-.20,-.08) .. controls (0,.30) and (1.30,.30) .. (1.35,.15)--(1.35,-.05);}'
src=(Path(__file__).resolve().parents[2]/'inputs/text/transcription/ps_pages/ps_134-4_067.tex').read_text()
changes=[
 (r"\unsure{X'}$\to$ \unsure{X}",r"X'$\hand{\to}$ X",'Both final capitals are legibly typed X, despite overstriking; the first has its visible prime. The connecting arrow is pen.'),
 (r"\inserted{: $X'\to X$}",r"\inserted[typed]{: $X'\hand{\to} X$}",'The added colon and X labels are typed, while the small connecting arrow and placement curve are handwritten.'),
 (r'\inserted{\unsure{I}}',r'\inserted[typed]{\unsure{I}}','The small vertical glyph under the cancelled run has regular typewriter serifs; its exact I/l reading remains uncertain.'),
 (r'\unsure{usin}',r'usin','The four cancelled letters u s i n are individually legible beneath x impressions.'),
 (r'\hand{\unsure{ed}}',r'\hand{ed}','The pen e and descending/ascending curved d are recognizable at the right edge despite clipping.'),
 (r'\hand{\unsure{p}}',r'\hand{p}','The vertical-arrow label has a clear stem and right bowl: handwritten p.'),
 (r'gu\unsure{arantees}',r'guarantees','All letters of guarantees are readable through the typewriter retouching in enlargement.'),
 (r'\inserted{u:}',r'\inserted[typed]{u:}','The added u and colon use the same regular typewriter face as the line below; the bracket is pen.'),
 (r'\begin{tikzcd}',r'\begin{tikzcd}[every arrow/.append style={draw=blue!65!black}]','All four square arrows are drawn in pen; the objects and cancelled old label remain typed.'),
]
# The source uses ordinary apostrophes in this editorial description.
changes.extend([
 (r'Y_{\unsure{\hand{x}}}\to X',r'Y_{\unsure{\hand{x}}}\hand{\to} X','The arrow from Y to X is drawn with a pen shaft and filled head; its adjacent doubtful lower mark is unchanged.'),
 (r"$F'\to F$",r"$F'\hand{\to} F$",'The bottom arrow from F-prime to F is handwritten; the capital labels and prime are typed.'),
 (r'i^{*}(\underline{Fl}(C)) \arrow[r]',r'i^{*}(\underline{F\over{l}{l}}(C)) \arrow[r]','The typed l in the square is retraced by a long oblique pen stroke.'),
 (r'\[ \underline{Fl}\,(C)',r'\[ \underline{F\over{l}{l}}\,(C)','The typed l in the defining formula has a long pen retracing.')
])
changes.append((r"\margin{transposition marks around ``using'' and ``constantly'': read ``constantly using''}using constantly",transposition,'Replace an editorial prose description of the source marks by the visible pen transposition curve at its actual words. The corrected word order is encoded separately in the master variant.'))
for line in src.splitlines():
 if (r'\to' in line or r'\longrightarrow' in line or r'\xrightarrow' in line) and not any(x in line for x in [r'\unsure{X',r'\inserted{:',r'\xout{\illegible',r'map\inserted']):
  after=line.replace(r'\to',r'\hand{\to}').replace(r'\longrightarrow',r'\hand{\longrightarrow}').replace(r'\xrightarrow{\ t\ }',r'\mathrel{\overset{\ t\ }{\hand{\longrightarrow}}}')
  after=after.replace(r'\underline{Fl}',r'\underline{F\over{l}{l}}')
  if after!=line:changes.append((line,after,'The connecting arrow is visibly drawn in pen; the l in Fl is also retraced with an oblique pen stroke where present. Other labels remain typed.'))
review('ps_134-4_067',owner='134_4_tail',changes=changes,doubts={'unsure':[
 ("X'",'doubt resolved','The final capital and prime are legible; no independent earlier letter can be recovered from the retouching.'),
 ('X','doubt resolved','The final typed capital X is clear.'),
 (r'\unsure{"asph}','doubt retained','The opening quote and first cancelled letters have overlapping pen and typewriter strokes; the whole proposed run remains uncertain.'),
 (r'\unsure{\hand{x}}','doubt retained','The small lower mark beneath Y has overlapping strokes and does not securely settle its glyph or exact relation to Y.'),
 (r'\unsure{I}','doubt retained','The regular serifed lower vertical mark may be I or l; its glyph stays doubtful, with its typed provenance corrected.'),
 ('usin','doubt resolved','The cancelled letters usin are readable independently.'),
 ('ed','doubt resolved','The visible pen strokes at the right edge resolve the ending as ed.'),
 (r'\unsure{x}','doubt retained','The small old top-arrow label is crossed by the drawn shaft and an overstrike; x remains uncertain.'),
 ('p','doubt resolved','The pen label has a clear right bowl and descender.'),
 ('arantees','doubt resolved','The letters of guarantees can be traced individually despite retouching.')
 ],'illegible':[
 (r'\illegible{1}','illegibility retained','Dense pen cancellation after c) conceals the old character.'),
 (r'\illegible{1}','illegibility retained','The cancelled run before f_Y has overlapping letters and strikes that do not yield a secure complete expression.'),
 (r'\illegible{1}','illegibility retained','The old character after category is blackened by pen hatching.')
 ]},notes=[
 'The final X prime and X are readable typed capitals; the u and arrow are handwritten. The earlier overtyped letters are not recoverable as separate content.',
 'The old sign after c) remains unreadable; its replacement comma is clearly pen.',
 'The lower mark by Y remains doubtful. The lower serifed I-like mark near f_Y is typed rather than pen, but its glyph remains uncertain.',
 'The cancelled opening quote/asph run remains uncertain because of overlapping strokes.',
 'The cancelled run before making is clearly usin.',
 'The right-arrow label is clearly handwritten p. The small top-arrow old label remains doubtful beneath its crossing strokes.',
 'Guarantees is legible after enlargement; the cancelled sign after category remains unreadable.',
 'The lower-left 67 is handwritten archive foliation.'
 ],summary='Both halves and seven enlarged details inspected. Settled six original doubtful readings, retained four doubts and all three lacunae, corrected typed interlinear insertions and marked pen arrows. Replaced the editorial prose description of the using/constantly transposition with the source curve and a recorded master transposition. The slice/fiber-product lemma, t as target map, and condition (14) remain intact. Literal f_Y, Y lower mark and plain W_A are preserved.',differences={
 4354:(r'c)\deleted{\illegible{1}}\hand{,}','the typescript reads as our transcription','The blackened old sign and pen comma both remain visible.'),
 4358:(r'\xout{\unsure{"asph}}','the typescript reads as our transcription','The old run is visibly cancelled; its unresolved reading is not silently discarded.'),
 4359:(r'Y_{\unsure{\hand{x}}}\to X','the typescript reads as our transcription','A small lower mark is present by Y and stays doubtful; the witness drops it.'),
 4360:(r'\xout{\illegible{1}}\inserted[typed]{\unsure{I}}','our transcription corrected','The old cancelled run and lower I-like mark remain, with the latter corrected to typed provenance.'),
 4362:('can be stated, saying that','the typescript reads as our transcription','The source uses a comma, with no as.'),
 4363:(r'\uline{a weakly} W-\uline{aspheric} \uline{map} \uline{in} (Cat) \uline{is in} W','the typescript reads as our transcription','The separate pen underlines do not form the witness single emphasis span.'),
 4368:(r'\hand{p}','our transcription corrected','The label is settled as handwritten p, which the witness omits.'),
 4369:(r'\xout{\unsure{x}}','the typescript reads as our transcription','The old top-arrow mark is visible but still doubtful; the witness has no label.'),
 4376:('plain W_A-aspheric','the typescript reads as our transcription','This W_A lacks underlining in the source.'),
 4378:('using constantly with a pen transposition to constantly using','our transcription corrected','The diplomatic form now carries the actual graphic, while the master applies the author transposition in both corrected forms.')
 })
vp=Path(__file__).resolve().parents[1]/'records/MASTER_VARIANTS_134_4_tail.json'
variants=json.loads(vp.read_text()) if vp.exists() else []
variants=[v for v in variants if v['source_id']!='DIFF:4378']
variants.append(dict(key='ps_134-4_067',before=transposition,after='constantly using',kind='author transposition',reason='The pen exchange curve interchanges using and constantly; the diplomatic form preserves their typed order and curve.',source_id='DIFF:4378'))
vp.write_text(json.dumps(variants,ensure_ascii=False,indent=2)+'\n')

review('ps_134-4_068',owner='134_4_tail',changes=[
 (r'\over{W}{\mathbb{W}}',r'\over{W}{W}','The pen retraces an ordinary W; the extra visible strokes are the old typed letter, not an independently drawn blackboard-bold symbol.'),
 ('6.3.',r'\hand{6.3.}','The date uses freehand numerals and round pen dots, visibly unlike the typewriter page heading.'),
 (r'\hand{for} \xout',r'\over{for}{for} \xout','The handwritten for retraces a legible typed for; preserve both layers.'),
 (r'\inserted{retraction}',r'\inserted[typed]{retraction}','Retraction is a regular typed interlinear addition with a pen placement bracket.'),
 (r'\inserted{a} final',r'\inserted[typed]{a} final','The added article a is typed above the line and placed by a pen slash.'),
 (r'(\hand{*})',r'(*)','The asterisk has the regular horizontal and diagonal typewriter strokes of the surrounding typed label, not freehand rays.')
 ],doubts={'unsure':[
 (r'\unsure{weak|wrak}','doubt retained','The second letter has overlapping e/r strokes in enlargement; the intended word is clear from context but the final typewriter reading is not independently settled.')
 ]},notes=[
 'The original typed W remains visible beneath pen retracing. It is an ordinary W, not a newly introduced blackboard-bold notation.',
 'The e/r overprint in weak remains uncertain after enlargement; context is not used to suppress the mark.',
 'A typed for is readable beneath the handwritten retracing and is now represented as its base.',
 'The formula arrows and Deltas are pen. The star in (*) has regular typewriter strokes and is corrected to the typed layer. Retraction and a are also typed additions.',
 'The lower-left 68 is handwritten archive foliation, distinct from the author section number 62 and the date 6.3.'
 ],summary='Both halves and five enlarged details inspected. Corrected the W retracing, date and typed asterisk layers, restored the typed for beneath pen, and identified two typed insertions. One weak/wrak doubt remains. The source date is 6.3., unlike witness 6.4.; the author explicitly abandons the two-independent-localizer attempt and assumes W=W prime. The restricted axiom list a)c)e)f), excluding b), is preserved.',differences={
 4379:(r'\underline{W}=\over{W}{W}_{(Cat)}','our transcription corrected','The right W is ordinary typed W retraced in pen; blackboard-bold notation was a transcription artifact.'),
 4381:('6.3.','the typescript reads as our transcription','The handwritten final digit is 3; the witness date 6.4. is not adopted.'),
 4382:('section number 62 only','the typescript reads as our transcription','No descriptive section title is present; the witness heading is editorial.'),
 4383:(r'\margin{62}','the typescript reads as our transcription','The handwritten 62 is visible at the paragraph opening.'),
 4389:(r'\inserted[typed]{retraction}','our transcription corrected','The interlinear addition is typed and placed by a pen bracket.'),
 4390:('of last corollary','the typescript reads as our transcription','The typed phrase has no the before last.'),
 4399:(r'\inserted[typed]{a}','our transcription corrected','The interlinear article is typed, with a pen placement slash.')
 })
