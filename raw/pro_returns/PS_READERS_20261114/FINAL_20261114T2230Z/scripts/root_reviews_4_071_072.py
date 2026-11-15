from review_root import review
from pathlib import Path

oldnote=r'\margin{\unsure{this impression} is \unsure{irrelevant} -- it would be \unsure{rather the biggest}, if one extra \unsure{property} on W is \unsure{made} -- \unsure{need} added}'
newnote=r'\margin{this impression is incorrect -- it would be rather the \unsure{biggest} if one extra \unsure{requirement} on $\underline{W}$ is added}'
review('ps_134-4_071',owner='134_4_tail',changes=[
 (r"won\unsure{\hand{'}}t",r"won\hand{'}t",'The apostrophe is a clear curved pen stroke above the space before t.'),
 (oldnote,newnote,'Rotation and an independent second inspection establish this impression is incorrect, not irrelevant, and is added, not made--need added. Require-/ment is divided across two lines. Biggest and the overlapped first part of requirement remain marked; the underlined W is restored.'),
 (r'comp\over{\unsure{b}}{l}exes',r'comp\over{b}{l}exes','The typed b retains a visible lower bowl beneath the looped pen l.'),
 (r'\inserted{usual}',r'\inserted[typed]{usual}','The interlinear usual is typed with regular serifs and placed by a handwritten curve.'),
 (r'\hand{t}he internal',r'\over{t}{t}he internal','The pen t retraces the typed t, whose crossbar and lower stem remain visible.'),
 (r'\hand{e}qui-',r'\over{e}{e}qui-','The dark pen e retraces a typed e rather than filling a completely blank place.'),
 (r'resu\hand{l}t',r'resu\over{\unsure{l}}{l}t','The pen l covers a typed letter. Its earlier l-like stem is not sufficiently exposed to settle the base, now explicitly retained as doubtful.')
 ],doubts={'unsure':[
 (r"\hand{'}",'doubt resolved','A full curved pen apostrophe is visible.'),
 ('this impression','doubt resolved','Both words are readable in the rotated margin crop and independently confirmed.'),
 ('incorrect','doubt resolved with corrected reading','The letter sequence is incorrect; irrelevant is unsupported by the image.'),
 (r'rather the \unsure{biggest}','doubt narrowed','Rather the is clear. Biggest is the best reading, independently supported, but its middle/end overlap printed body text and remain marked.'),
 (r'\unsure{requirement}','doubt revised','The word is divided require-/ment, not property. The overlapped first part remains doubtful although ment is clear.'),
 ('is added','doubt resolved with corrected reading','The marks read is followed by added on the next line; made is not a separate word.'),
 ('added','doubt resolved with corrected reading','The final word added is clear. The supposed need was part of the missegmented preceding require-/ment line.'),
 (r'\unsure{the}','doubt retained','Several typewriter impressions overlap in all three cells; a final live the is plausible but cannot be securely separated from the overprint.'),
 ('b','doubt resolved','The old lower bowl under the pen l is visible and belongs to typed b.'),
 (r'\unsure{2}','doubt retained','The heavy pen 3 obscures the old section digit; its proposed 2 remains uncertain.')
 ]},notes=[
 'The entire margin note was rotated, enlarged and independently inspected. It says this impression is incorrect and ends is added. Require-/ment is split across lines; biggest and the overlapped first part of requirement remain doubtful. The underlined W is preserved.',
 'The apostrophe in won\'t is clearly handwritten and is now settled.',
 'The word before other categories contains regular typewriter overprints, not an established pen deletion; its uncertainty remains.',
 'Conditions is legible despite a small retouch near d; no separate insertion or cancellation is established.',
 'The t and e are pen retracings of typed letters. The added opening parenthesis before Hot is pen.',
 'The right-edge splits interp/preted and correspon/dingly are preserved as supplied; no hidden text is reconstructed.',
 'The old second section digit remains uncertain beneath the pen 3; the live section number is 63.',
 'The pen l of result covers an earlier typed glyph; its l-like base is now marked doubtful instead of omitted.',
 'The lower-left 71 is handwritten archive foliation.'
 ],summary='Both halves, the full rotated marginal note and five enlarged details inspected. The margin materially revises the speculation: this impression is incorrect, with rather the biggest under an extra requirement, instead of the draft irrelevant/property/made--need wording. Two words remain doubtful where body typing crosses them. Resolved the apostrophe and old b, corrected typed usual, and retained the old section digit and dark the doubts. The new old-letter doubt in result records an omitted base. Simple homotopy types and the adjacent double-line/X marginal emphasis are preserved.',differences={
 4437:(newnote,'our transcription corrected','The complete note was reread after rotation and independently checked. The corrected wording challenges the smallest-class speculation; the witness omits the note.'),
 4439:(r'\unsure{the} other categories','the typescript reads as our transcription','The overtyped three-cell word remains visible and doubtful; the witness omits it.'),
 4440:('weaker than the so-called','the typescript reads as our transcription','The article the is fully typed.'),
 4442:(r'\inserted{possibly}','the typescript reads as our transcription','The pen possibly is present and prevents the speculation from becoming an unqualified assertion.'),
 4443:(r'\inserted[typed]{usual}','our transcription corrected','The interlinear usual is typed, with a pen placement curve.'),
 4448:(r'\margin{$\|$ \quad X}','the typescript reads as our transcription','The double vertical emphasis and X stand beside the simple-homotopy discussion.'),
 4449:('63.','the typescript reads as our transcription','The source has its numbered opening but no descriptive heading.')
 })

src=(Path(__file__).resolve().parents[2]/'inputs/text/transcription/ps_pages/ps_134-4_072.tex').read_text()
changes=[
 (r'F\unsure{\hand{$\dagger$}}irst',r'F\unsure{\ensuremath{\underset{\text{.}}{\overset{+}{\mathrm{i}}}}}rst','The regular cross is above the i, and a separate dot sits below it. Preserve that uncertain composite at its actual letter rather than inserting a baseline pen dagger before i.'),
 (r'A\unsure{\over{;}{,}};',r'A\over[typed]{\unsure{;}}{,}','The final comma is visible below a typewriter x overstrike on the old upper punctuation. Remove the duplicated extra semicolon, preserving uncertainty about the old semicolon.'),
 (r'\deleted{W-aspheric if}',r'\xout{W-aspheric if}','Regularly spaced typewriter x impressions cancel the whole phrase; it is not a pen cancellation.'),
 (r'ob\unsure{\hand{j}}ect',r'ob\over{j}{j}ect','The pen j has a clear long curved descender over the typed j, whose upper stem remains visible.'),
 (r'\unsure{\over{c}{c}}ourse',r'\over{c}{c}ourse','The pen c is a clear open curve over a visible typed c.'),
 ('The thing',r'T\over[typed]{h}{\unsure{H|h}}e thing','The h has regular upper crossbar/vertical overprinting, matching the recurring H-like typewriter retouch. The final H/h state remains uncertain.'),
 ('The terminology',r'T\over[typed]{h}{\unsure{H|h}}e terminology','The second The has the same regular H-like overprint; retain both the layer and its uncertainty.')
]
for line in src.splitlines():
 if any(x in line for x in [r'\longrightarrow',r'\to',r'\mathrm{Fl}']):
  after=line.replace(r'\longrightarrow',r'\hand{\longrightarrow}').replace(r'\to',r'\hand{\to}').replace(r'\mathrm{Fl}',r'\mathrm{F}\over{l}{\ell}')
  if line.startswith('(meaning that'):
   after=after.replace(r'e$ is W-aspheric',r'e$\deleted{\unsure{)}} is W-aspheric')
  changes.append((line,after,'The arrows and the diagonal strokes on Fl are pen. At the first explanatory map X to e, a blackened old closing-parenthesis-like glyph is separately retained as a doubtful cancellation.'))
review('ps_134-4_072',owner='134_4_tail',changes=changes,doubts={'unsure':[
 (r'\unsure{\ensuremath{\underset{\text{.}}{\overset{+}{\mathrm{i}}}}}','doubt retained with graphic corrected','The mark is a cross above i with a separate dot below; its interpretation is uncertain, but it is not a free-standing baseline dagger.'),
 (r'\unsure{\deleted{w}here|where}','doubt retained','The dense pen ink on w may be cancellation or retracing; its final status is not securely determined.'),
 (r'\over[typed]{\unsure{;}}{,}','doubt narrowed and transcription corrected','The final comma is clear; the old upper punctuation is crossed by a typewriter x and remains a doubtful semicolon.'),
 (r'\unsure{\over{o}{e}}','doubt retained','The dark loop has a small central bar but does not securely establish the earlier/later o/e order.'),
 (r'\unsure{say a map}','doubt retained','The last a map is readable, but the first two letter cells of the old run are covered by x impressions.'),
 (r'\over{j}{j}','doubt resolved','The curved descender establishes j, and the original typed upper stem remains visible beneath it.'),
 (r'\unsure{say W}','doubt retained','The short cancelled run is heavily overtyped; its full wording remains uncertain.'),
 (r'\over{c}{c}','doubt resolved','Both the pen open curve and its typed c base are visible.')
 ]},notes=[
 'First has a regular cross above i and a dot below it; the uncertain composite is now located on i. Both lower occurrences of The have H-like typewriter overprints, now represented with explicit final-letter doubts.',
 'The heavy ink on w does not securely distinguish deletion from retracing; the original where/here alternatives remain.',
 'Terminology we have is legible under regular x strikes. The old say a map and say W runs remain uncertain in their obscured initial cells.',
 'W-aspheric if is cancelled by regular typewriter x impressions, now correctly classified.',
 'The right-margin abbreviation reads i.e., followed by the complete pen insertion X to e is in W; it is not the witness abbreviation &c.',
 'The lower-left 72 is handwritten archive foliation.'
 ],summary='Both halves and eight enlarged details inspected. Corrected the First composite, duplicated punctuation, cancellation mechanism and pen retracings. Restored the omitted blackened glyph after the first explanatory X-to-e map and the two H-like retouches, with doubts where needed. All arrows and Fl pen strokes are marked. The text distinguishes W-aspheric objects from maps universally in W, proposes W-objects and M(W), then rejects its new terminology in the complete marginal note. No terminology is standardized in the source.',differences={
 4454:(r'A\over[typed]{\unsure{;}}{,}','our transcription corrected','The duplicated terminal semicolon was not on the page. The live comma and cancelled old punctuation are now represented once.'),
 4456:('an object such that','the typescript reads as our transcription','No X is printed after object; the witness supplies it.'),
 4463:(r'\hand{i.e.} \inserted{$X\hand{\to}e$ is in W,}','the typescript reads as our transcription','The source spells out the condition and introduces it with i.e.; the witness replaces it by &c.'),
 4471:('all those objects','the typescript reads as our transcription','The demonstrative is those, not these.'),
 4472:(r'M\hand{)},','the typescript reads as our transcription','The handwritten closing parenthesis and typed comma are both visible; the witness omits the parenthesis.')
 })
