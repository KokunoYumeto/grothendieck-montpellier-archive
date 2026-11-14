import sys,re
sys.path.insert(0,'PS_READERS_WORK/scripts')
from review_134_3_4 import save_review,TEXT

key='ps_134-4_016';src=(TEXT/'transcription/ps_pages'/f'{key}.tex').read_text();edits=[]
for line in src.splitlines():
 if line.startswith('%'):continue
 new=line.replace(r'\longrightarrow',r'\hand{\longrightarrow}').replace(r'\to',r'\hand{\to}')
 for sub in [r'\underline{I}',r'\underline{J}',r'\underline{I}_0','W']:
  new=new.replace(r'\underset{'+sub+r'}{\sim}',r'\underset{'+sub+r'}{\hand{\sim}}')
 if line.startswith(r'\[ \hand{\delta'):
  new=r'\[ \hand{\delta}^{\underline{I}}_0 \underset{\underline{I}_0}{\hand{\sim}} \hand{\delta}^{\underline{I}}_1 \qquad . \]'
 if new!=line:edits.append(['\n'+line+'\n','\n'+new+'\n','The arrows, deltas and homotopy tildes are penned. In the endpoint display the interval letters and their indices are typed, so the whole formula must not be classified as handwriting.'])
edits += [
 [r'\unsure{,|.}',',','The low curved tail resolves the punctuation as a comma.'],
 [r'\inserted{canonical}',r'\inserted[typed]{canonical}','Canonical is typed above the line, with a separate pen placing hook.'],
 [r'\xout{where $H = H_M = W^{-1}M$}',r'\xout{where $H$ \unsure{is} $= H_M = W^{-1}M$}','An additional i-like typed impression and obscured following cell stand between H and the equals sign beneath the x row; retain the tentative is rather than omit the visible cells.'],
 [' .  There  is',' .  T'+r'\over[typed]{H}{h}'+'ere  is','There has displaced H/h type impressions.'],
 [r'\uline{Remark}.  In',r'\uline{R\over[typed]{E}{e}mark}.  \over[typed]{I}{I}n','Remark has an old capital E behind the lowercase e; the following I is repeated in displaced typing.'],
 ['More generally',r'M$\overset{\hand{\unsure{\smile}}}{\underset{\hand{\wedge}}{\mathrm o}}$re generally','The typed o has a small pen caret below and an irregular cup-like pen mark above; preserve the latter as a graphic doubt.'],
 ['Fl(M),',r'F\over{l}{l}(M),','The l is retraced in pen over a typed l.'],
 ['in Fl(M)',r'in F\over{l}{l}(M)','The second l likewise has a long slanting pen retrace over its typed form.'],
 [r'\underline{I} = (I,',r'\underline{I} \over{\unsure{b}}{=} (I,','Two pen horizontal bars cover an older b-like typed cell; retain the uncertainty of that older cell.'],
 [r'\inserted{of M}',r'\inserted[typed]{of M}','Of M is typed above the line and located by a pen placing curve.'],
 [r'$M_{\underline{I}}$ , i.e. \hand{',r'$M_{\underline{I}}$ , \hand{i.e. ','The i.e. is part of the handwritten end-of-line addition.'],
 [r'$\underline{I}_0$  in M ,',r'$\underline{I}_0$  in \over{M}{M} ,','The capital M is retraced in pen over the typed M.'],
 [r'\xout{\illegible{1}}',r'\xout{call}','The c, a and two tall l cells remain readable beneath the machine x strikes.'],
 [r'\xout{\illegible{2}}',r'\xout{to check if}','The older phrase to check if is recoverable beneath the typed cancellation row.'],
 [r'\xout{\illegible{3}}',r'\deleted{\xout{if there exis\illegible{1}}}','The old if there exis is legible under both a machine x row and a later pen strike; the terminal cells remain obscured.'],
 [r'\deleted{one}\inserted{the,}',r'\inserted[typed]{\over[typed]{T}{t}he} one','One has no independent cancellation. The is typed above it with a displaced T/t first cell; the apparent comma belongs to the placing hook.']
]
save_review({'key':key,'edits':edits,'diffs':{
 3398:[r'\delta_i^{\underline I}:e\to\underline I','The endpoint target has its own underline, which is absent from the witness reading.'],
 3405:['is implied by all','The final d is visible. The witness is implies is not the page reading.'],
 3408:['can be checked','The source has the full checked, including ed.'],
 3409:['the one and unique','The scan leaves one live; the typed the and its placing hook were mistaken for a replacement and deletion in the initial draft.','correct transcription cancellation'],
 3411:['M=(Cat)','Both parentheses are present, with the closing one penned.']
 },'unsure':[[',','The low tail distinguishes a comma from a full stop.']],
 'illegible':[
 ['call','All four letter bodies remain readable beneath the x row.'],
 ['to check if','The separate words and their surviving letter contours are recoverable.'],
 [r'if there exis\illegible{1}','The opening words are readable, but the final cells beneath the pen strike are not securely recoverable.']
 ],'notes':[
 'The punctuation after J-homotopic resolves to a comma on enlargement.',
 'The membership signs are penned, including the whole handwritten final clause of the Remark.',
 'The deltas, tildes and Delta are penned. The interval letters and indices in the endpoint formula are typed; their provenance is separated.',
 'There is H/h typed overlap; Remark is E/e typed overlap. More has an irregular upper pen mark and a lower caret, retained graphically with doubt in the upper form.',
 'The cancelled call and to check if are recovered. The third phrase reads if there exis with an unreadable ending under both machine and pen cancellation.',
 'The lower-left 16 is handwritten. Canonical, of M and the are typed interlinear additions; one is live beneath the last placing curve.'
 ],'evidence':'Both original halves and thirteen enlarged detail panels inspected. The first doubtful punctuation is a comma. Canonical and of M are typed additions, not pen words. The first cancelled localization formula contains an additional uncertain is-like pair of cells. There has H/h typing, Remark E/e, and In a repeated I. More carries separate pen marks above and below o, with the upper form retained as doubtful. Both Fl occurrences have pen-retraced l. The defining equals sign covers an uncertain b-like cell; the later M is pen-retraced. The cancelled call and to check if are readable, while if there exis has an obscured ending. The final the is a typed insertion with T/t overlap. Its curved hook does not cancel one. The underlined endpoint target, is implied, checked and the Cat parentheses were compared directly with their required difference rows.'})

key='ps_134-4_017';src=(TEXT/'transcription/ps_pages'/f'{key}.tex').read_text();edits=[]
for line in src.splitlines():
 if line.startswith('%'):continue
 new=line.replace(r'\longrightarrow',r'\hand{\longrightarrow}').replace(r'\to',r'\hand{\to}').replace(r'\leqslant',r'\hand{\leqslant}')
 if new!=line:edits.append(['\n'+line+'\n','\n'+new+'\n','The directional arrows and preorder comparison sign are handwritten.'])
edits += [
 [r'se\unsure{c}tions',r'se\unsure{\over[typed]{v}{c}}tions','The crowded cell has v-like diagonals and a c-like curved layer; neither the old letter nor the layer order is secure enough to remove doubt.'],
 ['expect in',r'e\over{x}{x}pect in','The x is heavily retraced in pen over a typed x.'],
 [r'on F\unsure{l}(M) ,',r'on F\over{l}{l}(M) ,','The letter is a typed l with a long slanting pen retrace, matching the later occurrence.'],
 [r'on F\unsure{l}(M),',r'on F\over{l}{l}(M),','The second l has the same typed foot and pen retrace.'],
 [',,there is',r',,\over[typed]{t}{t}here is','The first t has a displaced repeated type impression. The two preceding commas remain distinct and are retained.'],
 ['intervals. Indeed,','intervals. I'+r'\over[typed]{n}{n}'+'deed,','The n has a lower displaced typed repetition.'],
 [r'\inserted{or union}',r'\inserted[typed]{or union}','Or union is typed above the line; the continuous pen hook leaves of the live.'],
 [r'categories $M_{\underline{I}}$ .',r'categories $M_{\over[typed]{\illegible{1}}{\underline{I}}}$ .','The interval subscript has an older looped impression beneath the live typed I; its older letter is not secure.'],
 [r'\varinjlim_{\underline{I}}',r'\underset{\underline{I}}{\underset{\hand{\longrightarrow}}{\mathrm{lim}}}','The limit word is typed and its rightward arrow is penned; separate their provenance.'],
 [r'\inserted{may} \xout{xxx}',r'\inserted[typed]{may} \xout{\illegible{1}}','May is typed interlinearly. The three underlying cells are obscured by machine x strikes.']
]
save_review({'key':key,'edits':edits,'diffs':{
 3426:['of the equivalence relations','There is a single the, still live beneath the placing curve of or union.'],
 3427:['having same objects','No the occurs between having and same.'],
 3430:[r"all $\underline{I}$'s\hand{,}",'The comma is a separate handwritten hook after the plural interval expression; its presence is already reflected in the witness punctuation.']
 },'unsure':[
 [r'\unsure{\over[typed]{v}{c}}','The overprinted cell has v-like diagonals and a c-like curve, but the layer order remains insecure.'],
 ['Pen l over typed l','The type foot and upper serif identify the older l; a long slanted pen stem retraces it.'],
 [r'\unsure{a}','The older rounded cell beneath pen o may be a, but its right side remains covered.'],
 [r'\unsure{s}','Only part of the last letter is visible at the cropped right edge.'],
 ['Pen l over typed l','The second occurrence has the same visible typed l and slanted pen retrace.']
 ],'notes':[
 'The sections cell retains explicit doubt about the v/c layers; the scan does not support a clean resolved c.',
 'Both Fl occurrences have a recognizable typed l with a pen retrace, rather than an unknown letter.',
 'The replacement o in décroissant is clear, but the older rounded a-like cell stays doubtful.',
 'The extra t at the end of characteris is machine-cancelled before tic continues on the next line.',
 'The rightmost s of morphisms is partly outside the supplied edge and remains doubtful.',
 'Or union is typed above the line. The hooked placing stroke does not cancel of the.',
 'The lower-left 17 is handwritten. May is typed interlinearly; preordered by and the pre prefix are pen additions. The cancelled ordered and longer phrase are preserved.'
 ],'extra_records':[
 {'source_id':'OBS:ps_134-4_017:underlying','before':'the underlying object of M is just IxJ','after':'Source M retained; the construction describes the underlying object of the interval K.','line':30,'decision':'retain source mathematical slip for guide','reason':'The preceding displayed equation defines K as the product of I and J, but the following typed sentence visibly says M.'}
 ],'evidence':'Both original halves and eleven enlarged detail panels inspected. The sections overprint remains doubtful; both Fl letters are identifiable l with pen retracing. Expect has a pen-retraced x. The old cell under décroissant o remains uncertain, and morphisms is clipped at its final s. Two commas are visible after the J relation, followed by a repeated typed t. Indeed has a displaced repeated n. Or union and may are typed insertions; the former placing hook leaves of the intact. The final category subscript has a live underlined I over an unreadable older looped type impression. The filtering-limit arrow is penned beneath typed lim. The source single the, absence of the before same, and added comma after I\'s were checked against every required difference row. The underlying object of M wording is retained and flagged separately as a source slip.'})
