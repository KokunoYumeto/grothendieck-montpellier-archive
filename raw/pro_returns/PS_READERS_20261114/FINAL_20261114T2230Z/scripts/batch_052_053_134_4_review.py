import sys
sys.path.insert(0,'PS_READERS_WORK/scripts')
from review_134_3_4 import save_review
key='ps_134-4_052';edits=[
 [r'\inserted{In fact}\xout{\illegible{1}}',r'\inserted[typed]{In fact} \xout{and hence}','In fact is typed above the readable machine-cancelled and hence.'],
 ['gene\\xout{r}\nrating','gene'+r'\xout{\unsure{r}}'+'%\nrating','The cancelled terminal r-like cell is clipped at the edge and remains doubtful. Join the physical continuation gene/rating without a false word space.'],
 ['ect I is',r'ect \over[typed]{X}{I} is','The live capital I has an older regular X impression beneath it.'],
 [r'\xout{co}connected',r'\deleted{\xout{co}}connected','The old co is additionally crossed by heavy irregular pen strokes over the machine cancellation.'],
 [r'\xout{\illegible{1}} Conversely\inserted{(cf.\ page 130),}',r'\xout{On the} Conversely \inserted{(cf.\ page 130)},','On the resolves beneath the strike. The comma is the existing typed comma after Conversely, outside the inserted parenthesis; restore its provenance and the parenthetical word space.'],
 ['If M admits even',r'If \over{M}{M} admits even','The capital M is retraced in pen over the typed M.'],
 [r'invol\xout{v}ved',r'invol\xout{\unsure{v}}ved','The struck extra cell is heavily blackened; its v reading remains only tentative.'],
 [r"\xout{In case (ii')}"+'\ncessary',r"\xout{In case (ii')}"+'%\ncessary','Join the physical ne/cessary continuation across the cancelled interlinear material so its removal cannot introduce an internal word space.'],
 ['The corresponding statements',r'T\over[typed]{h}{H}e corresponding sta\over[typed]{o}{t}ements','The has a regular H over h. The second t of statements is typed over a visible round o.'],
 ['2) The name',r'2) T$\overset{\hand{\scriptscriptstyle\perp\perp}}{\over{\mathrm h}{\mathrm h}}$e name','Paired upper pen marks and a small lower h-shaped retracing surround the typed h of The.'],
 [r'\xout{fx}',r'\xout{f\illegible{1}}','The initial old f is legible, but the following crossed cell is not securely an old x.'],
 ['we get a generating set',r'we get a gen\over[typed]{e}{e}rating set','The second e of generating has displaced repeated type impressions.']
]
save_review({'key':key,'edits':edits,'diffs':{
 4090:['object I, typed over X','The live I is secure, while the older X is retained in its typed overprint layer.'],
 4094:['capital Pi with subscript o','The sign has two straight upright legs and a single long top bar; retain the source capital Pi representation.'],
 4099:['this condition is equally','Is is plainly typed, not the witness es.'],
 4100:['corresponding higher notions','The source ends corresponding without ly.'],
 4101:['capital Pi with subscript n','The large penned sign has the capital-Pi form, not a newly supplied lowercase glyph.'],
 4106:['delta_o, delta_1','The deltas are penned and the first typed subscript is a small round o-shaped cell.']
 },'illegible':[
 ['and hence','All lower letters of and hence are readable beneath the machine row.'],
 ['On the','The initial capital O, n, space and the are readable through the strike.']
 ],'notes':[
 'The edge cell after gene is crossed and clipped; r remains tentative. Its physical continuation rating is joined mechanically.',
 'The old phrase is and hence, now resolved; In fact above it is typed.',
 'The bold I is a regular typed I over X. The j of object is penned over typed j, as encoded.',
 'The extra involved cell remains tentatively v. In the lower statements the second t overlies a typed o, while the second e of generating is repeated typing. The neighboring The patches and retraced M are also recorded.',
 'The handwritten folio 52 is present at lower left.'
 ],'evidence':'Both original halves and eleven enlarged panels inspected. In fact is typed and its old and hence resolves. The terminal r-like cell of gene is clipped; the continuation is joined without inventing a hyphen. I is typed over X. The cancelled co has both typewriter and pen cancellation, while and and the opening parenthesis have distinct pen strokes. On the resolves before Conversely; cf. page 130 has its own actual parentheses, with the following comma belonging to the typed baseline. M is pen-retraced. The involved extra cell remains tentative v. The has typed H over h in the corresponding-statements sentence, and that sentence has typed t over o. The name has paired upper pen marks and lower h retracing. The second e of generating is repeated typing. Capital Pi forms, the index set {0,3,4}, the Hom_3 indices and the rewritten final Remark are preserved. A mechanical continuation repair prevents a space inside necessary when the crossed interlinear phrase disappears.'})

key='ps_134-4_053';edits=[
 [r'\xout{4x}',r'\xout{4\illegible{1}}','The first cancelled cell is visibly 4, but the next lower cell cannot be read as an old x.'],
 [r'\unsure{universal}',r'univers\unsure{al}','The initial univers resolves beneath the machine row; the ending touches the clipped right edge and remains doubtful.'],
 ['the common  connected',r'the \over{co}{co}mmon  connected','The initial co is retraced in pen over its typed letters.'],
 ['the\ncanonical homotopy',r'the'+'\n'+r'ca\over[typed]{j}{n}onical homotopy','The first n of canonical is typed over a j, whose dot and lower hook remain visible.'],
 ['using connected intervals',r'using \over{co}{co}nnected intervals','Both initial co letters are retraced in pen over type.'],
 ['the familiar homotopy',r'the familiar ho\over[typed]{\unsure{t|m}}{m}otopy','The m has a displaced tall lower impression; t or repeated m remains uncertain beneath the live typed m.'],
 [r'W\subset Fl(M)',r'W\hand{\subset} F\over{l}{\ell}(M)','The inclusion is pen-drawn, and the typed l is crossed by a pen slash.'],
 [r'are \xout{xxxx} O-connected',r'are \xout{zero} O-connected','The old z-e-r-o sequence is legible under the typewriter cancellation.'],
 ["I'll assume",r"I'\xout{ll} assume",'The two l cells have regular diagonal x forms with top and bottom type bars. They are machine-cancelled, while the apostrophe is untouched and remains. Independent inspection confirms the cancellation.'],
 [r'(for simpli-',r'(\over{fo}{fo}r simpli-','The f and o of for are pen-retraced over type.'],
 ['M totally O-connected)',r'M totally O-\over{co}{co}\over{p}{n}\unsure{\over{n}{n|h}}e\over{c}{c}ted)','Several connected letters are pen-retraced. The first n overlies a typed p; the following tall n/h-like layer remains doubtful instead of being silently regularized.'],
 ['correspond at all',r'correspond \over{at}{at} all','Both a and t are retraced in pen over the typed word.'],
 [r'\xout{xxxxx}``',r'\xout{zero}``','The second old zero resolves beneath the machine row; the further x impression falls in the space before the quotation mark.']
]
save_review({'key':key,'edits':edits,'diffs':{
 4110:['the very first thing','Very is explicitly typed and remains live.'],
 4112:['Now let','Both words are clearly typed at the display introduction.'],
 4114:[r"I'\xout{ll} assume",'The two l letters are clearly machine-cancelled, leaving the visible untouched apostrophe after I. Do not silently adopt the witness I without its apostrophe.'],
 4120:['all that remains is','The final s is plainly typed in remains.']
 },'unsure':[[r'univers\unsure{al}','Univers resolves under the strike, while the final al is at the clipped edge and remains doubtful.']],
 'illegible':[
 [r'\illegible{1}','The old run beside the live subscript M is crossed by typing and a thick pen patch; no complete lower letters can be recovered.'],
 [r'\illegible{1}','The run immediately following O-connected is obscured by combined machine and pen strokes.']
 ],'notes':[
 'O-connected is typed above the line, and its placing curve leaves the following the live; there is no independent cancellation through the.',
 'The old univers is readable, but the final al is clipped and remains doubtful.',
 'The Fl l has a separate pen slash; the displayed inclusion is also handwritten.',
 'The short run after the live h_M index is still unreadable beneath the combined type and pen crossing.',
 'The two ll cells have regular diagonal x strokes and their typographic bars, confirming machine cancellation. The apostrophe remains live. Independent inspection agrees.',
 'The old run after O-connected remains unreadable. For is retraced, and the later connected contains several pen corrections with a retained n/h-layer doubt.',
 'Both comparison signs and the localization arrow are handwritten, as encoded.',
 'The pencil folio 53 is present at lower left.'
 ],'evidence':'Both original halves and twelve detail panels inspected. The interlinear O-connected is typed; its placing curve does not cancel the. Univers resolves below the old machine row, but its ending is clipped. Common and connected have pen co retracings, canonical has typed n over j, and homotopy has a live m over an uncertain tall lower impression. The displayed inclusion and Fl slash are penned. Both old zero words resolve. The ll of I\'ll has clear machine-x cancellation, confirmed independently; the apostrophe remains untouched, so the source yields I-apostrophe rather than the witness plain I. The old run next to h_M and the one after O-connected remain illegible. For and at are pen-retraced. The later connected has a pen n over typed p and an uncertain following n/h layer, which remains explicit. The source very, Now let and remains are retained.'})
