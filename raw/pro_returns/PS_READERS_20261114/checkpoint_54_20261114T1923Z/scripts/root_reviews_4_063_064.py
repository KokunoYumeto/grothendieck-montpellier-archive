from review_root import review

review('ps_134-4_063',owner='134_4_tail',changes=[
 ('The condition a)',r'T\over[typed]{h}{\unsure{H|h}}e condition a)','A serifed typewriter overprint crosses the h. The final H-like shape versus reinforced h is not securely separable and is now marked.'),
 ('One may object',r'O\over[typed]{n}{\unsure{H|n}}e may object','A regular H-like typewriter overprint crosses the n; retain uncertainty about its final reading.'),
 (r'\deleted{topos A}',r'\xout{topos A}','The letters and intervening spaces are cancelled with regularly spaced typewriter x impressions.'),
 (r'\deleted{of the typ}',r'\xout{of the typ}','Regular typewriter x impressions cancel this run before the handwritten wh replacement.'),
 (r'i\hand{t} occurs',r'i\over{t}{t} occurs','A handwritten t retraces a visibly typed t; the overwritten typed layer is retained.'),
 (r'6\over{\unsure{0}}{1}.',r'\over{6}{6}\over{8}{1}.','The old second digit has two left lobes, visibly 8 rather than 0. The first 6 is also retraced in pen; the live section number is 61.'),
 (r'\over{\illegible{1}}{A}',r'\over{A}{A}','The old typed A remains legible by its serifed feet and crossbar beneath the retraced pen A.'),
 (r'\over{\illegible{1}}{(}1)',r'\over{\unsure{(}}{(}1)','The surviving curve and lower stroke suggest an old parenthesis, but the pen retracing prevents certainty. Narrow the lacuna to an explicit doubtful glyph.'),
 (r'i : A \longrightarrow (Cat)',r'i : A \hand{\longrightarrow} (Cat)','The arrow in (1) is a drawn pen stroke with an irregular head, unlike the typed labels.'),
 (r'i^{*} : (Cat) \longrightarrow A\hat{}',r'i^{*} : (Cat) \hand{\longrightarrow} A\hat{}','The arrow in (2) is handwritten.'),
 (r'i_A : A\hat{} \rightarrow (Cat)',r'i_A : A\hat{} \hand{\rightarrow} (Cat)','The arrow in (3) is handwritten.')
 ],doubts={'unsure':[
 ('8','doubt resolved','The enlarged old digit has two left lobes, not the single oval of 0; the pen 1 crosses its middle.')
 ],'illegible':[
 ('A','illegibility resolved','The old typed A is readable beneath its pen retracing.'),
 (r'\unsure{(}','illegibility narrowed','The old curve probably is an opening parenthesis, but the overlapping ink leaves that reading doubtful.')
 ]},notes=[
 'The h of The and n of One have regular typewriter overprints. Their H-like final forms are now explicitly doubtful rather than unmarked.',
 'The cancellation runs use regularly spaced typewriter x impressions. The final wh is handwritten; both layers are retained.',
 'The three second letters of Fl have a pen diagonal, retained as the original over-l by ell. The unretouched F1 group is left literal; its inclusion is curved like the other subset signs.',
 'The old section digit is 8, crossed by a pen 1; the first 6 is also retraced. The live heading reads 61.',
 'The pen t retraces a typed t, now recorded as an overprint rather than a pure insertion.',
 'The old A is legible beneath retracing. The old opening parenthesis remains doubtful and is narrowed from a whole-word lacuna to that candidate.',
 'The line ending invers is cut at the right edge and is preserved without supplying e; the added closing parenthesis after Cat is visible at the edge.',
 'The lower-left 63 is separate archive foliation.'
 ],summary='Both halves and enlarged section number, overprints and cancellations inspected. Resolved the old section digit as 8 and the overwritten A; retained an uncertain old parenthesis and added two necessary letter-overprint doubts. Three formula arrows are now marked handwritten. The source literal Delta superscript 1, extra closing parenthesis in (4), and clipped invers remain. The false converse from an id-to-constant natural transformation to a final object is discussed in the guide, without a textual mathematical repair.',differences={
 4287:('for the proposition above for a','the typescript reads as our transcription','The typed word is above, not the witness over.'),
 4291:(r'\hand{\Delta}^1','the typescript reads as our transcription','A typed 1 sits above and right of the pen Delta; no superscript minus is visible.'),
 4292:('61.','the typescript reads as our transcription','The source has only its corrected section number; the descriptive heading is a witness addition.'),
 4293:('concerned with a functor','the typescript reads as our transcription','The typed indefinite article a is clear.'),
 4296:(r'\underline{W},\underline{W}\prime\subset\mathrm{F}\over{l}{\ell}(Cat))','the typescript reads as our transcription','The formula visibly has one opening and two closing parentheses after Fl; the witness balances them.')
 })

from pathlib import Path
src64=(Path(__file__).resolve().parents[2]/'inputs/text/transcription/ps_pages/ps_134-4_064.tex').read_text()
arrow_changes=[]
for line in src64.splitlines():
 if line.startswith(r'\[ (5)') or line.startswith(r'\[ (7)'):
  arrow_changes.append((line,line.replace(r'\xrightarrow{\approx}',r'\hand{\xrightarrow{\approx}}'),'The display arrows and their two-wave equivalence marks are handwritten; all object labels remain typed.'))

review('ps_134-4_064',owner='134_4_tail',changes=arrow_changes+[
 (r"f_{\hand{i}}{}'",r'f_{\hand{i}}','The apparent extra mark is the dot of the handwritten subscript i, not a separate typed prime. Enlargement shows the pen letter and its dot.'),
 (r'\xout{\unsure{A to be a}}',r'\xout{A to be a}','The cancelled letters are legible independently beneath the regularly spaced x impressions.'),
 (r'\xrightarrow{i^{*}}',r'\mathrel{\overset{i^{*}}{\hand{\longrightarrow}}}','The first arrow of (6) is drawn in pen, but its i-star label is typed.'),
 (r'\xrightarrow{i_A}',r'\mathrel{\overset{i_A}{\hand{\longrightarrow}}}','The second arrow of (6) is drawn in pen, but its i_A label is typed.')
 ],doubts={'unsure':[
 (r'\unsure{A}','doubt retained','The heavy pen A obscures the interior of its typed base; the base A remains a candidate, not a settled reading.'),
 ('A to be a','doubt resolved','The cancelled words are readable beneath the regular typewriter strikes.')
 ],'illegible':[
 (r'\illegible{1}','illegibility retained','The final cancelled run shows partial i/t-like strokes but does not yield a secure complete word.')
 ]},notes=[
 'The author page 152 is typed, and archive 64 is handwritten.',
 'The first W prime is a small oblique pen stroke, visibly unlike the typed primes that follow.',
 'The supposed prime after f is the dot of the pen subscript i and is removed as a duplicate representation of that letter. The old A beneath the pen A remains doubtful.',
 'The word corresponding is typed above the line with a handwritten placement bracket. The word the is not cancelled.',
 'The word requirement has minor typewriter retouching, but all letters are readable in their stated order.',
 'A to be a is readable beneath its x strikes. The short cancelled run after namely is still not recoverable.',
 'The final d of and is cancelled by irregular pen ink, leaving an; the cancellation is retained.'
 ],summary='Both halves and enlarged f_i, cancelled words and page-foot run inspected. Removed a spurious extra prime that duplicated the dot of the handwritten i; settled the cancelled A to be a. The old A and page-foot cancelled word remain doubtful. Formula arrows and equivalence marks are pen, with typed labels preserved. The stronger equality (8), definition (9), and equivalent condition (10) are complete. The first inclusion formula visibly uses plain W_A; it is not silently underlined.',differences={
 4300:(r'i^{* -1}(W_A),\quad i^{*}(\underline{W}\prime)\subset W_A','the typescript reads as our transcription','Both W_A occurrences in (*) lack underlining, while the surrounding W primes are underlined.'),
 4303:(r'f_{\hand{i}}:','our transcription corrected','The supposed additional prime is the handwritten i dot. The witness and the corrected transcription therefore agree on f_i without a prime.')
 })
